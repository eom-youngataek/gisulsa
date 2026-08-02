#### **NoSQL·SSD 저장 엔진의 핵심 트레이드오프: LSM-Tree & 쓰기 증폭**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 순차 쓰기 우선 설계가 필요한가)
Ⅱ. LSM-Tree 핵심 원리
Ⅲ. 쓰기 증폭 원리 및 완화 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 와이드 컬럼 스토어(HBase·Cassandra)에서 잠깐 언급했던 LSM 트리를 이번에는 심층적으로 다룬다 — B-Tree가 '읽기 최적화를 위해 데이터를 정렬된 상태로 즉시 갱신'하는 구조라면, LSM-Tree(Log-Structured Merge-Tree)는 '쓰기를 순차 append로만 처리하고 정렬·병합은 나중으로 미루는' 쓰기 최적화 구조로, 랜덤 쓰기가 치명적으로 느린 HDD와 수명이 제한된 SSD 양쪽 모두에서 B-Tree의 랜덤 I/O 문제를 회피하기 위해 고안됐다 — 그러나 이 '나중에 정리한다'는 전략은 동일한 데이터를 디스크에 여러 번 다시 쓰게 만드는 쓰기 증폭(Write Amplification)이라는 대가를 수반하며, 이 트레이드오프를 얼마나 정교하게 관리하느냐가 RocksDB·LevelDB·Cassandra 같은 현대 저장 엔진 설계의 핵심 승부처가 된 것"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.
![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzNDcuMjEzOTk5OTk5OTk5OTQgNTA4LjIwMDAwMDAwMDAwMDA1IiB3aWR0aD0iMzQ3LjIxMzk5OTk5OTk5OTk0IiBoZWlnaHQ9IjUwOC4yMDAwMDAwMDAwMDAwNSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJXcml0ZSIgZGF0YS10bz0iTWVtVGFibGUiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTczLjYwNjk5OTk5OTk5OTk3LDc2LjkgMTczLjYwNjk5OTk5OTk5OTk3LDEyNC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJNZW1UYWJsZSIgZGF0YS10bz0iTDAiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IkZsdXNoIiBwb2ludHM9IjE3My42MDY5OTk5OTk5OTk5NywxNjEuOCAxNzMuNjA2OTk5OTk5OTk5OTcsMjc4LjEiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkwwIiBkYXRhLXRvPSJMMSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iQ29tcGFjdGlvbiDrsJjrs7Ug67OR7ZWpIOyerOq4sOuhnSIgcG9pbnRzPSIxNzMuNjA2OTk5OTk5OTk5OTcsMzE1IDE3My42MDY5OTk5OTk5OTk5Nyw0MzEuMzAwMDAwMDAwMDAwMDciIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iTWVtVGFibGUiIGRhdGEtdG89IkwwIiBkYXRhLWxhYmVsPSJGbHVzaCI+CiAgPHJlY3QgeD0iMTUxLjEwNjk5OTk5OTk5OTk3IiB5PSIyMDQuOCIgd2lkdGg9IjQ0Ljk3NCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjE3My41OTM5OTk5OTk5OTk5NyIgeT0iMjE5Ljk1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5GbHVzaDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJMMCIgZGF0YS10bz0iTDEiIGRhdGEtbGFiZWw9IkNvbXBhY3Rpb24g67CY67O1IOuzke2VqSDsnqzquLDroZ0iPgogIDxyZWN0IHg9IjkzLjEwNjk5OTk5OTk5OTk5IiB5PSIzNTgiIHdpZHRoPSIxNjAuODA0MDAwMDAwMDAwMDYiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxNzMuNTA5MDAwMDAwMDAwMDEiIHk9IjM3My4xNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+Q29tcGFjdGlvbiDrsJjrs7Ug67OR7ZWpIOyerOq4sOuhnTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iV3JpdGUiIGRhdGEtbGFiZWw9IuyVsSDsk7DquLAg7JqU7LKtIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjExMy4zNTg5OTk5OTk5OTk5OCIgeT0iNDAiIHdpZHRoPSIxMjAuNDk1OTk5OTk5OTk5OTgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE3My42MDY5OTk5OTk5OTk5NyIgeT0iNTguNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyVsSDsk7DquLAg7JqU7LKtPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJNZW1UYWJsZSIgZGF0YS1sYWJlbD0iMS4g66mU66qo66asIE1lbVRhYmxlICZhbXA7IFdBTCDsiJzssKgg6riw66GdIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQyLjIyMjk5OTk5OTk5OTk1NiIgeT0iMTI0LjkiIHdpZHRoPSIyNjIuNzY4MDAwMDAwMDAwMDMiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNzMuNjA2OTk5OTk5OTk5OTciIHk9IjE0My4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+MS4g66mU66qo66asIE1lbVRhYmxlICZhbXA7IFdBTCDsiJzssKgg6riw66GdPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJMMCIgZGF0YS1sYWJlbD0iMi4g65SU7Iqk7YGsIEwwIFNTVGFibGUg67aI67OAIO2MjOydvCDsg53shLEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDAiIHk9IjI3OC4xIiB3aWR0aD0iMjY3LjIxMzk5OTk5OTk5OTk0IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTczLjYwNjk5OTk5OTk5OTk3IiB5PSIyOTYuNTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjIuIOuUlOyKpO2BrCBMMCBTU1RhYmxlIOu2iOuzgCDtjIzsnbwg7IOd7ISxPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJMMSIgZGF0YS1sYWJlbD0iMy4g7ZWY7JyEIEwxfkxuIOugiOuyqCDsnqzsoJXroKwg7YyM7J28IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU3LjQxMzQ5OTk5OTk5OTk4NSIgeT0iNDMxLjMwMDAwMDAwMDAwMDA3IiB3aWR0aD0iMjMyLjM4Njk5OTk5OTk5OTk3IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjE3My42MDY5OTk5OTk5OTk5NyIgeT0iNDQ5Ljc1MDAwMDAwMDAwMDA2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij4zLiDtlZjsnIQgTDF+TG4g66CI67KoIOyerOygleugrCDtjIzsnbw8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

***

#### Ⅱ. LSM-Tree 핵심 원리

**가. LSM-Tree 계층 구조**

```
[LSM-Tree 전체 구조]

쓰기 요청
  ↓
①WAL(Write-Ahead Log) 순차 기록
  장애 복구 대비, 앞서 다룬 ARIES WAL 원칙과 동일
  ↓
②MemTable (인메모리 정렬 구조, 보통 Skip List/Red-Black Tree)
  빠른 쓰기 응답 반환 ✅
  ↓ (MemTable 크기 임계값 도달 시)
③Immutable MemTable → Flush
  디스크에 정렬된 파일로 순차 기록
  ↓
④SSTable(Sorted String Table) 생성
  불변(Immutable) 파일 / Level 0에 누적
  ↓
⑤Compaction (백그라운드 병합)
  여러 SSTable을 병합해 상위 Level로 이동
  중복·삭제된 키 정리
  Level 0 → Level 1 → Level 2 → ...
  (레벨이 깊을수록 데이터 크기 커짐, 보통 10배씩)
```

**나. LSM-Tree 핵심 구성요소**

| 구성요소             | 역할                     | 특징                                   |
| :--------------- | :--------------------- | :----------------------------------- |
| **WAL**          | 장애 복구용 순차 로그           | 모든 쓰기를 append-only로 우선 기록            |
| **MemTable**     | 최신 쓰기를 담는 인메모리 정렬 버퍼   | 정렬된 자료구조로 빠른 삽입·조회                   |
| **SSTable**      | 디스크에 기록된 불변 정렬 파일      | 한 번 쓰면 수정 없이 병합으로만 갱신                |
| **Bloom Filter** | SSTable별 키 존재 여부 사전 확인 | 앞서 다룬 와이드 컬럼 스토어에서 다룬 불필요 디스크 I/O 회피 |
| **Compaction**   | 백그라운드에서 SSTable 병합·정리  | 읽기 성능 유지와 공간 회수의 핵심 메커니즘             |

**다. LSM-Tree vs B-Tree 비교**

| 비교 항목       | B-Tree                             | LSM-Tree                        |
| :---------- | :--------------------------------- | :------------------------------ |
| **쓰기 방식**   | 제자리 갱신(In-place Update), 랜덤 I/O 🚨 | **순차 append-only** ✅            |
| **쓰기 성능**   | 상대적으로 느림                           | **매우 빠름** ✅                     |
| **읽기 성능**   | 단일 구조 탐색, 빠름 ✅                     | 여러 레벨 탐색 필요, 상대적으로 느림 🚨        |
| **공간 활용**   | 즉시 갱신으로 효율적                        | 중복 데이터 일시 존재(Compaction 전)      |
| **적합 워크로드** | 읽기 위주(OLTP)                        | **쓰기 위주(대량 로그·이벤트)**            |
| **대표 구현**   | InnoDB(B+Tree)·PostgreSQL          | RocksDB·LevelDB·Cassandra·HBase |

***

#### Ⅲ. 쓰기 증폭 원리 및 완화 체계

**가. 쓰기 증폭(Write Amplification)의 발생 원인**

```
[쓰기 증폭 정의]

WA(Write Amplification) = 실제 디스크에 쓰인 데이터량 / 애플리케이션이 요청한 데이터량

예시: 100MB를 쓰라고 요청했는데
     WAL(100MB) + MemTable Flush(100MB)
     + Compaction 시 반복 재기록(수백MB)
     = 실제 디스크에는 500MB↑ 기록
     → WA = 5x 이상

[LSM-Tree에서 증폭이 발생하는 3단계]

①Flush 단계: MemTable → SSTable (1회 기록)
②Compaction 단계: 하위 레벨 SSTable들을 읽어
   병합 후 상위 레벨에 재기록 (반복적 재기록) ← 핵심 원인
③레벨이 깊어질수록: 동일 키가 여러 레벨을 거치며
   여러 번 다시 쓰임 (레벨당 크기 배율만큼 증폭)
```

**나. SSD 관점의 이중 쓰기 증폭**

| 계층                | 증폭 원인                                  | 비고                         |
| :---------------- | :------------------------------------- | :------------------------- |
| **소프트웨어(LSM) 계층** | Compaction으로 인한 반복 재기록                 | 애플리케이션·DB 엔진 레벨            |
| **하드웨어(SSD) 계층**  | 앞서 다룬 \*\*가비지 컬렉션(GC)\*\*으로 유효 페이지 재배치 | Flash Translation Layer 레벨 |
| **총 쓰기 증폭**       | 소프트웨어 WA × SSD 자체 WA                   | SSD 수명(TBW)에 직접 영향         |

**다. Compaction 전략별 쓰기 증폭 비교**

| Compaction 전략              | 원리                            | 쓰기 증폭    | 읽기 증폭 | 공간 증폭    |
| :------------------------- | :---------------------------- | :------- | :---- | :------- |
| **Leveled Compaction**     | 레벨별 크기 배율(보통 10x) 유지, 레벨 간 병합 | 높음 🚨    | 낮음 ✅  | **낮음** ✅ |
| **Size-Tiered Compaction** | 비슷한 크기의 SSTable끼리 병합          | **낮음** ✅ | 높음 🚨 | 높음 🚨    |
| **Universal Compaction**   | Size-Tiered의 변형, RocksDB 지원   | 중간       | 중간    | 중간       |
| **FIFO Compaction**        | 병합 없이 오래된 파일 단순 삭제(TTL 기반)    | **최소** ✅ | 최소    | 캐시·로그 특화 |

**라. 쓰기 증폭 완화 실무 기법**

| 기법                       | 원리                                                           |
| :----------------------- | :----------------------------------------------------------- |
| **레벨 크기 배율 조정**          | 배율을 낮추면(예: 10x→4x) 쓰기 증폭 감소하나 레벨 수 증가로 읽기 증폭 상승(트레이드오프)      |
| **Tiered+Leveled 하이브리드** | 상위 레벨은 Tiered로 빠르게, 하위 레벨은 Leveled로 압축(RocksDB의 Universal 등) |
| **압축(Compression) 적용**   | 실제 디스크 기록량 자체를 줄여 물리적 쓰기 증폭 완화                               |
| **SSD 오버프로비저닝**          | SSD 여유 공간 확보로 GC 부담 감소, 하드웨어 계층 증폭 완화                        |
| **워크로드 분리**              | 쓰기 위주 데이터는 LSM(Cassandra), 읽기 위주는 B-Tree(RDBMS)로 분리 배치       |

***

**(제언)** "LSM-Tree와 쓰기 증폭의 관계는 '지금 당장 빠르게 쓰기 위해 나중에 더 많이 다시 써야 하는' 시간을 미루는 부채와 같은 구조로, 이 부채를 언제 얼마나 갚을 것인가를 결정하는 것이 Compaction 전략 선택입니다. Leveled Compaction은 공간 효율과 읽기 성능이 중요한 범용 워크로드에 적합하지만 쓰기가 극단적으로 많은 시계열·로그 데이터에는 쓰기 증폭 부담이 과도할 수 있으므로, 실무에서는 데이터 접근 패턴을 먼저 분석해 쓰기 편중 워크로드에는 Size-Tiered나 FIFO Compaction을, 읽기·쓰기가 균형 잡힌 워크로드에는 Leveled를 선택하고, SSD 환경에서는 소프트웨어 쓰기 증폭과 SSD 자체 가비지 컬렉션의 이중 증폭을 함께 고려해 오버프로비저닝과 TRIM 명령 지원 여부까지 점검하는 것이 저장 엔진 설계·운영의 핵심 전략입니다.

***

**앞서 다룬 개념과의 연결**

| 연계 개념                           | 연결 내용                                         |
| :------------------------------ | :-------------------------------------------- |
| **와이드 컬럼 스토어(HBase·Cassandra)** | LSM-Tree가 이들의 핵심 저장 엔진 구조를 이루는 기반 기술          |
| **ARIES·WAL**                   | LSM-Tree의 WAL도 동일한 로그 선행 기록 원칙을 준수            |
| **이중 쓰기 버퍼**                    | 둘 다 쓰기 안전성을 위해 추가 I/O(증폭)를 감수하는 유사한 트레이드오프 철학 |
| **일관성 해싱**                      | 분산 LSM 기반 시스템에서 SSTable을 노드별로 분산 배치할 때 활용     |
| **CDC 기반 무중단 마이그레이션**           | LSM 기반 DB의 WAL을 CDC 소스로 활용해 실시간 변경 캡처         |

### **I. 고속 쓰기 전용 저장 구조, LSM-Tree와 쓰기 증폭의 개요**

전통적인 B-Tree 엔진은 무작위 쓰기(Random Write) 발생 시 디스크 덮어쓰기(In-place Update)로 인해 성능이 급격히 저하됩니다. \*\*LSM-Tree(Log-Structured Merge-Tree)\*\*는 모든 쓰기를 메모리(MemTable)와 디스크 끝에 순차(Append-only) 기록하여 쓰기 성능을 극대화합니다. 그러나 디스크에 쌓인 정렬 파일(SSTable)을 주기적으로 병합 정구하는 **컴팩션(Compaction)** 프로세스로 인해, **사용자가 요청한 실제 데이터 크기보다 훨씬 많은 양의 디스크 재기록이 발생하는 쓰기 증폭(WAF: Write Amplification Factor)** 현상이 유발됩니다.

***

### **II. 쓰기 증폭(WAF)의 메커니즘 및 컴팩션 전략**

#### **1. 쓰기 증폭 계수 (WAF: Write Amplification Factor) 정의**

WAF=스토리지(SSD/HDD)에 실제 기록된 총 바이트 수애플리케이션이 요청한 쓰기 바이트 수WAF=애플리케이션이 요청한 쓰기 바이트 수스토리지(SSD/HDD)에 실제 기록된 총 바이트 수​

* WAF가 높을수록 스토리지 I/O 병목이 심화되고, SSD의 NAND 플래시 메모리 수명(P/E Cycle)이 급격히 단축됩니다.

#### **2. LSM-Tree 컴팩션(Compaction) 전략별 WAF 영향**

| **컴팩션 전략 🔑**              | **🏁 동작 특성 및 WAF / RAF 영향 💯**                                                                          |
| :------------------------- | :------------------------------------------------------------------------------------------------------ |
| **Size-Tiered Compaction** | 비슷한 크기의 SSTable이 모이면 병합. **WAF가 상대적으로 낮음**, 읽기 증폭(RAF) 및 공간 증폭(SAF)은 증가                                 |
| **Leveled Compaction**     | 계층(L0,L1,…,Ln*L*0​,*L*1​,…,*Ln*​)별 용량을 10배씩 확정 후 하위 레벨과 중복 제거 병합. 읽기 성능 우수하나 **WAF가 매우 높음 (10\~30 이상)** |

***

### **III. B-Tree 아키텍처와 LSM-Tree 아키텍처의 상세 비교**

| **비교 항목**          | **🏛️ B-Tree (전통적 RDBMS)**         | **🚀 LSM-Tree (NoSQL / NewSQL)**         |
| :----------------- | :--------------------------------- | :--------------------------------------- |
| **디스크 I/O 패턴**     | 무작위 I/O (In-place Update 덮어쓰기)     | **순차 I/O (Append-only 전용 기록 및 병합)**      |
| **쓰기 증폭 원인 (WAF)** | 무작위 페이지 수정을 위한 WAL + 데이터 페이지 기록    | **컴팩션(Compaction) 시 SSTable 반복 읽기/재기록**  |
| **읽기 증폭 (RAF)**    | 낮음 (B-Tree 루트부터 1\~3회 트래버설로 즉시 탐색) | 높음 (MemTable + 여러 계층 SSTable 순회 필요)      |
| **주요 적합 워크로드**     | 읽기 위주(Read-Heavy) 트랜잭션 시스템         | **쓰기 위주(Write-Heavy) 대용량 로그, 이력, 분산 DB** |

***

### **IV. LSM-Tree 기반 엔진의 WAF 절감 엔지니어링 가이드라인**

1. **Key-Value 분리 저장 (WiscKey / BlobDB 아키텍처)**: LSM-Tree 컴팩션 시 데이터 부피의 대부분을 차지하는 대용량 값(Value)은 별도의 Append-only Value Log(vLog)에 보관하고, 키(Key)와 Pointer만 LSM-Tree에서 컴팩션하도록 분리하면 WAF를 획기적으로(최대 1/10 수준) 절감할 수 있습니다.
2. **블룸 필터(Bloom Filter) 및 동적 계층 조절**: 불필요한 SSTable 읽기를 막기 위해 블룸 필터를 적극 적용하고, 워크로드의 쓰기 폭주 시 컴팩션을 일시 유예하거나 동적 레벨 크기를 확장하여 병합 주기를 완화해야 합니다.
