### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (신경망의구조, 학습의두흐름) — 3~4줄
Ⅱ. 피드포워드 - 순전파 (본론①, 도식 1개 필수)
Ⅲ. 역전파와활성화함수, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

신경망은 \*\*"입력→은닉층→출력"\*\*으로 신호가흐르는 \*\*피드포워드(순전파)\*\*와, \*\*"오차를출력에서입력방향으로거꾸로전달해 가중치를수정"\*\*하는 **역전파** 두흐름으로 학습합니다 — 이는 앞서다룬 \*\*"귀납적학습"\*\*의 **"패턴추론"** 단계를, 신경망이라는 **구체적수학적구조**로 구현한 것입니다.

### Ⅱ. 피드포워드 — 순전파

| 단계                   | 내용                                 |
| :------------------- | :--------------------------------- |
| **가중합**(WeightedSum) | 각입력값에 **가중치를곱해모두더함**+편향(bias)추가    |
| **활성화**(Activation)  | 그가중합을 **활성화함수**에통과시켜 **다음층으로전달**   |
| **층별전파**             | 입력층→은닉층→...→출력층 순으로 **한방향으로만**계산진행 |

→ 암기: **"입력에가중치곱해더하고,활성화함수통과시켜,다음층으로쭉전달한다"**

### 도식화 제안

```
[피드포워드 - 순전파]
[입력층] → 가중치곱하기+더하기 → [활성화함수] → [은닉층]
                                                    ↓
                        가중치곱하기+더하기 → [활성화함수] → [출력층]
                        
(신호가 한방향으로만, 입력에서출력까지 흘러감)
```

### Ⅲ. 역전파와 활성화함수 — 핵심 배점

**함정 방지: "오차를되돌린다"고만답하면절반. 왜"미분(기울기)"이핵심인지, 그리고활성화함수가"왜비선형이어야하는지" 근본이유를보여줘야완성됩니다.**

**역전파(Backpropagation)**

| 개념                         | 내용                                                              |
| :------------------------- | :-------------------------------------------------------------- |
| **손실함수**(LossFunction)     | 예측값과 **실제정답의차이**를 수치화                                           |
| **경사하강법**(GradientDescent) | 손실을 \*\*줄이는방향(기울기의반대방향)\*\*으로 가중치를 조금씩조정                        |
| **연쇄법칙**(ChainRule,핵심)     | 출력층의오차를, **미분의연쇄법칙**을이용해 **각층으로거꾸로전파**하며 **각가중치가오차에얼마나기여했는지**계산 |

→ 암기: **"오차를내고,미분으로 '누구책임이큰지'거꾸로계산해서, 책임큰가중치를더많이수정한다"** — 앞서다룬 \*\*"REDO/UNDO"\*\*의 **"순차적으로쌓인것을거꾸로되짚어가는"** 원리와 유사하게, 역전파도 \*\*"출력층부터입력층방향으로 거꾸로오차책임을추적"\*\*합니다.

### 도식화 제안

```
[역전파 - 오차를거꾸로전파]
[입력층] ← 가중치수정 ← [은닉층] ← 가중치수정 ← [출력층]
                                                    ↑
                                            예측값 vs 실제정답
                                            (손실계산,여기서시작)

연쇄법칙으로: "이가중치가 최종오차에 얼마나책임있는가?" 각층마다계산
     ↓
경사하강법: 책임큰가중치는 크게수정, 책임적은가중치는 작게수정
```

**활성화함수 — 왜비선형이어야하는가**(핵심)

| 함수               | 특징                                                                                 |
| :--------------- | :--------------------------------------------------------------------------------- |
| **Sigmoid**      | 0\~1사이값 — \*\*기울기소실(Gradient Vanishing)\*\*문제(층이깊어지면 기울기가0에가까워짐)                   |
| **ReLU**(현재표준)   | 음수는0,양수는그대로 — **계산간단,기울기소실완화**                                                     |
| **핵심원리**(왜비선형인가) | 활성화함수가 **선형이면**, 아무리층을깊게쌓아도 **결국하나의선형함수와동일**— **비선형함수가있어야만** 복잡한패턴(곡선,비선형경계)을 학습가능 |

→ 암기: **"선형함수만쌓으면 결국하나의직선일뿐이다 — 비선형함수가있어야 복잡한곡선모양의패턴을 배울수있다"** — 앞서다룬 \*\*"SVM의커널트릭(선형으로안나뉘면 차원을높여서라도비선형경계를만든다)"\*\*과 **정확히같은문제의식**이, 신경망에서는 \*\*"활성화함수의비선형성"\*\*으로 해결됩니다.

### 도식화 제안

```
[활성화함수의 비선형성이 왜 중요한가]
[선형함수만사용시]
층1(선형) → 층2(선형) → 층3(선형) = 결국 "하나의선형함수"와동일
(아무리층을깊게쌓아도, 직선밖에못그림 - SVM에서직선으로 
 동심원을못나눴던문제와동일)

[비선형활성화함수사용시]
층1(비선형) → 층2(비선형) → 층3(비선형) = 복잡한곡선표현가능
(깊게쌓을수록 더복잡한패턴학습가능)
```

### Ⅳ. 결론

피드포워드NN은 \*\*"입력에서출력으로신호를한방향으로전달"\*\*하고, 역전파는 \*\*"그출력의오차를,연쇄법칙을이용해입력방향으로거꾸로전파하며 가중치를수정"\*\*합니다 — 이과정이 \*\*"앞서다룬귀납적학습(사례에서패턴을추론)"\*\*의 **구체적수학적실행메커니즘**이며, **활성화함수의비선형성**이 없다면 \*\*"아무리층을깊게쌓아도 결국하나의직선(선형함수)에불과"\*\*해 복잡한패턴을 학습할수없습니다 — 이는 앞서다룬 \*\*"SVM의커널트릭"\*\*과 \*\*동일한근본원리(비선형변환이있어야 복잡한경계를표현가능)\*\*를, 신경망이라는 다른형태로 구현한 것을 보여주며, 오늘하루의 머신러닝·딥러닝기초시리즈전체를 \*\*"기계가어떻게실제로 오차로부터배우는가"\*\*라는 핵심메커니즘으로 완결짓습니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "인공지능(딥러닝)이 스스로 학습하고 똑똑해지는 전체 과정인 '모의고사 풀고 오답 노트 정리하기'의 3대 핵심 메커니즘이다. 첫째, **'순전파(Feed-forward)'**. 학생이 문제를 입력받아 자기 머릿속(은닉층)을 거쳐 정답을 쭉쭉 적어 내려가는 '직진(예측)' 과정이다. 둘째, **'역전파(Backpropagation)'**. 딥러닝을 위대하게 만든 기적의 알고리즘이다. 채점 결과 틀린 오차(Loss)를 들고, 맨 뒤(출력층)에서부터 앞으로 거꾸로 돌아가며 "네가 계산을 잘못해서 틀린 거야!"라며 뇌세포의 가중치를 미분(편미분)으로 싹 다 고쳐버리는 오답 노트 과정이다. 셋째, **'활성화 함수(Activation)'**. 뇌세포가 신호를 다음 층으로 넘길지 말지 결정하는 문지기다. 핵심은 신경망에 곡선을 그리는 \*\*'비선형성'\*\*을 부여해, 단순한 직선 계산을 넘어 복잡하고 기하학적인 실세계의 문제를 풀게 해 주는 마법의 함수(ReLU, Sigmoid)다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 딥러닝 모델의 생명 주기, 인공신경망 3대 메커니즘 개요**

* **정의:** 데이터를 입력받아 예측값(출력)을 내는 **순전파(FNN)**, 그 예측값과 실제 정답의 오차를 줄이기 위해 가중치를 역방향으로 갱신하는 **역전파(Backprop)**, 그리고 각 노드에 비선형성을 부여하는 **활성화 함수**가 결합된 신경망의 학습 루프 체계.
* **목적:** 단순히 입력과 출력을 연결하는 1차원적 회귀 모델의 한계를 벗어나, 미분 최적화(Gradient Descent)를 통해 모델 스스로 가장 완벽한 패턴(가중치)을 찾아내기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 예측하고, 틀리고, 돌아가서 고친다!**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMTA5LjY3Nzk5OTk5OTk5OTkgMzU2LjciIHdpZHRoPSIxMTA5LjY3Nzk5OTk5OTk5OTkiIGhlaWdodD0iMzU2LjciIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9fMUN5Y2xlX0Vwb2NoIiBkYXRhLWxhYmVsPSLsnbjqs7Xsi6Dqsr3rp50g7ZWZ7Iq1IDEtQ3ljbGUgKEVwb2NoKSI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMTAyOS42Nzc5OTk5OTk5OTk5IiBoZWlnaHQ9IjI3Ni43IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMTAyOS42Nzc5OTk5OTk5OTk5IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+7J246rO17Iug6rK966edIO2VmeyKtSAxLUN5Y2xlIChFcG9jaCk8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IklOIiBkYXRhLXRvPSJPVVQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuKcqCAxLiDsiJzsoITtjIwg4p6h77iPCuyeheugpS0mZ3Q77J2A64uJLSZndDvstpzroKUiIHBvaW50cz0iNzI2LjU3NiwyNjYuMDc1IDg4NS4zMjYsMjY2LjA3NSA4ODUuMzI2LDI0My44NTAwMDAwMDAwMDAwMiA5MjEuMzI2LDI0My44NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iT1VUIiBkYXRhLXRvPSJMT1NTIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7KCV64u1KExhYmVsKeqzvCDruYTqtZAiIHBvaW50cz0iOTIxLjMyNiwyMzEuNTUgODg1LjMyNiwyMzEuNTUgODg1LjMyNiwyMDkuMzI1IDE5NCwyMDkuMzI1IDE5NCwyMTYuNyAxODIsMjE2LjciIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTE9TUyIgZGF0YS10bz0iVyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i4pyoIDIuIOyXreyghO2MjCDirIXvuI8K7Jik7LCo66W8IOuTpOqzoCDrkqTroZwg6rCA66mwCu2OuOuvuOu2hOycvOuhnCDqsIDspJHsuZgg7IiY7KCVISIgcG9pbnRzPSIxODIsMjU4LjcgMTk0LDI1OC43IDE5NCwyNjYuMDc1IDQxMi4zOSwyNjYuMDc1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJXIiBkYXRhLXRvPSJJTiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI1NjAuMzAzLDI2Ni4wNzUgNjA4LjMwMywyNjYuMDc1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IklOIiBkYXRhLXRvPSJPVVQiIGRhdGEtbGFiZWw9IuKcqCAxLiDsiJzsoITtjIwg4p6h77iPCuyeheugpS0mZ3Q77J2A64uJLSZndDvstpzroKUiPgogIDxyZWN0IHg9Ijc3MC41NzYiIHk9IjI0My4wNzUiIHdpZHRoPSIxMDYuNzUwMDAwMDAwMDAwMDEiIGhlaWdodD0iNDQuNiIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI4MjMuOTUxIiB5PSIyNjUuMzc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIj48dHNwYW4geD0iODIzLjk1MSIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPuKcqCAxLiDsiJzsoITtjIwg4p6h77iPPC90c3Bhbj48dHNwYW4geD0iODIzLjk1MSIgZHk9IjE0LjMiPuyeheugpS0mZ3Q77J2A64uJLSZndDvstpzroKU8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJPVVQiIGRhdGEtdG89IkxPU1MiIGRhdGEtbGFiZWw9IuygleuLtShMYWJlbCnqs7wg67mE6rWQIj4KICA8cmVjdCB4PSI0MzAuMjk4NSIgeT0iMTkzLjMyNSIgd2lkdGg9IjExMi4wOTYwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjQ4Ni4zNDY1IiB5PSIyMDguNDc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7soJXri7UoTGFiZWwp6rO8IOu5hOq1kDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJMT1NTIiBkYXRhLXRvPSJXIiBkYXRhLWxhYmVsPSLinKggMi4g7Jet7KCE7YyMIOKshe+4jwrsmKTssKjrpbwg65Ok6rOgIOuSpOuhnCDqsIDrqbAK7Y6466+467aE7Jy866GcIOqwgOykkey5mCDsiJjsoJUhIj4KICA8cmVjdCB4PSIyMjYiIHk9IjIzNi4wNzUiIHdpZHRoPSIxNDIuMzkwMDAwMDAwMDAwMDEiIGhlaWdodD0iNTguOTAwMDAwMDAwMDAwMDA2IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjI5Ny4xOTUiIHk9IjI2NS41MjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSIyOTcuMTk1IiBkeT0iLTEwLjQ1MDAwMDAwMDAwMDAwMSI+4pyoIDIuIOyXreyghO2MjCDirIXvuI88L3RzcGFuPjx0c3BhbiB4PSIyOTcuMTk1IiBkeT0iMTQuMyI+7Jik7LCo66W8IOuTpOqzoCDrkqTroZwg6rCA66mwPC90c3Bhbj48dHNwYW4geD0iMjk3LjE5NSIgZHk9IjE0LjMiPu2OuOuvuOu2hOycvOuhnCDqsIDspJHsuZgg7IiY7KCVITwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJJTiIgZGF0YS1sYWJlbD0i7J6F66ClIOuNsOydtO2EsCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI2MDguMzAzIiB5PSIyNDcuNjI1IiB3aWR0aD0iMTE4LjI3MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNjY3LjQzOTUiIHk9IjI2Ni4wNzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyeheugpSDrjbDsnbTthLA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik9VVCIgZGF0YS1sYWJlbD0iQUkg7JiI7Lih6rCSIOuPhOy2nCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI5MjEuMzI2IiB5PSIyMTkuMjUiIHdpZHRoPSIxMzIuMzUyIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI5ODcuNTAyMDAwMDAwMDAwMSIgeT0iMjM3LjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkFJIOyYiOy4oeqwkiDrj4Tstpw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkxPU1MiIGRhdGEtbGFiZWw9IuyYpOywqCDrsJzsg50KTG9zcyDqs4TsgrAiIGRhdGEtc2hhcGU9ImNpcmNsZSI+CiAgPGNpcmNsZSBjeD0iMTE5IiBjeT0iMjM3LjciIHI9IjYzIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjExOSIgeT0iMjM3LjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjExOSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuyYpOywqCDrsJzsg508L3RzcGFuPjx0c3BhbiB4PSIxMTkiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPkxvc3Mg6rOE7IKwPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlciIGRhdGEtbGFiZWw9IuqwgOykkey5mCDsl4XrjbDsnbTtirgiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDEyLjM5IiB5PSIyNDcuNjI1IiB3aWR0aD0iMTQ3LjkxMyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0ODYuMzQ2NSIgeT0iMjY2LjA3NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+6rCA7KSR7LmYIOyXheuNsOydtO2KuDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQSIgZGF0YS1sYWJlbD0i4pyoIDMuIO2ZnOyEse2ZlCDtlajsiJgg4pyoCuqwgSDrhbjrk5wo64+Z6re4652866+4KeuniOuLpCDrrLjsp4DquLAg67Cw7LmYCuyEoO2YlSDqs4TsgrDsnYQg67mE7ISg7ZiV7Jy866GcIOq1rOu2gOumvCEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMjYzLjUwOSIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTg3Ljc1NDUiIHk9IjExOS4zNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTg3Ljc1NDUiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj7inKggMy4g7Zmc7ISx7ZmUIO2VqOyImCDinKg8L3RzcGFuPjx0c3BhbiB4PSIxODcuNzU0NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+6rCBIOuFuOuTnCjrj5nqt7jrnbzrr7gp66eI64ukIOusuOyngOq4sCDrsLDsuZg8L3RzcGFuPjx0c3BhbiB4PSIxODcuNzU0NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7ISg7ZiVIOqzhOyCsOydhCDruYTshKDtmJXsnLzroZwg6rWs67aA66a8ITwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 순전파 vs 역전파 vs 활성화 함수 전격 해부 (3단 표)**

이 토픽은 데이터가 흐르는 방향(Forward/Backward)과 함께, 딥러닝이 단순 곱셈의 한계를 벗어나게 해 준 \*\*'비선형성(활성화 함수)'\*\*을 강조하는 것이 완벽한 득점 포인트입니다.

| **핵심 척도**              | **➡️ 순전파 (Feed-forward NN)**                                                            | **⬅️ 역전파 (Backpropagation) 🚨**                                                                           | **⚡ 활성화 함수 (Activation Function) 🚨**                                                                           |
| :--------------------- | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| **개념 / 역할**            | **'예측값을 향한 직진'.** 입력층에서 들어온 데이터가 은닉층을 거쳐 출력층까지, 루프나 뒤로 빠짐 없이 오직 앞(전방향)으로만 계산되어 흘러가는 구조. | **'오차를 고치는 역주행 💯'.** 순전파로 나온 예측값과 실제 정답의 차이(Loss)를 계산한 뒤, **출력층에서부터 역방향으로** 각 노드의 책임(가중치)을 묻고 수정하는 알고리즘. | **'신호 통과를 결정하는 문지기'.** 이전 층에서 넘겨받은 연산 결과(가중치 합)를 다음 층으로 보낼지 말지, 어떤 크기로 구부려서 보낼지 결정하는 수학적 함수.                    |
| **작동 메커니즘**            | 단순한 행렬 곱셈 연산 `(W*x + b)`의 연속.                                                           | 연쇄 법칙(Chain Rule) 기반의 편미분을 통해, 가중치 기울기(Gradient)의 반대 방향으로 값을 업데이트함.                                       | **\[Sigmoid]** 0과 1 사이로 압착 (과거형). **\[ReLU 💯]** 음수는 0, 양수는 그대로 통과 (현재 딥러닝 디폴트 표준).                             |
| **딥러닝 기여 (출제 포인트) 🚨** | 데이터를 넣으면 결과를 내주는 인공지능의 가장 기본적인 뼈대 모델(껍데기)을 제공함.                                         | 역전파가 없었다면 수백만 개의 가중치를 인간이 일일이 수정해야 했음. **오늘날의 딥러닝을 융성하게 만든 1등 공신.**                                       | **\[비선형성(Non-linearity) 부여 💯]** 활성화 함수가 없으면 신경망을 100층으로 쌓아도 결국 1층짜리 단순 1차 방정식 선형 모델이 되어버려 실세계의 복잡한 문제를 풀 수 없음. |

#### **IV. \[결론/제언] 기울기 소실(Vanishing Gradient) 극복과 ReLU의 등장**

* **(키워드 위주 2줄 마무리)** "과거 역전파는 신경망이 깊어질수록 뒤에서 앞으로 오차를 미분해 전달하다가 기울기가 0으로 깎여 사라지는 '기울기 소실' 문제로 빙하기를 맞았습니다. 그러나 미분값이 죽지 않는 **'ReLU(렐루)' 활성화 함수의 등장과 Adam 최적화 기법의 결합으로, 수백 층의 심층 신경망(DNN) 역전파 학습이 완벽하게 가능해졌습니다.**"

