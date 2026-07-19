### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (AOP 등장배경 - 횡단관심사문제) — 3~4줄
Ⅱ. 핵심개념 (본론①, 도식 1개 필수)
Ⅲ. 적용시점 - Join Point/Pointcut/Advice (본론②, 핵심 배점)
Ⅳ. 대표활용사례 및 결합도관점의의의
Ⅴ. 결론
```

포인트: 개요에서 \*\*"로깅,트랜잭션,보안검사같은기능은 '핵심비즈니스로직'이아니지만, 거의모든메서드에반복해서끼어들어야한다 → 앞서다룬헥사고날아키텍처가지키려던'핵심로직의순수성'이,이런반복코드때문에더러워지는문제 → 이횡단관심사를코드에서분리해별도로모듈화하는기법이AOP"\*\*라는한줄로시작하면, 앞서다룬헥사고날/클린아키텍처답안과바로이어집니다.

### Ⅱ. 핵심개념 — "핵심관심사 vs 횡단관심사"

| 구분                               | 내용                                   |
| :------------------------------- | :----------------------------------- |
| **핵심관심사(Core Concern)**          | 비즈니스로직 **본연의목적**(예:주문처리)             |
| **횡단관심사(Cross-cutting Concern)** | **여러모듈에걸쳐반복**되는부가기능(로깅,트랜잭션,보안,성능측정) |
| **Aspect(관점)**                   | 횡단관심사를 **모듈화한단위**(하나의독립된모듈로분리)       |

→ 암기: **"핵심은한곳,횡단은여러곳에흩어짐,Aspect는그흩어진걸모아놓은것"** — 앞서다룬"린SW개발의8대낭비" 중 \*\*"관리오버헤드"\*\*가바로이 반복되는횡단관심사코드때문에생기는낭비이며,AOP는이를제거하는도구입니다.

### 도식화 제안

```
[AOP 적용전]                        [AOP 적용후]
주문서비스(){                        주문서비스(){
  로깅();      ← 반복             주문로직만();
  트랜잭션시작();  ← 반복          }
  주문로직();
  트랜잭션종료();  ← 반복          [Aspect: 로깅+트랜잭션]
  로깅();      ← 반복              (별도모듈,여러곳에자동적용)
}
결제서비스(){
  로깅();      ← 또반복
  트랜잭션시작(); ← 또반복
  ...
}
```

→ "같은코드(로깅,트랜잭션)가 여러서비스에 복사-붙여넣기되어있던것을, 하나의Aspect로빼내고 자동으로끼워넣는다"는게핵심트릭입니다.

### Ⅲ. 적용시점 — Join Point/Pointcut/Advice, 핵심 배점

**함정 방지: "부가기능을분리한다"고만답하면절반. 정확히"언제,어디에" 끼워넣을지지정하는3요소를알아야완성됩니다.**

| 요소             | 의미                                               |
| :------------- | :----------------------------------------------- |
| **Join Point** | Aspect가 **끼어들수있는모든지점**(메서드호출,예외발생등)              |
| **Pointcut**   | Join Point중 **실제로적용할지점을선택**하는조건(예:"OO패키지의모든메서드") |
| **Advice**     | Pointcut에서 **실제로실행할부가기능코드**(로깅,트랜잭션처리등)          |

**Advice의 실행시점 4종**

| 시점                 | 의미                         |
| :----------------- | :------------------------- |
| **Before**         | 메서드 **실행전**에실행             |
| **After**          | 메서드 **실행후**(성공/실패무관)실행     |
| **AfterReturning** | 메서드가 **정상반환된후**실행          |
| **Around**         | 메서드 **실행전후를모두감싸서**제어(가장강력) |

→ 암기: **"Join Point는가능한모든자리,Pointcut은그중고른자리,Advice는거기서할일"** — 앞서다룬 **"GoF의데코레이터패턴"**(기존객체를감싸서기능을추가)이 바로AOP의 **Around Advice**와 원리가같습니다: 메서드실행을 앞뒤로 감싸서부가기능을입힙니다.

### 도식화 제안

```
[Pointcut] "OrderService의모든메서드"
     ↓
[Join Point] 실제orderService.save() 호출시점
     ↓
[Advice: Around]
  ┌────────────────┐
  │ 트랜잭션시작(Before)  │
  │  ↓                │
  │ [실제메서드실행]      │  ← 핵심로직은순수하게보존됨
  │  ↓                │
  │ 트랜잭션종료(After)  │
  └────────────────┘
```

### Ⅳ. 대표활용사례 및 결합도관점의의의

| 활용사례        | 내용                                           |
| :---------- | :------------------------------------------- |
| **로깅**      | 모든메서드호출을 **자동기록**                            |
| **트랜잭션관리**  | `@Transactional`처럼 **선언만하면** AOP가트랜잭션경계를자동처리 |
| **보안/인증검사** | 메서드실행전 **권한확인**자동삽입                          |
| **성능측정**    | 메서드실행시간을 **자동측정·로깅**                         |

→ 앞서다룬 "결합도"관점에서: AOP는 핵심로직과횡단관심사사이의 **결합도를거의0으로만듭니다** — 핵심로직코드어디에도 "로깅해라","트랜잭션시작해라"는 코드가없고,Aspect가 **외부에서주입**되기때문입니다.

### Ⅴ. 결론 포인트 (아키텍처 시리즈 대단원)

AOP의본질은 \*\*"모든모듈에공통으로필요하지만, 그모듈의핵심목적과는무관한코드(횡단관심사)를,핵심로직바깥으로완전히분리해내는것"\*\*입니다 — 이는앞서다룬헥사고날아키텍처(핵심을외부기술로부터격리),결합도/응집도(핵심의응집도를높이려는노력)의연장선이며, GoF의데코레이터패턴이 개별객체단위에서했던일을, AOP는 **프레임워크차원에서선언적으로,수많은객체에자동으로**적용한것입니다 — 이로써오늘다룬CBD→MSA→헥사고날→GoF패턴→결합도/응집도→MVC/MVVM→AOP 시리즈전체가, \*\*"관심사를분리하고,그분리를최소결합으로유지하는"\*\*소프트웨어설계의근본원리를,코드의가장미세한단위(메서드하나하나)까지관철시키는것으로완결됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "객체지향(OOP)으로 코드를 완벽하게 분리했다고 생각했는데, 막상 소스를 뜯어보면 지저분하기 짝이 없다. '계좌 이체'라는 순수한 핵심 비즈니스 로직 앞뒤로, 시간을 재는 로깅(Logging) 코드, DB 트랜잭션 코드, 사용자 권한을 체크하는 보안 코드들이 껍질처럼 덕지덕지 붙어있기 때문이다. 이런 부가 기능들은 계좌이체뿐만 아니라 회원가입, 결제 등 모든 클래스를 가로지르며(횡단하며) 흩뿌려져 코드 중복을 낳는다. 이 지저분한 공통 기능들을 마치 수술용 메스로 싹둑 잘라내어 한 곳으로 모아버리는 마법이 바로 \*\*'AOP(관점 지향 프로그래밍)'\*\*이다. AOP는 로깅, 보안 같은 흩어진 공통 기능들을 \*\*'Aspect(애스펙트/관점)'\*\*라는 별도의 모듈로 완전히 떼어낸다. 그리고 비즈니스 클래스에는 순수하게 '계좌 이체' 코드 딱 한 줄만 남겨둔다. 그렇다면 떼어낸 기능을 다시 어떻게 붙일까? '언제(Before/After) 어떤 부가 기능을' 실행할지 정하는 것을 \*\*'Advice'\*\*라 하고, 수많은 클래스의 메서드들 중 '정확히 어느 지점에' 꽂아 넣을지 타겟을 필터링하는 것을 \*\*'Pointcut'\*\*이라 부른다. 이렇게 따로 분리된 부가 기능을 프로그램 실행 중에 원래 코드 사이사이에 실처럼 엮어넣어 작동시키는 기술을 \*\*'위빙(Weaving)'\*\*이라고 한다. 자바 스프링의 `@Transactional` 어노테이션이 바로 이 AOP 철학의 가장 위대한 산물이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 핵심 코드에 엉겨 붙은 잡초(중복 코드)를 뽑아내다, AOP 개요**

* **정의:** 객체지향 프로그래밍(OOP)을 보완하는 패러다임으로, 애플리케이션 전체에 걸쳐 산발적으로 흩어져 있는 **'공통 부가 기능(횡단 관심사)'을 핵심 비즈니스 로직(핵심 관심사)으로부터 완벽하게 분리하여 모듈화하는 프로그래밍 기법**.
* **목적:** 핵심 비즈니스 로직은 오직 본연의 목적에만 집중하게 하여 \*\*'단일 책임 원칙(SRP)'\*\*을 극대화하고, 로깅/보안/트랜잭션과 같은 부가 기능의 코드 중복을 제거하여 유지보수성을 끌어올리기 위함.

#### **II. \[본론 1] 핵심 관심사와 횡단 관심사의 완벽한 십자가 분리 (도식화)**

OOP만으로는 해결할 수 없는 코드 흩뿌려짐(Scattering) 현상을 AOP가 어떻게 분리하는지 묘사합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1ODguNzY4IDYyOC40MDAwMDAwMDAwMDAxIiB3aWR0aD0iNTg4Ljc2OCIgaGVpZ2h0PSI2MjguNDAwMDAwMDAwMDAwMSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX09PUF9fX19fU2NhdHRlcmluZyIgZGF0YS1sYWJlbD0i6riw7KG0IE9PUOydmCDtlZzqs4Q6IOy9lOuTnOqwgCDslr3tnojqs6Ag7Z2p7Ja07KeQIChTY2F0dGVyaW5nKSI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMzMzLjAwNiIgaGVpZ2h0PSIyNjEuNDAwMDAwMDAwMDAwMDMiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIzMzMuMDA2IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+6riw7KG0IE9PUOydmCDtlZzqs4Q6IOy9lOuTnOqwgCDslr3tnojqs6Ag7Z2p7Ja07KeQIChTY2F0dGVyaW5nKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IkFPUF9fX19fU2VwYXJhdGlvbl9vZl9Db25jZXJucyIgZGF0YS1sYWJlbD0iQU9Q7J2YIO2VtOqysOyxhTog6rSA7Ius7IKs7J2YIOyZhOuyve2VnCDrtoTrpqwgKFNlcGFyYXRpb24gb2YgQ29uY2VybnMpIj4KICA8cmVjdCB4PSI0MCIgeT0iMzIxLjQwMDAwMDAwMDAwMDAzIiB3aWR0aD0iNTA4Ljc2ODAwMDAwMDAwMDAzIiBoZWlnaHQ9IjI2NyIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSIzMjEuNDAwMDAwMDAwMDAwMDMiIHdpZHRoPSI1MDguNzY4MDAwMDAwMDAwMDMiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSIzMzUuNDAwMDAwMDAwMDAwMDMiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+QU9Q7J2YIO2VtOqysOyxhTog6rSA7Ius7IKs7J2YIOyZhOuyve2VnCDrtoTrpqwgKFNlcGFyYXRpb24gb2YgQ29uY2VybnMpPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBMSIgZGF0YS10bz0iQzEiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsnITruZkgV2VhdmluZyIgcG9pbnRzPSI0MjguNDQzMzMzMzMzMzMzNCw1MzUuNSA0MjguNDQzMzMzMzMzMzMzNCw1MjMuNSA0NTcuNzAwMDAwMDAwMDAwMDUsNTIzLjUgNDU3LjcwMDAwMDAwMDAwMDA1LDQxOS4yMDAwMDAwMDAwMDAwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBMSIgZGF0YS10bz0iQzIiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsnITruZkgV2VhdmluZyIgcG9pbnRzPSIzODEuODU2MDAwMDAwMDAwMDUsNTM1LjUgMzgxLjg1NjAwMDAwMDAwMDA1LDUyMy41IDMzMS4wNjMsNTIzLjUgMzMxLjA2Myw0NTUuMjAwMDAwMDAwMDAwMDUgMzA5LjUyNjY2NjY2NjY2NjcsNDU1LjIwMDAwMDAwMDAwMDA1IDMwOS41MjY2NjY2NjY2NjY3LDQxOS4yMDAwMDAwMDAwMDAwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBMiIgZGF0YS10bz0iQzIiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsnITruZkgV2VhdmluZyIgcG9pbnRzPSIxOTQuNTYyLDUzNS41IDE5NC41NjIsNTIzLjUgMjQyLjg4NSw1MjMuNSAyNDIuODg1LDQ1NS4yMDAwMDAwMDAwMDAwNSAyNjQuNDIxMzMzMzMzMzMzMzQsNDU1LjIwMDAwMDAwMDAwMDA1IDI2NC40MjEzMzMzMzMzMzMzNCw0MTkuMjAwMDAwMDAwMDAwMDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQTIiIGRhdGEtdG89IkMzIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7JyE67mZIFdlYXZpbmciIHBvaW50cz0iMTUwLjQ0NDY2NjY2NjY2NjY4LDUzNS41IDE1MC40NDQ2NjY2NjY2NjY2OCw1MjMuNSAxMjMuNjU4MDAwMDAwMDAwMDIsNTIzLjUgMTIzLjY1OCw0MTkuMjAwMDAwMDAwMDAwMDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJBMSIgZGF0YS10bz0iQzEiIGRhdGEtbGFiZWw9IuychOu5mSBXZWF2aW5nIj4KICA8cmVjdCB4PSI0MTUuMjAwMDAwMDAwMDAwMDUiIHk9IjQ2Mi4yMDAwMDAwMDAwMDAwNSIgd2lkdGg9Ijg0LjE3ODAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNDU3LjI4OTAwMDAwMDAwMDA0IiB5PSI0NzcuMzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuychOu5mSBXZWF2aW5nPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkExIiBkYXRhLXRvPSJDMiIgZGF0YS1sYWJlbD0i7JyE67mZIFdlYXZpbmciPgogIDxyZWN0IHg9IjI4OC41NjMwMDAwMDAwMDAwNSIgeT0iNDYyLjIwMDAwMDAwMDAwMDA1IiB3aWR0aD0iODQuMTc4MDAwMDAwMDAwMDMiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzMzAuNjUyMDAwMDAwMDAwMDQiIHk9IjQ3Ny4zNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7JyE67mZIFdlYXZpbmc8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQTIiIGRhdGEtdG89IkMyIiBkYXRhLWxhYmVsPSLsnITruZkgV2VhdmluZyI+CiAgPHJlY3QgeD0iMjAwLjM4NSIgeT0iNDYyLjIwMDAwMDAwMDAwMDA1IiB3aWR0aD0iODQuMTc4MDAwMDAwMDAwMDMiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyNDIuNDc0IiB5PSI0NzcuMzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuychOu5mSBXZWF2aW5nPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkEyIiBkYXRhLXRvPSJDMyIgZGF0YS1sYWJlbD0i7JyE67mZIFdlYXZpbmciPgogIDxyZWN0IHg9IjgxLjE1OCIgeT0iNDYyLjIwMDAwMDAwMDAwMDA1IiB3aWR0aD0iODQuMTc4MDAwMDAwMDAwMDMiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxMjMuMjQ3MDAwMDAwMDAwMDEiIHk9IjQ3Ny4zNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7JyE67mZIFdlYXZpbmc8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlMxIiBkYXRhLWxhYmVsPSLtmozsm5DqsIDsnoUg66qo65OICuuztOyViCvroZzquYUr7Yq4656c7J6t7IWYK+2VteyLrCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxNDQuNjI2IiB5PSI4NCIgd2lkdGg9IjIxMi4zNzk5OTk5OTk5OTk5NyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjUwLjgxNTk5OTk5OTk5OTk3IiB5PSIxMTAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMjUwLjgxNTk5OTk5OTk5OTk3IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7ZqM7JuQ6rCA7J6FIOuqqOuTiDwvdHNwYW4+PHRzcGFuIHg9IjI1MC44MTU5OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+67O07JWIK+uhnOq5hSvtirjrnpzsnq3shZgr7ZW17IusPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlMyIiBkYXRhLWxhYmVsPSLqsrDsoJwg66qo65OICuuztOyViCvroZzquYUr7Yq4656c7J6t7IWYK+2VteyLrCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iMTU3LjgiIHdpZHRoPSIyMTIuMzc5OTk5OTk5OTk5OTciIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE2Mi4xOSIgeT0iMTg0LjcwMDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNjIuMTkiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7qsrDsoJwg66qo65OIPC90c3Bhbj48dHNwYW4geD0iMTYyLjE5IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rs7TslYgr66Gc6rmFK+2KuOuenOyereyFmCvtlbXsi6w8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzMiIGRhdGEtbGFiZWw9IuyjvOusuCDrqqjrk4gK67O07JWIK+uhnOq5hSvtirjrnpzsnq3shZgr7ZW17IusIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIyMzEuNjAwMDAwMDAwMDAwMDIiIHdpZHRoPSIyMTIuMzc5OTk5OTk5OTk5OTciIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE2Mi4xOSIgeT0iMjU4LjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE2Mi4xOSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuyjvOusuCDrqqjrk4g8L3RzcGFuPjx0c3BhbiB4PSIxNjIuMTkiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuuztOyViCvroZzquYUr7Yq4656c7J6t7IWYK+2VteyLrDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJOb3RlIiBkYXRhLWxhYmVsPSJOb3RlIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjY4LjYyNiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjkwLjMxMyIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5Ob3RlPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDMSIgZGF0YS1sYWJlbD0i7ZqM7JuQ6rCA7J6FIOuqqOuTiCDwn5GRCuyInOyImCDtlbXsi6wg66Gc7KeBIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM4Mi42MzIwMDAwMDAwMDAwNiIgeT0iMzY1LjQwMDAwMDAwMDAwMDAzIiB3aWR0aD0iMTUwLjEzNiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDU3LjcwMDAwMDAwMDAwMDA1IiB5PSIzOTIuMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNDU3LjcwMDAwMDAwMDAwMDA1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7ZqM7JuQ6rCA7J6FIOuqqOuTiCDwn5GRPC90c3Bhbj48dHNwYW4geD0iNDU3LjcwMDAwMDAwMDAwMDA1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7siJzsiJgg7ZW17IusIOuhnOyngTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDMiIgZGF0YS1sYWJlbD0i6rKw7KCcIOuqqOuTiCDwn5GRCuyInOyImCDtlbXsi6wg66Gc7KeBIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjIxOS4zMTYwMDAwMDAwMDAwMyIgeT0iMzY1LjQwMDAwMDAwMDAwMDAzIiB3aWR0aD0iMTM1LjMxNiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjg2Ljk3NDAwMDAwMDAwMDA1IiB5PSIzOTIuMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMjg2Ljk3NDAwMDAwMDAwMDA1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+6rKw7KCcIOuqqOuTiCDwn5GRPC90c3Bhbj48dHNwYW4geD0iMjg2Ljk3NDAwMDAwMDAwMDA1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7siJzsiJgg7ZW17IusIOuhnOyngTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDMyIgZGF0YS1sYWJlbD0i7KO866y4IOuqqOuTiCDwn5GRCuyInOyImCDtlbXsi6wg66Gc7KeBIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIzNjUuNDAwMDAwMDAwMDAwMDMiIHdpZHRoPSIxMzUuMzE2IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMjMuNjU4IiB5PSIzOTIuMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTIzLjY1OCIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuyjvOusuCDrqqjrk4gg8J+RkTwvdHNwYW4+PHRzcGFuIHg9IjEyMy42NTgiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyInOyImCDtlbXsi6wg66Gc7KeBPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkExIiBkYXRhLWxhYmVsPSLrs7TslYggQXNwZWN0IPCfm6HvuI8iIGRhdGEtc2hhcGU9InJvdW5kZWQiPgogIDxyZWN0IHg9IjMzNS4yNjg2NjY2NjY2NjY3IiB5PSI1MzUuNSIgd2lkdGg9IjEzOS43NjIiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iNiIgcnk9IjYiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNDA1LjE0OTY2NjY2NjY2NjciIHk9IjU1My45NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+67O07JWIIEFzcGVjdCDwn5uh77iPPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBMiIgZGF0YS1sYWJlbD0i66Gc6rmFIEFzcGVjdCDwn5OdIiBkYXRhLXNoYXBlPSJyb3VuZGVkIj4KICA8cmVjdCB4PSIxMDYuMzI3MzMzMzMzMzMzMzQiIHk9IjUzNS41IiB3aWR0aD0iMTMyLjM1MiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSI2IiByeT0iNiIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxNzIuNTAzMzMzMzMzMzMzMzMiIHk9IjU1My45NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+66Gc6rmFIEFzcGVjdCDwn5OdPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] AOP를 작동시키는 5대 핵심 구성 요소 용어 (3단 표 - 출제 1순위)**

AOP 메커니즘을 설명할 때 반드시 등장해야 하는 절대 키워드들입니다.

| **핵심 용어**             | **영문 명칭**     | **개념 및 작동 메커니즘 (역할)**                                                                                   |
| :-------------------- | :------------ | :------------------------------------------------------------------------------------------------------ |
| **1. 애스펙트** *(관점)*    | **Aspect**    | 로깅이나 트랜잭션 관리처럼 흩어진 여러 횡단 관심사를 묶어 **'하나의 독립된 모듈로 만들어 놓은 덩어리'** (Advice + Pointcut의 결합체).                 |
| **2. 조언** *(기능)*      | **Advice**    | 떼어낸 **'실제 부가 기능 코드(What)'** 그 자체이며, 핵심 로직의 \*\*'어느 시점(When)'\*\*에 실행할지(Before, After, Around 등)를 정의한 것. |
| **3. 조인포인트** *(합류점)*  | **JoinPoint** | Advice라는 부가 기능 코드가 핵심 로직 중간에 끼어들 수 있는(적용 가능한) **'합법적인 모든 실행 지점들의 후보군'**. (메서드 호출 시점, 예외 발생 시점 등).       |
| **4. 포인트컷** *(적용 타겟)* | **Pointcut**  | 수많은 JoinPoint(후보군) 중에서, 실제로 부가 기능을 꽂아 넣을 **'특정 메서드 타겟(Where)을 정확히 지정하는 필터링(정규표현식)'**.                   |
| **5. 위빙** *(엮기)*      | **Weaving**   | 분리해 둔 부가 기능(Advice)을 핵심 비즈니스 로직의 특정 타겟(Pointcut)에 **'조립하여 엮어 넣는 물리적인 과정'**. (컴파일, 로드, 런타임 위빙 존재).       |

#### **IV. \[결론/제언] OOP(객체지향)의 한계 극복과 Spring 프록시(Proxy) 패턴 기반의 진화**

* **(키워드 위주 2줄 마무리)** "AOP는 OOP를 대체하는 것이 아니라, OOP가 분리하지 못하는 '로깅/트랜잭션' 등의 횡단 관심사를 격리함으로써 객체지향을 더욱 객체지향답게 만들어주는 완벽한 보완재입니다. 자바 스프링(Spring Framework)은 런타임 시점에 가짜 대리자 객체를 앞세우는 **'프록시(Proxy) 디자인 패턴' 기반의 위빙 기술을 채택하여, 핵심 비즈니스 소스코드를 단 한 줄도 건드리지 않고 이 AOP의 위대한 마법을 구현**해 내고 있습니다."
