### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (보호대상의차이, 근본철학의차이) — 3~4줄
Ⅱ. DRM 핵심원리 (본론①, 도식 1개 필수)
Ⅲ. DLP 핵심원리 (본론②, 핵심 배점)
Ⅳ. 비교및조합전략
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬여러암호화기법(대칭/비대칭암호,전자봉투)이 '데이터를어떻게암호화할지'를다뤘는데, DRM과DLP는그암호화기술을 서로다른목적으로적용한다 — DRM은 '콘텐츠자체에 평생꺼지지않는자물쇠를건다'는것이고, DLP는 '데이터가조직밖으로나가는순간을감시해서차단한다'는것"\*\*이라는 한줄로시작하면, 왜둘이 자주혼동되지만 근본적으로다른지 드러납니다.

### Ⅱ. DRM 핵심원리 — 콘텐츠자체에영원히내재된보호

| 항목       | 내용                                                              |
| :------- | :-------------------------------------------------------------- |
| **보호대상** | **콘텐츠(문서,영상,음원등)자체**                                            |
| **적용방식** | 콘텐츠를 **암호화**하고, **사용권한(보기,인쇄,복사여부)을파일에영구적으로내재화**                |
| **핵심특징** | 파일이 **어디로이동해도**(USB,이메일첨부등) 권한이 **따라다님**(Persistent Protection) |
| **대표사례** | 전자책의 **인쇄·복사방지**,영화스트리밍의 **다운로드제한**,기업문서의 **외부유출후에도열람불가**       |

→ 암기: **"콘텐츠에권한을심어서, 어디로가든그권한이그대로따라다닌다"** — 앞서다룬 \*\*"전자봉투"\*\*의구조와유사하게, DRM도 \*\*"콘텐츠(편지)+권한정보(열쇠)"\*\*를 **하나로묶어서**배포합니다.

### 도식화 제안

```
[DRM 적용문서]
[암호화된콘텐츠 + 사용권한(보기O,인쇄X,복사X)]
     ↓ 어디로이동해도 함께따라다님
[USB로복사] → 그대로암호화+권한유지
[이메일첨부] → 그대로암호화+권한유지
[외부PC에서열기] → 권한서버에확인 → 권한없으면 열람불가
```

### Ⅲ. DLP 핵심원리 — 데이터흐름의감시와차단, 핵심 배점

**함정 방지: "유출을막는다"고만답하면절반. DRM과는"보호방식자체가다르다"는점 —콘텐츠에심는게아니라, "흐름을감시"한다는것을보여줘야완성됩니다.**

| 항목       | 내용                                                                    |
| :------- | :-------------------------------------------------------------------- |
| **보호대상** | **데이터의이동경로**(네트워크,이메일,USB,클립보드등)                                      |
| **적용방식** | 데이터에 **직접권한을심지않고**, **콘텐츠의패턴을분석**(주민번호,신용카드번호,키워드등)해 **정책위반시전송자체를차단** |
| **핵심특징** | 앞서다룬 **SIEM/UEBA**와유사하게, **"어디로,무엇이나가는지"를실시간감시**                      |
| **대표사례** | 이메일에 **주민번호패턴**포함시 **자동차단**,USB로 **대량파일복사시경고**                        |

→ 암기: **"콘텐츠자체를잠그는게아니라, 그콘텐츠가나가는길목을지킨다"** — 앞서다룬 \*\*"네트워크스캐닝→SIEM→SOAR"\*\*의 **감시-탐지-대응흐름**이, DLP에서는 \*\*"데이터유출시도감시-패턴탐지-전송차단"\*\*으로 재현됩니다.

### 도식화 제안

```
[DLP 감시체계]
[사용자PC] → 이메일작성(주민번호패턴포함)
                ↓
        [DLP엔진] 패턴검사 "민감정보포함!"
                ↓
        [정책위반] → 전송자동차단 + 관리자경고
        
(콘텐츠자체가아니라, "지금나가려는행위"를감시)
```

### Ⅳ. 비교 및 조합전략

**함정 방지: "둘중하나만쓴다"고하면절반. 앞서다룬여러조합전략(전자봉투,연합학습+차분프라이버시등)처럼 함께쓰는게실무라는점을보여줘야완성됩니다.**

| 구분                      | **DRM**                          | **DLP**                     |
| :---------------------- | :------------------------------- | :-------------------------- |
| **보호시점**                | **콘텐츠생성시부터영구적**                  | **이동/전송시점에감시**              |
| **보호범위**                | **이미유출된후에도**작동(암호화가 계속유지)        | **유출되기전차단**(유출후엔무력)         |
| **오탐(FalsePositive)위험** | 낮음(권한기반이라명확)                     | **있음**(패턴이비슷하면 정상문서도차단될수있음) |
| **한계**                  | **권한서버가없어지면 콘텐츠자체가못열림**(장기보존리스크) | **암호화된채로유출되면 내용을못보므로 검사불가** |

**조합전략(실무핵심)**: 앞서다룬 **"AI에게개인정보를입력하지않도록DLP연동으로기술적차단"**(N2SF답안)처럼, 실무에서는 **DLP로 1차감시**하다가, **핵심기밀문서는DRM으로 2차보호**하는 **계층적조합**이 일반적입니다 — DLP가막지못한(암호화되어통과한) 유출이라도, DRM이걸려있으면 **유출된후에도열람자체가불가능**합니다.

### 도식화 제안

```
[1차방어: DLP] "나가려는데이터의패턴을감시,의심되면차단"
     ↓ (그래도일부통과할경우)
[2차방어: DRM] "설령유출돼도, 콘텐츠자체가암호화+권한제한돼있어 못열림"
```

### Ⅴ. 결론

DRM과DLP는 \*\*"데이터를보호하는서로다른철학"\*\*입니다 — DRM은 \*\*"콘텐츠자체에영구적자물쇠를걸어, 유출된후에도무력화되지않게"\*\*하고, DLP는 \*\*"데이터가나가는순간을감시해, 애초에유출자체를막으려"\*\*합니다 — 앞서다룬 **"1차방어-2차방어의계층적구조"**(DDoS방어,제로트러스트등)와 마찬가지로, 실무에서는 \*\*"DLP(사전차단)+DRM(사후보호)"\*\*를 **함께조합**해야 오늘하루다룬 **인포스틸러,공급망공격**같은 다양한유출경로에 대해 **빈틈없는방어**를 구축할수있습니다.

### **1. 답안 전개 스토리**

> "직원들이 회사 기밀이나 고객 정보를 훔쳐 가는 것을 막기 위해 기업이 쓰는 방패는 크게 두 가지다. 하나는 기밀문서가 든 \*\*'서류 가방 자체에 자물쇠를 채우는 DRM'\*\*이고, 다른 하나는 회사 건물 출입구에 \*\*'공항 검색대를 설치해 서류를 뺏는 DLP'\*\*다. **DRM**은 직원이 엑셀 문서를 만드는 순간 강력한 암호(자물쇠)로 꽉 잠가버린다. 직원이 몰래 파일을 훔쳐서 집으로 가져가도 자물쇠가 걸려있어 열어볼 수 없다. 유출되어도 안전하다는 최강의 장점이 있지만, 엑셀이 업데이트될 때마다 자물쇠 프로그램과 충돌이 일어나 PC가 뻗는 단점이 있다. 반면 **DLP**는 파일을 잠그지 않고 놔둔다. 대신 직원이 이 파일을 USB에 담거나 메일로 첨부해 밖으로 나가려는 찰나의 순간, 검색대가 내용을 스캔해 기밀문서면 '차단!'을 외친다. 프로그램 충돌이 없어 가볍지만, 만약 해커나 직원이 꼼수로 검색대를 통과해 파일을 밖으로 빼돌리면 자물쇠가 없으므로 누구나 활짝 열어볼 수 있다는 치명적 단점이 있다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 내부자 정보 유출 방지를 위한 창과 방패, DRM과 DLP 개요**

* **DRM (Digital Rights Management, 문서 암호화):** 전자 문서 자체를 생성 시점부터 암호화하고, 열람/편집/인쇄/캡처 등 사용자의 권한을 세밀하게 통제하여 **문서의 생애 주기(Life Cycle) 전체를 보호**하는 기술.
* **DLP (Data Loss Prevention, 데이터 유출 방지):** 기업의 네트워크, 엔드포인트(PC), 스토리지 등 데이터를 외부로 유출할 수 있는 **'모든 이동 경로(통로)'를 실시간으로 감시**하고, 중요 데이터(주민번호, 기밀 키워드) 발견 시 유출을 차단하는 기술.

#### **II. \[본론 1] (단순화 버전) 자물쇠(DRM) vs 공항 검색대(DLP)의 유출 방어 파이프라인 (도식화)**

두 기술이 유출 시도를 막아내는 서로 다른 방어 메커니즘을 직관적으로 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NzEuMDcwOTk5OTk5OTk5OTcgMTIxMi4wMTYiIHdpZHRoPSI0NzEuMDcwOTk5OTk5OTk5OTciIGhlaWdodD0iMTIxMi4wMTYiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IkRSTV92c19ETFBfX19fIiBkYXRhLWxhYmVsPSJEUk0gdnMgRExQIOygleuztCDsnKDstpwg67Cp7Ja0IOuplOy7pOuLiOymmCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMzYzLjA3MDk5OTk5OTk5OTk3IiBoZWlnaHQ9IjExMzIuMDE2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMzYzLjA3MDk5OTk5OTk5OTk3IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+RFJNIHZzIERMUCDsoJXrs7Qg7Jyg7LacIOuwqeyWtCDrqZTsu6Tri4jsppg8L3RleHQ+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMV9EUk1fRGlnaXRhbF9SaWdodHNfTWFuYWdlbWVudCIgZGF0YS1sYWJlbD0iMS4gRFJNIChEaWdpdGFsIFJpZ2h0cyBNYW5hZ2VtZW50KSI+CiAgPHJlY3QgeD0iMTQ2Ljg0OSIgeT0iOTQiIHdpZHRoPSIyMTYuMjIxOTk5OTk5OTk5OTgiIGhlaWdodD0iNDIwLjIiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSIxNDYuODQ5IiB5PSI5NCIgd2lkdGg9IjIxNi4yMjE5OTk5OTk5OTk5OCIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTU4Ljg0OSIgeT0iMTA4IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjEuIERSTSAoRGlnaXRhbCBSaWdodHMgTWFuYWdlbWVudCk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSIyX0RMUF9EYXRhX0xvc3NfUHJldmVudGlvbiIgZGF0YS1sYWJlbD0iMi4gRExQIChEYXRhIExvc3MgUHJldmVudGlvbikiPgogIDxyZWN0IHg9IjE0Ni44NDkiIHk9IjU5OS4xIiB3aWR0aD0iMjE2LjIyMTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjU1Ni45MTYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSIxNDYuODQ5IiB5PSI1OTkuMSIgd2lkdGg9IjIxNi4yMjE5OTk5OTk5OTk5OCIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTU4Ljg0OSIgeT0iNjEzLjEiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+Mi4gRExQIChEYXRhIExvc3MgUHJldmVudGlvbik8L3RleHQ+CjwvZz4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRE9DIiBkYXRhLXRvPSJEUk0iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzYzLjA3MDk5OTk5OTk5OTk3LDU1NC41IDM3NS4wNzA5OTk5OTk5OTk5Nyw1NTQuNSAzNzUuMDcwOTk5OTk5OTk5OTcsMzE5LjI1IDQwMy4wNzA5OTk5OTk5OTk5NywzMTkuMjUgNDIzLjA3MDk5OTk5OTk5OTk3LDMxOS4yNSA0MjMuMDcwOTk5OTk5OTk5OTcsMjc5LjI1IDMzNS4wNzA5OTk5OTk5OTk5NywyNzkuMjUgMzM1LjA3MDk5OTk5OTk5OTk3LDQ0IDIxNC45NTk5OTk5OTk5OTk5OCw0NCAyMTQuOTU5OTk5OTk5OTk5OTgsNTQgNDIzLjA3MDk5OTk5OTk5OTk3LDU0IDQyMy4wNzA5OTk5OTk5OTk5NywxMzkuNDUgMjU0Ljk1OTk5OTk5OTk5OTk4LDEzOS40NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRE9DIiBkYXRhLXRvPSJETFAiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzYzLjA3MDk5OTk5OTk5OTk3LDU2Ni44MDAwMDAwMDAwMDAxIDM3NS4wNzA5OTk5OTk5OTk5Nyw1NjYuODAwMDAwMDAwMDAwMSAzNzUuMDcwOTk5OTk5OTk5OTcsNTc3Ljk1IDQwMy4wNzA5OTk5OTk5OTk5Nyw1NzcuOTUgMjAsNTc3Ljk1IDIwLDUzNy45NSAzMzUuMDcwOTk5OTk5OTk5OTcsNTM3Ljk1IDMzNS4wNzA5OTk5OTk5OTk5Nyw1NDkuMSAyMTQuOTU5OTk5OTk5OTk5OTgsNTQ5LjEgMjE0Ljk1OTk5OTk5OTk5OTk4LDU1OS4xIDIwLDU1OS4xIDIwLDY0MS42NSAyNTQuOTU5OTk5OTk5OTk5OTgsNjQxLjY1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJEUk0iIGRhdGEtdG89Ik9VVDEiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLtlbTsu6TqsIAg7ZuU7LOQ7IScIOynkeycvOuhnCDqsIDsoLjqsJAiIHBvaW50cz0iMjU0Ljk1OTk5OTk5OTk5OTk4LDE3Ni4zNSAyNTQuOTU5OTk5OTk5OTk5OTgsMjkxLjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iT1VUMSIgZGF0YS10bz0iRkFJTDEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyWtOywqO2UvCDslZTtmLjtmZTrkJjslrQg7J6I7J2MIiBwb2ludHM9IjI1NC45NTk5OTk5OTk5OTk5OCwzMjguMSAyNTQuOTU5OTk5OTk5OTk5OTgsNDQ0LjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkRMUCIgZGF0YS10bz0iR0FURSIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IlVTQuuCmCDrqZTsnbzroZwK67m864+M66as66CkIOyLnOuPhCEiIHBvaW50cz0iMjU0Ljk1OTk5OTk5OTk5OTk4LDY3OC41NSAyNTQuOTU5OTk5OTk5OTk5OTgsODEwLjYiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iR0FURSIgZGF0YS10bz0iQkxPQ0siIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iuq4sOuwgCDtgqTsm4zrk5wg67Cc6rKsISIgcG9pbnRzPSIyNTQuOTU5OTk5OTk5OTk5OTgsOTY5LjkxNiAyNTQuOTU5OTk5OTk5OTk5OTgsMTA4Ni4yMTYwMDAwMDAwMDAxIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkRSTSIgZGF0YS10bz0iT1VUMSIgZGF0YS1sYWJlbD0i7ZW07Luk6rCAIO2blOyzkOyEnCDsp5HsnLzroZwg6rCA7KC46rCQIj4KICA8cmVjdCB4PSIxNzEuOTU5OTk5OTk5OTk5OTgiIHk9IjIxNy45IiB3aWR0aD0iMTY1LjU1NjAwMDAwMDAwMDA0IiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjU0LjczOCIgeT0iMjMzLjA1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7tlbTsu6TqsIAg7ZuU7LOQ7IScIOynkeycvOuhnCDqsIDsoLjqsJA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iT1VUMSIgZGF0YS10bz0iRkFJTDEiIGRhdGEtbGFiZWw9IuyWtOywqO2UvCDslZTtmLjtmZTrkJjslrQg7J6I7J2MIj4KICA8cmVjdCB4PSIxODQuNDU5OTk5OTk5OTk5OTgiIHk9IjM3MS4xIiB3aWR0aD0iMTQwLjAxNCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjI1NC40NjY5OTk5OTk5OTk5OCIgeT0iMzg2LjI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7slrTssKjtlLwg7JWU7Zi47ZmU65CY7Ja0IOyeiOydjDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJETFAiIGRhdGEtdG89IkdBVEUiIGRhdGEtbGFiZWw9IlVTQuuCmCDrqZTsnbzroZwK67m864+M66as66CkIOyLnOuPhCEiPgogIDxyZWN0IHg9IjIwNy45NTk5OTk5OTk5OTk5OCIgeT0iNzIzLjAwMDAwMDAwMDAwMDEiIHdpZHRoPSI5My4wODgwMDAwMDAwMDAwMiIgaGVpZ2h0PSI0NC42IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjI1NC41MDQiIHk9Ijc0NS4zMDAwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIj48dHNwYW4geD0iMjU0LjUwNCIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPlVTQuuCmCDrqZTsnbzroZw8L3RzcGFuPjx0c3BhbiB4PSIyNTQuNTA0IiBkeT0iMTQuMyI+67m864+M66as66CkIOyLnOuPhCE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJHQVRFIiBkYXRhLXRvPSJCTE9DSyIgZGF0YS1sYWJlbD0i6riw67CAIO2CpOybjOuTnCDrsJzqsqwhIj4KICA8cmVjdCB4PSIyMDEuNDU5OTk5OTk5OTk5OTgiIHk9IjEwMTIuOTE2IiB3aWR0aD0iMTA2Ljc1MDAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjU0LjgzNDk5OTk5OTk5OTk4IiB5PSIxMDI4LjA2NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+6riw67CAIO2CpOybjOuTnCDrsJzqsqwhPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJET0MiIGRhdGEtbGFiZWw9Iu2ajOyCrCDquLDrsIAg66y47IScIPCfk4QiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjEwLjcxMTk5OTk5OTk5OTk2IiB5PSI1NDIuMiIgd2lkdGg9IjE1Mi4zNTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI4Ni44OTE0OTk5OTk5OTk5NSIgeT0iNTYwLjY1MDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPu2ajOyCrCDquLDrsIAg66y47IScIPCfk4Q8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkRSTSIgZGF0YS1sYWJlbD0iRFJNIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjcwLjg0ODk5OTk5OTk5OTk5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjkxLjQyNDUiIHk9IjEwMi40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+RFJNPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJETFAiIGRhdGEtbGFiZWw9IkRMUCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iMTM5LjQ1IiB3aWR0aD0iNjguNjI1OTk5OTk5OTk5OTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjkwLjMxMjk5OTk5OTk5OTk5IiB5PSIxNTcuODk5OTk5OTk5OTk5OTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkRMUDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRFJNIiBkYXRhLWxhYmVsPSJEUk0iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjE5LjUzNTQ5OTk5OTk5OTk4IiB5PSIxMzkuNDUiIHdpZHRoPSI3MC44NDg5OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIyNTQuOTU5OTk5OTk5OTk5OTgiIHk9IjE1Ny44OTk5OTk5OTk5OTk5OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+RFJNPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJPVVQxIiBkYXRhLWxhYmVsPSLtjIzsnbwg7Jyg7LacIOyEseqztSDwn4+D4oCN4pmC77iPIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjE2My45NjA0OTk5OTk5OTk5NyIgeT0iMjkxLjIiIHdpZHRoPSIxODEuOTk5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyNTQuOTU5OTk5OTk5OTk5OTgiIHk9IjMwOS42NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7YyM7J28IOycoOy2nCDshLHqs7Ug8J+Pg+KAjeKZgu+4jzwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRkFJTDEiIGRhdGEtbGFiZWw9Iu2MjOydvCDsl7Trnowg7KCI64yAIOu2iOqwgCDinYwK6riw67CAIOuztO2YuCDshLHqs7UhIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjE2Mi44NDkiIHk9IjQ0NC40IiB3aWR0aD0iMTg0LjIyMTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjI1NC45NTk5OTk5OTk5OTk5OCIgeT0iNDcxLjI5OTk5OTk5OTk5OTk1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIyNTQuOTU5OTk5OTk5OTk5OTgiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7tjIzsnbwg7Je0656MIOygiOuMgCDrtojqsIAg4p2MPC90c3Bhbj48dHNwYW4geD0iMjU0Ljk1OTk5OTk5OTk5OTk4IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7quLDrsIAg67O07Zi4IOyEseqztSE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRExQIiBkYXRhLWxhYmVsPSJETFAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjIwLjY0NyIgeT0iNjQzLjEiIHdpZHRoPSI2OC42MjU5OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjU0Ljk1OTk5OTk5OTk5OTk4IiB5PSI2NjEuNTUwMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+RExQPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJHQVRFIiBkYXRhLWxhYmVsPSJETFAg6rKA7IOJ64yAIPCfmqgK64K07JqpIOyKpOy6lCDqsoDsgqwiIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iMjU0Ljk1OTk5OTk5OTk5OTk4LDgxMC42IDMzNC42MTgsODkwLjI1OCAyNTQuOTU5OTk5OTk5OTk5OTgsOTY5LjkxNiAxNzUuMzAxOTk5OTk5OTk5OTYsODkwLjI1OCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIyNTQuOTU5OTk5OTk5OTk5OTgiIHk9Ijg5MC4yNTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjI1NC45NTk5OTk5OTk5OTk5OCIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPkRMUCDqsoDsg4nrjIAg8J+aqDwvdHNwYW4+PHRzcGFuIHg9IjI1NC45NTk5OTk5OTk5OTk5OCIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+64K07JqpIOyKpOy6lCDqsoDsgqw8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQkxPQ0siIGRhdGEtbGFiZWw9IuycoOy2nCDtlonsnIQg7KaJ7IucIOywqOuLqCDwn6exCuq4sOuwgCDrs7TtmLgg7ISx6rO1ISIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxNjIuODQ5IiB5PSIxMDg2LjIxNjAwMDAwMDAwMDEiIHdpZHRoPSIxODQuMjIxOTk5OTk5OTk5OTgiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMjU0Ljk1OTk5OTk5OTk5OTk4IiB5PSIxMTEzLjExNjAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjI1NC45NTk5OTk5OTk5OTk5OCIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuycoOy2nCDtlonsnIQg7KaJ7IucIOywqOuLqCDwn6exPC90c3Bhbj48dHNwYW4geD0iMjU0Ljk1OTk5OTk5OTk5OTk4IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7quLDrsIAg67O07Zi4IOyEseqztSE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 암호화 방패(DRM) vs 통로 차단벽(DLP) 전격 비교 해부 (3단 표 - 출제 1순위)**

방어의 타겟과 가장 치명적인 \*\*'단점(한계점)'\*\*을 대조하여 서술하는 것이 점수 획득의 핵심입니다.

| **핵심 척도 (비교 잣대)**                 | **🔒 DRM (문서 암호화/저작권 관리)**                                                                  | **🚨 DLP (데이터 유출 방지 시스템)**                                                                                  |
| :-------------------------------- | :------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------- |
| **방어의 핵심 메커니즘 및 기본 보호 대상**        | **'데이터(파일) 그 자체에 자물쇠 채우기'.** 워드, 엑셀 등으로 문서를 저장하는 순간 암호화를 수행하여 파일의 속성 자체를 바꿔버림.              | **'데이터가 나가는 문(통로) 틀어막기'.** 파일은 건드리지 않고(평문), USB 복사, 사내 메일 발송, 클라우드 업로드 등 사용자의 '행위'를 모니터링하여 막음.              |
| **사후 통제 및 외부 유출 시의 방어력**          | **\[방어력 최강 / 사후 추적 가능 💯]** 파일이 유출되어 외부로 나가더라도 암호화되어 있어 읽을 수 없음. 권한을 회수하면 밖에서도 즉시 문서가 안 열림. | **\[방어력 취약 / 사후 통제 불가 ❌]** 교묘하게 검색대(통로)를 우회하여 밖으로 빠져나간 파일은 100% 평문이므로 누구나 열어볼 수 있고 사후 통제가 전혀 안 됨.           |
| **운영 상의 치명적 단점 및 업무 호환성 (충돌 발생)** | **'잦은 프로그램 충돌 (유지보수 지옥)'.** 한글(HWP)이나 엑셀이 업데이트될 때마다, DRM 암호화 모듈을 다시 맞춰줘야 하므로 뻑하면 프로그램이 다운됨. | **'오탐지(False Positive) 및 퍼포먼스 저하'.** 모든 파일의 내용을 실시간으로 스캔해서 검사해야 하므로, 네트워크 속도가 느려지거나 정상 업무 파일을 차단하는 오탐이 발생함. |
| **권한 제어의 세밀함**                    | 열람, 수정, 인쇄, 화면 캡처, 복사 방지 등 사용자의 행동 하나하나를 아주 정밀하게 차단할 수 있음.                                  | 파일 자체의 세밀한 캡처나 편집을 막을 수는 없음. 오직 '외부 반출' 행위만 차단함.                                                            |

#### **IV. \[결론/제언] 단일 솔루션의 한계 극복을 위한 문서중앙화(ECM)와의 결합**

* **(키워드 위주 2줄 마무리)** "DRM은 잦은 충돌로 인한 사용자 불편을, DLP는 유출 후의 사후 통제 불가라는 치명적 한계를 가집니다. 현대 기업의 랜섬웨어 방어와 무결점 기밀 유출 차단을 위해서는 이 두 가지를 혼합 운영하는 것을 넘어, **개인 PC 저장을 원천 차단하고 중앙 클라우드에서만 문서를 열람·편집하는 '문서중앙화(ECM)'로의 진화가 필수적입니다.**"
