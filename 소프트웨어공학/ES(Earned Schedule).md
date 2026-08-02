#### **EVM의 일정 통제 한계 극복: ES (Earned Schedule)**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 SV·SPI는 프로젝트 후반부에 왜곡되는가)
Ⅱ. EVM의 일정 지표 한계
Ⅲ. ES(Earned Schedule) 핵심 원리 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 DORA 지표·심리적 안전감이 '애자일 개발팀의 성과 측정'을 다뤘다면, ES(Earned Schedule)는 전통적 프로젝트 관리 방법론인 EVM(Earned Value Management)의 오래된 통계적 결함을 보완하는 개념이다 — EVM은 획득가치(EV)에서 계획가치(PV)를 빼거나 나눠 일정 성과(SV·SPI)를 '금액(원화·달러)' 단위로 표현하는데, 이 방식은 프로젝트가 종료 시점에 다가갈수록 모든 작업이 결국 100% 완료되어 EV가 강제로 PV에 수렴하면서 실제로는 몇 달이나 지연되고 있어도 SV·SPI가 마치 정상인 것처럼 보이는 심각한 왜곡 현상을 낳으며, 2003년 Walt Lipke가 제안한 ES는 이 금액 단위의 일정 지표를 '시간(기간)' 단위로 재정의해 프로젝트 전체 기간에 걸쳐 신뢰할 수 있는 일정 통제 지표를 제공하는 것"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDU3LjM4OCAyMDEuOCIgd2lkdGg9IjEwNTcuMzg4IiBoZWlnaHQ9IjIwMS44IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkVWTSIgZGF0YS10bz0iRmFpbCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyNzguODI4OTk5OTk5OTk5OTUsNzYuOSAyNzguODI4OTk5OTk5OTk5OTUsMTI0LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkVTIiBkYXRhLXRvPSJGaXgiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNzgxLjUyMjk5OTk5OTk5OTksNzYuOSA3ODEuNTIyOTk5OTk5OTk5OCwxMjQuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRVZNIiBkYXRhLWxhYmVsPSLsoITthrXsoIEgRVZNIDog67mE7JqpIOuLqOychCDsnbzsoJUg7Ya17KCcLCDtlITroZzsoJ3tirgg7ZuE67CY67aAIFNWPTAgLyBTUEk9MS4wIOyZnOqzoSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI0NzcuNjU3OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjc4LjgyODk5OTk5OTk5OTk1IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7KCE7Ya17KCBIEVWTSA6IOu5hOyaqSDri6jsnIQg7J287KCVIO2GteygnCwg7ZSE66Gc7KCd7Yq4IO2bhOuwmOu2gCBTVj0wIC8gU1BJPTEuMCDsmZzqs6E8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkZhaWwiIGRhdGEtbGFiZWw9Iu2VnOqzhCA6IOyZhOujjCDsi5zsoJAg7KeA7JewIOywqeyLnCDrsJzsg50iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTYwLjc4Mjk5OTk5OTk5OTk2IiB5PSIxMjQuOSIgd2lkdGg9IjIzNi4wOTE5OTk5OTk5OTk5OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI3OC44Mjg5OTk5OTk5OTk5NSIgeT0iMTQzLjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7tlZzqs4QgOiDsmYTro4wg7Iuc7KCQIOyngOyXsCDssKnsi5wg67Cc7IOdPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJFUyIgZGF0YS1sYWJlbD0i7ZqN65Od7J287KCV67KVIEVTIDogRVbrpbwg7Iuc6rCEIOy2lSBQViDsu6TruIzroZwg66ek7ZWRLCDsi6TsoJwg6rK96rO87Iuc6rCEIEFEIOuMgOyhsCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NDUuNjU3OTk5OTk5OTk5OSIgeT0iNDAiIHdpZHRoPSI0NzEuNzI5OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI3ODEuNTIyOTk5OTk5OTk5OSIgeT0iNTguNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPu2ajeuTneydvOygleuylSBFUyA6IEVW66W8IOyLnOqwhCDstpUgUFYg7Luk67iM66GcIOunpO2VkSwg7Iuk7KCcIOqyveqzvOyLnOqwhCBBRCDrjIDsobA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkZpeCIgZGF0YS1sYWJlbD0i7ZW06rKwIDog7Iuc6rCEIOuLqOychCDsoJXrsIAg7KeA7ZGcIFNWIHQsIFNQSSB0IOyCsOy2nCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI2MzUuMzE4OTk5OTk5OTk5OCIgeT0iMTI0LjkiIHdpZHRoPSIyOTIuNDA3OTk5OTk5OTk5OTYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI3ODEuNTIyOTk5OTk5OTk5OCIgeT0iMTQzLjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7tlbTqsrAgOiDsi5zqsIQg64uo7JyEIOygleuwgCDsp4DtkZwgU1YgdCwgU1BJIHQg7IKw7LacPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

***

#### Ⅱ. EVM의 일정 지표 한계

**가. 기존 EVM 일정 지표 정의**

```
[EVM 3대 기본 지표]

PV(Planned Value)  : 특정 시점까지 계획된 작업의 가치
EV(Earned Value)    : 특정 시점까지 실제 완료된 작업의 가치
AC(Actual Cost)     : 특정 시점까지 실제 지출된 비용

기존 일정 지표:
  SV(Schedule Variance) = EV - PV
  SPI(Schedule Performance Index) = EV / PV

  SV > 0 또는 SPI > 1 → 일정 앞섬
  SV < 0 또는 SPI < 1 → 일정 지연
```

**나. 프로젝트 종료 시점 수렴 문제**

```
[EVM 왜곡 현상: 종료 시점의 강제 수렴]

프로젝트 진행 흐름(가치 기준 그래프):

가치
100%│                          ┌──PV(계획)
    │                      ┌───┘
    │                  ┌───┘  ┌──EV(실제, 지연 중)
    │              ┌───┘  ┌───┘
    │          ┌───┘  ┌───┘
    │      ┌───┘  ┌───┘
    │  ┌───┘  ┌───┘
    └──┴──────┴─────────────────→ 시간
       현재    프로젝트 종료 시점

핵심 문제:
  프로젝트가 아무리 지연되어도 결국 종료 시점에는
  모든 작업이 100% 완료(EV=PV=BAC)될 수밖에 없음

  → 종료 시점 근접 시 SV → 0, SPI → 1로 강제 수렴 🚨
  → "실제로는 6개월 지연됐는데 SPI는 정상처럼 보임" 왜곡 발생
  → 프로젝트 후반부일수록 SV·SPI의 신뢰도가 급격히 하락
```

**다. 근본 원인: 단위의 부적절성**

| 문제               | 내용                                                      |
| :--------------- | :------------------------------------------------------ |
| **차원의 불일치**      | SV·SPI는 '가치(금액)' 단위로 '시간(일정)'을 표현하려는 근본적 모순             |
| **비선형 작업량 왜곡**   | 프로젝트 후반부에 저비용 작업이 몰려 있으면 EV가 실제 진도보다 빠르게 증가해 SPI가 과대평가됨 |
| **종료 근접 시 무의미화** | 프로젝트가 90% 이상 진행되면 SV·SPI는 사실상 통제 정보로서 가치를 상실            |

***

#### Ⅲ. ES(Earned Schedule) 핵심 원리 및 적용 체계

**가. ES 핵심 정의 및 산출 방식**

```
[ES 산출 원리: 가치를 시간으로 역산]

현재 시점의 EV 값을 찾은 뒤,
"계획(PV) 곡선에서 동일한 가치에 도달했던 시점"이 언제인지 역산

가치
100%│         ┌──PV(계획 곡선)
    │      ┌──┘
    │   ┌──┘←────────┐ 동일 가치 수준
    │┌──┘             │
    └┴────────────────┴──────→ 시간
     ES시점(과거)      현재시점(AT)
     "계획상 이 가치에      "실제로 지금
      도달했어야 할 시점"    이 가치에 도달"

ES = "현재 EV와 동일한 가치를 PV 곡선에서 찾았을 때의 시간 좌표"

→ 시간(개월·주·일) 단위로 표현되는 완전히 새로운 접근
```

**나. ES 기반 신규 일정 지표**

| 지표                      | 산출식                  | 의미                                        |
| :---------------------- | :------------------- | :---------------------------------------- |
| **ES(Earned Schedule)** | PV 곡선 역산으로 산출되는 시간값  | "실제 진도가 계획상 몇 시점에 해당하는가"                  |
| **AT(Actual Time)**     | 현재 실제 경과 시간          | 현재 시점 그 자체                                |
| **SV(t) (시간 기준 일정차이)**  | **SV(t) = ES - AT**  | 시간 단위 지연/선행량(예: -2개월 = 2개월 지연)            |
| **SPI(t) (시간 기준 일정지수)** | **SPI(t) = ES / AT** | 1.0 미만이면 지연, 1.0 이상이면 앞섬(종료 시점에도 왜곡 없음 ✅) |

**다. 기존 EVM 지표 vs ES 지표 비교**

| 비교 항목          | 기존 SV/SPI(가치 기준)                 | ES 기반 SV(t)/SPI(t)(시간 기준)                                 |
| :------------- | :------------------------------- | :-------------------------------------------------------- |
| **측정 단위**      | 금액(원·달러)                         | **시간(월·주·일)** ✅                                           |
| **직관적 해석**     | "얼마만큼의 가치가 차이 나는가"               | **"몇 개월 지연/선행되었는가"** ✅                                    |
| **프로젝트 종료 시점** | SV→0, SPI→1로 강제 수렴, **왜곡 심각** 🚨 | **끝까지 신뢰할 수 있는 지표 유지** ✅                                  |
| **비선형 작업량 영향** | 후반부 저비용 작업 몰림에 취약 🚨             | 시간 축으로 환산되어 왜곡 완화                                         |
| **경영진 보고 용이성** | "SPI 0.85가 무슨 의미인가" 직관적이지 않음     | **"3개월 지연 중"으로 즉각 이해 가능** ✅                               |
| **표준 채택**      | PMBOK 전통적 핵심 지표                  | College of Performance Management(CPM) 인증, PMI 확장 실무지침 채택 |

**라. 실무 적용 절차**

| 단계                            | 내용                                                    |
| :---------------------------- | :---------------------------------------------------- |
| **①PV 곡선 확보**                 | 프로젝트 기준선(Baseline)의 시간별 누적 PV 곡선 준비                   |
| **②현재 EV 측정**                 | 보고 시점까지의 실제 획득가치 산출(기존 EVM과 동일)                       |
| **③ES 역산**                    | EV와 동일한 값을 PV 곡선에서 찾아 해당 시간 좌표를 선형보간으로 산출             |
| **④SV(t)/SPI(t) 계산**          | ES와 AT의 차이·비율로 시간 기준 일정 성과 산출                         |
| **⑤TSPI(To-Complete SPI) 활용** | 목표 완료일 달성을 위해 남은 기간 동안 필요한 성과율 예측(EVM의 TCPI와 대응되는 개념) |

***

**(제언)** "ES의 진정한 가치는 복잡한 신규 수학을 도입한 것이 아니라, 이미 수집하고 있던 동일한 EV·PV 데이터를 '가치'가 아닌 '시간'이라는 더 적절한 축으로 재해석했을 뿐이라는 점에서 최소한의 추가 데이터 수집 부담으로 EVM의 가장 치명적인 약점을 보완한 실용적 개선이며, 특히 프로젝트가 후반부에 접어들수록 SV·SPI가 무의미해지는 시점에 정확히 ES 지표가 진가를 발휘하므로 두 지표를 배타적으로 선택하기보다 프로젝트 초중반에는 기존 SV·SPI로 원가 대비 진도의 큰 흐름을 파악하고 후반부로 갈수록 ES 기반 SV(t)·SPI(t)의 비중을 높여가는 이원화된 통제 전략이 실무적으로 가장 신뢰도 높은 일정 관리 체계이며, 국내 공공 SI 사업에서도 EVM 기반 진도관리가 의무화된 사업이라면 후반부 보고서에 ES 지표를 병기해 경영진과 발주기관에 더 직관적이고 왜곡 없는 일정 상황을 전달하는 것이 프로젝트 리스크 관리의 핵심 실무 전략입니다.

***

**앞서 다룬 개념과의 연결**

| 연계 개념                  | 연결 내용                                                      |
| :--------------------- | :--------------------------------------------------------- |
| **DORA 지표**            | 애자일 환경의 리드타임이 전통 프로젝트 관리의 ES와 유사한 문제의식(왜곡 없는 시간 기준 통제)을 공유 |
| **SAFe**               | PI 단위의 대규모 프로그램 일정 관리에 ES 개념을 결합해 다중 ART 진척도 통제 가능         |
| **ISO/IEC/IEEE 29148** | 요구사항 변경관리가 PV 기준선의 안정성에 직접 영향을 미쳐 ES 산출 정확도와 연계            |
| **심리적 안전감**            | 지연 상황을 왜곡 없이 조기에 드러내는 ES 지표 문화가 블레임리스 보고 문화와 상호 강화         |

### **I. EVM 일정 통제의 왜곡과 ES(Earned Schedule)의 개요**

전통적인 획득가치관리(EVM)는 프로젝트의 일정 성과를 계획가치(PV)와 획득가치(EV)의 화폐(원화) 차이로 계산합니다. 이로 인해 프로젝트 후반부로 갈수록 실제 일정이 아무리 지연되어도 획득가치(EV)가 결국 완성 예산(BAC)에 도달하면서 **일정 편차(SV)가 0으로 수렴하고 일정수행지표(SPI)가 1.0으로 정상화되는 심각한 수리적 왜곡 현상**이 발생합니다. \*\*ES(Earned Schedule, 획득일정법)\*\*는 EVM의 금액 가치를 '물리적 시간(Time)' 축으로 매핑하여 프로젝트 완료 시점 이후에도 일정 지연 상태를 왜곡 없이 통제하는 확장 기법입니다.

***

### **II. 비용 기반 EVM의 2대 한계 및 ES의 산출 메커니즘**

#### **1. 전통적 비용 기반 EVM의 2대 한계점**

* **완료 시점 왜곡 현상 (EVM Anomaly)**: 프로젝트가 계획 기간(PD*PD*)을 초과하여 심각하게 지연되더라도, 최종 작업을 완료하면 무조건 EV=PV*EV*=*PV*가 되어 SV=0*SV*=0, SPI=1.0*SPI*=1.0으로 정상 완료된 것처럼 수치가 조작 및 착각됩니다.
* **직관성 결여**: 일정 지연을 "일정이 1억 원만큼 늦어졌다"라고 표현하여, 현장 관리자(PM)가 물리적 시간(주, 월)으로 지연 속도를 파악하기 어렵습니다.

#### **2. 획득일정법(ES)의 수리적 도출 메커니즘**

* **ES (Earned Schedule) 정의**: 현재 시점의 EV*EV*가 계획 S-Curve(PV*PV*) 상에서 몇 번째 달에 달성되었는지 역산한 **시간 가치**입니다.
* **핵심 지표 산출 수식**:

| **지표명 🔑**                          | **🏁 계산 수식 🚨**                               | **💯 현장 통제 의미**                                       |
| :---------------------------------- | :-------------------------------------------- | :---------------------------------------------------- |
| **SV(t)*SV*(*t*)** (시간 일정 편차)       | SV(t)=ES−ADSV(t)=ES−AD (AD*AD*: 실제 경과시간)      | 0보다 크면 일정 조기 달성, 0보다 작으면 **실제 지연된 물리적 시간(주/월)** 산출    |
| **SPI(t)*SPI*(*t*)** (시간 일정 지표)     | SPI(t)=ES/ADSPI(t)=ES/AD                      | 1.0 미만 시 지연 상태. 프로젝트 후반부 및 지연 완료 후에도 **1미만 수치 지속 보존** |
| **IEAC(t)*IEAC*(*t*)** (최종 완료 소요시간) | IEAC(t)=AD+PD−ESSPI(t)IEAC(t)=AD+SPI(t)PD−ES​ | 현재 추세를 반영하여 최종 프로젝트가 완료될 **정확한 총 소요 시간(달력 기준) 예측**    |

***

### **III. 전통적 EVM 일정 통제와 획득일정법(ES)의 상세 비교**

| **비교 항목**                   | **💵 전통적 EVM 일정 통제**                              | **⏱️ 획득일정법 (ES - Earned Schedule)**                                       |
| :-------------------------- | :------------------------------------------------ | :------------------------------------------------------------------------ |
| **일정 측정 단위**                | 화폐 가치 단위 (원, 달러 등)                                | **물리적 시간 단위 (월, 주, 일 등)**                                                 |
| **후반부 수치 왜곡**               | 지연되더라도 완료 시 SV→0,SPI→1.0*SV*→0,*SPI*→1.0 왜곡       | **프로젝트 완료 후에도 SV(t)<0,SPI(t)<1.0*SV*(*t*)<0,*SPI*(*t*)<1.0 지연 보존**        |
| **일정 지표 수식**                | SV=EV−PV*SV*=*EV*−*PV* / SPI=EV/PV*SPI*=*EV*/*PV* | **SV(t)=ES−AD*SV*(*t*)=*ES*−*AD*** **/ SPI(t)=ES/AD*SPI*(*t*)=*ES*/*AD*** |
| **계획 초과 시(AD>PD*AD*>*PD*)** | 일정 지표 지수 계산 불가능 및 무력화                             | **완료 예정일 초과 후에도 유효한 시간 지표 계산 지속 가능**                                      |
| **PM의 직관적 해석**              | "일정이 5천만 원 지연되었다" (직관성 결여)                        | **"일정이 3주 지연되었다" (직관성 매우 높음)**                                            |

***

### **IV. ES 기반 프로젝트 일정 통제 이행 가이드라인**

**IMPORTANT**

1. **CPM(주공정법) 임계 경로와 연계 조치**: ES 지표상 SPI(t)<1.0*SPI*(*t*)<1.0으로 일정 지연이 감지되면, WBS 상의 주공정(Critical Path) 상에 있는 액티비티를 조준하여 즉시 자원 투입(Crashing)이나 병렬 작업(Fast Tracking) 조치를 단행해야 합니다.
2. **BAC 초과 구간에서의 경영진 보고 정정**: 사업 종료 지점 부근에서 기존 EVM 수치만 보고할 경우 지연 위험이 은폐되므로, 주간/월간 경영보고서에 ES 기준의 SV(t)*SV*(*t*)와 예상 완료일(IEAC(t)*IEAC*(*t*))을 정량적 근거로 필히 병행 수록해야 합니다.
