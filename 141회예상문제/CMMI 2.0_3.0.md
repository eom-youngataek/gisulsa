### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 프로세스 성숙도가 SW 품질의 기반인가)
Ⅱ. CMMI 핵심 구조 및 성숙도 레벨
Ⅲ. CMMI 2.0 vs 3.0 비교
Ⅳ. 결론
```

포인트: 개요에서 **"앞서 다룬 DevOps·DORA 지표가 '소프트웨어 전달 속도와 안정성을 측정'한다면, CMMI(Capability Maturity Model Integration)는 '조직의 소프트웨어 개발 프로세스가 얼마나 성숙했는가'를 5단계 레벨로 측정·개선하는 프로세스 역량 프레임워크다 — 앞서 다룬 ISO 25010이 SW 제품 품질을 평가한다면, CMMI는 그 제품을 만드는 조직의 프로세스 품질을 평가하며, 공공 SI 사업 입찰 자격·방위산업·금융 IT 계약의 필수 요건으로 실무 조달 현장에서 직접 활용되는 국제 표준 프로세스 인증"**이라는 한 줄로 시작하면 전체 맥락이 드러납니다.
\
![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MDIuNzc5OTk5OTk5OTk5OSAyODYuNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSI4MDIuNzc5OTk5OTk5OTk5OSIgaGVpZ2h0PSIyODYuNzAwMDAwMDAwMDAwMDUiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQ01NSTIiIGRhdGEtdG89IkV2b2x2ZSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzODUuMDg3OTk5OTk5OTk5OTcsNzYuOSAzODUuMDg3OTk5OTk5OTk5OTcsMTI0LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkV2b2x2ZSIgZGF0YS10bz0iRE0iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzg1LjA4Nzk5OTk5OTk5OTk3LDE2MS44IDM4NS4wODc5OTk5OTk5OTk5NywxODUuOCAxMzcuNjY4NSwxODUuOCAxMzcuNjY4NSwyMDkuOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRXZvbHZlIiBkYXRhLXRvPSJTRUMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzg1LjA4Nzk5OTk5OTk5OTk3LDE2MS44IDM4NS4wODc5OTk5OTk5OTk5NywxODUuOCAzODUuMDg3OTk5OTk5OTk5OTcsMTg1LjggMzg1LjA4Nzk5OTk5OTk5OTk3LDIwOS44IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJFdm9sdmUiIGRhdGEtdG89IlZJUlQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzg1LjA4Nzk5OTk5OTk5OTk3LDE2MS44IDM4NS4wODc5OTk5OTk5OTk5NywxODUuOCA2NDguODA5NSwxODUuOCA2NDguODA5NSwyMDkuOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ01NSTIiIGRhdGEtbGFiZWw9IkNNTUkgMi4wIDogNOqwnCDrj4TrqZTsnbggREVWLCBTVkMsIFNQTSwgTVBPIOq4sOuwmCDshLHriqUg7KSR7IusIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjE4Ni42NDM1MDAwMDAwMDAwMiIgeT0iNDAiIHdpZHRoPSIzOTYuODg4OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzg1LjA4Nzk5OTk5OTk5OTk3IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Q01NSSAyLjAgOiA06rCcIOuPhOuplOyduCBERVYsIFNWQywgU1BNLCBNUE8g6riw67CYIOyEseuKpSDspJHsi6w8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkV2b2x2ZSIgZGF0YS1sYWJlbD0iQ01NSSAzLjAg7ZmV7J6lIDogM+qwnCDsi6Dqt5wg64+E66mU7J24IOyYgeyXrSDsoITrqbQg7IiY7JqpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjIxOS4yNDc0OTk5OTk5OTk5NSIgeT0iMTI0LjkiIHdpZHRoPSIzMzEuNjgxMDAwMDAwMDAwMDQiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMzg1LjA4Nzk5OTk5OTk5OTk3IiB5PSIxNDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkNNTUkgMy4wIO2ZleyepSA6IDPqsJwg7Iug6recIOuPhOuplOyduCDsmIHsl60g7KCE66m0IOyImOyaqTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRE0iIGRhdGEtbGFiZWw9IjEuIOuNsOydtO2EsCDqtIDrpqwgRE0g64+E66mU7J24IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwIiB5PSIyMDkuOCIgd2lkdGg9IjE5NS4zMzY5OTk5OTk5OTk5NiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEzNy42Njg1IiB5PSIyMjguMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjEuIOuNsOydtO2EsCDqtIDrpqwgRE0g64+E66mU7J24PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTRUMiIGRhdGEtbGFiZWw9IjIuIOuztOyViCDrsI8g7JWI7KCEIFNFQyAvIFNBRiDrj4TrqZTsnbgiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjYzLjMzNyIgeT0iMjA5LjgiIHdpZHRoPSIyNDMuNTAxOTk5OTk5OTk5OTUiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzODUuMDg3OTk5OTk5OTk5OTciIHk9IjIyOC4yNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Mi4g67O07JWIIOuwjyDslYjsoIQgU0VDIC8gU0FGIOuPhOuplOyduDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iVklSVCIgZGF0YS1sYWJlbD0iMy4g7JuQ6rKpL+qwgOyDgSDsnpHsl4UgVklSVCDrj4TrqZTsnbgiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTM0LjgzODk5OTk5OTk5OTkiIHk9IjIwOS44IiB3aWR0aD0iMjI3Ljk0MDk5OTk5OTk5OTk1IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNjQ4LjgwOTUiIHk9IjIyOC4yNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+My4g7JuQ6rKpL+qwgOyDgSDsnpHsl4UgVklSVCDrj4TrqZTsnbg8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

***

#### Ⅱ. CMMI 핵심 구조 및 성숙도 레벨

**가. CMMI 성숙도 5단계**

| 레벨    | 명칭                              | 핵심 특징               | 키워드           |
| :---- | :------------------------------ | :------------------ | :------------ |
| **1** | 초기 (Initial)                    | 프로세스 없음·개인 역량 의존    | 혼돈·영웅주의·재현 불가 |
| **2** | 관리됨 (Managed)                   | 프로젝트 단위 계획·추적·통제    | 요구관리·일정·비용 관리 |
| **3** | 정의됨 (Defined)                   | 조직 표준 프로세스 수립·전사 적용 | 조직 표준·테일러링·교육 |
| **4** | 정량적 관리 (Quantitatively Managed) | 통계·데이터 기반 프로세스 통제   | SPC·측정·예측 가능성 |
| **5** | 최적화 (Optimizing)                | 지속적 개선·혁신·결함 예방     | 혁신·원인분석·최적화   |

→ 암기: **"초관정정최 — 초기·관리·정의·정량·최적화"**

***

**나. CMMI 2.0 핵심 구조**

| **핵심 척도**       | **📊 실천 영역(PA) 체계 🚨**                                                                                                                         | **🔑 역량 레벨(CL) 구조 🚨**                                                                                    | **🏁 성과 중심 평가 💯**                                                                                        |
| :-------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| **핵심 개념**       | **20개 실천 영역(PA)** 5개 범주로 구성 / 거버넌스(GOV)·실행(IMPL)·엔지니어링(ENG)·지원(SUP)·관리(MAN)                                                                    | **역량 레벨 0\~5**: 레벨별 프랙티스 그룹(PG) 달성 여부 평가 / 조직 전체 성숙도 = 모든 PA 역량 레벨 종합                                     | **비즈니스 성과(BO) 연계**: 프로세스 성숙도→비즈니스 가치 연결 명시 / 앞서 다룬 **IT-ROI·Val IT** 철학과 동일                               |
| **5대 범주**       | **거버넌스(GOV)**: 조직 전략·경영진 지원 / **실행(IMPL)**: 프로세스 실행 인프라 / **엔지니어링(ENG)**: 요구→설계→개발→검증 / **지원(SUP)**: 품질보증·형상관리·측정 / **관리(MAN)**: 프로젝트·작업 계획·위험 | **CL0**: 프랙티스 미수행 / **CL1**: 프랙티스 수행 / **CL2**: 계획·관리됨 / **CL3**: 정의됨·표준화 / **CL4**: 정량 관리 / **CL5**: 최적화 | **평가 방식**: CMMI Institute 공인 평가사(Lead Appraiser) 수행 / Benchmark Appraisal(인증)·Evaluation(내부) 구분 / 3년 유효기간 |
| **CMMI 1.3 대비** | 스테이징(Staged)·연속(Continuous) 표현 통합 / 단일 모델로 통합 / 애자일·DevOps 명시적 지원 추가                                                                           | 앞서 다룬 **DevOps·CI/CD** 실천을 CMMI 프랙티스로 인정 / 속도와 성숙도 동시 달성 가능                                               | **온라인 평가 플랫폼**: CMMI Cynosure로 증거 수집·평가 디지털화                                                              |

***

#### Ⅲ. CMMI 2.0 vs 3.0 비교

**가. CMMI 3.0 핵심 변화 (2023 출시)**

| 비교 항목     | CMMI 2.0        | CMMI 3.0                  |
| :-------- | :-------------- | :------------------------ |
| **출시**    | 2018년           | 2023년                     |
| **PA 수**  | 20개             | **24개** (4개 추가)           |
| **신규 영역** | -               | **사이버보안·AI·공급망·안전** 4개 추가 |
| **AI 연계** | 미반영             | **AI 개발 프로세스** 성숙도 평가 포함  |
| **사이버보안** | 별도 모델(CMMI-SVC) | **CMMI 본체 통합**            |
| **애자일**   | 명시적 지원          | **DevSecOps 완전 통합**       |
| **평가 방식** | Cynosure 플랫폼    | 강화된 디지털 증거 기반             |

***

**나. CMMI 3.0 신규 4개 실천 영역**

```
[CMMI 3.0 신규 추가 PA]

①사이버보안 (Cybersecurity·CYB)
  앞서 다룬 AI-SOC·제로트러스트·CSAP 연계
  SW 개발 전 생명주기에 보안 내재화

②AI 엔지니어링 (AI Engineering·AIE)
  앞서 다룬 MLOps·AIDLC 프로세스 성숙도
  AI 모델 개발·검증·운영 프로세스 표준화

③공급망 관리 (Supply Chain Management·SCM)
  앞서 다룬 SBOM·공급망 보안 연계
  외주·협력사 SW 품질 관리 체계

④안전 (Safety·SAF)
  기능안전(ISO 26262·IEC 61508) 연계
  자동차·항공·의료 SW 안전 프로세스
```

***

**다. 도식화**

```
[CMMI 성숙도 레벨 vs 조직 특성]

레벨5 최적화  ←  혁신·결함예방·지속개선
  │              측정 기반 자동 개선
레벨4 정량관리 ← SPC·통계적 프로세스 통제
  │              예측 가능한 품질
레벨3 정의됨  ←  조직 표준 프로세스
  │              전사 표준화·테일러링
레벨2 관리됨  ←  프로젝트 계획·추적
  │              기본 PM 프로세스
레벨1 초기    ←  개인 역량 의존
                 "영웅이 나타나야 성공"

[CMMI 3.0 = CMMI 2.0 + 4개 PA]
  기존 20 PA
  + 사이버보안(CYB)
  + AI 엔지니어링(AIE)
  + 공급망 관리(SCM)
  + 안전(SAF)
  = 24개 PA 통합 모델
```

***

**(제언)** "CMMI는 '좋은 SW는 좋은 프로세스에서 나온다'는 원칙의 국제 표준 구현체입니다. **CMMI 3.0이 사이버보안·AI 엔지니어링을 본체에 통합한 것은 앞서 다룬 DevSecOps·MLOps·AIDLC가 더 이상 선택이 아닌 필수 프로세스임을 국제 표준이 공인한 것이며, 국내 공공 SI 입찰 요건(레벨 3 이상)과 방위산업 계약 요건에 CMMI 3.0 기준이 순차 반영될 것으로 예상되므로, 조직의 애자일·DevSecOps 실천을 CMMI 프랙티스 증거로 체계화하는 것이 성숙도 향상의 핵심 전략입니다.**"
