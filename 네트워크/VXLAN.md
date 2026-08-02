### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (VLAN의한계, VXLAN의해법) — 3~4줄
Ⅱ. 캡슐화원리 - MAC-in-UDP (본론①, 도식 1개 필수)
Ⅲ. VTEP와VNI - 핵심메커니즘, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

**VLAN**은 IEEE802.1Q표준으로 **12비트태그**만사용해 최대 **4096개**논리망만구분가능했습니다 — 앞서다룬 \*\*"MSA(수많은마이크로서비스)"\*\*나 **대규모클라우드데이터센터**환경에서는 이 **4096개한계**가 곧벽에부딪힙니다. VXLAN(VirtualExtensibleLAN)은 이문제를 **24비트식별자**로 확장해 해결하며, 물리적으로떨어진데이터센터끼리도 **같은L2망처럼**보이게합니다.

### Ⅱ. 캡슐화원리 — MAC-in-UDP

| 개념                     | 내용                                          |
| :--------------------- | :------------------------------------------ |
| **캡슐화**(Encapsulation) | 원본 **이더넷프레임전체를, UDP패킷안에통째로담아**전송            |
| **오버레이네트워크**           | 물리적네트워크(언더레이) **위에**, 논리적인가상네트워크를 **덧씌우는것** |
| **효과**                 | 서로다른데이터센터에있는서버들도, **같은L2브로드캐스트도메인**처럼동작     |

→ 암기: **"원본프레임을통째로 UDP봉투에넣어서 배송한다"** — 앞서다룬 \*\*"전자봉투"\*\*의구조(내용물+포장)와 유사하게, VXLAN도 **"원본이더넷프레임(내용물)을UDP(포장)로감싸"** 전송합니다.

### 도식화 제안

```
[원본이더넷프레임]
     ↓ 캡슐화(VXLAN헤더추가)
[VXLAN헤더 + UDP헤더 + IP헤더] + [원본이더넷프레임 전체]
     ↓ 물리망(IP네트워크)을통해전송
[목적지에서 캡슐제거] → 원본이더넷프레임 복원
```

### Ⅲ. VTEP와VNI — 핵심메커니즘, 핵심 배점

**함정 방지: "캡슐화한다"고만답하면절반. 누가캡슐을만들고, 어떻게4096개한계를넘는지 구체적으로보여줘야완성됩니다.**

| 개념                              | 내용                                                             |
| :------------------------------ | :------------------------------------------------------------- |
| **VTEP**(VXLANTunnelEndPoint)   | **캡슐화·역캡슐화를수행하는지점**— 물리스위치또는 **가상스위치(hypervisor내)**            |
| **VNI**(VXLANNetworkIdentifier) | **24비트**식별자— **최대1,677만개**의가상네트워크구분가능(VLAN의4096개 대비 **압도적확장**) |
| **동작흐름**                        | 송신측VTEP가 **캡슐화**→ IP망으로전송 → 수신측VTEP가 **VNI확인후캡슐제거** → 원본프레임전달  |

→ 암기: **"VTEP가 봉투를싸고푸는집배원,VNI는 24비트라서 VLAN보다 수천배많은구역을구분할수있는우편번호"** — 앞서다룬 \*\*"IP주소구조의네트워크/호스트분할"\*\*처럼, VNI도 \*\*"논리적으로격리된공간을 숫자하나로식별"\*\*하는 동일한원리를 **훨씬넓은규모**로 확장한 것입니다.

### 도식화 제안

```
[데이터센터A]                          [데이터센터B]
[VM1] → [VTEP-A] ══VNI=5000으로캡슐화══→ [VTEP-B] → [VM2]
                    (물리적으로떨어진 IP망을통과)
                    
결과: VM1과VM2는 "같은L2망(VNI 5000)"처럼 서로통신
(물리적위치와무관하게, 논리적으로같은네트워크)
```

**활용**: 앞서다룬 \*\*"MSA"\*\*나 \*\*"클라우드멀티테넌시"\*\*환경에서, VXLAN은 \*\*"수많은고객/서비스를서로격리된가상망으로분리"\*\*하는 핵심기반기술입니다 — 앞서다룬 \*\*"SDN컨트롤러"\*\*가 이 VTEP설정을 **중앙에서소프트웨어로관리**하는 경우가 많아, VXLAN은 종종 **SDN기반오버레이네트워킹**의 핵심구성요소로 함께쓰입니다.

### Ⅳ. 결론

VXLAN은 **"VLAN의4096개한계를 24비트VNI로대폭확장하고, 원본프레임을UDP로캡슐화해 물리적위치에상관없이 논리적으로같은네트워크처럼동작하게만드는"** 오버레이가상화기술입니다 — 이는 앞서다룬 \*\*VLSM(IP주소공간을세밀하게나누는것)\*\*과는 \*\*"물리적경계자체를소프트웨어로초월한다"\*\*는 점에서 다른차원의해법이며, 앞서다룬 \*\*SDN(중앙집중제어)\*\*과 결합해 **대규모클라우드데이터센터,MSA환경**의 필수기반기술로 자리잡았습니다 — 오늘하루다룬 방대한네트워크시리즈(QoS→WFQ→SDN→OpenRAN→VXLAN)전체가, **"물리적제약을소프트웨어로하나씩극복해가는"** 네트워크가상화의 완결된여정을 보여줍니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "아마존, 구글 같은 클라우드 센터에 가상 서버(VM)가 수십만 개씩 생기자, 기존의 네트워크 방 나누기 기술인 'VLAN'은 박살이 났다. 방 번호표(VLAN ID)가 4,000장뿐이라 수만 개의 서버를 그룹 지을 수 없었고, 서울 센터에서 부산 센터로 서버를 이사(마이그레이션)시킬 때 IP 대역이 바뀌어 서비스가 끊기는 치명적 제약(L2 종속)이 있었다. 이 한계를 깨부순 것이 \*\*'VXLAN(가상 확장 랜)'\*\*이다. VXLAN은 방 번호표(VNI)를 24비트로 확 늘려 무려 \*\*'1,600만 개'\*\*의 가상 네트워크 방을 만들 수 있게 했다(확장성 해결). 또한, 서울의 L2 패킷(MAC)을 L3 IP(UDP) 봉투로 통째로 감싸서(캡슐화) 부산으로 던져주는 터널 기술을 썼다. 이로 인해 서울과 부산 사이에 깔린 수많은 물리적 라우터를 무시하고, 마치 **'두 데이터센터가 하나의 커다란 공유기 밑에 찰싹 붙어 있는 것처럼(거대한 논리적 L2 평면망)'** 착각하게 만들었다. 덕분에 가상 서버가 전국 어디로 이사를 가도 IP 변경 없이 서비스가 유지된다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 클라우드 가상 머신의 무한 확장, VXLAN 개요**

* **정의:** 기존 802.1Q VLAN의 4,096개 확장성 한계를 극복하기 위해, **기존 L2 프레임(MAC)을 L3 패킷(UDP/IP)으로 캡슐화(MAC-in-UDP)하여 물리적인 L3 네트워크 위에서 거대한 논리적 L2 가상 네트워크(Overlay)를 덮어씌워 제공**하는 네트워크 가상화 기술.
* **도입 목적:** 클라우드 컴퓨팅(멀티 테넌트) 환경에서 수십만 개의 가상 머신(VM)을 논리적으로 격리(ID 확장)하고, 물리적인 라우터(L3) 장벽을 뚫고 IP 변경 없이 VM을 맘대로 이주(Live Migration)시키기 위함.

#### **\<span style="font 실="font-size: 1.5em; font-weight: bold;">II. \[본론 1] (극단적 단순화 버전) L3 라우터 망을 뚫어버리는 VXLAN 터널링 파이프라인**

복잡한 패킷 헤더 구조를 빼고, **물리적 망(L3) 위에 가상의 덮개 망(L2 Overlay)을 씌워 연결하는 터널 입구(VTEP)의 역할**만 직관적으로 그렸습니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5NDMuOTY5IDE5My44IiB3aWR0aD0iOTQzLjk2OSIgaGVpZ2h0PSIxOTMuOCIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iVlhMQU5fTDJfX19NQUNpblVEUF8iIGRhdGEtbGFiZWw9IlZYTEFO7J2YIEwyIOuFvOumrOyggSDsl7DsnqUgKE1BQy1pbi1VRFAg7Lqh7IqQ7ZmUKSI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iODYzLjk2OSIgaGVpZ2h0PSIxMTMuODAwMDAwMDAwMDAwMDEiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI4NjMuOTY5IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+VlhMQU7snZggTDIg64W866as7KCBIOyXsOyepSAoTUFDLWluLVVEUCDsuqHsipDtmZQpPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJWTTEiIGRhdGEtdG89IlZURVAxIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE5OC43MjYsMTEwLjkgMjQ2LjcyNiwxMTAuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVlRFUDEiIGRhdGEtdG89IlZURVAyIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLqsbDrjIDtlZwgTDMg7J247YSw64S3L+udvOyasO2EsCDrp50KKO2IrOuqhe2VmOqyjCDthrXqs7wg8J+agCkiIHBvaW50cz0iMzI3LjIwNzk5OTk5OTk5OTk3LDExMC45IDU3My4wNDIsMTEwLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlZURVAyIiBkYXRhLXRvPSJWTTIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNjU3Ljk3LDExMC45IDcwNS45NywxMTAuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJWVEVQMSIgZGF0YS10bz0iVlRFUDIiIGRhdGEtbGFiZWw9IuqxsOuMgO2VnCBMMyDsnbjthLDrhLcv65287Jqw7YSwIOunnQoo7Yis66qF7ZWY6rKMIO2GteqzvCDwn5qAKSI+CiAgPHJlY3QgeD0iMzcxLjIwNzk5OTk5OTk5OTk3IiB5PSI4Ny45IiB3aWR0aD0iMTU3LjgzNDAwMDAwMDAwMDAzIiBoZWlnaHQ9IjQ0LjYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNDUwLjEyNSIgeT0iMTEwLjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSI0NTAuMTI1IiBkeT0iLTMuMzAwMDAwMDAwMDAwMDAwNyI+6rGw64yA7ZWcIEwzIOyduO2EsOuEty/rnbzsmrDthLAg66edPC90c3Bhbj48dHNwYW4geD0iNDUwLjEyNSIgZHk9IjE0LjMiPijtiKzrqoXtlZjqsowg7Ya16rO8IPCfmoApPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlZNMSIgZGF0YS1sYWJlbD0i7ISc7Jq4IOyEvO2EsCBWTSDwn5K7CkwyIO2MqO2CtyDsj5jquLAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMTQyLjcyNiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTI3LjM2MyIgeT0iMTEwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjEyNy4zNjMiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7shJzsmrgg7IS87YSwIFZNIPCfkrs8L3RzcGFuPjx0c3BhbiB4PSIxMjcuMzYzIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5MMiDtjKjtgrcg7I+Y6riwPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlZURVAxIiBkYXRhLWxhYmVsPSJWVEVQMSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyNDYuNzI2IiB5PSI5Mi40NSIgd2lkdGg9IjgwLjQ4MiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIyODYuOTY3IiB5PSIxMTAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+VlRFUDE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlZURVAyIiBkYXRhLWxhYmVsPSJWVEVQMiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NzMuMDQyIiB5PSI5Mi40NSIgd2lkdGg9Ijg0LjkyOCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI2MTUuNTA2MDAwMDAwMDAwMSIgeT0iMTEwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlZURVAyPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJWTTIiIGRhdGEtbGFiZWw9Iuu2gOyCsCDshLzthLAgVk0g8J+SuwrslrQ/IOyasOumrCDrsJTroZwg7JiG7J2064SkPyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3MDUuOTciIHk9Ijg0IiB3aWR0aD0iMTgxLjk5ODk5OTk5OTk5OTk3IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI3OTYuOTY5NSIgeT0iMTEwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9Ijc5Ni45Njk1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+67aA7IKwIOyEvO2EsCBWTSDwn5K7PC90c3Bhbj48dHNwYW4geD0iNzk2Ljk2OTUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyWtD8g7Jqw66asIOuwlOuhnCDsmIbsnbTrhKQ/PC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 기존 VLAN 한계 붕괴! VXLAN 핵심 기술 전격 대조 (3단 표 - 1순위)**

가장 중요한 출제 포인트는 **'아이디(ID) 개수가 몇 개로 늘어났는가'**와 캡슐화를 하는 주체인 \*\*'VTEP'\*\*의 존재 의의를 대조하는 것입니다.

| **핵심 척도 (비교 잣대)**                  | **🛑 기존 802.1Q VLAN**                                                                                             | **🚀 VXLAN (클라우드 표준) 🚨**                                                                                                     |
| :--------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| **🚨 네트워크 식별자(ID)의 비트 수 및 최대 확장성** | **'12 Bit (최대 4,096개) / 확장 불가'.** 아무리 방을 쪼개도 4천 개가 끝임. 수만 명의 고객이 쓰는 현대 클라우드 멀티 테넌트(Multi-tenant) 환경을 절대 감당할 수 없음. | **'VNI 24 Bit (최대 1,600만 개) 💯'.** VXLAN Network Identifier(VNI)라는 24비트짜리 식별자를 써서, **방을 1,677만 7,216개까지 무한에 가깝게 쪼개버림.**       |
| **통신 범위의 물리적 제약 (L2 vs L3 의존성)**   | **'L2(스위치) 구역 안에서만 통신 가능'.** 물리적 라우터(L3)를 만나면 패킷이 차단됨. (서버를 물리적으로 멀리 떨어진 다른 센터로 이사시킬 수 없음).                       | **'물리적 L3 망을 무시하는 Overlay 💯'.** 패킷을 UDP/IP로 감싸버리므로, 중간에 라우터가 몇 개든 인터넷을 타든 상관없이 뚫고 지나가 **전국을 거대한 하나의 L2 망으로 덮어버림.**           |
| **✨ 캡슐화를 주도하는 가상 터널 엔드포인트**        | (스위치 내부의 태깅/언태깅)                                                                                                  | **\[VTEP (VXLAN Tunnel End Point)]** 기존 L2 패킷을 캡슐화(MAC-in-UDP)하여 터널로 쏴주고, 받는 쪽에서 봉투를 뜯어(역캡슐화) 오리지널 L2 패킷을 복원하는 VXLAN의 핵심 심장부. |

#### **IV. \[결론/제언] 브로드캐스트 폭풍(BUM 트래픽) 억제를 위한 BGP EVPN 도입**

* **(키워드 위주 2줄 마무리)** "VXLAN은 클라우드 가상화의 구세주지만, 수만 개의 서버가 동네방네 떠드는 브로드캐스트(BUM 트래픽)마저 터널을 타고 전국 센터로 퍼져나가 네트워크 대역폭을 마비시키는 치명적 단점이 있습니다. 이를 막기 위해, 통신을 시도하기 전에 라우터들끼리 MAC 주소를 미리 싹 다 교환해 놓고 목적지를 정확히 콕 집어 유니캐스트로만 쏘게 만드는 **'BGP EVPN' 제어 평면(Control Plane) 프로토콜과의 융합이 현대 소프트웨어 정의 데이터센터(SDDC)의 필수 아키텍처로 자리 잡았습니다.**"
