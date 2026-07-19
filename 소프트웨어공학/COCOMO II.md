### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (COCOMOII정의,FP와의차이) — 3~4줄
Ⅱ. 3단계서브모델 (본론①, 도식 1개 필수)
Ⅲ. 노력계산공식및보정요소 (본론②, 핵심 배점)
Ⅳ. FP와의연결및선택기준
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬FP는'사용자가보는기능'을세는방식이라 개발언어와무관했는데,COCOMOII는'실제작성될코드의규모(KLOC)'를기반으로,거기에여러보정요소를곱해서 노력(공수,Man-Month)을계산하는 수학적회귀모델"\*\*이라는한줄로시작하면, FP답안과 대비되는출발점이 명확해집니다.

### Ⅱ. 3단계서브모델 — 프로젝트단계에따라다른모델사용

| 모델                          | 적용시점          | 특징                   |
| :-------------------------- | :------------ | :------------------- |
| **Application Composition** | 매우초기(요구사항불명확) | 재사용,프로토타이핑 위주소규모추정   |
| **Early Design**            | 요구사항일부확정후     | **적은수의보정요소**로대략적추정   |
| **Post-Architecture**       | 아키텍처확정후       | **가장정밀**,17개보정요소전부적용 |

→ 암기: **"모르면대충(Application Composition),좀알면중간(EarlyDesign),다알면정밀하게(Post-Architecture)"** — 앞서다룬 \*\*"FP의간이법(초기)↔정밀법(후기)"\*\*의구분과 정확히같은논리가, COCOMOII에서는 **3단계**로더세분화되어있습니다.

### 도식화 제안

```
[프로젝트진행단계]
초기 ────────────────────────→ 후기
   ↓                    ↓                    ↓
[Application         [Early Design]      [Post-Architecture]
 Composition]         (일부보정요소)        (17개보정요소전부)
(재사용/프로토타입)
   
   정밀도: 낮음 ────────────────→ 높음
```

### Ⅲ. 노력계산공식및보정요소 — 핵심 배점

**함정 방지: "LOC로계산한다"고만답하면절반. 실제공식과, "규모경제/불경제"를반영하는지수항을보여줘야완성됩니다.**

**기본공식(Post-Architecture)**

```
Effort(PM) = A × (Size)^B × ∏EM
```

| 요소                        | 의미                                                     |
| :------------------------ | :----------------------------------------------------- |
| **A**                     | 보정계수(회귀분석으로도출된상수)                                      |
| **Size**                  | **KLOC**(코드라인수,천단위) — FP값을 **언어별백테이블로LOC로환산**하기도함      |
| **B**(지수)                 | **규모증가에따른비선형성**반영 — 프로젝트가커질수록 **초선형(B>1)적으로노력이증가**할수있음 |
| **EM**(Effort Multiplier) | **17개보정요소**의곱— 요구되는신뢰성,팀숙련도,도구활용도등                     |

→ 암기: **"기본규모(LOC)에지수를먹이고, 17개보정요소를다곱한다"** — 여기서 **지수B**가 앞서다룬 **"폴락의법칙"**(면적늘려도성능은제곱근만큼만증가)과 **정확히반대방향의비유**를제공합니다: 폴락의법칙은 **"더투자해도이득이줄어드는(수익감소)"** 관계였는데, COCOMO의 B가1보다크면 **"프로젝트가커질수록 오히려노력이초선형으로더늘어나는(규모의불경제)"** 관계를보여줍니다 — 이는 앞서다룬 \*\*"버스중재,MSA"\*\*등에서 \*\*"많은구성요소가늘어날수록 조율비용이기하급수적으로증가"\*\*했던원리와 같은맥락입니다.

**17개보정요소예시**: 요구신뢰성,DB규모,제품복잡도,**팀원숙련도**,**도구사용성**,**일정단축압박**등 — 앞서다룬 \*\*"CMMI성숙도"\*\*가높은조직은, 이 보정요소중 **"프로세스성숙도"** 항목에서유리한값을받게됩니다.

### Ⅳ. FP와의연결 및 선택기준

| 구분        | **FP(기능점수)**                          | **COCOMOII**           |
| :-------- | :------------------------------------ | :--------------------- |
| **측정기준**  | 사용자관점 **기능**                          | 개발자관점 **코드규모(LOC)**    |
| **언어의존성** | **독립적**(같은기능이면언어달라도동일)                | **의존적**(언어마다코드량이다름)    |
| **적용시점**  | 기획\~설계                                | **설계\~구현**(코드규모추정가능시점) |
| **연계방법**  | FP값을 **언어별변환표**로 KLOC로환산해 COCOMO에입력가능 | <br />                 |

→ 앞서다룬 \*\*"SW사업대가산정가이드"\*\*에서 한국공공사업은 **FP기반이원칙**이지만, COCOMO는 **국제적으로더범용적인 학술/실무추정모델**로 함께활용되며, 두모델을 **교차검증용도**로같이쓰는경우도많습니다.

### Ⅴ. 결론 포인트 (설계·비용산정 시리즈 대단원)

COCOMOII는 \*\*"코드규모(LOC)라는물리적척도에서, 수학적회귀모델과다양한보정요소를통해 실제투입노력(인월)을예측하는것"\*\*이며, 이는앞서다룬 FP(기능관점,언어독립적)와 **상호보완적인 서로다른출발점**을가진 비용산정방법론입니다 — 두모델모두 \*\*"규모를측정하고,그규모에보정요소를곱해현실적비용/노력을도출한다"\*\*는 공통구조를가지며, 오늘하루다룬 McCabe(코드복잡도)→Fan-in/Fan-out(관계복잡도)→FP(기능규모)→COCOMOII(노력추정)로이어지는 시리즈전체가, **"소프트웨어를만들기전에,그크기와비용을최대한합리적으로예측하려는"** 소프트웨어공학의 실무적노력으로완결됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "1981년, 배리 보엠(Barry Boehm) 교수가 발표한 'COCOMO' 모델은 원시 코드 라인 수(LOC)를 기반으로 예산을 짜는 비용 산정의 바이블이었다. 하지만 세월이 흘러 자바(Java) 같은 객체지향이 대세가 되고, 남이 짠 코드를 조립하는 컴포넌트 기반(CBD) 시대가 오자, 무식하게 코드 줄 수만 세던 오리지널 COCOMO는 낡은 유물이 되어버렸다. 이에 배리 보엠은 현대 소프트웨어 공학의 트렌드(객체점수, 기능점수, 재사용 등)를 전부 때려 넣은 진화형 абсолют 무기를 발표했다. 그것이 바로 \*\*'COCOMO II'\*\*다. COCOMO II의 가장 위대한 철학은 프로젝트의 '시간 흐름(단계)'에 따라 산정 무기를 3번 바꾼다는 것이다. 첫째, 프로젝트 극초기 프로토타입 단계다. 코드가 한 줄도 없으므로 UI 화면 스크린 개수나 보고서 개수(객체 점수)로 돈을 세는 \*\*'애플리케이션 합성 모델'\*\*을 쓴다. 둘째, 대략적인 시스템 뼈대(기본 아키텍처)가 잡혔을 때다. 이때는 대략적인 기능의 개수(기능점수, FP)를 기반으로 예산을 잡는 \*\*'초기 설계 모델'\*\*을 쓴다. 셋째, 상세 설계가 모두 끝나고 진짜 코딩에 돌입하는 시점이다. 이때는 실제로 개발자들이 짤 '디테일한 코드 줄 수(SLOC)'와 개발팀의 팀워크, 성숙도 같은 17가지 세밀한 비용 요인들을 믹서기에 넣고 갈아 오차율 0%에 도전하는 \*\*'포스트 아키텍처 모델(설계 이후 모델)'\*\*을 쓴다. 이렇게 COCOMO II는 프로젝트의 탄생부터 완성까지 모든 순간에 대응한다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 구시대 LOC의 한계를 깨부순 비용 산정 바이블, COCOMO II 개요**

* **정의:** 배리 보엠이 기존 COCOMO 81 모델의 한계를 극복하기 위해 제안한 것으로, 폭포수 모델뿐만 아니라 **나선형, 객체지향, 컴포넌트 조립(CBD) 등 현대적 소프트웨어 개발 환경에 맞게 재설계된 '다단계(Multi-stage) 소프트웨어 비용/일정 산정 모델'**.
* **핵심 철학:** 소프트웨어 생명주기(진행 단계)에 따라 가용한 정보의 수준이 다르다는 점에 착안하여, **프로젝트 초기의 불확실성부터 후반부의 확실성까지 대응할 수 있는 '3개의 서브 모델'을 유연하게 교체하며 적용**함.

#### **II. \[본론 1] 프로젝트 시간 흐름에 따라 무기를 바꾸는 3단 아키텍처 (도식화)**

정보가 없을 때부터 정보가 쏟아질 때까지 산정 모델이 어떻게 진화하는지 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxOTIxLjA3OSA0MjMuNjQ2OTk5OTk5OTk5OTMiIHdpZHRoPSIxOTIxLjA3OSIgaGVpZ2h0PSI0MjMuNjQ2OTk5OTk5OTk5OTMiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9fX0NPQ09NT19JSV8zX19fIiBkYXRhLWxhYmVsPSLsi5zqsIQg7Z2Q66aE7JeQIOuUsOuluCBDT0NPTU8gSUkgM+uMgCDshJzruIwg66qo6424IO2MjOydtO2UhOudvOyduCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMTg0MS4wNzkiIGhlaWdodD0iMzQzLjY0Njk5OTk5OTk5OTkzIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMTg0MS4wNzkiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7si5zqsIQg7Z2Q66aE7JeQIOuUsOuluCBDT0NPTU8gSUkgM+uMgCDshJzruIwg66qo6424IO2MjOydtO2UhOudvOyduDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUDEiIGRhdGEtdG89Ik0xIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjI4NS40MjMsMjY3Ljk4MTk5OTk5OTk5OTk3IDMzMy40MjMsMjY3Ljk4MTk5OTk5OTk5OTk3IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJNMSIgZGF0YS10bz0iUDIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyVhO2CpO2FjeyymCDrvIjrjIAg64+E7LacIiBwb2ludHM9IjU2MC4xNywyNjcuOTgxOTk5OTk5OTk5OTcgNzY0LjQyNCwyNjcuOTgxOTk5OTk5OTk5OTciIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlAyIiBkYXRhLXRvPSJNMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI5OTMuMTA2LDI0MC41NjUgMTA0MS4xMDYsMjQwLjU2NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTTIiIGRhdGEtdG89IlAzIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsg4HshLgg7ISk6rOEIOyZhOujjCIgcG9pbnRzPSIxMjEzLjAxOSwyNDAuNTY1IDEzOTMuNTEzLDI0MC41NjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlAzIiBkYXRhLXRvPSJNMyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxNjAwLjcwNiwyNTQuMjczNDk5OTk5OTk5OTggMTY0OC43MDYsMjYyLjc5NDk5OTk5OTk5OTk2IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209Ik0xIiBkYXRhLXRvPSJQMiIgZGF0YS1sYWJlbD0i7JWE7YKk7YWN7LKYIOu8iOuMgCDrj4TstpwiPgogIDxyZWN0IHg9IjYwNC4xNzAwMDAwMDAwMDAxIiB5PSIyMzguMjczNDk5OTk5OTk5OTgiIHdpZHRoPSIxMTYuMjU0MDAwMDAwMDAwMDIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI2NjIuMjk3IiB5PSIyNTMuNDIzNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7JWE7YKk7YWN7LKYIOu8iOuMgCDrj4Tstpw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iTTIiIGRhdGEtdG89IlAzIiBkYXRhLWxhYmVsPSLsg4HshLgg7ISk6rOEIOyZhOujjCI+CiAgPHJlY3QgeD0iMTI1Ny4wMTkiIHk9IjIzOC4yNzM0OTk5OTk5OTk5OCIgd2lkdGg9IjkyLjQ5NDAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTMwMy4yNjYiIHk9IjI1My40MjM1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7sg4HshLgg7ISk6rOEIOyZhOujjDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUDEiIGRhdGEtbGFiZWw9Iu2UhOuhnOygne2KuCDqt7nstIjquLAg8J+QowrtlITroZzthqDtg4DsnoUsIO2ZlOuptCDquLDtmo3rp4wg7J6I7J2MIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIyMjcuMzczNDk5OTk5OTk5OTgiIHdpZHRoPSIyMjkuNDIzIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNzAuNzExNSIgeT0iMjU0LjI3MzQ5OTk5OTk5OTk4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNzAuNzExNSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPu2UhOuhnOygne2KuCDqt7nstIjquLAg8J+QozwvdHNwYW4+PHRzcGFuIHg9IjE3MC43MTE1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7tlITroZzthqDtg4DsnoUsIO2ZlOuptCDquLDtmo3rp4wg7J6I7J2MPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik0xIiBkYXRhLWxhYmVsPSIxLiDslaDtlIzrpqzsvIDsnbTshZgg7ZWp7ISxIOuqqOuNuApBcHBsaWNhdGlvbiBDb21wb3NpdGlvbiIgZGF0YS1zaGFwZT0iZGlhbW9uZCI+CiAgPHBvbHlnb24gcG9pbnRzPSI0NDYuNzk2NSwxNTQuNjA4NSA1NjAuMTcsMjY3Ljk4MTk5OTk5OTk5OTk3IDQ0Ni43OTY1LDM4MS4zNTU0OTk5OTk5OTk5NSAzMzMuNDIzLDI2Ny45ODE5OTk5OTk5OTk5NyIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0NDYuNzk2NSIgeT0iMjY3Ljk4MTk5OTk5OTk5OTk3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0NDYuNzk2NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPjEuIOyVoO2UjOumrOy8gOydtOyFmCDtlanshLEg66qo6424PC90c3Bhbj48dHNwYW4geD0iNDQ2Ljc5NjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPkFwcGxpY2F0aW9uIENvbXBvc2l0aW9uPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlAyIiBkYXRhLWxhYmVsPSLquLDrs7gg7ISk6rOEIOuLqOqzhCDwn5ug77iPCuyWtOuWpCDquLDriqXsnbQg65Ok7Ja06rCI7KeAIOuMgOuetSDslY4iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNzY0LjQyNCIgeT0iMjI3LjM3MzQ5OTk5OTk5OTk4IiB3aWR0aD0iMjI4LjY4MiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iODc4Ljc2NSIgeT0iMjU0LjI3MzQ5OTk5OTk5OTk4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI4NzguNzY1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+6riw67O4IOyEpOqzhCDri6jqs4Qg8J+boO+4jzwvdHNwYW4+PHRzcGFuIHg9Ijg3OC43NjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyWtOuWpCDquLDriqXsnbQg65Ok7Ja06rCI7KeAIOuMgOuetSDslY48L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTTIiIGRhdGEtbGFiZWw9IjIuIOy0iOq4sCDshKTqs4Qg66qo6424CkVhcmx5IERlc2lnbiIgZGF0YS1zaGFwZT0iZGlhbW9uZCI+CiAgPHBvbHlnb24gcG9pbnRzPSIxMTI3LjA2MjUsMTU0LjYwODUgMTIxMy4wMTksMjQwLjU2NSAxMTI3LjA2MjUsMzI2LjUyMTUgMTA0MS4xMDYsMjQwLjU2NSIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxMTI3LjA2MjUiIHk9IjI0MC41NjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjExMjcuMDYyNSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPjIuIOy0iOq4sCDshKTqs4Qg66qo6424PC90c3Bhbj48dHNwYW4geD0iMTEyNy4wNjI1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5FYXJseSBEZXNpZ248L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUDMiIGRhdGEtbGFiZWw9IuyLpOygnCDsvZTrlKkg64+M7J6FIOuLqOqzhCDwn5K7CkRCIOq1rOyhsCwg7L2U65OcIOudvOyduCDsiJgg7ZmV7KCVIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjEzOTMuNTEzIiB5PSIyMjcuMzczNDk5OTk5OTk5OTgiIHdpZHRoPSIyMDcuMTkyOTk5OTk5OTk5OTgiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE0OTcuMTA5NSIgeT0iMjU0LjI3MzQ5OTk5OTk5OTk4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNDk3LjEwOTUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7si6TsoJwg7L2U65SpIOuPjOyehSDri6jqs4Qg8J+SuzwvdHNwYW4+PHRzcGFuIHg9IjE0OTcuMTA5NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+REIg6rWs7KGwLCDsvZTrk5wg65287J24IOyImCDtmZXsoJU8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTTMiIGRhdGEtbGFiZWw9IjMuIO2PrOyKpO2KuCDslYTtgqTthY3sspgg66qo6424ClBvc3QtQXJjaGl0ZWN0dXJlIiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjE3NTYuODkyNSwxNTQuNjA4NDk5OTk5OTk5OTYgMTg2NS4wNzksMjYyLjc5NDk5OTk5OTk5OTk2IDE3NTYuODkyNSwzNzAuOTgxNSAxNjQ4LjcwNiwyNjIuNzk0OTk5OTk5OTk5OTYiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTc1Ni44OTI1IiB5PSIyNjIuNzk0OTk5OTk5OTk5OTYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE3NTYuODkyNSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPjMuIO2PrOyKpO2KuCDslYTtgqTthY3sspgg66qo6424PC90c3Bhbj48dHNwYW4geD0iMTc1Ni44OTI1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5Qb3N0LUFyY2hpdGVjdHVyZTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJOb3RlIiBkYXRhLWxhYmVsPSJOb3RlIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjY4LjYyNiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjkwLjMxMyIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5Ob3RlPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] COCOMO II의 3대 서브 모델 전격 해부 (3단 표 - 출제 1순위)**

각 모델이 어느 시점에, '어떤 단위(Metric)'를 기준으로 돈을 계산하는지 찌르는 것이 핵심입니다.

| **3대 서브 모델 명칭**                                  | **적용 시기 (개발 생명주기)**                                                         | **핵심 산정 척도(Metric) 및 특징**                                                                                                          |
| :----------------------------------------------- | :-------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| **1. 애플리케이션 합성 모델** *(App. Composition)*         | **프로젝트 극초기 단계.** 코딩은 시작도 안 했고, GUI 화면(프로토타입) 정도만 대략적으로 기획할 때 적용.            | **산정 단위: 객체 점수 (Object Points).** 아직 코드 줄 수를 모르므로 화면 스크린의 개수, 리포트(출력물)의 개수, 조립할 3GL 컴포넌트의 개수 등을 세어서 비용을 계산함.                       |
| **2. 초기 설계 모델** *(Early Design)*                 | **기본(개략) 설계 단계.** 기본적인 시스템 아키텍처 뼈대가 잡히고, 대안들을 놓고 저울질할 때 적용.                 | **산정 단위: 기능 점수 (Function Points).** 대략 도출된 '기능점수(FP)'를 기반으로 개발 규모(UFP)를 파악하며, 7개의 초기 비용 요인을 곱해 예산을 책정함.                            |
| **3. 포스트 아키텍처 모델 (설계 이후)** *(Post-Architecture)* | **상세 설계 완료 및 코딩 돌입 단계.** 실제 개발에 들어가기 직전, 프로젝트의 모든 세부 정보가 가장 투명하게 드러났을 때 적용. | **산정 단위: 논리적 원시 코드 라인 수 (SLOC).** 기능점수 등을 실제 코드 라인 수(SLOC)로 환산하고, 개발팀의 능력, 성숙도 등 **17개의 치밀한 비용 요인(Cost Drivers)을 반영하는 가장 정밀한 모델.** |

#### **IV. \[결론/제언] COCOMO II의 규모 요인(Scale Factors)과 FP와의 융합 트렌드**

* **(키워드 위주 2줄 마무리)** "현대의 공공/민간 발주 환경에서는 COCOMO II 단독으로 쓰이기보다는, **정부 표준인 '기능점수(FP)'로 뼈대 예산을 잡고, 여기에 COCOMO II의 5대 규모 요인(선례성, 유연성, 위험 해상도, 팀워크, 프로세스 성숙도)을 가중치로 융합**하여 개발사의 역량에 따른 초정밀 IT 예산을 산출하는 복합 비용 산정 모델의 형태로 진화하고 있습니다."
