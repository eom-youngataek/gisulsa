
#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 "같은 SQL"이 다르게 실행되는가)
Ⅱ. RBO vs CBO 핵심 원리 비교
Ⅲ. CBO 동작 메커니즘 상세
Ⅳ. 실행계획 수립 및 최적화 기법
Ⅴ. 결론 및 발전 방향
```

포인트: 개요에서 **"앞서 다룬 데이터베이스 성능 관점에서 동일한 SQL이 수백 배 성능 차이를 내는 핵심 원인이 바로 옵티마이저(Optimizer)의 실행계획(Execution Plan) 선택이다 — RBO(Rule-Based Optimizer)가 '사전에 정의된 우선순위 규칙에 따라 기계적으로 실행계획을 수립'한다면, CBO(Cost-Based Optimizer)는 '통계 정보 기반으로 예상 비용을 수치화해 가장 낮은 비용의 실행계획을 동적으로 선택'하며, 현대 RDBMS(Oracle·PostgreSQL·MySQL)는 CBO를 기본 옵티마이저로 채택하되 통계 정보의 정확성이 CBO 성능의 핵심 변수"**라는 한 줄로 시작하면, 왜 이 답안이 앞서 다룬 DB 성능·최적화 시리즈 전체의 **쿼리 실행 핵심**인지 드러납니다.

---

#### Ⅱ. RBO vs CBO 핵심 원리 비교

**가. 개념 비교**

| ==구분==         | ==RBO (Rule-Based Optimizer)==     | ==CBO (Cost-Based Optimizer)==        |
| ---------- | ------------------------------ | --------------------------------- |
| **정의**     | 사전 정의된 **우선순위 규칙**에 따라 실행계획 수립 | **통계 정보 기반 비용 모델**로 최적 실행계획 선택    |
| **판단 기준**  | 규칙 우선순위(Rule Priority)         | 예상 비용(Estimated Cost·I/O·CPU·메모리) |
| **통계 정보**  | 불필요                            | **필수** (테이블·인덱스·컬럼 통계)            |
| **유연성**    | 낮음(규칙 고정)                      | 높음(데이터 분포 반영)                     |
| **예측 가능성** | 높음(동일 입력→동일 계획)                | 낮음(통계 변화→계획 변경)                   |



---

**나. RBO 15대 우선순위 규칙 (Oracle 기준)**

```
[RBO 규칙 우선순위 (높을수록 먼저 선택)]

1위  ROWID에 의한 단일 행 접근
2위  클러스터 조인에 의한 단일 행
3위  유일 인덱스(Unique Index) 동등 조건
4위  유일 클러스터 키에 의한 단일 행
5위  클러스터 키에 의한 단일 행
6위  해시 클러스터 키에 의한 단일 행
7위  인덱스 클러스터 키
8위  복합 인덱스(Composite Index)
9위  단일 컬럼 인덱스
10위 인덱스 범위 스캔(Range Scan)
...
15위 전체 테이블 스캔(Full Table Scan)

→ 문제점: 소규모 테이블이라도 인덱스가 있으면
           무조건 인덱스 스캔 선택 → 오히려 느릴 수 있음
```

---

#### Ⅲ. CBO 동작 메커니즘 상세

**가. CBO 동작 4단계==(파수실비)==**

```
[CBO 실행계획 수립 과정]

①파싱(Parsing)
  SQL 문법 검사·시맨틱 분석
  공유 풀(Shared Pool) 하드파싱·소프트파싱
       ↓
②통계 정보 수집
  딕셔너리(Data Dictionary)에서 통계 조회
  테이블 통계·인덱스 통계·컬럼 통계·시스템 통계
       ↓
③후보 실행계획 생성
  조인 순서·조인 방법·접근 경로 조합
  N개 테이블 → N! 조합 중 휴리스틱 제거 후 후보 선정
       ↓
④비용 계산·최적 계획 선택
  각 후보 계획의 예상 I/O·CPU·메모리 비용 계산
  총 비용 최소 계획 선택 → 실행
```

---

**나. CBO 비용 계산 핵심 요소**

| 비용 요소                       | 내용             | 핵심 지표                                    |
| --------------------------- | -------------- | ---------------------------------------- |
| ==**선택도 (Selectivity)**==   | 조건에 맞는 행 비율 예측 | 선택도 = 반환 행수 / 전체 행수 / 낮을수록 인덱스 유리        |
| ==**카디널리티 (Cardinality)**== | 예상 반환 행 수      | 카디널리티 = 전체 행수 × 선택도                      |
| ==**I/O 비용**==              | 디스크 읽기 블록 수 예측 | Full Scan: 전체 블록 / Index Scan: 인덱스 높이+리프 |
| ==**CPU 비용**==              | 연산 처리 비용       | 정렬·해시·집계 연산량                             |
| ==**네트워크 비용**==             | 분산 DB 환경 전송 비용 | 노드 간 데이터 전송량                             |

---

**다. 통계 정보 종류 및 관리**

| 통계 유형      | 수집 항목                      | 수집 명령                          |
| ---------- | -------------------------- | ------------------------------ |
| ==**테이블 통계**== | 총 행수(NUM_ROWS)·블록수·평균 행 길이 | ANALYZE TABLE / DBMS_STATS     |
| ==**인덱스 통계**== | 높이(HEIGHT)·리프 블록수·클러스터링 팩터 | ANALYZE INDEX                  |
| ==**컬럼 통계**==  | 최소·최대·NULL수·NDV(중복 제거 값 수) | DBMS_STATS.GATHER_TABLE_STATS  |
| ==**히스토그램**==  | 컬럼 값 분포(편향 분포 탐지)          | METHOD_OPT → FOR ALL COLUMNS   |
| ==**시스템 통계**== | CPU 속도·I/O 속도·멀티블록 읽기 크기   | DBMS_STATS.GATHER_SYSTEM_STATS |

```
[통계 미갱신 시 CBO 오작동 예시]

현실: 테이블 행수 1억 건 (대용량)
통계: 1천 건으로 오래된 통계 정보 유지
      ↓
CBO: "소규모 테이블이니 Full Scan이 유리"로 판단
결과: 1억 건 Full Scan 실행 → 심각한 성능 저하 🚨
해결: 통계 정기 갱신·자동 통계 수집 스케줄 설정
```

---

#### Ⅳ. 실행계획 수립 및 최적화 기법

**가. 접근 경로 선택 비교**

| 접근 경로                     | 선택 조건               | 비용 특성                |
| ------------------------- | ------------------- | -------------------- |
| ==**Full Table Scan**==   | 대량 데이터 조회·인덱스 없음    | 멀티블록 I/O·대용량 유리      |
| ==**Index Range Scan**==  | 범위 조건(BETWEEN·<·>)  | 소량 데이터·선택도 낮을 때      |
| ==**Index Unique Scan**== | 유일 조건(=·PK)         | 단일 행 접근·최고 효율        |
| ==**Index Full Scan**==   | ORDER BY·인덱스 정렬 활용  | 소트 대체·커버링 인덱스        |
| ==**Index Skip Scan**==   | 복합 인덱스 선두 컬럼 미사용    | Oracle 특화·카디널리티 낮을 때 |
| ==**Bitmap Index Scan**== | 저카디널리티·복수 조건 AND/OR | DW·분석 쿼리 특화          |
|                           |                     |                      |

---

**나. 조인 방법 비교**

| ==조인 방법==                | 동작 원리                 | 최적 조건             |
| ------------------------ | --------------------- | ----------------- |
| ==**Nested Loop Join**== | 외부 테이블 순회 → 내부 인덱스 조회 | 소량·인덱스 존재·OLTP    |
| ==**Sort Merge Join**==  | 양쪽 정렬 후 병합            | 대용량·비등가 조인·인덱스 없음 |
| ==**Hash Join**==        | 작은 테이블 해시→큰 테이블 탐색    | 대용량 동등 조인·메모리 충분  |
| ==**Cartesian Join**==   | 조인 조건 없음·전체 곱         | 피해야 할 패턴 🚨       |

---

**다. 힌트(Hint) 활용 — CBO 제어**

sql

```sql
-- CBO가 잘못된 계획을 선택할 때 힌트로 강제 제어
SELECT /*+ INDEX(emp emp_dept_idx) */
       emp_name, dept_id
FROM   emp
WHERE  dept_id = 10;

-- 주요 힌트 종류
/*+ FULL(table) */        -- Full Table Scan 강제
/*+ INDEX(table idx) */   -- 인덱스 사용 강제
/*+ USE_NL(table) */      -- Nested Loop Join 강제
/*+ USE_HASH(table) */    -- Hash Join 강제
/*+ LEADING(table) */     -- 조인 순서 강제
/*+ PARALLEL(table, n) */ -- 병렬 처리 강제
```

---

**라. 실행계획 확인 및 분석**

sql

```sql
-- Oracle
EXPLAIN PLAN FOR SELECT ...;
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);

-- PostgreSQL
EXPLAIN ANALYZE SELECT ...;

-- MySQL
EXPLAIN SELECT ...;

[실행계획 분석 포인트]
① COST 값: 높을수록 비용 큰 단계
② ROWS: 예상 행수 vs 실제 행수 차이 확인
③ WIDTH: 행 평균 크기
④ Full Scan: 대용량 테이블 Full Scan 경고
⑤ 조인 순서: 작은 테이블이 Driving 테이블인가
```

---

#### Ⅴ. 결론 및 발전 방향

**RBO vs CBO 종합 비교표**

|비교 항목|RBO|CBO|
|---|---|---|
|**판단 기준**|규칙 우선순위|통계 기반 비용|
|**통계 필요**|불필요|필수|
|**데이터 분포 반영**|불가 🚨|가능 ✅|
|**대용량 데이터**|부적합 🚨|적합 ✅|
|**예측 가능성**|높음|통계 의존|
|**튜닝 방법**|SQL 재작성|통계 갱신·힌트|
|**현재 사용**|레거시 시스템|현대 RDBMS 표준 ✅|

**발전 방향**

```
CBO 진화 방향:

①머신러닝 기반 옵티마이저
  과거 실행 통계 학습 → 실행계획 품질 예측
  구글 Bao·Microsoft Learned Cardinalities

②적응형 실행계획(Adaptive Query Processing)
  실행 중 실제 행수 vs 예측 행수 차이 탐지
  → 실행 중 실행계획 동적 변경
  Oracle 12c↑ Adaptive Plans

③AI 기반 자율 튜닝(Autonomous Database)
  Oracle Autonomous DB: AI가 통계 갱신·힌트·파라미터 자동 조정
  앞서 다룬 MLOps·AIOps 철학의 DB 적용

④분산 DB 옵티마이저
  앞서 다룬 CXL·분산 트랜잭션 환경의
  네트워크 비용·데이터 배치 고려 멀티노드 실행계획
```

**앞서 다룬 개념과의 연결**

|연계 개념|연결 내용|
|---|---|
|**DB 성능 관점**|인덱스·파티셔닝·샤딩과 결합해 CBO 비용 최소화|
|**통계 정보 관리**|MLOps 데이터 드리프트처럼 통계 오래되면 CBO 오작동|
|**AI 자율 튜닝**|AIOps·자율DB가 CBO 한계(통계 의존)를 ML로 극복|
|**ACID·트랜잭션**|옵티마이저가 선택한 실행계획이 트랜잭션 성능 직결|

---

#### 기술사 답안 포인트

**RBO(규칙 15단계 우선순위·통계 불필요·예측 가능) vs CBO(통계 기반 비용 계산·동적 선택·통계 정확성이 핵심) → CBO 4단계(파싱→통계수집→후보생성→비용계산) → 선택도·카디널리티·I/O·CPU 비용 요소 → 접근 경로(Full·Index Range·Unique·Skip) → 조인 방법(NL·Sort Merge·Hash) → 힌트로 CBO 제어 → 통계 미갱신=CBO 오작동 → ML 기반·Adaptive·자율DB 발전** 흐름으로 서술하면 DB 성능 최적화를 아우르는 완성도 높은 답안이 됩니다. **통계 정보 정확성이 CBO 성능의 핵심 변수**임을 강조하면 차별화됩니다.



#### **1. 답안 전개 스토리 (핵심 압축)**

> "우리가 작성한 SQL 쿼리문을 보고 \*\*"어떻게 해야 가장 빠른 지름길로 데이터를 찾아올지" 경로를 짜주는 DB 컴파일러(옵티마이저)의 양대 최적화 뇌(Brain)\*\*다. 첫째, **'규칙기반 옵티마이저(RBO)'**. 미리 정해진 15가지 우선순위 규칙(예: 기본키 인덱스 스캔이 Full Table 스캔보다 무조건 좋다)에 따라 기계적으로 길을 찾는다. 데이터가 몇 만 건이 있든 상관없이 규칙만 보므로 멍청하게 비효율적인 경로를 잡기 쉽다. 둘째, **'비용기반 옵티마이저(CBO) 🚨'**. 테이블 안에 데이터가 몇 건 들었는지 통계 정보(CPU, I/O 소모량)를 실시간 계산하여 가장 돈(비용)이 적게 드는 최적 경로를 계산한다. CBO가 똑똑하게 작동하려면 DB 통계 정보를 상시 최신화해 주어야 하며, 튜너가 직접 실행 경로를 강제하는 **'힌트(Hint)'** 제어법이 튜닝의 핵심이다."

#### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDI0LjQwNyAzMzQuMTQzIiB3aWR0aD0iMTAyNC40MDciIGhlaWdodD0iMzM0LjE0MyIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iU1FMX09wdGltaXplcl9fX18iIGRhdGEtbGFiZWw9IlNRTCBPcHRpbWl6ZXIg7Iuk7ZaJIOqzhO2ajSDsiJjrpr0g67aE6riwIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI5NDQuNDA2OTk5OTk5OTk5OSIgaGVpZ2h0PSIyNTQuMTQyOTk5OTk5OTk5OTciIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI5NDQuNDA2OTk5OTk5OTk5OSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPlNRTCBPcHRpbWl6ZXIg7Iuk7ZaJIOqzhO2ajSDsiJjrpr0g67aE6riwPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTUUwiIGRhdGEtdG89Ik9QVCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyMzUuMDM0OTk5OTk5OTk5OTcsMTgxLjA3MTUgMjgzLjAzNDk5OTk5OTk5OTk3LDE4MS4wNzE1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJPUFQiIGRhdGEtdG89IlJCTyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iMS4g7Jqw7ISg7Iic7JyEIOq3nOy5mSDsnZjsobQiIHBvaW50cz0iNDQ0LjgyMDgzMzMzMzMzMzI3LDE0OC43MTQzMzMzMzMzMzMzMSA0ODkuMTc3OTk5OTk5OTk5OTQsMTQ4LjcxNDMzMzMzMzMzMzMxIDQ4OS4xNzc5OTk5OTk5OTk5NCwxMzEuNzIxNSA3MDYuMzgsMTMxLjcyMTUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209Ik9QVCIgZGF0YS10bz0iQ0JPIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIyLiDrjbDsnbTthLAg7Ya16rOEL+u5hOyaqSDqs4TsgrAiIHBvaW50cz0iNDQ0LjgyMDgzMzMzMzMzMzMsMjEzLjQyODY2NjY2NjY2NjYzIDQ4OS4xNzc5OTk5OTk5OTk5NCwyMTMuNDI4NjY2NjY2NjY2NjMgNDg5LjE3Nzk5OTk5OTk5OTk0LDIzMC40MjE0OTk5OTk5OTk5NSA3MDYuMzgsMjMwLjQyMTQ5OTk5OTk5OTk4IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209Ik9QVCIgZGF0YS10bz0iUkJPIiBkYXRhLWxhYmVsPSIxLiDsmrDshKDsiJzsnIQg6rec7LmZIOydmOyhtCI+CiAgPHJlY3QgeD0iNTMwLjM4NSIgeT0iMTE1LjcyMTQ5OTk5OTk5OTk2IiB3aWR0aD0iMTIyLjc4ODAwMDAwMDAwMDA0IiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTkxLjc3OSIgeT0iMTMwLjg3MTQ5OTk5OTk5OTk3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij4xLiDsmrDshKDsiJzsnIQg6rec7LmZIOydmOyhtDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJPUFQiIGRhdGEtdG89IkNCTyIgZGF0YS1sYWJlbD0iMi4g642w7J207YSwIO2GteqzhC/ruYTsmqkg6rOE7IKwIj4KICA8cmVjdCB4PSI1MjEuMTc4IiB5PSIyMTQuNDIxNDk5OTk5OTk5OTUiIHdpZHRoPSIxNDEuMjAyMDAwMDAwMDAwMDMiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1OTEuNzc5IiB5PSIyMjkuNTcxNDk5OTk5OTk5OTYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjIuIOuNsOydtO2EsCDthrXqs4Qv67mE7JqpIOqzhOyCsDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU1FMIiBkYXRhLWxhYmVsPSLsgqzsmqnsnpAgU1FMIOyniOydmCDsnoXroKUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9IjE2Mi42MjE0OTk5OTk5OTk5NyIgd2lkdGg9IjE3OS4wMzQ5OTk5OTk5OTk5NyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE0NS41MTc0OTk5OTk5OTk5OCIgeT0iMTgxLjA3MTQ5OTk5OTk5OTk2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7sgqzsmqnsnpAgU1FMIOyniOydmCDsnoXroKU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik9QVCIgZGF0YS1sYWJlbD0i4pyoIERCIOyYte2LsOuniOydtOyggCDinKgiIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iMzgwLjEwNjUsODQgNDc3LjE3OCwxODEuMDcxNSAzODAuMTA2NSwyNzguMTQzIDI4My4wMzQ5OTk5OTk5OTk5NywxODEuMDcxNSIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzgwLjEwNjUiIHk9IjE4MS4wNzE1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7inKggREIg7Ji17Yuw66eI7J207KCAIOKcqDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUkJPIiBkYXRhLWxhYmVsPSLinKggUkJPIOq3nOy5meq4sOuwmCDinKgK642w7J207YSwIO2GteqzhCDrrLTsi5wgLyAxNeqwgOyngCDro7DshYsg6rOg7KCVCuKelCDsnLXthrXshLEg7JeG64qUIOqzoOyglSDsi6Ttlokg6rOE7ZqNIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjcwNi4zOCIgeT0iOTYuMzcxNDk5OTk5OTk5OTciIHdpZHRoPSIyNjIuMDI3IiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iODM3LjM5MzUiIHk9IjEzMS43MjE0OTk5OTk5OTk5NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iODM3LjM5MzUiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj7inKggUkJPIOq3nOy5meq4sOuwmCDinKg8L3RzcGFuPjx0c3BhbiB4PSI4MzcuMzkzNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+642w7J207YSwIO2GteqzhCDrrLTsi5wgLyAxNeqwgOyngCDro7DshYsg6rOg7KCVPC90c3Bhbj48dHNwYW4geD0iODM3LjM5MzUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuKelCDsnLXthrXshLEg7JeG64qUIOqzoOyglSDsi6Ttlokg6rOE7ZqNPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkNCTyIgZGF0YS1sYWJlbD0i4pyoIENCTyDruYTsmqnquLDrsJgg8J+aqCDinKgKQ2FyZGluYXJpdHksIENQVSwgSS9PIOu5hOyaqSDsgrDstpwK4p6UIOuPmeyggSDstZzsoIEg7Iuk7ZaJIOqzhO2ajSDrj4Tstpwg8J+agCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3MDYuMzgiIHk9IjE5NS4wNzE0OTk5OTk5OTk5NiIgd2lkdGg9IjIzMy4xMjgiIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjgyMi45NDQiIHk9IjIzMC40MjE0OTk5OTk5OTk5NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iODIyLjk0NCIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPuKcqCBDQk8g67mE7Jqp6riw67CYIPCfmqgg4pyoPC90c3Bhbj48dHNwYW4geD0iODIyLjk0NCIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+Q2FyZGluYXJpdHksIENQVSwgSS9PIOu5hOyaqSDsgrDstpw8L3RzcGFuPjx0c3BhbiB4PSI4MjIuOTQ0IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7inpQg64+Z7KCBIOy1nOyggSDsi6Ttlokg6rOE7ZqNIOuPhOy2nCDwn5qAPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

| **핵심 척도**      | **📊 규칙기반 옵티마이저 (RBO)**                                       | **🔑 비용기반 옵티마이저 (CBO) 🚨**                                                       | **🏁 실행 계획 (Execution Plan) 💯**                                                         |     |
| :------------- | :------------------------------------------------------------ | :------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------- | --- |
| **최적화 판단 기준**  | **'사전 정의된 규칙 순위'.** 인덱스 유무, 조인 연산자 형태 등 구조적 규칙 15단계 순위에만 의존함. | **'예상 소요 비용 (Cost) 💯'.** 디스크 I/O 횟수, CPU 연산 시간, 테이블 행 수 통계 기반 최소 비용 경로 선택.      | 옵티마이저가 최종 선택한 SQL 실행 로드맵 (인덱스 스캔 방향, 조인 방식인 Hash/Nested Loop 표기).                        |     |
| **단점 / 관리 요건** | 데이터 분포량이 바뀌어도 무조건 규칙만 따르므로 대량 데이터 검색 시 성능 참사 발생.              | **\[통계 정보의 최신성 요구 🚨]** 통계가 옛날 것에 머물러 있으면 엉뚱한 실행 계획을 세우므로 정기적 **ANALYZE** 갱신 필수. | 옵티마이저가 멍청한 계획을 세웠을 때, 쿼리 내부에 `/*+ INDEX(t idx_col) */` 같은 **Hint(힌트) 💯**를 주입해 수동 강제 제어. |     |

* **(제언)** "현대 상용 RDBMS의 99%는 CBO가 기본 탑재되어 작동합니다. **안정적인 쿼리 성능 유지를 위해 대량의 배치 데이터가 적재된 직후에는 반드시 통계 수집 명령어(예: Oracle** **`DBMS_STATS`)를 구동해 데이터 분포 실태를 옵티마이저에게 실시간 업데이트해 주어야 합니다.**"
