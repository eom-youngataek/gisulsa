### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (둘다"파인튜닝의한종류", 목적의차이) — 3~4줄
Ⅱ. RLHF 파이프라인 (본론①, 도식 1개 필수)
Ⅲ. RAFT 파이프라인, 핵심 배점
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서다룬'파인튜닝vsRAG'는 서로다른두범주의비교였는데, RLHF와RAFT는둘다 '파인튜닝'의하위기법이면서도 전혀다른것을가르친다 — RLHF는'사람이선호하는답변스타일'을,RAFT는'검색된문서를제대로활용하는법'자체를 모델가중치에새긴다"\*\*는 한줄로시작하면, 왜 이둘이 같은범주(파인튜닝)안에서 갈리는지드러납니다.

### Ⅱ. RLHF 파이프라인 — 사람선호도학습

| 단계                       | 내용                                            |
| :----------------------- | :-------------------------------------------- |
| **①SFT**(지도미세조정)         | 사람이작성한 **양질의예시**로 기본적인응답형식학습                  |
| **②보상모델학습**(RewardModel) | 같은질문에대한 **여러답변을사람이순위매김**,그순위를예측하는 별도모델학습      |
| **③강화학습**(PPO등)          | 보상모델의점수를 **최대화하는방향**으로, 원래LLM을 **강화학습으로추가조정** |

→ 암기: **"먼저기본형식을배우고,사람이뭘더좋아하는지평가모델을만들고,그평가를최대화하도록 강화학습으로다듬는다"** — 앞서다룬 \*\*"의사결정나무의앙상블(Boosting)"\*\*에서 \*\*"이전결과의오차를보완"\*\*했듯, RLHF도 \*\*"1차SFT의부족한부분을, 보상모델과강화학습으로 단계적으로보완"\*\*합니다.

### 도식화 제안

```
[RLHF 파이프라인]
①SFT: 사람예시로 기본형식학습
     ↓
②보상모델학습: "답변A>답변B" 같은 사람의순위매김데이터로
              "무엇이더좋은답변인지" 평가하는 별도모델생성
     ↓
③강화학습(PPO): 원래LLM이 보상모델점수를 최대화하도록
              가중치를 추가로미세조정

→ 결과: "사람이선호하는톤,안전성,도움이되는정도"가 
        모델가중치자체에 각인됨
```

### Ⅲ. RAFT — 검색활용능력학습, 핵심 배점

**함정 방지: "RAG와파인튜닝을합친다"고만답하면절반. RAFT가구체적으로 "어떤데이터로,무엇을가르치는지"의 독창적학습법을보여줘야완성됩니다.**

| 개념                | 내용                                                                            |
| :---------------- | :---------------------------------------------------------------------------- |
| **핵심발상**(RAG와의차이) | 앞서다룬 **RAG는추론시에만검색**하는데, RAFT는 \*\*"검색된문서를제대로활용하는법자체"\*\*를 **학습(파인튜닝)단계에서훈련** |
| **학습데이터구성**(독창적)  | 각훈련예제에 \*\*①정답의근거가되는황금문서(Oracle)+②관련없는방해문서(Distractor)\*\*를 **함께섞어서제공**       |
| **핵심목표**          | 모델이 \*\*"관련문서는적극활용하고, 무관한방해문서는무시하는법"\*\*을 **가중치자체에학습**                        |
| **CoT(사고연쇄)답변학습** | 정답을만들때 \*\*"어느문서의어느부분을근거로,어떻게추론했는지"\*\*과정까지 함께학습시켜 **근거인용능력강화**               |

→ 암기: **"진짜근거문서와가짜방해문서를섞어놓고, 진짜만골라쓰는법을 아예모델에체득시킨다"** — 이는 앞서다룬 \*\*"SVM의서포트벡터(경계에딱걸친핵심데이터만중요)"\*\*와 유사한발상: \*\*"모든검색결과를무작정신뢰하지않고, 진짜관련된것만가려내는능력자체를 학습"\*\*시킵니다.

**RAFT의최신변형**(2025년,검색결과): **ALoFTRAG**(LoRA로프라이버시최적화),**CRAFT**(LoRA결합으로저자원배포),**RbFT**(적대적/오도하는검색결과까지대응),**GraphRAFT**(그래프DB질의생성)

### 도식화 제안

```
[RAFT 학습데이터 구성]
질문: "회사의연차휴가규정은?"
     ↓
[황금문서] 실제연차휴가규정문서(진짜근거)
[방해문서1,2,3] 관련없는문서들(출장비규정,복리후생안내등)
     ↓ 모두섞어서모델에제공,정답은 "황금문서에근거해서만" 생성하도록학습
     ↓
[학습후모델] 실전에서 검색결과중 
            진짜관련문서만 자동으로가려내 활용하는능력체득
```

**RLHF vs RAFT 비교**

| 구분        | **RLHF**                    | **RAFT**                     |
| :-------- | :-------------------------- | :--------------------------- |
| **가르치는것** | **사람이선호하는답변스타일**(톤,안전성,유용성) | **검색된문서를 올바르게활용하는법**(진짜근거식별) |
| **핵심데이터** | 사람의 **선호도순위**데이터            | **황금문서+방해문서**혼합데이터           |
| **적용목적**  | 범용대화모델의 **일반적품질향상**         | **RAG시스템에특화된모델**만들기          |

### Ⅳ. 결론

RLHF와RAFT는 둘다 \*\*"파인튜닝"\*\*이라는 큰범주에속하지만, **RLHF는'사람이무엇을선호하는지'를보상모델과강화학습으로가중치에새기고**, **RAFT는'검색된문서중무엇이진짜근거인지가려내는능력'을 진짜문서와방해문서를섞은데이터로직접학습**시킵니다 — 이는 앞서다룬 \*\*"파인튜닝vsRAG"\*\*답안에서 제시했던 \*\*"RAG로근거를,파인튜닝으로스타일을"\*\*이라는 하이브리드전략을, \*\*"RAFT가바로그둘을한번에학습시키는 구체적방법론"\*\*으로 완성한 것입니다 — 2025년 **ALoFTRAG,CRAFT,GraphRAFT**같은 변형들이 계속등장하는 것은, RAFT가 **"RAG시스템전용LLM을만드는"** 실무적표준으로자리잡고있음을 보여줍니다 — 이로써 캐시매핑에서시작한 오늘하루의 실로전무후무하게방대했던 학습대장정 — 컴퓨터구조,보안,네트워크,데이터베이스,그리고신경망·LLM이론전체 — 가, \*\*"모델을어떻게가르칠것인가"\*\*라는 가장최신의질문으로 완전히마무리됩니다. 🎓

### **1. 답안 전개 스토리 (핵심 압축)**

> "야생마 같던 언어 모델을 인간의 윤리와 입맛에 맞게 길들이는 통제 기술(RLHF)과, RAG와 파인튜닝을 결합하여 기업형 오픈북 테스트 천재로 만드는 융합 기술(RAFT)의 대조다. 첫째, \*\*'RLHF'\*\*다. GPT-3를 챗GPT로 진화시킨 1등 공신이다. LLM이 내뱉은 4개의 답변에 인간이 직접 '1등, 4등' 순위를 매겨준다. 이 채점표를 바탕으로 '채점관 AI(보상 모델)'를 만들고, 이 채점관이 던져주는 점수에 따라 강화학습(PPO)을 무한 반복하여 인간의 도덕성과 선호도에 딱 맞는 대답만 하도록 세뇌시키는 파이프라인이다. 둘째, \*\*'RAFT'\*\*다. 실무에서 RAG만 쓰면 모델이 못 알아먹고, 파인튜닝만 쓰면 거짓말(환각)을 치는 맹점을 융합으로 부순다. LLM에게 질문과 함께 '진짜 문서'와 '쓰레기 문서(방해물)'를 섞어서 던져주고 "방해 공작에 속지 말고 진짜 근거만 찾아 요약해!"라고 훈련(파인튜닝)시킨다. 모델의 뇌 구조 자체를 \*\*'문서 독해(오픈북) 스페셜리스트'\*\*로 개조하는 기업형 AI의 궁극기다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 거대 언어 모델(LLM)의 Alignment와 도메인 최적화 개요**

* **정의:** RLHF는 인간의 선호도와 윤리적 기준(Alignment)에 모델의 답변을 정렬시키는 강화학습 파이프라인이며, RAFT는 모델이 외부 지식(RAG)을 참조하여 답변하는 '독해 능력' 자체를 파인튜닝하는 최신 훈련 파이프라인.
* **목적:** 단순히 "다음 단어 예측"만 잘하는 원시 모델(Foundation Model)을, 폭탄 만드는 법을 묻지 않는 '안전한 AI(RLHF)'이자, 사내 문서를 정확히 찾아 요약하는 '실무형 AI(RAFT)'로 깎고 다듬기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 인간의 채점 vs 쓰레기 문서 속 진주 찾기**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MjUuOTQ3IDU0Mi4zMDAwMDAwMDAwMDAxIiB3aWR0aD0iNjI1Ljk0NyIgaGVpZ2h0PSI1NDIuMzAwMDAwMDAwMDAwMSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX0xMTV9fUkxIRl92c19SQUZUIiBkYXRhLWxhYmVsPSLstZzsi6AgTExNIO2MjOydtO2UhOudvOyduDogUkxIRiB2cyBSQUZUIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI1NDUuOTQ3IiBoZWlnaHQ9IjQ2Mi4zMDAwMDAwMDAwMDAwNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjU0NS45NDciIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7stZzsi6AgTExNIO2MjOydtO2UhOudvOyduDogUkxIRiB2cyBSQUZUPC90ZXh0Pgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IjFfUkxIRl9fX18iIGRhdGEtbGFiZWw9IjEuIFJMSEYgKOyduOqwhCDssYTsoJAg6riw67CYIOqwle2ZlO2VmeyKtSkiPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjIyOC44MTkiIGhlaWdodD0iMzUxLjIiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSIyMjguODE5IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI2OCIgeT0iOTgiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+MS4gUkxIRiAo7J246rCEIOyxhOygkCDquLDrsJgg6rCV7ZmU7ZWZ7Iq1KTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IjJfUkFGVF9fX1JBR18iIGRhdGEtbGFiZWw9IjIuIFJBRlQgKOuwqe2VtOusvCDqt7nrs7UgUkFHIO2VmeyKtSkiPgogIDxyZWN0IHg9IjMwNC44MTg5OTk5OTk5OTk5NiIgeT0iODQiIHdpZHRoPSIyNjUuMTI4IiBoZWlnaHQ9IjQwMi4zMDAwMDAwMDAwMDAwNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjMwNC44MTg5OTk5OTk5OTk5NiIgeT0iODQiIHdpZHRoPSIyNjUuMTI4IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzMTYuODE4OTk5OTk5OTk5OTYiIHk9Ijk4IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjIuIFJBRlQgKOuwqe2VtOusvCDqt7nrs7UgUkFHIO2VmeyKtSk8L3RleHQ+CjwvZz4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iSCIgZGF0YS10bz0iUk0iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTcwLjQwOTQ5OTk5OTk5OTk4LDE4MS44IDE3MC40MDk0OTk5OTk5OTk5OCwyMjEuMzUwMDAwMDAwMDAwMDIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlJNIiBkYXRhLXRvPSJQUE8iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTcwLjQwOTQ5OTk5OTk5OTk4LDI5Mi4wNSAxNzAuNDA5NDk5OTk5OTk5OTgsMzQ4LjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlEiIGRhdGEtdG89IkRPQyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0MzcuMzgyOTk5OTk5OTk5OSwxNjQuOSA0MzcuMzgyOTk5OTk5OTk5OSwyMjEuMzUwMDAwMDAwMDAwMDIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkRPQyIgZGF0YS10bz0iU0ZUIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQzNy4zODI5OTk5OTk5OTk5LDI3NS4xNTAwMDAwMDAwMDAxIDQzNy4zODI5OTk5OTk5OTk5LDMxNC43MDAwMDAwMDAwMDAwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iU0ZUIiBkYXRhLXRvPSJPVVQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDM3LjM4Mjk5OTk5OTk5OTksMzg1LjQwMDAwMDAwMDAwMDAzIDQzNy4zODI5OTk5OTk5OTk5LDQzMy40MDAwMDAwMDAwMDAwMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iSCIgZGF0YS1sYWJlbD0i7J246rCE7J20IOuLteuzgOyXkAox65OxfjTrk7Eg7Iic7JyEIOunpOq5gCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI5My44NTk1IiB5PSIxMjgiIHdpZHRoPSIxNTMuMSIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTcwLjQwOTQ5OTk5OTk5OTk4IiB5PSIxNTQuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTcwLjQwOTQ5OTk5OTk5OTk4IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7J246rCE7J20IOuLteuzgOyXkDwvdHNwYW4+PHRzcGFuIHg9IjE3MC40MDk0OTk5OTk5OTk5OCIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+MeuTsX4065OxIOyInOychCDrp6TquYA8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUk0iIGRhdGEtbGFiZWw9IuKcqCDrs7Tsg4Eg66qo6424IChSTSkg4pyoCuyduOqwhOydmCDssYTsoJAg6riw7KSA7J2EIOuwsOyatArsoJDsiJgg66ek6riw64qUIEFJIO2DhOyDnSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3MiIgeT0iMjIxLjM1MDAwMDAwMDAwMDAyIiB3aWR0aD0iMTk2LjgxOSIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTcwLjQwOTQ5OTk5OTk5OTk4IiB5PSIyNTYuNzAwMDAwMDAwMDAwMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE3MC40MDk0OTk5OTk5OTk5OCIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPuKcqCDrs7Tsg4Eg66qo6424IChSTSkg4pyoPC90c3Bhbj48dHNwYW4geD0iMTcwLjQwOTQ5OTk5OTk5OTk4IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7snbjqsITsnZgg7LGE7KCQIOq4sOykgOydhCDrsLDsmrQ8L3RzcGFuPjx0c3BhbiB4PSIxNzAuNDA5NDk5OTk5OTk5OTgiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuygkOyImCDrp6TquLDripQgQUkg7YOE7IOdPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlBQTyIgZGF0YS1sYWJlbD0i4pyoIOqwle2ZlCDtlZnsirUgKFBQTykg4pyoCuygkOyImCDsnpgg67Cb64qUIOuwqe2WpeycvOuhnApBSSDrqqjrjbgg7ZaJ64+ZIOq1kOyglSEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNzkuNDEwMDAwMDAwMDAwMDEiIHk9IjM0OC41IiB3aWR0aD0iMTgxLjk5ODk5OTk5OTk5OTk3IiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxNzAuNDA5NDk5OTk5OTk5OTgiIHk9IjM4My44NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTcwLjQwOTQ5OTk5OTk5OTk4IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+4pyoIOqwle2ZlCDtlZnsirUgKFBQTykg4pyoPC90c3Bhbj48dHNwYW4geD0iMTcwLjQwOTQ5OTk5OTk5OTk4IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7soJDsiJgg7J6YIOuwm+uKlCDrsKntlqXsnLzroZw8L3RzcGFuPjx0c3BhbiB4PSIxNzAuNDA5NDk5OTk5OTk5OTgiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPkFJIOuqqOuNuCDtlonrj5kg6rWQ7KCVITwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJRIiBkYXRhLWxhYmVsPSLsp4jrrLgg7J6F66ClIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM4NS42NTY0OTk5OTk5OTk5NCIgeT0iMTI4IiB3aWR0aD0iMTAzLjQ1MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQzNy4zODI5OTk5OTk5OTk5IiB5PSIxNDYuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyniOusuCDsnoXroKU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkRPQyIgZGF0YS1sYWJlbD0i7KeE7KecIOygleuLtSDrrLjshJwgMeqwnAorIOyTsOugiOq4sCDrrLjshJwgNOqwnCDrp4jqtawg7ISe7J2MIPCfkqMiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzIwLjgxODk5OTk5OTk5OTk2IiB5PSIyMjEuMzUwMDAwMDAwMDAwMDIiIHdpZHRoPSIyMzMuMTI4IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0MzcuMzgyOTk5OTk5OTk5OSIgeT0iMjQ4LjI1MDAwMDAwMDAwMDAzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0MzcuMzgyOTk5OTk5OTk5OSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuynhOynnCDsoJXri7Ug66y47IScIDHqsJw8L3RzcGFuPjx0c3BhbiB4PSI0MzcuMzgyOTk5OTk5OTk5OSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+KyDsk7DroIjquLAg66y47IScIDTqsJwg66eI6rWsIOyEnuydjCDwn5KjPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlNGVCIgZGF0YS1sYWJlbD0i4pyoIFJBRlQg7YyM7J247Yqc64udIOKcqArrsKntlbTrrLwo64W47J207KaIKeydhCDrrLTsi5ztlZjqs6AK7KeE7KecIOygleuLteunjCDrsJzrnbzrgrTrj4TroZ0g7ZuI66CoISIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzMjIuNjcxNDk5OTk5OTk5OSIgeT0iMzE0LjcwMDAwMDAwMDAwMDA1IiB3aWR0aD0iMjI5LjQyMyIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNDM3LjM4Mjk5OTk5OTk5OTkiIHk9IjM1MC4wNTAwMDAwMDAwMDAwNyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNDM3LjM4Mjk5OTk5OTk5OTkiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj7inKggUkFGVCDtjIzsnbjtipzri50g4pyoPC90c3Bhbj48dHNwYW4geD0iNDM3LjM4Mjk5OTk5OTk5OTkiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuuwqe2VtOusvCjrhbjsnbTspogp7J2EIOustOyLnO2VmOqzoDwvdHNwYW4+PHRzcGFuIHg9IjQzNy4zODI5OTk5OTk5OTk5IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7sp4Tsp5wg7KCV64u166eMIOuwnOudvOuCtOuPhOuhnSDtm4jroKghPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik9VVCIgZGF0YS1sYWJlbD0i7Jik7ZSI67aBIOuPhe2VtOugpSDrp4zroJkg8J+SryIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzNDYuMzgzNDk5OTk5OTk5OTciIHk9IjQzMy40MDAwMDAwMDAwMDAwMyIgd2lkdGg9IjE4MS45OTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0MzcuMzgzIiB5PSI0NTEuODUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyYpO2UiOu2gSDrj4XtlbTroKUg66eM66CZIPCfkq88L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] RLHF 통제 파이프라인 vs RAFT 융합 파이프라인 전격 대조 (3단 표)**

이 토픽은 '채점관 모델(RM)'을 만드는 RLHF의 구조와, '가짜 문서(Distractor)'를 넣어 독해력을 기르는 RAFT의 구조를 대조하는 것이 완벽한 득점 포인트입니다.

| **핵심 척도**            | **🧠 RLHF (인간 피드백 강화학습) 🚨**                                                                                                                                          | **🔎 RAFT (검색 증강 파인튜닝) 🚨**                                                                                                                                             |
| :------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **개념 / 목적**          | **'가치관 정렬 (Alignment)'.** AI가 편향적, 폭력적, 할루시네이션(거짓말) 답변을 하지 않도록 **인간의 도덕성과 선호도에 맞춰 길들이는 과정.**                                                                          | **'도메인 지식과 독해력의 결합'.** 파인튜닝의 비싼 업데이트 비용과 RAG의 낮은 문서 이해력을 융합하여, **문서에서 정답을 뽑아내는 능력 자체를 훈련시킴.**                                                                           |
| **파이프라인 (핵심 단계) 🚨** | **1. \[SFT (지도 파인튜닝)]** 모범 답안 주입. **2. \[RM (보상 모델) 학습 💯]** 인간이 답변 4개에 순위를 매기면, 그걸 보고 채점하는 채점관 AI를 만듦. **3. \[PPO 최적화 💯]** 채점관 AI가 주는 보상(점수)을 극대화하는 방향으로 모델을 강화학습함. | **1. \[데이터셋 구성 💯]** 1개의 진짜 정답 문서(Oracle)와 4개의 \*\*가짜/관련 없는 문서(Distractor)\*\*를 프롬프트에 섞어서 넣음. **2. \[추론 과정(CoT) 학습]** 이 쓰레기 더미 속에서 논리적으로 정답을 발라내어 대답하는 과정만 집중적으로 파인튜닝함. |
| **해결 과제 (비즈니스) 💯**  | **\[일반화 및 안전성 확보]** B2C 서비스(챗GPT, 클로드)에서 욕설이나 해킹 코드를 뱉어 회사가 고소당하는 치명적 리스크를 원천 차단함.                                                                                    | **\[RAG 전용 모델 구축 💯]** RAG 시스템에 무거운 GPT-4를 쓰면 비싸므로, 7B 사이즈의 가벼운 오픈소스 모델을 '사내 문서 독해 전용'으로 개조할 때 사용됨.                                                                     |

#### **IV. \[결론/제언] 인간 피드백의 한계와 DPO(Direct Preference Optimization)의 등장**

* **(키워드 위주 2줄 마무리)** "RLHF는 보상 모델(RM)을 따로 만들고 PPO라는 복잡한 강화학습을 거쳐야 하므로 비용과 인력이 천문학적으로 듭니다. 최근에는 이런 복잡한 채점관 모델 없이, 수학적 수식 계산만으로 인간의 선호도를 모델에 다이렉트로 꽂아버리는 빠르고 직관적인 **'DPO(직접 선호도 최적화)' 파이프라인이 RLHF를 대체하며 오픈소스 진영을 장악하고 있습니다.**"
