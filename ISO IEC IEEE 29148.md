#### **요구공학 국제 표준: ISO/IEC/IEEE 29148**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 요구사항 작성에도 국제 표준이 필요한가)
Ⅱ. 29148 핵심 구조
Ⅲ. 요구사항 품질 특성 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 Shift-Left 테스팅이 '결함을 최대한 초기 단계에서 잡는다'는 철학이었다면, ISO/IEC/IEEE 29148은 그 초기 단계에서도 가장 왼쪽 끝 — 요구사항 자체가 처음부터 모호하거나 검증 불가능하게 작성되면 아무리 뒤에서 테스트를 강화해도 근본적으로 잘못된 시스템을 만들게 된다는 문제의식에서 출발한 요구공학(Requirements Engineering) 국제 표준이다 — ISO/IEC/IEEE 15288(시스템 생명주기)과 12207(소프트웨어 생명주기) 표준의 요구사항 프로세스를 구체화한 이 표준은 이해관계자 요구사항(StRS)·시스템 요구사항(SyRS)·소프트웨어 요구사항(SRS) 3단계 문서 체계와 좋은 요구사항이 갖춰야 할 특성(완전성·검증가능성·명확성 등)을 정형화해, 앞서 다룬 SAFe의 PI Planning에서 다루는 기능 요구사항이나 앞서 다룬 데이터 계약의 스키마 요구사항까지 모든 요구사항 산출물이 참조하는 근본 표준"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.
![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMjUuNzI0OTk5OTk5OTk5OTcgMzcxLjYiIHdpZHRoPSIzMjUuNzI0OTk5OTk5OTk5OTciIGhlaWdodD0iMzcxLjYiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQ29uT3BzIiBkYXRhLXRvPSJTdFJTIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE2Mi44NjI0OTk5OTk5OTk5OCw3Ni45IDE2Mi44NjI0OTk5OTk5OTk5OCwxMjQuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iU3RSUyIgZGF0YS10bz0iU3lSUyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxNjIuODYyNDk5OTk5OTk5OTgsMTYxLjggMTYyLjg2MjQ5OTk5OTk5OTk4LDIwOS44IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTeVJTIiBkYXRhLXRvPSJTUlMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTYyLjg2MjQ5OTk5OTk5OTk4LDI0Ni43MDAwMDAwMDAwMDAwMiAxNjIuODYyNDk5OTk5OTk5OTgsMjk0LjcwMDAwMDAwMDAwMDA1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDb25PcHMiIGRhdGEtbGFiZWw9IkNvbk9wcyAvIE9wc0NvbiA6IOyatOyYgSDqsJzrhZAg7KCV66a9IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjI0NS43MjQ5OTk5OTk5OTk5NyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE2Mi44NjI0OTk5OTk5OTk5OCIgeT0iNTguNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkNvbk9wcyAvIE9wc0NvbiA6IOyatOyYgSDqsJzrhZAg7KCV66a9PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTdFJTIiBkYXRhLWxhYmVsPSIxLiDsnbTtlbTqtIDqs4TsnpAg7JqU6rWs66qF7IS4IFN0UlMiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTQuMDc5MDAwMDAwMDAwMDEiIHk9IjEyNC45IiB3aWR0aD0iMjE3LjU2Njk5OTk5OTk5OTk1IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNjIuODYyNDk5OTk5OTk5OTgiIHk9IjE0My4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+MS4g7J207ZW06rSA6rOE7J6QIOyalOq1rOuqheyEuCBTdFJTPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTeVJTIiBkYXRhLWxhYmVsPSIyLiDsi5zsiqTthZwg7JqU6rWs66qF7IS4IFN5UlMiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNjQuNDUzIiB5PSIyMDkuOCIgd2lkdGg9IjE5Ni44MTg5OTk5OTk5OTk5NiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE2Mi44NjI0OTk5OTk5OTk5OCIgeT0iMjI4LjI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij4yLiDsi5zsiqTthZwg7JqU6rWs66qF7IS4IFN5UlM8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlNSUyIgZGF0YS1sYWJlbD0iMy4g7IaM7ZSE7Yq47Juo7Ja0IOyalOq1rOuqheyEuCBTUlMiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTMuMzM3OTk5OTk5OTk5OTk0IiB5PSIyOTQuNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSIyMTkuMDQ4OTk5OTk5OTk5OTgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTYyLjg2MjQ5OTk5OTk5OTk4IiB5PSIzMTMuMTUwMDAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjMuIOyGjO2UhO2KuOybqOyWtCDsmpTqtazrqoXshLggU1JTPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

***

#### Ⅱ. 29148 핵심 구조

**가. 3단계 요구사항 문서 체계**

```
[요구사항 문서 계층 구조]

①StRS (Stakeholder Requirements Specification)
  이해관계자 요구사항 명세서
  "사용자·고객이 무엇을 원하는가"(비즈니스 관점)
       ↓ 정제·구체화
②SyRS (System Requirements Specification)
  시스템 요구사항 명세서
  "시스템이 무엇을 해야 하는가"(시스템 경계·기능)
       ↓ 소프트웨어 영역 분해
③SRS (Software Requirements Specification)
  소프트웨어 요구사항 명세서
  "소프트웨어가 구체적으로 어떻게 동작해야 하는가"
  (앞서 다룬 TDD·BDD 시나리오 작성의 직접 입력)

→ 상위 문서의 각 요구사항은 하위 문서로 추적 가능해야 함
  (양방향 추적성, Traceability)
```

**나. 요구사항 프로세스 3대 활동**

| 활동                         | 내용                            |
| :------------------------- | :---------------------------- |
| **요구사항 도출(Elicitation)**   | 인터뷰·워크숍·관찰을 통해 이해관계자 니즈 수집    |
| **요구사항 분석(Analysis)**      | 수집된 요구를 명확화·우선순위화·충돌 해소       |
| **요구사항 명세(Specification)** | 표준 템플릿에 따라 문서화(StRS/SyRS/SRS) |
| **요구사항 검증(Validation)**    | "올바른 시스템을 만들고 있는가" 이해관계자와 재확인 |

***

#### Ⅲ. 요구사항 품질 특성 및 적용 체계

**가. 좋은 요구사항의 핵심 품질 특성**

| 품질 특성                 | 정의                    | 나쁜 예 vs 좋은 예                     |
| :-------------------- | :-------------------- | :------------------------------- |
| **필요성(Necessary)**    | 시스템에 실제로 필요한 요구인가     | 불필요한 "있으면 좋은" 항목 배제              |
| **명확성(Unambiguous)**  | 하나의 해석만 가능해야 함        | "빠르게 응답한다" ✗ → "3초 이내 응답한다" ✓    |
| **완전성(Complete)**     | 필요한 모든 정보가 포함되어야 함    | 예외 상황·경계 조건 누락 없이 기술             |
| **일관성(Consistent)**   | 다른 요구사항과 모순되지 않아야 함   | 상충되는 요구 사전 식별·조정                 |
| **검증가능성(Verifiable)** | 테스트로 충족 여부를 확인 가능해야 함 | "사용하기 편해야 한다" ✗ → 측정 가능한 기준 명시 ✓ |
| **추적가능성(Traceable)**  | 상위/하위 요구사항과 연결 관계 유지  | StRS→SyRS→SRS 추적 매트릭스            |
| **실현가능성(Feasible)**   | 기술적·예산적으로 구현 가능해야 함   | 현재 기술 수준에서 달성 불가능한 요구 배제         |

**나. 기능 요구사항 vs 비기능 요구사항 구조화**

| 구분                   | 내용                 | 예시                                   |
| :------------------- | :----------------- | :----------------------------------- |
| **기능 요구사항(FR)**      | 시스템이 수행해야 할 기능     | "사용자는 비밀번호를 재설정할 수 있어야 한다"           |
| **비기능 요구사항(NFR)**    | 품질 속성(성능·보안·가용성 등) | 앞서 다룬 **ISO/IEC 25010** 품질 특성과 직접 연계 |
| **제약사항(Constraint)** | 설계·구현의 제한 조건       | "온프레미스 환경에서만 운영 가능해야 한다"             |

**다. 전통 개발 vs 애자일 환경에서의 29148 적용 비교**

| 비교 항목                | 전통 폭포수(Waterfall) | 애자일(Agile/SAFe)                              |
| :------------------- | :---------------- | :------------------------------------------- |
| **문서화 시점**           | 프로젝트 초기 일괄 확정     | 점진적·반복적 구체화(User Story)                      |
| **StRS/SyRS/SRS 형태** | 별도 정식 문서로 완결      | Epic→Feature→Story 계층으로 경량화                  |
| **변경 관리**            | 엄격한 변경통제위원회(CCB)  | 앞서 다룬 **SAFe PI Planning**에서 반복적 재우선순위화      |
| **검증가능성 확보 방식**      | 별도 테스트 계획서        | 앞서 다룬 **BDD Given-When-Then**으로 요구사항=테스트 케이스 |
| **29148 적용 방식**      | 표준 템플릿 그대로 적용     | 품질 특성(명확성·검증가능성)만 정신을 계승해 경량 적용              |

**라. 요구사항 관리 도구 및 실무 연계**

| 활용 영역                 | 연계 방식                                            |
| :-------------------- | :----------------------------------------------- |
| **요구사항 추적 매트릭스(RTM)** | StRS→SyRS→SRS→테스트케이스 간 매핑표로 누락·불일치 방지            |
| **요구사항 관리 도구**        | Jira·Azure DevOps·DOORS로 요구사항-작업-테스트 연결          |
| **정보시스템 감리**          | 앞서 다룬 **감리** 시 요구사항 정의서의 29148 품질 특성 충족 여부 점검 항목 |
| **계약 기반 개발(SI)**      | 과업내용서·제안요청서(RFP) 작성 시 29148 구조를 준용해 분쟁 소지 최소화    |

***

**(제언)** "ISO/IEC/IEEE 29148의 핵심 가치는 화려한 신기술이 아니라 '무엇을 만들 것인가'에 대한 합의를 문서로 남기는 가장 기초적이면서도 가장 자주 소홀히 다뤄지는 단계를 표준화했다는 점이며, 실제 프로젝트 실패 사례의 상당수가 기술 부족이 아니라 요구사항의 모호함과 이해관계자 간 불일치에서 비롯된다는 점을 감안하면 그 실무적 가치가 큽니다. 다만 전통적인 3단계 문서 체계를 애자일 프로젝트에 그대로 무겁게 적용하면 오히려 민첩성을 해칠 수 있으므로, 앞서 다룬 SAFe나 BDD 환경에서는 정식 StRS/SyRS/SRS 문서 대신 Epic-Feature-Story 계층과 Given-When-Then 시나리오에 명확성·검증가능성·추적가능성이라는 29148의 핵심 품질 특성만 정신적으로 계승해 경량화하여 적용하는 것이 현대 개발 환경에서의 현실적인 활용 전략입니다.

***

**앞서 다룬 개념과의 연결**

| 연계 개념              | 연결 내용                                            |
| :----------------- | :----------------------------------------------- |
| **Shift-Left 테스팅** | 29148의 요구사항 검증 단계가 Shift-Left의 가장 초기 실천 지점       |
| **SAFe**           | PI Planning의 Feature·Story가 SyRS/SRS의 애자일 경량화 버전 |
| **BDD·TDD**        | 검증가능성 특성이 Given-When-Then 시나리오·테스트 코드로 직결        |
| **ISO/IEC 25010**  | 비기능 요구사항 작성 시 품질 특성 체계를 그대로 참조                   |
| **정보시스템 감리·CMMI**  | 요구사항 관리 프로세스 성숙도가 감리·CMMI 평가의 핵심 심사 항목           |

### **I. 차세대 시스템 및 SW 요구공학 표준, ISO/IEC/IEEE 29148의 개요**

과거 소프트웨어 단독 요구명세 표준이었던 IEEE Std 830은 복잡한 융합 시스템 환경에서 이해관계자의 사업적 니즈와 시스템(HW/SW) 전체 생명주기 간의 요구사항 추적성을 보장하지 못했습니다. **ISO/IEC/IEEE 29148**은 기존 표준들(IEEE 830, IEEE 1233, IEEE 1362 등)을 전면 대체 통합하여, **이해관계자 요구명세서(StRS) ➔ 시스템 요구명세서(SyRS) ➔ 소프트웨어 요구명세서(SRS)로 이어지는 위계 구조와 표준 요구공학 프로세스**를 확립한 글로벌 국제 표준입니다.

***

### **II. ISO/IEC/IEEE 29148의 요구공학 5대 프로세스 및 산출물 위계**

#### **1. 요구공학 5대 표준 프로세스**

* **도출 (Elicitation)**: 이해관계자 식별, 요구사항 도출 및 인터뷰 수행
* **분석 (Analysis)**: 상충되는 요구사항의 중재, 범위 정의 및 모델링
* **명세 (Specification)**: 표준 템플릿에 따라 정형화된 서식 형태로 산출물 작성
* **검증 및 승인 (Verification & Validation)**: 요구사항의 검증 가능성 및 비즈니스 목적 부합성 판정
* **관리 (Management)**: 요구사항 베이스라인 수립, 변경통제위원회(CCB) 운영, 양방향 추적성(Traceability) 통제

#### **2. 요구명세서 산출물 위계 구조**

* **StRS (Stakeholder Requirements Specification)**: 고객, 사용자 등 이해관계자의 비즈니스 니즈 정의
* **SyRS (System Requirements Specification)**: 시스템 전체(하드웨어, 소프트웨어, 인원)의 기능/비기능 사양
* **SRS (Software Requirements Specification)**: 실제 소프트웨어 구성요소별 세부 개발 사양서

***

### **III. 기존 IEEE Std 830 표준과 신규 ISO/IEC/IEEE 29148 표준의 상세 비교**

| **비교 항목**      | **🏛️ 기존 IEEE Std 830 표준** | **🌐 신규 ISO/IEC/IEEE 29148 표준**                        |
| :------------- | :------------------------- | :----------------------------------------------------- |
| **통합 대치 표준**   | 단일 소프트웨어 명세서 가이드           | **IEEE 830, IEEE 1233(SyRS), IEEE 1362(ConOps) 대치 통합** |
| **적용 범위 및 대상** | 순수 소프트웨어(SW) 제품 명세 국한      | **시스템(HW+SW) 및 수명주기 전체(ISO 12207 연계)**                 |
| **명세서 산출물 체계** | 단일 소프트웨어 요구명세서 (SRS)       | **StRS ➔ SyRS ➔ SRS 단계적 계층 명세 구조**                     |
| **품질 검증 관점**   | 명세서 전체의 8대 품질 특성 중심        | **개별 요구사항 항목 품질과 명세서 전체 품질을 분리 검증**                    |

***

### **IV. ISO/IEC/IEEE 29148 기준 개별 요구사항 작성 품질 기준**

**IMPORTANT**

1. **개별 요구사항 항목의 8대 품질 속성 준수**: 개별 요구사항 구문 작성 시 Unambiguous(명확성), Complete(완전성), Consistent(일관성), Correct(정확성), Feasible(실현가능성), Traceable(추적가능성), Verifiable(검증가능성), Bounded(경계성)의 8가지 조건을 반드시 충족해야 합니다.
2. **양방향 추적성(Bi-directional Traceability) 강제**: StRS의 비즈니스 요구사항이 SyRS와 SRS를 거쳐 실제 개발 및 테스트 케이스까지 1:N으로 빠짐없이 매핑되는 RTM(요구사항 추적표)을 구성하여 누락을 차단해야 합니다.
