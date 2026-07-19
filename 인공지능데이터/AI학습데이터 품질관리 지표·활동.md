### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (일반데이터품질과의차이, 왜AI학습데이터가특별한가) — 3~4줄
Ⅱ. 핵심품질지표5종 (본론①, 도식 1개 필수)
Ⅲ. 생애주기별품질관리활동, 핵심 배점
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서다룬데이터품질관리(11개오류진단기준)는 '값이맞는지'를 봤는데, AI학습데이터는 그것을넘어 '이데이터로학습한모델이 편향되거나,특정패턴만과도하게외우지는않는지'까지 봐야한다 — 앞서다룬귀납적사고와기계학습의한계(과적합,분포이동)가 여기서 학습데이터품질관리의핵심과제가된다"\*\*는 한줄로시작하면, 왜 AI학습데이터가 일반데이터품질관리와 다른차원인지드러납니다.

### Ⅱ. 핵심품질지표 5종

| 지표                    | 내용                                            |
| :-------------------- | :-------------------------------------------- |
| **정확성**(Accuracy)     | 라벨링이 **실제사실과일치**하는정도                          |
| **완전성**(Completeness) | 학습에 **필요한속성·클래스가누락없이**포함되는정도                  |
| **다양성**(Diversity)    | 앞서다룬 **AI윤리기준의③다양성존중**— 특정집단·패턴에 **편중되지않는정도** |
| **일관성**(Consistency)  | 같은유형의데이터가 **동일한기준으로라벨링**되는정도                  |
| **적시성**(Timeliness)   | 앞서다룬 \*\*"분포이동"\*\*대응 — 데이터가 **현재상황을반영**하는최신성 |

→ 암기: **"맞고,빠짐없고,치우치지않고,기준이일관되고,최신이어야한다"** — 앞서다룬 \*\*"AI윤리기준10대요건의③다양성존중"\*\*이 여기서 \*\*"학습데이터자체의다양성지표"\*\*로 구체적으로 측정가능한형태가 됩니다.

### 도식화 제안

```
[AI학습데이터 5대품질지표]
정확성: 라벨이실제와일치하는가?
완전성: 필요한클래스가 다있는가?
다양성: 특정집단에 치우치지않았는가? (편향방지)
일관성: 라벨링기준이 동일한가?
적시성: 최신상황을반영하는가? (분포이동대응)
```

### Ⅲ. 생애주기별품질관리활동 — 핵심 배점

**함정 방지: "지표를측정한다"고만답하면절반. 앞서다룬"수집전-수집중-학습후"각단계별로구체적으로무엇을하는지,그리고왜편향탐지가특히중요한지보여줘야완성됩니다.**

| 단계            | 활동                                                                           |
| :------------ | :--------------------------------------------------------------------------- |
| **수집전**       | **데이터소스다양화계획**수립 — 특정출처(예:특정연령대,특정지역)에만 의존하지않도록 **사전설계**                     |
| **수집·라벨링중**   | **라벨러간일치도검증**(Inter-annotatorAgreement) — 여러사람이 같은데이터를 라벨링했을때 **얼마나일치하는지**확인 |
| **학습전검증**(핵심) | **편향탐지**(BiasDetection)— 특정속성(성별,인종등)에 따라 **라벨분포가치우쳐있는지** 통계적으로검사            |
| **학습후검증**     | 앞서다룬 \*\*"혼동행렬"\*\*로 **집단별성능차이**확인— 특정집단에서만 유독 정확도가낮다면 **편향의증거**             |
| **배포후모니터링**   | 앞서다룬 **"MLOps의CT(ContinuousTraining)"**— **분포이동감지**시 데이터재수집                  |

→ 암기: **"모으기전에다양성을설계하고,라벨링할땐사람들끼리일치하는지보고,학습전엔편향을검사하고,학습후엔집단별성능차이를확인하고,배포후에도계속지켜본다"**

**편향탐지구체사례**(중요): 앞서다룬 \*\*"혼동행렬"\*\*을 **집단별로나눠서** 계산 — 예를들어 \*\*"남성지원자대상정확도90% vs 여성지원자대상정확도65%"\*\*라면, 이는 앞서다룬 \*\*"AI윤리기준의③다양성존중,인공지능기본법의채용분야고영향AI"\*\*에서 요구하는 \*\*"차별방지의무"\*\*를 **정량적으로위반**하는 명백한증거입니다.

### 도식화 제안

```
[생애주기별 품질관리 활동]
①수집전: 데이터소스 다양화계획
     ↓
②라벨링중: 라벨러간 일치도검증
     ↓
③학습전: 편향탐지(속성별라벨분포검사)
     ↓
④학습후: 혼동행렬을 "집단별로" 분리계산
     예: 남성정확도90% vs 여성정확도65% → 명백한편향!
     ↓
⑤배포후: MLOps CT로 분포이동 지속모니터링
```

**앞서다룬AI기본법과의연결**: 이런 \*\*"편향탐지,집단별성능검증"\*\*활동이 실제로는 앞서다룬 \*\*"인공지능기본법의고영향AI영향평가(제35조)"\*\*에서 요구하는 \*\*"영향받는자식별,관련기본권유형식별"\*\*의 **기술적실행수단**입니다 — 즉, **법이요구하는추상적의무를, 이런구체적지표·활동으로실제이행**하게됩니다.

### Ⅳ. 결론

### **1. 답안 전개 스토리 (핵심 압축)**

> "AI의 최종 성능은 100% '데이터 빨'이다. "쓰레기를 넣으면 쓰레기가 나온다(GIGO)"는 원칙에 따라, AI 학습용 데이터의 결함을 막고 성능 신뢰성을 확보하는 정량적 지표와 실무 관리 요령이다. 평가 지표는 세 가지가 핵심이다. 첫째, 데이터 포맷 규격이 깨지지 않았는지 확인하는 **'구문 정확성'**. 둘째, 이미지와 라벨링 꼬리표가 정확히 일치하는지 확인하는 **'의미 정확성'**. 셋째, 데이터 분포가 한쪽으로 쏠리지 않고 골고루 퍼졌는지 보는 \*\*'다양성'\*\*이다. 품질 활동은 데이터 수집-정제-가공-검수의 전 주기를 밀착 관리한다. 라벨링 작업자 간의 엇갈림을 막기 위해 깐깐한 가이드라인을 수립하고, 최종 검수 단계에서는 통계적 샘플링 검사 표준(KS Q ISO 2859-1)을 적용해 기계와 인간이 교차 검수를 진행하는 것이 실무 가이드라인의 정석이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 데이터 중심 AI(Data-Centric AI)의 핵심, 학습데이터 품질관리 개요**

* **정의:** 인공지능 모델 학습에 사용되는 원시 데이터 및 어노테이션(라벨링) 데이터의 정확성, 완전성, 일관성 등을 정량적으로 측정하고, 수집부터 검수까지의 주기별 프로세스를 모니터링하여 오류를 통제하는 활동.
* **목적:** 잘못 인코딩되거나 잘못 분류된 데이터 학습으로 인한 모델의 오작동 및 편향성을 예방하여 AI 시스템의 신뢰성과 안전성을 보장하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 수집에서 검수까지 이어지는 품질 보증 파이프라인**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1OTguNzMzIDIxMC43IiB3aWR0aD0iNTk4LjczMyIgaGVpZ2h0PSIyMTAuNyIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iQUlfX18iIGRhdGEtbGFiZWw9IkFJIO2VmeyKteuNsOydtO2EsCDtkojsp4jqtIDrpqwg65287J207ZSE7IKs7J207YG0Ij4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI1MTguNzMzIiBoZWlnaHQ9IjEzMC43IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNTE4LjczMyIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPkFJIO2VmeyKteuNsOydtO2EsCDtkojsp4jqtIDrpqwg65287J207ZSE7IKs7J207YG0PC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBIiBkYXRhLXRvPSJCIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjIxOC43MzMsMTE5LjM1IDI2Ni43MzMsMTE5LjM1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJCIiBkYXRhLXRvPSJDIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjMyNi43MzMsMTE5LjM1IDM3NC43MzMsMTE5LjM1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDIiBkYXRhLXRvPSJEIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQzNC43MzMsMTE5LjM1IDQ4Mi43MzMsMTE5LjM1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBIiBkYXRhLWxhYmVsPSLinKggMS4g7IiY7KeRIOuLqOqzhCDinKgK6rCc7J247KCV67O0IOu5hOyLneuzhO2ZlArtj6zrp7cg6rec6rKpIOqygOymnSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSIxNjIuNzMzIiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTM3LjM2NjUiIHk9IjExOS4zNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTM3LjM2NjUiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj7inKggMS4g7IiY7KeRIOuLqOqzhCDinKg8L3RzcGFuPjx0c3BhbiB4PSIxMzcuMzY2NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+6rCc7J247KCV67O0IOu5hOyLneuzhO2ZlDwvdHNwYW4+PHRzcGFuIHg9IjEzNy4zNjY1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7tj6zrp7cg6rec6rKpIOqygOymnTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJCIiBkYXRhLWxhYmVsPSJCIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjI2Ni43MzMiIHk9IjEwMC45IiB3aWR0aD0iNjAiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI5Ni43MzMiIHk9IjExOS4zNTAwMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+QjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQyIgZGF0YS1sYWJlbD0iQyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzNzQuNzMzIiB5PSIxMDAuOSIgd2lkdGg9IjYwIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjQwNC43MzMiIHk9IjExOS4zNTAwMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+QzwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRCIgZGF0YS1sYWJlbD0iRCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0ODIuNzMzIiB5PSIxMDAuOSIgd2lkdGg9IjYwIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjUxMi43MzMiIHk9IjExOS4zNTAwMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+RDwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 5대 핵심 지표 및 4대 주기별 관리 활동 전격 해부 (3단 표)**

이 토픽은 평가 지표를 단순 암기가 아닌 \*\*'구문'\*\*과 **'의미'** 정확성으로 논리적 분류하고, 실무 검수에서 쓰이는 \*\*'샘플링 검사 표준(KS Q ISO 2859-1)'\*\*을 언급하는 것이 합격을 결정짓는 포인트입니다.

| **핵심 척도**                | **📊 5대 품질 지표 (Metrics) 🚨**                                                                                                                                                                                            | **🛠️ 4대 품질 활동 (Lifecycle) 💯**                                                                                                                                         | **💼 품질 표준 규격 (KS/ISO) 💯**                                                                           |
| :----------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| **개념 / 위상**              | **'데이터 적합성 측정 자'.** 이 데이터를 신경망 모델에 주입해도 에러가 안 나고 똑똑해질 수 있는지 수치화함.                                                                                                                                                       | **'데이터 라이프사이클의 제어'.** 작업자(라벨러)의 실수를 방지하고 오류 데이터를 입구 컷하기 위한 단계별 액션.                                                                                                      | 정부(NIA) 가이드라인 및 국가 규격이 명시하는 **공식 데이터 평가 표준**.                                                         |
| **핵심 세부 내용 (출제 포인트) 🚨** | **1. \[구문 정확성 💯]** 파일 포맷, JSON 키 값 구조가 설계 명세서와 일치하는가? **2. \[의미 정확성 💯]** 사진 속 자동차에 'Car'라고 제대로 꼬리표를 달았는가? **3. \[다양성]** 특정 인종, 한쪽 성별로 데이터가 치우치지 않았는가? **4. 일관성** (작업자간 일치율 - Fleiss' Kappa 계수) **5. 완전성** (누락 데이터 제거) | **1. \[수집]** 수집 대상 획득 조건 수립 및 개인정보 비식별화. **2. \[정제]** 저화질, 깨진 이미지 등 불량 데이터 소거. **3. \[가공 🚨]** 라벨링 가이드라인을 세밀하게 제작해 배포하고 주기적으로 훈련. **4. \[검수 💯]** 자동화 규칙 검사 + 인간 교차 검수. | **\[KS Q ISO 2859-1 💯]** 수천만 장의 데이터를 다 전수 검사할 수 없으므로, 통계학에 기반하여 표본을 추출하여 합격/불합격을 판정하는 **샘플링 검사 규격**. |

#### **IV. \[결론/제언] 자동화 검수 도구(Linting) 도입과 MLOps 피드백 루프**

* **(키워드 위주 2줄 마무리)** "학습데이터의 지속적인 품질 유지를 위해서는 인간의 수동 검수에만 의존해서는 안 되며, 가공 단계에서 포맷 오류와 중복을 실시간 걸러주는 **'자동화 데이터 린터(Data Linter)'를 툴체인에 삽입하고, 모델 학습 후 오분류된 데이터를 다시 학습셋으로 재순환시키는 'MLOps 데이터 피드백 루프'를 정착시켜야 합니다.**"
