### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (MODBUS정의, 1979년탄생배경) — 3~4줄
Ⅱ. 통신구조 - 마스터/슬레이브와기능코드 (본론①, 도식 1개 필수)
Ⅲ. 근본적보안취약점, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

MODBUS는 **1979년개발된 산업자동화통신프로토콜**로, 앞서다룬 \*\*퍼듀모델의Level0\~2(물리프로세스,PLC,SCADA)\*\*에서 **PLC,센서,밸브간실제데이터**를 주고받는 **가장기본적인언어**입니다 — \*\*"단순하고,제조사에구애받지않는"\*\*것이 장점이라 사실상표준이됐지만, 그 **단순함이곧치명적보안약점**이 됩니다.

### Ⅱ. 통신구조 — 마스터/슬레이브와기능코드

| 항목             | 내용                                                      |
| :------------- | :------------------------------------------------------ |
| **아키텍처**       | **마스터(PC,PLC)** ↔ **슬레이브(센서,밸브,모터등)**— 요청-응답방식          |
| **PDU**(핵심데이터) | **기능코드+데이터**— "레지스터읽기","값쓰기"등 명령                        |
| **MODBUS TCP** | 기존RTU프레임을 **TCP포트502**로 캡슐화 — 앞서다룬 **VXLAN의캡슐화**와 유사한구조 |
| **데이터타입**      | **불리언값+16비트정수**만지원— 극도로 **단순**                          |

→ 암기: **"PC가묻고,센서/밸브가답한다,명령은기능코드하나로"** — 앞서다룬 \*\*"AODV의RREQ/RREP"\*\*처럼, MODBUS도 \*\*"요청-응답"\*\*의 단순한구조지만, 목적이 \*\*"실제물리적장비(밸브,모터)를제어하는것"\*\*이라는 점에서 결과의무게가 다릅니다.

### 도식화 제안

```
[마스터(PC/PLC)] ──기능코드+데이터(요청)──→ [슬레이브(센서/밸브/모터)]
[마스터(PC/PLC)] ←──────응답─────────────── [슬레이브]

예: "레지스터40001값을읽어라" → "현재온도75도입니다"
    "밸브를열어라" → "밸브개방완료"
```

### Ⅲ. 근본적보안취약점 — 핵심 배점

**함정 방지: "보안이약하다"고만답하면절반. 앞서다룬"인증,기밀성,무결성,부인방지" 4대보안속성이 왜"전부"빠져있는지, 그리고이게왜치명적인지보여줘야완성됩니다.**

| 취약점            | 내용                                                                  |
| :------------- | :------------------------------------------------------------------ |
| **인증부재**(핵심)   | **누가명령을보냈는지전혀확인안함**— 마스터인척하는 **어떤기기든슬레이브에명령가능**                     |
| **암호화부재**      | 모든통신이 **평문**— 앞서다룬 \*\*"패킷캡처"\*\*로 즉시내용확인가능                         |
| **무결성검증부재**    | 전송중 **값이변조돼도감지불가**(앞서다룬"변조"공격에완전노출)                                 |
| **실증사례**(국내연구) | **PERA모델(퍼듀모델)기반 Cell/AreaZone에서 MODBUS/TCP실험** — 실제로 **공격이가능함을확인** |

→ 암기: **"보낸사람을확인안하고,내용을암호화안하고,변조를감지도안한다"** — 이는 앞서다룬 \*\*"디지털포렌식의변조"\*\*답안에서 다룬 **"원본이있는데바꿔치기하는"** 공격을, MODBUS 환경에서는 \*\*"방화벽조차없이 그대로허용"\*\*한다는 뜻입니다 — 앞서다룬 **"밸브를열어라"** 명령을 **공격자가그대로위조**해서 보내면, **슬레이브는의심없이실행**합니다.

### 도식화 제안

```
[정상마스터] ──"밸브개방"──→ [슬레이브] → 밸브열림

[공격자]──(마스터인척위조,평문이라내용도알고있음)──"밸브개방"──→ [슬레이브]
                                                        ↓
                                              인증확인없이 그대로실행!
                                              (앞서다룬퍼듀모델의DMZ가
                                               없으면 IT에서 여기까지침투가능)
```

**대응연구**(2020년,DCS논문): **MODBUS-TCP에인증·기밀성·무결성·부인방지 4대보안서비스를추가**하는 프레임구성 — **산업제어시스템의계층별기기성능차이**를 고려해, **계층마다다른전자서명알고리즘**을 사용해 \*\*자원제약환경(VxWorks등)\*\*에서도 **기존E-Modbus보다1.36\~3.43배빠른성능**을 달성했습니다.

### Ⅳ. 결론

MODBUS는 \*\*"1979년,보안위협이없던시절에설계된 극도로단순한산업프로토콜"\*\*이며, 이 \*\*단순함(인증·암호화·무결성검증전부부재)\*\*이 오늘날 **가장치명적인OT보안취약점**이 되었습니다 — 이는 앞서다룬 \*\*ISA/IEC62443(보안수준요구사항)\*\*과 \*\*퍼듀모델(DMZ를통한IT/OT격리)\*\*이 **왜반드시필요한지**를 보여주는 **실제근거**입니다: MODBUS자체는 스스로를 지킬수없기때문에, \*\*그것을둘러싼계층적방어(DMZ)와보안수준(SL)\*\*이 대신그역할을 해야합니다 — 이로써 오늘하루다룬 **ISA/IEC62443→퍼듀모델→MODBUS**로 이어지는 OT보안시리즈가, **"가장근본적인프로토콜의무방비함이,왜그위에겹겹이보안계층을쌓아야하는지를설명하는"** 완결된논리로 마무리됩니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "1979년에 만들어져 전 세계 스마트팩토리와 발전소를 장악해 버린 '산업용 통신 프로토콜의 할아버지'이자 사실상 표준(De facto)이다. 통신의 핵심은 **'마스터-슬레이브(Master-Slave)'** 구조다. 대장(마스터)이 "지금 모터 온도 몇 도야?"라고 콕 집어 물어보면, 부하(슬레이브)가 "25도입니다"라고 대답하는 아주 단순하고 직관적인 폴링(Polling) 방식이다. 과거에는 직렬 선을 꼽는 시리얼 방식(RTU)을 썼고, 최근엔 랜선을 꽂는 이더넷 방식(TCP/IP)으로 진화했다. 하지만 최대 단점은 \*\*보안이 개판(Zero Security)\*\*이라는 점이다. 너무 옛날에 만들어져서 '암호화'나 '인증' 기능이 아예 없다. 해커가 대장 행세를 하며 밸브를 잠그라는 가짜 명령(Injection)을 쏘면 공장이 그대로 멈춰버리는 치명적 약점을 가졌다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 산업 자동화(OT) 통신의 절대 강자, Modbus 개요**

* **정의:** Modicon 사가 PLC(Programmable Logic Controller) 기기 간의 통신을 위해 개발한 개방형 직렬(Serial) 통신 프로토콜.
* **특징:** 오픈 소스(로열티 무료)에 구조가 극도로 단순하고 신뢰성이 높아, 기종이 다른 수많은 산업용 센서와 제어 기기(SCADA, DCS)들을 연결하는 '산업계의 공용어'로 자리 잡음.

#### **II. \[본론 1] (극단적 단순화 버전) 명령과 응답, 마스터-슬레이브 구조**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NzcuNzc3IDI3Ni40IiB3aWR0aD0iNjc3Ljc3NyIgaGVpZ2h0PSIyNzYuNCIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iTW9kYnVzX19fX19fX18iIGRhdGEtbGFiZWw9Ik1vZGJ1cyDthrXsi6Ag6rWs7KGwOiDrrLvripQg64aI66eMIOusu+qzoCwg64yA64u166eMIO2VmOuKlCDrhogiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjU5Ny43NzciIGhlaWdodD0iMTk2LjQiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI1OTcuNzc3IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+TW9kYnVzIO2GteyLoCDqtazsobA6IOusu+uKlCDrhojrp4wg66y76rOgLCDrjIDri7Xrp4wg7ZWY64qUIOuGiDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTSIgZGF0YS10bz0iUzEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjEuIOuEiCDsmKjrj4Qg66qHIOuPhOyVvD8gKOyalOyyrSkiIHBvaW50cz0iMjY3LjYzOSwxNDUuNDggMjkxLjYzOSwxNDUuNDggMjkxLjYzOSwxMjguMyA0NTcuODcxMDAwMDAwMDAwMDQsMTI4LjMgNDU3Ljg3MTAwMDAwMDAwMDA0LDEyMC42MTY2NjY2NjY2NjY2NiA0OTMuODcxMDAwMDAwMDAwMDQsMTIwLjYxNjY2NjY2NjY2NjY2IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTMSIgZGF0YS10bz0iTSIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjIuIDI164+EIOyeheuLiOuLpCAo7J2R64u1KSIgcG9pbnRzPSI0OTMuODcxMDAwMDAwMDAwMDQsMTAyLjY4MzMzMzMzMzMzMzM0IDQ1Ny44NzEwMDAwMDAwMDAwNCwxMDIuNjgzMzMzMzMzMzMzMzQgNDU3Ljg3MTAwMDAwMDAwMDA0LDk1IDI3OS42MzksOTUgMjc5LjYzOSwxMzEuMzQgMjY3LjYzOSwxMzEuMzQiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTSIgZGF0YS10bz0iUzIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjMuIOuwuOu4jCDri6vslYTrnbwhICjrqoXroLkpIiBwb2ludHM9IjI2Ny42MzksMTczLjc2IDI3OS42MzksMTczLjc2IDI3OS42MzksMjEwLjEwMDAwMDAwMDAwMDAyIDQ1Ny44NzEwMDAwMDAwMDAwNCwyMTAuMTAwMDAwMDAwMDAwMDIgNDU3Ljg3MTAwMDAwMDAwMDA0LDIwMi40MTY2NjY2NjY2NjY2OSA0OTMuODcxMDAwMDAwMDAwMDQsMjAyLjQxNjY2NjY2NjY2NjY5IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTMiIgZGF0YS10bz0iTSIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjQuIOuLq+yVmOyKteuLiOuLpCAo7J2R64u1KSIgcG9pbnRzPSI0OTMuODcxMDAwMDAwMDAwMDQsMTg0LjQ4MzMzMzMzMzMzMzM1IDQ1Ny44NzEwMDAwMDAwMDAwNCwxODQuNDgzMzMzMzMzMzMzMzUgNDU3Ljg3MTAwMDAwMDAwMDA0LDE3Ni44IDI5MS42MzksMTc2LjggMjkxLjYzOSwxNTkuNjIgMjY3LjYzOSwxNTkuNjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJNIiBkYXRhLXRvPSJTMSIgZGF0YS1sYWJlbD0iMS4g64SIIOyYqOuPhCDrqocg64+E7JW8PyAo7JqU7LKtKSI+CiAgPHJlY3QgeD0iMzExLjYzOSIgeT0iMTEyLjMwMDAwMDAwMDAwMDAxIiB3aWR0aD0iMTM4LjIzMjAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzgwLjc1NSIgeT0iMTI3LjQ1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij4xLiDrhIgg7Jio64+EIOuqhyDrj4Tslbw/ICjsmpTssq0pPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlMxIiBkYXRhLXRvPSJNIiBkYXRhLWxhYmVsPSIyLiAyNeuPhCDsnoXri4jri6QgKOydkeuLtSkiPgogIDxyZWN0IHg9IjMyMC41NDkwMDAwMDAwMDAwNCIgeT0iNzkiIHdpZHRoPSIxMjAuNDEyMDAwMDAwMDAwMDIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzODAuNzU1MDAwMDAwMDAwMDUiIHk9Ijk0LjE1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij4yLiAyNeuPhCDsnoXri4jri6QgKOydkeuLtSk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iTSIgZGF0YS10bz0iUzIiIGRhdGEtbGFiZWw9IjMuIOuwuOu4jCDri6vslYTrnbwhICjrqoXroLkpIj4KICA8cmVjdCB4PSIzMTkuMzYxIiB5PSIxOTQuMTAwMDAwMDAwMDAwMDIiIHdpZHRoPSIxMjIuNzg4MDAwMDAwMDAwMDQiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzODAuNzU1IiB5PSIyMDkuMjUwMDAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjMuIOuwuOu4jCDri6vslYTrnbwhICjrqoXroLkpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlMyIiBkYXRhLXRvPSJNIiBkYXRhLWxhYmVsPSI0LiDri6vslZjsirXri4jri6QgKOydkeuLtSkiPgogIDxyZWN0IHg9IjMyMS40NCIgeT0iMTYwLjgiIHdpZHRoPSIxMTguNjMwMDAwMDAwMDAwMDEiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzODAuNzU1IiB5PSIxNzUuOTUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjQuIOuLq+yVmOyKteuLiOuLpCAo7J2R64u1KTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTSIgZGF0YS1sYWJlbD0i66eI7Iqk7YSwIOq4sOq4sCDwn5GRCuuqheugueydhCDrgrTrpqzripQg7Jyg7J287ZWcIOyhtOyerAooSE1JLCBQQyDrk7EpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIxMTcuMTk5OTk5OTk5OTk5OTkiIHdpZHRoPSIyMTEuNjM5IiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxNjEuODE5NSIgeT0iMTUyLjU0OTk5OTk5OTk5OTk4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNjEuODE5NSIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPuuniOyKpO2EsCDquLDquLAg8J+RkTwvdHNwYW4+PHRzcGFuIHg9IjE2MS44MTk1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rqoXroLnsnYQg64K066as64qUIOycoOydvO2VnCDsobTsnqw8L3RzcGFuPjx0c3BhbiB4PSIxNjEuODE5NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+KEhNSSwgUEMg65OxKTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTMSIgZGF0YS1sYWJlbD0i7Iqs66CI7J2067iMIDEg8J+klgrsmKjrj4Qg7IS87IScIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQ5My44NzEwMDAwMDAwMDAwNCIgeT0iODQuNzUiIHdpZHRoPSIxMjMuNDYwMDAwMDAwMDAwMDEiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjU1NS42MDEiIHk9IjExMS42NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNTU1LjYwMSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuyKrOugiOydtOu4jCAxIPCfpJY8L3RzcGFuPjx0c3BhbiB4PSI1NTUuNjAxIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7smKjrj4Qg7IS87IScPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlMyIiBkYXRhLWxhYmVsPSLsiqzroIjsnbTruIwgMiDwn6SWCuuqqO2EsCDrsLjruIwiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDkzLjg3MTAwMDAwMDAwMDA0IiB5PSIxNjYuNTUiIHdpZHRoPSIxMjcuOTA2IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1NTcuODI0MDAwMDAwMDAwMSIgeT0iMTkzLjQ1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI1NTcuODI0MDAwMDAwMDAwMSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuyKrOugiOydtOu4jCAyIPCfpJY8L3RzcGFuPjx0c3BhbiB4PSI1NTcuODI0MDAwMDAwMDAwMSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+66qo7YSwIOuwuOu4jDwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] Modbus 진화 모델 및 OT 보안 취약점 전격 대조 (3단 표)**

이 토픽은 전통적인 RTU 방식과 최신 TCP/IP 방식을 비교하고, 제어망(OT) 보안 사고의 원흉이 되는 \*\*'인증/암호화 부재'\*\*를 짚어내는 것이 가장 강력한 득점 포인트입니다.

| **핵심 척도**      | **🔌 Modbus RTU (과거/시리얼)**                 | **🌐 Modbus TCP/IP (현대/이더넷)**                | **🚨 보안 취약점 (출제 포인트) 💯**                                                                                              |
| :------------- | :----------------------------------------- | :------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| **통신 매체 / 포트** | RS-232, RS-485 같은 전통적인 시리얼(직렬) 케이블 사용.     | 일반적인 LAN선(이더넷) 사용. **표준 포트: TCP 502번.**      | 과거엔 오프라인이라 안전했으나, TCP/IP로 진화하며 **외부 인터넷망 공격에 노출됨.**                                                                    |
| **데이터 전송 방식**  | 데이터를 バイ너리(이진수, 0과 1) 형태로 압축해서 쏨. 작고 매우 빠름. | Modbus RTU 패킷에 TCP/IP 헤더를 껍데기로 씌워서 인터넷망으로 쏨. | **\[평문(Plain Text) 전송 💯]** 데이터를 암호화하지 않고 날것으로 보내서 패킷 스니핑(도청) 시 제어 로직이 100% 노출됨.                                       |
| **제어 / 인증 구조** | 하나의 선에 1마스터 - 최대 247슬레이브가 주렁주렁 매달림.        | 다수의 마스터(클라이언트)가 다수의 슬레이브(서버)에 동시 접속 가능.      | **\[인증 체계 원천 부재 💯]** 명령을 내리는 놈이 '진짜 마스터'인지 검사하는 로직이 아예 없음. 해커가 IP만 속이고 **가짜 제어 명령을 주입(Injection)하면 밸브가 터지거나 공장이 멈춤.** |

#### **IV. \[결론/제언] 스턱스넷(Stuxnet) 사태의 교훈과 Modbus Secure 도입**

* **(키워드 위주 2줄 마무리)** "이란의 원심분리기를 파괴한 스턱스넷(Stuxnet) 해킹 사건이 증명하듯, 암호화 없는 Modbus는 국가 기반 시설의 시한폭탄입니다. 이를 방어하기 위해 최근 산업계는 기존 패킷에 TLS 암호화 래퍼(Wrapper)를 씌운 **'Modbus Secure (Modbus TCP Security)'를 도입하여 폐쇄망(OT)의 제로 트러스트(Zero Trust) 아키텍처를 구현하고 있습니다.**"
