### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (트랜잭션정의, ACID의역할) — 3~4줄
Ⅱ. ACID 4대속성 (본론①, 도식 1개 필수)
Ⅲ. 격리성(I)심화 - 격리수준4단계, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

트랜잭션은 **"논리적으로하나의작업단위"**입니다 — 앞서다룬 **"계좌이체"**처럼, **"출금+입금"** 두동작이 **"둘다성공하거나,둘다실패해야"** 합니다 — ACID는 이런 트랜잭션이 지켜야할 **4가지약속**입니다.

### Ⅱ. ACID 4대속성

| 속성                   | 내용                                               |
| :------------------- | :----------------------------------------------- |
| **원자성**(Atomicity)   | 트랜잭션은 **전부성공하거나전부실패**(All-or-Nothing)— 중간상태로남지않음 |
| **일관성**(Consistency) | 트랜잭션전후로 **데이터베이스의규칙(무결성제약)이항상유지**됨               |
| **격리성**(Isolation)   | 동시에실행되는 **여러트랜잭션이서로간섭하지않음**                      |
| **지속성**(Durability)  | 커밋된트랜잭션의결과는 **영구적으로저장**(장애가나도사라지지않음)             |

→ 암기: **"전부하거나안하거나(A),규칙은항상지켜지고(C),서로안건드리고(I),한번저장되면영원히남는다(D)"** — 앞서다룬 **"개체·참조·도메인무결성"**이 바로 \*\*"C(일관성)"\*\*가 지켜야할 그 **"규칙"**입니다.

### 도식화 제안

```
[계좌이체 트랜잭션]
BEGIN TRANSACTION
  출금(A계좌, -1000)
  입금(B계좌, +1000)
COMMIT

[원자성] 둘다성공 or 둘다실패(하나만성공한상태로안남음)
[일관성] 이체후에도 "전체계좌합계"는변함없음(무결성유지)
[격리성] 다른트랜잭션이 이체중간의"돈이잠깐사라진상태"를못봄
[지속성] COMMIT후 정전이나도 이체결과는영구보존
```

### Ⅲ. 격리성(I) 심화 — 격리수준4단계, 핵심 배점

**함정 방지: "서로간섭안한다"고만답하면절반. 격리를"완벽하게"하면성능이떨어지므로, 그정도를조절하는4단계와각단계가허용하는이상현상을보여줘야완성됩니다.**

| 격리수준                 | 허용되는이상현상                                | 성능   |
| :------------------- | :-------------------------------------- | :--- |
| **READ UNCOMMITTED** | **DirtyRead**(커밋안된데이터도읽힘)               | 가장빠름 |
| **READ COMMITTED**   | **NonRepeatableRead**(같은트랜잭션내같은쿼리결과가바뀜) | 빠름   |
| **REPEATABLE READ**  | **PhantomRead**(같은조건조회시 새로운행이나타남)       | 중간   |
| **SERIALIZABLE**     | 없음(완벽한격리)                               | 가장느림 |

→ 암기: **"밑에서부터, 더러운읽기허용→반복읽기불일치허용→유령행허용→완벽격리"** — 앞서다룬 \*\*"TOCTOU"\*\*에서 다룬 **"검사시점과사용시점사이의틈"**이, 바로 이 **격리수준이낮을수록그틈이더넓어져 이상현상이더많이발생**하는 것입니다 — 앞서다룬 \*\*"TCP혼잡제어의트레이드오프"\*\*처럼, **격리성도완벽할수록느려지므로, 상황에맞는수준을선택**해야합니다.

### 도식화 제안

```
[격리수준과 성능/안전성 트레이드오프]
READ UNCOMMITTED ──────────────────→ SERIALIZABLE
(빠름,위험한이상현상다허용)         (느림,이상현상완전차단)

[Dirty Read 예시]
트랜잭션A: 계좌잔액을 1000→2000으로변경(아직커밋안함)
트랜잭션B: 그2000을읽음(READUNCOMMITTED)
트랜잭션A: 롤백(취소!) → 실제론1000인데, B는 2000을읽은채로진행됨(오류)
```

### Ⅳ. 결론

ACID는 **"트랜잭션이지켜야할4가지약속(원자성,일관성,격리성,지속성)"**이며, 이중 \*\*격리성(I)\*\*은 **"완벽하게격리할수록안전하지만느려지는"** 트레이드오프를가져, **4단계격리수준중 상황에맞는것**을 선택해야합니다 — 이는 앞서다룬 **"무결성제약조건에서제약을엄격히할수록성능이떨어진다"**는 논리와 정확히같은구조이며, 앞서다룬 \*\*"MSA에서전통적FK를못쓴다"\*\*는 문제도, 사실 **"분산환경에서 ACID의A(원자성)를 여러DB에걸쳐보장하기어렵다"**는 근본적인 어려움에서 비롯됩니다 — 이는 다음으로 자연스럽게 **"분산트랜잭션(2PC),SAGA패턴,CAP정리"**같은 주제로 이어집니다.


답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 "ACID"로는 부족한가) — 3~4줄
Ⅱ. BASE 4대 속성 체계 (본론①, 도식 1개 필수)
Ⅲ. ACID와의 비교·CAP 정리 연계·BASE 적용 흐름 (핵심 배점)
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 2PC(2단계 커밋)가 '분산 환경에서도 ACID의 완벽한 일관성(Consistency)을 지키기 위해 모든 노드가 동의할 때까지 블로킹'하는 강한 일관성 모델이라면, BASE는 CAP 정리의 '일관성(C)·가용성(A)·분단 허용(P) 중 셋을 동시에 만족할 수 없다'는 수학적 한계를 인정하고, 일관성을 일시적으로 포기하는 대신 가용성과 확장성을 극대화하는 결과적 일관성(Eventual Consistency) 모델이다 — 아마존·넷플릭스·카카오처럼 수억 명이 동시 접속하는 서비스가 DynamoDB·Cassandra·Redis 기반으로 멈추지 않고 동작할 수 있는 이유가 바로 BASE"\*\*라는 한 줄로 시작하면, 왜 이 답안이 앞서 다룬 2PC·CAP·NoSQL 시리즈 전체의 **일관성 트레이드오프 핵심**인지 드러납니다.

***

#### Ⅱ. BASE 4대 속성 체계

| 속성          | 영문                            | 내용                                                                                                                                                  |
| :---------- | :---------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| **기본적 가용성** | **B**asically **A**vailable   | 시스템이 일부 노드 장애·네트워크 분단 상황에서도 **항상 응답을 반환**. 응답이 최신 데이터가 아닐 수 있지만 **서비스 중단(Downtime)은 없음**. 앞서 다룬 2PC의 블로킹(Blocking) 문제를 근본적으로 회피                     |
| **소프트 상태**  | **S**oft State                | 시스템 상태가 **시간이 지남에 따라 변할 수 있음**. 외부 입력 없이도 노드 간 데이터 동기화 과정에서 상태가 자동 변화. ACID의 지속성(Durability)처럼 **즉각적·영구적 확정을 요구하지 않음**                              |
| **결과적 일관성** | **E**ventual Consistency      | 일정 시간이 지나면 **모든 노드가 동일한 데이터 상태로 수렴**. 즉각 일관성(Immediate Consistency)이 아닌 **수렴 일관성(Convergent Consistency)**. DNS 전파·소셜미디어 좋아요 수가 대표 사례               |
| *(어원 보충)*   | **S**oft State → **E**ventual | BASE = Basically Available + Soft State + Eventual Consistency. \*\*ACID(산성)의 반대말 BASE(염기성)\*\*로 작명 — 화학적 대비를 통해 두 철학의 충돌을 표현한 Eric Brewer의 의도적 네이밍 |

→ 암기: **"일단 응답하고(BA), 상태는 흔들려도 되고(S), 언젠가는 맞춰진다(E) — ACID가 강산이라면 BASE는 강염기, 둘 다 극단이고 현실은 그 사이 어딘가"** — 앞서 다룬 \*\*"CAP 정리의 AP 선택"\*\*이 실제로 시스템 설계에서 BASE 철학을 채택하는 것과 동일한 의미입니다.

#### 도식화 제안

```
[CAP 정리와 BASE의 관계]

         Consistency (일관성)
              /\
             /  \
            / CA \  ← RDBMS·2PC
           /------\
          /   CP   \  ← HBase·Zookeeper
         /----------\
        /     AP     \  ← DynamoDB·Cassandra·Couchbase
       /──────────────\  ← BASE 채택 영역
Availability ────── Partition Tolerance
   (가용성)          (분단 허용)

BASE = AP를 선택한 분산 시스템의 일관성 철학
     = Basically Available + Soft State + Eventual Consistency
     = "즉각 일관성 포기 → 가용성·확장성 극대화"
```

***

#### Ⅲ. ACID와의 비교·CAP 정리 연계·BASE 적용 흐름 — 핵심 배점

**함정 방지: "BASE는 ACID와 반대"라고만 답하면 절반. 결과적 일관성이 실제로 어떤 메커니즘(벡터 클록·머클 트리·읽기 복구·안티엔트로피)으로 구현되는지, 그리고 어떤 도메인에서 BASE를 선택하고 어디서는 ACID를 고수해야 하는지를 단계별로 보여줘야 완성됩니다.**

| 단계           | 활동                                                                                                                                                 |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| **쓰기 분산**    | 클라이언트가 데이터를 쓰면 **복수 노드에 비동기 복제**. 앞서 다룬 2PC처럼 모든 노드의 동의를 기다리지 않고 **N개 중 W개 노드 쓰기 성공(Quorum Write)** 시 즉시 응답 반환                                     |
| **버전 충돌 추적** | **벡터 클록(Vector Clock)** 또는 \*\*MVCC(Multi-Version Concurrency Control)\*\*로 노드 간 데이터 버전 추적. 충돌(Conflict) 발생 시 Last Write Wins(LWW) 또는 애플리케이션 레벨 병합 |
| **안티엔트로피**   | **안티엔트로피(Anti-Entropy) 프로세스** — 백그라운드에서 노드 간 데이터를 지속 비교·동기화. 앞서 다룬 \*\*"머클 트리(Merkle Tree)"\*\*로 불일치 구간을 효율적으로 탐지해 전송량 최소화                         |
| **읽기 복구**    | 클라이언트 읽기 시 여러 노드 응답 비교 → 오래된 노드에 최신 데이터를 자동 업데이트하는 **읽기 복구(Read Repair)** 수행 → 결과적 일관성 수렴 가속                                                       |
| **수렴 시간 관리** | 결과적 일관성의 수렴 시간(Convergence Time)을 **SLA로 명시**. 예) "최대 500ms 내 전체 노드 동기화 보장". 수렴 시간이 비즈니스 허용 범위를 초과하면 BASE 적용 부적합 도메인                               |

→ 암기: **"쓸 때는 W개만 받고 응답하고, 버전 충돌은 벡터 클록으로 추적하고, 백그라운드 안티엔트로피가 머클 트리로 차이를 좁히고, 읽을 때 읽기 복구로 낡은 노드를 고친다 — 이 4가지가 결과적 일관성의 실제 구현 엔진"**

**ACID vs BASE 핵심 대비** (중요): 앞서 다룬 \*\*"2PC의 블로킹 문제"\*\*에서 조정자(Coordinator) 장애 시 모든 참여 노드가 락을 쥔 채 무한 대기하는 치명적 한계가 있었다면, BASE 시스템은 조정자 자체가 없고 **각 노드가 자율적으로 동작하며 언젠가 수렴** — 이는 앞서 다룬 \*\*"마이크로서비스(MSA)의 Saga 패턴"\*\*이 각 서비스가 로컬 트랜잭션을 독립 실행하고 실패 시 보상 트랜잭션으로 결과적 일관성을 맞추는 것과 정확히 동일한 철학입니다.

### **1. 답안 전개 스토리**

> "은행 계좌이체 사고를 막기 위해 DB 트랜잭션(작업 단위)이 반드시 지켜야 할 4대 절대 원칙이다. 첫째, **원자성(A)**. 내 통장에서 돈이 빠졌으면 상대방 통장에도 무조건 들어가야 한다. 중간에 끊기면 아예 처음으로 싹 다 취소(All or Nothing)시킨다. 둘째, **일관성(C)**. 이체 전후로 두 사람의 잔액 합계는 룰에 맞게 항상 똑같아야 한다. 셋째, **고립성(I)**. 내가 이체하는 도중에 다른 놈이 몰래 끼어들어 잔액을 건드리지 못하게 완벽히 격리(Lock)한다. 넷째, **영속성(D)**. 이체가 성공(Commit)되었다면, 그 직후 은행 서버에 벼락이 떨어져 폭발해도 내 이체 기록은 영원히 살아남아야 한다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 신뢰할 수 있는 데이터 처리의 기준, 트랜잭션 ACID 개요**

* **정의:** 트랜잭션(Transaction)이란 데이터베이스의 상태를 변화시키는 논리적인 작업의 단위이며, ACID는 이 트랜잭션이 안전하게 수행되기 위해 보장해야 하는 4가지 핵심 속성.
* **목적:** 동시다발적인 사용자의 요청과 예기치 못한 시스템 장애(정전, 디스크 고장) 속에서도 데이터의 무결성과 신뢰성을 100% 보장하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) All or Nothing, 원자성(Atomicity) 파이프라인**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5MzAuNjI4IDI5Mi41IiB3aWR0aD0iOTMwLjYyOCIgaGVpZ2h0PSIyOTIuNSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX0FfXyIgZGF0YS1sYWJlbD0i7Yq4656c7J6t7IWY7J2YIEEo7JuQ7J6Q7ISxKSDrs7TsnqUg66ek7Luk64uI7KaYIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI4NTAuNjI4IiBoZWlnaHQ9IjIxMi41IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iODUwLjYyOCIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPu2KuOuenOyereyFmOydmCBBKOybkOyekOyEsSkg67O07J6lIOunpOy7pOuLiOymmDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iU1RBUlQiIGRhdGEtdG89IlQxIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE1OS40NTMsMTU2LjAyNSAyMDcuNDUzLDE1Ni4wMjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlQxIiBkYXRhLXRvPSJUMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzNDcuOTU2LDE1Ni4wMjUgMzk1Ljk1NiwxNTYuMDI1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJUMiIgZGF0YS10bz0iQ09NTUlUIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLinKgg7ISx6rO1IOKcqCIgcG9pbnRzPSI1MzYuNDU5MDAwMDAwMDAwMSwxNDcuMDU4MzMzMzMzMzMzMzQgNTQ4LjQ1OTAwMDAwMDAwMDEsMTQ3LjA1ODMzMzMzMzMzMzM0IDU0OC40NTkwMDAwMDAwMDAxLDExMC45IDcwNy40NDkwMDAwMDAwMDAxLDExMC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJUMiIgZGF0YS10bz0iUk9MTEJBQ0siIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsl5Drn6wg67Cc7IOdIOyLnCEiIHBvaW50cz0iNTM2LjQ1OTAwMDAwMDAwMDEsMTY0Ljk5MTY2NjY2NjY2NjY3IDU0OC40NTkwMDAwMDAwMDAxLDE2NC45OTE2NjY2NjY2NjY2NyA1NDguNDU5MDAwMDAwMDAwMSwyMDEuMTUgNzA3LjQ0OTAwMDAwMDAwMDEsMjAxLjE1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iVDIiIGRhdGEtdG89IkNPTU1JVCIgZGF0YS1sYWJlbD0i4pyoIOyEseqztSDinKgiPgogIDxyZWN0IHg9IjU4Ny41ODcwMDAwMDAwMDAxIiB5PSI5NC45IiB3aWR0aD0iNjguNzM0MDAwMDAwMDAwMDEiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI2MjEuOTU0MDAwMDAwMDAwMSIgeT0iMTEwLjA1MDAwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7inKgg7ISx6rO1IOKcqDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJUMiIgZGF0YS10bz0iUk9MTEJBQ0siIGRhdGEtbGFiZWw9IuyXkOufrCDrsJzsg50g7IucISI+CiAgPHJlY3QgeD0iNTgwLjQ1OTAwMDAwMDAwMDEiIHk9IjE4NS4xNSIgd2lkdGg9IjgyLjk5MDAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjIxLjk1NDAwMDAwMDAwMDEiIHk9IjIwMC4zIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7sl5Drn6wg67Cc7IOdIOyLnCE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlNUQVJUIiBkYXRhLWxhYmVsPSLsnbTssrQg7Iuc7J6RIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIxMzcuNTc1IiB3aWR0aD0iMTAzLjQ1MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTA3LjcyNjUiIHk9IjE1Ni4wMjQ5OTk5OTk5OTk5OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7J207LK0IOyLnOyekTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iVDEiIGRhdGEtbGFiZWw9IuuCtCDqs4Tsoozsl5DshJwKMeunjCDsm5Ag7Lac6riIIOyZhOujjCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyMDcuNDUzIiB5PSIxMjkuMTI1IiB3aWR0aD0iMTQwLjUwMyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjc3LjcwNDUiIHk9IjE1Ni4wMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjI3Ny43MDQ1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+64K0IOqzhOyijOyXkOyEnDwvdHNwYW4+PHRzcGFuIHg9IjI3Ny43MDQ1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj4x66eMIOybkCDstpzquIgg7JmE66OMPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlQyIiBkYXRhLWxhYmVsPSLsg4HrjIDrsKkg6rOE7KKM7JeQCjHrp4wg7JuQIOyeheq4iCDsi5zrj4QiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzk1Ljk1NiIgeT0iMTI5LjEyNSIgd2lkdGg9IjE0MC41MDMiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQ2Ni4yMDc1IiB5PSIxNTYuMDI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0NjYuMjA3NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuyDgeuMgOuwqSDqs4Tsoozsl5A8L3RzcGFuPjx0c3BhbiB4PSI0NjYuMjA3NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+MeunjCDsm5Ag7J6F6riIIOyLnOuPhDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDT01NSVQiIGRhdGEtbGFiZWw9IkNPTU1JVArsnbTssrQg7JmE7KCEIOyiheujjCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3MDcuNDQ5MDAwMDAwMDAwMSIgeT0iODQiIHdpZHRoPSIxMzUuMzE2IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9Ijc3NS4xMDcwMDAwMDAwMDAxIiB5PSIxMTAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNzc1LjEwNzAwMDAwMDAwMDEiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5DT01NSVQ8L3RzcGFuPjx0c3BhbiB4PSI3NzUuMTA3MDAwMDAwMDAwMSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7J207LK0IOyZhOyghCDsooXro4w8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUk9MTEJBQ0siIGRhdGEtbGFiZWw9IlJPTExCQUNLIPCfkqMK7Lac6riI7ZaI642YIOqyg+uPhCDsi7kg64ukCuybkOyDgeuzteq1rCDsi5zsvJzrsoTrprwhIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjcwNy40NDkwMDAwMDAwMDAxIiB5PSIxNjUuOCIgd2lkdGg9IjE2Ny4xNzkiIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9Ijc5MS4wMzg1MDAwMDAwMDAxIiB5PSIyMDEuMTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9Ijc5MS4wMzg1MDAwMDAwMDAxIiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+Uk9MTEJBQ0sg8J+SozwvdHNwYW4+PHRzcGFuIHg9Ijc5MS4wMzg1MDAwMDAwMDAxIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7stpzquIjtlojrjZgg6rKD64+EIOyLuSDri6Q8L3RzcGFuPjx0c3BhbiB4PSI3OTEuMDM4NTAwMDAwMDAwMSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7JuQ7IOB67O16rWsIOyLnOy8nOuyhOumvCE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 트랜잭션의 4대 절대 원칙, A.C.I.D 전격 해부 (표)**

이 토픽은 4가지 특징의 정의뿐만 아니라, **이를 보장하기 위해 DBMS가 사용하는 구체적인 '보장 기법'**을 매핑하는 것이 1순위 득점 포인트입니다.

| **핵심 척도**    | **🅰️ 원자성 (Atomicity)**                                                                | **🅲 일관성 (Consistency)**                                                   | **🅸 고립성 (Isolation) 🚨**                                                        | **🅳 영속성 (Durability)**                                                |
| :----------- | :------------------------------------------------------------------------------------- | :------------------------------------------------------------------------- | :------------------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| **개념**       | **All or Nothing.** 트랜잭션 내의 작업들은 모두 완벽히 끝까지 수행되거나, 단 하나라도 실패하면 아예 시작 전 상태로 모두 취소되어야 함. | **무결성 유지.** 트랜잭션이 성공적으로 완료되면 언제나 일관성 있는(규칙과 제약조건을 위배하지 않는) DB 상태로 변환되어야 함. | **서로 간섭 불가 💯.** 둘 이상의 트랜잭션이 동시에 실행될 때, 남의 작업이 끝날 때까지 중간 진행 결과를 볼 수도, 끼어들 수도 없음. | **영원한 기록.** 트랜잭션이 성공(Commit)했다면, 그 직후 시스템이 다운되어도 결과는 디스크에 영원히 보존되어야 함. |
| **장애 요소**    | 중간에 쿼리 에러 발생                                                                           | 기본키, 외래키 위반                                                                | 동시에 같은 데이터를 수정                                                                   | 디스크 뻑남, 서버 정전                                                          |
| **보장 기법 💯** | **\[회복(Recovery) 기법]** Undo 로그를 이용한 Rollback.                                          | **\[무결성 제약조건]** PK, FK, CHECK 제약조건 등.                                      | **\[동시성 제어(Concurrency)]** Locking, 격리수준(Isolation Level).                       | **\[회복(Recovery) 기법]** Redo 로그를 이용한 데이터 복구.                            |

#### **IV. \[결론/제언] 클라우드 분산 환경(NoSQL)에서의 ACID 포기와 BASE 원칙의 부상**

* **(키워드 위주 2줄 마무리)** "전통적 RDBMS는 ACID를 완벽히 지키느라 분산 확장이 매우 어렵습니다. 이에 빅데이터와 클라우드를 다루는 NoSQL 진영에서는 완벽한 C(일관성)를 과감히 포기하고 가용성과 성능에 올인하는 **'BASE 원칙(결과적 일관성)'을 채택하여 글로벌 스케일의 대규모 트랜잭션을 처리하고 있습니다.**"


**I. 대규모 분산 데이터의 일관성 패러다임, BASE의 개요**

분산 시스템의 CAP 정리(CAP Theorem)에 따르면 일관성(C)과 가용성(A), 파티션 허용성(P)을 동시에 완벽히 만족할 수 없습니다. **BASE**는 대용량 트래픽 처리가 필요한 NoSQL 데이터베이스가 서비스 가용성(A)과 분산 확장성(P)을 우선 확보하기 위해 설계된 느슨한 트랜잭션 모델로, 데이터의 즉각적인 강한 일관성을 포기하는 대신 \*\*최종적으로 일관성이 정렬되는 결과적 일관성(Eventual Consistency)\*\*을 채택합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3OTAuOTk4NDk5OTk5OTk5OSAyODYuNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSI3OTAuOTk4NDk5OTk5OTk5OSIgaGVpZ2h0PSIyODYuNzAwMDAwMDAwMDAwMDUiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUk9PVCIgZGF0YS10bz0iQUNJRCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzODcuMTYyOTk5OTk5OTk5OTUsNzYuOSAzODcuMTYyOTk5OTk5OTk5OTUsMTAwLjkgMjAyLjg3NjQ5OTk5OTk5OTk2LDEwMC45IDIwMi44NzY0OTk5OTk5OTk5NiwxMjQuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUk9PVCIgZGF0YS10bz0iQkFTRSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzODcuMTYyOTk5OTk5OTk5OTUsNzYuOSAzODcuMTYyOTk5OTk5OTk5OTUsMTAwLjkgNTcxLjQ0OTUsMTAwLjkgNTcxLjQ0OTUsMTI0LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkJBU0UiIGRhdGEtdG89IkV2ZW50dWFsIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjU3MS40NDk1LDE2MS44IDU3MS40NDk1LDIwOS44IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJST09UIiBkYXRhLWxhYmVsPSLrtoTsgrAg642w7J207YSwIO2KuOuenOyereyFmCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyOTcuMjc1IiB5PSI0MCIgd2lkdGg9IjE3OS43NzU5OTk5OTk5OTk5OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzg3LjE2Mjk5OTk5OTk5OTk1IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+67aE7IKwIOuNsOydtO2EsCDtirjrnpzsnq3shZg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkFDSUQiIGRhdGEtbGFiZWw9IkFDSUQgOiBSREJNUyDquLDrsJgg6rCV7ZWcIOydvOq0gOyEsSwgQ0FQ7J2YIEMg7KeA7ZalIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwIiB5PSIxMjQuOSIgd2lkdGg9IjMyNS43NTI5OTk5OTk5OTk5MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjIwMi44NzY0OTk5OTk5OTk5NiIgeT0iMTQzLjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5BQ0lEIDogUkRCTVMg6riw67CYIOqwle2VnCDsnbzqtIDshLEsIENBUOydmCBDIOyngO2WpTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQkFTRSIgZGF0YS1sYWJlbD0iQkFTRSA6IE5vU1FMIOq4sOuwmCDqsrDqs7zsoIEg7J286rSA7ISxLCBDQVDsnZggQS1QIOyngO2WpSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzOTMuNzUyOTk5OTk5OTk5OTMiIHk9IjEyNC45IiB3aWR0aD0iMzU1LjM5MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI1NzEuNDQ5NSIgeT0iMTQzLjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5CQVNFIDogTm9TUUwg6riw67CYIOqysOqzvOyggSDsnbzqtIDshLEsIENBUOydmCBBLVAg7KeA7ZalPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJFdmVudHVhbCIgZGF0YS1sYWJlbD0i6rKw6rO87KCBIOydvOq0gOyEsSA6IOu5hOuPmeq4sCDrj5nquLDtmZQg6rGw7LOQIOy1nOyihSDsnbzsuZgg64us7ISxIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM5MS45MDA0OTk5OTk5OTk5NyIgeT0iMjA5LjgiIHdpZHRoPSIzNTkuMDk3OTk5OTk5OTk5OTYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1NzEuNDQ5NSIgeT0iMjI4LjI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7qsrDqs7zsoIEg7J286rSA7ISxIDog67mE64+Z6riwIOuPmeq4sO2ZlCDqsbDss5Ag7LWc7KKFIOydvOy5mCDri6zshLE8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

***

### **II. BASE 모델의 3대 핵심 속성**

| **🔑 BASE 핵심 속성 🚨**                  | **🏁 상세 내용 및 분산 제어 동작 💯**                                                    |
| :------------------------------------ | :---------------------------------------------------------------------------- |
| **1. Basically Available** (기본적 가용성)  | 분산 노드 중 일부가 정전/네트워크 장애를 겪어도, 시스템 전체는 완전 정지하지 않고 동작 가능한 영역에 대해 응답을 지속 보장       |
| **2. Soft State** (소프트 상태)            | 외부의 명시적인 변경 입력이 없더라도, 노드 간 비동기 복제(Replication) 프로세스로 인해 데이터 상태가 유동적으로 변할 수 있음 |
| **3. Eventual Consistency** (결과적 일관성) | 일시적으로 노드 간 데이터 불일치가 발생하지만, 일정 시간이 흐르면 결국 모든 노드가 동일한 최신 데이터 값으로 일치됨을 보장        |

***

### **III. RDBMS의 ACID 모델과 NoSQL의 BASE 모델 상세 비교**

| **비교 항목**      | **🏛️ ACID (Relational DB 모델)** | **☁️ BASE (Distributed NoSQL 모델)** |
| :------------- | :------------------------------ | :--------------------------------- |
| **일관성 강도**     | 강한 즉시 일관성 (Immediate/Strong)    | 느슨한 결과적 일관성 (Eventual Consistency) |
| **가용성 우선 순위**  | 데이터 정확성 최우선 (장애 발생 시 락 대기)      | 가용성 및 성능 최우선 (오류 데이터라도 즉각 응답)      |
| **트랜잭션 복잡도**   | 복잡함 (2-Phase Commit 등 오버헤드 유발)  | 단순함 (비동기 가십 프로토콜 등을 통한 전파)         |
| **적합 서비스 도메인** | 은행 금융 원장, 증권 주문, 철도 예약 시스템      | 소셜 미디어 피드, 장바구니 리스트, 클릭 스트림        |

***

### **IV. BASE 적용 분산 데이터의 데이터 충돌 제어 방안**

**IMPORTANT**

1. **벡터 클락(Vector Clock)을 통한 데이터 충돌 식별**: 비동기 쓰기가 병렬 발생하여 결과적 일관성이 깨질 때, 각 노드의 업데이트 버전 카운터를 맵 형태로 누적한 벡터 클락 정보를 패킷에 실어 최신 본을 판별하고 충돌 시 병합 로직을 동작시켜야 합니다.
2. **CRDT(Conflict-free Replicated Data Type)의 도입**: 분산 노드가 네트워크 단선 상태에서 합의 과정 없이 각자 로컬 쓰기를 수행한 뒤, 재연동되었을 때 수학적으로 별도의 격전 없이 자동 병합되는 CRDT(예: Counter, LWW-Element-Set) 데이터 구조를 적용하는 것이 시스템 안정성에 유리합니다.
