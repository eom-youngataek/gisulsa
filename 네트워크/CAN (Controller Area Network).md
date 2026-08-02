### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (CAN정의, MODBUS와의공통점) — 3~4줄
Ⅱ. 핵심원리 - 중재(Arbitration)방식 (본론①, 도식 1개 필수)
Ⅲ. 보안취약점및CAN-FD, 핵심 배점
Ⅳ. 차세대전환(이더넷) 및결론
```

포인트: 개요에서 \*\*"앞서다룬MODBUS가공장의PLC-센서언어였다면,CAN은자동차의ECU(전자제어장치)들이 서로대화하는언어 — 1985년보쉬가개발할때, 목표는'복잡한배선을단순화하는것'이었지 '보안'은 고려대상이아니었다"\*\*는한줄로시작하면, 왜 MODBUS와같은 근본적취약점을 안고있는지 논리가섭니다.

### Ⅱ. 핵심원리 — 중재(Arbitration)방식

| 항목                  | 내용                                                                                                   |
| :------------------ | :--------------------------------------------------------------------------------------------------- |
| **버스토폴로지**          | 모든ECU(엔진,브레이크,도어등)가 \*\*하나의공유선(버스)\*\*에 연결                                                           |
| **메시지기반**           | 특정목적지없이, **모든노드가모든메시지를수신**(브로드캐스트)                                                                   |
| **중재**(Arbitration) | 여러ECU가동시에전송하면, **ID값이낮은(우선순위높은)메시지가버스를차지** — 앞서다룬 \*\*"CSMA/CD의충돌처리"\*\*와 유사하지만, **충돌자체가아니라우선순위로결정** |
| **프레임크기제한**         | 최대 **8바이트**— 앞서다룬 \*\*"영상데이터전송에부적합"\*\*한 근본적한계                                                       |

→ 암기: **"모두가듣고,ID작은게이긴다,한번에8바이트만"** — 앞서다룬 **CSMA/CD**가 \*\*"충돌나면멈추고재시도"\*\*였다면, CAN은 \*\*"충돌이날것같으면 우선순위낮은쪽이스스로양보"\*\*하는 더정교한방식입니다.

### 도식화 제안

```
[CAN 버스 - 중재방식]
[엔진ECU] ──ID=0x100(우선순위높음)──┐
[도어ECU] ──ID=0x500(우선순위낮음)──┼──→ [공유버스]
                                    ↓
                          ID가작은 엔진ECU 메시지가 버스선점
                          (도어ECU는 대기후재시도)
```

### Ⅲ. 보안취약점 및 CAN-FD, 핵심 배점

**함정 방지: "보안이약하다"고만답하면절반. MODBUS와같은근본원인(인증/암호화부재)이면서, 자동차라는 "생명과직결"되는특수성을보여줘야완성됩니다.**

| 취약점                    | 내용                                                     |
| :--------------------- | :----------------------------------------------------- |
| **인증부재**               | 앞서다룬 **MODBUS와동일**— **어떤ECU든 다른ECU인척메시지위조가능**          |
| **암호화부재**              | 모든메시지가 **평문**, 버스에접근하면 **모든통신내용확인가능**                  |
| **실제공격사례**(이글루코퍼레이션연구) | **완성차벤더들의공격사례**분석— **OBD-II포트등물리적접근**을통한 CAN네트워크침해 확인  |
| **CAN-FD의양면성**         | **전송속도·용량증대**로 ECU증가에대응하지만, **"더많은데이터를더빠르게훔칠기회도함께제공"** |

→ 암기: **"보낸사람확인안하고,암호화안하고,속도가빨라지면 훔치는속도도빨라진다"** — 앞서다룬 \*\*"CAN은자동차·의료기기처럼 사람생명과직결된곳에쓰이는데도, 근본적으로보안을챙기기어려운 소프트웨어·하드웨어적한계"\*\*가 있다는게, 위키자료에서도 확인된 **가장중요한위험포인트**입니다 — 다만 \*\*"공격사례와그로얻는이득이유의미한경우가거의없어서 보통은따로보안을안챙긴다"\*\*는 현실도 함께존재합니다.

### 도식화 제안

```
[정상ECU] ──"브레이크작동"(평문,인증없음)──→ [버스]
[공격자(OBD-II포트로물리접근)] ──"브레이크무시"메시지 위조──→ [버스]
                                            ↓
                                    인증확인없이 그대로수신·실행
                                    (앞서다룬MODBUS와동일한근본구조)
```

### Ⅳ. 차세대전환(이더넷) 및 결론

**함정 방지: "CAN은한계가있다"로만끝내면절반. 2026년최신동향(차량용이더넷전환)을보여줘야완성됩니다.**

| 항목                      | 내용                                                                                                        |
| :---------------------- | :-------------------------------------------------------------------------------------------------------- |
| **테슬라등신생업체**            | **OTA(무선업데이트),영상데이터**처리를위해 **CAN Bus대신이더넷**을 혼용또는 완전대체                                                    |
| **10BASE-T1S**(2026년최신) | **CAN/CANFD의제한된대역폭+복잡한배선문제**를해결하는 **차세대차량용네트워크**— **멀티드롭구조지원+이더넷기반IP통신** 동시가능,**10Mbps**속도(기존CAN/LIN보다향상) |
| **2026년7월AID행사**        | 국내ICSKorea가 **CAN/CANFD,차량용이더넷(100M\~10G),FlexRay**등 **차세대차량망분석·검증솔루션**전시예정                               |

→ 앞서다룬 \*\*"MPLS-TP(확실성)vsIP-MPLS(유연성)"\*\*처럼, CAN(단순·확실,저용량)과 \*\*차량용이더넷(유연·고용량)\*\*이 \*\*"자동차네트워크영역에서도같은구도로공존"\*\*합니다 — **안전에직결된제어신호는여전히CAN**,**영상·OTA같은대용량데이터는이더넷**으로 **역할분담**하는 것이 최신흐름입니다.

### 결론

CAN통신은 **"MODBUS와똑같이,보안위협이없던시절에설계되어 인증·암호화가전혀없는"** 근본적취약점을가진 프로토콜이지만, \*\*"자동차·의료기기처럼사람의생명과직결"\*\*된다는점에서 그위험성이 더치명적입니다 — 이는 앞서다룬 **ISA/IEC62443,MODBUS**답안들과 **완전히같은교훈**을 보여줍니다: \*\*"산업/차량용프로토콜은자체적으로보안을갖추지못하므로, 물리적접근제어와상위계층방어가필수"\*\*입니다 — 2026년현재는 \*\*차세대차량용이더넷(10BASE-T1S등)\*\*으로의 **전환이가속화**되며, CAN은 \*\*"안전에직결된단순제어"\*\*영역으로 역할이재편되고있습니다 — 이로써 오늘하루다룬 **MODBUS→CAN**으로 이어지는 OT/자동차보안시리즈전체가, \*\*"산업화시대에설계된단순한프로토콜들이, 오늘날의보안위협앞에서 왜근본적으로재검토되어야하는지"\*\*를 보여주는 완결된교훈으로 마무리됩니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "자동차 내부의 수십 개 컴퓨터(ECU)들이 서로 대화하기 위해 만든 '차량용 혈관 통신망'이다. 과거엔 엔진, 브레이크끼리 구리선을 1:1로 다 엮느라 차가 무거웠는데, CAN은 단 두 가닥의 꼬인 선(Bus) 하나에 모든 부품을 묶어 배선 무게를 혁신적으로 줄였다. 가장 강력한 무기는 \*\*'비파괴적 중재(양보)'\*\*다. 브레이크와 에어컨이 동시에 신호를 쏘면 충돌해서 깨지는 게 아니라, ID 숫자가 낮은(우선순위가 높은) 브레이크 신호가 뚫고 나가고 에어컨은 조용히 찌그러진다. 하지만 뼈아픈 약점은 \*\*'보안이 제로'\*\*라는 것이다. 인증/암호화가 없어서, 해커가 블루투스로 침투해 우선순위 0번으로 '엑셀 밟아!'라는 가짜 신호를 마구 쏘면 속수무책으로 해킹당하는 원흉이 된다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 자동차 전장화의 혁명, CAN (Controller Area Network) 개요**

* **정의:** 보쉬(Bosch)사가 개발한 차량용 네트워크 표준으로, 마이크로컨트롤러(MCU)나 장치들(ECU)이 호스트 컴퓨터 없이 서로 통신할 수 있게 해주는 메시지 기반 직렬 통신 프로토콜.
* **목적:** 자동차 부품 간의 1:1(Point-to-Point) 복잡한 배선 뭉치를 버스(Bus) 토폴로지로 통합하여 차량의 무게와 원가를 절감하고 통신 신뢰성을 확보함.

#### **II. \[본론 1] (극단적 단순화 버전) 목숨이 달린 브레이크 신호의 무조건적 승리**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MTEuODI3IDI3NS42IiB3aWR0aD0iODExLjgyNyIgaGVpZ2h0PSIyNzUuNiIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iQ0FOX19fX18iIGRhdGEtbGFiZWw9IkNBTiDthrXsi6DsnZgg67mE7YyM6rS07KCBIOykkeyerCAo7Jqw7ISg7Iic7JyEIOuwsO2LgCkiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjczMS44MjciIGhlaWdodD0iMTk1LjYwMDAwMDAwMDAwMDAyIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNzMxLjgyNyIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPkNBTiDthrXsi6DsnZgg67mE7YyM6rS07KCBIOykkeyerCAo7Jqw7ISg7Iic7JyEIOuwsO2LgCk8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkIiIGRhdGEtdG89IkJVUyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyMzEuMzI5OTk5OTk5OTk5OTgsMTkyLjcwMDAwMDAwMDAwMDAyIDI2NS4zMzM0OTk5OTk5OTk5NiwxOTIuNzAwMDAwMDAwMDAwMDIgMjY1LjMzMzQ5OTk5OTk5OTk2LDE1MS44IDI4NS45OTg5OTk5OTk5OTk5NywxNTEuOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQSIgZGF0YS10bz0iQlVTIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjI0NC42Njc5OTk5OTk5OTk5NSwxMTAuOSAyNjUuMzMzNDk5OTk5OTk5OTYsMTEwLjkgMjY1LjMzMzQ5OTk5OTk5OTk2LDE1MS44IDI4NS45OTg5OTk5OTk5OTk5NywxNTEuOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQlVTIiBkYXRhLXRvPSJXSU4iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuKcqOy2qeuPjCDslYgg6rmo7KeQIeKcqCIgcG9pbnRzPSIzNTQuNjI0OTk5OTk5OTk5OTQsMTQ1LjY1IDM2Ni42MjQ5OTk5OTk5OTk5NCwxNDUuNjUgMzY2LjYyNDk5OTk5OTk5OTk0LDExMC45IDU0OS4zNzUsMTEwLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkJVUyIgZGF0YS10bz0iTE9TRSIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyXtOyEuCDqsJDsp4AiIHBvaW50cz0iMzU0LjYyNDk5OTk5OTk5OTk0LDE1Ny45NSAzNjYuNjI0OTk5OTk5OTk5OTQsMTU3Ljk1IDM2Ni42MjQ5OTk5OTk5OTk5NCwxOTIuNzAwMDAwMDAwMDAwMDIgNTQ5LjM3NSwxOTIuNzAwMDAwMDAwMDAwMDIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJCVVMiIGRhdGEtdG89IldJTiIgZGF0YS1sYWJlbD0i4pyo7Lap64+MIOyViCDquajsp5Ah4pyoIj4KICA8cmVjdCB4PSIzOTguNjI0OTk5OTk5OTk5OTQiIHk9Ijk0LjkiIHdpZHRoPSIxMDYuNzUwMDAwMDAwMDAwMDMiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI0NTEuOTk5OTk5OTk5OTk5OTQiIHk9IjExMC4wNTAwMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+4pyo7Lap64+MIOyViCDquajsp5Ah4pyoPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkJVUyIgZGF0YS10bz0iTE9TRSIgZGF0YS1sYWJlbD0i7Je07IS4IOqwkOyngCI+CiAgPHJlY3QgeD0iNDE4LjUyMzk5OTk5OTk5OTk0IiB5PSIxNzYuNzAwMDAwMDAwMDAwMDIiIHdpZHRoPSI2Ni45NTIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI0NTEuOTk5OTk5OTk5OTk5OTQiIHk9IjE5MS44NTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7Je07IS4IOqwkOyngDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQiIgZGF0YS1sYWJlbD0i67iM66CI7J207YGsIEVDVQpJRDogMDAxICjsmrDshKDsiJzsnIQgMeuTsSEpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjYyLjY2ODk5OTk5OTk5OTk4IiB5PSIxNjUuOCIgd2lkdGg9IjE2OC42NjEiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTQ2Ljk5OTQ5OTk5OTk5OTk4IiB5PSIxOTIuNzAwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE0Ni45OTk0OTk5OTk5OTk5OCIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuu4jOugiOydtO2BrCBFQ1U8L3RzcGFuPjx0c3BhbiB4PSIxNDYuOTk5NDk5OTk5OTk5OTgiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPklEOiAwMDEgKOyasOyEoOyInOychCAx65OxISk8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQlVTIiBkYXRhLWxhYmVsPSJCVVMiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjg1Ljk5ODk5OTk5OTk5OTk3IiB5PSIxMzMuMzUiIHdpZHRoPSI2OC42MjU5OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIzMjAuMzExOTk5OTk5OTk5OTUiIHk9IjE1MS44IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5CVVM8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkEiIGRhdGEtbGFiZWw9IuyXkOyWtOy7qCBFQ1UKSUQ6IDA5OSAo7Jqw7ISg7Iic7JyEIOq8tOywjCkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNjIuNjY4OTk5OTk5OTk5OTgiIHk9Ijg0IiB3aWR0aD0iMTgxLjk5ODk5OTk5OTk5OTk3IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNTMuNjY4NDk5OTk5OTk5OTciIHk9IjExMC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNTMuNjY4NDk5OTk5OTk5OTciIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7sl5DslrTsu6ggRUNVPC90c3Bhbj48dHNwYW4geD0iMTUzLjY2ODQ5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5JRDogMDk5ICjsmrDshKDsiJzsnIQg6ry07LCMKTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJXSU4iIGRhdGEtbGFiZWw9Iuu4jOugiOydtO2BrCDsi6DtmLgg7Iq566asIPCfj4YK7JeU7KeE7Jy866GcIOyLoO2YuCDrj4TssKkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTQ5LjM3NSIgeT0iODQiIHdpZHRoPSIxODEuOTk5IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjY0MC4zNzQ1IiB5PSIxMTAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNjQwLjM3NDUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7ruIzroIjsnbTtgawg7Iug7Zi4IOyKueumrCDwn4+GPC90c3Bhbj48dHNwYW4geD0iNjQwLjM3NDUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyXlOynhOycvOuhnCDsi6DtmLgg64+E7LCpPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkxPU0UiIGRhdGEtbGFiZWw9IuyXkOyWtOy7qCDsi6DtmLgg7KCE7IahIO2PrOq4sCDwn4+z77iPCuuCmOykkeyXkCDri6Tsi5wg7Iuc64+EIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU0OS4zNzUiIHk9IjE2NS44IiB3aWR0aD0iMjA2LjQ1MiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNjUyLjYwMSIgeT0iMTkyLjcwMDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI2NTIuNjAxIiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7JeQ7Ja07LuoIOyLoO2YuCDsoITshqEg7Y+s6riwIPCfj7PvuI88L3RzcGFuPjx0c3BhbiB4PSI2NTIuNjAxIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rgpjspJHsl5Ag64uk7IucIOyLnOuPhDwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] CAN 통신의 3대 핵심 메커니즘 전격 해부 (3단 표)**

| **핵심 척도**            | **🚘 버스 구조 및 통신 방식**                                                                         | **🚦 충돌 중재 메커니즘 🚨**                                                                              | **🚨 차량 해킹 보안 취약점 💯**                                                                                       |
| :------------------- | :------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------- |
| **핵심 원리**            | **'멀티 마스터 (Multi-Master)'.** 대장(Master)이 없음. 버스 선이 비어있으면 브레이크든 와이퍼든 어떤 ECU라도 먼저 데이터를 쏠 수 있음. | **'비파괴적 중재 (Arbitration) 💯'.** 이더넷(CSMA/CD)은 부딪히면 데이터가 깨지지만, CAN은 데이터가 안 깨지고 ID(식별자) 값으로 승패를 가름. | **'방송(Broadcast)과 무인증'.** 수신처 주소가 없음. 버스에 신호를 뿌리면 모든 ECU가 다 받음. 그리고 보낸 놈이 누군지 검사(인증) 안 함.                    |
| **작동 특징 및 취약 형태 🚨** | 꼬인 두 가닥 선(Twisted Pair)에 전압 차이를 이용해 신호를 보내서, 엔진 노이즈(전자기파) 간섭에 매우 강함.                         | **\[숫자가 작을수록(0) 이김 💯]** 메시지 헤더에 붙은 ID에 '0(Dominant)'이 많은 놈이 이김. (브레이크 등 생명과 직결된 부품에 낮은 ID 부여).   | **\[인젝션(Injection) 공격 💯]** 해커가 스마트폰 앱이나 정비용 포트(OBD-2)로 침투해, 가장 낮은 ID(예: 000)로 **조향장치 조작 메시지를 뿌리면 차가 급발진함.** |
| **해결 / 보완**          | 최근에는 대용량 영상 처리를 위해 대역폭이 넓은 CAN-FD나 차량용 이더넷으로 진화 중.                                           | 우선순위가 낮은 에어컨 같은 부품은 급박한 상황에서 메시지 전송이 계속 지연될 수 있음.                                                 | **\[해결책: CANsec 및 IDS]** 메시지에 MAC(인증 코드)을 달아 위변조를 막는 CANsec 암호화와 차량용 침입탐지시스템(IDS) 탑재 필수.                     |

#### **IV. \[결론/제언] SDV(소프트웨어 중심 자동차) 시대의 차량용 이더넷(Ethernet) 전환**

* **(키워드 위주 2줄 마무리)** "자율주행과 인포테인먼트가 고도화되는 SDV 시대에는 센서와 라이다(LiDAR)의 대용량 영상 데이터를 1Mbps짜리 낡은 CAN 통신으로는 절대 감당할 수 없습니다. 따라서 테슬라 등 선도 기업들은 **기가비트급 대역폭과 IP 기반의 강력한 보안(IPSec)을 제공하는 '차량용 이더넷(Automotive Ethernet)' 아키텍처로 차량 네트워크의 근간을 전면 교체하고 있습니다.**"
