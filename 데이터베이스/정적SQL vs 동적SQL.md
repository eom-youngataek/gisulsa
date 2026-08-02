### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (핵심차이 - 컴파일시점) — 3~4줄
Ⅱ. 정적SQL (본론①, 도식 1개 필수)
Ⅲ. 동적SQL, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

정적SQL과동적SQL의근본차이는 \*\*"SQL문의구조가 프로그램작성시점에확정되는가,실행시점에야확정되는가"\*\*입니다 — 이차이는 **성능,보안,유연성**모두에 영향을미칩니다.

### Ⅱ. 정적SQL — 컴파일시점에확정

| 항목       | 내용                                                             |
| :------- | :------------------------------------------------------------- |
| **정의**   | SQL문의 **테이블,컬럼,조건구조가 프로그램작성시점에 완전히고정**,값만바인딩변수로전달              |
| **실행계획** | **DB가미리파싱·최적화**해두어, 실행시 **바로재사용**(반복실행시빠름)                     |
| **보안**   | 앞서다룬 **"SQL인젝션방어의핵심"**— 파라미터화쿼리(PreparedStatement)가 정적SQL의대표구현 |
| **한계**   | **테이블명,컬럼명자체는동적으로바꿀수없음**(조건값만변경가능)                             |

→ 암기: **"틀은고정,값만바뀐다"** — 앞서다룬 \*\*"SQL인젝션방어"\*\*답안에서 다룬 \*\*"데이터와명령을분리"\*\*하는 원칙이, 바로 정적SQL(파라미터화쿼리)이 그방어의핵심수단이었다는 연결입니다.

### 도식화 제안

```
[정적SQL]
SELECT * FROM 주문 WHERE 고객번호 = ?  ← 구조는고정
     ↓ 값만바인딩
실행1: 고객번호=101
실행2: 고객번호=205
(구조가같으니 DB가 실행계획을 재사용,빠름)
```

### Ⅲ. 동적SQL — 실행시점에구조자체가결정, 핵심 배점

**함정 방지: "실행시생성한다"고만답하면절반. 왜필요한지(정적SQL로안되는경우), 그리고보안위험을반드시보여줘야완성됩니다.**

| 항목           | 내용                                                                  |
| :----------- | :------------------------------------------------------------------ |
| **정의**       | **SQL문의구조자체**(테이블명,컬럼명,조건개수등)를 **실행시점에프로그램이조합**해서 생성                |
| **필요한상황**    | **검색조건이가변적**인경우(사용자가 선택한필터에따라 WHERE절자체가달라짐),**테이블명자체를동적으로결정**해야하는경우 |
| **보안위험**(핵심) | **문자열을직접이어붙이면** 앞서다룬 **SQL인젝션에그대로노출**                               |
| **안전한구현**    | 동적으로**구조**는조합하되, **값은반드시파라미터화**해서 전달(EXECUTEIMMEDIATE+바인드변수)        |

→ 암기: **"틀자체를 실행할때조립한다 — 조립할때조심하지않으면 인젝션의문이열린다"** — 앞서다룬 \*\*"프롬프트인젝션"\*\*에서 \*\*"지시와데이터를구분하기어렵다"\*\*던 문제가, 동적SQL에서는 **"SQL구조(지시)와사용자입력(데이터)을 문자열로합칠때 구분이흐려지는"** 형태로 재현됩니다.

### 도식화 제안

```
[동적SQL - 위험한방식]
sql = "SELECT * FROM " + 테이블명변수 + " WHERE " + 조건변수
     ↓ (사용자입력이그대로문자열에합쳐짐)
공격자입력: "주문; DROP TABLE 고객;--" → SQL인젝션발생가능

[동적SQL - 안전한방식]
sql = "SELECT * FROM " + 테이블명변수(화이트리스트검증됨)
      + " WHERE 고객번호 = ?" ← 값은반드시파라미터화
     ↓
사용자입력값은 "데이터"로만처리, 구조에영향못줌
```

**대표활용사례**: **동적필터검색**(사용자가체크박스로여러조건선택),**동적피벗**(컬럼자체를런타임에결정),**관리자용범용조회도구** — 이런경우 **"WHERE절의개수·내용자체가 매번달라지므로"** 정적SQL로는불가능하고 동적SQL이 필수입니다.

### Ⅳ. 결론

정적SQL은 **"구조는고정,값만바뀌는"** 안전하고빠른방식이며, 동적SQL은 \*\*"구조자체를실행시점에조합해야하는 가변적요구사항"\*\*에대응하는 유연한방식입니다 — 앞서다룬 \*\*"SQL인젝션방어"\*\*의 핵심교훈은, \*\*"동적SQL이필요한상황에서도, 구조(테이블/컬럼명)는화이트리스트로검증하고,값(조건)은반드시파라미터화"\*\*해야한다는 것입니다 — 이는 오늘하루다룬 \*\*"프롬프트인젝션(지시와데이터분리의어려움)"\*\*과 정확히같은근본원리가, 전통적인SQL데이터베이스영역에서도 계속유효하다는 것을 보여줍니다.

## **1. 답안 전개 스토리 (핵심 압축)**

> "개발자가 애플리케이션 코드에 SQL을 어떻게 박아넣느냐에 따른 두 가지 쿼리 작성(실행) 방식이다. 첫째, **정적 SQL(Static)**. `SELECT * FROM 테이블 WHERE ID = ?`처럼 쿼리 뼈대(컬럼, 테이블명)를 콘크리트처럼 고정해 버리는 방식이다. DB가 미리 쿼리 실행 계획(길 찾기)을 세워두고 재활용(캐싱)할 수 있어 속도가 미친 듯이 빠르고 해킹(SQL Injection) 방어에 완벽하지만, 유연성이 떨어진다. 둘째, **동적 SQL(Dynamic)**. 실행될 때마다 `String sql = "SELECT * FROM " + 변수` 처럼 문자열을 레고처럼 조립해서 쏘는 방식이다. 게시판 다중 필터 검색처럼 조건이 휙휙 바뀌는 상황에선 최고지만, 쏠 때마다 DB가 구문 분석을 쌩으로 다시 해야 해서 성능이 떨어지며, 특히 해커의 조작 공격(SQL Injection)에 치명적으로 뚫리는 양날의 검이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 파싱(Parsing)과 유연성의 트레이드오프, SQL 실행 방식 개요**

* **정의:** 애플리케이션에서 DB로 쿼리를 날릴 때, 쿼리의 구조가 컴파일 시점에 100% 고정되어 있는지(정적), 아니면 런타임(실행 시점)에 문자열 결합으로 구조가 휙휙 바뀌는지(동적)에 따른 분류.
* **핵심 차이:** 오라클(Oracle) 등 DBMS의 공유 풀(Shared Pool) 메모리에 캐싱된 \*\*'실행 계획(Execution Plan)'\*\*을 재활용할 수 있느냐 없느냐가 성능을 가르는 핵심 기준임.

#### **II. \[본론 1] (극단적 단순화 버전) 뼈대를 굳히는 자 vs 문자열을 조립하는 자**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MjIuOTQ4MDAwMDAwMDAwMSA1OTEuMiIgd2lkdGg9IjUyMi45NDgwMDAwMDAwMDAxIiBoZWlnaHQ9IjU5MS4yIiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfU1FMX19TUUxfUGFyc2luZ18iIGRhdGEtbGFiZWw9IuygleyggSBTUUzqs7wg64+Z7KCBIFNRTOydmCDtjIzsi7EoUGFyc2luZykg66mU7Luk64uI7KaYIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI0NDIuOTQ4MDAwMDAwMDAwMDQiIGhlaWdodD0iNTExLjIwMDAwMDAwMDAwMDA1IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNDQyLjk0ODAwMDAwMDAwMDA0IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+7KCV7KCBIFNRTOqzvCDrj5nsoIEgU1FM7J2YIO2MjOyLsShQYXJzaW5nKSDrqZTsu6Tri4jsppg8L3RleHQ+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMV9fU1FMX1ByZXBhcmVkU3RhdGVtZW50IiBkYXRhLWxhYmVsPSIxLiDsoJXsoIEgU1FMIChQcmVwYXJlZFN0YXRlbWVudCkiPgogIDxyZWN0IHg9IjU2IiB5PSIzMTkuNiIgd2lkdGg9IjQxMC45NDgwMDAwMDAwMDAwNCIgaGVpZ2h0PSIyMTUuNjAwMDAwMDAwMDAwMDIiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI1NiIgeT0iMzE5LjYiIHdpZHRoPSI0MTAuOTQ4MDAwMDAwMDAwMDQiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjY4IiB5PSIzMzMuNiIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij4xLiDsoJXsoIEgU1FMIChQcmVwYXJlZFN0YXRlbWVudCk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSIyX19TUUxfU3RhdGVtZW50IiBkYXRhLWxhYmVsPSIyLiDrj5nsoIEgU1FMIChTdGF0ZW1lbnQpIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSIyNTMuMjcxOTk5OTk5OTk5OTYiIGhlaWdodD0iMjE1LjYwMDAwMDAwMDAwMDAyIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMjUzLjI3MTk5OTk5OTk5OTk2IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI2OCIgeT0iOTgiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+Mi4g64+Z7KCBIFNRTCAoU3RhdGVtZW50KTwvdGV4dD4KPC9nPgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTMSIgZGF0YS10bz0iUzIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzQwLjMxMiw0MTcuNDAwMDAwMDAwMDAwMDMgMzQwLjMxMiw0NjUuNDAwMDAwMDAwMDAwMDMiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlMyIiBkYXRhLXRvPSJTMiIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuqwkuunjCDrsJTqv5TshJwg7LSI6rOg7IaNIOyerO2ZnOyaqSIgcG9pbnRzPSIyMjkuNjc2MDAwMDAwMDAwMDQsNDgzLjMzMzMzMzMzMzMzMzM3IDIxOS42NzYwMDAwMDAwMDAwNCw0ODMuMzMzMzMzMzMzMzMzMzcgMjE5LjY3NjAwMDAwMDAwMDA0LDUwMS4yNjY2NjY2NjY2NjY3IDIyOS42NzYwMDAwMDAwMDAwNCw1MDEuMjY2NjY2NjY2NjY2NyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJEMSIgZGF0YS10bz0iRDIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTgyLjYzNTk5OTk5OTk5OTk3LDE4MS44IDE4Mi42MzU5OTk5OTk5OTk5NywyMjkuOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJTMiIgZGF0YS10bz0iUzIiIGRhdGEtbGFiZWw9IuqwkuunjCDrsJTqv5TshJwg7LSI6rOg7IaNIOyerO2ZnOyaqSI+CiAgPHJlY3QgeD0iNjgiIHk9IjQ3Ny4xNTAwMDAwMDAwMDAxIiB3aWR0aD0iMTUzLjY3NjAwMDAwMDAwMDA0IiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTQ0LjgzODAwMDAwMDAwMDAyIiB5PSI0OTIuMzAwMDAwMDAwMDAwMDciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuqwkuunjCDrsJTqv5TshJwg7LSI6rOg7IaNIOyerO2ZnOyaqTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzEiIGRhdGEtbGFiZWw9Iuu8iOuMgCDqs6DsoJUKU0VMRUNUIC4uLiBXSEVSRSBJRCA9ID8iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjQ1Ljk3ODAwMDAwMDAwMDA0IiB5PSIzNjMuNiIgd2lkdGg9IjE4OC42NjgiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjM0MC4zMTIiIHk9IjM5MC41IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIzNDAuMzEyIiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+67yI64yAIOqzoOyglTwvdHNwYW4+PHRzcGFuIHg9IjM0MC4zMTIiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPlNFTEVDVCAuLi4gV0hFUkUgSUQgPSA/PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlMyIiBkYXRhLWxhYmVsPSLinKggMeuyiOunjCDtjIzsi7Eg7JmE66OMIOKcqArsi6Ttlokg6rOE7ZqNIOy6kOyLsSAo66mU66qo66asIOyggOyepSkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjI5LjY3NjAwMDAwMDAwMDA0IiB5PSI0NjUuNDAwMDAwMDAwMDAwMDMiIHdpZHRoPSIyMjEuMjcyIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjM0MC4zMTIiIHk9IjQ5Mi4zIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIzNDAuMzEyIiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+4pyoIDHrsojrp4wg7YyM7IuxIOyZhOujjCDinKg8L3RzcGFuPjx0c3BhbiB4PSIzNDAuMzEyIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7si6Ttlokg6rOE7ZqNIOy6kOyLsSAo66mU66qo66asIOyggOyepSk8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRDEiIGRhdGEtbGFiZWw9IuufsO2DgOyehCDrrLjsnpDsl7Qg7KGw66a9ClNFTEVDVCAuLi4gV0hFUkUgSUQgPSAnYWRtaW4nIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjcyIiB5PSIxMjgiIHdpZHRoPSIyMjEuMjcxOTk5OTk5OTk5OTYiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE4Mi42MzU5OTk5OTk5OTk5NyIgeT0iMTU0LjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE4Mi42MzU5OTk5OTk5OTk5NyIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuufsO2DgOyehCDrrLjsnpDsl7Qg7KGw66a9PC90c3Bhbj48dHNwYW4geD0iMTgyLjYzNTk5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5TRUxFQ1QgLi4uIFdIRVJFIElEID0gJiMzOTthZG1pbiYjMzk7PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkQyIiBkYXRhLWxhYmVsPSLsi6TtlontlaAg65WM66eI64ukCuyymOydjOu2gO2EsCDsjKnsnLzroZwg7YyM7IuxIPCfkqYiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iODQuMjI2NDk5OTk5OTk5OTkiIHk9IjIyOS44IiB3aWR0aD0iMTk2LjgxOSIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxODIuNjM1OTk5OTk5OTk5OTciIHk9IjI1Ni43IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxODIuNjM1OTk5OTk5OTk5OTciIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7si6TtlontlaAg65WM66eI64ukPC90c3Bhbj48dHNwYW4geD0iMTgyLjYzNTk5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7sspjsnYzrtoDthLAg7Iyp7Jy866GcIO2MjOyLsSDwn5KmPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 정적 SQL vs 동적 SQL 전격 대조 (3단 표)**

이 토픽은 '실행 계획 재활용 여부(성능)'와 'SQL 인젝션 방어 여부(보안)'를 크로스(Cross)로 대조하는 것이 완벽한 득점 포인트입니다.

| **핵심 척도**        | **🧱 정적 SQL (Static) 🚨**                                                                                   | **🧩 동적 SQL (Dynamic) 🚨**                                                                                             |
| :--------------- | :---------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| **개념 / 구조**      | **'컴파일 시점 뼈대 고정'.** Java의 `PreparedStatement`를 사용. 테이블명이나 컬럼명은 바꿀 수 없고, 오직 조건 값(?)만 바인딩 변수로 나중에 꽂아 넣음.      | **'런타임 시점 문자열 조립 💯'.** Java의 `Statement`나 MyBatis의 `<if>` 태그를 사용. 조건에 따라 테이블명이나 컬럼명 자체를 텍스트로 이어 붙여서 통째로 새로 만듦.        |
| **성능 (실행계획) 🚨** | **\[실행 계획 100% 재활용 (초고속)]** DB가 쿼리 뼈대 구조를 딱 한 번만 하드 파싱(Hard Parsing)해서 메모리에 올려두고, 값만 바꿔가며 소프트 파싱(초고속 재활용)함. | **\[매번 하드 파싱 발생 (성능 저하) 💯]** 문자열이 1글자만 달라도 DB는 아예 새로운 쿼리로 인식하여, 쏠 때마다 문법 검사와 실행 계획을 처음부터 다시 짬. CPU 부하 심각.             |
| **보안 / 유연성 🚨**  | **\[보안 최강 💯]** 사용자가 ' OR 1=1 -- 같은 해킹 코드를 입력해도, DB가 이를 코드가 아닌 '단순 문자열(값)'로 인식하여 **SQL 인젝션 공격이 원천 차단됨.**    | **\[보안 취약점 💯 / 극강의 유연성]** 게시판의 다중 필터(제목, 작성자, 내용 등) 조합 검색 시 매우 유연하지만, **문자열 조립 시 해커의 악성 코드가 그대로 실행되는 SQL 인젝션에 치명적임.** |

#### **IV. \[결론/제언] 마이바티스(MyBatis)와 JPA 시대의 올바른 혼용 전략**

* **(키워드 위주 2줄 마무리)** "동적 SQL이 유연하다고 해서 모든 쿼리를 동적으로 짜면 DB 서버의 CPU 메모리(Shared Pool)가 터져버립니다. 따라서 최신 프레임워크(JPA, MyBatis) 개발 시 **기본적인 CRUD는 100% 바인딩 변수를 쓰는 정적 SQL(# 표기)로 구성하고, 복잡한 다중 조건 검색 등 불가피한 경우에만 제한적으로 동적 SQL($ 표기)을 쓰는 하이브리드 전략이 필수입니다.**"
