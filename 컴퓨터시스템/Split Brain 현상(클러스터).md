### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (Split Brain 정의, 발생배경) — 3~4줄
Ⅱ. 발생과정 (본론①, 도식 1개 필수)
Ⅲ. 발생시 문제점 (본론②, 핵심 배점)
Ⅳ. 방지기법 - 쿼럼과 펜싱 (본론③)
Ⅴ. 결론
```

포인트: 개요에서 \*\*"클러스터(여러 서버묶음)에서는 '지금 살아있는 리더(Active노드)가 누구인지'에 대한 합의가 반드시 필요하다 → 그런데 서버들간 통신하는 네트워크 자체가 끊기면(파티션), 양쪽 그룹이 서로를 '죽었다'고 오판해서 각자 리더를 새로 뽑아버리는 현상"\*\*이라는 한 줄로 시작하면, 왜 "두개의 뇌(Split Brain)"라는 이름이 붙었는지 바로 이해됩니다.

### Ⅱ. 발생과정 — "정·단·오·중" (정상운영→네트워크단절→오판→중복리더)

| 단계                     | 내용                                                         |
| :--------------------- | :--------------------------------------------------------- |
| **정상운영**               | 클러스터에 \*\*하나의 리더(Active)\*\*와 나머지 대기노드(Standby)들이 정상적으로 통신 |
| **네트워크단절** (Partition) | 클러스터 내부 통신선(하트비트)이 **끊김** — 물리적 회선문제, 스위치장애 등              |
| **오판**                 | 단절된 각 그룹이 **상대편이 죽었다고 착각**(사실은 살아있는데 통신만 끊긴 것)             |
| **중복리더**               | 양쪽 그룹이 **각자 독립적으로 새 리더를 선출** → 클러스터에 **리더가 2개** 존재하는 상태 발생 |

→ 암기: **"통신이 끊기면 상대가 죽었다고 오해하고, 각자 왕을 새로 뽑아서 나라가 두개로 갈라진다"** — 앞서 다룬 "MESI(캐시일관성)"에서 여러 코어가 "누가 최신값을 가졌는지" 합의해야 했던 문제가, 여기서는 "누가 진짜 리더인지"로 스케일이 커진 것입니다.

### 도식화 제안

```
[정상상태]
[리더A]═══하트비트═══[대기B]═══[대기C]
(A가 유일한 리더로 정상운영)

         ↓ 네트워크 파티션 발생(회선단절)

[그룹1: 리더A]    ╳(단절)    [그룹2: 대기B, 대기C]
                              ↓ B,C는 A가 죽었다고 오판
                           [그룹2: 새리더B 선출]

결과: 리더A(원래)와 리더B(새로선출)가 동시존재
     = SPLIT BRAIN (두개의 뇌)
```

### Ⅲ. 발생시 문제점 — 핵심 배점

**함정 방지: "리더가 2개면 헷갈리겠다"정도로 뭉뚱그리면 절반. 실제로 어떤 구체적 피해가 생기는지 보여줘야 완성됩니다.**

| 문제                              | 내용                                                                                           |
| :------------------------------ | :------------------------------------------------------------------------------------------- |
| **데이터불일치** (Data Inconsistency) | 양쪽 리더가 **각자 독립적으로 쓰기(write)작업을 수락** → 같은 데이터에 대해 **서로 다른값으로 갈라짐**(앞서 다룬 Race Condition의 분산판) |
| **데이터손실**                       | 네트워크 복구후 두 리더를 다시 하나로 합칠 때(병합), **한쪽의 변경사항을 버려야** 하는 경우 발생                                   |
| **서비스오작동**                      | 클라이언트가 **어느 리더에게 요청했는지에 따라 다른 결과**를 받는 등 일관성붕괴                                               |

→ 암기: **"따로따로 결정하다가 나중에 합치려니 누구말을 들어야할지 몰라서 데이터가 깨진다"** — 앞서 다룬 "우선순위역전"이 실시간시스템의 재앙이었듯, Split Brain은 **분산시스템의 재앙**입니다.

### Ⅳ. 방지기법 — 쿼럼과 펜싱, 핵심 해법

**함정 방지: "네트워크를 안 끊기게 하면 된다"는 근본적으로 불가능한 전제입니다(CAP이론). "끊겨도 괜찮게 설계"하는 게 진짜 해법입니다.**

| 기법                      | 원리                                                                                                           |
| :---------------------- | :----------------------------------------------------------------------------------------------------------- |
| **쿼럼(Quorum)**          | 리더선출에 **"과반수(majority)"의 동의**를 요구 — 클러스터가 절반으로 쪼개지면, **한쪽은 반드시 과반수미달**이라 새 리더를 못 뽑음                          |
| **펜싱(Fencing/STONITH)** | 기존리더가 응답이 없으면, **강제로 그 노드를 완전히 차단(전원차단 등, "Shoot The Other Node In The Head")** — 좀비상태로 계속 쓰기작업을 하지 못하게 원천봉쇄 |
| **분산합의 알고리즘**           | Raft, Paxos 등 — **다수결 기반으로 유일한 리더만 인정**하는 프로토콜을 시스템 근본에 내장                                                   |

→ 암기: **"과반수를 못얻으면 아예 리더가 될 수 없게 하고(쿼럼), 옛리더는 확실히 죽여서 좀비가 못되게 한다(펜싱)"** — 앞서 다룬 "은행가알고리즘"이 "자원을 주기 전에 안전한지 미리 검증"했던 것처럼, 쿼럼도 \*\*"리더가 되기 전에 반드시 과반수 검증을 통과해야 한다"\*\*는 사전검증원리입니다.

**쿼럼의 핵심 수학**: 노드가 **3개**면 쿼럼은 **2개(과반수)** — 클러스터가 1:2로 쪼개지면, 2개그룹만 과반수를 얻어 리더선출 가능, 1개그룹은 절대 리더를 못 뽑음(구조적으로 Split Brain 자체가 불가능해짐). 그래서 클러스터노드는 흔히 \*\*홀수개(3,5,7...)\*\*로 구성합니다.

### 도식화 제안

```
[3노드 클러스터, 쿼럼=2]
파티션 발생: [노드1] ╳ [노드2,노드3]
             1개(과반수미달)   2개(과반수충족)
                ↓                  ↓
          리더선출 불가!      리더선출 가능(정상)
          
→ 한쪽만 "확실한 리더"를 가질 수 있어 Split Brain 원천방지
```

### Ⅴ. 결론 포인트 (오늘 동시성/분산시스템 시리즈 최종연결)

Split Brain은 오늘 다룬 **데드락(자원경쟁의 함정)**, **세마포어/뮤텍스(공유자원 통제)**, **MESI(누가 최신값을 가졌는지 합의)** 문제가 **단일머신을 넘어 여러 서버로 분산될 때 필연적으로 마주치는 최종형태**입니다 — 네트워크는 언제든 끊길 수 있다(CAP이론의 P, Partition tolerance는 선택이 아니라 전제)는 현실을 받아들이고, **"끊겼을 때 누가 진실을 말할 자격이 있는지"를 과반수(쿼럼)라는 수학적 기준으로 미리 못박아두는 것**이 유일한 해법입니다 — 이는 오늘 하루 다룬 모든 동시성·분산시스템 답안들이 공통적으로 도달한 결론: \*\*"완벽한 예방은 불가능하니, 문제가 생겼을 때 누가 옳은지 판단할 규칙을 미리 정해두라"\*\*는 설계철학의 가장 극명한 사례입니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "HA(고가용성) 클러스터는 평소에 'A 서버(Active 마스터)'가 일하고 'B 서버(Standby 대기)'가 대기하는 구조다. 이 둘은 1초마다 '나 잘 살아있다'라는 심장 박동(Heartbeat) 신호를 네트워크 랜선으로 주고받는다. 그런데 어느 날, 두 서버는 멀쩡한데 이 둘을 잇는 '하트비트용 랜선'만 쥐가 파먹어서 툭 끊어졌다고 가정해 보자. 대기하던 B 서버 입장에서는 A의 심장 박동이 끊겼으니 '아, A가 죽었구나! 이제 내가 대장(Active)이다!' 하고 시스템을 장악하며 깨어난다. 하지만 A도 여전히 멀쩡히 살아있는 대장(Active) 상태다. 이처럼 하나의 클러스터 안에 두 명의 대장이 나타나 통제권이 두 갈래로 쪼개져 버리는 치명적인 장애를 \*\*'스플릿 브레인(Split Brain)'\*\*이라고 부른다. 이 상태에서 두 명의 대장이 똑같은 공유 스토리지(데이터베이스)에 동시에 데이터를 써버리면(Write), 데이터가 완전히 꼬이고 박살나서(Data Corruption) 회사가 망한다. 이를 막으려면 가장 과격하지만 확실한 'STONITH(상대방 머리에 총 쏘기)' 기법을 써서 통신이 끊기는 즉시 상대방의 물리적 전원 코드를 뽑아버려 확실히 죽이거나, 노드를 홀수로 구성해 과반수 다수결(Quorum) 투표로 진짜 대장만 살려두는 **'펜싱(Fencing)' 차단 기술**을 반드시 적용해야 한다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 뇌가 두 개로 쪼개지는 재앙, 스플릿 브레인(Split Brain) 개요**

* **정의:** 고가용성(HA, High Availability) 클러스터 시스템에서 노드 간의 상태를 체크하는 **네트워크(하트비트)가 단절되었을 때, 실제로는 노드가 살아있음에도 불구하고 서로 죽었다고 오판하여 여러 노드가 동시에 자신을 Active(마스터) 상태로 승격시키는 치명적인 장애 현상**.
* **발생 결과:** 동일한 클러스터 내에 2개의 뇌(Active 노드)가 존재하게 되어, **공유 스토리지(DB 등)에 대한 동시 쓰기(Write) 충돌이 발생하고, 결국 복구 불가능한 치명적 '데이터 붕괴(Data Corruption)'를 초래**함.

#### **II. \[본론 1] 하트비트 단절이 부른 비극: 스플릿 브레인 발생 메커니즘 (도식화)**

어떻게 Active-Active 충돌이 일어나는지 직관적으로 보여줍니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MzguNjc0IDUxNC4yIiB3aWR0aD0iNjM4LjY3NCIgaGVpZ2h0PSI1MTQuMiIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMV9fX0FjdGl2ZV9fU3RhbmRieSIgZGF0YS1sYWJlbD0iMS4g7KCV7IOBIOyDge2DnCAoQWN0aXZlIC0gU3RhbmRieSkiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjE4NS4xIiBoZWlnaHQ9IjI2NC4xIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMTg1LjEiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij4xLiDsoJXsg4Eg7IOB7YOcIChBY3RpdmUgLSBTdGFuZGJ5KTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IjJfX1NwbGl0X0JyYWluX19BY3RpdmVfX0FjdGl2ZV8iIGRhdGEtbGFiZWw9IjIuIPCfmqggU3BsaXQgQnJhaW4g67Cc7IOdISAoQWN0aXZlIC0gQWN0aXZlIOy2qeuPjCkiPgogIDxyZWN0IHg9IjI1My4xMDAwMDAwMDAwMDAwMiIgeT0iNDAiIHdpZHRoPSIzMzguMTc4IiBoZWlnaHQ9IjQzNC4yMDAwMDAwMDAwMDAwNSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjI1My4xMDAwMDAwMDAwMDAwMiIgeT0iNDAiIHdpZHRoPSIzMzguMTc4IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyNjUuMSIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+Mi4g8J+aqCBTcGxpdCBCcmFpbiDrsJzsg50hIChBY3RpdmUgLSBBY3RpdmUg7Lap64+MKTwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQSIgZGF0YS10bz0iUyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7KCV7IOBIFdyaXRlIiBwb2ludHM9IjEzMi41NSwxMjAuOSAxMzIuNTUsMjM3LjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkEyIiBkYXRhLXRvPSJCMiIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuuEpO2KuOybjO2BrCDrnpzshKDrp4wg64GK7Ja07KeQISDinYwiIHBvaW50cz0iNDI2LjM1MjgzMzMzMzMzMzM2LDEyMC45IDQyNi4zNTI4MzMzMzMzMzMzNiwxMzIuOSAzNzEuNTg1MDAwMDAwMDAwMDQsMTMyLjkgMzcxLjU4NTAwMDAwMDAwMDA0LDIzNy4yIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkEyIiBkYXRhLXRvPSJTMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iV3JpdGUg7Iuc64+EIPCfkqUiIHBvaW50cz0iNDg0LjMwMjE2NjY2NjY2NjY2LDEyMC45IDQ4NC4zMDIxNjY2NjY2NjY2NiwxMzIuOSA1MzkuMDcsMTMyLjkgNTM5LjA3LDM3MS4zIDQ4MC44NDQxNjY2NjY2NjY3LDM3MS4zIDQ4MC44NDQxNjY2NjY2NjY3LDQwNy4zIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJCMiIgZGF0YS10bz0iUzIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IldyaXRlIOyLnOuPhCDwn5KlIiBwb2ludHM9IjM3MS41ODUwMDAwMDAwMDAwNCwyOTEgMzcxLjU4NTAwMDAwMDAwMDA0LDM3MS4zIDQyOS44MTA4MzMzMzMzMzMzMywzNzEuMyA0MjkuODEwODMzMzMzMzMzMzMsNDA3LjMiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQSIgZGF0YS10bz0iUyIgZGF0YS1sYWJlbD0i7KCV7IOBIFdyaXRlIj4KICA8cmVjdCB4PSI5OC41NTAwMDAwMDAwMDAwMSIgeT0iMTYzLjkiIHdpZHRoPSI2Ny41NDYiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxMzIuMzIzIiB5PSIxNzkuMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuygleyDgSBXcml0ZTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJBMiIgZGF0YS10bz0iQjIiIGRhdGEtbGFiZWw9IuuEpO2KuOybjO2BrCDrnpzshKDrp4wg64GK7Ja07KeQISDinYwiPgogIDxyZWN0IHg9IjI5My4wODUwMDAwMDAwMDAwNCIgeT0iMTYzLjkiIHdpZHRoPSIxNTYuMDUyMDAwMDAwMDAwMDIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzNzEuMTExMDAwMDAwMDAwMDUiIHk9IjE3OS4wNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+64Sk7Yq47JuM7YGsIOuenOyEoOunjCDrgYrslrTsp5AhIOKdjDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJBMiIgZGF0YS10bz0iUzIiIGRhdGEtbGFiZWw9IldyaXRlIOyLnOuPhCDwn5KlIj4KICA8cmVjdCB4PSI0OTguMDciIHk9IjI0OC45NTAwMDAwMDAwMDAwMiIgd2lkdGg9IjgxLjIwOCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUzOC42NzQiIHk9IjI2NC4xIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5Xcml0ZSDsi5zrj4Qg8J+SpTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJCMiIgZGF0YS10bz0iUzIiIGRhdGEtbGFiZWw9IldyaXRlIOyLnOuPhCDwn5KlIj4KICA8cmVjdCB4PSIzMzAuNTg1MDAwMDAwMDAwMDQiIHk9IjMzNCIgd2lkdGg9IjgxLjIwOCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjM3MS4xODkiIHk9IjM0OS4xNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+V3JpdGUg7Iuc64+EIPCfkqU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkEiIGRhdGEtbGFiZWw9IuuFuOuTnCBBIDogQWN0aXZlIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjY4Ljk2NzUiIHk9Ijg0IiB3aWR0aD0iMTI3LjE2NDk5OTk5OTk5OTk5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMzIuNTUiIHk9IjEwMi40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+64W465OcIEEgOiBBY3RpdmU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlMiIGRhdGEtbGFiZWw9IuqzteycoCDsiqTthqDrpqzsp4AgREIiIGRhdGEtc2hhcGU9ImN5bGluZGVyIj4KICA8cmVjdCB4PSI1NiIgeT0iMjQ0LjIiIHdpZHRoPSIxNTMuMSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9Im5vbmUiIC8+CiAgPGxpbmUgeDE9IjU2IiB5MT0iMjQ0LjIiIHgyPSI1NiIgeTI9IjI4MS4xIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8bGluZSB4MT0iMjA5LjEiIHkxPSIyNDQuMiIgeDI9IjIwOS4xIiB5Mj0iMjgxLjEiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDxlbGxpcHNlIGN4PSIxMzIuNTUiIGN5PSIyODEuMSIgcng9Ijc2LjU1IiByeT0iNyIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDxlbGxpcHNlIGN4PSIxMzIuNTUiIGN5PSIyNDQuMiIgcng9Ijc2LjU1IiByeT0iNyIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEzMi41NSIgeT0iMjYyLjY1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7qs7XsnKAg7Iqk7Yag66as7KeAIERCPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBMiIgZGF0YS1sYWJlbD0i64W465OcIEEgOiDsl6zsoITtnoggQWN0aXZlIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM2OC40MDM1IiB5PSI4NCIgd2lkdGg9IjE3My44NDc5OTk5OTk5OTk5OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0NTUuMzI3NSIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7rhbjrk5wgQSA6IOyXrOyghO2eiCBBY3RpdmU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkIyIiBkYXRhLWxhYmVsPSLrhbjrk5wgQiA6IEHqsIAg7KO97J2AIOykhCDslYzqs6AK7J6Q7Iug7J2EIEFjdGl2ZeuhnCDsirnqsqnsi5ztgrQhIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjI2OS4xIiB5PSIyMzcuMiIgd2lkdGg9IjIwNC45Njk5OTk5OTk5OTk5NyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIzNzEuNTg1MDAwMDAwMDAwMDQiIHk9IjI2NC4wOTk5OTk5OTk5OTk5NyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMzcxLjU4NTAwMDAwMDAwMDA0IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+64W465OcIEIgOiBB6rCAIOyjveydgCDspIQg7JWM6rOgPC90c3Bhbj48dHNwYW4geD0iMzcxLjU4NTAwMDAwMDAwMDA0IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7snpDsi6DsnYQgQWN0aXZl66GcIOyKueqyqeyLnO2CtCE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzIiIGRhdGEtbGFiZWw9IuqzteycoCDsiqTthqDrpqzsp4AgREIiIGRhdGEtc2hhcGU9ImN5bGluZGVyIj4KICA8cmVjdCB4PSIzNzguNzc3NTAwMDAwMDAwMDMiIHk9IjQxNC4zIiB3aWR0aD0iMTUzLjEiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiBmaWxsPSIjZmZjZGQyIiBzdHJva2U9Im5vbmUiIC8+CiAgPGxpbmUgeDE9IjM3OC43Nzc1MDAwMDAwMDAwMyIgeTE9IjQxNC4zIiB4Mj0iMzc4Ljc3NzUwMDAwMDAwMDAzIiB5Mj0iNDUxLjIwMDAwMDAwMDAwMDA1IiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iM3B4IiAvPgogIDxsaW5lIHgxPSI1MzEuODc3NSIgeTE9IjQxNC4zIiB4Mj0iNTMxLjg3NzUiIHkyPSI0NTEuMjAwMDAwMDAwMDAwMDUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIzcHgiIC8+CiAgPGVsbGlwc2UgY3g9IjQ1NS4zMjc1MDAwMDAwMDAwNCIgY3k9IjQ1MS4yMDAwMDAwMDAwMDAwNSIgcng9Ijc2LjU1IiByeT0iNyIgZmlsbD0iI2ZmY2RkMiIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjNweCIgLz4KICA8ZWxsaXBzZSBjeD0iNDU1LjMyNzUwMDAwMDAwMDA0IiBjeT0iNDE0LjMiIHJ4PSI3Ni41NSIgcnk9IjciIGZpbGw9IiNmZmNkZDIiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIzcHgiIC8+CiAgPHRleHQgeD0iNDU1LjMyNzUwMDAwMDAwMDA0IiB5PSI0MzIuNzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuqzteycoCDsiqTthqDrpqzsp4AgREI8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik5vdGUiIGRhdGEtbGFiZWw9Ik5vdGUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjcxLjc3NzUwMDAwMDAwMDAzIiB5PSI4NCIgd2lkdGg9IjY4LjYyNiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjMwNi4wOTA1IiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk5vdGU8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 스플릿 브레인 방지를 위한 4대 펜싱(Fencing) 기술 전격 비교표 (출제 1순위)**

장애를 막기 위해 상대를 격리/차단하는 기술(Fencing)입니다.

| **방어 기술 명칭**                                        | **핵심 작동 메커니즘**                                                                                                                    | **장점 및 특징**                                              |
| :-------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------- |
| **1. STONITH** *(Shoot The Other Node In The Head)* | 네트워크가 단절되어 이상이 감지되면, 스마트 PDU나 관리 포트(IPMI)를 통해 **가짜 Active 노드의 물리적 '전원'을 강제로 내려버려 (머리에 총 쏘기) 확실하게 죽임.**                            | **가장 과격하지만 100% 확실한 방어책.** 비정상 노드의 디스크 접근을 물리적으로 완전 차단함. |
| **2. Quorum** *(정족수 다수결 투표)*                        | 노드를 항상 3개, 5개 등 \*\*'홀수'\*\*로 구성함. 단절이 발생하면 서로 투표를 진행해 **'과반수(Majority)' 이상의 연결을 확보한 그룹만 Active로 인정**하고, 소수 노드는 스스로 자살(Suicide)함. | 중앙 중재자 없이 동작 가능하며, 대규모 클라우드 클러스터의 표준 합의 방식.              |
| **3. 쿼럼 디스크** *(Tiebreaker Disk)*                   | 노드가 2대 짝수일 때 다수결이 불가능하므로, 제3의 판사 역할인 **'공유 디스크(Quorum Disk)' 영역에 먼저 도장(Lock)을 찍는 놈만 마스터로 인정**함.                                   | 적은 노드(2-Node 클러스터) 환경에서 매우 경제적이고 효과적임.                   |
| **4. Heartbeat 이중화**                                | 심장 박동을 주고받는 전용 랜선(Network)을 물리적으로 2\~3가닥 이상 이중화 구성함.                                                                              | 예방 차원의 1차 방어선 (비용 대비 효과 훌륭).                             |

#### **IV. \[결론/제언] 클라우드 네이티브(K8s) 환경에서의 분산 합의 알고리즘(Raft/Paxos) 융합**

* **(키워드 위주 2줄 마무리)** "전통적인 IDC 환경에서는 하드웨어 기반의 STONITH가 주로 쓰였으나, 노드가 수천 개로 동적으로 늘어나는 현대의 **쿠버네티스(Kubernetes) 및 MSA 분산 환경**에서는 스플릿 브레인을 방지하기 위해 **Raft나 Paxos 같은 '수학적 분산 합의(Distributed Consensus) 알고리즘'에 기반한 논리적 Quorum 투표 방식이 글로벌 스탠다드 아키텍처로 자리 잡았습니다.**"
