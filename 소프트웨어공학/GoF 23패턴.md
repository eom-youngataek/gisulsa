### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (GoF23패턴정의,3대분류기준) — 3~4줄
Ⅱ. 생성패턴5종 (본론①, 도식 1개 필수)
Ⅲ. 구조패턴7종 (본론②)
Ⅳ. 행위패턴11종 - 자주출제되는5개압축 (본론③, 핵심 배점)
Ⅴ. 결론
```

포인트: 개요에서 \*\*"객체지향프로그래밍에서반복적으로마주치는설계문제23가지에대해,4명의저자(Gang of Four)가정리한재사용가능한해법 — '객체를어떻게만들지(생성)','객체를어떻게조합할지(구조)','객체끼리어떻게소통할지(행위)'라는3가지질문으로분류된다"\*\*는한줄로시작하면, 23개가 왜3그룹으로나뉘는지논리가섭니다.

### Ⅱ. 생성패턴(Creational) 5종 — "객체를 어떻게 만들 것인가"

| 패턴         | 핵심                                 |
| :--------- | :--------------------------------- |
| **싱글턴**    | 인스턴스를 **오직하나만**생성·보장               |
| **팩토리메서드** | 객체생성을 **서브클래스에위임**(어떤클래스를만들지자식이결정) |
| **추상팩토리**  | **관련된객체군**을일관되게생성(팩토리들의팩토리)        |
| **빌더**     | 복잡한객체를 **단계별로조립**해생성               |
| **프로토타입**  | 기존객체를 \*\*복제(clone)\*\*해서새객체생성     |

→ 암기: **"하나만(싱글턴),자식이결정(팩토리메서드),세트로만들고(추상팩토리),단계별로쌓고(빌더),복제해서(프로토타입)"** — 앞서다룬"CBD"의 "컴포넌트를어떻게조달할지" 문제의식이, 객체단위에서는 이5가지생성전략으로구체화됩니다.

### Ⅲ. 구조패턴(Structural) 7종 — "객체를 어떻게 조합할 것인가"

| 패턴         | 핵심                         |
| :--------- | :------------------------- |
| **어댑터**    | 호환안되는 **인터페이스를변환**연결       |
| **브리지**    | 기능과구현을 **분리**해독립적으로확장      |
| **컴포지트**   | 개별객체와그룹을 **동일하게취급**(트리구조)  |
| **데코레이터**  | 객체에 **기능을동적으로추가**(포장지비유)   |
| **퍼사드**    | 복잡한내부를 **단순한창구하나로**감춤      |
| **플라이웨이트** | 공통데이터를 **공유**해메모리절약        |
| **프록시**    | 실제객체 **대리인**역할(접근제어,지연로딩등) |

→ 암기: **"어댑터는변환,브리지는분리,컴포지트는트리통일,데코레이터는포장,퍼사드는단순화창구,플라이웨이트는공유절약,프록시는대리인"** — 앞서다룬 "헥사고날아키텍처의어댑터"가 바로이 **어댑터패턴**의구조적개념을그대로가져온것이라는연결이핵심입니다.

### Ⅳ. 행위패턴(Behavioral) 11종 중 자주출제 5개 — 핵심 배점

**함정 방지: 11개를전부나열하면부담. 시험에서가장자주묻는5개를우선압축하고,나머지는범주로만인지하면충분합니다.**

| 패턴         | 핵심                                      |
| :--------- | :-------------------------------------- |
| **옵서버**    | 상태변화시 **등록된모든객체에자동통지**(발행-구독)           |
| **전략**     | 알고리즘을 **캡슐화해교체가능**하게(런타임에알고리즘변경)        |
| **템플릿메서드** | 알고리즘의 **골격은고정**,일부단계만서브클래스가재정의          |
| **커맨드**    | 요청자체를 **객체로캡슐화**(실행취소,큐잉가능)             |
| **상태**     | 객체의 **상태별로행동이달라짐**(앞서다룬MESI/상태머신과동일원리!) |

**+나머지6개(개념만인지)**: 책임연쇄,반복자,중재자,메멘토,방문자,인터프리터

→ 암기: **"옵서버는알림,전략은교체가능한알고리즘,템플릿은골격+커스텀,커맨드는요청을객체로,상태는상태별행동"** — 특히 \*\*"상태패턴"\*\*은 앞서 다룬 \*\*"상태머신다이어그램"\*\*과 \*\*"MESI(캐시일관성)"\*\*에서 반복됐던 \*\*"상태에따라행동이달라진다"\*\*는원리가, 객체지향설계패턴으로도구현된다는연결이 심화포인트입니다.

### 도식화 제안

```
[GoF 23패턴]
   ┌────────┼────────┐
[생성5종]    [구조7종]     [행위11종]
어떻게       어떻게        어떻게
만드나        조합하나       소통하나
싱글턴/       어댑터/데코레이터/  옵서버/전략/
팩토리/빌더    퍼사드/프록시등    템플릿메서드등
```

### Ⅴ. 결론 포인트 (아키텍처 시리즈 완결)

GoF23패턴의본질은 \*\*"변화가예상되는지점을미리식별하고,그지점을유연하게바꿀수있는표준적구조로미리대비하는것"\*\*입니다 — 이는앞서다룬헥사고날/클린아키텍처의 \*\*"핵심과기술을분리한다"\*\*는철학이,보다미시적인 클래스레벨에서 **구체적인23가지패턴**으로실현된것이며, MSA(서비스간경계)→헥사고날/클린아키텍처(서비스내부경계)→GoF패턴(클래스간관계)으로이어지는오늘의아키텍처시리즈전체가 \*\*"큰스케일에서작은스케일까지,변화에대비한경계짓기"\*\*라는하나의일관된설계원리로완결됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "건축가들이 건물을 지을 때마다 맨땅에 헤딩하지 않고 '아, 이런 지형에서는 이런 뼈대(패턴) 도면을 쓰면 안 무너지더라'라는 선배들의 족보를 참고하듯, 코딩의 세계에도 천재 개발자 4명(Gang of Four)이 집대성한 전설적인 설계 족보가 있다. 수백만 줄의 객체지향 코딩을 하다 보면 'A. 객체를 어떻게 안전하고 깔끔하게 낳게(생성) 할지?', 'B. 이 작은 객체 블록들을 어떻게 조립해서 거대한 로봇(구조)으로 만들지?', 'C. 그 로봇의 팔과 다리(객체들)가 서로 엉키지 않고 어떻게 통신(행위)하게 할지?'라는 똑같은 딜레마에 부딪힌다. GoF는 이 문제에 대한 23가지의 완벽한 정답을 3개의 거대한 카테고리로 쪼갰다. 첫째, 객체를 찍어내는 공장에 관한 **'생성(Creational) 패턴'**(싱글톤, 팩토리 등 5개). 둘째, 만들어진 블록들을 조립하여 뼈대를 튼튼하게 만드는 **'구조(Structural) 패턴'**(어댑터, 프록시 등 7개). 셋째, 객체들이 서로 어떻게 메시지를 주고받으며 임무를 나눌지를 결정하는 **'행위(Behavioral) 패턴'**(옵저버, 전략 패턴 등 11개)이다. 이 23가지의 족보는 무조건 외워야 하는 현대 프레임워크(Spring 등)의 뼈대 그 자체다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 바퀴를 다시 발명하지 마라, GoF 디자인 패턴 개요**

* **정의:** 소프트웨어 공학에서 객체지향 설계 과정 중 **자주 발생하는 설계 문제들에 대해, 재사용 가능하고 유연하며 모범적인 해결책(Best Practice)을 23가지로 체계화하여 정리한 패턴의 모음**.
* **기본 철학 2가지:**
  1. "구현(클래스)이 아닌 \*\*인터페이스(추상화)\*\*에 맞춰서 프로그래밍하라."
  2. "클래스의 상속(Inheritance)보다는 \*\*객체 합성(Composition)\*\*을 우선시하라."

#### **II. \[본론 1] 객체지향 설계의 3대 목적 체계 아키텍처 (도식화)**

패턴을 목적에 따라 3가지 거대한 범주로 나누는 것이 가장 중요합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5NjIuMjMxOTk5OTk5OTk5OSA0OTAuNSIgd2lkdGg9Ijk2Mi4yMzE5OTk5OTk5OTk5IiBoZWlnaHQ9IjQ5MC41IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJHb0ZfX18zX19fXzIzIiBkYXRhLWxhYmVsPSJHb0Yg65SU7J6Q7J24IO2MqO2EtOydmCAz64yAIOuqqeyggSDssrTqs4QgKOy0nSAyM+yihSkiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9Ijg4Mi4yMzE5OTk5OTk5OTk5IiBoZWlnaHQ9IjQxMC41IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iODgyLjIzMTk5OTk5OTk5OTkiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5Hb0Yg65SU7J6Q7J24IO2MqO2EtOydmCAz64yAIOuqqeyggSDssrTqs4QgKOy0nSAyM+yihSk8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkdvRiIgZGF0YS10bz0iQyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0NjcuNDA3NDk5OTk5OTk5OSwyMTQgNDY3LjQwNzQ5OTk5OTk5OTksMjM4IDQ2Ny40MDc0OTk5OTk5OTk5LDIzOCA0NjcuNDA3NDk5OTk5OTk5OSwyNjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkdvRiIgZGF0YS10bz0iUyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0NjcuNDA3NDk5OTk5OTk5OSwyMTQgNDY3LjQwNzQ5OTk5OTk5OTksMjM4IDc1OC45MTY0OTk5OTk5OTk4LDIzOCA3NTguOTE2NDk5OTk5OTk5OCwyNjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkdvRiIgZGF0YS10bz0iQiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0NjcuNDA3NDk5OTk5OTk5OSwyMTQgNDY3LjQwNzQ5OTk5OTk5OTksMjM4IDE4OS42MDY5OTk5OTk5OTk5NywyMzggMTg5LjYwNjk5OTk5OTk5OTk3LDI2MiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQyIgZGF0YS10bz0iQzEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDY3LjQwNzQ5OTk5OTk5OTksMzMyLjcgNDY3LjQwNzQ5OTk5OTk5OTksMzgwLjciIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlMiIGRhdGEtdG89IlMxIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9Ijc1OC45MTY0OTk5OTk5OTk4LDMzMi43IDc1OC45MTY0OTk5OTk5OTk4LDM4MC43IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJCIiBkYXRhLXRvPSJCMSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxODkuNjA2OTk5OTk5OTk5OTQsMzMyLjcgMTg5LjYwNjk5OTk5OTk5OTk3LDM4MC43IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJHb0YiIGRhdGEtbGFiZWw9IkdvRiAyMyDtjKjthLQiIGRhdGEtc2hhcGU9ImNpcmNsZSI+CiAgPGNpcmNsZSBjeD0iNDY3LjQwNzQ5OTk5OTk5OTkiIGN5PSIxNDkiIHI9IjY1IiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjQ2Ny40MDc0OTk5OTk5OTk5IiB5PSIxNDkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkdvRiAyMyDtjKjthLQ8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkMiIGRhdGEtbGFiZWw9IjEuIOyDneyEsSBDcmVhdGlvbmFsIPCfj60K7LSdIDXqsJwg7Yyo7YS0CuqwneyytOulvCDslrTrlrvqsowg64Kz7J2EIOqyg+yduOqwgD8iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzU3Ljg4Mjk5OTk5OTk5OTkiIHk9IjI2MiIgd2lkdGg9IjIxOS4wNDkiIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0NjcuNDA3NDk5OTk5OTk5OSIgeT0iMjk3LjM1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0NjcuNDA3NDk5OTk5OTk5OSIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPjEuIOyDneyEsSBDcmVhdGlvbmFsIPCfj608L3RzcGFuPjx0c3BhbiB4PSI0NjcuNDA3NDk5OTk5OTk5OSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7LSdIDXqsJwg7Yyo7YS0PC90c3Bhbj48dHNwYW4geD0iNDY3LjQwNzQ5OTk5OTk5OTkiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuqwneyytOulvCDslrTrlrvqsowg64Kz7J2EIOqyg+yduOqwgD88L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUyIgZGF0YS1sYWJlbD0iMi4g6rWs7KGwIFN0cnVjdHVyYWwg8J+nsQrstJ0gN+qwnCDtjKjthLQK6rCd7LK066W8IOyWtOuWu+qyjCDsobDrpr3tlaAg6rKD7J246rCAPyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI2NDEuOTgxOTk5OTk5OTk5OSIgeT0iMjYyIiB3aWR0aD0iMjMzLjg2OSIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9Ijc1OC45MTY0OTk5OTk5OTk4IiB5PSIyOTcuMzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9Ijc1OC45MTY0OTk5OTk5OTk4IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+Mi4g6rWs7KGwIFN0cnVjdHVyYWwg8J+nsTwvdHNwYW4+PHRzcGFuIHg9Ijc1OC45MTY0OTk5OTk5OTk4IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7stJ0gN+qwnCDtjKjthLQ8L3RzcGFuPjx0c3BhbiB4PSI3NTguOTE2NDk5OTk5OTk5OCIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+6rCd7LK066W8IOyWtOuWu+qyjCDsobDrpr3tlaAg6rKD7J246rCAPzwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJCIiBkYXRhLWxhYmVsPSIzLiDtlonsnIQgQmVoYXZpb3JhbCDwn4+D4oCN4pmC77iPCuy0nSAxMeqwnCDtjKjthLQK6rCd7LK064G866asIOyWtOuWu+qyjCDthrXsi6DtlaAg6rKD7J246rCAPyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI2NS4yNjI0OTk5OTk5OTk5NiIgeT0iMjYyIiB3aWR0aD0iMjQ4LjY4OSIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE4OS42MDY5OTk5OTk5OTk5NyIgeT0iMjk3LjM1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxODkuNjA2OTk5OTk5OTk5OTciIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj4zLiDtlonsnIQgQmVoYXZpb3JhbCDwn4+D4oCN4pmC77iPPC90c3Bhbj48dHNwYW4geD0iMTg5LjYwNjk5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7stJ0gMTHqsJwg7Yyo7YS0PC90c3Bhbj48dHNwYW4geD0iMTg5LjYwNjk5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7qsJ3ssrTrgbzrpqwg7Ja065a76rKMIO2GteyLoO2VoCDqsoPsnbjqsIA/PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkMxIiBkYXRhLWxhYmVsPSLsi7HquIDthqQsIO2Mqe2GoOumrCDrqZTshJzrk5wsCuy2lOyDgSDtjKnthqDrpqwsIOu5jOuNlCwg7ZSE66Gc7Yag7YOA7J6FIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM1MS4yMTM5OTk5OTk5OTk5NCIgeT0iMzgwLjciIHdpZHRoPSIyMzIuMzg2OTk5OTk5OTk5OTciIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0NjcuNDA3NDk5OTk5OTk5OSIgeT0iNDA3LjU5OTk5OTk5OTk5OTk3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0NjcuNDA3NDk5OTk5OTk5OSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuyLseq4gO2GpCwg7Yyp7Yag66asIOuplOyEnOuTnCw8L3RzcGFuPjx0c3BhbiB4PSI0NjcuNDA3NDk5OTk5OTk5OSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7LaU7IOBIO2Mqe2GoOumrCwg67mM642ULCDtlITroZzthqDtg4DsnoU8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzEiIGRhdGEtbGFiZWw9IuyWtOuMke2EsCwg7ZSE66Gd7IucLCDrjbDsvZTroIjsnbTthLAsCu2NvOyCrOuTnCwg67iM66a/7KeALCDsu7Ttj6zsp4DtirgsIO2UjOudvOydtOybqOydtO2KuCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI2MTEuNjAwOTk5OTk5OTk5OSIgeT0iMzgwLjciIHdpZHRoPSIyOTQuNjMxIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNzU4LjkxNjQ5OTk5OTk5OTgiIHk9IjQwNy41OTk5OTk5OTk5OTk5NyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNzU4LjkxNjQ5OTk5OTk5OTgiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7slrTrjJHthLAsIO2UhOuhneyLnCwg642w7L2U66CI7J207YSwLDwvdHNwYW4+PHRzcGFuIHg9Ijc1OC45MTY0OTk5OTk5OTk4IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7tjbzsgqzrk5wsIOu4jOumv+yngCwg7Lu07Y+s7KeA7Yq4LCDtlIzrnbzsnbTsm6jsnbTtirg8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQjEiIGRhdGEtbGFiZWw9IuyghOuetSwg7Ji17KCA67KELCDthZztlIzrpr8g66mU7ISc65OcLCDsg4Htg5wsCuy7pOunqOuTnCwg67CY67O17J6QLCDssYXsnoTsl7Dsh4QsIOykkeyerOyekCDrk7EiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9IjM4MC43IiB3aWR0aD0iMjY3LjIxMzk5OTk5OTk5OTk0IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTg5LjYwNjk5OTk5OTk5OTk3IiB5PSI0MDcuNTk5OTk5OTk5OTk5OTciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE4OS42MDY5OTk5OTk5OTk5NyIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuyghOuetSwg7Ji17KCA67KELCDthZztlIzrpr8g66mU7ISc65OcLCDsg4Htg5wsPC90c3Bhbj48dHNwYW4geD0iMTg5LjYwNjk5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7su6Trp6jrk5wsIOuwmOuzteyekCwg7LGF7J6E7Jew7IeELCDspJHsnqzsnpAg65OxPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] GoF 23가지 디자인 패턴 전격 분류 및 핵심 요약 (3단 표 - 출제 1순위)**

암기법(생성: 추빌팩프싱 / 구조: 어브컴데퍼플프)과 함께 시험에 가장 자주 나오는 핵심 패턴들입니다.

| **카테고리 목적**                                          | **빈출 핵심 패턴 명칭**               | **해결하려는 문제점 및 작동 메커니즘 요약**                                                             |
| :--------------------------------------------------- | :---------------------------- | :------------------------------------------------------------------------------------- |
| **1. 생성 🏭** *(Creational)* 객체의 생성 방식과 과정을 캡슐화       | **싱글톤 (Singleton)**           | 어떤 클래스의 인스턴스(객체)가 시스템 전체에서 **오직 딱 1개만 생성됨을 보장**하고, 어디서든 그 1개에만 접근하게 만듦. (예: DB 커넥션 풀). |
| <br />                                               | **팩토리 메서드 (Factory Method)**  | 객체를 생성하는 코드를 직접 짜지 않고, 생성 역할을 서브 클래스(공장)로 미뤄서 **객체 생성의 유연성**을 확보함.                     |
| **2. 구조 🧱** *(Structural)* 클래스와 객체들을 조합해 더 큰 구조를 만듦 | **어댑터 (Adapter)**             | 220V 플러그에 110V 변환기를 꽂듯, **호환되지 않는 두 인터페이스를 연결**하여 함께 작동할 수 있도록 중간 변환기를 만듦.             |
| <br />                                               | **프록시 (Proxy)**               | 원본 객체로 바로 접근하지 않고, **대리인(Proxy)을 거쳐서 접근**하게 하여 보안 제어, 흐름 제어, 로딩 지연(캐시) 등을 수행함.         |
| <br />                                               | **데코레이터 (Decorator)**         | 코드를 수정하지 않고, 객체에 기능(장식)을 동적으로 계속 덧붙이는 유연한 확장의 끝판왕.                                     |
| **3. 행위 🏃‍♂️** *(Behavioral)* 객체 간의 상호작용과 책임 분배     | **옵저버 (Observer)**            | 어떤 객체의 상태가 변하면, 그 객체를 구독하고 있는 수많은 쩌리들(Observer)에게 **자동으로 "나 변했어!"라고 알림을 쫙 뿌림.**        |
| <br />                                               | **전략 (Strategy)**             | 알고리즘(무기)들을 캡슐화해 놓고, 런타임에 언제든지 칼에서 총으로 **전략(알고리즘)을 갈아 끼울 수 있게(교체 가능하게)** 만듦.            |
| <br />                                               | **템플릿 메서드 (Template Method)** | 전체 뼈대(로직의 순서)는 부모 클래스에서 짜놓고, 구체적인 세부 구현만 자식 클래스에게 구멍을 뚫어(오버라이딩) 넘김.                    |

*(이 외에도 3대 분류에 속하는 23개 전체 이름을 인지하고 있어야 합니다.)*

#### **IV. \[결론/제언] 객체지향 SOLID 원칙의 실체화 및 프레임워크 설계의 절대 뼈대**

* **(키워드 위주 2줄 마무리)** "디자인 패턴은 단순히 코딩 기교가 아니라, 객체지향의 5대 원칙인 **'SOLID 원칙'이 어떻게 소스코드 레벨로 실체화되는지를 보여주는 완벽한 교과서**입니다. 자바의 Spring 프레임워크 내부 깊숙한 곳에는 이러한 싱글톤, 프록시, 템플릿 메서드 패턴들이 촘촘히 엮여있으며, 이 패턴들을 이해하는 것은 **견고한 아키텍처 설계를 위한 개발자의 최우선 필수 소양**입니다."
