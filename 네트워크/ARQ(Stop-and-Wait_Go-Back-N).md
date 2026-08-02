### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (ARQ정의, 신뢰성보장의근본원리) — 3~4줄
Ⅱ. Stop-and-Wait ARQ (본론①, 도식 1개 필수)
Ⅲ. Go-Back-N ARQ - 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

ARQ(AutomaticRepeatRequest)는 **"패킷을보내고,확인응답(ACK)이없으면다시보내는"** 오류복구방식입니다 — 앞서다룬 **TCP의신뢰성**이 실제로 구현되는 기본원리이며, \*\*"한번에몇개까지보내놓고기다리는가"\*\*에 따라 여러방식으로나뉩니다.

### Ⅱ. Stop-and-Wait ARQ — 가장단순한방식

| 항목     | 내용                                            |
| :----- | :-------------------------------------------- |
| **동작** | **패킷하나전송→ACK받을때까지대기→받으면다음패킷전송**               |
| **장점** | 구현이 **매우단순**,수신버퍼1개만필요                        |
| **단점** | **한번에1개만보내고멈춰서기다림**— 왕복시간(RTT)이길면 **효율극도로낮음** |

→ 암기: **"하나보내고,멈춰서,답오면다음보낸다"** — 앞서다룬 \*\*"동기식통신"\*\*처럼 \*\*"확인될때까지완전히정지"\*\*하는 가장보수적인방식입니다.

### 도식화 제안

```
[송신자]                    [수신자]
──패킷1──→
←──ACK1───
(대기끝, 다음전송)
──패킷2──→
←──ACK2───
(멈춰서기다리는시간이 계속낭비됨)
```

### Ⅲ. Go-Back-N ARQ — 핵심 배점

**함정 방지: "여러개를보낸다"고만답하면절반. "왜N개까지허용하고, 오류시왜'그이후전체'를다시보내는지"를 보여줘야완성됩니다.**

| 항목            | 내용                                                                         |
| :------------ | :------------------------------------------------------------------------- |
| **윈도우**       | **N개까지응답기다리지않고연속전송**가능(앞서다룬"윈도우크기"개념재사용)                                   |
| **정상시**       | **누적ACK**로 여러패킷을 한번에확인가능("ACK5"=1\~5번모두잘받음)                                |
| **오류발생시**(핵심) | 특정패킷(예:3번)이 **손실되면**, 수신자는 **그이후모든패킷(4,5,6...)을버림**,송신자는 **3번부터N개전체를다시전송** |

→ 암기: **"N개까지는안기다리고보내지만, 하나라도틀리면 그다음전부다시보낸다"** — 이 \*\*"전부다시보내기"\*\*가 Go-Back-N의 **가장큰비효율**입니다: 3번만틀렸어도 **4,5,6번이멀쩡히도착했어도 전부버려지고재전송**됩니다.

### 도식화 제안

```
[Stop-and-Wait]                   [Go-Back-N]
1개씩,매번대기                      N개까지연속전송(윈도우)
효율매우낮음                         
                                  [정상시]
                                  패킷1,2,3,4,5 연속전송
                                  → ACK5(누적,한번에확인)

                                  [3번손실시]
                                  패킷1,2,[3✗],4,5 전송
                                       ↓
                                  수신자: 3번부터틀렸으니 4,5도버림
                                       ↓
                                  송신자: 3,4,5 전체재전송
                                  (4,5는이미잘도착했었는데도 다시보냄→비효율)
```

**Stop-and-Wait vs Go-Back-N 비교**

| 구분        | **Stop-and-Wait** | **Go-Back-N**      |
| :-------- | :---------------- | :----------------- |
| **처리량**   | 매우낮음(1개씩)         | **높음**(N개연속전송)     |
| **재전송범위** | 손실된패킷 **1개만**     | 손실지점 **이후전부**(비효율) |
| **구현복잡도** | 단순                | 중간(윈도우관리필요)        |

→ 앞서다룬 \*\*"혼잡제어의윈도우크기"\*\*개념이, 여기서는 \*\*"한번에몇개까지보낼수있는지"\*\*를결정하는 **동일한메커니즘**으로 재사용됩니다 — 혼잡제어가 **"네트워크상태에따라"** 윈도우를조절했다면, ARQ는 **"오류복구방식자체가"** 윈도우크기(N)를 전제로합니다.

### Ⅳ. 결론

Stop-and-Wait는 **"확실하지만느린"** 가장기본적인방식이고, Go-Back-N은 **"여러개를연속전송해빠르지만, 오류시불필요한재전송이생기는"** 절충안입니다 — 앞서다룬 \*\*"쓰기정책","캐시매핑"\*\*에서 반복됐던 \*\*"단순함vs효율"\*\*의트레이드오프가, 여기서도 \*\*"안전한1개씩vs효율적인N개연속(단,오류시낭비)"\*\*으로 재현됩니다 — 이는 오늘하루다룬 \*\*TCP핸드셰이크(연결)→ARQ(전송보장)→혼잡제어(속도조절)\*\*로 이어지는 네트워크신뢰성보장의 3단계흐름을 완성합니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "배달부가 물건 10개를 배달해야 한다. 배달 과정에서 물건을 분실하거나 파손됐을 때 다시 가져다주는(재전송) 시스템이 바로 \*\*'ARQ(자동 재전송 요구)'\*\*다. 첫 번째 배달부는 **'정지-대기(Stop-and-Wait)'** 방식을 쓴다. 물건 1개를 주고 영수증(ACK)을 받을 때까지 멍하니 대기한다. 영수증을 받으면 그제야 다음 물건을 꺼낸다. 확실하지만 전송 효율이 최악이다. 두 번째 배달부는 영수증을 기다리지 않고 1번부터 5번까지 연속으로 막 던져주는 **'Go-Back-N(GBN)'** 방식을 쓴다. 그런데 고객이 '어? 3번이 깨졌는데요?(NAK)'라고 하면, 배달부는 이미 잘 도착한 4번, 5번 물건까지 싹 다 뺏은 뒤, 3번부터 5번까지 '다시 처음부터 통째로' 배달한다. 수신자는 순서대로만 받으면 되니 구조가 간단하지만, 배달망 대역폭이 낭비된다. 세 번째 배달부인 \*\*'선택적 재전송(Selective Repeat)'\*\*은 똑똑하다. 3번이 깨졌다고 하면 딱 에러가 난 그 '3번' 패킷 하나만 다시 가져다준다. 대역폭 낭비가 전혀 없어 완벽해 보이지만, 고객(수신자)이 나중에 도착한 3번을 기존에 받은 4, 5번과 순서대로 끼워 맞춰야(재조립) 하므로 수신자의 버퍼 로직이 매우 복잡해진다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 신뢰성 있는 전송을 위한 오류 제어, ARQ 개요**

* **정의:** 데이터 링크 계층이나 전송 계층(TCP)에서, 송신한 패킷이 네트워크 상에서 분실되거나 오류가 발생했을 때 **수신자의 응답(ACK/NAK)과 송신자의 타임아웃(Timeout)을 이용해 해당 패킷을 자동으로 재전송**하는 오류 제어 기법.
* **핵심 메커니즘:** 전진 에러 수정(FEC)처럼 수신자가 스스로 에러를 고치는 것이 아니라, 에러가 나면 "다시 보내줘!"라고 요구하는 후진 에러 수정(BEC) 방식의 대표 격임.

#### **II. \[본론 1] (단순화 버전) 3대 ARQ 기법의 재전송 파이프라인 (도식화)**

2번 패킷이 에러 났을 때, 송신자가 어떻게 대처하는지를 직관적으로 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3MjQuMTMyIDUyMS40MDAwMDAwMDAwMDAxIiB3aWR0aD0iNzI0LjEzMiIgaGVpZ2h0PSI1MjEuNDAwMDAwMDAwMDAwMSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iQVJRX19fXzNfX18yX19fXyIgZGF0YS1sYWJlbD0iQVJRICjsnpDrj5kg7J6s7KCE7IahIOyalOq1rCkgM+uMgCDquLDrspUg67mE6rWQICgy67KIIO2MqO2CtyDsl5Drn6wg67Cc7IOdIOyLnCkiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjY0NC4xMzIiIGhlaWdodD0iNDQxLjQwMDAwMDAwMDAwMDAzIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNjQ0LjEzMiIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPkFSUSAo7J6Q64+ZIOyerOyghOyGoSDsmpTqtawpIDPrjIAg6riw67KVIOu5hOq1kCAoMuuyiCDtjKjtgrcg7JeQ65+sIOuwnOyDnSDsi5wpPC90ZXh0Pgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IjFfU3RvcGFuZFdhaXRfX18iIGRhdGEtbGFiZWw9IjEuIFN0b3AtYW5kLVdhaXQgKOygleyngCDrjIDquLApIPCfkKIiPgogIDxyZWN0IHg9IjU2IiB5PSIzNTEuNiIgd2lkdGg9IjYxMi4xMzIiIGhlaWdodD0iMTEzLjgwMDAwMDAwMDAwMDAxIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNTYiIHk9IjM1MS42IiB3aWR0aD0iNjEyLjEzMiIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjgiIHk9IjM2NS42IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjEuIFN0b3AtYW5kLVdhaXQgKOygleyngCDrjIDquLApIPCfkKI8L3RleHQ+CjwvZz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSIyX0dvQmFja05fR0JOXyIgZGF0YS1sYWJlbD0iMi4gR28tQmFjay1OIChHQk4pIPCflIQiPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjU4Mi4zNjkiIGhlaWdodD0iMTEzLjgwMDAwMDAwMDAwMDAxIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iNTgyLjM2OSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjgiIHk9Ijk4IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjIuIEdvLUJhY2stTiAoR0JOKSDwn5SEPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iM19TZWxlY3RpdmVfUmVwZWF0X18iIGRhdGEtbGFiZWw9IjMuIFNlbGVjdGl2ZSBSZXBlYXQgKOyEoO2DneyggSkg8J+OryI+CiAgPHJlY3QgeD0iNTYiIHk9IjIxNy44IiB3aWR0aD0iNTk1LjY1OSIgaGVpZ2h0PSIxMTMuODAwMDAwMDAwMDAwMDEiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI1NiIgeT0iMjE3LjgiIHdpZHRoPSI1OTUuNjU5IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI2OCIgeT0iMjMxLjgiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+My4gU2VsZWN0aXZlIFJlcGVhdCAo7ISg7YOd7KCBKSDwn46vPC90ZXh0Pgo8L2c+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlMxIiBkYXRhLXRvPSJSRTEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuustOyekeyglSDrqYjstrDshJwg6riw64uk66a8IiBwb2ludHM9IjIzOS4xNzg5OTk5OTk5OTk5Nyw0MjIuNSA0NTUuMzEzLDQyMi41IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTMiIgZGF0YS10bz0iUkUyIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsiJjsi6DsnpA6IDLrsojrtoDthLAg64uk7IucIOykmCEiIHBvaW50cz0iMjM2LjIxNTAwMDAwMDAwMDAzLDE1NC45IDQ2NC44MjMwMDAwMDAwMDAwNCwxNTQuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUzMiIGRhdGEtdG89IlJFMyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7IiY7Iug7J6QOiDrlLEgMuuyiOunjCDspJghIiBwb2ludHM9IjIzNi4yMTUwMDAwMDAwMDAwMywyODguNzAwMDAwMDAwMDAwMDUgNDQxLjA2MzAwMDAwMDAwMDA1LDI4OC43MDAwMDAwMDAwMDAwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJTMSIgZGF0YS10bz0iUkUxIiBkYXRhLWxhYmVsPSLrrLTsnpHsoJUg66mI7Law7IScIOq4sOuLpOumvCI+CiAgPHJlY3QgeD0iMjgzLjE3OSIgeT0iNDA2LjUwMDAwMDAwMDAwMDA2IiB3aWR0aD0iMTI4LjEzNDAwMDAwMDAwMDAxIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzQ3LjI0NiIgeT0iNDIxLjY1MDAwMDAwMDAwMDAzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7rrLTsnpHsoJUg66mI7Law7IScIOq4sOuLpOumvDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJTMiIgZGF0YS10bz0iUkUyIiBkYXRhLWxhYmVsPSLsiJjsi6DsnpA6IDLrsojrtoDthLAg64uk7IucIOykmCEiPgogIDxyZWN0IHg9IjI4MC4yMTUwMDAwMDAwMDAwMyIgeT0iMTM4LjkiIHdpZHRoPSIxNDAuNjA4IiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzUwLjUxOSIgeT0iMTU0LjA1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7siJjsi6DsnpA6IDLrsojrtoDthLAg64uk7IucIOykmCE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iUzMiIGRhdGEtdG89IlJFMyIgZGF0YS1sYWJlbD0i7IiY7Iug7J6QOiDrlLEgMuuyiOunjCDspJghIj4KICA8cmVjdCB4PSIyODAuMjE1MDAwMDAwMDAwMDMiIHk9IjI3Mi43MDAwMDAwMDAwMDAwNSIgd2lkdGg9IjExNi44NDgiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzMzguNjM5IiB5PSIyODcuODUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuyImOyLoOyekDog65SxIDLrsojrp4wg7KSYITwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzEiIGRhdGEtbGFiZWw9IjHrsogg7I+Y6rOgIEFDSyDquLDri6TrprwKMuuyiCDsj5jqs6AgRXJyb3Ig4p2MIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjcyIiB5PSIzOTUuNiIgd2lkdGg9IjE2Ny4xNzg5OTk5OTk5OTk5NyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTU1LjU4OTUiIHk9IjQyMi41IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNTUuNTg5NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPjHrsogg7I+Y6rOgIEFDSyDquLDri6Trprw8L3RzcGFuPjx0c3BhbiB4PSIxNTUuNTg5NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+MuuyiCDsj5jqs6AgRXJyb3Ig4p2MPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJFMSIgZGF0YS1sYWJlbD0iMuuyiCDtjKjtgrcg65SxIDHqsJzrp4wg64uk7IucIOyPqCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0NTUuMzEzIiB5PSI0MDQuMDUiIHdpZHRoPSIxOTYuODE5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1NTMuNzIyNSIgeT0iNDIyLjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjLrsogg7Yyo7YK3IOuUsSAx6rCc66eMIOuLpOyLnCDsj6g8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlMyIiBkYXRhLWxhYmVsPSIxLCAyLCAzLCA067KIIOyXsOyGjSDsj6gg8J+agArqt7zrjbAgMuuyiOydtCBFcnJvciDinYwiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNzIiIHk9IjEyOCIgd2lkdGg9IjE2NC4yMTUwMDAwMDAwMDAwMyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTU0LjEwNzUwMDAwMDAwMDAyIiB5PSIxNTQuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTU0LjEwNzUwMDAwMDAwMDAyIiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+MSwgMiwgMywgNOuyiCDsl7Dsho0g7I+oIPCfmoA8L3RzcGFuPjx0c3BhbiB4PSIxNTQuMTA3NTAwMDAwMDAwMDIiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuq3vOuNsCAy67KI7J20IEVycm9yIOKdjDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJSRTIiIGRhdGEtbGFiZWw9IuKcqCAy67KILCAz67KILCA067KI7J2ECuyghOu2gCDsi7kg64ukIOuLpOyLnCDsj6ghIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQ2NC44MjMwMDAwMDAwMDAwNCIgeT0iMTI4IiB3aWR0aD0iMTU3LjU0NiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI1NDMuNTk2IiB5PSIxNTQuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNTQzLjU5NiIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuKcqCAy67KILCAz67KILCA067KI7J2EPC90c3Bhbj48dHNwYW4geD0iNTQzLjU5NiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7KCE67aAIOyLuSDri6Qg64uk7IucIOyPqCE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzMiIGRhdGEtbGFiZWw9IjEsIDIsIDMsIDTrsogg7Jew7IaNIOyPqCDwn5qACuq3vOuNsCAy67KI7J20IEVycm9yIOKdjCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3MiIgeT0iMjYxLjgiIHdpZHRoPSIxNjQuMjE1MDAwMDAwMDAwMDMiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE1NC4xMDc1MDAwMDAwMDAwMiIgeT0iMjg4LjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE1NC4xMDc1MDAwMDAwMDAwMiIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPjEsIDIsIDMsIDTrsogg7Jew7IaNIOyPqCDwn5qAPC90c3Bhbj48dHNwYW4geD0iMTU0LjEwNzUwMDAwMDAwMDAyIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7qt7zrjbAgMuuyiOydtCBFcnJvciDinYw8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUkUzIiBkYXRhLWxhYmVsPSLinKggMywgNOuyiOydgCDrhpTrkZDqs6AK7Jik7KeBIDLrsogg7Yyo7YK3IO2VmOuCmOunjCDsj6ghIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQ0MS4wNjMwMDAwMDAwMDAwNSIgeT0iMjYxLjgiIHdpZHRoPSIxOTQuNTk1OTk5OTk5OTk5OTUiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNTM4LjM2MSIgeT0iMjg4LjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjUzOC4zNjEiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7inKggMywgNOuyiOydgCDrhpTrkZDqs6A8L3RzcGFuPjx0c3BhbiB4PSI1MzguMzYxIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7smKTsp4EgMuuyiCDtjKjtgrcg7ZWY64KY66eMIOyPqCE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 통신 효율을 가르는 ARQ 3대 기법 전격 비교 해부 (3단 표 - 1순위)**

단순함과 효율성은 반비례합니다. **Go-Back-N의 낭비**와 **Selective Repeat의 복잡성**을 명확히 대조해야 합니다.

| **ARQ 기법 종류**                                      | **재전송 메커니즘 (어떻게 보내나?)**                                                                                                                         | **장점 및 치명적 단점 (Trade-off) 🚨**                                                                                                        |
| :------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| **1. Stop-and-Wait** *(정지-대기 ARQ)*                 | **'1개 쏘고 영수증 올 때까지 하염없이 대기'.** 송신자가 패킷 1개를 전송한 후 수신자로부터 긍정 응답(ACK)을 받을 때까지 다음 패킷을 전송하지 않고 송신을 멈추고 기다림.                                          | **\[구현은 쉽지만 전송 효율 최악]** 송/수신자의 버퍼 크기가 1이면 되므로 로직이 아주 단순함. 하지만 통신 회선이 텅텅 비어있는데도 **응답이 올 때까지 놀고 있어야 하므로 속도 효율이 최악임.**                   |
| **2. Go-Back-N** *(슬라이딩 윈도우)* **\[TCP의 기본 구조 💯]** | **'에러 난 지점부터 그 뒤의 모든 패킷 싹 다 재전송'.** 기다리지 않고 여러 개를 막 쏘다가, 수신자가 2번 패킷에 에러(NAK 2)를 보고하면, 이미 정상적으로 도착한 3, 4번 패킷을 깡그리 무시하고 **2, 3, 4번을 통째로 다시 다 쏨.** | **\[수신자 단순 vs 망 대역폭 낭비]** 수신자는 패킷을 무조건 '순서대로만' 받으므로 버퍼가 단순함. 하지만 **이미 잘 도착한 패킷(3, 4번)을 또다시 재전송해야 하므로 네트워크 대역폭 낭비가 심함.**               |
| **3. Selective Repeat** *(선택적 재전송)*                | **'에러 난 놈 딱 하나만 콕 집어서 재전송'.** 연속으로 쏘다가 2번이 에러 나면, 정상 도착한 3, 4번은 수신자가 그냥 잘 보관(버퍼링)해 두고, **송신자는 오직 분실된 '2번' 패킷 하나만 쏙 골라서 재전송함.**                  | **\[대역폭 효율 최상 vs 수신자 멘붕 🚨]** 불필요한 패킷을 안 보내므로 통신 낭비가 제로(0)임. 단, **수신자가 나중에 도착한 2번을 3, 4번과 조립하기 위해 패킷을 정렬해야 하므로 수신 버퍼와 로직이 극도로 복잡해짐.** |

#### **IV. \[결론/제언] 하이브리드 ARQ(HARQ)와 무선 통신(5G/6G)의 신뢰성 극복**

* **(키워드 위주 2줄 마무리)** "오류가 잦은 최신 5G 무선망에서는 데이터를 처음부터 무식하게 다시 쏘는 ARQ만으로는 지연(Latency) 요구사항을 맞출 수 없습니다. 따라서 에러가 발생한 패킷을 버리지 않고 다음 재전송 패킷과 결합(Combine)하여 스스로 에러를 복원해 내는 전진 에러 수정(FEC) 결합형 **'HARQ (Hybrid ARQ)' 기술이 초저지연 무선 통신의 필수 표준으로 자리 잡고 있습니다.**"
