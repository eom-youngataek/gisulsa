

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 "꽉 찬 후 버리는" 방식으로는 부족한가)
Ⅱ. RED 핵심 동작 원리
Ⅲ. RED 파라미터 체계 및 계산
Ⅳ. 기존 방식·변형 알고리즘 비교
Ⅴ. 결론 및 발전 방향
```

포인트: 개요에서 **"앞서 다룬 Slow Start·CUBIC·BBR이 '송신자 측에서 전송 속도를 조절하는 종단 간 혼잡 제어'라면, RED는 '라우터 버퍼가 꽉 차기 전에 선제적으로 일부 패킷을 무작위 폐기해 송신자에게 혼잡 신호를 미리 전달하는 라우터 측 능동 혼잡 회피 메커니즘'이다 — 기존 Tail-Drop이 버퍼가 꽉 찬 후 뒤에서 오는 패킷을 모두 버려 TCP 글로벌 동기화(Global Synchronization)를 유발하는 치명적 문제를 RED가 확률적 조기 폐기로 해소하며, QoS 아키텍처의 Active Queue Management(AQM) 표준 기법"**이라는 한 줄로 시작하면, 왜 이 답안이 앞서 다룬 TCP 혼잡 제어·CUBIC·BBR·QoS 시리즈 전체의 **라우터 측 혼잡 회피 핵심**인지 드러납니다.

---

#### Ⅱ. RED 핵심 동작 원리

**가. 기존 Tail-Drop의 문제점**

```
[Tail-Drop 방식의 한계]

라우터 버퍼: [■■■■■■■■■■] 100% 가득
                              ↓
이후 도착 패킷: 전부 폐기(Drop) 🚨

문제 1: TCP 글로벌 동기화 (Global Synchronization)
  버퍼 포화 → 다수 TCP 흐름 동시 패킷 손실 탐지
  → 모든 흐름이 동시에 Slow Start 진입
  → 버퍼 급격히 비워짐 → 링크 이용률 급락
  → 다시 동시 증가 → 반복 진동 🚨

문제 2: 버퍼 포화(Bufferbloat) 연계
  앞서 다룬 Bufferbloat: 버퍼가 꽉 찬 상태 지속
  → RTT 급증 → 실시간 서비스 품질 저하

문제 3: 특정 흐름 집중 폐기
  버퍼 도착 순서에 따라 특정 흐름만 손실
  → 불공정한 트래픽 처리
```

---

**나. RED 핵심 원리**

```
[RED 동작 원리]

평균 큐 길이(avg_q) 계산
       ↓
구간 판정:
  avg_q < min_th → 폐기 없음(정상)
  min_th ≤ avg_q < max_th → 확률적 폐기 (핵심!)
  avg_q ≥ max_th → 무조건 폐기

핵심 아이디어:
  "버퍼가 꽉 차기 전에
   일부 패킷을 무작위 폐기해
   송신자에게 혼잡 예고 신호 전달"

효과:
  → 특정 흐름만 집중 타격 없음 (무작위)
  → 글로벌 동기화 방지 (점진적·분산 신호)
  → 버퍼 사전 여유 확보 (사전 회피)
```

---

#### Ⅲ. RED 파라미터 체계 및 계산

**가. 4대 핵심 파라미터**

| 파라미터                 | 의미                 | 역할              |
| -------------------- | ------------------ | --------------- |
| ==**min_th (최소 임계값)**==  | 폐기 시작 큐 길이         | 이 값 미만: 폐기 없음   |
| ==**max_th (최대 임계값)**==  | 무조건 폐기 큐 길이        | 이 값 이상: 100% 폐기 |
| ==**max_p (최대 폐기 확률)**== | max_th 직전 최대 폐기 확률 | 보통 0.1(10%) 설정  |
| ==**w_q (큐 가중치)**==      | 평균 큐 계산 지수이동평균 가중치 | 낮을수록 평균이 완만     |

---

**나. 평균 큐 길이 계산**

```
[지수 이동 평균(EWMA) 기반 avg_q 계산]

avg_q = (1 - w_q) × avg_q + w_q × q_len

w_q: 큐 가중치 (보통 0.002)
q_len: 현재 실제 큐 길이

→ 순간적인 버스트를 평탄화
→ 안정적인 평균 큐 길이 추적
→ 일시적 급증에 과민 반응 방지
```

---

**다. 패킷 폐기 확률 계산**

```
[RED 폐기 확률 계산 공식]

구간 1: avg_q < min_th
  p_drop = 0 (폐기 없음)

구간 2: min_th ≤ avg_q < max_th
  p_b = max_p × (avg_q - min_th) / (max_th - min_th)
  p_a = p_b / (1 - count × p_b)
  → count: 마지막 폐기 이후 도착 패킷 수
  → 시간이 지날수록 폐기 확률 증가(강제성)

구간 3: avg_q ≥ max_th
  p_drop = 1 (100% 폐기·무조건)

[시각적 표현]
폐기확률
1.0│                          ┌──────
   │                          │
max│                  ╱───────┘
_p │              ╱
   │          ╱
 0 │──────────
   └──────────┴──────────┴──────→ avg_q
          min_th      max_th
```

---

**라. RED 동작 시나리오**

```
[예시: min_th=20, max_th=60, max_p=0.1]

avg_q=15: 정상 → 폐기 확률 0%
avg_q=40: 중간 → 폐기 확률 5% (선제 경고)
avg_q=50: 혼잡 → 폐기 확률 7.5% (추가 경고)
avg_q=60: 위험 → 폐기 확률 100% (강제)

→ avg_q=40 구간 일부 흐름 폐기 신호 수신
→ Slow Start 또는 Fast Recovery 진입
→ 전송률 감소 → avg_q 하락
→ 글로벌 동기화 없이 분산 대응 ✅
```

---

#### Ⅳ. 기존 방식·변형 알고리즘 비교

**가. Tail-Drop vs RED vs 변형 AQM 비교**

| 비교 항목           | Tail-Drop | RED    | WRED      | CoDel |
| --------------- | --------- | ------ | --------- | ----- |
| **폐기 시점**       | 버퍼 포화 후   | 사전 확률적 | 사전 확률적    | 지연 기반 |
| **글로벌 동기화**     | 발생 🚨     | 방지 ✅   | 방지 ✅      | 방지 ✅  |
| **QoS 차등**      | 불가        | 불가     | 가능 ✅      | 불가    |
| **Bufferbloat** | 심각 🚨     | 완화     | 완화        | 최적화 ✅ |
| **파라미터 튜닝**     | 불필요       | 복잡 🚨  | 복잡 🚨     | 단순 ✅  |
| **구현 복잡도**      | 낮음        | 중간     | 높음        | 낮음    |
| **적용 환경**       | 레거시       | 엔터프라이즈 | QoS 필요 환경 | 홈·ISP |

---

**나. 변형 RED 알고리즘 상세**

**① WRED (Weighted RED)**

```
[WRED 동작 원리]

IP DSCP·ToS 마킹 기반 트래픽 클래스별
서로 다른 min_th·max_th·max_p 적용

예시:
  Gold (AF11): min_th=40  max_th=80  max_p=0.05 ← 우선 보호
  Silver(AF21): min_th=30  max_th=70  max_p=0.10
  Bronze(AF31): min_th=20  max_th=60  max_p=0.15 ← 먼저 폐기

→ 중요 트래픽은 나중에 폐기
→ 덜 중요 트래픽이 먼저 희생
→ 앞서 다룬 QoS DiffServ 아키텍처 핵심 구현
```

**② GRED (Gentle RED)**

```
→ max_th 초과 후 100% 폐기 대신
  max_th ~ 2×max_th 구간에서
  max_p ~ 1.0으로 점진적 증가
→ 급격한 폐기 전환 완화
→ 부드러운 혼잡 신호 전달
```

**③ CoDel (Controlled Delay)**

```
→ 큐 길이가 아닌 패킷 대기 시간 기준
→ 5ms 이상 대기 패킷 폐기
→ Bufferbloat 직접 해소
→ 파라미터 자동 조정·튜닝 불필요
→ 현대 Linux 기본 AQM
```

---

**다. AQM 발전 계보**

```
[AQM 발전 흐름]

Tail-Drop (수동 대응)
    ↓ 글로벌 동기화 문제 → Floyd·Jacobson 1993
RED (능동 사전 회피)
    ↓ QoS 차등 필요
WRED (클래스별 차등 폐기)
    ↓ Bufferbloat 심화 → Nichols 2012
CoDel (지연 기반 AQM)
    ↓ CoDel + FQ(Fair Queue)
FQ-CoDel (현대 Linux 표준 AQM)
    ↓ 5G·초저지연 환경
PI2·L4S (저지연 AQM 차세대)
```

---

#### Ⅴ. 결론 및 발전 방향

**앞서 다룬 개념과의 연결**

| 연계 개념                        | 연결 내용                           |     |
| ---------------------------- | ------------------------------- | --- |
| **Slow Start·Fast Recovery** | RED 폐기 신호 → TCP 송신자 혼잡 제어 반응    |     |
| **CUBIC·BBR**                | BBR은 손실 아닌 RTT 기반 → RED와 보완적 관계 |     |
| **Bufferbloat**              | RED가 버퍼 사전 비워 Bufferbloat 완화    |     |
| **QoS·DiffServ**             | WRED가 DSCP 마킹 기반 차등 폐기로 QoS 구현  |     |
| **IBN·SDN**                  | SDN 컨트롤러가 RED 파라미터 동적 조정        |     |

**발전 방향**

```
①AI 기반 AQM
  트래픽 패턴 ML 예측으로
  min_th·max_th 동적 자동 조정
  앞서 다룬 AIOps·IBN 연계

②6G·초저지연 AQM
  앞서 다룬 6G의 0.1ms 목표
  L4S(Low Latency Low Loss Scalable)
  → 스칼라블한 ECN 기반 초저지연 AQM

③ECN 연계
  패킷 폐기 대신 ECN(Explicit Congestion Notification)
  마킹으로 송신자에게 혼잡 신호 전달
  → 패킷 손실 없는 혼잡 제어 실현
```

---

#### 기술사 답안 포인트

**Tail-Drop의 글로벌 동기화·Bufferbloat 한계 → RED 핵심 원리(버퍼 포화 전 확률적 조기 폐기) → 4대 파라미터(min_th·max_th·max_p·w_q) → EWMA 평균 큐 계산·3구간 폐기 확률 수식 → Tail-Drop·RED·WRED·CoDel 비교표 → WRED(DSCP 기반 클래스별 차등)·CoDel(지연 기반) 변형 → AQM 발전 계보(Tail-Drop→RED→WRED→CoDel→FQ-CoDel) → AI 기반 동적 조정·L4S·ECN 발전** 흐름으로 서술하면 완성도 높은 답안이 됩니다. **min_th~max_th 구간의 선형 확률 폐기로 글로벌 동기화를 방지하는 것**이 RED의 핵심 차별화 포인트입니다.


###I. 네트워크 병목 선제 제어, 라우터 혼잡 회피 RED의 개요

전통적인 라우터 큐 버퍼 관리 기법인 테일 드롭(Tail Drop)은 버퍼가 완전히 찰 때까지 패킷을 수용하다가, 마지막 유입 패킷들을 일괄 폐기합니다. 이는 동일 스위치를 통과하는 모든 TCP 송신자가 동시에 전송 속도를 낮추어 전체 네트워크 대역폭 활용 효율이 급락하는 TCP 전역 동기화 현상을 일으킵니다. **RED**는 대기 큐의 평균 길이를 지속 추적하여, **버퍼가 다 차기 전에 임계치 구간에 맞춰 유입 패킷을 임의의 선형 확률로 사전 폐기(Drop)**함으로써 혼잡을 능동적으로 우회하는 기술입니다.

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4NjAuNTc4IDI3MC4xIiB3aWR0aD0iODYwLjU3OCIgaGVpZ2h0PSIyNzAuMSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJRdWV1ZSIgZGF0YS10bz0iUGFzcyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7Y+J6regIO2BkCDtgazquLAgJmx0OyBtaW5fdGgiIHBvaW50cz0iMzc4LjMwNTUsNzYuOSAzNzguMzA1NSw4OC45IDE0Ni4xOSw4OC45IDE0Ni4xOSwxODEuMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUXVldWUiIGRhdGEtdG89IlJhbmRvbSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0ibWluX3RoICZsdDs9IO2Pieq3oCDtgZAg7YGs6riwICZsdDsgbWF4X3RoIiBwb2ludHM9IjQxMi4xMzQ1LDc2LjkgNDEyLjEzNDUsMTgxLjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlF1ZXVlIiBkYXRhLXRvPSJEcm9wQWxsIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLtj4nqt6Ag7YGQIO2BrOq4sCAmZ3Q7PSBtYXhfdGgiIHBvaW50cz0iNDQ1Ljk2MzQ5OTk5OTk5OTk1LDc2LjkgNDQ1Ljk2MzQ5OTk5OTk5OTk1LDg4LjkgNjk2LjIzMzUsODguOSA2OTYuMjMzNSwxODEuMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJRdWV1ZSIgZGF0YS10bz0iUGFzcyIgZGF0YS1sYWJlbD0i7Y+J6regIO2BkCDtgazquLAgJmx0OyBtaW5fdGgiPgogIDxyZWN0IHg9Ijg2LjE4OTk5OTk5OTk5OTk4IiB5PSI5NS45IiB3aWR0aD0iMTE5LjgxODAwMDAwMDAwMDAxIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTQ2LjA5OSIgeT0iMTExLjA1MDAwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7tj4nqt6Ag7YGQIO2BrOq4sCAmbHQ7IG1pbl90aDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJRdWV1ZSIgZGF0YS10bz0iUmFuZG9tIiBkYXRhLWxhYmVsPSJtaW5fdGggJmx0Oz0g7Y+J6regIO2BkCDtgazquLAgJmx0OyBtYXhfdGgiPgogIDxyZWN0IHg9IjMyNy42MzQ1IiB5PSIxMTkuOSIgd2lkdGg9IjE2OC41MjYwMDAwMDAwMDAwNCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjQxMS44OTc1MDAwMDAwMDAwNCIgeT0iMTM1LjA1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5taW5fdGggJmx0Oz0g7Y+J6regIO2BkCDtgazquLAgJmx0OyBtYXhfdGg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iUXVldWUiIGRhdGEtdG89IkRyb3BBbGwiIGRhdGEtbGFiZWw9Iu2Pieq3oCDtgZAg7YGs6riwICZndDs9IG1heF90aCI+CiAgPHJlY3QgeD0iNjMxLjIzMzUiIHk9Ijk1LjkiIHdpZHRoPSIxMjkuMzIyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjk1Ljg5NDUiIHk9IjExMS4wNTAwMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7Y+J6regIO2BkCDtgazquLAgJmd0Oz0gbWF4X3RoPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJRdWV1ZSIgZGF0YS1sYWJlbD0i65287Jqw7YSwIOuMgOq4sCDtgZAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzQ0LjQ3NjUiIHk9IjQwIiB3aWR0aD0iMTM1LjMxNiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDEyLjEzNDUiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7rnbzsmrDthLAg64yA6riwIO2BkDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUGFzcyIgZGF0YS1sYWJlbD0iMS4g7KCE65+JIO2GteqzvCA6IO2MqO2CtyDrk5zroa0g7JeG7J2MIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwIiB5PSIxODEuMiIgd2lkdGg9IjIxMi4zOCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE0Ni4xOSIgeT0iMTk5LjY0OTk5OTk5OTk5OTk4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij4xLiDsoITrn4kg7Ya16rO8IDog7Yyo7YK3IOuTnOuhrSDsl4bsnYw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJhbmRvbSIgZGF0YS1sYWJlbD0iMi4g7KGw6riwIOuTnOuhrSA6IOyEoO2YlSDtmZXrpaDsoIEg656c642kIO2PkOq4sCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyODAuMzgiIHk9IjE4MS4yIiB3aWR0aD0iMjYzLjUwOSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0MTIuMTM0NSIgeT0iMTk5LjY0OTk5OTk5OTk5OTk4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij4yLiDsobDquLAg65Oc66GtIDog7ISg7ZiVIO2ZleuloOyggSDrnpzrjaQg7Y+Q6riwPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJEcm9wQWxsIiBkYXRhLWxhYmVsPSIzLiDqsJXsoJwg7Y+Q6riwIDog7Jyg7J6FIO2MqO2CtyDsoITrn4kg65Oc66GtIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU3MS44ODkiIHk9IjE4MS4yIiB3aWR0aD0iMjQ4LjY4OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjY5Ni4yMzM1IiB5PSIxOTkuNjQ5OTk5OTk5OTk5OTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjMuIOqwleygnCDtj5DquLAgOiDsnKDsnoUg7Yyo7YK3IOyghOufiSDrk5zroa08L3RleHQ+CjwvZz4KPC9zdmc+)

---

### II. RED 알고리즘의 동작 매개변수 및 폐기 확률 공식

#### **1. 3대 동작 임계 영역**

- **min_th (최소 임계치)**: 큐 크기가 이보다 작으면 패킷을 정상 수용합니다.
- **max_th (최대 임계치)**: 큐 크기가 이보다 크면 유입 패킷을 즉시 전량 폐기합니다.
- **max_p (최대 폐기 확률)**: 평균 큐 크기가 max_thmax_th 직전일 때 적용되는 최대 드롭 확률입니다.

#### **2. 이동 평균 큐 크기 및 폐기 확률 계산**

- **평균 큐 크기 (Avg) 산출**: 지수 가중 이동 평균(EWMA) 필터 적용 Avg=(1−wq)×Avg+wq×qAvg=(1−wq​)×Avg+wq​×q (wqwq​: 가중치 필터, qq: 현재 큐 물리 크기)
- **임시 폐기 확률 (Pb​) 공식**: Pb=max_p×Avg−min_thmax_th−min_thPb​=max_p×max_th−min_thAvg−min_th​
- **최종 조정 폐기 확률 (Pa​) 공식**: 드롭의 고른 분포를 보장하기 위해 가중 보정 수행 Pa=Pb1−count×PbPa​=1−count×Pb​Pb​​ (countcount: 마지막 폐기 후 통과된 패킷 개수)

---

### III. 수동적 테일 드롭(Tail Drop) 기법과 능동적 RED(Random Early Detection)의 비교

| 비교 항목               | 📥 테일 드롭 (Tail Drop) 기법         | ⚡ 임의 조기 감지 (RED) 기법                       |     |
| ------------------- | ------------------------------- | ----------------------------------------- | --- |
| **폐기 발동 조건**        | 버퍼 메모리가 물리적으로 100% 가득 찬 시점      | **가중 평균 큐가 최소 임계치(min_thmin_th)에 도달한 시점** |     |
| **TCP 전역 동기화**      | 취약 (다중 세션의 패킷이 일괄 드롭되어 대역폭 급락)  | **예방 우수 (임의 세션만 순차 드롭되어 대역폭 유지)**         |     |
| **큐 전송 지연 (Delay)** | 높음 (버퍼가 항상 가득 찬 상태로 가동되어 지연 증가) | **낮음 (대기 큐의 평균 길이를 짧게 관리하여 저지연)**         |     |
| **장비 CPU 연산 오버헤드**  | 없음 (단순 버퍼 포인터 한계 비교만 수행)        | 보통 (유입 패킷마다 이동 평균 큐 연산 및 확률 계산 발생)        |     |

---

### IV. RED 알고리즘의 한계 보완을 위한 QoS 연계 기술

IMPORTANT

1. **서비스 차별화(WRED - Weighted RED)의 도입**: 모든 패킷을 동일 확률로 지우면 VIP 고객의 중요 트래픽까지 소실될 우려가 있습니다. 이를 방어하기 위해 패킷 헤더(IP Precedence, DSCP)의 우선순위에 따라 서로 다른 min_thmin_th와 max_pmax_p 값을 가중 적용하는 WRED 아키텍처를 도입해야 합니다.
2. **명시적 혼잡 통보(ECN)의 결합**: 패킷을 강제로 버려 TCP 재전송 오버헤드를 유발하는 대신, IP 헤더 내 **ECN 비트**를 11로 마킹하여 수신측에 혼잡을 통보하고 송신자의 전송 속도를 스스로 제어하게 만들어 패킷 손실율을 0%에 수렴시킬 수 있습니다.ㅋ

