### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (CRUD매트릭스정의, 앞서다룬ERD와의관계) — 3~4줄
Ⅱ. 매트릭스구조 (본론①, 도식 1개 필수)
Ⅲ. 검증기능 - 4대이상패턴탐지, 핵심 배점
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서다룬식별/비식별관계로엔티티(데이터)구조를완성했다면, CRUD매트릭스는'그데이터를 실제업무프로세스가 어떻게사용하는지'를 교차검증하는도구 — 세로축엔데이터(엔티티),가로축엔프로세스(기능)를놓고, 각교차점에Create/Read/Update/Delete중무엇이일어나는지표시"\*\*한다는 한줄로시작하면, 왜 ERD 다음단계에서 필요한지 드러납니다.

### Ⅱ. 매트릭스구조

| <br />            | **주문등록** | **주문조회** | **주문취소** | **재고관리** |
| :---------------- | :------- | :------- | :------- | :------- |
| **주문(Order)**     | **C**    | R        | **D**    | -        |
| **재고(Inventory)** | U        | R        | U        | **CRUD** |
| **고객(Customer)**  | R        | R        | R        | -        |

→ 암기: **"세로엔데이터,가로엔프로세스,교차점엔C/R/U/D"** — 이표하나로 \*\*"어떤프로세스가 어떤데이터에 어떤작업을하는지"\*\*를 **한눈에** 파악할수있습니다.

### 도식화 제안

```
        [프로세스1] [프로세스2] [프로세스3]
[데이터A]    C          R          -
[데이터B]    R          U          D
[데이터C]    -          R          C

→ 행(데이터)과 열(프로세스)의교차점마다 실제작업(CRUD)표시
```

### Ⅲ. 검증기능 — 4대이상패턴탐지, 핵심 배점

**함정 방지: "표를만든다"고만답하면절반. 이표가 실제로어떤설계결함을잡아내는지 구체적이상패턴을보여줘야완성됩니다.**

| 이상패턴                      | 의미                                                                     |
| :------------------------ | :--------------------------------------------------------------------- |
| **고아데이터**(Create가없음)      | 어떤프로세스도 **C(생성)를안하는데 R/U/D만있는데이터**— \*\*"이데이터는어디서생기는거지?"\*\*라는 근본적설계결함 |
| **좀비데이터**(Delete가없음)      | **생성만되고삭제프로세스가없는데이터**— 시간이지날수록 **무한히쌓이는위험**                            |
| **미사용데이터**(전체가없음)         | 어떤프로세스도 **건드리지않는엔티티**— 앞서다룬 \*\*"코드스멜"\*\*처럼, 존재의의가없는 **불필요한설계**       |
| **과도한책임집중**(한프로세스가CRUD전부) | 하나의프로세스가 **너무많은데이터를 너무깊이건드림**— 앞서다룬 \*\*"결합도과다"\*\*와 유사한 **설계경고신호**    |

→ 암기: **"생성이없으면고아,삭제가없으면좀비,아무것도없으면미사용,다있으면과부하"** — 앞서다룬 \*\*"결합도/응집도"\*\*답안의 논리가, CRUD매트릭스에서는 \*\*"프로세스와데이터간의건강한관계인지"\*\*를 검증하는 형태로 재현됩니다.

### 도식화 제안

```
[이상패턴 탐지]
[데이터X]: R U D 만있고 C가없음 → "고아데이터!어디서생성되나?"
[데이터Y]: C R U 만있고 D가없음 → "좀비데이터!영원히안지워짐?"
[데이터Z]: 모든프로세스에서 공란 → "미사용데이터,왜만들었나?"
[프로세스W]: 5개데이터에 모두CRUD → "책임과다,분리검토필요"
```

### Ⅳ. 결론

CRUD매트릭스는 \*\*"앞서다룬ERD(데이터구조)가 실제업무프로세스와제대로맞물려작동하는지"\*\*를 표하나로 검증하는 강력한도구입니다 — **고아데이터,좀비데이터,미사용데이터**같은 이상패턴을 **설계초기에발견**함으로써, 시스템이 실제로가동되기 전에 \*\*"이설계가완전한가"\*\*를 사전에 점검할수있습니다 — 이는 앞서다룬 \*\*"RTM(요구사항추적매트릭스)"\*\*과 유사한 **"매트릭스형태로누락을찾아내는"** 방법론이며, 데이터모델링(ERD)과 프로세스모델링(기능분석)을 **하나의표로교차검증**하는 실무의핵심기법입니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "우리가 설계한 업무 프로세스(행동)와 데이터베이스 테이블(저장소)이 서로 아귀가 잘 맞는지 2차원 표(Matrix)로 그려서 교차 검증하는 절대 규칙이다. 가로축엔 테이블(엔터티)을, 세로축엔 업무(프로세스)를 두고 두 개가 만나는 교차점에 **C(생성), R(읽기), U(수정), D(삭제)** 알파벳을 적어 넣는다. 핵심은 \*\*'불량품 찾기(검증)'\*\*다. 어떤 테이블이든 반드시 누군가는 데이터를 넣어줘야(C) 하고, 반드시 누군가는 읽어줘야(R) 한다. 만약 매트릭스에 'C'나 'R'이 아예 없는 고아 테이블이 발견되면, 설계가 박살 난 유령 테이블이므로 당장 설계도로 돌아가 에러를 뜯어고쳐야 한다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 모델링의 십자포화 검증, CRUD 매트릭스 개요**

* **정의:** 시스템 분석/설계 단계에서 도출된 프로세스(Process)와 데이터 엔터티(Entity) 간의 상관관계를 C, R, U, D로 매핑하여 누락이나 모순이 없는지 교차 검증하는 2차원 모델링 도구.
* **목적:** 사용자의 요구사항(업무)이 데이터 모델(ERD)에 완벽히 반영되었는지 점검하고, 쓸데없이 생성되거나 방치되는 잉여 데이터를 색출하여 시스템 최적화를 달성하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 프로세스와 데이터의 2차원 만남**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTQuOTIgMzA5LjQiIHdpZHRoPSI1MTQuOTIiIGhlaWdodD0iMzA5LjQiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IkNSVURfX19fIiBkYXRhLWxhYmVsPSJDUlVEIOunpO2KuOumreyKpOydmCDqtZDssKgg6rKA7KadIOybkOumrCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNDM0LjkxOTk5OTk5OTk5OTk2IiBoZWlnaHQ9IjIyOS40IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNDM0LjkxOTk5OTk5OTk5OTk2IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+Q1JVRCDrp6Ttirjrpq3siqTsnZgg6rWQ7LCoIOqygOymnSDsm5Drpqw8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlAiIGRhdGEtdG89IkNST1NTIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjIxNi41MSwyMTguMDQ5OTk5OTk5OTk5OTggMjQwLjUxLDIxOC4wNDk5OTk5OTk5OTk5OCAyNDAuNTEsMTY4LjcgMjY0LjUxLDE2OC43IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJFIiBkYXRhLXRvPSJDUk9TUyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyMTYuNTEsMTE5LjM1IDI0MC41MSwxMTkuMzUgMjQwLjUxLDE2OC43IDI2NC41MSwxNjguNyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQ1JPU1MiIGRhdGEtdG89IlYiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzUwLjkxOTk5OTk5OTk5OTk2LDE2OC43IDM5OC45MTk5OTk5OTk5OTk5NiwxNjguNyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUCIgZGF0YS1sYWJlbD0i7IS466Gc7LaVIOKsh++4jwrsl4XrrLQg7ZSE66Gc7IS47IqkCijtmozsm5DqsIDsnoUsIOqysOygnCDrk7EpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIxODIuNyIgd2lkdGg9IjE2MC41MSIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEzNi4yNTUiIHk9IjIxOC4wNDk5OTk5OTk5OTk5OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTM2LjI1NSIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPuyEuOuhnOy2lSDirIfvuI88L3RzcGFuPjx0c3BhbiB4PSIxMzYuMjU1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7sl4XrrLQg7ZSE66Gc7IS47IqkPC90c3Bhbj48dHNwYW4geD0iMTM2LjI1NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+KO2ajOybkOqwgOyehSwg6rKw7KCcIOuTsSk8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ1JPU1MiIGRhdGEtbGFiZWw9IkNST1NTIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjI2NC41MSIgeT0iMTUwLjI1IiB3aWR0aD0iODYuNDEiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMzA3LjcxNSIgeT0iMTY4LjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkNST1NTPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJFIiBkYXRhLWxhYmVsPSLqsIDroZzstpUg4p6h77iPCuuNsOydtO2EsCDsl5TthLDti7AKKO2ajOybkCwg7KO866y4IO2FjOydtOu4lCkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMTYwLjUxIiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTM2LjI1NSIgeT0iMTE5LjM1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxMzYuMjU1IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+6rCA66Gc7LaVIOKeoe+4jzwvdHNwYW4+PHRzcGFuIHg9IjEzNi4yNTUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuuNsOydtO2EsCDsl5TthLDti7A8L3RzcGFuPjx0c3BhbiB4PSIxMzYuMjU1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj4o7ZqM7JuQLCDso7zrrLgg7YWM7J2067iUKTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJWIiBkYXRhLWxhYmVsPSJWIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM5OC45MTk5OTk5OTk5OTk5NiIgeT0iMTUwLjI1IiB3aWR0aD0iNjAiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNDI4LjkxOTk5OTk5OTk5OTk2IiB5PSIxNjguNyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+VjwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] CRUD 매트릭스 구조 및 필수 검증 룰 전격 해부 (3단 표)**

이 토픽은 '어떻게 그리는가(구조)'보다 \*\*'그려놓고 무엇을 잡아낼 것인가(무결성 검증 룰)'\*\*를 나열하는 것이 완벽한 득점 포인트입니다.

| **핵심 척도**       | **📊 구성 요소 및 구조**                                                                             | **📝 CRUD 액션 매핑**                                                                        | **🚨 무결성 검증 룰 (Rule) 💯**                                                                                                             |
| :-------------- | :-------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| **개념 / 구조**     | **'가로와 세로의 만남'.** - 열(Column): ERD에서 도출한 엔터티(테이블). - 행(Row): DFD(데이터흐름도)나 요구사항에서 도출한 단위 프로세스. | **'4대 데이터 액션 정의'.** 각 프로세스가 특정 엔터티를 만날 때, 생성(C), 읽기(R), 갱신(U), 삭제(D) 중 무엇을 하는지 알파벳을 마킹함. | **'결함(Defect) 색출 💯'.** 마킹이 끝난 매트릭스를 상하좌우로 훑어보며, 설계가 빵꾸난 곳을 찾아내는 체크리스트.                                                               |
| **세부 작성법 및 특징** | 기능 분해도의 가장 최하위 단위(단위 프로세스)와 물리적 테이블 단위로 매핑하는 것이 원칙임.                                          | 하나의 교차점에 여러 액션이 동시에 일어날 수 있음 (예: 조회 후 수정 = RU, 생성 후 조회 = CR).                            | **\[모든 엔터티는 'C'가 필수 💯]** 입력되는 곳(C)이 없는데 R, U, D만 있다면 쓰레기(유령) 데이터임. **\[모든 엔터티는 'R'이 필수 💯]** 기껏 넣어(C) 놓고 아무 프로세스도 읽지(R) 않으면 잉여 저장소임. |
| **활용 범위**       | 시스템 개발 전 설계 검증.                                                                               | 각 트랜잭션의 부하량(성능) 예측.                                                                      | 모든 단위 프로세스는 반드시 하나 이상의 엔터티를 건드려야 함(CRUD 중 하나 이상).                                                                                     |

#### **IV. \[결론/제언] 마이크로서비스(MSA) 분리 기준(Bounded Context)으로서의 활용**

* **(키워드 위주 2줄 마무리)** "과거 CRUD 매트릭스는 단순한 모델링 에러 검증용이었으나, 현대 클라우드 아키텍처에서는 밀집된 CRUD 덩어리들을 분석하여 쪼개는 **마이크로서비스(MSA)의 '바운디드 컨텍스트(Bounded Context)' 식별 및 분리 기준(Heuristic) 도구로 그 가치가 재조명되고 있습니다.**".
