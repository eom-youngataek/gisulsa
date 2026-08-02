### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (TCP의신뢰성보장원리) — 3~4줄
Ⅱ. 3-way handshake(연결) (본론①, 도식 1개 필수)
Ⅲ. 4-way handshake(종료) - 왜한번더필요한가 (본론②, 핵심 배점)
Ⅳ. 보안적함의 - SYN Flood와의연결
Ⅴ. 결론
```

### Ⅰ. 개요

TCP는 \*\*"신뢰성있는연결"\*\*을보장하는프로토콜입니다. 데이터를보내기전에 \*\*"양쪽다준비됐는지"\*\*를 확인하는절차가 3-wayhandshake이고, 끝낼때도 \*\*"양쪽다더보낼데이터가없는지"\*\*를 확인하는절차가 4-wayhandshake입니다.

### Ⅱ. 3-way handshake — 연결수립

| 단계    | 신호          | 의미                              |
| :---- | :---------- | :------------------------------ |
| **①** | **SYN**     | 클라이언트→서버: "연결하고싶다"(동기화요청)       |
| **②** | **SYN+ACK** | 서버→클라이언트: "알았다,나도준비됐다"(응답+동시요청) |
| **③** | **ACK**     | 클라이언트→서버: "확인했다"(최종확인)          |

→ 암기: **"요청,응답+역요청,확인"** — 3번을거쳐야 \*\*양쪽모두"상대가살아있고준비됐다"\*\*는걸 확신할수있습니다.

### 도식화 제안

```
[클라이언트]                    [서버]
    ──────SYN──────→
    ←────SYN+ACK────
    ──────ACK──────→
         (연결수립완료)
```

### Ⅲ. 4-way handshake — 연결종료, 핵심 배점

**함정 방지: "왜종료는4번인가"를 3-way와비교해서보여줘야완성됩니다.**

| 단계    | 신호      | 의미                             |
| :---- | :------ | :----------------------------- |
| **①** | **FIN** | A→B: "나는더보낼데이터없다"              |
| **②** | **ACK** | B→A: "알았다"(확인만, 아직B는데이터남았을수있음) |
| **③** | **FIN** | B→A: "나도이제더보낼데이터없다"            |
| **④** | **ACK** | A→B: "알았다,이제진짜끝"               |

→ 핵심차이: **연결은양쪽이 "동시에준비됨"을 SYN+ACK로한번에처리**할수있지만, **종료는 "한쪽이먼저끝내도 다른쪽은아직데이터가남아있을수있어"**, **ACK와FIN을분리**해야합니다 — 이것이 \*\*"3번vs4번"\*\*의 근본이유입니다.

### 도식화 제안

```
[A]                              [B]
────FIN───→  "나는끝났다"
←───ACK────  "확인"(B는아직데이터있을수있음)
                                (B가 나머지데이터전송,이후)
←───FIN────  "나도끝났다"
────ACK───→  "확인,완전종료"
```

### Ⅳ. 보안적함의 — SYN Flood와의연결

**함정 방지: "그냥프로토콜"로만끝내면절반. 앞서다룬DDoS답안과직결되는보안적의미를보여줘야완성됩니다.**

| 취약점                       | 내용                                                                              |
| :------------------------ | :------------------------------------------------------------------------------ |
| **SYN Flood**(앞서다룬DDoS유형) | 공격자가 **SYN만대량전송**하고 **ACK로응답하지않음**— 서버는 **"반개방연결"상태로계속대기**,자원소진                 |
| **반개방연결**(앞서다룬"SYN스캔")    | 앞서다룬 \*\*"네트워크스캐닝의SYN스캔"\*\*이바로 이 **3단계중①②만수행**하고 **③을생략**하는것 — 로그를최소화하며 포트상태확인 |

→ 앞서다룬 \*\*"DDoS의프로토콜공격"\*\*유형이 바로 \*\*"3-wayhandshake의①②까지만하고 ③을일부러안보내 서버자원을고갈시키는것"\*\*이라는 연결이 핵심입니다.

### 도식화 제안

```
[정상연결]                    [SYN Flood공격]
SYN→SYN+ACK→ACK              SYN→SYN+ACK→(ACK안보냄,반복)
(완전한3-way)                  (서버는계속반개방상태로대기,
                               자원고갈)
```

### Ⅴ. 결론

3-wayhandshake는 \*\*"연결시양쪽이동시에준비상태를확인"\*\*하는 효율적절차이고, 4-wayhandshake는 **"종료시한쪽만먼저끝내도 다른쪽데이터가안전하게전송되도록"** ACK와FIN을분리한 신중한절차입니다 — 이단순한프로토콜의구조가, 앞서다룬 **DDoS(SYNFlood)와네트워크스캐닝(SYN스캔)** 같은 오늘하루의여러공격기법의 **근본적인기술적기반**이 된다는 것을보여줍니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "택배를 무작정 문 앞에 던져두고 가는 것이 UDP라면, TCP는 방문 전에 '집에 계시나요?' 하고 확인한 뒤 물건을 주고, 끝날 때도 '저 이제 갑니다' 하고 인사까지 완벽하게 나누는 신사적이고 신뢰성 높은 프로토콜이다. 처음 통신을 시작하기 위해 서로 3번에 걸쳐 인사를 나누며 연결을 맺는 과정을 \*\*'3-Way Handshake'\*\*라고 한다. 클라이언트가 '통신하자!(SYN)'고 하면, 서버가 '어, 통신하자!(SYN+ACK)'고 응답하고, 클라이언트가 다시 '알았어!(ACK)'라며 확정 짓는 3단계다. 반대로 통신이 끝난 뒤 미련 없이 깔끔하게 헤어질 때는 4번의 인사가 필요한데 이를 \*\*'4-Way Handshake'\*\*라고 한다. 클라이언트가 먼저 '나 끊을게(FIN)' 하면, 서버가 '알았어, 잠깐만!(ACK)' 하고 자기가 아직 덜 보낸 데이터가 있는지 확인한다. 다 털어낸 후 서버도 '나도 끊을게(FIN)' 하면, 클라이언트가 '응, 잘 가(ACK)' 하고 종료하는 4단계의 완벽한 이별 과정이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 신뢰성 있는 통신의 시작과 끝, TCP Handshake 개요**

* **정의:** 전송 계층(Transport Layer)의 TCP 프로토콜이 통신의 신뢰성과 순서를 보장하기 위해, 논리적인 연결을 맺는 \*\*'3-Way Handshake (연결 수립)'\*\*와 통신을 안전하게 종료하는 **'4-Way Handshake (연결 종료)'** 과정.
* **핵심 제어 플래그 (Control Flag):**
  * `SYN` (Synchronize): "연결해 줘!" (시작 번호 동기화)
  * `ACK` (Acknowledgment): "알았어, 확인했어!" (응답/수락)
  * `FIN` (Finish): "나 이제 다 보냈어, 끊을게!" (종료)

#### **II. \[본론 1] (단순화 버전) 3-Way (연결) & 4-Way (종료) 파이프라인 (도식화)**

어떤 플래그가 날아가고 상태(State)가 어떻게 변하는지 직관적으로 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3MzAuNjMwMDAwMDAwMDAwMSA1OTgiIHdpZHRoPSI3MzAuNjMwMDAwMDAwMDAwMSIgaGVpZ2h0PSI1OTgiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0ic2VxLWFycm93IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI4IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9InNlcS1hcnJvdy1vcGVuIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI4IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5bGluZSBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGxpbmUgY2xhc3M9ImxpZmVsaW5lIiBkYXRhLWFjdG9yPSJDIiB4MT0iMzMzLjI0OTUwMDAwMDAwMDA3IiB5MT0iNzAiIHgyPSIzMzMuMjQ5NTAwMDAwMDAwMDciIHkyPSI1NjgiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1kYXNoYXJyYXk9IjYgNCIgLz4KPGxpbmUgY2xhc3M9ImxpZmVsaW5lIiBkYXRhLWFjdG9yPSJTIiB4MT0iNTA2LjQ5MzUwMDAwMDAwMDA0IiB5MT0iNzAiIHgyPSI1MDYuNDkzNTAwMDAwMDAwMDQiIHkyPSI1NjgiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1kYXNoYXJyYXk9IjYgNCIgLz4KPGcgY2xhc3M9Im1lc3NhZ2UiIGRhdGEtZnJvbT0iQyIgZGF0YS10bz0iUyIgZGF0YS1sYWJlbD0iMS4gU1lOICjrgpgg7Jew6rKw7ZW064+EIOuPvD8pIiBkYXRhLWxpbmUtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LWhlYWQ9ImZpbGxlZCIgZGF0YS1zZWxmPSJmYWxzZSI+CiAgPGxpbmUgeDE9IjMzMy4yNDk1MDAwMDAwMDAwNyIgeTE9IjkwIiB4Mj0iNTA2LjQ5MzUwMDAwMDAwMDA0IiB5Mj0iOTAiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjc2VxLWFycm93KSIgLz4KICA8dGV4dCB4PSI0MTkuODcxNTAwMDAwMDAwMSIgeT0iODAiIGZvbnQtc2l6ZT0iMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LW11dGVkKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+MS4gU1lOICjrgpgg7Jew6rKw7ZW064+EIOuPvD8pPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJtZXNzYWdlIiBkYXRhLWZyb209IlMiIGRhdGEtdG89IkMiIGRhdGEtbGFiZWw9IjIuIFNZTiArIEFDSyAo7Ja0IOuPvCEg64KY64+EIOyXsOqysO2VoOqyjCEpIiBkYXRhLWxpbmUtc3R5bGU9ImRhc2hlZCIgZGF0YS1hcnJvdy1oZWFkPSJmaWxsZWQiIGRhdGEtc2VsZj0iZmFsc2UiPgogIDxsaW5lIHgxPSI1MDYuNDkzNTAwMDAwMDAwMDQiIHkxPSIxNzIiIHgyPSIzMzMuMjQ5NTAwMDAwMDAwMDciIHkyPSIxNzIiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjYgNCIgbWFya2VyLWVuZD0idXJsKCNzZXEtYXJyb3cpIiAvPgogIDx0ZXh0IHg9IjQxOS44NzE1MDAwMDAwMDAxIiB5PSIxNjIiIGZvbnQtc2l6ZT0iMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LW11dGVkKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+Mi4gU1lOICsgQUNLICjslrQg64+8ISDrgpjrj4Qg7Jew6rKw7ZWg6rKMISk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im1lc3NhZ2UiIGRhdGEtZnJvbT0iQyIgZGF0YS10bz0iUyIgZGF0YS1sYWJlbD0iMy4gQUNLICjslYzslZjslrQhIOydtOygnCDrjbDsnbTthLAg67O064K464ukISkiIGRhdGEtbGluZS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctaGVhZD0iZmlsbGVkIiBkYXRhLXNlbGY9ImZhbHNlIj4KICA8bGluZSB4MT0iMzMzLjI0OTUwMDAwMDAwMDA3IiB5MT0iMjEyIiB4Mj0iNTA2LjQ5MzUwMDAwMDAwMDA0IiB5Mj0iMjEyIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI3NlcS1hcnJvdykiIC8+CiAgPHRleHQgeD0iNDE5Ljg3MTUwMDAwMDAwMDEiIHk9IjIwMiIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtbXV0ZWQpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij4zLiBBQ0sgKOyVjOyVmOyWtCEg7J207KCcIOuNsOydtO2EsCDrs7Trgrjri6QhKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibWVzc2FnZSIgZGF0YS1mcm9tPSJDIiBkYXRhLXRvPSJTIiBkYXRhLWxhYmVsPSIxLiBGSU4gKOuCmCDsnbTsoJwg642w7J207YSwIOuLpCDsjbzslrQuIOuBiuydhOqyjCEpIiBkYXRhLWxpbmUtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LWhlYWQ9ImZpbGxlZCIgZGF0YS1zZWxmPSJmYWxzZSI+CiAgPGxpbmUgeDE9IjMzMy4yNDk1MDAwMDAwMDAwNyIgeTE9IjI5NCIgeDI9IjUwNi40OTM1MDAwMDAwMDAwNCIgeTI9IjI5NCIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNzZXEtYXJyb3cpIiAvPgogIDx0ZXh0IHg9IjQxOS44NzE1MDAwMDAwMDAxIiB5PSIyODQiIGZvbnQtc2l6ZT0iMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LW11dGVkKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+MS4gRklOICjrgpgg7J207KCcIOuNsOydtO2EsCDri6Qg7I287Ja0LiDrgYrsnYTqsowhKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibWVzc2FnZSIgZGF0YS1mcm9tPSJTIiBkYXRhLXRvPSJDIiBkYXRhLWxhYmVsPSIyLiBBQ0sgKOyWtCDslYzslZjslrQuIOyVhOyngSDrgqjsnYDqsbAg7J6I64KYIO2ZleyduCDrjIDquLAhKSIgZGF0YS1saW5lLXN0eWxlPSJkYXNoZWQiIGRhdGEtYXJyb3ctaGVhZD0iZmlsbGVkIiBkYXRhLXNlbGY9ImZhbHNlIj4KICA8bGluZSB4MT0iNTA2LjQ5MzUwMDAwMDAwMDA0IiB5MT0iMzQ5IiB4Mj0iMzMzLjI0OTUwMDAwMDAwMDA3IiB5Mj0iMzQ5IiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI2IDQiIG1hcmtlci1lbmQ9InVybCgjc2VxLWFycm93KSIgLz4KICA8dGV4dCB4PSI0MTkuODcxNTAwMDAwMDAwMSIgeT0iMzM5IiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1tdXRlZCkiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjIuIEFDSyAo7Ja0IOyVjOyVmOyWtC4g7JWE7KeBIOuCqOydgOqxsCDsnojrgpgg7ZmV7J24IOuMgOq4sCEpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJtZXNzYWdlIiBkYXRhLWZyb209IlMiIGRhdGEtdG89IkMiIGRhdGEtbGFiZWw9IjMuIEZJTiAo7ZmV7J24IOuBneuCrOyWtCwg64KY64+EIOydtOygnCDrgYrsnYTqsowhKSIgZGF0YS1saW5lLXN0eWxlPSJkYXNoZWQiIGRhdGEtYXJyb3ctaGVhZD0iZmlsbGVkIiBkYXRhLXNlbGY9ImZhbHNlIj4KICA8bGluZSB4MT0iNTA2LjQ5MzUwMDAwMDAwMDA0IiB5MT0iNDMxIiB4Mj0iMzMzLjI0OTUwMDAwMDAwMDA3IiB5Mj0iNDMxIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI2IDQiIG1hcmtlci1lbmQ9InVybCgjc2VxLWFycm93KSIgLz4KICA8dGV4dCB4PSI0MTkuODcxNTAwMDAwMDAwMSIgeT0iNDIxIiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1tdXRlZCkiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjMuIEZJTiAo7ZmV7J24IOuBneuCrOyWtCwg64KY64+EIOydtOygnCDrgYrsnYTqsowhKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibWVzc2FnZSIgZGF0YS1mcm9tPSJDIiBkYXRhLXRvPSJTIiBkYXRhLWxhYmVsPSI0LiBBQ0sgKOyVjOyVmOyWtCDslYjrhZUhKSIgZGF0YS1saW5lLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1oZWFkPSJmaWxsZWQiIGRhdGEtc2VsZj0iZmFsc2UiPgogIDxsaW5lIHgxPSIzMzMuMjQ5NTAwMDAwMDAwMDciIHkxPSI0ODYiIHgyPSI1MDYuNDkzNTAwMDAwMDAwMDQiIHkyPSI0ODYiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjc2VxLWFycm93KSIgLz4KICA8dGV4dCB4PSI0MTkuODcxNTAwMDAwMDAwMSIgeT0iNDc2IiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1tdXRlZCkiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjQuIEFDSyAo7JWM7JWY7Ja0IOyViOuFlSEpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub3RlIiBkYXRhLXBvc2l0aW9uPSJsZWZ0IiBkYXRhLWFjdG9ycz0iQyI+CiAgPHBvbHlnb24gcG9pbnRzPSIxNDEuMDc4MDAwMDAwMDAwMSw5OCAyNDIuMTA2MDAwMDAwMDAwMSw5OCAyNDguMTA2MDAwMDAwMDAwMSwxMDQgMjQ4LjEwNjAwMDAwMDAwMDEsMTIxIDE0MS4wNzgwMDAwMDAwMDAxLDEyMSIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8cG9seWdvbiBwb2ludHM9IjI0Mi4xMDYwMDAwMDAwMDAxLDk4IDI0OC4xMDYwMDAwMDAwMDAxLDEwNCAyNDIuMTA2MDAwMDAwMDAwMSwxMDQiIGZpbGw9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxOTQuNTkyMDAwMDAwMDAwMSIgeT0iMTA5LjUiIGZvbnQtc2l6ZT0iMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LW11dGVkKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+U1lOX1NFTlQg7IOB7YOcPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub3RlIiBkYXRhLXBvc2l0aW9uPSJyaWdodCIgZGF0YS1hY3RvcnM9IlMiPgogIDxwb2x5Z29uIHBvaW50cz0iNTc0LjU5NCwxMjUgNjc1LjYyMjAwMDAwMDAwMDEsMTI1IDY4MS42MjIwMDAwMDAwMDAxLDEzMSA2ODEuNjIyMDAwMDAwMDAwMSwxNDggNTc0LjU5NCwxNDgiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHBvbHlnb24gcG9pbnRzPSI2NzUuNjIyMDAwMDAwMDAwMSwxMjUgNjgxLjYyMjAwMDAwMDAwMDEsMTMxIDY3NS42MjIwMDAwMDAwMDAxLDEzMSIgZmlsbD0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjYyOC4xMDgwMDAwMDAwMDAxIiB5PSIxMzYuNSIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtbXV0ZWQpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5TWU5fUkNWRCDsg4Htg5w8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vdGUiIGRhdGEtcG9zaXRpb249Im92ZXIiIGRhdGEtYWN0b3JzPSJDLFMiPgogIDxwb2x5Z29uIHBvaW50cz0iMjk1LjM3NDUwMDAwMDAwMDEsMjIwIDUzOC4zNjg1LDIyMCA1NDQuMzY4NSwyMjYgNTQ0LjM2ODUsMjQzIDI5NS4zNzQ1MDAwMDAwMDAxLDI0MyIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8cG9seWdvbiBwb2ludHM9IjUzOC4zNjg1LDIyMCA1NDQuMzY4NSwyMjYgNTM4LjM2ODUsMjI2IiBmaWxsPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDE5Ljg3MTUwMDAwMDAwMDEiIHk9IjIzMS41IiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1tdXRlZCkiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPvCfn6IgRVNUQUJMSVNIRUQgKOyXsOqysCDsmYTro4whIOuNsOydtO2EsCDshqHsiJjsi6Ag8J+foik8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vdGUiIGRhdGEtcG9zaXRpb249Im92ZXIiIGRhdGEtYWN0b3JzPSJDLFMiPgogIDxwb2x5Z29uIHBvaW50cz0iMzA1LjE3NTUwMDAwMDAwMDA2LDI0NyA1MjguNTY3NTAwMDAwMDAwMSwyNDcgNTM0LjU2NzUwMDAwMDAwMDEsMjUzIDUzNC41Njc1MDAwMDAwMDAxLDI3MCAzMDUuMTc1NTAwMDAwMDAwMDYsMjcwIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDxwb2x5Z29uIHBvaW50cz0iNTI4LjU2NzUwMDAwMDAwMDEsMjQ3IDUzNC41Njc1MDAwMDAwMDAxLDI1MyA1MjguNTY3NTAwMDAwMDAwMSwyNTMiIGZpbGw9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0MTkuODcxNTAwMDAwMDAwMSIgeT0iMjU4LjUiIGZvbnQtc2l6ZT0iMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LW11dGVkKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+4pyoIDIuIFRDUCA0LVdheSBIYW5kc2hha2UgKOyXsOqysCDsooXro4wpIOKcqDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm90ZSIgZGF0YS1wb3NpdGlvbj0ibGVmdCIgZGF0YS1hY3RvcnM9IkMiPgogIDxwb2x5Z29uIHBvaW50cz0iMTQwLjQ4NDAwMDAwMDAwMDA3LDMwMiAyNDIuMTA2MDAwMDAwMDAwMDgsMzAyIDI0OC4xMDYwMDAwMDAwMDAwOCwzMDggMjQ4LjEwNjAwMDAwMDAwMDA4LDMyNSAxNDAuNDg0MDAwMDAwMDAwMDcsMzI1IiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDxwb2x5Z29uIHBvaW50cz0iMjQyLjEwNjAwMDAwMDAwMDA4LDMwMiAyNDguMTA2MDAwMDAwMDAwMDgsMzA4IDI0Mi4xMDYwMDAwMDAwMDAwOCwzMDgiIGZpbGw9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxOTQuMjk1MDAwMDAwMDAwMDciIHk9IjMxMy41IiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1tdXRlZCkiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPkZJTl9XQUlUXzEg7IOB7YOcPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub3RlIiBkYXRhLXBvc2l0aW9uPSJyaWdodCIgZGF0YS1hY3RvcnM9IlMiPgogIDxwb2x5Z29uIHBvaW50cz0iNTc0LjU5NCwzNTcgNjk0LjYzMDAwMDAwMDAwMDEsMzU3IDcwMC42MzAwMDAwMDAwMDAxLDM2MyA3MDAuNjMwMDAwMDAwMDAwMSwzODAgNTc0LjU5NCwzODAiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHBvbHlnb24gcG9pbnRzPSI2OTQuNjMwMDAwMDAwMDAwMSwzNTcgNzAwLjYzMDAwMDAwMDAwMDEsMzYzIDY5NC42MzAwMDAwMDAwMDAxLDM2MyIgZmlsbD0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjYzNy42MTIwMDAwMDAwMDAxIiB5PSIzNjguNSIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtbXV0ZWQpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5DTE9TRV9XQUlUIOyDge2DnCDij7M8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vdGUiIGRhdGEtcG9zaXRpb249ImxlZnQiIGRhdGEtYWN0b3JzPSJDIj4KICA8cG9seWdvbiBwb2ludHM9IjExMS4zNzgwMDAwMDAwMDAwNCwzODQgMjQyLjEwNjAwMDAwMDAwMDA4LDM4NCAyNDguMTA2MDAwMDAwMDAwMDgsMzkwIDI0OC4xMDYwMDAwMDAwMDAwOCw0MDcgMTExLjM3ODAwMDAwMDAwMDA0LDQwNyIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8cG9seWdvbiBwb2ludHM9IjI0Mi4xMDYwMDAwMDAwMDAwOCwzODQgMjQ4LjEwNjAwMDAwMDAwMDA4LDM5MCAyNDIuMTA2MDAwMDAwMDAwMDgsMzkwIiBmaWxsPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTc5Ljc0MjAwMDAwMDAwMDA4IiB5PSIzOTUuNSIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtbXV0ZWQpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5GSU5fV0FJVF8yIOyDge2DnCDrjIDquLA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vdGUiIGRhdGEtcG9zaXRpb249InJpZ2h0IiBkYXRhLWFjdG9ycz0iUyI+CiAgPHBvbHlnb24gcG9pbnRzPSI1NzQuNTk0LDQzOSA2NzUuNjIyMDAwMDAwMDAwMSw0MzkgNjgxLjYyMjAwMDAwMDAwMDEsNDQ1IDY4MS42MjIwMDAwMDAwMDAxLDQ2MiA1NzQuNTk0LDQ2MiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8cG9seWdvbiBwb2ludHM9IjY3NS42MjIwMDAwMDAwMDAxLDQzOSA2ODEuNjIyMDAwMDAwMDAwMSw0NDUgNjc1LjYyMjAwMDAwMDAwMDEsNDQ1IiBmaWxsPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNjI4LjEwODAwMDAwMDAwMDEiIHk9IjQ1MC41IiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1tdXRlZCkiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPkxBU1RfQUNLIOyDge2DnDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm90ZSIgZGF0YS1wb3NpdGlvbj0ibGVmdCIgZGF0YS1hY3RvcnM9IkMiPgogIDxwb2x5Z29uIHBvaW50cz0iMzAsNDk0IDI0Mi4xMDYwMDAwMDAwMDAwOCw0OTQgMjQ4LjEwNjAwMDAwMDAwMDA4LDUwMCAyNDguMTA2MDAwMDAwMDAwMDgsNTE3IDMwLDUxNyIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8cG9seWdvbiBwb2ludHM9IjI0Mi4xMDYwMDAwMDAwMDAwOCw0OTQgMjQ4LjEwNjAwMDAwMDAwMDA4LDUwMCAyNDIuMTA2MDAwMDAwMDAwMDgsNTAwIiBmaWxsPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTM5LjA1MzAwMDAwMDAwMDA1IiB5PSI1MDUuNSIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtbXV0ZWQpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7wn5qoIFRJTUVfV0FJVCAo7KeA7JewIO2MqO2CtyDrjIDruYQg64yA6riwKSDwn5qoPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub3RlIiBkYXRhLXBvc2l0aW9uPSJvdmVyIiBkYXRhLWFjdG9ycz0iQyxTIj4KICA8cG9seWdvbiBwb2ludHM9IjMzMC43MTc1MDAwMDAwMDAxLDUyMSA1MDMuMDI1NTAwMDAwMDAwMTQsNTIxIDUwOS4wMjU1MDAwMDAwMDAxNCw1MjcgNTA5LjAyNTUwMDAwMDAwMDE0LDU0NCAzMzAuNzE3NTAwMDAwMDAwMSw1NDQiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHBvbHlnb24gcG9pbnRzPSI1MDMuMDI1NTAwMDAwMDAwMTQsNTIxIDUwOS4wMjU1MDAwMDAwMDAxNCw1MjcgNTAzLjAyNTUwMDAwMDAwMDE0LDUyNyIgZmlsbD0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQxOS44NzE1MDAwMDAwMDAxIiB5PSI1MzIuNSIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtbXV0ZWQpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7inYwgQ0xPU0VEICjsl7DqsrAg7JmE7KCEIOyiheujjCDinYwpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJhY3RvciIgZGF0YS1pZD0iQyIgZGF0YS1sYWJlbD0i7YG065287J207Ja47Yq4IChDbGllbnQpIiBkYXRhLXR5cGU9InBhcnRpY2lwYW50Ij4KICA8cmVjdCB4PSIyNTguMTA2MDAwMDAwMDAwMDUiIHk9IjMwIiB3aWR0aD0iMTUwLjI4NyIgaGVpZ2h0PSI0MCIgcng9IjQiIHJ5PSI0IiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzMzLjI0OTUwMDAwMDAwMDA3IiB5PSI1MCIgZm9udC1zaXplPSIxMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7YG065287J207Ja47Yq4IChDbGllbnQpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJhY3RvciIgZGF0YS1pZD0iUyIgZGF0YS1sYWJlbD0i7ISc67KEIChTZXJ2ZXIpIiBkYXRhLXR5cGU9InBhcnRpY2lwYW50Ij4KICA8cmVjdCB4PSI0NDguMzkzMDAwMDAwMDAwMDMiIHk9IjMwIiB3aWR0aD0iMTE2LjIwMTAwMDAwMDAwMDAxIiBoZWlnaHQ9IjQwIiByeD0iNCIgcnk9IjQiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MDYuNDkzNTAwMDAwMDAwMDQiIHk9IjUwIiBmb250LXNpemU9IjEzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7shJzrsoQgKFNlcnZlcik8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 연결 수립(3-Way)과 종료(4-Way)의 핵심 동작 메커니즘 전격 해부 (3단 표)**

가장 중요한 출제 포인트인 각 과정에서의 **핵심 동작과, 발생할 수 있는 보안 취약점**을 대조해야 합니다.

| **TCP 동작 과정**                    | **핵심 동작 메커니즘 및 핑퐁(Ping-Pong) 순서**                                                                                           | **핵심 상태(State) 및 보안적 시사점 🚨**                                                                                                                 |
| :------------------------------- | :-------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| **3-Way Handshake** *(연결 수립 과정)* | **'3번의 인사를 통한 양방향 통신로 개척'.** ① 클라이언트 ➔ 서버 `(SYN)` ② 서버 ➔ 클라이언트 `(SYN + ACK)` ③ 클라이언트 ➔ 서버 `(ACK)` 이 과정이 끝나야 데이터를 주고받을 수 있음. | **\[SYN Flooding 공격의 표적 💣]** 해커가 가짜 IP로 1단계 `SYN`만 무한대로 보내고 3단계 `ACK`를 안 주면, 서버는 \*\*'SYN\_RCVD(반쯤 열린 상태)'\*\*로 멍하니 기다리다 자원이 고갈되어 다운됨(DDoS). |
| **4-Way Handshake** *(연결 종료 과정)* | **'남은 데이터를 버리지 않기 위한 4번의 작별 인사'.** ① 클라이언트 ➔ 서버 `(FIN)` ② 서버 ➔ 클라이언트 `(ACK)` ③ 서버 ➔ 클라이언트 `(FIN)` ④ 클라이언트 ➔ 서버 `(ACK)`      | **\[TIME\_WAIT 상태의 중요성 💯]** 마지막 4단계에서 클라이언트는 연결을 바로 끊지 않고 약 1~2분간 **`TIME_WAIT`** **상태**로 대기함. 혹시 늦게 도착하는 데이터(지연 패킷)가 유실되는 것을 막기 위함.         |
| **(참고) 4단계에서 서버의 CLOSE\_WAIT**   | 2단계와 3단계 사이에서 서버가 머무는 상태. \*\*'클라이언트가 끊자고 했지만, 나는 혹시 덜 보낸 데이터가 남아있는지 확인하고 처리하는 시간'\*\*임.                                    | 이 상태가 너무 많이 쌓이면, 서버 애플리케이션(개발자 코드)이 소켓(Socket)을 제대로 안 닫아준다는 치명적인 버그(누수)를 의미함.                                                                 |

#### **IV. \[결론/제언] TCP의 무거운 오버헤드를 극복하기 위한 'QUIC(UDP)' 프로토콜로의 진화**

* **(키워드 위주 2줄 마무리)** "TCP 3-Way Handshake는 완벽한 신뢰성을 보장하지만, 통신을 시작할 때마다 인사를 나누느라 왕복 시간(RTT, Round Trip Time)을 낭비하는 무거운 오버헤드(단점)를 가집니다. 이를 극복하기 위해 최근 구글과 HTTP/3는 TCP의 인사를 생략하고 **가벼운 UDP 기반 위에 자체적인 신뢰성을 얹은 'QUIC(Quick UDP Internet Connections)' 프로토콜을 도입하여 모바일 웹의 속도를 혁신적으로 끌어올리고 있습니다.**"
