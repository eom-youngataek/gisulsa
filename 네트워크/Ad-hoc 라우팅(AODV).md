### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (Ad-hoc네트워크정의, AODV의위치) — 3~4줄
Ⅱ. 동작원리 - RREQ/RREP (본론①, 도식 1개 필수)
Ⅲ. 핵심특징 - On-Demand방식, 핵심 배점
Ⅳ. 활용사례및한계
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬 5G특화망,Wi-Fi는모두 '기지국/AP라는고정된중심'이있었는데, Ad-hoc네트워크는그런중심자체가없다 — 여러기기(노드)들이서로를거쳐가며 즉석에서네트워크를만드는것 — AODV는그때 '어느경로로가야할지'를찾는대표적프로토콜"\*\*이라는 한줄로시작하면, 왜Ad-hoc이 오늘의무선시리즈에서 근본적으로다른범주인지 드러납니다.

### Ⅱ. 동작원리 — RREQ/RREP

| 단계        | 신호                             | 의미                                               |
| :-------- | :----------------------------- | :----------------------------------------------- |
| **①경로요청** | **RREQ**(RouteRequest)         | 출발지노드가 \*\*"목적지까지가는길아는사람?"\*\*를 **주변에broadcast** |
| **②경로전파** | 각중간노드가 **RREQ를계속전달**(자신의역경로기록) | <br />                                           |
| **③경로응답** | **RREP**(RouteReply)           | 목적지(또는경로를아는노드)가 **원래경로를따라거꾸로**응답                 |

→ 암기: **"길을물어보고(RREQ),전달받은노드들이계속퍼뜨리고,목적지가답을거꾸로돌려보낸다(RREP)"** — 앞서다룬 \*\*"AAODV(방향매개변수추가)"\*\*연구가 이 **RREQ/RREP메시지수를줄여** VANET(차량간)의 **종단간지연·패킷손실**문제를 개선하려는 시도입니다.

### 도식화 제안

```
[출발지A] ──RREQ(broadcast)──→ [B] ──RREQ──→ [C] ──RREQ──→ [목적지D]
                                                              ↓
[출발지A] ←──────────────RREP(역경로로응답)────────────────[D]

(경로가확정되면, 그경로로 실제데이터전송시작)
```

### Ⅲ. 핵심특징 — On-Demand방식, 핵심 배점

**함정 방지: "경로를찾는다"고만답하면절반. 앞서다룬DSR과의차이,그리고"필요할때만"이라는점이 왜중요한지보여줘야완성됩니다.**

| 특징                 | 내용                                                                       |
| :----------------- | :----------------------------------------------------------------------- |
| **주문형(On-Demand)** | **데이터를전달할필요가있을때만** 경로탐색— 평소엔 **라우팅부하없음**(앞서다룬"살충제패러독스"의반대: 필요할때만작동해자원절약) |
| **가벼운메모리사용**       | 각노드는 **다음홉정보만저장**(전체경로전부를저장하지않음)— DSR(경로전체를소스에저장)의 **문제점을개선**하기위해 제안됨    |
| **동적토폴로지대응**       | 노드가 **계속움직여도**(모바일,드론,차량), **네트워크가자동재구성**                                |

→ 암기: **"필요할때만찾고,다음홉만기억하고,움직여도스스로적응한다"** — 앞서다룬 \*\*"Ad-hoc네트워크는자율적구성(Self-organizing)"\*\*특성이, AODV의 \*\*"On-Demand+가벼운메모리"\*\*설계로 구체적으로실현됩니다.

### 도식화 제안

```
[DSR - 전체경로저장]              [AODV - 다음홉만저장]
[A]: "A→B→C→D 전체경로"           [A]: "다음은B로가면돼"
(메모리부담큼)                     [B]: "다음은C로가면돼"
                                  (각노드는다음홉만알면됨,경량화)
```

### Ⅳ. 활용사례 및 한계

**함정 방지: "기지국없이연결된다"고만하면절반. 실제활용분야와, VANET에서드러난한계를 균형있게보여줘야완성됩니다.**

| 활용/한계                | 내용                                                                                                |
| :------------------- | :------------------------------------------------------------------------------------------------ |
| **활용분야**             | **군사작전,재난복구,IoT,VANET(차량간),드론군집** — 앞서다룬 \*\*"안티드론"\*\*답안의 **드론군집제어**가 바로 이런 **Ad-hoc네트워크위에서** 작동 |
| **VANET에서의한계**       | **고속이동으로토폴로지급변**→ **종단간지연,패킷손실**증가— **다음홉릴레이노드선택이어려움**                                            |
| **개선연구**(AAODV)      | **방향매개변수+2단계필터링**추가해 **RREQ/RREP메시지수를줄임**,패킷전달율향상                                                 |
| **보안취약점**(SD-AODV연구) | 중간노드가 **목적지주소를악의적으로변경**할수있음 — **다이제스트계산으로악성노드탐지**하는 보안강화프로토콜연구 진행중                                |

→ 앞서다룬 \*\*"측면이동(Pass-the-Hash등)"\*\*처럼, AODV도 \*\*"중간노드가경로정보를조작"\*\*하는 유사한위협에직면하며, \*\*암호학적검증(다이제스트)\*\*으로 대응하는 연구가 진행되고있습니다.

### 도식화 제안

```
[Ad-hoc네트워크 활용]
[군사작전] [재난복구] [IoT] [VANET(차량)] [드론군집(앞서다룬안티드론)]
     ↓
공통과제: 고속이동시 지연·손실증가 → AAODV등 개선연구
보안과제: 악성노드의경로조작 → SD-AODV등 검증기법연구
```

### Ⅴ. 결론

AODV는 **"기지국이나AP같은고정인프라없이, 노드들끼리즉석에서네트워크를구성하는Ad-hoc망에서, 필요할때만(On-Demand) 경로를찾고 가벼운메모리로유지하는"** 라우팅프로토콜입니다 — 이는앞서다룬 **안티드론의드론군집제어,6G의UAM** 같은 \*\*"고정인프라가없거나불가능한환경"\*\*에서 필수적인기반기술이며, VANET에서드러난 **고속이동시의한계**와 **경로조작보안위협**은 여전히 활발한연구영역입니다 — 이로써 캐시매핑에서시작해 실로장대했던 오늘하루의컴퓨터구조·보안·네트워크대장정이, **"고정된중심조차없이, 스스로연결을만들어가는"** 가장근본적인 네트워크형태로 마무리됩니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "기지국(공유기)이 박살 난 지진 현장이나 전쟁터에서, 구조대원들의 스마트폰끼리 릴레이로 무선 연결을 해 임시 통신망을 구축하는 기술이 \*\*'Ad-hoc(애드혹) 네트워크'\*\*다. 기지국이 없으니 폰들이 스스로 길잡이(라우터) 역할을 해야 한다. 폰은 배터리가 생명이므로, 1초마다 지도를 업데이트하며 미리 길을 찾아놓는 '사전 구동 방식(Proactive)'은 배터리 낭비가 심해 탈락이다. 대신 \*\*'데이터를 보낼 일이 생겼을 때만 그때그때 길을 찾는 요구 기반(Reactive/On-demand) 방식'\*\*이 애드혹의 표준이 되었고, 그 끝판왕이 바로 \*\*'AODV'\*\*다. AODV의 길 찾기는 3가지 메시지로 끝난다. 출발지가 '도착지(목적지) 아는 사람?' 하고 동네방네 소리치면(**RREQ**), 도착지가 '나 여기 있어!' 하고 출발지에게 1:1로 답장을 준다(**RREP**). 그러다 중간에 있는 폰이 딴 데로 이동해 릴레이가 끊기면 '길 끊어졌어!' 하고 에러를 날려(**RERR**) 출발지가 다시 소리치게(RREQ) 만든다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 기지국 없는 무선 임시 통신망, Ad-hoc 라우팅 개요**

* **Ad-hoc 네트워크 정의:** 무선 AP나 기지국 같은 고정된 인프라 없이, 이동 가능한 노드(스마트폰, 노트북, 드론 등)들끼리 자율적으로 구성하는 **초임시(On-the-fly) 다중 홉(Multi-hop) 무선 네트워크**.
* **라우팅의 핵심 제약:** 노드들이 계속 움직이므로(동적 토폴로지) 길이 수시로 변하며, 배터리 용량과 대역폭이 극도로 제한되어 있어 **'최소한의 에너지'로 길을 찾는 최적화 알고리즘이 필수적**임.

#### **II. \[본론 1] (극단적 단순화 버전) 필요할 때만 길을 찾는 AODV 3단계 파이프라인**

복잡한 전파 수식 대신, **찾고(RREQ) ➔ 답하고(RREP) ➔ 끊기면 에러(RERR)** 내는 직관적 흐름만 그렸습니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0ODIuMDI3IDMwMS40IiB3aWR0aD0iNDgyLjAyNyIgaGVpZ2h0PSIzMDEuNCIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iQU9EVl9fX19fX18iIGRhdGEtbGFiZWw9IkFPRFYgKOyVoOuTnO2YuSDsmKjrlJTrp6jrk5wg6rGw66asIOuyoe2EsCkg65287Jqw7YyFIO2VteyLrCDrj5nsnpEiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjQwMi4wMjciIGhlaWdodD0iMjIxLjQiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI0MDIuMDI3IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+QU9EViAo7JWg65Oc7Zi5IOyYqOuUlOunqOuTnCDqsbDrpqwg67Kh7YSwKSDrnbzsmrDtjIUg7ZW17IusIOuPmeyekTwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUSIgZGF0YS10bz0iUCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzMTguMDI3LDIxMC4wNSAzNjYuMDI3LDIxMC4wNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUSIgZGF0YS1sYWJlbD0iMS4g6ri4IOywvuq4sCDsmpTssq0gKFJSRVEpIPCfk6MK7Lac67Cc7KeAOiAn64+E7LCp7KeAIOqwgOuKlCDquLgg7JWE64qUIOyCrOuejD8nCuu4jOuhnOuTnOy6kOyKpO2KuOuhnCDrj5nrhKTrsKnrhKQg7Jm47LmoIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIxNzQuNyIgd2lkdGg9IjI2Mi4wMjciIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjE4Ny4wMTM1IiB5PSIyMTAuMDQ5OTk5OTk5OTk5OTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE4Ny4wMTM1IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+MS4g6ri4IOywvuq4sCDsmpTssq0gKFJSRVEpIPCfk6M8L3RzcGFuPjx0c3BhbiB4PSIxODcuMDEzNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7Lac67Cc7KeAOiAmIzM5O+uPhOywqeyngCDqsIDripQg6ri4IOyVhOuKlCDsgqzrnow/JiMzOTs8L3RzcGFuPjx0c3BhbiB4PSIxODcuMDEzNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+67iM66Gc65Oc7LqQ7Iqk7Yq466GcIOuPmeuEpOuwqeuEpCDsmbjsuag8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUCIgZGF0YS1sYWJlbD0iUCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzNjYuMDI3IiB5PSIxOTEuNiIgd2lkdGg9IjYwIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjM5Ni4wMjciIHk9IjIxMC4wNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+UDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRSIgZGF0YS1sYWJlbD0iMy4g6rK966GcIOyXkOufrCAoUkVSUikg8J+aqArspJHqsIQg64W465OcOiAn7Ja0PyDrj4TssKnsp4Ag64+E66ed6rCU64ukIScK7Lac67Cc7KeA7JeQ6rKMIOyXkOufrCDslYzrprwg4p6UIOuLpOyLnCAx67KIIOyImO2WiSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSIyODAuNTUyIiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxOTYuMjc2IiB5PSIxMTkuMzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE5Ni4yNzYiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj4zLiDqsr3roZwg7JeQ65+sIChSRVJSKSDwn5qoPC90c3Bhbj48dHNwYW4geD0iMTk2LjI3NiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7KSR6rCEIOuFuOuTnDogJiMzOTvslrQ/IOuPhOywqeyngCDrj4Trp53qsJTri6QhJiMzOTs8L3RzcGFuPjx0c3BhbiB4PSIxOTYuMjc2IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7stpzrsJzsp4Dsl5Dqsowg7JeQ65+sIOyVjOumvCDinpQg64uk7IucIDHrsogg7IiY7ZaJPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 애드혹 라우팅 2대 진영 (Proactive vs Reactive) 및 AODV 특징 대조**

라우팅 테이블을 **'미리 갱신하느냐'** 아니면 \*\*'요청할 때만 만드느냐(AODV)'\*\*를 대조하는 것이 출제 의도입니다.

| **핵심 척도 (비교 잣대)**               | **🗺️ Proactive (사전 테이블 구동 방식)**                                                                               | **⚡ Reactive (온디맨드/요구 기반) 🚨**                                                                            |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| **라우팅 테이블 갱신 시점 (언제 길을 찾는가?)**  | **'주기적으로 미리미리 지도 업데이트'.** 데이터 전송 요구와 상관없이, 노드들이 주기적으로 라우팅 정보를 주고받으며 **항상 최신 지도를 유지**함.                         | **'데이터 보낼 일이 생겼을 때만 탐색'.** 평소엔 가만히 있다가, \*\*데이터를 보내려는 출발지의 요청(On-demand)\*\*이 있을 때만 비로소 지도를 탐색하여 경로를 개설함. |
| **장점 및 단점 (Trade-off 관계)**      | - **장점:** 길이 이미 있으니 데이터 전송 딜레이가 0초임. - **단점:** 노드가 계속 움직이는 애드혹 환경에서 지도 갱신하느라 **네트워크 대역폭과 스마트폰 배터리를 다 갉아먹음 ❌.** | - **장점:** 평소엔 메시지를 안 주고받으니 **배터리와 대역폭 낭비가 전혀 없음 (애드혹 최적화) 💯.** - **단점:** 처음 길을 찾을 때(RREQ) 초기 딜레이가 발생함.   |
| **대표적인 라우팅 프로토콜**               | **DSDV** (Destination Sequenced Distance Vector)                                                               | **\[AODV] (Ad-hoc On-demand Distance Vector) 💯**                                                         |
| **✨ AODV의 핵심 기술 (무한 루프 방지 무기)** | (해당 없음)                                                                                                        | 길잡이 메시지에 \*\*'목적지 순서 번호 (Sequence Number)'\*\*를 달아서, 옛날 정보가 빙글빙글 도는 라우팅 루프(Looping) 현상을 원천 차단함.           |

#### **IV. \[결론/제언] 사물인터넷(IoT) 확장에 따른 저전력 RPL 라우팅으로의 진화**

* **(키워드 위주 2줄 마무리)** "AODV는 무선 애드혹 네트워크의 실질적 표준이지만, 극단적으로 배터리와 메모리가 부족한 수만 개의 센서(스마트 팜, 온도계 등)가 깔리는 저전력 IoT 망(LLN)에는 여전히 버겁습니다. 이를 해결하기 위해 AODV를 경량화하고 센서망 토폴로지에 맞게 트리(Tree) 구조로 경로를 수집하는 **IPv6 기반의 저전력 라우팅 표준인 'RPL (Routing Protocol for LLN)' 프로토콜이 IoT 인프라의 핵심으로 자리 잡고 있습니다.**"
