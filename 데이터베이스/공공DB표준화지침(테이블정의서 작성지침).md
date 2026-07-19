### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (지침의법적위치, 8대산출물체계) — 3~4줄
Ⅱ. 산출물체계및테이블정의서의위치 (본론①, 도식 1개 필수)
Ⅲ. 표준용어·코드적용원칙, 핵심 배점
Ⅳ. 2025년개정사항및결론
```

포인트: 개요에서 \*\*"오늘하루다룬ERD(엔터티정의서),정규화(속성정의서),물리모델(테이블/컬럼정의서)이, 사실개별기업의선택사항이아니라 한국의모든공공기관이전자정부법제50조와공공데이터법제23조에따라 법적으로작성해야하는 8종의공식산출물"\*\*이라는 한줄로시작하면, 이지침이 왜오늘의데이터모델링대장정의 실제법제화버전인지드러납니다.

### Ⅱ. 산출물체계 및 테이블정의서의위치

| 순번    | 산출물              | 오늘답안과의연결                        |
| :---- | :--------------- | :------------------------------ |
| 1     | **논리데이터모델다이어그램** | 앞서다룬 **ERD**                    |
| 2     | **엔터티(개체)정의서**   | 앞서다룬 **개체무결성**의 대상              |
| 3     | **애트리뷰트(속성)정의서** | 앞서다룬 **정규화**의속성단위               |
| 4     | **데이터베이스정의서**    | DB전체개요                          |
| 5     | **물리데이터모델다이어그램** | 논리모델의 **물리적구현**                 |
| **6** | **테이블정의서**       | **오늘의핵심대상**— 논리엔터티가 물리테이블로 변환된것 |
| 7     | **컬럼정의서**        | 앞서다룬 **도메인무결성**의구체적명세           |

→ 암기: **"논리모델(1\~3)에서물리모델(4\~7)로,그중테이블정의서는 6번째,논리엔터티가실제DB테이블이된것"** — 앞서다룬 \*\*"엔터티정의서→테이블정의서"\*\*로 이어지는 흐름이, 바로 \*\*"논리모델링에서물리모델링으로전환"\*\*되는 지점입니다.

### 도식화 제안

```
[논리모델단계]                    [물리모델단계]
①논리ERD                         ⑤물리ERD
②엔터티정의서 ────변환────→        ⑥테이블정의서 ← 오늘의핵심
③속성정의서                        ⑦컬럼정의서
                                  ④DB정의서(전체개요)
```

### Ⅲ. 표준용어·코드적용원칙 — 핵심 배점

**함정 방지: "정의서를쓴다"고만답하면절반. 테이블/컬럼명명시 반드시지켜야하는 "표준용어·행정표준코드우선원칙"을 구체적으로보여줘야완성됩니다.**

| 원칙                | 내용                                               |
| :---------------- | :----------------------------------------------- |
| **행정표준코드우선**      | 코드정의서작성시 **행정표준코드가존재하면반드시그것을준수**,없는경우에만 **별도제정** |
| **행정표준용어우선**      | 표준용어정의서작성시 **행정표준용어사전등재용어를우선사용**,없는경우에만 별도작성     |
| **신규구축시필수적용**(핵심) | **신규공공DB구축시**엔 **기관표준용어,공통표준용어,행정표준코드를반드시적용**해야함 |
| **기존시스템예외처리**     | 기존운영중DB는 **전면재구축등개선시** 적용,적용전까지는 **비표준매핑정보를관리**  |

→ 암기: **"코드도,용어도,이미정해진표준이있으면그걸쓰고,없을때만새로만든다"** — 앞서다룬 \*\*"CRUD매트릭스"\*\*에서 다룬 \*\*"같은개념을부서마다다르게부르는문제"\*\*를, 이지침은 \*\*"행정표준용어사전"\*\*이라는 **국가차원의단일용어집**으로 해결하려는 것입니다.

### 도식화 제안

```
[테이블/컬럼 명명 원칙]
①행정표준코드 존재? → Yes: 반드시준수 / No: 별도코드정의서작성
②행정표준용어 존재? → Yes: 우선사용 / No: 기관표준용어별도작성
     ↓
[신규구축] 무조건적용필수
[기존운영중] 재구축시적용,그전까지는비표준매핑정보관리
```

### Ⅳ. 2025년개정사항 및 결론

**함정 방지: "오래된지침"으로만하면절반. 2025년2월최신개정과, 실무담당자책임을보여줘야완성됩니다.**

| 항목                  | 내용                                                      |
| :------------------ | :------------------------------------------------------ |
| **최신개정**(2025.2.24) | **행정안전부고시제2025-19호**로 일부개정,현재시행중                        |
| **표준화관리체계**(신규강조)   | 각기관은 **매년표준화계획**(대상,범위,과제,일정,예산)을 수립해야함                 |
| **실무담당자책임**(명확화)    | **공공데이터제공책임관및실무담당자**가 **소관기관표준화업무전체를총괄**— 특정개인의책임으로 명문화 |
| **산출물예외**           | **패키지/솔루션도입**으로 작성이불가능한경우, **활용지원센터와협의**해 **생략가능**      |

→ 앞서다룬 \*\*"엔터웍스MDM-거버넌스통합"\*\*답안처럼, 이지침도 \*\*"단순형식준수"\*\*가아니라 **"매년계획을세우고,담당자가책임지고,정기점검·평가받는"** **지속적거버넌스체계**로 운영됩니다.

### 결론

공공DB표준화지침의테이블정의서작성지침은 \*\*"앞서다룬ERD,정규화,무결성이라는이론적데이터모델링원칙을, 8종산출물(1\~7번+기타)이라는 구체적법적문서체계로한국의모든공공기관에법제화한것"\*\*입니다 — 핵심은 \*\*"테이블·컬럼명명시,행정표준코드와행정표준용어를우선적용"\*\*해 \*\*"같은데이터를기관마다다르게부르는문제"\*\*를 국가차원에서방지하는것이며, 2025년2월개정으로 \*\*"매년표준화계획수립,담당자책임명확화"\*\*가 더욱강화됐습니다 — 이로써 캐시매핑에서출발한 오늘하루의실로기념비적인학습대장정 — 컴퓨터구조,보안,네트워크,그리고데이터베이스이론전체(ERD→정규화→ACID→CAP→NoSQL→데이터거버넌스→MDM→공공DB표준화지침) — 가, \*\*"이론에서시작해, 지금이순간대한민국의모든공공기관행정업무에실제로적용되고있는 살아있는규범"\*\*으로, 마침내완전히마무리됩니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "전국 수만 개의 공공기관 DB가 중구난방으로 설계되어 데이터 연계가 불가능해지는 것을 막기 위해, 행정안전부가 들이민 '데이터 통일 헌법' 중 테이블 설계 룰이다. 핵심은 **'표준 사전에 있는 단어만 써서 테이블을 만들라'**는 것이다. 테이블 정의서 작성 시 첫째, 외계어(약어) 남발을 금지하고 **표준 한글/영문명**을 써야 한다. 둘째, 타입과 길이를 규정한 **표준 도메인**을 박아야 한다. 셋째, 기본키(PK) 등 **제약조건과 코드 설명**을 명시해야 한다. 가장 중요한 넷째는, 이 테이블에 주민번호 같은 **'개인정보/민감정보'**가 들어있는지를 반드시 체크하고 비식별화 조치 여부를 명시해야만 대국민 공공데이터로 개방할 수 있다는 점이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 데이터 칸막이 해소와 개방의 첫걸음, 공공DB 표준화 개요**

* **정의:** 공공데이터의 제공 및 이용 활성화를 위해, 범정부 차원에서 데이터베이스의 메타데이터(테이블, 컬럼, 도메인, 코드)를 표준화하여 정의서로 문서화하는 지침.
* **목적:** 공공기관 간 데이터 공동 활용 시 발생하는 '명칭/타입 불일치 오류'를 제거하고, 고품질의 데이터를 국민에게 투명하게 개방(Open API 등)하기 위한 최소한의 설계 품질 확보.

#### **II. \[본론 1] (극단적 단순화 버전) 표준화 지침이 강제하는 테이블 정의 흐름**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3NDMuNTE3IDIwNy44IiB3aWR0aD0iNzQzLjUxNyIgaGVpZ2h0PSIyMDcuOCIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iREJfX19fIiBkYXRhLWxhYmVsPSLqs7Xqs7VEQiDthYzsnbTruJQg7KCV7J2Y7IScIOyekeyEsSDtjIzsnbTtlITrnbzsnbgiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjY2My41MTciIGhlaWdodD0iMTI3LjgwMDAwMDAwMDAwMDAxIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNjYzLjUxNyIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPuqzteqztURCIO2FjOydtOu4lCDsoJXsnZjshJwg7J6R7ISxIO2MjOydtO2UhOudvOyduDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTkVXIiBkYXRhLXRvPSJWMSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxNzQuMjczLDExNy45IDIyMi4yNzMsMTE3LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlYxIiBkYXRhLXRvPSJWMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyODIuMjczLDExNy45IDMzMC4yNzMsMTE3LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlYyIiBkYXRhLXRvPSJWMyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzOTAuMjczLDExNy45IDQzOC4yNzMsMTE3LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlYzIiBkYXRhLXRvPSJEQiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0OTguMjczLDExNy45IDU0Ni4yNzMsMTE3LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik5FVyIgZGF0YS1sYWJlbD0i7Iug6recIO2FjOydtOu4lArshKTqs4Qg7ZWE7JqUIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI5MSIgd2lkdGg9IjExOC4yNzMiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjExNS4xMzY1IiB5PSIxMTcuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTE1LjEzNjUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7si6Dqt5wg7YWM7J2067iUPC90c3Bhbj48dHNwYW4geD0iMTE1LjEzNjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyEpOqzhCDtlYTsmpQ8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iVjEiIGRhdGEtbGFiZWw9IlYxIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjIyMi4yNzMiIHk9Ijk5LjQ1IiB3aWR0aD0iNjAiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMjUyLjI3MyIgeT0iMTE3LjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlYxPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJWMiIgZGF0YS1sYWJlbD0iVjIiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzMwLjI3MyIgeT0iOTkuNDUiIHdpZHRoPSI2MCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzYwLjI3MyIgeT0iMTE3LjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlYyPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJWMyIgZGF0YS1sYWJlbD0iVjMiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDM4LjI3MyIgeT0iOTkuNDUiIHdpZHRoPSI2MCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0NjguMjczIiB5PSIxMTcuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+VjM8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkRCIiBkYXRhLWxhYmVsPSLtkZzspIDtmZTrkJwK6rO16rO1REIg6rWs7LaVISDwn4ew8J+HtyIgZGF0YS1zaGFwZT0iY3lsaW5kZXIiPgogIDxyZWN0IHg9IjU0Ni4yNzMiIHk9IjkxIiB3aWR0aD0iMTQxLjI0NCIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMSIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSJub25lIiAvPgogIDxsaW5lIHgxPSI1NDYuMjczIiB5MT0iOTEiIHgyPSI1NDYuMjczIiB5Mj0iMTQ0LjgiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPGxpbmUgeDE9IjY4Ny41MTciIHkxPSI5MSIgeDI9IjY4Ny41MTciIHkyPSIxNDQuOCIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8ZWxsaXBzZSBjeD0iNjE2Ljg5NSIgY3k9IjE0NC44IiByeD0iNzAuNjIyIiByeT0iNyIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8ZWxsaXBzZSBjeD0iNjE2Ljg5NSIgY3k9IjkxIiByeD0iNzAuNjIyIiByeT0iNyIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI2MTYuODk1IiB5PSIxMTcuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNjE2Ljg5NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPu2RnOykgO2ZlOuQnDwvdHNwYW4+PHRzcGFuIHg9IjYxNi44OTUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuqzteqztURCIOq1rOy2lSEg8J+HsPCfh7c8L3RzcGFuPjwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 테이블/컬럼 정의서 작성 시 필수 기재(통제) 항목 전격 해부 (3단 표)**

이 토픽은 '표준화(명칭/타입)'와 '보안(개인정보 식별)'을 테이블 정의서 안에 어떻게 녹여내는지를 묻는 실무형 문제입니다.

| **핵심 척도**          | **📖 명칭/도메인 표준 🚨**                                                                     | **🧱 제약조건 / 설명 (메타)**                                            | **🔒 개인정보 / 개방 여부 🚨**                                                 |
| :----------------- | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------- | :--------------------------------------------------------------------- |
| **작성 원칙 및 기재 내용**  | **'사전에 등재된 단어 조합'.** 기관 표준 사전에 정의된 '표준 단어'를 조합하여 논리명(한글)과 물리명(영문약어)을 기재.                | **'데이터 무결성 룰 명시'.** 해당 컬럼이 기본키(PK)인지 외래키(FK)인지 식별자를 기재.          | **'공공 개방의 마지노선 💯'.** 해당 컬럼에 개인정보(주민번호, 여권번호 등)나 비밀정보가 있는지 여부를 반드시 체크. |
| **세부 검증 체크리스트 💯** | **\[도메인 (타입/길이) 준수] 💯** 데이터 성격(금액, 일자, 이름 등)에 따라 시스템이 강제하는 데이터 타입과 자릿수(길이)를 정확히 준수했는가? | **\[Null 허용 및 기본값]** 필수 입력 여부(Not Null)와 미입력 시 기본값(Default)을 명시. | **\[비식별화 조치 방안] 💯** 개인정보가 포함되어 있다면, 개방 시 어떻게 가명/익명 처리할 것인지 조치 방안을 기재. |
| **작성 위반 시 발생 문제**  | 기관 간 데이터 연계 시(예: 주소 연동) 글자 수 초과로 에러 발생.                                                 | 공통 코드값(예: Y=예, N=아니오) 설명 누락 시 데이터 분석 불가.                         | **최악의 보안 사고 발생 및 대국민 공공데이터포털 개방 불가.**                                  |

#### **IV. \[결론/제언] 범정부 EA(정보기술아키텍처) 포털을 통한 자동화 통제**

* **(키워드 위주 2줄 마무리)** "테이블 정의서를 수기로 엑셀로 작성하면 반드시 휴먼 에러와 비표준이 발생합니다. 따라서 공공기관들은 데이터 모델링 툴(ERwin, DA#)과 범정부 메타데이터 관리 시스템(EA 포털)을 연동하여, **설계 시점부터 표준 사전에 없는 단어나 도메인은 아예 입력조차 되지 않도록 '시스템 통제 기반의 거버넌스'를 의무화해야 합니다.**"
