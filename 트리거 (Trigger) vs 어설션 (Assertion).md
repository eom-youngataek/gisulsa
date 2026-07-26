### **트리거 (Trigger) vs 어설션 (Assertion)**

#### **데이터베이스 무결성 제어 메커니즘: 트리거 vs 어설션**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 제약조건만으로는 복잡한 무결성을 보장 못 하는가)
Ⅱ. 트리거 vs 어설션 핵심 비교
Ⅲ. 실무 적용 및 한계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 ACID의 무결성(Consistency)을 보장하는 기본 수단이 PRIMARY KEY·FOREIGN KEY·CHECK 제약조건이라면, 트리거(Trigger)는 '특정 이벤트 발생 시 자동 실행되는 사용자 정의 프로시저'로 제약조건으로 표현 못하는 복잡한 비즈니스 규칙을 강제하고, 어설션(Assertion)은 '데이터베이스 전체 상태에 항상 성립해야 하는 전역 조건을 선언하는 SQL 표준 객체'다 — 트리거가 '행위 기반(이벤트 후 처리)'이라면 어설션은 '상태 기반(조건 항상 참)' — 이 차이가 설계 철학의 근본 분기이며, 어설션은 SQL 표준에 정의됐으나 대부분 RDBMS가 미구현해 실무에서는 트리거로 대체 구현하는 것이 현실"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.

***

#### Ⅱ. 트리거 vs 어설션 핵심 비교

**가. 정의 및 구조**

```
[트리거 구조]
CREATE TRIGGER 트리거명
  {BEFORE | AFTER | INSTEAD OF}  ← 실행 시점
  {INSERT | UPDATE | DELETE}      ← 이벤트
  ON 테이블명
  [FOR EACH ROW | FOR EACH STATEMENT]
BEGIN
  -- 실행할 SQL·로직
END;

[어설션 구조 (SQL 표준)]
CREATE ASSERTION 어설션명
  CHECK (조건식);  ← DB 전체 상태에 항상 성립
-- 예: 급여 합계가 예산 초과 불가
CREATE ASSERTION 급여제한
  CHECK (
    (SELECT SUM(salary) FROM employee) <= 1000000
  );
```

***

**나. 핵심 비교**

| **핵심 척도** | **📊 트리거 (Trigger) 🚨**                                                                              | **🔑 어설션 (Assertion) 🚨**                                                                          | **🏁 실무 선택 기준 💯**                                                                 |
| :-------- | :--------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------- |
| **실행 방식** | **이벤트 기반**: INSERT·UPDATE·DELETE 발생 시 자동 실행 / BEFORE(사전 검증·변환)·AFTER(사후 처리·감사) / INSTEAD OF(뷰 갱신 처리) | **상태 기반**: 모든 DML 트랜잭션 후 조건식 항상 검증 / 조건 위반 시 트랜잭션 전체 롤백 / 테이블 단위가 아닌 **DB 전역 조건** 선언               | 단일 테이블 이벤트 처리 → **트리거** / 다중 테이블 전역 제약 → **어설션(미구현 시 트리거 대체)**                     |
| **적용 범위** | 특정 테이블·이벤트 한정 / 행 수준(ROW)·문장 수준(STATEMENT) / 앞서 다룬 **CDC 변경 캡처** 구현 수단 중 하나                          | **DB 전체 상태** 대상 / 복수 테이블 참조 가능 / "부서 직원 수는 항상 1명↑" 같은 전역 규칙                                        | **트리거 한계**: 복잡 연쇄 트리거 → 성능 저하·디버깅 어려움 / **어설션 한계**: Oracle·MySQL·PostgreSQL 미구현 🚨 |
| **구현 현황** | **모든 주요 RDBMS 지원** ✅ / Oracle·PostgreSQL·MySQL·SQL Server / 복잡한 비즈니스 규칙 구현 가능                        | **SQL 표준(SQL:1999) 정의** / **실제 구현: 거의 없음** 🚨 / Oracle·PostgreSQL·MySQL 미지원 / 성능 부담(매 DML마다 전체 검사) | 어설션 대체 패턴: 트리거 + CHECK 제약 + 애플리케이션 계층 검증 3중 구현                                     |

***

#### Ⅲ. 실무 적용 및 한계

**가. 트리거 주요 활용 패턴**

sql

```
-- ①감사 로그 자동 기록 (AFTER 트리거)
CREATE TRIGGER audit_salary_change
AFTER UPDATE OF salary ON employee
FOR EACH ROW
BEGIN
  INSERT INTO audit_log(user, old_val, new_val, changed_at)
  VALUES(USER(), OLD.salary, NEW.salary, NOW());
END;

-- ②데이터 정합성 강제 (BEFORE 트리거)
CREATE TRIGGER check_order_stock
BEFORE INSERT ON order_item
FOR EACH ROW
BEGIN
  IF (SELECT stock FROM product WHERE id = NEW.product_id)
     < NEW.quantity THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = '재고 부족';
  END IF;
END;

-- ③어설션 대체 구현 (다중 테이블 전역 규칙)
CREATE TRIGGER dept_employee_min
AFTER DELETE ON employee
FOR EACH ROW
BEGIN
  IF (SELECT COUNT(*) FROM employee
      WHERE dept_id = OLD.dept_id) = 0 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = '부서 최소 1명 유지';
  END IF;
END;
```

***

**나. 전체 비교 도식화**

```
[트리거 vs 어설션 작동 구조]

트리거:
  DML 이벤트 발생
  (INSERT·UPDATE·DELETE)
       ↓
  트리거 자동 실행
  (BEFORE·AFTER·INSTEAD OF)
       ↓
  행 수준·문장 수준 처리
  → 특정 테이블 중심

어설션:
  DML 이벤트 발생
       ↓
  트랜잭션 커밋 전
       ↓
  DB 전체 상태 조건 검증
  (복수 테이블 참조 가능)
       ↓
  위반 시 전체 롤백

[실무 무결성 구현 계층]

1계층: 기본 제약조건 (PK·FK·CHECK·UNIQUE)
       → 단순·단일 컬럼 규칙
2계층: 트리거
       → 복잡 비즈니스 규칙·감사 로그·어설션 대체
3계층: 어설션 (표준이나 미구현)
       → 트리거+CHECK+앱 계층으로 대체
4계층: 애플리케이션 계층 검증
       → 최후 방어선
```

***

**다. 트리거 설계 주의사항**

| 주의사항        | 내용                 | 대응 방향                    |
| :---------- | :----------------- | :----------------------- |
| **연쇄 트리거**  | 트리거→DML→트리거 무한 연쇄  | 재귀 깊이 제한·순환 방지 설계        |
| **성능 저하**   | 대량 DML 시 트리거 반복 실행 | AFTER STATEMENT 활용·배치 처리 |
| **디버깅 어려움** | 암묵적 실행으로 추적 어려움    | 감사 로그·명명 규칙 표준화          |
| **이식성**     | RDBMS별 문법 차이       | ORM·애플리케이션 계층 이관 검토      |

***

**(제언)** "트리거와 어설션은 DB 무결성 보장의 두 철학 — '언제 어떤 행위에 반응할 것인가(트리거)'와 '어떤 상태가 항상 참이어야 하는가(어설션)' — 을 대표합니다. **어설션이 SQL 표준에 정의됐으나 주요 RDBMS가 성능 부담을 이유로 미구현하는 현실에서, 앞서 다룬 ACID 무결성 보장을 위해 BEFORE 트리거(사전 검증)·AFTER 트리거(감사 추적·앞서 다룬 CDC 연계)·CHECK 제약조건·애플리케이션 계층 검증의 4중 구조로 어설션의 역할을 대체하는 것이 실무 DB 무결성 설계의 핵심 전략입니다.**"**제해야 합니다.**"
