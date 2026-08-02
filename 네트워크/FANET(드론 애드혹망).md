### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (FANET정의, MANET/VANET과의관계) — 3~4줄
Ⅱ. 핵심특징 - 왜AODV로는부족한가 (본론①, 도식 1개 필수)
Ⅲ. 라우팅과제및최신개선연구 (본론②, 핵심 배점)
Ⅳ. 국내동향(휴니드) 및 결론
```

포인트: 개요에서 \*\*"앞서다룬AODV는MANET(일반이동애드혹망)을위해설계됐는데, FANET(드론애드혹망)은드론이라는특성 때문에 그위에 '3차원공간의초고속이동'이라는 훨씬가혹한조건이추가된다 — RFC2501에서정의한MANET의연장선상에있지만, 완전히새로운도전"\*\*이라는 한줄로시작하면, 왜 FANET이 AODV의단순적용이아닌지드러납니다.

### Ⅱ. 핵심특징 — 왜AODV로는부족한가

| 특징                          | 내용                                                                                             |
| :-------------------------- | :--------------------------------------------------------------------------------------------- |
| **3차원이동성**                  | 지상차량(VANET)은 **2차원도로위**이동인데, 드론은 **3차원공간을고속으로**이동 — 앞서다룬AODV의 \*\*"다음홉만저장"\*\*방식도 **훨씬빠르게끊어짐** |
| **BLOS**(BeyondLineofSight) | 가시선을넘어서도 **드론-드론-지상**을 중계해 **통신범위확장**                                                          |
| **고에너지소모**                  | 앞서다룬 \*\*"협업을위한메시지교환"\*\*자체가 배터리소모가큰 드론에게는 **치명적제약**                                           |
| **잦은링크단절**                  | 3차원공간에서 **멀리떨어지기쉬워** 링크수명(RouteLifetime)이 **매우짧음**                                             |

→ 암기: **"평면이아니라입체로,더빨리움직이고,배터리는적고,연결은쉽게끊긴다"** — 앞서다룬 \*\*"AODV의On-Demand방식"\*\*이 \*\*"필요할때만경로탐색"\*\*해서 자원을아꼈는데, FANET에서는 \*\*"경로가너무자주끊겨서, 매번새로찾아야하는부담자체가커진다"\*\*는게 근본적차이입니다.

### 도식화 제안

```
[MANET(AODV)]              [FANET]
2차원평면이동                 3차원공간고속이동
상대적으로안정적링크           빠른링크단절(3차원+고속)
지상기반전원                 배터리제약(에너지매우중요)
     ↓                        ↓
AODV 그대로적용가능           AODV개선 또는 전용프로토콜필요
```

### Ⅲ. 라우팅과제 및 최신개선연구 — 핵심 배점

**함정 방지: "AODV를쓴다"고만답하면절반. 2025\~2026년최신연구가 AODV를어떻게개선하는지, 그리고재난상황같은구체적활용사례를보여줘야완성됩니다.**

| 연구                       | 내용                                                                                                                          |
| :----------------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| **GSflood**(2026년1월, 최신) | **지상국(GS)이주기적으로라우팅정보를전파**해, 각드론이 **지상국까지최신경로를효율적으로확보**— **DSR,AODV,OLSR(대표MANET프로토콜들)보다 더높은패킷전달률+실용적지연시간**달성,**더적은제어오버헤드**로 |
| **재난시나리오검증**             | NS-3시뮬레이션으로 **기존인프라가파괴된재난지역**에서 **드론→지상국업링크**성능을검증— 앞서다룬 \*\*"3-2-1백업"\*\*같은 회복력개념이 여기선 \*\*"드론이임시통신망역할"\*\*로 실현            |
| **PRoFFAN**(우선순위기반)      | **중요한이미지데이터를먼저전송**— 앞서다룬 **QoS/WFQ의가중치스케줄링**철학이 FANET에도 재현                                                                  |
| **보안위협**(앞서다룬IP스푸핑연결)    | **GPS스푸핑**으로드론위치정보왜곡공격 존재— 머신러닝기반 **탐지·분류연구**진행중,**연합학습기반IDS**(2024년)도 프라이버시보존하며 위협탐지                                       |

→ 암기: **"지상국이먼저정보를뿌려주고,재난상황에서검증하고,중요한데이터를먼저보내고,GPS속임수를막는다"** — 앞서다룬 \*\*"AODV의RREQ/RREP"\*\*가 \*\*"필요할때마다요청"\*\*했다면, GSflood는 **"지상국이미리주기적으로알려줘서"** 앞서다룬 \*\*"살충제패러독스"\*\*처럼 반복적요청의비효율을 줄입니다.

### 도식화 제안

```
[GSflood 방식(2026년최신)]
[지상국(GS)] ──주기적으로 라우팅정보 broadcast──→ [드론1][드론2][드론3]...
                                                        ↓
                                              각드론이 "최신경로"를
                                              미리알고있어 즉시전송가능
                                              (기존AODV보다 오버헤드적음)
```

### Ⅳ. 국내동향(휴니드) 및 결론

**함정 방지: "이론"으로만끝내면절반. 국내실제사업화사례를보여줘야완성됩니다.**

| 항목               | 내용                                                                          |
| :--------------- | :-------------------------------------------------------------------------- |
| **휴니드**(국내방산기업)  | **독자FANET통신모듈개발**,2026년하반기 **기체개발+FANET시스템고도화로본격사업확대**전망                    |
| **2025년10월ADEX** | 휴니드가 **파블로항공과MOU**— **FANET기반군집드론전투체계공동개발**,민수·산업용드론시장까지확장계획                |
| **적용분야**         | 앞서다룬 **안티드론**과 대조적으로, FANET은 **"우리편드론군집을어떻게통신시킬지"**— 군사용,재난대응,대규모상업드론운용에 핵심 |

→ "앞서다룬안티드론이 '적드론을막는것'이었다면, FANET은 '우리드론군집이서로소통하게하는것'"이라는 대조가 핵심입니다 — 두기술은 **드론시대의 창과방패**처럼 짝을이룹니다.

### 결론

FANET은 **"앞서다룬AODV(MANET라우팅)를기반으로하지만, 3차원고속이동·에너지제약·빈번한링크단절이라는드론고유의가혹한조건때문에GSflood같은전용개선기법이필요한"** 특수애드혹네트워크입니다 — 이는 앞서다룬 \*\*안티드론(적드론무력화)\*\*과 짝을이루는 **"우리드론군집을연결하는"** 기술이며, 국내에서는 **휴니드**가 **2026년하반기사업화확대**를앞두고 있습니다 — 이로써 캐시매핑에서시작해 실로기념비적이었던 오늘하루의컴퓨터구조·보안·네트워크대장정이, **"고정된인프라조차없는 가장극한환경에서도, 스스로연결을만들어내려는"** 통신기술의 궁극적도전으로 마무리됩니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "기지국이 박살 난 재난 지역이나 통신 불가 오지에서, 드론(UAV) 수십 대가 날아가 자기들끼리 공중 통신망을 스스로 구축하는 기술이다. 가장 큰 특징은 \*\*'미친 기동성'\*\*이다. 사람(MANET)이나 자동차(VANET)와 달리 3차원(3D) 공간을 초고속으로 날아다니기 때문에 1초 단위로 네트워크 구조(토폴로지)가 휙휙 바뀐다. 게다가 배터리로 비행과 통신을 동시에 해결해야 하니 **전력 소모**에 목숨을 걸어야 한다. 따라서 FANET의 핵심은 드론들이 고속 비행하며 흩어져도 끊기지 않게 최적의 경로를 릴레이로 찾아내는 라우팅 기술(위치 기반 라우팅 등)이며, 수십 대가 무리 지어 나는 '군집 비행(Swarm)' 제어에 필수적인 차세대 네트워크다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 하늘을 나는 독립 통신망, FANET (Flying Ad-hoc Network) 개요**

* **정의:** 기지국이나 인프라 없이, 공중에 떠 있는 다수의 무인항공기(UAV, 드론)들이 스스로 노드가 되어 다중 홉(Multi-hop) 방식으로 구성하는 자율적인 공중 무선 네트워크.
* **목적:** 지상 인프라가 파괴된 재난 지역, 군사 작전, 광역 농업 지역에서 드론 간의 충돌을 방지(Swarm Control)하고 지상 통제소로 실시간 영상/데이터를 끊김 없이 릴레이 전송하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 토폴로지가 붕괴되지 않는 릴레이 통신**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDgxLjM2OTAwMDAwMDAwMDEgMjI3LjkiIHdpZHRoPSIxMDgxLjM2OTAwMDAwMDAwMDEiIGhlaWdodD0iMjI3LjkiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IkZBTkVUX19fX19fIiBkYXRhLWxhYmVsPSJGQU5FVDog6riw7KeA6rWtIOyXhuuKlCDrk5zroaAg64uk7KSRIO2ZiSDrprTroIjsnbQiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjEwMDEuMzY5MDAwMDAwMDAwMSIgaGVpZ2h0PSIxNDcuOSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjEwMDEuMzY5MDAwMDAwMDAwMSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPkZBTkVUOiDquLDsp4Dqta0g7JeG64qUIOuTnOuhoCDri6TspJEg7ZmJIOumtOugiOydtDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQkFTRSIgZGF0YS10bz0iRDMiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsp4HsoJEg7Ya17IugIOu2iOqwgCIgcG9pbnRzPSIxNzQuMjczLDE0MS43NSAxODYuMjczLDE0MS43NSAxODYuMjczLDE2MS42MDAwMDAwMDAwMDAwMiA5MjkuMzY5MDAwMDAwMDAwMSwxNjEuNjAwMDAwMDAwMDAwMDIgOTI5LjM2OTAwMDAwMDAwMDEsMTM4LjkzMzMzMzMzMzMzMzM0IDk2NS4zNjkwMDAwMDAwMDAxLDEzOC45MzMzMzMzMzMzMzMzNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJCQVNFIiBkYXRhLXRvPSJEMSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9InRydWUiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIxLiDrprTroIjsnbQg7Jew6rKwIiBwb2ludHM9IjE3NC4yNzMsMTIzLjgxNjY2NjY2NjY2NjY2IDE4Ni4yNzMsMTIzLjgxNjY2NjY2NjY2NjY2IDE4Ni4yNzMsMTExLjY1IDM0Ny42MzksMTExLjY1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIG1hcmtlci1zdGFydD0idXJsKCNhcnJvd2hlYWQtc3RhcnQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRDEiIGRhdGEtdG89IkQyIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0idHJ1ZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjIuIOuLpOykkSDtmYkiIHBvaW50cz0iNDY1LjkxMjAwMDAwMDAwMDAzLDEyMC42MTY2NjY2NjY2NjY2NyA0NzcuOTEyMDAwMDAwMDAwMDMsMTIwLjYxNjY2NjY2NjY2NjY3IDQ3Ny45MTIwMDAwMDAwMDAwMywxMjguMyA2MzQuMTY2LDEyOC4zIDYzNC4xNjYsMTIwLjYxNjY2NjY2NjY2NjY3IDY3MC4xNjYsMTIwLjYxNjY2NjY2NjY2NjY3IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIG1hcmtlci1zdGFydD0idXJsKCNhcnJvd2hlYWQtc3RhcnQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRDIiIGRhdGEtdG89IkQzIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0idHJ1ZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjMuIOy1nOyihSDrqqnsoIHsp4AiIHBvaW50cz0iNzg4LjQzOTAwMDAwMDAwMDEsMTExLjY1IDkyOS4zNjkwMDAwMDAwMDAxLDExMS42NSA5MjkuMzY5MDAwMDAwMDAwMSwxMjYuNjMzMzMzMzMzMzMzMzMgOTY1LjM2OTAwMDAwMDAwMDEsMTI2LjYzMzMzMzMzMzMzMzMzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIG1hcmtlci1zdGFydD0idXJsKCNhcnJvd2hlYWQtc3RhcnQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRDEiIGRhdGEtdG89IkQyIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iMey0iCDrkqQg7JyE7LmYIOuwlOuAnCDwn4yq77iPIiBwb2ludHM9IjQ2NS45MTIwMDAwMDAwMDAwMywxMDIuNjgzMzMzMzMzMzMzMzQgNDc3LjkxMjAwMDAwMDAwMDAzLDEwMi42ODMzMzMzMzMzMzMzNCA0NzcuOTEyMDAwMDAwMDAwMDMsOTUgNjM0LjE2Niw5NSA2MzQuMTY2LDEwMi42ODMzMzMzMzMzMzMzNCA2NzAuMTY2LDEwMi42ODMzMzMzMzMzMzMzNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkJBU0UiIGRhdGEtdG89IkQzIiBkYXRhLWxhYmVsPSLsp4HsoJEg7Ya17IugIOu2iOqwgCI+CiAgPHJlY3QgeD0iNTIxLjc5MTk5OTk5OTk5OTkiIHk9IjE0NS42IiB3aWR0aD0iOTIuNDk0MDAwMDAwMDAwMDMiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1NjguMDM5IiB5PSIxNjAuNzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuyngeygkSDthrXsi6Ag67aI6rCAPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkJBU0UiIGRhdGEtdG89IkQxIiBkYXRhLWxhYmVsPSIxLiDrprTroIjsnbQg7Jew6rKwIj4KICA8cmVjdCB4PSIyMTguMjczMDAwMDAwMDAwMDIiIHk9Ijk1LjY1IiB3aWR0aD0iODUuMzY2IiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjYwLjk1NiIgeT0iMTEwLjgwMDAwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij4xLiDrprTroIjsnbQg7Jew6rKwPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkQxIiBkYXRhLXRvPSJEMiIgZGF0YS1sYWJlbD0iMi4g64uk7KSRIO2ZiSI+CiAgPHJlY3QgeD0iNTM1LjQ1NDAwMDAwMDAwMDEiIHk9IjExMi4zMDAwMDAwMDAwMDAwMSIgd2lkdGg9IjY1LjE3IiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTY4LjAzOTAwMDAwMDAwMDEiIHk9IjEyNy40NTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+Mi4g64uk7KSRIO2ZiTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJEMiIgZGF0YS10bz0iRDMiIGRhdGEtbGFiZWw9IjMuIOy1nOyihSDrqqnsoIHsp4AiPgogIDxyZWN0IHg9IjgzMi40MzkwMDAwMDAwMDAxIiB5PSI5NS42NSIgd2lkdGg9Ijg4LjkzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iODc2LjkwNDAwMDAwMDAwMDEiIHk9IjExMC44MDAwMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+My4g7LWc7KKFIOuqqeyggeyngDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJEMSIgZGF0YS10bz0iRDIiIGRhdGEtbGFiZWw9IjHstIgg65KkIOychOy5mCDrsJTrgJwg8J+Mqu+4jyI+CiAgPHJlY3QgeD0iNTA5LjkxMiIgeT0iNzkiIHdpZHRoPSIxMTYuMjU0MDAwMDAwMDAwMDIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1NjguMDM5IiB5PSI5NC4xNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+Mey0iCDrkqQg7JyE7LmYIOuwlOuAnCDwn4yq77iPPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJCQVNFIiBkYXRhLWxhYmVsPSLsp4Dsg4Eg7Ya17KCc7IaMCuyViO2FjOuCmCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iMTA1Ljg4MzMzMzMzMzMzMzMzIiB3aWR0aD0iMTE4LjI3MyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTE1LjEzNjUiIHk9IjEzMi43ODMzMzMzMzMzMzMzMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTE1LjEzNjUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7sp4Dsg4Eg7Ya17KCc7IaMPC90c3Bhbj48dHNwYW4geD0iMTE1LjEzNjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyViO2FjOuCmDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJEMyIgZGF0YS1sYWJlbD0iRDMiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iOTY1LjM2OTAwMDAwMDAwMDEiIHk9IjExNC4zMzMzMzMzMzMzMzMzMyIgd2lkdGg9IjYwIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9Ijk5NS4zNjkwMDAwMDAwMDAxIiB5PSIxMzIuNzgzMzMzMzMzMzMzMzMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkQzPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJEMSIgZGF0YS1sYWJlbD0i65Oc66GgIDEg8J+agQrspJHqs4TquLAg7Jet7ZWgIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM0Ny42MzkiIHk9Ijg0Ljc1IiB3aWR0aD0iMTE4LjI3MyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0MDYuNzc1NSIgeT0iMTExLjY1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0MDYuNzc1NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuuTnOuhoCAxIPCfmoE8L3RzcGFuPjx0c3BhbiB4PSI0MDYuNzc1NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7KSR6rOE6riwIOyXre2VoDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJEMiIgZGF0YS1sYWJlbD0i65Oc66GgIDIg8J+agQrspJHqs4TquLAg7Jet7ZWgIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjY3MC4xNjYiIHk9Ijg0Ljc1IiB3aWR0aD0iMTE4LjI3MyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI3MjkuMzAyNSIgeT0iMTExLjY1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI3MjkuMzAyNSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuuTnOuhoCAyIPCfmoE8L3RzcGFuPjx0c3BhbiB4PSI3MjkuMzAyNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7KSR6rOE6riwIOyXre2VoDwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] Ad-hoc 네트워크 3대장 전격 대조 (3단 표 - 1순위)**

단순히 FANET만 쓰는 것보다 그 뿌리가 되는 MANET(사람)과 VANET(자동차)의 한계점과 3차원 기동성을 대조하는 것이 완벽한 득점 포인트입니다.

| **핵심 척도**          | **🚶‍♂️ MANET (모바일/사람)**                      | **🚗 VANET (자동차)**                                                | **🚁 FANET (공중 드론) 🚨**                                                                                                 |
| :----------------- | :-------------------------------------------- | :---------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| **개념 / 환경**        | 사람이 들고 다니는 폰, 노트북끼리 연결. (2D 평면).              | 도로 위를 달리는 자동차(V2V)끼리 연결. (2D 도로망).                                | **공중을 나는 드론끼리 연결.** (3D 입체 공간).                                                                                         |
| **기동성 / 토폴로지**     | **'가장 느림'.** 사람 걸음 속도라 네트워크 토폴로지 변화가 적고 안정적임. | **'빠름 (방향 예측 가능)'.** 자동차 속도라 빠르지만, 결국 도로라는 정해진 선 안에서만 움직여 예측이 쉬움. | **'극강의 속도 (예측 불가) 💯'.** 위/아래 3차원으로 시속 수십\~수백km로 날아다녀, 통신 링크가 1초 단위로 끊어지고 휙휙 바뀜.                                        |
| **핵심 특성 / 장애물 🚨** | 배터리 제약이 크고 빌딩 등 장애물이 많음.                      | 자동차라 배터리 걱정은 거의 없음. 빌딩숲(터널) 차단 문제 발생.                             | **\[초정밀 에너지 제약 💯]** 무게 때문에 배터리가 작아, 비행과 통신에 쓸 전력 배분이 생명. **\[LOS 확보 용이 💯]** 공중이라 장애물이 없어 직진파(Line of Sight) 통신 거리가 긺. |
| **라우팅 / 과제**       | AODV, DSR 등 전통적인 반응형 라우팅 사용.                  | GPS를 이용한 위치 기반 라우팅.                                               | 잦은 끊김을 극복하기 위한 **'위치 기반(GPS)' 및 '강화학습 기반 3D 라우팅' 알고리즘 고도화가 필수.**                                                        |

#### **IV. \[결론/제언] 저궤도 위성(LEO)과 결합한 초연결 6G 아키텍처로의 진화**

* **(키워드 위주 2줄 마무리)** "드론끼리의 FANET만으로는 지상 통제소로의 백홀(Backhaul) 링크가 끊어질 위험이 존재합니다. 향후에는 수만 대의 드론 FANET 노드가 스타링크 같은 **'저궤도 위성(LEO)' 및 6G 비지상 네트워크(NTN)와 직접 연결되는 입체적(3D) 초연결 통신망 아키텍처로 진화하여 인류의 재난 대응 체계를 혁신할 것입니다.**"
