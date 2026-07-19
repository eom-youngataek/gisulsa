#### 답안 전개 스토리 (핵심 압축)

> "분산 시스템에서 '여러 노드가 단 하나의 진실에 동의하게 만드는 것'이 합의 알고리즘의 본질이다. **Raft**는 Paxos가 수학적으로 완벽하지만 '이해하기 너무 어렵다'는 실무 한계를 Diego Ongaro가 2014년 **'이해 가능하도록 설계'**하는 원칙 하나로 극복한 합의 알고리즘이다. 핵심은 세 메커니즘으로 완결된다. **①리더 선출(Leader Election)**: 클러스터는 항상 단 하나의 리더만 존재하며 팔로워가 Election Timeout(150~300ms) 안에 하트비트를 못 받으면 Term을 올려 투표를 요청하고 과반을 얻으면 새 리더가 된다. **②로그 복제(Log Replication)**: 리더만이 클라이언트 요청을 받아 로그 엔트리를 생성하고 AppendEntries RPC로 팔로워에 복제한 뒤 과반 ACK가 오면 커밋한다 — '과반이 동의해야 진실이 된다'는 단순한 규칙이 분기(Split Brain)를 수학적으로 불가능하게 만든다. **③안전성(Safety)**: 로그 매칭 속성과 리더 완전성으로 '한번 커밋된 엔트리는 영원히 모든 리더의 로그에 존재'함을 보장하며 투표 시 더 최신 로그를 가진 후보만 리더가 될 수 있어 커밋 데이터는 절대 유실되지 않는다."

---

#### 핵심 내용 (암기용)

**전제 개념**

|개념|내용|
|---|---|
|**Term(임기)**|단조 증가하는 논리 시간 / 리더 교체마다 +1 / 구 리더 탐지 수단|
|**과반(Quorum)**|N/2+1 노드 / 커밋·선출 모두 과반 필수 / Split Brain 방지 원리|
|**AppendEntries RPC**|리더→팔로워 로그 복제·하트비트 겸용 / 빈 내용=하트비트|
|**RequestVote RPC**|후보→전체 투표 요청 / 최신 로그 보유 후보에게만 투표|
|**Election Timeout**|150~300ms 무작위 / 동시 선출 충돌 방지|

---

|**핵심 척도**|**📊 리더 선출 (Leader Election) 🚨**|**🔑 로그 복제 (Log Replication) 🚨**|**🏁 안전성 (Safety) 💯**|
|---|---|---|---|
|**핵심 규칙**|**단일 리더 보장** / Election Timeout 초과 → Candidate 전환 → Term+1 → RequestVote 브로드캐스트 → 과반 득표 → Leader 승격|**리더 독점 수신** / 클라이언트 요청→리더 로그 추가→AppendEntries 복제→과반 ACK→커밋→상태 머신 적용→클라이언트 응답|**로그 매칭 속성**: 동일 인덱스·Term 엔트리는 동일 내용·이전 엔트리도 동일 / **리더 완전성**: 커밋 엔트리는 이후 모든 Term 리더 로그에 반드시 존재|
|**핵심 제약 🚨**|**투표 제한**: 요청자 로그가 자신보다 최신이어야만 투표 / (Term 비교→같으면 인덱스 비교) / 구 Term 리더의 메시지는 즉시 무시|**로그 충돌 복구**: 새 리더→팔로워 불일치 탐지→nextIndex 역방향 탐색→리더 로그로 강제 덮어쓰기→로그 매칭 복원|**네트워크 분단 시 CP 선택**: 과반 없는 파티션은 리더 선출·커밋 불가 → 가용성 포기·일관성 유지 / Split Brain 수학적 불가|
|**타이밍 💯**|**3단계 타이밍**: broadcastTime(0.5~20ms) ≪ Election Timeout(150~300ms) ≪ MTBF(수개월) / 이 계층 관계가 유지될 때 Raft 정상 동작 보장|**하트비트 주기**: broadcastTime 이내 주기적 전송 / 팔로워 Election Timeout 리셋 / 불필요한 선출 방지|**장애 복구 속도**: 리더 장애→최대 Election Timeout(300ms) 내 새 리더 자동 선출·서비스 재개 / 앞서 다룬 **2PC 블로킹** 한계 극복|

---

#### 도식화

```
[Raft 정상 동작 흐름]

클라이언트: x=5 쓰기 요청
       ↓
리더(Term=3, 노드1)
  로그 추가: [Term3, Index5, x=5]
  AppendEntries RPC 브로드캐스트
       ↓
팔로워2: ACK ✅   팔로워3: ACK ✅   팔로워4: (지연)
       ↓
과반(3/5) ACK → 커밋 확정
상태 머신 적용: x=5
클라이언트 응답 ✅
(팔로워4는 다음 AppendEntries에서 따라잡기)

[리더 장애·선출 흐름]

리더(노드1) 장애 🚨
       ↓
팔로워2·3·4·5: Election Timeout 초과
       ↓
가장 먼저 만료된 노드2: Term=4, RequestVote 브로드캐스트
  "나의 마지막 로그: Term=3, Index=5"
       ↓
노드3: 로그 확인(Term=3, Index=5 ≥ 자신) → 투표 ✅
노드4: 로그 확인 → 투표 ✅
       ↓
노드2: 과반(3/5) 득표 → 새 리더 ✅
       ↓
HeartBeat 즉시 전송 → 서비스 재개 (최대 300ms)

[네트워크 분단 시 Raft CP 선택]

분단 전: 노드1(리더)·2·3·4·5

분단 발생:
  파티션A: 노드1·2     (과반 미달·2/5)
  파티션B: 노드3·4·5   (과반 충족·3/5)

파티션A: 리더 선출 불가·커밋 불가 ❌
파티션B: 새 리더 선출·정상 서비스 ✅

→ 단 하나의 파티션만 동작
→ Split Brain 수학적 불가 ✅
→ 앞서 다룬 CAP의 CP 선택 구조적 구현
```

---

**(제언)** "Raft는 단일 리더·순차 로그·명시적 Term이라는 세 단순화로 Paxos의 수학적 완전성을 유지하면서 이해 가능성과 구현 가능성을 동시에 달성했습니다. **앞서 다룬 etcd(쿠버네티스 상태 저장)·CockroachDB·TiKV가 모두 Raft 위에서 동작하며, 분산 고속 스토리지 패브릭의 Ceph MON 클러스터·분산 메타데이터 일관성도 Raft 계열 합의로 보장됩니다. 실무 설계 시 Election Timeout(150~300ms)·broadcastTime·MTBF의 3단계 타이밍 계층 관계를 네트워크 환경에 맞게 조정하는 것이 Raft 클러스터 안정성의 핵심 튜닝 포인트입니다.**"


#### **1. 답안 전개 스토리 (핵심 압축)**

> "분산 데이터베이스 클러스터의 여러 노드들이 \*\*'누가 전체 대장(Leader)인지' 합의하고, 쓰기 로그를 전원에 오차 없이 똑같이 복제하도록 제어하는 '분산 합의 알고리즘'\*\*이다. 난해하기로 소문난 기존 'Paxos' 알고리즘을 인간이 이해하기 쉽게 직관적인 상태 전이 구조로 재설계했다. 역할은 3가지다. 대장인 **'Leader'**, 부하인 **'Follower'**, 대장이 죽었을 때 투표 출마를 선언하는 \*\*'Candidate'\*\*다. 동작은 2단계다. 1단계 **\[Leader Election (리더 선출) 🚨]**: 대장이 하트비트(Heartbeat)를 안 보내면, 시간 초과한 Follower가 Candidate로 변신해 투표를 요청하고, 과반수(Quorum) 찬성 표를 얻어 대장이 된다. 2단계 **\[Log Replication (로그 복제)]**: 대장이 모든 쓰기 명령을 받아 Follower들에게 뿌리고, 과반수가 잘 적었다고 응답(Commit)하면 전원에게 영구 저장을 승인한다. 분산 노드 간의 데이터 동기화와 이중화 충돌을 방어하는 핵심 뇌다."

#### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NDAuNDI5MDAwMDAwMDAwMSA1MTEuOSIgd2lkdGg9IjY0MC40MjkwMDAwMDAwMDAxIiBoZWlnaHQ9IjUxMS45IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJSYWZ0X19fX19fIiBkYXRhLWxhYmVsPSJSYWZ0IO2VqeydmCDslYzqs6Drpqzsppgg64W465OcIOyDge2DnCDsoITsnbTsmYAg64+Z7J6RIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI1NjAuNDI5MDAwMDAwMDAwMSIgaGVpZ2h0PSI0MzEuOSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjU2MC40MjkwMDAwMDAwMDAxIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+UmFmdCDtlansnZgg7JWM6rOg66as7KaYIOuFuOuTnCDsg4Htg5wg7KCE7J207JmAIOuPmeyekTwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRiIgZGF0YS10bz0iQyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7ZWY7Yq467mE7Yq4IO2DgOyehOyVhOybgyDrsJzsg50iIHBvaW50cz0iNDA5Ljk3MTUwMDAwMDAwMDA1LDQxOSA0MDkuOTcxNTAwMDAwMDAwMDUsMzgzIDUxOC45MTUwMDAwMDAwMDAxLDM4MyA1MTguOTE1MDAwMDAwMDAwMSwxMzIuOSA0MTEuODI0MDAwMDAwMDAwMDcsMTMyLjkgNDExLjgyNDAwMDAwMDAwMDA3LDEyMC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDIiBkYXRhLXRvPSJMIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIxLiDrpqzrjZQg7ISg7LacIEVsZWN0aW9uIPCfmqggCuqzvOuwmOyImCBRdW9ydW0g7LCs7ISxIO2IrO2RnCDtmo3rk50iIHBvaW50cz0iMzI5LjM0NiwxMjAuOSAzMjkuMzQ2LDEzMi45IDE2NC4wNDI1MDAwMDAwMDAwMiwxMzIuOSAxNjQuMDQyNTAwMDAwMDAwMDIsMjUxLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkMiIGRhdGEtdG89IkYiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iu2IrO2RnCDsi6TtjKggLyDtg4Ag7J6E7LCo7J24IOuLueyEoCIgcG9pbnRzPSIzNzAuNTg1MDAwMDAwMDAwMDQsMTIwLjkgMzcwLjU4NTAwMDAwMDAwMDA0LDQxOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTCIgZGF0YS10bz0iRiIgZGF0YS1zdHlsZT0idGhpY2siIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iMi4g66Gc6re4IOuzteygnCBSZXBsaWNhdGlvbiDwn5KvIArrqqjrk6Ag7YG065287J207Ja47Yq4IOyTsOq4sCDthrXsoJwg67CPIOuPmeq4sO2ZlCIgcG9pbnRzPSIxNjQuMDQyNTAwMDAwMDAwMDIsMjg4LjQgMTY0LjA0MjUwMDAwMDAwMDAyLDM4MyAzMzEuMTk4NSwzODMgMzMxLjE5ODUsNDE5IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIyIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkYiIGRhdGEtdG89IkMiIGRhdGEtbGFiZWw9Iu2VmO2KuOu5hO2KuCDtg4DsnoTslYTsm4Mg67Cc7IOdIj4KICA8cmVjdCB4PSI0NDguNDE1IiB5PSIyNTQuODAwMDAwMDAwMDAwMDQiIHdpZHRoPSIxNDAuMDE0IiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTE4LjQyMiIgeT0iMjY5Ljk1MDAwMDAwMDAwMDA1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7tlZjtirjruYTtirgg7YOA7J6E7JWE7JuDIOuwnOyDnTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJDIiBkYXRhLXRvPSJMIiBkYXRhLWxhYmVsPSIxLiDrpqzrjZQg7ISg7LacIEVsZWN0aW9uIPCfmqggCuqzvOuwmOyImCBRdW9ydW0g7LCs7ISxIO2IrO2RnCDtmo3rk50iPgogIDxyZWN0IHg9Ijc5LjU0MjUiIHk9IjE2My45IiB3aWR0aD0iMTY4LjUyNjAwMDAwMDAwMDA0IiBoZWlnaHQ9IjQ0LjYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTYzLjgwNTUwMDAwMDAwMDAyIiB5PSIxODYuMjAwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSIxNjMuODA1NTAwMDAwMDAwMDIiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij4xLiDrpqzrjZQg7ISg7LacIEVsZWN0aW9uIPCfmqggPC90c3Bhbj48dHNwYW4geD0iMTYzLjgwNTUwMDAwMDAwMDAyIiBkeT0iMTQuMyI+6rO867CY7IiYIFF1b3J1bSDssKzshLEg7Yis7ZGcIO2ajeuTnTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkMiIGRhdGEtdG89IkYiIGRhdGEtbGFiZWw9Iu2IrO2RnCDsi6TtjKggLyDtg4Ag7J6E7LCo7J24IOuLueyEoCI+CiAgPHJlY3QgeD0iMjk2LjA4NTAwMDAwMDAwMDA0IiB5PSIyNTQuODAwMDAwMDAwMDAwMDQiIHdpZHRoPSIxNDguMzMwMDAwMDAwMDAwMDQiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzNzAuMjUwMDAwMDAwMDAwMDYiIHk9IjI2OS45NTAwMDAwMDAwMDAwNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7Yis7ZGcIOyLpO2MqCAvIO2DgCDsnoTssKjsnbgg64u57ISgPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkwiIGRhdGEtdG89IkYiIGRhdGEtbGFiZWw9IjIuIOuhnOq3uCDrs7XsoJwgUmVwbGljYXRpb24g8J+SryAK66qo65OgIO2BtOudvOydtOyWuO2KuCDsk7DquLAg7Ya17KCcIOuwjyDrj5nquLDtmZQiPgogIDxyZWN0IHg9IjYxLjU0MjUwMDAwMDAwMDAyIiB5PSIzMzEuNCIgd2lkdGg9IjIwNC43NjAwMDAwMDAwMDAwNSIgaGVpZ2h0PSI0NC42IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjE2My45MjI1MDAwMDAwMDAwNCIgeT0iMzUzLjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSIxNjMuOTIyNTAwMDAwMDAwMDQiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij4yLiDroZzqt7gg67O17KCcIFJlcGxpY2F0aW9uIPCfkq8gPC90c3Bhbj48dHNwYW4geD0iMTYzLjkyMjUwMDAwMDAwMDA0IiBkeT0iMTQuMyI+66qo65OgIO2BtOudvOydtOyWuO2KuCDsk7DquLAg7Ya17KCcIOuwjyDrj5nquLDtmZQ8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRiIgZGF0YS1sYWJlbD0i67aA7ZWYIEZvbGxvd2VyIOuFuOuTnCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyOTEuODEyIiB5PSI0MTkiIHdpZHRoPSIxNTcuNTQ2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzcwLjU4NTAwMDAwMDAwMDA0IiB5PSI0MzcuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuu2gO2VmCBGb2xsb3dlciDrhbjrk5w8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkMiIGRhdGEtbGFiZWw9Iuy2nOuniCBDYW5kaWRhdGUg64W465OcIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjI4OC4xMDciIHk9Ijg0IiB3aWR0aD0iMTY0Ljk1NjAwMDAwMDAwMDAyIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzNzAuNTg1MDAwMDAwMDAwMDQiIHk9IjEwMi40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7Lac66eIIENhbmRpZGF0ZSDrhbjrk5w8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkwiIGRhdGEtbGFiZWw9IuKcqCDrjIDsnqUgTGVhZGVyIOuFuOuTnCDrk7Hqt7kg4pyoIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIyNTEuNSIgd2lkdGg9IjIxNi4wODUiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTY0LjA0MjUwMDAwMDAwMDAyIiB5PSIyNjkuOTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuKcqCDrjIDsnqUgTGVhZGVyIOuFuOuTnCDrk7Hqt7kg4pyoPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

| **핵심 척도**      | **📊 Paxos (전통 합의 표준)**                                | **🔑 Raft (현대 합의 표준) 🚨**                                            | **🏁 분산 합의 3대 상태 전이 💯**                                                                     |
| :------------- | :----------------------------------------------------- | :------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| **구현 편의성**     | 수학적 증명 중심 설계. 예외 케이스 제어가 극도로 복잡해 실제 코딩 구현 및 디버깅 지옥 유발. | **이해 및 구현 용이성 중심 💯.** 리더 선출, 로그 복제, 안전성 3가지 모듈로 분할 설계되어 신뢰성 최우수.    | 노드들이 실시간 하트비트 신호 상태에 따라 변경해 나가는 역할 모델.                                                       |
| **동작 메커니즘 🚨** | 다수의 제안자(Proposer)와 수락자(Acceptor) 간의 다단계 합의 투표 프로세스.    | **\[리더 중심 단일 통제 🚨]** 일단 강력한 리더 한 명을 뽑고, 모든 권한을 리더에게 몰아주어 합의 연산 간소화. | **1. Follower**: 수동적 상태. **2. Candidate 🚨**: 투표 모집 출마 상태. **3. Leader 💯**: 클라이언트 통신 독점 상태. |

* **(제언)** "Raft는 분산 코디네이터인 ZooKeeper를 대체하는 카프카(KRaft) 및 etcd의 코어 엔진입니다. **클러스터 설계 시 네트워크 단절로 인한 잦은 재선거(Election) 루프를 막으려면, 노드 개수를 무조건 홀수(3, 5, 7)로 구성하여 투표 동률 교착상태를 원천 예방해야 합니다.**"
