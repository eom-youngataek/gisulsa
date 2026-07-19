### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (IT보안과OT보안의근본적차이) — 3~4줄
Ⅱ. 4대구성체계 (본론①, 도식 1개 필수)
Ⅲ. 보안수준(SL) - 3중구조 (본론②, 핵심 배점)
Ⅳ. IT보안과의차이및오늘시리즈연결
Ⅴ. 결론
```

포인트: 개요에서 \*\*"오늘하루다룬 IT보안(암호,접근통제,백도어등)은 '데이터'를보호하는것이목표였는데, 산업제어시스템(발전소,공장)의보안목표는 '물리적안전(사람이안죽는것)'이최우선 — IT시스템은다운되면돈이드는것에서끝나지만,ICS가다운되면공장이폭발하거나전력망이멈춘다"\*\*는한줄로시작하면, 왜 IT표준(ISO27001등)과별도로 OT전용표준이 필요한지 논리가섭니다.

### Ⅱ. 4대구성체계

| Part                            | 명칭     | 내용                                  |
| :------------------------------ | :----- | :---------------------------------- |
| **일반**(General)                 | 개념·용어  | 표준전체의 **공통개념,모델**정의                 |
| **정책및절차**(Policies\&Procedures) | 조직관리체계 | **ISO27001을기반**으로 **14개영역보안통제항목**제시 |
| **시스템**(System)                 | 시스템설계  | 시스템 **아키텍처,보안수준요구사항**               |
| **컴포넌트**(Component)             | 개별부품   | **PLC,센서등개별장비**의 보안요구사항(4-2)        |

→ 암기: **"일반개념잡고,조직정책세우고,시스템전체를설계하고,개별부품까지검증한다"** — 앞서다룬 \*\*"ISO/IEC12207(소프트웨어생명주기)"\*\*과 유사하게, ISA/IEC62443도 \*\*"조직→시스템→컴포넌트"\*\*로 내려가는 계층구조를갖습니다 — 다만 대상이 **소프트웨어가아니라산업제어시스템**이라는 점이 다릅니다.

### 도식화 제안

```
[일반] 개념·용어 (전체의뼈대)
   ↓
[정책및절차] ISO27001기반 14개영역 (조직차원관리체계)
   ↓
[시스템] 시스템아키텍처,SL요구사항
   ↓
[컴포넌트] PLC,센서등 개별장비검증(4-2)
```

### Ⅲ. 보안수준(SL) — 3중구조, 핵심 배점

**함정 방지: "등급이있다"고만답하면절반. 목표(SL-T)-달성(SL-A)-역량(SL-C)3개가서로다른의미라는걸보여줘야완성됩니다.**

| SL유형                 | 의미                              |
| :------------------- | :------------------------------ |
| **SL-T**(Target)     | 위험평가를거쳐 **정해야할목표보안수준**          |
| **SL-A**(Achieved)   | 실제 **구현후달성된보안수준**(SL-T와비교해 갭분석) |
| **SL-C**(Capability) | 해당 **컴포넌트/시스템이설계상낼수있는최대보안역량**   |

→ 암기: **"목표를정하고(SL-T),실제구현한걸측정하고(SL-A),그부품이원래가진최대능력을확인한다(SL-C)"** — 예를들어 \*\*PLC(프로그래머블로직컨트롤러)\*\*가 \*\*"레벨1은공개키암호안써도되고,레벨2는인증서서명검사가필요"\*\*하다는 구체적기준이 이 SL 레벨에 명시됩니다 — 앞서다룬 \*\*비대칭키암호(공개키/서명)\*\*가 실제 산업현장부품의 **등급별요구사항**으로 구체화됩니다.

### 도식화 제안

```
[위험평가] → SL-T(목표: "레벨3필요") 설정
     ↓
[시스템구축] → SL-A(실제달성: "레벨2에그침") 측정
     ↓
[갭발견] SL-T(3) > SL-A(2) → 보완필요
     ↓
[컴포넌트선택] SL-C(그부품이낼수있는최대치) 확인후 교체/보강
```

### Ⅳ. IT보안과의차이 및 오늘시리즈연결

**함정 방지: "OT도결국보안이다"라고만하면절반. IT와OT의구체적차이,그리고오늘다룬IT공격이OT에어떻게적용되는지보여줘야완성됩니다.**

| 구분           | **IT보안**(오늘의시리즈)        | **OT보안**(ISA/IEC62443)                                  |
| :----------- | :---------------------- | :------------------------------------------------------ |
| **최우선목표**    | \*\*기밀성(C)\*\*우선        | **가용성·안전성**우선(다운되면 물리적사고)                               |
| **패치정책**     | **즉시패치**권장              | **가동중단없이패치어려움**— 24시간연속운영,재부팅자체가큰비용                     |
| **수명주기**     | 수년(빠른교체)                | **수십년**(발전소설비는교체가매우드묾) — 오래된취약점이 방치되기쉬움                 |
| **제로트러스트연계** | 앞서다룬 **RBAC/ABAC**가직접적용 | ISA/IEC62443도 **"제로트러스트모델실현에영향"**— 다만 **가용성최우선전제하에** 적용 |

→ 앞서다룬 \*\*"MITRE ATT\&CK"\*\*같은 프레임워크가 \*\*ICS전용버전(ATT\&CKforICS)\*\*으로도존재하며, **ISA/IEC62443의보안통제를이프레임워크에매핑**해 **실제위협에대응**하는 방법론이 활용됩니다 — 이는 앞서다룬 **미라이봇넷,측면이동**같은 IT영역공격기법이, **PLC·센서같은OT장비를노릴때** 어떻게대응해야하는지의 실무적연결점입니다.

### Ⅴ. 결론 포인트 (오늘 하루 방대한 암호·보안 시리즈 최종대단원)

ISA/IEC62443은 \*\*"오늘하루다룬모든IT보안원리(암호,접근통제,제로트러스트)가, '사람의생명과물리적안전'이걸린산업제어시스템환경에서는 어떻게재조정되어야하는가"\*\*를 보여주는 표준입니다 — **가용성과안전성이기밀성보다우선**되고, **수십년된낡은장비도보호대상**이되어야한다는점에서, IT의빠른패치문화와는 근본적으로다른접근이필요합니다 — 오늘하루다룬 대칭/비대칭암호부터 네트워크스캐닝,ISA/IEC62443까지이어지는 방대한암호·보안시리즈전체가, 결국 \*\*"보안은지키는대상(데이터냐,물리적안전이냐)에따라 그해법과우선순위가완전히달라진다"\*\*는 최종교훈으로, 하루종일이어진 이거대한여정을 완전히마무리합니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "일반 사무실 컴퓨터(IT 환경)가 해킹당하면 '정보 유출(기밀 파괴)'로 끝나지만, 원자력 발전소나 공장(OT/ICS 환경)이 해킹당하면 터빈이 멈추거나 폭발해 **'사람이 죽는다(가용성과 안전 파괴)'**. 따라서 기존 IT용 정보보안(ISO 27001 등)으로는 공장을 지킬 수 없다. 이란의 원심분리기를 파괴한 '스턱스넷(Stuxnet)' 사태 이후, 공장 인프라만을 지키기 위해 탄생한 전 세계의 절대 헌법이 바로 **'ISA/IEC 62443'** 표준이다. 이 표준의 핵심 암기 키워드는 딱 2개다. **① 구역과 파이프 (Zones & Conduits):** 거대한 공장 네트워크를 통째로 두지 않고 방화벽으로 잘게 쪼개어(Zone), 안전한 파이프라인(Conduit)으로만 통신하게 만들어 랜섬웨어 확산을 막는다. **② 보안 수준 (SL, Security Level):** 공장의 중요도에 따라, SL 1(단순 실수 방어)부터 SL 4(국가 단위의 정예 해커 방어)까지 방어의 체급을 4단계로 나눈다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 생명과 안전을 지키는 최후의 보루, ISA/IEC 62443 개요**

* **정의:** 산업 제어 시스템(ICS) 및 운영 기술(OT) 환경의 취약점을 완화하고 사이버 위협으로부터 안전하게 보호하기 위해 제정된 **'국제 공통 산업 보안 표준'**.
* **제정 목적:** 기밀성(C)을 최우선으로 하는 기존 IT 보안과 달리, 공장 셧다운을 막기 위한 \*\*'가용성(Availability)과 물리적 안전(Safety)'\*\*을 최우선 목표로 설계됨.

#### **II. \[본론 1] 확산을 막는 공장 내 격리 기술, Zones & Conduits (도식화)**

네트워크를 쪼개어 해커의 측면 이동을 막는 IEC 62443의 핵심 설계 사상을 단순화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDk1LjMwOCAzNTAuOSIgd2lkdGg9IjEwOTUuMzA4IiBoZWlnaHQ9IjM1MC45IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJJU0FJRUNfNjI0NDNfX19ab25lc19fX0NvbmR1aXRzX18iIGRhdGEtbGFiZWw9IklTQS9JRUMgNjI0NDPsnZgg7ZW17IusIDogWm9uZXMgKOq1rOyXrSkgJmFtcDsgQ29uZHVpdHMgKO2GteyLoCDtjIzsnbTtlIQpIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIxMDE1LjMwOCIgaGVpZ2h0PSIyNzAuOSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjEwMTUuMzA4IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+SVNBL0lFQyA2MjQ0M+ydmCDtlbXsi6wgOiBab25lcyAo6rWs7JetKSAmYW1wOyBDb25kdWl0cyAo7Ya17IugIO2MjOydtO2UhCk8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IloxIiBkYXRhLXRvPSJDMSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7Ya17IugIO2XiOyaqSIgcG9pbnRzPSI0MzQuOTAwOTk5OTk5OTk5OTUsMjE3LjkgNTg5Ljg1MywyMTcuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQzEiIGRhdGEtdG89IloyIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLthrXsi6Ag7ZeI7JqpIiBwb2ludHM9Ijc0My44NTMsMjE3LjkgODk4LjgwNSwyMTcuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iSEFDS0VSIiBkYXRhLXRvPSJaMSIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iu2VtO2CuSDsi5zrj4QiIHBvaW50cz0iMTQ0LjYzMjk5OTk5OTk5OTk4LDIxNy45IDI5OS41ODUsMjE3LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJaMSIgZGF0YS10bz0iQzEiIGRhdGEtbGFiZWw9Iu2GteyLoCDtl4jsmqkiPgogIDxyZWN0IHg9IjQ3OC45MDA5OTk5OTk5OTk5NSIgeT0iMjAxLjkiIHdpZHRoPSI2Ni45NTIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MTIuMzc3IiB5PSIyMTcuMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPu2GteyLoCDtl4jsmqk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQzEiIGRhdGEtdG89IloyIiBkYXRhLWxhYmVsPSLthrXsi6Ag7ZeI7JqpIj4KICA8cmVjdCB4PSI3ODcuODUzIiB5PSIyMDEuOSIgd2lkdGg9IjY2Ljk1MiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjgyMS4zMjkiIHk9IjIxNy4wNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7Ya17IugIO2XiOyaqTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJIQUNLRVIiIGRhdGEtdG89IloxIiBkYXRhLWxhYmVsPSLtlbTtgrkg7Iuc64+EIj4KICA8cmVjdCB4PSIxODguNjMyOTk5OTk5OTk5OTgiIHk9IjIwMS45IiB3aWR0aD0iNjYuOTUyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjIyLjEwODk5OTk5OTk5OTk4IiB5PSIyMTcuMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPu2VtO2CuSDsi5zrj4Q8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IloxIiBkYXRhLWxhYmVsPSJab25lIDEK6rO17J6lIOygnOyWtOyLpCDwn5K7IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjI5OS41ODUiIHk9IjE5MSIgd2lkdGg9IjEzNS4zMTYiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjM2Ny4yNDMiIHk9IjIxNy45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIzNjcuMjQzIiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+Wm9uZSAxPC90c3Bhbj48dHNwYW4geD0iMzY3LjI0MyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+6rO17J6lIOygnOyWtOyLpCDwn5K7PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkMxIiBkYXRhLWxhYmVsPSJDb25kdWl0CuuztOyViCDtjIzsnbTtlIQg8J+UkiIgZGF0YS1zaGFwZT0iY2lyY2xlIj4KICA8Y2lyY2xlIGN4PSI2NjYuODUzIiBjeT0iMjE3LjkiIHI9Ijc3IiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjY2Ni44NTMiIHk9IjIxNy45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI2NjYuODUzIiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+Q29uZHVpdDwvdHNwYW4+PHRzcGFuIHg9IjY2Ni44NTMiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuuztOyViCDtjIzsnbTtlIQg8J+UkjwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJaMiIgZGF0YS1sYWJlbD0iWm9uZSAyCuuhnOu0hyDtjJQgLyBQTEMg8J+kliIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI4OTguODA1IiB5PSIxOTEiIHdpZHRoPSIxNDAuNTAzIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI5NjkuMDU2NDk5OTk5OTk5OSIgeT0iMjE3LjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9Ijk2OS4wNTY0OTk5OTk5OTk5IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+Wm9uZSAyPC90c3Bhbj48dHNwYW4geD0iOTY5LjA1NjQ5OTk5OTk5OTkiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuuhnOu0hyDtjJQgLyBQTEMg8J+kljwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJIQUNLRVIiIGRhdGEtbGFiZWw9Iu2VtOy7pCDwn6W3IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIxOTkuNDUiIHdpZHRoPSI4OC42MzMiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEwMC4zMTY0OTk5OTk5OTk5OSIgeT0iMjE3Ljg5OTk5OTk5OTk5OTk4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7tlbTsu6Qg8J+ltzwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSI2OC42MjYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI5MC4zMTMiIHk9IjEwMi40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Tm90ZTwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] ISA/IEC 62443의 핵심 보안 수준 체계(SL) 전격 해부 (3단 표)**

표준이 요구하는 \*\*방어력의 체급(Security Level 1\~4)\*\*이 해커의 어떤 수준을 막아내는지를 찌르는 것이 가장 중요합니다.

| **보안 등급 (Security Level)** | **막아내야 하는 해커(위협)의 수준**                                                                               | **공격자의 리소스 및 기술력**                              |
| :------------------------- | :--------------------------------------------------------------------------------------------------- | :---------------------------------------------- |
| **SL 1** *(기본 방어)*         | **'우연한 사고나 실수' 방어 수준.** 해킹 목적이 아닌 직원의 단순 실수나 감염된 USB로 인한 바이러스 확산을 막는 기초적인 단계.                        | 의도적인 공격이 아님. (비의도적 노출).                         |
| **SL 2** *(단순 해커 방어)*      | **'단순하고 제한적인 기술을 가진 해커' 방어.** 일반적인 피싱, 알려진 취약점을 이용하는 저숙련 해커의 침투를 차단함.                                | 낮은 수준의 리소스, 일반적인 해킹 툴 사용자.                      |
| **SL 3** *(전문 해커 방어)*      | **'정교한 기술을 가진 해커 그룹' 방어.** 특정 공장 시스템(SCADA)을 이해하고, 맞춤형 악성코드를 제작하여 침투하는 전문 해커를 차단함.                   | 보통 수준 이상의 리소스, 고도의 기술력을 갖춘 갱단.                  |
| **SL 4 🚨** *(최고 기밀 방어)*   | **'국가 지원을 받는 최정예 해커(APT)' 방어.** 스턱스넷(Stuxnet)처럼 원전이나 국가 기반 시설을 마비시키려는 막강한 배후를 둔 국가급 해커의 집요한 공격을 견뎌냄. | **막대한 국가적 예산과 끝없는 시간(수년)을 투자하는 최고 수준의 스텔스 공격.** |

#### **IV. \[결론/제언] IT와 OT의 융합(Convergence) 시대와 보안의 의무화**

* **(키워드 위주 2줄 마무리)** "과거 외부망과 단절(Air-gap)되어 안전하다고 믿었던 공장(OT) 환경이 4차 산업혁명으로 클라우드(IT)와 융합되면서, 거대한 보안 위협에 노출되었습니다. **ISA/IEC 62443은 더 이상 선택이 아닌 스마트 팩토리의 생존을 위한 필수 설계 헌법으로 자리 잡고 있습니다.**"
