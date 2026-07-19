### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (WBS 정의·목적) — 3~4줄
Ⅱ. WBS 작성원칙 (본론①, 도식 1개)
Ⅲ. 일정지연 발생 시 만회대책 (본론②, 도식 1개)
Ⅳ. 결론
```

### Ⅱ. WBS 작성원칙 — "100·상·인·적·코"

| 원칙                                | 핵심                                                          |
| :-------------------------------- | :---------------------------------------------------------- |
| **100% Rule**                     | 상위 요소는 하위요소의 총합과 정확히 일치(초과·부족 없이) — **가장 자주 출제되는 원칙 1번**    |
| **상호배타성(MECE)**                   | 하위요소 간 중복·누락 없어야 함                                          |
| **인도물 중심** (Deliverable-oriented) | 활동(동사)이 아니라 **결과물(명사)** 기준으로 분해 — "설계한다"(X) → "설계서"(O)      |
| **적절한 분해수준**                      | 8/80 Rule — 최하위 작업패키지는 8시간\~80시간 사이가 적절 (너무 세분화/너무 큰 단위 지양) |
| **코드화/식별체계**                      | 각 요소에 고유번호(WBS Code) 부여 → 관리·추적 용이                          |

→ 암기 문장: **"100% 채우고, 중복없이 나누고, 결과물 중심으로, 8\~80시간 크기로, 번호 붙인다"** — 이 한 줄이 5원칙을 다 담고 있습니다.

**도식 (계층분해 구조):**

```
        [프로젝트]  ← 100%
      ┌────┼────┐
   [단계1] [단계2] [단계3]  ← 합=100%
      ┌──┼──┐
  [작업A][작업B]  ← 8~80시간 단위 (작업패키지)
```

### Ⅲ. 지연 시 만회대책 — "크·패·조·재" (일정단축 4대 기법)

여기가 실무형 문제에서 배점이 큰 부분입니다. 원리 → 기법 순서로 짜면 이해도가 보입니다.

**원리: 지연 회복 = ① 자원을 더 투입하거나(비용↑) ② 순서를 바꿔서 겹치거나(위험↑) 두 가지 축**

| 기법                       | 방법                                          | Trade-off                     |
| :----------------------- | :------------------------------------------ | :---------------------------- |
| **Crashing (일정압축)**      | 핵심경로(Critical Path) 작업에 **자원(인력/장비) 추가 투입** | 비용 증가, 최소비용으로 최대단축 조합 선택      |
| **Fast-Tracking (공정중첩)** | 순차적 작업을 **병행/중첩 수행**                        | 재작업 위험 증가 (예: 설계 끝나기 전 개발 착수) |
| **범위/품질 조정**             | 우선순위 낮은 요구사항 제거·연기 (Scope 조정)               | 고객 요구 충족도 하락                  |
| **재기준선 (Re-baseline)**   | 불가피한 지연을 인정, 일정 재수립 + 원인 재발방지               | 최후수단, 신뢰도 이슈                  |

→ 암기: **"돈으로 밀거나(Crashing), 겹쳐서 당기거나(Fast-track), 범위를 줄이거나(Scope), 인정하고 다시 짜거나(Re-baseline)"** — 4개를 비용↔위험 스펙트럼 순서로 나열하면 자동으로 순서가 외워집니다.

**도식 (Trade-off 스펙트럼):**

```
[Crashing]────[Fast-Tracking]────[범위조정]────[Re-baseline]
 비용↑ 중심                                    최후수단
        ↕ 공통: 반드시 Critical Path(주경로) 작업 대상으로 우선 적용
```

→ 여기서 핵심 포인트 한 줄: 만회대책은 **아무 작업에나 적용하는 게 아니라 반드시 Critical Path(주경로) 상의 작업**에 적용해야 실제 전체 일정이 단축된다는 점 — 이걸 안 쓰면 "CPM(Critical Path Method) 이해가 없다"는 인상을 줍니다.

### Ⅳ. 결론 포인트 (차별화 한 줄)

지연은 사후 대응보다 \*\*조기경보(Earned Value Management, SPI/CPI 모니터링)\*\*로 미리 감지하는 것이 우선이며, 만회대책은 근본원인 분석(원인이 자원부족인지 리스크발생인지) 후 적합한 기법을 선택해야 한다는 논리로 마무리하면 좋습니다.

#### **I. \[도입] 프로젝트 성공의 뼈대, WBS 개요**

* **정의:** 프로젝트의 최종 목표를 달성하기 위해 필요한 모든 작업과 산출물을 계층적(Tree 구조)으로 세분화한 작업 분할 구조도.
* **목적:** 정확한 일정/원가 산정의 기준선(Baseline) 제공, 이해관계자 간의 의사소통 도구, 업무 할당(Work Package) 명확화.

#### **II. \[본론 1] 성공적인 WBS 작성을 위한 4대 절대 원칙**

WBS 원칙 문제는 아래 4가지 키워드만 들어가면 무조건 만점을 받습니다.

| **원칙 명칭**                  | **핵심 메커니즘 및 상세 설명**                                                                          | **목적 / 기대효과**                       |
| :------------------------- | :------------------------------------------------------------------------------------------- | :---------------------------------- |
| **100% Rule** (100% 규칙)    | - 하위 계층 작업들의 합은 상위 계층 작업과 **100% 일치**해야 함 - WBS에 없는 작업은 프로젝트 범위에 속하지 않음                      | 작업의 누락 방지 및 불필요한 작업(Scope Creep) 차단 |
| **8/80 Rule** (8/80 시간 규칙) | - 최하위 단위인 워크 패키지(Work Package)는 **최소 8시간 이상, 최대 80시간 이하**의 크기로 분할                            | 과도한 쪼개기 방지 및 관리 가능한 통제 단위 설정        |
| **MECE** (상호 배타성)          | - 각 작업 패키지들은 서로 중복되지 않고(**Mutually Exclusive**), 합치면 전체를 포괄(**Collectively Exhaustive**)해야 함 | 업무 중복 및 책임 소재 불명확성 해소               |
| **산출물 중심** (Deliverable)   | - '행동(Act)' 중심이 아닌 눈에 보이는 **'결과물(산출물)'** 중심으로 계층 구조 작성                                       | 명확한 진도 측정 및 품질 검증 기준 제공             |

#### **III. \[본론 2] 프로젝트 일정 지연 시 만회 대책 (일정 단축 기법)**

지연 만회 대책은 무조건 **'주공정(Critical Path)'** 상의 작업을 대상으로 한다는 점을 전제해야 합니다.

**1) 지연 만회 대책(Crashing vs Fast Tracking) 개념도** 답안지에 아래와 같은 블록 다이어그램을 그려 직관적인 이해를 돕습니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MTkuNTE3IDU0Mi4zMDAwMDAwMDAwMDAxIiB3aWR0aD0iNDE5LjUxNyIgaGVpZ2h0PSI1NDIuMzAwMDAwMDAwMDAwMSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMV9fX18iIGRhdGEtbGFiZWw9IjEuIOygleyDgSDsnbzsoJUgKOyInOywqOyggSDsiJjtlokpIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIyNDUuNDA5OTk5OTk5OTk5OTciIGhlaWdodD0iOTYuOSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjI0NS40MDk5OTk5OTk5OTk5NyIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjEuIOygleyDgSDsnbzsoJUgKOyInOywqOyggSDsiJjtlokpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMl9DcmFzaGluZ19fX19fIiBkYXRhLWxhYmVsPSIyLiBDcmFzaGluZyAo6rO17KCVIOyVley2lSA6IOyekOybkCDstpTqsIApIj4KICA8cmVjdCB4PSI0MCIgeT0iMTY0LjkwMDAwMDAwMDAwMDAzIiB3aWR0aD0iMzM5LjUxNyIgaGVpZ2h0PSIxMTMuODAwMDAwMDAwMDAwMDEiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iMTY0LjkwMDAwMDAwMDAwMDAzIiB3aWR0aD0iMzM5LjUxNyIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjE3OC45MDAwMDAwMDAwMDAwMyIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij4yLiBDcmFzaGluZyAo6rO17KCVIOyVley2lSA6IOyekOybkCDstpTqsIApPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iM19GYXN0X1RyYWNraW5nX19fX18iIGRhdGEtbGFiZWw9IjMuIEZhc3QgVHJhY2tpbmcgKOqzteyglSDspJHssqkgOiDrs5Htlokg7IiY7ZaJKSI+CiAgPHJlY3QgeD0iNDAiIHk9IjMwNi43MDAwMDAwMDAwMDAwNSIgd2lkdGg9IjEzNS40NTMiIGhlaWdodD0iMTk1LjYwMDAwMDAwMDAwMDAyIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjMwNi43MDAwMDAwMDAwMDAwNSIgd2lkdGg9IjEzNS40NTMiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSIzMjAuNzAwMDAwMDAwMDAwMDUiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+My4gRmFzdCBUcmFja2luZyAo6rO17KCVIOykkeyyqSA6IOuzke2WiSDsiJjtlokpPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBIiBkYXRhLXRvPSJCIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE0MC4xODY5OTk5OTk5OTk5OCwxMDIuNDUgMTg2LjcwNDk5OTk5OTk5OTk4LDEwMi40NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQTIiIGRhdGEtdG89IkIyIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjIwMy45MTI5OTk5OTk5OTk5OCwyMzUuODAwMDAwMDAwMDAwMDQgMjUwLjQzMDk5OTk5OTk5OTk4LDIzNS44MDAwMDAwMDAwMDAwNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQSIgZGF0YS1sYWJlbD0i7J6R7JeFIEEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTcuNDgyIiB5PSI4NCIgd2lkdGg9IjgyLjcwNSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9Ijk4LjgzNDQ5OTk5OTk5OTk5IiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyekeyXhSBBPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJCIiBkYXRhLWxhYmVsPSLsnpHsl4UgQiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxODYuNzA0OTk5OTk5OTk5OTgiIHk9Ijg0IiB3aWR0aD0iODIuNzA1IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjI4LjA1NzQ5OTk5OTk5OTk4IiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyekeyXhSBCPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBMiIgZGF0YS1sYWJlbD0i7J6R7JeFIEEKKyDstpTqsIAg7J2466ClL+yVvOq3vCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1Ny40ODIiIHk9IjIwOC45MDAwMDAwMDAwMDAwMyIgd2lkdGg9IjE0Ni40MzA5OTk5OTk5OTk5OCIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZTBiMiIgc3Ryb2tlPSIjZWY2YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxMzAuNjk3NSIgeT0iMjM1LjgwMDAwMDAwMDAwMDA0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxMzAuNjk3NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuyekeyXhSBBPC90c3Bhbj48dHNwYW4geD0iMTMwLjY5NzUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPisg7LaU6rCAIOyduOugpS/slbzqt7w8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQjIiIGRhdGEtbGFiZWw9IuyekeyXhSBCCisg7LaU6rCAIOyekOybkCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyNTAuNDMwOTk5OTk5OTk5OTgiIHk9IjIwOC45MDAwMDAwMDAwMDAwMyIgd2lkdGg9IjExMy4wODYiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmUwYjIiIHN0cm9rZT0iI2VmNmMwMCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMzA2Ljk3NCIgeT0iMjM1LjgwMDAwMDAwMDAwMDA0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIzMDYuOTc0IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7J6R7JeFIEI8L3RzcGFuPjx0c3BhbiB4PSIzMDYuOTc0IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj4rIOy2lOqwgCDsnpDsm5A8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQTMiIGRhdGEtbGFiZWw9IuyekeyXhSBBCuyImO2WiSDspJEuLi4iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTcuNDgyIiB5PSIzNTAuNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSI5Ny41MjUiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWJlZTciIHN0cm9rZT0iI2MyMTg1YiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTA2LjI0NDUiIHk9IjM3Ny42IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxMDYuMjQ0NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuyekeyXhSBBPC90c3Bhbj48dHNwYW4geD0iMTA2LjI0NDUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyImO2WiSDspJEuLi48L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQjMiIGRhdGEtbGFiZWw9IuyekeyXhSBCCuyhsOq4sCDssKnsiJgiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTcuNDgyIiB5PSI0MzIuNTAwMDAwMDAwMDAwMDYiIHdpZHRoPSIxMDMuNDUzIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFiZWU3IiBzdHJva2U9IiNjMjE4NWIiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjEwOS4yMDg1IiB5PSI0NTkuNDAwMDAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjEwOS4yMDg1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7J6R7JeFIEI8L3RzcGFuPjx0c3BhbiB4PSIxMDkuMjA4NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7KGw6riwIOywqeyImDwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

**2) 만회 대책 상세 비교표**

| **구분**              | **Crashing (공정 압축)**                     | **Fast Tracking (공정 중첩)**                 |
| :------------------ | :--------------------------------------- | :---------------------------------------- |
| **개념**              | **비용(자원)을 추가로 투입**하여 주공정의 소요 기간을 단축하는 기법 | 원래 순차적으로 해야 할 작업을 **동시에 겹쳐서(병행)** 수행하는 기법 |
| **적용 방법**           | 야근, 주말 특근 실시, 외부 전문 인력 추가 투입, 고성능 장비 대여  | 설계가 완전히 끝나기 전에 개발을 조기 착수 (선후 관계 완화)       |
| **Trade-off (부작용)** | 💰 **프로젝트 원가(비용) 급증**                    | 💣 **재작업 리스크 및 품질 저하 위험 급증**              |
| **적용 시점**           | 자원/예산에 여유가 있을 때                          | 비용 추가는 불가하고 일정 단축만 필요할 때                  |

#### **IV. \[결론/제언] 성공적인 일정 단축을 위한 PM의 역할**

* "일정 단축 기법(Crashing/Fast Tracking)은 필연적으로 **비용 증가 또는 품질 저하의 리스크**를 동반합니다. 따라서 지연이 발생하기 전 철저한 WBS 관리가 우선되어야 하며, 부득이 단축 기법을 쓸 경우 \*\*통합변경통제위원회(CCB)\*\*를 통한 공론화와 이해관계자 간의 투명한 의사소통, 그리고 품질을 사수하는 PM의 리더십이 프로젝트 성패를 결정짓습니다."
