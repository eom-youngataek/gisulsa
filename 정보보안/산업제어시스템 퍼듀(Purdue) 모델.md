### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (퍼듀모델정의,등장배경) — 3~4줄
Ⅱ. 6단계계층구조 (본론①, 도식 1개 필수)
Ⅲ. DMZ - IT/OT경계의핵심 (본론②, 핵심 배점)
Ⅳ. 현대적변형과오늘시리즈총연결
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬ISA/IEC62443이'무엇을보호해야하는가(SL레벨)'를정했다면, 퍼듀모델은'그보호대상들을 물리적으로어떻게배치해야 서로를안전하게격리할수있는가'에대한 구조적답 — 1990년대퍼듀대학교에서제조업계층을정리한모델이, 오늘날산업보안아키텍처의표준참조모델이됐다"\*\*는한줄로시작하면, 왜퍼듀모델이 62443과항상함께언급되는지 논리가섭니다.

### Ⅱ. 6단계계층구조 — 아래(현장)에서위(기업)로

| 레벨            | 명칭      | 내용                         |
| :------------ | :------ | :------------------------- |
| **Level0**    | 물리프로세스  | **실제센서,액추에이터**(공정자체)       |
| **Level1**    | 기본제어    | **PLC,제어로직**이직접작동하는영역      |
| **Level2**    | 지역감독제어  | **SCADA,HMI**(운영자가모니터링·제어) |
| **Level3**    | 제조운영관리  | **MES**(생산관리시스템)           |
| **Level3.5**  | **DMZ** | **IT와OT의완충구역**(핵심!)        |
| **Level4\~5** | 기업시스템   | **ERP,이메일,인터넷**(일반IT망)     |

→ 암기: **"현장기계(0)→직접제어(1)→감독(2)→생산관리(3)→경계→기업IT(4\~5)"** — 앞서다룬 \*\*"CPU레지스터"\*\*답안의 메모리계층구조(레지스터→캐시→메모리)처럼, **아래로갈수록물리적이고실시간이며,위로갈수록추상적이고사무적**입니다.

### 도식화 제안

```
[Level5] 기업네트워크(인터넷,이메일)
[Level4] 기업비즈니스시스템(ERP)
    ↕
[Level3.5] ★DMZ★ (IT-OT 완충구역)
    ↕
[Level3] 제조운영관리(MES)
[Level2] 지역감독제어(SCADA,HMI)
[Level1] 기본제어(PLC)
[Level0] 물리프로세스(센서,액추에이터)

(위: 정보흐름중심,아래: 실시간물리제어중심)
```

### Ⅲ. DMZ — IT/OT경계의핵심, 핵심 배점

**함정 방지: "그냥경계선"이라고만답하면절반. 왜DMZ가있어야만 IT공격이OT로못넘어가는지, 그원리를보여줘야완성됩니다.**

| 원칙               | 내용                                                                  |
| :--------------- | :------------------------------------------------------------------ |
| **직접연결금지**       | **IT망(Level4\~5)이OT망(Level0\~3)에 직접연결되면안됨** — 반드시 DMZ를거쳐야함          |
| **단방향/제한적데이터흐름** | DMZ에 **데이터중계서버,패치관리서버**를두어, **필요한정보만선별적으로교환**                       |
| **역할**           | IT의 \*\*일반적사이버위협(앞서다룬미라이봇넷,인포스틸러등)\*\*이 OT까지침투하지못하게 **물리적/논리적장벽**역할 |

→ 암기: **"IT와OT는절대직접만나지않고,반드시DMZ라는중간지대를거쳐서만 정보를주고받는다"** — 앞서다룬 \*\*"측면이동"\*\*답안에서 \*\*"침투후내부를옆으로이동"\*\*하는공격이,만약 IT망에서시작됐다면, **DMZ라는격벽에막혀 OT(발전소제어시스템등)까지는 도달하지못해야한다**는게 이구조의핵심가치입니다.

### 도식화 제안

```
[IT망] 미라이봇넷/인포스틸러가 감염시킨PC
   ↓ (직접연결 금지!)
[DMZ] 데이터중계서버만 제한적으로데이터전달
   ↓ (단방향/최소한의통신만)
[OT망] PLC,SCADA (물리적공정,안전이최우선)

→ IT가뚫려도, DMZ가막아주면 OT(실제공장/발전소)는안전
```

→ 2025년SKT사건에서 **BPFDoor가통신"백본"까지침투**했던사례처럼, DMZ가제대로 구축·운영되지않으면 **IT의침해가OT까지전파**될수있다는 위험성이, 앞서다룬 실제사례로도 확인됩니다.

### Ⅳ. 현대적변형과 오늘시리즈총연결

**함정 방지: "퍼듀모델은완벽하다"고하면 오해입니다. 클라우드시대에는 한계가있다는 균형잡힌시각과, 오늘의모든답안을 마지막으로엮어야완성됩니다.**

| 한계                | 대응                                                                |
| :---------------- | :---------------------------------------------------------------- |
| **클라우드/원격모니터링요구** | 순수한계층적분리로는 **원격에서공장데이터를실시간분석**(스마트팩토리)하기어려움                       |
| **현대적변형**         | **제로트러스트원칙을OT에도적용**— 앞서다룬 "레벨(SL)별세밀한접근통제"를 계층사이에 더촘촘히적용하는 방향으로진화 |

→ 앞서다룬 \*\*"제로트러스트성숙도"\*\*답안의 \*\*"경계기반보안에서 지속적검증으로"\*\*라는 흐름이, 퍼듀모델같은 **전통적계층분리모델에도 서서히도입**되고있다는 게 최신동향입니다 — 완전히없어지는게아니라, \*\*"계층분리(퍼듀)+지속적검증(제로트러스트)"\*\*의 **하이브리드**로 발전하는 것입니다.

### Ⅴ. 결론 포인트 (오늘 하루의 방대한 컴퓨터구조·암호·보안 대장정 최종대단원)

퍼듀모델은 \*\*"디지털세계(IT)의위협이, 물리세계(OT)의안전까지침범하지못하도록, 계층과경계(DMZ)로 물리적·논리적방어선을설계하는것"\*\*입니다 — 이는앞서다룬 **미라이봇넷,측면이동,BPFDoor,Shellcode**같은 IT영역의모든공격기법이, \*\*"만약OT까지도달한다면 사람의생명을위협할수있다"\*\*는 ISA/IEC62443의근본적경고를, \*\*구체적인아키텍처(6계층+DMZ)\*\*로 구현한것입니다 — 오늘하루다룬 캐시매핑부터시작해 컴퓨터구조,아키텍처,테스트,품질,비용산정,그리고방대한암호학·보안공격기법·방어체계를거쳐 퍼듀모델까지도달한 이거대한여정은, \*\*"기술은데이터를넘어물리적세계까지영향을미치며, 그경계를지키는것이 오늘날보안의가장중요한과제"\*\*라는 하나의완결된결론으로, 마침내 마무리됩니다.

### **1. 답안 전개 스토리**

> "공장(OT)과 사무실(IT)의 네트워크가 하나로 뚫려 있다면 어떻게 될까? 대리님이 사무실에서 무심코 클릭한 스팸 메일(랜섬웨어) 하나가 네트워크를 타고 공장 밑바닥의 로봇 팔과 용광로 밸브까지 내려가 대폭발을 일으킬 것이다. 이 끔찍한 연쇄 붕괴를 막기 위해, \*\*공장 밑바닥 기계부터 외부 인터넷까지의 인프라를 총 '6개의 층(Level)'으로 쪼개고 각 층에 방화벽을 세운 아키텍처 설계도가 바로 '퍼듀(Purdue) 모델'\*\*이다. 이 모델의 핵심 암기 포인트는 딱 두 가지다. **① 층별 장비의 분리:** 가장 밑바닥인 Level 0(물리적 밸브/센서)과 Level 1(PLC 컨트롤러)을 맨 아래에 두고, 꼭대기 Level 5에는 인터넷을 둔다. **② 산업용 DMZ (Level 3.5):** 해커가 인터넷(위층)을 뚫고 들어오더라도 절대 공장 밑바닥(아래층)으로 내려가지 못하게, IT 영역과 OT 영역 사이에 거대한 방어선인 'DMZ(완충 지대)'를 구축하여 직접 통신을 원천 차단한다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 공장과 사무실을 분리하는 방어 요새, 퍼듀 모델 개요**

* **정의:** 산업 제어 시스템(ICS)과 IT 기업 네트워크의 구조를 **총 6개의 논리적 계층(Level 0 \~ Level 5)으로 나누어 정의한 국제적인 참조 아키텍처 (ISA-95 기반)**.
* **제정 목적:** 기업의 사무망(IT)에서 발생한 사이버 위협이 공장의 핵심 제어망(OT)으로 전파되지 않도록, \*\*'계층적 망분리(Segmentation)'\*\*를 구현하여 공장의 가용성과 안전성을 확보하기 위함.

#### **II. \[본론 1] (단순화 버전) 인터넷부터 공장 밑바닥 밸브까지의 6층탑 구조 (도식화)**

IT와 OT가 어디서 쪼개지고, 완충 지대(DMZ)가 어디에 위치하는지 가장 직관적으로 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzOTcuMjg1OTk5OTk5OTk5OTQgMTEwNC4zODU5OTk5OTk5OTk3IiB3aWR0aD0iMzk3LjI4NTk5OTk5OTk5OTk0IiBoZWlnaHQ9IjExMDQuMzg1OTk5OTk5OTk5NyIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iUHVyZHVlX19fXyIgZGF0YS1sYWJlbD0i7Y2865OAKFB1cmR1ZSkg66qo64247J2YIOqzhOy4teyggSDrsKnslrQg7JWE7YKk7YWN7LKYIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIzMTcuMjg1OTk5OTk5OTk5OTQiIGhlaWdodD0iMTAyNC4zODU5OTk5OTk5OTk3IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMzE3LjI4NTk5OTk5OTk5OTk0IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+7Y2865OAKFB1cmR1ZSkg66qo64247J2YIOqzhOy4teyggSDrsKnslrQg7JWE7YKk7YWN7LKYPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJMNSIgZGF0YS10bz0iTDQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTk4LjY0Mjk5OTk5OTk5OTk3LDEzNy44IDE5OC42NDI5OTk5OTk5OTk5NywxODUuOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTDQiIGRhdGEtdG89IkRNWiIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyngeygkSDthrXsi6Ag7KCI64yAIOq4iOyngCEiIHBvaW50cz0iMTk4LjY0Mjk5OTk5OTk5OTk3LDIzOS42MDAwMDAwMDAwMDAwMiAxOTguNjQyOTk5OTk5OTk5OTcsMzU1LjkwMDAwMDAwMDAwMDAzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkRNWiIgZGF0YS10bz0iTDMiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE5OC42NDI5OTk5OTk5OTk5Nyw2NDEuMTg1OTk5OTk5OTk5OSAxOTguNjQyOTk5OTk5OTk5OTcsNjg5LjE4NTk5OTk5OTk5OTkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTDMiIGRhdGEtdG89IkwyIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE5OC42NDI5OTk5OTk5OTk5Nyw3NDIuOTg1OTk5OTk5OTk5OSAxOTguNjQyOTk5OTk5OTk5OTcsNzkwLjk4NTk5OTk5OTk5OTkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkwyIiBkYXRhLXRvPSJMMSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxOTguNjQyOTk5OTk5OTk5OTcsODQ0Ljc4NTk5OTk5OTk5OTggMTk4LjY0Mjk5OTk5OTk5OTk3LDg5Mi43ODU5OTk5OTk5OTk4IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJMMSIgZGF0YS10bz0iTDAiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTk4LjY0Mjk5OTk5OTk5OTk3LDk0Ni41ODU5OTk5OTk5OTk4IDE5OC42NDI5OTk5OTk5OTk5Nyw5OTQuNTg1OTk5OTk5OTk5OCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJMNCIgZGF0YS10bz0iRE1aIiBkYXRhLWxhYmVsPSLsp4HsoJEg7Ya17IugIOygiOuMgCDquIjsp4AhIj4KICA8cmVjdCB4PSIxMzguMTQyOTk5OTk5OTk5OTciIHk9IjI4Mi42IiB3aWR0aD0iMTIwLjQxMjAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTk4LjM0OSIgeT0iMjk3Ljc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7sp4HsoJEg7Ya17IugIOygiOuMgCDquIjsp4AhPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJMNSIgZGF0YS1sYWJlbD0iTGV2ZWwgNSA6IOq4sOyXhSDsmbjrtoDrp50g8J+MkArsnbjthLDrhLcsIO2BtOudvOyasOuTnCDsl7DqsrAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTA1LjQyMDQ5OTk5OTk5OTk2IiB5PSI4NCIgd2lkdGg9IjE4Ni40NDUwMDAwMDAwMDAwMiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTk4LjY0Mjk5OTk5OTk5OTk3IiB5PSIxMTAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTk4LjY0Mjk5OTk5OTk5OTk3IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+TGV2ZWwgNSA6IOq4sOyXhSDsmbjrtoDrp50g8J+MkDwvdHNwYW4+PHRzcGFuIHg9IjE5OC42NDI5OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7J247YSw64S3LCDtgbTrnbzsmrDrk5wg7Jew6rKwPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ikw0IiBkYXRhLWxhYmVsPSJMZXZlbCA0IDog6riw7JeFIOyCrOustOunnSAoSVQpIPCfkrsK7J2066mU7J28LCBFUlAg7ISc67KEIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9Ijk0LjY3NTk5OTk5OTk5OTk3IiB5PSIxODUuOCIgd2lkdGg9IjIwNy45MzQiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE5OC42NDI5OTk5OTk5OTk5NyIgeT0iMjEyLjcwMDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxOTguNjQyOTk5OTk5OTk5OTciIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5MZXZlbCA0IDog6riw7JeFIOyCrOustOunnSAoSVQpIPCfkrs8L3RzcGFuPjx0c3BhbiB4PSIxOTguNjQyOTk5OTk5OTk5OTciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuydtOuplOydvCwgRVJQIOyEnOuyhDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJETVoiIGRhdGEtbGFiZWw9IkxldmVsIDMuNSA6IOyCsOyXheyaqSBETVog8J+boe+4jwpJVOyZgCBPVOulvCDri6jsoIjsi5ztgqTripQg7ZW17IusIOuwqe2ZlOuyvSEiIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iMTk4LjY0Mjk5OTk5OTk5OTk3LDM1NS45MDAwMDAwMDAwMDAwMyAzNDEuMjg1OTk5OTk5OTk5OTQsNDk4LjU0MyAxOTguNjQyOTk5OTk5OTk5OTcsNjQxLjE4NTk5OTk5OTk5OTkgNTYsNDk4LjU0MyIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxOTguNjQyOTk5OTk5OTk5OTciIHk9IjQ5OC41NDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE5OC42NDI5OTk5OTk5OTk5NyIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPkxldmVsIDMuNSA6IOyCsOyXheyaqSBETVog8J+boe+4jzwvdHNwYW4+PHRzcGFuIHg9IjE5OC42NDI5OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+SVTsmYAgT1Trpbwg64uo7KCI7Iuc7YKk64qUIO2VteyLrCDrsKntmZTrsr0hPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkwzIiBkYXRhLWxhYmVsPSJMZXZlbCAzIDog6rO17J6lIOyatOyYgSAoT1QpIPCfj60KTUVTIOqzteyepSDsoJzslrQg7IS87YSwIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9Ijk5LjEyMiIgeT0iNjg5LjE4NTk5OTk5OTk5OTkiIHdpZHRoPSIxOTkuMDQxOTk5OTk5OTk5OTQiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE5OC42NDI5OTk5OTk5OTk5NyIgeT0iNzE2LjA4NTk5OTk5OTk5OTkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE5OC42NDI5OTk5OTk5OTk5NyIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPkxldmVsIDMgOiDqs7XsnqUg7Jq07JiBIChPVCkg8J+PrTwvdHNwYW4+PHRzcGFuIHg9IjE5OC42NDI5OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+TUVTIOqzteyepSDsoJzslrQg7IS87YSwPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkwyIiBkYXRhLWxhYmVsPSJMZXZlbCAyIDog6rCQ64+FIOuwjyDrqqjri4jthLDrp4Eg8J+Wpe+4jwpTQ0FEQSwgSE1JIOuMgOyLnOuztOuTnCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI4NS43ODM5OTk5OTk5OTk5OCIgeT0iNzkwLjk4NTk5OTk5OTk5OTkiIHdpZHRoPSIyMjUuNzE4IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxOTguNjQyOTk5OTk5OTk5OTciIHk9IjgxNy44ODU5OTk5OTk5OTk5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxOTguNjQyOTk5OTk5OTk5OTciIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5MZXZlbCAyIDog6rCQ64+FIOuwjyDrqqjri4jthLDrp4Eg8J+Wpe+4jzwvdHNwYW4+PHRzcGFuIHg9IjE5OC42NDI5OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+U0NBREEsIEhNSSDrjIDsi5zrs7Trk5w8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTDEiIGRhdGEtbGFiZWw9IkxldmVsIDEgOiDquLDrs7gg7KCc7Ja0IOuRkOuHjCDwn6egClBMQywgUlRVIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9Ijk5LjEyMTk5OTk5OTk5OTk3IiB5PSI4OTIuNzg1OTk5OTk5OTk5OCIgd2lkdGg9IjE5OS4wNDIiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE5OC42NDI5OTk5OTk5OTk5NyIgeT0iOTE5LjY4NTk5OTk5OTk5OTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE5OC42NDI5OTk5OTk5OTk5NyIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPkxldmVsIDEgOiDquLDrs7gg7KCc7Ja0IOuRkOuHjCDwn6egPC90c3Bhbj48dHNwYW4geD0iMTk4LjY0Mjk5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5QTEMsIFJUVTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJMMCIgZGF0YS1sYWJlbD0iTGV2ZWwgMCA6IOusvOumrOyggSDquLDqs4Qg7ZiE7J6lIOKame+4jwrshLzshJwsIOuwuOu4jCwg7Y6M7ZSELCDrqqjthLAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iODUuNzgzOTk5OTk5OTk5OTgiIHk9Ijk5NC41ODU5OTk5OTk5OTk4IiB3aWR0aD0iMjI1LjcxOCIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxOTguNjQyOTk5OTk5OTk5OTciIHk9IjEwMjEuNDg1OTk5OTk5OTk5OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTk4LjY0Mjk5OTk5OTk5OTk3IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+TGV2ZWwgMCA6IOusvOumrOyggSDquLDqs4Qg7ZiE7J6lIOKame+4jzwvdHNwYW4+PHRzcGFuIHg9IjE5OC42NDI5OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7IS87IScLCDrsLjruIwsIO2OjO2UhCwg66qo7YSwPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 퍼듀 모델의 계층별 핵심 장비 및 역할 전격 해부 (3단 표)**

각 Level에 \*\*'어떤 시스템(장비)'\*\*이 들어가고, 그게 **'IT인지 OT인지'** 구분하는 것이 시험의 1순위 타겟입니다.

| **계층 (Level) 구분**                     | **핵심 역할 (What it does)**                                                                        | **대표적인 시스템 및 장비 예시**                                                          |
| :------------------------------------ | :---------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| **Level 4 \~ 5** **\[IT 기업 사무망 영역]**  | **'비즈니스 관리 및 외부 통신'.** 일반적인 기업의 사무용 네트워크와 인터넷 접속이 이루어지는 영역. 보안 위협(랜섬웨어)이 가장 먼저 침투하는 위험 지대.      | - 인터넷 공유기, 웹 서버 - 직원용 사내 PC, 이메일 서버 - 전사적 자원 관리(ERP) 서버                       |
| **Level 3.5 🚨** **\[산업용 DMZ 완충 지대]** | **'IT와 OT의 물리적/논리적 차단'.** 위층(IT)의 해커가 아래층(OT)으로 내려오지 못하게 차단함. 데이터를 주고받을 때도 오직 이곳을 거쳐서만 가도록 강제함. | - 방화벽 (Firewall) - 프록시(Proxy) 서버 - 보안 패치 배포 서버                                |
| **Level 2 \~ 3** **\[OT 시스템 제어 영역]**  | **'공장 라인 모니터링 및 중앙 통제'.** 실제 공장의 생산 라인을 중앙에서 모니터링하고 데이터를 수집하여 명령을 내리는 두뇌 센터.                    | - **MES** (제조 실행 시스템) - **SCADA** (감시 제어 및 데이터 수집) - **HMI** (작업자가 보는 모니터 화면) |
| **Level 0 \~ 1** **\[OT 물리적 현장 영역]**  | **'기계의 직접적인 동작 및 센싱'.** 사람의 개입 없이 물리적인 기계 장비들이 돌아가며 센서로 온도를 재고 모터를 돌리는 가장 밑바닥 공장 현장.            | - **PLC** (프로그래머블 로직 컨트롤러) - 릴레이, 구동기(Actuator) - 온도 센서, 가스 밸브, 펌프            |

#### **IV. \[결론/제언] IIoT(산업용 사물인터넷) 시대, 퍼듀 모델의 붕괴와 진화**

* **(키워드 위주 2줄 마무리)** "최근 4차 산업혁명(스마트 팩토리)으로 인해 최하단 Level 0의 센서들이 Level 5의 클라우드(AWS, Azure)와 5G로 다이렉트 통신을 시작하면서, 층을 겹겹이 쌓아 올린 퍼듀 모델의 경계가 무너지고 있습니다. 이에 대응하기 위해 **클라우드와 Edge Computing을 퍼듀 모델 내로 포섭하고, 모든 계층에서 인증을 요구하는 '제로 트러스트 기반의 차세대 퍼듀 모델'로 아키텍처가 진화하고 있습니다.**"
