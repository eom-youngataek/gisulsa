### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (다중화필요성, PDH의등장) — 3~4줄
Ⅱ. PDH - 비동기다중화의문제, 핵심함정 (본론①, 도식 1개 필수)
Ⅲ. SDH/SONET - 동기식의해법, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

앞서다룬 \*\*"NOMA,WFQ"\*\*가 \*\*"자원을어떻게나눠쓸지"\*\*를 다뤘다면, 디지털계위는 \*\*"여러개의저속신호(전화통화등)를, 하나의고속선로에어떻게합쳐서(다중화)보낼지"\*\*에대한 통신사백본망의 근본기술입니다. **PDH→SDH/SONET**순으로 발전했습니다.

### Ⅱ. PDH — 비동기다중화의문제

| 항목                                      | 내용                                                           |
| :-------------------------------------- | :----------------------------------------------------------- |
| **PDH**(PlesiochronousDigitalHierarchy) | **"거의동기화된"**— 각장비가 **독립된클럭**으로 동작,미세하게속도가다름                  |
| **다중화방식**                               | 여러개의저속신호(예:1.5Mbps)를 **비트단위로끼워넣어**(Bit Interleaving) 고속신호로합침 |
| **핵심문제**(함정)                            | 클럭이 **완전히똑같지않아서**, 특정신호하나를 **꺼내려면(Drop) 전체를역다중화**해야함         |

→ 암기: **"각자시계가조금씩달라서, 하나만꺼내려해도 전체를다풀어야한다"** — 앞서다룬 \*\*"Go-Back-N ARQ"\*\*에서 **"하나틀리면전체를다시보내는"** 비효율과 유사하게, PDH는 **"하나만필요해도 전체구조를해체해야하는"** 근본적비효율을 안고있습니다.

### 도식화 제안

```
[PDH 다중화]
[신호1(1.5Mbps,클럭A)] ─┐
[신호2(1.5Mbps,클럭B)] ─┼─비트단위로끼워넣기→ [고속신호(45Mbps)]
[신호3(1.5Mbps,클럭C)] ─┘   (각클럭이미세하게다름)

[특정신호만꺼내려면]
고속신호 → 전체를역다중화(Demux) → 신호1,2,3 모두복원 → 필요한것만추출
(하나만필요해도, 전체를다풀어야하는비효율)
```

### Ⅲ. SDH/SONET — 동기식의해법, 핵심 배점

**함정 방지: "더빠른버전"이라고만답하면절반. "포인터(Pointer)"라는핵심메커니즘으로 PDH의근본문제를어떻게해결하는지보여줘야완성됩니다.**

| 항목            | 내용                                                                                      |
| :------------ | :-------------------------------------------------------------------------------------- |
| **동기화**(핵심혁신) | 전체네트워크가 **하나의공통기준클럭**(원자시계기반)에 **동기화**— 클럭차이문제자체를 제거                                    |
| **포인터방식**     | 각신호의 **정확한시작위치를 "포인터"로직접가리킴**— 앞서다룬 \*\*"슬라이딩윈도우"\*\*처럼, 필요한부분만 **바로찾아추출가능**(전체역다중화불필요) |
| **표준명칭**      | **SDH**(국제표준,유럽·아시아중심) = **SONET**(북미표준)— **본질적으로같은개념**,세부규격만다름                         |
| **초고속장애복구**   | 앞서다룬 \*\*MPLS-TP가"SONET/SDH급50ms복구"\*\*를목표로삼은이유 — **링구조**로 **백업경로가항상준비**되어있어 즉시전환       |

→ 암기: **"모두가같은시계를보니, 원하는신호의위치를포인터로바로가리킬수있다 — 전체를풀필요없이"** — 앞서다룬 \*\*"MPLS-TP"\*\*답안에서 \*\*"IP기능을제거하고, 사전설정된경로+50ms초고속복구"\*\*를 추구했던 이유가, 바로 이 \*\*SDH/SONET전송망의핵심가치(확실성,초고속복구)\*\*를 **패킷시대에도계승**하려는 것이었습니다.

### 도식화 제안

```
[SDH/SONET - 포인터방식]
[공통기준클럭에 전체동기화]
     ↓
[고속신호] = [포인터→신호1위치][포인터→신호2위치][포인터→신호3위치]...
     ↓ 신호2만필요하면
포인터를따라 신호2 위치로 즉시이동 → 전체역다중화없이 바로추출

[링구조 장애복구]
[노드A]══[노드B]══[노드C]
   ╲___________________╱ (백업경로,항상준비됨)
장애발생시 → 50ms이내 백업경로로 즉시전환
```

### Ⅳ. 결론

PDH는 \*\*"각장비가서로다른시계로돌아가는비효율적인비동기다중화"\*\*였고, SDH/SONET은 **"전체를하나의공통클럭으로동기화해, 포인터로필요한신호를즉시찾아낼수있게한"** 근본적해법입니다 — 이는 앞서다룬 \*\*"MPLS-TP가50ms급초고속복구,사전설정경로"\*\*를 지향했던 이유를 완전히설명합니다: SDH/SONET의 \*\*"동기화+포인터+링구조"\*\*라는 검증된확실성의철학을, 오늘날의패킷기반망에서도 **계승하려는것**이 MPLS-TP였습니다 — 오늘하루다룬 방대한통신인프라시리즈(MPLS-TP/IP-MPLS→디지털계위)전체가, \*\*"통신사백본망의핵심가치(확실성,초고속복구)는 기술이바뀌어도 그본질이계속이어져내려온다"\*\*는 결론으로 마무리됩니다.



### **1. 답안 전개 스토리 (핵심 압축)**

> "전 세계 수억 명의 음성과 데이터를 묶어서 고속도로(백본망)에 태우기 위한 통신 계급(규격)이다. 과거 구리선 시절의 \*\*PDH(유사 동기식)\*\*는 북미(T1)와 유럽(E1) 규격이 달라서 통신이 꼬였고, 시계(클럭)가 미세하게 달라서 억지로 빈 비트를 채워 묶어야 했다. 특히 묶은 신호 중 1개만 빼려 해도 짐을 통째로 다 풀었다가 다시 싸야 하는 끔찍한 비효율이 있었다. 이를 광통신(빛) 기반으로 해결한 것이 \*\*SONET(미국)\*\*과 \*\*SDH(국제표준)\*\*이다. 전 세계 통신망의 시계를 100% 일치(동기식)시켰다. 데이터 위치(포인터)를 정확히 알기 때문에, 짐을 다 풀지 않고도 달리는 고속 트럭에서 원하는 짐만 쏙 빼고 넣을 수 있는(Direct Drop & Insert) 기적의 효율을 달성했다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 글로벌 통신망의 통합 규격, 디지털 계위(Digital Hierarchy) 개요**

* **정의:** 여러 개의 저속 디지털 신호를 다중화(Multiplexing)하여 고속의 대용량 신호로 묶어 전송하기 위한 단계별 전송 속도와 다중화 구조의 국제 표준 규격.
* **발전 방향:** 북미/유럽/일본 등 지역마다 중구난방이었던 비동기(유사 동기)식 PDH 체계에서, 하나의 글로벌 시계(클럭)로 완벽히 통일된 광통신망 기반의 동기식 체계(SDH/SONET)로 진화함.

#### **II. \[본론 1] (극단적 단순화 버전) 짐을 푸는 방식: 무식한 PDH vs 스마트한 SDH**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4ODUuNTc5OTk5OTk5OTk5OSAzODcuNiIgd2lkdGg9Ijg4NS41Nzk5OTk5OTk5OTk5IiBoZWlnaHQ9IjM4Ny42IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfX19fXyIgZGF0YS1sYWJlbD0i7Ya17Iug66ed7JeQ7IScIOynkCjrjbDsnbTthLApIO2VmOuCmCDrubzripQg67Cp7IudIOywqOydtCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iODA1LjU3OTk5OTk5OTk5OTkiIGhlaWdodD0iMzA3LjYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI4MDUuNTc5OTk5OTk5OTk5OSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPu2GteyLoOunneyXkOyEnCDsp5Ao642w7J207YSwKSDtlZjrgpgg67m864qUIOuwqeyLnSDssKjsnbQ8L3RleHQ+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMV9QREhfX18iIGRhdGEtbGFiZWw9IjEuIFBESCAo6rO86rGwKTog7JmE7KCEIOu2hO2VtCI+CiAgPHJlY3QgeD0iNTYiIHk9IjIzNC43IiB3aWR0aD0iNzczLjU3OTk5OTk5OTk5OTkiIGhlaWdodD0iOTYuOSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjU2IiB5PSIyMzQuNyIgd2lkdGg9Ijc3My41Nzk5OTk5OTk5OTk5IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI2OCIgeT0iMjQ4LjciIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+MS4gUERIICjqs7zqsbApOiDsmYTsoIQg67aE7ZW0PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMl9TREhTT05FVF9fXyIgZGF0YS1sYWJlbD0iMi4gU0RIL1NPTkVUICjtmITrjIApOiDsp4HsoJEg7LaU7LacIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSI1MzIuNzk3IiBoZWlnaHQ9IjEzMC43IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iNTMyLjc5NyIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjgiIHk9Ijk4IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjIuIFNESC9TT05FVCAo7ZiE64yAKTog7KeB7KCRIOy2lOy2nDwvdGV4dD4KPC9nPgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJQMSIgZGF0YS10bz0iUDIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjA1LjA5MzAwMDAwMDAwMDAyLDI5Ny4xNSAyNTMuMDkzMDAwMDAwMDAwMDIsMjk3LjE1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJQMiIgZGF0YS10bz0iUDMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDA3LjY3NSwyOTcuMTUgNDU1LjY3NSwyOTcuMTUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlAzIiBkYXRhLXRvPSJQNCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI1OTYuMTc4LDI5Ny4xNSA2NDQuMTc4LDI5Ny4xNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUzEiIGRhdGEtdG89IlMyIiBkYXRhLXN0eWxlPSJ0aGljayIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJmYWxzZSIgZGF0YS1sYWJlbD0i7Y+s7J247YSwIOyjvOyGjCDtmZXsnbgiIHBvaW50cz0iMjA1LjA5MzAwMDAwMDAwMDAyLDE2My4zNSAzOTcuNDY3MDAwMDAwMDAwMDQsMTYzLjM1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIyIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJTMSIgZGF0YS10bz0iUzIiIGRhdGEtbGFiZWw9Iu2PrOyduO2EsCDso7zshowg7ZmV7J24Ij4KICA8cmVjdCB4PSIyNDkuMDkzMDAwMDAwMDAwMDIiIHk9IjE0Ny4zNSIgd2lkdGg9IjEwNC4zNzQwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjMwMS4yODAwMDAwMDAwMDAwMyIgeT0iMTYyLjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPu2PrOyduO2EsCDso7zshowg7ZmV7J24PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQMSIgZGF0YS1sYWJlbD0i6rOg7IaN66edIPCfk6bwn5Om8J+TpiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3MiIgeT0iMjc4LjciIHdpZHRoPSIxMzMuMDkzMDAwMDAwMDAwMDIiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMzguNTQ2NSIgeT0iMjk3LjE1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7qs6Dsho3rp50g8J+TpvCfk6bwn5OmPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQMiIgZGF0YS1sYWJlbD0i7KCE7LK0IOynkCDri6Qg7ZKA6riwIPCfkqYiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjUzLjA5MzAwMDAwMDAwMDAyIiB5PSIyNzguNyIgd2lkdGg9IjE1NC41ODIiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjMzMC4zODQiIHk9IjI5Ny4xNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7KCE7LK0IOynkCDri6Qg7ZKA6riwIPCfkqY8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlAzIiBkYXRhLWxhYmVsPSLsm5DtlZjripQg7KeQIDHqsJwg67qMIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQ1NS42NzUiIHk9IjI3OC43IiB3aWR0aD0iMTQwLjUwMzAwMDAwMDAwMDAxIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNTI1LjkyNjUiIHk9IjI5Ny4xNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7JuQ7ZWY64qUIOynkCAx6rCcIOu6jDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUDQiIGRhdGEtbGFiZWw9IuuLpOyLnCDsp5Ag7Iu47IScIOy2nOuwnCDwn5KmIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjY0NC4xNzgiIHk9IjI3OC43IiB3aWR0aD0iMTY5LjQwMiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNzI4Ljg3OSIgeT0iMjk3LjE1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7ri6Tsi5wg7KeQIOyLuOyEnCDstpzrsJwg8J+SpjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzEiIGRhdGEtbGFiZWw9IuqzoOyGjeunnSDwn5Om8J+TpvCfk6YiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNzIiIHk9IjE0NC45IiB3aWR0aD0iMTMzLjA5MzAwMDAwMDAwMDAyIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTM4LjU0NjUiIHk9IjE2My4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+6rOg7IaN66edIPCfk6bwn5Om8J+TpjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzIiIGRhdGEtbGFiZWw9IuKcqCDsp5Ag7JWIIO2SgOqzoAox6rCc66eMIOyPmSDrubzqs6Ag64Sj7J2MISDinKgKKERyb3AgJmFtcDsgSW5zZXJ0KSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzOTcuNDY3MDAwMDAwMDAwMDQiIHk9IjEyOCIgd2lkdGg9IjE3NS4zMjk5OTk5OTk5OTk5OCIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNDg1LjEzMjAwMDAwMDAwMDA2IiB5PSIxNjMuMzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjQ4NS4xMzIwMDAwMDAwMDAwNiIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPuKcqCDsp5Ag7JWIIO2SgOqzoDwvdHNwYW4+PHRzcGFuIHg9IjQ4NS4xMzIwMDAwMDAwMDAwNiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+MeqwnOunjCDsj5kg67m86rOgIOuEo+ydjCEg4pyoPC90c3Bhbj48dHNwYW4geD0iNDg1LjEzMjAwMDAwMDAwMDA2IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj4oRHJvcCAmYW1wOyBJbnNlcnQpPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 아날로그에서 광통신으로, 디지털 계위 3대 규격 전격 대조 (3단 표)**

이 토픽은 과거 PDH의 비효율성(전체 역다중화)과 이를 해결한 동기식 망(포인터 기반 직접 다중화)의 차이를 명확히 비교하는 것이 완벽한 득점 포인트입니다.

| **핵심 척도**          | **📞 PDH (유사 동기식 / 과거) 🚨**                                                                        | **🇺🇸 SONET (북미 광통신 표준)**                                                                                                        | **🌐 SDH (국제 광통신 표준) 🚨**                                              |
| :----------------- | :------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| **개념 / 통신 환경**     | **'각자 따로 노는 시계'.** 과거 구리선 기반. 각 네트워크 장비마다 시계(클럭)가 미세하게 달라서(유사 동기), 억지로 빈 데이터(Stuffing)를 끼워 넣어 묶었음. | **'미국의 광통신 독립 규격'.** 미국(ANSI) 주도로 만든 동기식(시계 100% 일치) 광통신 네트워크 표준.                                                                 | **'전 세계 글로벌 통합 규격 💯'.** SONET을 바탕으로 ITU-T가 제정한 **진정한 글로벌 동기식 국제 표준.** |
| **다중화 (묶고 풀기) 🚨** | **\[비효율 끝판왕 ❌]** 고속망에서 저속 신호 하나만 빼거나(Drop) 넣으려면(Insert), 전체 패킷을 처음부터 끝까지 다 풀었다가 다시 묶어야 함.          | **\[직접 쏙 빼고 넣기 (Drop & Insert) 💯]** 데이터 프레임 안에 \*\*'포인터(Pointer)'\*\*라는 번지수가 있어서, 짐을 통째로 풀지 않고도 달리는 고속망에서 원하는 데이터만 쏙 빼고 넣을 수 있음. | (SONET과 동일한 포인터 기반 직접 다중화 메커니즘 사용)                                     |
| **호환성 / 속도**       | **\[호환성 개판]** 북미(T1, 1.5M)와 유럽(E1, 2.0M) 규격이 달라서 해외 통신 시 대환장 파티 발생.                                | **기본 속도: 51.84 Mbps** (STS-1 / OC-1 규격 사용)                                                                                        | **기본 속도: 155.52 Mbps 💯** (STM-1 규격 사용. SONET의 OC-3 속도와 완벽히 동일하여 호환됨)  |

#### **IV. \[결론/제언] 차세대 광전송 아키텍처, OTN(광전달망)으로의 진화**

* **(키워드 위주 2줄 마무리)** "과거 전화망 음성 위주로 설계된 SDH/SONET은 현대의 폭발적인 기가비트 이더넷(IP) 데이터를 담기에는 오버헤드가 너무 큽니다. 따라서 최근 통신 백본망은 IP 패킷을 캡슐화하여 빛의 파장(WDM) 단위로 쏴버리는 **초거대 대역폭의 'OTN(Optical Transport Network, 광전달망)' 아키텍처로 세대교체를 완료했습니다.**"
