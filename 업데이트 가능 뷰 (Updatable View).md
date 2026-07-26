### **데이터베이스 뷰 고급 기법: 업데이트 가능 뷰 & WITH CHECK OPTION**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 뷰를 통한 데이터 수정이 위험할 수 있는가)
Ⅱ. 업데이트 가능 뷰 핵심 원리
Ⅲ. WITH CHECK OPTION 핵심 원리
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 트리거·어설션이 '이벤트·상태 기반 무결성 제어'라면, 업데이트 가능 뷰(Updatable View)와 WITH CHECK OPTION은 '뷰(View)라는 가상 테이블을 통해 데이터를 수정할 때 원본 테이블 무결성과 뷰 정의 일관성을 동시에 보장하는 접근 제어 메커니즘'이다 — 뷰는 SELECT 결과를 가상 테이블로 노출하는 보안·추상화 도구이나, 뷰를 통해 INSERT·UPDATE·DELETE가 가능한 업데이트 가능 뷰는 수정 후 해당 행이 뷰 조건을 벗어나는 '유령 행(Phantom Write)' 문제가 발생하며, WITH CHECK OPTION이 '뷰 조건을 벗어나는 DML을 원천 차단'하는 선언적 무결성 보장 수단"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.

***

#### Ⅱ. 업데이트 가능 뷰 핵심 원리

**가. 뷰 업데이트 가능 조건**

```
[업데이트 가능 뷰 조건 (SQL 표준)]

✅ 업데이트 가능:
  단일 테이블 기반
  GROUP BY·HAVING·DISTINCT 없음
  집계 함수(SUM·COUNT) 없음
  서브쿼리 없음 (일부 RDBMS 예외)
  UNION·INTERSECT·EXCEPT 없음
  기본키 또는 고유키 포함

🚨 업데이트 불가:
  다중 테이블 JOIN (일부 RDBMS 가능)
  집계·그룹화 포함
  DISTINCT 포함
  산술 표현식 컬럼 (price*1.1)
```

***

**나. 유령 행(Phantom Write) 문제**

sql

```
-- 서울 직원만 노출하는 뷰
CREATE VIEW seoul_employees AS
SELECT emp_id, name, city, salary
FROM   employees
WHERE  city = '서울';

-- 뷰를 통해 UPDATE
UPDATE seoul_employees
SET    city = '부산'       -- 서울→부산으로 변경
WHERE  emp_id = 101;

-- 결과: 해당 행이 뷰에서 사라짐 🚨
-- 뷰 조건(city='서울')을 벗어난 유령 행 발생
-- 데이터는 변경됐으나 뷰로 확인 불가 → 혼란
```

***

#### Ⅲ. WITH CHECK OPTION 핵심 원리

**가. WITH CHECK OPTION 핵심 체계**

| **핵심 척도**   | **📊 LOCAL vs CASCADED 🚨**                                                                                                            | **🔑 동작 메커니즘 🚨**                                                                                                                          | **🏁 적용 효과 💯**                                                                                                                   |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| **핵심 정의**   | **WITH LOCAL CHECK OPTION**: 현재 뷰 조건만 검사 / 상위 뷰 조건 무시 / **WITH CASCADED CHECK OPTION**: 현재 + 모든 상위 뷰 조건 검사 / SQL 표준 기본값 / 더 엄격한 무결성 보장 | **INSERT 차단**: 뷰 조건 불만족 행 삽입 거부 / **UPDATE 차단**: 수정 후 뷰 조건 벗어나면 거부 / **DELETE**: 조건 무관 (삭제는 뷰에서 사라지므로 허용) / 앞서 다룬 **트리거 BEFORE** 검증과 유사 효과 | **유령 행 방지**: city='서울' 뷰에 city='부산' UPDATE 차단 ✅ / **데이터 일관성**: 뷰에서 보이는 행만 수정 가능 / **보안 강화**: 앞서 다룬 **RBAC** 연계 / 부서별 뷰로 접근 데이터 제한 |
| **중첩 뷰 차이** | **LOCAL 예시**: 뷰B가 뷰A 기반 / 뷰B WITH LOCAL CHECK: 뷰B 조건만 검사 / 뷰A 조건 위반 가능 🚨                                                              | **CASCADED 예시**: 뷰B WITH CASCADED CHECK: 뷰A+뷰B 조건 모두 검사 / 중첩 뷰 전체 무결성 보장 ✅                                                                 | **실무 권장**: CASCADED 기본 사용 / 보안 민감 데이터는 CASCADED 필수 / 앞서 다룬 **개인정보 안전조치** 접근통제 연계                                                  |

***

**나. SQL 예시 및 동작**

sql

```
-- WITH CHECK OPTION 적용 뷰
CREATE VIEW seoul_employees AS
SELECT emp_id, name, city, salary
FROM   employees
WHERE  city = '서울'
WITH CHECK OPTION;          -- CASCADED 기본값

-- ①INSERT 차단
INSERT INTO seoul_employees(emp_id, name, city, salary)
VALUES (201, '박지성', '부산', 3000);
-- ERROR: CHECK OPTION failed 🚨 (city≠'서울')

-- ②INSERT 성공
INSERT INTO seoul_employees(emp_id, name, city, salary)
VALUES (202, '이영희', '서울', 3500);
-- SUCCESS ✅ (city='서울' 조건 충족)

-- ③UPDATE 차단 (유령 행 방지)
UPDATE seoul_employees
SET    city = '대전'
WHERE  emp_id = 101;
-- ERROR: CHECK OPTION failed 🚨 (수정 후 city≠'서울')

-- ④UPDATE 성공
UPDATE seoul_employees
SET    salary = 4000        -- city는 유지
WHERE  emp_id = 101;
-- SUCCESS ✅ (city='서울' 조건 유지)

-- ⑤중첩 뷰 + CASCADED 예시
CREATE VIEW high_salary_seoul AS
SELECT emp_id, name, city, salary
FROM   seoul_employees      -- 뷰 기반 뷰
WHERE  salary >= 3000
WITH CASCADED CHECK OPTION; -- city='서울' AND salary>=3000 모두 검사

INSERT INTO high_salary_seoul VALUES(301,'김민준','서울', 2000);
-- ERROR: salary<3000 🚨

INSERT INTO high_salary_seoul VALUES(301,'김민준','부산', 4000);
-- ERROR: city≠'서울' 🚨 (CASCADED로 상위 뷰 조건도 검사)
```

***

**다. 전체 동작 도식화**

```
[업데이트 가능 뷰 + WITH CHECK OPTION 구조]

사용자 DML (INSERT/UPDATE)
       ↓
WITH CHECK OPTION 검사
  ┌────────────────────────────┐
  │ 수정/삽입 후 행이           │
  │ 뷰 WHERE 조건 충족하는가?   │
  └────────────────────────────┘
       ↓YES              ↓NO
  원본 테이블 반영      ERROR 반환
  (DML 성공) ✅         (DML 차단) 🚨

[LOCAL vs CASCADED 차이]

뷰A: WHERE city='서울'  (CHECK OPTION 없음)
  └─ 뷰B: WHERE salary>=3000
        WITH LOCAL CHECK OPTION

LOCAL:    salary>=3000만 검사
          city='부산' INSERT → 성공 🚨 (뷰A 조건 무시)

CASCADED: city='서울' AND salary>=3000 모두 검사
          city='부산' INSERT → 차단 ✅
```

***

**다. 앞서 다룬 개념과의 연결**

| 연계 개념         | 연결 내용                                             |
| :------------ | :------------------------------------------------ |
| **트리거·어설션**   | WITH CHECK OPTION = 선언적 뷰 무결성 / 트리거 = 절차적 이벤트 무결성 |
| **RBAC·접근통제** | 뷰로 컬럼·행 필터링 + CHECK OPTION으로 수정 범위 제한             |
| **5NF·무결성**   | 뷰 기반 무결성 = 스키마 설계 무결성의 런타임 보완                     |
| **개인정보 안전조치** | 부서별 뷰로 PII 컬럼 은닉 + CHECK OPTION으로 타 부서 데이터 수정 차단  |

***

**(제언)** "업데이트 가능 뷰와 WITH CHECK OPTION은 '보안 필터링과 데이터 무결성을 뷰 레이어에서 선언적으로 동시에 달성하는 우아한 DB 설계 도구'입니다. **앞서 다룬 개인정보 안전조치의 접근통제 요건을 RBAC 권한+부서별 뷰+WITH CASCADED CHECK OPTION의 3중 계층으로 구현하고, 앞서 다룬 트리거와 역할을 분담해 복잡한 비즈니스 규칙은 트리거로, 뷰 범위 일관성은 WITH CHECK OPTION으로 처리하는 것이 DB 무결성 설계의 핵심 전략입니다.**"
