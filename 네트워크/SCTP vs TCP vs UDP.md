### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (3대프로토콜의근본적차이축) — 3~4줄
Ⅱ. TCP vs UDP - 신뢰성vs속도 (본론①, 도식 1개 필수)
Ⅲ. SCTP - 멀티스트리밍·멀티호밍 (본론②, 핵심 배점)
Ⅳ. 결론
```

### Ⅰ. 개요

앞서다룬 **TCP의3-wayhandshake,ARQ,슬라이딩윈도우,혼잡제어**는 모두 \*\*"신뢰성을보장하는대가로속도를희생"\*\*하는 설계였습니다. UDP는 그 **신뢰성을완전히포기**하고 속도만취했고, SCTP는 \*\*"TCP의신뢰성+UDP의일부장점을결합"\*\*한 **제3의선택**입니다.

### Ⅱ. TCP vs UDP — 신뢰성vs속도

| 구분       | **TCP**                    | **UDP**                              |
| :------- | :------------------------- | :----------------------------------- |
| **연결설정** | 앞서다룬 **3-wayhandshake필요**  | **없음**(연결개념자체가없음)                    |
| **신뢰성**  | 앞서다룬 **ARQ,슬라이딩윈도우**로재전송보장 | **보장안함**(손실되면그냥사라짐)                  |
| **순서보장** | 순서대로도착보장                   | **보장안함**                             |
| **속도**   | 오버헤드로 **상대적으로느림**          | **매우빠름**                             |
| **대표활용** | 웹,파일전송,이메일                 | **DNS,스트리밍,VoIP,DDoS공격**(앞서다룬UDP플러드) |

→ 암기: **"TCP는확실하게,UDP는빠르게"** — 앞서다룬 \*\*"DDoS답안의UDP플러드"\*\*가 바로 UDP의 \*\*"연결설정없이그냥대량전송가능"\*\*이라는 특성을악용한것이었습니다.

### 도식화 제안

```
[TCP]                          [UDP]
3-way handshake                연결설정없음
ARQ로재전송보장                  손실보장안함
슬라이딩윈도우+혼잡제어           속도우선
     ↓                              ↓
신뢰성확보,속도희생                속도확보,신뢰성희생
```

### Ⅲ. SCTP — 멀티스트리밍·멀티호밍, 핵심 배점

**함정 방지: "TCP와UDP의중간"이라고만답하면절반. SCTP만의고유한2대핵심기능을보여줘야완성됩니다.**

| 기능                          | 내용                                                                                                |
| :-------------------------- | :------------------------------------------------------------------------------------------------ |
| **멀티스트리밍**(Multi-streaming) | 하나의연결안에 \*\*여러개의독립적인데이터흐름(스트림)\*\*을운반 — 한스트림에서 **패킷손실이생겨도**다른스트림은 **영향안받음**(HeadofLineBlocking해결) |
| **멀티호밍**(Multi-homing)      | 하나의연결이 \*\*여러개의IP주소(네트워크경로)\*\*를동시에가질수있음 — **한경로가끊겨도자동으로다른경로로전환**                                 |
| **4-way handshake**(연결설정)   | 앞서다룬 **TCP의3-way**가아니라 **SCTP는4-way**(SYN채우기공격에더강건)                                               |

→ 암기: **"여러줄로동시에보내고(멀티스트리밍),여러길로동시에연결하고(멀티호밍)"** — TCP는 \*\*"한줄로순서대로만"\*\*전송해야해서, 앞줄패킷이막히면 뒤에것도못가는 **HOL블로킹**문제가있는데, SCTP는 **독립된여러스트림**으로 이문제를해결합니다.

### 도식화 제안

```
[TCP - 단일스트림]
[패킷1][패킷2✗손실][패킷3][패킷4] → 순서보장해야해서 3,4도대기(HOL블로킹)

[SCTP - 멀티스트리밍]
스트림A: [1][2✗][3][4] → 스트림A만대기
스트림B: [1][2][3][4]  → 스트림B는영향없이계속진행

[SCTP - 멀티호밍]
[클라이언트] ══경로1(주경로)══→ [서버]
            ══경로2(백업경로)══→
            (경로1끊기면 자동으로경로2사용)
```

**왜통신사·전화망(SS7/Diameter)이 SCTP를쓰는가**: 앞서다룬 **BPFDoor의SCTP지원**답안에서, 통신사인프라가 \*\*"가입자행동,위치정보"\*\*같은 민감데이터를 SCTP로전송했던이유가바로 \*\*"통신사망은절대끊기면안되므로 멀티호밍의경로이중화가필수"\*\*이고, \*\*"여러종류의신호(음성제어,과금정보등)를한연결에서 독립적으로다뤄야해서 멀티스트리밍이유용"\*\*하기때문입니다.

### Ⅳ. 결론

TCP,UDP,SCTP는 \*\*"신뢰성,속도,그리고신뢰성+가용성"\*\*이라는 각기다른우선순위를가진 전송프로토콜입니다 — 앞서다룬 **TCP의핸드셰이크·ARQ·혼잡제어**가 \*\*"단일경로에서순서대로,확실하게"\*\*전송하는데초점을맞췄다면, SCTP는 **"여러경로,여러스트림을동시에"** 다뤄야하는 **통신사인프라같은고가용성환경**에특화되어있습니다 — 이는 앞서다룬 **BPFDoor가왜통신망을노렸는지**, 그리고 **왜그공격의흔적에 SCTP지원이포함됐는지**를 설명하며, 오늘하루다룬 네트워크신뢰성시리즈전체(TCP핸드셰이크→ARQ→슬라이딩윈도우→혼잡제어→SCTP)를 **"목적에따라다른프로토콜을선택하는"** 하나의완결된그림으로마무리합니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "인터넷 세상에서 데이터를 배달하는 배달부(프로토콜)는 크게 3명이다. 첫째, **'UDP(막무가내 퀵서비스)'**. 고객이 집에 있든 없든 묻지도 따지지도 않고 물건을 현관에 막 던지고 간다. 속도는 제일 빠르지만 분실(에러)돼도 절대 책임지지 않는다. (유튜브 라이브 영상 등에 쓰임). 둘째, **'TCP(꼼꼼한 우체국 등기)'**. 배달 전 전화로 확인(3-way)하고 서명까지 받아 확실하게 배달한다. 하지만 길이 '1차선'뿐이라, 앞차가 고장 나면 뒷차까지 싹 다 멈춰버리는 심각한 꽉 막힘(HOL Blocking) 병목 현상이 있다. 셋째, **'SCTP(차세대 멀티 배달부)'**. TCP의 '정확함'과 UDP의 '빠름'을 합친 사기 캐릭터다. 길이 끊어지면 즉시 예비 길로 우회(Multi-homing)하고, 1차선이 아니라 여러 개의 차선(Multi-streaming)으로 물건을 쪼개서 병렬로 배달하므로 하나가 막혀도 다른 차선은 쌩쌩 달리는 최강의 프로토콜이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 전송 계층(Transport Layer) 3대 프로토콜의 진화 개요**

* **UDP:** 신뢰성은 포기하고 속도(Speed)에 모든 것을 건 연결 지향 없는(Connectionless) 비신뢰성 프로토콜.
* **TCP:** 웹(HTTP) 통신의 근간으로, 데이터가 100% 도착함을 보장하지만 순서대로 꽉 막힌 1차선(단일 스트림)으로 쏘기 때문에 딜레이가 발생하는 신뢰성 프로토콜.
* **SCTP (차세대 프로토콜):** TCP의 신뢰성을 그대로 가져오면서, 여러 개의 길(다중 홈)과 여러 개의 차선(다중 스트림)을 뚫어 TCP의 병목 현상을 완벽히 해결한 하이브리드 프로토콜.

#### **II. \[본론 1] (극단적 단순화 버전) 3대 프로토콜 배달 방식 직관적 도식화**

복잡한 선을 모두 빼고, \*\*'길(차선)이 몇 개인가'\*\*에만 집중하여 그렸습니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MjQuNzE0IDQ3Ny43MDAwMDAwMDAwMDAwNSIgd2lkdGg9IjUyNC43MTQiIGhlaWdodD0iNDc3LjcwMDAwMDAwMDAwMDA1IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSIxX1VEUF9fX19fIiBkYXRhLWxhYmVsPSIxLiBVRFAgKOu5oOultOyngOunjCDrtoTsi6Qg7LGF7J6EIOyViCDsp5ApIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI0MjguNjc1OTk5OTk5OTk5OTMiIGhlaWdodD0iOTYuOSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjQyOC42NzU5OTk5OTk5OTk5MyIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjEuIFVEUCAo67mg66W07KeA66eMIOu2hOyLpCDssYXsnoQg7JWIIOynkCk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSIyX1RDUF8xX18iIGRhdGEtbGFiZWw9IjIuIFRDUCAoMeywqOyEoOydtOudvCDrp4ntnojrqbQg7Jis7Iqk7YaxKSI+CiAgPHJlY3QgeD0iNDAiIHk9IjE2NC45IiB3aWR0aD0iNDQ0LjcxNDAwMDAwMDAwMDA2IiBoZWlnaHQ9Ijk2LjkiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iMTY0LjkiIHdpZHRoPSI0NDQuNzE0MDAwMDAwMDAwMDYiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSIxNzguOSIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij4yLiBUQ1AgKDHssKjshKDsnbTrnbwg66eJ7Z6I66m0IOyYrOyKpO2GsSk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSIzX1NDVFBfX19fIiBkYXRhLWxhYmVsPSIzLiBTQ1RQICjsl6zrn6wg7LCo7ISg7Jy866GcIOyMqeyMqSEg8J+RkSkiPgogIDxyZWN0IHg9IjQwIiB5PSIyODkuOCIgd2lkdGg9IjQyNC41MTgwMDAwMDAwMDAwMyIgaGVpZ2h0PSIxNDcuOSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSIyODkuOCIgd2lkdGg9IjQyNC41MTgwMDAwMDAwMDAwMyIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjMwMy44IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjMuIFNDVFAgKOyXrOufrCDssKjshKDsnLzroZwg7Iyp7IypISDwn5GRKTwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVV9TRU5EIiBkYXRhLXRvPSJVX1JFQ1YiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLrjIDstqkg66eJIOuNmOynkCAo67mE7Iug66Kw7ISxKSIgcG9pbnRzPSIxNDIuNDEsMTAyLjQ1IDM3Mi4yMDYsMTAyLjQ1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlRfU0VORCIgZGF0YS10bz0iVF9SRUNWIiBkYXRhLXN0eWxlPSJ0aGljayIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJmYWxzZSIgZGF0YS1sYWJlbD0i7Jik7KeBIDHqsJzsnZgg6ri4ICjri6jsnbwg7Iqk7Yq466a8KSIgcG9pbnRzPSIxNDIuNDEsMjI3LjM1MDAwMDAwMDAwMDAyIDM3Mi4yMDYsMjI3LjM1MDAwMDAwMDAwMDAyIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIyIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iU19TRU5EIiBkYXRhLXRvPSJTX1JFQ1YiIGRhdGEtc3R5bGU9InRoaWNrIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9ImZhbHNlIiBkYXRhLWxhYmVsPSLssKjshKAgMSAo7Iqk7Yq466a8IDEpIiBwb2ludHM9IjE0Mi40MSwzODcuMzI1MDAwMDAwMDAwMDUgMTU0LjQxLDM4Ny4zMjUwMDAwMDAwMDAwNSAxNTQuNDEsNDExLjQgMzI2LjEwODAwMDAwMDAwMDA2LDQxMS40IDMyNi4xMDgwMDAwMDAwMDAwNiwzODcuMzI1MDAwMDAwMDAwMDUgMzcyLjIwNiwzODcuMzI1MDAwMDAwMDAwMDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjIiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTX1NFTkQiIGRhdGEtdG89IlNfUkVDViIgZGF0YS1zdHlsZT0idGhpY2siIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0iZmFsc2UiIGRhdGEtbGFiZWw9IuywqOyEoCAyICjsiqTtirjrprwgMikiIHBvaW50cz0iMTQyLjQxLDM3OC4xIDM3Mi4yMDYsMzc4LjEiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjIiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTX1NFTkQiIGRhdGEtdG89IlNfUkVDViIgZGF0YS1zdHlsZT0idGhpY2siIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0iZmFsc2UiIGRhdGEtbGFiZWw9IuywqOyEoCAzICjsmrDtmowg64+E66GcIO2ZleuztCkiIHBvaW50cz0iMTQyLjQxLDM2OC44NzUgMTU0LjQxLDM2OC44NzUgMTU0LjQxLDM0NC44IDMyNi4xMDgwMDAwMDAwMDAwNiwzNDQuOCAzMjYuMTA4MDAwMDAwMDAwMDYsMzY4Ljg3NSAzNzIuMjA2LDM2OC44NzUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjIiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlVfU0VORCIgZGF0YS10bz0iVV9SRUNWIiBkYXRhLWxhYmVsPSLrjIDstqkg66eJIOuNmOynkCAo67mE7Iug66Kw7ISxKSI+CiAgPHJlY3QgeD0iMTg2LjQxIiB5PSI4Ni40NDk5OTk5OTk5OTk5OSIgd2lkdGg9IjEzNS44NTYiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyNTQuMzM4IiB5PSIxMDEuNiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+64yA7LapIOuniSDrjZjsp5AgKOu5hOyLoOuisOyEsSk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iVF9TRU5EIiBkYXRhLXRvPSJUX1JFQ1YiIGRhdGEtbGFiZWw9IuyYpOyngSAx6rCc7J2YIOq4uCAo64uo7J28IOyKpO2KuOumvCkiPgogIDxyZWN0IHg9IjE4Ni40MTAwMDAwMDAwMDAwMyIgeT0iMjExLjM1IiB3aWR0aD0iMTUxLjg5NDAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjYyLjM1NyIgeT0iMjI2LjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuyYpOyngSAx6rCc7J2YIOq4uCAo64uo7J28IOyKpO2KuOumvCk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iU19TRU5EIiBkYXRhLXRvPSJTX1JFQ1YiIGRhdGEtbGFiZWw9IuywqOyEoCAxICjsiqTtirjrprwgMSkiPgogIDxyZWN0IHg9IjIwNS43MTUiIHk9IjM5NS40MDAwMDAwMDAwMDAwMyIgd2lkdGg9IjkzLjA4ODAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjUyLjI1OTAwMDAwMDAwMDAxIiB5PSI0MTAuNTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuywqOyEoCAxICjsiqTtirjrprwgMSk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iU19TRU5EIiBkYXRhLXRvPSJTX1JFQ1YiIGRhdGEtbGFiZWw9IuywqOyEoCAyICjsiqTtirjrprwgMikiPgogIDxyZWN0IHg9IjIwMi4xNTEiIHk9IjM2Mi4xIiB3aWR0aD0iMTAwLjIxNjAwMDAwMDAwMDAxIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjUyLjI1OTAwMDAwMDAwMDAxIiB5PSIzNzcuMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuywqOyEoCAyICjsiqTtirjrprwgMik8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iU19TRU5EIiBkYXRhLXRvPSJTX1JFQ1YiIGRhdGEtbGFiZWw9IuywqOyEoCAzICjsmrDtmowg64+E66GcIO2ZleuztCkiPgogIDxyZWN0IHg9IjE4Ni40MSIgeT0iMzI4LjgiIHdpZHRoPSIxMzEuNjk4MDAwMDAwMDAwMDQiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyNTIuMjU5MDAwMDAwMDAwMDEiIHk9IjM0My45NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7LCo7ISgIDMgKOyasO2ajCDrj4TroZwg7ZmV67O0KTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iVV9TRU5EIiBkYXRhLWxhYmVsPSLshqHsi6DsnpAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iODYuNDEiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9Ijk5LjIwNSIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7shqHsi6DsnpA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlVfUkVDViIgZGF0YS1sYWJlbD0i7IiY7Iug7J6QIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM3Mi4yMDYiIHk9Ijg0IiB3aWR0aD0iODYuNDEiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQxNS40MTEiIHk9IjEwMi40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7IiY7Iug7J6QPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJUX1NFTkQiIGRhdGEtbGFiZWw9IuyGoeyLoOyekCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iMjA4LjkiIHdpZHRoPSI4Ni40MSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iOTkuMjA1IiB5PSIyMjcuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyGoeyLoOyekDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iVF9SRUNWIiBkYXRhLWxhYmVsPSLsiJjsi6DsnpAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzcyLjIwNiIgeT0iMjA4LjkiIHdpZHRoPSI4Ni40MSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDE1LjQxMSIgeT0iMjI3LjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7siJjsi6DsnpA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlNfU0VORCIgZGF0YS1sYWJlbD0i7Iah7Iug7J6QIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIzNTkuNjUiIHdpZHRoPSI4Ni40MSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI5OS4yMDUiIHk9IjM3OC4wOTk5OTk5OTk5OTk5NyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7Iah7Iug7J6QPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTX1JFQ1YiIGRhdGEtbGFiZWw9IuyImOyLoOyekCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzNzIuMjA2IiB5PSIzNTkuNjUiIHdpZHRoPSI4Ni40MSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0MTUuNDExIiB5PSIzNzguMDk5OTk5OTk5OTk5OTciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyImOyLoOyekDwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 통신의 판도를 바꾸는 SCTP의 2대 필살기 전격 비교 (3단 표 - 1순위)**

SCTP가 기존 TCP/UDP를 어떻게 밟고 일어섰는지, \*\*'멀티 호밍'\*\*과 \*\*'멀티 스트리밍'\*\*이라는 두 단어만 무조건 대조해서 암기하시면 됩니다.

| **통신 프로토콜**                                   | **데이터 전송 단위 (어떤 모양인가?)**                                                         | **핵심 특징 및 TCP 대비 결정적 차이 🚨**                                                                                                                                                                                                        |
| :-------------------------------------------- | :------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **UDP**                                       | **'데이터그램 (Datagram)'.** 데이터를 자르거나 붙이지 않고 던져주는 봉투 그대로 휙휙 던짐.                      | **\[신뢰성 제로 / 속도 몰빵]** 에러 복구도 안 하고(ARQ 없음), 흐름 제어도 안 함. 그냥 빨리 던지는 게 최고인 영상/음성 통화(VoIP)에 씀.                                                                                                                                           |
| **TCP**                                       | **'바이트 스트림 (Byte Stream)'.** 데이터를 1바이트씩 줄을 세워, 물 흐르듯 아주 좁은 '1차선 파이프' 하나로만 밀어 넣음. | **\[HOL Blocking (병목 현상)의 치명적 단점 ❌]** 1차선이라서 앞에 가는 패킷이 에러(유실)가 나면, 뒤에 따라오는 멀쩡한 패킷들도 앞차가 복구될 때까지 **전부 멈춰 서서 무한정 대기해야 하는 치명적 속도 저하 발생.**                                                                                              |
| **SCTP 👑** *(Stream Control* *Transmission)* | **'메시지 (Message)'.** TCP처럼 100% 도착(신뢰성)을 보장하면서도, 메시지 단위로 독립적으로 데이터를 잘라서 보냄.      | **\[SCTP의 2대 마법 💯]** ① **멀티 스트리밍(Multi-streaming):** 길을 4차선으로 뚫어 패킷을 병렬로 보냄. 1차선 앞차가 멈춰도 2, 3차선은 쌩쌩 지나가므로(HOL 문제 해결) 딜레이 제로! ② **멀티 호밍(Multi-homing):** 랜카드 2개(IP 2개)를 동시에 연결함. 메인 랜선이 끊어지면 0.1초 만에 예비 랜선으로 우회하여 **인터넷이 절대 안 끊김.** |

#### **IV. \[결론/제언] 차세대 웹 통신(HTTP/3)의 'QUIC' 프로토콜로 이어지는 계보**

* **(키워드 위주 2줄 마무리)** "SCTP는 다중 차선(Multi-streaming)이라는 완벽한 기술로 TCP의 고질적인 병목(HOL Blocking)을 해결했습니다. 비록 OS 지원 부족으로 대중화되진 못했지만, **SCTP의 이 위대한 '다중 차선 아이디어'는 그대로 구글이 개발한 차세대 통신 프로토콜 'QUIC (HTTP/3 기반)'으로 계승되어 현재 전 세계 모바일 웹의 속도를 지배하고 있습니다.**"
