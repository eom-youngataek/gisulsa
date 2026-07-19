### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (DevSecOps 등장배경 - 보안이 항상 마지막이었던 문제) — 3~4줄
Ⅱ. 핵심원리 - Shift Left (본론①, 도식 1개 필수)
Ⅲ. 파이프라인 단계별 보안활동 (본론②, 핵심 배점)
Ⅳ. 문화적변화 및 도구체계
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 DevOps의 CI/CD파이프라인은 '빠르게 만들고 빠르게 배포하는 것'에 최적화됐는데, 보안점검이 전통적으로 '배포직전 마지막단계'에서만 이루어지다보니, 이 빨라진 파이프라인의 속도를 보안이 못따라가 병목이 되거나, 아예 건너뛰어지는 문제가 생겼다 → 보안을 파이프라인 전체(왼쪽 끝, 즉 초기단계)로 이동시키자는 게 DevSecOps"\*\*라는 한 줄로 시작하면, 왜 DevOps답안 바로 다음에 나오는 게 자연스러운지 논리가 섭니다.

### Ⅱ. 핵심원리 — Shift Left(왼쪽으로 이동)

| 구분         | 전통적방식                | DevSecOps            |
| :--------- | :------------------- | :------------------- |
| **보안개입시점** | 개발완료후 **배포직전(맨오른쪽)** | **요구분석·설계단계부터(맨왼쪽)** |
| **결함발견비용** | 늦게발견할수록 **수정비용급증**   | 초기발견으로 **수정비용최소화**   |
| **책임주체**   | **보안팀만의 책임**(Dev와분리) | **개발자도 보안책임 공유**     |

→ 암기: **"보안을 오른쪽(끝)에서 왼쪽(시작)으로 옮긴다"** — 앞서 다룬 "V모델의 조기테스트설계"와 정확히 같은 논리구조입니다: \*\*"검증(이경우보안검증)을 사후활동이 아니라 각 단계와 동시에 계획한다"\*\*는 원리가 여기서 보안영역에 적용된 것입니다.

### 도식화 제안

```
[전통방식]
요구→설계→개발→테스트→배포→[보안점검]  ← 맨끝에서만, 늦음, 병목

[DevSecOps - Shift Left]
[보안]요구→[보안]설계→[보안]개발→[보안]테스트→[보안]배포→운영
(모든단계에 보안이 촘촘히 내재화)
```

### Ⅲ. 파이프라인 단계별 보안활동 — 핵심 배점

**함정 방지: "보안을 앞에 놓는다"고만 답하면 절반. 각 단계마다 구체적으로 무엇을 하는지 나열해야 완성됩니다.**

| 단계           | 보안활동                                                                                         |
| :----------- | :------------------------------------------------------------------------------------------- |
| **설계단계**     | **위협모델링**(Threat Modeling) — 앞서다룬 "리스크관리"의 사전위험식별을 보안에 적용                                    |
| **코딩단계**     | **SAST**(정적분석, Static Application Security Testing) — 코드자체를 실행없이 분석해 취약점탐지                   |
| **빌드/테스트단계** | **SCA**(소프트웨어구성분석) — 오픈소스라이브러리의 **알려진취약점(CVE)** 검사, **DAST**(동적분석) — 실행중인애플리케이션을 공격해보며 취약점탐지 |
| **배포/운영단계**  | **컨테이너이미지스캐닝**, **런타임보안모니터링**, IaC(인프라코드) 보안점검                                               |

→ 암기: **"설계는 위협모델링, 코딩은 SAST, 빌드는 SCA+DAST, 운영은 이미지스캐닝+런타임감시"** — 앞서다룬 "CI/CD파이프라인"의 각 단계(빌드-테스트-배포)마다 **보안검사도구가 하나씩 끼어들어간다**는 게 실무구현의 핵심입니다.

### Ⅳ. 문화적변화 및 도구체계

**함정 방지: 도구나열만 하면 절반. "문화"가 왜 핵심가치인지 보여줘야 완성됩니다.**

| 구분                | 내용                                                      |
| :---------------- | :------------------------------------------------------ |
| **문화변화**          | "보안은 보안팀일" → **"보안은 모두의 일"**(개발자가 직접 SAST결과를 보고 스스로 수정) |
| **자동화게이트**        | 보안취약점이 **일정심각도이상**이면 파이프라인을 **자동으로 중단**(수동검토가 아닌 자동차단)  |
| **컴플라이언스as Code** | 보안·규제요건을 **코드형태로 자동검증**(수동체크리스트 대체)                     |

→ 앞서 다룬 "정보시스템감리"·"CSAP" 답안에서 봤던 \*\*"제3자가 사후에 검증하는 방식"\*\*과 달리, DevSecOps는 \*\*"파이프라인 자체가 실시간으로 자가검증"\*\*한다는 점에서 검증패러다임 자체가 다르다는 게 심화 비교 포인트입니다.

### Ⅴ. 결론 포인트 (DevOps 시리즈 완결)

DevSecOps의 본질은 \*\*"속도(DevOps)와 안전성(보안)이 상충한다는 통념을 깨고, 보안을 파이프라인에 내재화하면 오히려 둘 다 얻을 수 있다"\*\*는 것입니다 — 이는 앞서 다룬 V모델(조기테스트설계), 카나리테스트(위험의조기감지), 나선형모델(매반복마다 위험분석)에서 반복된 \*\*"문제를 늦게 발견할수록 비용이 커지니, 최대한 앞당겨 발견하라"\*\*는 오늘 하루 다룬 여러 시리즈의 공통결론이 보안영역에서 재현된 사례이며, 이로써 오늘 다룬 애자일→DevOps→DevSecOps 시리즈가 \*\*"빠르게, 안전하게, 처음부터 함께"\*\*라는 하나의 통합된 개발철학으로 완결됩니다.



### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "과거에는 보안팀이 깐깐한 경찰관 같았다. 데브옵스(DevOps)의 도입으로 개발팀이 코드를 미친 듯이 빨리 짜서 배포하려는데, 릴리즈 배포 바로 전날 보안팀이 나타나 '이 코드 취약점 투성이야! 다 다시 짜!'라며 거대한 태클을 걸었다. 1분 1초가 급한 데브옵스의 초고속 고속도로에 보안팀이라는 거대한 '톨게이트 병목(Bottleneck)'이 생겨버린 것이다. 이 딜레마를 박살 내기 위해 등장한 혁명이 바로 \*\*'DevSecOps(데브섹옵스)'\*\*다. DevSecOps는 보안 검사를 맨 마지막에 몰아서 하는 게 아니라, 코딩, 빌드, 테스트, 배포에 이르는 CI/CD 파이프라인 전 과정 구석구석에 \*\*'자동화된 보안 점검 로봇'\*\*을 내재화시켰다. 개발자가 코드를 타이핑하는 순간부터 플러그인이 보안을 실시간 체크하고, 젠킨스(Jenkins)에서 빌드할 때 남이 만든 오픈소스의 취약점(SCA)과 소스코드 오류(SAST)를 기계가 0.1초 만에 검사해 버린다. 즉, 보안 검사의 타이밍을 프로세스의 맨 앞단(왼쪽)으로 확 끌어당기는 **'Shift-Left(시프트 레프트)'** 사상이 핵심이다. 이를 통해 배포 속도를 1도 늦추지 않으면서, 태생부터 해킹에 안전한 '방탄조끼를 입은 소프트웨어'를 찍어내게 되었다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 속도와 보안의 딜레마를 박살 내다, DevSecOps 개요**

* **정의:** 기존의 DevOps(개발+운영) 환경에 \*\*'Security(보안)'\*\*를 통합하여, 소프트웨어 생명주기(SDLC)의 **기획부터 배포, 운영까지의 '모든 단계'에 보안을 투명하고 자동화된 형태로 내재화하는 철학이자 프랙티스**.
* **목적:** 보안 점검으로 인한 **배포 지연(병목)을 완전히 제거**하면서도, 무결성이 보장된 안전한 소프트웨어를 초고속으로 지속 배포(Continuous Delivery)하기 위함.

#### **II. \[본론 1] 보안 병목 톨게이트를 없애는 마법: 'Shift-Left' 사상 (도식화)**

보안 검사가 맨 끝에서 앞(왼쪽)으로 당겨지는 핵심 철학의 시각화입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MDYuNDYyNSA2NTUuOTU5MDAwMDAwMDAwMSIgd2lkdGg9IjYwNi40NjI1IiBoZWlnaHQ9IjY1NS45NTkwMDAwMDAwMDAxIiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfX19fX19fIiBkYXRhLWxhYmVsPSLquLDsobTsnZgg67O07JWIIOygkOqygCDrs5HrqqkgKOuztOyViOydtCDrp6gg64Gd7JeQIOychOy5mCkiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjI1My4zNDE1MDAwMDAwMDAwMiIgaGVpZ2h0PSI1NzUuOTU5MDAwMDAwMDAwMSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjI1My4zNDE1MDAwMDAwMDAwMiIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPuq4sOyhtOydmCDrs7TslYgg7KCQ6rKAIOuzkeuqqSAo67O07JWI7J20IOunqCDrgZ3sl5Ag7JyE7LmYKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IkRldlNlY09wc19fU2hpZnRMZWZ0X19fIiBkYXRhLWxhYmVsPSJEZXZTZWNPcHPsnZgg7ZW17IusOiBTaGlmdC1MZWZ0ICjsmbzsqr3snLzroZwg64u56riw6riwKSDsgqzsg4EiPgogIDxyZWN0IHg9IjMyMS4zNDE1IiB5PSI0MCIgd2lkdGg9IjI0NS4xMjA5OTk5OTk5OTk5OCIgaGVpZ2h0PSI1MDQuMSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjMyMS4zNDE1IiB5PSI0MCIgd2lkdGg9IjI0NS4xMjA5OTk5OTk5OTk5OCIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzMzLjM0MTUiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPkRldlNlY09wc+ydmCDtlbXsi6w6IFNoaWZ0LUxlZnQgKOyZvOyqveycvOuhnCDri7nquLDquLApIOyCrOyDgTwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTzEiIGRhdGEtdG89Ik8yIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE0NC4xNzk1MDAwMDAwMDAwMiwxMjAuOSAxNDQuMTc5NTAwMDAwMDAwMDIsMTY4LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209Ik8yIiBkYXRhLXRvPSJPMyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxNDQuMTc5NTAwMDAwMDAwMDIsMjA1LjggMTQ0LjE3OTUwMDAwMDAwMDAyLDI2Mi4yNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTzMiIGRhdGEtdG89Ik80IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE0NC4xNzk1MDAwMDAwMDAwMiwyOTkuMTUwMDAwMDAwMDAwMDMgMTQ0LjE3OTUwMDAwMDAwMDAyLDMzOC43MDAwMDAwMDAwMDAwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTzQiIGRhdGEtdG89Ik81IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE0NC4xNzk1MDAwMDAwMDAwMiw1MTUuMDU5MDAwMDAwMDAwMSAxNDQuMTc5NTAwMDAwMDAwMDIsNTYzLjA1OSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRDEiIGRhdGEtdG89IkQyIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQ0My45MDIsMTIwLjkgNDQzLjkwMiwxNjguOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRDIiIGRhdGEtdG89IkQzIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQ0My45MDIsMjIyLjcwMDAwMDAwMDAwMDAyIDQ0My45MDIsMjYyLjI1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJEMyIgZGF0YS10bz0iRDQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDQzLjkwMiwzMTYuMDQ5OTk5OTk5OTk5OTUgNDQzLjkwMiwzNzIuNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRDQiIGRhdGEtdG89IkQ1IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQ0My45MDIsNDI2LjMgNDQzLjkwMiw0NzQuMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTzEiIGRhdGEtbGFiZWw9IkNvZGUiIGRhdGEtc2hhcGU9InJvdW5kZWQiPgogIDxyZWN0IHg9IjEwNy42NDM1IiB5PSI4NCIgd2lkdGg9IjczLjA3MiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSI2IiByeT0iNiIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE0NC4xNzk1MDAwMDAwMDAwMiIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5Db2RlPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJPMiIgZGF0YS1sYWJlbD0iQnVpbGQiIGRhdGEtc2hhcGU9InJvdW5kZWQiPgogIDxyZWN0IHg9IjEwOC4zODQ1IiB5PSIxNjguOSIgd2lkdGg9IjcxLjU5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjYiIHJ5PSI2IiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTQ0LjE3OTUwMDAwMDAwMDAyIiB5PSIxODcuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkJ1aWxkPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJPMyIgZGF0YS1sYWJlbD0iVGVzdCIgZGF0YS1zaGFwZT0icm91bmRlZCI+CiAgPHJlY3QgeD0iMTA5Ljg2NjUiIHk9IjI2Mi4yNSIgd2lkdGg9IjY4LjYyNiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSI2IiByeT0iNiIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE0NC4xNzk1MDAwMDAwMDAwMiIgeT0iMjgwLjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlRlc3Q8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik80IiBkYXRhLWxhYmVsPSLrs7TslYjtjIAg6rKA7IKsIPCfmqgK7IiY64+ZIOygkOqygCDrsI8g7YOc7YG0IiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjE0NC4xNzk1MDAwMDAwMDAwMiwzMzguNzAwMDAwMDAwMDAwMDUgMjMyLjM1OTAwMDAwMDAwMDA0LDQyNi44Nzk1MDAwMDAwMDAwNiAxNDQuMTc5NTAwMDAwMDAwMDIsNTE1LjA1OTAwMDAwMDAwMDEgNTYuMDAwMDAwMDAwMDAwMDE0LDQyNi44Nzk1MDAwMDAwMDAwNiIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTQ0LjE3OTUwMDAwMDAwMDAyIiB5PSI0MjYuODc5NTAwMDAwMDAwMDYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE0NC4xNzk1MDAwMDAwMDAwMiIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuuztOyViO2MgCDqsoDsgqwg8J+aqDwvdHNwYW4+PHRzcGFuIHg9IjE0NC4xNzk1MDAwMDAwMDAwMiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7IiY64+ZIOygkOqygCDrsI8g7YOc7YG0PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik81IiBkYXRhLWxhYmVsPSJEZXBsb3kiIGRhdGEtc2hhcGU9InJvdW5kZWQiPgogIDxyZWN0IHg9IjEwMi40NTY1IiB5PSI1NjMuMDU5IiB3aWR0aD0iODMuNDQ2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjYiIHJ5PSI2IiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTQ0LjE3OTUwMDAwMDAwMDAyIiB5PSI1ODEuNTA5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5EZXBsb3k8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik5vdGUiIGRhdGEtbGFiZWw9Ik5vdGUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjA4LjcxNTUwMDAwMDAwMDAyIiB5PSI4NCIgd2lkdGg9IjY4LjYyNiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI0My4wMjg1IiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk5vdGU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkQxIiBkYXRhLWxhYmVsPSLrs7TslYgg6riw7ZqNIiBkYXRhLXNoYXBlPSJyb3VuZGVkIj4KICA8cmVjdCB4PSIzOTIuMTc1NSIgeT0iODQiIHdpZHRoPSIxMDMuNDUzIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjYiIHJ5PSI2IiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDQzLjkwMiIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7rs7TslYgg6riw7ZqNPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJEMiIgZGF0YS1sYWJlbD0iQ29kZSDwn5uh77iPCuyLpOyLnOqwhCDsi5ztgZDslrTsvZTrlKkiIGRhdGEtc2hhcGU9InJvdW5kZWQiPgogIDxyZWN0IHg9IjM2Mi41MzU0OTk5OTk5OTk5NiIgeT0iMTY4LjkiIHdpZHRoPSIxNjIuNzMzIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjYiIHJ5PSI2IiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0NDMuOTAxOTk5OTk5OTk5OTMiIHk9IjE5NS44IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0NDMuOTAxOTk5OTk5OTk5OTMiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5Db2RlIPCfm6HvuI88L3RzcGFuPjx0c3BhbiB4PSI0NDMuOTAxOTk5OTk5OTk5OTMiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyLpOyLnOqwhCDsi5ztgZDslrTsvZTrlKk8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRDMiIGRhdGEtbGFiZWw9IkJ1aWxkIPCfm6HvuI8K7J6Q64+Z7ZmUIOyGjOyKpC/smKTtlIjshozsiqQg6rKA7IKsIiBkYXRhLXNoYXBlPSJyb3VuZGVkIj4KICA8cmVjdCB4PSIzMzcuMzQxNSIgeT0iMjYyLjI1IiB3aWR0aD0iMjEzLjEyMDk5OTk5OTk5OTk4IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjYiIHJ5PSI2IiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0NDMuOTAyIiB5PSIyODkuMTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjQ0My45MDIiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5CdWlsZCDwn5uh77iPPC90c3Bhbj48dHNwYW4geD0iNDQzLjkwMiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7J6Q64+Z7ZmUIOyGjOyKpC/smKTtlIjshozsiqQg6rKA7IKsPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkQ0IiBkYXRhLWxhYmVsPSJUZXN0IPCfm6HvuI8K66qo7J2YIO2VtO2CuSDsnpDrj5kg7Iqk7LqUIiBkYXRhLXNoYXBlPSJyb3VuZGVkIj4KICA8cmVjdCB4PSIzNjAuMzEyNSIgeT0iMzcyLjUiIHdpZHRoPSIxNjcuMTc5IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjYiIHJ5PSI2IiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0NDMuOTAyIiB5PSIzOTkuNCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNDQzLjkwMiIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPlRlc3Qg8J+boe+4jzwvdHNwYW4+PHRzcGFuIHg9IjQ0My45MDIiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuuqqOydmCDtlbTtgrkg7J6Q64+ZIOyKpOy6lDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJENSIgZGF0YS1sYWJlbD0iRGVwbG95IPCfmoAK7JWI7KCE7ZWcIOy7qO2FjOydtOuEiCDrsLDtj6wiIGRhdGEtc2hhcGU9InJvdW5kZWQiPgogIDxyZWN0IHg9IjM1NC4wMTQiIHk9IjQ3NC4zIiB3aWR0aD0iMTc5Ljc3NTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjYiIHJ5PSI2IiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjQ0My45MDIiIHk9IjUwMS4yIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0NDMuOTAyIiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+RGVwbG95IPCfmoA8L3RzcGFuPjx0c3BhbiB4PSI0NDMuOTAyIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7slYjsoITtlZwg7Luo7YWM7J2064SIIOuwsO2PrDwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] CI/CD 파이프라인에 융합된 단계별 자동화 보안 기술 (3단 표 - 출제 1순위)**

보안 전문가 없이도 CI/CD 로봇이 알아서 수행하는 핵심 보안 스캐닝 3대장입니다.

| **CI/CD 단계**                  | **융합된 핵심 자동화 보안 기술**             | **상세 보안 수행 내용 및 목적**                                                                                    |
| :---------------------------- | :------------------------------- | :------------------------------------------------------------------------------------------------------ |
| **1. Code / Build (코드 통합 시)** | **SAST 🔍** *(정적 애플리케이션 보안 테스트)* | 앱을 실행하지 않고 **소스코드 자체의 텍스트 구조를 스캔**하여, SQL 인젝션이나 하드코딩된 패스워드 등 코드상의 보안 취약점을 즉각 찾아냄.                       |
| **2. Build (라이브러리 취약점)**      | **SCA 📦** *(소프트웨어 구성 분석)*       | 개발자가 가져다 쓴 수많은 **외부 오픈소스(Third-party) 라이브러리와 컨테이너 이미지**에 알려진 해킹 취약점이나 라이선스 위반이 있는지 분석함. (Log4j 사태 방어용). |
| **3. Test / Deploy (배포 직전)**  | **DAST 💥** *(동적 애플리케이션 보안 테스트)* | 앱이 테스트 서버에 올라가 **실제 '실행(Running)' 중인 상태에서**, 해커처럼 외부에서 공격 페이로드를 마구 던져보며 런타임 취약점을 스캐닝함.                  |

*(이 외에도 운영(Ops) 단계에서의 RASP(런타임 애플리케이션 자가 보호) 방어 기술이 적용됩니다.)*

#### **IV. \[결론/제언] '보안의 코드화(Security as Code)'와 클라우드 생태계의 필수 생존법**

* **(키워드 위주 2줄 마무리)** "DevSecOps를 성공시키는 열쇠는 사람(보안 담당자)의 개입을 줄이고 보안 정책 자체를 스크립트로 짜서 파이프라인에 박아 넣는 \*\*'보안의 코드화(Security as Code)'\*\*에 있습니다. 도커(Docker)와 쿠버네티스로 대변되는 현대 클라우드 마이크로서비스 환경에서, 1초 만에 생성되는 컨테이너들의 무결성을 지키기 위해 DevSecOps는 선택이 아닌 시스템 생존을 위한 절대적 필수 요소가 되었습니다."
