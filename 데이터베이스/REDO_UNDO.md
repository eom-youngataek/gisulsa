### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (지속성을보장하는방법, WAL원칙) — 3~4줄
Ⅱ. REDO와UNDO의역할분담 (본론①, 도식 1개 필수)
Ⅲ. 장애복구시나리오, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

앞서다룬 \*\*"ACID의지속성(D)"\*\*은 \*\*"커밋된데이터는장애가나도사라지지않아야한다"\*\*는 약속이었습니다 — 하지만 \*\*"매번데이터를디스크에직접,즉시반영"\*\*하면 너무느립니다. 그래서 DB는 \*\*"실제데이터변경전에, 먼저로그부터기록"\*\*하는 \*\*WAL(Write-AheadLogging)\*\*전략을 쓰며, 이때 **REDO로그와UNDO로그**가 각각다른역할을맡습니다.

### Ⅱ. REDO와UNDO의역할분담

| 로그         | 역할                | 기록내용              |
| :--------- | :---------------- | :---------------- |
| **REDO로그** | **커밋된변경을 재실행**해복구 | 변경 **후(After)값**  |
| **UNDO로그** | **커밋안된변경을 되돌려**복구 | 변경 **전(Before)값** |

→ 암기: **"REDO는'이미확정된걸 다시해라',UNDO는'아직확정안된걸 되돌려라'"** — 앞서다룬 \*\*"ACID의원자성(A)"\*\*이 \*\*"전부하거나전부안하거나"\*\*였는데, REDO/UNDO가 바로 그 **원자성을장애상황에서도지켜내는 구체적도구**입니다.

### 도식화 제안

```
[정상흐름]
①UPDATE 실행 → 먼저 UNDO로그(변경전값)+REDO로그(변경후값) 기록
②로그를 디스크에먼저저장(WAL원칙)
③실제데이터페이지 변경(메모리,나중에디스크반영)
④COMMIT → "이트랜잭션은완료됨"표시
```

### Ⅲ. 장애복구시나리오 — 핵심 배점

**함정 방지: "로그로복구한다"고만답하면절반. 장애발생시점에 커밋됐는지여부에따라 REDO와UNDO가 "정확히누구에게적용되는지" 구체적으로보여줘야완성됩니다.**

**장애발생상황**: 갑자기전원이꺼져서, **메모리의변경사항이디스크에완전히반영안된채** 시스템이재시작됨

| 단계          | 처리내용                                                          |
| :---------- | :------------------------------------------------------------ |
| **①분석단계**   | 로그를훑어 \*\*"어떤트랜잭션이커밋됐는지,안됐는지"\*\*목록작성                         |
| **②REDO단계** | **커밋된트랜잭션전부**를 REDO로그로 **다시실행**(디스크에못반영된변경을 완전히재현)            |
| **③UNDO단계** | \*\*커밋안된트랜잭션(진행중이던것)\*\*을 UNDO로그로 **되돌림**(장애당시 반쯍처리된상태를깨끗이제거) |

→ 암기: **"커밋된건다시해서 완성시키고,안커밋된건되돌려서지운다"** — 이순서(REDO **먼저**,UNDO **나중**)가 중요합니다: **REDO를먼저다적용해서 "장애직전의완전한상태"를만든후**, 그중 **커밋안됐던것만골라UNDO**합니다.

### 도식화 제안

```
[장애복구시나리오]
트랜잭션A: UPDATE+COMMIT (완료됨,하지만디스크반영전장애)
트랜잭션B: UPDATE만 (COMMIT전에장애발생)

재시작후:
①분석: "A는커밋됨,B는커밋안됨" 확인
②REDO: A의변경사항 재실행(A를 완전히복원)
        (B도일단로그대로재현해서 "장애당시상태"로만듦)
③UNDO: B는커밋안됐으므로 → 되돌림(B의변경분제거)

최종결과: A는완전히반영됨(지속성보장), B는완전히사라짐(원자성보장)
```

**체크포인트**(효율화): 로그가무한히쌓이면 복구시간이길어지므로, 주기적으로 \*\*"이시점까지는디스크에완전히반영됐다"\*\*는 **체크포인트**를 남겨, **복구시그이후로그만분석**하면됩니다 — 앞서다룬 \*\*"백업의증분/차등백업"\*\*과 유사하게, \*\*"전체를다시할필요없이,필요한부분만처리"\*\*하는 효율화입니다.

### Ⅳ. 결론

REDO/UNDO는 **"장애가나도, 커밋된트랜잭션은완전히살리고(REDO), 커밋안된트랜잭션은흔적도없이지우는(UNDO)"** 메커니즘으로, 앞서다룬 \*\*ACID의원자성(전부or전무)과지속성(커밋된건영원히보존)\*\*을 **실제장애상황에서구현하는 핵심기술**입니다 — 이는 앞서다룬 \*\*"WAL(먼저로그를쓰고,나중에실제데이터반영)"\*\*원칙이 있어야만 가능하며, 오늘하루다룬 데이터모델링·트랜잭션시리즈전체(정규화→무결성→ACID→격리수준→병행제어→REDO/UNDO)가, **"데이터를올바르게설계하는것에서, 동시에안전하게하는것,그리고장애에도살아남게하는것까지"** 완결된 데이터베이스이론의 전체여정을 마무리합니다.리합니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "데이터베이스가 정전이나 장애로 뻗었을 때, 트랜잭션의 생사를 결정짓는 두 가지 마법의 복구 주문이다. 이 주문은 무조건 '로그(Log) 파일'이라는 장부를 보고 외운다. 첫째, **UNDO (실행 취소)**. 트랜잭션이 아직 완료(Commit) 도장을 안 찍었는데 시스템이 뻗었거나 사용자가 롤백(Rollback)을 외친 경우다. 로그 장부에 적힌 '과거 데이터(Before Image)'를 꺼내와서 하던 작업을 다 취소하고 원상 복구(원자성 보장)시킨다. 둘째, **REDO (재실행)**. 이미 완료(Commit) 도장을 꽝 찍었는데, 하드디스크에 물리적으로 기록되기 0.1초 전에 정전이 난 경우다. 억울하지 않게 로그 장부에 적힌 '새로운 데이터(After Image)'를 꺼내와서 하드디스크에 다시 쾅쾅 덮어써서 끝까지 저장(영속성 보장)시켜 준다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] DB 장애 발생 시 최후의 보루, 회복(Recovery) 기법 개요**

* **정의:** 트랜잭션 수행 중 시스템 크래시(정전, 에러)가 발생했을 때, 데이터베이스를 장애 발생 이전의 일관된(Consistent) 상태로 복원하기 위한 핵심 연산.
* **전제 조건 (WAL 원칙):** REDO와 UNDO가 동작하려면, 실제 데이터 파일(디스크)에 값을 쓰기 전에 **반드시 로그(Log) 파일에 변경 내역을 먼저 기록해야 한다는 WAL(Write-Ahead Logging) 원칙이 무조건 지켜져야 함.**

#### **II. \[본론 1] (극단적 단순화 버전) Commit 도장 여부에 따른 생사 갈림길**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIuODkgNTY0LjU0NyIgd2lkdGg9IjUxMi44OSIgaGVpZ2h0PSI1NjQuNTQ3IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfX19fUkVET1VORE9fIiBkYXRhLWxhYmVsPSLsi5zsiqTthZwg7J6l7JWgIOuwnOyDnSDsi5wgUkVETy9VTkRPIOu2hOq4sCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNDMyLjg5IiBoZWlnaHQ9IjQ4NC41NDciIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI0MzIuODkiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7si5zsiqTthZwg7J6l7JWgIOuwnOyDnSDsi5wgUkVETy9VTkRPIOu2hOq4sDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQ1JBU0giIGRhdGEtdG89IkNISyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyNjIuMDAyNSwxMjAuOSAyNjIuMDAyNDk5OTk5OTk5OTQsMTY4LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkNISyIgZGF0YS10bz0iUiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iWWVzICjrj4TsnqUg7LCN7J2MKSIgcG9pbnRzPSIyMzYuNTYxMzMzMzMzMzMzMywyOTYuMTA1ODMzMzMzMzMzMzUgMjM2LjU2MTMzMzMzMzMzMzMyLDMzMy41NDcgMTU0Ljc3OTk5OTk5OTk5OTk3LDMzMy41NDcgMTU0Ljc3OTk5OTk5OTk5OTk3LDQzNy44NDcwMDAwMDAwMDAwNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQ0hLIiBkYXRhLXRvPSJVIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSJObyAo64+E7J6lIOyViCDssI3snYwpIiBwb2ludHM9IjI4Ny40NDM2NjY2NjY2NjY2LDI5Ni4xMDU4MzMzMzMzMzMzNSAyODcuNDQzNjY2NjY2NjY2NiwzMzMuNTQ3IDM2OS4yMjUsMzMzLjU0NyAzNjkuMjI1LDQzNy44NDcwMDAwMDAwMDAwNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJDSEsiIGRhdGEtdG89IlIiIGRhdGEtbGFiZWw9IlllcyAo64+E7J6lIOywjeydjCkiPgogIDxyZWN0IHg9IjEwNy43Nzk5OTk5OTk5OTk5NyIgeT0iMzY0LjU0NyIgd2lkdGg9IjkzLjY4MjAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTU0LjYyMDk5OTk5OTk5OTk4IiB5PSIzNzkuNjk3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5ZZXMgKOuPhOyepSDssI3snYwpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkNISyIgZGF0YS10bz0iVSIgZGF0YS1sYWJlbD0iTm8gKOuPhOyepSDslYgg7LCN7J2MKSI+CiAgPHJlY3QgeD0iMzE4LjIyNSIgeT0iMzY0LjU0NyIgd2lkdGg9IjEwMS40MDQwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjM2OC45MjciIHk9IjM3OS42OTciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPk5vICjrj4TsnqUg7JWIIOywjeydjCk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkNSQVNIIiBkYXRhLWxhYmVsPSLwn5KlIOy+hSEg7Iuc7Iqk7YWcIOygleyghC/snqXslaAg67Cc7IOdIPCfkqUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTQzLjIxNTUiIHk9Ijg0IiB3aWR0aD0iMjM3LjU3Mzk5OTk5OTk5OTk4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjI2Mi4wMDI1IiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPvCfkqUg7L6FISDsi5zsiqTthZwg7KCV7KCEL+yepeyVoCDrsJzsg50g8J+SpTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ0hLIiBkYXRhLWxhYmVsPSLtirjrnpzsnq3shZjsnbQKQ29tbWl0IOuPhOyepeydhArssI3sl4jripTqsIA/IiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjI2Mi4wMDI0OTk5OTk5OTk5NCwxNjguOSAzMzguMzI1OTk5OTk5OTk5OSwyNDUuMjIzNSAyNjIuMDAyNDk5OTk5OTk5OTQsMzIxLjU0NyAxODUuNjc4OTk5OTk5OTk5OTUsMjQ1LjIyMzUiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMjYyLjAwMjQ5OTk5OTk5OTk0IiB5PSIyNDUuMjIzNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMjYyLjAwMjQ5OTk5OTk5OTk0IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+7Yq4656c7J6t7IWY7J20PC90c3Bhbj48dHNwYW4geD0iMjYyLjAwMjQ5OTk5OTk5OTk0IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5Db21taXQg64+E7J6l7J2EPC90c3Bhbj48dHNwYW4geD0iMjYyLjAwMjQ5OTk5OTk5OTk0IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7ssI3sl4jripTqsIA/PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlIiIGRhdGEtbGFiZWw9IuKcqCBSRURPIOyXsOyCsCDrsJzrj5kg4pyoCuyDiOuhnOyatCDqsJLsnLzroZwK7ZWY65Oc65SU7Iqk7YGs7JeQIOuLpOyLnCDquLDroZ0hIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI0MzcuODQ3MDAwMDAwMDAwMDQiIHdpZHRoPSIxOTcuNTU5OTk5OTk5OTk5OTciIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNTQuNzc5OTk5OTk5OTk5OTciIHk9IjQ3My4xOTcwMDAwMDAwMDAwNiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTU0Ljc3OTk5OTk5OTk5OTk3IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+4pyoIFJFRE8g7Jew7IKwIOuwnOuPmSDinKg8L3RzcGFuPjx0c3BhbiB4PSIxNTQuNzc5OTk5OTk5OTk5OTciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyDiOuhnOyatCDqsJLsnLzroZw8L3RzcGFuPjx0c3BhbiB4PSIxNTQuNzc5OTk5OTk5OTk5OTciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPu2VmOuTnOuUlOyKpO2BrOyXkCDri6Tsi5wg6riw66GdITwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJVIiBkYXRhLWxhYmVsPSLinKggVU5ETyDsl7DsgrAg67Cc64+ZIOKcqArsmJvrgqAg6rCS7Jy866GcCuyLuSDri6Qg66Gk67CxICjst6jshowpISIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyODEuNTYiIHk9IjQzNy44NDcwMDAwMDAwMDAwNCIgd2lkdGg9IjE3NS4zMjk5OTk5OTk5OTk5OCIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjM2OS4yMjUiIHk9IjQ3My4xOTcwMDAwMDAwMDAwNiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMzY5LjIyNSIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPuKcqCBVTkRPIOyXsOyCsCDrsJzrj5kg4pyoPC90c3Bhbj48dHNwYW4geD0iMzY5LjIyNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7Jib64KgIOqwkuycvOuhnDwvdHNwYW4+PHRzcGFuIHg9IjM2OS4yMjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyLuSDri6Qg66Gk67CxICjst6jshowpITwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] UNDO vs REDO 핵심 복구 메커니즘 전격 대조 (3단 표)**

이 토픽은 두 연산이 '어떤 조건'에서 발동하며, 로그에 적힌 '어떤 데이터(Before/After)'를 사용하는지를 명확히 대조하는 것이 완벽한 득점 포인트입니다.

| **핵심 척도**                | **⏪ UNDO (실행 취소 / Rollback) 🚨**                                                                               | **⏩ REDO (재실행 / Rollforward) 🚨**                                                                             |
| :----------------------- | :------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| **발동 조건 (Commit 여부) 🚨** | **'도장 안 찍었는데 죽었을 때'.** 트랜잭션이 시작되었으나 아직 **Commit(완료)을 수행하지 못한 상태**에서 장애가 발생했을 때 발동함.                            | **'도장 찍었는데 죽었을 때 💯'.** **Commit을 이미 완료**했으나, 버퍼 메모리에만 있고 실제 디스크에 써지기(Flush) 전에 장애가 발생했을 때 발동함.               |
| **복구 원리 (Log 이미지) 🚨**   | **\[Before Image 사용 💯]** 로그(Log) 파일에 기록되어 있는 \*\*'변경 이전의 옛날 값(Before Image)'\*\*을 디스크에 덮어써서, 하던 작업을 취소하고 롤백함. | **\[After Image 사용 💯]** 로그(Log) 파일에 기록되어 있는 \*\*'변경 이후의 새로운 값(After Image)'\*\*을 디스크에 다시 덮어써서(재실행) 확실히 반영시킴. |
| **ACID 보장 💯**           | **\[원자성 (Atomicity)]** 모 아니면 도. 끝까지 못 할 거면 아예 시작조차 안 한 상태로 만들어 버림.                                             | **\[영속성 (Durability)]** 한 번 완료(Commit)된 트랜잭션의 결과는 정전이 나도 영원히 보존되어야 함.                                         |

#### **IV. \[결론/제언] 재해 복구(DR) 시점인 체크포인트(Checkpoint)와의 결합**

* **(키워드 위주 2줄 마무리)** "장애 발생 시 로그 파일의 처음부터 끝까지 모두 REDO/UNDO를 수행하면 복구 시간이 무한정 길어집니다. 따라서 주기적으로 메모리의 데이터를 디스크에 강제 저장하고 로그에 표시를 남기는 **'체크포인트(Checkpoint, 검사점)' 기법과 결합해야만, 장애 발생 시 체크포인트 이후의 로그만 뒤져서 복구 타임(RTO)을 극적으로 단축할 수 있습니다.**"
