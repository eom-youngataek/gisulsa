### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (표준의목적,4파트구조) — 3~4줄
Ⅱ. Part별핵심내용 (본론①, 도식 1개 필수)
Ⅲ. Part2(프로세스)심화 - 시험조직의핵심 (본론②, 핵심 배점)
Ⅳ. 오늘시리즈전체와의매핑
Ⅴ. 결론
```

포인트: 개요에서 \*\*"오늘하루다룬 살충제패러독스,화이트박스/블랙박스,TDD/BDD,회귀/뮤테이션,알파/베타테스트 같은개별기법·개념들은 각자따로존재하는게아니라, 이표준(ISO/IEC/IEEE 29119)안에서 '개념(Part1)-프로세스(Part2)-문서(Part3)-기법(Part4)'라는하나의체계로통합되어있다"\*\*는한줄로시작하면, 오늘의테스트시리즈전체를 이표준하나로수렴시킬수있습니다.

### Ⅱ. Part별핵심내용 — "개·프·문·기"

| Part       | 명칭      | 핵심내용                                   |
| :--------- | :------ | :------------------------------------- |
| **Part 1** | 개념과정의   | 테스팅 **원리,개념,용어**소개(앞서다룬**7대원칙**이여기속함)  |
| **Part 2** | 테스트프로세스 | SDLC상의 **테스트프로세스표준**(ISO/IEC 12207과연계) |
| **Part 3** | 테스트문서화  | 프로세스와연계된 **표준문서템플릿**                   |
| **Part 4** | 테스트설계기법 | **정적,동적,비기능**테스트케이스설계기법상세              |

→ 암기: **"개념을정의하고(1),프로세스를표준화하고(2),그결과를문서로남기고(3),구체적기법을제시한다(4)"** — 이4단계가 앞서다룬 \*\*"요구공학의도출-분석-명세-검증"\*\*과 유사한 \*\*"정의→절차→기록→실행"\*\*흐름입니다.

### 도식화 제안

```
[Part1: 개념과정의]
  테스팅원리,용어(앞서다룬7대원칙)
       ↓
[Part2: 테스트프로세스] ← 표준의핵심
  SDLC 전반의테스트프로세스체계
       ↓
[Part3: 테스트문서화]
  프로세스결과를 남기는 표준양식
       ↓
[Part4: 테스트설계기법]
  정적분석,동적분석,블랙박스/화이트박스기법 상세
```

### Ⅲ. Part2(프로세스) 심화 — 핵심 배점

**함정 방지: "Part2가핵심"이라고만말하면절반. 왜프로세스가핵심인지, 계층구조를보여줘야완성됩니다.**

Part2는 표준전체의 **핵심**으로평가되며, 테스트프로세스를 **3개계층**으로구조화합니다.

| 계층            | 내용                                              |
| :------------ | :---------------------------------------------- |
| **조직테스트프로세스** | 조직전체차원의 **테스트정책,전략** 수립                         |
| **테스트관리프로세스** | 프로젝트/테스트레벨의 **계획,모니터링,통제** — 앞서다룬**RTM**활용이여기속함 |
| **동적테스트프로세스** | 실제 **테스트케이스설계,실행,결과기록**(앞서다룬화이트박스/블랙박스실행이여기속함)  |

→ 암기: **"조직차원정책세우고,프로젝트차원관리하고,실제로테스트를수행한다"** — 앞서다룬 "정보시스템감리기준"에서 감리가 "절차·산출물·서비스"3단계로 나뉘었던것과 유사하게, 여기서도 \*\*"정책→관리→실행"\*\*3단계위계가 있습니다.

### Ⅳ. 오늘시리즈전체와의매핑

| 오늘다룬주제                         | 표준상위치            |
| :----------------------------- | :--------------- |
| **테스트7대원칙,살충제패러독스**            | Part1(개념과정의)     |
| **RTM,테스트계획,커버리지관리**           | Part2(테스트관리프로세스) |
| **테스트계획서,테스트케이스양식**            | Part3(테스트문서화)    |
| **화이트박스,블랙박스,정적/동적분석,회귀/뮤테이션** | Part4(테스트설계기법)   |

→ "오늘하루흩어져있던수십개의테스트개념들이, 사실이표준의4개Part어딘가에 정확히자리잡고있었다"는게 이답안의핵심통합포인트입니다.

### Ⅴ. 결론 포인트 (테스트 시리즈 최종완결)

KS X ISO/IEC/IEEE 29119은 \*\*"테스트라는활동이 감(느낌)이나개인기법의모음이아니라, 개념-프로세스-문서-기법으로체계화된국제표준화된공학"\*\*임을보여줍니다 — 2013년 키워드주도테스팅이독립파트로추가되며 발전해온이표준은, 오늘하루다룬 7대원칙(Part1)부터 알파/베타/몽키테스트,회귀/뮤테이션테스트같은구체적기법(Part4)까지 **모두하나의일관된체계안에통합**되어있다는것을보여주며, 이로써오늘의방대한테스트시리즈전체(7대원칙→살충제패러독스→화이트박스/블랙박스→TDD/BDD→정적/동적분석→회귀/뮤테이션→커버리지→알파/베타/인수→몽키→ISO29119표준)가, \*\*"개별기법들이사실은하나의국제표준체계아래통합되어있다"\*\*는 결론으로 완결됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "과거 글로벌 테스팅 업계는 춘추전국시대였다. 어떤 회사는 문서 양식을 맞추기 위해 IEEE 829 표준을 뒤적거리고, 테스트 기법을 적용할 때는 BS 7925 표준을 가져다 쓰는 등 뿔뿔이 흩어진 파편화된 규격들 때문에 글로벌 협업에 심각한 마찰 비용이 발생했다. 이 지긋지긋한 파편화를 종식시키고 전 세계 소프트웨어 테스팅의 룰을 하나로 통일한 절대 표준이 바로 \*\*'ISO/IEC/IEEE 29119'\*\*다. (한국에서는 KS X로 채택). 이 29119 표준의 심장을 꿰뚫는 하나의 거대한 철학이 있는데, 바로 \*\*'리스크 기반 테스팅(Risk-Based Testing, RBT)'\*\*이다. "모든 것을 완벽히 테스트하는 것은 불가능하니, 시스템이 죽었을 때 가장 큰 돈(리스크)이 날아가는 곳부터 집중 타격하자"는 철학이 표준 전체에 깔려있다. 29119는 총 5개의 핵심 파트로 무장되어 있다. 용어를 정리한 **Part 1(개념 및 정의)**, 회사 전체의 테스트 파이프라인을 규정한 **Part 2(프로세스)**, 개발자들이 제일 싫어하는 서류 양식을 통일한 **Part 3(문서화)**, 화이트박스/블랙박스 기법들을 싹 다 모아놓은 백과사전인 **Part 4(테스트 기법)**, 마지막으로 최신 테스트 자동화를 위해 도입된 \*\*Part 5(키워드 주도 테스팅)\*\*다. 이 5형제는 폭포수든 애자일이든 가리지 않고 현대 소프트웨어의 품질을 보증하는 글로벌 여권 역할을 한다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 춘추전국시대를 끝낸 테스팅의 천하통일, ISO 29119 개요**

* **정의:** 기존에 개별적으로 흩어져 있던 소프트웨어 테스팅 관련 국제 표준(IEEE, BS 등)들을 **단일 규격으로 통합한 글로벌 소프트웨어 테스팅 범용 국제 표준**.
* **핵심 사상 (RBT):** 애자일(Agile), 데브옵스, 폭포수(Waterfall) 등 어떤 개발 생명주기(SDLC)에서도 유연하게 적용 가능하도록 설계되었으며, 표준의 모든 프로세스는 위험도가 높은 곳에 테스트 자원을 집중하는 **'리스크 기반 테스팅(Risk-Based Testing)' 철학을 기반으로 구동**됨.

#### **II. \[본론 1] 구시대 파편화 표준들의 통합과 리스크 기반 철학 (도식화)**

어떤 과거의 표준들을 집어삼키며 진화했는지 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3ODguMTg1IDQ3Mi43NSIgd2lkdGg9Ijc4OC4xODUiIGhlaWdodD0iNDcyLjc1IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfX18iIGRhdGEtbGFiZWw9IuqzvOqxsOydmCDtjIztjrjtmZTrkJwg7YWM7Iqk7YyFIOq3nOqyqeuTpCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMzE5LjY2OCIgaGVpZ2h0PSIyNjEuNDAwMDAwMDAwMDAwMDMiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIzMTkuNjY4IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+6rO86rGw7J2YIO2MjO2OuO2ZlOuQnCDthYzsiqTtjIUg6rec6rKp65OkPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX19fX0lTT0lFQ0lFRUVfMjkxMTkiIGRhdGEtbGFiZWw9Iu2VmOuCmOuhnCDsnLXtlanrkJwg7KCI64yAIO2RnOykgDogSVNPL0lFQy9JRUVFIDI5MTE5Ij4KICA8cmVjdCB4PSI0MDMuNjY4IiB5PSI3Ni4yNSIgd2lkdGg9IjM0NC41MTY5OTk5OTk5OTk5NCIgaGVpZ2h0PSIzNTYuNSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwMy42NjgiIHk9Ijc2LjI1IiB3aWR0aD0iMzQ0LjUxNjk5OTk5OTk5OTk0IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI0MTUuNjY4IiB5PSI5MC4yNSIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7tlZjrgpjroZwg7Jy17ZWp65CcIOygiOuMgCDtkZzspIA6IElTTy9JRUMvSUVFRSAyOTExOTwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTzEiIGRhdGEtdG89IlUiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjI3LjEwNCwxMzcuOCAyMjcuMTA0LDIzNy42NjI1MDAwMDAwMDAwMiA0NzMuNjY4LDIzNy42NjI1MDAwMDAwMDAwMiA0NzMuNjY4LDI1MC4wNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTzIiIGRhdGEtdG89IlUiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjE5LjY5NDAwMDAwMDAwMDAyLDIyNS4yNzUwMDAwMDAwMDAwMyAyMTkuNjk0MDAwMDAwMDAwMDIsMjM3LjY2MjUwMDAwMDAwMDAyIDQ3My42NjgsMjM3LjY2MjUwMDAwMDAwMDAyIDQ3My42NjgsMjUwLjA1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJPMyIgZGF0YS10bz0iVSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzNDMuNjY4LDI1OC41IDM1OS42NjgsMjU4LjUgMzkzLjY2OCwyNTguNSAzOTMuNjY4LDI1OC41MDAwMDAwMDAwMDAwNiA0MDMuNjY4LDI1OC41IDQzMS42NjgsMjU4LjUgNDMxLjY2OCwyNTkuMjc1IDQ0My42NjgsMjU5LjI3NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVSIgZGF0YS10bz0iUDEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDczLjY2OCwyODYuOTUwMDAwMDAwMDAwMDUgNDczLjY2OCwzMDAuOTUwMDAwMDAwMDAwMDUgNjIxLjkxOTUsMzAwLjk1MDAwMDAwMDAwMDA1IDYyMS45MTk1LDMxNC45NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVSIgZGF0YS10bz0iUDIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDczLjY2OCwyODYuOTUwMDAwMDAwMDAwMDUgNDczLjY2OCwzMDAuOTUwMDAwMDAwMDAwMDUgNjQxLjkyNjUsMzAwLjk1MDAwMDAwMDAwMDA1IDY0MS45MjY1LDM3OS44NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVSIgZGF0YS10bz0iUDMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNTAzLjY2OCwyNTYuMjAwMDAwMDAwMDAwMDUgNTE1LjY2OCwyNTYuMjAwMDAwMDAwMDAwMDUgNTE1LjY2OCwxMzguNyA1NTEuNjY4LDEzOC43IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJVIiBkYXRhLXRvPSJQNCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI1MDMuNjY4LDI2Mi4zNSA1MjcuNjY4LDI2Mi4zNSA1MjcuNjY4LDIwMy42IDU1MS42NjgsMTg5LjkyNTAwMDAwMDAwMDA0IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJVIiBkYXRhLXRvPSJQNSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI1MDMuNjY4LDI2OC41IDU1MS42NjgsMjY4LjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik8xIiBkYXRhLWxhYmVsPSJJRUVFIDgyOQrthYzsiqTtirgg66y47ISc7ZmUIO2RnOykgCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxNDQuNjI2IiB5PSI4NCIgd2lkdGg9IjE2NC45NTYwMDAwMDAwMDAwMiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjI3LjEwNCIgeT0iMTEwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjIyNy4xMDQiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5JRUVFIDgyOTwvdHNwYW4+PHRzcGFuIHg9IjIyNy4xMDQiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPu2FjOyKpO2KuCDrrLjshJztmZQg7ZGc7KSAPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik8yIiBkYXRhLWxhYmVsPSJJRUVFIDEwMDgK64uo7JyEIO2FjOyKpO2KuCDtkZzspIAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTQ0LjYyNiIgeT0iMTcxLjQ3NTAwMDAwMDAwMDAyIiB3aWR0aD0iMTUwLjEzNiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjE5LjY5NDAwMDAwMDAwMDAyIiB5PSIxOTguMzc1MDAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjIxOS42OTQwMDAwMDAwMDAwMiIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPklFRUUgMTAwODwvdHNwYW4+PHRzcGFuIHg9IjIxOS42OTQwMDAwMDAwMDAwMiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+64uo7JyEIO2FjOyKpO2KuCDtkZzspIA8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTzMiIGRhdGEtbGFiZWw9IkJTIDc5MjUtMSwyCu2FjOyKpO2KuCDsmqnslrQg67CPIOq4sOuylSDtkZzspIAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTQ0LjYyNiIgeT0iMjMxLjYwMDAwMDAwMDAwMDAyIiB3aWR0aD0iMTk5LjA0MiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjQ0LjE0NyIgeT0iMjU4LjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjI0NC4xNDciIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5CUyA3OTI1LTEsMjwvdHNwYW4+PHRzcGFuIHg9IjI0NC4xNDciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPu2FjOyKpO2KuCDsmqnslrQg67CPIOq4sOuylSDtkZzspIA8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSI2OC42MjYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI5MC4zMTMiIHk9IjEwMi40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Tm90ZTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iVSIgZGF0YS1sYWJlbD0iVSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0NDMuNjY4IiB5PSIyNTAuMDUiIHdpZHRoPSI2MCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0NzMuNjY4IiB5PSIyNjguNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+VTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUDEiIGRhdGEtbGFiZWw9IlBhcnQgMTog6rCc64WQL+ygleydmCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NTEuNjY4IiB5PSIzMTQuOTUiIHdpZHRoPSIxNDAuNTAzIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI2MjEuOTE5NSIgeT0iMzMzLjQiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlBhcnQgMTog6rCc64WQL+ygleydmDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUDIiIGRhdGEtbGFiZWw9IlBhcnQgMjog7ZSE66Gc7IS47IqkIDPqs4TsuLUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTUxLjY2OCIgeT0iMzc5Ljg1IiB3aWR0aD0iMTgwLjUxNjk5OTk5OTk5OTk3IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI2NDEuOTI2NSIgeT0iMzk4LjMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlBhcnQgMjog7ZSE66Gc7IS47IqkIDPqs4TsuLU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlAzIiBkYXRhLWxhYmVsPSJQYXJ0IDM6IOusuOyEnCDslpHsi50iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTUxLjY2OCIgeT0iMTIwLjI1IiB3aWR0aD0iMTQzLjQ2Njk5OTk5OTk5OTk4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI2MjMuNDAxNDk5OTk5OTk5OSIgeT0iMTM4LjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlBhcnQgMzog66y47IScIOyWkeyLnTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUDQiIGRhdGEtbGFiZWw9IlBhcnQgNDog7YWM7Iqk7Yq4IOq4sOuylSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NTEuNjY4IiB5PSIxNzEuNDc1MDAwMDAwMDAwMDIiIHdpZHRoPSIxNTguMjg2OTk5OTk5OTk5OTgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjYzMC44MTE1IiB5PSIxODkuOTI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5QYXJ0IDQ6IO2FjOyKpO2KuCDquLDrspU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlA1IiBkYXRhLWxhYmVsPSJQYXJ0IDU6IOyekOuPme2ZlCDquLDrspUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTUxLjY2OCIgeT0iMjUwLjA1IiB3aWR0aD0iMTU4LjI4Njk5OTk5OTk5OTk4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI2MzAuODExNSIgeT0iMjY4LjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlBhcnQgNTog7J6Q64+Z7ZmUIOq4sOuylTwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] ISO/IEC/IEEE 29119의 5대 핵심 Part 전격 해부 (3단 표 - 출제 1순위)**

각 파트(Part)의 번호와 명칭, 그리고 담당하는 핵심 역할을 무조건 매핑해서 암기해야 합니다.

| **표준 체계 (Part 번호)** | **공식 명칭 (영문/국문)**                         | **담고 있는 핵심 내용 및 실무 역할**                                                                                        |
| :------------------ | :---------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| **Part 1**          | **Concepts and Definitions** *(개념 및 정의)*  | 소프트웨어 테스팅에 대한 \*\*공통된 어휘(용어 사전)\*\*를 정의하고, 소프트웨어 생명주기(SDLC) 내에서 테스팅이 차지하는 역할과 기본 개념(리스크 기반 등)을 설명함.            |
| **Part 2**          | **Test Processes** *(테스트 프로세스)*           | 시스템을 테스트하는 과정을 **'조직 레벨, 테스트 관리 레벨, 동적 테스트 레벨'의 3계층 모델**로 정의하여, 테스팅 업무의 절차와 생명주기를 완벽히 규격화함.                    |
| **Part 3**          | **Test Documentation** *(테스트 문서화)*        | (구 IEEE 829 흡수). 테스트 전략, 테스트 계획서, 테스트 명세서, 테스트 완료 보고서 등 **개발자와 QA가 산출해야 할 모든 테스트 문서의 목차와 템플릿(양식)을 제공**함.       |
| **Part 4**          | **Test Techniques** *(테스트 기법)*            | (구 BS 7925 흡수). 명세 기반(블랙박스), 구조 기반(화이트박스), 경험 기반 테스트 **기법들을 총망라한 백과사전.** (동등 분할, 경곗값, 구문/결정 커버리지 등의 산출 공식 명시). |
| **Part 5**          | **Keyword-Driven Testing** *(키워드 주도 테스팅)* | 최근 추가된 표준으로, 개발 지식이 없는 테스터도 자동화 스크립트를 쉽게 작성할 수 있도록 돕는 \*\*'키워드 기반 테스트 자동화 프레임워크'\*\*의 아키텍처와 지침을 명시함.           |

#### **IV. \[결론/제언] 폭포수를 넘어 AI 시대의 품질 검증으로의 무한 확장**

* **(키워드 위주 2줄 마무리)** "ISO 29119는 과거의 경직된 폭포수 모델 전용 표준이라는 오해를 벗고, **'리스크 기반 테스팅(RBT)'의 유연함을 통해 현대의 애자일(Agile) 스프린트에 완벽히 융화**되었습니다. 더 나아가 최근에는 정적 분석(Part 6)을 넘어 자율주행, 인공지능(AI) 시스템 품질 검증 가이드라인(Part 11)까지 제정하며 미래 IT 생태계의 절대적인 품질 나침반으로 진화하고 있습니다."
