### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (공격유형분류기준,공격자가진정보의차이) — 3~4줄
Ⅱ. 4대공격유형 (본론①, 도식 1개 필수)
Ⅲ. 심화 - 선택평문/암호문공격의실전위력 (본론②, 핵심 배점)
Ⅳ. 오늘암호시리즈의방어력검증
Ⅴ. 결론
```

포인트: 개요에서 \*\*"암호시스템의안전성은'절대안깨진다'가아니라'공격자가무엇을,얼마나가졌을때도안깨지는가'로평가된다 — 공격자가가진정보의양(암호문만/평문쌍도/직접선택가능)에따라 공격의강도가4단계로나뉜다"\*\*는 한줄로시작하면, 왜단계별로 분류하는지논리가섭니다.

### Ⅱ. 4대공격유형 — 공격자가가진정보순

| 공격유형             | 공격자가가진것              | 목표                   |
| :--------------- | :------------------- | :------------------- |
| **암호문단독공격**(COA) | **암호문만**             | 통계적패턴등으로 **평문·키추정**  |
| **알려진평문공격**(KPA) | **평문-암호문쌍일부**        | 나머지암호문의 **평문복원,키추정** |
| **선택평문공격**(CPA)  | **원하는평문을암호화시켜볼수있음**  | 그결과로 **키추정**         |
| **선택암호문공격**(CCA) | **원하는암호문을복호화시켜볼수있음** | 그결과로 **키추정,다른암호문해독** |

→ 암기: **"보기만(COA)→쌍으로알기(KPA)→내가골라서암호화해보기(CPA)→내가골라서복호화해보기(CCA)"** — 뒤로갈수록 \*\*공격자가더많은권한(오라클접근)\*\*을가지며, 그래서 **더강력한공격**입니다.

### 도식화 제안

```
[공격강도 낮음 ←──────────────────→ 높음]
   COA          KPA           CPA           CCA
암호문만봄    평문-암호문쌍     평문골라서      암호문골라서
             일부알고있음     암호화시켜봄     복호화시켜봄

← 안전성기준: CCA를견뎌야 "가장강한암호"로평가받음 →
```

### Ⅲ. 심화 — 선택평문/암호문공격의실전위력, 핵심 배점

**함정 방지: "이론적분류"로만끝내면절반. 오늘다룬구체적기법들이 왜이공격에취약/강한지연결해야완성됩니다.**

| 공격          | 오늘다룬사례연결                                                      | 취약점                                    |
| :---------- | :------------------------------------------------------------ | :------------------------------------- |
| **CPA취약사례** | 앞서다룬 **ECB모드**— 같은평문블록을 여러번암호화시켜보면 **같은암호문블록이나온다는패턴자체가노출**    | ECB는 **CPA에도취약**(패턴노출로구별가능)            |
| **CPA방어사례** | 앞서다룬 **CBC/CFB모드**— IV(초기화벡터)를 매번다르게써서 **같은평문도매번다른암호문**       | **CPA에안전**(확률적암호화)                     |
| **CCA공격사례** | **패딩오라클공격**(CBC모드의패딩오류메시지를악용해 암호문을조금씩바꿔가며 복호화시도결과를관찰,평문점진적복원) | 앞서다룬 **블록암호모드**도 **구현방식에따라CCA에취약**할수있음 |

→ 암기: **"CPA는패턴이보이면뚫리고,CCA는복호화오류메시지자체가정보가된다"** — 앞서다룬 \*\*"블록암호4모드"\*\*답안에서 ECB가 \*\*"가장위험한모드"\*\*로꼽혔던이유가, 사실은 **CPA조차못견디는가장약한안전성수준**이었기때문이라는 게 이답안에서 명확해집니다.

### 도식화 제안

```
[CPA 공격 - ECB의취약점]
공격자가 "AAAA"를 암호화요청 → 암호문X 획득
공격자가 "AAAA"를 다시 암호화요청 → 똑같이 암호문X 획득
→ "같은입력=같은출력"이라는패턴자체가 정보누출(안전성붕괴)

[CPA 방어 - CBC의안전성]
공격자가 "AAAA"를 암호화요청(IV1사용) → 암호문Y1
공격자가 "AAAA"를 다시 암호화요청(IV2사용) → 암호문Y2(완전히다름)
→ 패턴을알아낼수없음
```

### Ⅳ. 오늘암호시리즈의방어력검증

**함정 방지: 오늘다룬여러암호기법을 이공격기준으로 종합점검하지않으면절반. "IND-CPA","IND-CCA"같은 실제안전성증명개념까지연결해야완성됩니다.**

| 개념                      | 내용                                                               |
| :---------------------- | :--------------------------------------------------------------- |
| **IND-CPA**(구별불가능성-CPA) | 암호시스템이 **CPA공격에도 암호문으로부터평문에대한어떤정보도구별해낼수없음**을 의미하는 보안증명기준         |
| **IND-CCA(CCA2)**       | **CCA공격에도구별불가능**— 가장강한안전성기준,실무에서목표로하는수준                          |
| **AEAD**(인증암호화)         | 앞서다룬 **암호화+무결성검증을동시에** 제공하는방식(GCM모드등) — **CCA안전성**을실질적으로달성하는실무표준 |

→ 앞서다룬 \*\*"블록암호4모드"\*\*에서 언급했던 \*\*"실무에서는CTR/GCM모드가더선호된다"\*\*는 부분이, 바로이 **IND-CCA안전성**을 만족시키기위한 실질적선택이었다는게 여기서완전히연결됩니다 — ECB/CBC/CFB/OFB는 **기밀성(암호화)만**신경썼지 \*\*무결성검증(위변조탐지)\*\*이 없어서, CCA공격(암호문을조작해복호화반응을관찰)에 취약할수있습니다.

### Ⅴ. 결론 포인트 (암호학 시리즈 최종대단원)

암호문공격유형(COA→KPA→CPA→CCA)은 \*\*"암호시스템의안전성을무엇을기준으로평가할지"\*\*에대한 표준화된잣대이며, 오늘하루다룬 모든암호기법(대칭/비대칭키,블록암호모드,해시,전자봉투)이 \*\*"이4단계공격중어디까지견딜수있는가"\*\*로 최종평가받습니다 — 이는 앞서다룬 \*\*ISO/IEC25010(품질특성)\*\*이 소프트웨어전체의품질을 8개축으로평가했던것처럼, 암호학에서는 \*\*"공격자의권한단계"\*\*라는 하나의축으로 안전성을체계적으로평가한다는점에서, 오늘하루의방대한 컴퓨터구조→아키텍처→테스트→품질→비용산정→암호학시리즈전체를, \*\*"이론적으로우아한기법도, 실제공격모델앞에서엄격히검증받아야만 진짜안전하다고말할수있다"\*\*는 하나의최종교훈으로마무리할수있습니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "2차 세계대전 당시, 독일군의 절대 암호 기계 '애니그마'를 해독하려던 영국의 수학 천재 앨런 튜링을 떠올려보자. 처음 튜링이 마주한 상황은 절망 그 자체였다. 오직 라디오 전파에서 훔쳐 들은 알 수 없는 독일군의 '암호문(외계어)' 쪼가리들만 가득했다. 이것이 해커 입장에서 가장 해킹하기 어려운 가시밭길인 \*\*'암호문 단독 공격(COA)'\*\*이다. 그런데 어느 날 기적이 일어났다. 독일군 통신병이 매일 아침 6시마다 똑같이 '오늘의 날씨는'이라는 문장을 타이핑하여 암호문을 쏜다는 사실을 알아낸 것이다! 즉, 튜링의 손에 '암호문' 덩어리와 그 원본인 '평문' 쌍이 매칭되어 들어왔다. 퍼즐이 단숨에 맞춰지기 시작하는 이 공격 시나리오가 바로 \*\*'기지 평문 공격(KPA)'\*\*이다. 현대로 와보자. 이제 해커들은 직접 웹 서버를 가지고 논다. 해커가 회원가입 창에 마음대로 'AAAAA'라는 글자(원하는 평문)를 막 집어넣으면 서버가 친절하게 'X@#$'라는 암호문으로 바꿔서 보여준다. 기계의 반응을 관찰하는 이것이 \*\*'선택 평문 공격(CPA)'\*\*이다. 한발 더 나아가, 해커가 쓰레기 암호문을 막 던져주면 서버가 에러 메시지와 함께 '평문'을 뱉어내는 가장 끔찍한 보안 붕괴 상황이 바로 \*\*'선택 암호문 공격(CCA)'\*\*이다. 위대한 현대의 암호 알고리즘(RSA, AES)은 해커가 이렇게 마음대로 기계를 가지고 노는 CPA와 CCA 상황에서조차 절대 '비밀키'를 노출하지 않아야만 비로소 상용화 합격 판정을 받는다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 해커의 무기에 따라 달라지는 4단계 해킹 시나리오, 암호문 공격 개요**

* **정의:** 암호 해독자(해커)가 암호화된 데이터를 해독하여 원래의 \*\*'평문(Plaintext)'\*\*을 알아내거나, 시스템을 뚫기 위한 핵심 열쇠인 \*\*'비밀키(Key)'\*\*를 찾아내기 위해 시도하는 4가지 수학적/분석적 공격 모델.
* **분류 기준:** 해커가 현재 손에 쥐고 있는 **사전 정보(무기)가 얼마나 많은지, 그리고 암호화/복호화 기계(오라클)에 접근할 권한이 있는지**에 따라 난이도가 4단계로 구분됨.

#### **II. \[본론 1] 해커가 가진 정보(무기)가 많아질수록 뚫리는 보안의 벽 (도식화)**

COA에서 CCA로 갈수록 해커에게 유리해지고 방어자에겐 치명적이 되는 흐름을 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMzUwLjUxOCAyNTAuNzAwMDAwMDAwMDAwMDIiIHdpZHRoPSIxMzUwLjUxOCIgaGVpZ2h0PSIyNTAuNzAwMDAwMDAwMDAwMDIiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9fXzRfX19fXyIgZGF0YS1sYWJlbD0i7JWU7Zi4IO2VtOuPhSDqs7XqsqkgNOuMgCDrqqjrjbggKO2VtOy7pOyXkOqyjCDsnKDrpqztlZwg7Iic7IScIOKelCkiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjEyNzAuNTE4IiBoZWlnaHQ9IjE3MC43MDAwMDAwMDAwMDAwMiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjEyNzAuNTE4IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+7JWU7Zi4IO2VtOuPhSDqs7XqsqkgNOuMgCDrqqjrjbggKO2VtOy7pOyXkOqyjCDsnKDrpqztlZwg7Iic7IScIOKelCk8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkNPQSIgZGF0YS10bz0iS1BBIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLtnoztirgg7ZqN65OdISIgcG9pbnRzPSIyMTQuMjg2OTk5OTk5OTk5OTgsMTY3LjggMzcxLjYxNSwxNjcuOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iS1BBIiBkYXRhLXRvPSJDUEEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyVlO2YuO2ZlCDshJzrsoQg6raM7ZWcIO2DiOy3qCEiIHBvaW50cz0iNTE5LjUyOCwxNjcuOCA3MzkuODIsMTY3LjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkNQQSIgZGF0YS10bz0iQ0NBIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLrs7XtmLjtmZQg7ISc67KEIOq2jO2VnOq5jOyngCDtg4jst6ghIiBwb2ludHM9Ijg4Ny43MzMwMDAwMDAwMDAxLDE2Ny44IDExMzEuNzg1LDE2Ny44IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkNPQSIgZGF0YS10bz0iS1BBIiBkYXRhLWxhYmVsPSLtnoztirgg7ZqN65OdISI+CiAgPHJlY3QgeD0iMjU4LjI4NzAwMDAwMDAwMDAzIiB5PSIxNTEuOCIgd2lkdGg9IjY5LjMyOCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjI5Mi45NTEiIHk9IjE2Ni45NTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7Z6M7Yq4IO2ajeuTnSE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iS1BBIiBkYXRhLXRvPSJDUEEiIGRhdGEtbGFiZWw9IuyVlO2YuO2ZlCDshJzrsoQg6raM7ZWcIO2DiOy3qCEiPgogIDxyZWN0IHg9IjU2My41MjgiIHk9IjE1MS44IiB3aWR0aD0iMTMyLjI5MjAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjI5LjY3NCIgeT0iMTY2Ljk1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7slZTtmLjtmZQg7ISc67KEIOq2jO2VnCDtg4jst6ghPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkNQQSIgZGF0YS10bz0iQ0NBIiBkYXRhLWxhYmVsPSLrs7XtmLjtmZQg7ISc67KEIOq2jO2VnOq5jOyngCDtg4jst6ghIj4KICA8cmVjdCB4PSI5MzEuNzMzIiB5PSIxNTEuOCIgd2lkdGg9IjE1Ni4wNTIwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjEwMDkuNzU5IiB5PSIxNjYuOTUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuuzte2YuO2ZlCDshJzrsoQg6raM7ZWc6rmM7KeAIO2DiOy3qCE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkNPQSIgZGF0YS1sYWJlbD0iMS4g7JWU7Zi466y4IOuLqOuPhSDqs7XqsqkKQ09BICjqt7nsg4EpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIxNDAuOSIgd2lkdGg9IjE1OC4yODY5OTk5OTk5OTk5OCIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxMzUuMTQzNSIgeT0iMTY3LjgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjEzNS4xNDM1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+MS4g7JWU7Zi466y4IOuLqOuPhSDqs7Xqsqk8L3RzcGFuPjx0c3BhbiB4PSIxMzUuMTQzNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+Q09BICjqt7nsg4EpPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IktQQSIgZGF0YS1sYWJlbD0iMi4g6riw7KeAIO2PieusuCDqs7XqsqkKS1BBICjsg4EpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM3MS42MTUiIHk9IjE0MC45IiB3aWR0aD0iMTQ3LjkxMyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDQ1LjU3MTUiIHk9IjE2Ny44IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0NDUuNTcxNSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPjIuIOq4sOyngCDtj4nrrLgg6rO16rKpPC90c3Bhbj48dHNwYW4geD0iNDQ1LjU3MTUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPktQQSAo7IOBKTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDUEEiIGRhdGEtbGFiZWw9IjMuIOyEoO2DnSDtj4nrrLgg6rO16rKpCkNQQSAo7ZWYKSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3MzkuODIiIHk9IjE0MC45IiB3aWR0aD0iMTQ3LjkxMyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iODEzLjc3NjUiIHk9IjE2Ny44IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI4MTMuNzc2NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPjMuIOyEoO2DnSDtj4nrrLgg6rO16rKpPC90c3Bhbj48dHNwYW4geD0iODEzLjc3NjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPkNQQSAo7ZWYKTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDQ0EiIGRhdGEtbGFiZWw9IjQuIOyEoO2DnSDslZTtmLjrrLgg6rO16rKpCkNDQSAo7LWc7ZWYL+2VtOy7pCDqv4ApIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjExMzEuNzg1IiB5PSIxNDAuOSIgd2lkdGg9IjE2Mi43MzMiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTIxMy4xNTE1MDAwMDAwMDAyIiB5PSIxNjcuOCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTIxMy4xNTE1MDAwMDAwMDAyIiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+NC4g7ISg7YOdIOyVlO2YuOusuCDqs7Xqsqk8L3RzcGFuPjx0c3BhbiB4PSIxMjEzLjE1MTUwMDAwMDAwMDIiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPkNDQSAo7LWc7ZWYL+2VtOy7pCDqv4ApPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik5vdGUiIGRhdGEtbGFiZWw9Ik5vdGUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iNjguNjI2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iOTAuMzEzIiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk5vdGU8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 4대 암호 해독 공격 모델 전격 해부 (3단 표 - 출제 1순위)**

각 공격 모델에서 \*\*'해커가 쥐고 있는 힌트(무기)'\*\*가 무엇인지를 명확히 찌르는 것이 가장 중요합니다.

| **공격 모델 명칭**                                          | **해커가 손에 쥐고 있는 힌트 (공격자의 무기)**                                                            | **공격 상황 및 방어(난이도) 특징**                                                                      |
| :---------------------------------------------------- | :--------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| **1. 암호문 단독 공격** **COA** *(Ciphertext Only Attack)*   | 오직 와이어샤크(패킷 스니핑) 등으로 도청해서 긁어모은 **'수많은 알 수 없는 암호문'들만 쥐고 있음.**                             | **\[해커 난이도: 최상]** 단서가 없으므로 무차별 대입이나 알파벳 빈도수(통계적 특성)로 찍어야 함. 만약 이 공격에 뚫리면 그 암호는 쓰레기로 즉시 폐기됨. |
| **2. 기지 평문 공격** **KPA** *(Known Plaintext Attack)*    | 해커가 일정량의 **'암호문'과 그에 매칭되는 '원본 평문'의 쌍(Pair)을 몇 개 알고 있는 상태.**                              | **\[해커 난이도: 상]** 2차 대전 애니그마 해독처럼, "이 암호문은 '날씨'라는 단어야"라는 힌트를 가지고 비밀키를 역추적하는 방식.              |
| **3. 선택 평문 공격** **CPA** *(Chosen Plaintext Attack)*   | 해커가 \*\*'원하는 평문'을 선택(입력)\*\*하면, 암호화 기계가 그에 대한 **'암호문'을 만들어 내어주는 상태.** (암호화 기계 접근 권한 획득). | **\[해커 난이도: 하]** 해커가 특정 패턴(AAAAA, BBBBB)을 입력하며 기계의 반응을 분석함. 현대 암호 알고리즘은 이 공격을 막아내야 함.       |
| **4. 선택 암호문 공격** **CCA** *(Chosen Ciphertext Attack)* | 해커가 \*\*'원하는 암호문'을 선택(입력)\*\*하면, 서버가 그에 대한 **'평문'을 복호화해서 내어주는 상태.** (복호화 기계 접근 권한 획득).   | **\[해커 난이도: 최하]** 가장 강력하고 해커에게 완벽히 유리한 최악의 붕괴 상황. 해커가 쓰레기값을 던져 에러 반응을 살피며 비밀키를 탈취함.         |

#### **IV. \[결론/제언] 최악의 공격 모델(CCA)조차 견뎌내는 현대 암호의 안전성 증명**

* **(키워드 위주 2줄 마무리)** "과거의 단순한 암호들은 KPA 수준에서 모두 붕괴되었지만, 오늘날 글로벌 인프라를 지키는 AES, RSA-OAEP 같은 위대한 현대 암호 알고리즘들은 해커에게 100% 유리한 \*\*최악의 '선택 암호문 공격(IND-CCA)' 상황에서 기계를 마음껏 가지고 놀게 두어도, 절대 비밀키가 뚫리지 않음을 수학적으로 완벽히 증명(Provable Security)\*\*해 내고 있습니다."
