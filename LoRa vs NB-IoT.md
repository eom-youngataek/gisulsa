### **저전력 광역 통신망(LPWAN) 양대 기술: LoRa vs NB-IoT**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 IoT에 5G가 아닌 별도의 저전력 통신망이 필요한가)
Ⅱ. LoRa(LoRaWAN) 핵심 원리
Ⅲ. NB-IoT 핵심 원리
Ⅳ. 비교 및 적용 체계
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 차량용 이더넷·TSN이 '차량 내부의 초고속·결정론적 통신'을 다뤘다면, LoRa와 NB-IoT는 정반대 극단의 통신 요구사항 — '데이터는 아주 조금씩, 아주 가끔, 대신 배터리 하나로 10년을 버티고 수 킬로미터 밖까지 도달해야 하는' 저전력 광역 통신망(LPWAN)이다 — 스마트미터·환경센서·가축 위치추적처럼 초당 수백Mbps는 전혀 필요 없지만 광범위한 커버리지와 극한의 전력 효율이 핵심인 영역에서, LoRa는 '비면허 대역에서 독자 확산대역 변조로 통신사 없이도 직접 구축 가능한 사설망 진영'을, NB-IoT는 '기존 LTE 면허 대역을 재사용해 통신사가 표준화된 셀룰러망으로 제공하는 진영'을 대표하며 이 두 기술의 선택이 IoT 프로젝트의 비용 구조·구축 주체·확장성을 근본적으로 가르는 핵심 결정"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.
![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MjIuNDkwOTk5OTk5OTk5OCAyODYuNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSI4MjIuNDkwOTk5OTk5OTk5OCIgaGVpZ2h0PSIyODYuNzAwMDAwMDAwMDAwMDUiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iU2Vuc29yIiBkYXRhLXRvPSJMb1JhIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQxMS44MDEyNDk5OTk5OTk4Nyw3Ni45IDQxMS44MDEyNDk5OTk5OTk4NywxMDAuOSAyMTkuMTc4NDk5OTk5OTk5OTYsMTAwLjkgMjE5LjE3ODQ5OTk5OTk5OTk2LDEyNC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTZW5zb3IiIGRhdGEtdG89Ik5CSW9UIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQxMS44MDEyNDk5OTk5OTk4Nyw3Ni45IDQxMS44MDEyNDk5OTk5OTk4NywxMDAuOSA2MDQuNDIzOTk5OTk5OTk5OCwxMDAuOSA2MDQuNDIzOTk5OTk5OTk5OCwxMjQuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTG9SYSIgZGF0YS10bz0iQ2xvdWQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjE5LjE3ODQ5OTk5OTk5OTk2LDE2MS44IDIxOS4xNzg0OTk5OTk5OTk5NiwxODUuOCA0MTEuODAxMjQ5OTk5OTk5ODcsMTg1LjggNDExLjgwMTI0OTk5OTk5OTg3LDIwOS44IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJOQklvVCIgZGF0YS10bz0iQ2xvdWQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNjA0LjQyMzk5OTk5OTk5OTgsMTYxLjggNjA0LjQyMzk5OTk5OTk5OTgsMTg1LjggNDExLjgwMTI0OTk5OTk5OTg3LDE4NS44IDQxMS44MDEyNDk5OTk5OTk4NywyMDkuOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU2Vuc29yIiBkYXRhLWxhYmVsPSJJb1Qg7IS87IScIOuFuOuTnCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzNDkuMzMwMjQ5OTk5OTk5ODYiIHk9IjQwIiB3aWR0aD0iMTI0Ljk0MiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQxMS44MDEyNDk5OTk5OTk4NyIgeT0iNTguNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPklvVCDshLzshJwg64W465OcPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJMb1JhIiBkYXRhLWxhYmVsPSJMb1JhIDog67mE7J246rCAIElTTSDrjIDsl60sIOyCrOyEpCDqsozsnbTtirjsm6jsnbQg7KeB7KCRIOq1rOy2lSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MCIgeT0iMTI0LjkiIHdpZHRoPSIzNTguMzU2OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjE5LjE3ODQ5OTk5OTk5OTk2IiB5PSIxNDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkxvUmEgOiDruYTsnbjqsIAgSVNNIOuMgOyXrSwg7IKs7ISkIOqyjOydtO2KuOybqOydtCDsp4HsoJEg6rWs7LaVPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJOQklvVCIgZGF0YS1sYWJlbD0iTkItSW9UIDog7J246rCAIOydtOuPme2GteyLoCDrjIDsl60sIO2GteyLoOyCrCDquLDsp4Dqta3rp50g7LCo7JqpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQyNi4zNTY5OTk5OTk5OTk4NiIgeT0iMTI0LjkiIHdpZHRoPSIzNTYuMTMzOTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI2MDQuNDIzOTk5OTk5OTk5OCIgeT0iMTQzLjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5OQi1Jb1QgOiDsnbjqsIAg7J2064+Z7Ya17IugIOuMgOyXrSwg7Ya17Iug7IKsIOq4sOyngOq1reunnSDssKjsmqk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkNsb3VkIiBkYXRhLWxhYmVsPSLtgbTrnbzsmrDrk5wgSW9UIOyEnOuyhCDsl7Drj5kiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzE4LjU3ODc0OTk5OTk5OTkiIHk9IjIwOS44IiB3aWR0aD0iMTg2LjQ0NDk5OTk5OTk5OTk2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDExLjgwMTI0OTk5OTk5OTg3IiB5PSIyMjguMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPu2BtOudvOyasOuTnCBJb1Qg7ISc67KEIOyXsOuPmTwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

***

#### Ⅱ. LoRa(LoRaWAN) 핵심 원리

**가. LoRa 물리 계층 기술**

```
[LoRa 변조 방식: CSS(Chirp Spread Spectrum)]

일반 변조와 달리 주파수가 시간에 따라
연속적으로 증가/감소하는 처프(Chirp) 신호 사용

특징:
  낮은 SNR(신호대잡음비)에서도 복조 가능
  → 잡음 속에서도 먼 거리 신호 검출 ✅
  → 대신 데이터 전송 속도는 매우 낮음(수백bps~수십kbps)

확산 인자(SF, Spreading Factor):
  SF7(빠름·근거리) ~ SF12(느림·원거리)
  SF가 클수록 전송시간 길어지나 도달거리·수신감도 향상
  → 거리와 속도의 트레이드오프를 애플리케이션이 선택
```

**나. LoRaWAN 네트워크 구조**

| 계층            | 구성요소        | 역할                          |
| :------------ | :---------- | :-------------------------- |
| **엔드 디바이스**   | 센서·미터       | LoRa 모듈 탑재, 배터리 구동          |
| **게이트웨이**     | LoRa 안테나+백홀 | 여러 채널 동시 수신, 인터넷 백홀로 데이터 전달 |
| **네트워크 서버**   | LoRaWAN NS  | 중복 수신 제거, 디바이스 관리, 보안       |
| **애플리케이션 서버** | 사용자 애플리케이션  | 실제 데이터 처리·시각화               |

**다. LoRaWAN 디바이스 클래스**

| 클래스         | 특징                       | 전력 소모         |
| :---------- | :----------------------- | :------------ |
| **Class A** | 상향 전송 후 짧은 하향 수신창 2개만 개방 | **최저(기본값)** ✅ |
| **Class B** | 비콘 기반 정기 수신창 추가          | 중간            |
| **Class C** | 거의 상시 수신 대기(전력 소모 큼)     | 높음(전원 연결 기기용) |

***

#### Ⅲ. NB-IoT 핵심 원리

**가. NB-IoT 물리 계층 기술**

```
[NB-IoT: 3GPP 표준 셀룰러 기반]

기존 LTE 대역 내 200kHz 협대역 사용
  ①Standalone: 독립 주파수 대역 신규 할당
  ②Guard Band: LTE 대역 사이 보호대역 활용
  ③In-band: 기존 LTE 자원블록 내 삽입
     → 통신사 기존 LTE 인프라 재사용 가능 ✅

핵심 저전력 기법:
  eDRX(확장 불연속 수신): 수신 대기 주기를 최대 몇 시간까지 연장
  PSM(Power Saving Mode): 유휴 시간 동안 완전 절전 모드
  → 배터리 수명 최대 10년 목표
```

**나. NB-IoT 핵심 특징**

| 항목          | 내용                           |
| :---------- | :--------------------------- |
| **표준화 주체**  | 3GPP Release 13(2016) 정식 표준  |
| **주파수**     | 라이선스(면허) 대역, 통신사 독점 운영       |
| **네트워크 구축** | 통신사(SKT·KT·LGU+) 셀룰러망 그대로 활용 |
| **보안**      | LTE와 동일한 SIM 기반 인증·암호화(USIM) |
| **이동성**     | 기지국 간 핸드오버 지원(제한적)           |

***

#### Ⅳ. 비교 및 적용 체계

**가. LoRa vs NB-IoT 전면 비교**

| 비교 항목          | LoRa(LoRaWAN)                   | NB-IoT                     |
| :------------- | :------------------------------ | :------------------------- |
| **주파수 대역**     | **비면허 대역**(ISM, 920\~923MHz 국내) | **면허 대역**(통신사 LTE 대역)      |
| **네트워크 구축 주체** | **자가 구축 가능**(사설망) ✅             | 통신사 의존                     |
| **초기 구축 비용**   | 게이트웨이 구매만(수십\~수백만원)             | **구축 비용 없음**(통신사 인프라 활용) ✅ |
| **운영 비용**      | 자체 운영(통신비 없음)                   | **디바이스당 월 통신료 발생** 🚨      |
| **커버리지**       | 게이트웨이 범위 내(시골 15km, 도심 2\~5km)  | **통신사 셀 커버리지 전역** ✅        |
| **이동성**        | 로밍 어려움 🚨                       | **핸드오버 지원** ✅              |
| **표준화**        | LoRa Alliance(산업 컨소시엄)          | **3GPP 국제 표준** ✅           |
| **전송속도**       | 0.3\~50kbps                     | 최대 250kbps                 |
| **배터리 수명**     | 10년 이상(SF 설정에 따라)               | 10년 목표(PSM/eDRX 의존)        |
| **보안**         | AES-128(애플리케이션+네트워크 계층 이중)      | LTE SIM 기반 상호인증            |

**나. 적용 시나리오별 선택 기준**

| 시나리오                   | 권장 기술      | 이유                           |
| :--------------------- | :--------- | :--------------------------- |
| **넓은 사유지·농장·공장 자체망**   | **LoRa**   | 통신비 없이 자가 구축, 밀집 센서 다수 배치    |
| **전국 분산 스마트미터(가스·수도)** | **NB-IoT** | 통신사 인프라 즉시 활용, 별도 게이트웨이 불필요  |
| **이동하는 자산 추적(물류·차량)**  | **NB-IoT** | 핸드오버로 이동 중 연결 유지             |
| **스타트업·소규모 실증(PoC)**   | **LoRa**   | 초기 투자 최소화, 빠른 자체 구축          |
| **정부·공공 인프라 대규모 사업**   | **NB-IoT** | 3GPP 표준·통신사 SLA로 안정성·책임소재 명확 |
| **초저비용 대량 센서(수천 개)**   | **LoRa**   | 디바이스당 월 통신료 없어 총소유비용(TCO) 유리 |

**다. 유사 LPWAN 기술과의 위치**

| 기술              | 유형                  | 비고                                     |
| :-------------- | :------------------ | :------------------------------------- |
| **Sigfox**      | 비면허 대역(LoRa 유사 진영)  | 초협대역(UNB), 프랑스 기업 주도, 국내 점유율 낮음        |
| **LTE-M(eMTC)** | 면허 대역(NB-IoT 유사 진영) | NB-IoT보다 속도 빠름, 음성·이동성 지원 강화           |
| **5G RedCap**   | 면허 대역 차세대           | 5G 코어 통합, IoT 중간 성능대(NB-IoT와 5G 사이) 겨냥 |

***

**(제언)** "LoRa와 NB-IoT의 선택은 기술 우열의 문제가 아니라 '누가 네트워크를 소유하고 그 비용을 어떤 방식으로 지불할 것인가'라는 비즈니스 모델의 문제에 가깝습니다. LoRa는 초기 자본 투자로 통신비를 영구히 절감하는 자가망 모델에 적합하고 NB-IoT는 초기 투자 없이 사용량만큼 통신사에 비용을 지불하는 클라우드형 모델에 가까우므로, 실무에서는 프로젝트의 센서 밀도(제곱킬로미터당 개수)·통신 빈도·예상 운영 기간을 먼저 계산해 손익분기점을 넘는 시점을 기준으로 결정해야 하며, 이동성이 필요한 자산 추적이 아니라면 처음부터 하나를 확정하기보다 소규모 LoRa 자체망으로 빠르게 실증(PoC)한 뒤 전국 확산 단계에서 NB-IoT로 전환하거나 두 기술을 용도별로 병행 운영하는 하이브리드 전략이 현실적입니다.

***

**앞서 다룬 개념과의 연결**

| 연계 개념             | 연결 내용                                                    |
| :---------------- | :------------------------------------------------------- |
| **차량용 이더넷·TSN**   | 초고속·결정론적 통신(TSN)과 초저속·비결정론적 통신(LPWAN)이 IoT 스펙트럼의 양극단을 형성 |
| **3GPP NTN 위성통신** | NB-IoT가 3GPP Release 17부터 NTN과 결합해 위성 기반 IoT로 확장되는 추세    |
| **온디바이스 NPU**     | LPWAN 센서 데이터를 게이트웨이 단에서 온디바이스 AI로 1차 필터링 후 전송하는 아키텍처 결합  |
| **AI 반도체 국산화**    | 국내 LoRa/NB-IoT 모듈 칩셋 국산화도 IoT 인프라 자립의 연장선                |
| **분산 스토리지 패브릭**   | 대량 IoT 센서 데이터의 시계열 저장에 앞서 다룬 와이드 컬럼 스토어 적용               |


**I. 초저전력 광대역 사물인터넷(LPWAN) 양대 산맥의 개요**

소형 IoT 단말기들은 수년 이상 배터리 교체 없이 수 km 떨어진 서버로 통신해야 합니다. 이를 위해 비인가 주파수 대역을 활용하여 사용자가 직접 사설 망을 구축할 수 있는 \*\*LoRa(Long Range)\*\*와, 기존 이동통신사의 인가된 LTE 대역 및 기지국 인프라를 차용하는 3GPP 표준의 \*\*NB-IoT(Narrowband IoT)\*\*가 사물인터넷 시장의 주도권을 두고 경쟁 및 보완 관계를 형성하고 있습니다.

***

### **II. LoRa 및 NB-IoT의 핵심 기술 메커니즘**

#### **1. LoRa (Chirp Spread Spectrum 기반)**

* **변조 기법**: 주파수가 시간에 따라 변하는 **CSS(Chirp Spread Spectrum)** 방식을 사용하여 잡음(Noise)과 간섭에 극도로 강합니다.
* **비인가 대역 (Sub-GHz)**: 920MHz 대역 등 비인가 주파수를 사용하므로 통신사 가입 없이 기지국(게이트웨이)을 직접 설치하여 무료 전송이 가능합니다.
* **Class 분류**: 수신 대기 방식에 따라 Class A(최저전력), Class B(주기적 수신), Class C(상시 수신)로 분율 적용됩니다.

#### **2. NB-IoT (3GPP 표준 이동통신 기반)**

* **변조 및 협대역**: 200kHz의 좁은 대역폭에서 QPSK/BPSK 변조를 사용하며, 기존 LTE 기지국의 In-band, Guard-band, Standalone 모드로 동작합니다.
* **전력 절감 기술**: \*\*PSM(Power Saving Mode)\*\*과 **eDRX(Extended Discontinuous Reception)** 기술을 적용하여 수신 대기 시 모뎀을 슬립 상태로 유지하여 배터리 수명을 10년 이상 연장합니다.

***

### **III. 사설망 중심 LoRa와 통신사망 중심 NB-IoT의 상세 비교**

| **비교 항목**      | **📡 LoRa (Long Range)**              | **📶 NB-IoT (Narrowband IoT)**        |
| :------------- | :------------------------------------ | :------------------------------------ |
| **표준화 기구**     | LoRa Alliance (Semtech 특허 중심)         | **3GPP (국제 이동통신 표준 규격)**              |
| **주파수 대역**     | 비인가 대역 (Unlicensed Sub-GHz, 920MHz)   | **인가 대역 (Licensed Cellular LTE 대역)**  |
| **변조 방식**      | 대역 확산 기법 (CSS: Chirp Spread Spectrum) | **OFDMA (하향) / SC-FDMA (상향)**         |
| **네트워크 구축**    | **사용자 자급형 사설 망(Private Net) 구축 가능**   | **통신사(Telco) 상용 기지국 망 전적으로 가입**       |
| **전송 속도 & 지연** | 저속 (0.3 \~ 50 kbps), 높은 전송 지연         | **상대적 고속 (20 \~ 250 kbps), 낮은 전송 지연** |
| **비용 구조**      | 초기 게이트웨이 구축비 발생, 월 통신비 없음             | 초기 장비비 저렴, **월별 통신 회선료 지속 발생**        |

***

### **IV. 서비스 요구사항별 기술 선택 가이드라인**

**IMPORTANT**

1. **LoRa가 유리한 유스케이스**: 통신사 음영 지역인 오지, 산악 지대, 대규모 자급형 스마트 팜(농장), 스마트 공장 등 통신 회선료 부담 없이 사설 독립망을 오랫동안 운용해야 하는 환경에 최적입니다.
2. **NB-IoT가 유리한 유스케이스**: 전국 단위 지자체 수도/가스 원격 검침, 도심지 지하 매설물 관리, 위치 이동 추적 등 전국 단위 통신사 커버리지가 이미 갖추어진 환경에 최적입니다.
