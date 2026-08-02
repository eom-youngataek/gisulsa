### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (AS의개념, IGP/EGP분류기준) — 3~4줄
Ⅱ. IGP - AS내부라우팅 (본론①, 도식 1개 필수)
Ⅲ. EGP(BGP) - AS간라우팅, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

**AS**(AutonomousSystem,자율시스템)는 **하나의조직이독립적으로관리하는네트워크전체**(예:한통신사,한기업의전체망)입니다 — 앞서다룬 **RIP,OSPF**는 모두 \*\*"AS내부"\*\*에서 쓰이는 IGP였고, EGP는 **"서로다른AS끼리"** 라우팅정보를 교환하는 전혀다른차원의프로토콜입니다.

### Ⅱ. IGP — AS내부라우팅(InteriorGatewayProtocol)

| 항목         | 내용                        |
| :--------- | :------------------------ |
| **범위**     | **하나의AS내부**(단일조직관리)       |
| **대표프로토콜** | 앞서다룬 **RIP,OSPF**         |
| **목표**     | **최적경로(가장빠르거나비용이적은길)** 탐색 |
| **정책**     | **기술적효율성**우선(홉수,비용등)      |

→ 암기: **"한집안에서는 가장빠른길을찾는게목표"** — 앞서다룬 **OSPF의다익스트라알고리즘**이 바로 이 \*\*"내부의최적경로탐색"\*\*을 위한 도구였습니다.

### 도식화 제안

```
[AS 100 - 회사내부]
[라우터A]══OSPF══[라우터B]══OSPF══[라우터C]
(내부에서는 "가장빠른길"이 목표, IGP사용)
```

### Ⅲ. EGP(BGP) — AS간라우팅, 핵심 배점

**함정 방지: "AS끼리연결한다"고만답하면절반. 왜"기술적최적"이아니라"정책적선택"이핵심기준인지보여줘야완성됩니다.**

| 항목             | 내용                                                        |
| :------------- | :-------------------------------------------------------- |
| **범위**         | **서로다른AS사이**(인터넷전체를연결하는유일한프로토콜)                           |
| **대표프로토콜**     | **BGP**(BorderGatewayProtocol)— 현재 **인터넷전체의근간**(BGP4)     |
| **판단기준**       | **AS경로(AS-Path)**— 몇개의AS를거치는지, 그리고 \*\*정책(라우팅정책)\*\*이 최우선 |
| **핵심차이**(정책우선) | \*\*"기술적으로더빠른경로"\*\*보다 \*\*"계약,비즈니스관계에따른경로"\*\*를 선택할수있음   |

→ 암기: **"AS사이에서는 빠른길이아니라, 계약된길(정책)이우선"** — 예를들어 **"통신사A와B가피어링계약을맺었으면"**, 기술적으로 **더짧은경로가있어도** 계약에따라 **다른AS를거치는경로를선택**할수있습니다 — 이는 앞서다룬 \*\*IGP의"순수기술적최적화"\*\*와 근본적으로다른 \*\*"정책기반의사결정"\*\*입니다.

### 도식화 제안

```
[AS100] ──BGP──→ [AS200] ──BGP──→ [AS300]
(회사내부)         (통신사A)         (통신사B)

[BGP의AS-Path]: "AS100 → AS200 → AS300"
     ↓
목적지까지 여러경로가 있어도, 
"정책(계약관계,신뢰하는AS인지등)"에따라 경로선택
→ 반드시가장짧은경로가 선택되는것은아님(IGP와의핵심차이)
```

**IGP vs EGP 비교**

| 구분       | **IGP**(RIP,OSPF) | **EGP**(BGP)      |
| :------- | :---------------- | :---------------- |
| **적용범위** | AS **내부**         | AS **사이**         |
| **판단기준** | 기술적최적(비용,홉수)      | **정책**(비즈니스,신뢰관계) |
| **규모**   | 상대적으로 **작음**(한조직) | **전체인터넷**(수만개AS)  |
| **변경빈도** | 자주(트래픽변화에민감)      | **드묾**(안정성이더중요)   |

→ 앞서다룬 \*\*"5G특화망(Type1자가구축vsType3특화망사업자)"\*\*처럼, \*\*"내부(직접관리,최적화중시)vs외부(계약,정책중시)"\*\*의 구도가 여기서도 반복됩니다.

### Ⅳ. 결론

IGP와EGP의핵심차이는 \*\*"한조직내부에서는 기술적으로가장빠른길을찾지만, 조직간(AS간)에는 계약과정책이기술적효율보다우선한다"\*\*는것입니다 — 앞서다룬 \*\*RIP/OSPF(IGP)\*\*가 \*\*"AS내부의최적화"\*\*를 담당했다면, \*\*BGP(EGP)\*\*는 \*\*"AS-Path와정책에따라 인터넷전체를연결"\*\*합니다 — 이로써 오늘하루다룬 방대한라우팅시리즈전체(AODV→RIP/OSPF→MPLS→IGP/EGP)가, **"작은네트워크의최적경로탐색에서, 전세계를연결하는정책기반라우팅까지"** 확장되는 완결된 계층구조로 마무리됩니다.

### **1. 답안 전개 스토리**

> "인터넷은 수만 개의 거대한 '네트워크 영토(AS, Autonomous System)'들이 거미줄처럼 엮인 세계다. SKT 통신망, 대학교 망처럼 하나의 관리자가 통제하는 독립된 구역을 AS라 부른다. 라우팅은 이 영토를 기준으로 두 가지로 완벽히 쪼개진다. 내 땅 안에서 노는 \*\*'IGP'\*\*와, 남의 땅과 교류하는 외교관 \*\*'EGP'\*\*다. 첫째, \*\*IGP(내부 게이트웨이 프로토콜)\*\*는 하나의 AS 안(내 회사 내부)에서 라우터끼리 길을 찾는다. 온전히 내 구역이므로 돈이나 보안 따질 것 없이 무조건 **'가장 빠르고 짧은 길(최단 경로)'**을 찾는 것이 최고의 미덕이다. 대표적으로 RIP와 OSPF가 있다. 둘째, \*\*EGP(외부 게이트웨이 프로토콜)\*\*는 AS와 AS 사이(통신사와 통신사, 국가와 국가)를 연결한다. 남의 땅을 밟아야 하므로 단순히 빠른 길이 능사가 아니다. 아무리 물리적으로 빨라도 그 통신사가 망 사용료(돈)를 너무 많이 부르거나 해킹 위험(적성 국가)이 있으면 과감히 삥 돌아가는 우회로를 택한다. 즉, \*\*'정치와 비즈니스 정책(Policy)'\*\*이 최우선이다. 현재 전 세계 인터넷을 하나로 묶고 있는 유일무이한 외교관이 바로 \*\*'BGP'\*\*다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 인터넷 영토(AS)를 기준으로 나뉘는 두 세계, IGP와 EGP 개요**

* **AS (Autonomous System, 자율 시스템):** 하나의 기업, 통신사(ISP), 기관 등 동일한 관리 정책하에 운영되는 거대한 라우터들과 네트워크의 집합체 (인터넷을 구성하는 블록 단위).
* **라우팅의 이원화:** 수억 대의 전 세계 라우터를 한 번에 계산하는 것은 불가능함. 따라서 계층을 나누어, \*\*AS '내부'에서 지지고 볶는 라우팅(IGP)\*\*과 \*\*AS '외부'로 나가는 라우팅(EGP)\*\*으로 역할을 완벽하게 분담함.

#### **II. \[본론 1] (극단적 단순화 버전) 내 땅(IGP)과 남의 땅(EGP)의 라우팅 구조**

복잡한 그물망 대신, **동일한 영토 안(내부)과 영토를 벗어나는 외교(외부)의 경계선**만 직관적으로 그렸습니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3NDEuNzgwMDAwMDAwMDAwMSA3NzMuNyIgd2lkdGg9Ijc0MS43ODAwMDAwMDAwMDAxIiBoZWlnaHQ9Ijc3My43IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJBU19fX19fXyIgZGF0YS1sYWJlbD0iQVMgKOyekOycqCDsi5zsiqTthZwpIOq4sOuwmCDrnbzsmrDtjIUg6rOE7Li1IOq1rOyhsCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNjMzLjc4MDAwMDAwMDAwMDEiIGhlaWdodD0iNjkzLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI2MzMuNzgwMDAwMDAwMDAwMSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPkFTICjsnpDsnKgg7Iuc7Iqk7YWcKSDquLDrsJgg65287Jqw7YyFIOqzhOy4tSDqtazsobA8L3RleHQ+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iQVNfMTAwX19TS1RfXyIgZGF0YS1sYWJlbD0iQVMgMTAwICjsmIg6IFNLVCDthrXsi6Drp50g7JiB7YagKSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMTY4LjE3MjAwMDAwMDAwMDAzIiBoZWlnaHQ9IjM0OS4zIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMTY4LjE3MjAwMDAwMDAwMDAzIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI2OCIgeT0iOTgiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+QVMgMTAwICjsmIg6IFNLVCDthrXsi6Drp50g7JiB7YagKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IkFTXzIwMF9fS1RfXyIgZGF0YS1sYWJlbD0iQVMgMjAwICjsmIg6IEtUIO2GteyLoOunnSDsmIHthqApIj4KICA8cmVjdCB4PSI0ODkuNjA4MDAwMDAwMDAwMDYiIHk9IjQ1My4zMDAwMDAwMDAwMDAwNyIgd2lkdGg9IjE2OC4xNzIwMDAwMDAwMDAwMyIgaGVpZ2h0PSIyNjQuNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQ4OS42MDgwMDAwMDAwMDAwNiIgeT0iNDUzLjMwMDAwMDAwMDAwMDA3IiB3aWR0aD0iMTY4LjE3MjAwMDAwMDAwMDAzIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MDEuNjA4MDAwMDAwMDAwMDYiIHk9IjQ2Ny4zMDAwMDAwMDAwMDAwNyIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5BUyAyMDAgKOyYiDogS1Qg7Ya17Iug66edIOyYge2GoCk8L3RleHQ+CjwvZz4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRzEiIGRhdGEtdG89IkcyIiBkYXRhLXN0eWxlPSJ0aGljayIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJmYWxzZSIgZGF0YS1sYWJlbD0i4pyoIEVHUCAoQkdQKSDinKgK6rWt6rK97ISgIO2GteqzvCEg7ISc66Gc7J2YIOuPiCjruYTsmqkp6rO8CuygleyxhShQb2xpY3kp7J2EIOuUsOyngOupsCDsmbjqtZAg7ZiR7IOBIiBwb2ludHM9IjE0NC43NjA3NSw0MTcuMyAxNDQuNzYwNzUsNDMzLjMgNjkzLjc4MDAwMDAwMDAwMDEsNDMzLjMgNjkzLjc4MDAwMDAwMDAwMDEsNDAzLjMwMDAwMDAwMDAwMDA3IDEwMC41LDQwMy4zMDAwMDAwMDAwMDAwNyA1MzQuMTA4MDAwMDAwMDAwMSw0MDMuMzAwMDAwMDAwMDAwMDcgNTM0LjEwODAwMDAwMDAwMDEsNDEzLjMwMDAwMDAwMDAwMDA3IDY5My43ODAwMDAwMDAwMDAxLDQxMy4zMDAwMDAwMDAwMDAwNyA2OTMuNzgwMDAwMDAwMDAwMSw0OTcuMzAwMDAwMDAwMDAwMDcgNTc0LjEwODAwMDAwMDAwMDEsNDk3LjMwMDAwMDAwMDAwMDA3IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIyIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUjEiIGRhdGEtdG89IlIyIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i4pyoIElHUCAoT1NQRiDrk7EpCuuCtOu2gOunneydmCDstZzqs6Ag7IaN64+EIO2DkOyDiSEiIHBvaW50cz0iMTM2LjIzOTI1LDE2NC45IDEzNi4yMzkyNSwyOTUuNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJSMiIgZGF0YS10bz0iRzEiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE0NC43NjA3NSwzMzIuNCAxNDQuNzYwNzUsMzgwLjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRzIiIGRhdGEtdG89IlIzIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i4pyoIElHUCAoUklQIOuTsSkK64K067aA66ed7J2YIOy1nOuLqCDqsbDrpqwg7YOQ7IOJISIgcG9pbnRzPSI1NzQuMTA4MDAwMDAwMDAwMSw1MzQuMiA1NzQuMTA4MDAwMDAwMDAwMSw2NjQuODAwMDAwMDAwMDAwMSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkcxIiBkYXRhLXRvPSJHMiIgZGF0YS1sYWJlbD0i4pyoIEVHUCAoQkdQKSDinKgK6rWt6rK97ISgIO2GteqzvCEg7ISc66Gc7J2YIOuPiCjruYTsmqkp6rO8CuygleyxhShQb2xpY3kp7J2EIOuUsOyngOupsCDsmbjqtZAg7ZiR7IOBIj4KICA8cmVjdCB4PSIyMDQuNTg2IiB5PSIzNzMuODUwMDAwMDAwMDAwMSIgd2lkdGg9IjE3Ny40MzYwMDAwMDAwMDAwNCIgaGVpZ2h0PSI1OC45MDAwMDAwMDAwMDAwMDYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjkzLjMwNDAwMDAwMDAwMDAzIiB5PSI0MDMuMzAwMDAwMDAwMDAwMDciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSIyOTMuMzA0MDAwMDAwMDAwMDMiIGR5PSItMTAuNDUwMDAwMDAwMDAwMDAxIj7inKggRUdQIChCR1ApIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjI5My4zMDQwMDAwMDAwMDAwMyIgZHk9IjE0LjMiPuq1reqyveyEoCDthrXqs7whIOyEnOuhnOydmCDrj4go67mE7JqpKeqzvDwvdHNwYW4+PHRzcGFuIHg9IjI5My4zMDQwMDAwMDAwMDAwMyIgZHk9IjE0LjMiPuygleyxhShQb2xpY3kp7J2EIOuUsOyngOupsCDsmbjqtZAg7ZiR7IOBPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iUjEiIGRhdGEtdG89IlIyIiBkYXRhLWxhYmVsPSLinKggSUdQIChPU1BGIOuTsSkK64K067aA66ed7J2YIOy1nOqzoCDsho3rj4Qg7YOQ7IOJISI+CiAgPHJlY3QgeD0iNjgiIHk9IjIwNy45IiB3aWR0aD0iMTQ0LjE3MjAwMDAwMDAwMDAzIiBoZWlnaHQ9IjQ0LjYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTQwLjA4NiIgeT0iMjMwLjIwMDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIj48dHNwYW4geD0iMTQwLjA4NiIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPuKcqCBJR1AgKE9TUEYg65OxKTwvdHNwYW4+PHRzcGFuIHg9IjE0MC4wODYiIGR5PSIxNC4zIj7rgrTrtoDrp53snZgg7LWc6rOgIOyGjeuPhCDtg5Dsg4khPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iRzIiIGRhdGEtdG89IlIzIiBkYXRhLWxhYmVsPSLinKggSUdQIChSSVAg65OxKQrrgrTrtoDrp53snZgg7LWc64uoIOqxsOumrCDtg5Dsg4khIj4KICA8cmVjdCB4PSI1MDEuNjA4MDAwMDAwMDAwMDYiIHk9IjU3Ny4yMDAwMDAwMDAwMDAyIiB3aWR0aD0iMTQ0LjE3MjAwMDAwMDAwMDAzIiBoZWlnaHQ9IjQ0LjYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTczLjY5NDAwMDAwMDAwMDEiIHk9IjU5OS41MDAwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIj48dHNwYW4geD0iNTczLjY5NDAwMDAwMDAwMDEiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij7inKggSUdQIChSSVAg65OxKTwvdHNwYW4+PHRzcGFuIHg9IjU3My42OTQwMDAwMDAwMDAxIiBkeT0iMTQuMyI+64K067aA66ed7J2YIOy1nOuLqCDqsbDrpqwg7YOQ7IOJITwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJSMSIgZGF0YS1sYWJlbD0i64K067aAIOudvOyasO2EsCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3Ny4xMDI3NSIgeT0iMTI4IiB3aWR0aD0iMTE4LjI3MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTM2LjIzOTI1IiB5PSIxNDYuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuuCtOu2gCDrnbzsmrDthLA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlIyIiBkYXRhLWxhYmVsPSLrgrTrtoAg65287Jqw7YSwIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjgxLjM2MzUiIHk9IjI5NS41IiB3aWR0aD0iMTE4LjI3MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTQwLjUiIHk9IjMxMy45NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+64K067aAIOudvOyasO2EsDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRzEiIGRhdGEtbGFiZWw9Iuq0gOusuCDrnbzsmrDthLAg8J+aqiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3Ny4xMDI3NSIgeT0iMzgwLjQiIHdpZHRoPSIxMzUuMzE2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjE0NC43NjA3NSIgeT0iMzk4Ljg0OTk5OTk5OTk5OTk3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7qtIDrrLgg65287Jqw7YSwIPCfmqo8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkcyIiBkYXRhLWxhYmVsPSLqtIDrrLgg65287Jqw7YSwIPCfmqoiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTA2LjQ1MDAwMDAwMDAwMDA1IiB5PSI0OTcuMzAwMDAwMDAwMDAwMDciIHdpZHRoPSIxMzUuMzE2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjU3NC4xMDgwMDAwMDAwMDAxIiB5PSI1MTUuNzUwMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+6rSA66y4IOudvOyasO2EsCDwn5qqPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJSMyIgZGF0YS1sYWJlbD0i64K067aAIOudvOyasO2EsCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1MTQuOTcxNTAwMDAwMDAwMSIgeT0iNjY0LjgwMDAwMDAwMDAwMDEiIHdpZHRoPSIxMTguMjczIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1NzQuMTA4MDAwMDAwMDAwMSIgeT0iNjgzLjI1MDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuuCtOu2gCDrnbzsmrDthLA8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 라우팅 세계관의 충돌, IGP vs EGP 핵심 전격 비교 (3단 표 - 1순위)**

라우팅 경로를 결정할 때 최우선으로 치는 가치가 **'스피드(최적화)'냐 아니면 '돈/보안(정책)'이냐**를 대조하는 것이 핵심입니다.

| **핵심 척도 (비교 잣대)**                    | **🏠 IGP (Interior Gateway Protocol)**                                                                                | **🌐 EGP (Exterior Gateway Protocol) 🚨**                                                                                                  |
| :----------------------------------- | :-------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| **활동 영역 및 역할 (어디서 동작하는가?)**          | **'하나의 AS (자율 시스템) 내부'.** 단일 관리자가 통제하는 기업망, 학교망, 통신사 코어망 '내부'의 라우터들 사이에서 최적의 길을 찾아줌.                                  | **'서로 다른 AS (자율 시스템) 외부 간 💯'.** SKT와 구글, 한국망과 미국망 등 서로 주인이 완전히 다른 **거대 영토들을 국경선 밖에서 연결해 주는 외교관 역할.**                                      |
| **🚨 경로 탐색의 1순위 잣대 (무엇을 중요하게 여기나?)** | **'무조건 스피드 (최적화)'.** 내 구역이므로 돈이나 보안을 따질 필요가 없음. 속도(대역폭)가 가장 빠르거나, 거치는 장비 수(Hop)가 가장 적은 **'최적의 짧은 길'을 찾는 것이 최고의 미덕임.** | **'무조건 돈과 정책 (Policy) 💯'.** 남의 인프라를 타야 하므로 속도보다 돈이 중요함. 경로가 아무리 짧아도 통행료(망 사용료)가 비싸거나 보안 리스크가 있는 AS라면, **일부러 멀리 돌아가도록 정책(Policy)적으로 제어함.** |
| **데이터 수집/교환 대상 및 라우팅의 초점**           | 내 구역 안에 있는 모든 라우터의 세세한 네트워크 구조(Subnet)와 링크 상태를 샅샅이 다 수집함.                                                             | 남의 구역 라우터 속사정엔 관심 없음. 그저 "AS 100을 거쳐서 AS 200으로 가라"는 식의 **거대한 영토(AS) 단위의 경로(Path)만 수집함.**                                                   |
| **대표적인 프로토콜의 종류**                    | **RIP** (거리 벡터 / 장비 개수 기준) **OSPF** (링크 상태 / 도로 속도 기준)                                                                | **\[BGP (Border Gateway Protocol)]** 현재 전 세계 글로벌 인터넷망을 연결하는 **실질적인 유일무이한 표준 프로토콜.**                                                        |

#### **IV. \[결론/제언] BGP 하이재킹(Hijacking) 위협 및 RPKI 보안 인증의 도입 시급성**

* **(키워드 위주 2줄 마무리)** "전 세계 인터넷은 EGP의 끝판왕인 BGP로 묶여 있지만, BGP는 태생적으로 상대방이 알려주는 경로 정보를 '무조건 신뢰'하는 보안 취약점이 있습니다. 이로 인해 트래픽을 통째로 가로채는 넷플릭스/유튜브 'BGP 하이재킹' 사태가 빈발하고 있으므로, **경로 정보의 위변조를 암호학적으로 검증하는 'RPKI (리소스 공개키 기반구조)'의 전 세계 통신사 의무 도입이 인터넷 안보 차원에서 매우 시급합니다.**"
