### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (RAG의목적, 3세대진화) — 3~4줄
Ⅱ. Advanced RAG - 파이프라인개선 (본론①, 도식 1개 필수)
Ⅲ. Modular RAG - 레고블록화, 핵심 배점
Ⅳ. 2025~2026년동향 - Agentic RAG로의진화 및결론
```

포인트: 개요에서 \*\*"앞서다룬트랜스포머·Self-Attention은'주어진문맥안'에서만 관련성을계산했는데, RAG는 '모델이애초에모르는외부지식'을 실시간으로검색해 프롬프트에주입"\*\*하는 기법이라는 한줄로시작하면, 왜 RAG가 오늘의신경망시리즈의 실전응용편인지 드러납니다.

### Ⅱ. Advanced RAG — 파이프라인개선

| 개선기법                      | 내용                                                          |
| :------------------------ | :---------------------------------------------------------- |
| **쿼리확장**(QueryExpansion)  | 원래질문을 **여러버전으로확장**해 더많은관련정보검색                               |
| **다중검색**(Multi-Retrieval) | **여러번검색**을수행해 정보수집범위확대                                      |
| **재순위화**(Re-ranking)      | 검색된문서들을 **Cross-Encoder로다시평가**해 진짜관련성높은것만선별                 |
| **HyDE**(가상문서임베딩)         | LLM이 **가짜답변을먼저생성**한뒤 그답변을임베딩해검색— 답변끼리가 **질문-답변보다더가까운경향**을활용 |

→ 암기: **"질문을넓히고,여러번찾고,다시순위매기고,가짜답을만들어검색한다"** — 앞서다룬 \*\*"Bi-encoder(빠른1차검색)vsCross-encoder(정확한재랭킹)"\*\*처럼, Advanced RAG는 \*\*"Naive RAG의단순벡터유사도검색의한계"\*\*를 **여러정교한기법**으로 보완합니다.

### 도식화 제안

```
[Naive RAG]                    [Advanced RAG]
질문 → 벡터검색 → 상위K개 → 생성      질문 → 쿼리확장/HyDE → 다중검색
(단순,정확도한계)                        ↓
                                   재순위화(Cross-Encoder)
                                        ↓
                                   진짜관련문서만 선별 → 생성
```

### Ⅲ. Modular RAG — 레고블록화, 핵심 배점

**함정 방지: "모듈로나눈다"고만답하면절반. Advanced RAG와의근본적차이(선형파이프라인vs유연한구성)를 구체적으로보여줘야완성됩니다.**

| 항목                     | 내용                                                                                            |
| :--------------------- | :-------------------------------------------------------------------------------------------- |
| **핵심발상**(Advanced와의차이) | Advanced RAG가 \*\*"고정된순서의파이프라인을개선"\*\*했다면, Modular RAG는 **"인덱싱-검색-생성전체과정을 독립적이고교체가능한모듈로재구성"** |
| **유연한흐름제어**            | 조건에따라 **파이프라인자체를변경하거나분기처리**가능(예:질문유형에따라 다른검색전략선택)                                             |
| **멀티모달지원**             | 텍스트뿐아니라 **표,이미지등다양한데이터형태**를 처리하는 모듈설계                                                         |
| **비유**                 | **"레고블록처럼재구성가능한프레임워크"**— 각모듈을 독립적으로 개선·교체                                                     |

→ 암기: **"Advanced RAG는 정해진순서를더잘하게다듬은것,Modular RAG는 순서자체를상황에따라바꿀수있게 블록화한것"** — 앞서다룬 \*\*"MSA(마이크로서비스,서비스마다독립교체가능)"\*\*와 정확히같은철학이, RAG시스템설계에도 \*\*"모듈단위로독립적교체·확장"\*\*형태로 재현됩니다.

### 도식화 제안

```
[Advanced RAG - 개선된 선형파이프라인]
질문 → [쿼리확장] → [검색] → [재순위화] → [생성]
(순서고정,각단계를더잘하도록개선)

[Modular RAG - 레고블록]
        ┌─[검색모듈A]─┐
질문 → [라우팅] ┼─[검색모듈B]─┼→ [조건부생성모듈] → 답변
        └─[그래프탐색모듈]┘
(질문유형에따라 어떤모듈을,어떤순서로쓸지 동적으로결정)
```

### Ⅳ. 2025\~2026년동향 — Agentic RAG로의진화 및 결론

**함정 방지: "Modular RAG가최종형태"라고생각하면절반. 2025\~2026년 한단계더나아간Agentic RAG와, 2026년의현실적트렌드(하이브리드회귀)를 보여줘야완성됩니다.**

| 세대                          | 비유    | 특징                                                                  |
| :-------------------------- | :---- | :------------------------------------------------------------------ |
| **NaiveRAG**                | 자판기   | 버튼누르면결과나옴(단순)                                                       |
| **AdvancedRAG**             | 즉석요리사 | 주문받아,여러코너에서재료준비,깔끔하게플레이팅                                            |
| **Agentic RAG**(2025\~2026) | 수셰프   | **LLM이에이전트가되어 "검색결과가충분한지스스로판단"**,부족하면 **재검색,쿼리분해,다른데이터소스라우팅**까지자율수행 |

→ 앞서다룬 \*\*"트랜스포머의Self-Attention"\*\*이 \*\*"정적인문맥"\*\*만 봤다면, Agentic RAG는 **"LLM이능동적으로 검색전략자체를판단하고수정하는"** 동적제어루프입니다.

**2026년현실적트렌드**(핵심): 전문가전망에따르면 **"2025년은AgenticAI의해였지만, 2026년에는 Agentic AI와사전정의된워크플로우를결합한하이브리드모델로회귀할것"**— 이유는 \*\*"에이전트간조율복잡성(CoordinationComplexity),계산오버헤드,확장성한계"\*\*같은 **실전배포시의현실적문제** 때문입니다. RAG시장은 **2025년19.6억달러→2035년403억달러**로 성장전망되며, \*\*"가장단순한패턴으로 자기문제를해결하고 다음기능으로넘어가는팀"\*\*이 2026년성공할것으로 예측됩니다.

→ 암기: **"자율성(Agentic)이무조건좋은게아니라, 필요한복잡도만큼만 사전워크플로우와섞어쓰는게2026년의현실적선택"** — 앞서다룬 \*\*"MoE의조건부연산(필요한전문가만활성화)"\*\*과 유사하게, \*\*"RAG도필요한만큼만복잡하게설계하는것"\*\*이 최신교훈입니다.

### 도식화 제안

```
[RAG 진화 및 2026년 회귀]
Naive → Advanced → Modular → Agentic(2025)
(단순)   (파이프개선) (블록화)   (LLM이스스로판단)
                                    ↓
                          2026년: Agentic+사전워크플로우 하이브리드
                          (에이전트조율복잡성·비용문제로 순수Agentic에서 한발후퇴)
```

### 결론

Advanced RAG는 \*\*"Naive RAG의단순벡터검색을, 쿼리확장·재순위화·HyDE같은기법으로다듬은 개선된선형파이프라인"\*\*이고, Modular RAG는 \*\*"그파이프라인자체를 독립적으로교체·재구성가능한레고블록으로해체"\*\*한 것입니다 — 2025년 등장한 **Agentic RAG**는 이를 한단계더 발전시켜 \*\*"LLM이스스로검색전략을판단하고수정하는 자율제어루프"\*\*로 나아갔지만, 2026년현재는 \*\*"조율복잡성과비용문제로 사전워크플로우와의하이브리드로회귀"\*\*하는 것이 현실적트렌드입니다 — 이는 앞서다룬 \*\*"MoE의조건부연산"\*\*과 \*\*"MSA의모듈독립성"\*\*이 RAG설계에도 그대로적용된다는 것을 보여주며, 오늘하루의 신경망·LLM시리즈전체가 \*\*"이론에서출발해, 실제엔지니어링에서는복잡도와비용을고려한현실적선택이중요하다"\*\*는 결론으로 완결됩니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "챗GPT의 거짓말(환각)을 막기 위해 외부 사내 DB를 컨닝하게 만든 RAG(검색 증강 생성) 기술의 진화 단계다. 초기 단순(Naive) RAG가 엉뚱한 문서를 퍼와서 헛소리를 하는 한계를 극복하기 위해 두 가지 아키텍처가 등장했다. 첫째, **'Advanced RAG(고급 RAG)'**. 검색 전(Pre)에 떡진 질문을 다듬고(Query Rewriting), 검색 후(Post)에 가져온 문서의 퀄리티를 다시 평가해 줄 세우는(Re-ranking) '전후 처리 파이프라인'을 덧붙여 검색 품질을 극한으로 끌어올린 선형적 구조다. 둘째, **'Modular RAG(모듈형 RAG)'**. 현존하는 가장 진보된 아키텍처로, RAG의 모든 과정을 레고 블록(모듈)처럼 쪼개버렸다. 사용자 질문의 의도에 따라 검색 모듈, 외부 API(계산기) 모듈, 프롬프트 압축 모듈을 라우터가 런타임에 실시간으로 뗐다 붙였다 하며 동적인 파이프라인을 스스로 조립한다. 무한대의 유연성을 자랑하는 엔터프라이즈 AI의 절대 표준이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] Naive RAG의 한계와 LLM 파이프라인의 진화 개요**

* **정의:** 단순 검색 후 생성하는 Naive RAG의 '낮은 검색 정확도'와 '경직성'을 타파하기 위해, 데이터 파이프라인에 전처리/후처리 기술을 추가한 것이 **Advanced RAG**이며, 이를 아예 독립적인 기능 블록으로 해체하여 동적으로 조립하는 것이 **Modular RAG**임.
* **배경:** B2B 실무 환경에서는 사용자의 질문이 모호하고 문서가 방대하여, 단순히 Vector DB를 한 번 검색(Retrieve)하는 것만으로는 문맥 누락과 노이즈 폭발(환각)을 막을 수 없었기 때문.

#### **II. \[본론 1] (극단적 단순화 버전) 파이프라인 덧붙이기 vs 레고 블록 조립하기**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3ODEuODM5OTk5OTk5OTk5OSA2NzkuOTU5MDAwMDAwMDAwMSIgd2lkdGg9Ijc4MS44Mzk5OTk5OTk5OTk5IiBoZWlnaHQ9IjY3OS45NTkwMDAwMDAwMDAxIiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJSQUdfX19BZHZhbmNlZF92c19Nb2R1bGFyIiBkYXRhLWxhYmVsPSJSQUcg7Yyo65+s64uk7J6E7J2YIOynhO2ZlCAoQWR2YW5jZWQgdnMgTW9kdWxhcikiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjcwMS44Mzk5OTk5OTk5OTk5IiBoZWlnaHQ9IjU5OS45NTkwMDAwMDAwMDAxIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNzAxLjgzOTk5OTk5OTk5OTkiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5SQUcg7Yyo65+s64uk7J6E7J2YIOynhO2ZlCAoQWR2YW5jZWQgdnMgTW9kdWxhcik8L3RleHQ+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMV9BZHZhbmNlZF9SQUdfX18iIGRhdGEtbGFiZWw9IjEuIEFkdmFuY2VkIFJBRyAo7ISg7ZiVIOq1rOyhsOydmCDqsJXtmZQpIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSI2NjkuODM5OTk5OTk5OTk5OSIgaGVpZ2h0PSIxMTMuODAwMDAwMDAwMDAwMDEiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSI2NjkuODM5OTk5OTk5OTk5OSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjgiIHk9Ijk4IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjEuIEFkdmFuY2VkIFJBRyAo7ISg7ZiVIOq1rOyhsOydmCDqsJXtmZQpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMl9Nb2R1bGFyX1JBR19fX18iIGRhdGEtbGFiZWw9IjIuIE1vZHVsYXIgUkFHICjruYTshKDtmJUg64+Z7KCBIOyhsOumvSDwn5KvKSI+CiAgPHJlY3QgeD0iNTYiIHk9IjIxNy44IiB3aWR0aD0iNDczLjYzOSIgaGVpZ2h0PSI0MDYuMTU5IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNTYiIHk9IjIxNy44IiB3aWR0aD0iNDczLjYzOSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjgiIHk9IjIzMS44IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjIuIE1vZHVsYXIgUkFHICjruYTshKDtmJUg64+Z7KCBIOyhsOumvSDwn5KvKTwvdGV4dD4KPC9nPgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBMSIgZGF0YS10bz0iQTIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTkwLjI3MywxNTQuOSAyMzguMjczLDE1NC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBMiIgZGF0YS10bz0iQTMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzU2LjU0NiwxNTQuOSA0MDQuNTQ2LDE1NC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBMyIgZGF0YS10bz0iQTQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNTU5LjEyNzk5OTk5OTk5OTksMTU0LjkgNjA3LjEyNzk5OTk5OTk5OTksMTU0LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlEiIGRhdGEtdG89IlJPVVRFUiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0MjUuNDU5NSwyOTguNzAwMDAwMDAwMDAwMDUgNDI1LjQ1OTUsMzQ2LjcwMDAwMDAwMDAwMDA1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJST1VURVIiIGRhdGEtdG89Ik0xIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0MjUuNDU5NSw1MjMuMDU5MDAwMDAwMDAwMSA0MjUuNDU5NSw1NzEuMDU5IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209Ik0yIiBkYXRhLXRvPSJNNCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyMzguODc3NSwyOTguNzAwMDAwMDAwMDAwMDUgMjM4Ljg3NzUsMzQ2LjcwMDAwMDAwMDAwMDA1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJNNCIgZGF0YS10bz0iTCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyMzguODc3NSwzODMuNiAyMzguODc3NSw0MDcuNiAxNzAuNTU3NSw0MDcuNiAxNzAuNTU3NSw0MzEuNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTTMiIGRhdGEtdG89IkwiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTAyLjIzNzUsMzgzLjYgMTAyLjIzNzUsNDA3LjYgMTcwLjU1NzUsNDA3LjYgMTcwLjU1NzUsNDMxLjYiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkExIiBkYXRhLWxhYmVsPSJQcmUt6rKA7IOJCuyniOusuCDsnqzsnpHshLEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNzIiIHk9IjEyOCIgd2lkdGg9IjExOC4yNzMiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEzMS4xMzY1IiB5PSIxNTQuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTMxLjEzNjUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5QcmUt6rKA7IOJPC90c3Bhbj48dHNwYW4geD0iMTMxLjEzNjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyniOusuCDsnqzsnpHshLE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQTIiIGRhdGEtbGFiZWw9IlZlY3RvciBEQgrsnKDsgqzrj4Qg6rKA7IOJIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjIzOC4yNzMiIHk9IjEyOCIgd2lkdGg9IjExOC4yNzMiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI5Ny40MDk1IiB5PSIxNTQuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMjk3LjQwOTUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5WZWN0b3IgREI8L3RzcGFuPjx0c3BhbiB4PSIyOTcuNDA5NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7Jyg7IKs64+EIOqygOyDiTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBMyIgZGF0YS1sYWJlbD0iUG9zdC3qsoDsg4kKUmUtcmFua2luZyDsnqzsoJXroKwiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDA0LjU0NiIgeT0iMTI4IiB3aWR0aD0iMTU0LjU4MiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDgxLjgzNyIgeT0iMTU0LjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjQ4MS44MzciIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5Qb3N0LeqygOyDiTwvdHNwYW4+PHRzcGFuIHg9IjQ4MS44MzciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPlJlLXJhbmtpbmcg7J6s7KCV66CsPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkE0IiBkYXRhLWxhYmVsPSJMTE0g7IOd7ISxIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjYwNy4xMjc5OTk5OTk5OTk5IiB5PSIxMzYuNDUiIHdpZHRoPSIxMDIuNzExOTk5OTk5OTk5OTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI2NTguNDgzOTk5OTk5OTk5OSIgeT0iMTU0Ljg5OTk5OTk5OTk5OTk4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5MTE0g7IOd7ISxPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJRIiBkYXRhLWxhYmVsPSLsgqzsmqnsnpAg7KeI66y4IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM2Ni4zMjMiIHk9IjI2MS44IiB3aWR0aD0iMTE4LjI3MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQyNS40NTk1IiB5PSIyODAuMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyCrOyaqeyekCDsp4jrrLg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJPVVRFUiIgZGF0YS1sYWJlbD0i4pyoIOudvOyasO2EsCDrqqjrk4gg4pyoCuyWtOuWpCDruJTroZ0g7JO46rmMPyIgZGF0YS1zaGFwZT0iZGlhbW9uZCI+CiAgPHBvbHlnb24gcG9pbnRzPSI0MjUuNDU5NSwzNDYuNzAwMDAwMDAwMDAwMDUgNTEzLjYzOSw0MzQuODc5NTAwMDAwMDAwMDYgNDI1LjQ1OTUsNTIzLjA1OTAwMDAwMDAwMDEgMzM3LjI4LDQzNC44Nzk1MDAwMDAwMDAwNiIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0MjUuNDU5NSIgeT0iNDM0Ljg3OTUwMDAwMDAwMDA2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0MjUuNDU5NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuKcqCDrnbzsmrDthLAg66qo65OIIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjQyNS40NTk1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7slrTrlqQg67iU66GdIOyTuOq5jD88L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTTEiIGRhdGEtbGFiZWw9IuybuSDqsoDsg4kg66qo65OIIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM2NS4yMTE1IiB5PSI1NzEuMDU5IiB3aWR0aD0iMTIwLjQ5NTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDI1LjQ1OTUiIHk9IjU4OS41MDkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuybuSDqsoDsg4kg66qo65OIPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJNMiIgZGF0YS1sYWJlbD0iTTIiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjA4LjY0MDAwMDAwMDAwMDAxIiB5PSIyNjEuOCIgd2lkdGg9IjYwLjQ3NDk5OTk5OTk5OTk5NCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIyMzguODc3NSIgeT0iMjgwLjI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5NMjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTTQiIGRhdGEtbGFiZWw9IlJlLXJhbmtpbmcg66qo65OIIOKaoSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxNjAuNDc1IiB5PSIzNDYuNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSIxNTYuODA1IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjIzOC44Nzc1IiB5PSIzNjUuMTUwMDAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlJlLXJhbmtpbmcg66qo65OIIOKaoTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTCIgZGF0YS1sYWJlbD0iTExNIOyDneyEsSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMTkuMjAxNTAwMDAwMDAwMDEiIHk9IjQzMS42IiB3aWR0aD0iMTAyLjcxMTk5OTk5OTk5OTk5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTcwLjU1NzUiIHk9IjQ1MC4wNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+TExNIOyDneyEsTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTTMiIGRhdGEtbGFiZWw9Ik0zIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjcyIiB5PSIzNDYuNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSI2MC40NzQ5OTk5OTk5OTk5OTQiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTAyLjIzNzUiIHk9IjM2NS4xNTAwMDAwMDAwMDAwMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+TTM8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] Advanced RAG vs Modular RAG 핵심 아키텍처 전격 대조 (3단 표)**

이 토픽은 Advanced의 'Pre/Post 처리 메커니즘'과 Modular의 '다이내믹한 라우팅(동적 구성)'을 극명하게 대조하는 것이 완벽한 득점 포인트입니다.

| **핵심 척도**               | **🛠️ Advanced RAG (전후처리 강화) 🚨**                                                                                                                                                   | **🧩 Modular RAG (레고 블록 조립) 🚨**                                                                                                                      |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **개념 / 아키텍처**           | **'선형적 파이프라인의 고도화'.** 검색과 생성이라는 기존 파이프라인의 앞뒤에 성능 최적화 단계를 추가로 끼워 넣은 일방통행(단방향) 확장형 구조.                                                                                                | **'비선형적/동적 유연성 💯'.** RAG의 기능들을 독립된 모듈로 쪼개어 놓고, 질문의 성격에 따라 런타임에 필요한 모듈만 선택해서 워크플로우를 자유롭게 재구성함.                                                        |
| **핵심 메커니즘 (출제 포인트) 🚨** | **\[Pre-retrieval (검색 전)]** 사용자의 모호한 질문을 쪼개고 검색하기 좋게 재생성(Query Rewriting)함. **\[Post-retrieval (검색 후) 💯]** 검색해 온 수십 개의 문서 중 찌꺼기를 버리고 엑기스만 다시 줄 세우는 \*\*'Re-ranking(재랭킹)'\*\*을 수행함. | **\[라우팅 (Routing) 💯]** 질문이 수학 문제면 '계산기 모듈'을, 회사 규정이면 '내부 DB 검색 모듈'을 타도록 트래픽을 분기함. **\[기능적 모듈화]** 검색, 메모리, 검증, 프롬프트 압축 등이 모두 별개의 플러그인(Plug-in)처럼 동작함. |
| **장점 / 유연성 🚨**         | 엉뚱한 문서를 긁어오는 문제를 획기적으로 줄여 답변의 정확도가 매우 높아짐. (구현 난이도 중간).                                                                                                                             | 특정 태스크에 맞춰 파이프라인을 무한대로 커스텀 확장할 수 있어, 랭체인(LangChain) 기반 **엔터프라이즈 AI 에이전트(Agent) 구축의 핵심 표준이 됨.**                                                        |

#### **IV. \[결론/제언] DSPy와 GraphRAG를 통한 패러다임의 완성**

* **(키워드 위주 2줄 마무리)** "Modular RAG를 통해 아키텍처의 유연성은 확보되었으나, 어떤 모듈을 어떻게 조합할지 파라미터를 세팅하는 것은 여전히 인간의 노가다입니다. 최근에는 이를 극복하기 위해 모듈 파이프라인 자체를 스스로 최적화(컴파일)하는 프레임워크인 \*\*'DSPy'\*\*와, 점과 선의 연결 관계를 학습해 지식 추론을 극대화하는 **'GraphRAG'가 융합되며 RAG 기술의 SOTA(State-of-The-Art)를 갱신하고 있습니다.**"
