### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (상위개념vs하위개념관계) — 3~4줄
Ⅱ. 코드커버리지 - 코드기준측정 (본론①, 도식 1개 필수)
Ⅲ. 테스트커버리지 - 요구사항기준측정 (본론②, 핵심 배점)
Ⅳ. 함정 - 100%코드커버리지의착각
Ⅴ. 결론
```

포인트: 개요에서 \*\*"코드커버리지는 '코드의몇%가실행됐는가'를측정하는것이고, 테스트커버리지는더넓은개념으로 '요구사항,기능,리스크등이얼마나테스트로다뤄졌는가'를측정하는것 — 코드커버리지는테스트커버리지의한부분집합"\*\*이라는한줄로시작하면, 왜이름이비슷한데 자주혼동되는지 설명됩니다.

### Ⅱ. 코드커버리지 — 코드기준측정

| 유형                    | 측정기준                                     |
| :-------------------- | :--------------------------------------- |
| **구문커버리지(Statement)** | 전체 **코드줄**중실행된비율                         |
| **분기커버리지(Branch)**    | **if/else등분기**의True/False가모두실행된비율        |
| **조건커버리지(Condition)** | **개별조건식**(A&\&B의A,B각각)이True/False모두실행된비율 |

→ 암기: **"줄이실행됐나(구문),분기가다갔나(분기),조건이다따져졌나(조건)"** — 앞서다룬 \*\*"화이트박스테스트"\*\*의핵심측정지표가바로이코드커버리지입니다.

### 도식화 제안

```
[코드커버리지측정대상]
소스코드 ──→ [실행된부분/전체코드] = 코드커버리지%

if (a>0 && b>0) {      ← 조건커버리지:a>0,b>0 각각True/False확인필요
    처리1();           ← 구문커버리지:이줄이실행됐는가
} else {
    처리2();           ← 분기커버리지:else분기도실행됐는가
}
```

### Ⅲ. 테스트커버리지 — 요구사항기준측정, 핵심 배점

**함정 방지: "테스트커버리지=코드커버리지의다른이름"으로혼동하면절반. 코드가전혀아닌기준(요구사항,리스크)으로도측정된다는걸보여줘야완성됩니다.**

| 유형           | 측정기준                                            |
| :----------- | :---------------------------------------------- |
| **요구사항커버리지** | **요구사항중몇%가테스트케이스로다뤄졌는가 — 앞서다룬RTM**이바로이지표를추적하는도구 |
| **기능커버리지**   | \*\*기능목록중몇%\*\*가테스트됐는가                          |
| **리스크커버리지**  | \*\*식별된위험요소중몇%\*\*가테스트로검증됐는가                    |

→ 암기: **"요구사항몇%,기능몇%,위험요소몇%가다뤄졌나"** — 이지표들은 **코드를전혀보지않고도** 측정가능합니다: 요구사항명세서와 테스트케이스목록만비교하면됩니다.

### 도식화 제안

```
[테스트커버리지 - 더넓은개념]
   ┌──────────────────────────┐
   │      테스트커버리지            │
   │  ┌──────────┐             │
   │  │ 코드커버리지  │  ← 하위집합    │
   │  │(구문,분기,조건)│             │
   │  └──────────┘             │
   │  + 요구사항커버리지            │
   │  + 기능커버리지               │
   │  + 리스크커버리지              │
   └──────────────────────────┘
```

→ "코드커버리지는 테스트커버리지라는큰그림의 \*\*한조각(구현물이얼마나실행됐나)\*\*일뿐, 전체그림(요구사항이얼마나검증됐나)을보려면 다른지표도같이봐야한다"는게핵심입니다.

### Ⅳ. 함정 — 100%코드커버리지의착각

**함정 방지: "코드커버리지100%=완벽한테스트"라고생각하면 심각한오해입니다. 왜아닌지구체적으로보여줘야완성됩니다.**

| 함정상황                     | 문제                                                                |
| :----------------------- | :---------------------------------------------------------------- |
| **모든줄실행됐지만검증(assert)없음** | 코드는지나갔지만 **결과값이맞는지확인안함**(형식적통과)                                   |
| **코드는100%맞지만요구사항이틀림**    | 앞서다룬 **"오류-부재의궤변"**— 코드는완벽히실행됐지만 **애초에잘못된요구를구현**했을수있음             |
| **뮤테이션테스트로드러남**          | 앞서다룬 **뮤테이션테스트**를돌려보면, 100%코드커버리지에도 **뮤턴트가생존**(테스트가버그를못잡음)하는경우가흔함 |

→ 암기: **"코드를다지나갔다고, 제대로검증한건아니다"** — 이게바로앞서다룬 \*\*"살충제패러독스"\*\*와 \*\*"뮤테이션테스트"\*\*가 필요한 이유입니다: 코드커버리지숫자만보고 \*\*"테스트가충분하다"\*\*고안심하면 이패러독스에빠집니다.

### 도식화 제안

```
[코드커버리지100%인데버그있는코드]
function divide(a, b) {
    return a / b;    ← 이줄실행됨(커버리지100%)
}

테스트: divide(10, 2) → 5 확인       ← 통과,커버리지달성
누락: divide(10, 0) → ??? (0으로나누기) ← 커버리지는이미100%라 
                                        놓친게안보임!
```

### Ⅴ. 결론 포인트 (테스트 시리즈 대단원)

코드커버리지와테스트커버리지의관계는 \*\*"부분(코드가실행된비율)과전체(요구사항·리스크까지포함한검증정도)"\*\*이며, **"코드커버리지100%"라는숫자하나만믿는것자체가 살충제패러독스의한형태**입니다 — 이는앞서다룬 \*\*뮤테이션테스트(테스트품질의정량적검증)\*\*와 \*\*테스트7대원칙(완벽한테스팅은불가능)\*\*이경고했던것과 정확히같은함정이며, 오늘하루다룬테스트시리즈전체(7대원칙→살충제패러독스→화이트박스/블랙박스→TDD/BDD→정적/동적분석→회귀/뮤테이션→커버리지)가 \*\*"측정가능한숫자뒤에숨은진짜품질을놓치지말라"\*\*는하나의교훈으로완결됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "프로젝트 막바지, 개발팀장이 자랑스럽게 외친다. '자동화 테스트를 돌려보니, 우리가 짠 소스코드 1만 줄이 단 한 줄도 빠짐없이 모두 실행되었습니다! **코드 커버리지 100% 달성**입니다! 이 프로그램은 무결점이에요!' 그러자 QA 팀장이 서늘하게 대답한다. '네, 개발자님들이 짠 코드는 에러 없이 완벽하게 다 도네요. 그런데 고객이 요구한 핵심 기능인 장바구니 할인 로직은 아예 개발조차 안 되어 있어서, 테스트 명세서 항목이 텅 비어있습니다. 당신들의 코드 커버리지는 100%일지 몰라도, 우리의 \*\*테스트 커버리지는 80%\*\*입니다.' 이 끔찍한 일화가 두 용어의 본질적 차이를 극명하게 보여준다. \*\*'테스트 커버리지'\*\*는 철저하게 기획자와 요구사항 명세서 관점이다. 100개의 요구 기능 스펙이 있다면 이 100개의 기능(What)을 우리가 빼먹지 않고 모두 테스트했는가를 묻는 거시적이고 비즈니스적인 지표다. (블랙박스 영역). 반면 \*\*'코드 커버리지'\*\*는 철저하게 개발자와 작성된 소스코드 관점이다. 내 눈앞에 쓰여진 if문과 for문(How)의 복잡한 갈래길을 테스트 봇이 하나도 빠짐없이 밟아보며 실행했는가를 묻는 미시적이고 기술적인 지표다. (화이트박스 영역). 결국 '기능의 누락'을 막는 테스트 커버리지와 '로직의 폭탄'을 막는 코드 커버리지가 십자선처럼 교차 검증되어야만 진짜 무결점 소프트웨어가 탄생한다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 기능 누락을 막을 것인가, 코드 로직 결함을 막을 것인가? 개요**

* **테스트 커버리지 (Test Coverage):** 시스템의 전체 **'요구사항 명세서(Business Requirements)나 기능 명세'** 항목 중에서, 현재 우리의 테스트 케이스가 어느 정도의 기능 비율을 포괄하여 검증했는지를 나타내는 정량적 지표.
* **코드 커버리지 (Code Coverage):** 개발자가 작성한 전체 **'소스 코드(Source Code)의 구문, 분기, 제어 흐름'** 중에서, 테스트 케이스가 실제로 실행시키며(Run) 밟고 지나간 코드 라인 및 구조의 비율을 나타내는 정량적 지표.

#### **II. \[본론 1] 명세(QA) 타겟 vs 소스코드(개발자) 검증 타겟 (도식화)**

커버리지 대상의 범위와 지향점이 무엇인지 직관적으로 분리합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2ODQuMTIzNDk5OTk5OTk5OSA2MTcuMTU4IiB3aWR0aD0iNjg0LjEyMzQ5OTk5OTk5OTkiIGhlaWdodD0iNjE3LjE1OCIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX19UZXN0X0NvdmVyYWdlX19fIiBkYXRhLWxhYmVsPSLthYzsiqTtirgg7Luk67KE66as7KeAIChUZXN0IENvdmVyYWdlKSDinpQg7YOA6rKfOiDrqoXshLgv6riw64qlIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIzMzYuOTMwNSIgaGVpZ2h0PSI1MjEuNTk3IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMzM2LjkzMDUiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7thYzsiqTtirgg7Luk67KE66as7KeAIChUZXN0IENvdmVyYWdlKSDinpQg7YOA6rKfOiDrqoXshLgv6riw64qlPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX19Db2RlX0NvdmVyYWdlX19fIiBkYXRhLWxhYmVsPSLsvZTrk5wg7Luk67KE66as7KeAIChDb2RlIENvdmVyYWdlKSDinpQg7YOA6rKfOiDshozsiqTsvZTrk5wiPgogIDxyZWN0IHg9IjQwNC45MzA0OTk5OTk5OTk5NCIgeT0iNDAiIHdpZHRoPSIyMzkuMTkyOTk5OTk5OTk5OTgiIGhlaWdodD0iNTM3LjE1OCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwNC45MzA0OTk5OTk5OTk5NCIgeT0iNDAiIHdpZHRoPSIyMzkuMTkyOTk5OTk5OTk5OTgiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjQxNi45MzA0OTk5OTk5OTk5NCIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+7L2U65OcIOy7pOuyhOumrOyngCAoQ29kZSBDb3ZlcmFnZSkg4p6UIO2DgOqynzog7IaM7Iqk7L2U65OcPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJUMSIgZGF0YS10bz0iVDIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iuu4lOuemeuwleyKpCDthYzsiqTtirgiIHBvaW50cz0iMjQ0LjM2NjUsMTQyLjAyNSAyNDQuMzY2NSwyNTQuMTAwMDAwMDAwMDAwMDIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlQyIiBkYXRhLXRvPSJUMyIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjQ0LjM2NjUsNDQzLjc5NyAyNDQuMzY2NSw0OTkuNTc3NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDMSIgZGF0YS10bz0iQzIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iu2ZlOydtO2KuOuwleyKpC/ri6jsnIQg7YWM7Iqk7Yq4IiBwb2ludHM9IjUyNC41MjY5OTk5OTk5OTk5LDE0Mi4wMjUgNTI0LjUyNjk5OTk5OTk5OTksMjU0LjEwMDAwMDAwMDAwMDAyIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDMiIgZGF0YS10bz0iQzMiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjUyNC41MjY5OTk5OTk5OTk5LDQ1OS4zNTggNTI0LjUyNjk5OTk5OTk5OTksNDk5LjU3NzUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJUMSIgZGF0YS10bz0iVDIiIGRhdGEtbGFiZWw9Iuu4lOuemeuwleyKpCDthYzsiqTtirgiPgogIDxyZWN0IHg9IjE5Mi44NjY1MDAwMDAwMDAwMyIgeT0iMTgwLjgiIHdpZHRoPSIxMDIuNTkyMDAwMDAwMDAwMDEiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyNDQuMTYyNTAwMDAwMDAwMDIiIHk9IjE5NS45NTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+67iU656Z67CV7IqkIO2FjOyKpO2KuDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJDMSIgZGF0YS10bz0iQzIiIGRhdGEtbGFiZWw9Iu2ZlOydtO2KuOuwleyKpC/ri6jsnIQg7YWM7Iqk7Yq4Ij4KICA8cmVjdCB4PSI0NTMuNTI2OTk5OTk5OTk5OTMiIHk9IjE4MC44IiB3aWR0aD0iMTQxLjIwMjAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTI0LjEyNzk5OTk5OTk5OTkiIHk9IjE5NS45NTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7ZmU7J207Yq467CV7IqkL+uLqOychCDthYzsiqTtirg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlQxIiBkYXRhLWxhYmVsPSLsmpTqtazsgqztla0g66qF7IS47IScIPCfk5wKMS4g66Gc6re47J24IDIuIOqysOygnCAzLiDtlaDsnbgiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTUyLjYyNiIgeT0iODguMjI1IiB3aWR0aD0iMTgzLjQ4MSIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjQ0LjM2NjUiIHk9IjExNS4xMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjI0NC4zNjY1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7JqU6rWs7IKs7ZWtIOuqheyEuOyEnCDwn5OcPC90c3Bhbj48dHNwYW4geD0iMjQ0LjM2NjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPjEuIOuhnOq3uOyduCAyLiDqsrDsoJwgMy4g7ZWg7J24PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlQyIiBkYXRhLWxhYmVsPSLthYzsiqTtirgg7IiY7ZaJCjEsIDLrsojrp4wg7YWM7Iqk7Yq4IOyZhOujjCIgZGF0YS1zaGFwZT0iZGlhbW9uZCI+CiAgPHBvbHlnb24gcG9pbnRzPSIyNDQuMzY2NSwyNTQuMTAwMDAwMDAwMDAwMDIgMzM5LjIxNTAwMDAwMDAwMDAzLDM0OC45NDg1IDI0NC4zNjY1LDQ0My43OTcgMTQ5LjUxOCwzNDguOTQ4NSIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjQ0LjM2NjUiIHk9IjM0OC45NDg1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIyNDQuMzY2NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPu2FjOyKpO2KuCDsiJjtlok8L3RzcGFuPjx0c3BhbiB4PSIyNDQuMzY2NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+MSwgMuuyiOunjCDthYzsiqTtirgg7JmE66OMPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlQzIiBkYXRhLWxhYmVsPSLthYzsiqTtirgg7Luk67KE66as7KeAOiA2NiUg4pqg77iPCu2VoOyduCDquLDriqUg6rCc67CcL+2FjOyKpO2KuCDriITrnb3rkKghIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjEyNy44MDI1MDAwMDAwMDAwMSIgeT0iNDk5LjU3NzUiIHdpZHRoPSIyMzMuMTI4IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyNDQuMzY2NSIgeT0iNTI2LjQ3NzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjI0NC4zNjY1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7YWM7Iqk7Yq4IOy7pOuyhOumrOyngDogNjYlIOKaoO+4jzwvdHNwYW4+PHRzcGFuIHg9IjI0NC4zNjY1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7tlaDsnbgg6riw64qlIOqwnOuwnC/thYzsiqTtirgg64iE652965CoITwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJOb3RlIiBkYXRhLWxhYmVsPSJOb3RlIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI4OC4yMjUiIHdpZHRoPSI2OC42MjYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI5MC4zMTMiIHk9IjEwNi42NzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk5vdGU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkMxIiBkYXRhLWxhYmVsPSLsnpHshLHrkJwg7IaM7Iqk7L2U65OcIPCfkrsKaWYoQSkgeyAuLi4gfSBlbHNlIHsgLi4uIH0iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDQyLjA0ODk5OTk5OTk5OTkiIHk9Ijg4LjIyNSIgd2lkdGg9IjE2NC45NTYwMDAwMDAwMDAwMiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNTI0LjUyNjk5OTk5OTk5OTkiIHk9IjExNS4xMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjUyNC41MjY5OTk5OTk5OTk5IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7J6R7ISx65CcIOyGjOyKpOy9lOuTnCDwn5K7PC90c3Bhbj48dHNwYW4geD0iNTI0LjUyNjk5OTk5OTk5OTkiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPmlmKEEpIHsgLi4uIH0gZWxzZSB7IC4uLiB9PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkMyIiBkYXRhLWxhYmVsPSLroZzsp4Eg7Iuk7ZaJCkE9VHJ1ZSDro6jtirjrp4wg7Iuk7ZaJ65CoIiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjUyNC41MjY5OTk5OTk5OTk5LDI1NC4xMDAwMDAwMDAwMDAwNSA2MjcuMTU2LDM1Ni43MjkwMDAwMDAwMDAwNCA1MjQuNTI2OTk5OTk5OTk5OSw0NTkuMzU4MDAwMDAwMDAwMDYgNDIxLjg5Nzk5OTk5OTk5OTksMzU2LjcyOTAwMDAwMDAwMDA0IiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1MjQuNTI2OTk5OTk5OTk5OSIgeT0iMzU2LjcyOTAwMDAwMDAwMDA0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI1MjQuNTI2OTk5OTk5OTk5OSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuuhnOyngSDsi6Ttlok8L3RzcGFuPjx0c3BhbiB4PSI1MjQuNTI2OTk5OTk5OTk5OSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+QT1UcnVlIOujqO2KuOunjCDsi6TtlonrkKg8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQzMiIGRhdGEtbGFiZWw9Iuy9lOuTnCDsu6TrsoTrpqzsp4A6IDUwJSDimqDvuI8KZWxzZSDrtoTquLAoRmFsc2Up64qUIOyViCDtg4DrtIQhIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQyMC45MzA0OTk5OTk5OTk5NCIgeT0iNDk5LjU3NzUiIHdpZHRoPSIyMDcuMTkyOTk5OTk5OTk5OTgiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjUyNC41MjY5OTk5OTk5OTk5IiB5PSI1MjYuNDc3NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNTI0LjUyNjk5OTk5OTk5OTkiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7svZTrk5wg7Luk67KE66as7KeAOiA1MCUg4pqg77iPPC90c3Bhbj48dHNwYW4geD0iNTI0LjUyNjk5OTk5OTk5OTkiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPmVsc2Ug67aE6riwKEZhbHNlKeuKlCDslYgg7YOA67SEITwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 테스트 커버리지 vs 코드 커버리지 전격 비교 (3단 표 - 출제 1순위)**

실무에서 헷갈리지 않도록 테스트 기반(블랙 vs 화이트)과 세부 측정 지표를 명확히 대비시킵니다.

| **비교 척도 (잣대)**         | **📊 테스트 커버리지 (Test Coverage)**                                        | **💻 코드 커버리지 (Code Coverage)**                                                            |
| :--------------------- | :--------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| **핵심 타겟 (대상)**         | 고객과 약속한 **요구사항, 기능 명세서, 사용자 시나리오(유스케이스).**                             | 개발자가 작성한 **물리적 소스코드 라인, 제어 흐름, if/else 분기(Branch).**                                      |
| **기반 테스트 관점**          | **블랙박스(명세 기반) 테스팅 지향.** 코드를 몰라도 명세서의 기능(Input ➔ Output)이 똑바로 도는지에 집중함. | **화이트박스(구조 기반) 테스팅 지향.** 명세서는 몰라도 코드 안의 데드코드나 무한 루프가 없는지 치밀하게 해부함.                        |
| **주요 수행 주체**           | 비즈니스를 이해하는 **QA (품질보증) 엔지니어, 비즈니스 기획자, 고객.**                           | 로직을 직접 짠 **개발자**, 또는 CI/CD 파이프라인의 **자동화 테스트 봇(Bot).**                                     |
| **세부 측정 지표 예시**        | 1. 요구사항 커버리지 2. 기능 커버리지 3. 유스케이스(시나리오) 커버리지                            | 1. **구문(Statement) 커버리지** 2. **결정/분기(Decision/Branch) 커버리지** 3. 조건(Condition) 커버리지, MC/DC |
| **발생 가능한 맹점 (서로의 한계)** | 기능은 다 돌아가더라도, 그 기능 속에 숨겨진 코드의 메모리 누수나 데드코드(폭탄)를 찾아내지 못함.               | **코드 커버리지가 100%라고 해서 결함이 0개라는 착각.** (요구사항 스펙 자체가 아예 누락된 것은 알아채지 못함).                      |

#### **IV. \[결론/제언] '코드 커버리지 100%의 착각' 타파와 십자선 교차 검증의 필수성**

* **(키워드 위주 2줄 마무리)** "IT 업계의 흔한 함정은 JaCoCo나 SonarQube 같은 자동화 툴이 내뱉는 \*\*'코드 커버리지 100%'\*\*라는 숫자에 취해 완벽한 품질을 달성했다고 착각하는 것입니다. 진정한 의미의 무결점 소프트웨어는, 개발자가 화이트박스 기법으로 **코드 커버리지를 올려 내부의 로직 폭탄을 해체**함과 동시에, QA 팀이 블랙박스 기법으로 \*\*테스트 커버리지를 올려 비즈니스 가치(기능)의 누락을 완벽하게 틀어막는 '양방향 교차 검증'\*\*이 이루어질 때 비로소 달성됩니다."
