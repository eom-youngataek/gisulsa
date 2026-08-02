#### **확률 분포 간 거리 측정: JSD (Jensen-Shannon Divergence)**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 "거리"가 아니라 "발산"인가) — 3~4줄
Ⅱ. JSD 수식 체계 (본론①, 도식 1개 필수)
Ⅲ. KL 발산과의 비교·JSD 활용 단계별 흐름 (핵심 배점)
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 Demographic Parity의 DPR이 '집단 간 예측 비율 차이'를 단순 비율로 측정했다면, JSD는 '두 확률 분포 전체가 얼마나 다른가'를 정보이론 관점에서 측정한다 — 앞서 다룬 MLOps의 데이터 드리프트 탐지(PSI·KL Divergence)에서 KL 발산의 치명적 한계인 '비대칭성·무한대 발산'을 수학적으로 완전히 극복한 것이 JSD이며, GAN의 학습 목표 자체가 JSD를 0으로 수렴시키는 것"\*\*이라는 한 줄로 시작하면, 왜 이 답안이 앞서 다룬 확률론·GAN·MLOps 시리즈 전체의 **정보이론적 뼈대**인지 드러납니다.

***

#### Ⅱ. JSD 수식 체계

| 지표                       | 내용                                                                                                     |
| :----------------------- | :----------------------------------------------------------------------------------------------------- |
| **KL 발산(KL Divergence)** | D\_KL(P‖Q) = Σ P(x) log P(x)/Q(x). **비대칭** — D\_KL(P‖Q) ≠ D\_KL(Q‖P). Q(x)=0인 지점에서 **무한대 발산**하는 치명적 한계 |
| **혼합 분포 M**              | M = (P + Q) / 2. P와 Q의 **중간 참조 분포**. JSD의 핵심 매개체 — 양쪽을 각각 M과 비교함으로써 비대칭 문제를 수학적으로 제거                   |
| **JSD 정의**               | JSD(P‖Q) = ½ · D\_KL(P‖M) + ½ · D\_KL(Q‖M). 항상 **대칭** — JSD(P‖Q) = JSD(Q‖P)                            |
| **JSD 범위**               | 0 ≤ JSD ≤ 1 (로그 밑 2 사용 시). **JSD=0**: 두 분포 완전 동일. **JSD=1**: 두 분포 완전 상이. KL 발산과 달리 **유한·안정적**          |
| **JSD 거리**               | √JSD(P‖Q) = Jensen-Shannon **Distance**. 삼각부등식을 만족하는 **진정한 거리(Metric)**                                |

→ 암기: **"KL은 짝사랑(비대칭)이고 무한대까지 치솟는데, JSD는 중간에 M을 세워 양쪽을 공평하게 비교하는 대칭 심판 — 결과는 항상 0과 1 사이"** — 앞서 다룬 \*\*"GAN의 미니맥스 목적함수"\*\*가 수렴하면 생성 분포와 실제 분포의 JSD가 최소화되는 것이 바로 이 수식의 의미입니다.

#### 도식화 제안

```
[KL 발산 vs JSD 구조 비교]

KL 발산:
  P ──→ Q 방향만 측정 (비대칭·무한대 발산 위험)
  D_KL(P‖Q) ≠ D_KL(Q‖P)  🚨

JSD:
  P ──→ M ←── Q
       ↑
  M = (P+Q)/2  ← 중간 참조 분포 (핵심!)
  JSD = ½·D_KL(P‖M) + ½·D_KL(Q‖M)
  → 대칭·유한(0~1)·안정적  ✅
```

***

#### Ⅲ. KL 발산과의 비교·JSD 활용 단계별 흐름 — 핵심 배점

**함정 방지: "JSD는 KL 발산을 개선한 것"이라고만 답하면 절반. KL 발산의 비대칭·무한대 발산이 실제로 어떤 문제를 일으키는지, JSD가 이를 어떻게 수학적으로 해소하는지, 그리고 GAN·MLOps·데이터 드리프트에서 어떻게 쓰이는지를 단계별로 보여줘야 완성됩니다.**

| 단계         | 활동                                                                           |
| :--------- | :--------------------------------------------------------------------------- |
| **분포 측정**  | 비교 대상 두 분포 P(실제)·Q(예측·생성) 정의. 이산 분포는 Σ, 연속 분포는 ∫로 계산                         |
| **M 산출**   | 혼합 분포 M = (P+Q)/2 계산. **Q(x)=0인 구간도 M(x)=P(x)/2 > 0으로 안전** — KL 무한대 발산 원천 차단 |
| **JSD 계산** | JSD = ½·D\_KL(P‖M) + ½·D\_KL(Q‖M) 계산. 결과는 반드시 \[0, 1] 구간                     |
| **판정**     | JSD ≈ 0: 분포 동일(드리프트 없음·GAN 수렴). JSD → 1: 분포 완전 상이(드리프트 심각·GAN 미수렴)           |
| **대응**     | 앞서 다룬 **"MLOps CT(Continuous Training)"** — JSD 임계값 초과 시 자동 재학습 트리거          |

→ 암기: **"P와 Q를 직접 비교하지 말고 중간에 M을 세워라 — 그러면 비대칭도, 무한대도 사라지고 항상 0\~1 사이의 안전한 숫자가 나온다"**

**GAN과의 직접 연결** (중요): 앞서 다룬 \*\*"GAN의 미니맥스 목적함수 min\_G max\_D V(D,G)"\*\*가 수렴할 때 최적 판별자 D\*가 존재하면 목적함수의 값은 \*\*-log4 + 2·JSD(p\_data‖p\_G)\*\*로 표현된다 — 즉 **GAN 학습의 궁극적 목표는 p\_G와 p\_data 사이의 JSD를 0으로 수렴시키는 것**이며, 앞서 다룬 \*\*"WGAN이 JS 발산 대신 Wasserstein 거리로 교체한 이유"\*\*도 초기 학습 시 JSD가 포화되어 그래디언트 소실이 발생하기 때문입니다.

#### 도식화 제안

```
[JSD 활용 단계별 흐름]

①분포 정의
  P = 실제 데이터 분포 / Q = 생성·예측·배포 후 데이터 분포
     ↓
②M 산출: M = (P+Q)/2
  → Q(x)=0 구간도 M(x)>0 → KL 무한대 발산 차단 ✅
     ↓
③JSD 계산: ½·D_KL(P‖M) + ½·D_KL(Q‖M) → [0, 1] 유한값
     ↓
④판정
  JSD ≈ 0 → 분포 동일 (GAN 수렴 / 드리프트 없음)
  JSD → 1 → 분포 상이 (GAN 미수렴 / 드리프트 심각 🚨)
     ↓
⑤대응
  [GAN] WGAN으로 전환 (JSD 포화→Wasserstein 거리로 교체)
  [MLOps] CT 자동 트리거 → 데이터 재수집·모델 재학습
```

**앞서 다룬 GAN·MLOps·Diffusion과의 연결**: 이런 **"M을 매개로 한 JSD 계산, 0\~1 유한 범위 판정"** 이 실제로는 앞서 다룬 \*\*"GAN의 모드 붕괴 원인 분석"\*\*에서 D\_KL이 포화될 때 그래디언트가 소실되는 이유를 설명하고, 앞서 다룬 \*\*"MLOps의 데이터 드리프트 탐지(PSI·KL Divergence)"\*\*에서 KL 대신 JSD를 쓰면 Q(x)=0 구간의 무한대 폭발 없이 안정적으로 드리프트를 감지할 수 있음을 보여줍니다.

***

#### Ⅳ. 결론

JSD는 \*\*"KL 발산의 비대칭·무한대 발산 한계를 중간 참조 분포 M=(P+Q)/2 도입으로 완전히 극복하고, JSD = ½·D\_KL(P‖M) + ½·D\_KL(Q‖M) 수식으로 두 확률 분포 간 차이를 항상 0\~1 사이의 유한·대칭·안정적 값으로 측정하는 정보이론 지표"\*\*이며, 특히 \*\*"GAN 학습 목표가 JSD=0 수렴, WGAN 등장 이유가 초기 JSD 포화, MLOps 드리프트 탐지가 KL 대신 JSD로 안전성 확보"\*\*라는 세 연결이 핵심입니다 — 이는 앞서 다룬 \*\*KL 발산(정보이론 기반) → GAN 미니맥스(JSD 최소화 목표) → WGAN(JSD 한계 극복) → MLOps 드리프트 탐지(실무 적용)\*\*를 하나로 잇는 정보이론적 교량이며, \*\*"두 분포가 얼마나 다른가를 측정하는 모든 문제는, 결국 KL의 짝사랑을 고친 JSD로 귀결된다"\*\*는 결론으로 이어집니다.

### **I. 두 확률 분포의 통계적 거리 측정, JSD의 개요**

머신러닝 및 데이터 과학에서 원본 데이터 분포와 합성 데이터(혹은 모델 예측) 분포 간의 차이를 정밀 계량하는 것은 모델 성능 평가의 핵심입니다. \*\*JSD(젠센-샤논 다이버전스)\*\*는 기존 쿨백-라이블러 발산(KLD)의 비대칭성(P∥Q≠Q∥P*P*∥*Q*=*Q*∥*P*) 문제를 해결하기 위해, 두 분포 P*P*와 Q*Q*의 평균 분포인 M*M*을 상정하고 각 분포와 M*M* 간의 KLD 평균값으로 정의한 **대칭형 거리 측정 지표**입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MzAuOTM3OTk5OTk5OTk5OSAyODYuNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSI4MzAuOTM3OTk5OTk5OTk5OSIgaGVpZ2h0PSIyODYuNzAwMDAwMDAwMDAwMDUiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUk9PVCIgZGF0YS10bz0iQXZlcmFnZSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0NDkuOTI1NDk5OTk5OTk5OTQsNzYuOSA0NDkuOTI1NDk5OTk5OTk5OTQsOTQuOSAxNzguNzkzOTk5OTk5OTk5OTgsOTQuOSAxNzguNzkzOTk5OTk5OTk5OTgsMTEyLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlJPT1QiIGRhdGEtdG89IktMX1AiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDQ5LjkyNTQ5OTk5OTk5OTk0LDc2LjkgNDQ5LjkyNTQ5OTk5OTk5OTk0LDk0LjkgNDQ5LjkyNTQ5OTk5OTk5OTk0LDk0LjkgNDQ5LjkyNTQ5OTk5OTk5OTk0LDExMi45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJST09UIiBkYXRhLXRvPSJLTF9RIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQ0OS45MjU0OTk5OTk5OTk5NCw3Ni45IDQ0OS45MjU0OTk5OTk5OTk5NCw5NC45IDY4Ni42MDA0OTk5OTk5OTk5LDk0LjkgNjg2LjYwMDQ5OTk5OTk5OTksMTEyLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IktMX1AiIGRhdGEtdG89IlN1bSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0NDkuOTI1NDk5OTk5OTk5OTQsMTQ5LjggNDQ5LjkyNTQ5OTk5OTk5OTk0LDE3OS44IDU2OC4yNjI5OTk5OTk5OTk5LDE3OS44IDU2OC4yNjI5OTk5OTk5OTk5LDIwOS44IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJLTF9RIiBkYXRhLXRvPSJTdW0iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNjg2LjYwMDQ5OTk5OTk5OTksMTQ5LjggNjg2LjYwMDQ5OTk5OTk5OTksMTc5LjggNTY4LjI2Mjk5OTk5OTk5OTksMTc5LjggNTY4LjI2Mjk5OTk5OTk5OTksMjA5LjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJPT1QiIGRhdGEtbGFiZWw9IkpTRCDqs4TsgrAg66mU7Luk64uI7KaYIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM2OC45Mjk0OTk5OTk5OTk5NiIgeT0iNDAiIHdpZHRoPSIxNjEuOTkyIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0NDkuOTI1NDk5OTk5OTk5OTQiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5KU0Qg6rOE7IKwIOuplOy7pOuLiOymmDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQXZlcmFnZSIgZGF0YS1sYWJlbD0iMS4g7Y+J6regIOu2hO2PrCBNIDogUOyZgCBR7J2YIOykkeqwhCDrtoTtj6wg7IKw7LacIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwIiB5PSIxMTIuOSIgd2lkdGg9IjI3Ny41ODc5OTk5OTk5OTk5NyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE3OC43OTM5OTk5OTk5OTk5OCIgeT0iMTMxLjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij4xLiDtj4nqt6Ag67aE7Y+sIE0gOiBQ7JmAIFHsnZgg7KSR6rCEIOu2hO2PrCDsgrDstpw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IktMX1AiIGRhdGEtbGFiZWw9IjIuIEtMX1AgOiBQ7JmAIE3snZggS0xEIOyCsOy2nCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzNDUuNTg3OTk5OTk5OTk5OTciIHk9IjExMi45IiB3aWR0aD0iMjA4LjY3NDk5OTk5OTk5OTk4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDQ5LjkyNTQ5OTk5OTk5OTk0IiB5PSIxMzEuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjIuIEtMX1AgOiBQ7JmAIE3snZggS0xEIOyCsOy2nDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iS0xfUSIgZGF0YS1sYWJlbD0iMy4gS0xfUSA6IFHsmYAgTeydmCBLTEQg7IKw7LacIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU4Mi4yNjI5OTk5OTk5OTk5IiB5PSIxMTIuOSIgd2lkdGg9IjIwOC42NzQ5OTk5OTk5OTk5OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjY4Ni42MDA0OTk5OTk5OTk5IiB5PSIxMzEuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjMuIEtMX1EgOiBR7JmAIE3snZggS0xEIOyCsOy2nDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU3VtIiBkYXRhLWxhYmVsPSI0LiDstZzsooUg7ZWp7IKwIDog65GQIEtMROydmCDtj4nqt6Ag6rOE7IKw7ZWY7JesIOuMgOy5reyEsSDsmYTshLEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzkxLjMwNzQ5OTk5OTk5OTkiIHk9IjIwOS44IiB3aWR0aD0iMzUzLjkxMSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI1NjguMjYyOTk5OTk5OTk5OSIgeT0iMjI4LjI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij40LiDstZzsooUg7ZWp7IKwIDog65GQIEtMROydmCDtj4nqt6Ag6rOE7IKw7ZWY7JesIOuMgOy5reyEsSDsmYTshLE8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

***

### **II. JSD의 수리적 공식 및 핵심 특징**

#### **1. 수학적 공식**

JSD(P∥Q)=12DKL(P∥M)+12DKL(Q∥M)*JSD*(*P*∥*Q*)=21​*DKL*​(*P*∥*M*)+21​*DKL*​(*Q*∥*M*)

* M=12(P+Q)*M*=21​(*P*+*Q*) (두 분포의 가중 평균 분포)
* DKL(A∥B)=∑xA(x)log⁡A(x)B(x)*DKL*​(*A*∥*B*)=∑*x*​*A*(*x*)log*B*(*x*)*A*(*x*)​ (쿨백-라이블러 발산 공식)

#### **2. JSD의 3대 수학적 장점**

* **대칭성 (Symmetry)**: JSD(P∥Q)=JSD(Q∥P)*JSD*(*P*∥*Q*)=*JSD*(*Q*∥*P*)가 성립하여 객관적 거리 척도로 사용 가능합니다.
* **유한성 (Boundedness)**: 밑이 2인 로그 사용 시 항상 0≤JSD(P∥Q)≤10≤*JSD*(*P*∥*Q*)≤1 범위를 가집니다.
* **삼각부등식 성립 (Metric)**: JSD의 제곱근값(JSD*JSD*​)은 엄밀한 수학적 거리 공간(Metric Space) 정의를 충족합니다.

***

### **III. 비대칭성 KLD(쿨백-라이블러)와 대칭성 JSD(젠센-샤논)의 상세 비교**

| **비교 항목**      | **📉 쿨백-라이블러 발산 (KLD)**                                 | **📊 젠센-샤논 발산 (JSD)**                                      |
| :------------- | :------------------------------------------------------ | :--------------------------------------------------------- |
| **대칭성 여부**     | 비대칭 (DKL(P∥Q)≠DKL(Q∥P)*DKL*​(*P*∥*Q*)=*DKL*​(*Q*∥*P*)) | **완전 대칭 (JSD(P∥Q)=JSD(Q∥P)*JSD*(*P*∥*Q*)=*JSD*(*Q*∥*P*))** |
| **값의 범위**      | 00 \~ 무한대 (∞∞)                                          | **00 \~ 11 사이로 표준화 (로그 밑이 2일 때)**                          |
| **두 분포 불일치 시** | 분포의 겹침(Support)이 없을 경우 ∞∞ 발산                            | **평균 분포 M을 사용하여 항상 유한한 상한값으로 수렴**                          |
| **주요 활용 분야**   | 변이형 오토인코더(VAE) 손실함수, 확률 근사                              | **GAN(생성기-판별기) 최적화 손실, 합성 데이터 유사도 평가**                     |

***

### **IV. 정형 합성 데이터 검증 시 JSD의 공학적 활용 가이드라인**

**IMPORTANT**

1. **범주형(Categorical) 데이터 분포 검증**: 수치형 데이터 비교에는 KS-test를 주로 사용하지만, 범주형 열(예: 성별, 직급 등)은 연속형 CDF를 그릴 수 없으므로 원본과 합성본의 빈도분포 확률 간 JSD 값을 계산하여 범주형 복제 충실도를 0에 가깝도록 검증해야 합니다.
2. **Sparsity 처리 (평활화 적용)**: 특정 범주 값이 원본에만 존재하고 합성 데이터에는 아예 발생하지 않은 경우 분모가 0이 되는 오류가 생길 수 있으므로, 아주 작은 상수(Laplace Smoothing 등)를 빈도 테이블에 미세하게 더해 연산 정합성을 유지해야 합니다.
