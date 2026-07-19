### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (공통철학 - 테스트먼저) — 3~4줄
Ⅱ. TDD 사이클 (본론①, 도식 1개 필수)
Ⅲ. BDD - Given-When-Then (본론②, 핵심 배점)
Ⅳ. TDD vs BDD 비교
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬XP12대실천의TDD는'코드보다테스트를먼저쓴다'는원칙이었는데, 그테스트가개발자만이해하는코드언어로쓰이다보니, 고객/기획자는테스트내용을검토할수없었다 → BDD는 그테스트를 '사람이읽을수있는자연어(행위서술)'로바꿔서, 비개발자도참여할수있게한것"\*\*이라는 한줄로시작하면, 앞서다룬XP답안에서 BDD로 자연스럽게확장됩니다.

### Ⅱ. TDD 사이클 — "적·녹·청" (Red-Green-Refactor)

| 단계             | 색        | 내용                                |
| :------------- | :------- | :-------------------------------- |
| **①실패하는테스트작성** | Red      | 아직구현안된기능의 **테스트를먼저작성**(당연히실패)     |
| **②테스트통과최소코드** | Green    | 테스트를 **통과시키는가장단순한코드**작성(완벽하지않아도됨) |
| **③리팩토링**      | Refactor | 테스트가 **계속통과하는상태를유지**하며 코드품질개선     |

→ 암기: **"빨강(실패)→초록(통과)→다듬기(리팩토링)"** — 앞서다룬 \*\*"핑퐁프로그래밍"\*\*이 바로이TDD사이클을 두사람이 번갈아수행하는변형이었습니다.

### 도식화 제안

```
[Red] 실패하는테스트작성
    ↓
[Green] 테스트통과하는 최소코드작성
    ↓
[Refactor] 코드품질개선(테스트는계속통과유지)
    ↓
(다음기능으로반복)
```

### Ⅲ. BDD — Given-When-Then, 핵심 배점

**함정 방지: "TDD와같은것"으로혼동하면절반. "누구의언어로쓰는가"라는 근본적차이를보여줘야완성됩니다.**

| 구성            | 의미                  |
| :------------ | :------------------ |
| **Given(전제)** | 시나리오시작전 **초기상태/조건** |
| **When(행동)**  | 사용자가 **수행하는행동**     |
| **Then(결과)**  | 그행동으로 **기대되는결과**    |

→ 암기: **"\~인상황에서(Given), \~를하면(When), \~가된다(Then)"** — 이형식은 앞서다룬 **"사용자스토리"**(As a~I want~So that)와 마찬가지로 **비개발자도읽고쓸수있는자연어**입니다.

### 도식화 제안

```
Feature: 로그인기능

Scenario: 올바른비밀번호로로그인
  Given 사용자가 로그인페이지에있다
  When  올바른아이디와비밀번호를입력한다
  Then  메인화면으로이동한다

Scenario: 잘못된비밀번호로로그인
  Given 사용자가 로그인페이지에있다
  When  잘못된비밀번호를입력한다
  Then  "비밀번호가틀렸습니다" 오류가표시된다
```

→ "이Given-When-Then 문서는, 개발도구(Cucumber등)를통해 **그대로실행가능한자동테스트코드로변환**됩니다" — 즉 \*\*"문서=테스트"\*\*라는게BDD의핵심강점입니다.

### Ⅳ. TDD vs BDD 비교

| 구분       | **TDD**                 | **BDD**                         |
| :------- | :---------------------- | :------------------------------ |
| **작성언어** | **개발자코드**(단위테스트프레임워크)   | **자연어**(Given-When-Then)        |
| **관점**   | **기술적**(이함수가올바른값을반환하는가) | **행위적**(사용자입장에서이렇게동작하는가)        |
| **참여주체** | **개발자중심**               | **개발자+기획자+QA(협업)**              |
| **관계**   | -                       | **TDD의확장/변형**(BDD도결국내부는TDD로구현됨) |

→ 암기: **"TDD는함수단위로개발자가검증하고,BDD는시나리오단위로모두가함께검증한다"** — 앞서다룬"요구사항명세"에서 SRS문서가 **딱딱한명세**였다면, BDD는 \*\*"실행가능한명세(Executable Specification)"\*\*로,명세와테스트의경계를허뭅니다.

### Ⅴ. 결론 포인트 (테스트 시리즈 연결)

TDD와BDD는 \*\*"테스트를코드작성후가아니라 먼저쓴다"\*\*는 공통철학위에서, TDD는 **개발자의기술적정확성**을,BDD는 **비개발자까지포함한요구사항의공통이해**를추가로확보합니다 — 이는앞서다룬 \*\*"요구사항검증(Validation)"\*\*의문제(고객이진짜원하는게맞는지)를,BDD가 **테스트문서자체를 고객과의공통언어로만들어** 근본적으로해결하려는시도이며, 오늘다룬화이트박스/블랙박스(무엇을보고테스트할지)에 이어 TDD/BDD는 \*\*"언제,누구의언어로"\*\*테스트를설계할지답하는 시리즈의다음장이됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "일반적인 개발자들은 코드를 다 짜고 나서야 프로그램이 잘 돌아가는지 확인하려고 맨 마지막에 '테스트'를 돌린다. 하지만 이 당연한 순서를 완전히 거꾸로 뒤집어버린 파격적인 철학이 등장했다. 애자일 XP(익스트림 프로그래밍)의 꽃인 \*\*'TDD(테스트 주도 개발)'\*\*다. TDD는 실제 비즈니스 로직을 단 한 줄도 짜기 전에, 무조건 에러(실패)를 뿜어내는 \*\*'테스트 코드(Red)'\*\*부터 억지로 먼저 만든다. 그리고 이 에러를 잠재우기 위해 진짜 코드를 어떻게든 짜서 테스트를 **'통과(Green)'시키고, 지저분해진 코드를 예쁘게 다듬는다('Refactor'**). 코딩 전 테스트부터 짠다는 이 강박증은 개발자에게 완벽한 객체지향 설계와 결함 제로(Bug-Zero)라는 엄청난 선물을 안겨주었다. 하지만 TDD는 치명적 단점이 있었다. 철저히 '개발자 중심의 기술적 언어'라 기획자나 사장님은 그 테스트 코드를 전혀 읽을 수 없었다. 이 의사소통의 벽을 허물기 위해 TDD를 진화시킨 것이 바로 \*\*'BDD(행위 주도 개발)'\*\*다. BDD는 복잡한 코드 대신 누구나 읽을 수 있는 일상 언어(영어/한국어)로 시스템의 '행위'를 묘사한다. **'어떤 상황에서(Given), 고객이 무슨 행동을 하면(When), 어떤 결과가 튀어나와야 한다(Then).'** 이 마법의 3단계 시나리오 문법 덕분에, 기획자가 쓴 요구사항 스토리가 곧바로 젠킨스의 자동화 테스트 코드로 변신하게 되었고, 개발자와 비개발자 간의 거대한 장벽이 완벽히 박살 나게 되었다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 코딩의 상식을 거꾸로 뒤집다, TDD와 BDD 개요**

* **TDD (Test-Driven Development):** 실제 프로덕션 코드(비즈니스 로직)를 작성하기 전에, 그 코드가 통과해야 할 **'단위 테스트 코드'를 먼저 작성하여 설계와 구현을 주도해 나가는 애자일 개발 방법론**. (켄트 벡 창시).
* **BDD (Behavior-Driven Development):** TDD에서 파생되어, 개발자뿐만 아니라 기획자/고객 등 비기술자(Non-tech)도 이해할 수 있도록 **'사용자의 행위(시나리오)'를 자연어 문법으로 명세하고 이를 기반으로 테스트를 구동하는 방법론**. (댄 노스 창시).

#### **II. \[본론 1] 끝없는 톱니바퀴: TDD의 핵심 3단계 사이클 (도식화)**

코드의 설계와 품질을 끌어올리는 TDD의 무한 반복 메커니즘입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MzYuMzk0IDgyOC42IiB3aWR0aD0iNDM2LjM5NCIgaGVpZ2h0PSI4MjguNiIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iVEREX19fM19fUmVkX19HcmVlbl9fUmVmYWN0b3IiIGRhdGEtbGFiZWw9IlREROydmCDrrLTtlZwg67CY67O1IDPri6jqs4Qg7IKs7J207YG0IChSZWQgLSBHcmVlbiAtIFJlZmFjdG9yKSI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMzU2LjM5NCIgaGVpZ2h0PSI3NDguNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjM1Ni4zOTQiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5URETsnZgg66y07ZWcIOuwmOuztSAz64uo6rOEIOyCrOydtO2BtCAoUmVkIC0gR3JlZW4gLSBSZWZhY3Rvcik8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlIiIGRhdGEtdG89IkciIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyXkOufrCDrsJzsg50g7Iuc7YK0IiBwb2ludHM9IjI2My4yOTI2NjY2NjY2NjY2NiwyNTAgMjYzLjI5MjY2NjY2NjY2NjY2LDI2MiAzMTEuMzk0LDI2MiAzMTEuMzk0LDM2Ni4zIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJHIiBkYXRhLXRvPSJGIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLquLDriqUg7Lap7KGxIOyZhOujjCIgcG9pbnRzPSIzMTEuMzk0LDUwNC4zIDMxMS4zOTQsNTg0LjYgMjYwLjk1OTMzMzMzMzMzMzM1LDU4NC42IDI2MC45NTkzMzMzMzMzMzMzNSw2MjAuNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRiIgZGF0YS10bz0iUiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7IOI66Gc7Jq0IOq4sOuKpSDstpTqsIAg7IucIiBwb2ludHM9IjIxMC4yOTI2NjY2NjY2NjY3LDYyMC42IDIxMC4yOTI2NjY2NjY2NjY3LDU4NC42IDE1OS44NTgsNTg0LjYgMTU5Ljg1OCwyNjIgMjA3Ljk1OTMzMzMzMzMzMzM1LDI2MiAyMDcuOTU5MzMzMzMzMzMzMzUsMjUwIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlIiIGRhdGEtdG89IkciIGRhdGEtbGFiZWw9IuyXkOufrCDrsJzsg50g7Iuc7YK0Ij4KICA8cmVjdCB4PSIyNjQuODk0MDAwMDAwMDAwMDYiIHk9IjI5MyIgd2lkdGg9IjkyLjQ5NDAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzExLjE0MTAwMDAwMDAwMDEiIHk9IjMwOC4xNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7JeQ65+sIOuwnOyDnSDsi5ztgrQ8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iRyIgZGF0YS10bz0iRiIgZGF0YS1sYWJlbD0i6riw64qlIOy2qeyhsSDsmYTro4wiPgogIDxyZWN0IHg9IjI2NC44OTQwMDAwMDAwMDAwNiIgeT0iNTQ3LjMiIHdpZHRoPSI5Mi40OTQwMDAwMDAwMDAwMyIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjMxMS4xNDEwMDAwMDAwMDAxIiB5PSI1NjIuNDQ5OTk5OTk5OTk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+6riw64qlIOy2qeyhsSDsmYTro4w8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iRiIgZGF0YS10bz0iUiIgZGF0YS1sYWJlbD0i7IOI66Gc7Jq0IOq4sOuKpSDstpTqsIAg7IucIj4KICA8cmVjdCB4PSIxMDAuMzU4MDAwMDAwMDAwMDIiIHk9IjQyMC4xNTAwMDAwMDAwMDAwMyIgd2lkdGg9IjExOC4wMzYwMDAwMDAwMDAwMyIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjE1OS4zNzYwMDAwMDAwMDAwMyIgeT0iNDM1LjMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuyDiOuhnOyatCDquLDriqUg7LaU6rCAIOyLnDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUiIgZGF0YS1sYWJlbD0iMS4gUmVkIPCfmqgK7Iuk7Yyo7ZWY64qUIO2FjOyKpO2KuCIgZGF0YS1zaGFwZT0iY2lyY2xlIj4KICA8Y2lyY2xlIGN4PSIyMzUuNjI2IiBjeT0iMTY3IiByPSI4MyIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIyMzUuNjI2IiB5PSIxNjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjIzNS42MjYiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj4xLiBSZWQg8J+aqDwvdHNwYW4+PHRzcGFuIHg9IjIzNS42MjYiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyLpO2MqO2VmOuKlCDthYzsiqTtirg8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRyIgZGF0YS1sYWJlbD0iMi4gR3JlZW4g8J+fogrthYzsiqTtirgg7Ya16rO8IiBkYXRhLXNoYXBlPSJjaXJjbGUiPgogIDxjaXJjbGUgY3g9IjMxMS4zOTQiIGN5PSI0MzUuMyIgcj0iNjkiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMzExLjM5NCIgeT0iNDM1LjMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjMxMS4zOTQiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj4yLiBHcmVlbiDwn5+iPC90c3Bhbj48dHNwYW4geD0iMzExLjM5NCIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7YWM7Iqk7Yq4IO2GteqzvDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJGIiBkYXRhLWxhYmVsPSIzLiBSZWZhY3RvciDwn6e5Cuq1rOyhsCDrpqztjKnthqDrp4EiIGRhdGEtc2hhcGU9ImNpcmNsZSI+CiAgPGNpcmNsZSBjeD0iMjM1LjYyNjAwMDAwMDAwMDAzIiBjeT0iNjk2LjYiIHI9Ijc2IiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjIzNS42MjYwMDAwMDAwMDAwMyIgeT0iNjk2LjYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjIzNS42MjYwMDAwMDAwMDAwMyIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPjMuIFJlZmFjdG9yIPCfp7k8L3RzcGFuPjx0c3BhbiB4PSIyMzUuNjI2MDAwMDAwMDAwMDMiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuq1rOyhsCDrpqztjKnthqDrp4E8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iMTQ4LjU1IiB3aWR0aD0iNjguNjI2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iOTAuMzEzIiB5PSIxNjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk5vdGU8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 개발자 중심(TDD) vs 비즈니스 중심(BDD) 전격 비교 (3단 표 - 출제 1순위)**

면접과 지필에서 가장 핵심으로 보는, 두 방식의 '테스트 작성 문법과 관점의 차이'입니다.

| **비교 척도 (잣대)**                   | **💻 TDD (테스트 주도 개발)**                                                                        | **🤝 BDD (행위 주도 개발)**                                                                                                   |
| :------------------------------- | :-------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| **핵심 목적 및 관점**                   | **'개발자 중심' (How).** 이 클래스나 메서드가 '어떻게' 구현되었는지 기능적 정확성을 검증하고, 결함 제로의 단단한 객체지향 아키텍처 설계를 유도함.     | **'비즈니스 중심' (What).** 사용자가 이 시스템을 통해 '무엇을' 할 수 있는지(행위)를 명세하여, 이해관계자 전원의 공감대(의사소통)를 형성함.                                 |
| **작동 메커니즘 및 핵심 문법 3단계 (매우 중요!)** | **1. Red 🚨:** 실패하는 테스트 작성. **2. Green 🟢:** 통과하는 실제 코드 작성. **3. Refactor 🧹:** 중복 제거 및 리팩토링. | **1. Given (주어진 환경):** 초기 상태 설정. **2. When (이벤트/행위):** 사용자의 액션. **3. Then (기대 결과):** 행위 후의 상태 검증. *(자연어 Gherkin 문법 사용)* |
| **실제 작성 예시**                     | `assertEquals(2, cart.getTotal());`                                                           | **Given** 장바구니에 사과가 1개 있다. **When** 사과 1개를 추가로 담는다. **Then** 총개수는 2개가 되어야 한다.                                           |
| **대표적인 프레임워크 (자동화 도구)**          | JUnit (Java), PyTest (Python)                                                                 | **Cucumber (쿠컴버)**, JBehave                                                                                             |
| **도입 시 장단점**                     | 개발 후반부 버그 수정 비용을 극단적으로 낮추지만, 초기에 테스트 코드를 짜는 허들이 매우 높아 **단기 개발 속도가 2\~3배 느려짐.**                | 기획서(요구사항)가 곧바로 실행 가능한 테스트 코드가 되는 기적을 보여주지만, 자연어와 코드 간의 매핑 관리가 까다로움.                                                     |

#### **IV. \[결론/제언] 애자일 '사용자 스토리'에서 BDD 시나리오로 이어지는 CI/CD 파이프라인 완성**

* **(키워드 위주 2줄 마무리)** "TDD와 BDD는 경쟁 관계가 아니라 완벽하게 상호보완적인 개념입니다. 기획자가 작성한 애자일의 \*\*'사용자 스토리'\*\*는 그대로 BDD의 **'Given-When-Then' 시나리오**로 변환되어 큰 비즈니스 뼈대를 구축하고, 개발자는 그 뼈대 안에서 세부 모듈을 **'TDD(Red-Green-Refactor)' 사이클**로 구현함으로써, 명세서부터 CI/CD 자동화 배포까지 인간의 오류가 개입할 틈이 없는 궁극의 애자일/데브옵스 파이프라인을 완성하게 됩니다."
