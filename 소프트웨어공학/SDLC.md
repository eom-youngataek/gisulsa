### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (SDLC 정의, 모델선택의 중요성) — 3~4줄
Ⅱ. 공통 5단계 (본론①, 도식 1개 필수)
Ⅲ. 주요모델 비교 - 폭포수/애자일/나선형 (본론②, 핵심 배점)
Ⅳ. 모델선택기준
Ⅴ. 결론
```

포인트: 개요에서 \*\*"SDLC 자체는 '분석→설계→구현→테스트→유지보수'라는 공통뼈대이고, 각 방법론(폭포수/애자일/나선형)은 이 뼈대를 어떻게 반복·배치하느냐의 차이일 뿐"\*\*이라는 한 줄로 시작하면, 여러 모델을 별개로 외울 필요가 없다는 게 드러납니다.

### Ⅱ. 공통 5단계 — "요·설·구·시·유"

| 단계                      | 내용                  |
| :---------------------- | :------------------ |
| **요구분석** (Requirements) | 고객요구사항 수집·분석, 명세서작성 |
| **설계** (Design)         | 시스템구조, 데이터베이스, UI설계 |
| **구현** (Implementation) | 실제코딩                |
| **시험** (Testing)        | 단위/통합/시스템/인수테스트     |
| **유지보수** (Maintenance)  | 운영중 결함수정·개선         |

→ 암기: **"요구를 분석하고, 설계하고, 만들고, 검증하고, 계속 고친다"** — 이 5단계 자체는 어느 모델을 쓰든 반드시 등장합니다. 차이는 \*\*"이 5단계를 한번만 순서대로 도는가, 여러번 반복하는가, 위험을 관리하며 도는가"\*\*입니다.

### Ⅲ. 주요모델 비교 — "폭·애·나" (선형/반복/위험중심)

**함정 방지: 모델을 각각 설명만 하면 절반. "왜 이렇게 다르게 설계됐는가"의 근본철학차이를 보여줘야 완성됩니다.**

| 모델                    | 진행방식                                                     | 핵심철학                                                                              |
| :-------------------- | :------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| **폭포수모델** (Waterfall) | 5단계를 **순서대로 한번만**, 이전단계 완료해야 다음단계진입                      | **요구사항이 명확하고 안정적**일 때 유리 — 문서화철저, 단 **중간변경에 매우 취약**(앞서 다룬 WBS의 100%Rule처럼 사전계획중시) |
| **애자일** (Agile)       | 짧은주기(**스프린트**)로 5단계를 **작은단위로 여러번 반복**, 매 주기마다 동작하는 제품 산출 | **요구사항이 계속 변한다**는 걸 전제 — 빠른피드백, 유연성 (앞서 다룬 "터크만모델"의 팀발전단계와 자연스럽게 연동)              |
| **나선형모델** (Spiral)    | 계획→**위험분석**→개발→검토 사이클을 **나선형으로 반복**, 반복할수록 시스템이 완성되어감    | **위험(Risk)관리를 최우선**시 — 대규모/고위험 프로젝트에 적합(앞서 다룬 "리스크대응전략"이 매 사이클마다 적용됨)             |

→ 암기: **"폭포수는 한번에 끝까지(계획중시), 애자일은 짧게 여러번(변화대응), 나선형은 위험보며 여러번(위험중시)"** — 애자일과 나선형 둘 다 "반복"하지만, **애자일은 속도/피드백, 나선형은 위험분석**에 방점이 다르다는 게 헷갈리기 쉬운 변별포인트입니다.

### 도식화 제안

```
[폭포수] 요구→설계→구현→시험→유지보수  (한줄로 끝, 되돌아가기 어려움)
              ↓
[애자일] [요설구시]→[요설구시]→[요설구시]→...  (짧은사이클 반복, 스프린트마다 산출물)
              ↓
[나선형]      ┌──위험분석──┐
          계획 ↑         ↓ 개발
              └──검토←────┘  (반복할수록 나선이 커지며 완성도↑)
```

### Ⅳ. 모델선택기준 (실무형 배점)

| 상황                                                 | 권장모델                                            |
| :------------------------------------------------- | :---------------------------------------------- |
| **요구사항이 명확, 정부/공공사업처럼 문서화가 중요**                    | 폭포수 — 앞서 다룬 "정보시스템감리"가 각 단계 완료시점을 점검하는 구조와 잘 맞음 |
| **요구사항이 불확실, 빠른 시장대응 필요**(스타트업, 신규서비스)             | 애자일                                             |
| **대규모, 고위험, 신기술 도입**(예: KIPRIS Plus MCP전환같은 신아키텍처) | 나선형 — 매 반복마다 리스크를 재평가                           |

→ 앞서 다룬 "BPR추진절차"나 "AX추진절차"의 "진단-전략-파일럿-확산-내재화" 흐름도, 사실은 SDLC의 반복모델(애자일/나선형) 철학이 조직혁신영역에 응용된 것이라는 연결이 심화포인트입니다.

### Ⅴ. 결론 포인트

SDLC 모델선택의 본질은 \*\*"요구사항의 불확실성과 프로젝트의 위험도"\*\*라는 두 축에 따라 달라지며, 이는 오늘까지 다룬 "리스크대응전략(회피/완화/수용)"이나 "일정지연 만회대책(Crashing/Fast-tracking)"과 마찬가지로, \*\*"상황에 맞는 관리방식을 선택하는 것이 정답이며, 어느 하나가 절대적으로 우월하지 않다"\*\*는 프로젝트관리 전반의 공통결론과 일치합니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "집을 지을 때, 무턱대고 시멘트부터 부으면 결국 뼈대가 안 맞아 다 부수고 다시 지어야 한다. 먼저 어떤 집을 지을지 가족과 합의하고(요구사항 분석), 도면을 그리고(설계), 벽돌을 쌓고(구현), 비가 새는지 꼼꼼히 검사하고(테스트), 평생 수리하며 산다(유지보수). 소프트웨어 역시 이와 똑같은 과정을 거치는데, 코딩 전후의 모든 과정을 체계적으로 구조화한 뼈대가 바로 \*\*'SDLC(소프트웨어 생명주기)'\*\*다. 이 SDLC를 어떻게 굴리느냐에 따라 여러 철학(모델)으로 나뉜다. 폭포처럼 물이 떨어지면 절대 이전 단계로 거슬러 올라갈 수 없는 '폭포수 모델'은 과거의 방식이다. 고객이 뭘 원하는지 정확히 모를 때는 찰흙으로 모형부터 빨리 빚어 보여주는 '프로토타이핑 모델'을 쓴다. 실패하면 회사가 망하는 국가급 거대 프로젝트는 뱅글뱅글 돌면서 위험을 철저히 검증하는 '나선형 모델'을 쓴다. 그리고 오늘날, 고객의 변심이 하루가 다르게 일어나는 미친 속도의 IT 비즈니스 환경에서는, 무거운 계획을 잡지 않고 1\~2주 단위로 일단 동작하는 제품을 빠르게 내놓고 피드백을 반영하는 \*\*'애자일(Agile) 모델'\*\*이 현대 SDLC의 절대적 표준(De facto) 자리에 올랐다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 체계적인 소프트웨어 건축의 뼈대, SDLC 개요**

* **정의:** 소프트웨어의 타당성 검토와 기획부터 개발, 운영, 유지보수, 그리고 최종 폐기될 때까지의 **모든 과정을 체계적인 단계로 분할하고 구조화한 작업 프로세스 모델**.
* **목적:** 프로젝트의 고품질 보장, 비용 및 일정 산정의 명확한 기준(Milestone) 제공, 개발팀과 비즈니스 이해관계자 간의 **명확한 의사소통 표준 프레임워크 역할** 수행.

#### **II. \[본론 1] '무엇(What)'에서 '어떻게(How)'로: SDLC 5대 표준 프로세스 (도식화)**

가장 전통적인 폭포수 기준의 물 흐르듯 이어지는 5단계 핵심 뼈대입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzNjIuMTcwOTk5OTk5OTk5OTQgNjg1LjUiIHdpZHRoPSIzNjIuMTcwOTk5OTk5OTk5OTQiIGhlaWdodD0iNjg1LjUiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9TRExDX181IiBkYXRhLWxhYmVsPSLshoztlITtirjsm6jslrQg7IOd66qF7KO86riwKFNETEMpIO2VteyLrCA164uo6rOEIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIyODIuMTcwOTk5OTk5OTk5OTQiIGhlaWdodD0iNjA1LjUiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIyODIuMTcwOTk5OTk5OTk5OTQiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7shoztlITtirjsm6jslrQg7IOd66qF7KO86riwKFNETEMpIO2VteyLrCA164uo6rOEPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJSRVEiIGRhdGEtdG89IkRFUyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxODEuMDg1NDk5OTk5OTk5OTcsMTU0LjcgMTgxLjA4NTQ5OTk5OTk5OTk3LDIwMi43IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJERVMiIGRhdGEtdG89IklNUCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxODEuMDg1NDk5OTk5OTk5OTcsMjczLjQgMTgxLjA4NTQ5OTk5OTk5OTk3LDMyMS40IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJJTVAiIGRhdGEtdG89IlRFU1QiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTgxLjA4NTQ5OTk5OTk5OTk3LDM5Mi4xIDE4MS4wODU0OTk5OTk5OTk5Nyw0NDAuMSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVEVTVCIgZGF0YS10bz0iT1AiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTgxLjA4NTQ5OTk5OTk5OTk3LDUxMC44IDE4MS4wODU0OTk5OTk5OTk5Nyw1NTguOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUkVRIiBkYXRhLWxhYmVsPSIxLiDsmpTqtazsgqztla0g67aE7ISdIPCfjq8KJ+ustOyXhyhXaGF0KSfsnYQg66eM65OkIOqyg+yduOqwgCDsoJXsnZgK7JqU6rWs7IKs7ZWtIOuqheyEuOyEnChTUlMpIOuPhOy2nCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI2MS41NTc0OTk5OTk5OTk5OSIgeT0iODQiIHdpZHRoPSIyMzkuMDU1OTk5OTk5OTk5OTgiIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxODEuMDg1NDk5OTk5OTk5OTciIHk9IjExOS4zNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTgxLjA4NTQ5OTk5OTk5OTk3IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+MS4g7JqU6rWs7IKs7ZWtIOu2hOyEnSDwn46vPC90c3Bhbj48dHNwYW4geD0iMTgxLjA4NTQ5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj4mIzM5O+ustOyXhyhXaGF0KSYjMzk77J2EIOunjOuTpCDqsoPsnbjqsIAg7KCV7J2YPC90c3Bhbj48dHNwYW4geD0iMTgxLjA4NTQ5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7smpTqtazsgqztla0g66qF7IS47IScKFNSUykg64+E7LacPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkRFUyIgZGF0YS1sYWJlbD0iMi4g7ISk6rOEIChEZXNpZ24pIPCfk5AKJ+yWtOuWu+qyjChIb3cpJyDrp4zrk6Qg6rKD7J246rCAIOq1rOyhsO2ZlArslYTtgqTthY3sspgsIFVJLCBEQiDsiqTtgqTrp4gg7ISk6rOEIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIyMDIuNyIgd2lkdGg9IjI1MC4xNzA5OTk5OTk5OTk5NiIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE4MS4wODU0OTk5OTk5OTk5NyIgeT0iMjM4LjA0OTk5OTk5OTk5OTk4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxODEuMDg1NDk5OTk5OTk5OTciIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj4yLiDshKTqs4QgKERlc2lnbikg8J+TkDwvdHNwYW4+PHRzcGFuIHg9IjE4MS4wODU0OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+JiMzOTvslrTrlrvqsowoSG93KSYjMzk7IOunjOuTpCDqsoPsnbjqsIAg6rWs7KGw7ZmUPC90c3Bhbj48dHNwYW4geD0iMTgxLjA4NTQ5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7slYTtgqTthY3sspgsIFVJLCBEQiDsiqTtgqTrp4gg7ISk6rOEPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IklNUCIgZGF0YS1sYWJlbD0iMy4g6rWs7ZiEIChDb2RpbmcpIPCfkrsK7Iuk7KCcIO2UhOuhnOq3uOuemOuwjSDslrjslrTroZwK7IaM7Iqk7L2U65OcIOyekeyEsSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI4My43ODc1IiB5PSIzMjEuNCIgd2lkdGg9IjE5NC41OTU5OTk5OTk5OTk5OCIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE4MS4wODU0OTk5OTk5OTk5NyIgeT0iMzU2Ljc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxODEuMDg1NDk5OTk5OTk5OTciIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj4zLiDqtaztmIQgKENvZGluZykg8J+SuzwvdHNwYW4+PHRzcGFuIHg9IjE4MS4wODU0OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7Iuk7KCcIO2UhOuhnOq3uOuemOuwjSDslrjslrTroZw8L3RzcGFuPjx0c3BhbiB4PSIxODEuMDg1NDk5OTk5OTk5OTciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyGjOyKpOy9lOuTnCDsnpHshLE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iVEVTVCIgZGF0YS1sYWJlbD0iNC4g7YWM7Iqk7Yq4IChUZXN0aW5nKSDwn5CbCuyalOq1rOyCrO2VreqzvCDsnbzsuZjtlZjripTsp4AK64uo7JyEL+2Gte2VqS/si5zsiqTthZwv7J247IiYIOqysO2VqCDqsoDspp0iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9IjQ0MC4xIiB3aWR0aD0iMjUwLjE3MDk5OTk5OTk5OTk2IiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxODEuMDg1NDk5OTk5OTk5OTciIHk9IjQ3NS40NTAwMDAwMDAwMDAwNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTgxLjA4NTQ5OTk5OTk5OTk3IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+NC4g7YWM7Iqk7Yq4IChUZXN0aW5nKSDwn5CbPC90c3Bhbj48dHNwYW4geD0iMTgxLjA4NTQ5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7smpTqtazsgqztla3qs7wg7J287LmY7ZWY64qU7KeAPC90c3Bhbj48dHNwYW4geD0iMTgxLjA4NTQ5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7ri6jsnIQv7Ya17ZWpL+yLnOyKpO2FnC/snbjsiJgg6rKw7ZWoIOqygOymnTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJPUCIgZGF0YS1sYWJlbD0iNS4g7Jyg7KeA67O07IiYIChNYWludGVuYW5jZSkg8J+boO+4jwrrprTrpqzsiqQg7ZuEIOuyhOq3uCDtjKjsuZgg67CPIOq4sOuKpSDqsJzshKAKU0RMQyDsoITssrQg67mE7Jqp7J2YIDcwJSDsnbTsg4Eg7LCo7KeAISIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1Ni43NDA5OTk5OTk5OTk5ODUiIHk9IjU1OC44IiB3aWR0aD0iMjQ4LjY4OSIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTgxLjA4NTQ5OTk5OTk5OTk3IiB5PSI1OTQuMTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE4MS4wODU0OTk5OTk5OTk5NyIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPjUuIOycoOyngOuztOyImCAoTWFpbnRlbmFuY2UpIPCfm6DvuI88L3RzcGFuPjx0c3BhbiB4PSIxODEuMDg1NDk5OTk5OTk5OTciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuumtOumrOyKpCDtm4Qg67KE6re4IO2MqOy5mCDrsI8g6riw64qlIOqwnOyEoDwvdHNwYW4+PHRzcGFuIHg9IjE4MS4wODU0OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+U0RMQyDsoITssrQg67mE7Jqp7J2YIDcwJSDsnbTsg4Eg7LCo7KeAITwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 프로젝트 특성에 맞춘 4대 SDLC 핵심 모델 전격 비교표 (출제 1순위)**

면접과 지필에서 무조건 물어보는 4가지 핵심 모델의 사상적 차이점입니다.

| **SDLC 모델**                | **핵심 사상 (패러다임)**                                                                    | **최고 장점 및 적용 환경**                                           | **치명적 단점**                                  |
| :------------------------- | :---------------------------------------------------------------------------------- | :---------------------------------------------------------- | :------------------------------------------ |
| **폭포수** (Waterfall)        | 한 단계가 완전히 끝나야 다음 단계로 넘어가는 **가장 고전적인 하향식 선형 모델.**                                    | 관리가 매우 쉽고 직관적. **요구사항이 명확히 고정된 정적 프로젝트**에 적합.               | 중간에 **요구사항 변경이 거의 불가능**하여 현대 비즈니스에 부적합함.    |
| **프로토타이핑** (Prototyping)   | 핵심 기능만 가진 \*\*'시제품(Prototype)'\*\*을 먼저 만들어 고객에게 보여주고 피드백을 받아 요구사항을 확정함.             | 사용자의 요구를 정확히 파악 가능. **UI/UX 중심이나 요구가 불분명할 때** 최고.           | 시제품을 최종 제품으로 오해하거나, 버리는 시제품 비용 낭비 발생.       |
| **나선형** (Spiral)           | \*\*'계획 ➔ 위험 분석 ➔ 개발 ➔ 고객 평가'\*\*의 4단계를 뱅글뱅글 돌며 점진적으로 개발함.                          | \*\*'위험 분석'\*\*이 들어가 실패 확률 극소화. **초대규모 자본의 고위험 프로젝트**에 필수.  | 뱅글뱅글 돌기 때문에 관리가 매우 복잡하고 프로젝트 기간이 기약 없이 길어짐. |
| **애자일 🚀** (Agile / Scrum) | 거대한 계획 대신, **1\~4주(Sprint) 단위의 짧은 주기로 '실제로 동작하는 소프트웨어'를 지속적으로 배포**하며 고객 요구를 즉각 반영함. | **변화 수용력(적응성)이 압도적으로 높음.** **스타트업 및 현대의 거의 모든 IT 프로젝트 표준.** | 큰 그림(아키텍처)이 무너질 수 있고, 문서화가 부족해 인수인계가 어려움.   |

#### **IV. \[결론/제언] 애자일(Agile)을 넘어, 데브옵스(DevOps) 및 CI/CD 자동화 파이프라인으로의 진화**

* **(키워드 위주 2줄 마무리)** "현대의 SDLC는 단방향으로 흐르는 폭포수를 완전히 버리고, 빠른 변화를 수용하는 \*\*'애자일(Agile) 사상'\*\*을 뼈대로 삼고 있습니다. 나아가 개발(Dev)과 운영(Ops)의 벽마저 허물어버린 **'데브옵스(DevOps)' 철학**과, 사람이 직접 빌드하고 테스트하던 과정을 젠킨스(Jenkins) 등으로 자동화하는 \*\*'CI/CD(지속적 통합/배포) 파이프라인'\*\*이 현대 소프트웨어 생명주기의 절대적인 기술 표준으로 자리매김하였습니다."
