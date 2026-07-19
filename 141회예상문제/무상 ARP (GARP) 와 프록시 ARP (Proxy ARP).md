#### 답안 전개 스토리 (핵심 압축)

> "ARP는 원래 '이 IP를 가진 자의 MAC을 알려달라'는 단순한 질문이다. 그런데 이 단순한 프로토콜에 두 가지 영리한 확장이 있다. **GARP(Gratuitous ARP·무상 ARP)**는 '남에게 묻는 것이 아니라 자기 자신의 IP로 ARP 요청을 브로드캐스트하는' 자기 선언이다 — Target IP = Sender IP라는 구조적 특이점이 핵심이며, 이 자기 선언이 세 가지 강력한 기능을 수행한다. **①IP 충돌 탐지**: 아무도 응답 안 하면 안전·누군가 응답하면 충돌 🚨. **②FHRP 페일오버**: VRRP·HSRP 마스터 전환 시 전체 세그먼트 ARP 캐시를 GARP 한 방으로 강제 갱신. **③VM 라이브 마이그레이션**: 서버A→서버B로 VM 이동 후 GARP로 스위치 CAM 테이블 즉시 갱신. **Proxy ARP**는 반대로 '라우터가 다른 서브넷의 호스트를 대신해 ARP에 응답하는' 대리인 역할이다 — 게이트웨이 설정이 없는 호스트가 다른 서브넷에 ARP를 날리면 라우터가 자신의 MAC으로 응답해 패킷을 가로채 대신 전달함으로써 호스트는 게이트웨이의 존재를 모른 채 통신하게 된다. 둘 다 ARP 스푸핑 공격의 악용 경로가 되므로 DAI(Dynamic ARP Inspection)·no ip proxy-arp 비활성화로 보안 통제가 필수"

---

#### 핵심 내용 (암기용)

**전제 개념**

| 개념                  | 내용                                           |
| ------------------- | -------------------------------------------- |
| ==**ARP Request**== | 브로드캐스트(FF:FF:FF:FF:FF:FF) / Target MAC=00:00 |
| ==**ARP Reply**==   | 유니캐스트 / Sender MAC 포함 응답                     |
| ==**ARP 캐시**==      | IP→MAC 매핑 임시 저장 / TTL 기반 만료                  |
| ==**CAM 테이블**==     | 스위치의 MAC→포트 매핑 / GARP로 갱신                    |

---

| **핵심 척도**    | **📊 GARP (무상 ARP) 🚨**                                                                                                   | **🔑 Proxy ARP (프록시 ARP) 🚨**                                                                   | **🏁 보안 위협 및 대응 💯**                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **핵심 구조**    | **Target IP = Sender IP** (자기 자신에게 ARP 요청) / 브로드캐스트 전송 / 응답 기대 안 함                                                        | **라우터가 타 서브넷 호스트 대신 자신의 MAC으로 ARP 응답** / 패킷 수신 후 라우팅 전달                                         | ARP 스푸핑: 악성 GARP로 ARP 캐시 오염 → 중간자 공격 / 악성 Proxy ARP로 트래픽 탈취                                                                    |
| **3대 활용 🚨** | **①IP 충돌 탐지**: 응답 없음=안전·응답 있음=충돌 / **②FHRP 페일오버**: Master 교체 시 전체 ARP 캐시 강제 갱신 / **③VM 마이그레이션**: 물리 서버 이동 후 CAM·ARP 즉시 갱신 | **①게이트웨이 미설정 호스트 통신**: 서브넷 경계 투명화 / **②VPN 터널**: 원격 클라이언트 대리 응답 / **③클라우드 VPC**: VM 위치 무관 IP 응답 | **DAI(Dynamic ARP Inspection)**: DHCP 스누핑 테이블로 ARP 유효성 검증 / **no ip proxy-arp**: 불필요 인터페이스 비활성화 / **Static ARP**: 중요 호스트 정적 설정 |
| **패킷 구조 💯** | Sender IP=10.0.0.1 / **Target IP=10.0.0.1** (동일!) / Sender MAC=자신 / Target MAC=00:00 or FF:FF                             | Sender IP=10.0.1.1(타깃) / **Sender MAC=라우터 MAC** (대리!) / 호스트는 라우터 MAC을 타깃 MAC으로 착각               | IPv6 NDP(Neighbor Discovery)로 진화 → ARP 취약점 원천 제거 / SDN 컨트롤러 중앙 ARP 관리 / BGP EVPN 컨트롤 플레인 ARP 배포                                |

---

#### 도식화

```
[GARP vs Proxy ARP 동작 구조]

①GARP (자기 선언):
  호스트A (IP:10.0.0.1, MAC:AA)
       ↓ 브로드캐스트
  "10.0.0.1의 MAC을 가진 자 있는가?"
  (Sender IP = Target IP = 10.0.0.1)
       ↓
  충돌 없음: 무응답 → 정상 사용 ✅
  충돌 있음: 호스트B 응답 → 충돌 경보 🚨
  FHRP 전환: 전체 ARP 캐시 즉시 갱신 ✅
  VM 이동: 스위치 CAM 포트 갱신 ✅

②Proxy ARP (대리 응답):

  서브넷A                라우터              서브넷B
  호스트A ─ARP Request─▶ 라우터        호스트B
  10.0.0.1  "10.0.1.1    10.0.0.254    10.0.1.1
             MAC은?"       10.0.1.254

               ↓ 라우팅 경로 확인 후
             ARP Reply: "MAC은 RR:RR(나!)"
               ↓
  호스트A: 10.0.1.1→RR:RR 캐시
  패킷 → 라우터 → 서브넷B → 호스트B ✅
  (호스트A는 게이트웨이 모르고도 통신!)

[보안 위협: ARP 스푸핑]
  공격자 GARP: Sender IP=피해자IP, MAC=공격자MAC
  → 전체 ARP 캐시 오염 → 트래픽 도청 🚨
  방어: DAI → DHCP 스누핑 테이블 검증 ✅
```

---

**(제언)** "GARP는 'Target IP = Sender IP'라는 단 하나의 구조적 특이점으로 IP 충돌 탐지·FHRP 페일오버·VM 마이그레이션이라는 세 가지 고가치 기능을 수행하는 ARP의 가장 영리한 확장이며, Proxy ARP는 라우터가 대리 응답함으로써 호스트의 게이트웨이 부재를 투명하게 보완하는 네트워크 추상화 기법입니다. **그러나 둘 다 ARP 스푸핑의 악용 경로가 되므로 DAI·Static ARP·no ip proxy-arp 3중 통제를 적용하고, 장기적으로는 앞서 다룬 IPv6 NDP·SDN 중앙화 ARP 관리로 전환해 L2 레이어 신뢰 취약점을 근본 해소해야 합니다.**"


### **무상 ARP (GARP) 와 프록시 ARP (Proxy ARP)**

#### **1. 답안 전개 스토리 (핵심 압축)**

> "단말기 IP를 물리 맥(MAC) 주소로 연결해 주는 일반 ARP 외에, **'네트워크 주소 충돌을 막고 가상 이중화(VRRP) 시 장비 간 전환을 실시간 통보해 주는 무상 ARP(GARP)'와 '라우터가 대신 대답해 통신을 중계해 주는 프록시 ARP'의 특수 목적 2대 기술**이다. **GARP(Gratuitous ARP) 🚨**는 부팅할 때 자기 자신의 IP를 타깃으로 ARP 브로드캐스트를 날린다. 만약 답변이 오면 "내 IP를 남이 쓰고 있다"며 **IP 충돌 경보**를 띄운다. 또한, 이중화 장비가 다운되었을 때 대기 장비가 GARP를 뿌려 스위치들의 MAC 주소 테이블을 실시간으로 자동 갱신(Failover)시킨다. **프록시 ARP**는 서브넷이 다른 단말이 ARP를 보냈을 때, 라우터가 마치 자기가 그 목적지인 양 속여서 자기 MAC 주소를 응답해 통신을 강제로 중계해 주는 기법이다."

#### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjI4Ljk1OSAyNTguNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSIxMjI4Ljk1OSIgaGVpZ2h0PSIyNTguNzAwMDAwMDAwMDAwMDUiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9BUlBfR0FSUF9fX18iIGRhdGEtbGFiZWw9IuustOyDgSBBUlAgKEdBUlApIOu2gO2MhSDsi5wg7J6R64+ZIOunpOy7pOuLiOymmCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMTE0OC45NTkiIGhlaWdodD0iMTc4LjcwMDAwMDAwMDAwMDAyIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMTE0OC45NTkiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7rrLTsg4EgQVJQIChHQVJQKSDrtoDtjIUg7IucIOyekeuPmSDrp6Tsu6Tri4jsppg8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkJPIiBkYXRhLXRvPSJTX0dBUlAiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjU4LjAwNiwxMzkuMTI1IDMwNi4wMDYsMTM5LjEyNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iU19HQVJQIiBkYXRhLXRvPSJXQVJOIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIxLiDsnZHri7Ug7IiY7IugIOyLnCIgcG9pbnRzPSI1ODkuNTIyLDEzMC4xNTgzMzMzMzMzMzMzMyA2MDEuNTIyLDEzMC4xNTgzMzMzMzMzMzMzMyA2MDEuNTIyLDEwMi40NSA4MzIuMzg2MDAwMDAwMDAwMSwxMDIuNDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlNfR0FSUCIgZGF0YS10bz0iVVBEQVRFIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIyLiDri6Trpbgg7Iqk7JyE7LmYL+uFuOuTnCDsiJjsi6Ag7IucIiBwb2ludHM9IjU4OS41MjIsMTQ4LjA5MTY2NjY2NjY2NjY3IDYwMS41MjIsMTQ4LjA5MTY2NjY2NjY2NjY3IDYwMS41MjIsMTc1LjggODMyLjM4NjAwMDAwMDAwMDEsMTc1LjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iU19HQVJQIiBkYXRhLXRvPSJXQVJOIiBkYXRhLWxhYmVsPSIxLiDsnZHri7Ug7IiY7IugIOyLnCI+CiAgPHJlY3QgeD0iNjY3LjM4MDAwMDAwMDAwMDEiIHk9Ijg2LjQ0OTk5OTk5OTk5OTk5IiB3aWR0aD0iODcuMTQ4MDAwMDAwMDAwMDEiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI3MTAuOTU0MDAwMDAwMDAwMSIgeT0iMTAxLjYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjEuIOydkeuLtSDsiJjsi6Ag7IucPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlNfR0FSUCIgZGF0YS10bz0iVVBEQVRFIiBkYXRhLWxhYmVsPSIyLiDri6Trpbgg7Iqk7JyE7LmYL+uFuOuTnCDsiJjsi6Ag7IucIj4KICA8cmVjdCB4PSI2MzMuNTIyIiB5PSIxNTkuOCIgd2lkdGg9IjE1NC44NjQwMDAwMDAwMDAwMyIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjcxMC45NTQwMDAwMDAwMDAxIiB5PSIxNzQuOTUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjIuIOuLpOuluCDsiqTsnITsuZgv64W465OcIOyImOyLoCDsi5w8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkJPIiBkYXRhLWxhYmVsPSLrhbjrk5wg67aA7YyFIC8g6rCA7IOBIElQIO2ZnOyEse2ZlCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iMTIwLjY3NTAwMDAwMDAwMDAxIiB3aWR0aD0iMjAyLjAwNTk5OTk5OTk5OTk3IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTU3LjAwMyIgeT0iMTM5LjEyNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+64W465OcIOu2gO2MhSAvIOqwgOyDgSBJUCDtmZzshLHtmZQ8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlNfR0FSUCIgZGF0YS1sYWJlbD0i4pyoIEdBUlAg7Yyo7YK3IOu4jOuhnOuTnOy6kOyKpO2KuCDshqHsi6Ag8J+aqCDinKgKU291cmNlIElQID0g64K0IElQIC8gVGFyZ2V0IElQID0g64K0IElQIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjMwNi4wMDYiIHk9IjExMi4yMjUiIHdpZHRoPSIyODMuNTE2MDAwMDAwMDAwMSIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0NDcuNzY0IiB5PSIxMzkuMTI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0NDcuNzY0IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+4pyoIEdBUlAg7Yyo7YK3IOu4jOuhnOuTnOy6kOyKpO2KuCDshqHsi6Ag8J+aqCDinKg8L3RzcGFuPjx0c3BhbiB4PSI0NDcuNzY0IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5Tb3VyY2UgSVAgPSDrgrQgSVAgLyBUYXJnZXQgSVAgPSDrgrQgSVA8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iV0FSTiIgZGF0YS1sYWJlbD0i8J+SgCBJUCDstqnrj4wg67Cc7IOdIOqyveqzoCDrsJzsg50g8J+SgCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI4MzIuMzg2MDAwMDAwMDAwMSIgeT0iODQiIHdpZHRoPSIyMTUuMzQ0IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9Ijk0MC4wNTgwMDAwMDAwMDAxIiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPvCfkoAgSVAg7Lap64+MIOuwnOyDnSDqsr3qs6Ag67Cc7IOdIPCfkoA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlVQREFURSIgZGF0YS1sYWJlbD0i4pyoIOyghOyCsOunnSDrgrQgQVJQIOy6kOyLnCDthYzsnbTruJQg7KaJ7IucIOy1nOyLoO2ZlCDwn5KvIOKcqArinpQg7J207KSR7ZmUIOyepeyVoCDsoITtmZggRmFpbG92ZXIg7ISx6rO1IPCfmoAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iODMyLjM4NjAwMDAwMDAwMDEiIHk9IjE0OC45IiB3aWR0aD0iMzQwLjU3Mjk5OTk5OTk5OTkiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTAwMi42NzI1IiB5PSIxNzUuOCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTAwMi42NzI1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+4pyoIOyghOyCsOunnSDrgrQgQVJQIOy6kOyLnCDthYzsnbTruJQg7KaJ7IucIOy1nOyLoO2ZlCDwn5KvIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjEwMDIuNjcyNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+4p6UIOydtOykke2ZlCDsnqXslaAg7KCE7ZmYIEZhaWxvdmVyIOyEseqztSDwn5qAPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

| **핵심 척도**    | **📊 무상 ARP (GARP: Gratuitous ARP) 🚨**                                 | **🔑 프록시 ARP (Proxy ARP) 🚨**                                  | **🏁 이중화 갱신 메커니즘 (VRRP 연계) 💯**                                                         |
| :----------- | :---------------------------------------------------------------------- | :------------------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| **전송 목적**    | **자발적 공고 및 충돌 감지.** 물어보지 않았는데 스스로(Gratuitous) 자기 정보를 온 동네에 브로드캐스트로 전파함. | **경로 대리 중계.** 디폴트 게이트웨이가 없는 단말을 위해 라우터가 대리인(Proxy)이 되어 대신 응답함. | 마스터 라우터 장애 시, 백업 라우터가 동일한 가상 IP(VIP)를 쥐고 GARP를 뿜어 스위치 포트를 동적 전환함.                       |
| **동작 특징 🚨** | **\[패킷 구조 🚨]** 송신자 IP와 수신자 IP를 동일하게 세팅하여 전송.                           | 다른 서브넷의 ARP 요청에 대해 라우터 자신의 MAC 주소를 줌.                          | **\[ARP 스푸핑 보안 리스크 💯]** 해커가 가짜 GARP를 지속적으로 뿌려 스위치 데이터를 조작하는 해킹(ARP Spoofing) 차단 대책 필요. |

* **(제언)** "프록시 ARP는 해킹 공격 경로로 악용되기 쉬우므로 **보안 감리 시 백본 라우터의 프록시 ARP 기능은 기본 비활성화(`no ip proxy-arp`)할 것을 권고하고, 이중화 클러스터 장비(L4, 방화벽) 배치 구간에만 GARP가 안전하게 도달하도록 허용해야 합니다.**"
