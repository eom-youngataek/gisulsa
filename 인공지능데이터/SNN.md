### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (기존신경망과의근본적차이) — 3~4줄
Ⅱ. 핵심메커니즘 - 막전위와스파이크발화 (본론①, 도식 1개 필수)
Ⅲ. 이벤트기반연산과학습의어려움, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

앞서다룬 **CNN,GNN,VAE**는 모두 \*\*"매순간마다 모든뉴런이 실수값(연속적인숫자)을계산해서 다음층으로전달"\*\*합니다 — SNN은 실제 **생물학적뉴런**처럼, \*\*"평소엔조용히있다가, 특정조건이되면 순간적으로'스파이크(전기신호펄스)'하나만발사"\*\*하는 **훨씬생물학적이고,이벤트기반**의 방식입니다.

### Ⅱ. 핵심메커니즘 — 막전위와 스파이크발화

| 개념                         | 내용                                                                                                   |
| :------------------------- | :--------------------------------------------------------------------------------------------------- |
| **막전위**(MembranePotential) | 뉴런내부에 **입력신호가들어올때마다조금씩쌓이는 "전하"**— 배터리가충전되는것과유사                                                       |
| **임계값**(Threshold)         | 막전위가 **일정수준을넘으면**, 뉴런이 **"발화(스파이크)"**                                                                |
| **발화**(Spike)              | 스파이크발생시 막전위는 **즉시0으로리셋**,다음뉴런에 **신호전달**                                                              |
| **시간정보**(핵심차이)             | 스파이크는 \*\*"언제발생했는지(타이밍)"\*\*자체가 **정보를담음**— 앞서다룬 CNN의 \*\*"매순간실수값"\*\*과 달리, \*\*"스파이크간격,횟수"\*\*로 정보표현 |

→ 암기: **"입력이쌓이다가,임계값넘으면 스파이크한번쏘고 리셋된다 — 신호의크기가아니라, 스파이크의타이밍자체가정보다"**

### 도식화 제안

```
[SNN - 막전위 축적과 발화]
막전위
  │           ╱╲(임계값도달→발화!즉시리셋)
  │         ╱    
  │       ╱         ╱╲(다시축적→다시발화)
  │─────╱───────────
  └──────────────────────→ 시간
      입력없음(조용)  입력들어옴(축적)  발화(스파이크!)

[기존신경망(CNN등)]              [SNN]
매순간 모든뉴런이               평소엔 대부분뉴런이 "조용"
실수값을계산·전달                임계값넘을때만 "스파이크"발사
(항상연산,항상전력소모)          (이벤트발생시에만연산,저전력)
```

### Ⅲ. 이벤트기반연산과 학습의어려움 — 핵심 배점

**함정 방지: "저전력이다"고만답하면절반. 왜 저전력인지의구조적이유와, SNN이가진근본적학습난제(미분불가능문제)를 보여줘야완성됩니다.**

| 항목                  |                                                                                                     내용 |
| :------------------ | -----------------------------------------------------------------------------------------------------: |
| **초저전력의이유**(핵심)     | 대부분뉴런이 **"평소엔아무연산도안하고 조용히있다가"**, 스파이크가발생한 **극소수의뉴런만** 연산— 앞서다룬 \*\*"뉴로모픽컴퓨팅"\*\*이 **IoT저전력환경**에 유망한 이유 |
| **역전파의근본적문제**(핵심난제) |    앞서다룬 \*\*"역전파는미분가능해야작동"\*\*하는데, \*\*스파이크발화(0아니면1)\*\*는 **불연속적**이라 **미분자체가불가능**(계단함수의미분은 대부분0또는정의불가) |
| **해결시도**            |                    **서로게이트(SurrogateGradient)**— 실제로는 불연속이지만, 학습시에만 \*\*"가짜미분가능함수"\*\*로 근사해 역전파를 억지로적용 |

→ 암기: **"평소엔대부분이쉬니전력을덜쓰고,그런데스파이크는 On/Off라 미분이안돼서, 학습땐가짜기울기(서로게이트)로속여서 역전파를돌린다"** — 이는 앞서다룬 \*\*"VAE의재매개변수화트릭"\*\*과 **정확히같은문제의식**의 재현입니다: \*\*"역전파가필요로하는미분가능성과, 모델의본질적성질(확률성,불연속성)이충돌할때, 수학적트릭으로우회한다"\*\*는 오늘하루신경망시리즈전체의 공통패턴입니다.

### 도식화 제안

```
[SNN의 학습난제 - 미분불가능]
스파이크발화함수: 막전위<임계값 → 출력0
                막전위≥임계값 → 출력1 (계단함수)
     ↓ 미분하면
대부분구간에서 기울기=0 (역전파로 학습신호전달불가)

[해결: Surrogate Gradient]
실제발화함수(계단, 미분불가) 대신
학습시에만 "매끄러운근사함수"(예:시그모이드형태)로 대체
     ↓
가짜기울기로 역전파진행 → 실제로는 스파이크함수사용
```

**뉴로모픽하드웨어와의연결**: 앞서다룬 \*\*컴퓨터구조답안의뉴로모픽컴퓨팅(인메모리컴퓨팅,IoT저전력)\*\*이 바로 이SNN을 **하드웨어수준에서구현**한것입니다 — 일반GPU는 \*\*"모든뉴런을매순간계산"\*\*하도록설계돼있어 SNN의 \*\*"이벤트기반희소성"\*\*을 살리지못하지만, **뉴로모픽칩**은 \*\*"스파이크가발생할때만 회로가작동"\*\*하도록 설계되어 SNN의장점을 극대화합니다.

### Ⅳ. 결론

SNN은 \*\*"CNN,GNN,VAE같은기존신경망이 매순간모든뉴런을계산하는것과달리, 생물학적뉴런처럼 막전위를축적하다 임계값을넘을때만스파이크를발사하는 이벤트기반신경망"\*\*입니다 — 이 **"평소엔조용한"** 특성덕분에 **초저전력**이 가능해 뉴로모픽하드웨어·IoT에 유망하지만, \*\*"스파이크의불연속성이 역전파에필요한미분가능성과충돌"\*\*하는 근본적난제가있어 **서로게이트**같은 우회기법이 필요합니다 — 이는 앞서다룬 **VAE의재매개변수화트릭**과 함께, **"신경망모델의본질적특성(확률성,불연속성)과, 학습알고리즘(역전파)의요구조건사이의충돌을, 수학적트릭으로타협하는"** 오늘하루신경망시리즈전체의 핵심주제를 완결짓습니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "현재 세상을 지배하는 딥러닝(DNN, CNN)을 2세대라고 한다면, SNN은 실제 인간 뇌의 뉴런 동작 방식과 시간의 흐름까지 완벽하게 모방한 \*\*'제3세대 인공신경망'\*\*이다. 기존 2세대 신경망은 연속적인 소수점 숫자(0.85, 0.42 등)를 쉬지 않고 행렬 계산으로 주고받느라 전력(전기) 소모가 미친 듯이 많다. 하지만 SNN은 다르다. 뉴런이 에너지를 모으고 있다가 임계치를 넘는 순간에만 '팍!' 하고 이진 신호(Spike)를 쏘고(Fire) 쉰다. 스파이크가 튈 때만 칩이 일을 하기 때문에 전기를 거의 안 먹는 **'초저전력 뉴로모픽 칩'** 구현에 가장 완벽한 알고리즘이다. 하지만 신호가 불연속적으로 딱딱 끊기다 보니 미분(역전파)이 불가능해서, 지금의 딥러닝처럼 정밀하게 학습시키기가 극도로 어렵다는 치명적인 한계와 싸우고 있다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 뇌를 가장 완벽하게 모방한 제3세대 AI, SNN 개요**

* **정의:** 시간 축(Time Domain)을 포함하여, 일정 수준 이상의 자극이 누적되었을 때만 불연속적인 펄스(Spike) 신호를 발생시켜 정보를 전달하는 생물학적 뉴런 네트워크 모델.
* **목적:** GPU 기반의 기존 딥러닝이 잡아먹는 천문학적인 전력 소모와 탄소 배출 한계를 극복하고, 인간의 뇌처럼 전구 하나 켤 전력(20W)만으로 고도의 연산을 수행하는 엣지 AI(Edge AI)를 구현하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) SNN의 핵심: LIF(Leaky Integrate-and-Fire) 모델**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMTUyLjI2MiAyMjYuMjAwMDAwMDAwMDAwMDIiIHdpZHRoPSIxMTUyLjI2MiIgaGVpZ2h0PSIyMjYuMjAwMDAwMDAwMDAwMDIiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IlNOTl9fU3Bpa2VfXyIgZGF0YS1sYWJlbD0iU05OIOuJtOufsOydmCDsiqTtjIzsnbTtgawoU3Bpa2UpIOuwnOyCrCDrqZTsu6Tri4jsppgiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjEwNzIuMjYyIiBoZWlnaHQ9IjE0Ni4yMDAwMDAwMDAwMDAwMiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjEwNzIuMjYyIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+U05OIOuJtOufsOydmCDsiqTtjIzsnbTtgawoU3Bpa2UpIOuwnOyCrCDrqZTsu6Tri4jsppg8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IklOIiBkYXRhLXRvPSJJIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE1OS40NTMsMTIzLjM3NSAyMDcuNDUzLDEyMy4zNzUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkkiIGRhdGEtdG89IkwiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjI2Ny40NTMsMTI5LjUyNSAyNzkuNDUzLDEyOS41MjUgMjc5LjQ1MywxNTEuNzUgMzE1LjQ1MywxNTEuNzUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTCIgZGF0YS10bz0iQ0hLIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjM3NS40NTMsMTUxLjc1IDM4Ny40NTMsMTUxLjc1IDM4Ny40NTMsMTI5LjUyNSA0MjMuNDUzLDEyOS41MjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkNISyIgZGF0YS10bz0iRiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iWWVzICjrrLwg64SY7LmoISkiIHBvaW50cz0iNDkyLjA3ODk5OTk5OTk5OTk1LDEyMy4zNzUgNjY0LjI1NywxMjMuMzc1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDSEsiIGRhdGEtdG89IkkiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Ik5vIiBwb2ludHM9IjQyMy40NTMsMTE3LjIyNSAzODcuNDUzLDExNy4yMjUgMzg3LjQ1Myw5NSAyNzkuNDUzLDk1IDI3OS40NTMsMTE3LjIyNSAyNjcuNDUzLDExNy4yMjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkYiIGRhdGEtdG89Ik9VVCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI4ODAuMzQxOTk5OTk5OTk5OSwxMjMuMzc1IDkyOC4zNDE5OTk5OTk5OTk5LDEyMy4zNzUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQ0hLIiBkYXRhLXRvPSJGIiBkYXRhLWxhYmVsPSJZZXMgKOusvCDrhJjsuaghKSI+CiAgPHJlY3QgeD0iNTM2LjA3OSIgeT0iMTA3LjM3NSIgd2lkdGg9Ijg0LjE3ODAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTc4LjE2OCIgeT0iMTIyLjUyNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+WWVzICjrrLwg64SY7LmoISk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQ0hLIiBkYXRhLXRvPSJJIiBkYXRhLWxhYmVsPSJObyI+CiAgPHJlY3QgeD0iMzMwLjA5NCIgeT0iNzkiIHdpZHRoPSIzMC43MTgwMDAwMDAwMDAwMDQiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzNDUuNDUzIiB5PSI5NC4xNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+Tm88L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IklOIiBkYXRhLWxhYmVsPSLsnpDqt7kg7J6F66ClIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIxMDQuOTI1IiB3aWR0aD0iMTAzLjQ1MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEwNy43MjY1IiB5PSIxMjMuMzc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7snpDqt7kg7J6F66ClPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJJIiBkYXRhLWxhYmVsPSJJIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjIwNy40NTMiIHk9IjEwNC45MjUiIHdpZHRoPSI2MCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjM3LjQ1MyIgeT0iMTIzLjM3NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+STwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTCIgZGF0YS1sYWJlbD0iTCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzMTUuNDUzIiB5PSIxMzMuMyIgd2lkdGg9IjYwIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzNDUuNDUzIiB5PSIxNTEuNzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkNISyIgZGF0YS1sYWJlbD0iQ0hLIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQyMy40NTMiIHk9IjEwNC45MjUiIHdpZHRoPSI2OC42MjU5OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDU3Ljc2NTk5OTk5OTk5OTk2IiB5PSIxMjMuMzc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5DSEs8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkYiIGRhdGEtbGFiZWw9IuKcqCAzLiBGaXJlICjrsJztmZQv7Iqk7YyM7J207YGsKSDimqEKMOyXkOyEnCAx66GcIO2MjSEg7I+Y6rOgCuuLpOyLnCDqt7jrpofsnYQgMOycvOuhnCDruYTsm4AiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNjY0LjI1NyIgeT0iODguMDI1IiB3aWR0aD0iMjE2LjA4NDk5OTk5OTk5OTk4IiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI3NzIuMjk5NSIgeT0iMTIzLjM3NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNzcyLjI5OTUiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj7inKggMy4gRmlyZSAo67Cc7ZmUL+yKpO2MjOydtO2BrCkg4pqhPC90c3Bhbj48dHNwYW4geD0iNzcyLjI5OTUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPjDsl5DshJwgMeuhnCDtjI0hIOyPmOqzoDwvdHNwYW4+PHRzcGFuIHg9Ijc3Mi4yOTk1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7ri6Tsi5wg6re466aH7J2EIDDsnLzroZwg67mE7JuAPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik9VVCIgZGF0YS1sYWJlbD0i64uk7J2MIOuJtOufsOycvOuhnCDssIzrpr8hIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjkyOC4zNDE5OTk5OTk5OTk5IiB5PSIxMDQuOTI1IiB3aWR0aD0iMTY3LjkyIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTAxMi4zMDE5OTk5OTk5OTk5IiB5PSIxMjMuMzc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7ri6TsnYwg64m065+w7Jy866GcIOywjOumvyE8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 기존 2세대 DNN vs 3세대 SNN 전격 대조 (3단 표)**

이 토픽은 연속적인 실수형 연산(행렬 곱)과 불연속적인 스파이크(이벤트)의 차이를 설명하고, 미분이 안 되는 \*\*'역전파의 한계'\*\*를 짚어내는 것이 가장 압도적인 득점 포인트입니다.

| **핵심 척도**                | **🧠 2세대 인공신경망 (DNN)**                                                                    | **⚡ 3세대 스파이킹 신경망 (SNN) 🚨**                                                                                                                |
| :----------------------- | :---------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| **개념 / 구조 (3세대)**        | **'실수형 연산 기반'.** 0과 1 사이의 연속적인 실수 값(예: 0.87)을 활성화 함수(Sigmoid, ReLU)를 통해 다음 층으로 끊임없이 전달함.  | **'이진 스파이크 (0 또는 1) 💯'.** 시간 개념(Time)이 포함되어 있으며, 자극이 임계치를 넘는 특정 시점(Temporal)에만 펄스(Spike)를 쏘고 넘김.                                          |
| **작동 원리 및 하드웨어 🚨**      | **\[GPU / 행렬 곱 의존]** 모든 노드가 무조건 연산을 수행하므로 전력 소모(병목 현상)가 극심함 (폰 노이만 아키텍처).                 | **\[뉴로모픽(Neuromorphic) 칩 💯]** 스파이크가 발생하는 노드(이벤트)만 전기를 쓰므로 **초저전력 구현** 가능. (인텔 Loihi, IBM TrueNorth).                                      |
| **장단점 / 학습 (출제 포인트) 🚨** | **\[미분과 역전파 최적화 💯]** 그래프가 부드럽게 이어져 있어 미분(기울기) 계산이 쉬움. **역전파(Backprop)를 통해 완벽한 학습이 가능함.** | **\[장점]** 엣지 디바이스(자율주행, IoT 센서)의 극강 전력 효율. **\[단점 🚨]** 0에서 1로 수직 상승하는 스파이크는 **미분이 불가능하여 역전파(학습)가 박살 남.** (STDP 방식이나 대리 기울기 기법으로 우회 연구 중). |

#### **IV. \[결론/제언] 이벤트 기반 카메라(Event Camera)와의 결합 생태계**

* **(키워드 위주 2줄 마무리)** "SNN은 미분의 한계로 인해 기존 서버용 딥러닝 모델을 대체하기보다는, 초당 수천 프레임의 빛 번짐(이벤트)만 감지하는 **'이벤트 기반 비전 센서(Event Camera)'와 결합하여, 초고속/초저전력 자율주행 회피 시스템 같은 하드웨어 엣지 AI(Edge AI)의 패러다임을 바꿀 것입니다.**"
