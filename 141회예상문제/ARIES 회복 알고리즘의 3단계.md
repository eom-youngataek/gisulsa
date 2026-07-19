### **ARIES 회복 알고리즘의 3단계 (Analysis / Redo / Undo)**

#### 답안 전개 스토리 (핵심 압축)

> "데이터베이스가 갑자기 죽었을 때 '어디서부터 다시 시작해야 하는가'를 결정하는 것이 회복 알고리즘의 본질이다. \*\*ARIES(Algorithm for Recovery and Isolation Exploiting Semantics)\*\*는 이 문제를 세 단계의 정밀 외과 수술로 해결한다. **1단계 \[분석(Analysis)]**: 마지막 체크포인트부터 로그를 앞으로 훑어 '장애 시점에 어떤 트랜잭션이 살아있었고 어떤 페이지가 더러웠는지(Dirty)'를 파악하는 탐정 수사다. **2단계 \[재실행(Redo)]**: 분석이 찾아낸 Redo LSN부터 장애 직전까지 로그를 그대로 재실행해 '커밋됐든 미커밋됐든 로그에 기록된 모든 변경을 복원'하는 역사 반복이다. **3단계 \[취소(Undo)]**: Redo 완료 후 장애 시점에 미커밋 상태였던 트랜잭션의 변경을 역순으로 되돌려 '없던 일로 만드는' ACID 원자성 복원이다 — Redo는 Steal·No-Force 정책 덕분에 디스크에 내려가 있지 않을 수 있는 커밋 데이터를 살리고, Undo는 디스크에 내려가 있을 수 있는 미커밋 데이터를 지운다."

***

#### 핵심 내용 (암기용)

**전제 개념**

| 개념                                 | 내용                                      |
| :--------------------------------- | :-------------------------------------- |
| **LSN (Log Sequence Number)**      | 로그 레코드 고유 번호·단조 증가 / 모든 회복 판단의 기준       |
| **WAL (Write-Ahead Logging)**      | 페이지 디스크 기록 전 반드시 로그 먼저 기록 / ARIES 전제 조건 |
| **Steal 정책**                       | 미커밋 트랜잭션 페이지도 디스크에 쓸 수 있음 / Undo 필요 이유  |
| **No-Force 정책**                    | 커밋 시 즉시 디스크 쓰기 강제 안 함 / Redo 필요 이유      |
| **체크포인트 (Checkpoint)**             | 주기적으로 ATT·DPT 상태를 로그에 기록 / 분석 시작점       |
| **ATT (Active Transaction Table)** | 장애 시점 활성 트랜잭션 목록                        |
| **DPT (Dirty Page Table)**         | 버퍼에서 수정됐으나 디스크 미반영 페이지 목록               |

***

| **핵심 척도**    | **📊 1단계: 분석 (Analysis) 🚨**                                                  | **🔑 2단계: 재실행 (Redo) 🚨**                                              | **🏁 3단계: 취소 (Undo) 💯**                                    |
| :----------- | :---------------------------------------------------------------------------- | :--------------------------------------------------------------------- | :---------------------------------------------------------- |
| **시작점**      | **마지막 체크포인트 LSN** (로그 전체 스캔 불필요)                                              | **DPT 내 최소 RecLSN** (가장 오래된 Dirty Page)                                | **Redo 완료 직후** (로그 역방향)                                     |
| **진행 방향**    | **로그 순방향 스캔** (체크포인트→장애지점)                                                    | **로그 순방향 재실행** (RecLSN→장애지점)                                           | **로그 역방향 취소** (장애지점→트랜잭션 시작)                                |
| **핵심 작업 🚨** | **ATT 갱신** (Begin→Add / Commit·Abort→Remove) **DPT 갱신** (페이지 수정 로그→RecLSN 기록) | **모든 로그 무조건 재실행** (커밋·미커밋 구분 없음) **단, pageLSN ≥ 로그LSN이면 이미 반영 → Skip** | **ATT 내 미커밋 트랜잭션만** CLR(Compensation Log Record) 기록하며 역순 취소 |
| **산출물**      | 장애 시점 ATT·DPT 확정 → Redo 시작점 결정                                                | 장애 직전 DB 상태 완전 복원 (커밋 데이터 포함)                                          | ACID 원자성 보장 (미커밋 변경 전체 제거)                                  |

***

#### 도식화

```
[ARIES 3단계 전체 흐름]

로그 LSN →  100   200   300   400   500   600   700
            │     │     │     │     │     │     │
            CKPT  T1    T2    T1    T2    T3   CRASH
                  Begin Begin Write Commit Begin  ↑
                              T1-P1       장애

①분석 (Analysis): CKPT(LSN=100) → CRASH(LSN=700) 순방향
  ATT 확정: T1(미커밋), T3(미커밋)  ← T2는 Commit 확인
  DPT 확정: P1(RecLSN=300)

②재실행 (Redo): RecLSN=300 → CRASH(LSN=700) 순방향
  LSN=300 T1-P1 재실행 (P1.pageLSN<300 이면 실행)
  LSN=400 T2-Commit 재실행
  LSN=600 T3-Begin 재실행
  → 장애 직전 상태 완전 복원 ✅

③취소 (Undo): ATT(T1·T3) 역방향
  T3: LSN=600 취소 → CLR 기록
  T1: LSN=300 취소 → CLR 기록
  → 미커밋 변경 전부 제거 ✅

[최종 상태]
  T2: Commit됨 → 데이터 영구 반영 ✅
  T1·T3: Abort → 변경 없던 일로 ✅
```

***

**(제언)** "ARIES는 Steal·No-Force 정책의 자유도를 최대화하면서도 WAL과 3단계 회복으로 ACID를 완벽 보장하는 현대 RDBMS 회복의 사실상 표준입니다. **분산 DB·클라우드 환경에서는 체크포인트 대신 분산 스냅샷·Raft 로그와 결합한 ARIES 확장 변형**이 MySQL InnoDB·PostgreSQL·CockroachDB에서 실제 구현되고 있으며, 장애 복구 설계 시 RTO 목표에 따라 체크포인트 주기와 로그 버퍼 크기를 함께 최적화해야 합니다."

#### **1. 답안 전개 스토리 (핵심 압축)**

> "IBM의 C. Mohan이 제정하여 현대 오라클, MSSQL 등 대다수 RDBMS 복구 엔진의 글로벌 표준으로 자리 잡은 **'가장 정밀하고 신뢰성 높은 데이터베이스 로그 기반 장애 복구 알고리즘'**이다. 시스템이 뻗었다가 다시 켜질 때, ARIES는 3단계로 복구를 실행한다. 1단계 **\[Analysis (분석)]**: 마지막 체크포인트부터 로그를 앞으로 스캔하여, 장애 직전 죽어가던 트랜잭션(Loser)과 메모리가 더러워졌던 페이지(Dirty Page)를 파악한다. 2단계 **\[Redo (재실행) 🚨]**: \*\*'역사의 반복(Repeating History)'\*\*이라는 철학에 따라, 실패한 트랜잭션의 작업까지 일단 전부 디스크에 똑같이 다시 써서 장애 직전 상태로 완벽히 되돌려놓는다. 3단계 **\[Undo (취소) 💯]**: 최종 실패한 놈들(Loser)의 작업만 로그를 뒤로 스캔하며 싹 걷어내어 복구를 마친다. 복구 도중 다시 정전이 나도 중복 복구를 막는 CLR(보상로그레코드) 기술이 코어다."

#### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OTIuNTg2OTk5OTk5OTk5OTMgNDk5LjIwMDAwMDAwMDAwMDA1IiB3aWR0aD0iNDkyLjU4Njk5OTk5OTk5OTkzIiBoZWlnaHQ9IjQ5OS4yMDAwMDAwMDAwMDAwNSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iQVJJRVNfX18zXyIgZGF0YS1sYWJlbD0iQVJJRVMg67O16rWsIOyVjOqzoOumrOymmCAz64uo6rOEIOybjO2BrO2UjOuhnOyasCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNDEyLjU4Njk5OTk5OTk5OTkzIiBoZWlnaHQ9IjQxOS4yMDAwMDAwMDAwMDAwNSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjQxMi41ODY5OTk5OTk5OTk5MyIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPkFSSUVTIOuzteq1rCDslYzqs6DrpqzsppggM+uLqOqzhCDsm4ztgaztlIzroZzsmrA8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkNSQVNIIiBkYXRhLXRvPSJQMSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyNDYuMjkzNDk5OTk5OTk5OTcsMTIwLjkgMjQ2LjI5MzQ5OTk5OTk5OTk3LDE2OC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJQMSIgZGF0YS10bz0iUDIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjQ2LjI5MzQ5OTk5OTk5OTk3LDIyMi43MDAwMDAwMDAwMDAwMiAyNDYuMjkzNDk5OTk5OTk5OTcsMjcwLjcwMDAwMDAwMDAwMDA1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJQMiIgZGF0YS10bz0iUDMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjQ2LjI5MzQ5OTk5OTk5OTk3LDM0MS40MDAwMDAwMDAwMDAwMyAyNDYuMjkzNDk5OTk5OTk5OTcsMzg5LjQwMDAwMDAwMDAwMDAzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDUkFTSCIgZGF0YS1sYWJlbD0i7J6l7JWgIOuwnOyDnSDtm4Qg7Iuc7Iqk7YWcIOu2gO2MhSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxNDYuNzcyNDk5OTk5OTk5OTgiIHk9Ijg0IiB3aWR0aD0iMTk5LjA0MiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI0Ni4yOTM1IiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyepeyVoCDrsJzsg50g7ZuEIOyLnOyKpO2FnCDrtoDtjIU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlAxIiBkYXRhLWxhYmVsPSLinKggMS4g67aE7ISdIOuLqOqzhCAoQW5hbHlzaXMpIOKcqArroZzqt7gg7Iic67Cp7ZalIOyKpOy6lCDinpQgRGlydHkgUGFnZSDrsI8gTG9zZXIg7Yq4656c7J6t7IWYIOyLneuzhCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iMTY4LjkiIHdpZHRoPSIzODAuNTg2OTk5OTk5OTk5OTMiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyNDYuMjkzNDk5OTk5OTk5OTciIHk9IjE5NS44IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIyNDYuMjkzNDk5OTk5OTk5OTciIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7inKggMS4g67aE7ISdIOuLqOqzhCAoQW5hbHlzaXMpIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjI0Ni4yOTM0OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+66Gc6re4IOyInOuwqe2WpSDsiqTsupQg4p6UIERpcnR5IFBhZ2Ug67CPIExvc2VyIO2KuOuenOyereyFmCDsi53rs4Q8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUDIiIGRhdGEtbGFiZWw9IuKcqCAyLiDsnqzsi6Ttlokg64uo6rOEIChSZWRvKSDwn5qoIOKcqArsl63sgqzsnZgg67CY67O1IFJlcGVhdGluZyBIaXN0b3J5CuyLpO2MqO2VnCDsnpHsl4Ug7Y+s7ZWoIOyepeyVoCDsp4HsoIQg7IOB7YOc66GcIOustOyhsOqxtCDsm5Drs7UiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNzYuNzQ3OTk5OTk5OTk5OTYiIHk9IjI3MC43MDAwMDAwMDAwMDAwNSIgd2lkdGg9IjMzOS4wOTEiIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjI0Ni4yOTM0OTk5OTk5OTk5NyIgeT0iMzA2LjA1MDAwMDAwMDAwMDA3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIyNDYuMjkzNDk5OTk5OTk5OTciIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj7inKggMi4g7J6s7Iuk7ZaJIOuLqOqzhCAoUmVkbykg8J+aqCDinKg8L3RzcGFuPjx0c3BhbiB4PSIyNDYuMjkzNDk5OTk5OTk5OTciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyXreyCrOydmCDrsJjrs7UgUmVwZWF0aW5nIEhpc3Rvcnk8L3RzcGFuPjx0c3BhbiB4PSIyNDYuMjkzNDk5OTk5OTk5OTciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyLpO2MqO2VnCDsnpHsl4Ug7Y+s7ZWoIOyepeyVoCDsp4HsoIQg7IOB7YOc66GcIOustOyhsOqxtCDsm5Drs7U8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUDMiIGRhdGEtbGFiZWw9IuKcqCAzLiDst6jshowg64uo6rOEIChVbmRvKSDwn5KvIOKcqArroZzqt7gg7Jet67Cp7ZalIOyKpOy6lCDinpQgTG9zZXIg7Yq4656c7J6t7IWY66eMIOyEoO2DneyggSDroaTrsLEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNjUuNjMzMDAwMDAwMDAwMDEiIHk9IjM4OS40MDAwMDAwMDAwMDAwMyIgd2lkdGg9IjM2MS4zMjA5OTk5OTk5OTk5IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjI0Ni4yOTM0OTk5OTk5OTk5NyIgeT0iNDE2LjMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjI0Ni4yOTM0OTk5OTk5OTk5NyIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuKcqCAzLiDst6jshowg64uo6rOEIChVbmRvKSDwn5KvIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjI0Ni4yOTM0OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+66Gc6re4IOyXreuwqe2WpSDsiqTsupQg4p6UIExvc2VyIO2KuOuenOyereyFmOunjCDshKDtg53soIEg66Gk67CxPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

| **핵심 척도**    | **📊 1단계 : 분석 (Analysis Phase)**                        | **🔑 2단계 : 재실행 (Redo Phase) 🚨**                             | **🏁 3단계 : 취소 (Undo Phase) 💯**                                |
| :----------- | :------------------------------------------------------ | :----------------------------------------------------------- | :------------------------------------------------------------- |
| **수행 목적**    | 장애 발생 당시 활성 상태였던 트랜잭션 목록과 디스크에 쓰이지 못한 버퍼 풀 페이지 목록을 특정함. | **장애 직전 상태의 완벽한 복원 💯.** 취소될 트랜잭션일지라도 일단 디스크에 반영하여 상태를 일치시킴. | 실패한 트랜잭션이 수행한 모든 갱신 작업을 취소하여 일관성 무결성을 복구함.                     |
| **스캔 방향**    | 마지막 체크포인트 ➔ 로그 최신 방향 (순방향).                             | Dirty Page 중 가장 오래된 LSN ➔ 로그 최신 방향 (순방향).                    | 로그 최신 방향 ➔ 가장 오래된 Active Tx 시작점 (역방향).                         |
| **핵심 기법 🚨** | 트랜잭션 테이블 및 더티 페이지 테이블 구성.                               | 중복 작업 방지를 위해 페이지 LSN과 로그 LSN을 비교해 생략 결정.                     | 복구 중 또 다운되는 악순환 방지를 위해 **CLR(Compensation Log Record) 🚨** 발송. |

* **(제언)** "ARIES는 무조건 장애 이전 상태로 원복한 뒤 승리자와 패배자를 가리는 '역사의 반복' 기조를 가집니다. **복구 시간을 단축하려면, 더티 페이지 테이블을 실시간 관리하는 체크포인트를 조밀하게 돌려 분석 및 Redo의 스캔 범위를 최소화해야 합니다.**"
