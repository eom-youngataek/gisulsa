### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (RTM 정의, 필요성) — 3~4줄
Ⅱ. RTM 구조 (본론①, 도식 1개 필수)
Ⅲ. 유형 - 전방향/후방향/양방향 (본론②, 핵심 배점)
Ⅳ. 작성절차 및 활용
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 V모델은 요구분석↔인수테스트가 대응된다고 했는데, 실제프로젝트에서는 요구사항이 수백개씩 있어서 그대응관계를 한눈에보여줄 표가필요하다 — 이 표가RTM(요구사항추적매트릭스)"\*\*이라는 한 줄로 시작하면, V모델 답안과 자연스럽게 이어집니다.

### Ⅱ. RTM 구조 — "요·설·구·시" (요구사항이 각단계로 연결됨)

| 열             | 내용                       |
| :------------ | :----------------------- |
| **요구사항ID/내용** | 각 요구사항의 **고유번호와 설명**(원본) |
| **설계연결**      | 그요구를 반영한 **설계문서/모듈**     |
| **구현연결**      | 그요구를 구현한 **코드/컴포넌트**     |
| **테스트연결**     | 그요구를 검증하는 **테스트케이스ID**   |

→ 암기: **"요구하나가 설계-구현-테스트까지 한줄로 쭉이어진다"** — 앞서 다룬 "V모델"의 왼쪽(요구→설계→구현)과 오른쪽(단위→통합→인수테스트)의 대응관계를, **표한줄에다펼쳐놓은 것**이 RTM입니다.

### 도식화 제안

```
요구사항ID | 요구내용        | 설계문서   | 구현모듈    | 테스트케이스ID
REQ-001   | 로그인기능      | DES-05    | LoginMod   | TC-101,TC-102
REQ-002   | 비밀번호재설정   | DES-08    | PwdMod     | TC-103
REQ-003   | (설계에서빠짐!)  | (공란)    | (공란)     | (공란)  ← 즉시발견가능한 Gap
```

→ "REQ-003처럼 연결이 끊긴 빈칸이 보이면, 그요구사항이 \*\*누락(Gap)\*\*됐다는걸 즉시알수있다"는 게 RTM의 핵심 실전가치입니다.

### Ⅲ. 유형 — 전방향/후방향/양방향, 핵심 배점

**함정 방지: RTM을 "그냥표하나"로 답하면절반. 추적방향에따라 발견하는문제가다르다는걸 구분해야완성됩니다.**

| 유형                       | 추적방향               | 발견하는문제                                        |
| :----------------------- | :----------------- | :-------------------------------------------- |
| **전방향추적**(Forward)       | **요구사항→설계→구현→테스트** | 요구사항이 **빠짐없이 구현·테스트됐는가**(요구가누락안됐는지)           |
| **후방향추적**(Backward)      | **테스트/구현→요구사항**    | 구현된기능이 **실제요구사항에근거하는가**(불필요한기능,Scope Creep방지) |
| **양방향추적**(Bidirectional) | **양쪽모두**           | **완전성**(요구빠짐없음) + **정당성**(구현물다필요한것) 동시확보      |

→ 암기: **"앞으로추적하면빠진게없는지,뒤로추적하면쓸데없는게없는지"** — 앞서다룬 "린SW개발의 8대낭비" 중 **"불필요한기능"** 낭비를 잡아내는게 바로 후방향추적의 역할이라는 연결이 심화포인트입니다.

### Ⅳ. 작성절차 및 활용

| 단계           | 내용                                           |
| :----------- | :------------------------------------------- |
| **작성시점**     | 요구사항확정후 **즉시작성시작**, 설계/구현/테스트단계마다 **지속갱신**   |
| **변경관리연계**   | 요구사항변경시 RTM으로 **영향받는설계·코드·테스트를즉시식별**(영향도분석)  |
| **감리·인수시활용** | 앞서다룬 "정보시스템감리"에서 **요구사항충족여부를객관적으로입증**하는핵심산출물 |

→ 앞서다룬 "V모델"의 조기테스트설계철학이, RTM에서는 \*\*"요구사항이확정되는순간 테스트케이스ID칸을비워두고, 나중에채워나간다"\*\*는 실무적구현방식으로 나타납니다.

### Ⅴ. 결론 포인트 (요구공학 시리즈 완결)

RTM의 본질은 \*\*"수백개의요구사항중 하나라도 빠짐없이 구현·검증됐는지를, 감이아니라표하나로 객관적으로증명하는것"\*\*입니다 — 이는 앞서 다룬 요구사항검증(Validation)의 실무도구이자, V모델의 대응관계를 실제프로젝트규모로 확장한 것이며, \*\*"추적가능성이없으면, 요구사항이누락됐는지 아무도확신할수없다"\*\*는 게 오늘 다룬 요구공학시리즈(도출-분석-명세-검증-RTM)의 최종결론입니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "프로젝트 막바지 테스트 단계에서 고객이 화를 낸다. '제가 결제 화면에 취소 버튼 꼭 넣어달라고 요구사항 분석 때 분명히 말했는데 왜 코딩이 안 되어 있죠?' 개발팀은 당황한다. 1,000페이지짜리 회의록 어디에 그 말이 있었는지, 대체 어떤 개발자가 그 부분을 잊어먹고 안 짰는지 도무지 추적할 길이 없다. 이 거대한 혼란을 막기 위해 엑셀이나 툴에 그려놓는 마법의 표가 바로 \*\*'RTM(요구사항 추적 매트릭스)'\*\*이다. RTM은 고객의 요구사항(REQ-01)이 시스템 도면(설계서 ID) 어디에 그려졌고, 실제로 어떤 소스코드(Payment.java) 파일로 코딩되었으며, 마지막에 어떤 테스트 케이스(TC-01)로 검사하여 OK를 받았는지를 1:1로 쫙 매핑(연결)해 놓은 거대한 표다. 방향은 두 가지다. 위(요구사항)에서 아래(코드)로 훑어 내려가며 '고객의 요구가 하나도 안 빠지고 다 만들어졌나?' 검사하는 \*\*'정방향 추적'\*\*과, 밑(코드)에서 위로 거슬러 올라가며 '대체 이 쓸데없는 코드는 왜 짠 거지?'를 잡아내는 \*\*'역방향 추적'\*\*이다. 이 양방향 RTM은, 나중에 요구사항이 급변했을 때 어떤 소스코드를 뜯어고쳐야 하는지(영향도 분석)를 1초 만에 알려주는 네비게이션이자, 프로젝트 종료 시 고객의 승인을 받아내는 완벽한 방패다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 고객의 요구사항이 미아가 되는 것을 막아라, RTM 개요**

* **정의:** 고객의 초기 요구사항이 소프트웨어 개발의 각 생명주기(설계 ➔ 구현 ➔ 테스트)를 거치면서 **어떻게 분배되어 반영되고, 최종적으로 정확히 테스트 및 검증되었는지를 1:1 매핑하여 추적할 수 있도록 도식화한 표(Matrix)**.
* **목적:** 고객 요구사항의 **누락 방지** 및 오버엔지니어링 차단, 요구사항 변경 시 수정해야 할 소스코드와 테스트 케이스를 즉각 찾아내는 **영향도 분석(Impact Analysis)**, 그리고 프로젝트 종료 시 인수 조건(Acceptance)을 증명하는 무결성 보장.

#### **II. \[본론 1] 양방향 추적성의 뼈대: 정방향 vs 역방향 메커니즘 (도식화)**

요구사항이 아래로 흘러가는지, 코드가 위를 가리키고 있는지를 보여주는 쌍방향 흐름입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3ODAuMDgyMDAwMDAwMDAwMSA0OTkuMjAwMDAwMDAwMDAwMDUiIHdpZHRoPSI3ODAuMDgyMDAwMDAwMDAwMSIgaGVpZ2h0PSI0OTkuMjAwMDAwMDAwMDAwMDUiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9fX0JpZGlyZWN0aW9uYWxfVHJhY2VhYmlsaXR5IiBkYXRhLWxhYmVsPSLsmpTqtazsgqztla0g7JaR67Cp7ZalIOy2lOyggeyEsSAoQmlkaXJlY3Rpb25hbCBUcmFjZWFiaWxpdHkpIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI3MDAuMDgyMDAwMDAwMDAwMSIgaGVpZ2h0PSI0MTkuMjAwMDAwMDAwMDAwMDUiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI3MDAuMDgyMDAwMDAwMDAwMSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPuyalOq1rOyCrO2VrSDslpHrsKntlqUg7LaU7KCB7ISxIChCaWRpcmVjdGlvbmFsIFRyYWNlYWJpbGl0eSk8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlIiIGRhdGEtdG89IkQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJ0cnVlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0OTguMDY3LDEzNy44IDQ5OC4wNjcsMTQ5LjggNjY0LjIwNDUsMTQ5LjggNjY0LjIwNDUsMTg1LjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgbWFya2VyLXN0YXJ0PSJ1cmwoI2Fycm93aGVhZC1zdGFydCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJEIiBkYXRhLXRvPSJDIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0idHJ1ZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNjY0LjIwNDUsMjM5LjYwMDAwMDAwMDAwMDAyIDY2NC4yMDQ1LDI4Ny42IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIG1hcmtlci1zdGFydD0idXJsKCNhcnJvd2hlYWQtc3RhcnQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQyIgZGF0YS10bz0iVCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9InRydWUiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjY2NC4yMDQ1LDM0MS40MDAwMDAwMDAwMDAwMyA2NjQuMjA0NSwzNTMuNDAwMDAwMDAwMDAwMDMgNDkyLjY5NDc1LDM1My40MDAwMDAwMDAwMDAwMyA0OTIuNjk0NzUsMzg5LjQwMDAwMDAwMDAwMDAzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIG1hcmtlci1zdGFydD0idXJsKCNhcnJvd2hlYWQtc3RhcnQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUiIgZGF0YS10bz0iVCIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iuygleuwqe2WpSDstpTsoIEgKEZvcndhcmQpIOKsh++4jwrsmpTqtazsgqztla3snbQg66qo65GQIOy9lOuUqeuQmOqzoCDthYzsiqTtirjrkJjsl4jripTqsIA/CuuIhOudvSDqsrDtlagg67Cp7KeAISIgcG9pbnRzPSI0NjcuMjAyLDEzNy44IDQ2Ny4yMDIsMzg5LjQwMDAwMDAwMDAwMDAzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlQiIGRhdGEtdG89IlIiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsl63rsKntlqUg7LaU7KCBIChCYWNrd2FyZCkg4qyG77iPCuydtCDsvZTrk5zqsIAg64yA7LK0IOyZnCjslrTripAg7JqU6rWs7IKs7ZWtIOuVjOusuOyXkCkg7Kec7Jes7KGM64qU6rCAPwrsk7jrjbDsl4bripQg7J6J7JesIOq4sOuKpSDrsKnsp4AhIiBwb2ludHM9IjQ0MS43MDkyNSwzODkuNDAwMDAwMDAwMDAwMDMgNDQxLjcwOTI1LDM1My40MDAwMDAwMDAwMDAwMyAxOTcsMzUzLjQwMDAwMDAwMDAwMDAzIDE5NywxNDkuOCA0MzYuMzM3LDE0OS44IDQzNi4zMzcsMTM3LjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJSIiBkYXRhLXRvPSJUIiBkYXRhLWxhYmVsPSLsoJXrsKntlqUg7LaU7KCBIChGb3J3YXJkKSDirIfvuI8K7JqU6rWs7IKs7ZWt7J20IOuqqOuRkCDsvZTrlKnrkJjqs6Ag7YWM7Iqk7Yq465CY7JeI64qU6rCAPwrriITrnb0g6rKw7ZWoIOuwqeyngCEiPgogIDxyZWN0IHg9IjM0NS43MDIiIHk9IjE4My4yNSIgd2lkdGg9IjI0Mi43NzYwMDAwMDAwMDAwNyIgaGVpZ2h0PSI1OC45MDAwMDAwMDAwMDAwMDYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNDY3LjA5MDAwMDAwMDAwMDAzIiB5PSIyMTIuNyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSI+PHRzcGFuIHg9IjQ2Ny4wOTAwMDAwMDAwMDAwMyIgZHk9Ii0xMC40NTAwMDAwMDAwMDAwMDEiPuygleuwqe2WpSDstpTsoIEgKEZvcndhcmQpIOKsh++4jzwvdHNwYW4+PHRzcGFuIHg9IjQ2Ny4wOTAwMDAwMDAwMDAwMyIgZHk9IjE0LjMiPuyalOq1rOyCrO2VreydtCDrqqjrkZAg7L2U65Sp65CY6rOgIO2FjOyKpO2KuOuQmOyXiOuKlOqwgD88L3RzcGFuPjx0c3BhbiB4PSI0NjcuMDkwMDAwMDAwMDAwMDMiIGR5PSIxNC4zIj7riITrnb0g6rKw7ZWoIOuwqeyngCE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJUIiBkYXRhLXRvPSJSIiBkYXRhLWxhYmVsPSLsl63rsKntlqUg7LaU7KCBIChCYWNrd2FyZCkg4qyG77iPCuydtCDsvZTrk5zqsIAg64yA7LK0IOyZnCjslrTripAg7JqU6rWs7IKs7ZWtIOuVjOusuOyXkCkg7Kec7Jes7KGM64qU6rCAPwrsk7jrjbDsl4bripQg7J6J7JesIOq4sOuKpSDrsKnsp4AhIj4KICA8cmVjdCB4PSI1MiIgeT0iMTgzLjI1IiB3aWR0aD0iMjg5LjcwMiIgaGVpZ2h0PSI1OC45MDAwMDAwMDAwMDAwMDYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTk2Ljg1MSIgeT0iMjEyLjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSIxOTYuODUxIiBkeT0iLTEwLjQ1MDAwMDAwMDAwMDAwMSI+7Jet67Cp7ZalIOy2lOyggSAoQmFja3dhcmQpIOKshu+4jzwvdHNwYW4+PHRzcGFuIHg9IjE5Ni44NTEiIGR5PSIxNC4zIj7snbQg7L2U65Oc6rCAIOuMgOyytCDsmZwo7Ja064qQIOyalOq1rOyCrO2VrSDrlYzrrLjsl5ApIOynnOyXrOyhjOuKlOqwgD88L3RzcGFuPjx0c3BhbiB4PSIxOTYuODUxIiBkeT0iMTQuMyI+7JO4642w7JeG64qUIOyeieyXrCDquLDriqUg67Cp7KeAITwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJSIiBkYXRhLWxhYmVsPSIxLiDsmpTqtazsgqztla0KUmVxdWlyZW1lbnRzIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwNS40NzIiIHk9Ijg0IiB3aWR0aD0iMTIzLjQ2MDAwMDAwMDAwMDAxIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0NjcuMjAyIiB5PSIxMTAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNDY3LjIwMiIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPjEuIOyalOq1rOyCrO2VrTwvdHNwYW4+PHRzcGFuIHg9IjQ2Ny4yMDIiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPlJlcXVpcmVtZW50czwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJEIiBkYXRhLWxhYmVsPSIyLiDshKTqs4QKRGVzaWduIC8gVUkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNjEyLjQ3ODAwMDAwMDAwMDEiIHk9IjE4NS44IiB3aWR0aD0iMTAzLjQ1MyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjY2NC4yMDQ1IiB5PSIyMTIuNzAwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjY2NC4yMDQ1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+Mi4g7ISk6rOEPC90c3Bhbj48dHNwYW4geD0iNjY0LjIwNDUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPkRlc2lnbiAvIFVJPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkMiIGRhdGEtbGFiZWw9IjMuIOq1rO2YhApTb3VyY2UgQ29kZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI2MDQuMzI3MDAwMDAwMDAwMSIgeT0iMjg3LjYiIHdpZHRoPSIxMTkuNzU1IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNjY0LjIwNDUiIHk9IjMxNC41IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI2NjQuMjA0NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPjMuIOq1rO2YhDwvdHNwYW4+PHRzcGFuIHg9IjY2NC4yMDQ1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5Tb3VyY2UgQ29kZTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJUIiBkYXRhLWxhYmVsPSI0LiDqsoDspp0KVGVzdCBDYXNlIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQxNi4yMTY1IiB5PSIzODkuNDAwMDAwMDAwMDAwMDMiIHdpZHRoPSIxMDEuOTcxIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjQ2Ny4yMDIiIHk9IjQxNi4zIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0NjcuMjAyIiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+NC4g6rKA7KadPC90c3Bhbj48dHNwYW4geD0iNDY3LjIwMiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+VGVzdCBDYXNlPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] RTM 매트릭스의 핵심 구성 요소 및 추적 방향별 상세 역할 (3단 표)**

이 표가 실제로 어떻게 구성되고, 왜 양방향이 필요한지에 대한 핵심 논리입니다.

| **추적 방향 구분**                             | **핵심 검증 목표 (Why)**                     | **RTM 상에서의 흐름 및 대응 전략**                                                                                          |
| :--------------------------------------- | :------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| **정방향 추적성 ⬇️** *(Forward Traceability)*  | **요구사항 누락(Omission) 완벽 방지**            | 요구사항 명세서(SRS)에서 출발하여 설계서 ➔ 소스코드 ➔ 테스트 케이스 방향으로 내려가며 **빈칸이 있는지 확인**함. 빈칸이 있다면 고객이 원한 기능을 개발자가 빼먹었다는 뜻.            |
| **역방향 추적성 ⬆️** *(Backward Traceability)* | **오버엔지니어링(Gold Plating) 차단**           | 완성된 소스코드나 테스트 케이스에서 위로 거슬러 올라가며 연결된 요구사항 ID가 있는지 확인함. 없다면 개발자가 **고객이 시키지도 않은 쓸데없는 기능(예산 낭비)을 멋대로 만들었다는 뜻.**      |
| **양방향 추적성 🔄** *(Bidirectional)*         | 요구사항 **변경 시 영향도 분석** (Impact Analysis) | 고객이 중간에 "REQ-01 기능을 바꿀게요"라고 하면, RTM을 통해 매핑된 Design-01 도면과 Code-01 파일, TC-01 문서만 딱 집어내어 **어디를 고쳐야 할지 1초 만에 식별**함. |

*(실제 RTM 엑셀/툴 구성 예시: \[요구사항 ID] - \[요구사항 내용] - \[설계서 ID] - \[소스코드 파일명] - \[테스트 케이스 ID] - \[테스트 성공 여부])*

#### **IV. \[결론/제언] 애자일 환경에서의 자동화된 RTM과 Jira 연동의 중요성**

* **(키워드 위주 2줄 마무리)** "과거 폭포수 환경에서는 엑셀(Excel)에 RTM을 수기로 작성하여 관리비용이 막대했습니다. 그러나 현대의 애자일/데브옵스 환경에서는 요구사항(User Story)부터 소스코드(Git Commit ID), 그리고 CI/CD 자동화 테스트 결과까지 **Jira(지라)와 같은 ALM(애플리케이션 수명주기 관리) 툴을 통해 체인처럼 자동으로 엮어 실시간 RTM 추적성을 확보**하는 것이 시스템 무결성의 글로벌 스탠다드로 자리매김하였습니다."
