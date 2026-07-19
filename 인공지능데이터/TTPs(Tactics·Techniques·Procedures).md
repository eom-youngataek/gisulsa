### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (정의, 3단계추상화의목적) — 3~4줄
Ⅱ. TTPs 3단계구조 (본론①, 도식 1개 필수)
Ⅲ. MITRE ATT&CK과의연결및오늘시리즈총정리, 핵심 배점
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서다룬랜섬웨어,BPFDoor,미라이봇넷,측면이동은각각다른악성코드이름이었는데, 방어자입장에서는 '악성코드이름'보다 '공격자가어떤전략으로,어떤기술로,구체적으로어떤절차를밟는지'가 훨씬중요하다 — 새악성코드는계속나오지만, 공격의근본전략(TTPs)은 재사용된다"\*\*는 한줄로시작하면, 왜 이답안이 오늘의보안시리즈전체를 아우르는 \*\*"공통분류체계"\*\*인지드러납니다.

### Ⅱ. TTPs 3단계구조 — 추상화의피라미드

| 단계                 | 추상화수준          | 질문                         |
| :----------------- | :------------- | :------------------------- |
| **전술**(Tactics)    | **가장추상적**(왜)   | "공격자가 **지금달성하려는목표**가무엇인가?" |
| **기법**(Techniques) | **중간**(어떻게)    | 그목표를 **어떤방법으로**달성하는가?      |
| **절차**(Procedures) | **가장구체적**(무엇을) | 그기법을 **실제로어떤순서·도구**로실행하는가? |

→ 암기: **"전술은목표(초기접근하기),기법은방법(피싱메일보내기),절차는실행디테일(특정첨부파일이름,특정C2서버주소)"** — 앞서다룬 \*\*"측면이동"\*\*답안에서 다룬 **PassTheHash**를 이피라미드에넣으면: **전술=측면이동자체**,**기법=PassTheHash**,**절차=구체적으로어떤도구(Mimikatz등)로,어떤해시값을** 사용했는지입니다.

### 도식화 제안

```
[TTPs 3단계 피라미드]
        [전술(Tactics)] ← 가장추상적,안정적
        "왜?" 예: 초기접근,측면이동,자격증명접근
              ↓
        [기법(Techniques)]
        "어떻게?" 예: 피싱,PassTheHash(앞서다룬그것)
              ↓
        [절차(Procedures)] ← 가장구체적,자주바뀜
        "무엇을?" 예: 특정악성첨부파일명,특정도구(Mimikatz)

← 위로갈수록 오래유지되고,아래로갈수록 매번달라짐 →
```

### Ⅲ. MITRE ATT\&CK과의연결 및 오늘시리즈총정리 — 핵심 배점

**함정 방지: "추상화단계가있다"고만답하면절반. 앞서다룬여러공격을실제로 이피라미드에분류해보고, 왜"전술"이가장중요한방어포인트인지보여줘야완성됩니다.**

**MITRE ATT\&CK 프레임워크**(TTPs의실제표준화): 전세계보안업계가 공유하는 \*\*"전술14개카테고리(초기접근,실행,지속성,권한상승,방어우회,자격증명접근,탐색,측면이동,수집,명령제어,유출,영향등)"\*\*로 TTPs를 **표준분류**합니다.

**오늘하루다룬공격들을TTP로재분류**

| 오늘답안                    | 전술(Tactics)    | 기법(Techniques)     |
| :---------------------- | :------------- | :----------------- |
| **BPFDoor**             | 방어우회,지속성       | 은닉기법(프로세스위장,메모리실행) |
| **측면이동(Pass-the-Hash)** | 측면이동,자격증명접근    | PtH,PtT            |
| **랜섬웨어**                | 영향(Impact)     | 파일암호화              |
| **프롬프트인젝션**             | 초기접근/실행(LLM맥락) | 직접/간접인젝션           |

→ **왜"전술"이핵심방어포인트인가**(핵심통찰): 앞서다룬 \*\*"살충제패러독스"\*\*처럼, \*\*"절차(구체적도구·파일명)"\*\*는 공격자가 **매번쉽게바꿀수있어** 시그니처기반탐지가 금방무력화됩니다 — 하지만 \*\*"전술(측면이동해야한다,자격증명을훔쳐야한다)"\*\*은 공격자가 **목표를달성하려면 반드시거쳐야하는 근본적단계**라 **바꾸기어렵습니다** — 그래서 앞서다룬 \*\*"UEBA(행동기반이상탐지)"\*\*는 \*\*"절차의세부사항"\*\*이아니라 \*\*"전술수준의이상행동패턴"\*\*을 탐지하는것이 훨씬효과적입니다.

### 도식화 제안

```
[방어관점에서 "전술"이 가장강력한이유]

[절차수준탐지] "이파일명,이C2주소를차단" 
     ↓ 공격자가 파일명·주소만바꾸면
     즉시무력화(앞서다룬살충제패러독스)

[전술수준탐지] "자격증명접근시도자체,측면이동패턴자체"를 탐지
     ↓ 공격자가 절차를아무리바꿔도
     전술(목표)자체는 바꿀수없어 지속적으로탐지가능
     (앞서다룬 UEBA의행동기반탐지가 여기해당)
```

### Ⅳ. 결론

TTPs는 \*\*"오늘하루다룬랜섬웨어,BPFDoor,미라이,측면이동같은 개별악성코드·공격사례를,전술(왜)→기법(어떻게)→절차(무엇을)라는 3단계공통언어로분류"\*\*하는 프레임워크이며, **MITREATT\&CK**이 이를 **업계표준으로체계화**했습니다 — 핵심교훈은 \*\*"절차(구체적도구,파일명)는공격자가쉽게바꿀수있어시그니처기반탐지가금방무력화되지만, 전술(측면이동,자격증명접근같은근본목표)은 바꾸기어려워 UEBA같은행동기반탐지가훨씬효과적"\*\*이라는 것입니다 — 이는 앞서다룬 \*\*"살충제패러독스(고정된탐지방식의무력화),UEBA(행동패턴탐지)"\*\*의 교훈을, \*\*"공격자체를분류하는프레임워크수준"\*\*에서 재확인시켜주며, 오늘하루다룬 방대한사이버공격시리즈전체(랜섬웨어→BPFDoor→미라이→측면이동→적대적공격→ModelDoS→TTPs)가 \*\*"개별공격사례를넘어, 공격자의행동패턴자체를이해해야 진짜효과적인방어가가능하다"\*\*는 궁극의결론으로 완결됩니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "특정 해커 집단(APT 그룹 등)의 공격 습성과 행동 지문을 데이터베이스화하는 최첨단 사이버 위협 인텔리전스(CTI)의 코어 개념이다. 해커가 침투할 때 쓰는 전술(Tactics), 기술(Techniques), 행동 절차(Procedures)의 앞 글자를 땄다. \*\*'전술(T)'\*\*은 초기 침투 등 해킹 목표다. \*\*'기술(T)'\*\*은 피싱 메일 전송 등 목표 달성 수단이다. \*\*'절차(P)'\*\*는 공격 툴 사용법 같은 세부 시나리오다. 핵심 출제 포인트는 \*\*'고통의 피라미드(Pyramid of Pain)'\*\*이다. 해커의 IP나 악성코드 파일 해시값은 해커가 1초 만에 바꿀 수 있어 차단해 봤자 소용없다. 하지만 해커 고유의 공격 뼈대인 'TTPs'를 간파해 방어망을 치면, 해커는 침투 시나리오를 처음부터 새로 공부하고 설계해야 하므로 극단적인 피로감(고통의 꼭대기)을 주어 해킹을 포기하게 만든다. 이 TTPs를 바둑판처럼 매핑해 둔 표준 사전이 바로 \*\*'MITRE ATT\&CK'\*\*이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 해커의 행동 패턴을 프로파일링하는 CTI의 정수, TTPs 개요**

* **정의:** 사이버 위협 행위자(APT 그룹 등)가 표적 시스템을 공격할 때 사용하는 전술(Tactics), 기술(Techniques), 그리고 구체적인 절차(Procedures)의 결합체로 정의되는 위협 프로파일링 데이터.
* **목적:** 단순히 단발성 침입 지표(IoC: IP, 파일 해시) 차단 위주의 소극적 보안을 탈피하고, 해커 고유의 행동 특징과 시나리오를 예측하여 선제적 방어 체계(Proactive Defense)를 구축하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 전술에서 절차로 이어지는 공격 구조화**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMDIuMTUgMzgwLjUiIHdpZHRoPSIzMDIuMTUiIGhlaWdodD0iMzgwLjUiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IlRUUHNfM19fXyIgZGF0YS1sYWJlbD0iVFRQc+ydmCAz64uo6rOEIOqwnOuFkOyggSDsiJjsp4Eg6rWs7KGwIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIyMjIuMTQ5OTk5OTk5OTk5OTgiIGhlaWdodD0iMzAwLjUiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIyMjIuMTQ5OTk5OTk5OTk5OTgiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5UVFBz7J2YIDPri6jqs4Qg6rCc64WQ7KCBIOyImOyngSDqtazsobA8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlQxIiBkYXRhLXRvPSJUMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxNTEuMDc1LDE1NC43IDE1MS4wNzUsMjAyLjciIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlQyIiBkYXRhLXRvPSJQIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE1MS4wNzUsMjM5LjYwMDAwMDAwMDAwMDAyIDE1MS4wNzUsMjg3LjYiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlQxIiBkYXRhLWxhYmVsPSLwn5KhIDEuIOyghOyIoCAoVGFjdGljcykg8J+SoQrqs7XqsqnsnZgg7LWc7KKFICfrqqntkZwnIOygleydmArsmIg6IOuCtOu2gCDsoITtjIwsIOy0iOq4sCDsuajtiKwiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMTkwLjE0OTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTUxLjA3NSIgeT0iMTE5LjM1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNTEuMDc1IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+8J+SoSAxLiDsoITsiKAgKFRhY3RpY3MpIPCfkqE8L3RzcGFuPjx0c3BhbiB4PSIxNTEuMDc1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7qs7XqsqnsnZgg7LWc7KKFICYjMzk766qp7ZGcJiMzOTsg7KCV7J2YPC90c3Bhbj48dHNwYW4geD0iMTUxLjA3NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7JiIOiDrgrTrtoAg7KCE7YyMLCDstIjquLAg7Lmo7YisPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlQyIiBkYXRhLWxhYmVsPSJUMiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMjEuMDc0OTk5OTk5OTk5OTkiIHk9IjIwMi43IiB3aWR0aD0iNjAiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTUxLjA3NSIgeT0iMjIxLjE0OTk5OTk5OTk5OTk4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5UMjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUCIgZGF0YS1sYWJlbD0iUCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMjEuMDc0OTk5OTk5OTk5OTkiIHk9IjI4Ny42IiB3aWR0aD0iNjAiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTUxLjA3NSIgeT0iMzA2LjA1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5QPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] TTPs 구조 및 고통의 피라미드(Pyramid of Pain) 전격 해부 (3단 표)**

이 토픽은 해커에게 최강의 타격을 주는 지표인 **'고통의 피라미드(Pyramid of Pain)'** 구조를 그리고, 글로벌 위협 맵인 **'MITRE ATT\&CK'** 프레임워크와의 연계성을 정확히 서술하는 것이 정답의 차별성을 가져다줍니다.

| **핵심 척도**                | **📊 TTPs 3대 핵심 구성 🚨**                                                                                                                                                                    | **🔑 고통의 피라미드 (Pyramid of Pain) 💯**                                                                                                                                      | **💼 위협 인텔리전스 (MITRE ATT\&CK) 💯**                                                                                                      |
| :----------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **개념 / 필요성**             | **'공격자의 행동 양식'.** 단일 보안 로그 분석을 넘어, 해커가 목표 탈취를 위해 밟아가는 논리적 흐름과 단계들을 도식화함.                                                                                                                   | **'침입 지표별 방어 효율성'.** 해킹 탐지/차단 시 해커가 이를 우회하기 위해 겪어야 하는 고통과 비용의 깊이를 등급화한 모델.                                                                                                | **'공동 해커 지식 사전'.** 전 세계 APT 공격 그룹의 기 구축된 TTPs 사례들을 집대성한 글로벌 사실상 표준(De Facto) 프레임워크.                                                     |
| **세부 구성 요건 (출제 포인트) 🚨** | **\[Tactics (전술) 💯]** 공격의 중간 목표 (예: Privilege Escalation). **\[Techniques (기술) 🚨]** 전술을 실행하기 위한 기술적 기법 (예: OS Credential Dumping). **\[Procedures (절차)]** 실제 구동 툴 및 순서 (예: Mimikatz 실행). | **\[피라미드 최하단: 쉬운 차단]** Hash 값, IP 주소, 도메인 차단 (해커는 툴 컴파일 한 번으로 우회 가능. 해커 고통 무색). **\[피라미드 최상단: 극심한 고통 💯]** **'TTPs 차단'.** 해커 고유의 공격 습관과 설계 방법론을 원천 차단하여 **우회에 수개월이 소요됨.** | **\[MITRE ATT\&CK 매트릭스 💯]** 실제 14개의 전술(Tactics)과 수백 개의 기술(Techniques) 바둑판 매트릭스를 구성하여, 우리 기업의 보안 탐지 룰셋(SIEM/SOAR) 커버리지를 점검하는 표준 맵으로 활용. |

#### **IV. \[결론/제언] 사이버 위협 인텔리전스(CTI) 플랫폼과 STIX/TAXII의 융합**

* **(키워드 위주 2줄 마무리)** "TTPs 기반 보안을 선제적으로 구현하기 위해서는 사내 탐지에만 머무르지 않고, 타사/글로벌 기관과 위협 정보를 실시간 자동 공유해야 합니다. 이를 위해 위협 표현 포맷인 **'STIX'** 표준 규격과, 정보 전송 프로토콜인 **'TAXII'** 인터페이스를 사내 보안 운영(SOAR) 시스템에 통합하여 실시간 능동 방어 생태계를 구축해야 합니다."
