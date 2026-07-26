### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (등장배경, 앞서다룬PQC/QKD와의연결) — 3~4줄
Ⅱ. 마스터플랜4대추진전략 (본론①, 도식 1개 필수)
Ⅲ. 단계별전환로드맵및암호자산인벤토리, 핵심 배점
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서다룬양자컴퓨터가RSA/ECC를무너뜨릴수있다는위협앞에서, 개별기업이각자PQC로전환하면 서로다른시점에,서로다른방식으로바뀌어 '호환성혼란'이생긴다 — 그래서국가가나서서 '언제까지,무엇을,어떻게'전환할지 전체그림(마스터플랜)을그린것"\*\*이라는한줄로시작하면, 왜 국가차원의계획이 필요한지드러납니다.

### Ⅱ. 마스터플랜 4대추진전략

| 전략              | 내용                                              |
| :-------------- | :---------------------------------------------- |
| **①암호체계전환기반마련** | **암호자산인벤토리구축**(어떤시스템이어떤암호를쓰는지 전수조사)             |
| **②PQC기술자립화**   | 해외표준(NIST의ML-KEM등)에만 의존하지않고, **국산PQC알고리즘개발·검증** |
| **③분야별시범전환**    | 앞서다룬 \*\*"금융,공공,국방"\*\*등 **우선순위분야부터단계적시범적용**    |
| **④국제협력·표준화참여** | NIST,ISO등 **국제표준화기구에한국이직접참여**해 발언권확보            |

→ 암기: **"먼저뭘쓰고있는지파악하고,우리기술도개발하고,중요한곳부터시범적용하고,국제무대에서도목소리를낸다"** — 앞서다룬 \*\*"OpenRAN의표준화경쟁"\*\*과 유사하게, PQC도 \*\*"단순히따라가는것이아니라, 표준을함께만드는데참여"\*\*하는 것이 핵심전략입니다.

### 도식화 제안

```
[PQC 국가전환 마스터플랜 4대전략]
①암호자산인벤토리 → "우리가 어디에어떤암호를쓰고있는가?"
②PQC기술자립화 → "우리기술로도 PQC를만들수있는가?"
③분야별시범전환 → "금융·공공·국방부터 먼저바꿔보자"
④국제표준화참여 → "우리목소리도 국제표준에반영시키자"
```

### Ⅲ. 단계별전환로드맵 및 암호자산인벤토리 — 핵심 배점

**함정 방지: "언젠가바꾼다"고만답하면절반. 구체적인전환시기와, 왜"인벤토리"가가장먼저필요한필수단계인지보여줘야완성됩니다.**

**암호자산인벤토리**(가장먼저해야하는이유,핵심)

| 이유               | 내용                                                                                        |
| :--------------- | :---------------------------------------------------------------------------------------- |
| **"모르는것은지킬수없다"** | 앞서다룬 \*\*"데이터거버넌스,데이터관측가능성"\*\*의 논리와동일— **"어떤시스템이,어떤암호알고리즘을, 어디에쓰고있는지"** 모르면 **전환자체가불가능** |
| **레거시시스템의숨은위험**  | 오래된시스템일수록 \*\*"어떤암호를쓰는지 문서조차없는경우"\*\*가 많아, **인벤토리조사자체가가장오래걸리는작업**                         |

**단계별로드맵**(예시적,국가전략)

| 단계      | 시기         | 내용                                                  |
| :------ | :--------- | :-------------------------------------------------- |
| **1단계** | 2023\~2025 | **암호자산인벤토리**,PQC **표준동향분석**(앞서다룬NIST FIPS203\~205등) |
| **2단계** | 2025\~2027 | **금융·공공핵심시스템** **시범전환**(하이브리드방식,앞서다룬그것)             |
| **3단계** | 2027\~2030 | **민간전반확산**,전면적용                                     |

→ 암기: **"뭘쓰는지부터파악하고(1단계),중요한곳에먼저시범적용하고(2단계),그다음전체로퍼뜨린다(3단계)"** — 이는 앞서다룬 \*\*"5G특화망도입절차,ISMS-P의계획-구축-운영"\*\*과 **동일한3단계논리**(파악→시범→확산)가 반복되는 것입니다.

**앞서다룬"하이브리드전환"과의연결**: 앞서다룬 \*\*"Chrome의X25519+Kyber768하이브리드"\*\*처럼, 국가마스터플랜도 \*\*"기존RSA/ECC와새PQC를 동시에적용하는하이브리드방식"\*\*으로 \*\*"점진적,안전한전환"\*\*을 추구합니다 — \*\*"한번에완전히전환"\*\*하면 **호환성문제·검증부족위험**이 있기때문입니다.

### 도식화 제안

```
[PQC 국가전환 3단계 로드맵]
1단계(2023~25): 암호자산인벤토리 + PQC표준분석
     ↓ "우리가뭘쓰는지부터안다"
2단계(25~27): 금융·공공핵심시스템 하이브리드시범전환
     ↓ "중요한곳부터, 기존+PQC동시적용으로안전하게"
3단계(27~30): 민간전반확산,전면적용
     ↓ "검증된방식을 전체로확대"

[왜인벤토리가 가장먼저인가]
"어떤시스템이 어떤암호를쓰는지" 모르면
     ↓
전환대상자체를 특정할수없음 → 모든전환의 출발점
```

**앞서다룬"PQC/QKD비교"와의재연결**: 이 마스터플랜의 \*\*"3단계전환"\*\*이 실제로 성공하려면, 앞서다룬 \*\*"AES는키길이강화로대응,RSA/ECC는PQC로교체"\*\*라는 **기술적차별화**가 **국가정책수준에서도동일하게반영**되어야합니다 — 즉 \*\*"모든암호를무조건바꾸는것이아니라, 진짜취약한부분(공개키암호)부터우선순위를매겨전환"\*\*하는 것이 마스터플랜의 실무적핵심입니다.

### Ⅳ. 결론

PQC국가전환마스터플랜은 **"앞서다룬양자컴퓨터의쇼어알고리즘위협에대응해, 개별기업이아니라국가차원에서 암호자산인벤토리→시범전환→전면확산이라는3단계로 체계적으로대비하는"** 전략입니다 — 가장먼저해야할 \*\*"암호자산인벤토리"\*\*는 앞서다룬 \*\*"데이터거버넌스,관측가능성"\*\*의 논리와 동일하게 \*\*"모르는것은지킬수없다"\*\*는 원칙에서출발하며, \*\*"하이브리드방식(기존+PQC동시적용)"\*\*으로 **점진적이고안전한전환**을 추구합니다 — 이는 앞서다룬 \*\*"PQC/QKD비교"\*\*답안에서 \*\*"AES는강화,RSA/ECC는교체"\*\*라는 **기술적차별화전략**이, 국가정책수준으로 확장된것을 보여주며, 오늘하루다룬 **양자컴퓨터→PQC/QKD→ECC→PQC국가전환마스터플랜**으로 이어지는 암호학시리즈전체가 \*\*"미래의위협에,오늘부터체계적으로,단계적으로대비하는것이 국가안보의핵심"\*\*이라는 결론으로 완결됩니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "미래 고성능 양자컴퓨터가 기존 공개키 암호(RSA, ECC 등)를 빛의 속도로 풀어헤칠 재앙(Y2Q)에 선제 대비하기 위해, 대한민국 행정망과 금융망의 국가 암호 뼈대를 \*\*양자컴퓨터로도 해독할 수 없는 '양자내성암호(PQC)'\*\*로 순차 교체하는 정부 합동 로드맵이다. 해커들이 "현재 국가 기밀 데이터를 일단 암호화 상태로 다 다운로드해 훔쳐 두고, 향후 양자컴퓨터가 상용화되면 풀어보자(Store Now, Decrypt Later)"며 벼르고 있어 시급성이 극도로 높다. 타임라인은 3단계다. 첫째, **'\~2026년(준비)'** 암호 실태 조사 및 KCMVP(한국형 암호검증제도) 기준 수립. 둘째, **'\~2030년(시범)'** 국가 중요 행정 시스템 시범 적용. 셋째, **'\~2035년(전면 전환)'** 전 공공·금융망 전면 교체 완료다. 전환 시 급격한 시스템 장애를 막기 위해, 기존 암호와 PQC를 겹쳐서 쓰는 \*\*'하이브리드(Hybrid) 암호 아키텍처'\*\*를 징검다리 방패로 세운다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 양자 컴퓨팅에 의한 암기 붕괴 예방책, PQC 국가 전환 마스터플랜 개요**

* **정의:** 양자컴퓨터가 구현할 Shor(쇼어) 알고리즘의 인수분해 파괴력에 대응해, 기존 정보통신망의 암호체계(RSA 등)를 수학적 격자 문제 등 양자난독화 기반의 \*\*양자내성암호(PQC: Post-Quantum Cryptography)\*\*로 전환하기 위해 범정부(과기정통부, 국정원 등)가 공동 수립한 국가 전략 로드맵.
* **배경:** 2030년대 중반 양자 컴퓨터가 비약적인 이득을 달성하는 시점(Y2Q)을 타깃으로 하는 전 세계적인 사이버 안보 체질 개선 기조에 동참하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 조사부터 전면 교체까지 이어지는 3단계 타임라인**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MDYuNTM4IDIxMC43IiB3aWR0aD0iNjA2LjUzOCIgaGVpZ2h0PSIyMTAuNyIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX1BRQ19fXzNfIiBkYXRhLWxhYmVsPSLslpHsnpDrgrTshLHslZTtmLggKFBRQykg6rWt6rCAIOyghO2ZmCAz64uo6rOEIOuhnOuTnOuntSI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNTI2LjUzOCIgaGVpZ2h0PSIxMzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjUyNi41MzgiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7slpHsnpDrgrTshLHslZTtmLggKFBRQykg6rWt6rCAIOyghO2ZmCAz64uo6rOEIOuhnOuTnOuntTwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iU1RFUDEiIGRhdGEtdG89IlNURVAyIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjI4NC42ODIsMTE5LjM1IDMzMi42ODIsMTE5LjM1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTVEVQMiIgZGF0YS10bz0iU1RFUDMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDE3LjYxLDExOS4zNSA0NjUuNjEsMTE5LjM1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTVEVQMSIgZGF0YS1sYWJlbD0i4pyoIDHri6jqs4Q6IOykgOu5hOq4sCAofjIwMjbrhYQpIOKcqArqta3qsIAg7KCV67O07J6Q7IKwIOyVlO2YuCDsi6Ttg5wg7YyM7JWFCu2VnOq1re2YlSBLQ01WUCDslZTtmLjrqqjrk4gg6rKA7KadIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjIyOC42ODIiIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNzAuMzQxIiB5PSIxMTkuMzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE3MC4zNDEiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj7inKggMeuLqOqzhDog7KSA67mE6riwICh+MjAyNuuFhCkg4pyoPC90c3Bhbj48dHNwYW4geD0iMTcwLjM0MSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+6rWt6rCAIOygleuztOyekOyCsCDslZTtmLgg7Iuk7YOcIO2MjOyVhTwvdHNwYW4+PHRzcGFuIHg9IjE3MC4zNDEiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPu2VnOq1re2YlSBLQ01WUCDslZTtmLjrqqjrk4gg6rKA7KadPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlNURVAyIiBkYXRhLWxhYmVsPSJTVEVQMiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzMzIuNjgyIiB5PSIxMDAuOSIgd2lkdGg9Ijg0LjkyOCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIzNzUuMTQ2IiB5PSIxMTkuMzUwMDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlNURVAyPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTVEVQMyIgZGF0YS1sYWJlbD0iU1RFUDMiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDY1LjYxIiB5PSIxMDAuOSIgd2lkdGg9Ijg0LjkyOCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI1MDguMDc0IiB5PSIxMTkuMzUwMDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlNURVAzPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 단계별 국가 마스터플랜 및 기술적 하이브리드 전환 전략 (3단 표)**

이 토픽은 실현 가능성을 입증하기 위한 \*\*'하이브리드(Dual-key/Double-wrapping) 암호 설계'\*\*의 중요성과, NIST가 표준화한 대표적인 \*\*'PQC 알고리즘 유형(격자 기반)'\*\*을 답안지에 녹여 적는 것이 합격의 고득점 열쇠입니다.

| **핵심 척도**                | **📊 마스터플랜 3대 전환 로드맵 🚨**                                                                                                                                | **🔑 과도기 하이브리드 암호 전략 💯**                                                                                                                                 | **💼 주요 PQC 알고리즘 분류 (NIST) 💯**                                                                                                                                                        |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **개념 / 역할**              | **'범국가적 보안 이정표'.** Y2Q 도래 전까지 국가 행정, 입법, 사법, 금융, 에너지 등 사회 전체 암호망을 점진적으로 갱신하는 단계별 시나리오.                                                                   | **'충격 없는 징검다리 아키텍처'.** 단번에 PQC로 교체 시 생길 호환성 장애와 미지의 알고리즘 결함 위험을 분산하는 과도기 기술.                                                                              | 양자 컴퓨터가 풀기 극도로 힘든 수학적 난제를 기반으로 하여 설계된 차세대 암호 원천 기술군.                                                                                                                                   |
| **핵심 세부 요건 (출제 포인트) 🚨** | **1. \[1단계 (\~'26)]** 암호 자산 식별, KCMVP(한국형 검증제도) 개편. **2. \[2단계 (\~'30) 🚨]** 국가망 하이브리드 시범 적용 및 안전성 검증. **3. \[3단계 (\~'35) 💯]** 국가 인프라 및 전 사설 금융망 전면 전환. | **\[하이브리드 암호화 아키텍처 💯]** - 기존 서명/키 교환 알고리즘(RSA/ECC)과 신규 PQC 알고리즘을 \*\*이중으로 바인딩(Double-wrapping)\*\*하여 동시 연산 처리. - 어느 한쪽 알고리즘이 깨져도 나머지 하나가 데이터 보안을 2차 방어함. | **1. \[격자 기반 암호 (Lattice-based) 💯]** 가장 성능이 우수해 NIST 표준화 대세 장악. (Kyber: 키 교환, Dilithium: 서명). **2. 코드 기반 암호** (McEliece 등). **3. 다변수 기반 암호** (Rainbow 등). **4. 해시 기반 서명** (SPHINCS+). |
| **핵심 고려 사항**             | **\[Store Now, Decrypt Later 방어]** 현재 훔친 암호가 향후 양자컴퓨터로 열릴 우려를 막기 위해 **키 교환(KEM) 전환이 서명보다 급함.**                                                           | 구형 임베디드 단말기 등 CPU 연산 속도가 느린 엣지 장비에서는 하이브리드 연산 시 메모리 및 지연 지연율 폭증 리스크 존재.                                                                                   | 한국 국가보안기술연구소(NSR)가 개발한 국내 독자 PQC 알고리즘과의 연계 규범 제정 논의 진행 중.                                                                                                                              |

#### **IV. \[결론/제언] 공공 조달 체계와의 연계 및 보안인증(KCMVP)의 신속한 개편**

* **(키워드 위주 2줄 마무리)** "국가 PQC 마스터플랜의 성공적 안착을 위해서는 법적 기한 선언에 그치지 않고, 공공 시스템 구매 규격에 PQC 의무화 조항을 신설해야 합니다. 이를 위해 **양자 암호가 포함된 보안 제품에 도장을 찍어주는 '한국형 암호모듈검증제도(KCMVP)'의 PQC 평가 기준 고시 및 인증 심사 병목 현상 해소가 실무 활성화의 가장 시급한 전제조건입니다.**"
