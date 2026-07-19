컴퓨팅 컨티뉴엄은 오늘 다룬 "서버리스"·"앰비언트컴퓨팅"·"멀티클라우드"의 아이디어를 **"어디서 처리할 것인가"** 축으로 통합하는 최상위 개념입니다. 극단(엣지vs클라우드) 사이의 \*\*연속체(Continuum)\*\*라는 하나의 시각으로 스토리를 짜겠습니다.

### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (컴퓨팅 컨티뉴엄 정의, 등장배경) — 3~4줄
Ⅱ. 3대 계층 - 엣지/포그/클라우드 (본론①, 도식 1개 필수)
Ⅲ. 컨티뉴엄으로서의 특성 (본론②, 핵심 배점)
Ⅳ. 워크로드 배치기준 및 오늘 시리즈 총연결
Ⅴ. 결론
```

포인트: 개요에서 \*\*"기존엔 '데이터를 클라우드로 보낼지, 엣지에서 처리할지' 양자택일로 생각했는데, 실제로는 그 사이에 무수한 중간지점(포그)이 있고, 하나의 작업도 상황에 따라 그 스펙트럼 위를 오갈 수 있다 — 이 연속적 스펙트럼 전체를 하나의 자원풀처럼 관리하자는 게 컴퓨팅 컨티뉴엄"\*\*이라는 한 줄로 시작하면, 왜 "컨티뉴엄(연속체)"이라는 이름이 붙었는지 논리가 섭니다.

### Ⅱ. 3대 계층 — "엣·포·클" (Edge-Fog-Cloud)

| 계층              |                                위치 | 특징                                       |
| :-------------- | --------------------------------: | :--------------------------------------- |
| **엣지(Edge)**    |                 데이터발생지점(**최단거리**) | 센서/IoT기기 자체 또는 바로 옆 — **초저지연**, 자원 제한적   |
| **포그(Fog)**     | 엣지와 클라우드 **사이**(게이트웨이/라우터/사설클라우드) | 엣지의 연산뿐 아니라 **엣지→클라우드 전송과정까지 포함**(다리 역할) |
| **클라우드(Cloud)** |               중앙집중 **데이터센터**(원거리) | 자원 풍부, 대규모연산 가능, 단 **지연이 큼**             |

→ 암기: **"엣지는 현장에서 즉시(초저지연), 포그는 그 근처에서 중간처리(다리), 클라우드는 멀리서 크게(고성능)"** — 포그와 엣지의 차이가 헷갈리기 쉬운데, \*\*"포그는 엣지의 연산 + 클라우드까지 가는 네트워크 전송과정까지 포함하는 더 넓은 개념"\*\*이라는 게 핵심 구분점입니다.

### 도식화 제안

```
[엣지]────────[포그]────────[클라우드]
센서/IoT기기    게이트웨이/       중앙데이터센터
(현장, 즉시)    라우터/사설클라우드  (원거리, 대규모)
                (다리역할)
   ←──────── 지연 증가, 자원 증가 ────────→
   ←──────────── 컨티뉴엄(연속체) ────────────→
```

→ "이 스펙트럼이 3개의 뚝뚝 끊긴 단계가 아니라, **하나의 연속된 자원풀**로 관리된다"는 게 "컨티뉴엄"이라는 이름의 핵심 의미입니다.

### Ⅲ. 컨티뉴엄으로서의 특성 — 핵심 배점 포인트

**함정 방지: 그냥 "엣지+포그+클라우드가 있다"고 답하면 절반. "왜 이걸 굳이 컨티뉴엄(연속체)으로 봐야 하는가"의 논리가 핵심입니다.**

| 기존 관점의 한계                                | 컨티뉴엄 관점의 해법                               |
| :--------------------------------------- | :---------------------------------------- |
| 클라우드중심(CIoT)은 **지연증가·네트워크부하·프라이버시 문제**   | 데이터발생지점 근처(포그)에서 **선별적으로 분석**             |
| 엣지만 쓰면 **자원부족·신뢰성 문제**, 클라우드만 쓰면 **고지연** | 자원(엣지)-지연(클라우드) **트레이드오프를 동적으로 관리**       |
| 서버리스만 쓰면 **자원관리 제어권이 제한적**(공급자에 종속)      | 엣지+포그+클라우드를 **함께(in tandem) 활용**하는 유연한 배치 |

→ 암기: **"클라우드만 쓰면 느리고, 엣지만 쓰면 힘이 부족하니, 작업 특성에 맞게 그 사이 어디서든 처리할 수 있게 하자"** — 앞서 다룬 "멀티클라우드"(여러 CSP를 목적별로 병행)와 정확히 같은 논리가, 이번엔 "위치(거리)" 축에서 재현됩니다.

### Ⅳ. 워크로드 배치기준 및 오늘 시리즈 총연결

| 워크로드 특성                        | 배치위치                  | 오늘 다룬 연결답안                             |
| :----------------------------- | :-------------------- | :------------------------------------- |
| **초저지연 필수**(자율주행 제동, 실시간제어)    | **엣지**                | 앞서 다룬 "RM(실시간스케줄링)"의 마감시한 개념           |
| **국지적 집계·필터링**(공장의 여러센서 통합)    | **포그**                | "SQMS/MQMS"의 자원배분 문제와 유사(어디서 병목이 생기는가) |
| **대규모학습·장기저장**(AI모델훈련, 빅데이터분석) | **클라우드**              | "GPU/HBM/CXL" 답안의 대규모 연산인프라            |
| **간헐적·불규칙 트리거**                | **서버리스**(클라우드 내 특수배치) | 바로 앞서 다룬 "서버리스 컴퓨팅"                    |
| **배터리없는 초저전력센서**               | **엣지의 극단**            | 앞서 다룬 "인터미턴트컴퓨팅"·"뉴로모픽"                |

→ "오늘 다룬 뉴로모픽(저전력엣지), 인터미턴트컴퓨팅(전원제약엣지), 서버리스(클라우드의 간헐적실행), 멀티클라우드(자원분산)가 사실은 모두 이 컴퓨팅 컨티뉴엄이라는 하나의 큰 스펙트럼 위의 각기 다른 지점"이라는 게 이 답안의 핵심 통합 포인트입니다.

### 도식화 제안 (오늘 시리즈 총정리)

```
[엣지]──────────[포그]──────────[클라우드]
뉴로모픽,          국지적게이트웨이     GPU/HBM/CXL,
인터미턴트컴퓨팅                      서버리스,멀티클라우드
(저전력,초저지연)                     (고성능,대규모)
```

### Ⅴ. 결론 포인트 (오늘 미래컴퓨팅 시리즈 대단원)

컴퓨팅 컨티뉴엄은 \*\*"어디서(위치) 계산할 것인가"\*\*라는 질문에 대해, "엣지 아니면 클라우드"라는 이분법을 버리고 \*\*"작업의 지연요구·자원요구에 맞춰 연속된 스펙트럼 위의 최적점을 동적으로 선택한다"\*\*는 철학입니다 — 이는 오늘 다룬 뉴로모픽(저전력이벤트), 앰비언트컴퓨팅(환경에스며듦), 인터미턴트컴퓨팅(전원제약 극복), 서버리스(온디맨드실행)가 각자 다른 제약조건(전력/관리부담/비용) 위에서 발전해온 것을, **"위치"라는 하나의 통합축으로 다시 엮어내는 최상위 프레임워크**라는 결론으로, 오늘 하루 다룬 미래컴퓨팅 패러다임 시리즈 전체(뉴로모픽→양자컴퓨터→앰비언트→인터미턴트→서버리스→컴퓨팅컨티뉴엄)를 완결할 수 있습니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "과거에는 무조건 모든 데이터를 저 멀리 거대한 중앙의 '클라우드'로 쏴버렸다. 하지만 자율주행차가 초당 쏟아내는 기가바이트 단위의 데이터를 다 쏘다간 지연 시간(Latency) 때문에 차가 사고 나고 통신망이 마비된다. 그래서 단말기 근처에서 데이터를 처리하는 '엣지 컴퓨팅'이 나왔다. 하지만 엣지 단말은 성능이 부족해 무거운 딥러닝 학습을 돌리지 못한다. 결국 정답은 하나다. 내 손안의 초소형 '디바이스'부터, 동네 통신사 기지국의 '엣지', 그리고 저 멀리 있는 초거대 '클라우드'까지를 하나로 묶어 거대한 척추처럼 매끄럽게 연결하는 것이다. 바로 이것이 \*\*'컴퓨팅 컨티뉴엄(Computing Continuum)'\*\*이다. 컨티뉴엄은 '연속체'라는 뜻이다. 가벼운 얼굴 인식은 내 스마트폰이 즉시 처리하고, 버거운 동네 영상 분석은 기지국 엣지로 넘기며, 전국의 10년 치 빅데이터 학습은 중앙 클라우드로 넘긴다. 이렇게 단절 없이 상황에 따라 작업(워크로드)을 가장 효율적인 위치로 유연하게 던져주는(오프로딩) 지능형 분산 연산 생태계가 바로 미래의 인프라 구조다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 클라우드와 엣지의 한계를 넘은 융합 생태계, 컴퓨팅 컨티뉴엄 개요**

* **정의:** 데이터를 생성하는 가장 끝단의 \*\*디바이스(Device)\*\*부터 중간 거점인 **엣지(Edge)**, 그리고 거대한 중앙 \*\*클라우드(Cloud)\*\*에 이르기까지, 물리적으로 분산된 컴퓨팅 자원들이 **경계나 단절 없이(Seamless) 하나의 연속적인 연산 자원처럼 묶여 작동하는 융합 컴퓨팅 패러다임**.
* **등장 배경:** 클라우드의 극심한 통신 지연(Latency)과 트래픽 비용 폭증 문제, 그리고 엣지 디바이스의 제한된 연산력(배터리/메모리) 문제를 상호 보완하여, 워크로드를 동적으로 분배하기 위함.

#### **II. \[본론 1] 단절 없는(Seamless) 연산의 연속체 아키텍처 (도식화)**

작업의 크기와 지연 시간 민감도에 따라 연산의 위치가 연속적으로 흘러가는 모습을 그려줍니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMTMxLjMyNiAyODguMSIgd2lkdGg9IjExMzEuMzI2IiBoZWlnaHQ9IjI4OC4xIiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfX0NvbXB1dGluZ19Db250aW51dW1fIiBkYXRhLWxhYmVsPSLsu7Ttk6jtjIUg7Luo7Yuw64m07JeEIChDb21wdXRpbmcgQ29udGludXVtKSDwn5qAIj4KICA8cmVjdCB4PSI0MCIgeT0iMTA0LjkiIHdpZHRoPSIxMDUxLjMyNiIgaGVpZ2h0PSIxNDMuMiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSIxMDQuOSIgd2lkdGg9IjEwNTEuMzI2IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iMTE4LjkiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+7Lu07ZOo7YyFIOy7qO2LsOuJtOyXhCAoQ29tcHV0aW5nIENvbnRpbnV1bSkg8J+agDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRCIgZGF0YS10bz0iRSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i67KF7LCsIOyXsOyCsOydhArsg4HsnITroZwg64SY6rmAIChPZmZsb2FkaW5nKSIgcG9pbnRzPSIyNTIuOTcwMDAwMDAwMDAwMDMsMTk5LjY2NjY2NjY2NjY2NjY5IDI3Mi45NywxOTkuNjY2NjY2NjY2NjY2NjkgMjcyLjk3LDIxMC44NTAwMDAwMDAwMDAwMiA0NDUuODU2LDIxMC44NTAwMDAwMDAwMDAwMiA0NDUuODU2LDE5OS42NjY2NjY2NjY2NjY2OSA0ODEuODU2LDE5OS42NjY2NjY2NjY2NjY2OSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRSIgZGF0YS10bz0iQyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i66y06rGw7Jq0IOuUpeufrOuLnSDtlZnsirXsnYQK7KSR7JWZ7Jy866GcIOuEmOq5gCIgcG9pbnRzPSI3MDEuNjQ2LDE5OS42NjY2NjY2NjY2NjY2OSA3MTMuNjQ2LDE5OS42NjY2NjY2NjY2NjY2OSA3MTMuNjQ2LDIxNC41IDg4MS43OCwyMTQuNSA4ODEuNzgsMTk5LjY2NjY2NjY2NjY2NjY5IDkxNy43OCwxOTkuNjY2NjY2NjY2NjY2NjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkMiIGRhdGEtdG89IkUiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLqsIDrsrzsm4zsp4Qg7LaU66GgIOuqqOuNuOydhArtlZjsnITroZwg67Cw7Y+sIiBwb2ludHM9IjkxNy43OCwxODEuNzMzMzMzMzMzMzMzMzUgODgxLjc4LDE4MS43MzMzMzMzMzMzMzMzNSA4ODEuNzgsMTY2LjkgNzEzLjY0NiwxNjYuOSA3MTMuNjQ2LDE4MS43MzMzMzMzMzMzMzMzNSA3MDEuNjQ2LDE4MS43MzMzMzMzMzMzMzMzNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJFIiBkYXRhLXRvPSJEIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7KaJ6rCB7KCB7J24IO2UvOuTnOuwsSDsoITshqEiIHBvaW50cz0iNDgxLjg1NiwxODEuNzMzMzMzMzMzMzMzMzUgNDQ1Ljg1NiwxODEuNzMzMzMzMzMzMzMzMzUgNDQ1Ljg1NiwxNzAuNTUgMjcyLjk3LDE3MC41NSAyNzIuOTcsMTgxLjczMzMzMzMzMzMzMzM1IDI1Mi45NzAwMDAwMDAwMDAwMywxODEuNzMzMzMzMzMzMzMzMzUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJEIiBkYXRhLXRvPSJFIiBkYXRhLWxhYmVsPSLrsoXssKwg7Jew7IKw7J2ECuyDgeychOuhnCDrhJjquYAgKE9mZmxvYWRpbmcpIj4KICA8cmVjdCB4PSIzMDQuOTciIHk9IjE4Ny44NSIgd2lkdGg9IjEzMi44ODYiIGhlaWdodD0iNDQuNiIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzNzEuNDEzIiB5PSIyMTAuMTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSIzNzEuNDEzIiBkeT0iLTMuMzAwMDAwMDAwMDAwMDAwNyI+67KF7LCsIOyXsOyCsOydhDwvdHNwYW4+PHRzcGFuIHg9IjM3MS40MTMiIGR5PSIxNC4zIj7sg4HsnITroZwg64SY6rmAIChPZmZsb2FkaW5nKTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkUiIGRhdGEtdG89IkMiIGRhdGEtbGFiZWw9IuustOqxsOyatCDrlKXrn6zri50g7ZWZ7Iq17J2ECuykkeyVmeycvOuhnCDrhJjquYAiPgogIDxyZWN0IHg9Ijc0NS42NDYiIHk9IjE5MS41IiB3aWR0aD0iMTI4LjEzNDAwMDAwMDAwMDAxIiBoZWlnaHQ9IjQ0LjYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iODA5LjcxMyIgeT0iMjEzLjgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSI4MDkuNzEzIiBkeT0iLTMuMzAwMDAwMDAwMDAwMDAwNyI+66y06rGw7Jq0IOuUpeufrOuLnSDtlZnsirXsnYQ8L3RzcGFuPjx0c3BhbiB4PSI4MDkuNzEzIiBkeT0iMTQuMyI+7KSR7JWZ7Jy866GcIOuEmOq5gDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkMiIGRhdGEtdG89IkUiIGRhdGEtbGFiZWw9IuqwgOuyvOybjOynhCDstpTroaAg66qo64247J2ECu2VmOychOuhnCDrsLDtj6wiPgogIDxyZWN0IHg9Ijc0NS42NDYiIHk9IjE0My44OTk5OTk5OTk5OTk5OCIgd2lkdGg9IjEyOC4xMzQwMDAwMDAwMDAwMSIgaGVpZ2h0PSI0NC42IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjgwOS43MTMiIHk9IjE2Ni4yIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIj48dHNwYW4geD0iODA5LjcxMyIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPuqwgOuyvOybjOynhCDstpTroaAg66qo64247J2EPC90c3Bhbj48dHNwYW4geD0iODA5LjcxMyIgZHk9IjE0LjMiPu2VmOychOuhnCDrsLDtj6w8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJFIiBkYXRhLXRvPSJEIiBkYXRhLWxhYmVsPSLsponqsIHsoIHsnbgg7ZS865Oc67CxIOyghOyGoSI+CiAgPHJlY3QgeD0iMzA3LjM0NiIgeT0iMTU0LjU1IiB3aWR0aD0iMTI4LjEzNDAwMDAwMDAwMDAxIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzcxLjQxMyIgeT0iMTY5LjcwMDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7sponqsIHsoIHsnbgg7ZS865Oc67CxIOyghOyGoTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0OCIgeT0iNDAiIHdpZHRoPSI2OC42MjYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI4Mi4zMTMiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5Ob3RlPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJEIiBkYXRhLWxhYmVsPSIxLiBEZXZpY2UgLyBGYXIgRWRnZQoo7Iqk66eI7Yq47Y+wLCDsnpDsnKjso7ztlokg7IS87IScKSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0OCIgeT0iMTYzLjgiIHdpZHRoPSIyMDQuOTciIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE1MC40ODUiIHk9IjE5MC43MDAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTUwLjQ4NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPjEuIERldmljZSAvIEZhciBFZGdlPC90c3Bhbj48dHNwYW4geD0iMTUwLjQ4NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+KOyKpOuniO2KuO2PsCwg7J6Q7Jyo7KO87ZaJIOyEvOyEnCk8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRSIgZGF0YS1sYWJlbD0iMi4gRWRnZSAvIEZvZyAvIE1FQwoo7Ya17Iug7IKsIOq4sOyngOq1rSwg6rKM7J207Yq47Juo7J20KSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0ODEuODU2IiB5PSIxNjMuOCIgd2lkdGg9IjIxOS43ODk5OTk5OTk5OTk5NiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNTkxLjc1MSIgeT0iMTkwLjcwMDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI1OTEuNzUxIiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+Mi4gRWRnZSAvIEZvZyAvIE1FQzwvdHNwYW4+PHRzcGFuIHg9IjU5MS43NTEiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPijthrXsi6Dsgqwg6riw7KeA6rWtLCDqsozsnbTtirjsm6jsnbQpPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkMiIGRhdGEtbGFiZWw9IjMuIENlbnRyYWwgQ2xvdWQKKEFXUywg642w7J207YSw7IS87YSwKSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI5MTcuNzgiIHk9IjE2My44IiB3aWR0aD0iMTU3LjU0NiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI5OTYuNTUzIiB5PSIxOTAuNzAwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9Ijk5Ni41NTMiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj4zLiBDZW50cmFsIENsb3VkPC90c3Bhbj48dHNwYW4geD0iOTk2LjU1MyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+KEFXUywg642w7J207YSw7IS87YSwKTwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 컴퓨팅 컨티뉴엄을 구성하는 3대 계층과 최적 역할 분담표 (출제 포인트)**

| **계층 (Layer)**                     | **주요 구성 요소 및 특징**                                 | **컨티뉴엄 내에서의 핵심 역할 분담**                                                    |
| :--------------------------------- | :------------------------------------------------ | :------------------------------------------------------------------------ |
| **1. 디바이스 엣지** (Device Edge)       | 센서, 로봇, 자율주행차, 스마트폰 등 데이터가 생성되는 **가장 끝단 물리적 기기.** | - 1ms 이내의 찰나의 **초실시간 반응 요구.** - 가벼운 데이터 수집 및 온디바이스(On-device) AI 추론 연산.   |
| **2. 포그 / 엣지 노드** (Fog / MEC Edge) | 동네 통신사 기지국(MEC), 공장 내 라우터/게이트웨이 등 **중간 거점 인프라.**  | - 디바이스와 클라우드 사이의 버퍼 역할. - 클라우드로 갈 불필요한 트래픽 필터링 및 **민감 개인정보 제거 후 요약본 전송.** |
| **3. 중앙 클라우드** (Central Cloud)     | AWS, Azure 등 **무한에 가까운 자원을 가진 거대 데이터센터 인프라.**     | - 지연 시간은 다소 길어도 무방한 **거대 AI 모델의 분산 학습(Training) 및 장기 빅데이터 아카이빙** 처리.      |

#### **IV. \[결론/제언] 성공적 컨티뉴엄을 위한 '지능형 오프로딩(Offloading)'과 오케스트레이션**

* **(키워드 위주 2줄 마무리)** "컴퓨팅 컨티뉴엄이 완벽히 작동하려면, 현재 앱이 돌아가는 디바이스의 배터리가 부족할 때 그 연산(워크로드)을 실시간으로 기지국 엣지로 부드럽게 넘겨주는 **'지능형 워크로드 오프로딩(Offloading)'** 기술이 필수적입니다. 이를 위해 수만 개의 엣지와 클라우드 노드를 중앙에서 하나의 오케스트라처럼 지휘하는 **'Edge Kubernetes(K8s)' 기반의 분산 컨테이너 관리 아키텍처**가 6G 통신망의 가장 중요한 인프라 기술로 대두되고 있습니다."
