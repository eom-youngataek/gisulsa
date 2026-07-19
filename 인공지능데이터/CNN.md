### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (기존완전연결망의문제, CNN의발상전환) — 3~4줄
Ⅱ. 핵심연산 - 합성곱(Convolution) (본론①, 도식 1개 필수)
Ⅲ. 풀링과계층적특징추출, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

앞서다룬 **피드포워드NN**은 \*\*"모든입력뉴런을 다음층의모든뉴런과연결"\*\*하는데, 100×100픽셀이미지만해도 **입력이1만개**— 파라미터가 **폭발적으로증가**하고, \*\*"이미지의픽셀들이서로가까이있다"\*\*는 **공간적정보자체를무시**합니다 — CNN은 **"작은필터(커널)로 이미지의일부분씩만훑으며 지역적패턴을찾는"** 방식으로 이문제를해결합니다.

### Ⅱ. 핵심연산 — 합성곱(Convolution)

| 개념                  | 내용                                                            |
| :------------------ | :------------------------------------------------------------ |
| **필터(커널)**          | **작은크기(예:3×3)의가중치행렬**— 특정패턴(모서리,곡선등)을 감지하도록 학습됨               |
| **합성곱연산**           | 필터를 이미지위에서 **조금씩이동시키며**, 겹치는영역과 **가중합계산**                     |
| **특징맵**(FeatureMap) | 합성곱결과로 만들어지는, \*\*"이패턴이어디에있는지"\*\*를 보여주는 출력                   |
| **파라미터공유**(핵심혁신)    | 같은필터를 **이미지전체에반복사용**— 앞서다룬 \*\*"완전연결의폭발적파라미터"\*\*를 **극적으로줄임** |

→ 암기: **"작은필터하나로 이미지전체를 스캔하듯훑으며, 그필터가감지하는패턴이어디있는지 표시한다 — 같은필터를 재사용하니 파라미터가훨씬적다"**

### 도식화 제안

```
[합성곱 연산 - 필터가 이미지를 훑는과정]
[이미지]                    [3×3필터]         [특징맵]
1 2 3 4                    1 0 1             
5 6 7 8    ← 필터가         0 1 0      →     [결과값1][결과값2]...
9 8 7 6      슬라이딩          1 0 1
3 2 1 0      하며연산

(같은필터가 이미지전체를이동하며 반복사용 - 파라미터절약)
```

### Ⅲ. 풀링과 계층적특징추출 — 핵심 배점

**함정 방지: "필터로패턴을찾는다"고만답하면절반. 풀링이왜필요한지, 그리고층이깊어질수록"무엇을"학습하는지 계층적변화를보여줘야완성됩니다.**

| 개념                | 내용                                                                            |
| :---------------- | :---------------------------------------------------------------------------- |
| **풀링**(Pooling)   | 특징맵을 **더작게압축**(예:MaxPooling — 영역내 **최대값만남김**)— 위치가 **약간달라져도 같은특징으로인식**(위치불변성) |
| **계층적특징추출**(핵심통찰) | **얕은층**은 **모서리,색상같은단순패턴**감지 → **깊은층**으로갈수록 **눈,코,얼굴전체같은복잡한개념**으로 조합           |

→ 암기: **"풀링으로압축해서, 위치가조금달라도같은걸로인식하고, 층이깊어질수록 단순한선에서→복잡한사물전체로 개념이커진다"** — 앞서다룬 \*\*"Boosting의순차적보완"\*\*과 유사하게, CNN도 **"앞층의단순한특징을, 다음층이조합해더복잡한특징을만드는"** 계층적축적방식입니다.

### 도식화 제안

```
[CNN의 계층적 특징 추출]
[입력이미지: 고양이사진]
     ↓ 1층 합성곱
[단순패턴감지] 세로선,가로선,모서리
     ↓ 2층 합성곱
[중간패턴조합] 눈모양,귀모양,털무늬
     ↓ 3층 합성곱
[복잡한개념조합] 고양이얼굴전체
     ↓ 최종
[분류결과] "고양이"

(얕은층: 단순→ 깊은층: 복잡한개념으로 점점추상화)
```

**MaxPooling 동작예시**

```
[4×4 특징맵]           [2×2 MaxPooling적용후]
1 3 | 2 4              [3, 4]
5 2 | 1 6         →     [8, 6]
─────────
7 8 | 3 1
2 4 | 5 6

(각2×2영역에서 최대값만남김 → 크기줄이면서 핵심특징은보존)
```

### Ⅳ. 결론

CNN은 **"앞서다룬완전연결신경망이이미지에서겪는파라미터폭발과공간정보무시문제를, 작은필터로 지역패턴을찾고(합성곱),그것을압축하며(풀링),층을쌓아 단순한패턴에서복잡한개념으로 계층적으로조합하는"** 방식으로 해결합니다 — 이는 앞서다룬 \*\*"활성화함수의비선형성"\*\*이 복잡한패턴표현을가능하게했던것처럼, \*\*"파라미터공유(합성곱)"\*\*가 \*\*"이미지처리에특화된효율적인구조"\*\*를 가능하게합니다 — 오늘하루의신경망시리즈(피드포워드NN→역전파→CNN)가, \*\*"데이터의특성(이미지의공간적구조)에맞춰 신경망구조자체를설계하는것"\*\*이 왜 중요한지를 보여주며 완결됩니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "이미지, 자율주행, 영상 인식 분야를 제패한 딥러닝의 꽃이다. 인간의 시각 세포가 사물을 볼 때 일부분씩 뜯어보고 나중에 전체를 조합하는 생물학적 원리를 모방했다. 기존 인공신경망은 2차원 이미지를 억지로 한 줄(1차원)로 쫙 펴서 학습시키다 보니, 눈 옆에 코가 있다는 '공간적 정보'가 다 박살 났다. CNN은 다르다. 첫째, 작은 돋보기(필터/커널)로 2차원 이미지 전체를 훑어가며 공간 정보를 살린 채 특징(선, 윤곽선)만 도장 찍듯 뽑아내는 **'합성곱 층'**. 둘째, 뽑아낸 특징들의 해상도를 팍팍 압축하여 연산량을 줄이고 과적합을 막는 **'풀링 층'**. 마지막 셋째, 엑기스만 남은 특징들을 모아 최종적으로 "이건 고양이다!"라고 라벨을 분류하는 \*\*'완전 연결 층'\*\*까지 3박자로 움직인다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 공간 정보를 파괴하지 않는 비전 AI의 핵심, CNN 개요**

* **정의:** 다차원 배열(주로 2차원 이미지 픽셀) 데이터의 공간적(Spatial) 구조를 보존하면서, 합성곱 연산과 서브샘플링(풀링)을 통해 데이터의 특징(Feature)을 스스로 추출하고 분류하는 심층 인공신경망.
* **목적:** 기존 DNN(심층신경망)이 2차원 이미지를 1차원(Flatten)으로 쭉 펴버리면서 데이터 형상(Topology)이 무시되는 치명적 단점을 해결하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 특징을 뽑고 압축하여 분류하는 파이프라인**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NjkuMDkzMDAwMDAwMDAwMSAxOTMuOCIgd2lkdGg9IjU2OS4wOTMwMDAwMDAwMDAxIiBoZWlnaHQ9IjE5My44IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJDTk5fM19fIiBkYXRhLWxhYmVsPSJDTk4gM+uLqOqzhCDtlbXsi6wg66mU7Luk64uI7KaYIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI0ODkuMDkzIiBoZWlnaHQ9IjExMy44MDAwMDAwMDAwMDAwMSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjQ4OS4wOTMiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5DTk4gM+uLqOqzhCDtlbXsi6wg66mU7Luk64uI7KaYPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJJTiIgZGF0YS10bz0iQyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxODkuMDkzMDAwMDAwMDAwMDIsMTEwLjkgMjM3LjA5MzAwMDAwMDAwMDAyLDExMC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDIiBkYXRhLXRvPSJQIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjI5Ny4wOTMsMTEwLjkgMzQ1LjA5MywxMTAuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUCIgZGF0YS10bz0iRkMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDA1LjA5MywxMTAuOSA0NTMuMDkzLDExMC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJJTiIgZGF0YS1sYWJlbD0i6rOg7JaR7J20IOydtOuvuOyngAoyOHgyOCDtlL3shYAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMTMzLjA5MzAwMDAwMDAwMDAyIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTIyLjU0NjUwMDAwMDAwMDAxIiB5PSIxMTAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTIyLjU0NjUwMDAwMDAwMDAxIiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+6rOg7JaR7J20IOydtOuvuOyngDwvdHNwYW4+PHRzcGFuIHg9IjEyMi41NDY1MDAwMDAwMDAwMSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+Mjh4Mjgg7ZS97IWAPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkMiIGRhdGEtbGFiZWw9IkMiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjM3LjA5MzAwMDAwMDAwMDAyIiB5PSI5Mi40NSIgd2lkdGg9IjYwIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjI2Ny4wOTMiIHk9IjExMC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5DPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQIiBkYXRhLWxhYmVsPSJQIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM0NS4wOTMiIHk9IjkyLjQ1IiB3aWR0aD0iNjAiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMzc1LjA5MyIgeT0iMTEwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkZDIiBkYXRhLWxhYmVsPSJGQyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0NTMuMDkzIiB5PSI5Mi40NSIgd2lkdGg9IjYwIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0ODMuMDkzIiB5PSIxMTAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+RkM8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] CNN을 구성하는 3대 핵심 레이어(Layer) 전격 해부 (3단 표)**

이 토픽은 '돋보기(필터)'가 특징을 뽑아내는 과정과, 풀링이 부여하는 \*\*'위치 불변성(고양이가 구석에 있어도 알아봄)'\*\*을 설명하는 것이 압도적인 득점 포인트입니다.

| **핵심 척도**                 | **🔍 합성곱 층 (Convolution) 🚨**                                                                                                    | **📉 풀링 층 (Pooling) 🚨**                                                                              | **🏁 완전 연결 층 (FC Layer)**                                                                |
| :------------------------ | :------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------- |
| **핵심 역할**                 | **'공간 정보 기반 특징 추출 💯'.** 이미지의 윤곽선, 질감, 색상 패턴 등의 기하학적 특징(Feature)을 뽑아냄.                                                           | **'크기 압축 및 파라미터 감소 💯'.** 뽑아낸 특징 맵(Feature Map)의 크기를 줄여서 연산량을 획기적으로 낮춤.                               | **'최종 예측 및 분류'.** 앞선 층에서 걸러진 고급 특징들을 취합하여, 이게 어떤 클래스(개/고양이)인지 확률로 도출함.                   |
| **작동 원리 및 핵심 메커니즘 🚨**    | **\[필터(Filter) / 커널(Kernel)]** 3x3 크기의 작은 돋보기(필터)가 이미지 전체를 훑으며(Sliding Window) 픽셀값과 행렬 곱 연산을 수행함. **\[스트라이드(Stride)]** 필터 이동 보폭. | **\[Max Pooling (최대 풀링) 💯]** 2x2 칸에서 가장 큰(튀는) 값 1개만 뽑아서 이미지를 4분의 1로 압축해 버림. (Average Pooling 등도 있음). | 기존 신경망(DNN)과 동일한 구조. 추출된 2차원 데이터를 1차원으로 쭉 펴서(Flatten) 분류함. **소프트맥스(Softmax)** 활성화 함수 사용. |
| **CNN에 부여하는 가치 (출제 포인트)** | 픽셀 하나가 아닌, '주변 픽셀들과의 관계'를 연산하므로 이미지가 가진 공간 형상을 그대로 유지함.                                                                          | **\[위치 불변성 (Translation Invariance) 💯]** 고양이가 사진 정중앙에 있든 왼쪽 구석에 찌그러져 있든 동일하게 고양이로 인식하게 해줌 (과적합 방지).  | 분류의 최종 결과를 사람이 알아볼 수 있는 확률(Label) 값으로 번역해 줌.                                             |

#### **IV. \[결론/제언] CNN의 한계와 비전 트랜스포머(Vision Transformer, ViT)의 부상**

* **(키워드 위주 2줄 마무리)** "CNN은 돋보기(필터) 크기라는 좁은 시야(Local Receptive Field)에 갇혀 이미지 전체의 전역적 문맥(Global Context)을 파악하는 데는 한계가 있습니다. 이를 극복하기 위해 최근 컴퓨터 비전 분야는 NLP(자연어 처리)에서 넘어온 어텐션(Attention) 메커니즘 기반의 **'비전 트랜스포머(ViT)' 아키텍처가 CNN을 대체하며 새로운 SOTA(State-Of-The-Art) 모델로 등극하고 있습니다.**"
