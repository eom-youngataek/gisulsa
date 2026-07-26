#### **IPv6 전환의 3대 핵심 기술: 듀얼스택 / 터널링 / 변환**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 IPv4에서 IPv6로의 전환이 "한 번에" 안 되는가)
Ⅱ. 3대 전환 기술 핵심 원리
Ⅲ. 비교 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 LPM(최장 프리픽스 매칭)이 'CIDR 환경에서 하나의 주소 체계 내 라우팅을 최적화'하는 문제였다면, IPv4-IPv6 전환 기술은 '서로 다른 두 주소 체계(32비트 vs 128비트)가 인터넷 전역에 걸쳐 수십 년간 공존해야 하는' 훨씬 근본적인 문제를 다룬다 — IPv4 주소 고갈이 2011년 이미 현실화됐음에도 전 세계 인터넷을 하룻밤 사이 IPv6로 전환하는 것은 불가능하므로, 신규 시스템은 두 프로토콜을 동시에 지원하는 듀얼스택(Dual Stack)으로 시작하고, 한쪽 프로토콜만 지원하는 구간은 다른 프로토콜 패킷을 감싸서 통과시키는 터널링(Tunneling)으로 우회하며, 아예 서로 통신이 불가능한 순수 IPv4-only와 IPv6-only 사이는 변환(Translation) 기술로 주소 자체를 바꿔주는 3가지 접근이 IETF에 의해 표준화되어 지난 20년 이상 인터넷의 점진적 전환을 지탱해온 것"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMTU4LjQ2IDIwMS44IiB3aWR0aD0iMTE1OC40NiIgaGVpZ2h0PSIyMDEuOCIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJST09UIiBkYXRhLXRvPSJEUyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI1NTkuNTkzNTAwMDAwMDAwMSw3Ni45IDU1OS41OTM1MDAwMDAwMDAxLDk0LjkgMjA5LjU0NTUsOTQuOSAyMDkuNTQ1NSwxMTIuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUk9PVCIgZGF0YS10bz0iVHVubmVsIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjU1OS41OTM1MDAwMDAwMDAxLDc2LjkgNTU5LjU5MzUwMDAwMDAwMDEsOTQuOSA1NTkuNTkzNTAwMDAwMDAwMSw5NC45IDU1OS41OTM1MDAwMDAwMDAxLDExMi45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJST09UIiBkYXRhLXRvPSJUcmFucyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI1NTkuNTkzNTAwMDAwMDAwMSw3Ni45IDU1OS41OTM1MDAwMDAwMDAxLDk0LjkgOTI5LjI3OCw5NC45IDkyOS4yNzgsMTEyLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJPT1QiIGRhdGEtbGFiZWw9IklQdjQtSVB2NiAz64yAIOyghO2ZmCDquLDsiKAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDY2LjAwMDUwMDAwMDAwMDA1IiB5PSI0MCIgd2lkdGg9IjE4Ny4xODU5OTk5OTk5OTk5OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNTU5LjU5MzUwMDAwMDAwMDEiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5JUHY0LUlQdjYgM+uMgCDsoITtmZgg6riw7IigPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJEUyIgZGF0YS1sYWJlbD0iMS4gRHVhbCBTdGFjayA6IOuFuOuTnOyXkCDrkZAg7ZSE66Gc7Yag7L2cIOyKpO2DnSDrj5nsi5wg7YOR7J6sIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwIiB5PSIxMTIuOSIgd2lkdGg9IjMzOS4wOTEiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMjA5LjU0NTUiIHk9IjEzMS4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+MS4gRHVhbCBTdGFjayA6IOuFuOuTnOyXkCDrkZAg7ZSE66Gc7Yag7L2cIOyKpO2DnSDrj5nsi5wg7YOR7J6sPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJUdW5uZWwiIGRhdGEtbGFiZWw9IjIuIFR1bm5lbGluZyA6IDZpbjQgLyA0aW42IOy6oeyKkO2ZlCDthLDrhJDrp4Eg7KCE7IahIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwNy4wOTEwMDAwMDAwMDAwNyIgeT0iMTEyLjkiIHdpZHRoPSIzMDUuMDA0OTk5OTk5OTk5OTQiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1NTkuNTkzNTAwMDAwMDAwMSIgeT0iMTMxLjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij4yLiBUdW5uZWxpbmcgOiA2aW40IC8gNGluNiDsuqHsipDtmZQg7YSw64SQ66eBIOyghOyGoTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iVHJhbnMiIGRhdGEtbGFiZWw9IjMuIFRyYW5zbGF0aW9uIDogTkFUNjQgLyBETlM2NCDquLDrsJgg7ZSE66Gc7Yag7L2cIO2XpOuNlCDrs4DtmZgiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNzQwLjA5NiIgeT0iMTEyLjkiIHdpZHRoPSIzNzguMzYzOTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjkyOS4yNzgiIHk9IjEzMS4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+My4gVHJhbnNsYXRpb24gOiBOQVQ2NCAvIEROUzY0IOq4sOuwmCDtlITroZzthqDsvZwg7Zek642UIOuzgO2ZmDwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

***

#### Ⅱ. 3대 전환 기술 핵심 원리

**가. ①듀얼스택(Dual Stack)**

```
[듀얼스택 동작 원리]

호스트/라우터가 IPv4·IPv6 스택을 동시에 보유

  애플리케이션
       ↓
  ┌─────────┬─────────┐
  │ IPv4 스택 │ IPv6 스택 │  ← 독립적으로 병존
  └─────────┴─────────┘
       ↓            ↓
   IPv4 인터페이스  IPv6 인터페이스

통신 시:
  DNS 조회 → A 레코드(IPv4) 또는 AAAA 레코드(IPv6)
  상대방이 IPv6 지원 시 → IPv6로 직접 통신
  상대방이 IPv4만 지원 시 → IPv4로 직접 통신
  → 프로토콜 변환·캡슐화 없이 각자 네이티브로 통신 ✅
```

**나. ②터널링(Tunneling)**

```
[터널링 동작 원리: IPv6 in IPv4 예시]

IPv6 전용 네트워크A ──[IPv4 전용 구간]── IPv6 전용 네트워크B

  IPv6 패킷을 IPv4 패킷 안에 캡슐화(Encapsulation)
  ┌───────────────────────────┐
  │ IPv4 헤더 │ IPv6 패킷 전체(헤더+데이터) │
  └───────────────────────────┘
       ↓ IPv4 전용 구간 통과
  터널 종료점에서 IPv4 헤더 제거(역캡슐화)
       ↓
  원본 IPv6 패킷 복원 → 목적지로 전달

→ 앞서 다룬 VXLAN의 캡슐화 원리와 동일한 개념
  (다른 계층 프로토콜을 감싸서 이종 구간을 통과)
```

**다. ③변환(Translation)**

```
[변환(NAT64/DNS64) 동작 원리]

IPv6 전용 호스트 ── 변환 장비(NAT64) ── IPv4 전용 서버

  IPv6-only 클라이언트가 IPv4-only 서버 접근 시:
  ①DNS64: AAAA 레코드 없으면 A 레코드를 IPv6 형식으로 합성
    (예: 64:ff9b::/96 접두사 + IPv4 주소)
  ②클라이언트: 합성된 IPv6 주소로 요청 전송
  ③NAT64 장비: IPv6 헤더 → IPv4 헤더로 실제 변환
    (캡슐화 아닌 헤더 자체를 재작성)
  ④IPv4 서버 응답 → NAT64가 역변환 → 클라이언트 전달

→ 캡슐화(터널링)와 달리 패킷 헤더 자체를 변환
→ 서로 다른 두 세상을 실질적으로 "번역"
```

***

#### Ⅲ. 비교 및 적용 체계

**가. 3대 전환 기술 전면 비교**

| 비교 항목       | 듀얼스택                     | 터널링                       | 변환                         |
| :---------- | :----------------------- | :------------------------ | :------------------------- |
| **핵심 동작**   | 두 스택 병존(독립 통신)           | 캡슐화(Encapsulation)        | 헤더 변환(Translation)         |
| **전제 조건**   | 양 끝단 모두 IPv6 지원 필요       | 양 끝단 IPv6 지원, 중간 구간만 IPv4 | **한쪽만 IPv6 지원해도 가능** ✅     |
| **적용 시나리오** | 신규 구축 인프라(가장 이상적)        | IPv6 섬(Island) 간 연결       | **레거시 IPv4-only 서비스 접근**   |
| **오버헤드**    | 없음(각자 네이티브) ✅            | 캡슐화로 헤더 오버헤드 추가           | 변환 장비의 상태 관리 부담            |
| **확장성/단순성** | **가장 단순·권장 방식** ✅        | 과도기적·임시방편 성격              | 변환 장비가 병목·단일장애점 가능 🚨      |
| **대표 기술**   | Dual Stack Lite 등        | **6to4·6in4·Teredo·GRE**  | **NAT64/DNS64·NAT-PT(구식)** |
| **최종 지향점**  | **최종 목표 상태**(전환 완료 후 유지) | 과도기 임시 수단                 | 과도기 임시 수단                  |

**나. 대표 세부 기술 비교**

| 기술                        | 유형        | 특징                                                          |
| :------------------------ | :-------- | :---------------------------------------------------------- |
| **6to4**                  | 터널링       | 자동 터널링, 2002::/16 접두사 사용, 별도 설정 최소화하나 신뢰성 이슈로 쇠퇴            |
| **Teredo**                | 터널링       | NAT 뒤의 IPv6 호스트를 위한 UDP 기반 터널링(마이크로소프트 주도)                  |
| **6rd(Rapid Deployment)** | 터널링       | ISP 사업자 자체 주소 체계 기반 대규모 배포용, IPTV 등에 실무 활용                  |
| **NAT64/DNS64**           | 변환        | **현재 가장 널리 쓰이는 실무 표준**, IPv6-only 모바일망(예: T-Mobile)에서 핵심 기술 |
| **464XLAT**               | 변환+터널링 혼합 | 모바일 환경에서 IPv4 애플리케이션 호환성까지 확보하는 하이브리드 접근                    |

**다. 적용 시나리오별 선택 기준**

| 시나리오                        | 권장 기술                         | 이유                                                   |
| :-------------------------- | :---------------------------- | :--------------------------------------------------- |
| **신규 데이터센터·클라우드 구축**        | **듀얼스택**                      | 가장 단순하고 표준적, 장기적으로 유지보수 부담 최소                        |
| **모바일 통신사 망(IPv6-only 전환)** | **NAT64/DNS64(464XLAT)**      | 앞서 다룬 IoT NB-IoT처럼 대규모 단말 IPv6 전환 시 레거시 IPv4 앱 호환 필수 |
| **원격지 IPv6 네트워크 간 임시 연결**   | **터널링(6in4/GRE)**             | 중간 ISP 구간이 아직 IPv4만 지원할 때 임시 우회                      |
| **공공기관 IPv6 전환 로드맵**        | **듀얼스택 우선, 단계적 IPv6-only 전환** | 국내 IPv6 전환 정책의 표준 권고 방식                              |

***

**(제언)** "듀얼스택·터널링·변환의 관계는 목적지가 아니라 여정에서의 서로 다른 역할로 이해하는 것이 정확합니다. 듀얼스택이 궁극적으로 도달해야 할 안정적 종착지에 가깝다면, 터널링과 변환은 그 과도기 동안 발생하는 특수한 연결 문제(IPv6 섬끼리의 연결, IPv6-only 환경에서 레거시 IPv4 서비스 접근)를 해결하는 임시 다리이므로, 신규 인프라를 설계할 때는 처음부터 IPv4를 흉내내는 변환·터널링에 의존하기보다 듀얼스택을 기본으로 채택하고 IPv4 주소 고갈이 특히 심각한 모바일·IoT 대규모 단말 환경에서만 NAT64 계열의 변환 기술을 전략적으로 도입하는 것이 장기적인 운영 복잡도를 최소화하는 핵심 전략이며, 국내 공공기관과 통신사들이 추진 중인 IPv6 전환 로드맵도 이 3단계(듀얼스택 확산→변환 기술로 레거시 호환→최종 IPv6-only化)를 순차적으로 밟아가는 구조를 따르고 있습니다.

***

**앞서 다룬 개념과의 연결**

| 연계 개념               | 연결 내용                                                     |
| :------------------ | :-------------------------------------------------------- |
| **LPM(최장 프리픽스 매칭)** | IPv6 128비트 주소공간에서도 LPM 원리가 그대로 적용되어 라우팅 결정                |
| **VXLAN·캡슐화**       | 터널링 기술의 캡슐화 원리가 VXLAN의 UDP 캡슐화와 개념적으로 동일                  |
| **SRv6**            | IPv6 확장 헤더(SRH) 활용이 IPv6 네이티브 전환이 완료된 이후 얻는 대표적 이점        |
| **LoRa/NB-IoT**     | 대규모 IoT 단말의 IPv6-only 확산 시 NAT64 계열 변환 기술이 실무적으로 중요해지는 영역 |
| **AIDC 특별법·데이터센터**  | 신규 AI 데이터센터 네트워크 설계 시 처음부터 듀얼스택을 기본 아키텍처로 채택하는 것이 권장      |

### **I. 차세대 프로토콜 공존을 위한 IPv4-IPv6 전환 기술의 개요**

IPv4와 IPv6는 헤더 구조와 주소 체계가 근본적으로 달라 상호 호환성이 없습니다. 따라서 전체 인터넷 망을 한꺼번에 IPv6로 전환할 수 없으므로, 점진적 이동을 유도하는 **1) 듀얼 스택(Dual Stack)**, 이종 프로토콜 망을 캡슐화하여 통과하는 **2) 터널링(Tunneling)**, 그리고 단말과 서버의 주소를 직접 상호 바꿀 수 있는 **3) 변환(Translation)** 기술의 3대 매커니즘을 유기적으로 조합하여 운용해야 합니다.

***

### **II. IPv4-IPv6 3대 전환 기술별 세부 메커니즘**

#### **1. 듀얼 스택 (Dual Stack)**

* **동작 원리**: 단말 및 라우터 장비에 IPv4와 IPv6 프로토콜 스택을 동시에 탑재하여 수신된 패킷의 주소 타입에 따라 적절한 스택을 선택하여 처리합니다.
* **DNS 연동**: DNS 질의 시 A 레코드(IPv4)와 AAAA 레코드(IPv6)를 모두 조회하여 IPv6 주소를 우선 선택 처리합니다.

#### **2. 터널링 (Tunneling)**

* **동작 원리**: 이종 네트워크 구간을 통과할 때 패킷 전체를 다른 프로토콜 헤더로 캡슐화(Encapsulation)하여 보낸 뒤, 목적지 터널 단말에서 역캡슐화합니다.
* **주요 방식**:
  * **설정 터널링 (6in4, GRE)**: 터널 양단 라우터를 고정 수동 설정
  * **자동 터널링 (6to4, ISATAP, Teredo)**: 목적지 IPv4 주소를 IPv6 주소 안에 매핑하여 터널 자동 생성

#### **3. 변환 (Translation / NAT64 & DNS64)**

* **동작 원리**: IPv6 전용 호스트가 IPv4 전용 서버와 통신할 때, L3 헤더를 1:1로 직접 변환(Translating)하여 연결을 매개합니다.
* **NAT64 / DNS64**: DNS64 서버가 IPv4 A 레코드를 IPv6 주소 형태로 가공(Synthetic IPv6)해 전달하고, NAT64 장비가 L3/L4 IP 및 포트를 상호 매핑 변환합니다.

***

### **III. IPv4-IPv6 3대 전환 기술의 상세 비교**

| **비교 항목**         | **🥞 듀얼 스택 (Dual Stack)** | **🚇 터널링 (Tunneling)**        | **🔄 주소/헤더 변환 (Translation)** |
| :---------------- | :------------------------ | :---------------------------- | :---------------------------- |
| **연동 메커니즘**       | 장비 내 두 프로토콜 스택 동시 유지 및 가동 | 이종 프로토콜 헤더 캡슐화 (MAC/IP-in-IP) | 패킷 헤더(L3/L4) 필드를 1:1 직접 개조    |
| **End-to-End 보장** | **완벽히 보장 (Native IP 전송)** | 터널 구간 양단 간 전송 보장              | 변환 지점에서 파괴될 위험 (ALG 필요)       |
| **인프라 요구 조건**     | 라우터/단말의 듀얼 스택 지원 및 주소 자원  | 터널링 게이트웨이 장비 구축 필요            | **NAT64 / DNS64 게이트웨이 설치 필수** |
| **오버헤드 특성**       | 메모리 소요 증가 (주소 자원 이중 관리)   | **캡슐화로 인한 오버헤드 및 MTU 단편화**    | **헤더 변환에 따른 라우터 CPU 성능 부담**   |
| **주요 적용 구간**      | 전환 초창기 백본 라우터 및 서버 구간     | 격리된 IPv6 아일랜드 망 간 IPv4 백본 통과  | IPv6-Only 스마트폰 ➔ 레거시 IPv4 인터넷 |

***

### **IV. 엔터프라이즈 망의 단계별 IPv6 이행(Migration) 로드맵**

**IMPORTANT**

1. **1단계 (Dual Stack 백본 구축)**: 코어 백본 라우터와 핵심 서버에 듀얼 스택을 적용하여 기존 IPv4 통신 품질을 유지한 채 IPv6 기반 통신망을 준비합니다.
2. **2단계 (NAT64/DNS64 전진 배치)**: 모바일 단말 및 신규 모바일 망을 IPv6-Only로 우선 구성하고, 레거시 IPv4 전용 서버와의 접점에 NAT64/DNS64 게이트웨이를 배치하여 변환 오버헤드를 통제합니다.
