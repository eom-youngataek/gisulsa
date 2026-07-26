### **산업제어시스템 프로토콜 보안: Modbus/TCP 취약성 & DNP3 SAv5**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 산업제어 프로토콜이 사이버 보안의 최약점인가)
Ⅱ. Modbus/TCP 핵심 취약성
Ⅲ. DNP3 SAv5 보안 강화 원리
Ⅳ. 비교 및 적용 체계
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 일방향 데이터 다이오드가 'ICS/SCADA 환경에서 물리적으로 역방향을 차단하는 최후 방어선'이라면, Modbus/TCP와 DNP3는 그 ICS/SCADA 내부에서 PLC·RTU·HMI가 실제로 주고받는 산업제어 프로토콜 자체의 문제다 — 1979년 개발된 Modbus는 애초에 폐쇄된 시리얼 통신망을 전제로 설계되어 인증·암호화 개념 자체가 없었는데, 이를 그대로 이더넷·TCP/IP 위에 얹은 Modbus/TCP가 IT-OT 융합 시대에 그대로 인터넷에 노출되면서 치명적 보안 공백이 되었으며, DNP3는 여기에 SAv5(Secure Authentication version 5)라는 IEEE 1815-2012 표준의 챌린지-응답 기반 인증 계층을 추가해 전력망 등 핵심 인프라의 명령 위변조를 방어하는 현실적 대안으로 자리잡은 것"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.
\
![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3NDcuMjc5NDk5OTk5OTk5OSAyMDEuOCIgd2lkdGg9Ijc0Ny4yNzk0OTk5OTk5OTk5IiBoZWlnaHQ9IjIwMS44IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209Ik1vZGJ1cyIgZGF0YS10bz0iQXR0YWNrIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE5NC43MjU0OTk5OTk5OTk5OCw3Ni45IDE5NC43MjU0OTk5OTk5OTk5OCwxMjQuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRE5QMyIgZGF0YS10bz0iQXV0aCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI1NDEuODA5NSw3Ni45IDU0MS44MDk1LDEyNC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJNb2RidXMiIGRhdGEtbGFiZWw9Ik1vZGJ1cy9UQ1AgOiDtj4nrrLgg7KCE7IahICZhbXA7IOyduOymnSDrtoDsnqwg7Leo7JW97ISxIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjMwOS40NTA5OTk5OTk5OTk5NiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTk0LjcyNTQ5OTk5OTk5OTk4IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+TW9kYnVzL1RDUCA6IO2PieusuCDsoITshqEgJmFtcDsg7J247KadIOu2gOyerCDst6jslb3shLE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkF0dGFjayIgZGF0YS1sYWJlbD0i6rO16rKp7J6QIDog7KSR6rCE7J6QIOqzteqyqSAmYW1wOyDsoJzslrQg66qF66C5IOqwleygnCDso7zsnoUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDEuMTExNDk5OTk5OTk5OTgiIHk9IjEyNC45IiB3aWR0aD0iMzA3LjIyOCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE5NC43MjU0OTk5OTk5OTk5OCIgeT0iMTQzLjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7qs7XqsqnsnpAgOiDspJHqsITsnpAg6rO16rKpICZhbXA7IOygnOyWtCDrqoXroLkg6rCV7KCcIOyjvOyehTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRE5QMyIgZGF0YS1sYWJlbD0iRE5QMyBTQXY1IDogQ2hhbGxlbmdlLVJlc3BvbnNlIOuztOyZhCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MDQuODY3OTk5OTk5OTk5OTQiIHk9IjQwIiB3aWR0aD0iMjczLjg4MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI1NDEuODA5NSIgeT0iNTguNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkROUDMgU0F2NSA6IENoYWxsZW5nZS1SZXNwb25zZSDrs7TsmYQ8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkF1dGgiIGRhdGEtbGFiZWw9IuyViOyghO2VnCDsoJzslrQg66qF66C5IOqygOymnSAmYW1wOyBITUFDLVNIQTI1NiDrrLTqsrDshLEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzc2LjMzOTQ5OTk5OTk5OTkzIiB5PSIxMjQuOSIgd2lkdGg9IjMzMC45Mzk5OTk5OTk5OTk5NCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjU0MS44MDk0OTk5OTk5OTk4IiB5PSIxNDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyViOyghO2VnCDsoJzslrQg66qF66C5IOqygOymnSAmYW1wOyBITUFDLVNIQTI1NiDrrLTqsrDshLE8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

***

#### Ⅱ. Modbus/TCP 핵심 취약성

**가. Modbus/TCP 프로토콜 구조**

```
[Modbus/TCP 패킷 구조]

TCP/IP 헤더
  ↓
MBAP Header(7바이트)
  Transaction ID·Protocol ID·Length·Unit ID
  ↓
PDU(Protocol Data Unit)
  Function Code(1바이트) + Data
  예: FC=05(Single Coil Write)·주소·값

핵심 문제: 이 전체 패킷 어디에도
  인증 필드·암호화·무결성 검증이 없음 🚨
```

**나. 핵심 취약성 체계**

| 취약성 유형        | 내용                                            | 실제 위험                                    |
| :------------ | :-------------------------------------------- | :--------------------------------------- |
| **인증 부재**     | 어떤 클라이언트든 Master로 위장해 명령 전송 가능                | 앞서 다룬 **SSRF**로 내부망 진입 후 직접 PLC 제어 명령 전송 |
| **평문 전송**     | 모든 명령·응답이 암호화 없이 전송                           | 패킷 스니핑으로 제어 로직·설비 상태 완전 노출               |
| **무결성 검증 부재** | 전송 중 패킷 변조 여부 확인 불가                           | 중간자 공격으로 밸브 개폐 명령 값 조작                   |
| **재전송 공격 취약** | 타임스탬프·논스 없음                                   | 정상 명령 패킷 캡처 후 재전송으로 오작동 유발               |
| **기능 코드 남용**  | 위험한 FC(예: Write Multiple Registers)도 제한 없이 허용 | 안전 한계값을 벗어난 값 주입(예: 압력·온도 임계치 조작)        |

**다. 실제 공격 시나리오**

```
[Modbus/TCP 공격 시나리오: MITM 명령 조작]

정상 흐름:
  SCADA(Master) → Modbus/TCP → PLC(Slave)
  "FC=06, 주소=40001, 값=50" (밸브 개도 50%)

공격자 개입(앞서 다룬 파일리스·LotL로 내부망 침투 후):
  패킷 가로채기 → 값 조작
  "FC=06, 주소=40001, 값=100" (밸브 완전 개방)
  → PLC는 인증·무결성 검증 수단이 없어 그대로 수행 🚨
  → 물리적 설비 손상·안전사고 위험
```

***

#### Ⅲ. DNP3 SAv5 보안 강화 원리

**가. DNP3 기본 구조와 SAv5의 위치**

| 구분            | 내용                                                    |
| :------------ | :---------------------------------------------------- |
| **DNP3 기본**   | 1990년대 전력망 특화 설계 / Modbus보다 견고한 데이터 모델이나 초기 버전은 인증 없음 |
| **SAv2 (초기)** | 2007년 첫 보안 확장 / 이후 취약점 발견으로 v5로 전면 개정                 |
| **SAv5 (현행)** | IEEE 1815-2012 표준 / 챌린지-응답 기반 인증 프로토콜 도입              |

**나. SAv5 챌린지-응답 인증 메커니즘**

```
[DNP3 SAv5 인증 흐름]

①Outstation(RTU) → Master: 중요 명령 요청 감지
②Outstation → Master: Challenge 메시지 전송
   (난수 + HMAC 요구)
③Master: 사전 공유 세션키로 HMAC 계산
④Master → Outstation: Response(HMAC) 전송
⑤Outstation: HMAC 검증
   일치 → 명령 수행 ✅
   불일치 → 명령 거부 + 보안 이벤트 로그 🚨

핵심: 매 중요 명령마다 챌린지-응답 재수행
      재전송 공격 방어(난수 매번 변경)
```

**다. SAv5 핵심 보안 기능**

| 기능                       | 원리                             | 방어 대상                |
| :----------------------- | :----------------------------- | :------------------- |
| **인증(Authentication)**   | HMAC-SHA256 기반 챌린지-응답          | Master 신원 위장 공격      |
| **키 관리(Key Management)** | Update Key로 Session Key 주기적 갱신 | 키 유출 시 피해 범위 제한      |
| **역할 기반 접근**             | 사용자별 권한 등급 구분                  | 내부자 권한 오남용           |
| **선택적 적용**               | 중요 명령(제어)만 인증, 일반 폴링은 평문 유지 가능 | 성능·지연 영향 최소화         |
| **감사 로그**                | 인증 실패 이벤트 자동 기록                | 앞서 다룬 **디지털 포렌식** 연계 |

***

#### Ⅳ. 비교 및 적용 체계

**가. Modbus/TCP vs DNP3(SAv5 미적용) vs DNP3 SAv5 비교**

| 비교 항목         | Modbus/TCP          | DNP3(기본)           | DNP3 SAv5            |
| :------------ | :------------------ | :----------------- | :------------------- |
| **인증**        | 없음 🚨               | 없음 🚨              | **챌린지-응답 인증** ✅      |
| **암호화**       | 없음 🚨               | 없음 🚨              | 선택적(별도 TLS 결합 가능)    |
| **무결성 검증**    | 없음 🚨               | CRC(오류 검출용, 보안 아님) | **HMAC 기반 무결성** ✅    |
| **재전송 공격 방어** | 없음 🚨               | 없음 🚨              | **난수 기반 방어** ✅       |
| **주 적용 분야**   | 공장 자동화·경공업          | 전력망(변전소·송배전)       | **전력망 보안 강화 구간**     |
| **표준화**       | Modbus Organization | IEEE 1815          | **IEEE 1815-2012** ✅ |

**나. Modbus/TCP 보안 강화 대안**

| 대안                      | 원리                      | 한계                      |
| :---------------------- | :---------------------- | :---------------------- |
| **Modbus/TCP over TLS** | TCP 계층에 TLS 래핑(포트 802)  | PLC 성능 제약으로 구형 장비 미지원 多 |
| **앞서 다룬 데이터 다이오드**      | 물리적 단방향 통제로 원천 차단       | 양방향 제어 불가(모니터링 전용)      |
| **앞서 다룬 NGFW/방화벽 룰**    | Modbus DPI로 위험 FC 코드 차단 | 애플리케이션 계층 세밀 정책 필요      |
| **네트워크 세그멘테이션**         | Purdue 모델 기반 계층 분리      | 근본 프로토콜 취약성은 미해결        |

**다. 산업별 적용 우선순위**

| 산업 분야             | 권장 프로토콜/대책                  | 이유                     |
| :---------------- | :-------------------------- | :--------------------- |
| **전력망(변전소)**      | **DNP3 SAv5 필수**            | 국가 핵심 인프라·IEEE 1815 요구 |
| **일반 공장 자동화**     | Modbus/TCP + 망분리 + NGFW DPI | 비용 대비 실용적 절충           |
| **상수도·가스**        | DNP3 SAv5 또는 IEC 62351 결합   | 안전사고 직결 설비             |
| **레거시 PLC 다수 환경** | 데이터 다이오드 + 세그멘테이션           | 프로토콜 교체 불가 시 물리적 차단    |

***

**(제언)** "Modbus/TCP의 근본 문제는 '평생 물리적으로 고립된 시리얼 케이블 안에서만 살 것을 전제로 설계된 프로토콜을 그대로 인터넷 프로토콜 스택 위에 얹었다'는 설계 시대의 근본적 불일치이며, 이는 패치로 완전히 해결되지 않으므로 DNP3 SAv5처럼 프로토콜 자체에 인증을 내장하거나 그것이 불가능한 레거시 환경에서는 앞서 다룬 일방향 데이터 다이오드·NGFW DPI·네트워크 세그멘테이션을 다층으로 결합해야 합니다. 실무적으로는 신규 전력망 구축 시 DNP3 SAv5를 기본 채택하되 이미 설치된 수만 대의 Modbus 레거시 PLC를 일괄 교체하는 것은 비현실적이므로, 앞서 다룬 Purdue 모델의 계층 분리와 데이터 다이오드로 물리적 방어선을 먼저 구축한 뒤 점진적으로 프로토콜 보안을 강화하는 단계적 전환 전략이 산업제어시스템 보안 투자의 현실적 우선순위입니다.

***

**앞서 다룬 개념과의 연결**

| 연계 개념             | 연결 내용                                           |
| :---------------- | :---------------------------------------------- |
| **일방향 데이터 다이오드**  | Modbus 레거시 환경에서 프로토콜 보안 부재를 물리적으로 보완하는 최후 방어선   |
| **NGFW·DPI**      | Modbus 위험 기능 코드(FC=05·06·16 등)를 애플리케이션 계층에서 필터링 |
| **SSRF**          | 웹 애플리케이션 취약점을 통해 OT 네트워크의 Modbus 장비까지 침투하는 경로   |
| **파일리스·LotL**     | ICS 환경 침투 후 흔적 없이 Modbus 명령을 직접 전송하는 공격 기법      |
| **디지털 포렌식 5대 원칙** | SAv5의 인증 실패 로그가 사고 조사 시 핵심 증거로 활용               |
