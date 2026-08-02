### **분산 확장성과 ACID의 결합: NewSQL 아키텍처**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 RDBMS와 NoSQL 사이의 제3의 길이 필요했는가)
Ⅱ. NewSQL 핵심 아키텍처
Ⅲ. 비교 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 와이드 컬럼 스토어(Cassandra·HBase)가 'CAP의 AP 또는 CP를 선택해 확장성을 확보하는 대신 ACID 트랜잭션을 포기'한 NoSQL이라면, NewSQL은 '전통 RDBMS의 ACID 트랜잭션과 SQL 인터페이스를 유지하면서도 NoSQL 수준의 수평 확장성을 동시에 달성하려는 분산 데이터베이스 아키텍처'다 — 앞서 다룬 Raft 합의 알고리즘으로 강한 일관성을 분산 환경에서 구현하고, 앞서 다룬 일관성 해싱으로 데이터를 샤드(Shard)로 자동 분산하며, Google이 2012년 Spanner 논문으로 이 조합의 실현 가능성을 증명한 이후 CockroachDB·TiDB·YugabyteDB가 오픈소스로 이를 구현해 '확장성이냐 일관성이냐'라는 앞서 다룬 CAP 이론의 오랜 딜레마에 실용적 답을 제시한 것"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.
\
![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzODIuMDQwOTk5OTk5OTk5OTQgMzcxLjYiIHdpZHRoPSIzODIuMDQwOTk5OTk5OTk5OTQiIGhlaWdodD0iMzcxLjYiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQ2xpZW50IiBkYXRhLXRvPSJTUUxMYXllciIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxOTEuMDIwNDk5OTk5OTk5OTcsNzYuOSAxOTEuMDIwNDk5OTk5OTk5OTcsMTI0LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlNRTExheWVyIiBkYXRhLXRvPSJUeEVuZ2luZSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxOTEuMDIwNDk5OTk5OTk5OTcsMTYxLjggMTkxLjAyMDQ5OTk5OTk5OTk3LDIwOS44IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJUeEVuZ2luZSIgZGF0YS10bz0iUmFmdEdyb3VwIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE5MS4wMjA0OTk5OTk5OTk5NywyNDYuNzAwMDAwMDAwMDAwMDIgMTkxLjAyMDQ5OTk5OTk5OTk3LDI5NC43MDAwMDAwMDAwMDAwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ2xpZW50IiBkYXRhLWxhYmVsPSLtgbTrnbzsnbTslrjtirggOiDtkZzspIAgU1FMIOyniOydmCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI4NC4wODk0OTk5OTk5OTk5NyIgeT0iNDAiIHdpZHRoPSIyMTMuODYyIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTkxLjAyMDQ5OTk5OTk5OTk3IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7YG065287J207Ja47Yq4IDog7ZGc7KSAIFNRTCDsp4jsnZg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlNRTExheWVyIiBkYXRhLWxhYmVsPSIxLiDrtoTsgrAgU1FMIO2MjOyEnCAmYW1wOyDrtoTsgrAg7Ji17Yuw66eI7J207KCAIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjYxLjg1OTQ5OTk5OTk5OTk3IiB5PSIxMjQuOSIgd2lkdGg9IjI1OC4zMjIiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE5MS4wMjA0OTk5OTk5OTk5NyIgeT0iMTQzLjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij4xLiDrtoTsgrAgU1FMIO2MjOyEnCAmYW1wOyDrtoTsgrAg7Ji17Yuw66eI7J207KCAPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJUeEVuZ2luZSIgZGF0YS1sYWJlbD0iMi4g67aE7IKwIO2KuOuenOyereyFmCDsoJzslrTquLAgOiAyUEMgJmFtcDsgTVZDQyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1My43MDg0OTk5OTk5OTk5OSIgeT0iMjA5LjgiIHdpZHRoPSIyNzQuNjIzOTk5OTk5OTk5OTciIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxOTEuMDIwNDk5OTk5OTk5OTciIHk9IjIyOC4yNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Mi4g67aE7IKwIO2KuOuenOyereyFmCDsoJzslrTquLAgOiAyUEMgJmFtcDsgTVZDQzwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUmFmdEdyb3VwIiBkYXRhLWxhYmVsPSIzLiDrtoTsgrAg7IOk65OcIOyggOyepeyGjCA6IE11bHRpLVJhZnQgLyBQYXhvcyDquLDrsJgiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDAiIHk9IjI5NC43MDAwMDAwMDAwMDAwNSIgd2lkdGg9IjMwMi4wNDA5OTk5OTk5OTk5NCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxOTEuMDIwNDk5OTk5OTk5OTciIHk9IjMxMy4xNTAwMDAwMDAwMDAwMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+My4g67aE7IKwIOyDpOuTnCDsoIDsnqXshowgOiBNdWx0aS1SYWZ0IC8gUGF4b3Mg6riw67CYPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

***

#### Ⅱ. NewSQL 핵심 아키텍처

**가. NewSQL 4대 핵심 계층**

```
[NewSQL 전형적 아키텍처 계층]

①SQL 계층
  표준 SQL 파서·쿼리 옵티마이저
  앞서 다룬 RBO·CBO 기반 실행계획 생성
       ↓
②트랜잭션 계층
  분산 트랜잭션 관리(2PC 또는 최적화된 변형)
  앞서 다룬 MVCC 기반 스냅샷 격리
       ↓
③분산 합의 계층
  샤드(Range/Region)별 앞서 다룬 Raft 그룹
  각 샤드마다 독립적 리더·팔로워 복제
       ↓
④분산 스토리지 계층
  샤드 자동 분할(Auto-sharding)·재배치
  앞서 다룬 일관성 해싱 기반 데이터 배치
```

**나. 핵심 기술 구성요소**

| 구성요소                     | 원리                                                                 | 앞서 다룬 연계 개념          |
| :----------------------- | :----------------------------------------------------------------- | :------------------- |
| **자동 샤딩(Auto-Sharding)** | 데이터를 Range 또는 Hash 기준으로 자동 분할해 여러 노드에 배치 / 샤드 크기 초과 시 자동 분리(Split) | 일관성 해싱의 확장 구현        |
| **샤드별 Raft 그룹**          | 각 데이터 샤드가 독립적인 합의 그룹을 구성 / 샤드마다 별도 리더 선출                           | Raft 리더 선출·과반 쿼럼     |
| **분산 트랜잭션 프로토콜**         | 여러 샤드에 걸친 트랜잭션의 원자성 보장(2PC 또는 Percolator 방식)                       | ACID 지속성·원자성         |
| **글로벌 시계(TrueTime/HLC)** | 분산 노드 간 시간 순서를 보장하는 논리적/물리적 시계                                     | Raft Term·MVCC 타임스탬프 |
| **분산 MVCC**              | 각 샤드의 다중 버전 관리로 읽기 시 잠금 없는 스냅샷 제공                                  | 앞서 다룬 MVCC 버전 체인     |

**다. Google Spanner의 TrueTime (NewSQL 이론적 기반)**

| 개념                       | 내용                                                                      |
| :----------------------- | :---------------------------------------------------------------------- |
| **TrueTime API**         | GPS + 원자시계 기반 전역 물리 시계 / 시간 불확실성 구간(epsilon)을 명시적으로 노출                  |
| **External Consistency** | 전역적으로 트랜잭션의 커밋 순서가 실제 발생 순서와 일치함을 보장                                    |
| **Commit Wait**          | 불확실성 구간만큼 커밋을 지연시켜 전역 순서 보장 (트레이드오프: 약간의 지연 vs 강한 일관성)                  |
| **오픈소스 대안**              | CockroachDB·TiDB는 GPS 없이 \*\*HLC(Hybrid Logical Clock)\*\*로 유사 효과 근사 구현 |

***

#### Ⅲ. 비교 및 적용 체계

**가. RDBMS vs NoSQL vs NewSQL 비교**

| 비교 항목         | 전통 RDBMS         | NoSQL(Cassandra 등)  | NewSQL                   |
| :------------ | :--------------- | :------------------ | :----------------------- |
| **ACID 트랜잭션** | 완전 지원 ✅          | 미지원/제한적(BASE) 🚨    | **완전 지원** ✅              |
| **수평 확장성**    | 어려움(수직 확장 위주) 🚨 | 우수 ✅                | **우수** ✅                 |
| **SQL 인터페이스** | 표준 SQL ✅         | 제한적(CQL 등 별도 언어) 🚨 | **표준 SQL 호환** ✅          |
| **일관성 모델**    | 강한 일관성           | 결과적 일관성(AP)         | **강한 일관성(분산 환경)** ✅      |
| **CAP 선택**    | 단일 노드(해당 없음)     | AP 또는 CP            | **CP 지향(가용성 일부 트레이드오프)** |
| **적합 워크로드**   | 단일 서버 OLTP       | 대규모 비정형·시계열         | **대규모 정형 OLTP+글로벌 서비스**  |

**나. 대표 NewSQL 구현체 비교**

| 구현체                | 개발사            | 합의 알고리즘         | 특징                           |
| :----------------- | :------------- | :-------------- | :--------------------------- |
| **Google Spanner** | Google         | Paxos           | TrueTime 기반 최초 구현, 클라우드 관리형  |
| **CockroachDB**    | Cockroach Labs | **Raft**        | PostgreSQL 호환, 오픈소스          |
| **TiDB**           | PingCAP        | **Raft** (TiKV) | MySQL 호환, HTAP 지원(OLTP+OLAP) |
| **YugabyteDB**     | Yugabyte       | Raft            | PostgreSQL 호환, 클라우드 네이티브     |
| **VoltDB**         | VoltDB         | 인메모리+파티셔닝       | 초저지연 특화(합의 방식 상이)            |

**다. 적용 시나리오별 선택 기준**

| 시나리오                   | 권장 방식                           | 이유                    |
| :--------------------- | :------------------------------ | :-------------------- |
| **단일 리전·소규모 서비스**      | 전통 RDBMS                        | 불필요한 분산 복잡도 회피        |
| **글로벌 다중 리전 서비스**      | **NewSQL(Spanner·CockroachDB)** | 지역 간 강한 일관성 필요        |
| **대규모 비정형·시계열 데이터**    | NoSQL(와이드 컬럼 스토어)               | ACID보다 확장성·유연 스키마 우선  |
| **금융·주문 시스템(글로벌 확장)**  | **NewSQL**                      | ACID 필수 + 수평 확장 동시 요구 |
| **HTAP 요구(실시간 분석+거래)** | **TiDB**                        | 단일 시스템에서 OLTP·OLAP 통합 |

***

**(제언)** "NewSQL은 '분산 시스템 이론의 발전(Raft·MVCC·일관성 해싱)이 충분히 성숙했기에 CAP의 트레이드오프를 완전히 피할 수는 없어도 실용적 수준까지 완화할 수 있다'는 것을 증명한 결과물입니다. 다만 NewSQL이 제공하는 강한 일관성은 공짜가 아니어서 여러 샤드에 걸친 분산 트랜잭션은 단일 노드 RDBMS 대비 지연시간이 증가하고 TrueTime의 Commit Wait처럼 일관성을 위해 의도적으로 지연을 감수하는 설계가 필요하므로, 실무에서는 데이터 모델링 시 관련 데이터를 가능한 동일 샤드(Range)에 위치시켜 분산 트랜잭션 발생 빈도 자체를 최소화하는 스키마 설계가 성능 최적화의 핵심이며, 진정한 글로벌 서비스가 아니라면 전통 RDBMS나 단순 Read Replica 구성이 더 합리적일 수 있다는 점을 함께 고려해야 합니다.

***

**앞서 다룬 개념과의 연결**

| 연계 개념            | 연결 내용                                    |
| :--------------- | :--------------------------------------- |
| **Raft 합의 알고리즘** | NewSQL 각 샤드의 복제·리더 선출을 담당하는 핵심 엔진        |
| **일관성 해싱**       | 자동 샤딩·데이터 재배치의 이론적 기반                    |
| **MVCC·스냅샷 격리**  | 분산 환경에서 잠금 없는 읽기 일관성 제공 메커니즘             |
| **와이드 컬럼 스토어**   | NewSQL과 대비되는 NoSQL 진영의 확장성 우선 접근         |
| **스플릿 브레인·펜싱**   | NewSQL의 샤드별 Raft 그룹이 스플릿 브레인을 원천 방지하는 구조 |
