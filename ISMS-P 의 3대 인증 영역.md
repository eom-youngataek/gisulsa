#### **국내 정보보호·개인정보보호 통합 인증: ISMS-P 3대 인증 영역**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 정보보안과 개인정보보호 인증을 하나로 통합했는가)
Ⅱ. ISMS-P 3대 인증 영역 핵심 구조
Ⅲ. 인증 체계 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 ISO/IEC 27701이 '국제 표준 체계에서 27001 위에 개인정보보호를 확장'한 것이라면, ISMS-P(정보보호 및 개인정보보호 관리체계 인증)는 국내에서 동일한 문제의식 — 기존 정보보안 인증(ISMS)과 개인정보보호 인증(PIMS)이 별도로 운영되며 발생한 기업의 중복 심사 부담과 관리 비효율 — 을 2018년 두 인증을 통합해 해결한 국가 공인 인증제도다 — 정보통신망법·개인정보보호법을 법적 근거로 하며, 일정 규모 이상 정보통신서비스 제공자에게는 ISMS 인증이 의무이고, 개인정보를 처리하는 기업이 신청 시 개인정보보호 영역까지 확장해 통합 인증받을 수 있는 구조로, 크게 '관리체계 수립 및 운영'·'보호대책 요구사항'·'개인정보 처리단계별 요구사항'의 3대 영역, 총 101개 인증기준으로 구성된 국내 정보보호 거버넌스의 핵심 표준"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDUxLjAxNDk5OTk5OTk5OTkgMjAxLjgiIHdpZHRoPSIxMDUxLjAxNDk5OTk5OTk5OTkiIGhlaWdodD0iMjAxLjgiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUk9PVCIgZGF0YS10bz0iQXJlYTEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDkyLjUzMjk5OTk5OTk5OTk2LDc2LjkgNDkyLjUzMjk5OTk5OTk5OTk2LDk0LjkgMTgzLjIzOTk5OTk5OTk5OTk4LDk0LjkgMTgzLjIzOTk5OTk5OTk5OTk4LDExMi45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJST09UIiBkYXRhLXRvPSJBcmVhMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0OTIuNTMyOTk5OTk5OTk5OTYsNzYuOSA0OTIuNTMyOTk5OTk5OTk5OTYsOTQuOSA0OTIuNTMyOTk5OTk5OTk5OTYsOTQuOSA0OTIuNTMyOTk5OTk5OTk5OTYsMTEyLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlJPT1QiIGRhdGEtdG89IkFyZWEzIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQ5Mi41MzI5OTk5OTk5OTk5Niw3Ni45IDQ5Mi41MzI5OTk5OTk5OTk5Niw5NC45IDgzNC44MDA0OTk5OTk5OTk5LDk0LjkgODM0LjgwMDQ5OTk5OTk5OTksMTEyLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJPT1QiIGRhdGEtbGFiZWw9IklTTVMtUCAz64yAIOyduOymnSDsmIHsl60gOiDstJ0gMTAy6rCcIO2GteygnO2VreuqqSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzNDUuOTU4NDk5OTk5OTk5OTYiIHk9IjQwIiB3aWR0aD0iMjkzLjE0OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDkyLjUzMjk5OTk5OTk5OTk2IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+SVNNUy1QIDPrjIAg7J247KadIOyYgeyXrSA6IOy0nSAxMDLqsJwg7Ya17KCc7ZWt66qpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBcmVhMSIgZGF0YS1sYWJlbD0i7JiB7JetIDEuIOq0gOumrOyytOqzhCDsiJjrpr0g67CPIOyatOyYgSA6IDE26rCcIO2VreuqqSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MCIgeT0iMTEyLjkiIHdpZHRoPSIyODYuNDc5OTk5OTk5OTk5OTYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxODMuMjM5OTk5OTk5OTk5OTgiIHk9IjEzMS4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7JiB7JetIDEuIOq0gOumrOyytOqzhCDsiJjrpr0g67CPIOyatOyYgSA6IDE26rCcIO2VreuqqTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQXJlYTIiIGRhdGEtbGFiZWw9IuyYgeyXrSAyLiDrs7TtmLjrjIDssYUg7JqU6rWs7IKs7ZWtIDogNjTqsJwg7ZWt66qpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM1NC40Nzk5OTk5OTk5OTk5NiIgeT0iMTEyLjkiIHdpZHRoPSIyNzYuMTA2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDkyLjUzMjk5OTk5OTk5OTk2IiB5PSIxMzEuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyYgeyXrSAyLiDrs7TtmLjrjIDssYUg7JqU6rWs7IKs7ZWtIDogNjTqsJwg7ZWt66qpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBcmVhMyIgZGF0YS1sYWJlbD0i7JiB7JetIDMuIOqwnOyduOygleuztCDsspjrpqzri6jqs4Trs4Qg7JqU6rWs7IKs7ZWtIDogMjLqsJwg7ZWt66qpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjY1OC41ODYiIHk9IjExMi45IiB3aWR0aD0iMzUyLjQyODk5OTk5OTk5OTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iODM0LjgwMDQ5OTk5OTk5OTkiIHk9IjEzMS4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7JiB7JetIDMuIOqwnOyduOygleuztCDsspjrpqzri6jqs4Trs4Qg7JqU6rWs7IKs7ZWtIDogMjLqsJwg7ZWt66qpPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

***

#### Ⅱ. ISMS-P 3대 인증 영역 핵심 구조

**가. 3대 인증 영역 개요**

```
[ISMS-P 인증기준 구조: 3개 영역, 101개 항목]

①관리체계 수립 및 운영 (16개 항목)
  ISMS·ISMS-P 공통 적용
  PDCA 사이클 기반 관리체계 자체의 존재·작동 여부
       ↓
②보호대책 요구사항 (64개 항목)
  ISMS·ISMS-P 공통 적용
  정보보안 기술적·관리적·물리적 통제
       ↓
③개인정보 처리단계별 요구사항 (21개 항목)
  ISMS-P 신청 시에만 추가 적용
  개인정보 수집부터 파기까지 생애주기별 통제

→ ISMS만 신청: ①+②(80개 항목)
→ ISMS-P 신청: ①+②+③(101개 항목 전체)
```

**나. 영역별 핵심 통제 내용**

| 인증 영역                | 하위 분류                                                                                                                       | 핵심 내용                                                      |
| :------------------- | :-------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------- |
| **①관리체계 수립 및 운영**    | 관리체계 기반 마련 / 위험 관리 / 관리체계 운영 / 관리체계 점검 및 개선                                                                                 | 경영진 참여·정책 수립·위험평가·내부감사의 **PDCA 순환 체계**                     |
| **②보호대책 요구사항**       | 정책·조직·자산관리 / 인적보안 / 외부자보안 / 물리보안 / 인증 및 권한관리 / 접근통제 / 암호화 적용 / 정보시스템 도입·개발보안 / 시스템·서비스 운영관리 / 시스템·서비스 보안관리 / 사고예방·대응 / 재해복구 | 앞서 다룬 **RBAC·Bcrypt·NGFW·SIEM·백업체계** 등 12개 세부 분야의 기술·관리 통제 |
| **③개인정보 처리단계별 요구사항** | 개인정보 수집 시 보호조치 / 개인정보 보유·이용 시 보호조치 / 개인정보 제공 시 보호조치 / 개인정보 파기 시 보호조치 / 정보주체 권리보호                                            | 앞서 다룬 **개인정보 안전성 확보조치 기준**의 관리체계 인증 버전                     |

***

#### Ⅲ. 인증 체계 및 적용 체계

**가. ISMS vs ISMS-P 비교**

| 비교 항목            | ISMS(정보보호)         | ISMS-P(정보보호+개인정보보호)       |
| :--------------- | :----------------- | :------------------------ |
| **인증기준 수**       | 80개(①+②)           | **101개(①+②+③)**           |
| **적용 대상**        | 정보보안 전반 관리 필요 기업   | 개인정보를 대량·핵심적으로 처리하는 기업    |
| **법적 의무 여부**     | 일정 매출·이용자 규모 이상 의무 | 자율 신청(확장 형태)              |
| **개인정보 생애주기 통제** | 미포함 🚨             | **수집→이용→제공→파기 전 단계 포함** ✅ |
| **정보주체 권리보호**    | 미포함                | **열람·정정·삭제권 대응 절차 포함** ✅  |

**나. ISMS-P vs ISO/IEC 27701 비교**

| 비교 항목       | ISMS-P                    | ISO/IEC 27701                      |
| :---------- | :------------------------ | :--------------------------------- |
| **인증 성격**   | **국내 법정 인증**              | 국제 자율 인증(27001 확장)                 |
| **인증기준 구조** | 3대 영역·101개 항목(독자 체계)      | 27001 Annex A + 별도 부속서             |
| **법적 근거**   | 정보통신망법·개인정보보호법            | 법률 아님(표준)                          |
| **역할 구분**   | 명시적 역할 구분 없음              | **PII Controller/Processor 명확 구분** |
| **글로벌 통용성** | 국내 중심 🚨                  | **전 세계 상호운용** ✅                    |
| **동시 취득**   | 앞서 다룬 것처럼 통합 심사로 비용 절감 가능 | ISMS-P 기반 위에 27701 갭 분석 추가         |

**다. 인증 절차**

| 단계         | 내용                                              |
| :--------- | :---------------------------------------------- |
| **①신청·계약** | 한국인터넷진흥원(KISA) 또는 지정 심사기관에 신청                   |
| **②사전 준비** | 관리체계 수립·정책 문서화·기술적 통제 구현(최소 2개월 이상 실제 운영 이력 필요) |
| **③인증 심사** | 서면 심사 + 현장 심사(관리체계 운영 증적 확인)                    |
| **④인증 유지** | 인증 유효기간 3년, 매년 **사후 심사** 수행                     |
| **⑤갱신**    | 3년 주기로 갱신 심사(최초 심사 수준으로 재검증)                    |

**라. 실무 적용 시 핵심 고려사항**

| 고려사항            | 내용                                                             |
| :-------------- | :------------------------------------------------------------- |
| **최소 운영기간 요건**  | 관리체계를 수립만 해서는 안 되며 일정 기간 실제 운영한 증적(로그·회의록 등) 필요                |
| **경영진 참여 증적**   | 정보보호 최고책임자(CISO) 지정, 경영진 보고 체계가 형식이 아닌 실질적으로 작동해야 함            |
| **위험평가 연계**     | 앞서 다룬 **AI 레드티밍**처럼 정기적 취약점 점검 결과가 위험평가 항목의 근거 자료로 활용          |
| **개인정보 흐름표 작성** | 앞서 다룬 **데이터 계보(Lineage)** 개념처럼 개인정보 처리 현황을 전사적으로 매핑해야 심사 대응 가능 |

***

**(제언)** "ISMS-P의 3대 영역 구조가 보여주는 핵심 통찰은 '관리체계(①)라는 지속 가능한 운영 사이클 위에 기술적 보호대책(②)을 얹고, 개인정보를 다루는 조직이라면 그 위에 생애주기별 통제(③)까지 확장한다'는 계층적 설계로, 단순히 한 번의 기술 점검이 아니라 조직이 지속적으로 위험을 평가하고 개선하는 PDCA 문화를 갖췄는지를 증명하는 데 방점이 있다는 점입니다. 실무에서는 이미 ISMS-P를 보유한 조직이 해외 진출이나 글로벌 고객사 대응을 앞두고 있다면 상당 부분 중복되는 ISO/IEC 27701을 통합 심사로 추가 취득해 비용 효율을 높이는 것이 합리적이며, 특히 앞서 다룬 개인정보 안전성 확보조치 기준의 유형별(1\~3) 의무가 개별 기술 통제를 규정한다면 ISMS-P는 그 통제들이 실제로 조직 전체에서 일관되게 작동하는지를 제3자가 정기적으로 검증하는 상위 거버넌스 장치라는 점에서 두 제도를 상호 보완적으로 이해하고 준비하는 것이 핵심 전략입니다.

***

**앞서 다룬 개념과의 연결**

### **I. 대한민국 대표 종합 보안 표준, ISMS-P의 개요**

과거 정보보호 관리체계(ISMS)와 개인정보보호 관리체계(PIMS)가 이원화되어 발생하던 기업의 수검 오버헤드와 관리 사각지대를 해소하기 위해 두 제도를 하나로 통합했습니다. **ISMS-P 인증**은 기업이 주요 정보 자산과 고객의 개인정보를 안전하게 보호하기 위해 수립·운영하는 관리체계가 국가 통합 기준에 적합한지 심사하는 제도로, **총 102개의 통제 항목을 3대 영역으로 체계화**하여 운영하고 있습니다.

***

### **II. ISMS-P 3대 인증 영역 및 세부 통제항목 구성**

| **🔑 3대 인증 영역 🚨**              | **🏁 세부 통제 세부 항목 (총 102개) 💯**                                                                      | **주요 심사 및 이행 포인트**                                            |
| :------------------------------ | :-------------------------------------------------------------------------------------------------- | :------------------------------------------------------------ |
| **영역 1. 관리체계 수립 및 운영** (16개 항목) | 1.1 관리체계 기반 마련 (4개) 1.2 위험 관리 (6개) 1.3 관리체계 운영 (3개) 1.4 관리체계 점검 및 개선 (3개)                           | 최고경영자(CISO/CPO) 지정, 정보자산 식별, 위험평가(Risk Assessment), 내부감사 및 보고 |
| **영역 2. 보호대책 요구사항** (64개 항목)    | 2.1 정책/조직/자산 관리, 2.2 인적보안 2.3 외부자보안, 2.4 물리보안 2.5 암호화, 2.6 접근통제 2.7 운영보안, 2.8 사고관리 2.9 자반/클라우드/개발보안 | 네트워크 망분리, 서버/DB 접근제어, 개인정보 DB 암호화, 개발 보안(시큐어 코딩), 백업          |
| **영역 3. 개인정보 처리단계별** (22개 항목)   | 3.1 수집 시 보호조치 (5개) 3.2 보유 및 이용 시 보호조치 (6개) 3.3 제공 시 보호조치 (5개) 3.4 파기 시 보호조치 (3개) 3.5 정보주체 권리보장 (3개) | 최소 수집 필수 동의, 제3자 제공 및 위탁 관리, 복구 불가능한 파기, 열람/정정/삭제 처리          |

***

### **III. 기존 ISMS(정보보안) 단독 인증과 통합 ISMS-P 인증의 비교**

| **비교 항목**    | **🛡️ 기존 ISMS (정보보안 단독)**  | **🔒 통합 ISMS-P (보안 + 개인정보)**          |
| :----------- | :------------------------- | :------------------------------------ |
| **법적 근거**    | 정보통신망법 제47조                | 정보통신망법 제47조 + 개인정보보호법 제32조의2          |
| **통제 항목 수**  | **총 80개 항목 (영역 1, 2만 적용)** | **총 102개 항목 (영역 1, 2 + 영역 3 전체 적용)**  |
| **주요 심사 자산** | 기업의 IT 인프라, 서버, 네트워크 자산    | IT 인프라 + **고객/임직원 개인정보(PII) 생명주기 전체** |
| **관할 주무 부처** | 과학기술정보통신부, KISA            | **과학기술정보통신부 + 개인정보보호위원회**, KISA       |
| **인증 가치**    | 일반 정보시스템 기술적 보안성 입증        | **대국민 개인정보 서비스 법적 컴플라이언스 완전 입증**      |

***

### **IV. ISMS-P 수검 및 운용 시 엔지니어링 이행 가이드라인**

**IMPORTANT**

1. **증적(Evidence) 관리의 상시 자동화**: 인증 심사 시 가장 흔히 지적되는 결함은 '정책 수립 대비 이행 증적 유실'입니다. 접근제어 승인 이력, 데이터 파기 확인서, 암호화 키 관리 일지 등을 시스템 로그 및 전자 결재와 연동하여 자동으로 증적 트레일(Audit Trail)이 남도록 구축해야 합니다.
2. **개인정보 처리 시스템(영역 3)과 개발보안(영역 2)의 교차 검증**: 개인정보 수집/제공 동의 화면 구현 시, 프론트엔드 입력값 검증과 백엔드 파기 스케줄러가 법적 보존 기간(예: 3년/5년) 종료 즉시 DB 및 백업본에서 완전 삭제되는지 기술적 정합성을 확인해야 합니다.
