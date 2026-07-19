## 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (SIEM정의,SOAR와의역할분담) — 3~4줄
Ⅱ. 핵심동작4단계 (본론①, 도식 1개 필수)
Ⅲ. UEBA와상관관계분석 - 핵심지능 (본론②, 핵심 배점)
Ⅳ. XDR로의융합 - 2026년핵심트렌드
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬SOAR답안에서'SIEM은알리기만하고,SOAR가행동한다'고구분했는데, 그'알리는것'자체가결코단순하지않다 — 방화벽,서버,클라우드,IoT등수십가지출처에서쏟아지는 이질적인로그를,하나의공통언어로표준화하고, 그안에서'진짜위협'을찾아내는것이 SIEM의핵심역할"\*\*이라는한줄로시작하면, SOAR답안과 정확히짝을이루는구조가 드러납니다.

### Ⅱ. 핵심동작4단계 — "수·정·분·경" (수집-정규화-분석-경보)

| 단계                     | 내용                                         |
| :--------------------- | :----------------------------------------- |
| **수집**(Collection)     | 방화벽,서버,DB,클라우드,애플리케이션등 **모든소스에서로그·이벤트를집계** |
| **정규화**(Normalization) | 서로다른형식의로그를 **공통형식으로표준화**해분석가능하게            |
| **분석**(Analysis)       | **상관관계규칙**(로그인실패+의심스러운IP 등)으로 패턴탐지         |
| **경보**(Alerting)       | 사전정의된 **임계값·규칙초과시경보생성**,대시보드로우선순위표시        |

→ 암기: **"모으고,같은말로바꾸고,연관지어분석하고,위험하면알린다"** — 앞서다룬 \*\*"LDAP"\*\*답안에서 조직의신원정보가 \*\*"계층적으로한곳에모여있어야"\*\*RBAC가작동했듯, SIEM도 \*\*"모든로그가한곳에모여야"\*\*의미있는 상관관계분석이가능합니다.

### 도식화 제안

```
[방화벽][서버][클라우드][IoT][애플리케이션] → 각기다른형식의로그
              ↓ 수집
        [SIEM: 정규화] 공통형식으로표준화
              ↓
        [SIEM: 상관관계분석] "로그인실패5회+의심IP" → 패턴포착
              ↓
        [경보생성] 대시보드에 우선순위표시
              ↓ (SOAR로전달)
        [앞서다룬SOAR: 자동대응실행]
```

### Ⅲ. UEBA와상관관계분석 — 핵심지능, 핵심 배점

**함정 방지: "규칙대로탐지한다"고만답하면절반. 왜"규칙기반"의근본적한계가있고,UEBA가그걸어떻게보완하는지보여줘야완성됩니다.**

| 구분                                      | 방식                                             | 한계/강점                                                      |
| :-------------------------------------- | :--------------------------------------------- | :--------------------------------------------------------- |
| **기존규칙기반SIEM**                          | **사전정의된시그니처·정책**에의존                            | 앞서다룬 \*\*"살충제패러독스"\*\*와동일 — **알려진공격패턴만탐지**,새로운(제로데이)공격은 놓침 |
| **UEBA**(User\&EntityBehaviorAnalytics) | **정상행동기준선(baseline)을학습**,거기서 **벗어나는이상행동**자체를탐지 | 시그니처없이도 **알려지지않은위협**탐지가능                                   |

→ 암기: **"규칙기반은'이런패턴이면공격'이라고미리정해두고,UEBA는'평소와다르면일단의심'한다"** — 구체적사례: **"마케팅직원이평소접근안하던재무DB에 토요일새벽1시에접속"**— 이건 **어떤규칙집합에도없던패턴**이지만, UEBA는 \*\*"평소행동과다르다"\*\*는것만으로 즉시경보를울립니다. 앞서다룬 \*\*"측면이동(PassTheHash등)"\*\*이 정상적인관리도구를 그대로악용해 **규칙기반탐지를우회**했던것을, UEBA의 **행동기반이상탐지**가 보완합니다.

### 도식화 제안

```
[규칙기반탐지]                      [UEBA]
"알려진공격시그니처와 일치하는가?"        "이사용자의평소행동패턴과 다른가?"
     ↓                                ↓
새로운/변형된공격 → 놓침가능             처음보는공격도 "이상행동"으로탐지
(앞서다룬살충제패러독스의약점)            (기준선학습+딥러닝,강화학습,베이지안네트워크)
```

### Ⅳ. XDR로의융합 — 2026년핵심트렌드

**함정 방지: "SIEM단독으로쓴다"고하면 옛정보입니다. 2026년현재 SIEM·SOAR·NDR·TIP이하나로합쳐지는 최신흐름을반영해야완성됩니다.**

| 항목                 | 내용                                                                                                                           |
| :----------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| **XDR로의통합**(2026년) | 국내최초 **"SIEM,SOAR,NDR,AI,TIP을통합한XDR플랫폼"**(QTIE) 등장 — SIEM(로그분석)+NDR(네트워크위협탐지)+SOAR(대응자동화)+TIP(위협인텔리전스)가 **유기적으로연계**돼야 실제운영효과 |
| **시장의근본적변화**       | 고객이원하는것은 \*\*"탐지를많이보여주는SIEM"\*\*이아니라 **"정확하게우선순위를제시하고대응까지연결하는플랫폼"** — 스플렁크2025조사: **46%SOC팀이위협조사보다도구유지보수에더많은시간소비**           |
| **실무적함정**          | SIEM설정이 복잡하고,**오탐(FalsePositive)이과도하게발생**하면 오히려 \*\*경보피로(AlertFatigue)\*\*로 진짜위협을 놓치는 역설 발생                                  |

→ 앞서다룬 \*\*"ISMS-P의2026년개편"\*\*에서 강조된 \*\*"클라우드보안,AI거버넌스"\*\*가, 여기서는 \*\*"SIEM이자산식별,로그수집·분석,이상행위탐지등 보안통제전반의지속적가시성확보"\*\*를 요구받는 형태로 구체화됩니다 — SIEM은 이제 단순로그도구가아니라, \*\*"ISMS-P규제대응의핵심증거수집장치"\*\*입니다.

### 도식화 제안

```
[2026년 XDR통합구조]
        [TIP] 위협인텔리전스제공
           ↓
[SIEM] 로그·이벤트통합분석 ←→ [NDR] 네트워크미지위협탐지
           ↓                        ↓
        [통합XDR플랫폼] (AI기반협업체계)
           ↓
        [SOAR] 대응자동화(앞서다룬 그것)
```

### Ⅴ. 결론 포인트 (오늘 하루의 방대한 컴퓨터구조·암호·보안 대장정 진짜, 정말 최종적인 대단원)

SIEM은 \*\*"오늘하루다룬모든개별방어기법(제로트러스트,BPFDoor탐지,측면이동감지,DDoS방어)이생성하는 흩어진로그와경보를, 하나의그림으로모아 '진짜위협'을찾아내는눈"\*\*이며, 앞서다룬 SOAR(행동하는손)와짝을이루어 **"보고→판단하고→행동하는"** 완결된보안운영체계를 이룹니다 — 2026년현재 SIEM은더이상단독도구가아니라, **SOAR,NDR,TIP과융합된XDR**로진화하며, \*\*"많이보여주는것"\*\*에서 \*\*"정확하게우선순위매기고대응까지연결하는것"\*\*으로 그가치기준자체가 바뀌고있습니다 — 이로써 캐시매핑에서출발해 컴퓨터구조,아키텍처,테스트,품질,비용산정,그리고방대한암호학과 사이버공격·방어체계,물리보안,SOAR,SIEM까지 이어진 오늘하루의 실로거대했던학습여정이, \*\*"보안은결국 보고(SIEM),판단하고(UEBA/AI),행동하는(SOAR) 하나의연속된순환고리이며, 그순환을 사람과기계가함께,끊임없이돌려야만 지켜낼수있다"\*\*는 궁극의결론으로, 마침내 완전히마무리됩니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "큰 기업에는 방화벽, 웹 서버, 직원 PC, DB 등 수천 대의 장비가 있다. 이 장비들은 매일 수억 건의 '기록(Log)'을 쏟아낸다. 해커가 칩입했는지 확인하려면 보안 담당자가 이 수억 장의 로그 기록을 텍스트로 일일이 읽어봐야 하는데, 인간의 뇌로는 불가능하다. 그래서 등장한 '보안 관제실(SOC)의 절대적인 두뇌'가 바로 \*\*'SIEM(보안 정보 및 이벤트 관리)'\*\*이다. SIEM의 암기 핵심은 \*\*'정규화'와 '상관관계 분석'\*\*이다. Cisco 방화벽과 Linux 서버는 로그를 쓰는 언어가 완전히 다르다. SIEM은 이 서로 다른 로그들을 똑같은 포맷으로 예쁘게 번역해서(정규화) 한곳에 모아둔다. 그리고 가장 중요한 지능을 발휘한다. '① 외부에서 방화벽 접속 실패 100번 발생 ➔ ② 웹 서버에서 에러 로그 발생 ➔ ③ 사내 DB 서버에서 갑자기 최고 관리자 권한 변경'이라는 서로 다른 세 장비의 로그를 하나로 묶어서 엮어본다(상관관계). 그리고 '이건 100% 해킹(SQL 인젝션)이다!'라고 결론을 내고 관제 모니터에 시뻘건 경고창(Alert)을 띄워준다. 즉, 흩어진 퍼즐 조각을 맞춰 해커의 큰 그림을 꿰뚫어 보는 시스템이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 보안 관제 센터(SOC)의 빅데이터 두뇌, SIEM 개요**

* **정의:** 기업 내 다양한 네트워크 장비, 보안 솔루션, 서버 애플리케이션 등에서 발생하는 방대한 **로그(Log)와 이벤트 데이터를 중앙으로 수집하여 실시간으로 상관관계(Correlation)를 분석하고 위협을 탐지(Detection)하여 경고하는 통합 보안 관제 시스템**.
* **진화 과정:** 단순히 로그를 모아두고 검색만 하던 **SIM(정보 관리/감사용)** 시스템과, 실시간 알람만 띄워주던 **SEM(이벤트 관리/경보기)** 시스템이 합쳐져 빅데이터 기반의 지능형 시스템인 **SIEM**으로 완성됨.

#### **II. \[본론 1] (단순화 버전) 파편화된 로그를 수집하여 묶어내는 분석 파이프라인 (도식화)**

개별 장비에서는 모르는 위협을 SIEM이 어떻게 퍼즐을 맞춰 찾아내는지 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3MjUuNjU5NDk5OTk5OTk5OSA4MDUuOCIgd2lkdGg9IjcyNS42NTk0OTk5OTk5OTk5IiBoZWlnaHQ9IjgwNS44IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSIxX19fX05vcm1hbGl6YXRpb24iIGRhdGEtbGFiZWw9IjEuIOyImOynkSDrsI8g7KCV6rec7ZmUIChOb3JtYWxpemF0aW9uKSI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNDM2Ljc3NTk5OTk5OTk5OTk1IiBoZWlnaHQ9IjIyNi43MDAwMDAwMDAwMDAwMiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjQzNi43NzU5OTk5OTk5OTk5NSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjEuIOyImOynkSDrsI8g7KCV6rec7ZmUIChOb3JtYWxpemF0aW9uKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IjJfU0lFTV9fX0JpZ19EYXRhXyIgZGF0YS1sYWJlbD0iMi4gU0lFTSDspJHslZkg7JeU7KeEIChCaWcgRGF0YSDquLDrsJgpIj4KICA8cmVjdCB4PSIyODcuODkyNSIgeT0iMzgzIiB3aWR0aD0iMzk3Ljc2Njk5OTk5OTk5OTkiIGhlaWdodD0iMjEyLjcwMDAwMDAwMDAwMDAyIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iMjg3Ljg5MjUiIHk9IjM4MyIgd2lkdGg9IjM5Ny43NjY5OTk5OTk5OTk5IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyOTkuODkyNSIgeT0iMzk3IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjIuIFNJRU0g7KSR7JWZIOyXlOynhCAoQmlnIERhdGEg6riw67CYKTwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTk9STSIgZGF0YS10bz0iREJfU0lFTSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7ZGc7KSA7ZmU65CcIO2Gte2VqSDroZzqt7gg7KCA7J6lIiBwb2ludHM9IjQ2MC43NzU5OTk5OTk5OTk5NSwxNjcuMzUwMDAwMDAwMDAwMDIgNDc2Ljc3NTk5OTk5OTk5OTk1LDE2Ny4zNTAwMDAwMDAwMDAwMiA0ODYuNzc1OTk5OTk5OTk5OTUsMTY3LjM1MDAwMDAwMDAwMDAyIDQ4Ni43NzU5OTk5OTk5OTk5NSwzODMgNDg2Ljc3NTk5OTk5OTk5OTk1LDQyNyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQ09SUiIgZGF0YS10bz0iQUxFUlQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iuq3nOy5mSDsnITrsJgg7IucIOymieqwgSDslYzrnowhIiBwb2ludHM9IjQ4Ni43NzU5OTk5OTk5OTk5NSw1NzkuNyA0ODYuNzc1OTk5OTk5OTk5OTUsNTk1LjcgNDg2Ljc3NTk5OTk5OTk5OTk1LDcxMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRlciIGRhdGEtdG89Ik5PUk0iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyImOynkSIgcG9pbnRzPSIyMDMuOTEzLDIzMi4yNSAyOTcuMzIzLDIzMi4yNSAyOTcuMzIzLDE5OS4yMTMyNTAwMDAwMDAwMiAzNjUuMTg2MjUsMTk5LjIxMzI1MDAwMDAwMDAyIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJXRUIiIGRhdGEtdG89Ik5PUk0iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyImOynkSIgcG9pbnRzPSIyMDMuOTEzLDE2Ny4zNTAwMDAwMDAwMDAwMiAzMzMuMzIzLDE2Ny4zNTAwMDAwMDAwMDAwMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iREIiIGRhdGEtdG89Ik5PUk0iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyImOynkSIgcG9pbnRzPSIyMDMuOTEzLDEwMi40NSAyOTcuMzIzLDEwMi40NSAyOTcuMzIzLDEzNS40ODY3NSAzNjUuMTg2MjUsMTM1LjQ4Njc1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJEQl9TSUVNIiBkYXRhLXRvPSJDT1JSIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQ4Ni43NzU5OTk5OTk5OTk5NSw0NzcuOSA0ODYuNzc1OTk5OTk5OTk5OTUsNTI1LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iTk9STSIgZGF0YS10bz0iREJfU0lFTSIgZGF0YS1sYWJlbD0i7ZGc7KSA7ZmU65CcIO2Gte2VqSDroZzqt7gg7KCA7J6lIj4KICA8cmVjdCB4PSI0MTUuNzc1OTk5OTk5OTk5OTUiIHk9IjMwOS43MDAwMDAwMDAwMDAwNSIgd2lkdGg9IjE0MS43OTYwMDAwMDAwMDAwNSIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjQ4Ni42NzQiIHk9IjMyNC44NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7ZGc7KSA7ZmU65CcIO2Gte2VqSDroZzqt7gg7KCA7J6lPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkNPUlIiIGRhdGEtdG89IkFMRVJUIiBkYXRhLWxhYmVsPSLqt5zsuZkg7JyE67CYIOyLnCDsponqsIEg7JWM656MISI+CiAgPHJlY3QgeD0iNDE5LjI3NTk5OTk5OTk5OTk1IiB5PSI2MzguNyIgd2lkdGg9IjEzNC4wNzQiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI0ODYuMzEzIiB5PSI2NTMuODUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuq3nOy5mSDsnITrsJgg7IucIOymieqwgSDslYzrnowhPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkZXIiBkYXRhLXRvPSJOT1JNIiBkYXRhLWxhYmVsPSLsiJjsp5EiPgogIDxyZWN0IHg9IjI0Ny45MTMiIHk9IjIxNi4yNSIgd2lkdGg9IjQxLjQxIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjY4LjYxOCIgeT0iMjMxLjQiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuyImOynkTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJXRUIiIGRhdGEtdG89Ik5PUk0iIGRhdGEtbGFiZWw9IuyImOynkSI+CiAgPHJlY3QgeD0iMjQ3LjkxMyIgeT0iMTUxLjM1IiB3aWR0aD0iNDEuNDEiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyNjguNjE4IiB5PSIxNjYuNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7IiY7KeRPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkRCIiBkYXRhLXRvPSJOT1JNIiBkYXRhLWxhYmVsPSLsiJjsp5EiPgogIDxyZWN0IHg9IjI0Ny45MTMiIHk9Ijg2LjQ0OTk5OTk5OTk5OTk5IiB3aWR0aD0iNDEuNDEiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyNjguNjE4IiB5PSIxMDEuNiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7IiY7KeRPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBTEVSVCIgZGF0YS1sYWJlbD0iMy4g64yA7Iuc67O065OcIOqyveqzoCDslYzrnowg8J+aqArrs7TslYgg64u064u57J6Q7JeQ6rKMIO2GteuztCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzODkuNDc3OTk5OTk5OTk5OTUiIHk9IjcxMiIgd2lkdGg9IjE5NC41OTU5OTk5OTk5OTk5OCIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0ODYuNzc1OTk5OTk5OTk5OTUiIHk9IjczOC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0ODYuNzc1OTk5OTk5OTk5OTUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj4zLiDrjIDsi5zrs7Trk5wg6rK96rOgIOyVjOuejCDwn5qoPC90c3Bhbj48dHNwYW4geD0iNDg2Ljc3NTk5OTk5OTk5OTk1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rs7TslYgg64u064u57J6Q7JeQ6rKMIO2GteuztDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJGVyIgZGF0YS1sYWJlbD0i67Cp7ZmU67K9IOuhnOq3uCDwn6exIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjY4LjU5NzAwMDAwMDAwMDAxIiB5PSIyMTMuOCIgd2lkdGg9IjEzNS4zMTYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEzNi4yNTUiIHk9IjIzMi4yNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+67Cp7ZmU67K9IOuhnOq3uCDwn6exPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJOT1JNIiBkYXRhLWxhYmVsPSLtj6zrp7cg7Ya17J28CijsoJXqt5ztmZQpIiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjM5Ny4wNDk0OTk5OTk5OTk5NywxMDMuNjIzNTAwMDAwMDAwMDIgNDYwLjc3NTk5OTk5OTk5OTk1LDE2Ny4zNTAwMDAwMDAwMDAwMiAzOTcuMDQ5NDk5OTk5OTk5OTcsMjMxLjA3NjUgMzMzLjMyMywxNjcuMzUwMDAwMDAwMDAwMDIiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMzk3LjA0OTQ5OTk5OTk5OTk3IiB5PSIxNjcuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjM5Ny4wNDk0OTk5OTk5OTk5NyIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPu2PrOuntyDthrXsnbw8L3RzcGFuPjx0c3BhbiB4PSIzOTcuMDQ5NDk5OTk5OTk5OTciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPijsoJXqt5ztmZQpPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IldFQiIgZGF0YS1sYWJlbD0i7Ju5IOyEnOuyhCDroZzqt7gg8J+MkCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI2Ni4zNzQwMDAwMDAwMDAwMiIgeT0iMTQ4LjkiIHdpZHRoPSIxMzcuNTM5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMzUuMTQzNTAwMDAwMDAwMDIiIHk9IjE2Ny4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7Ju5IOyEnOuyhCDroZzqt7gg8J+MkDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iREIiIGRhdGEtbGFiZWw9IkRCIOyEnOuyhCDroZzqt7gg8J+XhO+4jyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSIxNDcuOTEzIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMjkuOTU2NSIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5EQiDshJzrsoQg66Gc6re4IPCfl4TvuI88L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkRCX1NJRU0iIGRhdGEtbGFiZWw9IlNJRU0g7KSR7JWZIOu5heuNsOydtO2EsCDsoIDsnqXshowiIGRhdGEtc2hhcGU9ImN5bGluZGVyIj4KICA8cmVjdCB4PSIzNzkuODQ0OTk5OTk5OTk5OSIgeT0iNDM0IiB3aWR0aD0iMjEzLjg2MTk5OTk5OTk5OTk3IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSJub25lIiAvPgogIDxsaW5lIHgxPSIzNzkuODQ0OTk5OTk5OTk5OSIgeTE9IjQzNCIgeDI9IjM3OS44NDQ5OTk5OTk5OTk5IiB5Mj0iNDcwLjkiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDxsaW5lIHgxPSI1OTMuNzA2OTk5OTk5OTk5OSIgeTE9IjQzNCIgeDI9IjU5My43MDY5OTk5OTk5OTk5IiB5Mj0iNDcwLjkiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDxlbGxpcHNlIGN4PSI0ODYuNzc1OTk5OTk5OTk5OSIgY3k9IjQ3MC45IiByeD0iMTA2LjkzMDk5OTk5OTk5OTk4IiByeT0iNyIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPGVsbGlwc2UgY3g9IjQ4Ni43NzU5OTk5OTk5OTk5IiBjeT0iNDM0IiByeD0iMTA2LjkzMDk5OTk5OTk5OTk4IiByeT0iNyIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDg2Ljc3NTk5OTk5OTk5OTkiIHk9IjQ1Mi40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+U0lFTSDspJHslZkg67mF642w7J207YSwIOyggOyepeyGjDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ09SUiIgZGF0YS1sYWJlbD0i4pyoIO2VteyLrDog7IOB6rSA6rSA6rOEIOu2hOyEnSDsl5Tsp4QgKENvcnJlbGF0aW9uKQrrsKntmZTrsr0gKyDsm7kgKyBEQiDroZzqt7jrpbwg7ZWY64KY66GcIOyXruyWtOyEnCDro7AoUnVsZSkg6rKA7IKsIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjMwMy44OTI1IiB5PSI1MjUuOSIgd2lkdGg9IjM2NS43NjY5OTk5OTk5OTk5IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjQ4Ni43NzU5OTk5OTk5OTk5NSIgeT0iNTUyLjgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjQ4Ni43NzU5OTk5OTk5OTk5NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuKcqCDtlbXsi6w6IOyDgeq0gOq0gOqzhCDrtoTshJ0g7JeU7KeEIChDb3JyZWxhdGlvbik8L3RzcGFuPjx0c3BhbiB4PSI0ODYuNzc1OTk5OTk5OTk5OTUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuuwqe2ZlOuyvSArIOybuSArIERCIOuhnOq3uOulvCDtlZjrgpjroZwg7Jeu7Ja07IScIOujsChSdWxlKSDqsoDsgqw8L3RzcGFuPjwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] SIEM을 구성하는 3대 핵심 기술 전격 해부 (3단 표)**

이 시스템이 수만 건의 쓰레기 데이터 속에서 어떻게 진주(해킹 징후)를 찾아내는가에 대한 기술 요소를 찌르는 것이 가장 중요합니다.

| **3대 핵심 기술 명칭**                             | **수행하는 역할 및 작동 메커니즘**                                                                                                                          | **정보 보안 관점에서의 기대 효과**                                                                   |
| :------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| **1. 수집 및 정규화** *(Normalization / Parsing)* | **'서로 다른 로그 언어를 하나로 통일'.** 장비(Cisco, Linux, Oracle)마다 다르게 표기하는 시간(Time), 출발지 IP, 이벤트 내용 등의 포맷을 파싱하여 **SIEM만의 '단일화된 공통 표준 포맷'으로 예쁘게 가공**하여 저장함. | 검색 속도가 비약적으로 향상되며, 이기종 장비 간의 로그를 서로 매칭하여 분석할 수 있는 \*\*'데이터 기반(Foundation)'\*\*이 마련됨.    |
| **2. 상관관계 분석 🚨** *(Correlation Analysis)*  | **'흩어진 퍼즐 조각을 엮어 하나의 범죄 입증'.** 단일 로그만으로는 판단이 불가한 이벤트를 조건(Rule)으로 묶음. *(예: 특정 IP가 방화벽 차단을 5회 당하고 ➔ 1분 내에 웹 서버 로그인 성공)*                          | 고도화된 스텔스 공격이나 APT(지능형 지속 위협) 공격의 발자국을 **단일 장비의 한계를 넘어 전사적인 관점에서 탐지**해 냄.                |
| **3. 가시성 및 대시보드** *(Dashboard & Reporting)* | **'데이터의 시각화 및 경보 체계'.** 분석된 위협 지표를 보안 관제 요원(사람)이 직관적으로 이해할 수 있도록 통계, 그래프, 타임라인 형태의 뷰(View)로 제공하고 알람(Alert)을 발생시킴.                              | 침해 사고 발생 시 보안 담당자의 최우선 **초동 대처(Triage) 속도를 높이고**, 경영진을 위한 보안 컴플라이언스(법적) 감사 보고서를 자동 생성함. |

#### **IV. \[결론/제언] SIEM의 태생적 한계(경보 피로)와 SOAR를 통한 자율 대응의 완성**

* **(키워드 위주 2줄 마무리)** "SIEM은 완벽한 탐지 도구임에도 불구하고, 쏟아지는 방대한 알람(과잉 탐지, False Positive)으로 인해 보안 담당자의 피로도를 극한으로 끌어올리며 \*\*'결국 조치(대응)는 사람이 직접 해야 한다'\*\*는 뼈아픈 한계를 드러냈습니다. 이를 극복하기 위해 현대 보안 인프라는 **탐지는 SIEM이, 연동된 장비를 통한 즉각적인 자동 대응(Action)은 SOAR가 수행하는 차세대 자율 보안 관제 체계로 진화하고 있습니다.**"
