
#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 공공 SaaS 도입에 별도 거버넌스가 필요한가)
Ⅱ. 공공 SaaS 거버넌스 가이드라인 체계
Ⅲ. 위험관리 4대 원칙
Ⅳ. 단계별 도입 절차
Ⅴ. 결론 및 발전 방향
```

포인트: 개요에서 **"앞서 다룬 CSAP 3등급제가 '공공 클라우드 보안 인증 관문'이라면, 공공 SaaS 거버넌스 가이드라인은 그 인증을 통과한 SaaS를 공공기관이 실제 도입·운영할 때 데이터 주권·서비스 연속성·개인정보 보호·공급자 종속(Vendor Lock-in) 위험을 체계적으로 관리하는 의사결정 프레임워크다 — 디지털플랫폼정부 구현·AIDC 특별법 시행과 맞물려 공공 SaaS 도입이 급증하는 상황에서 앞서 다룬 IT거버넌스의 5대 구성요소(전략적 정렬·가치 전달·리스크 관리·자원 관리·성과 측정)를 SaaS 도입 맥락에 특화 적용한 것"**이라는 한 줄로 시작하면, 왜 이 답안이 앞서 다룬 클라우드 보안·IT거버넌스·개인정보보호 시리즈 전체의 **공공 SaaS 실행 기반**인지 드러납니다.

---

#### Ⅱ. 공공 SaaS 거버넌스 가이드라인 체계

**가. 법적 근거 및 정책 체계**

| 근거               | 내용                          | 핵심 키워드                                      |
| ---------------- | --------------------------- | ------------------------------------------- |
| ==**클라우드컴퓨팅법**== | 제2조·제16조 공공기관 클라우드 우선 도입 원칙 | 클라우드 퍼스트(Cloud First) 정책 / 민간 클라우드 우선 검토 의무 |
| ==**전자정부법**==    | 정보시스템 구축·운영 기준·보안 요건        | 정보자원 관리·상호운용성·표준화                           |
| ==**개인정보보호법**==  | 제29조 안전조치·제35조의2 전송요구권      | 개인정보 처리 위탁 관리·수탁사 감독                        |
| ==**CSAP 등급제**== | 2023.1 시행·상·중·하 3등급         | 하등급: 공개데이터 SaaS / 중등급: 비공개 업무 / 상등급: 민감 행정  |
| ==**N2SF 연계**==  | 국가망보안체계 데이터 민감도 매핑          | S(기밀)→상등급 / C(민감)→중등급 / O(공개)→하등급 CSP       |

---

**나. 거버넌스 5대 구성 요소**==(전가리자성)==

```
[공공 SaaS 거버넌스 5대 구성요소]

①전략적 정렬 (Strategic Alignment)
  디지털플랫폼정부 목표 ↔ SaaS 도입 방향 일치
  ISP·EA 기반 중장기 SaaS 로드맵 수립
       ↓
②가치 전달 (Value Delivery)
  SaaS 도입 ROI 측정·편익 실현 관리
  TCO(구축비 절감)·운영 효율·서비스 품질 향상
       ↓
③리스크 관리 (Risk Management)
  4대 위험(아래 Ⅲ 참조) 식별·평가·대응
  공급자 종속·데이터 유출·서비스 중단·컴플라이언스
       ↓
④자원 관리 (Resource Management)
  SaaS 계약·비용·인력·데이터 자원 관리
  멀티 SaaS 환경의 통합 관리 체계
       ↓
⑤성과 측정 (Performance Measurement)
  SLA 준수율·가용성·응답시간·보안사고 건수
  KPI 기반 정기 성과 점검·재계약 의사결정
```

---

**다. SaaS 도입 적합성 평가 기준**

| ==평가 항목==       | 세부 기준                 | 판단 방법                    |
| ----------- | --------------------- | ------------------------ |
| ==**보안 적합성**==  | CSAP 등급 충족 여부·데이터 민감도 | N2SF 데이터 등급 ↔ CSAP 등급 매핑 |
| ==**기능 적합성**==  | 업무 요건 충족률·커스터마이징 가능성  | RFP 기반 기능 체크리스트          |
| ==**상호운용성**==   | 기존 시스템 연계·표준 API 지원   | OpenAPI·REST·데이터 표준 준수   |
| ==**서비스 연속성**== | SLA 수준·재해복구·백업 정책     | RTO·RPO·가용성 99.9% 이상     |
| ==**공급자 건전성**== | 재무 안정성·시장 지위·레퍼런스     | 재무제표·인증·공공 레퍼런스 확인       |
| ==**탈출 가능성**==  | 데이터 이식성·계약 종료 조건      | 표준 포맷 내보내기·이관 계획         |

---

#### Ⅲ. 위험관리 4대 원칙(==공데가컴==)

---

==**원칙 1️⃣ 공급자 종속 위험 관리 (Vendor Lock-in Risk)**==

```
[공급자 종속 위험 발생 구조]

SaaS 도입 → 독자 포맷·API 의존
    → 데이터·프로세스 종속 심화
    → 계약 종료·가격 인상 시 탈출 불가 🚨
```

| ==대응 원칙==          | 세부 내용                              | 실행 수단                                  |
| ------------------ | ---------------------------------- | -------------------------------------- |
| ==**데이터 이식성 확보**== | 표준 포맷(CSV·JSON·XML) 내보내기 의무 계약     | 앞서 다룬 **개인정보 전송요구권** 연계 / 정기 데이터 백업 수령 |
| ==**멀티 SaaS 전략**== | 단일 공급자 의존 배제·대체 서비스 선정             | 핵심 기능 2개↑ SaaS 검토 / 오픈소스 대안 사전 식별      |
| ==**표준 API 요구**==  | 독자 API 대신 RESTful·OpenAPI 표준 준수 계약 | 연계 시스템 독립성 유지                          |
| ==**계약 탈출 조항**==   | 계약 종료 시 데이터 반환·이관 지원 의무화           | 이관 기간 최소 90일 보장·비용 명시                  |

---

==**원칙 2️⃣ 데이터 주권·보안 위험 관리 (Data Sovereignty Risk)**==

```
[데이터 주권 위험 발생 구조]

공공 데이터 → 해외 SaaS 서버 저장
    → 외국 법령 적용(미국 CLOUD Act 등)
    → 국가 데이터 주권 침해 위험 🚨
```

| ==대응 원칙==             | 세부 내용                        | 실행 수단                                   |
| --------------------- | ---------------------------- | --------------------------------------- |
| ==**데이터 저장 위치 통제**==  | 국내 데이터센터 저장 의무 계약            | CSAP 인증 국내 CSP 우선 / 해외 SaaS는 하등급 공개데이터만 |
| ==**암호화 의무**==        | 저장·전송 전 구간 암호화               | AES-256·TLS 1.3 / 키 관리 공공기관 직접 보유       |
| ==**접근 통제**==         | SaaS 공급자 직원의 공공 데이터 접근 제한    | 접근 로그 감사·정기 점검                          |
| ==**개인정보 처리 위탁 관리**== | 앞서 다룬 **안전성 확보조치** 수탁사 관리 의무 | 위탁 계약서 필수 기재·연 1회↑ 점검                   |

---

==**원칙 3️⃣ 서비스 연속성 위험 관리 (Service Continuity Risk)**==

```
[서비스 연속성 위험 발생 구조]

SaaS 공급자 장애·파산·서비스 종료
    → 공공 서비스 중단
    → 국민 행정 서비스 불가 🚨
```

| ==대응 원칙==               | 세부 내용                 | 실행 수단                                      |
| ----------------------- | --------------------- | ------------------------------------------ |
| ==**SLA 수준 명시**==       | 가용성·응답시간·복구시간 계약 명시   | 가용성 99.9%↑ / RTO 4시간↓ / RPO 1시간↓           |
| ==**에스크로(Escrow) 계약**== | 소스코드·데이터 제3자 보관       | 공급자 파산 시 에스크로 기관에서 인수                      |
| ==**비상 대응 계획**==        | 공급자 장애 시 대체 운영 방안     | 앞서 다룬 **BCP·DRP** 연계 / 대체 SaaS 전환 절차 사전 수립 |
| ==**정기 복구 훈련**==        | SaaS 장애 시 복구 절차 정기 검증 | 연 1회↑ 모의 장애 훈련·복구 시간 측정                    |

---

==**원칙 4️⃣ 컴플라이언스 위험 관리 (Compliance Risk)**==

```
[컴플라이언스 위험 발생 구조]

SaaS 도입 → 법령·규제 준수 미확인
    → 개인정보 유출·보안 인증 미충족
    → 과징금·형사처벌·감사 지적 🚨
```

| ==대응 원칙==          | 세부 내용                          | 실행 수단                       |
| -------------- | ------------------------------ | --------------------------- |
| ==**CSAP 인증 확인**== | 도입 SaaS의 CSAP 등급 적합성 검증        | N2SF 데이터 등급 ↔ CSAP 등급 매핑 준수 |
| ==**개인정보 영향평가**==  | 앞서 다룬 **PIA 의무 대상** 해당 시 사전 평가 | 5만명↑ 공공기관 SaaS 도입 시 PIA 필수  |
| ==**정기 보안 감사**==   | SaaS 공급자의 보안 수준 정기 점검          | 연 2회↑ 취약점 점검·ISMS 인증 확인     |
| ==**변경 관리**==      | 법령 개정·CSAP 기준 변경 시 재평가         | 분기별 규제 변화 모니터링·계약 반영        |

---

#### Ⅳ. 단계별 도입 절차

```
[공공 SaaS 도입 4단계 절차]

①사전 검토 단계
  업무 적합성 분석·데이터 민감도 분류
  N2SF 등급 결정 → CSAP 요구 등급 도출
  ISP·EA 연계 검토
       ↓
②공급자 선정 단계
  RFP 작성(보안·SLA·이식성·컴플라이언스)
  CSAP 인증 확인·기술 평가·가격 평가
  위험관리 4대 원칙 기반 계약서 작성
       ↓
③도입·운영 단계
  데이터 이관·연계 시스템 구축
  사용자 교육·내부 관리계획 수립
  SLA 모니터링·접속 기록 관리
       ↓
④성과 평가·갱신 단계
  KPI 기반 성과 측정(가용성·만족도·보안)
  재계약·서비스 교체·탈출 의사결정
  앞서 다룬 DORA 지표 연계 운영 성숙도 평가
```

---

#### Ⅴ. 결론 및 발전 방향

**앞서 다룬 개념과의 통합 연결**

| 연계 개념            | 연결 내용                                 |
| ---------------- | ------------------------------------- |
| **CSAP 3등급제**    | SaaS 도입 시 데이터 민감도별 인증 등급 필수 확인        |
| **N2SF**         | S·C·O 등급 → 상·중·하 CSAP 매핑으로 SaaS 선택 기준 |
| **개인정보 안전조치**    | 수탁사 관리·암호화·접속기록 SaaS 계약에 의무 반영        |
| **IT거버넌스 5대 요소** | SaaS 거버넌스의 전략적 정렬·가치 전달·리스크 관리 구조화    |
| **AIDC 특별법**     | AI 데이터센터 기반 공공 AI SaaS 도입 가속화 대응      |
| **제로트러스트**       | SaaS 접근 시 ZTNA·MFA·지속 검증 체계 적용        |

**발전 방향**

- **AI SaaS 거버넌스 특화**: 고영향 AI SaaS 도입 시 인공지능기본법 영향평가 연계
- **마이데이터 연계**: 공공 SaaS 보유 데이터 전송요구권 이행 체계 구축
- **소버린 클라우드**: 국내 법령 적용 가능한 공공 전용 SaaS 환경 구축
- **멀티 SaaS 통합 관리**: 공공기관 SaaS 포털 단일 가시성(Single Pane of Glass) 구현

---

#### 기술사 답안 포인트

**클라우드컴퓨팅법·CSAP·N2SF·개인정보보호법 법적 근거 → IT거버넌스 5대 요소 SaaS 특화 적용 → 공급자 종속·데이터 주권·서비스 연속성·컴플라이언스 위험관리 4대 원칙 → 원칙별 대응 수단(에스크로·멀티 SaaS·PIA·CSAP 매핑) → 사전검토·선정·운영·평가 4단계 절차 → AI SaaS·마이데이터·소버린 클라우드 발전 방향** 흐름으로 서술하면 거버넌스·보안·법제도를 아우르는 완성도 높은 답안이 됩니다. **위험관리 4대 원칙(공급자 종속·데이터 주권·서비스 연속성·컴플라이언스)이 핵심 차별화 포인트**입니다.

### **I. 공공 SaaS 도입의 거버넌스 가이드라인, 위험관리 4대 원칙 개요**

공공기관이 민간 SaaS를 도입하면 인프라 및 소프트웨어 소스코드에 대한 통제권이 외부 클라우드 제공업체(CSP)로 이전되어 새로운 보안 위협과 운영 위험이 발생합니다. 이에 대응하여 행정안전부는 공공기관이 안전하게 민간 클라우드를 이용할 수 있도록 책임 분담 및 대체 수단 확보 등을 골자로 하는 \*\*'위험관리 4대 원칙'\*\*을 정립하고, 도입 전 \*\*'보안성 검토 절차'\*\*를 이행하도록 강제하고 있습니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjE2LjI1Nzk5OTk5OTk5OTggMjAxLjgiIHdpZHRoPSIxMjE2LjI1Nzk5OTk5OTk5OTgiIGhlaWdodD0iMjAxLjgiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUk9PVCIgZGF0YS10bz0iU2hhcmVkIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjU4NS44OTg5OTk5OTk5OTk5LDc2LjkgNTg1Ljg5ODk5OTk5OTk5OTksOTQuOSAyMDYuMjEwOTk5OTk5OTk5OTgsOTQuOSAyMDYuMjEwOTk5OTk5OTk5OTgsMTEyLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlJPT1QiIGRhdGEtdG89Ik1vbml0b3IiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNTg1Ljg5ODk5OTk5OTk5OTksNzYuOSA1ODUuODk4OTk5OTk5OTk5OSw5NC45IDU4NS44OTg5OTk5OTk5OTk5LDk0LjkgNTg1Ljg5ODk5OTk5OTk5OTksMTEyLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlJPT1QiIGRhdGEtdG89IkV4aXQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNTg1Ljg5ODk5OTk5OTk5OTksNzYuOSA1ODUuODk4OTk5OTk5OTk5OSw5NC45IDk4Ny44MTY5OTk5OTk5OTk5LDk0LjkgOTg3LjgxNjk5OTk5OTk5OTksMTEyLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJPT1QiIGRhdGEtbGFiZWw9IlNhYVMg7JyE7ZeY6rSA66asIOybkOy5mSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1MDEuOTM4OTk5OTk5OTk5OSIgeT0iNDAiIHdpZHRoPSIxNjcuOTIiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjU4NS44OTg5OTk5OTk5OTk5IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+U2FhUyDsnITtl5jqtIDrpqwg7JuQ7LmZPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTaGFyZWQiIGRhdGEtbGFiZWw9IjEuIOyxheyehCDrtoTri7QgOiBDU1DsmYAg6rO16rO16riw6rSA7J2YIOuztOyViCDqsr3qs4Qg67aE7ZWgIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwIiB5PSIxMTIuOSIgd2lkdGg9IjMzMi40MjE5OTk5OTk5OTk5NyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjIwNi4yMTA5OTk5OTk5OTk5OCIgeT0iMTMxLjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij4xLiDssYXsnoQg67aE64u0IDogQ1NQ7JmAIOqzteqzteq4sOq0gOydmCDrs7TslYgg6rK96rOEIOu2hO2VoDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTW9uaXRvciIgZGF0YS1sYWJlbD0iMi4g7KeA7IaN7KCBIOqwkOyLnCA6IOyEnOu5hOyKpCDqsIDsmqnshLEv7J6l7JWgIOyLpOyLnOqwhCDrqqjri4jthLDrp4EiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDAwLjQyMTk5OTk5OTk5OTk3IiB5PSIxMTIuOSIgd2lkdGg9IjM3MC45NTM5OTk5OTk5OTk5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNTg1Ljg5ODk5OTk5OTk5OTkiIHk9IjEzMS4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Mi4g7KeA7IaN7KCBIOqwkOyLnCA6IOyEnOu5hOyKpCDqsIDsmqnshLEv7J6l7JWgIOyLpOyLnOqwhCDrqqjri4jthLDrp4E8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkV4aXQiIGRhdGEtbGFiZWw9IjMuIOuMgOyytOyImOuLqCDtmZXrs7QgOiDshJzruYTsiqQg7J6l7JWgL+yiheujjCDsi5wg7J206rSAL+yasO2ajCDsoITrnrUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNzk5LjM3NiIgeT0iMTEyLjkiIHdpZHRoPSIzNzYuODgxOTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI5ODcuODE2OTk5OTk5OTk5OSIgeT0iMTMxLjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij4zLiDrjIDssrTsiJjri6gg7ZmV67O0IDog7ISc67mE7IqkIOyepeyVoC/sooXro4wg7IucIOydtOq0gC/smrDtmowg7KCE6561PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

***

### **II. 공공기관 민간 클라우드(SaaS) 이용 위험관리 4대 원칙의 세부 내용**

| ==**🔑 위험관리 4대 원칙 🚨**== | **🏁 상세 내용 및 통제 가이드라인 💯**                                           |
| :------------------- | :------------------------------------------------------------------- |
| ==**1. 책임 분담의 원칙**==     | 서비스 모델(SaaS)에 따라 클라우드 제공업체(CSP)와 도입 기관 간의 보안 및 장애 책임을 명확히 분할         |
| ==**2. 위험 수인의 원칙**==     | 민간 클라우드 이용에 따른 잔재 위험을 완벽히 제거할 수 없음을 인지하고, 수용 가능한 위험 수준(Appetite) 정의  |
| ==**3. 지속적 모니터링 원칙**==   | 도입 이후에도 서비스수준계약(SLA) 준수 여부 및 보안 설정 변경 상태를 실시간/주기적으로 모니터링             |
| ==**4. 대체 수단 확보 원칙**==   | 서비스 중단, 사업자 부도 등 비상 상황 발생 시 업무 마비를 방지하기 위한 백업 시스템 또는 수작업 전환 등 우회책 수립 |

***

### **III. 기존 공공 클라우드 가이드(IaaS/PaaS)와 민간 SaaS 이용 가이드라인의 비교**

| **비교 항목**        | **💻 기존 공공 클라우드 가이드 (IaaS/PaaS)** | **☁️ 신규 민간 SaaS 이용 가이드라인**               |
| :--------------- | :-------------------------------- | :--------------------------------------- |
| **통제 범위**        | 인프라 자원(VM, 스토리지 등) 직접 제어          | 완성된 어플리케이션(SaaS) 구독 및 API 연동 제어          |
| **보안 검토 기준**     | 가상 방화벽, 포트 및 암호화 등 기관 설정 확인       | **CSAP 등급제 인증 여부** 및 **SaaS 보안인증 획득 확인** |
| **장애 대응 책임**     | 가상 인프라 위의 운영체제 및 앱 장애는 기관 책임      | **SaaS 자체 버그 및 실행 장애는 전적으로 CSP 책임**      |
| **출구 전략 (Exit)** | VM 이미지 백업 및 타 CSP 이식성 검증          | **SaaS Exit 전략(데이터 추출, 타 서비스 연동) 검증**    |

***

### **IV. 공공기관 민간 SaaS 도입 시 보안성 검토 수행 절차**

**IMPORTANT**

1. **서비스 대상 선정 및 등급 분류**: 행정안전부 고시에 의거, 도입하려는 정보시스템의 중요도를 분류하여 상/중/하 등급에 적합한 CSAP 인증을 획득한 SaaS 제품군을 필터링해야 합니다.
2. **망분리 예외 연동성 검토**: 공공기관 내부 업무망에서 외부 민간 클라우드 SaaS로 연동될 때, 내부 데이터 유출 경로가 되지 않도록 전용 API 게이트웨이 보안 통제 및 데이터 마스킹 조치 여부를 국정원 보안성 심사 기준에 맞춰 검증해야 합니다.
