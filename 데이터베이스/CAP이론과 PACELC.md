### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (CAP의3요소, 왜"2개만"선택가능한가) — 3~4줄
Ⅱ. CAP의3대속성및선택조합 (본론①, 도식 1개 필수)
Ⅲ. PACELC - CAP의확장, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

CAP이론은 \*\*"분산시스템은일관성(C),가용성(A),분할내성(P) 3가지를 동시에완벽하게만족할수없고,최대2개만선택할수있다"\*\*는 것입니다 — 앞서다룬 \*\*"샤딩(여러서버로분산)"\*\*을 하는순간, \*\*"네트워크단절(P)이라는현실"\*\*을 피할수없고, 그때 **"정확성(C)과응답성(A)중 무엇을희생할지"** 선택해야합니다.

### Ⅱ. CAP의3대속성 및선택조합

| 속성                           | 내용                         |
| :--------------------------- | :------------------------- |
| **일관성**(Consistency)         | 모든노드가 **항상같은최신데이터**를보여줌    |
| **가용성**(Availability)        | 요청이오면 **항상응답**(설령오래된데이터라도) |
| **분할내성**(PartitionTolerance) | 네트워크가 **끊겨도시스템이계속동작**      |

**핵심통찰**: P(네트워크분할)는 \*\*"선택사항이아니라, 분산시스템이라면반드시일어나는현실"\*\*입니다 — 그래서 실제선택은 \*\*"P가발생했을때,C와A중무엇을포기할지"\*\*입니다.

| 조합     | 선택                        | 대표사례             |
| :----- | :------------------------ | :--------------- |
| **CP** | 분할시 **일관성우선**(불확실하면응답거부)  | 앞서다룬 **금융거래시스템** |
| **AP** | 분할시 **가용성우선**(오래된데이터라도응답) | 앞서다룬 **소셜미디어피드** |

→ 암기: **"분할은피할수없으니, 그순간에정확함을택할지, 응답함을택할지 정하는것"** — 앞서다룬 \*\*"격리수준"\*\*에서 \*\*"정확성vs성능"\*\*의 트레이드오프를 다뤘던것과 유사한구조가, 여기서는 \*\*"분산환경전체차원"\*\*으로 확장됩니다.

### 도식화 제안

```
[네트워크분할(P) 발생 - 피할수없는현실]
[서버A] ─────╳(단절)──────  [서버B]

[CP선택]                        [AP선택]
서버A: "B와연결안돼서            서버A: "일단내가가진값으로응답"
       확신할수없으니 응답거부"    (최신인지불확실해도 일단답함)
     ↓                          ↓
정확하지만 응답없을수있음         응답은있지만 오래된값일수있음
```

### Ⅲ. PACELC — CAP의확장, 핵심 배점

**함정 방지: "CAP만있다"고답하면절반. CAP이 "분할이생겼을때만"다룬다는한계와, PACELC가"평상시"트레이드오프까지다룬다는걸보여줘야완성됩니다.**

| 항목                 | 내용                                                                           |
| :----------------- | :--------------------------------------------------------------------------- |
| **CAP의한계**(핵심)     | CAP은 \*\*"네트워크분할(P)이발생했을때"\*\*의 선택만다룸 — \*\*"분할이없는평상시"\*\*는 다루지않음            |
| **PACELC의확장**      | **"P(분할)가생기면 A와C중선택,분할이Else(평상시)라면 L(지연시간)과C중선택"**                           |
| **평상시트레이드오프**(ELC) | 평상시에도, **"더빠른응답(Latency)을위해 약간의데이터불일치를감수할지, 확실한일관성(Consistency)을위해 좀더기다릴지"** |

→ 암기: **"PAC는분할시 가용성이냐일관성이냐,ELC는평상시에도 속도냐일관성이냐"** — 앞서다룬 \*\*"복제투명성(여러곳에복제)"\*\*을 생각하면: **"복제본에서읽으면빠르지만(L),혹시최신데이터가아직복제안됐으면 오래된값(C포기)"**— 이건 **네트워크가끊긴것도아닌데,평상시에도늘존재하는트레이드오프**입니다.

### 도식화 제안

```
[PACELC 구조]
     [P: 네트워크분할이발생하면?]
          ↙          ↘
       [A선택]      [C선택]
    (가용성우선)   (일관성우선)

     [Else: 평상시(분할없음)라면?]
          ↙          ↘
       [L선택]      [C선택]
    (빠른응답우선)  (일관성우선,약간느림)

예: DynamoDB = PA/EL (분할시가용성,평상시에도속도우선)
    MongoDB(기본설정) = PC/EC (일관성을더중시)
```

**실무적용예시**: 앞서다룬 \*\*"복제(Replication)"\*\*시스템에서 — \*\*"쓰기후바로읽으면, 복제가아직안끝나 최신값이안보일수있다"\*\*는 상황이, 바로 \*\*PACELC의"EL(평상시에도지연-일관성트레이드오프)"\*\*을 보여주는 대표사례입니다.

### Ⅳ. 결론

CAP이론은 \*\*"분산시스템에서네트워크분할은피할수없는현실이며, 그순간일관성과가용성중하나를반드시희생해야한다"\*\*는 근본적한계를 보여주고, PACELC는 여기서 한걸음더나가 \*\*"분할이없는평상시에도, 속도와일관성사이에서 늘선택이필요하다"\*\*는 것을 보여줍니다 — 이는 앞서다룬 \*\*"샤딩(분산으로확장하려는순간, CAP의트레이드오프를피할수없음)","복제투명성(여러복제본간 일관성유지의어려움)"\*\*같은 답안들이 왜 \*\*"완벽한해법이없는지"\*\*를 이론적으로설명하는 근본원리입니다 — 오늘하루다룬 방대한데이터베이스시리즈전체(정규화→ACID→REDO/UNDO→분산DB투명성→샤딩→CAP/PACELC)가, \*\*"분산시스템은결국,무엇을희생할지를 명확히인식하고선택하는것"\*\*이라는 데이터베이스이론의 궁극적깨달음으로 완결됩니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "분산 시스템(NoSQL) 설계에서 세 마리 토끼를 다 잡을 수 없다는 잔혹한 법칙이다. 첫째, **CAP 이론**. 분산 시스템은 일관성(C), 가용성(A), 네트워크 단절 감내(P) 세 가지를 절대 다 가질 수 없다. 현실에선 네트워크 통신 장애(P)가 언제든 터지므로 P를 고정하고 나면, 결국 '응답을 멈춰서라도 정확성을 지킬지(CP)' 아니면 '오류가 있더라도 일단 응답은 할지(AP)' 둘 중 하나만 골라야 한다. 둘째, **PACELC 정리**. CAP 이론은 '장애가 터졌을 때'의 이야기만 한다. 이를 보완한 PACELC는 '네트워크가 멀쩡할 때(Else)'의 딜레마를 추가했다. 평상시에도 데이터를 완벽히 똑같이(일관성, C) 맞추려면 동기화하느라 응답이 느려지고, 빛의 속도로 응답(지연시간 최소화, L)하려면 일관성을 포기해야 한다는 것을 수식화한 완성형 이론이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 분산 환경의 트레이드오프, CAP와 PACELC 개요**

* **CAP 이론:** 분산 시스템은 Consistency(일관성), Availability(가용성), Partition Tolerance(네트워크 단절 허용)의 3가지 속성 중 최대 2가지만 가질 수 있다는 에릭 브루어의 정리.
* **PACELC 정리:** CAP 이론이 평상시(네트워크 정상 상태)의 성능 딜레마를 설명하지 못하는 단점을 보완하여, 평상시에는 Latency(지연시간)와 Consistency(일관성) 중 하나를 선택해야 함을 증명한 확장 이론.

#### **II. \[본론 1] (극단적 단순화 버전) 장애 시와 평상시의 양자택일 파이프라인**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzNTYuOTg0MDAwMDAwMDAwMDQgNDM3LjQwMDAwMDAwMDAwMDAzIiB3aWR0aD0iMzU2Ljk4NDAwMDAwMDAwMDA0IiBoZWlnaHQ9IjQzNy40MDAwMDAwMDAwMDAwMyIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iUEFDRUxDX19fIiBkYXRhLWxhYmVsPSJQQUNFTEMg7KCV66as7J2YIOyEoO2DnSDrhbzrpqwiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjI3Ni45ODQwMDAwMDAwMDAwNCIgaGVpZ2h0PSIzNTcuNDAwMDAwMDAwMDAwMDMiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIyNzYuOTg0MDAwMDAwMDAwMDQiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5QQUNFTEMg7KCV66as7J2YIOyEoO2DnSDrhbzrpqw8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlAiIGRhdGEtdG89IkMxIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE2Mi45MzA5OTk5OTk5OTk5OCwxMjAuOSAxNjIuOTMwOTk5OTk5OTk5OTgsMTY4LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkUiIGRhdGEtdG89IkMyIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE3OC40OTIwMDAwMDAwMDAwMiwyNzkuNiAxNzguNDkyMDAwMDAwMDAwMDIsMzI3LjYiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlAiIGRhdGEtbGFiZWw9IlA6IOuEpO2KuOybjO2BrCDri6jsoIgg7J6l7JWgIOuwnOyDnSEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMjEzLjg2MTk5OTk5OTk5OTk3IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjE2Mi45MzA5OTk5OTk5OTk5OCIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5QOiDrhKTtirjsm4ztgawg64uo7KCIIOyepeyVoCDrsJzsg50hPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDMSIgZGF0YS1sYWJlbD0iQzog7KCV7ZmV7ISxIOyngO2CpOyekArrp57stpwg65WM6rmM7KeAIOyLnOyKpO2FnCDsiqTthrEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNjQuNTIxNDk5OTk5OTk5OTkiIHk9IjE2OC45IiB3aWR0aD0iMTk2LjgxOSIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE2Mi45MzA5OTk5OTk5OTk5OCIgeT0iMTk1LjgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE2Mi45MzA5OTk5OTk5OTk5OCIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPkM6IOygle2ZleyEsSDsp4DtgqTsnpA8L3RzcGFuPjx0c3BhbiB4PSIxNjIuOTMwOTk5OTk5OTk5OTgiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuunnuy2nCDrlYzquYzsp4Ag7Iuc7Iqk7YWcIOyKpO2GsTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJFIiBkYXRhLWxhYmVsPSJFIChFbHNlKTog64Sk7Yq47JuM7YGsIO2PieyDgeyLnCDrqYDsqaHtlagiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9IjI0Mi43MDAwMDAwMDAwMDAwMiIgd2lkdGg9IjI0NC45ODQiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTc4LjQ5MjAwMDAwMDAwMDAyIiB5PSIyNjEuMTUwMDAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkUgKEVsc2UpOiDrhKTtirjsm4ztgawg7Y+J7IOB7IucIOupgOypoe2VqDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQzIiIGRhdGEtbGFiZWw9IkM6IOyZhOuyve2VmOqyjCDrj5nquLDtmZTtlZjsnpAK64yA7IugIOydkeuLtSDsho3rj4Qg64qQ66Ck7KeQIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjgyLjY3NjAwMDAwMDAwMDAyIiB5PSIzMjcuNiIgd2lkdGg9IjE5MS42MzE5OTk5OTk5OTk5OCIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE3OC40OTIwMDAwMDAwMDAwMiIgeT0iMzU0LjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE3OC40OTIwMDAwMDAwMDAwMiIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPkM6IOyZhOuyve2VmOqyjCDrj5nquLDtmZTtlZjsnpA8L3RzcGFuPjx0c3BhbiB4PSIxNzguNDkyMDAwMDAwMDAwMDIiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuuMgOyLoCDsnZHri7Ug7IaN64+EIOuKkOugpOynkDwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] CAP 이론과 PACELC 정리 핵심 전격 대조 (3단 표)**

가장 중요한 출제 포인트는 PACELC에서 \*\*'네트워크 정상 시(Else)'\*\*에 발생하는 \*\*'속도(Latency)와 정확성(Consistency)'\*\*의 충돌을 명확히 설명하는 것입니다.

| **핵심 척도**         | **⚖️ CAP 이론**                                                                    | **🎯 PACELC 정리 (확장) 🚨**                                                                                                                |
| :---------------- | :------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **핵심**            | 분산 시스템은 C, A, P 중 **2가지만 선택 가능**함. (실제로는 CA는 불가능하여 CP vs AP로 귀결됨).               | 장애 시(P)의 A/C 선택뿐만 아니라, **평상시(E)의 속도(L)/정확성(C) 선택을 추가함.**                                                                                |
| **장애 시 (P) 🚨**   | **'CP 아님 AP 선택'.** 네트워크가 끊어지면 데이터 동기화가 안 되므로, 응답을 멈출지(CP) 그냥 옛날 데이터라도 줄지(AP) 고름. | **'PAC (CAP와 동일)'.** Partition 발생 시 Availability 와 Consistency 중 하나를 선택함.                                                               |
| **정상 시 (E) 🚨**   | **\[언급 없음 (한계점) ❌]** 네트워크가 멀쩡할 때는 시스템이 어떻게 동작해야 하는지 설명하지 못함.                     | **\[ELC (Latency vs Consistency) 💯]** 네트워크가 정상(Else)일 때, 데이터를 0.1초 만에 빨리 줄지(Latency), 아니면 전 세계 백업 서버를 완벽히 동기화하고 줄지(Consistency) 양자택일함. |
| **대표적인 NoSQL 분류** | HBase, MongoDB (CP 모델) Cassandra, DynamoDB (AP 모델)                               | **PA/EL:** DynamoDB (일단 빠르고 안 멈춤) **PC/EC:** HBase (조금 느려도 무조건 정확함)                                                                     |

#### **IV. \[결론/제언] 글로벌 서비스의 표준, 결과적 일관성(Eventual Consistency) 추구**

* **(키워드 위주 2줄 마무리)** "페이스북, 아마존 같은 글로벌 서비스는 시스템이 멈추거나(A 포기) 응답이 느려지는 것(L 포기)을 절대 용납하지 않습니다. 따라서 현대 분산DB는 PA/EL 구조를 채택하여 즉각적인 응답을 주되, 백그라운드 동기화를 통해 **'언젠가는 데이터가 일치하게 되는(Eventual Consistency)' 결과적 일관성 모델을 아키텍처의 기본 표준으로 삼고 있습니다.**"
