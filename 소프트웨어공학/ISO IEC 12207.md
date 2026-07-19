### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (표준의목적,SDLC와의관계) — 3~4줄
Ⅱ. 3대프로세스카테고리 (본론①, 도식 1개 필수)
Ⅲ. 기본생명주기프로세스 심화 (본론②, 핵심 배점)
Ⅳ. 연관표준체계및오늘시리즈와의연결
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬 폭포수,애자일,나선형같은SDLC방법론들은 '어떤순서로개발할지(How)'를다뤘는데,ISO/IEC12207은 그보다한단계위에서 '소프트웨어생애전체에어떤작업(What)이필요한지'를 정의 — 방법론이아니라, 그방법론이채워야할프로세스의뼈대"\*\*라는 한줄로시작하면, 왜 "무엇을(What)정의하되 어떻게(How)는규정하지않는다"는 표준의성격이 명확해집니다.

### Ⅱ. 3대프로세스카테고리 — "기·지·조"

| 카테고리           | 내용                                              |
| :------------- | :---------------------------------------------- |
| **기본생명주기프로세스** | **획득,공급,개발,운영,유지보수** 등 핵심프로세스                   |
| **지원생명주기프로세스** | 기본프로세스를 **지원**(품질보증,검증,확인,형상관리,문서화등) — 필요시선택적수행 |
| **조직생명주기프로세스** | **조직전체차원**의관리(관리,기반구조,개선,교육훈련)                  |

→ 암기: **"기본은핵심작업,지원은핵심작업을돕는것,조직은그모든걸받쳐주는터전"** — 앞서다룬 \*\*"정보시스템감리"\*\*에서 \*\*"절차(기본)-산출물검증(지원)-거버넌스(조직)"\*\*로나뉘던 구조가, 사실이 12207의 3대카테고리와 정확히같은 3층구조입니다.

### 도식화 제안

```
      [조직생명주기프로세스]
   조직관리,기반구조,개선,교육 
              ↓ (터전을제공)
      [기본생명주기프로세스]
   획득→공급→개발→운영→유지보수
              ↑ (지원을받음)
      [지원생명주기프로세스]
   품질보증,검증,확인,형상관리,문서화,
   앞서다룬 "테스트프로세스(29119)"도 여기속함
```

### Ⅲ. 기본생명주기프로세스 심화 — 핵심 배점

**함정 방지: "개발프로세스만있다"고생각하면절반. 개발앞뒤로 "획득/공급","운영/유지보수"까지 포함하는 전체생애주기라는걸보여줘야완성됩니다.**

| 프로세스                  | 내용                                                   |
| :-------------------- | :--------------------------------------------------- |
| **획득(Acquisition)**   | 발주자관점 — **요구정의,공급자선정,계약관리** — 앞서다룬 "정보시스템감리"의발주단계와연결 |
| **공급(Supply)**        | 공급자관점 — **제안,계약이행,인도**                               |
| **개발(Development)**   | 앞서다룬 **SDLC전체**(요구분석\~시험) 가여기속함                      |
| **운영(Operation)**     | 실제 **운영환경에서의사용지원**                                   |
| **유지보수(Maintenance)** | 앞서다룬 \*\*"Lehman의소프트웨어진화법칙"\*\*이설명하는 그지속적수정단계        |

→ 암기: **"사는사람(획득)과파는사람(공급)이계약을맺고,만들고(개발),쓰고(운영),계속고친다(유지보수)"** — 앞서다룬 \*\*"SDLC의5단계(요구-설계-구현-시험-유지보수)"\*\*는 사실 이 **"개발"프로세스하나를 더세분화한것**이며, 12207은 그개발프로세스 **앞뒤로 획득·공급·운영까지포함하는 더넓은생애주기**를 다룹니다.

### Ⅳ. 연관표준체계 및 오늘시리즈와의연결

| 표준                       | 관계                                              |
| :----------------------- | :---------------------------------------------- |
| **ISO/IEC 15288**        | **시스템**생명주기프로세스(12207의 소프트웨어버전과 짝을이루는 상위/병행표준)  |
| **ISO/IEC 15504(SPICE)** | 12207을 **기본틀로삼아** 프로세스의 **성숙도를평가**하는모델          |
| **ISO/IEC 29119**        | 12207의 **지원프로세스중"테스팅"부분을 별도로심화**한표준(앞서다룬그표준)    |
| **ISO/IEC 25010**        | 12207프로세스를거쳐만들어진 **결과물(제품)의품질을평가**하는모델(앞서다룬그표준) |

→ 암기: **"12207이전체뼈대,SPICE는그뼈대로성숙도재고,29119는그중테스팅만심화,25010은결과물품질을잰다"** — 오늘하루다룬 \*\*ISO29119(테스트프로세스표준)\*\*과 \*\*ISO25010(품질모델)\*\*이 사실 **이12207이라는 더큰우산아래, 각자다른관심영역(테스팅/품질)을 심화한전문표준들**이었다는게 이답안의핵심통합포인트입니다.

### 도식화 제안

```
        [ISO/IEC 12207] ← 소프트웨어생명주기전체(최상위우산)
              ↓
    ┌─────────┼─────────┐
[SPICE/15504]      [29119]         [25010]
프로세스성숙도평가   테스팅프로세스심화   제품품질모델
```

### Ⅴ. 결론 포인트 (표준 시리즈 대단원)

ISO/IEC 12207은 \*\*"소프트웨어를만들고,쓰고,고치는모든과정에서 실무자들이같은언어로소통할수있게 프로세스의뼈대(What)를표준화"\*\*한 것이며, 어떻게(How)수행할지는 각조직/프로젝트가 **폭포수,애자일,나선형등원하는방법론으로자유롭게테일러링**하도록열어둡니다 — 이는 오늘하루다룬SDLC(어떻게)→ISO29119(테스팅을어떻게)→ISO25010(품질을무엇으로볼지)의 시리즈전체가, 사실 **이12207이라는하나의공통뼈대위에서 각자의전문영역을살로채워온것**이었다는 결론으로, 오늘의방대한 소프트웨어공학표준시리즈전체를 완결할수있습니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "소프트웨어 프로젝트를 시작하면 난장판이 벌어지기 일쑤다. 돈을 낸 발주처(고객)는 '이거 왜 이렇게 느려?'라고 화를 내고, 수주한 개발사는 '우린 다 만들었는데 인프라팀이 서버를 안 주잖아!'라며 서로 책임을 떠넘긴다. 소프트웨어가 처음 기획되어 개발되고 운영되다가 마지막에 폐기될 때까지, 도대체 \*\*'누가, 언제, 어떤 프로세스를 책임져야 하는가'\*\*를 명확히 룰로 정해놓지 않으면 프로젝트는 무조건 산으로 간다. 이 혼돈을 끝내기 위해 전 세계 공통으로 약속한 '소프트웨어 생명주기 헌법'이 바로 \*\*'ISO/IEC 12207'\*\*이다. 12207은 소프트웨어와 얽힌 모든 인간의 활동을 \*\*'3대 생명주기 프로세스(기본, 지원, 조직)'\*\*로 완벽하게 쪼갰다. 첫째, 무대 위에서 직접 땀 흘리며 뛰는 주인공들인 \*\*'기본 생명주기'\*\*다. 돈을 주고 사는 사람(획득), 만들어 파는 사람(공급), 코드를 짜는 사람(개발), 시스템을 돌리는 사람(운영), 버그를 고치는 사람(유지보수)의 임무를 정의한다. 둘째, 무대 뒤에서 주인공들이 헛발질 못하게 돕고 감시하는 스태프들인 \*\*'지원 생명주기'\*\*다. 소스코드가 꼬이지 않게 막아주는 '형상 관리', 버그가 없는지 검사하는 '품질 보증(QA)' 등이 속한다. 셋째, 회사 차원에서 아예 멍석을 깔아주는 \*\*'조직 생명주기'\*\*다. 직원들 교육 훈련 시키고, 서버 인프라를 구축해 주는 일이다. 이 12207 표준 헌법 덕분에 전 세계의 발주자와 수주자는 드디어 하나의 동일한 언어로 계약하고 다툼 없이 프로젝트를 완수할 수 있게 되었다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 누가, 언제, 무엇을 할 것인가? SDLC의 헌법 ISO 12207 개요**

* **정의:** 소프트웨어의 획득, 공급, 개발, 운영, 유지보수 및 폐기에 이르기까지 **소프트웨어 생명주기(SDLC) 전 과정에서 수행되는 프로세스와 활동, 역할(누가 무엇을 할지)을 포괄적으로 정의한 국제 표준 프레임워크**.
* **제정 목적:** 발주자(구매자)와 수주자(공급자) 간의 의사소통 혼란을 없애기 위해 '공통의 언어'를 제공하고, 소프트웨어 개발 및 관리 프로젝트의 투명성과 품질을 극대화하기 위함.

#### **II. \[본론 1] 소프트웨어 생명주기를 지탱하는 3대 프로세스 아키텍처 (도식화)**

각 계층이 어떻게 서로 맞물려 시스템을 굴러가게 하는지 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMTA3LjI5NyA2MzYuNSIgd2lkdGg9IjExMDcuMjk3IiBoZWlnaHQ9IjYzNi41IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfX19fXyIgZGF0YS1sYWJlbD0i7KGw7KeBIOyDneuqheyjvOq4sCAo7ZqM7IKsIOywqOybkOydmCDrqY3shJ0g6rmU6riwKSI+CiAgPHJlY3QgeD0iMTM2LjYyNiIgeT0iNDAiIHdpZHRoPSI5MzAuNjcxIiBoZWlnaHQ9IjU1Ni41IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iMTM2LjYyNiIgeT0iNDAiIHdpZHRoPSI5MzAuNjcxIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxNDguNjI2IiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7sobDsp4Eg7IOd66qF7KO86riwICjtmozsgqwg7LCo7JuQ7J2YIOupjeyEnSDquZTquLApPC90ZXh0Pgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9fX18iIGRhdGEtbGFiZWw9IuyngOybkCDsg53rqoXso7zquLAgKOyKpO2DnO2UhOuTpOydmCDtkojsp4gv6rCQ7IucIOyngOybkCkiPgogIDxyZWN0IHg9IjQ5Ni43NDYiIHk9Ijg0IiB3aWR0aD0iNTU0LjU1MSIgaGVpZ2h0PSI0OTYuNSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQ5Ni43NDYiIHk9Ijg0IiB3aWR0aD0iNTU0LjU1MSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTA4Ljc0NiIgeT0iOTgiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+7KeA7JuQIOyDneuqheyjvOq4sCAo7Iqk7YOc7ZSE65Ok7J2YIO2SiOyniC/qsJDsi5wg7KeA7JuQKTwvdGV4dD4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfX19fX18iIGRhdGEtbGFiZWw9Iuq4sOuzuCDsg53rqoXso7zquLAgKOustOuMgCDsnIQg7KO87J246rO165Ok7J2YIO2VteyLrCDsl4XrrLQpIj4KICA8cmVjdCB4PSI5MDIuMDY3IiB5PSIxMjgiIHdpZHRoPSIxMzMuMjMiIGhlaWdodD0iNDM2LjUiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI5MDIuMDY3IiB5PSIxMjgiIHdpZHRoPSIxMzMuMjMiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjkxNC4wNjciIHk9IjE0MiIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7quLDrs7gg7IOd66qF7KO86riwICjrrLTrjIAg7JyEIOyjvOyduOqzteuTpOydmCDtlbXsi6wg7JeF66y0KTwvdGV4dD4KPC9nPgo8L2c+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlAxIiBkYXRhLXRvPSJQMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI5NjguNjgyLDIwOC45IDk2OC42ODIsMjU2LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlAyIiBkYXRhLXRvPSJQMyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI5NjguNjgyLDI5My44IDk2OC42ODIsMzI3LjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlAzIiBkYXRhLXRvPSJQNCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI5NjguNjgyLDM2NC43MDAwMDAwMDAwMDAwNSA5NjguNjgyLDQyNi43MDAwMDAwMDAwMDAwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUDQiIGRhdGEtdG89IlA1IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9Ijk2OC42ODIsNDYzLjYgOTY4LjY4Miw1MTEuNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI2OC42MjYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI3NC4zMTMiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5Ob3RlPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJPIiBkYXRhLWxhYmVsPSLqtIDrpqwsIOyduO2UhOudvCDsp4Dsm5AsIOq1kOycoSDtm4jroKgsIO2UhOuhnOyEuOyKpCDqsJzshKAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTUyLjYyNiIgeT0iMzI3LjgiIHdpZHRoPSIzMTYuMTE5OTk5OTk5OTk5OTUiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjMxMC42ODYiIHk9IjM0Ni4yNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+6rSA66asLCDsnbjtlITrnbwg7KeA7JuQLCDqtZDsnKEg7ZuI66CoLCDtlITroZzshLjsiqQg6rCc7ISgPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTIiBkYXRhLWxhYmVsPSLrrLjshJztmZQsIO2YleyDgSDqtIDrpqwsIO2SiOyniCDrs7Tspp0oUUEpLCDqsoDspp0g67CPIO2ZleyduChWJmFtcDtWKSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1MTIuNzQ2IiB5PSIzMjcuOCIgd2lkdGg9IjM2MS4zMjEiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjY5My40MDY1IiB5PSIzNDYuMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuusuOyEnO2ZlCwg7ZiV7IOBIOq0gOumrCwg7ZKI7KeIIOuztOymnShRQSksIOqygOymnSDrsI8g7ZmV7J24KFYmYW1wO1YpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQMSIgZGF0YS1sYWJlbD0i7ZqN65OdIiBkYXRhLXNoYXBlPSJyb3VuZGVkIj4KICA8cmVjdCB4PSI5MzIuODg3IiB5PSIxNzIiIHdpZHRoPSI3MS41OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSI2IiByeT0iNiIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9Ijk2OC42ODE5OTk5OTk5OTk5IiB5PSIxOTAuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPu2ajeuTnTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUDIiIGRhdGEtbGFiZWw9Iuqzteq4iSIgZGF0YS1zaGFwZT0icm91bmRlZCI+CiAgPHJlY3QgeD0iOTMyLjg4NyIgeT0iMjU2LjkiIHdpZHRoPSI3MS41OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSI2IiByeT0iNiIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9Ijk2OC42ODE5OTk5OTk5OTk5IiB5PSIyNzUuMzQ5OTk5OTk5OTk5OTciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuqzteq4iTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUDMiIGRhdGEtbGFiZWw9IuqwnOuwnCIgZGF0YS1zaGFwZT0icm91bmRlZCI+CiAgPHJlY3QgeD0iOTMyLjg4NyIgeT0iMzI3LjgiIHdpZHRoPSI3MS41OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSI2IiByeT0iNiIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI5NjguNjgxOTk5OTk5OTk5OSIgeT0iMzQ2LjI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7qsJzrsJw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlA0IiBkYXRhLWxhYmVsPSLsmrTsmIEiIGRhdGEtc2hhcGU9InJvdW5kZWQiPgogIDxyZWN0IHg9IjkzMi44ODciIHk9IjQyNi43MDAwMDAwMDAwMDAwNSIgd2lkdGg9IjcxLjU5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjYiIHJ5PSI2IiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iOTY4LjY4MTk5OTk5OTk5OTkiIHk9IjQ0NS4xNTAwMDAwMDAwMDAwMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7Jq07JiBPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQNSIgZGF0YS1sYWJlbD0i7Jyg7KeA67O07IiYIiBkYXRhLXNoYXBlPSJyb3VuZGVkIj4KICA8cmVjdCB4PSI5MTguMDY3IiB5PSI1MTEuNiIgd2lkdGg9IjEwMS4yMjk5OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSI2IiByeT0iNiIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9Ijk2OC42ODIiIHk9IjUzMC4wNTAwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7snKDsp4Drs7TsiJg8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 기본 / 지원 / 조직 3대 프로세스 전격 해부 (3단 표 - 출제 1순위)**

각 3대 대분류 안에 '어떤 세부 활동'들이 속해 있는지를 섞이지 않게 구분해야 합니다.

| **프로세스 대분류**                              | **핵심 역할 및 개념 정의**                                                          | **속해 있는 세부 활동 (서브 프로세스)**                                                                                                                                                                                |
| :---------------------------------------- | :------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. 기본 생명주기** *(Primary Process)*        | 소프트웨어를 획득(구매)하고, 구축(개발)하며, 직접 돌리고(운영) 고치는 **비즈니스의 뼈대이자 직접적인 '주역'들의 프로세스.** | 1. **획득 (Acquisition):** 시스템을 구매하는 발주자. 2. **공급 (Supply):** 시스템을 만들어 파는 수주자. 3. **개발 (Development):** 실제로 코드를 짜고 설계함. 4. **운영 (Operation):** 실제 환경에서 시스템을 구동함. 5. **유지보수 (Maintenance):** 버그 패치 및 기능 개선. |
| **2. 지원 생명주기** *(Supporting Process)*     | 기본 프로세스가 성공적으로 완료될 수 있도록 **측면에서 지원하고, 품질을 통제/감시하는 '스태프'들의 보조 프로세스.**       | 1. **형상 관리 (Configuration Mgt):** 소스 버전 통제. 2. **품질 보증 (QA):** 제품이 품질 요구를 만족하는지 보증. 3. **검증 및 확인 (V\&V):** 올바르게 만들어졌는지 테스트. 4. 문서화, 합동 검토, 감사(Audit), 문제 해결.                                             |
| **3. 조직 생명주기** *(Organizational Process)* | 특정 프로젝트 하나에 국한되지 않고, 회사(조직) 차원에서 **지속적인 비즈니스 수행을 위해 기반 환경을 구축하는 프로세스.**    | 1. **관리 (Management):** 프로젝트 관리 및 자원 통제. 2. **인프라스트럭처 (Infrastructure):** H/W, S/W 환경 제공. 3. **훈련 (Training):** 개발자 및 직원 교육. 4. 프로세스 개선 (Improvement).                                                   |

#### **IV. \[결론/제언] CMMI 및 SPICE(ISO 15504) 품질 심사 모델로의 연결고리**

* **(키워드 위주 2줄 마무리)** "ISO 12207은 단순히 프로세스의 '목록'을 나열한 참조 모델에 불과합니다. 따라서 기업이 이 12207 프로세스를 얼마나 성숙하게 잘 수행하고 있는지를 1~5단계로 채점하고 평가하기 위해 등장한 심사 모델이 바로 그 유명한 **SPICE(ISO 15504)와 CMMI**이며, 12207은 이 위대한 품질 인증 심사들의 가장 근본적인 뼈대 역할을 수행하고 있습니다."
