#### **개인정보보호 관리체계 국제 표준: ISO/IEC 27701**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 정보보안 인증만으로는 개인정보보호를 증명 못 하는가)
Ⅱ. ISO/IEC 27701 핵심 구조
Ⅲ. 국내외 인증 체계 비교 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 개인정보 안전성 확보조치 기준이 '국내 개인정보보호법의 구체적 기술·관리 의무'라면, ISO/IEC 27701은 그 개인정보보호를 전사적 경영시스템(Management System) 수준으로 끌어올려 국제적으로 공인받는 표준이다 — 기존 ISO/IEC 27001이 '정보 자산 전반의 기밀성·무결성·가용성을 보호하는 정보보안경영시스템(ISMS)'을 다룬다면, 2019년 제정된 27701은 그 위에 '개인정보(PII)를 처리하는 조직이 GDPR·CCPA 같은 전 세계 다양한 개인정보 법제를 하나의 공통 프레임워크로 충족할 수 있게 확장한 개인정보보호경영시스템(PIMS) 인증'이며, 국내 ISMS-P가 정보보안+개인정보보호를 결합한 국내 특화 인증이라면 27701은 그 국제판에 해당하는 글로벌 상호운용 표준"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.
![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MDMuOTY1OTk5OTk5OTk5OSAyODYuNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSI4MDMuOTY1OTk5OTk5OTk5OSIgaGVpZ2h0PSIyODYuNzAwMDAwMDAwMDAwMDUiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iSVNNUyIgZGF0YS10bz0iUElNUyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0MDAuNTAwOTk5OTk5OTk5OSw3Ni45IDQwMC41MDA5OTk5OTk5OTk5LDEyNC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJQSU1TIiBkYXRhLXRvPSJDb250cm9sbGVyIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQwMC41MDA5OTk5OTk5OTk5LDE2MS44IDQwMC41MDA5OTk5OTk5OTk5LDE4NS44IDIxMi41MDk0OTk5OTk5OTk5NywxODUuOCAyMTIuNTA5NDk5OTk5OTk5OTcsMjA5LjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlBJTVMiIGRhdGEtdG89IlByb2Nlc3NvciIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0MDAuNTAwOTk5OTk5OTk5OSwxNjEuOCA0MDAuNTAwOTk5OTk5OTk5OSwxODUuOCA1ODguNDkyNDk5OTk5OTk5OCwxODUuOCA1ODguNDkyNDk5OTk5OTk5OCwyMDkuOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iSVNNUyIgZGF0YS1sYWJlbD0iSVNPL0lFQyAyNzAwMSA6IOygleuztOuztOyViCDqsr3smIHsi5zsiqTthZwg7ZWE7IiYIOyEoO2WiSDquLDrsJgiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjIwLjIxMDk5OTk5OTk5OTkzIiB5PSI0MCIgd2lkdGg9IjM2MC41OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDAwLjUwMDk5OTk5OTk5OTkiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5JU08vSUVDIDI3MDAxIDog7KCV67O067O07JWIIOqyveyYgeyLnOyKpO2FnCDtlYTsiJgg7ISg7ZaJIOq4sOuwmDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUElNUyIgZGF0YS1sYWJlbD0iSVNPL0lFQyAyNzcwMSA6IOqwnOyduOygleuztOuztO2YuCDqsr3smIHsi5zsiqTthZwg7ZmV7J6lIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjIzNy4yNTM5OTk5OTk5OTk5MyIgeT0iMTI0LjkiIHdpZHRoPSIzMjYuNDkzOTk5OTk5OTk5OTciIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNDAwLjUwMDk5OTk5OTk5OTkiIHk9IjE0My4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+SVNPL0lFQyAyNzcwMSA6IOqwnOyduOygleuztOuztO2YuCDqsr3smIHsi5zsiqTthZwg7ZmV7J6lPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDb250cm9sbGVyIiBkYXRhLWxhYmVsPSJDbGF1c2UgNyAvIEFubmV4IEEgOiBQSUkgQ29udHJvbGxlciDsspjrpqzsnpAg7KCE7JqpIO2GteygnCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MCIgeT0iMjA5LjgiIHdpZHRoPSIzNDUuMDE4OTk5OTk5OTk5OTUiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyMTIuNTA5NDk5OTk5OTk5OTciIHk9IjIyOC4yNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Q2xhdXNlIDcgLyBBbm5leCBBIDogUElJIENvbnRyb2xsZXIg7LKY66as7J6QIOyghOyaqSDthrXsoJw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlByb2Nlc3NvciIgZGF0YS1sYWJlbD0iQ2xhdXNlIDggLyBBbm5leCBCIDogUElJIFByb2Nlc3NvciDsiJjtg4HsnpAg7KCE7JqpIO2GteygnCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MTMuMDE4OTk5OTk5OTk5OTUiIHk9IjIwOS44IiB3aWR0aD0iMzUwLjk0Njk5OTk5OTk5OTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1ODguNDkyNDk5OTk5OTk5OCIgeT0iMjI4LjI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5DbGF1c2UgOCAvIEFubmV4IEIgOiBQSUkgUHJvY2Vzc29yIOyImO2DgeyekCDsoITsmqkg7Ya17KCcPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

***

#### Ⅱ. ISO/IEC 27701 핵심 구조

**가. 27701의 위치: 27001의 확장(Extension)**

```
[ISO 27000 패밀리 내 27701의 구조적 위치]

ISO/IEC 27001 (ISMS·정보보안경영시스템)
  Annex A: 정보보안 통제 항목(93개, 2022개정판 기준)
       ↓ 확장(Extension)
ISO/IEC 27701 (PIMS·개인정보보호경영시스템)
  27001의 모든 요구사항 그대로 승계 +
  개인정보 처리자 역할별(PII Controller/Processor) 추가 통제

핵심 특징:
  27701은 단독 인증이 불가능 🚨
  반드시 27001 인증을 기반으로 그 위에 확장 인증받는 구조
  (27001 없이 27701만 취득 불가)
```

**나. PII Controller vs PII Processor 역할 구분**

| 역할                          | 정의                           | 국내 개인정보보호법 대응   |
| :-------------------------- | :--------------------------- | :-------------- |
| **PII Controller(개인정보처리자)** | 개인정보 처리 목적·방법을 결정하는 주체       | 개인정보처리자         |
| **PII Processor(수탁처리자)**    | Controller의 지시에 따라 위탁 처리만 수행 | 개인정보처리 위탁을 받은 자 |

**다. 27701 부속서(Annex) 구조**

| 부속서           | 대상             | 내용                        |
| :------------ | :------------- | :------------------------ |
| **Annex A**   | PII Controller | 개인정보처리자 특화 추가 통제 항목       |
| **Annex B**   | PII Processor  | 수탁처리자 특화 추가 통제 항목         |
| **Annex C**   | ISO 29100 매핑   | 개인정보보호 프레임워크(29100)와의 연계표 |
| **Annex D**   | GDPR 매핑        | EU GDPR 조항별 대응 관계표        |
| **Annex E/F** | 기타 국가별 규제 매핑   | 각국 개인정보 법제와의 상호 대응표       |

***

#### Ⅲ. 국내외 인증 체계 비교 및 적용 체계

**가. ISO/IEC 27701 vs ISMS-P vs GDPR 인증 비교**

| 비교 항목         | ISO/IEC 27701          | ISMS-P(국내)         | GDPR(EU 규제)               |
| :------------ | :--------------------- | :----------------- | :------------------------ |
| **성격**        | **국제 인증 표준**           | 국내 법정 인증           | 법률(인증 아님)                 |
| **기반 표준**     | ISO 27001 확장           | K-ISMS + 개인정보보호 결합 | 별도 법조문                    |
| **적용 범위**     | **전 세계 상호운용** ✅        | 국내 한정              | EU 역내·역외 적용               |
| **법적 강제성**    | 자율 인증(계약상 요구 가능)       | 일부 대상 의무           | **법적 의무**(위반 시 매출 4% 과징금) |
| **글로벌 사업 활용** | **해외 고객사 신뢰 확보에 유리** ✅ | 해외에서 인지도 낮음 🚨     | 준수 증빙 자료로 27701 활용 가능     |
| **인증 기관**     | 국제 인증기관(공인 CB)         | KISA·인터넷진흥원 지정기관   | 별도 인증기관 없음                |

**나. 국내 ISMS-P와의 관계 및 활용 전략**

| 항목                              | 내용                                                    |
| :------------------------------ | :---------------------------------------------------- |
| **중복성**                         | ISMS-P와 27701은 통제 항목이 상당 부분 유사(둘 다 27001 계열 기반)       |
| **동시 취득 이점**                    | 통합 심사(Integrated Audit)로 심사 비용·시간 절감 가능               |
| **국내기업 활용 시나리오**                | 국내는 ISMS-P로 법적 요건 충족, 해외 수출·글로벌 클라이언트 대응은 27701 추가 취득 |
| **KIPRIS Plus 등 공공 IP 플랫폼 시사점** | 해외 특허청·글로벌 IP 기관과의 데이터 연동 시 27701이 신뢰 기반 근거로 작용 가능    |

**다. 27701 도입 프로세스**

| 단계                      | 내용                                                |
| :---------------------- | :------------------------------------------------ |
| **①갭 분석(Gap Analysis)** | 기존 27001 통제와 27701 추가 요구사항 간 차이 진단                |
| **②PII 처리 활동 매핑**       | 앞서 다룬 \*\*데이터 계보(Lineage)\*\*처럼 개인정보 흐름을 전사적으로 매핑 |
| **③역할 결정**              | 조직이 Controller인지 Processor인지(또는 둘 다인지) 명확화        |
| **④통제 이행**              | Annex A/B의 추가 통제 항목을 정책·절차·기술로 구현                 |
| **⑤내부 심사·인증 심사**        | 27001 인증 심사와 통합해 진행하는 것이 일반적                      |

**라. 27701이 요구하는 대표 추가 통제 영역**

| 영역               | 내용                                           |
| :--------------- | :------------------------------------------- |
| **동의 관리**        | 정보주체 동의 취득·철회 절차의 체계적 관리                     |
| **정보주체 권리 대응**   | 열람·정정·삭제·전송 요구에 대한 표준화된 대응 절차(SLA 포함)        |
| **PII 처리 목적 제한** | 수집 목적 외 사용 방지를 위한 기술적·관리적 통제                 |
| **국외 이전 관리**     | 앞서 다룬 **가명정보 결합**과 유사하게, 국경 간 이전 시 적정성 보장 절차 |
| **개인정보 침해 통지**   | 사고 발생 시 규제기관·정보주체 통지 절차 및 기한 관리              |

***

**(제언)** "ISO/IEC 27701의 실질적 가치는 GDPR·CCPA·국내 개인정보보호법처럼 국가마다 제각각인 개인정보 규제를 매번 별도로 대응하는 대신, 하나의 국제 표준 프레임워크를 구축해두면 Annex C\~F의 매핑표를 통해 여러 법제 요구사항을 동시에 충족했음을 효율적으로 증명할 수 있다는 데 있습니다. 국내 조직 입장에서는 이미 ISMS-P를 획득했다면 통제 체계의 상당 부분이 27701과 중복되므로 추가 취득 비용이 크지 않은 반면, 해외 고객사·글로벌 파트너와의 계약에서 국제적으로 통용되는 신뢰 증빙이 필요한 경우(예: KIPRIS Plus의 해외 특허청 데이터 연동, 글로벌 SaaS 진출) 27701이 ISMS-P보다 훨씬 설득력 있는 근거가 되므로, 국내 규제 대응은 ISMS-P로, 국제 신뢰 확보는 27701로 이원화하는 전략과 두 인증의 통합 심사를 통한 비용 효율화를 함께 고려하는 것이 실무적으로 합리적입니다.

***

**앞서 다룬 개념과의 연결**

| 연계 개념                   | 연결 내용                                                      |
| :---------------------- | :--------------------------------------------------------- |
| **개인정보 안전성 확보조치 기준**    | 27701의 기술적 통제 항목이 국내 안전조치 기준과 상당 부분 내용상 대응                 |
| **가명정보 결합**             | 27701의 국외 이전·목적 제한 통제가 가명정보 결합 시의 안전조치 요구와 연계              |
| **데이터 계보(Lineage)**     | PII 처리 활동 매핑 단계에서 데이터 계보 추적 체계를 그대로 활용 가능                  |
| **Hoepman 8대 프라이버시 전략** | 27701의 통제 항목들이 Hoepman 전략을 경영시스템 차원에서 제도화한 것               |
| **AI 레드티밍·인공지능기본법**     | 향후 AI 특화 확장(ISO/IEC 42001 등)과 함께 AI 개인정보 거버넌스의 국제 표준 기반 형성 |

### **I. 글로벌 프라이버시 관리체계의 표준, ISO/IEC 27701의 개요**

전 세계적으로 개인정보 침해에 대한 과징금 수위가 높아짐에 따라, 글로벌 서비스를 제공하는 기업들은 국별 개인정보 법률을 넘어서는 통합 관리체계가 필요해졌습니다. **ISO/IEC 27701**은 정보보안 경영시스템 표준인 **ISO/IEC 27001 및 27002의 확장 표준**으로 제정되었으며, 기업이 개인식별정보(PII: Personally Identifiable Information)를 수집, 처리, 보관, 파기하는 전 과정에 대해 **PII 처리자(Controller)와 수탁자(Processor)의 통제 항목을 제시하는 글로벌 PIMS 인증 표준**입니다.

***

### **II. ISO/IEC 27701의 아키텍처 및 4대 핵심 구조**

#### **1. 표준문서 조항(Clause) 체계**

* **Clause 5**: ISO/IEC 27001 연계 개인정보보호 조직 요구사항 확장 (PIMS 전용 리스크 평가)
* **Clause 6**: ISO/IEC 27002 정보보안 통제 항목에 프라이버시 관점의 지침 확장
* **Clause 7 (Annex A)**: **PII Controller (개인정보 처리자)** 지침 (동의 관리, 최소 수집, 주체 권리 보장 등)
* **Clause 8 (Annex B)**: **PII Processor (개인정보 수탁자)** 지침 (위탁 계약 준수, 하도급 통제 등)

#### **2. 프라이버시 핵심 통제 원칙**

* **Privacy by Design (기획 단계 프라이버시 내재화)**: 서비스 개발 기획 시점부터 프라이버시 영향평가(PIA) 수행
* **주체 권리 보장 (Data Subject Rights)**: 데이터 열람, 정정, 삭제(잊힐 권리), 이동권 보장 통제

***

### **III. 기존 ISO/IEC 27001(정보보안)과 신규 ISO/IEC 27701(개인정보)의 상세 비교**

| **비교 항목**     | **🛡️ ISO/IEC 27001 (ISMS 표준)** | **🔒 ISO/IEC 27701 (PIMS 표준)**                        |
| :------------ | :------------------------------ | :---------------------------------------------------- |
| **핵심 보안 목표**  | 정보 자산의 기밀성, 무결성, 가용성 (CIA) 보장   | **개인식별정보(PII) 주체의 프라이버시 보호 및 규제 준수**                  |
| **인증 획득 조건**  | **단독 독립 인증 획득 가능**              | **단독 인증 불가 (ISO/IEC 27001 인증 보유 선행 필수)**              |
| **보안 대상 자산**  | 기업의 모든 IT 인프라, 데이터, 인적 자원       | **기업이 취급하는 모든 PII (고객/임직원 개인정보)**                     |
| **통제 역할 분리**  | 정보보안 담당자 및 IT 관리자 중심 통제         | **PII Controller(처리자)와 PII Processor(수탁자)로 역할 명확 분리** |
| **글로벌 규제 매핑** | 기업 일반 정보보안 관리체계 수립 지표           | **EU GDPR, US CCPA 등 글로벌 프라이버시 법률 대치 증적**             |

***

### **IV. ISO/IEC 27701 기반 글로벌 프라이버시 거버넌스 구축 전략**

1. **EU GDPR 적격성 증적 활용**: ISO/IEC 27701 인증을 보유하면 GDPR Article 42(인증 메커니즘)에 의거하여 감독기관 검사 시 개인정보보호 조치의 유효성을 입증하는 강력한 면책/감경 증적으로 활용할 수 있습니다.
2. **국내 ISMS-P 인증과의 통합 운용**: 국내 기업이 해외 진출 시 한국의 ISMS-P 인증과 ISO 27701을 별도로 수립하면 중복 오버헤드가 크므로, 동일한 프라이버시 영향평가(PIA)와 PII 자산 카탈로그를 공유하여 수평 통합 심사를 받는 것이 효율적입니다.
