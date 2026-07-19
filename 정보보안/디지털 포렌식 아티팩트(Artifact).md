### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (아티팩트정의, 앞서다룬포렌식시리즈와의연결) — 3~4줄
Ⅱ. OS 레벨 아티팩트 4대유형 (본론①, 도식 1개 필수)
Ⅲ. 애플리케이션·네트워크아티팩트 (본론②, 핵심 배점)
Ⅳ. 오늘시리즈총연결 - 안티포렌식과의공방
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬파일카빙은'삭제된파일본체'를,파일슬랙은'클러스터의여백'을다뤘는데,아티팩트는더넓은개념 — OS와프로그램이 정상적으로동작하는과정에서 '의도치않게남기는 사용자행동의모든흔적' — 레지스트리,이벤트로그,브라우저기록등"\*\*이라는한줄로시작하면, 왜아티팩트가 포렌식의가장풍부한증거원천인지드러납니다.

### Ⅱ. OS 레벨 아티팩트 — "레·이·프·점"

| 아티팩트               | 내용                                              |
| :----------------- | :---------------------------------------------- |
| **레지스트리**(Windows) | **최근실행프로그램,USB연결기록,계정정보** 등 시스템설정 전체가 기록됨       |
| **이벤트로그**          | **로그인/로그아웃,권한변경,서비스실행** 등 시스템이벤트 시간순기록          |
| **프리페치**(Prefetch) | 프로그램 **실행속도향상용캐시**— \*\*"이프로그램이언제몇번실행됐는지"\*\*남음 |
| **점프리스트/최근문서**     | 사용자가 **최근연파일,자주쓴프로그램** 목록                       |

→ 암기: **"설정은레지스트리에,사건은이벤트로그에,실행이력은프리페치에,파일이력은점프리스트에"** — 앞서다룬 \*\*"BPFDoor의프로세스이름위장"\*\*답안에서, 공격자가 아무리이름을바꿔도 \*\*"프리페치에는실제실행파일경로의흔적이남을수있다"\*\*는 게 조사관의핵심무기입니다.

### 도식화 제안

```
[OS레벨 아티팩트]
[레지스트리] "USB언제꽂았나,어떤프로그램설치했나"
[이벤트로그] "언제로그인했나,권한이언제바뀌었나"
[프리페치]   "이악성코드가몇시몇분에실행됐나"
[점프리스트] "최근에어떤파일을열었나"
     ↓ 모두조합하면
[사용자행동의전체타임라인 재구성가능]
```

### Ⅲ. 애플리케이션·네트워크아티팩트 — 핵심 배점

**함정 방지: "OS만본다"고답하면절반. 브라우저·네트워크레벨아티팩트까지 확장해야완성됩니다.**

| 아티팩트              | 내용                                                              |
| :---------------- | :-------------------------------------------------------------- |
| **브라우저기록**        | **방문URL,다운로드기록,캐시,쿠키,저장된비밀번호**— 앞서다룬 \*\*"인포스틸러"\*\*가노리는 바로그데이터 |
| **이메일메타데이터**      | 발신·수신경로,헤더정보 — **피싱경로추적**의핵심                                    |
| **네트워크연결기록**      | 앞서다룬 **SIEM/방화벽로그**— **누가언제어디로접속했는지**                           |
| **메모리(RAM) 아티팩트** | **실행중인프로세스,열린네트워크연결,복호화된키**등 — **전원을끄면사라짐**(휘발성)                |

→ 암기: **"브라우저엔웹행동,이메일엔소통경로,네트워크엔접속기록,메모리엔지금이순간의모든것(단,휘발성)"** — 특히 **메모리아티팩트**는 앞서다룬 \*\*"동형암호,대칭키"\*\*답안에서 \*\*"복호화된평문이나키가메모리에잠깐존재한다"\*\*는 사실과연결되어, \*\*"라이브포렌식(전원끄기전분석)이왜중요한지"\*\*를 보여줍니다.

### 도식화 제안

```
[아티팩트의 휘발성스펙트럼]
[메모리(RAM)] ← 가장휘발성높음(전원끄면즉시소실)
   ↓
[레지스트리/이벤트로그/프리페치] ← 디스크에저장,비교적안정적
   ↓
[브라우저기록/이메일] ← 사용자행동의직접적증거
   ↓
[네트워크로그(SIEM)] ← 별도서버에저장,공격자접근이어려움(가장안전)
```

### Ⅳ. 오늘시리즈총연결 — 안티포렌식과의공방

**함정 방지: "아티팩트가많다"로만끝내면절반. 앞서다룬안티포렌식이이아티팩트들을어떻게노리는지 마지막연결을보여줘야완성됩니다.**

| 안티포렌식시도      | 대상아티팩트        | 대응                                      |
| :----------- | :------------ | :-------------------------------------- |
| **타임스탬프조작**  | 이벤트로그,파일메타데이터 | 여러아티팩트 **교차검증**(프리페치와이벤트로그가불일치하면 조작의증거) |
| **로그삭제**     | 이벤트로그         | 앞서다룬 **SIEM으로별도저장**(원본이지워져도복사본존재)       |
| **메모리휘발성악용** | RAM아티팩트       | **라이브포렌식**으로 **전원끄기전메모리덤프**우선수집         |

→ "공격자가하나의아티팩트를지워도, 다른아티팩트와의 \*\*교차검증(Cross-validation)\*\*으로 조작사실자체가드러난다"는게 이답안의핵심포인트— 앞서다룬 \*\*"UEBA의행동기준선"\*\*처럼, \*\*"여러흔적이서로안맞으면 그자체가강력한증거"\*\*입니다.

### Ⅴ. 결론 포인트 (오늘 포렌식 시리즈 완결)

디지털포렌식아티팩트는 \*\*"사용자와시스템이의도하지않아도 남기는 수백가지흔적의총합"\*\*이며, 앞서다룬 \*\*파일카빙(삭제된본체복구),디스크이미징(전체보존),파일슬랙(여백속흔적),안티포렌식(지우려는시도)\*\*이 모두 \*\*"이아티팩트들을둘러싼공격과방어의공방"\*\*이었다는것을 보여줍니다 — 결국 오늘하루다룬포렌식시리즈전체가 \*\*"디지털세계에서완벽한흔적삭제는거의불가능하며, 여러곳에흩어진조각들을교차검증하면 진실은결국드러난다"\*\*는 결론으로 완결됩니다.

### **1. 답안 전개 스토리**

> "범죄자가 해킹 툴을 다운받아 기밀을 턴 뒤, 모든 파일을 지우고 휴지통까지 완벽히 비웠다. 범죄자는 '완전 범죄'라며 안심하겠지만 포렌식 수사관은 비웃는다. 왜냐하면 사용자가 컴퓨터에서 한 모든 행동은 윈도우 운영체제 구석구석에 \*\*'아티팩트(Artifact, 디지털 흔적)'\*\*라는 이름의 숨겨진 지문으로 자동 기록되어 빽빽하게 남아있기 때문이다. 이 아티팩트들은 수사관에게 완벽한 범죄 타임라인(알리바이)을 만들어준다. 수사관은 먼저 \*\*'웹 브라우저 역사(History)'\*\*를 뒤져 범죄자가 해킹 툴을 다운받은 내역을 찾는다. 그다음 윈도우의 **'프리패치(Prefetch)'** 폴더를 까서 그 해킹 툴이 언제, 몇 번이나 실행됐는지 횟수를 증명해 낸다. 마지막으로 윈도우 \*\*'레지스트리'\*\*를 열어 범죄자가 몇 시 몇 분에 USB를 꽂아 기밀을 빼갔는지 쐐기를 박는다. 아티팩트는 절대 위증을 하지 않는 시스템의 완벽한 목격자다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 위증하지 않는 시스템 블랙박스, 포렌식 아티팩트 개요**

* **정의:** 사용자가 PC나 스마트폰(운영체제)을 사용하고 응용 프로그램을 실행하는 과정에서, **사용자의 의도와 상관없이 시스템(OS) 내부에 자동으로 생성되고 남겨지는 모든 디지털 흔적(지문)과 기록물**.
* **포렌식적 가치:** 범죄자가 원본 문서(증거)를 파괴(안티 포렌식)하더라도, 운영체제가 몰래 남겨둔 아티팩트를 조합하면 범죄자의 과거 행위(누가, 언제, 어떤 프로그램을 켜서 무슨 문서를 열었는가)를 역추적하여 **완벽한 타임라인(Timeline)을 재구성**할 수 있음.

#### **II. \[본론 1] (단순화 버전) 아티팩트를 이용한 범죄 타임라인 재구성 파이프라인 (도식화)**

범죄자의 부인(오리발)을 3가지 아티팩트의 조합으로 박살 내는 과정을 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5OTEuNzYgNjE5LjEiIHdpZHRoPSI5OTEuNzYiIGhlaWdodD0iNjE5LjEiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9fX19UaW1lbGluZV9BbmFseXNpcyIgZGF0YS1sYWJlbD0i7Y+s66CM7IudIOyVhO2LsO2Mqe2KuCDsnLXtlakg67aE7ISdIChUaW1lbGluZSBBbmFseXNpcykiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9Ijg4My43NiIgaGVpZ2h0PSI1MzEuMSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9Ijg4My43NiIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPu2PrOugjOyLnSDslYTti7DtjKntirgg7Jy17ZWpIOu2hOyEnSAoVGltZWxpbmUgQW5hbHlzaXMpPC90ZXh0Pgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9fX19BcnRpZmFjdHMiIGRhdGEtbGFiZWw9IuyciOuPhOyasCDsmrTsmIHssrTsoJzsl5Ag7Iio6rKo7KeEIOuqqeqyqeyekCAoQXJ0aWZhY3RzKSI+CiAgPHJlY3QgeD0iMjg5Ljc3NTAwMDAwMDAwMDAzIiB5PSIxNDAuOSIgd2lkdGg9IjQwMi41MDE5OTk5OTk5OTk5NSIgaGVpZ2h0PSIyODguNDAwMDAwMDAwMDAwMDMiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSIyODkuNzc1MDAwMDAwMDAwMDMiIHk9IjE0MC45IiB3aWR0aD0iNDAyLjUwMTk5OTk5OTk5OTk1IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzMDEuNzc1MDAwMDAwMDAwMDMiIHk9IjE1NC45IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPuyciOuPhOyasCDsmrTsmIHssrTsoJzsl5Ag7Iio6rKo7KeEIOuqqeqyqeyekCAoQXJ0aWZhY3RzKTwvdGV4dD4KPC9nPgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTVVNQRUNUIiBkYXRhLXRvPSJUSU1FTElORSIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuqxsOynkyDslYzrpqzrsJTsnbQg67aV6rS0IiBwb2ludHM9IjMzOS4xOTksNTMxLjEwMDAwMDAwMDAwMDEgMzM5LjE5OSw1NDMuMSAyMjQuODQ5NSw1NDMuMSAyMjQuODQ5NSw1NzEuMSA5NDMuNzYsNTcxLjEgOTQzLjc2LDUwMy4xIDE4NC44NDk1LDUwMy4xIDcwLjUsNTAzLjEgNzAuNSwxNDQuOSAyNDkuNzc1MDAwMDAwMDAwMDMsMTQ0LjkgOTQzLjc2LDE0NC45IDk0My43NiwxODQuOSA1NDguODI0MDAwMDAwMDAwMSwxODQuOSA1NDguODI0MDAwMDAwMDAwMSwyNTIuNjMgNTcyLjgyNDAwMDAwMDAwMDEsMjUyLjYzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlRJTUVMSU5FIiBkYXRhLXRvPSJQUk9PRiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i6rGw7KeT66eQIOqwhO2MjCEiIHBvaW50cz0iNjc2LjI3NywyNjMuNzAwMDAwMDAwMDAwMDUgNjkyLjI3NywyNjMuNzAwMDAwMDAwMDAwMDUgMjAsMjYzLjcwMDAwMDAwMDAwMDA1IDIwLDIyMy43MDAwMDAwMDAwMDAwMiA4MzEuNTUxOTk5OTk5OTk5OSwyMjMuNzAwMDAwMDAwMDAwMDIgODMxLjU1MTk5OTk5OTk5OTksNTAzLjEgNzI1Ljk1LDUwMy4xIDcyNS45NSw1MzEuMSAyMCw1MzEuMSAyMCw1NDMuMSA3NjUuOTUsNTQzLjEgNjYwLjM0OCw1NDMuMSA2NjAuMzQ4MDAwMDAwMDAwMSw1MzEuMTAwMDAwMDAwMDAwMSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQVJUMSIgZGF0YS10bz0iVElNRUxJTkUiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNTI0LjgyNDAwMDAwMDAwMDEsMjIyLjggNTM2LjgyNDAwMDAwMDAwMDEsMjIyLjggNTM2LjgyNDAwMDAwMDAwMDEsMjYwLjAxIDU3Mi44MjQwMDAwMDAwMDAxLDI2MC4wMSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQVJUMiIgZGF0YS10bz0iVElNRUxJTkUiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNTI0LjgyNDAwMDAwMDAwMDEsMzA0LjYgNTM2LjgyNDAwMDAwMDAwMDEsMzA0LjYgNTM2LjgyNDAwMDAwMDAwMDEsMjY3LjM5IDU3Mi44MjQwMDAwMDAwMDAxLDI2Ny4zOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQVJUMyIgZGF0YS10bz0iVElNRUxJTkUiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNTI0LjgyNDAwMDAwMDAwMDEsMzg2LjQwMDAwMDAwMDAwMDAzIDU0OC44MjQwMDAwMDAwMDAxLDM4Ni40MDAwMDAwMDAwMDAwMyA1NDguODI0MDAwMDAwMDAwMSwyNzQuNzcgNTcyLjgyNDAwMDAwMDAwMDEsMjc0Ljc3IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlNVU1BFQ1QiIGRhdGEtdG89IlRJTUVMSU5FIiBkYXRhLWxhYmVsPSLqsbDsp5Mg7JWM66as67CU7J20IOu2leq0tCI+CiAgPHJlY3QgeD0iNDAuNTcwMDAwMDAwMDAwMDgiIHk9IjQ4Ny45NTAwMDAwMDAwMDAwNSIgd2lkdGg9IjExNi4yNTQwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9Ijk4LjY5NzAwMDAwMDAwMDA5IiB5PSI1MDMuMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+6rGw7KeTIOyVjOumrOuwlOydtCDrtpXqtLQ8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iVElNRUxJTkUiIGRhdGEtdG89IlBST09GIiBkYXRhLWxhYmVsPSLqsbDsp5Prp5Ag6rCE7YyMISI+CiAgPHJlY3QgeD0iNzkwLjk0Nzk5OTk5OTk5OTkiIHk9IjQzNS44ODc0OTk5OTk5OTk5MyIgd2lkdGg9IjgxLjIwODAwMDAwMDAwMDAxIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iODMxLjU1MTk5OTk5OTk5OTkiIHk9IjQ1MS4wMzc0OTk5OTk5OTk5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7qsbDsp5Prp5Ag6rCE7YyMITwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU1VTUEVDVCIgZGF0YS1sYWJlbD0i67KU7KOE7J6QOiAmcXVvdDvsoIQg7ZW07YK5IO2ItOydhCDquZAg7KCB64+EIOyXhuqzoArquLDrsIDsnYQgVVNC7JeQIOuzteyCrO2VnCDsoIHrj4Qg7JeG7Iq164uI64ukISDwn6SlJnF1b3Q7IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjE5Mi4yNTQwMDAwMDAwMDAwMiIgeT0iNDc3LjMwMDAwMDAwMDAwMDA3IiB3aWR0aD0iMjkzLjg5IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzMzkuMTk5IiB5PSI1MDQuMjAwMDAwMDAwMDAwMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjMzOS4xOTkiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7rspTso4TsnpA6ICZxdW90O+yghCDtlbTtgrkg7Yi07J2EIOq5kCDsoIHrj4Qg7JeG6rOgPC90c3Bhbj48dHNwYW4geD0iMzM5LjE5OSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+6riw67CA7J2EIFVTQuyXkCDrs7XsgqztlZwg7KCB64+EIOyXhuyKteuLiOuLpCEg8J+kpSZxdW90OzwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJUSU1FTElORSIgZGF0YS1sYWJlbD0iVElNRUxJTkUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMTAzLjQ1MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxMDcuNzI2NSIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5USU1FTElORTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUFJPT0YiIGRhdGEtbGFiZWw9IuuyleyglSDspp3qsbAg7KCc7LacIOKalu+4jwomcXVvdDvtlLzsnZjsnpDqsIAgVVNC66GcIOycoOy2nO2VnCDsgqzsi6TsnYQg7J6F7Kad7ZWoJnF1b3Q7IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjUxNC4xNDQiIHk9IjQ3Ny4zMDAwMDAwMDAwMDAwNyIgd2lkdGg9IjI5Mi40MDc5OTk5OTk5OTk5NiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI2NjAuMzQ4IiB5PSI1MDQuMjAwMDAwMDAwMDAwMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjY2MC4zNDgiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7rspXsoJUg7Kad6rGwIOygnOy2nCDimpbvuI88L3RzcGFuPjx0c3BhbiB4PSI2NjAuMzQ4IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj4mcXVvdDvtlLzsnZjsnpDqsIAgVVNC66GcIOycoOy2nO2VnCDsgqzsi6TsnYQg7J6F7Kad7ZWoJnF1b3Q7PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkFSVDEiIGRhdGEtbGFiZWw9IuybuSDruIzrnbzsmrDsoIAg6riw66GdIPCfjJAK7Ja07KCcIDE07IucIO2VtO2CuSDtiLQg64uk7Jq066Gc65OcIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjMxNS40MDgiIHk9IjE5NS45IiB3aWR0aD0iMjA5LjQxNTk5OTk5OTk5OTk3IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0MjAuMTE2IiB5PSIyMjIuOCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNDIwLjExNiIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuybuSDruIzrnbzsmrDsoIAg6riw66GdIPCfjJA8L3RzcGFuPjx0c3BhbiB4PSI0MjAuMTE2IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7slrTsoJwgMTTsi5wg7ZW07YK5IO2ItCDri6TsmrTroZzrk5w8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iVElNRUxJTkUiIGRhdGEtbGFiZWw9IlRJTUVMSU5FIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU3Mi44MjQwMDAwMDAwMDAxIiB5PSIyNDUuMjUiIHdpZHRoPSIxMDMuNDUzIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjYyNC41NTA1IiB5PSIyNjMuNyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+VElNRUxJTkU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkFSVDIiIGRhdGEtbGFiZWw9Iu2UhOumrO2MqOy5mCAoUHJlZmV0Y2gpIOKaoQrslrTsoJwgMTTsi5wgMTDrtoQg7ZW07YK5IO2ItCDsi6TtlokiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzE3LjYzMTAwMDAwMDAwMDAzIiB5PSIyNzcuNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSIyMDcuMTkyOTk5OTk5OTk5OTgiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQyMS4yMjc1IiB5PSIzMDQuNiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNDIxLjIyNzUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7tlITrpqztjKjsuZggKFByZWZldGNoKSDimqE8L3RzcGFuPjx0c3BhbiB4PSI0MjEuMjI3NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7Ja07KCcIDE07IucIDEw67aEIO2VtO2CuSDtiLQg7Iuk7ZaJPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkFSVDMiIGRhdGEtbGFiZWw9IuugiOyngOyKpO2KuOumrCAoUmVnaXN0cnkpIPCfl4TvuI8K7Ja07KCcIDE07IucIDE167aEIO2KueyglSBVU0Ig7IK97J6FIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjMwNS43NzUwMDAwMDAwMDAwMyIgeT0iMzU5LjUiIHdpZHRoPSIyMTkuMDQ4OTk5OTk5OTk5OTgiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQxNS4yOTk1IiB5PSIzODYuNCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNDE1LjI5OTUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7roIjsp4DsiqTtirjrpqwgKFJlZ2lzdHJ5KSDwn5eE77iPPC90c3Bhbj48dHNwYW4geD0iNDE1LjI5OTUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyWtOygnCAxNOyLnCAxNeu2hCDtirnsoJUgVVNCIOyCveyehTwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 윈도우(Windows) 시스템의 4대 핵심 아티팩트 전격 해부 (3단 표 - 1순위)**

운영체제가 자동으로 남기는 대표적인 흔적 창고들을 뒤지면 **'무엇을 얻을 수 있는지'** 대조하는 것이 완벽한 출제 포인트입니다.

| **핵심 아티팩트 명칭**              | **발생 원리 (왜 생기는가?)**                                                                                                             | **포렌식 관점에서의 증거 가치 (무엇을 찾나?) 🚨**                                                                                                |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------ |
| **1. 프리패치** *(Prefetch)*    | **'프로그램 로딩을 빠르게 하려고 캐싱함'.** 윈도우가 응용 프로그램의 실행 속도를 높이기 위해, 프로그램이 부팅될 때 필요한 메모리 정보를 미리 C드라이브 `\Prefetch` 폴더에 캐싱(저장)해 두는 파일(`.pf`). | **\[응용 프로그램 실행 흔적 입증 💯]** 범죄자가 해킹 툴(Wiping 툴)을 쓰고 삭제했어도, 이 폴더를 뒤지면 **'특정 프로그램이 언제, 총 몇 번이나 실행되었는지'** 완벽하게 횟수와 타임스탬프를 입증할 수 있음. |
| **2. 레지스트리** *(Registry)*   | **'운영체제의 모든 뼈대와 설정 저장소'.** 윈도우 시스템의 부팅, 하드웨어 설정, 사용자 계정, 설치된 소프트웨어 정보 등 OS가 굴러가기 위한 모든 환경 설정이 기록된 거대한 데이터베이스.                   | **\[USB 접속 흔적 및 자동 실행 악성코드]** 범죄자가 꽂은 **USB의 고유 시리얼 넘버와 최초/최근 연결 시간**을 완벽히 추적 가능. 해커가 심어둔 시작프로그램(Run) 악성코드의 존재도 입증 가능.          |
| **3. 이벤트 로그** *(Event Log)* | **'시스템 내부에서 발생한 중대 사건의 일기장'.** 운영체제, 애플리케이션, 보안 프로세스가 작동하면서 발생하는 에러, 경고, 성공 상태를 `EVTX` 파일 형태로 꼼꼼하게 기록해 두는 블랙박스.                 | **\[해커의 불법 로그인 시도 타임라인]** 해커가 RDP(원격 데스크톱)로 접속을 시도하여 성공했는지(Event ID 4624), 실패했는지(Event ID 4625) 등 **침입 흔적과 계정 도용 여부**를 명백히 밝혀냄. |
| **4. 웹 브라우저 아티팩트**          | 사용자가 인터넷을 서핑할 때 속도 향상을 위해 캐시(Cache), 다운로드 기록, 방문 기록(History), 쿠키(Cookie)를 내부에 저장함.                                              | 범죄자의 관심사(검색어), 다운로드한 악성 파일, 접속한 불법 사이트 등 \*\*'범행 전 사전 조사(의도)'\*\*를 입증하는 강력한 프로파일링 도구임.                                          |

#### **IV. \[결론/제언] 파편화된 아티팩트의 자동 융합 분석(AI 기반)의 필요성**

* **(키워드 위주 2줄 마무리)** "단일 아티팩트 하나만으로는 결정적 증거가 될 수 없습니다. 수만 개의 이벤트 로그와 프리패치 파일 속에 숨겨진 해커의 타임라인을 빠르고 입체적으로 구성하기 위해, 최신 포렌식 수사는 **머신러닝(AI)을 활용하여 파편화된 다기종 아티팩트의 상관관계를 자동으로 매핑해 내는 '슈퍼 타임라인(Super Timeline)' 분석 기술로 진화하고 있습니다.**"
