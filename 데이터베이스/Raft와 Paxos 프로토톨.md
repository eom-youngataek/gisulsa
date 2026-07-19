#### **분산 합의 알고리즘: Raft 프로토콜**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 "Paxos"로는 부족한가) — 3~4줄
Ⅱ. Raft 3대 핵심 메커니즘 (본론①, 도식 1개 필수)
Ⅲ. Paxos와의 비교·Raft 동작 단계별 흐름 (핵심 배점)
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 BASE의 결과적 일관성이 '언젠가 맞춰진다'는 느슨한 수렴이라면, Raft는 '분산 클러스터 안에서 단 하나의 리더가 로그 순서를 독점 결정하고 과반 복제를 확인해야만 커밋'하는 강한 합의(Strong Consensus) 프로토콜이다 — Paxos가 수학적으로 완벽하지만 '이해하기 너무 어렵다'는 실무 한계를 Diego Ongaro가 2014년 '이해 가능하도록 설계된 합의 알고리즘(In Search of an Understandable Consensus Algorithm)'으로 극복한 것이 Raft이며, etcd·Consul·CockroachDB·TiKV가 Raft 위에서 동작"\*\*이라는 한 줄로 시작하면, 왜 이 답안이 앞서 다룬 2PC·BASE·CAP 시리즈 전체의 **강한 합의 구현 수단**인지 드러납니다.

***

#### Ⅱ. Raft 3대 핵심 메커니즘

| 메커니즘                        | 내용                                                                                                                                                                                                                          |
| :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **리더 선출 (Leader Election)** | 클러스터는 항상 **리더(Leader) 1개·팔로워(Follower) N개·후보(Candidate) 0개** 상태 유지. 팔로워가 **Election Timeout(150\~300ms)** 내 리더 하트비트를 수신하지 못하면 Candidate로 전환 → **Term(임기) 번호를 1 증가**시켜 투표 요청(RequestVote) 브로드캐스트 → **과반(N/2+1) 득표** 시 리더로 승격 |
| **로그 복제 (Log Replication)** | 리더만이 클라이언트 요청을 수신해 **로그 엔트리(Log Entry)를 자신의 로그에 추가**. AppendEntries RPC로 **모든 팔로워에게 복제** 요청 → **과반 팔로워가 ACK 응답** 시 해당 엔트리를 **커밋(Commit)** → 상태 머신(State Machine)에 적용 후 클라이언트에 응답. 과반 미달 시 커밋하지 않고 대기                        |
| **안전성 보장 (Safety)**         | **로그 매칭 속성(Log Matching Property)**: 두 노드의 로그에서 동일 인덱스·Term의 엔트리는 **동일한 명령**을 포함하고, 그 이전 모든 엔트리도 동일. **리더 완전성(Leader Completeness)**: 커밋된 엔트리는 **이후 모든 Term의 리더 로그에 반드시 존재** — 투표 시 더 최신 로그를 가진 후보에게만 투표함으로써 보장             |

→ 암기: **"리더 1명이 독점 수신하고, 과반에 복제해야 커밋하고, 새 리더는 반드시 가장 최신 로그를 가진 놈이 된다 — 이 세 규칙이 Raft가 절대 데이터를 잃지 않는 이유"** — 앞서 다룬 \*\*"2PC의 블로킹 문제"\*\*에서 조정자 장애 시 전체가 멈췄다면, Raft는 리더 장애 시 **Election Timeout 안에 새 리더가 자동 선출**되어 서비스가 지속됩니다.

#### 도식화 제안

```
[Raft 클러스터 정상 동작 흐름]

클라이언트
    ↓ 요청(Write x=1)
  리더(Leader, Term=3)
    ├─ 로그에 엔트리 추가: [Term3, x=1]
    ├─ AppendEntries RPC ──→ 팔로워A → ACK ✅
    ├─ AppendEntries RPC ──→ 팔로워B → ACK ✅
    └─ AppendEntries RPC ──→ 팔로워C → (네트워크 지연) ⏳
         ↓
  과반(3/5) ACK 수신 → 커밋 확정
  상태 머신 적용 → 클라이언트 응답 ✅
  (팔로워C는 다음 AppendEntries에서 따라잡기)

[리더 장애 시 선출 흐름]
리더 장애 🚨 → 팔로워들 Election Timeout 초과
    → 팔로워B: Term=4, RequestVote 브로드캐스트
    → 팔로워A·C: 최신 로그 확인 후 투표 ✅
    → 팔로워B: 과반 득표 → 새 리더 승격 ✅
    → 서비스 재개 (전체 소요: 150~300ms)
```

***

#### Ⅲ. Paxos와의 비교·Raft 동작 단계별 흐름 — 핵심 배점

**함정 방지: "Raft는 Paxos보다 이해하기 쉽다"고만 답하면 절반. Term·인덱스 기반 로그 매칭이 실제로 어떻게 분기(Split Brain)를 방지하는지, 네트워크 분단(Partition) 시 Raft가 어떻게 CAP의 CP를 선택하는지를 단계별로 보여줘야 완성됩니다.**

| 단계           | 활동                                                                                                                                             |
| :----------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| **정상 운영**    | 리더가 \*\*HeartBeat(빈 AppendEntries RPC)\*\*를 주기적으로 브로드캐스트 → 팔로워들의 Election Timeout 리셋 → 불필요한 선출 방지. 클라이언트 쓰기는 **리더에게만** 전달 (팔로워 수신 시 리더로 리다이렉트) |
| **로그 충돌 복구** | 새 리더 선출 후 팔로워 로그가 리더와 불일치 시 → **nextIndex를 역방향으로 탐색**해 불일치 시작점 발견 → 리더 로그로 팔로워 로그를 **강제 덮어쓰기(Override)** → 로그 매칭 속성 복원                         |
| **네트워크 분단**  | 앞서 다룬 **"CAP의 CP 선택"** — 분단 발생 시 **과반 노드가 없는 파티션은 리더 선출·커밋 불가** → 서비스 중단(가용성 포기). 과반 파티션만 정상 동작 → **분기(Split Brain) 원천 차단**                    |
| **멤버십 변경**   | 클러스터 노드 추가·제거 시 **Joint Consensus(공동 합의)** 사용. 구성 변경 중 두 개의 과반(Old·New 설정 각각)이 동시에 필요 → 단 하나의 리더만 존재하는 안전성 유지                                  |
| **선출 제한**    | 투표 요청(RequestVote) 수신 시 요청자의 **마지막 로그 Term·인덱스가 자신보다 최신이어야만** 투표 허용 → 커밋된 엔트리를 모르는 후보가 리더가 되는 것을 원천 차단 → 리더 완전성 보장                             |

→ 암기: **"하트비트로 선출을 막고, 과반 ACK로 커밋하고, 분단 시 소수 파티션은 멈추고, 새 리더는 로그가 가장 최신인 놈만 되고, 충돌 로그는 리더가 강제로 덮어쓴다"**

**Split Brain 방지 구조** (중요): 앞서 다룬 \*\*"BASE의 Quorum Write(N개 중 W개)"\*\*가 유연하게 과반을 조절했다면, Raft는 **과반(N/2+1)을 절대 기준**으로 고정해 네트워크 분단 시 두 파티션이 각각 리더를 선출하는 Split Brain을 수학적으로 불가능하게 만든다 — 5노드 클러스터가 3·2로 분단되면 **3노드 파티션만 과반을 충족해 리더 유지**, 2노드 파티션은 **영원히 후보 상태**에 머물며 커밋 불가. 이는 앞서 다룬 \*\*"CAP 정리에서 CP를 선택한 대가로 가용성을 포기"\*\*하는 구조적 결정입니다.

#### 도식화 제안

```
[Paxos vs Raft 전면 비교]

항목              Paxos                    Raft
────────────────────────────────────────────────────
설계 목표         수학적 완전성              이해 가능성·실용성
역할 구분         Proposer·Acceptor·Learner  Leader·Follower·Candidate
리더십            멀티 Proposer 가능         단일 리더 강제
로그 순서         복잡한 Phase1·Phase2       리더 로그가 단일 진실
구현 복잡도       매우 높음 🚨               상대적 낮음 ✅
멤버십 변경       별도 프로토콜 필요          Joint Consensus 내장
대표 구현체       Chubby(Google)             etcd·Consul·TiKV·CockroachDB

[Raft CAP 위치]
       C(일관성) ✅  ← 과반 커밋·로그 매칭으로 강한 일관성
      /
     CP  ← Raft 선택
      \
       P(분단 허용) ✅ ← 과반 파티션만 동작
        A(가용성) ❌  ← 소수 파티션 서비스 중단
```

**앞서 다룬 2PC·BASE·CAP·etcd와의 연결**: 이런 **"Term 기반 리더 선출·AppendEntries 과반 복제·로그 매칭 속성"** 구조가 실제로는 앞서 다룬 \*\*"쿠버네티스(Kubernetes)의 etcd"\*\*가 클러스터 상태(Pod·Service·ConfigMap)를 저장하는 분산 KV 저장소로 Raft를 사용해 단 하나의 진실(Single Source of Truth)을 보장하고, 앞서 다룬 \*\*"CXL 메모리 풀링의 분산 메모리 관리"\*\*에서 노드 간 메모리 상태 합의에 Raft 계열 프로토콜이 활용되는 전 과정을 직접 연결합니다.

***

#### Ⅳ. 결론

Raft 프로토콜은 \*\*"단일 리더가 로그 순서를 독점 결정하고, AppendEntries RPC로 팔로워에 복제해 과반 ACK 확인 후 커밋하며, Election Timeout·Term 번호·로그 최신성 투표 제한으로 Split Brain을 수학적으로 차단하는 강한 합의 알고리즘"\*\*이며, 특히 \*\*"Paxos의 수학적 완전성을 유지하면서 단일 리더·순차 로그·명시적 Term이라는 세 단순화로 이해 가능성과 구현 가능성을 동시에 달성하고, 네트워크 분단 시 CAP의 CP를 선택해 가용성보다 일관성을 우선"\*\*하는 것이 핵심입니다 — 이는 앞서 다룬 \*\*2PC(블로킹 합의) → CAP 정리(한계 증명) → BASE(약한 일관성·AP) → Raft(강한 합의·CP) → etcd·쿠버네티스(실무 적용)\*\*를 하나로 잇는 분산 합의의 실무적 교량이며, \*\*"분산 시스템에서 단 하나의 진실이 필요할 때, 결국 과반이 동의한 리더의 로그만이 진실이며 그것을 구현한 것이 Raft"\*\*라는 결론으로 이어집니다.

### **I. 분산 데이터 동기화의 표준, Raft 프로토콜의 개요**

기존 분산 합의 알고리즘의 표준인 팍소스(Paxos)는 지나치게 난해하여 실제 구현 및 예외 처리에 많은 오버헤드가 존재했습니다. **Raft**는 팍소스와 동등한 성능 및 내결함성을 제공하면서도, 아키텍처를 **리더 선출(Leader Election), 로그 복제(Log Replication), 안전성(Safety)** 3가지 컴포넌트로 완벽히 분할하여 직관성과 구현성을 극대화한 강력한 단일 리더 기반 합의 알고리즘입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3NTguNTk5OTk5OTk5OTk5OSAzNzUuMyIgd2lkdGg9Ijc1OC41OTk5OTk5OTk5OTk5IiBoZWlnaHQ9IjM3NS4zIiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkZvbGxvd2VyIiBkYXRhLXRvPSJDYW5kaWRhdGUiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iu2VmO2KuOu5hO2KuCDtg4DsnoTslYTsm4Mg7IucIiBwb2ludHM9IjU2NS4wMDY4NzQ5OTk5OTk5LDI5OC40MDAwMDAwMDAwMDAwMyA1NjUuMDA2ODc0OTk5OTk5OSwyODYuNDAwMDAwMDAwMDAwMDMgNjU4Ljk2NTk5OTk5OTk5OTksMjg2LjQwMDAwMDAwMDAwMDAzIDY1OC45NjU5OTk5OTk5OTk5LDIxOC4xMDAwMDAwMDAwMDAwMiA1NzQuMTc2NzQ5OTk5OTk5OSwyMTguMTAwMDAwMDAwMDAwMDIgNTc0LjE3Njc0OTk5OTk5OTksNzYuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQ2FuZGlkYXRlIiBkYXRhLXRvPSJMZWFkZXIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuqzvOuwmOyImCDrk53tkZwg7ISx6rO1IiBwb2ludHM9IjQyNS4zNzkyNDk5OTk5OTk5Niw3Ni45IDQyNS4zNzkyNDk5OTk5OTk5Niw4OC45IDIxMi4xMzg5OTk5OTk5OTk5OCw4OC45IDIxMi4xMzg5OTk5OTk5OTk5OCwxNjkuMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTGVhZGVyIiBkYXRhLXRvPSJGb2xsb3dlciIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7J6l7JWgIOuwnOyDnS/sg4HrjIAg64W465OcIOyaqeyWtCDqsLHsi6Ag7IucIiBwb2ludHM9IjIxMi4xMzg5OTk5OTk5OTk5OCwyMDYuMTAwMDAwMDAwMDAwMDIgMjEyLjEzODk5OTk5OTk5OTk4LDI4Ni40MDAwMDAwMDAwMDAwMyA0MjguNDM1ODc1LDI4Ni40MDAwMDAwMDAwMDAwMyA0MjguNDM1ODc1LDI5OC40MDAwMDAwMDAwMDAwMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQ2FuZGlkYXRlIiBkYXRhLXRvPSJGb2xsb3dlciIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7ISg7LacIOyLpO2MqC/tg4Ag66as642UIO2VmO2KuOu5hO2KuCDqsJDsp4AiIHBvaW50cz0iNDk5Ljc3Nzk5OTk5OTk5OTksNzYuOSA0OTkuNzc3OTk5OTk5OTk5OSwyODYuNDAwMDAwMDAwMDAwMDMgNDk2LjcyMTM3NDk5OTk5OTk3LDI4Ni40MDAwMDAwMDAwMDAwMyA0OTYuNzIxMzc0OTk5OTk5OTcsMjk4LjQwMDAwMDAwMDAwMDAzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkZvbGxvd2VyIiBkYXRhLXRvPSJDYW5kaWRhdGUiIGRhdGEtbGFiZWw9Iu2VmO2KuOu5hO2KuCDtg4DsnoTslYTsm4Mg7IucIj4KICA8cmVjdCB4PSI1OTQuNDY1OTk5OTk5OTk5OSIgeT0iMjI1LjEwMDAwMDAwMDAwMDAyIiB3aWR0aD0iMTI4LjEzNDAwMDAwMDAwMDAxIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjU4LjUzMjk5OTk5OTk5OTkiIHk9IjI0MC4yNTAwMDAwMDAwMDAwMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7ZWY7Yq467mE7Yq4IO2DgOyehOyVhOybgyDsi5w8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQ2FuZGlkYXRlIiBkYXRhLXRvPSJMZWFkZXIiIGRhdGEtbGFiZWw9IuqzvOuwmOyImCDrk53tkZwg7ISx6rO1Ij4KICA8cmVjdCB4PSIxNTkuNjM5IiB5PSI5NS45IiB3aWR0aD0iMTA0LjM3NDAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjExLjgyNjAwMDAwMDAwMDAyIiB5PSIxMTEuMDUwMDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuqzvOuwmOyImCDrk53tkZwg7ISx6rO1PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkxlYWRlciIgZGF0YS10bz0iRm9sbG93ZXIiIGRhdGEtbGFiZWw9IuyepeyVoCDrsJzsg50v7IOB64yAIOuFuOuTnCDsmqnslrQg6rCx7IugIOyLnCI+CiAgPHJlY3QgeD0iMTIwLjEzOSIgeT0iMjQ5LjEiIHdpZHRoPSIxODMuOTcwMDAwMDAwMDAwMDYiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyMTIuMTI0MDAwMDAwMDAwMDIiIHk9IjI2NC4yNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7J6l7JWgIOuwnOyDnS/sg4HrjIAg64W465OcIOyaqeyWtCDqsLHsi6Ag7IucPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkNhbmRpZGF0ZSIgZGF0YS10bz0iRm9sbG93ZXIiIGRhdGEtbGFiZWw9IuyEoOy2nCDsi6TtjKgv7YOAIOumrOuNlCDtlZjtirjruYTtirgg6rCQ7KeAIj4KICA8cmVjdCB4PSI0MDguMjc3OTk5OTk5OTk5OSIgeT0iMjI1LjEwMDAwMDAwMDAwMDAyIiB3aWR0aD0iMTgyLjE4ODAwMDAwMDAwMDA1IiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNDk5LjM3MTk5OTk5OTk5OTk2IiB5PSIyNDAuMjUwMDAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuyEoOy2nCDsi6TtjKgv7YOAIOumrOuNlCDtlZjtirjruYTtirgg6rCQ7KeAPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJGb2xsb3dlciIgZGF0YS1sYWJlbD0iRm9sbG93ZXIgOiDrjIDquLAg67CPIOumrOuNlCDsi6zsnqXrsJXrj5kg6rCQ7IucIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM2MC4xNTAzNzQ5OTk5OTk5NCIgeT0iMjk4LjQwMDAwMDAwMDAwMDAzIiB3aWR0aD0iMjczLjE0MiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDk2LjcyMTM3NDk5OTk5OTk3IiB5PSIzMTYuODUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkZvbGxvd2VyIDog64yA6riwIOuwjyDrpqzrjZQg7Ius7J6l67CV64+ZIOqwkOyLnDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ2FuZGlkYXRlIiBkYXRhLWxhYmVsPSJDYW5kaWRhdGUgOiDtiKztkZwg7JqU7LKtIOuwjyDqs7zrsJjsiJgg65Od7ZGcIOyLnOuPhCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzNTAuOTgwNDk5OTk5OTk5OSIgeT0iNDAiIHdpZHRoPSIyOTcuNTk1IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDk5Ljc3Nzk5OTk5OTk5OTkiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5DYW5kaWRhdGUgOiDtiKztkZwg7JqU7LKtIOuwjyDqs7zrsJjsiJgg65Od7ZGcIOyLnOuPhDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTGVhZGVyIiBkYXRhLWxhYmVsPSJMZWFkZXIgOiDrqqjrk6Ag7JOw6riwIO2KuOuenOyereyFmCDrsI8g66Gc6re4IOuPmeq4sO2ZlCDso7zrj4QiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDAiIHk9IjE2OS4yIiB3aWR0aD0iMzQ0LjI3Nzk5OTk5OTk5OTk2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjIxMi4xMzg5OTk5OTk5OTk5OCIgeT0iMTg3LjY0OTk5OTk5OTk5OTk4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5MZWFkZXIgOiDrqqjrk6Ag7JOw6riwIO2KuOuenOyereyFmCDrsI8g66Gc6re4IOuPmeq4sO2ZlCDso7zrj4Q8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

***

### **II. Raft 프로토콜의 3대 동작 메커니즘**

#### **1. 리더 선출 (Leader Election)**

* **Term (임기)**: 논리적 시간 단위인 Term을 사용하여 구세대 리더와 신세대 리더를 구분합니다.
* **임의 투표 타임아웃 (Randomized Election Timeout)**: 팔로워가 후보자로 전환되는 대기 시간을 노드마다 무작위(예: 150\~300ms)로 다르게 주어, 표가 갈려 리더가 선출되지 않는 분할 투표(Split Vote)를 방지합니다.

#### **2. 로그 복제 (Log Replication)**

* 리더는 클라이언트의 쓰기 요청을 받아 로컬 로그에 우선 기록하고, 팔로워에게 복제 요청(`RequestVote` 및 `AppendEntries` RPC)을 보냅니다.
* 전체 노드의 과반수(⌊N/2⌋+1⌊*N*/2⌋+1)가 동기화 완료 신호를 보내면 리더는 해당 쓰기 요청을 **Commit(커밋)** 처리하고 최종 응답합니다.

#### **3. 안전성 (Safety)**

* **리더 완전성 (Leader Completeness)**: 반드시 최신 커밋 로그를 모두 보유한 노드만 새 리더로 선출될 수 있게 제한함으로써 데이터 누실을 원천 차단합니다.

***

### **III. 고전 팍소스(Paxos) 프로토콜과 현대 라프트(Raft) 프로토콜의 비교**

| **비교 항목**      | **🏛️ 팍소스 (Paxos) 프로토콜**              | **⛵ 라프트 (Raft) 프로토콜**                              |
| :------------- | :------------------------------------ | :------------------------------------------------- |
| **디자인 핵심 철학**  | 수리적 정합성 및 엄밀한 논리 증명 지향                | **이해 가능성(Understandability) 및 구현 직관성 지향**          |
| **리더 아키텍처**    | 대칭 구조 (Proposer 간 임시 리더 지정, 리더 부재 허용) | **비대칭 구조 (강력한 단일 리더 기반 통제)**                       |
| **알고리즘 구성**    | Single-Paxos와 Multi-Paxos의 복잡한 조합     | **선출, 복제, 안전성의 3가지 독립 서브 컴포넌트 구성**                 |
| **실제 오픈소스 적용** | 직접 구현이 어려워 Chubby 등 한정적 적용            | **etcd(Kubernetes), Consul, CockroachDB 등 광범위 적용** |

***

### **IV. Raft 적용 분산 환경의 스플릿 브레인(Split-Brain) 방어 전략**

**IMPORTANT**

1. **과반수 쿼럼(Majority Quorum) 합의**: 네트워크 파티션 발생으로 클러스터가 2개로 쪼개질 때(예: 5개 노드가 2개와 3개로 분할), 과반수를 확보하지 못한 2개 쪽 파티션은 리더 선출 및 커밋 처리가 불가하도록 차단하여 데이터 불일치(Split-Brain)를 방어합니다.
2. **조인트 컨센서스(Joint Consensus)를 통한 설정 변경**: 노드를 추가/제거하여 클러스터 구조가 변경될 때, 구설정 정족수와 신설정 정족수가 일시적으로 겹치지 않도록 이단계 설정 변경(Joint Consensus) 프로토콜을 가동하여 일시적 이중 리더 생성을 원천 무효화해야 합니다.
