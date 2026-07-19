### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (패키지SW 정의, 자체개발과의 차이) — 3~4줄
Ⅱ. 도입절차 5단계 (본론①, 도식 1개 필수)
Ⅲ. Fit/Gap분석 - 핵심단계 심화 (본론②, 핵심 배점)
Ⅳ. 도입방식 결정기준 및 리스크
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 CBD는 '컴포넌트를 조립해 시스템을 만든다'는 것이었는데, 패키지SW 도입은 한걸음 더 나가 '이미 완성된 상용제품(ERP, CRM 등)을 우리 조직에 맞게 이식하는 것' — 만드는 게 아니라 맞추는 것"\*\*이라는 한 줄로 시작하면, CBD 답안과 자연스럽게 이어집니다.

### Ⅱ. 도입절차 — "요·선·핏·구·안" (5단계)

| 단계             | 내용                                |
| :------------- | :-------------------------------- |
| **요구정의**       | 조직의 업무요구사항 정리, 도입목표 설정            |
| **패키지선정**      | 시장조사 후 **후보제품 비교평가**(기능·비용·벤더신뢰도) |
| **Fit/Gap분석**  | 패키지기능과 **우리요구사항의 일치/불일치** 분석      |
| **구축(커스터마이징)** | Gap을 메우기 위한 **설정변경 또는 추가개발**      |
| **안정화**        | 데이터이관, 사용자교육, 운영전환                |

→ 암기: **"요구를 정리하고, 제품을 고르고, 안맞는 부분을 찾고, 그 부분을 메우고, 안정시킨다"** — 앞서 다룬 "차세대시스템 오픈 후 문제점" 답안의 "안정화기간" 개념이 여기서도 마지막단계로 이어집니다.

### Ⅲ. Fit/Gap분석 — 핵심단계 심화, 핵심 배점

**함정 방지: "안맞는 부분을 찾는다"고만 답하면 절반. 그 다음 처리방향까지 구조화해야 완성됩니다.**

| 분류             | 대응방향                     | 비용/리스크                     |
| :------------- | :----------------------- | :------------------------- |
| **Fit(일치)**    | 패키지 표준기능 **그대로 사용**      | 낮음(가장 이상적)                 |
| **Gap-설정변경**   | **파라미터/설정만 조정**(코드변경없음)  | 중간(패키지업그레이드에 영향적음)         |
| **Gap-커스터마이징** | 패키지 **소스코드를 직접수정**해 요구반영 | **높음**(패키지 향후 업그레이드시 충돌위험) |

→ 암기: **"딱맞으면 그냥쓰고, 조금다르면 설정만 바꾸고, 많이다르면 코드를 고친다(위험↑)"** — 앞서 다룬 "IT-ROI"에서 비용과 효과를 저울질했듯, **Gap을 어떻게 메울지가 곧 비용과 리스크를 결정**한다는 게 이 답안의 핵심 통찰입니다.

### 도식화 제안

```
[패키지 표준기능] ←──비교──→ [우리 요구사항]
        │                        │
   Fit(일치)                Gap(불일치)
    ↓                          ↓
 그대로사용              [설정변경] or [커스터마이징]
                        (낮은위험)    (높은위험,업그레이드충돌가능)
```

### Ⅳ. 도입방식 결정기준 및 리스크

| 기준                 | 권장방향                              | 이유                                                      |
| :----------------- | :-------------------------------- | :------------------------------------------------------ |
| **표준업무(회계,인사등)**   | **Fit 최대화**(패키지표준 그대로)            | 업계 베스트프랙티스가 이미 반영되어 있음                                  |
| **핵심경쟁력업무**        | **최소한의 커스터마이징 허용**                | 조직만의 차별화된 프로세스는 보존필요                                    |
| **커스터마이징 남발시 리스크** | **"두번째 폭포수"화**(자체개발과 비슷한 리스크로 회귀) | 앞서 다룬 "패키지SW의 장점(속도·검증됨)"이 사라지고, 오히려 자체개발보다 더 복잡해질 수 있음 |

→ **실무 격언**: "커스터마이징을 많이 할수록, 패키지SW 도입의 의미(속도·안정성·저비용)가 사라진다" — 그래서 Fit/Gap분석에서 \*\*"업무를 패키지에 맞추는 것(To-Be 조정)"\*\*이 \*\*"패키지를 업무에 맞추는 것(과도한커스터마이징)"\*\*보다 우선적으로 검토되어야 합니다.

### Ⅴ. 결론 포인트 (오늘 SDLC/개발방법론 시리즈 최종연결)

패키지SW 도입의 핵심성공요인은 \*\*"우리 요구사항을 얼마나 정확히 알아냈는가"\*\*가 아니라, \*\*"패키지의 표준방식에 우리 업무를 얼마나 유연하게 맞출 수 있는가"\*\*입니다 — 이는 앞서 다룬 CBD(컴포넌트 재사용)의 극단화된 형태로, \*\*"처음부터 만들지 않는다"\*\*는 철학이 여기서는 \*\*"업무프로세스 자체도 표준에 맞춰 바꾼다"\*\*는 데까지 나아간 것이며, 오늘 다룬 SDLC/개발방법론 시리즈(폭포수→나선형→V모델→CBD→패키지SW도입)가 결국 \*\*"직접 만들기(폭포수 등) ↔ 재사용하기(CBD) ↔ 사서 맞추기(패키지SW)"\*\*라는 하나의 스펙트럼으로 완결됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "회사에서 회계나 재고 관리 시스템(ERP 등)을 만들려고 한다. 옛날에는 개발 업체를 불러다가 바닥부터 코딩을 시켰다(자체 개발/맞춤복). 하지만 요새는 SAP나 오라클 같은 기업이 이미 전 세계 1등 기업들의 베스트 프랙티스를 녹여 기성복으로 만들어 놓은 \*\*'패키지 SW'\*\*를 사다 쓰는 게 트렌드다. 이 비싼 기성복을 사 오는 절차는 꽤 깐깐하다. 먼저 우리 회사에 필요한 게 뭔지 요구사항을 적어(RFP 발송), 업체들을 부른 뒤, 이 옷이 튼튼한지 우리 회사 시스템에 잘 맞는지 입어보고 달리기 테스트를 해보는 **'BMT와 PoC(검증)'** 과정을 거쳐 최종 1등을 선정한다. 선정하고 나면 가장 큰 딜레마에 빠진다. 글로벌 표준으로 만든 옷이라 우리 회사 방식과 살짝 안 맞기 때문이다. 이때 돈을 들여 옷을 뜯어고쳐(과도한 Customizing) 우리 몸에 억지로 맞추면, 나중에 패키지가 버전업될 때 에러가 터지고 유지보수(AS)를 전혀 받을 수 없다. 그래서 패키지 도입의 황금률은 \*\*'옷(표준 패키지)에 몸(회사 업무)을 맞춰라'\*\*다. 즉, 회사의 옛날 업무 방식을 패키지의 선진 표준 프로세스에 맞게 뜯어고치는 \*\*'BPR(업무 프로세스 재설계)'\*\*을 병행해야만 패키지 도입이 성공할 수 있다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 바닥부터 짜지 말고 검증된 기성복을 사 입자, 패키지 SW 도입 개요**

* **정의:** 기업의 정보시스템(ERP, CRM 등)을 구축할 때, 처음부터 자체 개발(In-House)하지 않고 이미 시장에서 기능과 안정성이 검증된 **상용 소프트웨어 제품(Package)을 구매하여 자사 환경에 맞게 적용하는 일련의 방법론**.
* **목적:** 개발 기간 획기적 단축, 불확실성/버그 위험 최소화, 그리고 패키지에 내장된 **'글로벌 선진 업무 프로세스(Best Practice)'를 회사 내부로 자연스럽게 이식**하기 위함.

#### **II. \[본론 1] 최적의 기성복을 찾아 입는 과정: 패키지 도입 4대 절차 (도식화)**

제품을 고르고, 우리 환경에 맞추고, 교육하여 오픈하는 절차입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OTguOTU0OTk5OTk5OTk5OSA4NDYuODY1MDAwMDAwMDAwMSIgd2lkdGg9IjQ5OC45NTQ5OTk5OTk5OTk5IiBoZWlnaHQ9Ijg0Ni44NjUwMDAwMDAwMDAxIiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfU1dfU29sdXRpb25fX18iIGRhdGEtbGFiZWw9Iu2MqO2CpOyngCBTVyAoU29sdXRpb24pIOuPhOyehSDtlbXsi6wg65287J207ZSE7IKs7J207YG0Ij4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI0MTguOTU0OTk5OTk5OTk5OSIgaGVpZ2h0PSI3NjYuODY1MDAwMDAwMDAwMSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjQxOC45NTQ5OTk5OTk5OTk5IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+7Yyo7YKk7KeAIFNXIChTb2x1dGlvbikg64+E7J6FIO2VteyLrCDrnbzsnbTtlITsgqzsnbTtgbQ8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlMxIiBkYXRhLXRvPSJTMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyMDUuNjgyNSwxNDIuMDI1IDIwNS42ODI1LDE4NS44IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTMiIgZGF0YS10bz0iUzMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iuy1nOyihSDshpTro6jshZgg6rOE7JW9IiBwb2ludHM9IjIwNS42ODI1LDQ4NS4xNjUgMjA1LjY4MjUsNjAxLjQ2NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUzMiIGRhdGEtdG89IlM0IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjIwNS42ODI1LDY3Mi4xNjUwMDAwMDAwMDAxIDIwNS42ODI1LDcyMC4xNjUwMDAwMDAwMDAxIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlMyIiBkYXRhLXRvPSJTMyIgZGF0YS1sYWJlbD0i7LWc7KKFIOyGlOujqOyFmCDqs4Tslb0iPgogIDxyZWN0IHg9IjE1My4xODI1IiB5PSI1MjguMTY1MDAwMDAwMDAwMSIgd2lkdGg9IjEwNC4zNzQwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjIwNS4zNjk1MDAwMDAwMDAwMiIgeT0iNTQzLjMxNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7LWc7KKFIOyGlOujqOyFmCDqs4Tslb08L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlMxIiBkYXRhLWxhYmVsPSIxLiDrj4TsnoUg7KSA67mEIOuwjyDquLDtmo0K7JqU6rWs7IKs7ZWtIOu2hOyEnSAvIFJGUCjsoJzslYjsmpTssq3shJwpIOyekeyEsSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI2NS4wMzYwMDAwMDAwMDAwNCIgeT0iODguMjI1IiB3aWR0aD0iMjgxLjI5Mjk5OTk5OTk5OTk1IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjA1LjY4MjUiIHk9IjExNS4xMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjIwNS42ODI1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+MS4g64+E7J6FIOykgOu5hCDrsI8g6riw7ZqNPC90c3Bhbj48dHNwYW4geD0iMjA1LjY4MjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyalOq1rOyCrO2VrSDrtoTshJ0gLyBSRlAo7KCc7JWI7JqU7LKt7IScKSDsnpHshLE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzIiIGRhdGEtbGFiZWw9IjIuIOygnO2SiCDqsoDspp0g67CPIOyEoOyglSDwn5qoClJGSSAvIFBvQyAo6rCc64WQIOqygOymnSkgLyBCTVQgKOyEseuKpSDtj4nqsIApIiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjIwNS42ODI1LDE4NS44IDM1NS4zNjUsMzM1LjQ4MjUgMjA1LjY4MjUsNDg1LjE2NSA1NiwzMzUuNDgyNSIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIyMDUuNjgyNSIgeT0iMzM1LjQ4MjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjIwNS42ODI1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+Mi4g7KCc7ZKIIOqygOymnSDrsI8g7ISg7KCVIPCfmqg8L3RzcGFuPjx0c3BhbiB4PSIyMDUuNjgyNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+UkZJIC8gUG9DICjqsJzrhZAg6rKA7KadKSAvIEJNVCAo7ISx64qlIO2PieqwgCk8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzMiIGRhdGEtbGFiZWw9IjMuIOy7pOyKpO2EsOuniOydtOynlSDrsI8g6rWs7LaVCu2MqO2CpOyngCDtjIzrnbzrr7jthLAg7IS47YyFIChDb25maWd1cmF0aW9uKQrquLDsobQg66CI6rGw7IucIOyLnOyKpO2FnCDsl7Drj5kgKEVBSS9BUEkpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjcxLjcwNTAwMDAwMDAwMDA0IiB5PSI2MDEuNDY1IiB3aWR0aD0iMjY3Ljk1NDk5OTk5OTk5OTkiIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyMDUuNjgyNSIgeT0iNjM2LjgxNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMjA1LjY4MjUiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj4zLiDsu6TsiqTthLDrp4jsnbTsp5Ug67CPIOq1rOy2lTwvdHNwYW4+PHRzcGFuIHg9IjIwNS42ODI1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7tjKjtgqTsp4Ag7YyM652866+47YSwIOyEuO2MhSAoQ29uZmlndXJhdGlvbik8L3RzcGFuPjx0c3BhbiB4PSIyMDUuNjgyNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+6riw7KG0IOugiOqxsOyLnCDsi5zsiqTthZwg7Jew64+ZIChFQUkvQVBJKTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTNCIgZGF0YS1sYWJlbD0iNC4g7YWM7Iqk7Yq4IOuwjyDsnbTqtIAgKOyghO2MjCkK7IKs7Jqp7J6QIOyduOyImCDthYzsiqTtirgoVUFUKQrtmITsl4Ug6rWQ7JyhIOuwjyDquLDsobQg642w7J207YSwIOuniOydtOq3uOugiOydtOyFmCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI2MC41OTAwMDAwMDAwMDAwMyIgeT0iNzIwLjE2NTAwMDAwMDAwMDEiIHdpZHRoPSIyOTAuMTg0OTk5OTk5OTk5OTUiIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjA1LjY4MjUiIHk9Ijc1NS41MTUwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIyMDUuNjgyNSIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPjQuIO2FjOyKpO2KuCDrsI8g7J206rSAICjsoITtjIwpPC90c3Bhbj48dHNwYW4geD0iMjA1LjY4MjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyCrOyaqeyekCDsnbjsiJgg7YWM7Iqk7Yq4KFVBVCk8L3RzcGFuPjx0c3BhbiB4PSIyMDUuNjgyNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7ZiE7JeFIOq1kOycoSDrsI8g6riw7KG0IOuNsOydtO2EsCDrp4jsnbTqt7jroIjsnbTshZg8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzNzQuMzI4OTk5OTk5OTk5OTUiIHk9Ijg4LjIyNSIgd2lkdGg9IjY4LjYyNiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQwOC42NDE5OTk5OTk5OTk5NCIgeT0iMTA2LjY3NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Tm90ZTwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 패키지 SW 선정 및 구축 시 핵심 고려 요소 (3단 표)**

성공적인 도입을 위해 각 단계에서 주의해야 할 핵심 키워드들입니다.

| **구분 (도입 단계)**             | **핵심 수행 기법 / 키워드**                              | **상세 고려사항 및 딜레마**                                                                                            |
| :------------------------- | :---------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| **선정 단계 (Selection)**      | **1. PoC (개념 증명)** Proof of Concept             | 벤더사가 제안한 패키지가 **우리 회사의 핵심 요구사항을 진짜로 기술적으로 구현 가능한지** 샘플로 증명해 보게 함.                                            |
| <br />                     | **2. BMT (벤치마크 테스트)** Benchmark Test            | 도입 후보 2~3개 패키지를 동일한 서버와 데이터 환경에 깔아놓고 **트래픽을 쏴서 성능(응답속도 등)을 객관적으로 수치화하여 비교.**                                 |
| **구축 단계 (Implementation)** | **3. TCO (총 소유 비용) 산정** Total Cost of Ownership | 초기 구매비(라이선스) 외에 하드웨어 증설비, 매년 내야 하는 **유지보수비(MA), 벤더 종속성(Lock-in) 비용까지 전체 10년 치를 계산**해야 함.                     |
| <br />                     | **4. 커스터마이징 (수정) 🚨**                           | 우리 회사 입맛에 맞추려고 **패키지 소스를 과도하게 수정(Customizing)하면 나중에 패키지 업그레이드가 불가능해짐.** 껍데기 설정(Configuration)만 건드리는 것이 이상적임. |

#### **IV. \[결론/제언] 과도한 커스터마이징의 비극과 BPR(업무 프로세스 재설계) 동반의 필수성**

* **(키워드 위주 2줄 마무리)** "패키지 도입 실패의 90%는 기존 회사의 낡은 결재 방식을 유지하려고 비싼 패키지 소스코드를 누더기로 뜯어고치는 \*\*'과도한 커스터마이징'\*\*에서 발생합니다. 성공적인 패키지 도입의 황금률은 옷을 내 몸에 맞추는 것이 아니라, 패키지에 담긴 글로벌 스탠다드 로직에 맞춰 우리 회사의 낡은 업무 체계를 갈아엎어 버리는 **'BPR(Business Process Reengineering, 업무 프로세스 재설계)'을 강력한 리더십으로 병행**하는 것입니다."
