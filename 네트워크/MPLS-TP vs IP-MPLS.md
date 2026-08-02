### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (MPLS공통기반, 두갈래로나뉜이유) — 3~4줄
Ⅱ. IP-MPLS 핵심특징 (본론①, 도식 1개 필수)
Ⅲ. MPLS-TP 핵심특징, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

**MPLS**(MultiProtocolLabelSwitching)는 앞서다룬 \*\*"IP주소를매번보고라우팅결정"\*\*하는 대신, \*\*"레이블(꼬리표)만보고빠르게전달"\*\*하는 공통기술입니다 — 이위에서 **IP-MPLS**는 \*\*"IP망의유연성"\*\*을, **MPLS-TP**는 \*\*"전통전송망의확실성"\*\*을 각각 추구하며 갈라졌습니다.

### Ⅱ. IP-MPLS — IP망의유연성

| 항목       | 내용                                         |
| :------- | :----------------------------------------- |
| **제어방식** | \*\*IP라우팅프로토콜(OSPF,BGP등)\*\*로 **동적으로**경로결정 |
| **장애복구** | 라우팅프로토콜이 **자동으로새경로재계산**(수초\~수십초)           |
| **장점**   | 앞서다룬 **혼잡제어,QoS**와결합해 **트래픽상황에유연하게적응**     |
| **적합대상** | **데이터트래픽중심**의 일반인터넷백본,데이터센터                |

→ 암기: **"IP라우팅으로 스스로알아서길을찾는, 유연하지만조금느린복구"**

### 도식화 제안

```
[IP-MPLS]
[라우터A] ══(IP라우팅프로토콜로 동적경로결정)══→ [라우터B]
     ↓ 장애발생
라우팅프로토콜이 자동으로 새경로 재계산(수초~수십초)
```

### Ⅲ. MPLS-TP — 전송망의확실성, 핵심 배점

**함정 방지: "MPLS의변형"이라고만답하면절반. 왜"TP(TransportProfile)"라는이름이붙었는지, 그리고IP-MPLS와정반대의설계철학을보여줘야완성됩니다.**

| 항목                  | 내용                                                             |
| :------------------ | :------------------------------------------------------------- |
| **IP기능제거**(핵심차이)    | **IP라우팅기능을완전히배제**— 오직 **연결지향적(ConnectionOriented)** 경로만사용      |
| **사전설정경로**(정적)      | 경로를 **관리자가미리설정**(NMS,네트워크관리시스템) — 앞서다룬 **IntServ의사전예약**과유사한 철학 |
| **초고속장애복구**         | 앞서다룬 **SONET/SDH(전통전화망)급 50ms이내복구** — IP-MPLS보다 **훨씬빠르고예측가능**  |
| **OAM**(운영·관리·유지보수) | ITU-T 표준화된 **강력한장애감시·성능측정기능** 내장                               |

→ 암기: **"IP기능을빼버리고,경로는미리정해두고,장애나면50ms안에복구하고,감시기능이철저하다"** — 앞서다룬 \*\*"IntServ(사전예약,확실한보장,낮은확장성)vsDiffServ(딱지기반,느슨한보장,높은확장성)"\*\*의 대비가, 여기서 \*\*"MPLS-TP(사전설정,확실한보장)vsIP-MPLS(동적라우팅,유연한적응)"\*\*로 정확히 재현됩니다.

### 도식화 제안

```
[MPLS-TP]
[관리자] → 경로를 미리설정(정적,Connection-Oriented)
     ↓
[노드A] ══(사전설정된고정경로)══→ [노드B]
     ↓ 장애발생
사전에준비된 백업경로로 50ms이내 즉시전환(예측가능한복구)

[비교]
IP-MPLS: 동적,유연,복구는느림(수초)
MPLS-TP: 정적,확실,복구는초고속(50ms)
```

**적합대상**: MPLS-TP는 **통신사백본의핵심전송망(코어망)**, 특히 **음성,금융거래등"끊기면안되는"** 서비스에 적합— 앞서다룬 \*\*"5G특화망의Type1(자가구축)"\*\*처럼, \*\*"확실성이생명인영역"\*\*에 쓰입니다.

### Ⅳ. 결론

IP-MPLS와MPLS-TP는 **"같은MPLS기술을기반으로하지만, IP-MPLS는유연성(동적라우팅)을,MPLS-TP는확실성(사전설정,초고속복구)을"** 추구하는 정반대설계철학입니다 — 이는 앞서다룬 **IntServ/DiffServ**의 대립과 \*\*본질적으로같은트레이드오프(엄격한보장vs유연한확장성)\*\*이며, 실제통신사는 \*\*"데이터트래픽구간엔IP-MPLS,핵심전송망(음성,금융)구간엔MPLS-TP"\*\*를 **함께혼용**해 사용합니다 — 오늘하루다룬 방대한네트워크시리즈전체(SCTP→VXLAN→슬라이싱→MPLS)가, **"목적에맞는프로토콜을선택하고조합하는"** 네트워크설계의 근본원리로 마무리됩니다.

### **1. 답안 전개 스토리** 

> "라우터가 매번 IP 주소를 까보느라 느려지는 병목을 해결하기 위해, 패킷에 '번호표(라벨)'만 딱 붙여서 고속으로 휙휙 던지는 기술이 'MPLS'다. 이 기술은 성향이 다른 두 형제로 발전했다. 첫째는 라우터 중심의 \*\*'IP-MPLS'\*\*다. 라우터들이 똑똑하게 서로 소통하며 알아서(동적) 길을 찾는다. 유연성은 최고지만 중간에 길이 끊어지면 새 길을 찾느라 딜레이가 생겨 통신 품질이 들쭉날쭉하다. 둘째는 절대 끊기면 안 되는 통신사/기업 전용선을 위한 \*\*'MPLS-TP'\*\*다. 이놈은 IP-MPLS에서 '스스로 길을 찾는 복잡한 뇌'를 싹 뽑아버렸다(경량화). 대신 중앙 관리자가 수동(정적)으로 철길을 쫙 깔아둔다. 길을 찾을 필요가 없으니 딜레이가 항상 일정하고, 철길이 폭파되어도 미리 깔아둔 예비 철길로 0.05초(50ms) 만에 휙 갈아타는 강력한 유지보수(OAM) 능력을 갖췄다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 라벨 스위칭의 진화, MPLS-TP와 IP-MPLS 개요**

* **MPLS 공통 개념:** 패킷을 IP 주소 라우팅 대신 짧은 '라벨(Label)'로 고속 스위칭하는 기반 기술.
* **IP-MPLS:** 인터넷 망의 유연성을 극대화하기 위해 **'동적 라우팅 프로토콜(OSPF 등)'**을 사용하여 IP 기반의 트래픽 엔지니어링을 수행하는 기술.
* **MPLS-TP (Transport Profile):** IP-MPLS에서 복잡한 L3 제어 기능(동적 라우팅)을 제거하고, 통신사 캐리어 전송망(TDM/광통신)에 필수적인 \*\*'OAM(운용/유지보수) 및 50ms 이내 보호 절체(Protection) 기능'\*\*을 극대화한 전송망 전용 프로토콜.

#### **II. \[본론 1] (극단적 단순화 버전) 스스로 길 찾기(IP) vs 깔아둔 철길 달리기(TP)**

복잡한 프로토콜 스택 대신, **길이 끊어졌을 때의 대처 방식(우회 탐색 vs 즉시 예비선 탑승)**만 직관적으로 그렸습니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NTguNTUwOTk5OTk5OTk5OSA0MjMuOSIgd2lkdGg9IjY1OC41NTA5OTk5OTk5OTk5IiBoZWlnaHQ9IjQyMy45IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJJUE1QTFNfdnNfTVBMU1RQX19fX19fIiBkYXRhLWxhYmVsPSJJUC1NUExTIHZzIE1QTFMtVFAg6rK966GcIOyDneyEsSDrsI8g7J6l7JWgIOuMgOyymCDrsKnsi50iPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjU3OC41NTA5OTk5OTk5OTk5IiBoZWlnaHQ9IjM0My45IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNTc4LjU1MDk5OTk5OTk5OTkiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5JUC1NUExTIHZzIE1QTFMtVFAg6rK966GcIOyDneyEsSDrsI8g7J6l7JWgIOuMgOyymCDrsKnsi508L3RleHQ+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMV9JUE1QTFNfXyIgZGF0YS1sYWJlbD0iMS4gSVAtTVBMUyAo7J247YSw64S366edL+uPmeyggSDwn6egKSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMjIxLjQwOSIgaGVpZ2h0PSIyODMuOSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjIyMS40MDkiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjY4IiB5PSI5OCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij4xLiBJUC1NUExTICjsnbjthLDrhLfrp50v64+Z7KCBIPCfp6ApPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMl9NUExTVFBfX18iIGRhdGEtbGFiZWw9IjIuIE1QTFMtVFAgKO2GteyLoOyCrCDsoITshqHrp50v7KCV7KCBIPCfmoIpIj4KICA8cmVjdCB4PSIyOTcuNDA5IiB5PSI4NCIgd2lkdGg9IjMwNS4xNDIiIGhlaWdodD0iMjgzLjkiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSIyOTcuNDA5IiB5PSI4NCIgd2lkdGg9IjMwNS4xNDIiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjMwOS40MDkiIHk9Ijk4IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjIuIE1QTFMtVFAgKO2GteyLoOyCrCDsoITshqHrp50v7KCV7KCBIPCfmoIpPC90ZXh0Pgo8L2c+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkkxIiBkYXRhLXRvPSJJMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i6ri4IOuBiuyWtOynkCEiIHBvaW50cz0iMTY2LjcwNDUsMTY0LjkgMTY2LjcwNDUsMjgxLjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlQxIiBkYXRhLXRvPSJUMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i6ri4IOuBiuyWtOynkCEiIHBvaW50cz0iNDQ5Ljk4LDE2NC45IDQ0OS45OCwyODEuMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJJMSIgZGF0YS10bz0iSTIiIGRhdGEtbGFiZWw9Iuq4uCDrgYrslrTsp5AhIj4KICA8cmVjdCB4PSIxMzEuNzA0NSIgeT0iMjA3LjkiIHdpZHRoPSI2OS4zMjgiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxNjYuMzY4NDk5OTk5OTk5OTgiIHk9IjIyMy4wNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+6ri4IOuBiuyWtOynkCE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iVDEiIGRhdGEtdG89IlQyIiBkYXRhLWxhYmVsPSLquLgg64GK7Ja07KeQISI+CiAgPHJlY3QgeD0iNDE0Ljk4IiB5PSIyMDcuOSIgd2lkdGg9IjY5LjMyOCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjQ0OS42NDQiIHk9IjIyMy4wNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+6ri4IOuBiuyWtOynkCE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkkxIiBkYXRhLWxhYmVsPSLstpzrsJzsp4AiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTIzLjQ5OTUiIHk9IjEyOCIgd2lkdGg9Ijg2LjQxIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTY2LjcwNDUiIHk9IjE0Ni40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7Lac67Cc7KeAPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJJMiIgZGF0YS1sYWJlbD0i65iR65iR7ZWcIOudvOyasO2EsOuTpArslYzslYTshJwg7IOIIOq4uCDtg5Dsg4kg7Iuc7J6RIQrinKgg65Sc66CI7J20KOyngOyXsCkg67Cc7IOdIOKcqCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3MiIgeT0iMjgxLjIiIHdpZHRoPSIxODkuNDA5IiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTY2LjcwNDUiIHk9IjMxNi41NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTY2LjcwNDUiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj7rmJHrmJHtlZwg65287Jqw7YSw65OkPC90c3Bhbj48dHNwYW4geD0iMTY2LjcwNDUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyVjOyVhOyEnCDsg4gg6ri4IO2DkOyDiSDsi5zsnpEhPC90c3Bhbj48dHNwYW4geD0iMTY2LjcwNDUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuKcqCDrlJzroIjsnbQo7KeA7JewKSDrsJzsg50g4pyoPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlQxIiBkYXRhLWxhYmVsPSLstpzrsJzsp4AiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDA2Ljc3NSIgeT0iMTI4IiB3aWR0aD0iODYuNDEiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0NDkuOTc5OTk5OTk5OTk5OTYiIHk9IjE0Ni40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7Lac67Cc7KeAPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJUMiIgZGF0YS1sYWJlbD0i6rOg66+8IOyViCDtlaghCuq0gOumrOyekOqwgCDrr7jrpqwg6rmU7JWE65GUCuKcqCDsmIjruYQg7LKg6ri466GcIDAuMDXstIgg66eM7JeQIOqwiOyVhO2DkCDinKgiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzEzLjQwOSIgeT0iMjgxLjIiIHdpZHRoPSIyNzMuMTQyIiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0NDkuOTgiIHk9IjMxNi41NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNDQ5Ljk4IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+6rOg66+8IOyViCDtlaghPC90c3Bhbj48dHNwYW4geD0iNDQ5Ljk4IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7qtIDrpqzsnpDqsIAg66+466asIOq5lOyVhOuRlDwvdHNwYW4+PHRzcGFuIHg9IjQ0OS45OCIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+4pyoIOyYiOu5hCDssqDquLjroZwgMC4wNey0iCDrp4zsl5Ag6rCI7JWE7YOQIOKcqDwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 통신망의 목적이 낳은 두 형제, IP-MPLS vs MPLS-TP 전격 대조 (3단 표)**

이 둘을 가르는 가장 큰 차이점인 제어 평면의 **'라우팅 방식(동적/정적)'**과, MPLS-TP의 무기인 **'강력한 OAM(운용 관리)'**을 대조해야 합니다.

| **핵심 척도 (비교 잣대)**                  | **🧠 IP-MPLS (라우터 인터넷망 진영)**                                                                 | **🚂 MPLS-TP (캐리어 전송망 진영) 🚨**                                                                                    |
| :--------------------------------- | :------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------- |
| **경로 생성/제어 방식 (Control Plane)**    | **'장비가 스스로 길을 찾는 동적 제어'.** L3 라우터들이 OSPF, BGP 등의 프로토콜로 통신하며 스스로 최적의 경로를 동적(Dynamic)으로 찾아냄.   | **'수동으로 철길을 까는 정적 제어 💯'.** 동적 라우팅 기능을 싹 빼버림. 중앙 NMS 시스템이나 관리자가 수동(Static)으로 **절대 경로(철길)를 미리 깔아둠.**               |
| **망 장애 발생 시 복구 메커니즘 (Protection)** | **'복구(우회로 탐색)에 시간 소요'.** 망이 끊어지면 라우터들이 새 길을 다시 계산하느라 시간이 걸림 (수 초 이상 딜레이). 트래픽 지터(Jitter) 발생. | **'0.05초 (50ms) 이내 즉시 절체 💯'.** 장애가 나면 고민 없이, 미리 깔아둔 예비 경로(Protection Path)로 **50ms 안에 순식간에 스위칭(갈아탐). 통신 끊김 없음.** |
| **OAM (운용, 관리, 유지보수) 및 QoS 보장 능력** | 복잡한 IP 라우팅에 집중하느라, 전송망 수준의 꼼꼼한 모니터링(OAM) 기능이 매우 부족함.                                         | **\[OAM 기능 극대화 및 고정 딜레이]** 경로가 고정되어 딜레이(지연시간)가 변하지 않음(결정론적 전송). 장애 감지 및 성능 모니터링(OAM)에 모든 스펙을 올인함.                 |
| **주요 적용처 및 목적**                    | 인터넷망, 클라우드, 기업용 L3 VPN                                                                       | 기지국 백홀 망(PTN/SPTN), **5G 코어 전송망**                                                                                 |

#### **IV. \[결론/제언] 5G 초저지연을 향한 SDN 제어 평면과의 융합 (SDN-TP)**

* **(키워드 위주 2줄 마무리)** "MPLS-TP는 기존 통신사 광전송망(SDH/SONET)을 대체하는 완벽한 기술이지만, 관리자가 수동으로 경로를 깔아줘야 하는 불편함이 큽니다. 다가오는 5G/6G 환경에서는 이 TP 장비의 뇌를 중앙의 SDN 컨트롤러로 통합하여, 필요할 때마다 소프트웨어로 철길(경로)을 자동 생성해 주는 **'SDN 기반 패킷 전송망(SDN-TP 또는 SPTN)' 아키텍처로 진화하고 있습니다.**"
