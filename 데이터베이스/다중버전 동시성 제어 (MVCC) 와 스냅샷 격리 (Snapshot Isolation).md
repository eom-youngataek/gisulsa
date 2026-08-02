#### **동시성 제어의 핵심: MVCC 와 스냅샷 격리(Snapshot Isolation)**

---

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 "잠금"보다 "버전"으로 동시성을 제어하는가)
Ⅱ. MVCC 핵심 원리 및 구조
Ⅲ. 스냅샷 격리(Snapshot Isolation) 상세
Ⅳ. 격리 수준 비교 및 이상 현상
Ⅴ. 결론 및 발전 방향
```

포인트: 개요에서 **"앞서 다룬 ACID의 격리성(Isolation)을 구현하는 전통적 방법이 '잠금(Lock) 기반 2PL(2단계 잠금)'이라면, MVCC(Multi-Version Concurrency Control)는 '데이터를 수정할 때 기존 버전을 유지한 채 새 버전을 생성해 읽기는 과거 스냅샷·쓰기는 새 버전으로 분리 처리하여 읽기-쓰기 충돌을 원천 제거'하는 패러다임이다 — 앞서 다룬 그래프 DB·분산 DB의 동시 다중 접근 환경에서 Oracle·PostgreSQL·MySQL InnoDB가 MVCC를 기본 동시성 제어 메커니즘으로 채택하는 핵심 이유"**라는 한 줄로 시작하면, 왜 이 답안이 앞서 다룬 DB 무결성·트랜잭션·성능 시리즈 전체의 **동시성 제어 핵심**인지 드러납니다.

---

#### Ⅱ. MVCC 핵심 원리 및 구조

**가. MVCC 기본 원리**

```
[MVCC 동작 원리]

기존 잠금 방식:
  Reader ──대기(Block)──▶ Writer 완료 후 접근
  Writer ──대기(Block)──▶ Reader 완료 후 수정
  → 읽기-쓰기 충돌 → 성능 저하 🚨

MVCC 방식:
  Reader ──▶ 과거 버전(Snapshot) 즉시 읽기 ✅
  Writer ──▶ 새 버전 생성 (기존 버전 유지) ✅
  → 읽기-쓰기 비충돌 → 동시성 극대화 ✅

핵심 원칙:
  "읽기는 쓰기를 막지 않는다"
  "쓰기는 읽기를 막지 않는다"
```

---

**나. MVCC 버전 구조**

|구성요소|내용|핵심 키워드|
|---|---|---|
|**트랜잭션 ID (XID)**|각 트랜잭션에 단조 증가 고유 ID 부여|PostgreSQL: txid / Oracle: SCN(System Change Number)|
|**버전 체인 (Version Chain)**|동일 행의 여러 버전을 연결리스트로 관리|최신→이전 버전 포인터 연결 / Undo 로그 기반|
|**가시성 규칙 (Visibility Rule)**|트랜잭션이 어느 버전을 볼 수 있는지 결정|시작 시점 XID 기반 / 자신보다 작은 XID만 가시|
|**Undo 로그**|이전 버전 데이터를 저장하는 공간|롤백·이전 버전 조회 모두 활용 / Oracle: Undo Segment|
|**가비지 컬렉션**|더 이상 참조되지 않는 오래된 버전 정리|PostgreSQL: VACUUM / Oracle: 자동 Undo 만료|

---

**다. PostgreSQL MVCC 구체 구조**

```
[PostgreSQL 행 버전 구조]

각 행(Tuple)이 보유하는 메타데이터:
┌─────────────────────────────────────┐
│ xmin: 이 버전을 생성한 트랜잭션 ID   │
│ xmax: 이 버전을 삭제한 트랜잭션 ID   │
│       (0이면 아직 유효)              │
│ data: 실제 데이터                    │
└─────────────────────────────────────┘

[예시: 잔액 1000→1500 수정]

트랜잭션 T1(XID=100): INSERT 잔액=1000
  → 행: xmin=100, xmax=0, data=1000

트랜잭션 T2(XID=200): UPDATE 잔액=1500
  → 기존 행: xmin=100, xmax=200, data=1000 (무효화)
  → 신규 행: xmin=200, xmax=0,   data=1500 (최신)

트랜잭션 T3(XID=150, T2 시작 전 시작):
  → xmin=100 < 150 ✅, xmax=200 > 150 ✅
  → 1000 읽기 (T2 수정 전 버전 가시)

트랜잭션 T4(XID=300, T2 완료 후 시작):
  → xmin=200 < 300 ✅, xmax=0 ✅
  → 1500 읽기 (최신 버전 가시)
```

---

#### Ⅲ. 스냅샷 격리(Snapshot Isolation) 상세

**가. 스냅샷 격리 정의**

```
[스냅샷 격리 동작 원리]

트랜잭션 시작 시점의 DB 상태를
"스냅샷(Snapshot)"으로 고정

T1 시작 ─────────────────────── T1 커밋
  │                                │
  │ 스냅샷 고정(SCN=1000)          │
  │ → 이후 다른 트랜잭션 변경 무시  │
  │                                │
  T2 시작 ─── T2 커밋(SCN=1100)   │
    잔액 변경 → T1에게 보이지 않음  │
                                   │
T1은 항상 SCN=1000 시점 데이터만 조회
→ 일관된 읽기(Consistent Read) 보장
```

---

**나. 스냅샷 격리 핵심 속성**

|속성|내용|핵심 키워드|
|---|---|---|
|**일관된 읽기**|트랜잭션 시작 시점 스냅샷 기준 일관된 조회|Consistent Read / 읽기 중 다른 변경 무시|
|**쓰기-쓰기 충돌 탐지**|동일 행을 두 트랜잭션이 수정하면 나중 커밋 차단|First-Committer-Wins 원칙|
|**Repeatable Read 보장**|같은 쿼리를 반복 실행해도 동일 결과|앞서 다룬 격리 수준 3단계 수준 달성|
|**팬텀 리드 부분 방지**|스냅샷 기반으로 대부분의 팬텀 방지|Serializable SI에서 완전 방지|

---

**다. Write Skew 이상 현상 (SI의 한계)**

```
[Write Skew 예시]

규칙: 의사 A·B 중 최소 1명은 당직 유지

초기 상태: 의사A=당직중, 의사B=당직중

T1(의사A 퇴근): 스냅샷 조회 → B 당직중 확인
                → A 당직 해제 결정
T2(의사B 퇴근): 스냅샷 조회 → A 당직중 확인
                → B 당직 해제 결정

T1 커밋 ✅ → 의사A 당직 해제
T2 커밋 ✅ → 의사B 당직 해제

결과: A·B 모두 퇴근 → 규칙 위반 🚨
      (각자 스냅샷에서는 규칙 준수처럼 보였으나
       전체적으로 일관성 위반)

→ Write Skew: SI가 방지 못하는 이상 현상
→ 해결: Serializable Snapshot Isolation (SSI)
         PostgreSQL 9.1↑ SSI 구현
```

---

#### Ⅳ. 격리 수준 비교 및 이상 현상

**가. ANSI SQL 격리 수준 4단계**

|격리 수준|Dirty Read|Non-Repeatable Read|Phantom Read|동시성|
|---|---|---|---|---|
|**Read Uncommitted**|발생 🚨|발생 🚨|발생 🚨|최고|
|**Read Committed**|방지 ✅|발생 🚨|발생 🚨|높음|
|**Repeatable Read**|방지 ✅|방지 ✅|발생 🚨|중간|
|**Serializable**|방지 ✅|방지 ✅|방지 ✅|최저|
|**Snapshot Isolation**|방지 ✅|방지 ✅|대부분 방지|높음 ✅|

---

**나. 이상 현상 5가지 상세**

```
①더티 리드 (Dirty Read)
  T1이 미커밋 데이터를 T2가 읽음
  → T1 롤백 시 T2는 존재하지 않는 데이터 사용
  → Read Uncommitted에서 발생

②반복 불가 읽기 (Non-Repeatable Read)
  T1이 같은 행을 두 번 읽는 사이 T2가 수정
  → 두 읽기 결과가 다름
  → Read Committed에서 발생

③팬텀 리드 (Phantom Read)
  T1이 같은 조건으로 두 번 조회하는 사이
  T2가 행을 삽입·삭제
  → 조회 결과 행 수가 달라짐
  → Repeatable Read에서 발생

④쓰기 왜곡 (Write Skew)
  두 트랜잭션이 각자 스냅샷 조건 확인 후
  서로 다른 행을 수정 → 전체 제약 위반
  → Snapshot Isolation에서 발생

⑤갱신 분실 (Lost Update)
  두 트랜잭션이 같은 행을 읽고 수정
  → 나중 커밋이 앞선 커밋을 덮어씀
  → MVCC + 낙관적 잠금으로 방지
```

---

**다. MVCC 구현별 비교**

| 구분                | PostgreSQL              | Oracle                    | MySQL InnoDB        |
| ----------------- | ----------------------- | ------------------------- | ------------------- |
| **버전 저장**         | 테이블 내 다중 버전(튜플)         | Undo Segment 별도           | Undo Log            |
| **스냅샷 기준**        | XID(트랜잭션 ID)            | SCN(System Change Number) | 트랜잭션 ID             |
| **기본 격리**         | Read Committed          | Read Committed            | Repeatable Read     |
| **SI 지원**         | ✅ (Repeatable Read·SSI) | ✅ (기본 동작)                 | ✅ (Repeatable Read) |
| **가비지 컬렉션**       | VACUUM 수동·자동            | 자동 Undo 만료                | Purge Thread 자동     |
| **Write Skew 방지** | SSI(9.1↑)               | SELECT FOR UPDATE         | FOR UPDATE·잠금       |


---

**라. 잠금 기반(2PL) vs MVCC 비교**

|비교 항목|2PL (잠금 기반)|MVCC|
|---|---|---|
|**읽기-쓰기 충돌**|상호 차단 🚨|비충돌 ✅|
|**동시성**|낮음|높음 ✅|
|**데드락**|발생 가능 🚨|읽기 데드락 없음 ✅|
|**오래된 버전 관리**|불필요|필요(가비지 컬렉션)|
|**쓰기-쓰기 충돌**|잠금으로 직렬화|First-Committer-Wins|
|**Write Skew**|방지(Serializable)|SI 한계·SSI로 해결|
|**일관된 읽기**|잠금 해제 후|스냅샷 기반 즉시|
|**적합 환경**|쓰기 집중·강한 일관성|읽기 집중·고동시성 OLTP|

---

#### Ⅴ. 결론 및 발전 방향

**앞서 다룬 개념과의 연결**

|연계 개념|연결 내용|
|---|---|
|**ACID 격리성**|MVCC+SI로 격리성을 잠금 없이 고성능 구현|
|**BASE·결과적 일관성**|분산 DB에서 SI를 완화해 가용성 확보|
|**Raft 합의**|분산 MVCC에서 버전 순서를 Raft로 전역 정렬|
|**CBO 옵티마이저**|MVCC Undo 버전 수가 많을수록 쿼리 비용 증가|
|**2PC**|분산 트랜잭션에서 MVCC + 2PC 결합으로 분산 격리|

**발전 방향**

```
①SSI (Serializable Snapshot Isolation)
  Write Skew 탐지 알고리즘 내장
  PostgreSQL 9.1↑ 실제 구현
  직렬화 수준 + MVCC 성능 동시 달성

②분산 MVCC
  Google Spanner: TrueTime API로 전역 시간 동기화
  CockroachDB: Hybrid Logical Clock(HLC)
  글로벌 트랜잭션 MVCC 일관성 보장

③AI 기반 버전 관리
  앞서 다룬 AIOps·자율 DB
  가비지 컬렉션 타이밍 ML 예측
  VACUUM 자동 최적화
  버전 폭발(Version Explosion) 사전 방지
```

---

#### 기술사 답안 포인트

**잠금 기반 2PL의 읽기-쓰기 충돌 한계 → MVCC(버전 체인·xmin·xmax·Undo 로그) → 스냅샷 격리(트랜잭션 시작 시점 고정·First-Committer-Wins) → 격리 수준 4단계 + SI 비교표 → 5대 이상 현상(더티·반복불가·팬텀·Write Skew·갱신분실) → SI의 Write Skew 한계·SSI로 해결 → PostgreSQL·Oracle·MySQL InnoDB 구현 비교 → Spanner 분산 MVCC·AI 자율 가비지 컬렉션** 흐름으로 서술하면 완성도 높은 답안이 됩니다. **Write Skew가 SI의 핵심 한계이며 SSI가 해결책**임을 강조하면 차별화됩니다.




#### **1. 답안 전개 스토리 (핵심 압축)**

> "읽기 트랜잭션과 쓰기 트랜잭션이 **서로 락을 걸어 길을 막지 않고(Readers do not block Writers, and vice versa), 데이터의 다차원 버전(Snapshot)을 활용해 동시에 고속 질주하게 만드는 동시성 제어 엔진**이다. 기존 락 기반은 내가 책을 수정하고 있으면 남이 읽지도 못하게 락으로 가둔다. MVCC는 원본 데이터의 수정본이 생길 때마다 **롤백 세그먼트(Undo 영역)에 이전 데이터의 과거 버전을 보관**한다. 읽기 요청이 들어오면, 내 트랜잭션 시작 시점의 타임스탬프(SCN)에 맞는 과거 조각(Snapshot)을 조용히 보여준다. 락이 없으니 조회 속도가 극상이다. 다만, 두 트랜잭션이 서로 다른 데이터 조각을 동시에 고쳐서 최종 모순이 발생하는 **'쓰기 왜곡(Write Skew) 🚨'** 이상 현상이 터질 수 있어, 이를 잡아내는 추가 거버넌스가 필요하다."

#### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5NDAuNjggMzI5LjYiIHdpZHRoPSI5NDAuNjgiIGhlaWdodD0iMzI5LjYiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Ik1WQ0NfTXVsdGlWZXJzaW9uX0NvbmN1cnJlbmN5X0NvbnRyb2xfX18iIGRhdGEtbGFiZWw9Ik1WQ0MgKE11bHRpLVZlcnNpb24gQ29uY3VycmVuY3kgQ29udHJvbCkg64+Z7IucIOydveq4sC/sk7DquLAg7J6R64+ZIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI4NjAuNjgiIGhlaWdodD0iMjQ5LjYwMDAwMDAwMDAwMDAyIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iODYwLjY4IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+TVZDQyAoTXVsdGktVmVyc2lvbiBDb25jdXJyZW5jeSBDb250cm9sKSDrj5nsi5wg7J296riwL+yTsOq4sCDsnpHrj5k8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkRBVEEiIGRhdGEtdG89IldSSVRFIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE4OC4zNTIsMjE0Ljk3NTAwMDAwMDAwMDAyIDIzNi4zNTIsMjE0Ljk3NTAwMDAwMDAwMDAyIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJXUklURSIgZGF0YS10bz0iVU5ETyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i6riw7KG0IHYxIOuNsOydtO2EsCDqsqnrpqwg64yA7ZS8IiBwb2ludHM9IjQ1Ni4xNDIsMjA4LjgyNSA0NjguMTQyLDIwOC44MjUgNDY4LjE0MiwxNzQuOCA2ODQuMTU2LDE3NC44IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJXUklURSIgZGF0YS10bz0iTkVXIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsi6Dqt5wg67KE7KCEIOuTseuhnSIgcG9pbnRzPSI0NTYuMTQyLDIyMS4xMjUgNDY4LjE0MiwyMjEuMTI1IDQ2OC4xNDIsMjU1LjE1MDAwMDAwMDAwMDAzIDY4NC4xNTYsMjU1LjE1MDAwMDAwMDAwMDAzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IldSSVRFIiBkYXRhLXRvPSJVTkRPIiBkYXRhLWxhYmVsPSLquLDsobQgdjEg642w7J207YSwIOqyqeumrCDrjIDtlLwiPgogIDxyZWN0IHg9IjUwMC4xNDIiIHk9IjE1OC44IiB3aWR0aD0iMTQwLjAxNCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjU3MC4xNDkiIHk9IjE3My45NTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+6riw7KG0IHYxIOuNsOydtO2EsCDqsqnrpqwg64yA7ZS8PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IldSSVRFIiBkYXRhLXRvPSJORVciIGRhdGEtbGFiZWw9IuyLoOq3nCDrsoTsoIQg65Ox66GdIj4KICA8cmVjdCB4PSI1MjMuOTAyIiB5PSIyMzkuMTUwMDAwMDAwMDAwMDMiIHdpZHRoPSI5Mi40OTQwMDAwMDAwMDAwMyIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjU3MC4xNDkiIHk9IjI1NC4zMDAwMDAwMDAwMDAwNCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7Iug6recIOuyhOyghCDrk7HroZ08L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkRBVEEiIGRhdGEtbGFiZWw9IuuNsOydtO2EsCDtlokgWF92MSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iMTk2LjUyNSIgd2lkdGg9IjEzMi4zNTIiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMjIuMTc2IiB5PSIyMTQuOTc1MDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuuNsOydtO2EsCDtlokgWF92MTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iV1JJVEUiIGRhdGEtbGFiZWw9Iu2KuOuenOyereyFmCBBOiBY66W8IDIw7Jy866GcIOyImOyglSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyMzYuMzUyIiB5PSIxOTYuNTI1IiB3aWR0aD0iMjE5Ljc5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzQ2LjI0NyIgeT0iMjE0Ljk3NTAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7tirjrnpzsnq3shZggQTogWOulvCAyMOycvOuhnCDsiJjsoJU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlVORE8iIGRhdGEtbGFiZWw9IuKcqCBVbmRvIOuhpOuwsSDshLjqt7jrqLztirgg4pyoCuqzvOqxsCDrsoTsoIQgWF92MSDrs7TqtIAiIGRhdGEtc2hhcGU9ImN5bGluZGVyIj4KICA8cmVjdCB4PSI2ODQuMTU2IiB5PSIxNDcuOSIgd2lkdGg9IjIwMC41MjQiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDEiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0ibm9uZSIgLz4KICA8bGluZSB4MT0iNjg0LjE1NiIgeTE9IjE0Ny45IiB4Mj0iNjg0LjE1NiIgeTI9IjIwMS43MDAwMDAwMDAwMDAwMiIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8bGluZSB4MT0iODg0LjY4IiB5MT0iMTQ3LjkiIHgyPSI4ODQuNjgiIHkyPSIyMDEuNzAwMDAwMDAwMDAwMDIiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPGVsbGlwc2UgY3g9Ijc4NC40MTc5OTk5OTk5OTk5IiBjeT0iMjAxLjcwMDAwMDAwMDAwMDAyIiByeD0iMTAwLjI2MiIgcnk9IjciIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPGVsbGlwc2UgY3g9Ijc4NC40MTc5OTk5OTk5OTk5IiBjeT0iMTQ3LjkiIHJ4PSIxMDAuMjYyIiByeT0iNyIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI3ODQuNDE3OTk5OTk5OTk5OSIgeT0iMTc0LjgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9Ijc4NC40MTc5OTk5OTk5OTk5IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+4pyoIFVuZG8g66Gk67CxIOyEuOq3uOuovO2KuCDinKg8L3RzcGFuPjx0c3BhbiB4PSI3ODQuNDE3OTk5OTk5OTk5OSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+6rO86rGwIOuyhOyghCBYX3YxIOuztOq0gDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJORVciIGRhdGEtbGFiZWw9IuuNsOydtO2EsCDtlokgWF92MiDsl4XrjbDsnbTtirgiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNjg0LjE1NiIgeT0iMjM2LjcwMDAwMDAwMDAwMDAyIiB3aWR0aD0iMTk4LjMwMSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9Ijc4My4zMDY0OTk5OTk5OTk5IiB5PSIyNTUuMTUwMDAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuuNsOydtO2EsCDtlokgWF92MiDsl4XrjbDsnbTtirg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJFQUQiIGRhdGEtbGFiZWw9Iu2KuOuenOyereyFmCBCOiBYIOydveq4sCDsmpTssq0iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMTkwLjE0OTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjE1MS4wNzUiIHk9IjEwMi40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7Yq4656c7J6t7IWYIEI6IFgg7J296riwIOyalOyyrTwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

| **핵심 척도**      | **📊 MVCC (다중 버전 제어) 🚨**                                                               | **🔑 스냅샷 격리 (Snapshot Isolation) 🚨**                                                             | **🏁 쓰기 왜곡 (Write Skew) 이상 현상 💯**                                                                    |
| :------------- | :-------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------- |
| **동시성 해법**     | 락 대기 없이 데이터의 다중 버전 이력을 유지하여 동시 읽기/쓰기 성능을 극대화함.                                          | 트랜잭션 시작 시점의 스냅샷을 기준으로 데이터를 읽으며, 커밋 시점에 충돌이 없으면 기록함.                                               | 스냅샷 격리 수준에서 발생하는 독특한 동시성 제어 실패에 따른 무결성 붕괴 이상 현상.                                                      |
| **세부 메커니즘 🚨** | **\[Undo 영역 활용 🚨]** 오라클의 Undo Tablespace, MySQL의 Rollback Segment에 과거 버전을 보존 및 체이닝 연결. | **\[First-committer-wins 💯]** 동일 행에 대해 두 트랜잭션이 동시에 쓰기를 시도하면, **먼저 커밋을 요청한 쪽만 승리**시키고 늦은 쪽은 무효화함. | **\[Write Skew (쓰기 왜곡) 💯]** 두 트랜잭션이 서로 다른 두 행을 동시에 수정하여 비즈니스 논리적 제약(예: 두 계좌의 합은 0원 이상이어야 함)이 깨지는 현상. |

* **(제언)** "MVCC 환경에서 쓰기 왜곡(Write Skew)을 완벽히 방어하려면 개발자가 조회 쿼리 시점에 **`SELECT ... FOR UPDATE`** **구문을 작성해 명시적으로 비관적 락을 유도하거나, 트랜잭션 격리 수준을 최종 단계인 'Serializable'로 승격시켜 직렬화 검증망을 강제해야 합니다.**"
