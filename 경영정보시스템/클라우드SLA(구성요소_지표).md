클라우드 SLA는 앞서 다룬 IT투자평가(정량/정성)와 구조가 비슷합니다. **"약속(구성요소) + 증명(지표) + 어길 때(패널티)"** 3단으로 짜면, SLA 문서 하나를 통째로 외우지 않고도 답안이 완성됩니다.

### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (클라우드 SLA 정의, 온프레미스 SLA와의 차이) — 3~4줄
Ⅱ. SLA 구성요소 (본론①, 도식 1개)
Ⅲ. SLA 핵심지표 (본론②, 계산예시 포함)
Ⅳ. 패널티/보상체계 및 고려사항
Ⅴ. 결론
```

포인트: 개요에서 "클라우드는 공급자·이용자 간 물리적 통제권이 분리되어 있어 **SLA가 신뢰의 유일한 계약적 근거**"라는 한 줄을 넣으면, 왜 SLA가 온프레미스보다 더 중요한지 논리가 섭니다.

### Ⅱ. SLA 구성요소 — "정·측·보·검" (4대 구성)

| 구성요소                            | 핵심내용                               |
| :------------------------------ | :--------------------------------- |
| **서비스 정의** (Service Definition) | 제공 서비스 범위, 책임분계점(공급자 vs 이용자 책임 경계) |
| **측정기준** (Measurement)          | 지표별 산정공식, 측정주기, 측정도구/방법            |
| **보상/패널티** (Remedy)             | 목표 미달 시 서비스크레딧(비용환급) 등 보상          |
| **검토/보고** (Reporting & Review)  | 정기 리포팅 주기, SLA 재검토(갱신) 절차          |

→ 암기: **"뭘 해주고(정의), 어떻게 재고(측정), 못 지키면 어떻게 물어주고(보상), 어떻게 확인하는지(검토)"** 4문장으로 압축.

**+ 책임분계점(RACI 유사개념) — 자주 나오는 함정포인트**

클라우드 서비스모델(IaaS/PaaS/SaaS)에 따라 **공급자-이용자 책임범위가 다르다**는 점(공동책임모델, Shared Responsibility Model)을 여기서 한 줄 넣으면 심화 배점을 받습니다.

```
IaaS: 공급자(인프라~하이퍼바이저) / 이용자(OS~애플리케이션~데이터)
PaaS: 공급자(~런타임/OS) / 이용자(애플리케이션~데이터)
SaaS: 공급자(~애플리케이션) / 이용자(데이터~접근관리)
```

### Ⅲ. SLA 핵심지표 — "가·성·안·지" (4대 지표군)

| 지표군                      | 대표지표                                 | 계산/의미                                            |
| :----------------------- | :----------------------------------- | :----------------------------------------------- |
| **가용성** (Availability)   | **Uptime %**                         | (전체시간-장애시간)/전체시간 ×100 — 흔히 "몇 나인(Nine)"으로 표현     |
| **성능** (Performance)     | 응답시간(Response Time), 처리량(Throughput) | 요청-응답 지연, 초당 처리건수                                |
| **안정성/복구** (Reliability) | **MTTR/MTBF**                        | MTTR(평균복구시간)=총복구시간/장애건수, MTBF(평균고장간격)=총가동시간/장애건수 |
| **지원** (Support)         | 응답시간(Response), 해결시간(Resolution)     | 장애등급별 초기대응·해결 목표시간(예: Critical 15분 내 대응)         |

→ 암기: **"떠있나(가용성), 빠른가(성능), 잘 버티나(안정성), 도와주나(지원)"** 4질문으로 압축.

**가용성 "나인(Nine)" 표 — 계산문제 대비 필수**

| 가용성              | 연간 다운타임  |
| :--------------- | :------- |
| 99% (2 Nine)     | 약 3.65일  |
| 99.9% (3 Nine)   | 약 8.76시간 |
| 99.99% (4 Nine)  | 약 52.6분  |
| 99.999% (5 Nine) | 약 5.26분  |

→ "9가 하나 늘 때마다 다운타임이 약 1/10로 줄어든다"는 감각만 있으면 계산문제 대응 가능합니다.

### 도식화 제안

```
        [클라우드 SLA]
   ┌──────┴──────┐
[구성요소]        [지표]
정의/측정/         가용성(Uptime)
보상/검토          성능(응답시간)
                  안정성(MTTR/MTBF)
                  지원(대응/해결시간)
        ↓
  [미달 시 서비스크레딧 보상]
```

### Ⅳ. 패널티/보상체계 및 고려사항 (실무 배점)

* **서비스크레딧(Service Credit)**: 목표 미달 시 이용료의 일정 % 환급 (직접 손해배상이 아닌 크레딧 방식이 일반적)
* **측정 예외조항**: 계획된 유지보수(Scheduled Maintenance), 이용자 과실, 천재지변 등은 다운타임 산정에서 제외 — **이 예외조항 범위를 명확히 계약서에 규정해야 분쟁예방**
* **다중 SLA 계층**: IaaS(인프라 가용성) + PaaS/SaaS(애플리케이션 가용성)가 중첩되므로, **전체 서비스 체인의 종단간(End-to-End) 가용성**은 개별 SLA의 곱으로 낮아진다는 점(예: 99.99%×99.9%<99.9%) — 심화 포인트

### Ⅴ. 결론 포인트 (차별화 한 줄)

SLA는 "숫자로 약속받는 것"이지만, 실제 리스크관리는 **단일 지표(가용성)만 보지 말고 MTTR·지원지표까지 종합적으로 평가**해야 한다는 점 — 가용성 99.99%라도 MTTR이 길면 1회 장애의 업무영향이 크다는 논리를 넣으면, 앞서 다룬 리스크관리 답안과도 자연스럽게 연결됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "클라우드를 도입할 때 벤더(AWS, Azure 등)가 알아서 잘 해줄 것이라고 믿으면, 장애 발생 시 엄청난 피해를 고스란히 떠안게 된다. 클라우드 서비스는 눈에 보이지 않기 때문에, 서비스 수준을 객관적으로 보장하는 \*\*'SLA 계약'\*\*이 필수적이다. 성공적인 SLA를 맺으려면 측정 지표인 **'SLI'**, 달성해야 할 목표치인 **'SLO'**, 그리고 목표 미달 시 벤더가 물어내야 할 보상/페널티 조항을 명확히 구성해야 하며, 특히 클라우드 특성에 맞는 **가용성(99.99%)과 데이터 복원력(RTO/RPO) 지표**를 꼼꼼히 챙겨야 한다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 클라우드 서비스 신뢰성의 최후 보루, 클라우드 SLA 개요**

* **정의:** 클라우드 서비스 제공자(CSP)와 이용자(CSC) 간에 제공될 서비스의 수준(가용성, 성능, 보안 등)과 측정 방법, 그리고 목표 미달 시의 보상 체계를 명시한 **공식적인 합의(계약)**.
* **목적:** 서비스 품질에 대한 상호 간의 기대치 일치, 장애 발생 시 책임 소재 명확화, 벤더 종속성(Lock-in) 방지 및 분쟁 예방.

#### **II. \[본론 1] 클라우드 SLA의 3대 핵심 구성요소 (포함 관계 도식화)**

이 부분은 SRE(사이트 신뢰성 공학)에서 강조하는 **SLI < SLO < SLA 의 포함 관계**를 명확히 보여주는 것이 고득점 포인트입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NjQuNzE3OTk5OTk5OTk5OTYgMzkyLjEiIHdpZHRoPSI0NjQuNzE3OTk5OTk5OTk5OTYiIGhlaWdodD0iMzkyLjEiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9TTEFfX19fIiBkYXRhLWxhYmVsPSLtgbTrnbzsmrDrk5wgU0xBIO2VteyLrCDqtazshLHsmpTshowgKO2PrO2VqCDqtIDqs4QpIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIzODQuNzE3OTk5OTk5OTk5OTYiIGhlaWdodD0iMzEyLjEiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIzODQuNzE3OTk5OTk5OTk5OTYiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7tgbTrnbzsmrDrk5wgU0xBIO2VteyLrCDqtazshLHsmpTshowgKO2PrO2VqCDqtIDqs4QpPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTTE8iIGRhdGEtdG89IlNMQSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxMjQuNjI1OTk5OTk5OTk5OTksMzAwLjc1IDE3Mi42MjU5OTk5OTk5OTk5OCwzMDAuNzUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlNMSSIgZGF0YS1sYWJlbD0iMS4gU0xJICjsp4DtkZwpCuustOyXh+ydhCDsuKHsoJXtlaAg6rKD7J246rCAPwoo7JiIOiDsl5Drn6zsnKgsIOydkeuLteyLnOqwhCkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMTg3LjE4NTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UzZjJmZCIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxNDkuNTkzIiB5PSIxMTkuMzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE0OS41OTMiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj4xLiBTTEkgKOyngO2RnCk8L3RzcGFuPjx0c3BhbiB4PSIxNDkuNTkzIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rrLTsl4fsnYQg7Lih7KCV7ZWgIOqyg+yduOqwgD88L3RzcGFuPjx0c3BhbiB4PSIxNDkuNTkzIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj4o7JiIOiDsl5Drn6zsnKgsIOydkeuLteyLnOqwhCk8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iLS0iIGRhdGEtbGFiZWw9IiBTTE9bJnF1b3Q7Mi4gU0xPICjrqqntkZwpCuyWtOuKkCDsiJjspIDquYzsp4Ag64us7ISx7ZWgIOqyg+yduOqwgD8KKOyYiDog6rCA64+Z66WgIDk5LjklIOuztOyepSkmcXVvdDsiIGRhdGEtc2hhcGU9ImFzeW1tZXRyaWMiPgogIDxwb2x5Z29uIHBvaW50cz0iNjgsMTc0LjcgMzAxLjg2OSwxNzQuNyAzMDEuODY5LDI0NS4zOTk5OTk5OTk5OTk5OCA2OCwyNDUuMzk5OTk5OTk5OTk5OTggNTYsMjEwLjA0OTk5OTk5OTk5OTk4IiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTc4LjkzNDUiIHk9IjIxMC4wNDk5OTk5OTk5OTk5OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTc4LjkzNDUiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj4gU0xPWyZxdW90OzIuIFNMTyAo66qp7ZGcKTwvdHNwYW4+PHRzcGFuIHg9IjE3OC45MzQ1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7slrTripAg7IiY7KSA6rmM7KeAIOuLrOyEse2VoCDqsoPsnbjqsIA/PC90c3Bhbj48dHNwYW4geD0iMTc4LjkzNDUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPijsmIg6IOqwgOuPmeuloCA5OS45JSDrs7TsnqUpJnF1b3Q7PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlNMTyIgZGF0YS1sYWJlbD0iU0xPIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIyODIuMyIgd2lkdGg9IjY4LjYyNTk5OTk5OTk5OTk5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjkwLjMxMjk5OTk5OTk5OTk5IiB5PSIzMDAuNzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlNMTzwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU0xBIiBkYXRhLWxhYmVsPSIzLiBTTEEgKOqzhOyVvS/rs7Tsg4EpCuuvuOuLrCDsi5wg7Ja065a76rKMIOyxheyehOyniCDqsoPsnbjqsIA/CijsmIg6IOyalOq4iOydmCAxMCUg7YGs66CI65SnIO2ZmOu2iCkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTcyLjYyNTk5OTk5OTk5OTk4IiB5PSIyNjUuNCIgd2lkdGg9IjIzNi4wOTE5OTk5OTk5OTk5NiIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmY2U0ZWMiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMjkwLjY3MTk5OTk5OTk5OTk3IiB5PSIzMDAuNzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjI5MC42NzE5OTk5OTk5OTk5NyIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPjMuIFNMQSAo6rOE7JW9L+uztOyDgSk8L3RzcGFuPjx0c3BhbiB4PSIyOTAuNjcxOTk5OTk5OTk5OTciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuuvuOuLrCDsi5wg7Ja065a76rKMIOyxheyehOyniCDqsoPsnbjqsIA/PC90c3Bhbj48dHNwYW4geD0iMjkwLjY3MTk5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj4o7JiIOiDsmpTquIjsnZggMTAlIO2BrOugiOuUpyDtmZjrtogpPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

* **추가 필수 구성요소:** 서비스 카탈로그(제공 서비스 명세), 서비스 측정 및 보고 방법론, 면책 조항(예: 고객 측 실수로 인한 장애는 보상 제외).

#### **III. \[본론 2] 클라우드 특화 핵심 SLA 관리 지표 (Metrics)**

온프레미스(자체 구축)와 구별되는 클라우드만의 핵심 관리 지표를 4가지 관점으로 나누어 제시합니다.

| **관점**                 | **세부 측정 지표 (Metrics)**                                   | **측정 기준 및 클라우드 특성 반영**                                                                             |
| :--------------------- | :------------------------------------------------------- | :------------------------------------------------------------------------------------------------- |
| **가용성** (Availability) | **- 서비스 가동률 (Uptime)** - MTBF (무고장 시간) - MTTR (평균 수리 시간) | - 클라우드 SLA에서 **가장 중요한 1순위 지표 (예: 99.99% '4 Nines' 보장)** - 월/연간 허용 가능한 최대 중단 시간(Downtime)으로 환산하여 측정 |
| **성 능** (Performance)  | **- 응답 시간 (Response Time)** - 처리량 (Throughput)           | - 오토 스케일링(Auto Scaling) 발동 시 지연 시간 초과 여부 측정 - 초당 트랜잭션 처리량(TPS) 보장 여부                               |
| **보안 및** **복원력**       | **- RPO (복구 목표 시점)** **- RTO (복구 목표 시간)** - 침해사고 대응 시간   | - 데이터 유실 허용 한계(RPO) 및 서비스 복구 소요 시간(RTO) 명시 - 랜섬웨어 등 보안 인시던트 발생 시 초기 보고 및 차단 시간                     |
| **고객 지원** (Support)    | **- 최초 응답 시간 (Initial Response)** - 장애 해결 완료 시간          | - 티켓(이슈) 접수 후 고객센터 지원팀이 개입하는 데 걸리는 시간 - 장애 등급(Severity 1\~4)별로 보장 시간을 차등 적용                        |

#### **IV. \[결론/제언] 성공적인 클라우드 SLA를 위한 멀티 클라우드 관리 전략**

* **(키워드 위주 2줄 마무리)** "최근 벤더 종속성을 피하기 위해 AWS, Azure 등을 혼용하는 멀티/하이브리드 클라우드 도입이 대세입니다. 이에 따라 각기 다른 CSP의 SLA를 통합 모니터링하고 일관된 서비스 수준을 보장받을 수 있도록, **클라우드 서비스 브로커리지(CSB)의 활용과 통합 CMP(Cloud Management Platform) 구축**이 필수적으로 병행되어야 합니다."
