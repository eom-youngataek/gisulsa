### **I. 공공 SW 조달의 핵심 가드레일, 직접구매 및 BMT 제도의 개요**

과거 대규모 시스템 통합(SI) 사업 발주 시 상용 소프트웨어가 하도급 형태로 묶여 발주되면서 단가 후려치기와 품질 저하 문제가 빈발했습니다. 이를 방지하기 위해 상용 SW를 국가 기관이 직접 별도 계약하는 **상용SW 직접구매 제도**와, 직접구매 대상 제품 간의 공정한 기술성 검증을 강제하는 **품질성능평가시험(BMT) 의무화 제도**가 소프트웨어 진흥법에 의거하여 시행되고 있습니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5MTQuMzc0OTk5OTk5OTk5OSAyMDEuOCIgd2lkdGg9IjkxNC4zNzQ5OTk5OTk5OTk5IiBoZWlnaHQ9IjIwMS44IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlJPT1QiIGRhdGEtdG89IkRpcmVjdCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0NDYuMjU3NzUsNzYuOSA0NDYuMjU3NzUsMTAwLjkgMjMwLjY2NCwxMDAuOSAyMzAuNjY0LDEyNC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJST09UIiBkYXRhLXRvPSJCTVQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDQ2LjI1Nzc1LDc2LjkgNDQ2LjI1Nzc1LDEwMC45IDY2MS44NTE1LDEwMC45IDY2MS44NTE1LDEyNC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJST09UIiBkYXRhLWxhYmVsPSLqs7Xqs7UgU1cg7KGw64usIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM4My40MTYyNSIgeT0iNDAiIHdpZHRoPSIxMjUuNjgyOTk5OTk5OTk5OTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQ0Ni4yNTc3NSIgeT0iNTguNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuqzteqztSBTVyDsobDri6w8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkRpcmVjdCIgZGF0YS1sYWJlbD0i7IOB7JqpU1cg7KeB7KCR6rWs66ekIDogU0kg7Ya17ZWpIOqzhOyVvSDrtoTrpqwsIOuNsOydtO2EsCDso7zqtowg7ZmV67O0IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwIiB5PSIxMjQuOSIgd2lkdGg9IjM4MS4zMjgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyMzAuNjY0IiB5PSIxNDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyDgeyaqVNXIOyngeygkeq1rOunpCA6IFNJIO2Gte2VqSDqs4Tslb0g67aE66asLCDrjbDsnbTthLAg7KO86raMIO2ZleuztDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQk1UIiBkYXRhLWxhYmVsPSJCTVQg7J2Y66y07ZmUIDog6rCd6rSA7KCBIOyEseuKpSDrjIDsobAsIOu2hOumrOuwnOyjvCDsmIjsmbgg7KGw7ZWtIOyVheyaqSDssKjri6giIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDQ5LjMyOCIgeT0iMTI0LjkiIHdpZHRoPSI0MjUuMDQ2OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI2NjEuODUxNSIgeT0iMTQzLjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5CTVQg7J2Y66y07ZmUIDog6rCd6rSA7KCBIOyEseuKpSDrjIDsobAsIOu2hOumrOuwnOyjvCDsmIjsmbgg7KGw7ZWtIOyVheyaqSDssKjri6g8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

***

### **II. 상용SW 직접구매 및 BMT 의무화의 법적 기준 및 절차**

| **분류**     | **🔑 상용SW 직접구매 (분리발주) 🚨**                        | **🏁 품질성능평가시험 (BMT) 💯**                |
| :--------- | :------------------------------------------------ | :-------------------------------------- |
| **의무화 기준** | 총 사업규모 **3억 원 이상** 공공사업 중 개별 단품 **5천만 원 이상** 상용SW | 직접구매 대상 중 국가기관 등 발주 금액이 **1억 원 이상**인 경우 |
| **평가 기관**  | 조달청 (디지털서비스몰 등록 대행 및 계약)                          | TTA(한국정보통신기술협회), KISA 등 국가 지정 시험기관      |
| **예외 조항**  | 현저한 비용 증가, 현저한 사업 지연, 상호 호환성 불가                   | 동일 제품군 2개 미만, 이미 BMT를 통과한 유효 제품 등       |

***

### **III. 상용SW 직접구매 제도와 BMT 의무화 제도의 비교**

| **비교 항목** | **📦 상용SW 직접구매 (분리발주) 제도** | **🧪 품질성능평가시험 (BMT) 제도**   |
| :-------- | :------------------------- | :------------------------- |
| **핵심 목적** | SW 제값받기 실현 및 중소 패키지 기업 육성  | 서류 평가 한계 극복 및 기술 변별력 확보    |
| **법적 근거** | 소프트웨어 진흥법 제54조             | 소프트웨어 진흥법 제54조 제2항 및 관련 고시 |
| **통제 대상** | 조달 등록된 모든 패키지 소프트웨어 제품군    | 직접구매 대상 중 단일 예산 1억 이상 품목   |
| **평가 방식** | 조달청 종합쇼핑몰 계약 조건 심사         | 실제 가동 환경과 동일한 벤치마크 테스트 수행  |

***

### **IV. 공공 소프트웨어 사업 제값받기 정착을 위한 조달 거버넌스 가이드라인**

**IMPORTANT**

1. **통합발주 예외 신청 심사의 강화**: 발주 기관이 편의성을 이유로 상용SW 직접구매를 우회하지 못하도록, '상호 호환성 불가' 신청 시 기술성평가위원회의 객관적 소명 심사를 강제해야 합니다.
2. **유지관리 요율의 현실화**: 조달 구매 완료 후 매년 지급되는 유지관리 대가 요율을 현행 10~15% 수준에서 **글로벌 스탠다드 수준(20%대)으로 점진적 인상 유도**하여 패키지 소프트웨어의 지속 가능한 품질 업그레이드 생태계를 지원해야 합니다.
