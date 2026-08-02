### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (라우팅프로토콜분류기준) — 3~4줄
Ⅱ. RIP - 거리벡터방식 (본론①, 도식 1개 필수)
Ⅲ. OSPF - 링크상태방식, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

RIP와OSPF는 둘다 \*\*"어느경로로가야가장빠른지"\*\*를 자동으로계산하는 동적라우팅프로토콜이지만, \*\*"판단기준(거리벡터vs링크상태)"\*\*이 근본적으로다릅니다 — 앞서다룬 \*\*AODV(경로요청→응답)\*\*가 온디맨드방식이었다면, RIP/OSPF는 **"평소에도미리경로를계산해두는"** 선제적방식입니다.

### Ⅱ. RIP — 거리벡터방식(DistanceVector)

| 항목         | 내용                                                 |
| :--------- | :------------------------------------------------- |
| **판단기준**   | **홉수**(경유하는라우터개수)만으로 최적경로결정                        |
| **한계**     | **최대15홉**까지만지원(16이면"도달불가"로처리)                      |
| **정보공유방식** | 인접라우터에게 \*\*"내가아는전체경로표"\*\*를 **주기적으로**통째로전달(30초마다) |
| **수렴속도**   | **느림**— 변화가전체망에퍼지는데시간걸림("count-to-infinity"문제)     |

→ 암기: **"몇번거쳐가는지만세고,15홉넘으면포기,옆라우터에게전체표를통째로자주보낸다"** — 단순하지만 \*\*"거리만보고, 실제링크속도나상태는전혀고려하지않는다"\*\*는게 근본적한계입니다.

### 도식화 제안

```
[RIP - 거리벡터]
[라우터A] --1홉--> [라우터B] --1홉--> [목적지]  (총2홉)
[라우터A] --1홉--> [라우터C] --1홉--> [라우터D] --1홉--> [목적지] (총3홉)

→ RIP는 "홉수가적은" 경로A를선택
   (설령 경로A가 느린링크이고, 경로C가 빠른링크라도 무시됨)
```

### Ⅲ. OSPF — 링크상태방식(LinkState), 핵심 배점

**함정 방지: "더정확하다"고만답하면절반. "전체지형도를각자갖고있다"는근본적차이와, 구체적계산방법(다익스트라)을보여줘야완성됩니다.**

| 항목          | 내용                                                     |
| :---------- | :----------------------------------------------------- |
| **판단기준**    | **비용(Cost)**— 링크의 **대역폭,지연시간등실제상태**를반영한 종합점수           |
| **정보공유방식**  | 각라우터가 **자신과직접연결된링크상태만** 전체네트워크에 **broadcast**(전체표를안보냄) |
| **전체지형도구축** | 모든라우터가 받은정보를모아 \*\*"네트워크전체지도(링크상태DB)"\*\*를 **동일하게보유**  |
| **경로계산**    | 각자 **다익스트라알고리즘**으로 자신의지도위에서 **최단경로독자적계산**              |
| **수렴속도**    | **매우빠름**(변화발생시 그부분만 즉시전체에알림)                           |

→ 암기: **"내주변링크상태만알리고, 모두가받은정보를모아 전체지도를그리고, 각자그지도로최적경로를계산한다"** — 앞서다룬 \*\*"McCabe순환복잡도"\*\*에서 언급했던 \*\*"그래프이론(노드,엣지)"\*\*이, OSPF에서는 \*\*"라우터=노드,링크=엣지"\*\*로 정확히 대응되며, **다익스트라알고리즘**으로 최단경로를 계산합니다.

### 도식화 제안

```
[OSPF - 링크상태]
각라우터가 "내주변링크상태"만 broadcast
     ↓
모든라우터가 동일한"전체네트워크지도" 보유
     ↓
[다익스트라알고리즘]으로 각자 최단경로계산
(대역폭,지연시간등 실제비용을반영 - 홉수만보는RIP보다 정확)

예: 경로A(홉수적음,but느린링크) vs 경로C(홉수많음,but빠른링크)
→ OSPF는 "비용"기준으로 경로C를 선택가능(RIP는못함)
```

### Ⅳ. 결론

RIP와OSPF의근본적차이는 \*\*"거리(홉수)만보는가vs실제링크상태(비용)까지반영한전체지형도를보는가"\*\*입니다 — RIP는 **단순하지만느리고부정확**해 소규모망에만적합하고, OSPF는 **복잡하지만빠르고정확**해 대규모기업·통신사망의표준으로 자리잡았습니다 — 이는 앞서다룬 \*\*"IP-MPLS가OSPF/BGP같은동적라우팅으로경로를결정"\*\*한다고 했던 것의 **구체적내부메커니즘**이며, 오늘하루다룬 \*\*AODV(온디맨드탐색)→RIP/OSPF(사전계산)→MPLS(레이블기반빠른전달)\*\*로 이어지는 라우팅기술의 진화를 완성합니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "회사나 학교 내부망(동일 AS)에서 라우터들끼리 목적지 가는 길을 찾는 방식에는 두 가지 철학이 있다. 이정표만 믿는 \*\*'RIP(거리 벡터)'\*\*와 내비게이션을 들고 다니는 \*\*'OSPF(링크 상태)'\*\*다. 첫째, **RIP**는 아주 단순하고 무식하다. 이웃 라우터가 입으로 전해준 정보만 믿고, 오직 거쳐 가는 장비 개수(Hop Count)가 적은 길만 고른다. 10G짜리 뻥 뚫린 고속도로가 있어도 장비를 두 개 거치면 포기하고, 장비를 한 개만 거치는 10M짜리 꽉 막힌 흙길을 고른다. 업데이트 속도가 늦어 소규모 망에만 쓰인다. 둘째, **OSPF**는 라우터가 직접 전국 지도를 그린다. 망 내 모든 라우터의 연결 상태(Link)를 싹 수집한 뒤 수학(다익스트라 알고리즘)을 돌려 완벽한 지도를 완성한다. 거치는 장비가 많더라도 대역폭(Bandwidth)이 넓어 가장 빠른 최단 시간을 찾아낸다. 길이 끊기면 순식간에 새 길을 찾는 수렴 속도를 자랑해 대규모 네트워크의 영원한 1인자로 군림 중이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 내부망(IGP) 라우팅의 양대 산맥, RIP와 OSPF 개요**

* **공통점:** 동일한 관리자 권한 아래에 있는 단일 자율 시스템(AS, Autonomous System) 내부에서, 라우터들 간에 최적의 경로를 교환하고 찾아내는 **내부 게이트웨이 프로토콜(IGP)**.
* **RIP (거리 벡터):** 이웃이 주는 정보에만 의존해 '거리와 방향'만으로 길을 찾는 초창기 소규모망용 프로토콜.
* **OSPF (링크 상태):** 망 내 모든 링크(선로)의 속도와 상태 정보를 수집해, 뇌(CPU)를 굴려 스스로 전체 지도를 그리고 최적의 고속도로를 찾아내는 대규모망용 프로토콜.

#### **II. \[본론 1] (극단적 단순화 버전) 흙길로 가는 RIP vs 고속도로로 가는 OSPF**

복잡한 알고리즘을 빼고, **'장비 개수(RIP)'를 고를 것이냐 '도로의 속도(OSPF)'를 고를 것이냐**의 본질적 차이만 그렸습니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMTA4LjU4NyAyNDEuOCIgd2lkdGg9IjExMDguNTg3IiBoZWlnaHQ9IjI0MS44IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJSSVBfT1NQRl9fX01ldHJpY18iIGRhdGEtbGFiZWw9IlJJUOyZgCBPU1BG7J2YIOq4uCDssL7quLAg7LKZ64+EKE1ldHJpYykg64yA7KGwIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIxMDI4LjU4NyIgaGVpZ2h0PSIxNjEuOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjEwMjguNTg3IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+UklQ7JmAIE9TUEbsnZgg6ri4IOywvuq4sCDsspnrj4QoTWV0cmljKSDrjIDsobA8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlNUQVJUIiBkYXRhLXRvPSJSMSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i6rK966GcIEE6IDEwTSDtnZnquLghCuyepeu5hCAx6rCcIOqxsOy5qCIgcG9pbnRzPSIxOTEuMzE2LDE0MS4wNSAyMDMuMzE2LDE0MS4wNSAyMDMuMzE2LDE2Ny4zNTAwMDAwMDAwMDAwMiA0MDAuOTE2LDE2Ny4zNTAwMDAwMDAwMDAwMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUjEiIGRhdGEtdG89IkVORCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iUklQ7J2YIOyEoO2DnSEg4p2MCuyepeu5hCDsoIHqsowg6rGw7LmY64uIIOydtOumrOuhnCDqsJAiIHBvaW50cz0iNDYwLjkxNiwxNjcuMzUwMDAwMDAwMDAwMDIgOTEzLjEzNCwxNjcuMzUwMDAwMDAwMDAwMDIgOTEzLjEzNCwxNDEuMDUgOTQ5LjEzNCwxNDEuMDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlNUQVJUIiBkYXRhLXRvPSJSMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i6rK966GcIEI6IDEwRyDqs6Dsho3rj4TroZwhCuyepeu5hCAy6rCcIOqxsOy5qCIgcG9pbnRzPSIxOTEuMzE2LDEyOC43NSAyMDMuMzE2LDEyOC43NSAyMDMuMzE2LDEwMi40NSA0MDAuOTE2LDEwMi40NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUjIiIGRhdGEtdG89IlIzIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQ2MC45MTYsMTAyLjQ1IDU1Mi42NDUsMTAyLjQ1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJSMyIgZGF0YS10bz0iRU5EIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSJPU1BG7J2YIOyEoO2DnSEg8J+SrwrsnqXruYQg66eO7JWE64+EIOyGjeuPhOqwgCDruaDrpbTri4gg7J2066as66GcIOqwkCIgcG9pbnRzPSI2MTIuNjQ1LDEwMi40NSA5MTMuMTM0LDEwMi40NSA5MTMuMTM0LDEyOC43NSA5NDkuMTM0LDEyOC43NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJTVEFSVCIgZGF0YS10bz0iUjEiIGRhdGEtbGFiZWw9IuqyveuhnCBBOiAxME0g7Z2Z6ri4IQrsnqXruYQgMeqwnCDqsbDsuagiPgogIDxyZWN0IHg9IjI0Ni4zMDUwMDAwMDAwMDAwNCIgeT0iMTQ0LjM1IiB3aWR0aD0iOTkuNjIyMDAwMDAwMDAwMDMiIGhlaWdodD0iNDQuNiIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyOTYuMTE2MDAwMDAwMDAwMDQiIHk9IjE2Ni42NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSI+PHRzcGFuIHg9IjI5Ni4xMTYwMDAwMDAwMDAwNCIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPuqyveuhnCBBOiAxME0g7Z2Z6ri4ITwvdHNwYW4+PHRzcGFuIHg9IjI5Ni4xMTYwMDAwMDAwMDAwNCIgZHk9IjE0LjMiPuyepeu5hCAx6rCcIOqxsOy5qDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlIxIiBkYXRhLXRvPSJFTkQiIGRhdGEtbGFiZWw9IlJJUOydmCDshKDtg50hIOKdjArsnqXruYQg7KCB6rKMIOqxsOy5mOuLiCDsnbTrpqzroZwg6rCQIj4KICA8cmVjdCB4PSI1MDQuOTE1OTk5OTk5OTk5OTQiIHk9IjE0NC4zNSIgd2lkdGg9IjE1NS40NTgwMDAwMDAwMDAwMyIgaGVpZ2h0PSI0NC42IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjU4Mi42NDUiIHk9IjE2Ni42NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSI+PHRzcGFuIHg9IjU4Mi42NDUiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij5SSVDsnZgg7ISg7YOdISDinYw8L3RzcGFuPjx0c3BhbiB4PSI1ODIuNjQ1IiBkeT0iMTQuMyI+7J6l67mEIOyggeqyjCDqsbDsuZjri4gg7J2066as66GcIOqwkDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlNUQVJUIiBkYXRhLXRvPSJSMiIgZGF0YS1sYWJlbD0i6rK966GcIEI6IDEwRyDqs6Dsho3rj4TroZwhCuyepeu5hCAy6rCcIOqxsOy5qCI+CiAgPHJlY3QgeD0iMjM1LjMxNTk5OTk5OTk5OTk3IiB5PSI3OS40NSIgd2lkdGg9IjEyMS42MDAwMDAwMDAwMDAwMSIgaGVpZ2h0PSI0NC42IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjI5Ni4xMTYiIHk9IjEwMS43NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSI+PHRzcGFuIHg9IjI5Ni4xMTYiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij7qsr3roZwgQjogMTBHIOqzoOyGjeuPhOuhnCE8L3RzcGFuPjx0c3BhbiB4PSIyOTYuMTE2IiBkeT0iMTQuMyI+7J6l67mEIDLqsJwg6rGw7LmoPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iUjMiIGRhdGEtdG89IkVORCIgZGF0YS1sYWJlbD0iT1NQRuydmCDshKDtg50hIPCfkq8K7J6l67mEIOunjuyVhOuPhCDsho3rj4TqsIAg67mg66W064uIIOydtOumrOuhnCDqsJAiPgogIDxyZWN0IHg9IjcwMC4zNzQiIHk9Ijc5LjQ1IiB3aWR0aD0iMjA0Ljc2MDAwMDAwMDAwMDA1IiBoZWlnaHQ9IjQ0LjYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iODAyLjc1NCIgeT0iMTAxLjc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIj48dHNwYW4geD0iODAyLjc1NCIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPk9TUEbsnZgg7ISg7YOdISDwn5KvPC90c3Bhbj48dHNwYW4geD0iODAyLjc1NCIgZHk9IjE0LjMiPuyepeu5hCDrp47slYTrj4Qg7IaN64+E6rCAIOu5oOultOuLiCDsnbTrpqzroZwg6rCQPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlNUQVJUIiBkYXRhLWxhYmVsPSLstpzrsJwg65287Jqw7YSwIPCfmqUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9IjExNi40NSIgd2lkdGg9IjEzNS4zMTYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEyMy42NTgiIHk9IjEzNC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7stpzrsJwg65287Jqw7YSwIPCfmqU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlIxIiBkYXRhLWxhYmVsPSJSMSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MDAuOTE2IiB5PSIxNDguOSIgd2lkdGg9IjYwIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjQzMC45MTYiIHk9IjE2Ny4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+UjE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkVORCIgZGF0YS1sYWJlbD0i66qp7KCB7KeAIPCfj4EiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iOTQ5LjEzNCIgeT0iMTE2LjQ1IiB3aWR0aD0iMTAzLjQ1MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTAwMC44NjA1IiB5PSIxMzQuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+66qp7KCB7KeAIPCfj4E8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlIyIiBkYXRhLWxhYmVsPSJSMiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MDAuOTE2IiB5PSI4NCIgd2lkdGg9IjYwIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDMwLjkxNiIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5SMjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUjMiIGRhdGEtbGFiZWw9IlIzIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU1Mi42NDUiIHk9Ijg0IiB3aWR0aD0iNjAiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNTgyLjY0NSIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5SMzwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 라우팅 세계관의 충돌, RIP vs OSPF 핵심 전격 비교 (3단 표 - 1순위)**

가장 중요한 출제 포인트는 경로를 선택하는 \*\*'척도(Metric)'\*\*가 무엇인지, 그리고 지도를 주고받는 방식에 따른 **'수렴(Convergence) 속도'**를 대조하는 것입니다.

| **핵심 척도 (비교 잣대)**                 | **🛑 RIP (거리 벡터 방식)**                                                                                                             | **🚀 OSPF (링크 상태 방식) 🚨**                                                                                                       |
| :-------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| **길을 고르는 절대 기준 (Metric 척도)**      | **'장비 통과 개수 (Hop Count)'.** 링크의 속도가 10G든 10M든 전혀 상관 안 함. 오직 **거쳐 가는 라우터 개수(Hop)가 적은 경로**만을 최적이라고 판단함. (최대 15 홉까지만 통신 가능).         | **'링크의 대역폭과 비용 (Cost) 💯'.** 장비를 10개 거치더라도 그 길이 광랜(대역폭이 큰 고속도로)이면 무조건 그 길을 선택함. **실질적인 네트워크 체감 속도가 가장 빠름.**                     |
| **정보 교환 방식 및 수렴(Convergence) 속도** | **\[30초마다 무조건 통째로 교환 / 엄청 느림 ❌]** 변화가 있든 없든 30초마다 이웃에게 자기 지도를 통째로 다 던짐. 길이 끊어졌을 때 망 전체가 알게 되는 수렴 속도가 매우 느려 핑핑 도는 루핑(Looping)이 생김. | **\[변화가 있을 때만 부분 교환 / 엄청 빠름 💯]** 평소엔 가만히 있다가, **어디 선로 하나가 끊어지면 그 정보만 즉시 전체에 방송(Flooding)함.** 수렴 속도가 초고속이라 대규모 네트워크 장애 복구에 탁월함. |
| **구동 핵심 알고리즘 및 장비 부하**            | **벨만-포드 (Bellman-Ford) 알고리즘.** 계산이 너무 단순해서 라우터의 CPU와 메모리를 전혀 잡아먹지 않음. (싸구려 장비에서도 잘 돔).                                            | **\[다익스트라 (Dijkstra) SPF 알고리즘]** 전국 지도를 그리고 수학 계산을 해야 하므로, 라우터의 CPU와 메모리 등 자원 소모가 매우 큼.                                         |

#### **IV. \[결론/제언] IS-IS 프로토콜과의 경쟁 및 SDN 중앙 집중화로의 진화**

* **(키워드 위주 2줄 마무리)** "현재 대규모 엔터프라이즈 내부망은 OSPF가 100% 장악하고 있지만, 통신사(ISP) 급의 초대형 백본망에서는 OSPF보다 확장성이 뛰어나고 IPv6 처리가 부드러운 'IS-IS' 프로토콜이 경쟁하고 있습니다. 나아가 현대 클라우드 인프라에서는 이 복잡한 OSPF 수학 계산마저 라우터 장비에서 빼앗아, **SDN 중앙 컨트롤러가 전국망을 단숨에 계산하여 내려꽂아 주는 중앙 통제형(SDN 기반 라우팅) 구조로 패러다임이 이동하고 있습니다.**"
