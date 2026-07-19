## 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (NoSQL등장배경, CAP과의연결) — 3~4줄
Ⅱ. Key-Value - 가장단순한구조 (본론①, 도식 1개 필수)
Ⅲ. Document/Graph - 구조화된유연성, 핵심 배점
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서다룬CAP이론에서'분산환경에서는C와A를둘다완벽히가질수없다'고했는데, RDBMS는전통적으로C(일관성)에크게치우쳐있다 — NoSQL은 '정규화,ACID같은엄격함을일부포기하고,대신A(가용성)와확장성을택하는'철학으로등장"\*\*했다는 한줄로시작하면, 왜 CAP이론직후 NoSQL이 논리적으로이어지는지 드러납니다.

### Ⅱ. Key-Value — 가장단순한구조

| 항목       | 내용                                                               |
| :------- | :--------------------------------------------------------------- |
| **구조**   | \*\*키(Key)\*\*와 \*\*값(Value)\*\*의 단순한쌍 — 값의내부구조는 **DB가전혀신경쓰지않음** |
| **장점**   | **극도로빠른조회**(키만알면 O(1)에가까운속도)                                     |
| **한계**   | **값내부의특정필드로검색불가**(값전체를 하나의블록으로만다룸)                               |
| **대표사례** | **Redis,DynamoDB**— 캐시,세션관리                                      |

→ 암기: **"열쇠하나로,금고하나를 통째로꺼낸다"** — 앞서다룬 \*\*"확장성해싱"\*\*의 원리가 그대로 재현됩니다: \*\*"키를해시해서 버킷(값)을찾는것"\*\*이 Key-Value DB의핵심동작입니다.

### 도식화 제안

```
[Key-Value 구조]
Key: "user:1001"  →  Value: {전체데이터블록,내용은DB가모름}
Key: "session:abc" →  Value: {로그인상태,만료시간등}

조회: "user:1001" 키로 즉시전체값반환(내부필드검색은불가)
```

### Ⅲ. Document / Graph — 구조화된유연성, 핵심 배점

**함정 방지: "Key-Value보다복잡하다"고만답하면절반. 각각이 "무엇을위해특화됐는지" RDBMS와의구체적차이를보여줘야완성됩니다.**

**Document(문서형)**

| 항목            | 내용                                                                                                                  |
| :------------ | :------------------------------------------------------------------------------------------------------------------ |
| **구조**        | **JSON/BSON형태**로, **자유로운스키마**(같은컬렉션안에서도 문서마다필드가다를수있음)                                                               |
| **RDBMS와의차이** | 앞서다룬 \*\*"정규화"\*\*가 \*\*"관련데이터를 여러테이블로쪼개는것"\*\*이었다면, Document는 **"관련데이터를 한문서안에 중첩(nested)해서 통째로저장"**— **반정규화가기본전제** |
| **대표사례**      | **MongoDB**                                                                                                         |

**Graph(그래프형)**

| 항목       | 내용                                                                                                                                 |
| :------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| **구조**   | \*\*노드(개체)+엣지(관계)\*\*로 데이터자체를 **그래프로표현**                                                                                           |
| **강점**   | 앞서다룬 \*\*"참조무결성(FK로연결)"\*\*을 통한JOIN이 **관계가복잡해질수록기하급수적으로느려지는데**, Graph DB는 \*\*"관계자체가1급데이터"\*\*라 **친구의친구의친구**같은 **깊은관계탐색이일정한속도**로가능 |
| **대표사례** | **Neo4j**— 소셜네트워크,추천시스템                                                                                                            |

→ 암기: **"Document는 관련데이터를한바구니에 통째로담고(반정규화),Graph는 관계자체를노드와선으로직접표현한다(JOIN회피)"** — 앞서다룬 \*\*"반정규화"\*\*답안에서 \*\*"조회성능을위해정규화를의도적으로깨는것"\*\*이 Document DB에서는 \*\*"기본설계철학자체"\*\*로 승격됩니다.

### 도식화 제안

```
[Document - MongoDB]
{
  "주문번호": 1001,
  "고객": {"이름":"김철수","주소":"서울"},  ← 중첩(정규화안함)
  "상품목록": [{"상품A",2개},{"상품B",1개}]
}
(관련정보를 조인없이 한번에 통째로조회)

[Graph - Neo4j]
[김철수]──친구──→[이영희]──친구──→[박민수]
   ↓RDBMS라면
   3단계JOIN 필요(친구의친구의친구찾기)
   ↓Graph DB라면
   그래프를 관계선따라 그냥타고가면끝(일정속도)
```

**3구조비교**

| 구분        | **Key-Value**     | **Document**    | **Graph**          |
| :-------- | :---------------- | :-------------- | :----------------- |
| **최적사례**  | 캐시,세션             | 반정형데이터(로그,카탈로그) | 관계탐색(추천,소셜)        |
| **CAP성향** | 대부분 **AP**(가용성우선) | 설정에따라다름         | 대부분 **CP** 또는일관성중시 |

### Ⅳ. 결론

Key-Value,Document,Graph는 **"앞서다룬RDBMS의정규화·ACID·CAP의엄격함을각자다른방식으로내려놓아, 특정용도에더적합해진"** 구조들입니다 — Key-Value는 \*\*"극도의단순함으로속도"\*\*를, Document는 \*\*"반정규화를기본전제로 유연성"\*\*을, Graph는 \*\*"관계자체를1급데이터로만들어 JOIN의한계를우회"\*\*합니다 — 이는 앞서다룬 \*\*"CAP이론(완벽한선택은없다)"\*\*이 \*\*"그럼그특성을 각데이터모델이 어떻게다르게받아들이는지"\*\*로 구체화된 것이며, 오늘하루다룬 방대한데이터베이스시리즈전체(정규화→ACID→CAP→NoSQL)가 \*\*"모든데이터가관계형테이블에맞는건아니다"\*\*라는 결론으로 완결됩니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "표(테이블)라는 감옥에서 벗어나 빅데이터를 무한대로 담고 쪼개기(Scale-out) 위해 탄생한 NoSQL의 3대장이다. 첫째, **키-값(Key-Value)**. DB계의 단순 무식한 사전이다. 유일한 '키'에 통짜 '값'을 묶어 저장한다. 복잡한 검색은 못 하지만, 구조가 너무 가벼워 초당 수백만 건을 쳐내는 초고속 캐시(Redis)의 제왕이다. 둘째, **문서(Document)**. 키-값 모델의 진화형이다. 값 부분에 'JSON' 문서 덩어리를 통째로 집어넣는데, DB가 문서 속을 들여다볼 수 있어 "나이가 20살인 문서 다 가져와" 같은 유연한 검색이 가능한 가장 대중적인 NoSQL(MongoDB)이다. 셋째, **그래프(Graph)**. 점(노드)과 선(관계)으로 데이터를 거미줄처럼 엮는다. '내 친구의 친구가 산 물건' 같은 RDBMS의 조인(Join) 폭탄을 빛의 속도로 풀어내는 추천 시스템의 제왕(Neo4j)이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] RDBMS의 스케일업 한계 돌파, NoSQL (Not Only SQL) 개요**

* **정의:** 고정된 스키마와 복잡한 조인(Join) 연산을 과감히 버리고, 분산 아키텍처를 통한 무한한 수평 확장성(Scale-out)과 고가용성을 확보한 비관계형 데이터베이스 저장소.
* **등장 배경:** 비정형 데이터(JSON, 이미지, 로그)의 폭발적 증가와 글로벌 웹 서비스의 수만 TPS 트래픽을 기존 RDBMS로는 감당할 수 없었기 때문.

#### **II. \[본론 1] (극단적 단순화 버전) NoSQL 3대 구조의 데이터 저장 사상**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzNDguODMyOTk5OTk5OTk5OTcgMzkyLjEiIHdpZHRoPSIzNDguODMyOTk5OTk5OTk5OTciIGhlaWdodD0iMzkyLjEiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Ik5vU1FMXzNfX18iIGRhdGEtbGFiZWw9Ik5vU1FMIDPrjIAg642w7J207YSwIOuqqOuNuCDslYTtgqTthY3sspgiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjI2OC44MzI5OTk5OTk5OTk5NyIgaGVpZ2h0PSIzMTIuMSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjI2OC44MzI5OTk5OTk5OTk5NyIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPk5vU1FMIDPrjIAg642w7J207YSwIOuqqOuNuCDslYTtgqTthY3sspg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IktWIiBkYXRhLWxhYmVsPSIxLiBLZXktVmFsdWUg8J+UkQonVXNlcjEnIOKelCAnRGF0YeuNqeyWtOumrCcK7LSI6rOg7IaNIDE6MSDrp6TtlZEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMTc2LjgxMTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxNDQuNDA2IiB5PSIxMTkuMzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE0NC40MDYiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj4xLiBLZXktVmFsdWUg8J+UkTwvdHNwYW4+PHRzcGFuIHg9IjE0NC40MDYiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPiYjMzk7VXNlcjEmIzM5OyDinpQgJiMzOTtEYXRh642p7Ja066asJiMzOTs8L3RzcGFuPjx0c3BhbiB4PSIxNDQuNDA2IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7stIjqs6Dsho0gMToxIOunpO2VkTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJET0MiIGRhdGEtbGFiZWw9IjIuIERvY3VtZW50IPCfk4QKJ1VzZXIxJyDinpQge+ydtOumhDrtmY3quLjrj5ksIOuCmOydtDoyMH0KSlNPTiDrjanslrTrpqwg7JGk7IWU64Sj6riwIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIyNjUuNCIgd2lkdGg9IjIzNi44MzMiIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjE3NC40MTY0OTk5OTk5OTk5OCIgeT0iMzAwLjc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNzQuNDE2NDk5OTk5OTk5OTgiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj4yLiBEb2N1bWVudCDwn5OEPC90c3Bhbj48dHNwYW4geD0iMTc0LjQxNjQ5OTk5OTk5OTk4IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj4mIzM5O1VzZXIxJiMzOTsg4p6UIHvsnbTrpoQ67ZmN6ri464+ZLCDrgpjsnbQ6MjB9PC90c3Bhbj48dHNwYW4geD0iMTc0LjQxNjQ5OTk5OTk5OTk4IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5KU09OIOuNqeyWtOumrCDskaTshZTrhKPquLA8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iR1JBIiBkYXRhLWxhYmVsPSIzLiBHcmFwaCDwn5W477iPCu2Zjeq4uOuPmSDinpQgKOy5nOq1rCkg4p6UIOydtOuqveujoQrrqqjrk6Ag6rKD7J2EIOyEoOycvOuhnCDsl67quLAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9IjE3NC43IiB3aWR0aD0iMjA2LjQ1MiIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTU5LjIyNiIgeT0iMjEwLjA0OTk5OTk5OTk5OTk4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNTkuMjI2IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+My4gR3JhcGgg8J+VuO+4jzwvdHNwYW4+PHRzcGFuIHg9IjE1OS4yMjYiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPu2Zjeq4uOuPmSDinpQgKOy5nOq1rCkg4p6UIOydtOuqveujoTwvdHNwYW4+PHRzcGFuIHg9IjE1OS4yMjYiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuuqqOuToCDqsoPsnYQg7ISg7Jy866GcIOyXruq4sDwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] Key-Value vs Document vs Graph 전격 대조 (3단 표)**

이 토픽은 각 모델이 데이터의 '내용물(Value)'을 데이터베이스 엔진이 이해할 수 있는지 없는지에 따른 **'검색 능력의 차이'**를 대조하는 것이 핵심입니다.

| **핵심 척도**            | **🔑 Key-Value Store**                                                                     | **📄 Document Store 🚨**                                                                               | **🕸️ Graph Store**                                                              |
| :------------------- | :----------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------- |
| **데이터 구조**           | **'키와 통짜 값 (Dictionary)'.** 단순한 식별자(Key)에 텍스트, 이미지 등 무엇이든 담길 수 있는 값(Value)을 1:1로 매핑.       | **'키와 JSON 문서 (Tree) 💯'.** 값(Value) 자리에 구조화된 반정형 문서(JSON, XML)를 통째로 때려 박음.                            | **'노드와 엣지 (Network)'.** 데이터를 개체(Node)로 정의하고, 개체 간의 관계를 선(Edge)으로 연결하여 속성 부여.     |
| **검색 능력 및 주요 강점 🚨** | **\[속도 최강 / 내부 검색 불가]** DB가 Value 안에 뭐가 들었는지 모름(Opaque). 오직 'Key'로만 값을 찾을 수 있어 빛의 속도를 자랑함. | **\[스키마 프리 / 유연한 검색 💯]** DB가 JSON 문서 내부 구조를 읽어냄. 따라서 "JSON 안의 `age>20`인 놈들" 식의 **유연한 쿼리(필드 검색)가 가능.** | **\[조인(Join) 없이 관계 추적]** 꼬리에 꼬리를 무는 연관 관계 탐색에 있어 RDBMS의 수십 개 조인보다 수백 배 빠른 성능 발휘. |
| **대표 제품 / 활용**       | **Redis, DynamoDB.** 인메모리 캐시, 장바구니, 세션.                                                    | **MongoDB, Couchbase.** 웹 게시판, 로그 수집, 백엔드 서버.                                                          | **Neo4j, AWS Neptune.** SNS 친구 추천, 사기 탐지(FDS).                                   |

*(참고: NoSQL의 4대 구조로 꼽히는 Column-Family(HBase, Cassandra) 모델은 엄청나게 거대한 열(Column)들의 집합으로 빅데이터 쓰기에 특화된 모델입니다.)*

#### **IV. \[결론/제언] Polyglot Persistence 전략 및 NewSQL의 등장**

* **(키워드 위주 2줄 마무리)** "현대 글로벌 아키텍처는 단일 DB에 모든 것을 담지 않습니다. RDB(결제), MongoDB(사용자 프로필), Redis(캐시), Neo4j(추천)를 섞어 쓰는 **'다국어 영속성(Polyglot Persistence)'이 기본입니다. 나아가 최근에는 NoSQL의 확장성(Scale-out)과 RDBMS의 트랜잭션(ACID)을 동시에 보장하는 구글 Spanner 같은 'NewSQL'이 차세대 분산 DB로 부상하고 있습니다.**"
