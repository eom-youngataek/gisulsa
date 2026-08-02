### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (체크포인트필요성, REDO/UNDO와의관계) — 3~4줄
Ⅱ. 체크포인트동작원리 (본론①, 도식 1개 필수)
Ⅲ. 체크포인트유형및복구범위축소, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

앞서다룬 **REDO/UNDO**는 \*\*"장애시전체로그를분석"\*\*해야했는데, 시스템이 **오래운영될수록로그가무한히쌓여** 복구시간이 **몇시간씩걸릴수있습니다**. 체크포인트는 \*\*"이시점까지의모든변경은 이미디스크에안전하게반영됐다"\*\*는 **확실한기준점**을 주기적으로찍어, **그이전로그는복구시무시**할수있게합니다.

### Ⅱ. 체크포인트동작원리

| 단계                    | 내용                                                     |
| :-------------------- | :----------------------------------------------------- |
| **①활성트랜잭션중단**(또는계속허용) | 체크포인트생성순간의 **진행중인트랜잭션목록**파악                            |
| **②더티페이지플러시**(핵심)     | 메모리에서 \*\*아직디스크에안반영된변경(Dirty Page)\*\*을 **모두디스크에강제기록** |
| **③체크포인트레코드기록**       | \*\*"이시점까지는모두디스크와일치한다"\*\*는 표시를 로그에남김                  |

→ 암기: **"진행중인걸확인하고, 밀린변경사항을전부디스크에쏟아내고, 여기까지는안전하다고표시한다"** — 앞서다룬 \*\*"UPS의정기점검"\*\*처럼, 체크포인트도 \*\*"평소에는효율을위해미뤄둔작업을, 주기적으로한번에확실히처리"\*\*하는 원리입니다.

### 도식화 제안

```
[체크포인트 없이]
[T1시작]──[T2시작]──[T3시작]──...──[장애발생]
     ↑
복구시: T1부터 장애시점까지 모든로그를 분석해야함(매우느림)

[체크포인트 적용]
[T1시작]──[체크포인트]──[T2시작]──[T3시작]──[장애발생]
              ↑(여기까지는 디스크와100%일치보장)
복구시: 체크포인트이후 로그만분석하면됨(훨씬빠름)
```

### Ⅲ. 체크포인트유형 및 복구범위축소 — 핵심 배점

**함정 방지: "그냥기준점을찍는다"고만답하면절반. 활성트랜잭션이있을때어떻게처리하는지, 그리고왜"완전정지"방식은비현실적인지보여줘야완성됩니다.**

| 유형                   | 내용                                                  |
| :------------------- | :-------------------------------------------------- |
| **Sharp체크포인트**(정지형)  | 체크포인트동안 **모든트랜잭션을일시정지**— **단순하지만서비스중단발생**(실무에서비현실적) |
| **Fuzzy체크포인트**(무중단형) | 체크포인트 **진행중에도새트랜잭션계속허용**— 실제운영DB의 **표준방식**          |

**Fuzzy체크포인트의핵심트릭**: 체크포인트시작시점에 \*\*"현재활성화된트랜잭션목록"\*\*을 함께기록해둡니다 — 그러면 복구시:

```
[Fuzzy체크포인트 복구범위]
체크포인트기록: "이시점기준 활성트랜잭션은 T2,T3였음"
     ↓
복구시 REDO 시작점: 체크포인트 시점(디스크와대부분일치,차이만복구)
복구시 UNDO 대상: 체크포인트당시 활성이었던 T2,T3부터 (완료여부재확인)
```

→ 암기: **"체크포인트순간에 진행중이던트랜잭션목록만따로적어두면, 서비스를안멈춰도 나중에정확히어디서부터확인해야할지알수있다"** — 앞서다룬 \*\*"슬라이딩윈도우"\*\*가 **"확인된만큼씩만창을옮기는"** 것처럼, 체크포인트도 \*\*"확실한만큼만기준점을당기고, 그이후불확실한부분만정밀검토"\*\*합니다.

### 도식화 제안

```
[Fuzzy체크포인트 - 무중단]
     [T1]────[T2]──────[T3]────
서비스: ──────────────────────────→ (한번도안멈춤)
     ↑체크포인트시작
     "지금활성:T2,T3" 기록
              ↑체크포인트완료(더티페이지플러시완료)

복구시: T1은 체크포인트이전에끝났으니 무시가능
       T2,T3는 체크포인트당시활성 → REDO/UNDO 대상으로정밀확인
```

### Ⅳ. 결론

체크포인트는 \*\*"REDO/UNDO가매번전체로그를분석해야하는비효율을, 주기적으로 '여기까지는안전하다'는 기준점을찍어 해결하는것"\*\*입니다 — 실무에서는 **서비스중단없는Fuzzy체크포인트**가 표준이며, \*\*"체크포인트순간의활성트랜잭션목록"\*\*을 함께기록해 **복구범위를정확하게좁힙니다** — 이는 앞서다룬 \*\*"UNDO/REDO(장애복구의실행)"\*\*와 짝을이루어, **"장애복구를더빠르고효율적으로만드는"** 핵심최적화이며, 오늘하루다룬 데이터베이스트랜잭션시리즈(ACID→격리수준→병행제어→REDO/UNDO→체크포인트)를 **"안전성과효율성을동시에추구하는"** 완결된하나의그림으로 마무리합니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "DB가 뻗었을 때 REDO/UNDO 복구를 하려고 10년 치 로그 파일을 처음부터 다 뒤지면 복구에 몇 달이 걸릴 수도 있다. 이 무식한 짓을 막기 위해 주기적으로 꽂아두는 '안전 깃발'이 바로 체크포인트다. 핵심은 **'저장 완료 도장'**이다. DB는 평소에 주기적으로 메모리(버퍼)의 데이터를 디스크에 강제로 쏟아붓고(Flush), 로그 파일에 `<Checkpoint>` 도장을 쾅 찍는다. 서버가 폭발한 후 복구할 때, 이 깃발 이전에 완료(Commit)된 작업은 이미 디스크에 안전하게 들어간 게 확실하므로 검사조차 안 하고 쿨하게 무시(Ignore)한다. 오직 깃발 전후로 걸쳐 있거나 깃발 이후에 벌어진 일들만 REDO/UNDO를 수행하여 복구 시간(RTO)을 기적처럼 단축한다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] DB 회복 시간(RTO) 단축의 핵심, 체크포인트 기법 개요**

* **정의:** 로그 기반 회복 기법의 비효율성(로그 전체 검색)을 해결하기 위해, 주기적으로 메모리 버퍼의 변경 내용(Dirty Page)을 디스크에 강제로 기록하고 그 시점을 로그에 명시하는 기법.
* **목적:** 장애 발생 시 로그 검색 범위를 가장 최근의 체크포인트 시점으로 확 줄여, 시스템 복구 시간(RTO, Recovery Time Objective)을 최소화하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 깃발을 기준으로 뻗었을 때의 운명**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MTguNzUyIDU2OC4zNzYiIHdpZHRoPSI4MTguNzUyIiBoZWlnaHQ9IjU2OC4zNzYiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9fX18iIGRhdGEtbGFiZWw9IuyytO2BrO2PrOyduO2KuCjquYPrsJwpIOq4sOykgCDtirjrnpzsnq3shZgg67O16rWsIOyatOuqhSI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNzM4Ljc1MiIgaGVpZ2h0PSI0ODguMzc2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNzM4Ljc1MiIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPuyytO2BrO2PrOyduO2KuCjquYPrsJwpIOq4sOykgCDtirjrnpzsnq3shZgg67O16rWsIOyatOuqhTwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVDEiIGRhdGEtdG89IkNISyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyNDIuNDQ0OTk5OTk5OTk5OTYsNDg0Ljk1OTMzMzMzMzMzMzM1IDI2Ni40NDQ5OTk5OTk5OTk5NCw0ODQuOTU5MzMzMzMzMzMzMzUgMjY2LjQ0NDk5OTk5OTk5OTk0LDI2MS4xNjMgMjkwLjQ0NDk5OTk5OTk5OTk0LDI2MS4xNjMiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlQyIiBkYXRhLXRvPSJDSEsiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjQyLjQ0NDk5OTk5OTk5OTk2LDExOS44NjY2NjY2NjY2NjY2MyAyNjYuNDQ0OTk5OTk5OTk5OTQsMTE5Ljg2NjY2NjY2NjY2NjYzIDI2Ni40NDQ5OTk5OTk5OTk5NCwyNjEuMTYzIDI5MC40NDQ5OTk5OTk5OTk5NCwyNjEuMTYzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJUMyIgZGF0YS10bz0iQ0hLIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjI0Mi40NDQ5OTk5OTk5OTk5NiwzNDAuODY5NDk5OTk5OTk5OTYgMjY2LjQ0NDk5OTk5OTk5OTk0LDM0MC44Njk0OTk5OTk5OTk5NiAyNjYuNDQ0OTk5OTk5OTk5OTQsMjYxLjE2MyAyOTAuNDQ0OTk5OTk5OTk5OTQsMjYxLjE2MyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQ0hLIiBkYXRhLXRvPSJGQUlMIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjUzMS4yNzEsMjYxLjE2MyA1NzkuMjcxLDI2MS4xNjMiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlQxIiBkYXRhLXRvPSJJRyIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuydtOuvuCDrlJTsiqTtgazsl5Ag7J6I7J2MIiBwb2ludHM9IjI0Mi40NDQ5OTk5OTk5OTk5Niw0OTMuOTI2MDAwMDAwMDAwMDQgNTc5LjI3MSw0OTMuOTI2IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlQyIiBkYXRhLXRvPSJSRSIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuuUlOyKpO2BrOyXkCDslYgg7JOw7JiA7J2EIOyImCDsnojsnYwiIHBvaW50cz0iMjQyLjQ0NDk5OTk5OTk5OTk2LDExMC44OTk5OTk5OTk5OTk5NiAyNTQuNDQ0OTk5OTk5OTk5OTYsMTEwLjg5OTk5OTk5OTk5OTk2IDI1NC40NDQ5OTk5OTk5OTk5NiwxMDIuNDQ5OTk5OTk5OTk5OTkgNTc5LjI3MSwxMDIuNDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVDMiIGRhdGEtdG89IlVOIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7JmE66OMIOuquyDtlZjqs6Ag67uX7J2MIiBwb2ludHM9IjI0Mi40NDQ5OTk5OTk5OTk5NiwzNDkuODM2MTY2NjY2NjY2NjYgMjc4LjQ0NDk5OTk5OTk5OTk0LDM0OS44MzYxNjY2NjY2NjY2IDI3OC40NDQ5OTk5OTk5OTk5NCw0MjAuNTc2IDU3OS4yNzEsNDIwLjU3NTk5OTk5OTk5OTk2IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iVDEiIGRhdGEtdG89IklHIiBkYXRhLWxhYmVsPSLsnbTrr7gg65SU7Iqk7YGs7JeQIOyeiOydjCI+CiAgPHJlY3QgeD0iMzUyLjczMDk5OTk5OTk5OTk0IiB5PSI0NzcuOTI2MDAwMDAwMDAwMDQiIHdpZHRoPSIxMTYuMjU0MDAwMDAwMDAwMDIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI0MTAuODU3OTk5OTk5OTk5OTUiIHk9IjQ5My4wNzYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuydtOuvuCDrlJTsiqTtgazsl5Ag7J6I7J2MPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlQyIiBkYXRhLXRvPSJSRSIgZGF0YS1sYWJlbD0i65SU7Iqk7YGs7JeQIOyViCDsk7DsmIDsnYQg7IiYIOyeiOydjCI+CiAgPHJlY3QgeD0iMzMzLjEyODk5OTk5OTk5OTkiIHk9Ijg2LjQ0OTk5OTk5OTk5OTk5IiB3aWR0aD0iMTU1LjQ1ODAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNDEwLjg1Nzk5OTk5OTk5OTk1IiB5PSIxMDEuNiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+65SU7Iqk7YGs7JeQIOyViCDsk7DsmIDsnYQg7IiYIOyeiOydjDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJUMyIgZGF0YS10bz0iVU4iIGRhdGEtbGFiZWw9IuyZhOujjCDrqrsg7ZWY6rOgIOu7l+ydjCI+CiAgPHJlY3QgeD0iMzU3Ljc4IiB5PSI0MDQuNTc2IiB3aWR0aD0iMTA2LjE1NjAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNDEwLjg1OCIgeT0iNDE5LjcyNiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7JmE66OMIOuquyDtlZjqs6Ag67uX7J2MPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJUMSIgZGF0YS1sYWJlbD0iVDE6IOq5g+uwnCDsoITsl5AKQ29tbWl0IOuBneuCqCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMjEuOTQ4OTk5OTk5OTk5OTgiIHk9IjQ1OC4wNTkzMzMzMzMzMzMzNyIgd2lkdGg9IjEyMC40OTU5OTk5OTk5OTk5OCIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE4Mi4xOTY5OTk5OTk5OTk5NyIgeT0iNDg0Ljk1OTMzMzMzMzMzMzM1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxODIuMTk2OTk5OTk5OTk5OTciIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5UMTog6rmD67CcIOyghOyXkDwvdHNwYW4+PHRzcGFuIHg9IjE4Mi4xOTY5OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+Q29tbWl0IOuBneuCqDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJUMiIgZGF0YS1sYWJlbD0iVDI6IOq5g+uwnCDsoITsl5Ag7Iuc7J6R7ZW07IScCuyepeyVoCDsoITsl5AgQ29tbWl0IOuQqCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iOTIuOTY2NjY2NjY2NjY2NjMiIHdpZHRoPSIxODYuNDQ0OTk5OTk5OTk5OTYiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNDkuMjIyNDk5OTk5OTk5OTciIHk9IjExOS44NjY2NjY2NjY2NjY2MyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTQ5LjIyMjQ5OTk5OTk5OTk3IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+VDI6IOq5g+uwnCDsoITsl5Ag7Iuc7J6R7ZW07IScPC90c3Bhbj48dHNwYW4geD0iMTQ5LjIyMjQ5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7snqXslaAg7KCE7JeQIENvbW1pdCDrkKg8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iVDMiIGRhdGEtbGFiZWw9IlQzOiDquYPrsJwg7KCE7JeQIOyLnOyeke2VtOyEnArsnqXslaAg64KgIOuVjOq5jOyngCDsnpHsl4Ug7KSRIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIzMTMuOTY5NSIgd2lkdGg9IjE4Ni40NDQ5OTk5OTk5OTk5NiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE0OS4yMjI0OTk5OTk5OTk5NyIgeT0iMzQwLjg2OTQ5OTk5OTk5OTk2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNDkuMjIyNDk5OTk5OTk5OTciIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5UMzog6rmD67CcIOyghOyXkCDsi5zsnpHtlbTshJw8L3RzcGFuPjx0c3BhbiB4PSIxNDkuMjIyNDk5OTk5OTk5OTciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyepeyVoCDrgqAg65WM6rmM7KeAIOyekeyXhSDspJE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ0hLIiBkYXRhLWxhYmVsPSLinKgg7LK07YGs7Y+s7J247Yq4IOq5g+uwnCDqvYLtnpghIOKcqArrqZTrqqjrpqwgLSZndDsg65SU7Iqk7YGsIOqwleygnCDsoIDsnqUiIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iNDEwLjg1Nzk5OTk5OTk5OTk1LDE0MC43NSA1MzEuMjcxLDI2MS4xNjMgNDEwLjg1Nzk5OTk5OTk5OTk1LDM4MS41NzYgMjkwLjQ0NDk5OTk5OTk5OTk0LDI2MS4xNjMiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNDEwLjg1Nzk5OTk5OTk5OTk1IiB5PSIyNjEuMTYzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0MTAuODU3OTk5OTk5OTk5OTUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7inKgg7LK07YGs7Y+s7J247Yq4IOq5g+uwnCDqvYLtnpghIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjQxMC44NTc5OTk5OTk5OTk5NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+66mU66qo66asIC0mZ3Q7IOuUlOyKpO2BrCDqsJXsoJwg7KCA7J6lPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkZBSUwiIGRhdGEtbGFiZWw9IvCflKUg7Iuc7Iqk7YWcIOu7l+ydjCEg8J+UpSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NzkuMjcxIiB5PSIyNDIuNzEzIiB3aWR0aD0iMTU1LjMyMyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI2NTYuOTMyNSIgeT0iMjYxLjE2MyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+8J+UpSDsi5zsiqTthZwg67uX7J2MISDwn5SlPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJJRyIgZGF0YS1sYWJlbD0i7JWE66y06rKD64+EIOyViCDtlaggKElnbm9yZSkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTc5LjI3MSIgeT0iNDc1LjQ3NiIgd2lkdGg9IjE4My40ODEwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNjcxLjAxMTUiIHk9IjQ5My45MjYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyVhOustOqyg+uPhCDslYgg7ZWoIChJZ25vcmUpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJSRSIgZGF0YS1sYWJlbD0iUkVETyAo64uk7Iuc7ZWY6riwKSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NzkuMjcxIiB5PSI4NCIgd2lkdGg9IjE0Ni40MzA5OTk5OTk5OTk5OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNjUyLjQ4NjUiIHk9IjEwMi40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+UkVETyAo64uk7Iuc7ZWY6riwKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iVU4iIGRhdGEtbGFiZWw9IlVORE8gKOy3qOyGjO2VmOq4sCkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTc5LjI3MSIgeT0iNDAyLjEyNiIgd2lkdGg9IjE0Ni40MzA5OTk5OTk5OTk5OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNjUyLjQ4NjUiIHk9IjQyMC41NzU5OTk5OTk5OTk5NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+VU5ETyAo7Leo7IaM7ZWY6riwKTwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 체크포인트 시점 기준 트랜잭션 상태별 복구(Action) 전격 대조 (3단 표)**

| **핵심 척도**    | **쿨하게 무시 (Ignore)**                                                           | **다시 하기 (REDO) 🚨**                                                                  | **전부 취소 (UNDO) 🚨**                                                                         |
| :----------- | :---------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| **적용 대상**    | 깃발(Checkpoint)이 꽂히기 **전에 이미 작업이 완료(Commit)된** 트랜잭션.                           | 깃발 전에 시작했든 후에 시작했든, **시스템 뻗기 전에 어떻게든 작업이 완료(Commit)된** 트랜잭션.                         | 시스템이 뻗는 순간까지 **완료(Commit) 도장을 찍지 못하고 작업 중이던** 트랜잭션.                                         |
| **복구 로직 💯** | **'아무것도 안 함'.** 깃발 꽂을 때 이미 하드디스크에 안전하게 쾅쾅 박혀서 저장되었으므로, 복구 과정에서 아예 쳐다볼 필요도 없음. | **'새로운 값(After) 덮어쓰기'.** 완료는 쳤는데 디스크에 안 들어갔을 확률이 매우 높으므로, 로그에 남은 새 값을 디스크에 다시 쾅쾅 찍음. | **'과거 값(Before) 덮어쓰기'.** 끝까지 가지 못했으므로 원자성(All or Nothing) 원칙에 따라 로그의 과거 값을 꺼내 전부 없던 일로 되돌림. |
| **시간 단축 기여** | **이 Ignore 조치 덕분에 로그 파일을 처음부터 뒤질 필요가 없어져 복구 시간이 혁신적으로 단축됨.**                  | 디스크 저장 누락분만 복구함.                                                                     | 쓰레기 데이터를 신속하게 청소함.                                                                          |

#### **IV. \[결론/제언] 퍼지 체크포인트(Fuzzy Checkpoint)를 통한 성능 저하 방지**

* **(키워드 위주 2줄 마무리)** "전통적인 체크포인트는 디스크에 강제 저장하는 동안 모든 DB 작업을 일시 정지(Stop-the-world)시켜 심각한 병목을 유발합니다. 현대 대용량 DBMS는 시스템을 멈추지 않고 백그라운드에서 조금씩 데이터를 내려쓰는 **'퍼지 체크포인트(Fuzzy Checkpoint)' 기법을 도입하여, 무중단 서비스와 빠른 복구 성능을 동시에 달성하고 있습니다.**"
