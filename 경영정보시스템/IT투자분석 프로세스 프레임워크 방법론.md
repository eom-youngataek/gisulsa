### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (IT투자분석의 필요성, ROI평가와의 차이) — 3~4줄
Ⅱ. IT투자분석 프로세스 (절차, 본론①)
Ⅲ. IT투자분석 프레임워크 (관리구조, 본론②, 도식 1개)
Ⅳ. IT투자분석 방법론 (평가기법, 본론③)
Ⅴ. 결론
```

포인트: "프로세스=시간흐름, 프레임워크=관리조직/거버넌스, 방법론=계산도구"라는 3분류 자체가 채점자에게 구조적 이해를 어필하는 핵심입니다.

### Ⅱ. 프로세스 — "기·선·집·사" (투자 생애주기)

| 단계                | 핵심활동                      |
| :---------------- | :------------------------ |
| ① 투자기획 (Plan)     | 전략과 연계된 투자후보 발굴, 사전타당성 검토 |
| ② 투자선정 (Select)   | 포트폴리오 관점에서 우선순위화·예산배분     |
| ③ 투자집행 (Deliver)  | 사업관리(PM), 진도·품질 관리        |
| ④ 사후평가 (Evaluate) | 효과분석, 환류(Lessons learned) |

→ 암기: \*\*"기획-선정-집행-사후평가"\*\*는 사실 PMO의 사업 생애주기와 동일 구조입니다. 이미 아는 PM 프로세스에 얹으면 새로 외울 게 거의 없습니다.

### Ⅲ. 프레임워크 — "포·거·연" (관리구조 3요소)

| 프레임워크                                     | 핵심                                          |
| :---------------------------------------- | :------------------------------------------ |
| **IT 포트폴리오 관리** (IT Portfolio Management) | 개별사업이 아니라 **전체 사업군을 자산처럼** 관리 (위험-수익 균형)    |
| **거버넌스 연계** (Val IT / COBIT)              | ISACA의 Val IT — IT투자가치를 COBIT(운영통제)와 연계해 관리 |
| **전략 연계** (BSC 기반)                        | 앞서 다룬 BSC 4관점에 투자효과 매핑                      |

→ 도식으로 표현하면 아래처럼 "개별사업이 아니라 포트폴리오로 본다"는 게 핵심 논리입니다.

```
        [경영전략]
           ↓
   [IT 투자포트폴리오] ← 여러 사업을 자산처럼 묶어 관리
     ↓        ↓        ↓
   [사업A]   [사업B]   [사업C]
   (각각 ROI/NPV로 개별평가 + 포트폴리오 차원 위험분산)
```

→ 여기서 실무 포인트 한 줄: 개별 사업은 ROI가 낮아도, 전략적 필수사업(예: 보안, 법규대응)이면 포트폴리오 관점에서 채택될 수 있다는 논리 — 이게 "왜 포트폴리오 관리가 필요한가"의 답입니다.

### Ⅳ. 방법론 — 앞 답변과 연결 (중복 최소화)

| 구분    | 기법                            | 한 줄 특징                                       |
| :---- | :---------------------------- | :------------------------------------------- |
| 정량기법  | ROI, NPV, IRR, PP             | (전회 답변 참조) 재무적 타당성                           |
| 통합기법  | **IE**(Information Economics) | 정량+정성 가중점수 통합                                |
| 고도화기법 | **Real Option** (실물옵션)        | 불확실성 큰 IT투자를 "옵션"처럼 평가 — 지금 투자안해도 나중에 선택권 확보 |
| 총원가기법 | **TCO/TVO**                   | 총소유비용(TCO) 대비 총가치(TVO, Gartner)              |

→ 새로 외울 건 **Real Option 하나**입니다. "확실하지 않은 미래 투자는 지금 다 걸지 않고, 선택권(옵션)만 사둔다"는 개념 — AI/신기술 투자처럼 불확실성 큰 사업에 특히 잘 어울려서 최근 출제 포인트로 자주 나옵니다.

### Ⅴ. 결론 포인트 (차별화 한 줄)

전통적 ROI 중심 평가의 한계는 \*\*"확실한 것만 투자하게 만든다"\*\*는 점입니다. AI/신기술처럼 불확실성이 큰 투자는 Real Option이나 포트폴리오 관점으로 보완해야 한다는 논리로 마무리하면, 최신성과 통합적 이해를 동시에 보여줄 수 있습니다.


**1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "전사적 가치 창출을 위해 \*\*\[프로세스]\*\*에 따라 절차를 밟고, \*\*\[프레임워크(Val IT)]\*\*로 거버넌스 뼈대를 세우며, 상황에 맞는 \*\*\[방법론(정보경제학, ITPM 등)]\*\*을 표로 비교하여 제시한다. 마지막으로 **EA와 PMO**로 실행력을 강조하며 결론을 낸다."

***

### **2. 실제 답안지 구성용 도식 및 표**

#### **I. \[도입] 가치 중심의 전사적 IT 투자분석 체계 개요**

* **정의:** 단순 재무적 수익(ROI) 검토를 넘어, 전사 비즈니스 전략과 IT를 연계하여 가치를 극대화하고 리스크를 통제하는 종합 분석 체계.

#### **II. \[프로세스] 전주기적 IT 투자분석 프로세스 흐름도**

답안 작성 시 화살표로 이어지는 블록 다이어그램을 그려주면 가시성이 매우 높아집니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDU3LjYyODAwMDAwMDAwMDIgMTUyLjc1IiB3aWR0aD0iMTA1Ny42MjgwMDAwMDAwMDAyIiBoZWlnaHQ9IjE1Mi43NSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBIiBkYXRhLXRvPSJCIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjgwNC42NzIsODUuODUgODQwLjY3Miw4NS44NSA4NDAuNjcyLDc1Ljg2NjY2NjY2NjY2NjY3IDg1Mi42NzIsNzUuODY2NjY2NjY2NjY2NjciIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkIiIGRhdGEtdG89IkMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iODUyLjY3Miw1Ny45MzMzMzMzMzMzMzMzMyA4NDAuNjcyLDU3LjkzMzMzMzMzMzMzMzMzIDg0MC42NzIsNDcuOTQ5OTk5OTk5OTk5OTk2IDI2Ni4xNSw0Ny45NDk5OTk5OTk5OTk5OTYgMjY2LjE1LDU3LjkzMzMzMzMzMzMzMzMzIDIzMC4xNDk5OTk5OTk5OTk5OCw1Ny45MzMzMzMzMzMzMzMzMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQyIgZGF0YS10bz0iRCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyMzAuMTQ5OTk5OTk5OTk5OTgsNzUuODY2NjY2NjY2NjY2NjcgMjY2LjE1LDc1Ljg2NjY2NjY2NjY2NjY3IDI2Ni4xNSw4NS44NSAyNzguMTUsODUuODUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkQiIGRhdGEtdG89IkEiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLtlLzrk5zrsLEgKExlc3NvbnMgTGVhcm5lZCkiIHBvaW50cz0iNDI2LjA2Myw4NS44NSA2NjEuMjA1LDg1Ljg1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iRCIgZGF0YS10bz0iQSIgZGF0YS1sYWJlbD0i7ZS865Oc67CxIChMZXNzb25zIExlYXJuZWQpIj4KICA8cmVjdCB4PSI0NzAuMDYzIiB5PSI2OS44NSIgd2lkdGg9IjE0Ny4xNDIwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjU0My42MzQiIHk9Ijg1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7tlLzrk5zrsLEgKExlc3NvbnMgTGVhcm5lZCk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkEiIGRhdGEtbGFiZWw9IjEuIO2IrOyekCDquLDtmowg7Iud67OECihBbGlnbm1lbnQpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjY2MS4yMDUiIHk9IjU4Ljk0OTk5OTk5OTk5OTk5NiIgd2lkdGg9IjE0My40NjY5OTk5OTk5OTk5OCIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UzZjJmZCIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI3MzIuOTM4NSIgeT0iODUuODUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjczMi45Mzg1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+MS4g7Yis7J6QIOq4sO2ajCDsi53rs4Q8L3RzcGFuPjx0c3BhbiB4PSI3MzIuOTM4NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+KEFsaWdubWVudCk8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQiIgZGF0YS1sYWJlbD0iMi4g64yA7JWIIOu2hOyEnSDrsI8g7Y+J6rCACihBbmFseXNpcykiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iODUyLjY3MiIgeT0iNDAiIHdpZHRoPSIxNjQuOTU2MDAwMDAwMDAwMDIiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iOTM1LjE1MDAwMDAwMDAwMDEiIHk9IjY2LjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjkzNS4xNTAwMDAwMDAwMDAxIiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+Mi4g64yA7JWIIOu2hOyEnSDrsI8g7Y+J6rCAPC90c3Bhbj48dHNwYW4geD0iOTM1LjE1MDAwMDAwMDAwMDEiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPihBbmFseXNpcyk8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQyIgZGF0YS1sYWJlbD0iMy4g7Y+s7Yq47Y+066as7JikIOydmOyCrOqysOyglQooUG9ydGZvbGlvICZhbXA7IERlY2lzaW9uKSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIxOTAuMTQ5OTk5OTk5OTk5OTgiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTM1LjA3NSIgeT0iNjYuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTM1LjA3NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPjMuIO2PrO2KuO2PtOumrOyYpCDsnZjsgqzqsrDsoJU8L3RzcGFuPjx0c3BhbiB4PSIxMzUuMDc1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj4oUG9ydGZvbGlvICZhbXA7IERlY2lzaW9uKTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJEIiBkYXRhLWxhYmVsPSI0LiDsgqztm4Qg7ISx6rO8IOy4oeyglQooUG9zdC1SZXZpZXcpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjI3OC4xNSIgeT0iNTguOTQ5OTk5OTk5OTk5OTk2IiB3aWR0aD0iMTQ3LjkxMyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZjZTRlYyIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIzNTIuMTA2NSIgeT0iODUuODUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjM1Mi4xMDY1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+NC4g7IKs7ZuEIOyEseqzvCDsuKHsoJU8L3RzcGFuPjx0c3BhbiB4PSIzNTIuMTA2NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+KFBvc3QtUmV2aWV3KTwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

* **식별:** 비즈니스 전략에 부합하는 과제 도출
* **평가:** 정량/정성적 기법 융합 타당성 분석
* **결정:** 한정된 예산 내 최적의 프로젝트 조합 선정
* **측정:** 실제 가치 실현 여부 추적 및 피드백

#### **III. \[프레임워크 및 방법론] 핵심 분석 체계 (채점 포인트)**

이 영역은 프레임워크(뼈대)를 도식으로, 세부 방법론(도구)을 표로 분리하여 제시합니다.

**1) 핵심 프레임워크: Val IT (가치 기반 IT 거버넌스)**

* **목적:** IT 투자가 비즈니스 가치를 실제로 창출하도록 통제하는 COBIT 연계 프레임워크.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OTkuOTk2OTk5OTk5OTk5OSA0MjYuMzAwMDAwMDAwMDAwMDciIHdpZHRoPSI0OTkuOTk2OTk5OTk5OTk5OSIgaGVpZ2h0PSI0MjYuMzAwMDAwMDAwMDAwMDciIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IlZhbF9JVF9fM19fIiBkYXRhLWxhYmVsPSJWYWwgSVQg7ZSE66CI7J6E7JuM7YGsIDPrjIAg7ZW17IusIOuPhOuplOyduCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNDE5Ljk5Njk5OTk5OTk5OTkiIGhlaWdodD0iMzQ2LjMwMDAwMDAwMDAwMDA3IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNDE5Ljk5Njk5OTk5OTk5OTkiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5WYWwgSVQg7ZSE66CI7J6E7JuM7YGsIDPrjIAg7ZW17IusIOuPhOuplOyduDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUE0iIGRhdGEtdG89IklNIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjIzOS45OTQ5OTk5OTk5OTk5NSwyNjguNSAyMzkuOTk0OTk5OTk5OTk5OTUsMzE2LjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlZHIiBkYXRhLWxhYmVsPSLqsIDsuZgg6rGw67KE64SM7IqkIChWYWx1ZSBHb3Zlcm5hbmNlKQrstZzqs6Ag6rK97JiB7KeEIOyjvOuPhOydmCDqsIDsuZgg7LWc7KCB7ZmUIOuwqe2WpSDrsI8g7Ya17KCcIOq1rOyhsCDrp4jroKgiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9IjE1Ny44IiB3aWR0aD0iMzg3Ljk5Njk5OTk5OTk5OTkiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmM2U1ZjUiIHN0cm9rZT0iIzE5NzZkMiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMjQ5Ljk5ODQ5OTk5OTk5OTk1IiB5PSIxODQuNzAwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjI0OS45OTg0OTk5OTk5OTk5NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuqwgOy5mCDqsbDrsoTrhIzsiqQgKFZhbHVlIEdvdmVybmFuY2UpPC90c3Bhbj48dHNwYW4geD0iMjQ5Ljk5ODQ5OTk5OTk5OTk1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7stZzqs6Ag6rK97JiB7KeEIOyjvOuPhOydmCDqsIDsuZgg7LWc7KCB7ZmUIOuwqe2WpSDrsI8g7Ya17KCcIOq1rOyhsCDrp4jroKg8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iLS0iIGRhdGEtbGFiZWw9IiBQTVsmcXVvdDvtj6ztirjtj7TrpqzsmKQg6rSA66asIChQb3J0Zm9saW8gTWFuYWdlbWVudCkK7KCE65617JeQIOunnuuKlCDstZzsoIHsnZgg7Yis7J6QIOyhsO2VqSDshKDtg50g67CPIOyekOybkCDtlaDri7kmcXVvdDsiIGRhdGEtc2hhcGU9ImFzeW1tZXRyaWMiPgogIDxwb2x5Z29uIHBvaW50cz0iNjgsODQgNDEzLjAxODk5OTk5OTk5OTk1LDg0IDQxMy4wMTg5OTk5OTk5OTk5NSwxMzcuOCA2OCwxMzcuOCA1NiwxMTAuOSIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjIzNC41MDk0OTk5OTk5OTk5NyIgeT0iMTEwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjIzNC41MDk0OTk5OTk5OTk5NyIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPiBQTVsmcXVvdDvtj6ztirjtj7TrpqzsmKQg6rSA66asIChQb3J0Zm9saW8gTWFuYWdlbWVudCk8L3RzcGFuPjx0c3BhbiB4PSIyMzQuNTA5NDk5OTk5OTk5OTciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyghOueteyXkCDrp57ripQg7LWc7KCB7J2YIO2IrOyekCDsobDtlakg7ISg7YOdIOuwjyDsnpDsm5Ag7ZWg64u5JnF1b3Q7PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlBNIiBkYXRhLWxhYmVsPSJQTSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyMDkuMDE2NDk5OTk5OTk5OTUiIHk9IjIzMS42MDAwMDAwMDAwMDAwMiIgd2lkdGg9IjYxLjk1Njk5OTk5OTk5OTk5NCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZWFmNiIgc3Ryb2tlPSIjN2IxZmEyIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIyMzkuOTk0OTk5OTk5OTk5OTUiIHk9IjI1MC4wNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+UE08L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IklNIiBkYXRhLWxhYmVsPSLtiKzsnpAg6rSA66asIChJbnZlc3RtZW50IE1hbmFnZW1lbnQpCuyEoOygleuQnCDqsJzrs4QgSVQg7ZSE66Gc6re4656o7J2YIOq1rOyytOyggSDsi6Ttlokg67CPIOyEseqzvCDqtIDrpqwiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9IjMxNi41IiB3aWR0aD0iMzY3Ljk4OTk5OTk5OTk5OTkiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMGYyZjEiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMjM5Ljk5NDk5OTk5OTk5OTk1IiB5PSIzNDMuNCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMjM5Ljk5NDk5OTk5OTk5OTk1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7Yis7J6QIOq0gOumrCAoSW52ZXN0bWVudCBNYW5hZ2VtZW50KTwvdHNwYW4+PHRzcGFuIHg9IjIzOS45OTQ5OTk5OTk5OTk5NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7ISg7KCV65CcIOqwnOuzhCBJVCDtlITroZzqt7jrnqjsnZgg6rWs7LK07KCBIOyLpO2WiSDrsI8g7ISx6rO8IOq0gOumrDwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

**2) IT 투자분석 핵심 방법론 3대장 비교표** 답안지 분량을 채우고 전문성을 뽐내기 가장 좋은 3단 표 형식입니다.

| **구분**      | **방법론**                           | **핵심 메커니즘 및 특징**                                                            | **활용 목적 (적용 환경)**                    |
| :---------- | :-------------------------------- | :-------------------------------------------------------------------------- | :----------------------------------- |
| **종합 평가**   | **정보경제학** (Information Economics) | - 전통적 ROI (재무적 수치) + **무형의 가치** - 기술적 리스크, 전략적 연계도 등을 **점수화하여 가감(+,-)**     | 단순 재무 지표의 한계 극복 및 종합적 타당성 검증 시       |
| **리스크 분산**  | **IT 포트폴리오 관리** (ITPM)            | - 주식 투자처럼 IT 프로젝트를 분류(인프라/전략/혁신형 등) - 여러 바구니에 담아 **리스크를 분산**하고 가치 극대화       | 한정된 예산 내에서 전사적 자원 할당 및 리스크 최적화 시     |
| **불확실성 대응** | **실물 옵션** (Real Options)          | - 1단계 소규모 투자(PoC) 후 성과에 따라 2단계를 \*\*확대/연기/축소할 수 있는 '선택권(Option)'\*\*의 가치 산정 | AI, 클라우드 등 불확실성 및 변동성이 큰 신기술 도입 검증 시 |

#### **IV. \[결론/제언] 성공적인 IT 투자분석 체계 정착을 위한 제언**

* 아무리 좋은 프레임워크라도 실행력이 중요합니다.
* "\*\*전사 PMO(프로젝트 관리 조직)\*\*를 통한 전 주기적 성과 모니터링 통제와, 중복 투자를 원천 차단하기 위한 **EA(엔터프라이즈 아키텍처) 기반의 의사결정 체계**가 필수적으로 병행되어야 합니다."
