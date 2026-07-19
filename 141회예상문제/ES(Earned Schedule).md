### **I. 비용 기반 일정 통제의 한계와 ES(Earned Schedule)의 개요**

전통적인 EVM은 일정 차이(SV)와 일정수행지표(SPI)를 화폐 가치(원)로 계산합니다. 이로 인해 프로젝트가 심각하게 지연되더라도 완료 시점에는 획득가치(EV)와 계획가치(PV)가 같아져 무조건 SV=0, SPI=1.0(정상 완료)으로 수치가 왜곡되는 결함이 존재합니다. \*\*ES(획득일정법)\*\*는 이러한 왜곡을 극복하기 위해 일정을 비용이 아닌 실제 '물리적 시간(Time)' 단위를 기준 삼아 통제하고 지연 상태를 정상 노출시키는 확장 기법입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5NTEuNDI0OTk5OTk5OTk5OCAyMDEuOCIgd2lkdGg9Ijk1MS40MjQ5OTk5OTk5OTk4IiBoZWlnaHQ9IjIwMS44IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlJPT1QiIGRhdGEtdG89IkVWTSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0NjIuNTU5NzQ5OTk5OTk5OTUsNzYuOSA0NjIuNTU5NzQ5OTk5OTk5OTUsMTAwLjkgMjM3LjcwMzQ5OTk5OTk5OTk2LDEwMC45IDIzNy43MDM0OTk5OTk5OTk5NiwxMjQuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUk9PVCIgZGF0YS10bz0iRVMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDYyLjU1OTc0OTk5OTk5OTk1LDc2LjkgNDYyLjU1OTc0OTk5OTk5OTk1LDEwMC45IDY4Ny40MTU5OTk5OTk5OTk5LDEwMC45IDY4Ny40MTU5OTk5OTk5OTk5LDEyNC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJST09UIiBkYXRhLWxhYmVsPSLsnbzsoJUg6rSA66asIO2GteygnCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzOTQuOTAxNzQ5OTk5OTk5OTQiIHk9IjQwIiB3aWR0aD0iMTM1LjMxNiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDYyLjU1OTc0OTk5OTk5OTk1IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7J287KCVIOq0gOumrCDthrXsoJw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkVWTSIgZGF0YS1sYWJlbD0iRVZNIDog67mE7JqpIOq4sOuwmCDsnbzsoJUg7JiI7LihLCDsmYTro4wg7Iuc7KCQ7JeQIOustOyhsOqxtCDsmZzqs6Eg67Cc7IOdIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwIiB5PSIxMjQuOSIgd2lkdGg9IjM5NS40MDY5OTk5OTk5OTk5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjM3LjcwMzQ5OTk5OTk5OTk2IiB5PSIxNDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkVWTSA6IOu5hOyaqSDquLDrsJgg7J287KCVIOyYiOy4oSwg7JmE66OMIOyLnOygkOyXkCDrrLTsobDqsbQg7Jmc6rOhIOuwnOyDnTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRVMiIGRhdGEtbGFiZWw9IkVTIDog7Iuc6rCEIOy2lSDquLDrsJgg7J287KCVIOyYiOy4oSwg7JmE66OMIOyLnOygkCDsnbTtm4Tsl5Drj4Qg7KeA7JewIOygle2Zle2eiCDrs7TsobQiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDYzLjQwNjk5OTk5OTk5OTkiIHk9IjEyNC45IiB3aWR0aD0iNDQ4LjAxNzk5OTk5OTk5OTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNjg3LjQxNTk5OTk5OTk5OTkiIHk9IjE0My4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+RVMgOiDsi5zqsIQg7LaVIOq4sOuwmCDsnbzsoJUg7JiI7LihLCDsmYTro4wg7Iuc7KCQIOydtO2bhOyXkOuPhCDsp4Dsl7Ag7KCV7ZmV7Z6IIOuztOyhtDwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

***

### **II. ES(획득일정법)의 핵심 측정 수식 및 예측 메커니즘**

* **획득일정(ES) 정의**: 현재 시점의 EV가 계획(PV) 상에서 몇 번째 달에 달성되었는지 역산한 시간 값
* **핵심 지표 통제 공식**:

| **지표명**                | **🔑 계산 공식 🚨**                                               | **🏁 의미 및 관리 기준 💯**               |
| :--------------------- | :------------------------------------------------------------ | :--------------------------------- |
| **SV(t)** (시간 일정 편차)   | SV(t)=ES−ADSV(t)=ES−AD (AD*AD*: 실제 경과 시간)                     | 0보다 크면 일정 단축(조기 완료), 0보다 작으면 일정 지연 |
| **SPI(t)** (시간 일정 지표)  | SPI(t)=ES/ADSPI(t)=ES/AD                                      | 1.0보다 크면 일정 단축, 1.0보다 작으면 일정 지연 상태 |
| **IEAC(t)** (완료 시간 예측) | IEAC(t)=AD+PD−ESSPI(t)IEAC(t)=AD+SPI(t)PD−ES​ (PD*PD*: 계획 기간) | 현재 추세를 반영한 최종 프로젝트 완료 소요 시간 예측     |

***

### **III. 전통적 EVM(비용 기반)과 획득일정법(ES, 시간 기반)의 비교**

| **비교 항목**      | **💵 전통적 EVM (비용 기반)**                          | **⏱️ 획득일정법 (ES, 시간 기반)**                                                |
| :------------- | :---------------------------------------------- | :---------------------------------------------------------------------- |
| **일정 측정 단위**   | 화폐 가치 (원, 달러 등)                                 | 물리적 시간 단위 (월, 주, 일 등)                                                   |
| **완료 시점의 오류**  | 프로젝트가 지연 완료되어도 결국 SV=0, SPI=1.0으로 왜곡됨           | 지연 완료 시 SV(t)는 음수, SPI(t)는 1미만으로 정상 유지                                  |
| **주요 수식 매핑**   | SV=EV−PV*SV*=*EV*−*PV* SPI=EV/PV*SPI*=*EV*/*PV* | **SV(t)=ES−AD*SV*(*t*)=*ES*−*AD*** **SPI(t)=ES/AD*SPI*(*t*)=*ES*/*AD*** |
| **PM의 해석 직관성** | "일정이 1억 원만큼 늦어졌다" (직관성 떨어짐)                     | **"일정이 2주만큼 지연되었다" (직관성 매우 높음)**                                        |

***

### **IV. 공공 대형 IT 사업 일정 지연 예방을 위한 WBS-ES 연계 거버넌스**

**IMPORTANT**

1. **임계경로(CPM)와의 병행 모니터링**: ES 지표가 지연 상태를 보일 경우, WBS 상의 여유 시간(Float)이 없는 임계경로 작업들의 지연이 원인인지 교차 분석하여 자원을 추가 투입(Crashing)하거나 병렬 수행(Fast Tracking)해야 합니다.
2. **비정상 작업 정합성 검증**: EVM/ES는 100% 규칙(WBS 분할 규칙)을 준수해야 정확하므로, 실제 투입된 비용(AC)의 기록이 지연되지 않도록 관리 회계 결산 시스템과 실시간 연계되어야 합니다.
