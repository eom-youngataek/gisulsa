### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (가드레일정의, 앞서다룬"100%우회"의함의) — 3~4줄
Ⅱ. 가드레일 3대유형 (본론①, 도식 1개 필수)
Ⅲ. 구현계층 - 어디에배치하는가 (본론②, 핵심 배점)
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서다룬가드레일제품(AzurePromptShield등)이100%우회당했다는사실은, '가드레일이무용하다'는뜻이아니라 '가드레일을어떻게,몇겹으로,어느계층에배치하는지가더중요하다'는뜻이다 — 가드레일은 단일제품이아니라 여러계층의검증체계"\*\*라는한줄로시작하면, 이답안이 왜 별도로필요한지 드러납니다.

### Ⅱ. 가드레일 3대유형 — "입·출·행" (입력/출력/행동)

| 유형                 | 감시대상                          | 예시                                                  |
| :----------------- | :---------------------------- | :-------------------------------------------------- |
| **입력가드레일**(Input)  | 사용자프롬프트,외부문서                  | 앞서다룬 **프롬프트인젝션·탈옥탐지**,PII포함여부검사                     |
| **출력가드레일**(Output) | LLM이생성한응답                     | 앞서다룬 **부적절한출력처리(OWASP LLM05)** 방지— 민감정보노출,악성URL생성차단 |
| **행동가드레일**(Action) | AI에이전트의 **실제행동**(API호출,파일접근등) | 앞서다룬 **RBAC/ABAC의최소권한**을 AI에이전트에적용                  |

→ 암기: **"들어오는말을검사하고,나가는말을검사하고,실제로하는행동을검사한다"** — 앞서다룬 **"메일읽기+DB조회+메일발송"조합공격**을 막으려면, **입력가드레일만으로는부족**하고 \*\*행동가드레일(도구조합제한)\*\*까지필요하다는게 핵심입니다.

### 도식화 제안

```
[사용자입력] ──[입력가드레일]──→ [LLM처리]
                (인젝션·탈옥탐지,               ↓
                 PII검사)              [행동가드레일]
                                        (API호출권한제한,
                                         도구조합제한)
                                              ↓
                                       [출력가드레일]
                                       (민감정보,악성URL검사)
                                              ↓
                                          [최종응답]
```

### Ⅲ. 구현계층 — 어디에배치하는가, 핵심 배점

**함정 방지: "가드레일을하나설치한다"고답하면절반. 앞서다룬"AIGateway"개념처럼, 여러계층에분산배치해야하는이유를보여줘야완성됩니다.**

| 계층                | 내용                                                                                          |
| :---------------- | :------------------------------------------------------------------------------------------ |
| **모델자체수준**        | \*\*적대적훈련(AdversarialTraining)\*\*으로 모델이스스로 인젝션에저항하도록 학습— 가장근본적이지만 **완벽하지않음**(앞서다룬100%우회사례) |
| **별도가드레일LLM**     | 원래LLM과 **별도의검증전용LLM**을 앞뒤에배치해 입출력검사 — 앞서다룬 **Google Model Armor**방식                         |
| **AI게이트웨이**(중앙집중) | 앞서다룬 **"모든AI에이전트·도구상호작용을중앙에서정책관리"**— 개별앱마다가드레일을따로만들지않고 **하나의관문**으로통합                        |
| **모니터링·레드팀**(지속)  | 앞서다룬 **CTEM처럼**,**포괄적로깅+이상탐지**로 지속감시,**전담AI레드팀**이 선제적으로취약점탐색                                |

→ 암기: **"모델자체를훈련시키고,별도검증LLM을세우고,전체를관문하나로모으고,계속감시한다"** — 앞서다룬 **"WAAP5.0검증프로그램"**(2026년,MITREATT&CK+OWASP연계테스트)이 바로 이런 **다계층가드레일의효과성을객관적으로측정**하려는 최신시도입니다.

### 도식화 제안

```
[계층1: 모델자체] 적대적훈련(근본적,단독으론불충분)
     ↓
[계층2: 별도가드레일LLM] Model Armor류(입출력검증)
     ↓
[계층3: AI Gateway] 모든에이전트·도구의 중앙정책관리
     ↓
[계층4: 지속모니터링] 로깅+이상탐지+레드팀(CTEM식상시검증)

→ 어느한계층이뚫려도, 나머지계층이보완(Defense in Depth)
```

### Ⅳ. 결론

LLM가드레일의핵심은 \*\*"단하나의필터가아니라, 모델자체훈련부터별도검증LLM,중앙집중게이트웨이,지속적모니터링까지 4개계층이겹겹이보완하는 심층방어체계"\*\*라는것입니다 — 앞서다룬 \*\*"AzurePromptShield100%우회"\*\*사례가 보여주듯 **어느한계층도단독으로완벽할수없기**때문에, **"뚫려도다음계층이잡아내는"** 구조설계가 유일한현실적해법입니다 — 이는 앞서다룬 \*\*오늘하루전체의결론(완벽한방어는없으니,다층방어와지속검증으로대응한다)\*\*이 AI가드레일이라는 가장최신의영역에서도 정확히똑같이적용된다는 것을 보여줍니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "고속도로를 달리는 스포츠카가 운전대를 잘못 꺾었을 때 낭떠러지로 추락하지 않게 막아주는 것이 '가드레일'이다. 통제 불능의 엄청난 상상력을 가진 LLM(거대 언어 모델)이 비윤리적인 욕설을 내뱉거나, 환각(거짓말)을 진실처럼 우기거나, 해커의 최면(프롬프트 인젝션)에 뚫려 해킹 도구로 전락하는 것을 막아주는 안전 방화벽이 바로 \*\*'LLM 가드레일(Guardrail)'\*\*이다. 가드레일은 LLM 앞뒤로 겹겹이 세워진 별도의 인공지능 필터다. 첫째, 질문이 들어올 때 \*\*'입력 가드레일'\*\*이 해커의 탈옥(Jailbreak) 시도와 비속어를 1차로 튕겨낸다. 둘째, 대화 도중 \*\*'토픽 가드레일'\*\*이 개입하여, 은행 고객센터 AI가 뜬금없이 주식 종목을 추천하거나 정치 이야기를 하지 못하도록 화제를 억지로 통제한다. 셋째, 모델이 답변을 뱉기 직전 \*\*'출력 가드레일'\*\*이 가동되어, 답변에 주민번호나 회사 소스코드가 섞여 있는지, 혹은 엉터리로 지어낸 환각 정보인지 최종 스캔하여 안전하지 않다면 출력을 백지화해 버린다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] AI의 폭주를 막는 윤리와 보안의 경계선, LLM 가드레일 개요**

* **정의:** 생성형 AI(LLM)가 사용자와 상호작용하는 과정에서 보안 위협, 비윤리적 발언, 편향성, 환각(Hallucination), 기밀 유출 등 **'원치 않는 결과'를 생성하지 않도록 입력과 출력 양방향을 통제하는 정책 기반의 실시간 안전 필터 체계**. (대표적 오픈소스: Nvidia의 NeMo Guardrails).
* **도입 목적:** 단순한 해킹(OWASP Top 10) 방어를 넘어서, AI 서비스의 신뢰도와 품질을 보장하고, 기업의 법적/윤리적 컴플라이언스(저작권 침해, 개인정보 유출) 위반을 원천 차단하기 위함.

#### **II. \[본론 1] (단순화 버전) 3단계 방어벽으로 구성된 LLM 가드레일 파이프라인 (도식화)**

메인 AI 모델이 헛소리를 하지 못하게 앞뒤로 감싸고 있는 가드레일의 위치를 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5MTEuNDk0OTk5OTk5OTk5OSA0MzUuNDUwMDAwMDAwMDAwMDUiIHdpZHRoPSI5MTEuNDk0OTk5OTk5OTk5OSIgaGVpZ2h0PSI0MzUuNDUwMDAwMDAwMDAwMDUiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IkxMTV9fR3VhcmRyYWlsc18zX18iIGRhdGEtbGFiZWw9IkxMTSDqsIDrk5zroIjsnbwgKEd1YXJkcmFpbHMpIDPri6jqs4Qg7Ya17KCcIOuplOy7pOuLiOymmCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iODAzLjQ5NDk5OTk5OTk5OTkiIGhlaWdodD0iMzU1LjQ1MDAwMDAwMDAwMDA1IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iODAzLjQ5NDk5OTk5OTk5OTkiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5MTE0g6rCA65Oc66CI7J28IChHdWFyZHJhaWxzKSAz64uo6rOEIO2GteygnCDrqZTsu6Tri4jsppg8L3RleHQ+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iTExNX19fX19fIiBkYXRhLWxhYmVsPSJMTE0g7YyM7Jq0642w7J207IWYIOuqqOuNuCAo6rGw64yAIOyWuOyWtCDrqqjrjbgg8J+noCkiPgogIDxyZWN0IHg9IjE1OC44NDkiIHk9IjIwNi42NSIgd2lkdGg9IjI4My4yMDA5OTk5OTk5OTk5NiIgaGVpZ2h0PSIxMDcuOSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjE1OC44NDkiIHk9IjIwNi42NSIgd2lkdGg9IjI4My4yMDA5OTk5OTk5OTk5NiIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTcwLjg0OSIgeT0iMjIwLjY1IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPkxMTSDtjIzsmrTrjbDsnbTshZgg66qo6424ICjqsbDrjIAg7Ja47Ja0IOuqqOuNuCDwn6egKTwvdGV4dD4KPC9nPgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJHVUFSRF9JTiIgZGF0YS10bz0iTExNIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLslYjsoITtlZwg7KeI66y466eMIiBwb2ludHM9IjU5NS43MjU5OTk5OTk5OTk5LDE1MS43NSA2MDcuNzI1OTk5OTk5OTk5OSwxNTEuNzUgNjA3LjcyNTk5OTk5OTk5OTksMTIzLjM3NSA4NDMuNDk0OTk5OTk5OTk5OSwxMjMuMzc1IDg2My40OTQ5OTk5OTk5OTk5LDEyMy4zNzUgODYzLjQ5NDk5OTk5OTk5OTksODMuMzc1IDU2Ny43MjU5OTk5OTk5OTk5LDgzLjM3NSA1NjcuNzI1OTk5OTk5OTk5OSw1NSAxMDYuODQ4OTk5OTk5OTk5OTksNTUgMTA2Ljg0ODk5OTk5OTk5OTk5LDIxMC42NSAxMTguODQ4OTk5OTk5OTk5OTksMjEwLjY1IDg2My40OTQ5OTk5OTk5OTk5LDIxMC42NSA4NjMuNDk0OTk5OTk5OTk5OSwyNTAuNjUgMzE5LjIwMDk5OTk5OTk5OTk2LDI1MC42NSAzMTkuMjAwOTk5OTk5OTk5OTYsMjY0LjcyNSAzNTUuMjAwOTk5OTk5OTk5OTYsMjY0LjcyNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTExNIiBkYXRhLXRvPSJHVUFSRF9PVVQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iuy0iOyViCDri7Xrs4Ag7IOd7ISxIiBwb2ludHM9IjQyNi4wNDk5OTk5OTk5OTk5NSwyNzMuOTUwMDAwMDAwMDAwMDUgNDQyLjA0OTk5OTk5OTk5OTk1LDI3My45NTAwMDAwMDAwMDAwNSAyMCwyNzMuOTUwMDAwMDAwMDAwMDUgMjAsMjMzLjk1MDAwMDAwMDAwMDAyIDc3NS40OTQ5OTk5OTk5OTk5LDIzMy45NTAwMDAwMDAwMDAwMiA3NzUuNDk0OTk5OTk5OTk5OSwyODAuNTUgODAzLjQ5NDk5OTk5OTk5OTksMjgwLjU1IDIwLDI4MC41NSAyMCwzMjAuNTUgODE1LjQ5NDk5OTk5OTk5OTksMzIwLjU1IDgxNS40OTQ5OTk5OTk5OTk5LDM3NS4yMjUgNDU0LjA0OTk5OTk5OTk5OTk1LDM3NS4yMjUgNDU0LjA0OTk5OTk5OTk5OTk1LDM2Ny4xNTAwMDAwMDAwMDAwMyA0NDIuMDQ5OTk5OTk5OTk5OTUsMzY3LjE1MDAwMDAwMDAwMDAzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJVU0VSIiBkYXRhLXRvPSJHVUFSRF9JTiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0NDIuMDQ5OTk5OTk5OTk5OTUsMTUxLjc1IDQ5MC4wNDk5OTk5OTk5OTk5NSwxNTEuNzUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkdVQVJEX09VVCIgZGF0YS10bz0iUkVTVUxUIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsoJXsoJzrkJwg64u167OA66eMIiBwb2ludHM9IjQ0Mi4wNDk5OTk5OTk5OTk5NSwzNTQuODUgNDU0LjA0OTk5OTk5OTk5OTk1LDM1NC44NSA0NTQuMDQ5OTk5OTk5OTk5OTUsMzQ2Ljc3NTAwMDAwMDAwMDAzIDY0My43MjU5OTk5OTk5OTk5LDM0Ni43NzUwMDAwMDAwMDAwMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTExNIiBkYXRhLXRvPSJHVUFSRF9UT1BJQyIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzU1LjIwMDk5OTk5OTk5OTk2LDI4My4xNzUgMzE5LjIwMDk5OTk5OTk5OTk2LDI4My4xNzUgMzE5LjIwMDk5OTk5OTk5OTk2LDI4Ni4yNSAzMDcuMjAwOTk5OTk5OTk5OTYsMjg2LjI1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkdVQVJEX1RPUElDIiBkYXRhLXRvPSJMTE0iIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjMwNy4yMDA5OTk5OTk5OTk5NiwyNzMuOTUwMDAwMDAwMDAwMDUgMzU1LjIwMDk5OTk5OTk5OTk2LDI3My45NTAwMDAwMDAwMDAwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkdVQVJEX0lOIiBkYXRhLXRvPSJMTE0iIGRhdGEtbGFiZWw9IuyViOyghO2VnCDsp4jrrLjrp4wiPgogIDxyZWN0IHg9IjExOC41OTMwMDAwMDAwMDAwMyIgeT0iMTk1LjUiIHdpZHRoPSI5MC43MTIwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjE2My45NDkwMDAwMDAwMDAwNCIgeT0iMjEwLjY1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7slYjsoITtlZwg7KeI66y466eMPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkxMTSIgZGF0YS10bz0iR1VBUkRfT1VUIiBkYXRhLWxhYmVsPSLstIjslYgg64u167OAIOyDneyEsSI+CiAgPHJlY3QgeD0iMzgzLjcyODAwMDAwMDAwMDI0IiB5PSIyNjUuNDAwMDAwMDAwMDAwMDMiIHdpZHRoPSI5Mi40OTQwMDAwMDAwMDAwMyIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjQyOS45NzUwMDAwMDAwMDAyNSIgeT0iMjgwLjU1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7stIjslYgg64u167OAIOyDneyEsTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJHVUFSRF9PVVQiIGRhdGEtdG89IlJFU1VMVCIgZGF0YS1sYWJlbD0i7KCV7KCc65CcIOuLteuzgOunjCI+CiAgPHJlY3QgeD0iNDk3LjUzMTk5OTk5OTk5OTkiIHk9IjMzMC43NzUiIHdpZHRoPSI5MC43MTIwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjU0Mi44ODc5OTk5OTk5OTk5IiB5PSIzNDUuOTI0OTk5OTk5OTk5OTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuygleygnOuQnCDri7Xrs4Drp4w8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlVTRVIiIGRhdGEtbGFiZWw9IuyCrOyaqeyekCDtlITroaztlITtirgg8J+RpAomcXVvdDvtg4jsmKUv7KCV7LmYL+2Pre2DhCZxdW90OyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyNzcuMDkzOTk5OTk5OTk5OTQiIHk9IjEyNC44NSIgd2lkdGg9IjE2NC45NTYwMDAwMDAwMDAwMiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzU5LjU3MTk5OTk5OTk5OTk1IiB5PSIxNTEuNzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjM1OS41NzE5OTk5OTk5OTk5NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuyCrOyaqeyekCDtlITroaztlITtirgg8J+RpDwvdHNwYW4+PHRzcGFuIHg9IjM1OS41NzE5OTk5OTk5OTk5NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+JnF1b3Q77YOI7JilL+ygley5mC/tj63tg4QmcXVvdDs8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iR1VBUkRfSU4iIGRhdGEtbGFiZWw9IkdVQVJEX0lOIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQ5MC4wNDk5OTk5OTk5OTk5NSIgeT0iMTMzLjMiIHdpZHRoPSIxMDUuNjc1OTk5OTk5OTk5OTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNTQyLjg4Nzk5OTk5OTk5OTkiIHk9IjE1MS43NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+R1VBUkRfSU48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkxMTSIgZGF0YS1sYWJlbD0iTExNIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjcwLjg0ODk5OTk5OTk5OTk5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI5MS40MjQ1IiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkxMTTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iR1VBUkRfT1VUIiBkYXRhLWxhYmVsPSJHVUFSRF9PVVQiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzIxLjU1NCIgeT0iMzQyLjU1IiB3aWR0aD0iMTIwLjQ5NTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjM4MS44MDE5OTk5OTk5OTk5NiIgeT0iMzYxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5HVUFSRF9PVVQ8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJFU1VMVCIgZGF0YS1sYWJlbD0i7JWI7KCE7ZWcIOy1nOyihSDri7Xrs4Ag8J+foiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI2NDMuNzI1OTk5OTk5OTk5OSIgeT0iMzI4LjMyNTAwMDAwMDAwMDA1IiB3aWR0aD0iMTU5Ljc2OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI3MjMuNjEwNDk5OTk5OTk5OSIgeT0iMzQ2Ljc3NTAwMDAwMDAwMDAzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7slYjsoITtlZwg7LWc7KKFIOuLteuzgCDwn5+iPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJMTE0iIGRhdGEtbGFiZWw9IkxMTSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzNTUuMjAwOTk5OTk5OTk5OTYiIHk9IjI1NS41IiB3aWR0aD0iNzAuODQ4OTk5OTk5OTk5OTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjM5MC42MjU1IiB5PSIyNzMuOTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkxMTTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iR1VBUkRfVE9QSUMiIGRhdGEtbGFiZWw9IkdVQVJEX1RPUElDIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjE3NC44NDkiIHk9IjI2MS42NSIgd2lkdGg9IjEzMi4zNTE5OTk5OTk5OTk5OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIyNDEuMDI0OTk5OTk5OTk5OTgiIHk9IjI4MC4wOTk5OTk5OTk5OTk5NyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+R1VBUkRfVE9QSUM8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] LLM 가드레일을 구성하는 3대 핵심 통제 구역 전격 해부 (3단 표 - 1순위)**

입력과 출력 방어뿐만 아니라, 화제가 산으로 가지 않게 막는 \*\*'대화(토픽) 통제'\*\*의 중요성을 대조하는 것이 핵심입니다.

| **가드레일 통제 단계**                                  | **통제(필터링)의 핵심 목적 및 감지 대상**                                                                                                          | **실무 작동 메커니즘 및 방어 효과 🚨**                                                                                                      |
| :---------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| **1. 입력 가드레일** *(Input Guardrails)*             | **'LLM 방화벽 (악성 요청 입구 컷)'.** 메인 LLM이 질문을 처리하기 전에, 프롬프트 인젝션(가스라이팅), PII(주민번호) 입력, 노골적인 비속어나 유해한 지시를 먼저 스캔하여 차단함.                      | **\[보안 및 프라이버시 사고 방지]** 사용자가 회사의 소스코드를 복사해 넣고 질문하면, 이를 가드레일이 인지하고 **"기밀 정보는 처리할 수 없습니다"라며 AI에게 넘기지 않고 거절해 버림.**                |
| **2. 토픽/대화 가드레일** *(Dialog/Topic* *Guardrails)* | **'AI의 역할 고정 및 헛소리(주제 이탈) 방지'.** 챗봇이 설계된 목적(도메인)에 맞게 행동하도록 대화의 문맥을 꽉 잡음. 금지된 주제(정치, 주식 투자 조언, 폭력)로 유도하면 궤도를 수정함.                    | **\[기업 평판 보호 및 법적 리스크 차단 💯]** 금융 상담 AI 봇에게 "지금 테슬라 주식 사도 돼?"라고 물으면, **"저는 금융 상품 안내만 가능하며, 투자 조언은 할 수 없습니다"라고 대화의 선을 긋고 통제함.** |
| **3. 출력 가드레일** *(Output Guardrails)*            | **'환각 검증 및 민감 정보 최종 마스킹'.** 메인 AI가 내뱉은 답변이 사용자 화면에 출력되기 직전에, 답변에 악성코드(XSS 등)가 섞였는지, 혹은 없는 사실을 지어낸 환각(Hallucination)인지 한 번 더 팩트 체크함. | **\[환각(오류) 차단 및 품질 보장]** 답변 내용에 사내망 IP나 타인의 개인정보가 튀어나오면 즉시 `***` 기호로 마스킹 처리하거나, **근거 없는 답변 생성 시 자체적으로 출력을 취소해 버림.**            |

#### **IV. \[결론/제언] 환각 억제를 위한 RAG 시스템과의 필수적인 결합 (하이브리드 방어)**

* **(키워드 위주 2줄 마무리)** "가드레일만으로는 AI가 지어내는 교묘한 환각(거짓말)을 100% 탐지해 낼 수 없습니다. 따라서 가드레일 시스템은 반드시 신뢰할 수 있는 사내 문서만을 참고하여 답변을 생성하도록 강제하는 **'RAG(검색 증강 생성)' 아키텍처와 결합하여, 통제(가드레일)와 근거(RAG)의 하이브리드 안전망을 구축해야 합니다.**"
