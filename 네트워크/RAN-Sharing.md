RAN-Sharing은 오늘 다룬 "5G특화망","6G"에서 이어지는, \*\*"통신3사가 값비싼무선망장비를 어떻게나눠쓸것인가"\*\*에대한 답입니다. 마침 검색과정에서 확인된 **OpenRAN/AI-RAN**최신동향과 함께 짚어드리겠습니다.

### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (RAN공유필요성, 구축비용문제) — 3~4줄
Ⅱ. 공유방식3가지유형 (본론①, 도식 1개 필수)
Ⅲ. Open RAN - 공유를넘어선개방화, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

앞서다룬 **6G의막대한투자비용**(GaN반도체,광인터커넥트등)처럼, 무선망(RAN,RadioAccessNetwork)은 **기지국,안테나등장비구축비용이통신사수익의상당부분**을차지합니다. RAN-Sharing은 \*\*"경쟁사끼리 이비싼인프라의일부를함께쓰는것"\*\*으로, 특히 **인구밀도가낮아 개별구축이비효율적인지역**에서 활용됩니다.

### Ⅱ. 공유방식 3가지유형

| 유형                                 | 내용                                                                |
| :--------------------------------- | :---------------------------------------------------------------- |
| **수동공유**(PassiveSharing)           | **철탑,전력,공간등물리적시설만공유**,각자통신장비는따로운영 — 가장기본적,낮은수준                    |
| **능동공유**(ActiveSharing)            | **기지국장비(RAN장비)자체를공유**,주파수는각자또는공동사용 — 앞서다룬 \*\*"자원을공유"\*\*하는 더깊은결합 |
| **MOCN**(MultiOperatorCoreNetwork) | 무선망은 **완전히공유**,코어망(가입자관리등)만 각자 **별도로운영**해 요금제·서비스차별화유지            |

→ 암기: **"철탑만같이쓰거나(수동),장비를같이쓰거나(능동),무선망전체를같이쓰고코어만따로(MOCN)"** — 뒤로갈수록 **비용절감효과는커지지만, 통신사간독립성은줄어듭니다**.

### 도식화 제안

```
[수동공유]              [능동공유]              [MOCN]
철탑·전력만공유           RAN장비까지공유          무선망전체공유
각자장비따로             각자또는공동주파수         코어망만별도(차별화유지)
(낮은결합,낮은절감)                              (높은결합,높은절감)
```

### Ⅲ. Open RAN — 공유를넘어선개방화, 핵심 배점

**함정 방지: "RAN공유는2사가함께쓰는것"이라고만답하면절반. 앞서검색에서확인된OpenRAN이 "공유"와는또다른"개방화"차원의문제를푼다는걸보여줘야완성됩니다.**

| 항목                     | 내용                                                                |
| :--------------------- | :---------------------------------------------------------------- |
| **문제의식**(5G이전)         | RAN이 **폐쇄적아키텍처**— 소수대형장비업체가 **각자독자적방식**을사용,다른업체장비와호환안됨            |
| **OpenRAN의해법**         | **무선장치(O-RU),디지털장치(O-DU/CU)를분리·표준화**해, **여러업체장비를혼용가능**하게함         |
| **RIC**(RAN지능형컨트롤러)    | AI/ML로 **무선망장비의기능·운영을자동화**— LG유플러스가 **주니퍼네트웍스의RIC기술검증완료**         |
| **AI-RAN**(2026년핵심트렌드) | RIC를넘어, **AI가네트워크를스스로최적화·운영**— SKT가 **"차세대기지국AI-RAN실증성공"**(2026년) |

→ 암기: **"OpenRAN은 '누구장비든호환되게 표준화'하는것,AI-RAN은그위에서 'AI가스스로운영'하는것"** — 앞서다룬 \*\*"RAN-Sharing(비용을나눠쓰기)"\*\*과 \*\*OpenRAN(장비를표준화해호환되게)\*\*은 **"둘다비용·효율문제를풀지만, 방법이다른"** 두갈래해법입니다: **공유는같은장비를나눠쓰는것**, **개방화는다른업체장비를섞어쓸수있게하는것**입니다.

### 도식화 제안

```
[비용절감의 두갈래해법]
   ┌──────────┴──────────┐
[RAN-Sharing]              [Open RAN]
"같은장비를                 "표준화로 여러업체장비를
 여러통신사가 나눠쓴다"        혼용가능하게 해서
 (수동/능동/MOCN)             특정업체종속탈피"
                                ↓
                          [AI-RAN] AI가스스로 최적화·운영
                          (SKT 2026년 실증성공)
```

**2026년MWC경쟁구도**(최신): 엔비디아 **6G연합**(SKT참여,통신사·장비업체중심,**AI-RAN,소프트웨어기반전환**목표)과 퀄컴 **6G연합**(통신3사모두참여,**IoT·모바일기기**중심)으로 **세력이재편**되고있습니다 — 이는 \*\*"RAN을누가,어떤철학으로설계할지"\*\*를둘러싼 **표준화주도권경쟁**입니다.

### Ⅳ. 결론

RAN-Sharing은 **"통신사들이비용이많이드는무선망인프라를,수동공유→능동공유→MOCN순으로점점더깊이나눠쓰는"** 전통적해법이며, OpenRAN/AI-RAN은 이를넘어 **"장비자체를표준화해다양한업체제품을섞어쓰고,AI로자동최적화하는"** 새로운차원의효율화입니다 — 2026년MWC에서 드러난 **엔비디아vs퀄컴6G연합구도**는, 앞서다룬 **6G표준화경쟁**이 이제 \*\*"누가RAN의AI·소프트웨어기본값을선점할것인가"\*\*로 옮겨가고있음을 보여줍니다 — 이로써 캐시매핑에서시작해 실로장대했던 오늘하루의네트워크시리즈전체가, **"인프라를나눠쓰는것에서, 표준을함께만들고AI로운영하는것으로"** 진화하는 통신산업의 최신흐름으로 마무리됩니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "5G는 속도는 빠르지만 전파가 멀리 가지 못해, 인구가 적은 산골짜기(농어촌)까지 터지게 하려면 SKT, KT, LGU+가 각자 기지국 철탑을 수만 개씩 중복해서 박아야 한다. 수조 원의 돈(설비투자, CAPEX)이 날아간다. 이를 막기 위해 나온 묘수가 \*\*'RAN-Sharing (기지국 공유)'\*\*이다. '어차피 사람도 적은데 철탑 3개 박지 말고, SKT가 세운 철탑 1개에 KT와 LGU+ 폰도 같이 접속하게 하자!'는 통신 3사의 동맹이다. 공유의 수준에 따라 두 가지로 나뉜다. 첫째, \*\*'MORAN'\*\*은 철탑만 같이 쓰고 '주파수'는 통신사 각자 자기 것을 쏘는 방식이다. 둘째, \*\*'MOCN'\*\*은 철탑뿐만 아니라 **'주파수'까지 3사가 하나로 퉁쳐서 공유**하는 방식이다. 현재 대한민국의 '농어촌 5G 공동망'이 바로 이 MOCN 방식을 적용하여, 기지국 중복 투자를 막고 전국 5G 커버리지를 세계에서 가장 빠르게 확보할 수 있었다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 5G 커버리지 확대와 CAPEX 절감의 핵심, RAN-Sharing 개요**

* **정의:** 복수의 이동통신 사업자(MNO)가 철탑, 안테나, 기지국 장비(RAN) 등의 **무선 액세스 인프라를 상호 공유하여 공동으로 사용하는 네트워크 기술 및 비즈니스 모델**.
* **도입 목적:** 초고주파를 사용하는 5G 특성상 기지국 밀집 구축이 필수적인데, 농어촌 및 외곽 지역에서의 기지국 중복 구축으로 인한 막대한 설비투자(CAPEX) 및 운용비(OPEX)를 획기적으로 절감하고 친환경(탄소 배출 저감)을 실현하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 철탑 3개를 1개로 줄이는 망 공유 파이프라인**

복잡한 코어망 연결 선을 빼고, **통신 3사가 어떻게 기지국을 쪼개 쓰는지** 직관적으로 그렸습니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3NDkuMTEgNDM1LjYiIHdpZHRoPSI3NDkuMTEiIGhlaWdodD0iNDM1LjYiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IlJBTlNoYXJpbmdfMl9fXyIgZGF0YS1sYWJlbD0iUkFOLVNoYXJpbmcgMuuMgCDtlbXsi6wg67Cp7IudIOuMgOyhsCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNjY5LjExIiBoZWlnaHQ9IjM1NS42IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNjY5LjExIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+UkFOLVNoYXJpbmcgMuuMgCDtlbXsi6wg67Cp7IudIOuMgOyhsDwvdGV4dD4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSIxX01PUkFOX19fXyIgZGF0YS1sYWJlbD0iMS4gTU9SQU4g67Cp7IudICjssqDtg5Hrp4wg6rO17JygIPCfl7wpIj4KICA8cmVjdCB4PSI1NiIgeT0iMjE3LjgiIHdpZHRoPSI0NjAuMTc5IiBoZWlnaHQ9IjE2MS44IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNTYiIHk9IjIxNy44IiB3aWR0aD0iNDYwLjE3OSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjgiIHk9IjIzMS44IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjEuIE1PUkFOIOuwqeyLnSAo7LKg7YOR66eMIOqzteycoCDwn5e8KTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IjJfTU9DTl9fX19fIiBkYXRhLWxhYmVsPSIyLiBNT0NOIOuwqeyLnSAo7KO87YyM7IiY6rmM7KeAIO2GteynuOuhnCDqs7XsnKAg8J+MiCkiPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjYzNy4xMSIgaGVpZ2h0PSIxMTMuODAwMDAwMDAwMDAwMDEiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSI2MzcuMTEiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjY4IiB5PSI5OCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij4yLiBNT0NOIOuwqeyLnSAo7KO87YyM7IiY6rmM7KeAIO2GteynuOuhnCDqs7XsnKAg8J+MiCk8L3RleHQ+CjwvZz4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTTEiIGRhdGEtdG89IkEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IlNLVCDso7ztjIzsiJgg67Cc7IKsISIgcG9pbnRzPSIyMjIuMTM2LDMwNi41NSAyMzQuMTM2LDMwNi41NSAyMzQuMTM2LDI4MC4yNSA0MTQuNTEsMjgwLjI1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJNMSIgZGF0YS10bz0iQiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iS1Qg7KO87YyM7IiYIOuwnOyCrCEiIHBvaW50cz0iMjIyLjEzNiwzMTguODUgMjM0LjEzNiwzMTguODUgMjM0LjEzNiwzNDUuMTUwMDAwMDAwMDAwMDMgNDE0LjUxLDM0NS4xNTAwMDAwMDAwMDAwMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTTIiIGRhdGEtdG89IkMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyjvO2MjOyImCAx6rCc66GcIDPsgqwg7Y+wIOuqqOuRkCDsoJHsho0hIiBwb2ludHM9IjI3Ni4yMjkwMDAwMDAwMDAwNCwxNTQuOSA1MzIuMTYxMDAwMDAwMDAwMSwxNTQuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJNMSIgZGF0YS10bz0iQSIgZGF0YS1sYWJlbD0iU0tUIOyjvO2MjOyImCDrsJzsgqwhIj4KICA8cmVjdCB4PSIyNjYuMTM1OTk5OTk5OTk5OTciIHk9IjI2NC4yNTAwMDAwMDAwMDAwNiIgd2lkdGg9IjEwNC4zNzQwMDAwMDAwMDAwMSIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjMxOC4zMjMiIHk9IjI3OS40MDAwMDAwMDAwMDAwMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+U0tUIOyjvO2MjOyImCDrsJzsgqwhPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209Ik0xIiBkYXRhLXRvPSJCIiBkYXRhLWxhYmVsPSJLVCDso7ztjIzsiJgg67Cc7IKsISI+CiAgPHJlY3QgeD0iMjY5LjciIHk9IjMyOS4xNTAwMDAwMDAwMDAwMyIgd2lkdGg9Ijk3LjI0NjAwMDAwMDAwMDAxIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzE4LjMyMyIgeT0iMzQ0LjMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPktUIOyjvO2MjOyImCDrsJzsgqwhPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209Ik0yIiBkYXRhLXRvPSJDIiBkYXRhLWxhYmVsPSLso7ztjIzsiJggMeqwnOuhnCAz7IKsIO2PsCDrqqjrkZAg7KCR7IaNISI+CiAgPHJlY3QgeD0iMzIwLjIyOTAwMDAwMDAwMDA0IiB5PSIxMzguOSIgd2lkdGg9IjE2Ny45MzIwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjQwNC4xOTUwMDAwMDAwMDAwNSIgeT0iMTU0LjA1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7so7ztjIzsiJggMeqwnOuhnCAz7IKsIO2PsCDrqqjrkZAg7KCR7IaNITwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTTEiIGRhdGEtbGFiZWw9IuqzteuPmSDquLDsp4Dqta0g7J6l67mEIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjcyIiB5PSIyOTQuMjUiIHdpZHRoPSIxNTAuMTM2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNDcuMDY3OTk5OTk5OTk5OTgiIHk9IjMxMi43IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7qs7Xrj5kg6riw7KeA6rWtIOyepeu5hDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQSIgZGF0YS1sYWJlbD0iU0tUIO2PsCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MTQuNTEiIHk9IjI2MS44IiB3aWR0aD0iODUuNjY4OTk5OTk5OTk5OTgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0NTcuMzQ0NSIgeT0iMjgwLjI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5TS1Qg7Y+wPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJCIiBkYXRhLWxhYmVsPSJLVCDtj7AiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDE0LjUxIiB5PSIzMjYuNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSI3Ni43NzY5OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQ1Mi44OTg1IiB5PSIzNDUuMTUwMDAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPktUIO2PsDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTTIiIGRhdGEtbGFiZWw9IuqzteuPmSDquLDsp4Dqta0g7J6l67mECuKcqCDqs7Xsmqkg7KO87YyM7IiYIDHqsJzrp4wg7JSAIOKcqCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3MiIgeT0iMTI4IiB3aWR0aD0iMjA0LjIyOSIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxNzQuMTE0NTAwMDAwMDAwMDIiIHk9IjE1NC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNzQuMTE0NTAwMDAwMDAwMDIiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7qs7Xrj5kg6riw7KeA6rWtIOyepeu5hDwvdHNwYW4+PHRzcGFuIHg9IjE3NC4xMTQ1MDAwMDAwMDAwMiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+4pyoIOqzteyaqSDso7ztjIzsiJggMeqwnOunjCDslIAg4pyoPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkMiIGRhdGEtbGFiZWw9IlNLVC9LVC9MR1UrIO2PsCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1MzIuMTYxMDAwMDAwMDAwMSIgeT0iMTM2LjQ1IiB3aWR0aD0iMTQ0Ljk0ODk5OTk5OTk5OTk4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjYwNC42MzU1MDAwMDAwMDAxIiB5PSIxNTQuODk5OTk5OTk5OTk5OTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlNLVC9LVC9MR1UrIO2PsDwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 주파수를 나누는가 합치는가? MORAN vs MOCN 전격 대조 (3단 표)**

가장 중요한 출제 포인트는 **'각자의 주파수를 쓰는가(MORAN)'** 아니면 \*\*'주파수 대역마저 하나로 합쳐서(Pooling) 같이 쓰는가(MOCN)'\*\*를 대조하는 것입니다.

| **핵심 척도 (비교 잣대)**              | **🗼 MORAN (철탑 장비만 공유)**                                                                                         | **🌈 MOCN (주파수 자원까지 공유) 🚨**                                                                                                      |
| :----------------------------- | :--------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| **풀네임 및 공유의 범위 (어디까지 같이 쓰나?)** | **Multi-Operator RAN.** 물리적인 철탑, 안테나, 기지국 하드웨어 장비까지만 공유하고, 전파를 쏘는 **'주파수 대역'은 각 통신사별로 독립적으로 할당하여 전송함.**          | **Multi-Operator Core Network. 💯** 하드웨어 장비는 물론이고, **'무선 주파수 자원(Spectrum)'까지 하나로 합쳐서(Pooling)** 여러 통신사가 완전히 똑같은 주파수 대역으로 단말과 통신함. |
| **운영의 장점 및 단점 (Trade-off)**    | - **장점:** 주파수가 분리되어 있어 통신사별로 세밀한 품질(QoS) 차별화와 독립적 제어가 쉬움. - **단점:** 안테나 장비가 각 주파수를 모두 지원해야 하므로 구축 복잡도가 상대적으로 높음. | - **장점:** 1개의 주파수만 쏘면 되므로 기지국 장비가 가장 단순하고 저렴해짐 (비용 절감 효과 최상 💯). - **단점:** 주파수가 같아 3사가 동일한 품질을 갖게 되며, 트래픽 폭증 시 상호 간섭 관리가 어려움.     |
| **국내 도입 실제 사례 (단골 득점 포인트 🚨)** | 2000년대 3G(WCDMA) 도입 시절이나 지하철 중계기 등 제한적 하드웨어 공동 구축에 쓰임.                                                           | 현재 과기부와 통신 3사가 구축한 **'농어촌 5G 공동망'이 바로 이 MOCN 방식을 100% 채택하여 전국망을 완성함.**                                                            |

#### **IV. \[결론/제언] 오픈랜(O-RAN) 확산과 이기종 네트워크(HetNet) 지능화의 필요성**

* **(키워드 위주 2줄 마무리)** "RAN-Sharing은 CAPEX 절감의 치트키지만, 특정 통신장비(화웨이, 에릭슨 등)에 종속되는 벤더 락인(Lock-in) 문제가 큽니다. 향후 6G 인프라 공동 구축을 위해서는 기지국 하드웨어와 소프트웨어의 인터페이스를 100% 개방하여 어떤 장비든 호환되게 섞어 쓰는 **'오픈랜(O-RAN)' 표준화가 선행되어야 진정한 망 공유의 경제성을 극대화할 수 있습니다.**"
