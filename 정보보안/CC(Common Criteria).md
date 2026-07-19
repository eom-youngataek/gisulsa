### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (CC정의,등장배경-각국평가기준의통일) — 3~4줄
Ⅱ. CC 3대구성체계 (본론①, 도식 1개 필수)
Ⅲ. EAL등급및PP/ST (본론②, 핵심 배점)
Ⅳ. 오늘시리즈와의연결
Ⅴ. 결론
```

포인트: 개요에서 \*\*"1994년미국·캐나다·영국·독일·프랑스·네덜란드등이, 각자다른보안평가기준(미국TCSEC,유럽ITSEC,캐나다CTCPEC)을 따로쓰다보니 국가간상호인정이안되는문제가있었다 → 이를하나로통일해ISO/IEC15408로표준화한것이CC — 'CC로한번평가받으면, 여러나라에서똑같이인정받는다'는게핵심가치"\*\*라는한줄로시작하면, 왜 "공통(Common)"이라는이름이붙었는지 논리가섭니다.

### Ⅱ. CC 3대구성체계

| Part      | 명칭                | 내용                               |
| :-------- | :---------------- | :------------------------------- |
| **Part1** | 소개및일반모델           | CC의 **구성요소,활용방법**(PP,ST개념) 소개    |
| **Part2** | **보안기능요구사항**(SFR) | 제품이 갖춰야할 **구체적보안기능**(암호화,접근통제등)  |
| **Part3** | **보안보증요구사항**(SAR) | 그기능이 **얼마나신뢰성있게구현·검증됐는지**에대한요구사항 |

→ 암기: **"소개하고,기능을정하고,그기능을얼마나믿을수있는지검증기준을정한다"** — 앞서다룬 \*\*"ISO/IEC25010(품질특성)"\*\*이 소프트웨어전반의품질을다뤘다면, CC는 \*\*"보안기능"\*\*이라는 **한영역에특화**된 유사한체계를갖고있다는 연결이핵심입니다.

### 도식화 제안

```
[CC 3대Part]
Part1: 소개/일반모델 (PP,ST 개념)
   ↓
Part2: 보안기능요구사항(SFR) ← "무엇을할수있어야하는가"
   ↓
Part3: 보안보증요구사항(SAR) ← "그것을얼마나확실하게보증하는가"
```

### Ⅲ. EAL등급 및 PP/ST — 핵심 배점

**함정 방지: "등급이있다"고만답하면절반. PP/ST가무엇이고, 왜필요한지의구조를보여줘야완성됩니다.**

| 개념                                | 내용                                                         |
| :-------------------------------- | :--------------------------------------------------------- |
| **PP**(ProtectionProfile,보호프로파일)  | 특정제품군(예:방화벽)이 **일반적으로갖춰야할보안요구사항**을 **소비자/사용자관점**에서정의한문서    |
| **ST**(SecurityTarget,보안목표명세서)    | 특정제조사의 **실제제품**이 **PP의요구사항을어떻게구현했는지**를 **공급자관점**에서명세한문서    |
| **EAL**(EvaluationAssuranceLevel) | 보증등급 — **EAL1(최저)\~EAL7(최고)** — 등급이높을수록 **더엄격한검증절차와제출물**요구 |

→ 암기: **"PP는소비자가'이런제품이면좋겠다'는요구사항목록, ST는공급자가'우리제품은이렇게만족시켰다'는답변서, EAL은그답변을얼마나엄격하게검증했는지"** — 앞서다룬 \*\*"요구사항명세서(SRS)와인수기준"\*\*의 관계와 유사한구조가, 여기서는 **소비자요구(PP)↔공급자구현(ST)** 형태로재현됩니다.

**등급별평가제출물차이**: EAL등급이 올라갈수록 **제출해야할문서·증거의양과깊이**가 급증합니다 — 예를들어 EAL2/3/4는 각각 요구되는 **소스코드분석범위,침투테스트강도**가 다릅니다.

### 도식화 제안

```
[PP: 소비자요구사항]  "방화벽은 이런보안기능이필요하다"
        ↓
[ST: 공급자구현명세]  "우리회사방화벽은 이렇게구현했다"
        ↓
[평가기관검증] → [EAL등급부여] (EAL1~EAL7)
        
EAL1 ─ EAL2 ─ EAL3 ─ EAL4 ─ EAL5 ─ EAL6 ─ EAL7
(검증강도·제출물요구량이 오른쪽으로갈수록기하급수적으로증가)
```

### Ⅳ. 오늘시리즈와의연결

**함정 방지: CC를독립된주제로만끝내면절반. 오늘다룬여러보안기법이 실제로CC평가대상이된다는걸보여줘야완성됩니다.**

| 오늘다룬기술                 | CC평가와의연결                                                    |
| :--------------------- | :---------------------------------------------------------- |
| **대칭/비대칭암호,PQC**       | 암호모듈제품이 **CC평가대상**의핵심(Part2의보안기능요구사항에 암호기능포함)               |
| **접근통제(MAC/DAC/RBAC)** | 방화벽,IAM솔루션등이 CC평가시 **접근통제기능(SFR)로검증**됨                      |
| **GS인증**(앞서다룬)         | 정보보호제품의경우, **GS인증시CC/보안기능확인서보유시 보안성평가면제** — 두인증제도가 **상호연계** |

→ 앞서다룬 \*\*"상용SW직접구매/GS인증"\*\*답안에서 \*\*"CC인증,보안기능확인서를획득한경우 GS인증시보안성평가면제"\*\*라는 실제제도적연결이 있었다는게, CC가단순히독립된인증이아니라 **오늘다룬여러공공보안제도와 서로맞물려있다**는 점을보여줍니다.

### Ⅴ. 결론 포인트 (암호·보안 시리즈 최종대단원)

CC는 \*\*"각국이따로쓰던보안평가기준을 하나로통일해, 한번평가받으면여러국가에서상호인정받도록만든 국제표준"\*\*이며, \*\*PP(소비자요구)-ST(공급자구현)-EAL(검증강도등급)\*\*이라는 체계로 \*\*"이보안제품이정말안전한지"\*\*를 객관적으로증명합니다 — 이는 앞서다룬 \*\*ISMS-P(조직의보안운영검증),GS인증(SW품질검증)\*\*과 함께 **"기술-제품-조직"** 3층위의보안검증체계를 완성하는 마지막조각이며, 오늘하루다룬 방대한 대칭/비대칭암호→동형암호→PQC/QKD→해시함수→접근통제모델→식별인증→제로트러스트→CC로이어지는 암호·보안시리즈전체가, \*\*"이론적암호기술에서시작해, 그기술이실제제품으로,조직운영으로,국제적신뢰체계로확장되는 완전한보안생태계"\*\*로 마무리됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "과거 방화벽 제조사들은 피눈물을 흘렸다. 한국에서 국가 인증을 받아도, 미국에 수출하려면 미국의 TCSEC 인증을 받아야 했고, 유럽에 수출하려면 ITSEC 인증을 또 받아야 했다. 이 미친 중복 규제를 타파하기 위해 전 세계 국가들이 모여 '앞으로 정보보호 제품의 평가는 이 기준 하나로만 통일하고, 서로 인정해 주자(CCRA)!'라고 대통합을 이뤄낸 국제 표준(ISO 15408)이 바로 \*\*'CC(Common Criteria, 공통평가기준)'\*\*다. 이 CC 인증의 심장에는 서로 문서를 주고받는 3명의 주인공이 있다. 첫 번째는 '사용자(고객)'다. 국방부 같은 기관은 제품을 사기 전에 '우리가 쓸 방화벽은 무조건 이런 보안 기능이 있어야 해'라며 '구현 방식'은 묻지 않고 기능만 적어 놓은 요구사항 문서인 \*\*'PP(보호프로파일)'\*\*를 허공에 던진다. 두 번째 주인공은 '제조사(개발자)'다. 안랩이나 시스코 같은 제조사는 고객의 PP를 보고 '우리가 개발한 이 특정 방화벽 모델(제품)은 당신의 PP 요구사항을 이렇게 완벽히 구현했습니다'라는 방어 답변서인 \*\*'ST(보안목표명세서)'\*\*를 평가기관에 제출한다. 세 번째 주인공은 바로 책상 위에 올려져 평가를 받는 그 방화벽 제품 자체, \*\*'TOE(평가대상)'\*\*다. 이 TOE 제품이 얼마나 빡세게 검증받았는지를 나타내는 성적표가 \*\*'EAL(평가보증등급)'\*\*이다. 1등급부터 7등급까지 있는데, 등급이 높다고 '방화벽 기능이 많다'는 뜻이 절대 아니다. '소스코드부터 취약점까지 얼마나 현미경으로 꼼꼼히 뜯어봤느냐(보증 신뢰도)'를 뜻한다. 상업용 제품은 보통 4등급(EAL4)을 받고, 국방용 최고 기밀 장비는 수학적 증명까지 거친 7등급(EAL7)을 받는다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 파편화된 규제를 통합한 글로벌 헌법, CC(공통평가기준) 개요**

* **정의:** 국가마다 서로 다르던 정보보호 시스템(방화벽, 백신, DB보안 등)의 평가 기준을 국제적으로 연동하고 통일하기 위해 제정된 **'정보보호 제품 평가를 위한 국제 공통 표준 (ISO/IEC 15408)'**.
* **CCRA (상호인정협정):** CC 인증을 획득한 제품은 협정에 가입된 다른 국가들(한국, 미국, 영국 등)에서도 동일하게 보안성을 인정받아 별도의 추가 인증 없이 수출 및 납품이 가능한 체계.

#### **II. \[본론 1] 고객의 요구(PP)와 제조사의 답변(ST) 검증 파이프라인 (도식화)**

사용자의 요구사항 문서를 개발자가 어떻게 받아내서 제품으로 연결하는지 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxOTgzLjMxNzAwMDAwMDAwMDIgNDgwLjkyMjUiIHdpZHRoPSIxOTgzLjMxNzAwMDAwMDAwMDIiIGhlaWdodD0iNDgwLjkyMjUiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IkNDQ29tbW9uX0NyaXRlcmlhX18zX19fIiBkYXRhLWxhYmVsPSJDQyhDb21tb24gQ3JpdGVyaWEpIOyduOymnSAz64yAIO2VteyLrCDsmpTshozsnZgg7IOB7Zi47J6R7JqpIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIxOTAzLjMxNzAwMDAwMDAwMDIiIGhlaWdodD0iNDAwLjkyMjUiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIxOTAzLjMxNzAwMDAwMDAwMDIiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5DQyhDb21tb24gQ3JpdGVyaWEpIOyduOymnSAz64yAIO2VteyLrCDsmpTshozsnZgg7IOB7Zi47J6R7JqpPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJVIiBkYXRhLXRvPSJQUCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7JqU6rWs7IKs7ZWtIOuqheyEuCIgcG9pbnRzPSIyMzQuMjkzOTk5OTk5OTk5OTgsMzIyLjk5ODc1IDQxMy4wMDYsMzIyLjk5ODc1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJQUCIgZGF0YS10bz0iU1QiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuqzoOqwnSDsmpTqtawg7KGw6rG0IOyImOyaqSIgcG9pbnRzPSI2MTIuMzM2LDMyMi45OTg3NSA4MDYuMTMyMDAwMDAwMDAwMSwzMjUuMjU3NSA4MDYuMTMyMDAwMDAwMDAwMSwyODMuNjY2NjY2NjY2NjY2NjMgODc3LjgyMzY2NjY2NjY2NjcsMjgzLjY2NjY2NjY2NjY2NjYzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJWIiBkYXRhLXRvPSJTVCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7Jqw66as6rCAIOq1rO2YhO2VnCDsiqTtjpkg7J6R7ISxIiBwb2ludHM9IjYxMi4zMzYsMTcwLjY5MjUgODA2LjEzMjAwMDAwMDAwMDEsMTcwLjY5MjUgODA2LjEzMjAwMDAwMDAwMDEsMjEyLjI4MzMzMzMzMzMzMzMzIDg3Ny44MjM2NjY2NjY2NjY4LDIxMi4yODMzMzMzMzMzMzMzMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iU1QiIGRhdGEtdG89IlRPRSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7J20IOusuOyEnOuMgOuhnCDrp4zrk6TslrTsp5AiIHBvaW50cz0iMTA1NC4wMjMyNTAwMDAwMDAyLDI1MC4yMzM3NTAwMDAwMDAwMSAxMjcyLjQxNjAwMDAwMDAwMDIsMjUwLjIzMzc1MDAwMDAwMDAxIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJUT0UiIGRhdGEtdG89IkVBTCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7J247KadIOq4sOq0gCDsi6zsgqwiIHBvaW50cz0iMTUxNS45MTgwMDAwMDAwMDAxLDI1MC4yMzM3NTAwMDAwMDAwMSAxNjk2LjQxMjAwMDAwMDAwMDMsMjQ3Ljk3NDk5OTk5OTk5OTk3IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlUiIGRhdGEtdG89IlBQIiBkYXRhLWxhYmVsPSLsmpTqtazsgqztla0g66qF7IS4Ij4KICA8cmVjdCB4PSIyNzguMjk0IiB5PSIzMDkuMjU3NSIgd2lkdGg9IjkwLjcxMjAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzIzLjY1IiB5PSIzMjQuNDA3NDk5OTk5OTk5OTciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuyalOq1rOyCrO2VrSDrqoXshLg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iUFAiIGRhdGEtdG89IlNUIiBkYXRhLWxhYmVsPSLqs6DqsJ0g7JqU6rWsIOyhsOqxtCDsiJjsmqkiPgogIDxyZWN0IHg9IjY2OC4yMTYiIHk9IjMwOS4yNTc1IiB3aWR0aD0iMTE4LjAzNjAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNzI3LjIzNCIgeT0iMzI0LjQwNzQ5OTk5OTk5OTk3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7qs6DqsJ0g7JqU6rWsIOyhsOqxtCDsiJjsmqk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iViIgZGF0YS10bz0iU1QiIGRhdGEtbGFiZWw9IuyasOumrOqwgCDqtaztmITtlZwg7Iqk7Y6ZIOyekeyEsSI+CiAgPHJlY3QgeD0iNjU2LjMzNiIgeT0iMTU0LjY5MjUiIHdpZHRoPSIxNDEuNzk2MDAwMDAwMDAwMDUiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI3MjcuMjM0IiB5PSIxNjkuODQyNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7Jqw66as6rCAIOq1rO2YhO2VnCDsiqTtjpkg7J6R7ISxPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlNUIiBkYXRhLXRvPSJUT0UiIGRhdGEtbGFiZWw9IuydtCDrrLjshJzrjIDroZwg66eM65Ok7Ja07KeQIj4KICA8cmVjdCB4PSIxMTAwLjI4MjAwMDAwMDAwMDIiIHk9IjIzMS45NzUiIHdpZHRoPSIxMjguMTM0MDAwMDAwMDAwMDEiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxMTY0LjM0OTAwMDAwMDAwMDIiIHk9IjI0Ny4xMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuydtCDrrLjshJzrjIDroZwg66eM65Ok7Ja07KeQPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlRPRSIgZGF0YS10bz0iRUFMIiBkYXRhLWxhYmVsPSLsnbjspp0g6riw6rSAIOyLrOyCrCI+CiAgPHJlY3QgeD0iMTU1OS45MTgwMDAwMDAwMDAxIiB5PSIyMzEuOTc1IiB3aWR0aD0iOTIuNDk0MDAwMDAwMDAwMDMiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxNjA2LjE2NTAwMDAwMDAwMDIiIHk9IjI0Ny4xMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuyduOymnSDquLDqtIAg7Ius7IKsPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJVIiBkYXRhLWxhYmVsPSLsgqzsmqnsnpAgLyDrsJzso7zsspgg8J+nkeKAjfCfkrwK6rWt67Cp67aALCDqs7Xqs7XquLDqtIAg65OxIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIyOTguMzU3NDk5OTk5OTk5OTYiIHdpZHRoPSIxNzguMjkzOTk5OTk5OTk5OTgiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNDUuMTQ3IiB5PSIzMjUuMjU3NDk5OTk5OTk5OTQiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE0NS4xNDciIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7sgqzsmqnsnpAgLyDrsJzso7zsspgg8J+nkeKAjfCfkrw8L3RzcGFuPjx0c3BhbiB4PSIxNDUuMTQ3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7qta3rsKnrtoAsIOqzteqzteq4sOq0gCDrk7E8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUFAiIGRhdGEtbGFiZWw9IlBQICjrs7TtmLjtlITroZztjIzsnbwpIPCfk4QKUHJvdGVjdGlvbiBQcm9maWxlIiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjUxMi42NzA5OTk5OTk5OTk5LDIyMy4zMzM3NDk5OTk5OTk5OCA2MTIuMzM1OTk5OTk5OTk5OSwzMjIuOTk4NzUgNTEyLjY3MDk5OTk5OTk5OTksNDIyLjY2Mzc0OTk5OTk5OTk0IDQxMy4wMDYsMzIyLjk5ODc1IiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjUxMi42NzA5OTk5OTk5OTk5IiB5PSIzMjIuOTk4NzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjUxMi42NzA5OTk5OTk5OTk5IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+UFAgKOuztO2YuO2UhOuhnO2MjOydvCkg8J+ThDwvdHNwYW4+PHRzcGFuIHg9IjUxMi42NzA5OTk5OTk5OTk5IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5Qcm90ZWN0aW9uIFByb2ZpbGU8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU1QiIGRhdGEtbGFiZWw9IlNUICjrs7TslYjrqqntkZzrqoXshLjshJwpIPCfk50KU2VjdXJpdHkgVGFyZ2V0IiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9Ijk0OS4yMDcwMDAwMDAwMDAxLDE0MC45IDEwNTYuMjgyMDAwMDAwMDAwMiwyNDcuOTc1IDk0OS4yMDcwMDAwMDAwMDAxLDM1NS4wNDk5OTk5OTk5OTk5NSA4NDIuMTMyMDAwMDAwMDAwMSwyNDcuOTc1IiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9Ijk0OS4yMDcwMDAwMDAwMDAxIiB5PSIyNDcuOTc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI5NDkuMjA3MDAwMDAwMDAwMSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPlNUICjrs7TslYjrqqntkZzrqoXshLjshJwpIPCfk508L3RzcGFuPjx0c3BhbiB4PSI5NDkuMjA3MDAwMDAwMDAwMSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+U2VjdXJpdHkgVGFyZ2V0PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlYiIGRhdGEtbGFiZWw9IuqwnOuwnOyekCAvIOygnOyhsOyCrCDwn6eR4oCN8J+SuwrrsKntmZTrsr0g7KCc7KGwIOuypOuNlCDrk7EiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDM0LjA0MiIgeT0iMTQzLjc5MjUiIHdpZHRoPSIxNzguMjkzOTk5OTk5OTk5OTgiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1MjMuMTg5IiB5PSIxNzAuNjkyNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNTIzLjE4OSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuqwnOuwnOyekCAvIOygnOyhsOyCrCDwn6eR4oCN8J+SuzwvdHNwYW4+PHRzcGFuIHg9IjUyMy4xODkiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuuwqe2ZlOuyvSDsoJzsobAg67Kk642UIOuTsTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJUT0UiIGRhdGEtbGFiZWw9IlRPRSAo7Y+J6rCA64yA7IOBKSDwn5OmCu2PieqwgOuwm+uKlCDsoJXrs7Trs7TtmLgg7KCc7ZKIIOq3uCDsnpDssrQiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTI3Mi40MTYwMDAwMDAwMDAyIiB5PSIyMjMuMzMzNzUiIHdpZHRoPSIyNDMuNTAxOTk5OTk5OTk5OTgiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTM5NC4xNjcwMDAwMDAwMDAxIiB5PSIyNTAuMjMzNzUwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjEzOTQuMTY3MDAwMDAwMDAwMSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPlRPRSAo7Y+J6rCA64yA7IOBKSDwn5OmPC90c3Bhbj48dHNwYW4geD0iMTM5NC4xNjcwMDAwMDAwMDAxIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7tj4nqsIDrsJvripQg7KCV67O067O07Zi4IOygnO2SiCDqt7gg7J6Q7LK0PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkVBTCIgZGF0YS1sYWJlbD0i7LWc7KKFIOyEseygge2RnDogRUFMIOuTseq4iSDrtoDsl6wg8J+PhiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxNjk2LjQxMjAwMDAwMDAwMDMiIHk9IjIyOS41MjQ5OTk5OTk5OTk5OCIgd2lkdGg9IjIzMC45MDQ5OTk5OTk5OTk5NyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2YzZTVmNSIgc3Ryb2tlPSIjOGUyNGFhIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTgxMS44NjQ1MDAwMDAwMDAxIiB5PSIyNDcuOTc0OTk5OTk5OTk5OTciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuy1nOyihSDshLHsoIHtkZw6IEVBTCDrk7HquIkg67aA7JesIPCfj4Y8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik5vdGUiIGRhdGEtbGFiZWw9Ik5vdGUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iNjguNjI2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iOTAuMzEzIiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk5vdGU8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] CC 인증의 3대 핵심 구성 요소 전격 해부 (3단 표 - 출제 1순위)**

PP와 ST가 작성되는 \*\*'관점(사용자 vs 개발자)'\*\*과 \*\*'제품 종속성 여부'\*\*를 날카롭게 대조해야 합니다.

| **3대 구성 요소**                                 | **관점 및 역할의 본질 (What & Who)**                                                                                             | **구현 및 제품 종속성 특징**                                                                        |
| :------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| **1. 보호프로파일** **PP** *(Protection Profile)*  | **\[사용자 및 고객 집단 관점의 요구사항]** 소비자가 자신이 도입할 정보보호 제품에 대해 "이러이러한 보안 기능과 보증 요건이 필요하다"라고 모아놓은 **'구현 독립적'인 요구사항 묶음서.**           | 특정 회사의 제품에 **'종속되지 않음' (구현 독립적).** 예: "우리 공공기관에 들어올 방화벽은 이런 수준이어야 함" (어느 회사 제품인지는 아직 모름). |
| **2. 보안목표명세서** **ST** *(Security Target)*    | **\[개발자 및 제조사 벤더 관점의 답변서]** 고객이 제시한 PP를 기반으로, 개발자가 "우리가 개발한 이 방화벽 제품은 PP의 요구사항을 어떻게 충족하고 구현했는지"를 구체적으로 명시한 **'스펙 정의서'**. | 평가를 받는 특정 제조사의 특정 제품 모델에 **'완벽하게 종속됨' (구현 종속적).** ST 문서를 기준으로 실제 제품이 제대로 만들어졌는지 평가함.      |
| **3. 평가대상** **TOE** *(Target of Evaluation)* | **\[평가 기관의 실제 도마 위에 오르는 타겟]** ST에 명시된 내용대로 작동하는지 시험기관(KISA 등)에 제출되어 **실제로 평가를 받는 정보보호 '제품 또는 시스템' 그 자체.**                | H/W 펌웨어 칩셋일 수도 있고, S/W 프로그램일 수도 있음. CC 인증의 최종 심사 대상물.                                     |

#### **IV. \[결론/제언] 기능이 아닌 '신뢰도'를 묻는 EAL 7단계와 클라우드 CC 대응**

* **(키워드 위주 2줄 마무리)** "CC 인증의 EAL(Evaluation Assurance Level) 등급은 숫자가 높다고 보안 기능이 화려한 것이 아니라, **EAL1(기능 테스트)부터 EAL4(취약점/소스코드 분석), EAL7(수학적 정형 증명)에 이르기까지 제조사의 주장을 '얼마나 치밀하게 뜯어보고 검증(보증)했는가'를 나타내는 신뢰도의 척도**입니다. 최근에는 전통적인 어플라이언스(장비)를 넘어 SECaaS 등 클라우드 보안 제품으로까지 CC 평가 체계가 진화하고 있습니다."
