### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (앞서다룬CT의복습, 오늘의새로운질문) — 3~4줄
Ⅱ. 중앙집중형vs연합학습형CT (본론①, 도식 1개 필수)
Ⅲ. 어노테이션파이프라인과의통합, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

앞서다룬 \*\*CT(ContinuousTraining)\*\*는 \*\*"데이터드리프트감지→재학습"\*\*이었는데, 이는 \*\*"모든데이터가한곳에모여있다"\*\*는 전제였습니다 — 그런데 방금다룬 \*\*"연합학습"\*\*환경에서는 데이터가 **애초에한곳에없으므로**, CT의동작방식자체가 달라집니다.

### Ⅱ. 중앙집중형vs연합학습형 CT

| 구분           | **중앙집중형CT**(앞서다룬그것)  | **연합학습형CT**                                       |
| :----------- | :------------------- | :------------------------------------------------ |
| **드리프트감지위치** | 중앙서버에서 **전체데이터**모니터링 | **각로컬기기**가 자기데이터의드리프트를 **개별감지**                   |
| **재학습트리거**   | 중앙서버가 **일괄적으로**재학습결정 | 각기기가 \*\*"내데이터가바뀌었다"\*\*신호를 **중앙에보고**,집계후재학습라운드시작 |
| **재학습대상**    | 전체모델을 **한번에**재학습     | 앞서다룬 \*\*"FedAvg"\*\*로 **각기기의로컬업데이트를다시집계**        |

→ 암기: **"중앙집중형은한곳에서모니터링·재학습을다하고,연합학습형은 각자가드리프트를감지해서보고하면 그때전체가다시학습라운드를돈다"**

### 도식화 제안

```
[중앙집중형 CT(앞서다룬것)]
[중앙DB] → 데이터드리프트감지 → 재학습 → 배포

[연합학습형 CT]
[기기A]드리프트감지→보고 ┐
[기기B]정상→보고없음    ├→ [중앙서버]"A에서변화감지됨"
[기기C]드리프트감지→보고 ┘         ↓
                          새로운연합학습라운드시작
                          (A,B,C 모두참여,파라미터재집계)
```

### Ⅲ. 어노테이션파이프라인과의통합 — 핵심 배점

**함정 방지: "재학습한다"고만답하면절반. 앞서다룬어노테이션이 CT사이클안에서 어떻게자동화되는지, 그리고Human-in-the-Loop이CT에서어떤역할을하는지보여줘야완성됩니다.**

| 단계                                    | 내용                                                |
| :------------------------------------ | :------------------------------------------------ |
| **①운영중오류탐지**                          | 배포된모델이 **낮은신뢰도로예측**한사례를 **자동수집**(Active Learning) |
| **②우선순위선정**                           | 앞서다룬 \*\*"불확실성이가장높은샘플"\*\*을 **우선적으로**사람에게전달       |
| **③Human-in-the-Loop 재어노테이션**(앞서다룬그것) | 사람이 **새로운정답라벨**을붙임                                |
| **④재학습→검증→배포**(앞서다룬A/B테스트)            | 새라벨로 재학습후 **A/B테스트**로 **실제개선여부검증**                |

→ 암기: **"모델이헷갈려하는사례를자동으로골라내서,사람에게우선적으로보여주고,새라벨을받아재학습하고,A/B테스트로검증한다"** — 이는 앞서다룬 \*\*"어노테이션(라벨링)"\*\*이 \*\*"한번하고끝나는것이아니라, CT사이클안에서 계속반복되는활동"\*\*이라는 것을 보여줍니다 — 특히 \*\*"Active Learning(모델이가장헷갈려하는데이터를 우선라벨링요청)"\*\*은, 앞서다룬 \*\*"MIT의80%시간이라벨링에소요"\*\*되는 문제를 \*\*"가장가치있는데이터만 선별적으로라벨링"\*\*해 효율화하는 핵심기법입니다.

### 도식화 제안

```
[CT와 어노테이션의 통합사이클]
[배포된모델] → 낮은신뢰도예측사례 자동수집(Active Learning)
     ↓
[사람에게우선전달] → Human-in-the-Loop 재라벨링(앞서다룬그것)
     ↓
[재학습] → [A/B테스트로검증](앞서다룬그것) → 개선확인시 전체배포
     ↓ (다시)
[배포된모델] ← 순환반복
```

### Ⅳ. 결론

MLOps의CT파이프라인은 \*\*"중앙집중형(앞서다룬드리프트감지→재학습)"\*\*과 \*\*"연합학습형(각기기가개별감지→집계후재학습라운드)"\*\*으로 나뉘며, 실무에서는 여기에 \*\*"Active Learning으로모델이헷갈려하는사례를우선선별→Human-in-the-Loop로재라벨링→A/B테스트로검증"\*\*하는 **어노테이션파이프라인**이 통합됩니다 — 이는 앞서다룬 \*\*연합학습(분산학습),데이터어노테이션(라벨링효율화),A/B테스트(검증)\*\*가 모두 CT라는 하나의순환고리안에서 **유기적으로연결**된다는 것을 보여주며, 오늘하루다룬 방대한AI운영시리즈전체가 \*\*"모델은한번만들고끝나는것이아니라, 데이터-라벨링-학습-검증-배포가끝없이순환하는살아있는시스템"\*\*이라는 결론으로 귀결됩니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "소프트웨어 개발(Dev)과 운영(Ops)을 합친 DevOps에 머신러닝 특유의 자산인 '데이터와 모델'을 얹어 자동화한 공장 라인이다. DevOps는 코드만 빌드해서 배포(CI/CD)하면 끝이지만, AI 모델은 시간이 흐르면 세상 트렌드가 바뀌어 성능이 썩어 문드러지는 '모델 열화(Model Drift)' 현상이 터진다. 이를 막기 위해 MLOps는 **'CT(Continuous Training: 지속적 학습)'** 파이프라인을 가동한다. 작동 방식은 명확하다. 센서(모니터링)가 실시간 유입 데이터의 성질 변화(**Data Drift**)나 모델 정확도 하락을 감지하는 순간, **자동으로 재학습 버튼(트리거)을 눌러** 새 데이터를 먹여 모델을 리프레시한다. 즉, 인간 개발자가 퇴근해도 데이터 수집-재학습(CT)-코드 검증(CI)-모델 서빙(CD)이 스스로 굴러가며 최상의 똑똑함을 유지하는 현대 AI 서비스의 표준 뼈대다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 모델 노화(Drift)에 대응하는 실시간 순환계, MLOps 개요**

* **정의:** 머신러닝 시스템 개발(Dev)과 머신러닝 시스템 운영(Ops)을 통합하여, 모델 학습-검증-배포-모니터링의 전 과정을 자동화하고 지속적 통합(CI), 지속적 배포(CD), \*\*지속적 학습(CT)\*\*을 실현하는 엔지니어링 체계.
* **목적:** 현실 세계 데이터의 통계적 분포가 바뀌는 현상(Data/Concept Drift)에 즉각 대응하여 배포된 AI 모델의 예측 정확도를 상시 최상으로 유지하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 데이터의 변화가 재학습(CT)을 깨우는 순환 흐름**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMTYuMjI5MDAwMDAwMDAwMDQgNTg0LjgiIHdpZHRoPSIzMTYuMjI5MDAwMDAwMDAwMDQiIGhlaWdodD0iNTg0LjgiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Ik1MT3BzX19DVF9fIiBkYXRhLWxhYmVsPSJNTE9wc+ydmCDtlbXsi6w6IENUKOyngOyGjeyggSDtlZnsirUpIOujqO2UhCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMjM2LjIyOSIgaGVpZ2h0PSI1MDQuNzk5OTk5OTk5OTk5OTUiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIyMzYuMjI5IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+TUxPcHPsnZgg7ZW17IusOiBDVCjsp4Dsho3soIEg7ZWZ7Iq1KSDro6jtlIQ8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlNSViIgZGF0YS10bz0iTU9OIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE5Mi4xNTI2NjY2NjY2NjY2OCwzNTkgMTkyLjE1MjY2NjY2NjY2NjY4LDM3MSAxOTUuNDM1NzUsMzcxIDE5NS40MzU3NSw0MDciIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209Ik1PTiIgZGF0YS10bz0iVFJJRyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxOTUuNDM1NzUsNDQzLjkgMTk1LjQzNTc1LDQ1NS45IDE3MC4wNDYxNjY2NjY2NjY3LDQ1NS45IDE3MC4wNDYxNjY2NjY2NjY3LDQ5MS45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJUUklHIiBkYXRhLXRvPSJTUlYiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSJObyIgcG9pbnRzPSIxNDYuMTgyODMzMzMzMzMzMzUsNDkxLjkgMTQ2LjE4MjgzMzMzMzMzMzM1LDQ1NS45IDEyMC43OTMyNSw0NTUuOSAxMjAuNzkzMjUsMzcxIDEyNC4wNzYzMzMzMzMzMzMzNCwzNzEgMTI0LjA3NjMzMzMzMzMzMzM0LDM1OSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJQSVBFTElORSIgZGF0YS10bz0iVkFMIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE1OC4xMTQ1MDAwMDAwMDAwMiwxMjAuOSAxNTguMTE0NTAwMDAwMDAwMDIsMTY4LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlZBTCIgZGF0YS10bz0iU1JWIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsi6DtmJUg66qo6424IOuwsO2PrCDwn5qAIiBwb2ludHM9IjE1OC4xMTQ1MDAwMDAwMDAwMiwyMDUuOCAxNTguMTE0NTAwMDAwMDAwMDIsMzIyLjEiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iVFJJRyIgZGF0YS10bz0iU1JWIiBkYXRhLWxhYmVsPSJObyI+CiAgPHJlY3QgeD0iMTA1LjI5MzI1IiB5PSI0MTAuMyIgd2lkdGg9IjMwLjcxODAwMDAwMDAwMDAwNCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjEyMC42NTIyNTAwMDAwMDAwMSIgeT0iNDI1LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5ObzwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJWQUwiIGRhdGEtdG89IlNSViIgZGF0YS1sYWJlbD0i7Iug7ZiVIOuqqOuNuCDrsLDtj6wg8J+agCI+CiAgPHJlY3QgeD0iMTA0LjYxNDUiIHk9IjI0OC44MDAwMDAwMDAwMDAwNCIgd2lkdGg9IjEwNi4xNTYwMDAwMDAwMDAwMyIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjE1Ny42OTI1MDAwMDAwMDAwMiIgeT0iMjYzLjk1MDAwMDAwMDAwMDA1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7si6DtmJUg66qo6424IOuwsO2PrCDwn5qAPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTUlYiIGRhdGEtbGFiZWw9IjEuIOyatOyYgSDshJzrsoTsl5DshJwgQUkg7J6R64+ZIOykkSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iMzIyLjEiIHdpZHRoPSIyMDQuMjI5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTU4LjExNDUwMDAwMDAwMDAyIiB5PSIzNDAuNTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjEuIOyatOyYgSDshJzrsoTsl5DshJwgQUkg7J6R64+ZIOykkTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTU9OIiBkYXRhLWxhYmVsPSJNT04iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTYwLjAxMTI1MDAwMDAwMDAyIiB5PSI0MDciIHdpZHRoPSI3MC44NDkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE5NS40MzU3NSIgeT0iNDI1LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5NT048L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlRSSUciIGRhdGEtbGFiZWw9IlRSSUciIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTIyLjMxOTUiIHk9IjQ5MS45IiB3aWR0aD0iNzEuNTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTU4LjExNDUwMDAwMDAwMDAyIiB5PSI1MTAuMzQ5OTk5OTk5OTk5OTciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlRSSUc8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlBJUEVMSU5FIiBkYXRhLWxhYmVsPSJQSVBFTElORSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMDcuNDk5NTAwMDAwMDAwMDEiIHk9Ijg0IiB3aWR0aD0iMTAxLjIyOTk5OTk5OTk5OTk5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjE1OC4xMTQ1MDAwMDAwMDAwMiIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5QSVBFTElORTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iVkFMIiBkYXRhLWxhYmVsPSI1LiDrqqjrjbgg6rKA7KadIOuwjyBDSS9DRCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3My43ODQiIHk9IjE2OC45IiB3aWR0aD0iMTY4LjY2MSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE1OC4xMTQ1MDAwMDAwMDAwMiIgeT0iMTg3LjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij41LiDrqqjrjbgg6rKA7KadIOuwjyBDSS9DRDwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 구글 MLOps 진화 레벨 및 CT 핵심 메커니즘 전격 해부 (3단 표)**

이 토픽은 구글이 정의한 \*\*'MLOps 3단계 레벨'\*\*의 구분을 확실히 기술하고, 모델 재학습이 일어나는 조건인 \*\*'트리거 요건(Drift)'\*\*을 정확히 써주는 것이 채점관의 점수를 긁어모으는 무기입니다.

| **핵심 척도**                | **⚙️ 구글 MLOps 진화 단계 (Level) 🚨**                                                                                                                                                                    | **🎯 CT 자동 재학습 트리거 💯**                                                                                                                                                                                                                | **💼 DevOps vs MLOps 차이 💯**                                                                                                                       |
| :----------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| **개념 / 차별성**             | **'자동화 성숙도 모델'.** 조직의 AI 개발 프로세스가 얼마나 수동 노가다를 탈피하고 자율 주행화되어 있는지 측정하는 기준.                                                                                                                            | **'자동 학습 실행 조건 (Trigger)'.** 인간 개입 없이 시스템이 판단하여 스스로 학습 파이프라인을 기동시키는 기준표.                                                                                                                                                               | **'코드 중심 vs 코드+데이터+모델'.** 단순 프로그램 패치 배포와 딥러닝 모델의 복잡한 재생성 프로세스의 근본적 차이.                                                                             |
| **핵심 세부 내용 (출제 포인트) 🚨** | **\[Level 0 (Manual)]** 데이터 추출, 학습, 배포가 모두 수작업. **\[Level 1 (Pipeline 자동화) 🚨]** 새 데이터 유입 시 모델을 자동으로 재학습하는 **'CT'** 구현 단계. **\[Level 2 (CI/CD 자동화) 💯]** 코드 수정 시 파이프라인 자체를 테스트/빌드하여 자동 무한 서빙하는 완성형. | **1. \[성능 저하 지표 🚨]** F1-Score, RMSE 등 모델 품질 점수가 한계치(Threshold) 미만으로 하락할 때. **2. \[데이터 드리프트 (Data Drift) 💯]** 입력 데이터의 평균, 분산 등 통계 성격이 급변할 때. **3. \[콘셉트 드리프트 (Concept Drift)]** 데이터는 같으나 타깃 변수의 비즈니스 정의가 바뀔 때. **4. 주기적/배치식** (매일 밤). | **\[DevOps]** 단일 프로그램 소스 코드(Code) 통합(CI) 및 운영 배포(CD) 관리. **\[MLOps 💯]** 코드뿐만 아니라 데이터 버전(DVC), 학습 파라미터 족보(MLflow), 성능 메트릭 모니터링을 포괄하는 다차원 파이프라인 관리. |

#### **IV. \[결론/제언] 피처 스토어(Feature Store)와 모델 레지스트리(Registry)의 도입**

* **(키워드 위주 2줄 마무리)** "CT 파이프라인이 매끄럽게 가동되기 위해서는 여러 개발자가 전처리한 데이터를 중복 없이 재사용하는 \*\*'피처 스토어(Feature Store)'\*\*와, 재학습을 통해 생성된 역대 버젼의 AI 모델 파일을 계통 관리하는 **'모델 레지스트리(Model Registry)' 컴포넌트의 유기적 연동이 견고한 MLOps 인프라 완성을 위해 전제되어야 합니다.**"
