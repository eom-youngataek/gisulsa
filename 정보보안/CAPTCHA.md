### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (CAPTCHA정의, 튜링테스트의역설) — 3~4줄
Ⅱ. 세대별진화 (본론①, 도식 1개 필수)
Ⅲ. AI시대의붕괴및차세대전환 (본론②, 핵심 배점)
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서다룬크리덴셜스터핑,DDoS-for-hire는모두 '자동화된봇의대량요청'을전제로했는데, CAPTCHA는바로그 '이요청을보낸게사람인지기계인지'를구별하는 첫번째관문 — 그런데정작CAPTCHA를풀게하려고학습시킨AI기술이, 이제CAPTCHA를푸는데더강력해지는역설적상황"\*\*이라는한줄로시작하면, 왜 CAPTCHA가 "AI와의군비경쟁"인지 드러납니다.

### Ⅱ. 세대별진화 — 계속뚫리고, 계속진화

| 세대                      | 방식                       | 뚫린이유                                   |
| :---------------------- | :----------------------- | :------------------------------------- |
| **1세대**                 | 왜곡된 **텍스트**읽기            | 2014년 **99.8%인식**하는OCR등장으로무력화          |
| **2세대**                 | **이미지선택**(신호등,택시등 실물체식별) | 딥러닝이미지인식으로 뚫림                          |
| **3세대**(reCAPTCHAv2/v3) | **체크박스**("나는로봇이아닙니다")    | **마우스이동패턴,쿠키등행동데이터**로판별 — 데이터부족시2세대로회귀 |

→ 암기: **"텍스트→이미지→행동패턴, 매번AI가따라잡으면 다음세대로진화"** — 앞서다룬 \*\*"랜섬웨어/RaaS,인포스틸러"\*\*에서 봤던 **"공격기술발전에방어기술이쫓기는"** 구조가, CAPTCHA에서도 **정확히같은패턴**으로 반복됩니다.

### 도식화 제안

```
[1세대: 왜곡텍스트] ──OCR발전으로뚫림──→ [2세대: 이미지선택]
                                              ↓ 딥러닝으로뚫림
[3세대: 행동기반(reCAPTCHAv3)] ←──────────────┘
     ↓ AI 에이전트의행동패턴모방으로 위협받음(2025~2026년현재)
[차세대: ?]
```

### Ⅲ. AI시대의붕괴 및 차세대전환 — 핵심 배점

**함정 방지: "AI가다뚫는다"고만하면절반. 구체적붕괴사례와, 앞서다룬여러답안과연결된 차세대대안을보여줘야완성됩니다.**

| 위협                         | 내용                                                                                        |
| :------------------------- | :---------------------------------------------------------------------------------------- |
| **LLM기반솔버**(2024\~2025년연구) | \*\*"Oedipus"\*\*같은 **LLM기반추론솔버**등장 — 앞서다룬 **OWASPLLM**의역설: **AI가AI방어(CAPTCHA)를 뚫는도구로악용** |
| **에이전틱비전언어모델**             | 2025년USENIX보안학회연구: **"CAPTCHA는여전히봇에게어려운가?"**— **일반화된비전언어모델**이 **일반적인시각적CAPTCHA를풀수있음을입증**  |
| **인간솔버서비스**(우회서비스)         | AI가안되면, **실제사람이돈받고CAPTCHA를대신풀어주는서비스**존재 — 기술적방어의 **근본적한계**                                |
| **2026년구글reCAPTCHA유료화**    | \*\*"자율주행학습용데이터수집이필요없어지자 유료화"\*\*라는비판 — CAPTCHA가 **AI학습데이터수집도구였다는역설**도드러남                 |

→ 암기: **"AI로풀거나,AI로도안되면사람이대신풀어준다"** — 앞서다룬 \*\*"DDoS-for-hire(시간당38달러)"\*\*처럼, CAPTCHA우회도 \*\*"돈만내면누구나뚫을수있는서비스"\*\*가 되어버린것이 핵심위협입니다.

**차세대대안(앞서다룬답안들과연결)**

| 대안                              | 오늘답안연결                                                              |
| :------------------------------ | :------------------------------------------------------------------ |
| **행동기반+AI위험평가**                 | 앞서다룬 \*\*UEBA(사용자행동분석)\*\*의 웹버전                                     |
| **생체인식**                        | 앞서다룬 **패스키/FIDO2**와같은방향 — **"CAPTCHA를풀필요없이, 신원자체를증명"**              |
| **PoW기반CAPTCHA**(Proof-of-Work) | 컴퓨터에 **일정연산부담**을줘서, **대량요청자체를경제적으로비효율화**— 앞서다룬 \*\*"키스트레칭"\*\*의 웹버전 |

→ "결국CAPTCHA의미래는, **문제를푸는것자체보다 신원(패스키)이나행동(UEBA)으로 판별하는쪽으로진화**한다"는게 이답안의핵심통찰입니다.

### 도식화 제안

```
[전통CAPTCHA]                    [차세대접근]
"이문제를풀어봐"                   "네가누군지증명해(패스키)"
(AI가결국풀어버림)                 "네행동이이상해(UEBA)"
                                 "풀려면돈들게해(PoW)"
```

### Ⅳ. 결론

CAPTCHA는 \*\*"사람과기계를구별하려는 튜링테스트의실용적구현"\*\*이었지만, 2025\~2026년현재 **"CAPTCHA를풀도록학습된AI기술자체가, 이제CAPTCHA를무력화하는도구가되는"** 역설에직면했습니다 — 이는 앞서다룬 \*\*크리덴셜스터핑(재사용된비밀번호),DDoS-for-hire(공격의서비스화),OWASPLLM(AI가새로운공격도구)\*\*에서 반복된 **"방어기술의약점을, 바로그기술을만든AI가찾아내는"** 오늘하루전체를관통하는패턴을 다시확인시켜주며, 결국 \*\*"문제풀이(CAPTCHA)에서신원증명(패스키)과행동분석(UEBA)으로"\*\*전환하는 것이 2026년현재의 현실적방향이라는 결론으로 마무리됩니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "유명 가수의 콘서트 티켓팅 날, 1초 만에 전석이 매진됐다. 알고 보니 암표상들이 수만 개의 '매크로 봇(Bot)' 프로그램을 돌려 표를 싹쓸이한 것이다. 이런 봇들의 무차별적인 예매, 스팸 도배, 그리고 무한대로 비밀번호를 때려 맞추는 해킹(크리덴셜 스터핑)을 막아내기 위해 로그인 창 앞에 세워둔 문지기가 바로 \*\*'캡차(CAPTCHA)'\*\*다. 캡차는 기계가 풀 수 없는 문제를 내어 인간과 기계를 구별하는 '역 튜링 테스트'다. 1세대 캡차는 찌그러진 글자를 읽게 했다. 하지만 봇(Bot)이 글자 인식(OCR) 기술을 발전시켜 다 읽고 뚫어버렸다. 그래서 2세대(v2)는 '신호등 사진을 고르시오'라며 이미지를 고르게 했다. 하지만 사람을 너무 귀찮게 한다는 원성이 빗발쳤다. 결국 최신 3세대(v3, Invisible) 캡차는 아예 사용자에게 퀴즈를 내지 않는다. 유저가 마우스를 움직이는 궤적, 클릭하는 속도를 백그라운드에서 AI가 몰래 분석하여 '마우스가 기계처럼 자로 잰 듯 0.1초 만에 일직선으로 움직이네? 넌 사람(Human)이 아니라 봇이야!'라고 판단해 차단하는 은밀하고 편리한 시스템으로 진화했다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 기계의 침입을 막는 역 튜링 테스트, 캡차(CAPTCHA) 개요**

* **정의:** 사용자가 폼(Form)을 제출할 때, **컴퓨터(매크로 봇)는 풀기 어렵지만 사람은 쉽게 풀 수 있는 퍼즐이나 퀴즈를 제공**하여, 현재 접속자가 '진짜 사람(Human)'인지 '악성 봇(Bot)'인지 완전히 자동화된 방식으로 식별하는 보안 기술.
* **보안 적용 목적:** 브루트포스(무차별 대입)를 통한 계정 해킹 방지, 크리덴셜 스터핑 차단, 무작위 스팸 메일 발송 및 게시물 도배 방지, 콘서트 예매 등에서의 매크로(Macro) 싹쓸이 차단.

#### **II. \[본론 1] (단순화 버전) 사람과 봇을 걸러내는 캡차 방어 파이프라인 (도식화)**

사용자(사람)와 매크로(기계)가 로그인 창에서 어떻게 걸러지는지 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMTQ3LjI1NDk5OTk5OTk5OTkgMzk1LjY0NTk5OTk5OTk5OTk2IiB3aWR0aD0iMTE0Ny4yNTQ5OTk5OTk5OTk5IiBoZWlnaHQ9IjM5NS42NDU5OTk5OTk5OTk5NiIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX19fX18iIGRhdGEtbGFiZWw9IuybueyCrOydtO2KuCDroZzqt7jsnbggLyDsmIjrp6Qg7Y6Y7J207KeAIOuwqeyWtOyEoCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMTA2Ny4yNTQ5OTk5OTk5OTk5IiBoZWlnaHQ9IjMxNS42NDU5OTk5OTk5OTk5NiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjEwNjcuMjU0OTk5OTk5OTk5OSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPuybueyCrOydtO2KuCDroZzqt7jsnbggLyDsmIjrp6Qg7Y6Y7J207KeAIOuwqeyWtOyEoDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iSFVNQU4iIGRhdGEtdG89IldFQiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyMjMuMTc5LDI0OC40OTggMjQ3LjE3ODk5OTk5OTk5OTk3LDI0OC40OTggMjQ3LjE3ODk5OTk5OTk5OTk3LDIxMS44MjI5OTk5OTk5OTk5OCAyNzEuMTc5LDIxMS44MjI5OTk5OTk5OTk5OCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQk9UIiBkYXRhLXRvPSJXRUIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjIzLjE3OSwxNzUuMTQ4IDI0Ny4xNzg5OTk5OTk5OTk5NywxNzUuMTQ4IDI0Ny4xNzg5OTk5OTk5OTk5NywyMTEuODIyOTk5OTk5OTk5OTggMjcxLjE3OSwyMTEuODIyOTk5OTk5OTk5OTgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IldFQiIgZGF0YS10bz0iQ0FQVENIQSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzODkuNDUyLDIxMS44MjI5OTk5OTk5OTk5OCA0MzcuNDUyLDIxMS44MjI5OTk5OTk5OTk5OCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQ0FQVENIQSIgZGF0YS10bz0iREVOWSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i66eI7Jqw7IqkIOybgOyngeyehCDruYTsoJXsg4EK66y47KCc66W8IOuquyDtkogiIHBvaW50cz0iNjUwLjQ5MDMzMzMzMzMzMzMsMTY5LjIxNTMzMzMzMzMzMzMyIDkyMS4xMTIsMTY5LjIxNTMzMzMzMzMzMzMyIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDQVBUQ0hBIiBkYXRhLXRvPSJBTExPVyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7Y287KaQIO2GteqzvArsnpDsl7DsiqTrn6zsmrQg66eI7Jqw7IqkIOq2pOyggSIgcG9pbnRzPSI2NTAuNDkwMzMzMzMzMzMzMywyNTQuNDMwNjY2NjY2NjY2NjcgOTIxLjExMiwyNTQuNDMwNjY2NjY2NjY2NjciIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQ0FQVENIQSIgZGF0YS10bz0iREVOWSIgZGF0YS1sYWJlbD0i66eI7Jqw7IqkIOybgOyngeyehCDruYTsoJXsg4EK66y47KCc66W8IOuquyDtkogiPgogIDxyZWN0IHg9Ijc0My4wMzc5OTk5OTk5OTk5IiB5PSIxNDYuMjE1MzMzMzMzMzMzMzIiIHdpZHRoPSIxMjguMTM0MDAwMDAwMDAwMDEiIGhlaWdodD0iNDQuNiIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI4MDcuMTA0OTk5OTk5OTk5OSIgeT0iMTY4LjUxNTMzMzMzMzMzMzMzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIj48dHNwYW4geD0iODA3LjEwNDk5OTk5OTk5OTkiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij7rp4jsmrDsiqQg7JuA7KeB7J6EIOu5hOygleyDgTwvdHNwYW4+PHRzcGFuIHg9IjgwNy4xMDQ5OTk5OTk5OTk5IiBkeT0iMTQuMyI+66y47KCc66W8IOuquyDtkog8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJDQVBUQ0hBIiBkYXRhLXRvPSJBTExPVyIgZGF0YS1sYWJlbD0i7Y287KaQIO2GteqzvArsnpDsl7DsiqTrn6zsmrQg66eI7Jqw7IqkIOq2pOyggSI+CiAgPHJlY3QgeD0iNzM3LjA5OCIgeT0iMjMxLjQzMDY2NjY2NjY2NjY3IiB3aWR0aD0iMTQwLjAxNCIgaGVpZ2h0PSI0NC42IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjgwNy4xMDUiIHk9IjI1My43MzA2NjY2NjY2NjY2OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSI+PHRzcGFuIHg9IjgwNy4xMDUiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij7tjbzsppAg7Ya16rO8PC90c3Bhbj48dHNwYW4geD0iODA3LjEwNSIgZHk9IjE0LjMiPuyekOyXsOyKpOufrOyatCDrp4jsmrDsiqQg6rak7KCBPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkhVTUFOIiBkYXRhLWxhYmVsPSLsp4Tsp5wg7IKs656MIPCfp5EiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTAyLjY4Mjk5OTk5OTk5OTk5IiB5PSIyMzAuMDQ4IiB3aWR0aD0iMTIwLjQ5NjAwMDAwMDAwMDAxIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNjIuOTMwOTk5OTk5OTk5OTgiIHk9IjI0OC40OTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuynhOynnCDsgqzrnowg8J+nkTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iV0VCIiBkYXRhLWxhYmVsPSLroZzqt7jsnbgg7Iuc64+EIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjI3MS4xNzkiIHk9IjE5My4zNzMiIHdpZHRoPSIxMTguMjczIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzMwLjMxNTUiIHk9IjIxMS44MjI5OTk5OTk5OTk5OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+66Gc6re47J24IOyLnOuPhDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQk9UIiBkYXRhLWxhYmVsPSLtlbTsu6TsnZgg66ek7YGs66GcIOu0hyDwn5G+CuustOywqOuzhCDroZzqt7jsnbgg6rO16rKpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIxNDguMjQ4IiB3aWR0aD0iMTY3LjE3OSIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxMzkuNTg5NSIgeT0iMTc1LjE0OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTM5LjU4OTUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7tlbTsu6TsnZgg66ek7YGs66GcIOu0hyDwn5G+PC90c3Bhbj48dHNwYW4geD0iMTM5LjU4OTUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuustOywqOuzhCDroZzqt7jsnbgg6rO16rKpPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkNBUFRDSEEiIGRhdGEtbGFiZWw9IkNBUFRDSEEg66y47KeA6riwIPCfm6HvuI8KJnF1b3Q764u57Iug7J20IOyCrOuejOyehOydhCDspp3rqoXtlZjsi5zsmKQmcXVvdDsiIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iNTY1LjI3NSw4My45OTk5OTk5OTk5OTk5OSA2OTMuMDk4LDIxMS44MjI5OTk5OTk5OTk5OCA1NjUuMjc1LDMzOS42NDU5OTk5OTk5OTk5NiA0MzcuNDUyLDIxMS44MjI5OTk5OTk5OTk5OCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI1NjUuMjc1IiB5PSIyMTEuODIyOTk5OTk5OTk5OTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjU2NS4yNzUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5DQVBUQ0hBIOusuOyngOq4sCDwn5uh77iPPC90c3Bhbj48dHNwYW4geD0iNTY1LjI3NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+JnF1b3Q764u57Iug7J20IOyCrOuejOyehOydhCDspp3rqoXtlZjsi5zsmKQmcXVvdDs8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iREVOWSIgZGF0YS1sYWJlbD0i67SHKEJvdCnsnLzroZwg7YyQ7KCVIOKdjArsoJHsho0g67CPIOuhnOq3uOyduCDssKjri6ghIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjkyMS4xMTIiIHk9IjE0Mi4zMTUzMzMzMzMzMzMzNCIgd2lkdGg9IjE3MC4xNDI5OTk5OTk5OTk5NyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTAwNi4xODM1IiB5PSIxNjkuMjE1MzMzMzMzMzMzMzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjEwMDYuMTgzNSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuu0hyhCb3Qp7Jy866GcIO2MkOyglSDinYw8L3RzcGFuPjx0c3BhbiB4PSIxMDA2LjE4MzUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuygkeyGjSDrsI8g66Gc6re47J24IOywqOuLqCE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQUxMT1ciIGRhdGEtbGFiZWw9IuyCrOuejOycvOuhnCDtjJDsoJUg8J+fogrsoJXsg4Eg7ISc67mE7IqkIOydtOyaqSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI5MjEuMTEyIiB5PSIyMjcuNTMwNjY2NjY2NjY2NjYiIHdpZHRoPSIxNTAuMTM2IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI5OTYuMTgiIHk9IjI1NC40MzA2NjY2NjY2NjY2NyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iOTk2LjE4IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7IKs656M7Jy866GcIO2MkOyglSDwn5+iPC90c3Bhbj48dHNwYW4geD0iOTk2LjE4IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7soJXsg4Eg7ISc67mE7IqkIOydtOyaqTwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 해커의 창과 방패의 대결: 캡차의 세대별 진화 과정 전격 해부 (3단 표)**

단순한 '텍스트 읽기'에서 점차 사용자를 귀찮게 하지 않는 \*\*'행위 기반(Invisible)'\*\*으로 진화하는 과정을 대조하는 것이 핵심입니다.

| **캡차의 진화 세대**                            | **제공하는 인증 방식 (어떻게 묻는가?)**                                                                                                                  | **한계점 및 해커의 우회 공격(창) 방식 🚨**                                                                                                    |
| :--------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| **1세대 (v1)** *(텍스트 캡차)*                  | **'찌그러진 글자나 숫자 읽기'.** 일부러 심하게 왜곡되거나 겹쳐진 알파벳/숫자 이미지를 보여주고, 그 값을 키보드로 똑같이 타이핑하게 만드는 가장 초창기 방식.                                               | **\[OCR 기술의 발달로 붕괴]** 초기 봇은 막았으나, 해커들이 머신러닝 기반의 **광학문자인식(OCR)** 알고리즘을 봇에 달아주면서 왜곡된 글자까지 다 읽어내어 무력화됨.                            |
| **2세대 (v2)** *(이미지 / 오디오 캡차)*            | **'특정 사물(신호등, 버스)이 있는 사진 고르기'.** 구글의 reCAPTCHA가 대표적. 9개의 분할된 사진을 주고 정답을 클릭하게 함. (시각장애인을 위한 오디오/음성 캡차도 함께 지원).                              | **\[AI 비전 기술의 발달과 유저의 극심한 피로]** 컴퓨터 비전(CNN) 딥러닝 기술이 발달하며 AI가 사진을 다 맞추기 시작함. 게다가 문제를 푸는 **사용자(사람)가 너무 귀찮아해서 UX(사용자 경험)가 최악**이 됨. |
| **3세대 (v3) 🚨** *(행위 기반 캡차 / Invisible)* | **'보이지 않는 백그라운드 AI 평가'.** 사용자에게 귀찮은 사진 퀴즈를 아예 안 냄. 유저가 페이지에 머문 시간, **'마우스 커서를 움직이는 궤적의 삐뚤삐뚤한 정도'**, 클릭 속도 등을 수집해 AI가 점수(Score)를 매겨 봇을 판단함. | **\[캡차 팜(CAPTCHA Farm)의 등장]** 봇으로 뚫기 힘들어지자, 해커들이 개발도상국의 저임금 노동자 수천 명을 고용해 **'사람이 직접 손으로 광클해서 캡차를 대신 풀어주는(휴먼 노동)'** 편법 공격을 시도함.  |

#### **IV. \[결론/제언] FIDO(생체 인증) 및 블록체인 DID와의 결합을 통한 Passwordless 시대**

* **(키워드 위주 2줄 마무리)** "AI의 발전으로 기계가 인간보다 캡차를 더 빨리 푸는 모순이 발생하고 있습니다. 향후 캡차 기술은 사용자에게 퀴즈를 강요하는 방식을 벗어나, 기기 자체의 고유 인증(FIDO 생체 인식)이나 제로 트러스트 기반의 사용자 평판 조회를 결합한 **'비밀번호 없는(Passwordless) 인증 생태계'의 보조적인 방어 수단으로 진화할 것입니다.**"
