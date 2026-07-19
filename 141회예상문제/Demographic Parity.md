#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 "정확도"가 아니라 "공정성"인가) — 3~4줄
Ⅱ. 공정성 지표 체계 (본론①, 도식 1개 필수)
Ⅲ. Demographic Parity 측정·판정·완화 방법 (핵심 배점)
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 AI 윤리기준의 ③다양성 존중·인공지능기본법의 채용·대출 고영향 AI 규제는 모두 '차별 금지'를 원칙으로 선언하는데, 정작 그 원칙을 실제로 측정·수치화하는 도구가 없다면 선언에 그친다 — Demographic Parity는 '보호 속성과 무관하게 긍정 결과 비율이 동일해야 한다'는 공정성을 P(Ŷ=1│A=0) = P(Ŷ=1│A=1)이라는 수식 하나로 정량화하는 핵심 측정 도구다"\*\*라는 한 줄로 시작하면, 왜 이 답안이 앞서 다룬 AI 윤리·법제도 시리즈 전체의 **기술적 실행 수단**인지 드러납니다.

***

#### Ⅱ. AI 공정성 지표 체계

| 지표                     | 내용                                                                                        |
| :--------------------- | :---------------------------------------------------------------------------------------- |
| **Demographic Parity** | 보호 속성(성별·인종 등)과 **무관하게 집단별 긍정 예측 비율이 동일**한 정도. 채용·대출 AI의 핵심 지표                            |
| **Equalized Odds**     | 정답(Y)을 조건으로 집단별 **TPR(참양성률)·FPR(거짓양성률)이 동일**한 정도. 형사사법·의료 AI의 핵심 지표                       |
| **Equal Opportunity**  | 앞서 다룬 **AI 윤리기준의 ①인권 보장** — 긍정 집단(Y=1)에서만 **TPR 동일**을 요구하는 완화 버전                          |
| **Calibration**        | 동일한 예측 점수를 받은 개인이 집단에 관계없이 **동일한 실제 결과 비율**을 가져야 하는 정도                                    |
| **공정성 불가능 정리**         | 앞서 다룬 **"AI 윤리기준·법제도의 한계"** — 위 지표들을 **동시에 완벽히 만족하는 모델은 수학적으로 존재 불가** (Chouldechova 2017) |

→ 암기: **"집단 결과 같고, 오류율 같고, 기회 같고, 점수가 같아야 한다 — 그런데 넷을 동시에 만족하는 AI는 없다"** — 앞서 다룬 \*\*"AI 윤리기준 10대 요건의 ③다양성 존중"\*\*이 여기서 \*\*"집단별 긍정 예측 비율 동등"\*\*이라는 측정 가능한 수치로 구체화됩니다.

#### 도식화 제안

```
[AI 공정성 지표 체계]

보호 속성(성별·인종·나이·종교·장애)
         ↓ 영향 여부 측정
┌─────────────────────────────────────┐
│ Demographic Parity  : P(Ŷ=1│A=0) = P(Ŷ=1│A=1)   ← 결과 동등  │
│ Equalized Odds      : TPR·FPR 집단 간 동등          ← 오류율 동등 │
│ Equal Opportunity   : TPR만 집단 간 동등             ← 기회 동등  │
│ Calibration         : 예측 점수 의미 집단 간 동등     ← 점수 동등  │
└─────────────────────────────────────┘
         ↓ 동시 만족 불가 (Impossibility Theorem)
  도메인 위험에 따라 우선 지표 1개 선택 필수
```

***

#### Ⅲ. Demographic Parity 측정·판정·완화 방법 — 핵심 배점

**함정 방지: "보호 속성과 무관하게 동등해야 한다"고만 답하면 절반. DPD·DPR 수식으로 실제 수치를 산출하고, 80% 규칙으로 판정하고, 전처리·학습중·후처리 3단계로 완화하는 구체적 흐름을 보여줘야 완성됩니다.**

| 단계      | 활동                                                                       |
| :------ | :----------------------------------------------------------------------- |
| **측정**  | **DPD(Difference)** 산출 — P(Ŷ=1│A=1) − P(Ŷ=1│A=0), │DPD│ ≤ 0.1이면 허용       |
| **측정**  | **DPR(Ratio)** 산출 — P(Ŷ=1│A=1) ÷ P(Ŷ=1│A=0), 0.8 이상이면 허용                 |
| **판정**  | **EEOC 80% 규칙** — 불리한 집단 선발률이 유리한 집단의 80% 미만이면 **차별로 판정·AI 폐기·법적 제재**    |
| **완화①** | **전처리(Pre-processing)** — 앞서 다룬 \*\*"합성데이터·SMOTE"\*\*로 학습 데이터의 집단 불균형 보정 |
| **완화②** | **학습 중(In-processing)** — 손실함수에 **공정성 제약 조건**을 추가해 편향 최소화 방향으로 학습        |
| **완화③** | **후처리(Post-processing)** — 집단별 **분류 임계값을 차등 적용**해 예측 결과 동등화              |

→ 암기: **"먼저 DPD·DPR로 수치를 재고, 80%룰로 판정하고, 편향이 있으면 데이터를 고치거나(전처리), 학습 목표에 넣거나(학습중), 결과를 조정한다(후처리)"**

**편향 탐지 구체 사례** (중요): 앞서 다룬 \*\*"혼동행렬"\*\*을 **집단별로 나눠서** 계산 — 예를 들어 \*\*"남성 지원자 합격률 40% vs 여성 지원자 합격률 20% → DPR = 0.5"\*\*라면, 이는 앞서 다룬 \*\*"AI 윤리기준의 ③다양성 존중, 인공지능기본법의 채용 분야 고영향 AI"\*\*에서 요구하는 \*\*"차별 방지 의무"\*\*를 **정량적으로 위반**하는 명백한 증거입니다.

#### 도식화 제안

```
[Demographic Parity 측정·판정·완화 흐름]

①측정: DPD = P(Ŷ=1│A=1) − P(Ŷ=1│A=0)
        DPR = P(Ŷ=1│A=1) ÷ P(Ŷ=1│A=0)
     ↓
②판정: DPR ≥ 0.8 (EEOC 80% 규칙)
        예) 남성 합격률 40% / 여성 합격률 20% → DPR=0.5 → 차별 판정 🚨
     ↓
③완화: 전처리(데이터 균형) → 학습중(공정성 제약) → 후처리(임계값 조정)
     ↓
④검증: XAI(SHAP·LIME)로 어떤 특성이 편향을 일으켰는지 원인 설명
     ↓
⑤보고: 알고리즘 영향 평가(AIA) + 인공지능기본법 영향평가 의무 이행
```

**앞서 다룬 AI 윤리기준·인공지능기본법과의 연결**: 이런 **"DPR 측정, 집단별 혼동행렬 분리 계산, 전처리·후처리 완화"** 활동이 실제로는 앞서 다룬 \*\*"인공지능기본법의 고영향 AI 영향평가"\*\*에서 요구하는 \*\*"영향받는 자 식별, 관련 기본권 유형 식별"\*\*의 **기술적 실행 수단**이며, 앞서 다룬 **"EU AI Act Article 10의 학습 데이터 거버넌스"** 심사 항목에도 그대로 반영됩니다.

***

#### Ⅳ. 결론

Demographic Parity는 \*\*"보호 속성과 무관하게 집단별 긍정 예측 비율을 동등하게 하라는 공정성 원칙을, DPD·DPR이라는 수식과 EEOC 80% 규칙으로 정량화하고, 전처리·학습중·후처리 3단계로 완화하는 것"\*\*이며, 특히 \*\*"DPR = 불리 집단 선발률 ÷ 유리 집단 선발률 ≥ 0.8"\*\*이라는 판정 기준 하나가 앞서 다룬 **AI 윤리기준의 다양성 존중 원칙**과 **인공지능기본법의 차별 방지 의무**를 **실제로 측정하는 기술적 도구**입니다 — 이는 앞서 다룬 \*\*편향 탐지(측정 도구) → AI 윤리기준(원칙) → 인공지능기본법(법적 의무) → XAI(원인 설명) → 알고리즘 영향 평가(제도적 이행)\*\*를 하나로 잇는 실무적 교량이며, \*\*"공정한 AI는 결국, 집단 간 결과를 정량적으로 측정하고 관리하는 것에서 시작하며, 그 측정 수단이 바로 Demographic Parity다"\*\*라는 결론으로 귀결됩니다.

### **I. AI 공정성 확보를 위한 Demographic Parity의 개요**

인공지능 모델이 대출 심사나 채용 평가를 수행할 때 성별, 인종 등의 보호 속성(Protected Attribute)에 의해 특정 그룹이 차별받는 문제가 빈발하고 있습니다. \*\*Demographic Parity(인구통계학적 동등성)\*\*는 이러한 편향을 통제하기 위해, **보호 속성(A)의 값과 상관없이 최종적으로 긍정적인 예측(Y^=1*Y*^=1, 예: 대출 승인)을 받을 확률이 모든 그룹에서 동일해야 한다**고 규정하는 강력한 공정성 기준입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NjIuNCAyODYuNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSI1NjIuNCIgaGVpZ2h0PSIyODYuNzAwMDAwMDAwMDAwMDUiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUk9PVCIgZGF0YS10bz0iR3JvdXAwIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjI4My40MjMsNzYuOSAyODMuNDIzLDEwMC45IDE1NS44MjMsMTAwLjkgMTU1LjgyMywxMjQuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUk9PVCIgZGF0YS10bz0iR3JvdXAxIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjI4My40MjMsNzYuOSAyODMuNDIzLDEwMC45IDQxMS4wMjI5OTk5OTk5OTk5NywxMDAuOSA0MTEuMDIyOTk5OTk5OTk5OTcsMTI0LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209Ikdyb3VwMCIgZGF0YS10bz0iQ29tcGFyZSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxNTUuODIzLDE2MS44IDE1NS44MjMsMTg1LjggMjgzLjQyMywxODUuOCAyODMuNDIzLDIwOS44IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJHcm91cDEiIGRhdGEtdG89IkNvbXBhcmUiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDExLjAyMjk5OTk5OTk5OTk3LDE2MS44IDQxMS4wMjI5OTk5OTk5OTk5NywxODUuOCAyODMuNDIzLDE4NS44IDI4My40MjMsMjA5LjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJPT1QiIGRhdGEtbGFiZWw9IuqzteygleyEsSDtj4nqsIAgOiBEZW1vZ3JhcGhpYyBQYXJpdHkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTYyLjQxMyIgeT0iNDAiIHdpZHRoPSIyNDIuMDE5OTk5OTk5OTk5OTgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI4My40MjMiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7qs7XsoJXshLEg7Y+J6rCAIDogRGVtb2dyYXBoaWMgUGFyaXR5PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJHcm91cDAiIGRhdGEtbGFiZWw9IuuztO2YuCDqt7jro7kgQT0wIDog7ZWp6rKp66WgIFAwIOqzhOyCsCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MCIgeT0iMTI0LjkiIHdpZHRoPSIyMzEuNjQ2MDAwMDAwMDAwMDIiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNTUuODIzIiB5PSIxNDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuuztO2YuCDqt7jro7kgQT0wIDog7ZWp6rKp66WgIFAwIOqzhOyCsDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iR3JvdXAxIiBkYXRhLWxhYmVsPSLrs7TtmLgg6re466O5IEE9MSA6IO2VqeqyqeuloCBQMSDqs4TsgrAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjk5LjY0NTk5OTk5OTk5OTk2IiB5PSIxMjQuOSIgd2lkdGg9IjIyMi43NTQiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0MTEuMDIyOTk5OTk5OTk5OTciIHk9IjE0My4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+67O07Zi4IOq3uOujuSBBPTEgOiDtlanqsqnrpaAgUDEg6rOE7IKwPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDb21wYXJlIiBkYXRhLWxhYmVsPSLtj4nqsIAgOiDrkZAg7ZWp6rKp66Wg7J2YIOywqOydtCBQMCAtIFAxID0gMCDqsoDspp0iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTQ0Ljk5OTUiIHk9IjIwOS44IiB3aWR0aD0iMjc2Ljg0NyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIyODMuNDIzIiB5PSIyMjguMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPu2PieqwgCA6IOuRkCDtlanqsqnrpaDsnZgg7LCo7J20IFAwIC0gUDEgPSAwIOqygOymnTwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

***

### **II. Demographic Parity의 수리적 정의 및 한계점**

#### **1. 수학적 공식 정의**

P(Y^=1∣A=0)=P(Y^=1∣A=1)*P*(*Y*^=1∣*A*=0)=*P*(*Y*^=1∣*A*=1)

* A*A*: 보호 속성 (예: 0=여성, 1=남성)
* Y^*Y*^: 모델의 예측값 (0=거절, 1=승인)
* 즉, 성별과 무관하게 대출 승인을 받는 절대 비율이 완벽히 대칭을 이루어야 함을 의미합니다.

#### **2. 공학적/비즈니스적 한계점**

* **실제 정답(Ground Truth, Y*Y*)의 배제**: 실제 개인의 상환 능력이나 자격 요건(Y*Y*)을 전혀 고려하지 않고 비율만 맞춥니다. 이로 인해 우수한 자격을 갖춘 그룹의 합격자가 인위적으로 탈락하는 **역차별**이나 모델 전체의 **정확도(Accuracy) 저하**가 발생할 수 있습니다.

***

### **III. 정답 무관 공정성(Demographic Parity)과 정답 기반 공정성(Equal Opportunity)의 비교**

| **비교 항목**       | **⚖️ 인구통계학적 동등성 (Demographic Parity)**                     | **🎯 동등한 기회 (Equal Opportunity)**                                                  |
| :-------------- | :--------------------------------------------------------- | :--------------------------------------------------------------------------------- |
| **핵심 지향점**      | 보호 속성과 무관하게 동일한 결과 비율 보장                                   | **실제 자격(Y=1)이 있는 대상**에게 동등한 합격 기회 제공                                               |
| **수학적 공식**      | P(Y^=1∣A=0)=P(Y^=1∣A=1)*P*(*Y*^=1∣*A*=0)=*P*(*Y*^=1∣*A*=1) | **P(Y^=1∣A=0,Y=1)=P(Y^=1∣A=1,Y=1)*P*(*Y*^=1∣*A*=0,*Y*=1)=*P*(*Y*^=1∣*A*=1,*Y*=1)** |
| **정답(Y) 고려 여부** | **고려하지 않음** (결과 평등 지향)                                     | **적극 고려** (기회 평등 지향, 진양성률 TPR 동등화)                                                 |
| **사회적 정책 매핑**   | 소수자 우대 정책 (Affirmative Action) 지지                          | 실력 기반의 공정한 경쟁 환경 보장 지지                                                             |

***

### **IV. AI 모델의 Demographic Parity 달성을 위한 단계별 편향 완화 전략**

**IMPORTANT**

1. **전처리(Pre-processing) 단계 - Reweighing**: 학습 데이터셋 구축 시 편향을 예방하기 위해, 소외 그룹의 긍정 데이터에 가중치(Weight)를 부여하여 모델이 편향을 학습하지 않도록 데이터 분포를 조정해야 합니다.
2. **학습 중(In-processing) 단계 - Adversarial Debiasing**: 예측 모델을 학습할 때 보호 속성(A)을 예측하려는 대적(Adversarial) 신경망을 결합하여, 모델이 보호 속성 정보 자체를 추출하지 못하도록 페널티를 부여해야 합니다.
