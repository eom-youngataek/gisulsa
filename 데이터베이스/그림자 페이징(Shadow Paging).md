### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (REDO/UNDO와의근본적차이) — 3~4줄
Ⅱ. 동작원리 - 페이지테이블의이중화 (본론①, 도식 1개 필수)
Ⅲ. 원자적전환및장단점, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

앞서다룬 **REDO/UNDO**는 \*\*"로그를남기고, 문제생기면로그로되돌리거나재실행"\*\*하는 방식이었습니다 — 그림자페이징은 **로그자체가필요없습니다**: \*\*"원본페이지는절대건드리지않고, 수정할내용을새페이지(그림자)에써서, 다완성되면 포인터를한번에바꿔치기"\*\*하는 방식입니다.

### Ⅱ. 동작원리 — 페이지테이블의이중화

| 개념            | 내용                                                         |
| :------------ | :--------------------------------------------------------- |
| **현재페이지테이블**  | 트랜잭션동안 **작업중인새페이지들을가리킴**                                   |
| **그림자페이지테이블** | **트랜잭션시작시점의 원본페이지들을그대로가리킴**(수정안됨)                          |
| **수정방식**      | 페이지수정시, **원본은그대로두고 새로운위치에복사본을만들어수정**,현재페이지테이블만 그새위치를가리키게변경 |

→ 암기: **"원본은안건드리고, 수정은전부복사본에서, 두종류의지도(테이블)로원본과작업본을각각가리킨다"** — 앞서다룬 \*\*"디스크이미징(원본불가침원칙)"\*\*과 정확히같은철학: \*\*"원본에절대손대지않는다"\*\*는 원칙이, 여기서는 트랜잭션복구에 적용됩니다.

### 도식화 제안

```
[트랜잭션시작]
[그림자페이지테이블] → 원본페이지A,B,C (안건드림)
[현재페이지테이블]   → 원본페이지A,B,C (처음엔 동일하게가리킴)

[페이지B 수정시]
     ↓ 원본B는그대로,새위치에 B'(수정된복사본) 생성
[그림자페이지테이블] → 원본A, 원본B, 원본C  (여전히안건드려짐)
[현재페이지테이블]   → 원본A, B'(수정본), 원본C
```

### Ⅲ. 원자적전환 및 장단점 — 핵심 배점

**함정 방지: "복사본에서작업한다"고만답하면절반. 왜"포인터교체"가원자적(한순간에)이어야하는지,그리고REDO/UNDO대비 장단점을보여줘야완성됩니다.**

**커밋시점의핵심동작**: 모든수정이완료되면, **"그림자페이지테이블포인터"를 "현재페이지테이블"로 한번에교체**— 이 **포인터교체자체는 매우작은(디스크블록하나)원자적연산**이라, **중간에실패할틈이없습니다**.

```
[커밋순간]
디스크의 "루트포인터" 하나만 
  구(舊)그림자테이블 → 신(新)현재테이블 로 교체
     ↓ (이교체자체는 하드웨어차원에서원자적으로보장됨)
[커밋완료] 새페이지테이블이 이제 "정식" 데이터가됨
[이전그림자테이블] → 더이상필요없으니 폐기(공간회수)
```

**REDO/UNDO대비장단점**

| 구분             | **그림자페이징**                                                        | **REDO/UNDO(로그기반)**       |
| :------------- | :---------------------------------------------------------------- | :------------------------ |
| **복구속도**       | **매우빠름**(로그분석불필요,포인터만확인)                                          | 로그전체분석필요(체크포인트로완화)        |
| **UNDO자체가불필요** | **원본이그대로있어서**,실패시그냥 **그림자테이블을버리면끝**                               | 명시적으로되돌리는연산필요             |
| **단점**(핵심)     | **데이터가분산됨**(연속된페이지들이흩어짐→디스크단편화),**동시성지원이어려움**(여러트랜잭션이동시에그림자만들기복잡) | 로그오버헤드는있지만, **동시성처리에더유리** |

→ 암기: **"그림자페이징은복구가빠르고UNDO가필요없지만, 데이터가흩어지고여러트랜잭션동시처리가어렵다"** — 앞서다룬 \*\*"락기반vs타임스탬프기반"\*\*의 트레이드오프처럼, 여기서도 \*\*"복구단순성vs동시성처리능력"\*\*이라는 트레이드오프가 존재합니다 — 이런 **동시성문제때문에, 실무에서는REDO/UNDO(로그기반)가더보편적으로쓰입니다**.

### 도식화 제안

```
[장애발생시나리오]
[그림자페이징]                        [REDO/UNDO]
장애시 → "루트포인터가 아직           장애시 → 로그전체분석
        그림자를가리키는가,           → 커밋된건REDO
        현재를가리키는가" 확인만       → 안커밋된건UNDO
        (매우빠름,분석불필요)         (상대적으로복잡,시간소요)
```

### Ⅳ. 결론

그림자페이징은 \*\*"로그를남기지않고, 원본을절대건드리지않은채 복사본에서작업하다, 완성되면포인터를원자적으로한번에교체"\*\*하는 방식으로, REDO/UNDO와는 **완전히다른철학**으로 같은목표(장애시데이터안전보장)를 달성합니다 — **복구가매우빠르고UNDO자체가불필요**하다는 장점이있지만, **디스크단편화와동시성처리의어려움**때문에 **실무에서는REDO/UNDO(로그기반)가더널리쓰입니다** — 이는 앞서다룬 \*\*"정적할당vs동적할당","락기반vs낙관적"\*\*같은 여러답안에서 반복된 \*\*"단순함과성능,동시성사이의트레이드오프"\*\*가, 데이터베이스회복기법에서도 동일하게나타난다는 것을 보여주며, 오늘하루다룬 방대한데이터베이스트랜잭션·회복시리즈전체를 완결짓습니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "DB가 뻗었을 때를 대비해 로그(Log)를 남기는 대신, 복사본(그림자)을 몰래 만드는 특이한 회복 기법이다. 핵심은 **'원본 절대 사수'**다. 데이터를 수정할 때 원본을 건드리지 않고, '그림자 페이지'를 하나 복사해 놓고 거기다가 실컷 수정한다. 작업이 성공(Commit)하면 짠! 하고 포인터(디렉터리)만 그림자 쪽으로 휙 바꿔치기한다. 서버가 뻗어서 취소(UNDO)해야 한다면? 덮어쓰지 않고 남겨둔 원본 쪽으로 포인터만 다시 돌리면 1초 만에 원상 복구된다. 로그를 안 쓰기 때문에 REDO(다시하기)는 아예 불가능하지만, 취소(UNDO) 속도만큼은 우주 최강인 기법이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 로그(Log) 기반 회복의 대안, 그림자 페이징 개요**

* **정의:** 트랜잭션 수행 시 데이터를 직접 수정하지 않고 복사본인 '그림자 페이지'를 생성하여 갱신한 후, 완료(Commit) 시 페이지 테이블 포인터를 교체하는 데이터베이스 회복 기법.
* **목적:** 방대한 로그 파일을 유지하고 검색해야 하는 오버헤드를 없애고, 실패한 트랜잭션의 원상복구(UNDO) 속도를 극대화하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 포인터 스위칭을 통한 초고속 복구**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5NjAuNTcxOTk5OTk5OTk5OSA0MDUuNzI2NjY2NjY2NjY2NyIgd2lkdGg9Ijk2MC41NzE5OTk5OTk5OTk5IiBoZWlnaHQ9IjQwNS43MjY2NjY2NjY2NjY3IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfX19fXyIgZGF0YS1sYWJlbD0i6re466a87J6QIO2OmOydtOynleydmCDsiJjsoJUg67CPIOuzteq1rCDsm5DrpqwiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9Ijg4MC41NzE5OTk5OTk5OTk5IiBoZWlnaHQ9IjMyNS43MjY2NjY2NjY2NjY3IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iODgwLjU3MTk5OTk5OTk5OTkiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7qt7jrprzsnpAg7Y6Y7J207KeV7J2YIOyImOyglSDrsI8g67O16rWsIOybkOumrDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUyIgZGF0YS10bz0iUCIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuybkOuzuCDqsbTrk6Tsp4Ag7JWK7J2MIiBwb2ludHM9IjI2MC4yMjksMTEwLjkgNDYwLjI3OSwxMTAuOSA0NjAuMjc5LDExNi4yNSA0OTYuMjc5LDExNi4yNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDIiBkYXRhLXRvPSJQIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7ISx6rO1IOyLnCDtj6zsnbjthLAg7Iqk7JyE7LmtIiBwb2ludHM9IjI0NS40MDksMjExLjAxNTAwMDAwMDAwMDAxIDI2NC44MTg5OTk5OTk5OTk5NiwyMTEuMDE1MDAwMDAwMDAwMDEgMjY0LjgxODk5OTk5OTk5OTk2LDE2My45NjY2NjY2NjY2NjY2NyA0NjAuMjc5LDE2My45NjY2NjY2NjY2NjY2NyA0NjAuMjc5LDEzOC44NTAwMDAwMDAwMDAwMiA0OTYuMjc5LDEzOC44NTAwMDAwMDAwMDAwMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJGQUlMIiBkYXRhLXRvPSJTMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i4pyoIOy0iOqzoOyGjSBVTkRPIOKcqCIgcG9pbnRzPSI0NDguMjc5LDI3NS45OTY2NjY2NjY2NjY2NyA2NjAuMzI5LDI3NS45OTY2NjY2NjY2NjY2NyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQyIgZGF0YS10bz0iRkFJTCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyNDUuNDA5LDIyOC45NDgzMzMzMzMzMzMzNSAyNjQuODE4OTk5OTk5OTk5OTYsMjI4Ljk0ODMzMzMzMzMzMzMyIDI2NC44MTg5OTk5OTk5OTk5NiwyNzUuOTk2NjY2NjY2NjY2NjcgMzAwLjgxODk5OTk5OTk5OTk2LDI3NS45OTY2NjY2NjY2NjY2NyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJTIiBkYXRhLXRvPSJQIiBkYXRhLWxhYmVsPSLsm5Drs7gg6rG065Ok7KeAIOyViuydjCI+CiAgPHJlY3QgeD0iMzIyLjM2MTk5OTk5OTk5OTk3IiB5PSI5NC45IiB3aWR0aD0iMTA0LjM3NDAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzc0LjU0OSIgeT0iMTEwLjA1MDAwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7sm5Drs7gg6rG065Ok7KeAIOyViuydjDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJDIiBkYXRhLXRvPSJQIiBkYXRhLWxhYmVsPSLshLHqs7Ug7IucIO2PrOyduO2EsCDsiqTsnITsua0iPgogIDxyZWN0IHg9IjMwOS41OTEiIHk9IjE0Ny45NjY2NjY2NjY2NjY2NyIgd2lkdGg9IjEyOS45MTYiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzNzQuNTQ5IiB5PSIxNjMuMTE2NjY2NjY2NjY2NjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuyEseqztSDsi5wg7Y+s7J247YSwIOyKpOychOy5rTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJGQUlMIiBkYXRhLXRvPSJTMiIgZGF0YS1sYWJlbD0i4pyoIOy0iOqzoOyGjSBVTkRPIOKcqCI+CiAgPHJlY3QgeD0iNDk4Ljg0OTk5OTk5OTk5OTk3IiB5PSIyNTkuOTk2NjY2NjY2NjY2NyIgd2lkdGg9IjExMC45MDgiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1NTQuMzA0IiB5PSIyNzUuMTQ2NjY2NjY2NjY2NyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+4pyoIOy0iOqzoOyGjSBVTkRPIOKcqDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUCIgZGF0YS1sYWJlbD0i7ZWY65Oc65SU7Iqk7YGsCu2OmOydtOyngCIgZGF0YS1zaGFwZT0iY3lsaW5kZXIiPgogIDxyZWN0IHg9IjQ5Ni4yNzkiIHk9IjEwMC42NSIgd2lkdGg9IjExNi4wNSIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMSIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0ibm9uZSIgLz4KICA8bGluZSB4MT0iNDk2LjI3OSIgeTE9IjEwMC42NSIgeDI9IjQ5Ni4yNzkiIHkyPSIxNTQuNDUwMDAwMDAwMDAwMDIiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDxsaW5lIHgxPSI2MTIuMzI5IiB5MT0iMTAwLjY1IiB4Mj0iNjEyLjMyOSIgeTI9IjE1NC40NTAwMDAwMDAwMDAwMiIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPGVsbGlwc2UgY3g9IjU1NC4zMDQiIGN5PSIxNTQuNDUwMDAwMDAwMDAwMDIiIHJ4PSI1OC4wMjUiIHJ5PSI3IiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPGVsbGlwc2UgY3g9IjU1NC4zMDQiIGN5PSIxMDAuNjUiIHJ4PSI1OC4wMjUiIHJ5PSI3IiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNTU0LjMwNCIgeT0iMTI3LjU1MDAwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI1NTQuMzA0IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7ZWY65Oc65SU7Iqk7YGsPC90c3Bhbj48dHNwYW4geD0iNTU0LjMwNCIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7Y6Y7J207KeAPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlMiIGRhdGEtbGFiZWw9Iuq3uOumvOyekCDthYzsnbTruJQK7JWI7KCE7ZWcIOqzvOqxsCDsm5Drs7gg6rCA66as7YK0IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjYzLjQxIiB5PSI4NCIgd2lkdGg9IjE5Ni44MTkiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE2MS44MTk1IiB5PSIxMTAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTYxLjgxOTUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7qt7jrprzsnpAg7YWM7J2067iUPC90c3Bhbj48dHNwYW4geD0iMTYxLjgxOTUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyViOyghO2VnCDqs7zqsbAg7JuQ67O4IOqwgOumrO2CtDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDIiBkYXRhLWxhYmVsPSLtmITsnqwg7YWM7J2067iUCuuzteyCrOuzuOyXkCDqsLHsi6Ag7J6R7JeFIOykkSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI2My40MSIgeT0iMTkzLjA4MTY2NjY2NjY2NjY4IiB3aWR0aD0iMTgxLjk5OSIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTU0LjQwOTQ5OTk5OTk5OTk4IiB5PSIyMTkuOTgxNjY2NjY2NjY2NjgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE1NC40MDk0OTk5OTk5OTk5OCIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPu2YhOyerCDthYzsnbTruJQ8L3RzcGFuPjx0c3BhbiB4PSIxNTQuNDA5NDk5OTk5OTk5OTgiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuuzteyCrOuzuOyXkCDqsLHsi6Ag7J6R7JeFIOykkTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJGQUlMIiBkYXRhLWxhYmVsPSLsnqXslaAg67Cc7IOdISDwn5KjIiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjM3NC41NDksMjAyLjI2NjY2NjY2NjY2NjY1IDQ0OC4yNzksMjc1Ljk5NjY2NjY2NjY2NjY3IDM3NC41NDksMzQ5LjcyNjY2NjY2NjY2NjcgMzAwLjgxODk5OTk5OTk5OTk2LDI3NS45OTY2NjY2NjY2NjY2NyIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIzNzQuNTQ5IiB5PSIyNzUuOTk2NjY2NjY2NjY2NjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyepeyVoCDrsJzsg50hIPCfkqM8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlMyIiBkYXRhLWxhYmVsPSLtmITsnqwg7YWM7J2067iUIOuyhOugpOuyhOumrOqzoArqt7jrprzsnpAg7YWM7J2067iU7J2EIOuplOyduOycvOuhnCDrs7XqtawhIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjY2MC4zMjkiIHk9IjI0OS4wOTY2NjY2NjY2NjY2NiIgd2lkdGg9IjI0NC4yNDMiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNzgyLjQ1MDQ5OTk5OTk5OTkiIHk9IjI3NS45OTY2NjY2NjY2NjY2NyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNzgyLjQ1MDQ5OTk5OTk5OTkiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7tmITsnqwg7YWM7J2067iUIOuyhOugpOuyhOumrOqzoDwvdHNwYW4+PHRzcGFuIHg9Ijc4Mi40NTA0OTk5OTk5OTk5IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7qt7jrprzsnpAg7YWM7J2067iU7J2EIOuplOyduOycvOuhnCDrs7XqtawhPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 로그(Log) 기반 회복 vs 그림자 페이징(Shadow) 전격 대조 (3단 표)**

이 토픽은 전통적인 로그 기반 회복과 비교하여, REDO/UNDO의 여부와 성능 한계를 명확히 대조하는 것이 핵심입니다.

| **핵심 척도**             | **📝 기존 로그(Log) 기반 회복**                                                         | **👥 그림자 페이징 (Shadow) 🚨**                                                             |
| :-------------------- | :------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------- |
| **동작 방식**             | **'원본 덮어쓰기 + 일기장 쓰기'.** 디스크의 원본 데이터를 직접 덮어쓰며, 변경 전/후의 모든 기록을 일기장(Log)에 빼곡히 적어둠. | **'원본 보존 + 포인터 스위칭 💯'.** 원본은 절대 안 건드림. 복사본(그림자)을 만들어 수정한 뒤, 성공하면 디렉터리 포인터만 교체함.       |
| **복구 (UNDO/REDO) 🚨** | **\[REDO 가능 / UNDO 가능]** 로그 파일에 과거 값(Before)과 미래 값(After)이 다 있어서 둘 다 수행 가능함.    | **\[REDO 불가 ❌ / UNDO 빛의 속도 💯]** 로그를 안 남기므로 REDO는 애초에 불가능함. 대신 원본이 살아있어 UNDO는 1초 만에 됨. |
| **장단점**               | 가장 범용적이고 안전하지만, 로그 파일 관리로 인한 디스크 I/O 오버헤드가 큼.                                   | UNDO가 미친 듯이 빠름. 하지만 복사본을 계속 만들다 보니 디스크 파편화(단편화)가 끔찍하게 발생함.                             |
| **동시성 제어**            | 락(Lock) 기법 등과 결합하여 동시 다발적인 트랜잭션 처리가 수월함.                                        | 복사본 페이지가 너무 얽혀서 다중 트랜잭션 병행 처리가 극도로 까다로움.                                               |

#### **IV. \[결론/제언] 최신 인메모리(In-Memory) DB와 SSD 환경에서의 제한적 활용**

* **(키워드 위주 2줄 마무리)** "과거 HDD 환경에서는 그림자 페이징의 극심한 데이터 단편화 문제로 인해 사장되었습니다. 그러나 랜덤 액세스 속도가 빛에 가까운 최신 NVMe SSD와 인메모리(In-Memory) 데이터베이스 환경에서는 단편화 오버헤드가 상쇄되므로, **가비지 컬렉션(GC)이나 CoW(Copy-on-Write) 방식의 스토리지 엔진에서 그 사상이 부활하여 응용되고 있습니다.**"
