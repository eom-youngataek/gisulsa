***

#### **RDBMS 버퍼 관리의 핵심: STEAL & No-Force 정책**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 버퍼 관리 정책이 성능과 회복의 트레이드오프 핵심인가)
Ⅱ. 4대 버퍼 관리 정책 핵심 비교
Ⅲ. STEAL·No-Force 조합의 현대 표준 이유
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 ARIES 회복 알고리즘이 '장애 후 WAL로 Redo·Undo를 수행'한다면, STEAL·No-Force는 '그 ARIES가 왜 Redo와 Undo 모두 필요한가'를 결정하는 버퍼 관리 정책이다 — STEAL은 '미커밋 트랜잭션의 Dirty Page를 디스크에 먼저 쓸 수 있는가', Force는 '커밋 시 모든 Dirty Page를 즉시 디스크에 강제 기록하는가'의 두 축으로 4가지 조합이 만들어지며, 현대 RDBMS(InnoDB·PostgreSQL·Oracle)는 모두 STEAL+No-Force를 채택해 버퍼 효율·커밋 성능을 극대화하는 대신 Undo·Redo 양쪽 로그를 모두 유지하는 트레이드오프를 선택한 것"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.

***

#### Ⅱ. 4대 버퍼 관리 정책 핵심 비교

**가. 2축 4조합 정의**

```
[버퍼 관리 정책 2대 축]

STEAL 축 (미커밋 Dirty Page 선기록):
  STEAL:    미커밋 트랜잭션 Dirty Page → 디스크 가능
  No-STEAL: 미커밋 트랜잭션 Dirty Page → 디스크 불가
            (커밋 전까지 버퍼에만 존재)

FORCE 축 (커밋 시 강제 디스크 기록):
  FORCE:    커밋 시 모든 Dirty Page → 즉시 디스크 기록
  No-FORCE: 커밋 시 디스크 기록 강제 안 함
            (나중에 비동기로 기록)

[4가지 조합]
             FORCE           No-FORCE
STEAL      STEAL+FORCE      STEAL+No-Force ✅ (현대 표준)
No-STEAL   No-STEAL+FORCE   No-STEAL+No-Force (이론)
```

***

**나. 4조합 핵심 비교**

| **핵심 척도**    | **📊 STEAL 정책 🚨**                                                                                                        | **🔑 FORCE 정책 🚨**                                                                                                  | **🏁 STEAL+No-Force 현대 표준 💯**                                                                  |
| :----------- | :------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------- |
| **STEAL 의미** | **미커밋 Dirty Page 선기록 허용** / 버퍼 부족 시 미커밋 페이지도 디스크로 쫓아냄 / 버퍼 효율 최대화 ✅ / **Undo 필요**: 미커밋 데이터 디스크에 있으므로 장애 시 Undo 필수         | **No-STEAL**: 미커밋 페이지 디스크 기록 금지 / Undo 불필요 (미커밋 데이터 디스크에 없음) / **치명적 한계**: 트랜잭션 크기 > 버퍼 크기 → 불가 🚨 / 대용량 트랜잭션 처리 불가 | **STEAL 채택 이유**: 버퍼 크기와 무관한 트랜잭션 처리 / 대용량 배치·OLAP도 처리 가능 / Undo 로그 비용 < 버퍼 제약 이점                |
| **FORCE 의미** | **FORCE**: 커밋 시 모든 Dirty Page 즉시 디스크 기록 / **Redo 불필요**: 커밋 데이터 항상 디스크에 존재 / **치명적 한계**: 커밋마다 대규모 랜덤 I/O 🚨 / 커밋 성능 극도로 저하 | **No-FORCE 채택**: 커밋 시 WAL만 fsync / Dirty Page는 나중에 비동기 기록 / 커밋 성능 최대화 ✅ / **Redo 필요**: 커밋했으나 미기록 페이지 장애 시 Redo 필요   | **No-Force 채택 이유**: WAL(순차 I/O) fsync는 빠름 / Dirty Page 랜덤 I/O 지연 없음 / 커밋 응답시간 최소화 / OLTP 고성능 필수 |
| **회복 필요성**   | **STEAL → Undo 필요**: 미커밋 Dirty Page가 디스크에 있을 수 있음 / 장애 시 이를 원상복구해야 / 앞서 다룬 **ARIES Undo 단계** 필요 이유                        | **No-Force → Redo 필요**: 커밋됐으나 버퍼에만 있던 페이지 / 장애 시 WAL로 재실행 / 앞서 다룬 **ARIES Redo 단계** 필요 이유                           | **STEAL+No-Force = Undo+Redo 모두 필요** / WAL이 양쪽 모두 지원 / 앞서 다룬 **ARIES 3단계** 완전한 이유               |

***

#### Ⅲ. STEAL·No-Force 조합의 현대 표준 이유

**가. WAL과의 관계**

```
[STEAL+No-Force + WAL 황금 조합]

트랜잭션 실행 중:
  Dirty Page → 버퍼 풀 유지 (No-Force)
  버퍼 부족 시 미커밋 Dirty Page 디스크 기록 (STEAL)
  모든 변경: WAL 로그에 먼저 기록 (WAL 원칙)

커밋 시:
  WAL 로그 fsync (순차 I/O·빠름) ✅
  Dirty Page 디스크 기록 강제 안 함 (No-Force)
  → 커밋 응답 즉시 반환

백그라운드:
  체크포인터: 주기적 Dirty Page 디스크 기록
  앞서 다룬 ARIES DPT 관리

장애 복구:
  STEAL → 미커밋 데이터 디스크 있을 수 있음
          → ARIES Undo 단계로 제거
  No-Force → 커밋 데이터 버퍼에만 있을 수 있음
             → ARIES Redo 단계로 재적용
```

***

**나. 도식화**

```
[4대 정책 성능·회복 트레이드오프]

             버퍼 효율
                ↑
  STEAL+       │    STEAL+
  No-Force ✅  │    Force
  (현대 표준)  │
               │
  No-STEAL+   │    No-STEAL+
  No-Force     │    Force
  (이론)       │
               └──────────────→ 커밋 성능
                             ↑
                          No-Force 방향

[정책별 Undo·Redo 필요성]

정책               Undo 필요  Redo 필요
STEAL+Force        ✅         ✗
No-STEAL+Force     ✗          ✗ (이상적이나 비현실)
STEAL+No-Force     ✅         ✅ (현대 표준·ARIES)
No-STEAL+No-Force  ✗          ✅

[실무 RDBMS 구현]

InnoDB (MySQL):
  STEAL: 버퍼 풀 eviction 시 미커밋 페이지 기록
  No-Force: 커밋 시 redo log만 fsync
  회복: ARIES 기반 Undo(롤백 세그먼트)+Redo

PostgreSQL:
  STEAL: shared_buffers 교체 시 Dirty Page 기록
  No-Force: WAL fsync 후 커밋 완료
  회복: WAL Redo (Undo는 MVCC 버전 체인 활용)

Oracle:
  STEAL: DB Writer 백그라운드 프로세스
  No-Force: LGWR가 redo log만 커밋 시 기록
  회복: Redo(아카이브 로그)+Undo(롤백 세그먼트)
```

***

**다. 앞서 다룬 개념과의 연결**

| 연계 개념         | 연결 내용                                          |
| :------------ | :--------------------------------------------- |
| **ARIES 3단계** | STEAL→Undo 필요 / No-Force→Redo 필요 / ARIES 설계 이유 |
| **WAL 원칙**    | STEAL+No-Force의 안전망 / 로그 선행 기록으로 양쪽 보완         |
| **이중 쓰기 버퍼**  | STEAL로 기록된 Dirty Page의 Torn Page 방지            |
| **MVCC**      | PostgreSQL: Undo 대신 MVCC 버전 체인 활용              |
| **체크포인트**     | No-Force로 미기록된 Dirty Page의 주기적 디스크 반영          |

***

**(제언)** "STEAL+No-Force는 '버퍼 효율과 커밋 성능을 동시에 극대화하는 대신 Undo·Redo 모두 필요하다는 복잡성을 WAL로 감당하는 현대 RDBMS의 황금 트레이드오프'입니다. **앞서 다룬 ARIES가 Analysis→Redo→Undo 3단계를 수행하는 근본 이유가 바로 STEAL+No-Force 정책이며, 이중 쓰기 버퍼가 STEAL로 기록된 Dirty Page의 Torn Page를 방지하고, WAL fsync가 No-Force 커밋의 내구성을 보장하는 것이 InnoDB·PostgreSQL·Oracle 모든 현대 RDBMS 회복 아키텍처의 핵심 설계 원칙임을 이해하는 것이 DB 시스템 설계 역량의 핵심입니다.**"
