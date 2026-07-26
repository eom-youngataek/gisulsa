
#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 "구두 약속"이 아닌 "계약"으로 데이터를 관리하는가)
Ⅱ. 데이터 계약 핵심 구조 및 구성요소
Ⅲ. 데이터 계약 수명주기 및 운영
Ⅳ. 관련 개념과의 비교 및 연계
Ⅴ. 결론 및 발전 방향
```

포인트: 개요에서 **"앞서 다룬 데이터 메시의 4대 원칙 중 '데이터 제품(Data as a Product)'이 데이터를 제품처럼 관리하라는 철학이라면, 데이터 계약은 그 제품의 생산자(Producer)와 소비자(Consumer) 사이에 데이터 스키마·품질·SLA·소유권·보안을 명시적으로 합의하는 법적 계약에 준하는 기술 문서다 — 앞서 다룬 MVCC·스냅샷 격리가 '트랜잭션 수준의 데이터 일관성'을 보장한다면, 데이터 계약은 '파이프라인·조직 경계를 넘나드는 데이터 흐름의 신뢰성'을 제도적으로 보장하며 데이터 품질 사고의 80%가 스키마 변경·미공지에서 비롯된다는 현실적 문제를 해결"**이라는 한 줄로 시작하면, 왜 이 답안이 앞서 다룬 데이터 메시·데이터 품질·MLOps 시리즈 전체의 **데이터 신뢰 기반**인지 드러납니다.

---

#### Ⅱ. 데이터 계약 핵심 구조 및 구성요소

**가. 데이터 계약 정의 및 위치**

```
[데이터 계약의 위치]

데이터 생산자 (Producer)
  원천 시스템·이벤트 스트림·API
       │
       │ ← 데이터 계약 (Data Contract)
       │   "이런 형태의 데이터를
       │    이런 품질로
       │    이런 조건에 제공한다"
       │
데이터 소비자 (Consumer)
  ML 파이프라인·BI 대시보드·다운스트림 서비스
```

---

**나. 데이터 계약 6대 구성요소**

| ==구성요소==                              | 내용                    | 핵심 키워드                                                         |
| --------------------------------- | --------------------- | -------------------------------------------------------------- |
| ==**스키마 정의 (Schema)**==               | 데이터 구조·필드·타입·제약 명시    | 컬럼명·데이터 타입·Null 허용·기본값·Enum 범위                                 |
| ==**품질 기준 (Quality)**==               | 완전성·정확성·적시성 기준 명시     | Null 비율 상한·유일성·참조 무결성·임계값                                      |
| ==**SLA (Service Level Agreement)**== | 데이터 제공 시간·빈도·지연 기준    | 업데이트 주기(실시간·일배치)·최대 지연 시간·가용성                                  |
| ==**소유권 (Ownership)**==               | 데이터 생산자·책임자·연락처 명시    | Data Owner·Data Steward·팀·Slack 채널                             |
| ==**보안·프라이버시 (Security)**==           | 개인정보 포함 여부·접근 권한 명시   | PII 포함 여부·마스킹 정책·RBAC·앞서 다룬 LINDDUN 연계                         |
| ==**버전·변경 관리 (Versioning)**==         | 스키마 변경 시 하위 호환성·공지 정책 | Semantic Versioning(Major·Minor·Patch) / Breaking Change 공지 기간 |

---

**다. 데이터 계약 예시 (YAML 형식)**

yaml

```yaml
# data_contract_v1.2.yaml
apiVersion: "1.0"
name: "user_transaction_events"
version: "1.2.0"
owner:
  team: "결제 플랫폼팀"
  contact: "payment@company.com"

schema:
  fields:
    - name: user_id
      type: STRING
      nullable: false
      description: "사용자 고유 식별자"
      pii: false

    - name: amount
      type: DECIMAL(18,2)
      nullable: false
      constraints:
        min: 0
        max: 10000000

    - name: email
      type: STRING
      nullable: true
      pii: true          # 개인정보 포함 표시
      masking: "hash"    # 마스킹 정책

quality:
  completeness:
    user_id: 100%        # Null 허용 없음
    amount:  100%
  uniqueness:
    transaction_id: 100%
  freshness:
    max_delay: "5분"

sla:
  delivery: "실시간 스트리밍"
  availability: "99.9%"
  update_frequency: "이벤트 발생 즉시"

security:
  access_roles: ["analyst", "ml_engineer"]
  pii_columns: ["email", "phone"]

versioning:
  breaking_change_notice: "30일 전 공지"
  backward_compatible: true
```

---

#### Ⅲ. 데이터 계약 수명주기 및 운영

**가. 데이터 계약 수명주기**

```
[데이터 계약 4단계 수명주기]

①협의·설계 (Negotiate & Design)
  생산자·소비자 공동 스키마·품질·SLA 협의
  → 앞서 다룬 데이터 메시 도메인 간 계약 수립
       ↓
②등록·배포 (Register & Publish)
  Data Contract 저장소(Git·카탈로그)에 등록
  → OpenDataContractStandard(ODCS) 포맷 활용
  → 앞서 다룬 데이터 카탈로그·메타데이터 연계
       ↓
③검증·모니터링 (Validate & Monitor)
  파이프라인에서 계약 자동 검증
  → 스키마 변경·품질 임계값 위반 시 알림
  → Great Expectations·Soda·Deequ 도구 활용
       ↓
④변경·폐기 (Evolve & Deprecate)
  Breaking Change: 30일 전 공지·버전 증가
  Backward Compatible: Minor 버전 증가
  폐기: Deprecation Notice·마이그레이션 지원
```

---

**나. 데이터 계약 검증 자동화**

```
[CI/CD 파이프라인 내 계약 검증]

코드 커밋 (스키마 변경)
       ↓
①계약 린트 (Contract Linting)
  YAML 문법·필수 항목 검사
       ↓
②호환성 검사 (Compatibility Check)
  기존 버전 대비 Breaking Change 탐지
  → user_id 타입 변경: Major 버전 필수 🚨
  → 새 컬럼 추가: Minor 버전 가능 ✅
       ↓
③품질 규칙 테스트 (Quality Test)
  샘플 데이터로 품질 기준 충족 여부 검증
       ↓
④소비자 영향 분석 (Impact Analysis)
  해당 계약을 사용하는 다운스트림 목록 조회
  → 영향받는 ML 파이프라인·대시보드 자동 통보
       ↓
프로덕션 배포 승인
```

---

**다. 계약 위반 대응 체계**

| 위반 유형         | 탐지 방법                 | 대응 절차                |
| ------------- | --------------------- | -------------------- |
| **스키마 불일치**   | 파이프라인 자동 검증           | 소비자 알림·업스트림 수정 요청    |
| **품질 기준 미달**  | Great Expectations 검사 | 데이터 격리·Owner 긴급 알림   |
| **SLA 지연**    | 모니터링 대시보드 탐지          | 인시던트 생성·PagerDuty 연동 |
| **무단 스키마 변경** | Git 커밋 추적·계약 차이 비교    | PR 차단·리뷰어 강제 지정      |
| **보안 정책 위반**  | PII 컬럼 마스킹 미적용        | 파이프라인 즉시 중단·보안팀 통보   |

---

#### Ⅳ. 관련 개념과의 비교 및 연계

**가. 데이터 계약 vs 유사 개념 비교**

| 비교 항목     | 데이터 계약                | API 계약(OpenAPI) | 데이터 카탈로그  | SLA       |
| --------- | --------------------- | --------------- | --------- | --------- |
| **목적**    | 데이터 신뢰·품질 합의          | API 인터페이스 명세    | 데이터 자산 발견 | 서비스 수준 합의 |
| **대상**    | 데이터 파이프라인·팀 간         | 서비스 간 API 호출    | 전체 데이터 자산 | 서비스 운영 전반 |
| **품질 기준** | 명시적 포함 ✅              | 미포함             | 부분적       | 미포함       |
| **자동 검증** | 파이프라인 내 검증 ✅          | Swagger 검증      | 수동 점검     | 모니터링      |
| **소유권**   | 명시 필수 ✅               | 팀 단위            | 데이터 스튜어드  | 서비스 오너    |
| **버전 관리** | Semantic Versioning ✅ | OpenAPI 버전      | 메타데이터 버전  | 계약 기간     |

---

**나. 앞서 다룬 개념과의 연결**

|연계 개념|연결 내용|
|---|---|
|**데이터 메시**|도메인 간 데이터 제품 교환의 공식 합의 수단|
|**데이터 패브릭**|액티브 메타데이터가 계약 정보를 자동 탐색·추천|
|**MLOps 피처스토어**|피처 정의·품질 기준을 데이터 계약으로 공식화|
|**개인정보 안전조치**|PII 컬럼 마스킹·접근 권한을 계약에 명시|
|**LINDDUN Non-Compliance**|계약 위반 = Non-Compliance 위협 탐지·대응|
|**AI 학습데이터 품질**|학습 데이터 공급자가 계약으로 품질 보증|

---

**다. 데이터 계약 도구 생태계**

| 도구                                 | 역할                | 특징                          |
| ---------------------------------- | ----------------- | --------------------------- |
| **OpenDataContractStandard(ODCS)** | 오픈 표준 스키마 포맷      | Linux Foundation 주관·YAML 기반 |
| **Great Expectations**             | 데이터 품질 검증 자동화     | 기대값 정의·파이프라인 통합             |
| **Soda**                           | 데이터 계약 기반 품질 모니터링 | SodaCL 언어·계약 연동             |
| **Deequ (AWS)**                    | Spark 기반 대규모 검증   | Amazon 오픈소스·MLOps 연계        |
| **Atlan·DataHub**                  | 데이터 카탈로그+계약 통합    | 계약 저장·검색·영향 분석              |

---

#### Ⅴ. 결론 및 발전 방향

**데이터 계약 도입 효과**

```
[데이터 계약 도입 전후 비교]

도입 전:
  스키마 변경 → 다운스트림 파이프라인 무단 중단
  품질 문제 → 원인 불명·책임 소재 불분명
  ML 모델 → 학습 데이터 신뢰 불가 → 성능 저하

도입 후:
  스키마 변경 → 30일 전 공지·영향 분석 자동화 ✅
  품질 위반 → 계약 기준 즉시 탐지·Owner 알림 ✅
  ML 모델 → 계약 보증 데이터로 신뢰 확보 ✅
  데이터 사고 80% 감소 (스키마 변경 기인)
```

**발전 방향**

```
①LLM 기반 계약 자동 생성
  데이터 샘플 입력 → LLM이 계약 초안 자동 작성
  앞서 다룬 에이전틱 코딩으로 계약 갱신 자동화

②실시간 계약 모니터링
  스트리밍 파이프라인에서 이벤트별 계약 검증
  Kafka Schema Registry + 계약 통합

③AI 품질 예측
  과거 계약 위반 패턴 학습
  → 위반 사전 예측·선제 대응
  앞서 다룬 MLOps CT 자동 트리거 연계

④글로벌 데이터 계약 표준화
  ODCS 기반 산업별 표준 계약 템플릿
  국가 간 데이터 공유 계약(앞서 다룬
  개인정보 전송요구권 국경 간 적용)
```

---

#### 기술사 답안 포인트

**데이터 품질 사고 80%=스키마 변경 미공지 → 생산자·소비자 공식 합의 수단 → 6대 구성요소(스키마·품질·SLA·소유권·보안·버전) → YAML 계약 예시(PII 표시·마스킹·품질 임계값) → 수명주기(협의→등록→검증→변경) → CI/CD 파이프라인 내 자동 검증·Breaking Change 탐지 → 데이터 메시·MLOps·개인정보보호 연계 → LLM 기반 계약 자동 생성 발전** 흐름으로 서술하면 데이터 거버넌스·품질·운영을 아우르는 완성도 높은 답안이 됩니다. **Semantic Versioning 기반 Breaking Change 30일 전 공지 체계**가 핵심 차별화 포인트입니다.



#### **1. 답안 전개 스토리 (핵심 압축)**

> "데이터를 보내주는 원천 시스템(생산자)과 데이터를 받아 리포트를 그리거나 AI를 학습시키는 현업(소비자) 사이에 \*\*"이런 형식의 데이터 규격만 주고받겠다"고 맺는 '기계 작동식 데이터 협정 명세서(YAML/JSON)'\*\*다. 서비스 기획자가 아무 생각 없이 DB 컬럼 이름(예: 'user\_id' ➔ 'id')을 바꾸면, 다음 날 출근한 데이터 분석가와 AI 모델 파이프라인은 에러를 뿜으며 붕괴한다. 데이터 계약은 이를 원천 차단한다. 스키마와 데이터 포맷을 담은 계약 문서를 작성하고, **CI/CD 파이프라인 빌드 시점에 테스트를 걸어둔다.** 생산자가 계약에 위반되는 구조 변경을 시도하면 빌드가 실패하여 배포 자체가 막힌다. 사후 소 잃고 외양간 고치는 모니터링을 넘어, 데이터 사고를 입구에서 완벽하게 예방하는 최신 수호 장치다."

#### **2. 실제 답안에 쓸 핵심 내용 (암기용)**


![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5MzIuNzc1IDM1NC4xNSIgd2lkdGg9IjkzMi43NzUiIGhlaWdodD0iMzU0LjE1IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJEYXRhX0NvbnRyYWN0X19fXyIgZGF0YS1sYWJlbD0iRGF0YSBDb250cmFjdCDquLDrsJgg7YyM7J207ZSE65287J24IOq1rOyhsCDrs7TtmLgiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9Ijg1Mi43NzUiIGhlaWdodD0iMjc0LjE1IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iODUyLjc3NSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPkRhdGEgQ29udHJhY3Qg6riw67CYIO2MjOydtO2UhOudvOyduCDqtazsobAg67O07Zi4PC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJQUk9EIiBkYXRhLXRvPSJDSSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyMjMuMTc5LDE5MS4wNzUgMjcxLjE3OSwxOTEuMDc1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDSSIgZGF0YS10bz0iQkxLIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLqs4Tslb0g7JyE67CYISDwn5KlCuy7rOufvCDsgq3soJwv7YOA7J6FIOuzgOuPmSIgcG9pbnRzPSI0ODUuMzI4OTk5OTk5OTk5OTUsMTkxLjA3NSA2OTIuNTUzLDE5MS4wNzUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQ0kiIGRhdGEtdG89IkJMSyIgZGF0YS1sYWJlbD0i6rOE7JW9IOychOuwmCEg8J+SpQrsu6zrn7wg7IKt7KCcL+2DgOyehSDrs4Drj5kiPgogIDxyZWN0IHg9IjUyOS4zMjkwMDAwMDAwMDAxIiB5PSIxNjguMDc1IiB3aWR0aD0iMTE5LjIyNDAwMDAwMDAwMDAyIiBoZWlnaHQ9IjQ0LjYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTg4Ljk0MSIgeT0iMTkwLjM3NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSI+PHRzcGFuIHg9IjU4OC45NDEiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij7qs4Tslb0g7JyE67CYISDwn5KlPC90c3Bhbj48dHNwYW4geD0iNTg4Ljk0MSIgZHk9IjE0LjMiPuy7rOufvCDsgq3soJwv7YOA7J6FIOuzgOuPmTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQUk9EIiBkYXRhLWxhYmVsPSLrjbDsnbTthLAg7IOd7IKw7J6QCuyGjOyKpCDsvZTrk5wg67Cw7Y+sIOyLnOuPhCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iMTY0LjE3NSIgd2lkdGg9IjE2Ny4xNzkiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMzkuNTg5NSIgeT0iMTkxLjA3NTAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxMzkuNTg5NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuuNsOydtO2EsCDsg53sgrDsnpA8L3RzcGFuPjx0c3BhbiB4PSIxMzkuNTg5NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7IaM7IqkIOy9lOuTnCDrsLDtj6wg7Iuc64+EPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkNJIiBkYXRhLWxhYmVsPSLinKggQ0kvQ0Qg6rOE7JW9IOqygOymnSDwn5qoIOKcqApEYXRhIENvbnRyYWN0IOuqheyEuOyEnOyZgArsiJjsoJXrkJwg7Iqk7YKk66eIIOuMgOyhsCIgZGF0YS1zaGFwZT0iZGlhbW9uZCI+CiAgPHBvbHlnb24gcG9pbnRzPSIzNzguMjUzOTk5OTk5OTk5OTYsODMuOTk5OTk5OTk5OTk5OTkgNDg1LjMyODk5OTk5OTk5OTk1LDE5MS4wNzUgMzc4LjI1Mzk5OTk5OTk5OTk2LDI5OC4xNSAyNzEuMTc5LDE5MS4wNzUiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMzc4LjI1Mzk5OTk5OTk5OTk2IiB5PSIxOTEuMDc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIzNzguMjUzOTk5OTk5OTk5OTYiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj7inKggQ0kvQ0Qg6rOE7JW9IOqygOymnSDwn5qoIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjM3OC4yNTM5OTk5OTk5OTk5NiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+RGF0YSBDb250cmFjdCDrqoXshLjshJzsmYA8L3RzcGFuPjx0c3BhbiB4PSIzNzguMjUzOTk5OTk5OTk5OTYiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyImOygleuQnCDsiqTtgqTrp4gg64yA7KGwPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkJMSyIgZGF0YS1sYWJlbD0i67Cw7Y+sIOqwleygnCDssKjri6gg67CPIOyVjOumvCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI2OTIuNTUzIiB5PSIxNzIuNjI1IiB3aWR0aD0iMTg0LjIyMTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI3ODQuNjY0IiB5PSIxOTEuMDc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7rsLDtj6wg6rCV7KCcIOywqOuLqCDrsI8g7JWM66a8PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

| **핵심 척도**                | **📊 데이터 계약 필수 명세 항목 🚨**                                                                                             | **🔑 데이터 관측성(Observability) 대조 💯**                                                                                                            | **🏁 스키마 드리프트 방어 메커니즘 💯**                                                                |
| :----------------------- | :-------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| **역할 / 관점**              | **'프로토콜 합의 규격'.** 데이터의 형식, 타입, 비즈니스 의미 및 SLA 약속을 기계 판독형 문서(YAML 등)로 기술함.                                              | **'선제적 차단 vs 사후 모니터링'.** 장애가 터지기 전 입구에서 막는 기술과, 흘러가는 도중 감시하는 기술의 보완 관계.                                                                        | 생산자의 무분별한 소스 변경으로 하류(Downstream) 시스템이 연쇄 붕괴하는 현상 제어.                                      |
| **핵심 세부 내용 (출제 포인트) 🚨** | **1. \[Schema 규격 🚨]** 컬럼명, 타입, Null 허용 여부. **2. \[SLA/품질 지표 💯]** 신선도, 허용 오류 임계치. **3. \[Terms 🚨]** 소유자 정보 및 버전 번호. | **\[데이터 관측성 (Observability)]** 파이프라인 유동 데이터를 실시간 스캔해 장애 사후 탐지. **\[데이터 계약 (Data Contract) 💯]** **CI/CD 파이프라인에서 스키마 변경을 미리 체크해 사전에 배포 원천 차단.** | 데이터 계약 사양을 **Protobuf**나 **Avro Schema**로 굳히고, 생산자가 이를 어길 시 배포 파이프라인 빌드를 자동으로 깨버리는 기술 연동. |

* **(제언)** "데이터 계약의 도입 성공은 개발 생산성 저하를 방어하는 데 있습니다. **이를 위해 계약 작성을 자동화해 주는 도구(예: dbt, Soda)를 빌드 파이프라인에 결합하여 개발자의 귀찮음을 덜고 자발적 준수 문화를 정착시켜야 합니다.**"
