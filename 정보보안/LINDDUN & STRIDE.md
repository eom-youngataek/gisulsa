#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 "STRIDE"로는 프라이버시를 못 잡는가) — 3~4줄
Ⅱ. LINDDUN 7대 위협 체계 (본론①, 도식 1개 필수)
Ⅲ. STRIDE와의 비교·LINDDUN 수행 단계별 흐름 (핵심 배점)
Ⅳ. 결론
```

포인트: 개요에서 **"앞서 다룬 STRIDE가 '기밀성·무결성·가용성 침해라는 보안 위협'을 모델링한다면, LINDDUN은 '데이터가 올바르게 보호되더라도 그 수집·처리·공유 자체가 프라이버시를 침해할 수 있다'는 관점에서 개인정보 흐름(Data Flow)의 위협을 체계화한 프라이버시 특화 위협 모델링 프레임워크다 — 앞서 다룬 인공지능기본법의 고영향 AI 영향평가·EU GDPR의 DPIA(데이터 보호 영향평가)·AI 학습데이터 품질관리가 요구하는 '프라이버시 설계(Privacy by Design)'를 실제로 수행하는 구체적 기술 도구가 바로 LINDDUN"**이라는 한 줄로 시작하면, 왜 이 답안이 앞서 다룬 AI 윤리·개인정보보호·보안 아키텍처 시리즈 전체의 **프라이버시 위협 분석 핵심**인지 드러납니다.

---

#### Ⅱ. LINDDUN 7대 위협 체계

|약자|위협 유형|핵심 내용|
|---|---|---|
|**L**|**Linking (연계)**|서로 다른 데이터 소스·세션·시스템의 정보를 **연결해 개인을 식별**하는 위협. 각각은 무해한 데이터도 결합 시 개인정보가 되는 **모자이크 효과(Mosaic Effect)**. 앞서 다룬 **"합성데이터의 k-익명성"**이 연계 위협의 방어 수단|
|**I**|**Identifying (식별)**|익명화·가명화된 데이터에서 **특정 개인의 신원을 재식별(Re-identification)**하는 위협. 넷플릭스 시청 기록 익명화 데이터에서 개인 재식별 성공 사례(Narayanan 2008)가 대표. 앞서 다룬 **"차분 프라이버시"**가 핵심 방어 기법|
|**N**|**Non-Repudiation (부인 불가)**|사용자가 특정 행위를 **부인하지 못하도록 증거가 지나치게 상세히 기록**되는 위협. 보안 관점의 부인 방지(Non-repudiation)는 좋은 속성이나, 프라이버시 관점에서는 **과도한 감시·행동 추적**의 원인|
|**D**|**Detecting (탐지)**|사용자가 특정 서비스를 이용하거나 특정 행동을 한다는 사실 자체가 **노출(관찰 가능)**되는 위협. 암호화 통신도 **트래픽 분석(Traffic Analysis)**으로 "누가 언제 접속했는지"가 드러나는 메타데이터 노출이 대표|
|**D**|**Disclosure (노출)**|개인 데이터가 **권한 없는 주체에게 직접 노출**되는 위협. 앞서 다룬 **"인포스틸러·크리덴셜 스터핑·PtH"**의 프라이버시 영향이 바로 Disclosure 위협. STRIDE의 Information Disclosure와 중첩되나 **개인정보 맥락에 특화**|
|**U**|**Unawareness (비인지)**|데이터 주체(사용자)가 **자신의 데이터가 어떻게 수집·처리·공유되는지 알지 못하는** 위협. GDPR의 **투명성 원칙·정보 주체 권리(열람·삭제·이동권)**가 Unawareness 위협의 법적 대응. 앞서 다룬 **"콘텐츠 워터마킹 의무화·AI 생성 표시"**가 Unawareness 완화 수단|
|**N**|**Non-Compliance (법 위반)**|**개인정보 관련 법령·정책·계약을 위반**해 데이터를 처리하는 위협. GDPR·개인정보보호법·인공지능기본법·CSAP의 컴플라이언스 요건과 직결. 앞서 다룬 **"고영향 AI 영향평가 의무"**가 Non-Compliance 위협의 법적 방어선|

→ 암기: **"연계·식별·부인불가·탐지·노출·비인지·법위반 — L·I·N·D·D·U·N. 앞 두 글자(LI)는 익명화를 깨는 공격, 중간(NDD)은 행동이 드러나는 위협, 끝(UN)은 사용자가 모르거나 법을 어기는 위협"** — 앞서 다룬 **"Demographic Parity의 보호 속성 침해"**가 LINDDUN의 Identifying + Disclosure 위협이 결합된 형태임을 연결할 수 있습니다.

#### 도식화 제안

```
[LINDDUN 7대 위협 분류 구조]

개인정보 흐름 (Data Flow Diagram 기반)

데이터 수집 단계
  L - Linking    : 여러 소스 연계 → 개인 식별 (모자이크 효과)
  I - Identifying: 익명 데이터 재식별 (k-익명성 무력화)

데이터 처리·전송 단계
  N - Non-Repudiation: 과도한 로그 → 행동 추적
  D - Detecting      : 접속 사실 자체 노출 (메타데이터)
  D - Disclosure     : 권한 없는 자에게 직접 노출

데이터 주체 관점
  U - Unawareness    : 사용자가 처리 사실 모름
  N - Non-Compliance : 법령·정책 위반

          방어 수단 매핑
  L → k-익명성·데이터 최소화
  I → 차분 프라이버시·가명화
  N(부인) → 로그 최소화·목적 제한
  D(탐지) → 트래픽 패딩·Tor·VPN
  D(노출) → 암호화·접근 제어·제로트러스트
  U → GDPR 투명성·동의 관리·AI 표시 의무
  N(법위반) → DPIA·개인정보 영향평가·컴플라이언스
```

---

#### Ⅲ. STRIDE와의 비교·LINDDUN 수행 단계별 흐름 — 핵심 배점

**함정 방지: "LINDDUN은 프라이버시 위협 모델링"이라고만 답하면 절반. DFD 기반 분석이 어떻게 각 데이터 흐름에 7가지 위협을 매핑하는지, STRIDE와 LINDDUN을 병행해야 하는 이유, 그리고 Privacy by Design 8원칙과 어떻게 연결되는지를 단계별로 보여줘야 완성됩니다.**

|단계|활동|
|---|---|
|**DFD 작성**|**데이터 흐름 다이어그램(DFD)** 작성 — 데이터 저장소·프로세스·외부 엔티티·데이터 흐름 4요소 식별. 앞서 다룬 **"EA의 데이터 아키텍처(DA)"**에서 정의한 데이터 흐름이 LINDDUN 분석의 입력물|
|**위협 매핑**|DFD의 각 데이터 흐름·저장소·프로세스에 **LINDDUN 7개 위협 카테고리를 순차 적용**. "이 흐름에서 Linking이 가능한가?"·"Identifying 위험이 있는가?" 체크리스트 방식으로 위협 식별|
|**위협 트리 분석**|각 위협을 **위협 트리(Threat Tree)**로 구체화 — Linking 위협의 경우 "어떤 두 데이터 소스가 연결되는가?"·"연결 가능한 식별자는 무엇인가?"를 트리 형태로 분해|
|**프라이버시 전략 선택**|**최소화(Minimization)**: 수집 데이터 최소화. **분리(Separation)**: 데이터 결합 방지. **추상화(Abstraction)**: 상세도 낮춤·집계. **숨김(Hiding)**: 암호화·익명화. **통보(Informing)**: 투명성 제공. **통제(Controlling)**: 동의·접근 제어. **강제(Enforcing)**: 기술적 통제 구현. **시연(Demonstrating)**: 컴플라이언스 증명|
|**Privacy by Design 연계**|Ann Cavoukian의 **Privacy by Design 7원칙** — 사전 예방·기본값으로 프라이버시·설계에 내재화·전체 기능성·종단간 보안·가시성·사용자 중심. LINDDUN 분석 결과를 PbD 원칙에 매핑해 **설계 단계에서 프라이버시 내재화**|

→ 암기: **"DFD 그리고 → 7위협 체크리스트 매핑 → 위협 트리 구체화 → 최소화·분리·추상화·숨김·통보·통제·강제·시연 8전략으로 완화 → Privacy by Design으로 설계 내재화"**

**STRIDE vs LINDDUN 병행 필요성** (중요): 앞서 다룬 **"AI-SOC·보안 아키텍처"**에서 STRIDE가 **"시스템을 어떻게 공격하는가(How)"**를 분석한다면, LINDDUN은 **"개인정보가 어떻게 침해되는가(Who's data·What impact)"**를 분석한다 — 동일한 DFD에 STRIDE로 보안 위협을, LINDDUN으로 프라이버시 위협을 **병행 분석**해야 앞서 다룬 **"인공지능기본법의 고영향 AI 영향평가"**와 **"GDPR의 DPIA"**가 요구하는 **보안+프라이버시 통합 위험 평가**가 완성됩니다.

#### 도식화 제안

```
[STRIDE vs LINDDUN 전면 비교]

항목          STRIDE                    LINDDUN
──────────────────────────────────────────────────────
분석 관점     보안 (CIA 삼각형)           프라이버시 (개인정보 흐름)
위협 범주     S·T·R·I·D·E 6가지          L·I·N·D·D·U·N 7가지
분석 대상     시스템 컴포넌트·경계         개인정보 데이터 흐름
적용 표준     NIST SP 800-30             GDPR·DPIA·개인정보보호법
완화 방법     보안 통제 (암호화·인증)      프라이버시 전략 (최소화·분리)
법적 연계     정보보안 법령               개인정보보호법·GDPR·AI기본법
병행 필요성   보안 위협 식별              프라이버시 위협 식별
결합 시 효과  보안+프라이버시 통합 DPIA 완성 ✅

[LINDDUN 수행 단계 흐름]

①DFD 작성
  데이터 저장소·프로세스·외부 엔티티·흐름 식별
     ↓
②LINDDUN 7위협 매핑
  각 흐름 × 7위협 체크리스트 → 위협 목록 도출
     ↓
③위협 트리 구체화
  우선순위 위협 → 공격 경로 트리 분해
     ↓
④프라이버시 전략 적용
  최소화·분리·추상화·숨김·통보·통제·강제·시연
     ↓
⑤Privacy by Design 내재화
  설계 문서에 반영 → DPIA 제출 → 컴플라이언스 증명
```

**앞서 다룬 AI 윤리·개인정보보호법·고영향 AI·합성데이터와의 연결**: 이런 **"DFD 기반 7위협 매핑·위협 트리·8전략 완화"** 구조가 실제로는 앞서 다룬 **"인공지능기본법 제35조 고영향 AI 영향평가"**에서 요구하는 **"영향받는 자 식별·기본권 침해 유형 분석"**의 기술적 수행 방법론이 되고, 앞서 다룬 **"합성데이터의 차분 프라이버시·k-익명성"**이 LINDDUN의 Linking·Identifying 위협 완화 수단으로 직접 연결되며, 앞서 다룬 **"Demographic Parity의 보호 속성"**이 LINDDUN Identifying 위협의 피해 대상과 동일한 개념임을 통합 연결합니다.

---

#### Ⅳ. 결론

LINDDUN은 **"DFD의 각 개인정보 흐름에 Linking·Identifying·Non-Repudiation·Detecting·Disclosure·Unawareness·Non-Compliance 7가지 프라이버시 위협을 체계적으로 매핑하고, 최소화·분리·추상화·숨김·통보·통제·강제·시연 8전략으로 완화해 Privacy by Design을 설계 단계에서 실현하는 프라이버시 특화 위협 모델링 프레임워크"**이며, 특히 **"STRIDE가 보안 위협을 잡는다면 LINDDUN은 프라이버시 위협을 잡는다 — 동일 DFD에 두 프레임워크를 병행 적용할 때 GDPR DPIA·인공지능기본법 고영향 AI 영향평가가 요구하는 보안+프라이버시 통합 위험 평가가 완성"**되는 것이 핵심입니다 — 이는 앞서 다룬 **STRIDE(보안 위협 모델링) → LINDDUN(프라이버시 위협 모델링) → 차분 프라이버시·k-익명성(기술적 완화) → Privacy by Design(설계 내재화) → GDPR DPIA·인공지능기본법 영향평가(법적 이행)**를 하나로 잇는 프라이버시 엔지니어링의 실무적 교량이며, **"보안이 잠금장치를 만드는 일이라면, 프라이버시는 그 잠금장치 안에 넣을 데이터가 처음부터 최소화되도록 설계하는 일이며, 그 설계의 시작이 LINDDUN"**이라는 결론으로 이어집니다.

### **I. 프라이버시 중심 위협 모델링의 표준 프레임워크, LINDDUN의 개요**

소프트웨어 아키텍처 설계 단계에서 보안 취약점뿐만 아니라 개인정보 침해 리스크를 체계적으로 식별하고 대응하기 위한 위협 모델링 프레임워크가 바로 **LINDDUN**입니다. 기존의 보안 중심 방법론(예: STRIDE)과 달리, LINDDUN은 정보주체(사용자)의 프라이버시 권리 보호에 초점을 맞추어 데이터 생명주기 전반의 흐름을 분석하고 개인정보 규제(GDPR 등) 준수를 보장하는 것을 목표로 합니다.

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NDUuOTAzOTk5OTk5OTk5OTQgOTUwLjYiIHdpZHRoPSI0NDUuOTAzOTk5OTk5OTk5OTQiIGhlaWdodD0iOTUwLjYiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IlN5c3RlbU1hcHBpbmciIGRhdGEtbGFiZWw9IjEuIOyLnOyKpO2FnCDslYTtgqTthY3sspgg66ek7ZWRIj4KICA8cmVjdCB4PSI3Ny4wNDk5OTk5OTk5OTk5OCIgeT0iNDAiIHdpZHRoPSIyOTEuODA0IiBoZWlnaHQ9IjExMy44MDAwMDAwMDAwMDAwMSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9Ijc3LjA0OTk5OTk5OTk5OTk4IiB5PSI0MCIgd2lkdGg9IjI5MS44MDQiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9Ijg5LjA0OTk5OTk5OTk5OTk4IiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij4xLiDsi5zsiqTthZwg7JWE7YKk7YWN7LKYIOunpO2VkTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IlRocmVhdElkZW50aWZpY2F0aW9uIiBkYXRhLWxhYmVsPSIyLiBMSU5ERFVOIOychO2YkSDsi53rs4QiPgogIDxyZWN0IHg9Ijg2LjMxMjQ5OTk5OTk5OTk3IiB5PSIyODIuMSIgd2lkdGg9IjI3My4yNzkiIGhlaWdodD0iMjUwLjEiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI4Ni4zMTI0OTk5OTk5OTk5NyIgeT0iMjgyLjEiIHdpZHRoPSIyNzMuMjc5IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI5OC4zMTI0OTk5OTk5OTk5NyIgeT0iMjk2LjEiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+Mi4gTElORERVTiDsnITtmJEg7Iud67OEPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iTWl0aWdhdGlvbiIgZGF0YS1sYWJlbD0iMy4g7JmE7ZmUIOyhsOy5mCAoTWl0aWdhdGlvbikiPgogIDxyZWN0IHg9IjQwIiB5PSI2NjAuNSIgd2lkdGg9IjM2NS45MDM5OTk5OTk5OTk5NCIgaGVpZ2h0PSIyNTAuMSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI2NjAuNSIgd2lkdGg9IjM2NS45MDM5OTk5OTk5OTk5NCIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjY3NC41IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjMuIOyZhO2ZlCDsobDsuZggKE1pdGlnYXRpb24pPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJERkQiIGRhdGEtdG89IlRocmVhdFRyZWUiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuychO2YkSDtirjrpqwg66ek7ZWRIiBwb2ludHM9IjIyMi45NTE5OTk5OTk5OTk5NywxMzcuOCAyMjIuOTUxOTk5OTk5OTk5OTcsMzI2LjEiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlRocmVhdExpc3QiIGRhdGEtdG89IlBFVCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7ZSE65287J2067KE7IucIOqwle2ZlCDquLDsiKAgUEVUIOyggeyaqSIgcG9pbnRzPSIyMjIuOTUxOTk5OTk5OTk5OTcsNTE2LjIgMjIyLjk1MTk5OTk5OTk5OTk3LDcwNC41IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJUaHJlYXRUcmVlIiBkYXRhLXRvPSJUaHJlYXRMaXN0IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLrtoTshJ0g7IiY7ZaJIiBwb2ludHM9IjIyMi45NTE5OTk5OTk5OTk5NywzNjMgMjIyLjk1MTk5OTk5OTk5OTk3LDQ3OS4zIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJQRVQiIGRhdGEtdG89IkNvbXBsaWFuY2UiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuqygO2GoCDrsI8g6rCc7ISgIiBwb2ludHM9IjIyMi45NTE5OTk5OTk5OTk5Nyw3NDEuNCAyMjIuOTUxOTk5OTk5OTk5OTcsODU3LjciIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iREZEIiBkYXRhLXRvPSJUaHJlYXRUcmVlIiBkYXRhLWxhYmVsPSLsnITtmJEg7Yq466asIOunpO2VkSI+CiAgPHJlY3QgeD0iMTc2LjQ1MTk5OTk5OTk5OTk3IiB5PSIyMDIuOCIgd2lkdGg9IjkyLjQ5NDAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjIyLjY5ODk5OTk5OTk5OTk4IiB5PSIyMTcuOTUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuychO2YkSDtirjrpqwg66ek7ZWRPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlRocmVhdExpc3QiIGRhdGEtdG89IlBFVCIgZGF0YS1sYWJlbD0i7ZSE65287J2067KE7IucIOqwle2ZlCDquLDsiKAgUEVUIOyggeyaqSI+CiAgPHJlY3QgeD0iMTM0LjQ1MiIgeT0iNTgxLjIiIHdpZHRoPSIxNzYuODQyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjIyLjg3MyIgeT0iNTk2LjM1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7tlITrnbzsnbTrsoTsi5wg6rCV7ZmUIOq4sOyIoCBQRVQg7KCB7JqpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlRocmVhdFRyZWUiIGRhdGEtdG89IlRocmVhdExpc3QiIGRhdGEtbGFiZWw9Iuu2hOyEnSDsiJjtlokiPgogIDxyZWN0IHg9IjE4OS40NTE5OTk5OTk5OTk5NyIgeT0iNDA2LjAwMDAwMDAwMDAwMDA2IiB3aWR0aD0iNjYuOTUyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjIyLjkyNzk5OTk5OTk5OTk3IiB5PSI0MjEuMTUwMDAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuu2hOyEnSDsiJjtlok8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iUEVUIiBkYXRhLXRvPSJDb21wbGlhbmNlIiBkYXRhLWxhYmVsPSLqsoDthqAg67CPIOqwnOyEoCI+CiAgPHJlY3QgeD0iMTgyLjQ1MTk5OTk5OTk5OTk0IiB5PSI3ODQuNCIgd2lkdGg9IjgwLjYxNCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjIyMi43NTg5OTk5OTk5OTk5NiIgeT0iNzk5LjU1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7qsoDthqAg67CPIOqwnOyEoDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iREZEIiBkYXRhLWxhYmVsPSLrjbDsnbTthLAg7Z2Q66aE64+EIChERkQpIOyekeyEsQoo7ZSE66Gc7IS47IqkLCDsoIDsnqXshowsIOyZuOu2gCDso7zssrQsIO2dkOumhCkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iOTMuMDQ5OTk5OTk5OTk5OTgiIHk9Ijg0IiB3aWR0aD0iMjU5LjgwNCIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UzZjJmZCIgc3Ryb2tlPSIjMWU4OGU1IiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIyMjIuOTUxOTk5OTk5OTk5OTciIHk9IjExMC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIyMjIuOTUxOTk5OTk5OTk5OTciIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7rjbDsnbTthLAg7Z2Q66aE64+EIChERkQpIOyekeyEsTwvdHNwYW4+PHRzcGFuIHg9IjIyMi45NTE5OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+KO2UhOuhnOyEuOyKpCwg7KCA7J6l7IaMLCDsmbjrtoAg7KO87LK0LCDtnZDrpoQpPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlRocmVhdFRyZWUiIGRhdGEtbGFiZWw9IkxJTkREVU4gN+uMgCDsnITtmJEg7KCB7JqpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjEyOS43Mjk0OTk5OTk5OTk5NyIgeT0iMzI2LjEiIHdpZHRoPSIxODYuNDQ0OTk5OTk5OTk5OTYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2M2MjgyOCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMjIyLjk1MTk5OTk5OTk5OTk0IiB5PSIzNDQuNTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkxJTkREVU4gN+uMgCDsnITtmJEg7KCB7JqpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJUaHJlYXRMaXN0IiBkYXRhLWxhYmVsPSLtlITrnbzsnbTrsoTsi5wg7JyE7ZiRIOyLnOuCmOumrOyYpCDrj4TstpwiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTAyLjMxMjQ5OTk5OTk5OTk3IiB5PSI0NzkuMyIgd2lkdGg9IjI0MS4yNzkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyMjIuOTUxOTk5OTk5OTk5OTciIHk9IjQ5Ny43NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7ZSE65287J2067KE7IucIOychO2YkSDsi5zrgpjrpqzsmKQg64+E7LacPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQRVQiIGRhdGEtbGFiZWw9IuyVlO2YuO2ZlCwg67mE7Iud67OE7ZmULCDrj5nsnZgg6rSA66asIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjExNC4xNjg1IiB5PSI3MDQuNSIgd2lkdGg9IjIxNy41NjY5OTk5OTk5OTk5NSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjIyMi45NTE5OTk5OTk5OTk5NyIgeT0iNzIyLjk1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7slZTtmLjtmZQsIOu5hOyLneuzhO2ZlCwg64+Z7J2YIOq0gOumrDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ29tcGxpYW5jZSIgZGF0YS1sYWJlbD0i7ZSE65287J2067KE7IucIOq3nOyglSDspIDsiJggKEdEUFIsIOqwnOyduOygleuztOuztO2YuOuylSkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg1Ny43IiB3aWR0aD0iMzMzLjkwMzk5OTk5OTk5OTk0IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMyZTdkMzIiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjIyMi45NTE5OTk5OTk5OTk5NyIgeT0iODc2LjE1MDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPu2UhOudvOydtOuyhOyLnCDqt5zsoJUg7KSA7IiYIChHRFBSLCDqsJzsnbjsoJXrs7Trs7TtmLjrspUpPC90ZXh0Pgo8L2c+Cjwvc3ZnPg==)

---

### **II. LINDDUN의 7대 개인정보 위협 요소**

|**분류**|**🔗 연결 및 식별성 (Linkability & Identifiability)**|**🕵️ 추적·탐지 및 정보 누출 (Non-repudiation, Detectability, Disclosure)**|**⚖️ 사용자 미인지 및 미준수 (Unawareness & Non-compliance)**|
|---|---|---|---|
|**대상 위협**|**Linkability (L)**: 둘 이상의 데이터 조각을 동일 주체와 연관시키는 위협  <br>**Identifiability (I)**: 특정 데이터를 통해 정보주체를 직접 식별하는 위협|**Non-repudiation (N)**: 사용자가 특정 행동을 수행했음을 부인할 수 없게 만드는 위협  <br>**Detectability (D)**: 데이터 존재 유무가 탐지되는 위협  <br>**Disclosure (D)**: 권한 없는 대상에게 정보가 노출되는 위협|**Unawareness (U)**: 사용자가 자신의 데이터 수집/처리를 인지하지 못하는 위협  <br>**Non-compliance (N)**: 개인정보 관련 법령(GDPR 등) 및 정책을 준수하지 않는 위협|
|**상세 설명**|다양한 소스의 비식별 정보들을 결합하여 특정 개인을 재식별해 냄으로써 개인정보 프로파일링 유발|사용자가 활동 흔적을 부인하고 싶어도 추적 가능한 단서가 남거나, 전송 데이터의 크기/빈도로 사용자의 활동 양상이 노출되는 위협|동의 과정의 투명성 부족, 개인정보의 수집 범위 미고지 및 데이터 보호 규제 위반으로 인한 법적 리스크 유발|
|**방어 기술 (PETs)**|가명화, 데이터 마스킹, 차분 프라이버시(Differential Privacy)|암호화, 더미 트래픽 생성, 영지식 증명(Zero-Knowledge Proof)|개인정보 보호정책 공시, 동의 관리 시스템(CMP) 도입, 데이터 수명주기 관리|

---

### **III. LINDDUN과 타 위협 모델링 방법론(STRIDE)의 비교**

|**비교 항목**|**🛡️ LINDDUN (프라이버시 중심)**|**🔒 STRIDE (보안 중심)**|
|---|---|---|
|**주요 목표**|소프트웨어 설계 시 시스템 내 개인정보 침해 위협의 조기 식별 및 차단|소프트웨어 및 시스템의 기술적 보안 취약점(취약성) 식별 및 방어|
|**관점의 중심**|**정보주체(User/Data Subject)**의 프라이버시 권리 보호|**시스템(System/Asset)**의 안전성 및 신뢰성 확보|
|**주요 위협 카테고리**|Linkability, Identifiability, Non-repudiation, Detectability, Disclosure, Unawareness, Non-compliance|Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege|
|**보안 3대 요소 매핑**|기밀성(Confidentiality)에 편중되나, 법적 준수성 영역을 추가 포괄|기밀성(C), 무결성(I), 가용성(A) 전반을 6대 요소에 균형 있게 매핑|
|**주요 산출물**|프라이버시 위협 시나리오, 프라이버시 강화 기술(PETs) 적용 계획|기술적 보안 요구사항 정의서, 보안 패치 계획|

---

### **IV. LINDDUN 위협 모델링 적용을 위한 가이드라인**

**IMPORTANT**

1. **데이터 흐름도(DFD)의 정교화 및 프라이버시 속성 매핑**: LINDDUN 분석을 시작하기 전 시스템 DFD를 설계할 때, 일반적인 컴포넌트 정보 외에 **개인식별정보(PII)의 수집 경로, 저장 위치(DB), 외부 기관 전송 구간, 데이터 파기 주기**를 명확히 도식화하여 위협을 적용해야 합니다.
2. **프라이버시 강화 기술(PETs) 설계 반영**: 식별된 프라이버시 위협을 방지하기 위해 시스템 아키텍처 설계 초기에 데이터 가명처리 모듈을 반영하고, 동의 관리 플랫폼(CMP)과의 연동 및 데이터 보존 기간 만료 시 영구 파기 프로세스를 자동화해야 합니다.