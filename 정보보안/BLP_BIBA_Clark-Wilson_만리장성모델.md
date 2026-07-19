### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (4모델의공통점,보호목표의차이) — 3~4줄
Ⅱ. BLP - 기밀성모델 (본론①, 도식 1개 필수)
Ⅲ. Biba - 무결성모델 (본론②, 핵심 배점 - BLP와의대칭)
Ⅳ. Clark-Wilson/만리장성 - 실무형모델
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬MAC(강제접근통제)은'시스템이강제로정책을적용한다'는원칙만말했는데, 실제로'어떤규칙으로강제할지'를 수학적으로정의한게이4가지모델 — BLP는기밀성(비밀누출방지),Biba는무결성(데이터오염방지),Clark-Wilson은상업적무결성,만리장성은이해충돌방지"\*\*라는한줄로시작하면, 왜4개나필요한지 (목표가다다르다는것) 명확해집니다.

### Ⅱ. BLP(Bell-LaPadula) — 기밀성모델

| 원칙                       | 규칙                | 의미                          |
| :----------------------- | :---------------- | :-------------------------- |
| **단순보안속성**(No Read Up)   | **낮은등급이높은등급을못읽음** | "일반사원이비밀문서를못본다"             |
| \***-속성**(No Write Down) | **높은등급이낮은등급에못씀**  | "비밀취급자가일반문서에비밀내용을못쓴다"(유출방지) |

→ 암기: **"위로못읽고,아래로못쓴다"** — 오직 \*\*"비밀이위에서아래로새는것"\*\*만막는데집중합니다. 앞서다룬 **"MAC"**(국방·정부시스템)이 바로이 BLP원칙을 구현한 대표사례입니다.

### 도식화 제안

```
[등급: 비밀]  ← No Write Down(위에서아래로못씀,유출방지)
     ↑ No Read Up(아래에서위로못읽음)
[등급: 일반]
```

### Ⅲ. Biba — 무결성모델, 핵심 배점(BLP와의완벽한대칭)

**함정 방지: "BLP와비슷하다"고만답하면절반. BLP와 정확히정반대방향이라는 것,그리고 왜 "정반대"인지를 보여줘야완성됩니다.**

| 원칙                        | 규칙                | 의미                              |
| :------------------------ | :---------------- | :------------------------------ |
| **단순무결성속성**(No Read Down) | **높은등급이낮은등급을못읽음** | "신뢰도높은프로세스가 신뢰도낮은(오염된)데이터를못읽는다" |
| \***-무결성속성**(No Write Up) | **낮은등급이높은등급에못씀**  | "신뢰도낮은사용자가 신뢰도높은데이터를오염시키지못한다"   |

→ 암기: **"BLP는비밀이새는걸막고(기밀성),Biba는오염이퍼지는걸막는다(무결성)"** — 방향이 **완전히거꾸로**입니다: BLP는 "위로읽기금지,아래로쓰기금지", Biba는 **"아래로읽기금지,위로쓰기금지"**.

### 도식화 제안

```
[BLP - 기밀성]                    [Biba - 무결성]
[비밀]                             [신뢰도높음]
  ↑읽기금지                          ↓읽기금지(아래를못읽음)
[일반] ←쓰기금지(위에서씀)             [신뢰도낮음] →쓰기금지(위로못씀)

BLP: "비밀이 아래로새면안됨" (정보의하향유출방지)
Biba: "오염이 위로퍼지면안됨" (낮은신뢰데이터의상향오염방지)
```

→ "비밀정보를보호할땐BLP,데이터의정확성을보호할땐Biba를쓴다"는게 목적에따른선택기준입니다 — 예를들어 \*\*은행시스템(거래정확성이생명)\*\*은 Biba가더적합하고, \*\*국방시스템(기밀유지가생명)\*\*은 BLP가적합합니다.

### Ⅳ. Clark-Wilson/만리장성 — 실무형모델

**함정 방지: BLP/Biba는이론적모델이라고만끝내면절반. 실제상업환경에맞춘 두모델을보여줘야완성됩니다.**

| 모델                     | 핵심원리                                                                                                                       |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| **Clark-Wilson**       | \*\*"잘정의된트랜잭션(Well-formed Transaction)"\*\*만허용— 데이터는반드시 \*\*인증된절차(프로그램)\*\*를통해서만변경가능(직접수정금지),**직무분리**(한사람이거래의전과정을혼자처리못하게함) |
| **만리장성**(Chinese Wall) | **이해충돌(Conflict of Interest)방지**— 한사람이 **경쟁관계에있는두회사의데이터**에 **동시접근하면안됨**(과거접근한적있으면,경쟁사데이터접근이자동차단)                           |

→ 암기: **"Clark-Wilson은은행시스템스타일(정해진절차로만,여러사람이나눠서),만리장성은컨설팅·회계법인스타일(한번이쪽고객봤으면 경쟁사쪽은못본다)"** — 앞서다룬 \*\*"직무분리"\*\*개념이 Clark-Wilson의핵심이고, \*\*"동적으로과거접근기록에따라 접근범위가바뀐다"\*\*는점에서 만리장성은 앞서다룬 \*\*ABAC(속성기반,동적판단)\*\*의 초기형태라고볼수있습니다.

### 도식화 제안

```
[Clark-Wilson]                        [만리장성모델]
사용자 → [인증된프로그램(트랜잭션)]        [분석가A] 회사X데이터 접근(이미접근)
              ↓ (직접수정불가)                ↓
         [데이터변경]                    [분석가A] 회사Y(X의경쟁사) 데이터
         (절차/직무분리로무결성보장)          → 자동차단(이해충돌방지)
```

### Ⅴ. 결론 포인트 (보안 모델 시리즈 완결)

이4가지모델은 \*\*"MAC(강제접근통제)이라는큰틀을,서로다른보호목표(기밀성/무결성/상업적신뢰성/이해충돌방지)에맞춰 구체적수학규칙으로구현한것"\*\*입니다 — BLP↔Biba가 \*\*"읽기/쓰기방향의완벽한대칭"\*\*을보여주는 이론적짝이라면, Clark-Wilson과만리장성은 \*\*"실제상업환경(은행,컨설팅업)"\*\*에 맞춘 실무형응용입니다 — 앞서다룬 \*\*RBAC/ABAC(누가접근을결정하는가)\*\*답안과 이답안(BLP/Biba등,무엇을어떻게보호하는가)이 결합되어야, 오늘다룬 **ISMS-P의보호대책요구사항**전체가완성된다는점에서, 두답안이 \*\*"접근통제의두축(주체중심 vs 목표중심)"\*\*으로 서로를완성하는 결론으로마무리됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "보안 모델의 역사는 '기밀성'과 '무결성'의 숨바꼭질이다. 가장 먼저 군대(국방)에서 만든 \*\*'벨-라파듈라(BLP)'\*\*를 보자. 이 녀석의 목적은 오직 하나, '기밀 유출 방지'다. 이등병은 장군 문서를 못 읽게 막고(No Read Up), 장군이 실수로 1급 기밀을 일반 게시판에 복사(쓰기)하는 것을 막는다(No Write Down). 기밀성은 완벽히 지켰지만, 이등병이 장군 문서에 몰래 쓰레기 값을 쓰는(위조하는) 것은 막지 못했다. (무결성 붕괴). 그래서 이를 180도 뒤집어버린 **'비바(Biba)'** 모델이 등장했다. 비바의 목적은 '무결성(오염 방지)'이다. 깨끗한 물에 흙탕물을 섞지 않는다는 철학이다. 이등병이 감히 장군 문서에 손대는 것을 막고(No Write Up), 반대로 장군이 이등병의 엉터리 보고서를 읽어버리고 오판하는 것을 막는다(No Read Down). 즉, BLP와 규칙이 완벽히 반대다. 하지만 상업용 은행에서는 비바 모델의 룰 만으로는 부족했다. 그래서 나온 정교한 모델이 \*\*'클락-윌슨(Clark-Wilson)'\*\*이다. 은행원이 고객 계좌 숫자를 직접 더블클릭해서 수정하는 걸 막고, 오직 인가된 '송금 프로그램(트랜잭션)'을 통해서만 DB를 건드리게 만들었다(임무 분리와 트랜잭션). 마지막으로, 주식 시장이나 컨설팅 회사에 꼭 필요한 \*\*'만리장성 모델(Chinese Wall / Brewer-Nash)'\*\*이 있다. 한 직원이 코카콜라의 기밀을 열람했다면, 시스템이 그 즉시 만리장성을 쳐버려서 경쟁사인 펩시콜라의 데이터에는 절대 접근하지 못하게 막는다. 즉, '이해충돌'과 스파이 짓을 막는 최고의 상업용 모델이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 기밀성과 무결성의 숨바꼭질, 보안 모델 4대장 개요**

* **정의:** 운영체제나 데이터베이스 등에서 강제 접근 통제(MAC) 정책을 시스템에 수학적, 논리적으로 구현하기 위해 설계된 정형화된 보안 체계 모델.
* **분류 기준:** 해당 모델이 정보보안 3요소(CIA) 중 **'무엇(기밀성, 무결성, 이해충돌 방지)'을 1순위로 지키고자 탄생했느냐**에 따라 4가지 대표 모델로 나뉨.

#### **II. \[본론 1] BLP(기밀성) vs Biba(무결성)의 정반대 통제 파이프라인 (도식화)**

어째서 BLP는 하향 쓰기를 막고, Biba는 상향 쓰기를 막는지 그 방향을 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2OTEuOTYgNDY3LjYiIHdpZHRoPSI2OTEuOTYiIGhlaWdodD0iNDY3LjYiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IkJMUF9CaWJhX19UcmFkZW9mZl9fIiBkYXRhLWxhYmVsPSJCTFDsmYAgQmliYSDrqqjrjbjsnZgg7KCV67CY64yAKFRyYWRlLW9mZikg66OwIOyytOqzhCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNjExLjk2IiBoZWlnaHQ9IjM4Ny42IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNjExLjk2IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+QkxQ7JmAIEJpYmEg66qo64247J2YIOygleuwmOuMgChUcmFkZS1vZmYpIOujsCDssrTqs4Q8L3RleHQ+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iQkxQX19fXyIgZGF0YS1sYWJlbD0iQkxQIOuqqOuNuCAo6riw67CA7ISxIOyImO2YuCkg8J+boe+4jyI+CiAgPHJlY3QgeD0iNTYiIHk9IjI1Ny44IiB3aWR0aD0iNTc5Ljk2IiBoZWlnaHQ9IjE1My44IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNTYiIHk9IjI1Ny44IiB3aWR0aD0iNTc5Ljk2IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI2OCIgeT0iMjcxLjgiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+QkxQIOuqqOuNuCAo6riw67CA7ISxIOyImO2YuCkg8J+boe+4jzwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IkJpYmFfX19fIiBkYXRhLWxhYmVsPSJCaWJhIOuqqOuNuCAo66y06rKw7ISxIOyImO2YuCkg4pyoIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSI1NTAuNTg0MDAwMDAwMDAwMSIgaGVpZ2h0PSIxNTMuOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjU1MC41ODQwMDAwMDAwMDAxIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI2OCIgeT0iOTgiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+QmliYSDrqqjrjbggKOustOqysOyEsSDsiJjtmLgpIOKcqDwvdGV4dD4KPC9nPgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJVMSIgZGF0YS10bz0iQl9ISUdIIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iTm8gUmVhZCBVcCDinYwK7J2065Ox67OR7J2AIDHquIkg6riw67CAIOuquyDsnb3snYwiIHBvaW50cz0iMTkwLjI3MywzMjAuMjUgNDI0LjIyNzAwMDAwMDAwMDAzLDMyMC4yNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJVMiIgZGF0YS10bz0iQl9MT1ciIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSJObyBXcml0ZSBEb3duIOKdjArsnqXqtbDsnbQgMeq4iSDquLDrsIDsnYQg67CR7Jy866GcIOycoOy2nCDquIjsp4AiIHBvaW50cz0iMTkwLjI3MywzNzcuMTUwMDAwMDAwMDAwMDMgNDczLjUyOSwzNzcuMTUwMDAwMDAwMDAwMDMiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVTMiIGRhdGEtdG89IkJJX0hJR0giIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSJObyBXcml0ZSBVcCDinYwK7J2065Ox67OR7J20IOyepeq1sCDrrLjshJwg7JyE7KGwIOq4iOyngCIgcG9pbnRzPSIxOTAuMjczLDE0Ni40NSA0NDUuNjExMDAwMDAwMDAwMDUsMTQ2LjQ1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlU0IiBkYXRhLXRvPSJCSV9MT1ciIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSJObyBSZWFkIERvd24g4p2MCuyepeq1sOydtCDsl4nthLDrpqwg7LCM65287IucIOywuOyhsCDquIjsp4AiIHBvaW50cz0iMTkwLjI3MywyMDMuMzUwMDAwMDAwMDAwMDIgNDU3LjQ5MTAwMDAwMDAwMDA0LDIwMy4zNTAwMDAwMDAwMDAwMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlUxIiBkYXRhLXRvPSJCX0hJR0giIGRhdGEtbGFiZWw9Ik5vIFJlYWQgVXAg4p2MCuydtOuTseuzkeydgCAx6riJIOq4sOuwgCDrqrsg7J297J2MIj4KICA8cmVjdCB4PSIyMzQuMjcyOTk5OTk5OTk5OTciIHk9IjI5Ny4yNSIgd2lkdGg9IjE0NS45NTQwMDAwMDAwMDAwNCIgaGVpZ2h0PSI0NC42IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjMwNy4yNSIgeT0iMzE5LjU1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIj48dHNwYW4geD0iMzA3LjI1IiBkeT0iLTMuMzAwMDAwMDAwMDAwMDAwNyI+Tm8gUmVhZCBVcCDinYw8L3RzcGFuPjx0c3BhbiB4PSIzMDcuMjUiIGR5PSIxNC4zIj7snbTrk7Hrs5HsnYAgMeq4iSDquLDrsIAg66q7IOydveydjDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlUyIiBkYXRhLXRvPSJCX0xPVyIgZGF0YS1sYWJlbD0iTm8gV3JpdGUgRG93biDinYwK7J6l6rWw7J20IDHquIkg6riw67CA7J2EIOuwkeycvOuhnCDsnKDstpwg6riI7KeAIj4KICA8cmVjdCB4PSIyMzQuMjczIiB5PSIzNTQuMTUwMDAwMDAwMDAwMDMiIHdpZHRoPSIxOTUuMjU2MDAwMDAwMDAwMDMiIGhlaWdodD0iNDQuNiIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzMzEuOTAxIiB5PSIzNzYuNDUwMDAwMDAwMDAwMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSIzMzEuOTAxIiBkeT0iLTMuMzAwMDAwMDAwMDAwMDAwNyI+Tm8gV3JpdGUgRG93biDinYw8L3RzcGFuPjx0c3BhbiB4PSIzMzEuOTAxIiBkeT0iMTQuMyI+7J6l6rWw7J20IDHquIkg6riw67CA7J2EIOuwkeycvOuhnCDsnKDstpwg6riI7KeAPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iVTMiIGRhdGEtdG89IkJJX0hJR0giIGRhdGEtbGFiZWw9Ik5vIFdyaXRlIFVwIOKdjArsnbTrk7Hrs5HsnbQg7J6l6rWwIOusuOyEnCDsnITsobAg6riI7KeAIj4KICA8cmVjdCB4PSIyMzQuMjcyOTk5OTk5OTk5OTciIHk9IjEyMy40NSIgd2lkdGg9IjE2Ny4zMzgwMDAwMDAwMDAwNSIgaGVpZ2h0PSI0NC42IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjMxNy45NDIiIHk9IjE0NS43NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSI+PHRzcGFuIHg9IjMxNy45NDIiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij5ObyBXcml0ZSBVcCDinYw8L3RzcGFuPjx0c3BhbiB4PSIzMTcuOTQyIiBkeT0iMTQuMyI+7J2065Ox67OR7J20IOyepeq1sCDrrLjshJwg7JyE7KGwIOq4iOyngDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlU0IiBkYXRhLXRvPSJCSV9MT1ciIGRhdGEtbGFiZWw9Ik5vIFJlYWQgRG93biDinYwK7J6l6rWw7J20IOyXie2EsOumrCDssIzrnbzsi5wg7LC47KGwIOq4iOyngCI+CiAgPHJlY3QgeD0iMjM0LjI3Mjk5OTk5OTk5OTk3IiB5PSIxODAuMzUiIHdpZHRoPSIxNzkuMjE4MDAwMDAwMDAwMDUiIGhlaWdodD0iNDQuNiIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzMjMuODgyIiB5PSIyMDIuNjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSIzMjMuODgyIiBkeT0iLTMuMzAwMDAwMDAwMDAwMDAwNyI+Tm8gUmVhZCBEb3duIOKdjDwvdHNwYW4+PHRzcGFuIHg9IjMyMy44ODIiIGR5PSIxNC4zIj7snqXqtbDsnbQg7JeJ7YSw66asIOywjOudvOyLnCDssLjsobAg6riI7KeAPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkJfSElHSCIgZGF0YS1sYWJlbD0iVG9wIFNlY3JldCDqsJ3ssrQiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDI0LjIyNzAwMDAwMDAwMDAzIiB5PSIzMDEuOCIgd2lkdGg9IjEzOS43NjIiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0OTQuMTA4MDAwMDAwMDAwMDYiIHk9IjMyMC4yNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+VG9wIFNlY3JldCDqsJ3ssrQ8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkJfTE9XIiBkYXRhLWxhYmVsPSJVbmNsYXNzaWZpZWQg6rCd7LK0IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQ3My41MjkiIHk9IjM1OC43MDAwMDAwMDAwMDAwNSIgd2lkdGg9IjE0Ni40MzA5OTk5OTk5OTk5OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjU0Ni43NDQ1IiB5PSIzNzcuMTUwMDAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlVuY2xhc3NpZmllZCDqsJ3ssrQ8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlUxIiBkYXRhLWxhYmVsPSLsgqzsmqnsnpAg7KO87LK0IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjcyIiB5PSIzMDEuOCIgd2lkdGg9IjExOC4yNzMiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMzEuMTM2NSIgeT0iMzIwLjI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7sgqzsmqnsnpAg7KO87LK0PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJVMiIgZGF0YS1sYWJlbD0i7IKs7Jqp7J6QIOyjvOyytCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3MiIgeT0iMzU4LjcwMDAwMDAwMDAwMDA1IiB3aWR0aD0iMTE4LjI3MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEzMS4xMzY1IiB5PSIzNzcuMTUwMDAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyCrOyaqeyekCDso7zssrQ8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkJJX0hJR0giIGRhdGEtbGFiZWw9IuqzoOustOqysOyEsSDqsJ3ssrQiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDQ1LjYxMTAwMDAwMDAwMDA1IiB5PSIxMjgiIHdpZHRoPSIxMzMuMDkzMDAwMDAwMDAwMDIiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1MTIuMTU3NSIgeT0iMTQ2LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7qs6DrrLTqsrDshLEg6rCd7LK0PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJCSV9MT1ciIGRhdGEtbGFiZWw9IuyggOustOqysOyEsSDqsJ3ssrQiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDU3LjQ5MTAwMDAwMDAwMDA0IiB5PSIxODQuOSIgd2lkdGg9IjEzMy4wOTMwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjUyNC4wMzc1IiB5PSIyMDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyggOustOqysOyEsSDqsJ3ssrQ8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlUzIiBkYXRhLWxhYmVsPSLsgqzsmqnsnpAg7KO87LK0IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjcyIiB5PSIxMjgiIHdpZHRoPSIxMTguMjczIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTMxLjEzNjUiIHk9IjE0Ni40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7IKs7Jqp7J6QIOyjvOyytDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iVTQiIGRhdGEtbGFiZWw9IuyCrOyaqeyekCDso7zssrQiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNzIiIHk9IjE4NC45IiB3aWR0aD0iMTE4LjI3MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEzMS4xMzY1IiB5PSIyMDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyCrOyaqeyekCDso7zssrQ8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 보안 모델 4대장 전격 해부 (3단 표 - 출제 1순위)**

각 모델이 수호하는 \*\*'핵심 목표'\*\*와 이를 달성하기 위한 \*\*'고유의 통제 규칙(키워드)'\*\*을 정확히 찌르는 것이 가장 중요합니다.

| **보안 모델 명칭**                                    | **모델의 탄생 배경 및 보호하는 '핵심 목표'**                                                                | **통제 메커니즘 (핵심 키워드 및 룰)**                                                                                                                   |
| :---------------------------------------------- | :------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Bell-LaPadula** **BLP (벨-라파듈라)**           | 군대, 국방부 등 군사적 환경에서 군사 기밀이 하위 계층으로 새어나가는 것을 막기 위함. ➔ **오직 "기밀성(Confidentiality)" 유지.**       | - **단순 보안 속성 (Simple Security):** 상향 읽기 금지 (No Read Up). - **스타 속성 (\*-Property):** 하향 쓰기 금지 (No Write Down). *(단점: 무결성은 빵점임. 위조는 막지 못함).* |
| **2. Biba** **(비바 모델)**                         | BLP가 무결성을 보장하지 못하는 단점을 해결하기 위해 완전히 정반대로 설계된 모델. ➔ **오직 "무결성(Integrity)" 유지.**               | - **단순 무결성 속성:** 하향 읽기 금지 (No Read Down). 더러운 정보 참조 금지. - **무결성 스타 속성:** 상향 쓰기 금지 (No Write Up). 위로 갈수록 수정 불가.                             |
| **3. Clark-Wilson** **(클락-윌슨)**                 | 무결성이 가장 중요한 금융권, 상업용 환경에서 비바(Biba) 모델보다 더 정교한 통제를 위해 등장. ➔ **"비즈니스 무결성 및 변조 방지".**          | - 사용자가 객체(데이터)에 직접 접근 불가. - 반드시 \*\*'검증된 프로그램(트랜잭션)'\*\*을 통해서만 접근하도록 강제함. - **직무 분리(Separation of Duty)** 원칙 적용.                           |
| **4. 만리장성 모델** **(Chinese Wall / Brewer-Nash)** | 회계법인, 컨설팅 회사 등에서 내부자가 얻은 정보로 경쟁사 간 스파이 짓을 하는 것을 차단함. ➔ **"이해충돌(Conflict of Interest) 방지".** | - 사용자가 그룹 A의 데이터에 접근(Read)하는 순간, 시스템이 즉각 만리장성을 쳐서 **경쟁 그룹 B의 데이터에 대한 접근을 원천 차단**해 버림.                                                      |

#### **IV. \[결론/제언] 정보보안 3요소(CIA)의 밸런스와 하이브리드 보안 모델의 필요성**

* **(키워드 위주 2줄 마무리)** "BLP는 기밀성을, 비바(Biba)는 무결성을 극단적으로 추구하다 보니 양쪽 모두 현실의 비즈니스 요건을 100% 충족시키지는 못했습니다. 현대 운영체제와 클라우드 인프라는 이들의 단일적 한계를 극복하기 위해, **기밀성과 무결성을 동시에 보호하면서도 ABAC 같은 동적 제어를 결합한 다차원 하이브리드(Hybrid) 보안 접근 통제 아키텍처로 진화**하고 있습니다."
