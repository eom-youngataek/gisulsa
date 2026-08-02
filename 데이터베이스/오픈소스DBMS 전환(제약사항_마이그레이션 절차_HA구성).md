### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (전환배경, 국내정책흐름) — 3~4줄
Ⅱ. 제약사항3대유형 (본론①, 도식 1개 필수)
Ⅲ. 마이그레이션절차및HA구성, 핵심 배점
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서다룬ACID,격리수준,REDO/UNDO가 '오라클(상용DB)에서든,PostgreSQL(오픈소스)에서든' 똑같이지켜져야하는데, 실제전환과정에서는 '구현방식의미세한차이'가 큰장애물이된다 — 카카오뱅크가 EDBPostgres로전환하며 TCO를대폭절감했지만, 그과정이간단하지않았다"\*\*는 한줄로시작하면, 왜 제약사항부터 살펴봐야하는지 드러납니다.

### Ⅱ. 제약사항3대유형

| 유형            | 내용                                                                                               |
| :------------ | :----------------------------------------------------------------------------------------------- |
| **호환성제약**     | 오라클 \*\*전용문법(PL/SQL,계층쿼리등)\*\*이 오픈소스DB에서 **100%지원안됨**— EPAS12는 **스키마호환성90%이상**이지만 나머지10%는 수동전환필요 |
| **라이선스구조차이**  | 오라클은 **CPU코어수기준추가라이선스**필요(확장시비용급증) — 오픈소스는 **필요한만큼서버추가**가능(라이선스제약없음)                             |
| **성능/HA기능격차** | 상용DB의 **네이티브고가용성기능**을, 오픈소스는 \*\*별도도구(AgensHAManager등)\*\*로 보완해야하는경우多                            |

→ 암기: **"문법이안맞고,라이선스구조가다르고,고가용성기능을따로덧붙여야한다"** — 앞서다룬 \*\*"EPAS12(오라클호환PostgreSQL)"\*\*가 시장에서인기있는이유가, 바로이 \*\*"호환성제약을최소화"\*\*하기때문입니다.

### 도식화 제안

```
[제약사항 3대유형]
호환성: 오라클PL/SQL → PostgreSQL(90%호환,10%수동전환)
라이선스: CPU코어당비용(오라클) → 서버추가시비용(오픈소스,유연함)
HA기능: 네이티브지원(상용) → 별도도구로보완(오픈소스,Agens HA Manager등)
```

### Ⅲ. 마이그레이션절차 및 HA구성 — 핵심 배점

**함정 방지: "옮기면끝"이라고답하면절반. 실제단계별절차와, 앞서다룬REDO/UNDO·ACID가 HA구성에서어떻게재현되는지보여줘야완성됩니다.**

**마이그레이션 절차**

| 단계               | 내용                                                    |
| :--------------- | :---------------------------------------------------- |
| **①사전분석**        | 기존DB의 **스키마,저장프로시저,쿼리패턴**분석— **호환성갭(앞서다룬10%)** 식별     |
| **②스키마·데이터전환**   | **마이그레이션툴킷**(EDB등제공)으로 **자동전환**,수동수정필요분처리             |
| **③애플리케이션수정**    | 호환안되는 **SQL문법,드라이버**교체                                |
| **④병행운영·검증**(핵심) | 기존DB와신규DB를 **동시운영**하며 **결과값교차검증**(앞서다룬"CTEM의검증단계"와유사) |
| **⑤전환·안정화**      | 실제전환후 **일정기간모니터링**(앞서다룬맥스게이지같은 DBPM도구활용)              |

→ 암기: **"분석하고,자동전환툴로옮기고,앱을고치고,병행운영으로검증하고,최종전환후지켜본다"** — \*\*"병행운영·검증"\*\*단계가 특히중요합니다: 앞서다룬 \*\*"타임스탬프기반낙관적잠금"\*\*의 **"일단하고나중에확인"** 철학처럼, \*\*"전환도 한번에스위치하지않고 충분히검증한뒤 최종전환"\*\*하는 것이 안전합니다.

**HA(고가용성)구성**

| 구성                      | 내용                                                            |
| :---------------------- | :------------------------------------------------------------ |
| **Primary-Secondary복제** | Primary(쓰기전용)의데이터를 **Secondary(읽기전용)에실시간복제** — 부하분산+장애대비 동시달성 |
| **자동장애전환**(Failover)    | Primary장애시 **Secondary가자동으로Primary역할승계**,다운타임최소화              |
| **부하분산**                | 일반조회는 **Secondary로분산**해 Primary부담경감(앞서다룬"WFQ의가중치분산"과유사원리)     |

→ 앞서다룬 \*\*"REDO/UNDO"\*\*가 \*\*"단일DB의장애복구"\*\*를 다뤘다면, HA구성의 \*\*"자동장애전환"\*\*은 \*\*"복제본이있어야만가능한 더큰스케일의장애대응"\*\*이며, 앞서다룬 \*\*"분산DB의장애투명성"\*\*이 바로 이 **Primary-Secondary구조**를 통해 실현됩니다.

### 도식화 제안

```
[HA 구성 - Primary-Secondary]
[Primary서버] ──실시간복제──→ [Secondary서버(읽기전용)]
  ↓쓰기트래픽                    ↓읽기트래픽(부하분산)
     
[Primary장애발생시]
[Primary서버] ✗ 장애
     ↓ 자동감지
[Secondary서버] → Primary로자동승격(Failover)
     ↓
서비스계속(다운타임최소화, 앞서다룬장애투명성구현)
```

**국내정책현황**(2026년): 행안부는 **2026년까지70%이상공공시스템클라우드네이티브전환**목표로, **2025년430억원,2026년100억원(컨설팅)** 투입중이며, **국가정보자원관리원대구센터**는 **큐브리드,알티베이스,골디락스,마리아DB,PostgreSQL** 5대오픈소스DB를 **우선검토대상**으로 지정했습니다.

### Ⅳ. 결론

오픈소스DBMS전환은 **"앞서다룬ACID,격리수준,REDO/UNDO같은이론이, 실제로는오라클과오픈소스DB사이의구현방식차이(제약사항)때문에 신중한마이그레이션절차와HA구성이필요한"** 실무프로젝트입니다 — 카카오뱅크의 \*\*EPAS12전환(TCO대폭절감)\*\*사례가보여주듯, \*\*"호환성90%이상"\*\*이라도 **나머지10%와HA구성**에 세심한주의가필요하며, 2026년현재 한국공공부문은 **대구센터의5대오픈소스DB**를 중심으로 **클라우드네이티브전환**을 가속화하고있습니다 — 이로써 오늘하루다룬 방대한데이터베이스이론시리즈(정규화→ACID→REDO/UNDO→분산DB→오픈소스전환)전체가, \*\*"이론에서출발해, 실제한국의공공·금융시장에서 지금이순간구현되고있는 현재진행형실무"\*\*로 완결됩니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "수십억 원의 오라클 라이선스와 벤더 종속성(Lock-in)에서 탈출해 MySQL, PostgreSQL 같은 오픈소스로 이사 가는 전략이다. 첫째, **제약사항**. 완벽한 1:1 이사는 불가능하다. 오라클만의 강력한 PL/SQL 프로시저, 힌트 구문, 엑티브-엑티브 클러스터링(RAC)은 오픈소스에 없거나 성능이 떨어져 애플리케이션 코드를 다 뜯어고쳐야 한다. 둘째, **전환 절차**. 뼈대(스키마)와 함수를 먼저 자동 툴로 변환하고, 본 데이터는 CDC(변경 데이터 캡처)를 통해 무중단으로 밀어 넣으며, 반드시 쿼리 튜닝을 거쳐 컷오버(Cut-over)한다. 셋째, **HA(고가용성) 구성**. 오라클처럼 디스크를 공유하는 RAC 대신, 마스터(쓰기)와 슬레이브(읽기) 서버를 물리적으로 쪼개고 실시간 '복제(Replication)'를 걸어, 장애 시 슬레이브를 마스터로 즉각 승격(Failover)시키는 Active-Standby 구조를 쓴다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 벤더 종속성 탈피와 클라우드 네이티브, 오픈소스 DBMS 전환 개요**

* **전환 목적:** 막대한 라이선스/유지보수 비용(TCO) 절감, 벤더 락인(Lock-in) 탈피, 클라우드 환경(MSA)에 적합한 가볍고 유연한 분산 데이터베이스 환경 구축.
* **핵심 과제:** 이기종 DB 간의 아키텍처 사상 차이로 인해 발생하는 '비즈니스 로직(PL/SQL) 재작성' 및 '무중단 데이터 이관(Zero Downtime)'의 리스크 최소화.

#### **II. \[본론 1] (극단적 단순화 버전) 무중단 컷오버(Cut-over) 마이그레이션 파이프라인**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDI5LjQ1OCAyNzAuOCIgd2lkdGg9IjEwMjkuNDU4IiBoZWlnaHQ9IjI3MC44IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfREJfX18iIGRhdGEtbGFiZWw9IuyYpO2UiOyGjOyKpCBEQiDrrLTspJHri6gg66eI7J206re466CI7J207IWYKOyghO2ZmCkg7Z2Q66aEIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI5NDkuNDU4IiBoZWlnaHQ9IjE5MC44IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iOTQ5LjQ1OCIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPuyYpO2UiOyGjOyKpCBEQiDrrLTspJHri6gg66eI7J206re466CI7J207IWYKOyghO2ZmCkg7Z2Q66aEPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBUyIgZGF0YS10bz0iVE8iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjEuIOyKpO2CpOuniC/tlajsiJgKMeywqCDrs4DtmZgiIHBvaW50cz0iMTQyLjQxLDE2Ni41NSAxNTQuNDEsMTY2LjU1IDE1NC40MSwxOTcuMiAzNDguMDg2LDE5Ny4yIDM0OC4wODYsMTY2LjU1IDM4NC4wODYsMTY2LjU1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBUyIgZGF0YS10bz0iVE8iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjIuIOy0iOq4sCDrjbDsnbTthLAKRnVsbCBMb2FkIiBwb2ludHM9IjE0Mi40MSwxNDkuNiAzODQuMDg2LDE0OS42IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBUyIgZGF0YS10bz0iVE8iIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIzLiDinKgg7ZW17IusOiBDREMg6riw67CYIOKcqArsi6Tsi5zqsIQg67OA6rK9IOuNsOydtO2EsCDrj5nquLDtmZQiIHBvaW50cz0iMTQyLjQxLDEzMi42NSAxNTQuNDEsMTMyLjY1IDE1NC40MSwxMDIgMzQ4LjA4NiwxMDIgMzQ4LjA4NiwxMzIuNjUgMzg0LjA4NiwxMzIuNjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVE8iIGRhdGEtdG89IkNVVCIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjQuIOygle2VqeyEsSDqsoDspp0g67CPCuyVoO2UjOumrOy8gOydtOyFmCDtipzri50g7JmE66OMIO2bhCIgcG9pbnRzPSI1MDAuMTM1OTk5OTk5OTk5OTcsMTQ5LjYgNzQxLjgxMiwxNDkuNjAwMDAwMDAwMDAwMDIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJBUyIgZGF0YS10bz0iVE8iIGRhdGEtbGFiZWw9IjEuIOyKpO2CpOuniC/tlajsiJgKMeywqCDrs4DtmZgiPgogIDxyZWN0IHg9IjIxOS45NzEiIHk9IjE3NC4yIiB3aWR0aD0iODYuNTU0IiBoZWlnaHQ9IjQ0LjYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjYzLjI0OCIgeT0iMTk2LjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSIyNjMuMjQ4IiBkeT0iLTMuMzAwMDAwMDAwMDAwMDAwNyI+MS4g7Iqk7YKk66eIL+2VqOyImDwvdHNwYW4+PHRzcGFuIHg9IjI2My4yNDgiIGR5PSIxNC4zIj4x7LCoIOuzgO2ZmDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkFTIiBkYXRhLXRvPSJUTyIgZGF0YS1sYWJlbD0iMi4g7LSI6riwIOuNsOydtO2EsApGdWxsIExvYWQiPgogIDxyZWN0IHg9IjIxOC43ODMwMDAwMDAwMDAwNCIgeT0iMTI2LjU5OTk5OTk5OTk5OTk4IiB3aWR0aD0iODguOTMiIGhlaWdodD0iNDQuNiIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyNjMuMjQ4MDAwMDAwMDAwMDUiIHk9IjE0OC44OTk5OTk5OTk5OTk5OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSI+PHRzcGFuIHg9IjI2My4yNDgwMDAwMDAwMDAwNSIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPjIuIOy0iOq4sCDrjbDsnbTthLA8L3RzcGFuPjx0c3BhbiB4PSIyNjMuMjQ4MDAwMDAwMDAwMDUiIGR5PSIxNC4zIj5GdWxsIExvYWQ8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJBUyIgZGF0YS10bz0iVE8iIGRhdGEtbGFiZWw9IjMuIOKcqCDtlbXsi6w6IENEQyDquLDrsJgg4pyoCuyLpOyLnOqwhCDrs4Dqsr0g642w7J207YSwIOuPmeq4sO2ZlCI+CiAgPHJlY3QgeD0iMTg2LjQxMDAwMDAwMDAwMDAzIiB5PSI3OSIgd2lkdGg9IjE1My42NzYwMDAwMDAwMDAwNCIgaGVpZ2h0PSI0NC42IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjI2My4yNDgwMDAwMDAwMDAwNSIgeT0iMTAxLjMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSIyNjMuMjQ4MDAwMDAwMDAwMDUiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij4zLiDinKgg7ZW17IusOiBDREMg6riw67CYIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjI2My4yNDgwMDAwMDAwMDAwNSIgZHk9IjE0LjMiPuyLpOyLnOqwhCDrs4Dqsr0g642w7J207YSwIOuPmeq4sO2ZlDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlRPIiBkYXRhLXRvPSJDVVQiIGRhdGEtbGFiZWw9IjQuIOygle2VqeyEsSDqsoDspp0g67CPCuyVoO2UjOumrOy8gOydtOyFmCDtipzri50g7JmE66OMIO2bhCI+CiAgPHJlY3QgeD0iNTQ0LjEzNiIgeT0iMTI2LjU5OTk5OTk5OTk5OTk4IiB3aWR0aD0iMTUzLjY3NjAwMDAwMDAwMDA0IiBoZWlnaHQ9IjQ0LjYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjIwLjk3Mzk5OTk5OTk5OTkiIHk9IjE0OC44OTk5OTk5OTk5OTk5OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSI+PHRzcGFuIHg9IjYyMC45NzM5OTk5OTk5OTk5IiBkeT0iLTMuMzAwMDAwMDAwMDAwMDAwNyI+NC4g7KCV7ZWp7ISxIOqygOymnSDrsI88L3RzcGFuPjx0c3BhbiB4PSI2MjAuOTczOTk5OTk5OTk5OSIgZHk9IjE0LjMiPuyVoO2UjOumrOy8gOydtOyFmCDtipzri50g7JmE66OMIO2bhDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBUyIgZGF0YS1sYWJlbD0iQXMtSXMK7Jik65287YG0IiBkYXRhLXNoYXBlPSJjeWxpbmRlciI+CiAgPHJlY3QgeD0iNTYiIHk9IjEyMi42OTk5OTk5OTk5OTk5OSIgd2lkdGg9Ijg2LjQxIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAxIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9Im5vbmUiIC8+CiAgPGxpbmUgeDE9IjU2IiB5MT0iMTIyLjY5OTk5OTk5OTk5OTk5IiB4Mj0iNTYiIHkyPSIxNzYuNSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8bGluZSB4MT0iMTQyLjQxIiB5MT0iMTIyLjY5OTk5OTk5OTk5OTk5IiB4Mj0iMTQyLjQxIiB5Mj0iMTc2LjUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPGVsbGlwc2UgY3g9Ijk5LjIwNSIgY3k9IjE3Ni41IiByeD0iNDMuMjA1IiByeT0iNyIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8ZWxsaXBzZSBjeD0iOTkuMjA1IiBjeT0iMTIyLjY5OTk5OTk5OTk5OTk5IiByeD0iNDMuMjA1IiByeT0iNyIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI5OS4yMDUiIHk9IjE0OS42IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI5OS4yMDUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5Bcy1JczwvdHNwYW4+PHRzcGFuIHg9Ijk5LjIwNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7Jik65287YG0PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlRPIiBkYXRhLWxhYmVsPSJUby1CZQpQb3N0Z3JlU1FMIiBkYXRhLXNoYXBlPSJjeWxpbmRlciI+CiAgPHJlY3QgeD0iMzg0LjA4NiIgeT0iMTIyLjY5OTk5OTk5OTk5OTk5IiB3aWR0aD0iMTE2LjA0OTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAxIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9Im5vbmUiIC8+CiAgPGxpbmUgeDE9IjM4NC4wODYiIHkxPSIxMjIuNjk5OTk5OTk5OTk5OTkiIHgyPSIzODQuMDg2IiB5Mj0iMTc2LjUiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPGxpbmUgeDE9IjUwMC4xMzU5OTk5OTk5OTk5NyIgeTE9IjEyMi42OTk5OTk5OTk5OTk5OSIgeDI9IjUwMC4xMzU5OTk5OTk5OTk5NyIgeTI9IjE3Ni41IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDxlbGxpcHNlIGN4PSI0NDIuMTExIiBjeT0iMTc2LjUiIHJ4PSI1OC4wMjQ5OTk5OTk5OTk5OSIgcnk9IjciIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPGVsbGlwc2UgY3g9IjQ0Mi4xMTEiIGN5PSIxMjIuNjk5OTk5OTk5OTk5OTkiIHJ4PSI1OC4wMjQ5OTk5OTk5OTk5OSIgcnk9IjciIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNDQyLjExMSIgeT0iMTQ5LjYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjQ0Mi4xMTEiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5Uby1CZTwvdHNwYW4+PHRzcGFuIHg9IjQ0Mi4xMTEiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPlBvc3RncmVTUUw8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ1VUIiBkYXRhLWxhYmVsPSI1LiDsu7fsmKTrsoQg8J+agArsmKTrnbztgbQg7Iqk7JyE7LmYIOuBhOqzoCDsmYTsoIQg7KCE7ZmYISIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3NDEuODEyIiB5PSIxMjIuNyIgd2lkdGg9IjIzMS42NDYiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iODU3LjYzNSIgeT0iMTQ5LjYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9Ijg1Ny42MzUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj41LiDsu7fsmKTrsoQg8J+agDwvdHNwYW4+PHRzcGFuIHg9Ijg1Ny42MzUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyYpOudvO2BtCDsiqTsnITsuZgg64GE6rOgIOyZhOyghCDsoITtmZghPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 오픈소스 DBMS 전환 시 3대 핵심 고려 전략 전격 해부 (3단 표)**

| **핵심 척도**           | **⚠️ 오라클(As-Is)의 종속성 한계**                                                                        | **🚀 오픈소스(To-Be) 전환 및 구성 전략 🚨**                                                                                                                              |
| :------------------ | :----------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **제약사항 (비호환성)**     | **'특화 로직의 족쇄'.** 수십 년간 오라클에 최적화된 PL/SQL, 계층형 쿼리(CONNECT BY), 아우터 조인(+), 옵티마이저 힌트 등은 타 DB에서 안 먹힘. | **'애플리케이션 계층으로 로직 이관 💯'.** 자동 변환 툴(AWS SCT 등)로 문법을 변환하되, 복잡한 프로시저는 DB에 남기지 않고 **Java/Spring 백엔드 비즈니스 로직으로 뜯어고쳐 올림.**                                         |
| **전환 절차 (무중단)**     | DB 스위칭 시 발생하는 다운타임(수 시간\~며칠)으로 인해 글로벌 24시간 서비스 불가능.                                              | **'CDC(변경 데이터 캡처) 기반 무중단 이관 💯'.** 초기 적재(Full) 후, 전환 기간 동안 발생하는 모든 실시간 트랜잭션을 **CDC 솔루션으로 캡처해 타겟 DB에 끊임없이 복제(Replication)하여 동기화함.**                            |
| **HA 구성 (고가용성) 🚨** | **'공유 스토리지 (Oracle RAC)'.** 모든 노드가 활성화되어(Active-Active) 디스크 하나를 쳐다보는 극강의 고가용성 제공.                | **'복제 기반 Active-Standby 💯'.** 오픈소스는 완벽한 RAC가 불가능함. 따라서 마스터(쓰기)-슬레이브(읽기)로 역할을 쪼개고 실시간 복제를 건 뒤, MHA/Patroni 등을 써서 **장애 시 슬레이브를 마스터로 쳐올리는(Failover) 클러스터링 적용.** |

#### **IV. \[결론/제언] Polyglot Persistence(다국어 영속성) 시대의 분산 DB 아키텍처**

* **(키워드 위주 2줄 마무리)** "과거처럼 오라클 하나에 모든 업무를 쑤셔 넣던 시대는 끝났습니다. 이제는 오픈소스로 전환하면서, 관계형 데이터는 PostgreSQL, 비정형 데이터는 MongoDB, 캐시는 Redis 등 **데이터의 특성에 맞게 여러 오픈소스 DB를 골라 쓰는 'Polyglot Persistence' 아키텍처 구현이 MSA 환경의 필수 과제입니다.**"
