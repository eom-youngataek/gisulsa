#### **IPSec 핵심 동작 방식: 전송 모드 vs 터널 모드**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 IPSec은 두 가지 캡슐화 방식을 나눠 두었는가)
Ⅱ. 전송 모드 & 터널 모드 핵심 원리
Ⅲ. 비교 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 IPv4-IPv6 전환 기술의 터널링이 '서로 다른 IP 버전을 캡슐화해 통과시키는' 문제였다면, IPSec의 전송 모드·터널 모드는 '동일한 IPv4/IPv6 체계 안에서 원본 IP 헤더를 그대로 노출할 것인가, 아니면 그것마저 암호화해 새로운 헤더로 감쌀 것인가'를 결정하는 IPSec의 핵심 동작 방식이다 — 전송 모드(Transport Mode)는 '두 호스트 간 종단 간(End-to-End) 통신에서 페이로드만 보호하고 원본 IP 헤더는 그대로 노출'하는 반면, 터널 모드(Tunnel Mode)는 '원본 IP 패킷 전체를 새로운 IP 헤더로 완전히 감싸 원본 출발지·목적지 정보까지 은닉'하며, 이 차이가 바로 종단 간 보안(호스트-호스트)과 사이트 간 VPN(네트워크-네트워크)이라는 전혀 다른 두 가지 활용 사례를 결정짓는 근본 요인"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5MTIuODkyOTk5OTk5OTk5OCAyMDEuOCIgd2lkdGg9IjkxMi44OTI5OTk5OTk5OTk4IiBoZWlnaHQ9IjIwMS44IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlJPT1QiIGRhdGEtdG89IlRyYW5zcG9ydCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0MjUuMTM5MjQ5OTk5OTk5OTUsNzYuOSA0MjUuMTM5MjQ5OTk5OTk5OTUsMTAwLjkgMjA5LjkxNiwxMDAuOSAyMDkuOTE2LDEyNC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJST09UIiBkYXRhLXRvPSJUdW5uZWwiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDI1LjEzOTI0OTk5OTk5OTk1LDc2LjkgNDI1LjEzOTI0OTk5OTk5OTk1LDEwMC45IDY0MC4zNjI1LDEwMC45IDY0MC4zNjI1LDEyNC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJST09UIiBkYXRhLWxhYmVsPSJJUFNlYyDrj5nsnpEg66qo65OcIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM1NC41MTcyNDk5OTk5OTk5MyIgeT0iNDAiIHdpZHRoPSIxNDEuMjQ0IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDI1LjEzOTI0OTk5OTk5OTk1IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+SVBTZWMg64+Z7J6RIOuqqOuTnDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iVHJhbnNwb3J0IiBkYXRhLWxhYmVsPSLsoITshqEg66qo65OcIDogSG9zdC10by1Ib3N0LCDsg4HsnIQg7Y6Y7J2066Gc65Oc66eMIOyVlO2YuO2ZlCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MCIgeT0iMTI0LjkiIHdpZHRoPSIzMzkuODMyIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyMDkuOTE2IiB5PSIxNDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyghOyGoSDrqqjrk5wgOiBIb3N0LXRvLUhvc3QsIOyDgeychCDtjpjsnbTroZzrk5zrp4wg7JWU7Zi47ZmUPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJUdW5uZWwiIGRhdGEtbGFiZWw9Iu2EsOuEkCDrqqjrk5wgOiBHYXRld2F5LXRvLUdhdGV3YXksIO2MqO2CtyDsoITssrQg7JWU7Zi47ZmUICsg7Iug6recIE91dGVyIElQIO2XpOuNlCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MDcuODMyIiB5PSIxMjQuOSIgd2lkdGg9IjQ2NS4wNjA5OTk5OTk5OTk4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjY0MC4zNjI1IiB5PSIxNDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPu2EsOuEkCDrqqjrk5wgOiBHYXRld2F5LXRvLUdhdGV3YXksIO2MqO2CtyDsoITssrQg7JWU7Zi47ZmUICsg7Iug6recIE91dGVyIElQIO2XpOuNlDwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

***

#### Ⅱ. 전송 모드 & 터널 모드 핵심 원리

**가. 전송 모드(Transport Mode) 패킷 구조**

```
[전송 모드: 원본 IP 헤더 유지, 페이로드만 보호]

원본 패킷:
  [IP 헤더][TCP/UDP 헤더][데이터]

전송 모드 적용 후(ESP 기준):
  [원본 IP 헤더][ESP 헤더][TCP/UDP 헤더][데이터][ESP Trailer][ESP 인증]
   ↑ 그대로 노출          ↑───── 암호화 대상 ─────↑

핵심 특징:
  원본 출발지·목적지 IP 주소가 그대로 보임 🚨(라우팅 가능하나 은닉 안 됨)
  헤더 오버헤드가 최소(추가 IP 헤더 없음) ✅
  통신 주체 = 보안 적용 주체(호스트가 직접 IPSec 종단)
```

**나. 터널 모드(Tunnel Mode) 패킷 구조**

```
[터널 모드: 원본 패킷 전체를 캡슐화]

원본 패킷:
  [원본 IP 헤더][TCP/UDP 헤더][데이터]

터널 모드 적용 후(ESP 기준):
  [새 IP 헤더][ESP 헤더][원본 IP 헤더][TCP/UDP 헤더][데이터][ESP Trailer][ESP 인증]
   ↑ 게이트웨이 주소     ↑───────── 암호화 대상(원본 패킷 전체) ─────────↑

핵심 특징:
  원본 IP 헤더까지 암호화되어 완전히 은닉 ✅(출발지·목적지 위장)
  새 IP 헤더 = VPN 게이트웨이의 주소(실제 통신 주체와 다름)
  통신 주체(내부 호스트) ≠ 보안 적용 주체(게이트웨이) ← 프록시 개념과 유사
```

**다. 두 모드에서 AH vs ESP 프로토콜 비교**

| 구분              | AH(Authentication Header)                 | ESP(Encapsulating Security Payload) |
| :-------------- | :---------------------------------------- | :---------------------------------- |
| **제공 기능**       | 무결성·인증만(암호화 없음)                           | **암호화 + 무결성 + 인증**                  |
| **전송 모드 보호 범위** | 원본 IP 헤더 포함 전체 무결성 검증                     | 페이로드만 암호화, IP 헤더는 무결성 미검증           |
| **터널 모드 보호 범위** | 새 헤더 제외 원본 패킷 전체 무결성 검증                   | **원본 패킷 전체 암호화**(가장 널리 사용)          |
| **실무 활용도**      | NAT 환경에서 헤더 변경 시 무결성 검증 실패 → 거의 사용 안 함 🚨 | **사실상 표준**(NAT-Traversal 지원) ✅      |

***

#### Ⅲ. 비교 및 적용 체계

**가. 전송 모드 vs 터널 모드 전면 비교**

| 비교 항목           | 전송 모드(Transport Mode)    | 터널 모드(Tunnel Mode)             |
| :-------------- | :----------------------- | :----------------------------- |
| **보호 대상**       | 페이로드(상위 계층 데이터)만         | **원본 IP 패킷 전체**(헤더 포함) ✅       |
| **원본 IP 주소 은닉** | 노출됨 🚨                   | **완전히 은닉됨** ✅                  |
| **오버헤드**        | **적음**(새 IP 헤더 없음) ✅     | 상대적으로 큼(새 IP 헤더 추가)            |
| **통신 주체**       | **종단 호스트 간(End-to-End)** | **게이트웨이 간(사이트 간)** ✅           |
| **주 적용 시나리오**   | 호스트-호스트 직접 암호화 통신        | **사이트 간 VPN(Site-to-Site)** ✅  |
| **NAT 통과**      | 어려움(IP 헤더 변경 시 인증 실패) 🚨 | NAT-T(UDP 캡슐화)로 비교적 용이         |
| **실무 사용 빈도**    | 상대적으로 낮음                 | **압도적으로 높음**(대부분의 IPSec VPN) ✅ |

**나. 적용 시나리오별 선택 기준**

| 시나리오                          | 권장 모드             | 이유                                        |
| :---------------------------- | :---------------- | :---------------------------------------- |
| **본사-지사 간 VPN(Site-to-Site)** | **터널 모드**         | 양쪽 네트워크 전체를 게이트웨이가 대표해 보호, 원본 주소 은닉 필요    |
| **원격 근무자 개별 VPN 접속**          | **터널 모드**(사실상 표준) | 클라이언트가 사내망 게이트웨이를 거쳐 접속(앞서 다룬 SDP의 대안 기술) |
| **관리자가 특정 서버에 직접 원격 관리**      | 전송 모드 검토 가능       | 호스트 대 호스트 간 오버헤드 최소화가 중요한 경우              |
| **클라우드 VPC 간 사설 연결**          | **터널 모드**         | AWS Site-to-Site VPN 등 대부분 터널 모드 기반       |
| **호스트 간 DB 복제 트래픽 암호화**       | 전송 모드 검토 가능       | 앞서 다룬 이중화 복제 시 두 DB 서버 간 직접 암호화           |

**다. 앞서 다룬 캡슐화 개념들과의 구조적 비교**

| 비교 항목          | IPSec 터널 모드                     | VXLAN               | IPv6 터널링         |
| :------------- | :------------------------------ | :------------------ | :--------------- |
| **캡슐화 목적**     | **암호화·인증**(보안)                  | 네트워크 가상화(L2 확장)     | 이종 IP 버전 통과(호환성) |
| **새 헤더 부가 내용** | 새 IP 헤더 + ESP                   | UDP + VXLAN 헤더(VNI) | IPv4/IPv6 헤더     |
| **암호화 여부**     | **있음(ESP)** ✅                   | 없음(별도 IPSec 결합 필요)  | 없음               |
| **공통 원리**      | 원본 패킷을 새 헤더로 완전히 감싸는 캡슐화 구조는 동일 | <br />              | <br />           |

**라. SDP·SASE와의 관계**

| 항목             | 내용                                                                                               |
| :------------- | :----------------------------------------------------------------------------------------------- |
| **역할 관계**      | 앞서 다룬 SDP·ZTNA가 '누구에게 접속을 허용할지' 결정하는 접근 제어 계층이라면, IPSec 터널 모드는 그 허용된 트래픽을 실제로 암호화 전송하는 데이터 평면 기술 |
| **전통 VPN의 한계** | IPSec 터널 모드 기반 전통 VPN은 앞서 다룬 것처럼 터널 진입 시 내부망 전체 접근권을 부여하는 과신뢰 구조가 되기 쉬움                          |
| **현대적 결합**     | SDP/ZTNA의 세밀한 정책 결정 + IPSec/TLS의 암호화 전송을 결합해 SASE로 통합하는 것이 최신 아키텍처                               |

***

**(제언)** "전송 모드와 터널 모드의 근본적 차이는 '보호받는 것이 데이터인가, 아니면 통신 주체의 정체성 자체인가'라는 질문으로 요약할 수 있으며, 실무에서 전송 모드보다 터널 모드가 압도적으로 많이 쓰이는 이유는 대부분의 VPN 요구사항이 개별 호스트 간 통신 보호가 아니라 서로 다른 물리적 위치의 네트워크 전체를 마치 하나의 사설망처럼 연결하는 사이트 간 연결이기 때문입니다. 다만 IPSec 터널 모드 기반의 전통적 VPN은 일단 터널이 수립되면 내부망 전체에 대한 암묵적 신뢰를 부여하는 구조적 특성이 있으므로, 앞서 다룬 SDP·ZTNA와 결합해 터널이 열려도 개별 서비스 단위로 접근을 세분화하는 제로트러스트 원칙을 함께 적용하는 것이 현대 네트워크 보안 아키텍처 설계의 핵심이며, NAT 환경이 보편화된 오늘날에는 AH보다 NAT-Traversal을 지원하는 ESP 기반 터널 모드가 사실상 유일한 실무 표준으로 자리잡았다는 점을 설계 시 고려해야 합니다.

***

**앞서 다룬 개념과의 연결**

### **I. L3 보안 프레임워크의 핵심, IPSec 동작 모드의 개요**

IPSec은 인터넷 상에서 원격 지사 간 혹은 단말과 본사 간에 데이터 기밀성과 무결성을 보장하는 L3 VPN 표준입니다. IPSec을 적용할 때 암호화의 범위와 네트워크 라우팅 헤더의 재구성 방식에 따라 \*\*상위 페이로드만 암호화하여 종단 간(Host-to-Host) 통신에 쓰이는 전송 모드(Transport Mode)\*\*와, \*\*원본 패킷 전체를 암호화하고 신규 IP 헤더를 씌워 사이트 간(Site-to-Site) 게이트웨이 전송에 쓰이는 터널 모드(Tunnel Mode)\*\*로 구분되어 적용됩니다.

***

### **II. 모드별 패킷 캡슐화 헤더 구조 비교 (ESP 기준)**

#### **1. 전송 모드 (Transport Mode) 헤더 구조**

* **패킷 구성**: `[원본 IP 헤더] + [ESP 헤더] + [TCP/UDP 페이로드 (암호화)] + [ESP 트레일러] + [ESP 인증]`
* **특징**: 원본 IP 헤더를 그대로 라우팅에 사용하므로, 발신자와 수신자의 실제 IP 주소가 그대로 노출됩니다.

#### **2. 터널 모드 (Tunnel Mode) 헤더 구조**

* **패킷 구성**: `[신규 외부 IP 헤더] + [ESP 헤더] + [원본 IP 헤더 (암호화)] + [TCP/UDP 페이로드 (암호화)] + [ESP 트레일러] + [ESP 인증]`
* **특징**: 원본 IP 헤더까지 완벽 암호화하고, 보안 게이트웨이 간 통신을 위한 \*\*신규 외부 IP 헤더(Outer IP Header)\*\*를 추가하여 내부 사설망 구조를 완전 은닉합니다.

***

### **III. IPSec 전송 모드(Transport)와 터널 모드(Tunnel)의 상세 비교**

| **비교 항목**       | **💻 전송 모드 (Transport Mode)** | **🏢 터널 모드 (Tunnel Mode)**                            |
| :-------------- | :---------------------------- | :---------------------------------------------------- |
| **암호화 보호 범위**   | L4 상위 페이로드만 보호 (원본 IP 헤더 보존)  | **원본 IP 패킷 전체 (원본 IP 헤더 포함) 보호**                      |
| **신규 IP 헤더 추가** | 추가 없음 (원본 IP 헤더로 통신)          | **신규 외부 IP 헤더 (Outer IP Header 20B) 추가**              |
| **주요 적용 통신 구간** | **Host-to-Host (서버 간 종단 통신)** | **Gateway-to-Gateway (Site-to-Site VPN), Host-to-GW** |
| **내부 주소 은닉성**   | 불가능 (실제 발신/수신 IP 노출)          | **완벽 보장 (내부 사설 IP 주소를 암호화하여 은닉)**                     |
| **오버헤드 및 크기**   | 패킷 추가 오버헤드가 상대적으로 작음          | 신규 IP 헤더 추가로 오버헤드가 전송 모드보다 큼                          |
| **NAT 트래버설 이슈** | NAT 통과 시 원본 IP 변경으로 무결성 깨짐    | **NAT-T(UDP 4500 포트) 연동을 통해 NAT 통과 우수**               |

***

### **IV. IPSec VPN 구축 시 모드 선택 및 엔지니어링 가이드라인**

**IMPORTANT**

1. **Site-to-Site 본지사 연동 시 터널 모드 적용**: 본사와 지사 간 라우터/방화벽 통신 구간에는 반드시 터널 모드(ESP Tunnel)를 적용하여 내부 10.x.x.x 대역의 사설 IP 토폴로지가 외부 인터넷망에 노출되지 않도록 차단해야 합니다.
2. **NAT-T (NAT Traversal - UDP 4500) 설정**: 터널 모드 적용 시 중간에 공유기나 NAT 장비가 존재하면 ESP 패킷(프로토콜 50번)이 포트 번호가 없어 차단될 수 있으므로, **UDP 4500번 포트로 캡슐화하는 NAT-T 기능**을 필수로 활성화해야 정상적인 VPN 터널이 유지됩니다.
