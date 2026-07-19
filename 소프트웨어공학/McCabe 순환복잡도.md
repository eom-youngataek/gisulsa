### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (McCabe순환복잡도정의,등장배경) — 3~4줄
Ⅱ. 계산공식및그래프이론 (본론①, 도식 1개 필수)
Ⅲ. 계산예시및복잡도등급 (본론②, 핵심 배점)
Ⅳ. 활용 - 테스트케이스개수와의관계
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬정적분석에서'복잡도(순환복잡도등)를수치로측정한다'고했는데, 그측정법의원조가 1976년토마스맥케이브가제안한 순환복잡도 — 프로그램의소스코드를보지않고도, '분기(if,while,for등)가몇개인지'만세면 그프로그램이얼마나복잡한지,테스트에얼마나많은경로가필요한지를수치로알수있다"\*\*는한줄로시작하면, 왜이지표가 오늘다룬여러답안(정적분석,결합도)의 기반이됐는지논리가섭니다.

### Ⅱ. 계산공식및그래프이론 — "그래프로코드를본다"

| 개념               | 내용                                        |
| :--------------- | :---------------------------------------- |
| **제어흐름그래프(CFG)** | 코드를 \*\*노드(처리)와엣지(흐름)\*\*로이루어진그래프로표현      |
| **공식**           | **V(G) = E - N + 2** (E:엣지수,N:노드수)        |
| **간편공식**         | **V(G) = 분기점(if,while,for,case등)의개수 + 1** |

→ 암기: **"그래프로그리고, 엣지에서노드를빼고2를더하거나, 그냥분기개수에1만더한다"** — 앞서다룬 \*\*"UML의상태머신다이어그램"\*\*과 같은 **그래프기반사고**가, 여기서는 코드복잡도측정에 활용됩니다.

### 도식화 제안

```
[제어흐름그래프예시]
if (a > 0) {
    처리1();          [시작]
} else {                ↓
    처리2();           [조건a>0?]
}                      ↙      ↘
                  [처리1]    [처리2]
                      ↘      ↙
                      [종료]

노드(N)=4, 엣지(E)=4
V(G) = E-N+2 = 4-4+2 = 2
(간편공식: 분기1개+1 = 2, 동일결과)
```

### Ⅲ. 계산예시및복잡도등급 — 핵심 배점

**함정 방지: 공식만알면절반. "숫자가나오면 그게뭘의미하는지" 등급기준을알아야완성됩니다.**

| 복잡도(V(G))  | 등급   | 의미                   |
| :--------- | :--- | :------------------- |
| **1\~10**  | 낮음   | 단순,테스트용이,**권장수준**    |
| **11\~20** | 중간   | 약간복잡,주의필요            |
| **21\~50** | 높음   | 복잡,**리팩토링권장**        |
| **50초과**   | 매우높음 | **테스트불가능수준**,반드시분리필요 |

→ 암기: **"10이하는안전,20넘으면주의,50넘으면손대야한다"** — 앞서다룬 **"테스트7대원칙의⑤결함집중"**(복잡한모듈에결함이몰림)의원인이바로 이 **순환복잡도가높은모듈**이며, 정적분석도구는이수치를 **자동으로계산해위험모듈을알려줍니다**.

**계산예시 (분기여러개인경우)**

```
if(A) { ... }
else if(B) { ... }
else if(C) { ... }
else { ... }
for(...) { ... }

분기개수: if/elseif/elseif(3) + for(1) = 4
V(G) = 4 + 1 = 5  ← 낮음등급,안전한수준
```

### Ⅳ. 활용 — 테스트케이스개수와의관계

**함정 방지: "복잡도측정용"으로만알면절반. "테스트를몇개짜야하는지"와의직결관계를보여줘야완성됩니다.**

| 활용             | 내용                                            |
| :------------- | :-------------------------------------------- |
| **최소테스트케이스수**  | **V(G)값이곧, 모든독립경로를커버하기위한 최소테스트케이스개수**와같음      |
| **화이트박스테스트연결** | 앞서다룬 **분기커버리지**를 100%달성하려면, 최소V(G)개의테스트케이스가필요 |
| **리팩토링우선순위결정** | V(G)가높은모듈을 **우선적으로**함수분리·단순화대상으로선정            |

→ 암기: **"복잡도숫자=최소테스트개수"** — 앞서예시의 V(G)=5인코드는, **최소5개의테스트케이스**로모든독립경로를검증할수있다는뜻입니다. 이연결이바로 앞서다룬 \*\*"화이트박스테스트(분기커버리지)"\*\*이 순환복잡도와 실무에서 항상함께쓰이는이유입니다.

### Ⅴ. 결론 포인트 (테스트·품질 시리즈 완결)

McCabe순환복잡도는 \*\*"코드가얼마나복잡한지"\*\*를 **주관적느낌이아니라객관적숫자**로바꿔주는 도구이며, 이는앞서다룬 \*\*정적분석(자동으로측정),결합도/응집도(복잡도를낮추는설계원칙),화이트박스테스트(그숫자만큼테스트케이스설계),테스트7대원칙의결함집중(복잡한곳에버그가몰림)\*\*을 모두하나의숫자로연결하는 핵심지표입니다 — 오늘하루다룬방대한소프트웨어공학·품질시리즈전체가, 결국 \*\*"복잡도를측정하고,줄이고,그복잡도에맞게테스트하는것"\*\*이라는하나의실무적순환고리로 완결됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "개발팀 막내가 자기가 짠 1,000줄짜리 코드를 보고 흐뭇해한다. '내 코드는 예술이야.' 하지만 QA 팀장이 그 코드를 보더니 기겁하며 소리친다. 'if문 안에 for문이 있고 또 그 안에 if문이 있는 이 스파게티 덩어리를 도대체 어떻게 테스트하라는 겁니까!' 이처럼 사람의 눈에 보이지 않는 코드의 '복잡함'과 '유지보수의 끔찍함'을 명확한 숫자로 때려잡기 위해 토마스 맥케이브(Thomas McCabe)가 발명한 공식이 바로 \*\*'순환 복잡도(Cyclomatic Complexity)'\*\*다. 복잡도를 구하는 법은 의외로 간단하다. 소스 코드를 동그라미와 화살표로 이루어진 흐름도(제어 흐름 그래프)로 바꾼 뒤, 선(Edge)의 개수에서 동그라미(Node)의 개수를 빼고 2를 더한다(**V(G) = E - N + 2**). 눈으로 푸는 더 쉬운 야매(?) 방법도 있다. 코드 안에 있는 조건 분기문(if, while, case 등 갈림길)의 개수를 센 다음 그냥 1을 더하면 끝난다(**P + 1**). 이렇게 계산되어 나온 복잡도 숫자 '10'이 의미하는 바는 매우 중대하다. 첫째, 이 코드를 완벽히 화이트박스 테스트하기 위해 필요한 \*\*'독립적인 테스트 케이스가 최소 10개'\*\*라는 뜻이다. 둘째, 이 숫자가 10을 넘어 20, 30으로 치솟는다면 코드에 치명적인 버그 폭탄이 숨어있을 확률이 극도로 높으니 당장 코드를 쪼개서(리팩토링) 복잡도를 낮추라는 강력한 경고등 역할을 한다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 스파게티 코드의 꼬임을 수학으로 증명하다, McCabe 순환 복잡도 개요**

* **정의:** 토마스 맥케이브가 제안한, 소프트웨어의 제어 흐름 그래프(Control Flow Graph)를 바탕으로 **코드 내부의 논리적 구조가 얼마나 복잡하게 얽혀있는지를 정량적인 수치로 측정하는 소프트웨어 복잡도 평가 지표**.
* **존재 목적:**
  1. 이 숫자는 화이트박스 테스팅(기본 경로 테스트) 시, 모든 코드를 한 번씩 실행하기 위해 \*\*'설계해야 할 최소한의 테스트 케이스(Test Case) 개수'\*\*를 의미함.
  2. 수치가 높을수록 버그 발생 확률이 높으므로 **리팩토링(Refactoring)의 우선순위를 결정**하는 지표가 됨.

#### **II. \[본론 1] 코드를 해부하는 제어 흐름 그래프와 면적(Region) (도식화)**

단순한 if-else 문이 들어간 코드가 어떻게 그래프로 변환되고 계산되는지 보여줍니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MTEuMTI2MDAwMDAwMDAwMDMgOTM1Ljc1OCIgd2lkdGg9IjQxMS4xMjYwMDAwMDAwMDAwMyIgaGVpZ2h0PSI5MzUuNzU4IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfX19Db250cm9sX0Zsb3dfR3JhcGhfXyIgZGF0YS1sYWJlbD0i7KCc7Ja0IO2dkOumhCDqt7jrnpjtlIQgKENvbnRyb2wgRmxvdyBHcmFwaCkg67OA7ZmYIOyYiOyLnCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMzMxLjEyNjAwMDAwMDAwMDAzIiBoZWlnaHQ9Ijg1NS43NTgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIzMzEuMTI2MDAwMDAwMDAwMDMiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7soJzslrQg7Z2Q66aEIOq3uOuemO2UhCAoQ29udHJvbCBGbG93IEdyYXBoKSDrs4DtmZgg7JiI7IucPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJOMSIgZGF0YS10bz0iTjIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iu2ZlOyCtO2RnCBFZGdlIiBwb2ludHM9IjIxNi4xMjYsMjExIDIxNi4xMjYsMzI3LjMiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209Ik4yIiBkYXRhLXRvPSJOMyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iVHJ1ZSDsobDqsbQg67aE6riwIiBwb2ludHM9IjIzNy45ODU2NjY2NjY2NjY2Nyw0MzYuNTk4MzMzMzMzMzMzMzYgMjM3Ljk4NTY2NjY2NjY2NjY3LDQ3MC40NTggMjkyLjYyNiw0NzAuNDU4IDI5Mi42MjYsNTc0Ljc1OCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTjIiIGRhdGEtdG89Ik40IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSJGYWxzZSDsobDqsbQg67aE6riwIiBwb2ludHM9IjE5NC4yNjYzMzMzMzMzMzMzNCw0MzYuNTk4MzMzMzMzMzMzMzYgMTk0LjI2NjMzMzMzMzMzMzM0LDQ3MC40NTggMTM5LjYyNiw0NzAuNDU4IDEzOS42MjYsNTc0Ljc1OCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTjMiIGRhdGEtdG89Ik41IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjI5Mi42MjYsNjk5Ljc1OCAyOTIuNjI2LDcyMy43NTggMjE2LjEyNiw3MjMuNzU4IDIxNi4xMjYsNzQ3Ljc1OCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTjQiIGRhdGEtdG89Ik41IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjEzOS42MjYsNjk5Ljc1OCAxMzkuNjI2LDcyMy43NTggMjE2LjEyNiw3MjMuNzU4IDIxNi4xMjYsNzQ3Ljc1OCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJOMSIgZGF0YS10bz0iTjIiIGRhdGEtbGFiZWw9Iu2ZlOyCtO2RnCBFZGdlIj4KICA8cmVjdCB4PSIxNzUuNjI2MDAwMDAwMDAwMDMiIHk9IjI1My45OTk5OTk5OTk5OTk5NyIgd2lkdGg9IjgwLjAyMDAwMDAwMDAwMDAxIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjE1LjYzNjAwMDAwMDAwMDAyIiB5PSIyNjkuMTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPu2ZlOyCtO2RnCBFZGdlPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209Ik4yIiBkYXRhLXRvPSJOMyIgZGF0YS1sYWJlbD0iVHJ1ZSDsobDqsbQg67aE6riwIj4KICA8cmVjdCB4PSIyNDYuMTI2MDAwMDAwMDAwMDMiIHk9IjUwMS40NTc5OTk5OTk5OTk5NyIgd2lkdGg9IjkyLjQ5NDAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjkyLjM3MzAwMDAwMDAwMDA1IiB5PSI1MTYuNjA4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5UcnVlIOyhsOqxtCDrtoTquLA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iTjIiIGRhdGEtdG89Ik40IiBkYXRhLWxhYmVsPSJGYWxzZSDsobDqsbQg67aE6riwIj4KICA8cmVjdCB4PSI5MS4xMjYiIHk9IjUwMS40NTc5OTk5OTk5OTk5NyIgd2lkdGg9Ijk2LjA1OCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjEzOS4xNTUiIHk9IjUxNi42MDgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPkZhbHNlIOyhsOqxtCDrtoTquLA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik4xIiBkYXRhLWxhYmVsPSIxLiDsi5zsnpEgTm9kZSIgZGF0YS1zaGFwZT0iY2lyY2xlIj4KICA8Y2lyY2xlIGN4PSIyMTYuMTI2IiBjeT0iMTQ3LjUiIHI9IjYzLjUiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjIxNi4xMjYiIHk9IjE0Ny41IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij4xLiDsi5zsnpEgTm9kZTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTjIiIGRhdGEtbGFiZWw9IjIuIOyhsOqxtOusuCBpZiIgZGF0YS1zaGFwZT0iZGlhbW9uZCI+CiAgPHBvbHlnb24gcG9pbnRzPSIyMTYuMTI2LDMyNy4zIDI4MS43MDUwMDAwMDAwMDAwNCwzOTIuODc5IDIxNi4xMjYsNDU4LjQ1OCAxNTAuNTQ3LDM5Mi44NzkiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMjE2LjEyNiIgeT0iMzkyLjg3OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Mi4g7KGw6rG066y4IGlmPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJOMyIgZGF0YS1sYWJlbD0iMy4g7Iuk7ZaJ66y4IEEiIGRhdGEtc2hhcGU9ImNpcmNsZSI+CiAgPGNpcmNsZSBjeD0iMjkyLjYyNiIgY3k9IjYzNy4yNTgiIHI9IjYyLjUiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI5Mi42MjYiIHk9IjYzNy4yNTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjMuIOyLpO2WieusuCBBPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJONCIgZGF0YS1sYWJlbD0iNC4g7Iuk7ZaJ66y4IEIiIGRhdGEtc2hhcGU9ImNpcmNsZSI+CiAgPGNpcmNsZSBjeD0iMTM5LjYyNiIgY3k9IjYzNy4yNTgiIHI9IjYyLjUiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEzOS42MjYiIHk9IjYzNy4yNTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjQuIOyLpO2WieusuCBCPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJONSIgZGF0YS1sYWJlbD0iNS4g7KKF66OMIE5vZGUiIGRhdGEtc2hhcGU9ImNpcmNsZSI+CiAgPGNpcmNsZSBjeD0iMjE2LjEyNiIgY3k9IjgxMy43NTgiIHI9IjY2IiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyMTYuMTI2IiB5PSI4MTMuNzU4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij41LiDsooXro4wgTm9kZTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iMTI5LjA1IiB3aWR0aD0iNjguNjI2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iOTAuMzEzIiB5PSIxNDcuNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Tm90ZTwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 순환 복잡도를 도출하는 3대 산출 공식 전격 해부 (3단 표 - 출제 1순위)**

위 도식을 바탕으로 계산 공식을 적용하면 3가지 방법 모두 똑같이 \*\*'2'\*\*라는 결과가 나와야 합니다.

| **산출 방식 명칭**                      | **복잡도 도출 공식 및 변수 의미**                                                               | **위 도식에 적용한 산출 결과 (예시)**           |
| :-------------------------------- | :---------------------------------------------------------------------------------- | :--------------------------------- |
| **방식 1. 노드와 간선** *(그래프 이론 기반)*    | **V(G) = E - N + 2** - `E` (Edge): 제어 흐름도의 간선(화살표) 수 - `N` (Node): 실행 구문을 의미하는 노드 수 | 화살표(E) 6개 - 노드(N) 5개 + 2 **= 2**   |
| **방식 2. 조건 분기문** *(실무에서 가장 많이 씀)* | **V(G) = P + 1** - `P` (Predicate Node): 갈림길이 2개 이상인 조건 노드(if, while, case 등)의 총 개수 | 조건문 if(P) 1개 + 1 **= 2**           |
| **방식 3. 면적(영역)** *(시각적 직관 기반)*    | **V(G) = R** - `R` (Region): 그래프의 선분들로 인해 닫혀진 내부 공간의 수 + 그래프 바깥쪽의 전체 외부 공간(1)       | 내부 닫힌 면적 1개 + 바깥쪽 외부 면적 1개 **= 2** |

#### **IV. \[결론/제언] 복잡도 "10"의 임계치(Threshold)와 화이트박스 테스팅의 척도**

* **(키워드 위주 2줄 마무리)** "McCabe 순환 복잡도의 맹점은 단순한 switch-case 문이 길어져도 복잡도 수치가 폭증한다는 것이지만, 일반적인 소프트웨어 공학에서는 **V(G) 수치를 '10 이하'로 유지하는 것을 강력히 권고**합니다. 이 10이라는 숫자는 해당 모듈을 완전히 커버하기 위해 10개의 독립된 테스트 케이스가 필요함을 의미하며, 수치가 이를 초과할 경우 개발자는 즉각적인 **메서드 추출(Extract Method) 등의 리팩토링을 통해 복잡도를 낮추어야 결함을 예방**할 수 있습니다."
