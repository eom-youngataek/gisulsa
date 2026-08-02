### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (WFQ정의, FIFO의한계) — 3~4줄
Ⅱ. 동작원리 - 가중치기반가상시간 (본론①, 도식 1개 필수)
Ⅲ. 계산예시및공정성보장 (본론②, 핵심 배점)
Ⅳ. 결론
```

### Ⅰ. 개요

일반적인 **FIFO(선입선출)큐**는 \*\*"먼저온패킷을먼저처리"\*\*할뿐, 트래픽의 **중요도(가중치)를전혀고려하지않습니다**. 앞서다룬 **DiffServ의DSCP딱지**가 "이패킷이얼마나중요한지"를 표시했다면, WFQ는 그 \*\*"가중치를실제로큐에서어떤순서로꺼낼지"\*\*결정하는 스케줄링알고리즘입니다.

### Ⅱ. 동작원리 — 가중치기반가상시간

| 개념                            | 내용                                                       |
| :---------------------------- | :------------------------------------------------------- |
| **흐름(Flow)별큐**                | 앞서다룬 **DiffServ의클래스**처럼, 트래픽을 **흐름별로별도큐에분류**             |
| **가중치(Weight)**               | 각흐름에 **우선순위(가중치)부여**— 가중치가높을수록 **더많은대역폭할당**              |
| **가상완료시간**(VirtualFinishTime) | 각패킷마다 \*\*"가중치를고려했을때언제전송완료돼야하는지"\*\*계산해, **그값이작은패킷부터전송** |

→ 암기: **"각패킷에 '가중치반영한도착순서표'를매겨서, 그순서대로꺼낸다"** — 앞서다룬 \*\*"SQMS(단일대기열,효율적)"\*\*의구조위에, \*\*"가중치라는공정성기준"\*\*을 추가로얹은것이 WFQ입니다.

### 도식화 제안

```
[FIFO - 가중치없음]              [WFQ - 가중치있음]
[A][B][A][C][B]... 순서대로만      [흐름A,가중치3] ─┐
(중요한트래픽도 늦게온순서면       [흐름B,가중치2] ─┼→ 가상완료시간계산
 뒤로밀림)                       [흐름C,가중치1] ─┘   → 시간이빠른것부터전송
```

### Ⅲ. 계산예시 및 공정성보장 — 핵심 배점

**함정 방지: "가중치대로처리한다"고만답하면절반. 실제로"어떻게자원을나누는지" 비율계산을보여줘야완성됩니다.**

**대역폭배분원리**: 총대역폭을 **가중치비율대로나눔**

```
흐름A(가중치3) : 흐름B(가중치2) : 흐름C(가중치1)
→ 총가중치합=6
→ A는 3/6=50%, B는 2/6≈33%, C는 1/6≈17% 대역폭할당
```

| 상황                       | WFQ의동작                           |
| :----------------------- | :------------------------------- |
| **흐름중하나가유휴상태**(전송할데이터없음) | 그몫을 **나머지흐름들이가중치비율대로나눠가짐**(낭비없음) |
| **모든흐름이바쁠때**             | 각자 **정확히가중치비율만큼**대역폭확보(기아상태방지)   |

→ 암기: **"전체파이를가중치비율로나누고, 누가안먹으면 나머지가그몫을나눠먹는다"** — 앞서다룬 \*\*"MLFQ의에이징"\*\*이 \*\*"오래기다린프로세스를구제"\*\*했듯, WFQ는 \*\*"가중치라는사전약속으로 애초에굶는일이없게"\*\*설계되어있습니다.

### 도식화 제안

```
[대역폭100%를 가중치비율로배분]
흐름A(가중치3): ████████████████████████████████████████████████ 50%
흐름B(가중치2): █████████████████████████████████ 33%
흐름C(가중치1): █████████████████ 17%

[흐름C가유휴상태가되면]
흐름A(가중치3): ████████████████████████████████████████████████████████ 60%
흐름B(가중치2): ████████████████████████████████████████ 40%
(C의몫을 A,B가 가중치비율(3:2)대로나눠가짐)
```

### Ⅳ. 결론

WFQ는 \*\*"FIFO의단순함(먼저온것먼저처리)"\*\*과 **"IntServ의완전예약(엄격하지만확장성없음)"** 사이의 실용적절충안입니다 — 앞서다룬 **DiffServ가패킷에딱지(DSCP)만붙였다면**, WFQ는 그딱지(가중치)를 실제로 \*\*"가상완료시간계산→대역폭비율배분"\*\*이라는구체적알고리즘으로 구현하는 **큐스케줄링엔진**입니다 — 이는 오늘하루다룬 \*\*TCP핸드셰이크(연결)→ARQ/슬라이딩윈도우(전송보장)→혼잡제어(속도조절)→SCTP(다중화)→DiffServ(우선순위표시)→WFQ(실제스케줄링)\*\*로 이어지는 네트워크신뢰성·품질보장시리즈전체를 완결짓는, **"약속한우선순위를실제로,공정하게지켜내는"** 마지막실행메커니즘입니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "네트워크 라우터(톨게이트)에서 패킷들을 어떤 순서로 내보낼지(줄 세우기) 결정하는 기술을 '큐잉(Queuing)'이라고 한다. 처음엔 \*\*'선착순(FIFO)'\*\*으로 보냈더니, 거대한 화물차(파일 다운로드)가 톨게이트를 꽉 막아서 뒤에 온 구급차(실시간 음성)의 지연 시간이 박살 났다. 그래서 구급차만 무조건 먼저 빼주는 \*\*'우선순위 큐잉(PQ)'\*\*을 썼더니, 구급차가 계속 오면 일반 승용차는 영원히 톨게이트를 빠져나가지 못하는 '기아 현상(Starvation, 굶어 죽음)'이 발생했다. 이를 완벽하게 해결하기 위해 등장한 끝판왕이 \*\*'WFQ(가중치 기반 공평 큐잉)'\*\*이다. 트래픽 종류별로 여러 개의 줄(Queue)을 따로 세운 뒤, 트래픽을 찔끔찔끔 보내는 구급차(음성 트래픽)에는 '가중치(Weight)'를 팍팍 줘서 우선적으로 문을 열어주고, 대역폭을 짐승처럼 집어삼키는 화물차(FTP 트래픽)는 가중치를 낮게 줘서 가끔씩만 열어준다. 결과적으로 일반 차도 굶어 죽지 않으면서 구급차의 지연 시간도 최소화하는 최고의 밸런스를 달성했다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 기아 현상을 막는 스마트한 QoS 톨게이트, WFQ 개요**

* **정의:** 네트워크 장비(라우터)에서 병목 현상이 발생할 때, 여러 개의 큐(Queue)를 만들어 패킷을 분류하고, **각 큐의 대역폭 소모량(IP Precedence)에 따라 '가중치(Weight)'를 곱해 서비스 우선순위를 동적으로 할당**하는 스케줄링(줄 세우기) 알고리즘.
* **도입 목적:** 단순 선착순(FIFO)의 지연 문제와 우선순위 방식(PQ)의 '기아 현상(Starvation)' 단점을 동시에 극복하여, 소량의 실시간 트래픽(음성/영상)을 보호하면서 대용량 트래픽도 굶어 죽지 않게 밸런스를 맞추기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) WFQ의 가중치 기반 문지기 파이프라인**

복잡한 선을 빼고, **'줄(Queue)을 나누고, 가중치에 따라 문 열어주는 횟수를 달리하는'** 직관적 원리만 그렸습니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNDMzLjE3OTk5OTk5OTk5OTggNDQ4LjczIiB3aWR0aD0iMTQzMy4xNzk5OTk5OTk5OTk4IiBoZWlnaHQ9IjQ0OC43MyIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX19XRlFfX18iIGRhdGEtbGFiZWw9IuudvOyasO2EsCDrgrTrtoDsnZggV0ZRIO2GqOqyjOydtO2KuCAo6rCA7KSR7LmYIOuwsOu2hCkiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjEzMTMuMTc5OTk5OTk5OTk5OCIgaGVpZ2h0PSIzNjguNzMiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIxMzEzLjE3OTk5OTk5OTk5OTgiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7rnbzsmrDthLAg64K067aA7J2YIFdGUSDthqjqsozsnbTtirggKOqwgOykkey5mCDrsLDrtoQpPC90ZXh0Pgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9fUXVldWVfIiBkYXRhLWxhYmVsPSLsooXrpZjrs4TroZwg64uk66W4IOykhChRdWV1ZSkg64yA6riwIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSI3ODUuNDYzIiBoZWlnaHQ9Ijk2LjkiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSI3ODUuNDYzIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI2OCIgeT0iOTgiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+7KKF66WY67OE66GcIOuLpOuluCDspIQoUXVldWUpIOuMgOq4sDwvdGV4dD4KPC9nPgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJRMSIgZGF0YS10bz0iRE9PUiIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuKcqCDqsIDspJHsuZggNTAlICjrrLgg7J6Q7KO8IOyXtOyWtOykjCkiIHBvaW50cz0iMjA3LjgyOTk5OTk5OTk5OTk4LDE2NC45IDIwNy44Mjk5OTk5OTk5OTk5OCwxODAuOSAxMzczLjE3OTk5OTk5OTk5OTgsMTgwLjkgMTM3My4xNzk5OTk5OTk5OTk4LDE4NC4yIDE2Ny44Mjk5OTk5OTk5OTk5OCwxODQuMiAxMjg1LjE3OTk5OTk5OTk5OTgsMTg0LjIgMTI4NS4xNzk5OTk5OTk5OTk4LDI0My40MTkgMTMxMy4xNzk5OTk5OTk5OTk4LDI0My40MTkgMTM3My4xNzk5OTk5OTk5OTk4LDI0My40MTkgMTM3My4xNzk5OTk5OTk5OTk4LDI4My40MTkgMTMyNS4xNzk5OTk5OTk5OTk4LDI4My40MTkgMTMyNS4xNzk5OTk5OTk5OTk4LDM0NC4zNDAwMDAwMDAwMDAwMyA4NTMuNDYzLDM0NC4zNDAwMDAwMDAwMDAwMyA4NTMuNDYzLDM0Mi42MzgwMDAwMDAwMDAwMyA4MjguOTM5OTk5OTk5OTk5OSwzNDIuNjM4MDAwMDAwMDAwMDMiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUTIiIGRhdGEtdG89IkRPT1IiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLqsIDspJHsuZggMzAlIiBwb2ludHM9IjQ2Ni44ODU5OTk5OTk5OTk5NywxNjQuOSA0NjYuODg1OTk5OTk5OTk5OTcsMTgwLjkgMjAsMTgwLjkgMjAsMjE3LjUgNDI2Ljg4NTk5OTk5OTk5OTk3LDIxNy41IDEyNzMuMTc5OTk5OTk5OTk5OCwyMTcuNSAxMjczLjE3OTk5OTk5OTk5OTgsMjY2LjU2OSAxMzEzLjE3OTk5OTk5OTk5OTgsMjY2LjU2OSAxMzEzLjE3OTk5OTk5OTk5OTgsMzA2LjU2OSAxMzEzLjE3OTk5OTk5OTk5OTgsMzYzLjM2MyA4NTMuNDYzLDM2My4zNjMgODUzLjQ2MywzNjcuNjgzOTk5OTk5OTk5OTcgODAzLjg5NCwzNjcuNjgzOTk5OTk5OTk5OTciIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUTMiIGRhdGEtdG89IkRPT1IiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLqsIDspJHsuZggMjAlICjqsIDrgZQg7Je07Ja07KSMKSIgcG9pbnRzPSI3MDcuNzg3NDk5OTk5OTk5OSwxNjQuOSA3MDcuNzg3NDk5OTk5OTk5OSwxODAuOSAxMzg1LjE3OTk5OTk5OTk5OTgsMTgwLjkgMTM4NS4xNzk5OTk5OTk5OTk4LDE1MC45IDY2Ny43ODc0OTk5OTk5OTk5LDE1MC45IDEyNjEuMTc5OTk5OTk5OTk5OCwxNTAuOSAxMjYxLjE3OTk5OTk5OTk5OTgsMTk3LjgxOTAwMDAwMDAwMDAyIDEzMTMuMTc5OTk5OTk5OTk5OCwxOTcuODE5MDAwMDAwMDAwMDIgMTM4NS4xNzk5OTk5OTk5OTk4LDE5Ny44MTkwMDAwMDAwMDAwMiAxMzg1LjE3OTk5OTk5OTk5OTgsMjM3LjgxOTAwMDAwMDAwMDAyIDEzMDEuMTc5OTk5OTk5OTk5OCwyMzcuODE5MDAwMDAwMDAwMDIgMTMwMS4xNzk5OTk5OTk5OTk4LDI4NC43MzgwMDAwMDAwMDAwNiA4NTMuNDYzLDI4NC43MzgwMDAwMDAwMDAwNiA4NTMuNDYzLDI5Mi41NDYgODAzLjg5NCwyOTIuNTQ2IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkRPT1IiIGRhdGEtdG89Ik9VVCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i6rWs6riJ7LCo64qUIOu5qOumrCDruaDsp5AhCu2ZlOusvOywqOuPhCDslYgg6rW27Ja07KO97J2MISIgcG9pbnRzPSI4MjguOTM5OTk5OTk5OTk5OSwzMTcuNTkyIDg1My40NjMsMzE3LjU5MiA4NTMuNDYzLDMxNS44OSAxMDk5Ljc3MSwzMTUuODkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iUTEiIGRhdGEtdG89IkRPT1IiIGRhdGEtbGFiZWw9IuKcqCDqsIDspJHsuZggNTAlICjrrLgg7J6Q7KO8IOyXtOyWtOykjCkiPgogIDxyZWN0IHg9IjMyOC4yMjE0OTk5OTk5OTk5IiB5PSIxNjkuMDQ5OTk5OTk5OTk5OTgiIHdpZHRoPSIxNzAuMzA4MDAwMDAwMDAwMDUiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI0MTMuMzc1NDk5OTk5OTk5OSIgeT0iMTg0LjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuKcqCDqsIDspJHsuZggNTAlICjrrLgg7J6Q7KO8IOyXtOyWtOykjCk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iUTIiIGRhdGEtdG89IkRPT1IiIGRhdGEtbGFiZWw9IuqwgOykkey5mCAzMCUiPgogIDxyZWN0IHg9IjY5MC43NTc0OTk5OTk5OTk2IiB5PSIyMDIuMzUiIHdpZHRoPSI3NC4wODAwMDAwMDAwMDAwMSIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjcyNy43OTc0OTk5OTk5OTk2IiB5PSIyMTcuNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+6rCA7KSR7LmYIDMwJTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJRMyIgZGF0YS10bz0iRE9PUiIgZGF0YS1sYWJlbD0i6rCA7KSR7LmYIDIwJSAo6rCA64GUIOyXtOyWtOykjCkiPgogIDxyZWN0IHg9IjYxNS4zMTAyNTAwMDAwMDAyIiB5PSIxMzUuNzUiIHdpZHRoPSIxNDIuOTg0MDAwMDAwMDAwMDQiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI2ODYuODAyMjUwMDAwMDAwMiIgeT0iMTUwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuqwgOykkey5mCAyMCUgKOqwgOuBlCDsl7TslrTspIwpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkRPT1IiIGRhdGEtdG89Ik9VVCIgZGF0YS1sYWJlbD0i6rWs6riJ7LCo64qUIOu5qOumrCDruaDsp5AhCu2ZlOusvOywqOuPhCDslYgg6rW27Ja07KO97J2MISI+CiAgPHJlY3QgeD0iOTA1LjM2MiIgeT0iMjkyLjg5IiB3aWR0aD0iMTMwLjUxMDAwMDAwMDAwMDAyIiBoZWlnaHQ9IjQ0LjYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iOTcwLjYxNyIgeT0iMzE1LjE5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIj48dHNwYW4geD0iOTcwLjYxNyIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPuq1rOq4ieywqOuKlCDruajrpqwg67mg7KeQITwvdHNwYW4+PHRzcGFuIHg9Ijk3MC42MTciIGR5PSIxNC4zIj7tmZTrrLzssKjrj4Qg7JWIIOq1tuyWtOyjveydjCE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRE9PUiIgZGF0YS1sYWJlbD0i66y47KeA6riwCuyKpOy8gOykhOufrArslYzqs6DrpqzsppgiIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iNzc4Ljg0OCwyNjcuNSA4NDEuNDYzLDMzMC4xMTUgNzc4Ljg0OCwzOTIuNzMgNzE2LjIzMywzMzAuMTE1IiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9Ijc3OC44NDgiIHk9IjMzMC4xMTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9Ijc3OC44NDgiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj7rrLjsp4DquLA8L3RzcGFuPjx0c3BhbiB4PSI3NzguODQ4IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7siqTsvIDspITrn6w8L3RzcGFuPjx0c3BhbiB4PSI3NzguODQ4IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7slYzqs6Drpqzsppg8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iT1VUIiBkYXRhLWxhYmVsPSLsnbjthLDrhLcg66ed7Jy866GcIOy2nOuwnCDwn5uj77iPIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjEwOTkuNzcxIiB5PSIyOTcuNDQiIHdpZHRoPSIxODkuNDA5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMTk0LjQ3NTUiIHk9IjMxNS44OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7J247YSw64S3IOunneycvOuhnCDstpzrsJwg8J+bo++4jzwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUTEiIGRhdGEtbGFiZWw9Iuq1rOq4ieywqCDspIQgKOyLpOyLnOqwhCDsnYzshLEv7J6R7J2AIO2MqO2Ctykg8J+akSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3MiIgeT0iMTI4IiB3aWR0aD0iMjcxLjY1OTk5OTk5OTk5OTk3IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjIwNy44Mjk5OTk5OTk5OTk5OCIgeT0iMTQ2LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7qtazquInssKgg7KSEICjsi6Tsi5zqsIQg7J2M7ISxL+yekeydgCDtjKjtgrcpIPCfmpE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlEyIiBkYXRhLWxhYmVsPSLsirnsmqnssKgg7KSEICjsnbzrsJgg7Ju57ISc7ZWRKSDwn5qXIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM2My42NTk5OTk5OTk5OTk5NyIgeT0iMTI4IiB3aWR0aD0iMjA2LjQ1MiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDY2Ljg4NTk5OTk5OTk5OTk3IiB5PSIxNDYuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyKueyaqeywqCDspIQgKOydvOuwmCDsm7nshJztlZEpIPCfmpc8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlEzIiBkYXRhLWxhYmVsPSLqsbDrjIAg7ZmU66y87LCoIOykhCAo64yA7Jqp65+JIEZUUCkg8J+amyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1OTAuMTEyIiB5PSIxMjgiIHdpZHRoPSIyMzUuMzUwOTk5OTk5OTk5OTciIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjcwNy43ODc0OTk5OTk5OTk5IiB5PSIxNDYuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuqxsOuMgCDtmZTrrLzssKgg7KSEICjrjIDsmqnrn4kgRlRQKSDwn5qbPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 라우터 톨게이트 스케줄링 3대 방식 전격 비교 해부 (3단 표 - 1순위)**

WFQ가 왜 나왔는지를 설명하기 위해, 멍청한 \*\*'선착순(FIFO)'\*\*과 극단적인 \*\*'우선순위(PQ)'\*\*의 단점을 반드시 대조해야 합니다.

| **큐잉(Queuing) 알고리즘**                      | **패킷을 빼내는(처리하는) 기본 방식**                                                                                                  | **치명적 단점 및 WFQ의 극복 원리 🚨**                                                                                              |
| :---------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| **1. FIFO** *(First In First Out)*        | **'무식한 선착순'.** 들어오는 트래픽 종류를 따지지 않고 무조건 하나의 거대한 큐(줄)에 세운 뒤, 먼저 들어온 놈부터 내보냄.                                               | **\[대용량 트래픽의 독점 차단 불가]** FTP 같은 덩치 큰 트래픽 1개가 줄을 꽉 차지해버리면, 그 뒤에 온 작고 급한 음성(VoIP) 트래픽이 통과하지 못하고 무한정 지연됨. (QoS 보장 0%).     |
| **2. PQ** *(Priority Queuing)*            | **'VIP 절대 우대'.** 큐를 상/중/하로 나눈 뒤, 최상위 큐(VIP)에 있는 패킷을 무조건 0순위로 다 빼줌. 상위 큐가 텅 비어야만 비로소 중/하위 큐를 빼줌.                          | **\[기아 현상(Starvation) 발생 ❌]** 상위 큐에 패킷이 끊임없이 계속 들어오면, 하위 큐(일반 트래픽)에 있는 애들은 영원히 문턱을 넘지 못하고 굶어 죽는(Drop) 참사가 발생함.          |
| **3. WFQ 👑** *(Weighted Fair* *Queuing)* | **'가중치에 따른 공평한 밸런스 분배'.** 트래픽을 종류별로 여러 큐로 찢어놓음. **작은 대역폭을 쓰는 트래픽(보통 지연에 민감한 음성)에는 높은 가중치를 주어 빨리 빼주고**, 대용량 트래픽은 가중치를 낮춤. | **\[기아 현상 해결 및 자동 QoS 보장 💯]** 대용량 파일 다운로드 트래픽도 가중치가 적을 뿐 문은 열어주기 때문에 굶어 죽지 않음(기아 현상 방지). 동시에 실시간 트래픽은 지연 없이 빠져나갈 수 있음. |

#### **IV. \[결론/제언] 하드웨어 가속 한계 극복을 위한 CBWFQ(클래스 기반)로의 진화**

* **(키워드 위주 2줄 마무리)** "WFQ는 완벽한 밸런스를 자랑하지만, 라우터가 수천 개의 트래픽 흐름(Flow)을 일일이 계산하여 가중치를 매겨야 하므로 라우터 CPU에 엄청난 부하를 줍니다. 이를 현실적으로 해결하기 위해, 개별 흐름이 아닌 **관리자가 지정한 '클래스(Class, 예: 음성반/메일반)' 단위로 큐를 묶어 뭉텅이로 가중치를 부여하는 'CBWFQ(Class-Based WFQ)'가 기업형 QoS 장비의 실질적 표준으로 사용되고 있습니다.**"
