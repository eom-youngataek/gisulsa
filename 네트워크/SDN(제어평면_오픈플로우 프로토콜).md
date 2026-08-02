### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (SDN정의, 전통네트워크와의차이) — 3~4줄
Ⅱ. 3계층분리구조 (본론①, 도식 1개 필수)
Ⅲ. OpenFlow - 제어/데이터평면통신, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

전통적인라우터·스위치는 \*\*"어디로보낼지결정하는 두뇌(제어평면)"\*\*와 \*\*"실제로패킷을보내는 손발(데이터평면)"\*\*이 **하나의장비안에고정**되어 있었습니다. SDN(Software-DefinedNetworking)은 이 둘을 **분리**해서, **"두뇌는중앙의소프트웨어컨트롤러하나로,손발은여러장비로"** 재구성합니다.

### Ⅱ. 3계층분리구조

| 계층             | 역할                                             |
| :------------- | :--------------------------------------------- |
| **애플리케이션평면**   | 네트워크서비스·정책을 **정의**(앞서다룬IBN의 \*\*"의도"\*\*가여기위치) |
| **제어평면**(중앙집중) | **SDN컨트롤러**가 전체네트워크상태를파악해 **라우팅결정**            |
| **데이터평면**(분산)  | 스위치·라우터가 **컨트롤러의지시대로 단순히패킷전달만** 수행             |

→ 암기: **"정책을정하고(앱),중앙두뇌가결정하고(제어),여러장비가그저전달만한다(데이터)"** — 앞서다룬 \*\*"IBN의4대구성요소"\*\*중 \*\*"자동구현"\*\*단계가, 바로 이 **SDN의데이터평면**을 통해 실제로 구현됩니다.

### 도식화 제안

```
[애플리케이션평면] 정책·의도 정의(IBN의영역)
        ↓
[제어평면] SDN컨트롤러 (중앙집중,전체네트워크"두뇌")
        ↓ (OpenFlow로지시)
[데이터평면] 스위치1  스위치2  스위치3 ... (단순전달만,"손발")

← 전통네트워크: 각장비마다 두뇌+손발이 함께내장되어 있었음
```

### Ⅲ. OpenFlow — 제어/데이터평면통신, 핵심 배점

**함정 방지: "SDN컨트롤러가지시한다"고만답하면절반. 그지시가 구체적으로어떤형태(플로우테이블)로전달되는지보여줘야완성됩니다.**

| 개념                    | 내용                                                                                                |
| :-------------------- | :------------------------------------------------------------------------------------------------ |
| **OpenFlow프로토콜**      | SDN **컨트롤러와스위치사이의표준통신규약**— "이런패킷이오면이렇게처리해라"를 전달                                                   |
| **플로우테이블**(FlowTable) | 스위치에 저장되는 \*\*"매치조건→처리동작"\*\*규칙목록 — 앞서다룬 **DiffServ의DSCP딱지**처럼, **패킷의헤더값(출발지,목적지,포트등)을 매치**해 동작결정 |
| **동작예시**              | "출발지IP가X이고목적지포트가80이면 → 포트3으로전달"                                                                   |

→ 암기: **"컨트롤러가규칙표(플로우테이블)를스위치에심어주고, 스위치는그표만보고 기계적으로처리한다"** — 앞서다룬 \*\*"QoS의DiffServ(패킷헤더의딱지만보고처리)"\*\*철학이, SDN에서는 \*\*"플로우테이블의매치규칙"\*\*으로 더세밀하고 유연하게 구현됩니다.

### 도식화 제안

```
[SDN컨트롤러] ──OpenFlow로 규칙전달──→ [스위치]
                                        [플로우테이블]
                                        조건: 출발지IP=X,포트=80
                                        동작: 포트3으로전달
                                        조건: 목적지IP=Y
                                        동작: 폐기(보안차단)
                                              ↓
                                     실제패킷이 오면 표만보고 즉시처리
```

**SDN의핵심가치**: 앞서다룬 \*\*"방법론테일러링"\*\*처럼, **네트워크정책을 물리적장비하나하나가아니라 중앙컨트롤러에서 소프트웨어적으로한번에변경**할수있어, \*\*"새로운정책적용속도"\*\*가 획기적으로빨라집니다 — 이는 앞서다룬 **"LGU+의컴포저블인프라"**(자원을소프트웨어로유연하게재배치)의 핵심기반기술입니다.

### Ⅳ. 결론

SDN은 \*\*"제어평면(두뇌)과데이터평면(손발)을분리해, 중앙집중식소프트웨어로전체네트워크를유연하게제어"\*\*하는 아키텍처이며, OpenFlow는 그 **"컨트롤러의결정을 플로우테이블이라는구체적규칙으로 스위치에전달하는"** 표준통신규약입니다 — 이는 앞서다룬 \*\*IBN(의도기반자동화)\*\*이 \*\*"왜SDN위에얹어지는지"\*\*를 명확히보여줍니다: SDN이 \*\*"중앙에서네트워크를조작할수있는창구"\*\*를 만들어줬기에, IBN은 그위에서 \*\*"자연어의도를 OpenFlow규칙으로번역"\*\*할수있게됩니다 — 이로써 오늘하루의방대한네트워크시리즈전체(QoS→WFQ→AODV→IBN→SDN)가, **"네트워크를사람이일일이설정하는것에서, 소프트웨어가유연하게제어하고, 결국AI가의도를이해해자동화하는"** 하나의완결된진화의역사로 마무리됩니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "과거 라우터(네트워크 장비)는 길을 계산하는 똑똑한 '머리(제어부)'와 패킷을 던져주는 '손발(데이터부)'이 한 기계 안에 뭉쳐있었다. 그래서 시스코(Cisco) 같은 비싼 장비를 사면 그 회사의 명령어로만 관리해야 하는 벤더 종속(노예) 상태였다. 이 사슬을 끊어버린 아키텍처 혁명이 \*\*'SDN(소프트웨어 정의 네트워크)'\*\*이다. 장비들에서 똑똑한 \*\*'머리(제어 평면, Control Plane)'\*\*를 쏙 뽑아내어 중앙의 컨트롤러 서버 하나로 싹 모아버렸다. 그리고 전국의 스위치들은 뇌가 없는 단순한 깡통(데이터 평면)으로 전락시켰다. 이제 중앙의 똑똑한 뇌 하나가 전국의 깡통 스위치들을 지휘한다. 이때 뇌가 깡통들에게 명령을 내릴 때 쓰는 글로벌 표준 공용어가 바로 **'오픈플로우(OpenFlow) 프로토콜'**이다. 뇌와 깡통을 잇는 이 남단 인터페이스(Southbound API) 덕분에, 비싼 브랜드 장비를 버리고 이름 없는 싸구려 화이트박스(깡통) 수천 대를 꽂아도 완벽히 통제되는 인프라 혁신이 일어났다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 네트워크 하드웨어의 노예 해방 선언, SDN 개요**

* **정의:** 네트워크 장비에서 '경로를 제어하는 뇌(Control Plane)'와 '데이터를 단순히 전달하는 손발(Data Plane)'을 **물리적/논리적으로 분리**하고, 제어부를 소프트웨어 기반의 중앙 컨트롤러로 집중시켜 전체 네트워크를 통합 프로그래밍(제어)하는 아키텍처.
* **도입 목적:** 특정 벤더(Cisco, Huawei 등)의 폐쇄적인 하드웨어 종속성(Lock-in)을 탈피하고, 클라우드 환경의 잦은 네트워크 변경 요구에 소프트웨어 코딩만으로 수 분 내에 인프라를 재구성할 수 있는 '민첩성(Agility)'을 확보하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 뇌와 깡통을 분리한 SDN 3계층 파이프라인**

복잡한 계층 박스 대신, **머리(응용/제어)와 손발(스위치), 그리고 그 사이를 잇는 'API 통신선'**만 직관적으로 그렸습니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzNzcuNzMxOTk5OTk5OTk5OTcgNTAwLjIwMDAwMDAwMDAwMDA1IiB3aWR0aD0iMzc3LjczMTk5OTk5OTk5OTk3IiBoZWlnaHQ9IjUwMC4yMDAwMDAwMDAwMDAwNSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iU0ROX19fT3BlbkZsb3dfIiBkYXRhLWxhYmVsPSJTRE4g6rOE7Li1IOq1rOyhsOyZgCDsmKTtlIjtlIzroZzsmrAoT3BlbkZsb3cp7J2YIOyXre2VoCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMjk3LjczMTk5OTk5OTk5OTk3IiBoZWlnaHQ9IjQyMC4yMDAwMDAwMDAwMDAwNSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjI5Ny43MzE5OTk5OTk5OTk5NyIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPlNETiDqs4TsuLUg6rWs7KGw7JmAIOyYpO2UiO2UjOuhnOyasChPcGVuRmxvdynsnZgg7Jet7ZWgPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBUFAiIGRhdGEtdG89IkNUUkwiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSJOb3J0aGJvdW5kIEFQSSAoUkVTVCkiIHBvaW50cz0iMTg4Ljg2NTk5OTk5OTk5OTk5LDEzNy44IDE4OC44NjU5OTk5OTk5OTk5OSwyNTQuMTAwMDAwMDAwMDAwMDIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQ1RSTCIgZGF0YS10bz0iU1dJVENIIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i4pyoIFNvdXRoYm91bmQgQVBJICjsmKTtlIjtlIzroZzsmrApIOKcqCIgcG9pbnRzPSIxODguODY1OTk5OTk5OTk5OTksMjkxIDE4OC44NjU5OTk5OTk5OTk5OSw0MDcuMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkFQUCIgZGF0YS10bz0iQ1RSTCIgZGF0YS1sYWJlbD0iTm9ydGhib3VuZCBBUEkgKFJFU1QpIj4KICA8cmVjdCB4PSIxMjQuMzY1OTk5OTk5OTk5OTkiIHk9IjE4MC44IiB3aWR0aD0iMTI4LjEzNDAwMDAwMDAwMDAxIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTg4LjQzMyIgeT0iMTk1Ljk1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5Ob3J0aGJvdW5kIEFQSSAoUkVTVCk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQ1RSTCIgZGF0YS10bz0iU1dJVENIIiBkYXRhLWxhYmVsPSLinKggU291dGhib3VuZCBBUEkgKOyYpO2UiO2UjOuhnOyasCkg4pyoIj4KICA8cmVjdCB4PSI5NC44NjU5OTk5OTk5OTk5NyIgeT0iMzM0IiB3aWR0aD0iMTg3LjUzNDAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTg4LjYzMjk5OTk5OTk5OTk4IiB5PSIzNDkuMTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuKcqCBTb3V0aGJvdW5kIEFQSSAo7Jik7ZSI7ZSM66Gc7JqwKSDinKg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkFQUCIgZGF0YS1sYWJlbD0iMS4g7J2R7JqpIOqzhOy4tSAo67Cp7ZmU67K9L+udvOyasO2MhSDslbEpIPCfk7EK7IKs656M7J2YIOyDneqwgTogJ+yVvCwgQeq4uCDrp4nqs6AgQuq4uCDsl7TslrQhJyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSIyNjUuNzMxOTk5OTk5OTk5OTciIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE4OC44NjU5OTk5OTk5OTk5OSIgeT0iMTEwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE4OC44NjU5OTk5OTk5OTk5OSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPjEuIOydkeyaqSDqs4TsuLUgKOuwqe2ZlOuyvS/rnbzsmrDtjIUg7JWxKSDwn5OxPC90c3Bhbj48dHNwYW4geD0iMTg4Ljg2NTk5OTk5OTk5OTk5IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7sgqzrnozsnZgg7IOd6rCBOiAmIzM5O+yVvCwgQeq4uCDrp4nqs6AgQuq4uCDsl7TslrQhJiMzOTs8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ1RSTCIgZGF0YS1sYWJlbD0iQ1RSTCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxNTAuMTA2OTk5OTk5OTk5OTciIHk9IjI1NC4xMDAwMDAwMDAwMDAwMiIgd2lkdGg9Ijc3LjUxOCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxODguODY1OTk5OTk5OTk5OTkiIHk9IjI3Mi41NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Q1RSTDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU1dJVENIIiBkYXRhLWxhYmVsPSJTV0lUQ0giIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTQzLjA2NzUiIHk9IjQwNy4zIiB3aWR0aD0iOTEuNTk3MDAwMDAwMDAwMDEiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTg4Ljg2NTk5OTk5OTk5OTk5IiB5PSI0MjUuNzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlNXSVRDSDwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 기존 라우터 vs SDN의 제어 방식 대조 및 오픈플로우의 가치 (3단 표)**

가장 중요한 포인트인 제어권(Control Plane)이 **'어디에 위치하는가(분산 vs 중앙)'**와 뇌를 연결하는 **'오픈플로우'**의 존재 의의를 대조해야 합니다.

| **핵심 척도 (비교 잣대)**                     | **🛑 기존 레거시 라우터 (전통 방식)**                                                                                      | **🚀 SDN 구조 및 오픈플로우(OpenFlow) 🚨**                                                                                             |
| :------------------------------------ | :------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| **제어 평면(Control Plane)의 위치와 의사결정 구조** | **'장비마다 뇌가 박혀 있는 분산형'.** 전국에 깔린 스위치(라우터) 100대가 각각 뇌를 가지고 스스로 경로를 계산함. 정책 하나 바꾸려면 100대 장비에 일일이 접속해 명령어를 다 쳐야 함. | **'중앙 통제형 (머리와 손발의 분리) 💯'.** 장비에서 뇌(제어 평면)를 싹 뽑아서 **중앙의 단일 서버(SDN 컨트롤러)**로 뭉쳐놓음. 관리자는 컨트롤러 하나만 조작하면 전국 100대의 스위치가 일사불란하게 움직임. |
| **✨ 뇌와 깡통 스위치를 연결하는 킬러 프로토콜**         | (각 장비 제조사 고유의 폐쇄적 CLI 명령어 사용 ➔ 시스코 노예됨)                                                                        | **\[오픈플로우 (OpenFlow / Southbound API)]** 컨트롤러(뇌)가 깡통 스위치(데이터 평면)에게 길(Flow Table)을 세팅해 줄 때 쓰는 **'제조사 상관없이 다 통하는 글로벌 공용어'**.     |
| **하드웨어 종속성 및 경제성 극대화 요소**             | 비싼 브랜드(Cisco) 장비를 사야만 그 회사의 뇌(라우팅 기능)를 쓸 수 있어 비용 폭발 (Vendor Lock-in ❌).                                        | 뇌는 컨트롤러(S/W)가 다 하므로, **밑에 깔리는 스위치는 싼 중국산 깡통(화이트박스)을 써도 똑같은 성능을 발휘함 (CAPEX 획기적 절감 💯).**                                        |

#### **IV. \[결론/제언] IBN(인텐트 기반)으로의 진화와 데이터 평면 프로그래밍(P4)**

* **(키워드 위주 2줄 마무리)** "SDN과 오픈플로우는 네트워킹의 역사를 바꿨지만, 아직도 관리자가 뇌(컨트롤러)에게 스크립트(How)를 짜서 명령을 내려야 하는 수동 작업이 남습니다. 이를 극복하기 위해 단순히 '의도(What)'만 던지면 AI가 알아서 SDN을 세팅하는 **IBN(인텐트 기반 네트워킹)으로 진화하고 있으며, 깡통 스위치의 동작조차 하드웨어 칩(ASIC) 단에서 프로그래밍하는 차세대 언어 'P4'가 도입되고 있습니다.**"
