### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (3대주소체계, 계층별역할분담) — 3~4줄
Ⅱ. MAC주소구조 (본론①, 도식 1개 필수)
Ⅲ. IP주소구조 (본론②, 핵심 배점)
Ⅳ. Port주소구조 및 종합연결
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬ARP스푸핑은 'IP에대응하는MAC주소'를속였고, IP스푸핑은 '발신지IP주소'를속였다 — 이두공격이서로다른것은, 애초에MAC과IP가서로다른계층에서, 서로다른역할을하기때문"\*\*이라는한줄로시작하면, 오늘의답안이 왜필요한지 명확해집니다.

### Ⅱ. MAC주소구조 — "물리적기기의고유번호"

| 항목     | 내용                                                        |
| :----- | :-------------------------------------------------------- |
| **계층** | **2계층(데이터링크계층)**                                          |
| **크기** | **48비트(6바이트)**,16진수로표현(예:00:1A:2B:3C:4D:5E)               |
| **구조** | 앞 **24비트=OUI**(제조사식별코드,IEEE가발급) + 뒤 **24비트=일련번호**(제조사가부여) |
| **범위** | **같은네트워크(LAN)안에서만유효**— 라우터를넘어가면 사라짐                       |

→ 암기: **"앞은누가만들었는지,뒤는몇번째제품인지"** — 앞서다룬 **ARP스푸핑**이 **"IP에대응하는MAC을거짓으로알려주는"** 공격이었던 이유는, MAC주소가 \*\*"같은LAN안에서기기를최종적으로찾아가는 물리적주소"\*\*이기때문입니다.

### 도식화 제안

```
[MAC주소: 48비트]
00:1A:2B : 3C:4D:5E
└──OUI──┘ └일련번호┘
(제조사식별)  (제품고유번호)

→ LAN(로컬망) 안에서만 유효, 라우터를넘으면 의미없음
```

### Ⅲ. IP주소구조 — "논리적위치주소", 핵심 배점

**함정 방지: "그냥주소"라고만답하면절반. IPv4/IPv6구조와, 왜MAC과다른"논리적"주소인지보여줘야완성됩니다.**

| 버전       | 크기        | 구조                                        |
| :------- | :-------- | :---------------------------------------- |
| **IPv4** | **32비트**  | **네트워크부분+호스트부분**(서브넷마스크로구분),예:192.168.1.1 |
| **IPv6** | **128비트** | IPv4주소고갈해결,예:2001:0db8::1                 |

**IPv4의네트워크/호스트분할**

| 클래스        | 구조                            |
| :--------- | :---------------------------- |
| **네트워크주소** | "어느네트워크에속하는가"(예:192.168.1.0)  |
| **호스트주소**  | "그네트워크안에서몇번째기기인가"(예:.1,.2...) |

→ 암기: **"MAC은물리적으로고정된주소,IP는네트워크구조에따라 논리적으로부여되는주소"** — 앞서다룬 **IP스푸핑**이 \*\*"발신지IP를속인다"\*\*고했는데, 이것이가능한이유는 \*\*IP가MAC과달리 '소프트웨어적으로설정가능한논리적값'\*\*이기때문입니다.

### 도식화 제안

```
[IPv4: 192.168.1.100/24]
192.168.1 . 100
└─네트워크(24비트)─┘└호스트(8비트)┘
"어느집단인가"      "그집단내몇번째인가"

[MAC vs IP 비교]
MAC: 물리적,공장에서고정,LAN내에서만유효
IP : 논리적,설정가능,라우터넘어인터넷전체에서유효
```

### Ⅳ. Port주소구조 및 종합연결

**함정 방지: "포트는프로그램구분"이라고만하면절반. 범위별분류와, 앞서다룬TCP핸드셰이크와의연결을보여줘야완성됩니다.**

| 항목       | 내용                                                                                              |
| :------- | :---------------------------------------------------------------------------------------------- |
| **계층**   | **4계층(전송계층)**                                                                                   |
| **크기**   | **16비트**(0\~65535)                                                                              |
| **범위분류** | **WellKnown(0\~1023,표준서비스)**,**Registered(1024\~49151)**,**Dynamic/Private(49152\~65535,임시할당)** |

→ 암기: **"MAC은'어느기기',IP는'어느네트워크위치',Port는'그기기안의어느프로그램'"** — 앞서다룬 **TCP3-wayhandshake**가 **"IP:Port"** 조합(소켓)단위로 연결을식별한다는것이, 이답안과 직접연결됩니다.

### 도식화 제안

```
[OSI 계층별 주소체계]
2계층(데이터링크): MAC주소 → "같은LAN안의물리적기기"
3계층(네트워크):   IP주소  → "인터넷전체에서의논리적위치"
4계층(전송):      Port주소 → "그기기안의어느프로그램/서비스"

[전체통신흐름]
[클라이언트: IP-A, Port-5000] ──→ [서버: IP-B, Port-80(HTTP)]
   ↓LAN내에서는
[MAC-A] ──ARP로 IP-B에해당하는 MAC알아냄──→ [MAC-B]
```

### Ⅴ. 결론

MAC,IP,Port는 \*\*"물리적기기식별(2계층)→논리적위치식별(3계층)→프로그램식별(4계층)"\*\*로 이어지는 **계층적주소체계**입니다 — 앞서다룬 \*\*ARP스푸핑(MAC위조),IP스푸핑(IP위조)\*\*이 서로다른공격으로분류되는이유가, 바로이 \*\*"각계층마다역할이다른주소를각각공격한것"\*\*이기때문임을 보여줍니다 — 이는 오늘하루다룬 **TCP핸드셰이크,ARQ,혼잡제어,QoS**등 모든네트워크시리즈가 결국 **"IP:Port로식별된연결위에서, MAC으로실제기기를찾아가는"** 이주소체계기반위에서 작동한다는 것을 확인시켜줍니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "내가 친구에게 택배를 보낼 때를 상상해 보자. 택배 배달이 꼬이지 않으려면 3가지 주소가 완벽하게 맞물려야 한다. 첫째, 친구 집의 '아파트 도로명 주소'가 필요하다. 인터넷 세상에서 내 컴퓨터의 위치를 알려주는 논리적 주소가 \*\*'IP 주소(3계층)'\*\*다. 이사를 가면 주소가 바뀌듯, 내가 카페로 이동해 와이파이를 잡으면 IP 주소도 바뀐다. 둘째, 아파트에 도착했는데 동명이인이 있을 수 있다. 절대 변하지 않는 친구의 '주민등록번호(지문)'가 필요한데, 이것이 랜카드 공장에서 찍혀 나오는 물리적 주소인 \*\*'MAC 주소(2계층)'\*\*다. 평생 바뀌지 않는다. 셋째, 친구 집에 택배가 무사히 도착했는데, 그걸 뜯을 사람이 친구인지 동생인지 정해야 한다. 내 컴퓨터 안에도 카톡, 유튜브, 게임 등 수많은 프로그램이 켜져 있는데, 데이터가 어떤 프로그램의 문을 열고 들어가야 할지 지정해 주는 방문 번호가 바로 \*\*'Port 주소(4계층)'\*\*다. 이 3박자가 맞아야 통신이 완성된다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 데이터 배달을 완성하는 네트워크 3대 식별자 개요**

* **IP 주소 (Internet Protocol Address):** 인터넷망 전체에서 길(라우팅 경로)을 찾기 위해 부여된 가변적인 논리 주소 (아파트 주소).
* **MAC 주소 (Media Access Control Address):** 같은 로컬 네트워크(공유기 등) 안에서 정확한 단말기 기계를 식별하기 위해 랜카드(NIC) 하드웨어에 새겨진 불변의 물리 주소 (주민번호).
* **Port 주소 (포트 번호):** 컴퓨터에 무사히 도착한 데이터가, 내부에서 실행 중인 여러 '소프트웨어(프로세스)' 중 누구에게 전달되어야 하는지 식별하는 논리적 채널 번호 (방 번호).

#### **II. \[본론 1] (극단적 단순화 버전) 3대 주소를 거쳐 데이터가 도착하는 파이프라인**

복잡한 OSI 7계층 선을 빼고, **인터넷 ➔ 내 컴퓨터 ➔ 내 프로그램**으로 들어가는 직관적 흐름만 그렸습니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MDYuNTA3MDAwMDAwMDAwMSAyMTAuNyIgd2lkdGg9IjgwNi41MDcwMDAwMDAwMDAxIiBoZWlnaHQ9IjIxMC43IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfX18zX18iIGRhdGEtbGFiZWw9IuuNsOydtO2EsCDrsLDri6wg6rO87KCV7J2YIDPri6jqs4Qg7KO87IaMIO2ZleyduCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNzI2LjUwNzAwMDAwMDAwMDEiIGhlaWdodD0iMTMwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI3MjYuNTA3MDAwMDAwMDAwMSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPuuNsOydtO2EsCDrsLDri6wg6rO87KCV7J2YIDPri6jqs4Qg7KO87IaMIO2ZleyduDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iSVAiIGRhdGEtdG89Ik1BQyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7J247YSw64S37J2EIOqxtOuEiOyZgOyEnCIgcG9pbnRzPSIyMjAuOTU2MDAwMDAwMDAwMDIsMTE5LjM1IDQyMy40MjgwMDAwMDAwMDAwNSwxMTkuMzUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209Ik1BQyIgZGF0YS10bz0iUE9SVCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7Lu07ZOo7YSwIOyViOyXkOyEnCIgcG9pbnRzPSI0OTQuMjc3MDAwMDAwMDAwMDQsMTE5LjM1IDY3Mi45ODksMTE5LjM1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IklQIiBkYXRhLXRvPSJNQUMiIGRhdGEtbGFiZWw9IuyduO2EsOuEt+ydhCDqsbTrhIjsmYDshJwiPgogIDxyZWN0IHg9IjI2NC45NTYiIHk9IjEwMy4zNSIgd2lkdGg9IjExNC40NzIwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjMyMi4xOTIiIHk9IjExOC41IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7snbjthLDrhLfsnYQg6rG064SI7JmA7IScPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209Ik1BQyIgZGF0YS10bz0iUE9SVCIgZGF0YS1sYWJlbD0i7Lu07ZOo7YSwIOyViOyXkOyEnCI+CiAgPHJlY3QgeD0iNTM4LjI3NyIgeT0iMTAzLjM1IiB3aWR0aD0iOTAuNzEyMDAwMDAwMDAwMDIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1ODMuNjMzIiB5PSIxMTguNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7Lu07ZOo7YSwIOyViOyXkOyEnDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iSVAiIGRhdGEtbGFiZWw9IjEuIElQIOyjvOyGjCAoM+qzhOy4tSkg8J+MjQrslYTtjIztirgg64+E66Gc66qFIOyjvOyGjAoxOTIuMTY4LjAuMTAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMTY0Ljk1NjAwMDAwMDAwMDAyIiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxMzguNDc4IiB5PSIxMTkuMzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjEzOC40NzgiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj4xLiBJUCDso7zshowgKDPqs4TsuLUpIPCfjI08L3RzcGFuPjx0c3BhbiB4PSIxMzguNDc4IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7slYTtjIztirgg64+E66Gc66qFIOyjvOyGjDwvdHNwYW4+PHRzcGFuIHg9IjEzOC40NzgiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPjE5Mi4xNjguMC4xMDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJNQUMiIGRhdGEtbGFiZWw9Ik1BQyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MjMuNDI4MDAwMDAwMDAwMDUiIHk9IjEwMC45IiB3aWR0aD0iNzAuODQ5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjQ1OC44NTI1MDAwMDAwMDAxIiB5PSIxMTkuMzUwMDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk1BQzwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUE9SVCIgZGF0YS1sYWJlbD0iUE9SVCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI2NzIuOTg5IiB5PSIxMDAuOSIgd2lkdGg9Ijc3LjUxOCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI3MTEuNzQ4IiB5PSIxMTkuMzUwMDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlBPUlQ8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] OSI 계층별 3대 주소의 구조 및 핵심 특성 전격 대조 (3단 표 - 1순위)**

각 주소가 **'총 몇 비트(Bit)인지'**, 그리고 \*\*'구조가 어떻게 반으로 나뉘는지'\*\*를 명확히 대조하는 것이 핵심입니다.

| **핵심 척도 (비교 잣대)**            | **🌍 IP 주소 (IPv4 기준)**                                                                      | **💻 MAC 주소**                                                                                          | **🚪 Port 주소**                                                                                      |
| :--------------------------- | :------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| **OSI 동작 계층 및 부여(변경)의 성격**   | **\[네트워크 계층 / 3계층]** 논리적 주소. 장소를 이동하거나 다른 와이파이를 잡으면 주소가 맘대로 바뀜(가변적).                        | **\[데이터링크 계층 / 2계층]** 물리적 하드웨어 주소. 랜카드(NIC) 칩셋에 각인되어 나와서 죽을 때까지 평생 안 바뀜(불변).                           | **\[전송 계층 / 4계층]** 서비스 식별 번호. 실행 중인 소프트웨어(프로세스)마다 부여되는 채널 번호.                                       |
| **주소의 총 길이(Bit) 및 표기 방식**    | **'총 32비트 (4바이트)'.** 8비트씩 4개의 덩어리로 나누고 10진수로 표기함. *(예: 192.168.0.1)*                        | **'총 48비트 (6바이트)'.** 8비트씩 6개의 덩어리로 나누고 16진수로 표기함. *(예: 00:1A:2B:3C:4D:5E)*                             | **'총 16비트 (2바이트)'.** 총 0번부터 65535번까지의 십진수 방 번호로 존재함. *(예: Port 80, 443)*                            |
| **주소 구조의 분할 특징 🚨 (무조건 출제)** | **\[네트워크 ID + 호스트 ID]** 앞부분은 속해있는 동네(네트워크 대역)를 뜻하고, 뒷부분은 그 동네의 개별 PC 번호를 뜻함. (서브넷 마스크로 구분). | **\[제조사 번호(OUI) + 일련번호(UAA)]** 앞 24비트는 랜카드를 만든 '제조사 고유번호(삼성, 인텔 등)'이고, 뒤 24비트는 해당 공장에서 찍어낸 '기기 일련번호'임. | **\[잘 알려진 포트 + 동적 포트]** `0~1023`번은 HTTP(80)처럼 세계적으로 약속된 고정 방(Well-known)이고, 나머지는 클라이언트가 막 쓰는 임시 방임. |
| **주소를 변환해 주는 핵심 연결 프로토콜**    | 영문 도메인명([www.naver.com)을](http://www.naver.xn--com\)-jy1s/) IP 주소로 바꿔주는 것은 **'DNS'** 프로토콜.  | IP 주소를 알고 있을 때 그 기계의 MAC 주소를 물어봐서 찾아주는 것은 **'ARP'** 프로토콜.                                              | (IP와 Port 번호를 콜론으로 묶어서 '소켓(Socket, 예: 192.168.0.1:80)' 형태로 씀).                                      |

#### **IV. \[결론/제언] 주소 고갈 문제의 극복과 차세대 주소 체계(IPv6)로의 마이그레이션**

* **(키워드 위주 2줄 마무리)** "IP, MAC, Port가 유기적으로 엮인 3단계 주소 체계는 현재의 인터넷을 만들었지만, 32비트의 IPv4 체계는 폭발하는 IoT 기기들로 인해 주소 고갈이라는 치명적 한계를 맞았습니다. 이를 해결하기 위해 사설 IP를 돌려쓰는 NAT와 포트포워딩(PAT)이라는 꼼수를 넘어, **128비트의 무한한 주소 공간과 강력한 IPSec 보안을 기본 탑재한 'IPv6'로의 국가적 마이그레이션이 필수적입니다.**"
