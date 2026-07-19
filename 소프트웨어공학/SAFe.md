### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (SAFe 등장배경 - 애자일의 확장문제) — 3~4줄
Ⅱ. 4대 구성(레벨) (본론①, 도식 1개 필수)
Ⅲ. 핵심가치 및 원칙 (본론②, 핵심 배점)
Ⅳ. 최신동향 - AI시대 대응
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 스크럼은 팀단위(5\~9명)에서 완벽하게 동작하지만, 수백개 팀이 하나의 대형시스템을 함께 만들어야 하는 대기업환경에서는 '팀들 간 정렬(Alignment)'이라는 새로운 문제가 생긴다 — SAFe는 린의 원칙 위에 스크럼/칸반 팀들을 계층적으로 쌓아올려 이 정렬문제를 해결하는 프레임워크"\*\*라는 한 줄로 시작하면, 오늘 앞서 다룬 스크럼·린 답안과 자연스럽게 이어집니다.

### Ⅱ. 4대 구성(레벨) — "팀·프·대·포"

| 레벨   | 구성명                     | 핵심역할                            |
| :--- | :---------------------- | :------------------------------ |
| 최소단위 | **Essential SAFe**      | 팀·프로그램수준 정렬 — 모든 구성의 **기본단위**   |
| 중간규모 | **Large Solution SAFe** | 여러 프로그램(ART)이 모여 **대규모솔루션** 개발시 |
| 전략연계 | **Portfolio SAFe**      | 전략포트폴리오와 **예산·투자 연계**           |
| 최대규모 | **Full SAFe**           | 위 3개를 **모두 포함**한 최대구성           |

→ 암기: **"필수(팀+프로그램) → 대형솔루션(여러프로그램) → 포트폴리오(전략연계) → 전체(다합침)"** — 조직규모가 커질수록 아래 구성요소를 계층적으로 얹어가는 구조입니다.

### 도식화 제안

```
              [Full SAFe] (전체통합)
                    ↑
         [Portfolio SAFe] (전략·투자연계)
                    ↑
      [Large Solution SAFe] (다중프로그램 솔루션)
                    ↑
        [Essential SAFe] ← 모든구성의 기본토대
       (팀+프로그램 수준 정렬, 스크럼팀들의 집합)
```

→ "피라미드처럼 아래(팀)에서 위(전략)로 정렬이 쌓여올라간다"는 게 SAFe의 핵심 이미지입니다.

### Ⅲ. 핵심가치 및 원칙 — 핵심 배점

**함정 방지: "여러팀을 관리하는 프레임워크"라고만 답하면 절반. 무엇을 기준으로 정렬시키는지 구체적 원칙을 보여줘야 완성됩니다.**

| 원칙           | 내용                                              |
| :----------- | :---------------------------------------------- |
| **가치중심조직화**  | 전문성·부서 위계가 아니라 **가치흐름(Value Stream)** 중심으로 조직구성 |
| **점진적구축**    | **짧은반복학습주기**로 고객피드백을 빠르게 반영(앞서다룬 애자일원칙 확장)      |
| **객관적마일스톤**  | 개발생애주기 전반에 **객관적 평가지점**을 두어 투자성과 확인             |
| **끊김없는가치흐름** | 가치전달을 막는요소를 **신속히 식별·제거**(린의 낭비제거 원칙 그대로)       |

→ 앞서 다룬 "린SW개발 7대원칙(전체최적화·낭비제거)"이 SAFe의 조직설계원리로 그대로 확장되어 있다는 연결이 핵심입니다. 또한 **정보전달이 하향식(top-down)이 아니라 적시에 위아래로 오간다**는 것과, \*\*"품질을 타협하고 애자일을 얻을 수 없다"\*\*는 원칙에 따라 흐름·아키텍처·코드·시스템·릴리스 5차원의 \*\*"내재된품질(Built-in Quality)"\*\*을 모든수준에서 요구한다는 점이 특징적입니다.

### Ⅳ. 최신동향 — AI시대 대응 (2026, 최신성 어필)

2026년 6월, Scaled Agile은 \*\*"AI-Native SAFe"\*\*를 새롭게 발표했습니다 — 이는 기존SAFe에 AI기능을 단순히 얹은 것이 아니라, **AI가 제품팀뿐 아니라 조직전체의 업무방식을 재편하는 상황에서, 엔터프라이즈규모로 AI를 거버넌스있게 활용하도록 설계된 운영모델**입니다. 현재 SAFe는 전세계 **2만개이상의 기업·정부기관, 200만명이상의 실무자**가 사용하는 프레임워크로 성장했습니다.

→ "SAFe도 앞서 다룬 AX(AI전환) 흐름을 조직관리프레임워크 차원에서 받아들이고 있다"는 점이, 이 답안을 오늘 초반에 다룬 "AX 추진절차" 답안과 연결시켜주는 최신 포인트입니다.

### Ⅴ. 결론 포인트 (애자일확장 시리즈 완결)

SAFe는 \*\*"팀단위 애자일(스크럼/칸반/XP)의 성공을, 조직전체 규모로 확장하려면 무엇이 더 필요한가"\*\*에 대한 답이며, 이는 린의 원칙(전체최적화, 낭비제거)을 계층적 조직구조(Essential→Large Solution→Portfolio→Full)로 구현한 것입니다 — 앞서 다룬 방법론테일러링의 논리처럼, 조직규모가 작으면 스크럼/칸반만으로 충분하지만, \*\*"수십\~수백개 팀이 하나의 전략을 향해 동시에 나아가야 할 때"\*\*는 SAFe같은 확장프레임워크가 필요해진다는 결론으로, 오늘 다룬 애자일계열 시리즈(매니페스토→스크럼/칸반/XP→린→SAFe)를 팀규모의 스펙트럼(소규모→대규모)으로 완결할 수 있습니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "애자일의 스크럼(Scrum)은 5~~9명 내외의 작은 팀이 빠르고 기민하게 움직이는 데 최적화된 방법론이다. 하지만 삼성전자나 은행처럼 1,000명의 개발자가 모여 거대한 차세대 시스템을 만들 때, 이 작은 스크럼 팀 100개가 각자 알아서 뛰어다니면 팀 간에 엉키고 통합이 불가능해 프로젝트가 산으로 간다. 작은 톱니바퀴들을 모아 거대한 기업 단위의 톱니바퀴로 정확하게 맞물려 돌아가게 만드는 '확장팩'이 필요한데, 이것이 바로 \*\*'SAFe(Scaled Agile Framework, 대규모 애자일 프레임워크)'\*\*다. SAFe는 작은 애자일 팀 10개 정도(약 50~~125명)를 묶어 \*\*'ART(Agile Release Train, 애자일 릴리즈 기차)'\*\*라는 가상의 거대 조직에 태운다. 이 기차에 탄 모든 팀들은 똑같은 일정 주기(PI: Program Increment, 보통 10주)에 맞춰 동시에 개발하고, 묶어서 릴리즈한다. 기차가 출발하기 전, 100명이 한 강당에 모여 서로의 일정을 조율하는 'PI Planning'이라는 거대한 회의를 연다. 이처럼 제일 밑의 단위 '팀(Team)'부터, 팀들의 묶음인 '프로그램(Program)', 회사의 전략과 예산을 쥐고 있는 임원진 '포트폴리오(Portfolio)'까지, 애자일을 전사적으로 층층이 스케일업(Scaling)한 궁극의 체계가 바로 SAFe다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 작은 스크럼 팀을 묶어 거대한 군단으로, SAFe 개요**

* **정의:** 애자일(Agile), 린(Lean) 제품 개발, 그리고 시스템 사고(Systems Thinking)의 철학을 결합하여, **수십 명에서 수천 명에 이르는 대규모 엔터프라이즈 환경 전사적 규모(Enterprise-Scale)로 애자일을 확장(Scaling)하여 적용할 수 있도록 만든 프레임워크**.
* **등장 배경:** 기존 스크럼이나 XP는 10명 미만의 단일 팀 단위 개발에는 강력하나, \*\*부서 간 의존성이 높고 아키텍처가 복잡한 대규모 엔터프라이즈 프로젝트에서는 팀 간 일정 동기화 및 통합(Integration)의 실패(병목 현상)\*\*를 초래했기 때문임.

#### **II. \[본론 1] 팀에서 전사 경영까지: SAFe의 핵심 계층 구조 (도식화)**

Essential SAFe 모델을 기준으로 하위 팀부터 상위 포트폴리오까지의 수직 구조를 그립니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3NDUuMTE4OTk5OTk5OTk5OSA0MzEuMiIgd2lkdGg9Ijc0NS4xMTg5OTk5OTk5OTk5IiBoZWlnaHQ9IjQzMS4yIiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJTQUZlX1NjYWxlZF9BZ2lsZV9GcmFtZXdvcmtfX18iIGRhdGEtbGFiZWw9IlNBRmUgKFNjYWxlZCBBZ2lsZSBGcmFtZXdvcmspIO2VteyLrCDqs4TsuLUg7JWE7YKk7YWN7LKYIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI2NjUuMTE4OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNTEuMiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjY2NS4xMTg5OTk5OTk5OTk5IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+U0FGZSAoU2NhbGVkIEFnaWxlIEZyYW1ld29yaykg7ZW17IusIOqzhOy4tSDslYTtgqTthY3sspg8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlAiIGRhdGEtdG89IlIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzcyLjU1OTQ5OTk5OTk5OTk2LDE2My4xNDk5OTk5OTk5OTk5OCAzNzIuNTU5NDk5OTk5OTk5OTYsMjAyLjciIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlIiIGRhdGEtdG89IlQxIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjM3Mi41NTk0OTk5OTk5OTk5NiwyNzMuNCAzNzIuNTU5NDk5OTk5OTk5OTYsMjk3LjQgMzcyLjU1OTQ5OTk5OTk5OTk2LDI5Ny40IDM3Mi41NTk0OTk5OTk5OTk5NiwzMjEuNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUiIgZGF0YS10bz0iVDIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzcyLjU1OTQ5OTk5OTk5OTk2LDI3My40IDM3Mi41NTk0OTk5OTk5OTk5NiwyOTcuNCA1OTIuOTMyNSwyOTcuNCA1OTIuOTMyNSwzMjEuNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUiIgZGF0YS10bz0iVDMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzcyLjU1OTQ5OTk5OTk5OTk2LDI3My40IDM3Mi41NTk0OTk5OTk5OTk5NiwyOTcuNCAxNTIuMTg2NSwyOTcuNCAxNTIuMTg2NSwzMjEuNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUCIgZGF0YS1sYWJlbD0iMy4gUG9ydGZvbGlvIExldmVsICjtj6ztirjtj7TrpqzsmKQg6rOE7Li1KSDwn4+b77iPCuq4sOyXheydmCDsoITrnrXsoIEg67Cp7ZalIOuwjyDtiKzsnpAg7JiI7IKwIOuwsOu2hArsnoTsm5Dsp4TsnZgg7JeQ7ZS9KEVwaWMpIOygleydmCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyMzIuNjU0IiB5PSI5Mi40NSIgd2lkdGg9IjI3OS44MTEiIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzNzIuNTU5NDk5OTk5OTk5OTYiIHk9IjEyNy44MDAwMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMzcyLjU1OTQ5OTk5OTk5OTk2IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+My4gUG9ydGZvbGlvIExldmVsICjtj6ztirjtj7TrpqzsmKQg6rOE7Li1KSDwn4+b77iPPC90c3Bhbj48dHNwYW4geD0iMzcyLjU1OTQ5OTk5OTk5OTk2IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7quLDsl4XsnZgg7KCE65617KCBIOuwqe2WpSDrsI8g7Yis7J6QIOyYiOyCsCDrsLDrtoQ8L3RzcGFuPjx0c3BhbiB4PSIzNzIuNTU5NDk5OTk5OTk5OTYiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyehOybkOynhOydmCDsl5DtlL0oRXBpYykg7KCV7J2YPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlIiIGRhdGEtbGFiZWw9IjIuIFByb2dyYW0gTGV2ZWwgKO2UhOuhnOq3uOueqCDqs4TsuLUpIPCfmoQK7Jes65+sIOyVoOyekOydvCDtjIDsnYQg66y27J2AIOqxsOuMgO2VnCAnQVJUIOq4sOywqCcKUEkgKFByb2dyYW0gSW5jcmVtZW50KSDri6jsnITroZwg6rCA7LmYIOumtOumrOymiCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyMjIuMjc5OTk5OTk5OTk5OTciIHk9IjIwMi43IiB3aWR0aD0iMzAwLjU1ODk5OTk5OTk5OTk3IiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIzNzIuNTU5NDk5OTk5OTk5OTYiIHk9IjIzOC4wNDk5OTk5OTk5OTk5OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMzcyLjU1OTQ5OTk5OTk5OTk2IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+Mi4gUHJvZ3JhbSBMZXZlbCAo7ZSE66Gc6re4656oIOqzhOy4tSkg8J+ahDwvdHNwYW4+PHRzcGFuIHg9IjM3Mi41NTk0OTk5OTk5OTk5NiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7Jes65+sIOyVoOyekOydvCDtjIDsnYQg66y27J2AIOqxsOuMgO2VnCAmIzM5O0FSVCDquLDssKgmIzM5OzwvdHNwYW4+PHRzcGFuIHg9IjM3Mi41NTk0OTk5OTk5OTk5NiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+UEkgKFByb2dyYW0gSW5jcmVtZW50KSDri6jsnITroZwg6rCA7LmYIOumtOumrOymiDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJUMSIgZGF0YS1sYWJlbD0iMS4gVGVhbSBMZXZlbCAo7YyAIOqzhOy4tSkg8J+PgwrsiqTtgazrn7wg7YyAIDEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjc2LjM3MyIgeT0iMzIxLjQiIHdpZHRoPSIxOTIuMzczIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzNzIuNTU5NDk5OTk5OTk5OTYiIHk9IjM0OC4yOTk5OTk5OTk5OTk5NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMzcyLjU1OTQ5OTk5OTk5OTk2IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+MS4gVGVhbSBMZXZlbCAo7YyAIOqzhOy4tSkg8J+PgzwvdHNwYW4+PHRzcGFuIHg9IjM3Mi41NTk0OTk5OTk5OTk5NiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7Iqk7YGs65+8IO2MgCAxPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlQyIiBkYXRhLWxhYmVsPSIxLiBUZWFtIExldmVsICjtjIAg6rOE7Li1KSDwn4+DCuyKpO2BrOufvCDtjIAgMiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0OTYuNzQ2IiB5PSIzMjEuNCIgd2lkdGg9IjE5Mi4zNzMiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjU5Mi45MzI1IiB5PSIzNDguMjk5OTk5OTk5OTk5OTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjU5Mi45MzI1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+MS4gVGVhbSBMZXZlbCAo7YyAIOqzhOy4tSkg8J+PgzwvdHNwYW4+PHRzcGFuIHg9IjU5Mi45MzI1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7siqTtgazrn7wg7YyAIDI8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iVDMiIGRhdGEtbGFiZWw9IjEuIFRlYW0gTGV2ZWwgKO2MgCDqs4TsuLUpIPCfj4MK7Lm467CYIO2MgCAzIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIzMjEuNCIgd2lkdGg9IjE5Mi4zNzMiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE1Mi4xODY1IiB5PSIzNDguMjk5OTk5OTk5OTk5OTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE1Mi4xODY1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+MS4gVGVhbSBMZXZlbCAo7YyAIOqzhOy4tSkg8J+PgzwvdHNwYW4+PHRzcGFuIHg9IjE1Mi4xODY1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7subjrsJgg7YyAIDM8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NDAuNDY0OTk5OTk5OTk5OSIgeT0iOTIuNDUiIHdpZHRoPSI2OC42MjYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1NzQuNzc3OTk5OTk5OTk5OSIgeT0iMTEwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk5vdGU8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] SAFe를 굴러가게 만드는 3대 핵심 메커니즘 (3단 표 - 출제 1순위)**

SAFe를 일반 애자일과 구분 짓는 가장 고유한 용어들입니다.

| **핵심 용어 명칭**                          | **개념 및 정의 (What)**                                                                    | **수행 역할 및 목적 (Why & How)**                                                                    |
| :------------------------------------ | :------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------- |
| **1. ART 🚄** *(Agile Release Train)* | **약 50명\~125명의 인원으로 구성된 '애자일 릴리즈 기차'.** 여러 개의 애자일(스크럼) 팀들을 가상으로 묶어 놓은 거대한 애자일 부대.     | 개별 팀들이 제멋대로 개발하지 못하도록, **이 기차에 탄 모든 팀은 동일한 박자(Cadence)와 목표에 맞춰 솔루션을 설계, 구축, 통합, 배포**함.        |
| **2. PI ⏱️** *(Program Increment)*    | 애자일 팀의 작은 주기인 스프린트(2주)가 여러 번(보통 5번) 모인, **8\~12주(약 3개월) 길이의 거대한 '타임박스 주기'.**          | ART라는 거대 기차가 10주마다 멈춰 서서 **가치 있는 소프트웨어를 한꺼번에 묶어서 릴리즈(통합)하는 거대한 심장 박동** 역할.                    |
| **3. PI 플래닝** 🗺️ *(PI Planning)*     | PI(거대 주기)가 시작되기 전, **ART에 소속된 100여 명의 모든 인원이 이틀 동안 오프라인 한 공간에 모여 진행하는 초대형 대면 계획 회의.** | 각 팀이 알아서 계획을 짜면 팀 간에 의존성이 꼬이므로, \*\*전원이 모여 10주간의 비전과 아키텍처 제약 사항을 맞추고 종속성을 해결(Alignment)\*\*함. |

#### **IV. \[결론/제언] LeSS 등 다른 확장 모델과의 차이 및 엔터프라이즈 도입의 현실적 한계**

* **(키워드 위주 2줄 마무리)** "대규모 애자일 모델에는 스크럼을 단순히 확장한 \*\*LeSS(Large-Scale Scrum)\*\*나 **스포티파이(Spotify) 모델**도 존재하지만, **SAFe는 기존의 무거운 기업 경영 계층(포트폴리오)까지 완벽하게 애자일과 접목시킨 가장 포괄적이고 무거운 체계**입니다. 다만 그 구조가 매우 방대하여 학습 곡선이 가파르고, 기존 폭포수 관료주의 조직(Top-down)의 저항을 뚫어내는 것이 실제 현업 도입의 가장 큰 장벽으로 지적받고 있습니다."
