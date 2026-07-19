### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (RSA/DSA공통점,근본적차이) — 3~4줄
Ⅱ. RSA - 암호화+서명겸용 (본론①, 도식 1개 필수)
Ⅲ. DSA - 서명전용 (본론②, 핵심 배점)
Ⅳ. 성능비교및선택기준
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬RSA는소인수분해에기반한 비대칭키알고리즘으로, 암호화·복호화와전자서명을 모두할수있는'다재다능한'알고리즘 — 반면DSA(DigitalSignatureAlgorithm)는 이름부터'서명'이명시되어있듯, 오직전자서명만을위해설계된 특화알고리즘"\*\*이라는 한줄로시작하면, 두알고리즘의출발점자체가다르다는게드러납니다.

### Ⅱ. RSA — 암호화+서명겸용

| 항목        | 내용                                                         |
| :-------- | :--------------------------------------------------------- |
| **수학적기반** | **소인수분해문제**(앞서다룬그것)                                        |
| **기능**    | **암호화/복호화**(공개키로암호화,개인키로복호화) **+전자서명**(개인키로서명,공개키로검증) 모두가능 |
| **서명방식**  | 메시지의해시값을 **개인키로직접암호화**하는것과유사한방식                            |
| **속도특성**  | **서명은느리지만,검증은빠름**(공개키연산이 개인키연산보다가벼움)                       |

→ 암기: **"RSA는암호화도서명도다되는범용도구"** — 앞서다룬 \*\*"TLS의하이브리드방식"\*\*에서, RSA는 **키교환(암호화)과서버인증(서명)** 두역할을동시에 수행할수있다는게 실무적강점입니다.

### 도식화 제안

```
[RSA의두가지용도]
   ┌────────┴────────┐
[암호화용도]              [서명용도]
공개키로암호화              개인키로서명
개인키로복호화              공개키로검증
(기밀성보장)               (인증·부인방지보장)
```

### Ⅲ. DSA — 서명전용, 핵심 배점

**함정 방지: "DSA도비대칭키니까RSA와비슷하다"고답하면절반. "왜암호화를못하는가"의 근본적차이를보여줘야완성됩니다.**

| 항목        | 내용                                                         |
| :-------- | :--------------------------------------------------------- |
| **수학적기반** | **이산대수문제**(앞서다룬ECC와같은계열이지만, **유한체위에서**연산— ECC는타원곡선위)       |
| **기능**    | **오직전자서명만**— 암호화/복호화기능이 **구조적으로없음**                        |
| **서명방식**  | 서명생성시 \*\*매번새로운난수(k)\*\*를사용— **서명값이매번달라짐**(RSA는같은메시지면같은서명) |
| **속도특성**  | **서명은RSA보다빠르지만,검증은RSA보다느림**— RSA와 **정반대의속도프로파일**           |

→ 암기: **"DSA는서명하나만잘하는전문가,서명생성은빠르지만확인은느리다"** — RSA와DSA는 \*\*"어느쪽작업을더자주하느냐"\*\*에따라 유불리가갈립니다: **서명을자주생성**해야하면DSA가유리,**검증을자주해야**하면RSA가유리합니다.

### 도식화 제안

```
[RSA 서명]                          [DSA 서명]
서명생성: 느림(개인키연산,무거움)          서명생성: 빠름(이산대수기반,가벼움)
서명검증: 빠름(공개키연산,가벼움)          서명검증: 느림(상대적으로무거움)

→ RSA: "적게서명하고 많이검증"하는상황에유리
→ DSA: "많이서명하고 적게검증"하는상황에유리
```

### Ⅳ. 성능비교및선택기준

**함정 방지: 표만나열하면절반. 앞서다룬ECC와의관계(ECDSA)까지 연결해야완성됩니다.**

| 구분          | **RSA**                | **DSA**                                               |
| :---------- | :--------------------- | :---------------------------------------------------- |
| **암호화가능여부** | **가능**                 | **불가능**(서명전용)                                         |
| **표준화현황**   | SSL/TLS의 **가장보편적**알고리즘 | 미국NIST \*\*DSS(DigitalSignatureStandard)\*\*의일부       |
| **키생성속도**   | 느림(큰소수2개를찾아야함)         | 상대적으로빠름                                               |
| **파생기술**    | RSA-PSS등               | **ECDSA**(앞서다룬**타원곡선**위에서DSA방식적용) — **비트코인전자서명이바로이것** |

→ 앞서다룬 \*\*"타원곡선암호(ECC)"\*\*답안에서 비트코인이 ECC-256을 쓴다고했는데, 정확히는 **ECDSA(EllipticCurveDSA)**— **DSA의서명방식**을 **ECC의작은키크기장점**과결합한것입니다. 즉 DSA는 RSA의대안이자, ECC와결합해 \*\*더작고빠른전자서명(ECDSA)\*\*으로 발전했다는 연결이 심화포인트입니다.

### Ⅴ. 결론 포인트 (암호·보안 시리즈 최종연결)

RSA와DSA의근본적차이는 \*\*"범용성(RSA:암호화+서명) vs 전문성(DSA:서명전용,생성속도최적화)"\*\*입니다 — 이는 앞서다룬 **CPU/GPU/FPGA/ASIC**답안의 **"범용프로세서vs특화칩"** 구도와 동일한설계철학이 암호알고리즘세계에도나타나는것이며, DSA가 ECC와결합해 **ECDSA**로진화한것은, 오늘다룬 **타원곡선암호의키크기효율성**이 **서명알고리즘영역**까지확장된사례입니다 — 이로써오늘하루다룬 대칭/비대칭암호→동형암호→PQC/QKD→ECC→블록암호모드→해시함수→RSA vs DSA로이어지는 방대한암호학시리즈전체가, \*\*"목적(기밀성보장 vs 인증·무결성보장)에맞는수학적도구를선택하고 조합하는것"\*\*이라는 하나의완결된원리로마무리됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "비대칭키(공개키) 암호학의 두 거장, RSA와 DSA를 비교해 보자. 먼저 \*\*'RSA'\*\*는 1970년대에 탄생한 절대 만능 스위스 아미 나이프다. 무식하게 큰 두 소수를 곱하는 건 쉽지만 다시 쪼개는 건 불가능에 가깝다는 \*\*'소인수분해(Factoring)'\*\*의 수학적 미로를 무기로 쓴다. RSA의 가장 위대한 점은 만능이라는 것이다. '수신자의 공개키'로 찰칵 잠그면 데이터를 남몰래 숨기는 \*\*'암호화(기밀성)'\*\*가 되고, 반대로 '송신자의 개인키'로 도장을 쾅 찍으면 누가 보냈는지 증명하는 완벽한 \*\*'전자서명(부인방지)'\*\*이 된다. 혼자서 북 치고 장구 치는 완벽한 알고리즘이다. 반면 \*\*'DSA'\*\*는 미국 정부(NIST)가 아예 작정하고 '서명 검증' 하나만 패려고 만든 전용 저격총이다. ElGamal 암호의 **'이산대수(Discrete Logarithm)'** 난제를 기반으로 탄생했다. 이 녀석의 가장 치명적인 특징은 RSA와 달리, 데이터를 몰래 숨겨서 전달하는 **'암호화(기밀성)' 기능이 아예 없다는 것**이다! 오직 이 문서가 위조되지 않았고 네가 보낸 것이 맞다는 도장을 찍고(서명 생성), 그 도장이 맞는지 확인(서명 검증)하는 데에만 100% 특화되어 있다. 정리하자면, 웹브라우저처럼 데이터를 몰래 주고받으면서 신원 확인도 같이 해야 한다면 'RSA'를 쓰고, 굳이 내용을 숨길 필요 없이 오직 빠르고 표준화된 '공인인증 전자서명'만 필요하다면 'DSA'를 쓰는 것이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 만능 나이프와 서명 전용 저격총, RSA 및 DSA 개요**

* **RSA (Rivest-Shamir-Adleman):** 1977년 개발된 세계에서 가장 널리 쓰이는 비대칭키 암호 시스템. 하나의 알고리즘으로 **'데이터 암호화(기밀성 유지)'와 '전자서명(인증 및 부인방지)'을 모두 수행**할 수 있는 만능 구조를 가짐.
* **DSA (Digital Signature Algorithm):** 미국 국립표준기술연구소(NIST)가 전자서명 표준(DSS)으로 제정한 비대칭키 알고리즘. 데이터를 암호화하는 기능은 없고, **오직 원본의 무결성과 송신자 인증을 증명하는 '전자서명' 용도로만 특화**되어 설계됨.

#### **II. \[본론 1] 기밀성 유지와 전자서명의 파이프라인 차이 (도식화)**

RSA가 왜 양방향으로 쓰일 수 있는지, DSA는 왜 서명만 되는지 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDQ0LjAxIDU3My40Mzc5OTk5OTk5OTk5IiB3aWR0aD0iMTA0NC4wMSIgaGVpZ2h0PSI1NzMuNDM3OTk5OTk5OTk5OSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX19fX19fdnNfIiBkYXRhLWxhYmVsPSLruYTrjIDsua3tgqTsnZgg67Cp7Zal7JeQIOuUsOuluCDquLDriqUg7LCo7J20OiDslZTtmLjtmZQgdnMg7KCE7J6Q7ISc66qFIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI5NjQuMDEiIGhlaWdodD0iNDkzLjQzNzk5OTk5OTk5OTkzIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iOTY0LjAxIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+67mE64yA7Lmt7YKk7J2YIOuwqe2WpeyXkCDrlLDrpbgg6riw64qlIOywqOydtDog7JWU7Zi47ZmUIHZzIOyghOyekOyEnOuqhTwvdGV4dD4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfMV9fX19fXyIgZGF0YS1sYWJlbD0iW+q4sOuKpSAxXSDrjbDsnbTthLAg7JWU7Zi47ZmUIO2GteyLoCAo6riw67CA7ISxIOuztOyepSkg8J+UkiI+CiAgPHJlY3QgeD0iNTYiIHk9IjMwMC4zNDQ5OTk5OTk5OTk5NyIgd2lkdGg9IjkyMC4xMTgwMDAwMDAwMDAyIiBoZWlnaHQ9IjIxNy4wOTI5OTk5OTk5OTk5NiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjU2IiB5PSIzMDAuMzQ0OTk5OTk5OTk5OTciIHdpZHRoPSI5MjAuMTE4MDAwMDAwMDAwMiIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjgiIHk9IjMxNC4zNDQ5OTk5OTk5OTk5NyIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5b6riw64qlIDFdIOuNsOydtO2EsCDslZTtmLjtmZQg7Ya17IugICjquLDrsIDshLEg67O07J6lKSDwn5SSPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iXzJfX19fXyIgZGF0YS1sYWJlbD0iW+q4sOuKpSAyXSDsoITsnpDshJzrqoUgKOyduOymnSDrsI8g67aA7J2467Cp7KeAKSDinI3vuI8iPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjkzMi4wMSIgaGVpZ2h0PSIxOTYuMzQ0OTk5OTk5OTk5OTciIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSI5MzIuMDEiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjY4IiB5PSI5OCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5b6riw64qlIDJdIOyghOyekOyEnOuqhSAo7J247KadIOuwjyDrtoDsnbjrsKnsp4ApIOKcje+4jzwvdGV4dD4KPC9nPgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJEMSIgZGF0YS10bz0iRU5DIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsiJjsi6DsnpDsnZggJ+qzteqwnO2CpCfroZwg7JWU7Zi47ZmUIiBwb2ludHM9IjE3NS40NTMsNDIyLjg5MTQ5OTk5OTk5OTk1IDQyMC4wOTkwMDAwMDAwMDAwNSw0MjIuODkxNDk5OTk5OTk5OTUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkVOQyIgZGF0YS10bz0iTzEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyImOyLoOyekOydmCAn6rCc7J247YKkJ+uhnCDrs7XtmLjtmZQiIHBvaW50cz0iNTc3LjE5Miw0MjIuODkxNDk5OTk5OTk5OTUgODIxLjgzODAwMDAwMDAwMDEsNDIyLjg5MTQ5OTk5OTk5OTk1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJEMiIgZGF0YS10bz0iU0lHIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLshqHsi6DsnpDsnZggJ+qwnOyduO2CpCfroZwg64+E7J6lIOy+hSEiIHBvaW50cz0iMTkwLjI3MywxOTYuMTcyNDk5OTk5OTk5OTkgNDM5LjA3NywxOTYuMTcyNDk5OTk5OTk5OTkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlNJRyIgZGF0YS10bz0iTzIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyGoeyLoOyekOydmCAn6rO16rCc7YKkJ+uhnCDrj4TsnqUg7ZmV7J24IiBwb2ludHM9IjU3NS40MjIsMTk2LjE3MjQ5OTk5OTk5OTk5IDgzMy43MywxOTYuMTcyNDk5OTk5OTk5OTkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iRDEiIGRhdGEtdG89IkVOQyIgZGF0YS1sYWJlbD0i7IiY7Iug7J6Q7J2YICfqs7XqsJztgqQn66GcIOyVlO2YuO2ZlCI+CiAgPHJlY3QgeD0iMjE5LjQ1Mjk5OTk5OTk5OTk3IiB5PSI0MDYuODkxNDk5OTk5OTk5OTUiIHdpZHRoPSIxNTYuNjQ2MDAwMDAwMDAwMDQiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyOTcuNzc2IiB5PSI0MjIuMDQxNDk5OTk5OTk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7IiY7Iug7J6Q7J2YICYjMzk76rO16rCc7YKkJiMzOTvroZwg7JWU7Zi47ZmUPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkVOQyIgZGF0YS10bz0iTzEiIGRhdGEtbGFiZWw9IuyImOyLoOyekOydmCAn6rCc7J247YKkJ+uhnCDrs7XtmLjtmZQiPgogIDxyZWN0IHg9IjYyMS4xOTIiIHk9IjQwNi44OTE0OTk5OTk5OTk5NSIgd2lkdGg9IjE1Ni42NDYwMDAwMDAwMDAwNCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjY5OS41MTUiIHk9IjQyMi4wNDE0OTk5OTk5OTk5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7siJjsi6DsnpDsnZggJiMzOTvqsJzsnbjtgqQmIzM5O+uhnCDrs7XtmLjtmZQ8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iRDIiIGRhdGEtdG89IlNJRyIgZGF0YS1sYWJlbD0i7Iah7Iug7J6Q7J2YICfqsJzsnbjtgqQn66GcIOuPhOyepSDsvoUhIj4KICA8cmVjdCB4PSIyMzQuMjczIiB5PSIxODAuMTcyNDk5OTk5OTk5OTkiIHdpZHRoPSIxNjAuODA0MDAwMDAwMDAwMDMiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzMTQuNjc1IiB5PSIxOTUuMzIyNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7Iah7Iug7J6Q7J2YICYjMzk76rCc7J247YKkJiMzOTvroZwg64+E7J6lIOy+hSE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iU0lHIiBkYXRhLXRvPSJPMiIgZGF0YS1sYWJlbD0i7Iah7Iug7J6Q7J2YICfqs7XqsJztgqQn66GcIOuPhOyepSDtmZXsnbgiPgogIDxyZWN0IHg9IjYxOS40MjIiIHk9IjE4MC4xNzI0OTk5OTk5OTk5OSIgd2lkdGg9IjE3MC4zMDgwMDAwMDAwMDAwNSIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjcwNC41NzYiIHk9IjE5NS4zMjI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7shqHsi6DsnpDsnZggJiMzOTvqs7XqsJztgqQmIzM5O+uhnCDrj4TsnqUg7ZmV7J24PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJEMSIgZGF0YS1sYWJlbD0i7Y+J66y4IOusuOyEnCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3MiIgeT0iNDA0LjQ0MTQ5OTk5OTk5OTk2IiB3aWR0aD0iMTAzLjQ1MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEyMy43MjY1IiB5PSI0MjIuODkxNDk5OTk5OTk5OTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPu2PieusuCDrrLjshJw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkVOQyIgZGF0YS1sYWJlbD0iUlNBIOyghOyaqSDquLDriqUKRFNB64qUIOu2iOqwgOuKpSEiIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iNDk4LjY0NTUsMzQ0LjM0NDk5OTk5OTk5OTk3IDU3Ny4xOTIsNDIyLjg5MTQ5OTk5OTk5OTk1IDQ5OC42NDU1LDUwMS40Mzc5OTk5OTk5OTk5MyA0MjAuMDk5MDAwMDAwMDAwMDUsNDIyLjg5MTQ5OTk5OTk5OTk1IiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0OTguNjQ1NSIgeT0iNDIyLjg5MTQ5OTk5OTk5OTk1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0OTguNjQ1NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPlJTQSDsoITsmqkg6riw64qlPC90c3Bhbj48dHNwYW4geD0iNDk4LjY0NTUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPkRTQeuKlCDrtojqsIDriqUhPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik8xIiBkYXRhLWxhYmVsPSLruYTrsIAg7Ya17IugIOyEseqztSEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iODIxLjgzODAwMDAwMDAwMDEiIHk9IjQwNC40NDE0OTk5OTk5OTk5NiIgd2lkdGg9IjEzOC4yODAwMDAwMDAwMDAwMyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9Ijg5MC45NzgwMDAwMDAwMDAxIiB5PSI0MjIuODkxNDk5OTk5OTk5OTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuu5hOuwgCDthrXsi6Ag7ISx6rO1ITwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRDIiIGRhdGEtbGFiZWw9IuusuOyEnCDtlbTsi5zqsJIiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNzIiIHk9IjE3Ny43MjI0OTk5OTk5OTk5NyIgd2lkdGg9IjExOC4yNzMiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMzEuMTM2NSIgeT0iMTk2LjE3MjQ5OTk5OTk5OTk2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7rrLjshJwg7ZW07Iuc6rCSPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTSUciIGRhdGEtbGFiZWw9IlJTQeyZgCBEU0EK66qo65GQIOqwgOuKpSEiIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iNTA3LjI0OTUsMTI4IDU3NS40MjIsMTk2LjE3MjQ5OTk5OTk5OTk5IDUwNy4yNDk1LDI2NC4zNDQ5OTk5OTk5OTk5NyA0MzkuMDc3LDE5Ni4xNzI0OTk5OTk5OTk5OSIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNTA3LjI0OTUiIHk9IjE5Ni4xNzI0OTk5OTk5OTk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNTA3LjI0OTUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5SU0HsmYAgRFNBPC90c3Bhbj48dHNwYW4geD0iNTA3LjI0OTUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuuqqOuRkCDqsIDriqUhPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik8yIiBkYXRhLWxhYmVsPSLshJzrqoUg6rKA7KadIOyZhOujjCEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iODMzLjczIiB5PSIxNzcuNzIyNDk5OTk5OTk5OTciIHdpZHRoPSIxMzguMjgwMDAwMDAwMDAwMDMiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI5MDIuODciIHk9IjE5Ni4xNzI0OTk5OTk5OTk5NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7ISc66qFIOqygOymnSDsmYTro4whPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] RSA 암호 vs DSA 전자서명 전격 해부 (3단 표 - 출제 1순위)**

두 알고리즘의 \*\*'수학적 기반'\*\*과 \*\*'제공하는 보안 서비스 범위'\*\*를 날카롭게 찌르는 것이 핵심입니다.

| **핵심 척도 (비교 잣대)**             | **🛠️ RSA (만능 스위스 아미 나이프)**                                                                                                               | **🎯 DSA (서명 전용 저격총)**                                                                                                          |
| :---------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| **보안 강도의 근원이 되는 수학적 난제 (원리)** | **'소인수분해 문제 (Factoring)'.** 무지막지하게 큰 두 개의 소수를 곱하는 것은 쉽지만, 곱해진 결과를 역으로 쪼개어 원래 소수를 찾아내는 것은 불가능하다는 원리에 기반.                                   | **'이산대수 문제 (Discrete Logarithm)'.** 매우 큰 소수를 모듈로(Modulo) 하는 지수 연산은 쉽지만, 그 결괏값만 보고 지수에 사용된 원래 숫자를 역추적하는 것은 불가능하다는 원리에 기반.        |
| **제공하는 보안 서비스의 범위**           | **\[암호화 + 전자서명 모두 가능]** 상대방 공개키로 잠가서 몰래 보내는 \*\*'기밀성(암호화 통신)'\*\*과, 내 개인키로 암호화하여 내가 보냈음을 증명하는 \*\*'인증/부인방지(전자서명)'\*\*를 하나의 알고리즘으로 모두 수행함. | **\[오직 전자서명만 가능]** 메시지를 남몰래 숨기는 데이터 암호화(기밀성) 기능은 원천적으로 **불가능함.** 오직 내 개인키를 이용해 문서 해시값에 전자 도장을 찍는 \*\*'인증/부인방지(서명 검증)'\*\*만 수행함. |
| **퍼포먼스 (서명 및 검증 속도)**         | 서명 검증(공개키 연산)은 매우 빠르나, **서명 생성(개인키 연산) 및 새로운 키 쌍을 생성하는 속도가 상대적으로 무겁고 매우 느림.**                                                             | 서명을 생성하는 속도는 RSA보다 상대적으로 빠르나, 역으로 **수신자가 서명을 검증하는 속도는 느린 편임.** (스마트카드 등 서명 전용 매체에 유리).                                          |
| **현대 IT 인프라 적용 표준**           | HTTPS, SSL/TLS 기반의 웹 브라우저 통신과 인터넷 뱅킹에서 전방위적으로 활용되는 글로벌 범용 표준.                                                                             | 미국 전자서명 표준(DSS)에 채택되었으며, 굳이 기밀성이 필요 없는 순수 공인인증 체계나 SSH 접속 인증 등에 사용됨.                                                            |

#### **IV. \[결론/제언] 양자 위협의 도래와 타원곡선(ECDSA) 기반 서명으로의 진화**

* **(키워드 위주 2줄 마무리)** "RSA와 DSA는 20세기 인터넷 보안의 근간을 세운 위대한 알고리즘이지만, 무거운 키 길이로 인한 모바일 환경의 한계에 부딪혔습니다. 현재 글로벌 보안 표준은 긴 키 길이를 요구하는 구형 DSA를 버리고, \*\*타원곡선의 극강의 효율성을 융합하여 짧은 키로도 동일한 보안을 제공하는 'ECDSA(타원곡선 전자서명 알고리즘)'\*\*로 비트코인 지갑과 모바일 보안의 권력을 완전히 이양하는 추세입니다."
