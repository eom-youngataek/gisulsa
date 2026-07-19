### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (접근통제정의,4모델의진화순서) — 3~4줄
Ⅱ. DAC/MAC - 초기2대모델 (본론①, 도식 1개 필수)
Ⅲ. RBAC - 역할기반의혁신 (본론②, 핵심 배점)
Ⅳ. ABAC - 속성기반의최종진화
Ⅴ. 결론
```

포인트: 개요에서 \*\*"접근통제(누가무엇에접근할수있는가)의핵심질문은'그결정을누가내리는가' — 소유자개인이정하는지(DAC),중앙정책이강제하는지(MAC),역할로묶어정하는지(RBAC),다양한속성을조합해동적으로정하는지(ABAC) 이4단계로진화해왔다"\*\*는한줄로시작하면, 순서자체가 논리를담고있다는게드러납니다.

### Ⅱ. DAC/MAC — 초기2대모델

| 모델              | 결정주체                         | 특징                                            |
| :-------------- | :--------------------------- | :-------------------------------------------- |
| **DAC**(임의접근통제) | **자원의소유자**가직접결정              | 유연하지만, 소유자실수로 **과도한권한부여위험**                   |
| **MAC**(강제접근통제) | \*\*시스템(중앙정책)\*\*이강제,소유자도못바꿈 | **보안등급**(기밀,비밀등)에따라 **엄격히강제** — 국방·정부시스템에주로사용 |

→ 암기: **"DAC는집주인마음대로,MAC은국가가정한법대로"** — 앞서다룬 \*\*"소프트웨어사업영향평가"\*\*에서 **국가안보관련사업은공시제외**될수있었던것처럼, MAC도 **국방·기밀시스템**에서 **개인의재량을허용하지않는 강제성**이핵심입니다.

### 도식화 제안

```
[DAC]                              [MAC]
[파일소유자] ──직접결정──→ 접근권한       [보안레이블: 비밀]
"내파일이니 내가허락한사람만"              ↓
                                  [시스템정책이강제]
                                  "소유자도못바꿈,
                                   보안등급이맞아야만접근"
```

### Ⅲ. RBAC — 역할기반의혁신, 핵심 배점

**함정 방지: "역할별로권한을준다"고만답하면절반. 왜이게DAC/MAC의문제를해결했는지구체적으로보여줘야완성됩니다.**

| 항목        | 내용                                                             |
| :-------- | :------------------------------------------------------------- |
| **핵심원리**  | 사용자에게 **직접권한을주지않고**, \*\*역할(Role)\*\*에권한을부여 → 사용자는 **역할을할당**받음 |
| **해결한문제** | DAC의 **관리부담**(수천명개별권한설정)과 MAC의 **경직성**(등급외의세밀한통제불가) 동시완화       |
| **핵심요소**  | **사용자-역할할당(UA)**,**역할-권한할당(PA)**,**역할계층**(상위역할이하위역할권한포함)       |

→ 암기: **"사람마다권한주지말고, '팀장','사원'같은역할에권한을주고, 사람은역할만맡는다"** — 앞서다룬 \*\*"결합도/응집도"\*\*의 논리처럼, RBAC는 \*\*"사용자와권한사이에역할이라는중간계층을둬서 결합도를낮춘것"\*\*입니다 — 사람이바뀌어도 **역할-권한관계는안바뀌니 관리가훨씬쉬워집니다**.

### 도식화 제안

```
[DAC/MAC의문제]                    [RBAC의해법]
사용자1000명 ── 각자권한 1000개설정      [사용자1000명] ──할당──→ [역할10개]
(관리부담폭증,실수위험)                                        ↓
                                                        [역할10개] ──매핑──→ [권한]
                                                        (역할만관리하면 
                                                         사용자변경에안전)
```

### Ⅳ. ABAC — 속성기반의최종진화

**함정 방지: "RBAC보다더세밀하다"고만답하면절반. RBAC로는못푸는 "동적,상황적"통제문제를 ABAC가어떻게푸는지보여줘야완성됩니다.**

| 항목          | 내용                                                                 |
| :---------- | :----------------------------------------------------------------- |
| **핵심원리**    | **사용자속성+자원속성+환경속성**을 **조합**해 **실시간으로**접근여부결정                       |
| **RBAC의한계** | "같은역할(예:의사)"이라도 **상황에따라접근을달리해야하는경우**(예:본인이담당한환자데이터만,근무시간중에만) 처리어려움 |
| **ABAC의해법** | **"역할=의사" AND "환자=본인담당" AND "시간=근무시간"** 같은 **정책규칙**으로 세밀하게판단       |

→ 암기: **"역할하나로는부족할때, 여러조건(누구,무엇,언제,어디서)을동시에따진다"** — 앞서다룬 \*\*"제로트러스트"\*\*적사고(매요청마다다시검증)와 맞닿아있으며, **클라우드·마이크로서비스환경**처럼 **접근상황이매우동적인시스템**에 적합합니다.

### 도식화 제안

```
[ABAC 판단]
사용자속성(역할=의사,부서=내과)
   +
자원속성(데이터=환자기록,담당의=김의사)
   +
환경속성(시간=09:00~18:00,위치=병원내부IP)
   ↓
[정책엔진이 실시간판단] → 허용/거부
```

### Ⅴ. 결론 포인트 (보안 시리즈 최종연결)

DAC→MAC→RBAC→ABAC의진화는 \*\*"통제를누가내릴지(개인→시스템)"\*\*에서 \*\*"통제를어떻게효율적으로관리할지(직접→역할)"\*\*로, 다시 \*\*"통제를얼마나동적이고세밀하게할지(고정역할→실시간속성)"\*\*로 발전해온과정입니다 — 이는앞서다룬 \*\*"ISMS-P의2026년개편"\*\*에서 강조된 \*\*"클라우드보안(공유책임모델),AI거버넌스(동적데이터흐름관리)"\*\*같은 최신요구사항이, 결국 **ABAC같은더동적이고세밀한접근통제모델**을 요구한다는 것과 직결됩니다 — 오늘하루다룬 방대한암호학·보안관리체계시리즈전체가, \*\*"기술로데이터를지키는것에서, 그기술을조직적으로,그리고점점더정교하게관리하는것"\*\*으로 완결되는 하나의완전한이야기로마무리됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "당신이 군대에 입대했다고 치자. 장군님 책상 위에 있는 '1급 기밀' 문서는 당신이 '1급 비밀 취급 인가'가 없으면 죽었다 깨어나도 못 본다. 심지어 그 문서를 만든 장군님이 '이등병, 너 이거 봐'라고 허락해도 시스템(관리자)이 강제로 막아버린다. 이것이 극강의 보안, \*\*'MAC(강제 접근 통제)'\*\*다. 반대로 당신이 집에서 쓰는 윈도우 컴퓨터를 보자. 당신(소유자)이 만든 일기장 파일은 당신 마음대로 동생에게 읽기(Read), 쓰기(Write) 권한을 나눠줄 수 있다. 소유자가 권한을 임의로 뿌리는 이 자유로운 방식이 바로 운영체제의 표준인 \*\*'DAC(임의 접근 통제)'\*\*다. 매우 유연하지만, 동생이 해킹당하면 일기장이 털린다는 치명적 약점이 있다. 당신이 1,000명의 직원을 둔 회사를 차렸다고 해보자. 직원 한 명 한 명에게 DAC처럼 권한을 일일이 매달아 주려면 관리자는 미쳐버릴 것이다. 그래서 등장한 것이 \*\*'RBAC(역할 기반 접근 통제)'\*\*다. 권한을 사람에게 직접 주지 않고 '과장', '대리'라는 직급(Role) 묶음에 준다. 신입사원이 오면 '사원' 역할표만 목에 걸어주면 모든 세팅이 끝난다. 대다수 기업 전산망의 표준이다. 하지만 재택근무와 클라우드 시대가 열렸다. 권한을 가진 '과장'이긴 한데, 새벽 2시에 해외 수상한 IP로 접속하면 해킹당한 것이 분명하니까 막아야 하지 않을까? 그래서 등장한 4세대 최신 모델이 \*\*'ABAC(속성 기반 접근 통제)'\*\*다. 사람의 직급(역할)뿐만 아니라 접속 시간, 위치, 디바이스 기종 등 모든 '속성(조건)'을 종합적으로 믹서기에 갈아서 실시간으로 접근을 허락한다. 이것이 현대 '제로 트러스트(Zero Trust)' 보안의 심장이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 누가 감히 자산에 접근하는가? 4대 접근 통제 모델 개요**

* **접근 통제 (Access Control):** 인가된 주체(사용자)만이 객체(파일, DB, 네트워크)에 접근할 수 있도록 권한을 통제하여 시스템의 기밀성과 무결성을 지키는 보안 메커니즘.
* **모델의 진화:** 중앙 통제가 빡센 국방 환경(MAC) ➔ 개인의 유연성이 중시되는 PC 환경(DAC) ➔ 인사이동 관리가 편한 기업 환경(RBAC) ➔ 복잡하고 동적인 클라우드 환경(ABAC)으로 시대에 맞게 진화해 옴.

#### **II. \[본론 1] 군대식 룰에서 클라우드식 동적 통제로 진화하는 파이프라인 (도식화)**

각 모델이 중간에 어떤 '매개체'를 거쳐서 문을 열어주는지 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3NTAuMjg2IDEwODkuNDkyIiB3aWR0aD0iNzUwLjI4NiIgaGVpZ2h0PSIxMDg5LjQ5MiIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX180X19fX18iIGRhdGEtbGFiZWw9Iuygkeq3vCDthrXsoJwgNOuMgCDrqqjrjbjsnZgg7KeE7ZmU7JmAIOusuCDsl7Trprwo7ZeI7JqpKSDrqZTsu6Tri4jsppgiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjY3MC4yODYiIGhlaWdodD0iMTAwOS40OTIiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI2NzAuMjg2IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+7KCR6re8IO2GteygnCA064yAIOuqqOuNuOydmCDsp4TtmZTsmYAg66y4IOyXtOumvCjtl4jsmqkpIOuplOy7pOuLiOymmDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVSIgZGF0YS10bz0iTTEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjcwLjMwODk5OTk5OTk5OTk3LDU1NC40NDE3NSAyOTQuMzA4OTk5OTk5OTk5OTcsNTU0LjQ0MTc1IDI5NC4zMDg5OTk5OTk5OTk5Nyw0MzUuODE4NTAwMDAwMDAwMDMgMzI0LjYwNzQ5OTk5OTk5OTk2LDQzNS44MTg1MDAwMDAwMDAwMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTTEiIGRhdGEtdG89IkQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNTM2LjUzNDUsNDM1LjgxODUwMDAwMDAwMDAzIDU1NC44MzMsNDM1LjgxODUwMDAwMDAwMDAzIDU1NC44MzMsNTQ3LjY4MTc1IDU5MC44MzMsNTQ3LjY4MTc1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJVIiBkYXRhLXRvPSJNMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyNzAuMzA4OTk5OTk5OTk5OTcsNTY1LjIwMTc1IDI5NC4zMDg5OTk5OTk5OTk5Nyw1NjUuMjAxNzUgMjk0LjMwODk5OTk5OTk5OTk3LDY3NS4zNzUgMzI0Ljk3ODAwMDAwMDAwMDEsNjc1LjM3NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTTIiIGRhdGEtdG89IkQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNTM2LjE2Mzk5OTk5OTk5OTksNjc1LjM3NSA1NTQuODMzLDY3NS4zNzUgNTU0LjgzMyw1NTUuMDYxNzUwMDAwMDAwMSA1OTAuODMzLDU1NS4wNjE3NTAwMDAwMDAxIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJVIiBkYXRhLXRvPSJNMyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyNzAuMzA4OTk5OTk5OTk5OTcsNTc1Ljk2MTc0OTk5OTk5OTkgMjgyLjMwODk5OTk5OTk5OTk3LDU3NS45NjE3NDk5OTk5OTk5IDI4Mi4zMDg5OTk5OTk5OTk5Nyw5MjEuMjMgMzE4LjMwODk5OTk5OTk5OTk3LDkyMS4yMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTTMiIGRhdGEtdG89IkQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNTQyLjgzMyw5MjEuMjMgNTY2LjgzMyw5MjEuMjMgNTY2LjgzMyw1NjIuNDQxNzUgNTkwLjgzMyw1NjIuNDQxNzUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlUiIGRhdGEtdG89Ik00IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjI3MC4zMDg5OTk5OTk5OTk5Nyw1NDMuNjgxNzUgMjgyLjMwODk5OTk5OTk5OTk3LDU0My42ODE3NSAyODIuMzA4OTk5OTk5OTk5OTcsMTkyLjkyNzUgMzIxLjY0MzUsMTkyLjkyNzUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209Ik00IiBkYXRhLXRvPSJEIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjUzOS40OTg1LDE5Mi45Mjc1IDU2Ni44MzMsMTkyLjkyNzUgNTY2LjgzMyw1NDAuMzAxNzUwMDAwMDAwMSA1OTAuODMzLDU0MC4zMDE3NTAwMDAwMDAxIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJVIiBkYXRhLWxhYmVsPSLsgqzsmqnsnpAg8J+nkeKAjfCfkrsK7KO87LK0IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjE0NC42MjYiIHk9IjUzMi45MjE3NSIgd2lkdGg9IjEyNS42ODI5OTk5OTk5OTk5OSIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjIwNy40Njc1IiB5PSI1NTkuODIxNzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjIwNy40Njc1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7IKs7Jqp7J6QIPCfp5HigI3wn5K7PC90c3Bhbj48dHNwYW4geD0iMjA3LjQ2NzUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyjvOyytDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJNMSIgZGF0YS1sYWJlbD0iTUFDIPCfjpbvuI8K64KY7J2YICfruYTrsIAg7Leo6riJIOuTseq4iSfqs7wK66y47ISc7J2YICfquLDrsIAg65Ox6riJJyDruYTqtZAiIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iNDMwLjU3MDk5OTk5OTk5OTk3LDMyOS44NTUgNTM2LjUzNDUsNDM1LjgxODUwMDAwMDAwMDAzIDQzMC41NzA5OTk5OTk5OTk5Nyw1NDEuNzgyIDMyNC42MDc0OTk5OTk5OTk5Niw0MzUuODE4NTAwMDAwMDAwMDMiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNDMwLjU3MDk5OTk5OTk5OTk3IiB5PSI0MzUuODE4NTAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjQzMC41NzA5OTk5OTk5OTk5NyIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPk1BQyDwn46W77iPPC90c3Bhbj48dHNwYW4geD0iNDMwLjU3MDk5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rgpjsnZggJiMzOTvruYTrsIAg7Leo6riJIOuTseq4iSYjMzk76rO8PC90c3Bhbj48dHNwYW4geD0iNDMwLjU3MDk5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rrLjshJzsnZggJiMzOTvquLDrsIAg65Ox6riJJiMzOTsg67mE6rWQPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkQiIGRhdGEtbGFiZWw9IuuNsOydtO2EsCDwn5OBIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU5MC44MzMiIHk9IjUzMi45MjE3NSIgd2lkdGg9IjEwMy40NTMiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI2NDIuNTU5NSIgeT0iNTUxLjM3MTc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7rjbDsnbTthLAg8J+TgTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTTIiIGRhdGEtbGFiZWw9IkRBQyDwn4+gCuusuOyEnCAn7IaM7Jyg7J6QJ+qwgArrgpjsl5Dqsowg7ZeI65297ZW0IOykrOuKlOqwgD8iIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iNDMwLjU3MSw1NjkuNzgxOTk5OTk5OTk5OSA1MzYuMTY0LDY3NS4zNzQ5OTk5OTk5OTk5IDQzMC41NzEsNzgwLjk2Nzk5OTk5OTk5OTggMzI0Ljk3ODAwMDAwMDAwMDA3LDY3NS4zNzQ5OTk5OTk5OTk5IiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0MzAuNTcxIiB5PSI2NzUuMzc0OTk5OTk5OTk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNDMwLjU3MSIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPkRBQyDwn4+gPC90c3Bhbj48dHNwYW4geD0iNDMwLjU3MSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+66y47IScICYjMzk77IaM7Jyg7J6QJiMzOTvqsIA8L3RzcGFuPjx0c3BhbiB4PSI0MzAuNTcxIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rgpjsl5Dqsowg7ZeI65297ZW0IOykrOuKlOqwgD88L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTTMiIGRhdGEtbGFiZWw9IlJCQUMg8J+PogrrgrTqsIAg7ZqM7IKs7JeQ7IScCuunoeydgCAn7Jet7ZWgKOyngeq4iSkn7J20IOutlOqwgD8iIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iNDMwLjU3MDk5OTk5OTk5OTk3LDgwOC45NjgwMDAwMDAwMDAxIDU0Mi44MzMsOTIxLjIzIDQzMC41NzA5OTk5OTk5OTk5NywxMDMzLjQ5MiAzMTguMzA4OTk5OTk5OTk5OTcsOTIxLjIzIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0MzAuNTcwOTk5OTk5OTk5OTciIHk9IjkyMS4yMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNDMwLjU3MDk5OTk5OTk5OTk3IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+UkJBQyDwn4+iPC90c3Bhbj48dHNwYW4geD0iNDMwLjU3MDk5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rgrTqsIAg7ZqM7IKs7JeQ7IScPC90c3Bhbj48dHNwYW4geD0iNDMwLjU3MDk5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rp6HsnYAgJiMzOTvsl63tlaAo7KeB6riJKSYjMzk77J20IOutlOqwgD88L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTTQiIGRhdGEtbGFiZWw9IkFCQUMg4piB77iPCuuCtCDsl63tlaAgKyDtmITsnqwg7Iuc6rCEICsK7KCR7IaNIElQICsg6riw6riwIOyDge2DnCDrr7nsiqQhIiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjQzMC41NzEsODQuMDAwMDAwMDAwMDAwMDEgNTM5LjQ5ODUsMTkyLjkyNzUgNDMwLjU3MSwzMDEuODU1IDMyMS42NDM1LDE5Mi45Mjc1IiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjQzMC41NzEiIHk9IjE5Mi45Mjc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0MzAuNTcxIiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+QUJBQyDimIHvuI88L3RzcGFuPjx0c3BhbiB4PSI0MzAuNTcxIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rgrQg7Jet7ZWgICsg7ZiE7J6sIOyLnOqwhCArPC90c3Bhbj48dHNwYW4geD0iNDMwLjU3MSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7KCR7IaNIElQICsg6riw6riwIOyDge2DnCDrr7nsiqQhPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik5vdGUiIGRhdGEtbGFiZWw9Ik5vdGUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iNjguNjI2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iOTAuMzEzIiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk5vdGU8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 접근 통제 4대 모델 전격 해부 (3단 표 - 출제 1순위)**

모델마다 \*\*'권한을 결정하는 기준'\*\*과 \*\*'누가 권한을 부여하는가'\*\*를 헷갈리지 않게 찌르는 것이 가장 중요합니다.

| **4대 모델 명칭**                                    | **접근 권한을 결정하는 '핵심 기준'과 메커니즘**                                                                                          | **통제 환경 및 권한 부여 주체**                                                                                |
| :---------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| **1. 강제 접근 통제** **MAC** *(Mandatory)*           | **기준: '보안 등급(Clearance) 및 레이블'.** 사용자의 허가 등급과 파일에 부여된 기밀 등급을 강제로 매칭함. (예: Top Secret 등급).                              | **\[중앙 집중형 국방/군사 환경]** 오직 \*\*'시스템 관리자(Admin)'\*\*만이 권한을 부여함. 문서의 원작자라도 권한 변경 불가.                   |
| **2. 임의 접근 통제** **DAC** *(Discretionary)*       | **기준: '사용자의 신분(Identity)'.** ACL(접근 제어 목록)에 이름이 있는지 확인함.                                                               | **\[PC, 리눅스, 윈도우 OS 표준 환경]** 해당 파일의 \*\*'소유자(Owner)'\*\*가 자기 마음대로 임의로 타인에게 권한을 줌. (트로이 목마 해킹에 취약함). |
| **3. 역할 기반 접근 통제** **RBAC** *(Role-Based)*      | **기준: '사용자의 역할(Role) / 직급'.** 권한을 사용자에게 주지 않고 '과장', '부장'이라는 역할 그룹에 준 뒤, 사용자를 그 역할에 배정함.                                | **\[인사이동이 잦은 대기업, DBMS 환경]** 관리자가 권한 부여. 인사이동이나 퇴사 시 관리가 매우 편함 (관리의 복잡도 극단적 감소).                    |
| **4. 속성 기반 접근 통제** **ABAC** *(Attribute-Based)* | **기준: '주체 + 객체 + 동적 환경 조건'.** 사용자의 직급뿐만 아니라 위치, IP, 접속 시간(오전 9시) 등 다양한 속성을 종합하여 \*\*'조건문(IF-THEN)'\*\*으로 접근을 동적으로 허용함. | **\[클라우드, MSA, 제로 트러스트 환경]** 세밀하고 유연한 접근 제어가 가능. 글로벌 클라우드의 IAM(권한 관리) 정책에 널리 쓰임. (XACML 언어 등 활용).   |

#### **IV. \[결론/제언] 제로 트러스트(Zero Trust) 아키텍처와 ABAC의 완벽한 융합**

* **(키워드 위주 2줄 마무리)** "과거 사내망 기반의 RBAC 모델은 퇴사자의 권한 회수 누락이나 계정 탈취(Credential Theft) 시 속수무책이었습니다. 오늘날 경계가 무너진 클라우드 환경에서는 **'아무도 믿지 마라(Never Trust, Always Verify)'라는 제로 트러스트 철학을 근간으로, 사용자의 맥락(Context)과 환경을 실시간으로 분석하여 권한을 제어하는 ABAC 모델이 차세대 인프라 보안의 심장으로 확고히 자리 잡고 있습니다.**"
