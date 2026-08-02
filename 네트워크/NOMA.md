### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (NOMA정의, OFDMA와의근본적차이) — 3~4줄
Ⅱ. 핵심원리 - 전력차이로구분 (본론①, 도식 1개 필수)
Ⅲ. SIC - 순차적간섭제거 (본론②, 핵심 배점)
Ⅳ. 6G에서의확장및한계
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬Wi-Fi의OFDMA는 '주파수를쪼개서(직교하게분리) 각사용자에게한조각씩배정'했는데, NOMA는정반대 — '같은주파수,같은시간을 여러사용자가동시에공유'하게 의도적으로직교성을깨뜨린다"\*\*는 한줄로시작하면, 왜NOMA가 "비직교(Non-Orthogonal)"라는 이름을가졌는지 명확해집니다.

### Ⅱ. 핵심원리 — 전력차이로구분

| 개념                            | 내용                                                                             |
| :---------------------------- | :----------------------------------------------------------------------------- |
| **중첩코딩**(SuperpositionCoding) | 여러사용자의신호를 **같은주파수·시간에겹쳐서전송**                                                   |
| **전력할당의역설**                   | 기지국에서 \*\*가까운사용자(신호강함)\*\*에겐 **적은전력**,\*\*먼사용자(신호약함)\*\*에겐 **더많은전력**할당         |
| **왜역설인가**                     | 직관적으론"가까운사람에게전력을더줘야할것같은데", 실제로는 \*\*"약한신호를전력으로보완해주고, 강한신호는적은전력으로도구분가능"\*\*하기때문 |

→ 암기: **"같은주파수·시간에겹쳐보내고, 멀리있는사람에게전력을더준다"** — 앞서다룬 \*\*"Wi-Fi의OFDMA"\*\*가 **"자원(RU)을나눠서"** 구분했다면, NOMA는 **"전력의크기로"** 구분한다는게 근본적차이입니다.

### 도식화 제안

```
[OFDMA - 앞서다룬Wi-Fi방식]           [NOMA]
주파수를쪼개서 각자할당               같은주파수·시간을 공유
[RU1:사용자A][RU2:사용자B]           [사용자A(낮은전력)+사용자B(높은전력)] 중첩전송
(자원을나눔,직교)                    (전력차이로구분,비직교)
```

### Ⅲ. SIC — 순차적간섭제거, 핵심 배점

**함정 방지: "겹쳐서보낸다"고만답하면절반. 겹쳐진신호를 수신자가어떻게다시분리해내는지구체적과정을보여줘야완성됩니다.**

| 단계            | 내용                                               |
| :------------ | :----------------------------------------------- |
| **①강한신호부터해독** | 신호가강한사용자(가까운A)는 **먼저상대(B)의고출력신호를해독**             |
| **②제거**       | 해독한B의신호를 **전체수신신호에서빼서(제거)**                      |
| **③자신의신호해독**  | 남은(B신호가제거된) 신호에서 **자신(A)의저출력신호를해독**              |
| **먼사용자(B)는**  | 자신에게할당된 **고출력신호만바로해독**(다른신호제거불필요, 신호가원래강해서묻히지않음) |

→ 암기: **"가까운사람은남의(먼사람의)신호를먼저알아내고빼버린다음,자기신호를찾는다 — 먼사람은자기신호가원래크니까바로찾는다"** — 이 \*\*SIC(SuccessiveInterferenceCancellation,순차적간섭제거)\*\*가 NOMA의핵심메커니즘이며, 앞서다룬 \*\*"해밍코드"\*\*가 \*\*"오류를수학적으로찾아내정정"\*\*했듯, SIC는 \*\*"겹쳐진신호를수학적으로벗겨내분리"\*\*합니다.

### 도식화 제안

```
[SIC 해독과정 - 사용자A(가까움,저전력) 관점]
[수신된중첩신호] = A의신호(약함) + B의신호(강함)
        ↓
①B의강한신호를먼저해독
        ↓
②전체신호에서 B신호를제거
        ↓
③남은신호 = A의신호만 → 해독완료

[사용자B(멀리,고전력) 관점]
[수신된중첩신호] = A의신호(약함,거의무시) + B의신호(강함)
        ↓
바로B신호해독(A신호가약해서 큰방해안됨)
```

### Ⅳ. 6G에서의확장 및 한계

**함정 방지: "6G에좋다"고만하면절반. 구체적확장기술과, 앞서다룬6G요구사항(mMTC등)과의직결점, 그리고현실적한계를보여줘야완성됩니다.**

| 확장/한계             | 내용                                                                                            |
| :---------------- | :-------------------------------------------------------------------------------------------- |
| **CD-NOMA**(코드기반) | **SCMA,PDMA**등 — 사용자마다 **고유코드/패턴**부여,**대규모IoT연결(mMTC)+URLLC**에적합 — 앞서다룬 **6G의"연결밀도"성능지표**와 직결 |
| **협력형NOMA**       | 사용자간 **신호중계**로 커버리지·신뢰성향상                                                                     |
| **핵심한계**          | **복잡도가높음**(SIC를수신단마다구현해야함)— 다만6G시대 **연산능력향상으로 극복가능**하다고전망                                     |

→ 앞서다룬 \*\*"6G의목표서비스(신규결합서비스,연결성확장)"\*\*답안에서 다뤘던 \*\*"수많은기기의동시연결"\*\*요구가, NOMA의 \*\*"같은자원을여러사용자가동시공유"\*\*라는 근본원리와 정확히맞아떨어집니다 — 앞서다룬 **6G상용화가 2030년에서2029년으로단축**전망되는 만큼, NOMA같은핵심기술의 실용화도 가속화되고있습니다.

### 도식화 제안

```
[NOMA 6G 활용]
CD-NOMA(SCMA,PDMA) → 대규모IoT(mMTC) + 초저지연(URLLC)
협력형NOMA → 커버리지·신뢰성향상
     ↓
앞서다룬 6G의"연결밀도","신뢰성" 성능지표를 직접구현하는기술
```

### Ⅴ. 결론

NOMA는 **"앞서다룬OFDMA(자원을나눠서직교하게분리)의정반대접근 — 자원을나누지않고, 전력차이와SIC(순차적간섭제거)로 여러사용자를동시에같은자원에태우는"** 혁신적인다중접속기술입니다 — 이는앞서다룬 \*\*6G의핵심요구사항(연결밀도확장,mMTC,URLLC)\*\*을 물리계층에서 직접실현하는 핵심기술이며, \*\*"직교성을지키는것이항상최선은아니다"\*\*라는 통신이론적발상의전환을 보여줍니다 — 이로써 캐시매핑에서시작해 오늘하루종일이어진 방대한컴퓨터구조·보안·네트워크의대장정이, \*\*"자원을어떻게나누고,공유할것인가"\*\*라는 근본질문에대한 가장최신의답(NOMA)으로 마무리됩니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "기존 4G(LTE)까지의 통신은 \*\*'OMA(직교 방식)'\*\*이었다. 주파수(도로)를 시간이나 대역으로 완벽히 쪼개서 차들이 절대 부딪히지 않게 다녔다. 간섭(에러)은 없었지만, 차선이 꽉 차면 더 이상 접속을 수용할 수 없는 치명적 한계가 있었다. 5G/6G 시대에는 좁은 반경에 수만 대의 IoT 기기가 동시 접속해야 한다. 그래서 룰을 깨버린 천재적인 아이디어가 \*\*'NOMA(비직교 방식)'\*\*이다. 차선을 쪼개지 않고, 동일한 시간과 주파수에 여러 명의 데이터를 확 겹쳐서(중첩) 동시에 쏴버리는 것이다. 이 마법을 가능케 하는 두 가지 무기가 있다. 기지국(송신자)은 멀리 있는 폰에겐 '큰 전력(목소리)'을, 가까이 있는 폰에겐 '작은 전력'을 할당해 하나의 덩어리로 뭉쳐서 쏘는 \*\*'중첩 코딩(SC)'\*\*을 쓴다. 덩어리를 받은 스마트폰(수신자)은 수학적 공식을 이용해, 나보다 전력이 큰 남의 데이터를 쓰레기(노이즈)로 취급해 확 빼버리고(제거) 내 데이터만 쏙 발라내는 **'간섭 제거(SIC)'** 기술을 쓴다."

***

### **\<span style="font 시="font-size: 1.5em; font-weight: bold;">2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 수용 용량의 한계를 부수는 마법, NOMA(비직교 다중 접속) 개요**

* **정의:** 5G 및 6G 이동통신에서 초연결(mMTC)과 대용량 접속을 지원하기 위해, **동일한 시간·주파수 자원에 다수의 사용자 데이터를 '서로 다른 전력(Power) 크기'로 겹쳐서(중첩하여) 전송**하는 다중 접속 기술.
* **도입 배경:** 시간, 주파수, 코드를 서로 겹치지 않게 철저히 직교(Orthogonal)시켜 나누어 쓰던 기존 OMA(OFDMA 등) 방식은 더 이상 폭증하는 IoT 기기를 감당할 물리적 대역폭이 없기 때문에, 발상의 전환이 필요했음.

#### **II. \[본론 1] (극단적 단순화 버전) 겹쳐서 쏘고, 수학으로 빼내는 NOMA 파이프라인**

복잡한 전파 수식 다 빼고, **송신자가 합치고 수신자가 빼내는 과정**만 직관적으로 그렸습니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5NTIuNDMyIDI0NC41IiB3aWR0aD0iOTUyLjQzMiIgaGVpZ2h0PSIyNDQuNSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iTk9NQV9fX18yX19fIiBkYXRhLWxhYmVsPSJOT01BICjruYTsp4HqtZAg64uk7KSRIOygkeyGjSkgMuuMgCDtlbXsi6wg6riw7IigIOuplOy7pOuLiOymmCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iODcyLjQzMiIgaGVpZ2h0PSIxNjQuNSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9Ijg3Mi40MzIiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5OT01BICjruYTsp4HqtZAg64uk7KSRIOygkeyGjSkgMuuMgCDtlbXsi6wg6riw7IigIOuplOy7pOuLiOymmDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQkFTRSIgZGF0YS10bz0iUEhPTkUiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuuPmeydvO2VnCDso7ztjIzsiJjroZwg6rK57LOQ7IScIOyghOyGoSIgcG9pbnRzPSIyMjkuMTA3LDEzNi4yNSA0ODIuNjYzLDEzNi4yNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUEhPTkUiIGRhdGEtdG89Ik1BVEgiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNTY5LjA3MywxMzYuMjUgNjE3LjA3MywxMzYuMjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209Ik1BVEgiIGRhdGEtdG89Ik1JTkUiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNjk2LjgxNCwxMzYuMjUgNzQ0LjgxNCwxMzYuMjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQkFTRSIgZGF0YS10bz0iUEhPTkUiIGRhdGEtbGFiZWw9IuuPmeydvO2VnCDso7ztjIzsiJjroZwg6rK57LOQ7IScIOyghOyGoSI+CiAgPHJlY3QgeD0iMjczLjEwNjk5OTk5OTk5OTk3IiB5PSIxMjAuMjUiIHdpZHRoPSIxNjUuNTU2MDAwMDAwMDAwMDQiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzNTUuODg1IiB5PSIxMzUuNCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+64+Z7J287ZWcIOyjvO2MjOyImOuhnCDqsrnss5DshJwg7KCE7IahPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJCQVNFIiBkYXRhLWxhYmVsPSLquLDsp4Dqta0g8J+ToQrinKggMS4g7KSR7LKpIOy9lOuUqSAoU0MpIOKcqArqsIDquYzsmrQg7Y+wID0gMjBXIO2VoOuLuQrrqLwg7Y+wID0gODBXIO2VoOuLuQrstJ0gMTAwVyDrrYntg7HsnbTroZwg7I+oISIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSIxNzMuMTA3IiBoZWlnaHQ9IjEwNC41MDAwMDAwMDAwMDAwMSIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjE0Mi41NTM0OTk5OTk5OTk5OSIgeT0iMTM2LjI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNDIuNTUzNDk5OTk5OTk5OTkiIGR5PSItMjkuMjUwMDAwMDAwMDAwMDA0Ij7quLDsp4Dqta0g8J+ToTwvdHNwYW4+PHRzcGFuIHg9IjE0Mi41NTM0OTk5OTk5OTk5OSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+4pyoIDEuIOykkeyyqSDsvZTrlKkgKFNDKSDinKg8L3RzcGFuPjx0c3BhbiB4PSIxNDIuNTUzNDk5OTk5OTk5OTkiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuqwgOq5jOyatCDtj7AgPSAyMFcg7ZWg64u5PC90c3Bhbj48dHNwYW4geD0iMTQyLjU1MzQ5OTk5OTk5OTk5IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rqLwg7Y+wID0gODBXIO2VoOuLuTwvdHNwYW4+PHRzcGFuIHg9IjE0Mi41NTM0OTk5OTk5OTk5OSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7LSdIDEwMFcg662J7YOx7J2066GcIOyPqCE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUEhPTkUiIGRhdGEtbGFiZWw9IlBIT05FIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQ4Mi42NjMiIHk9IjExNy44MDAwMDAwMDAwMDAwMSIgd2lkdGg9Ijg2LjQxIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1MjUuODY4IiB5PSIxMzYuMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlBIT05FPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJNQVRIIiBkYXRhLWxhYmVsPSJNQVRIIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjYxNy4wNzMiIHk9IjExNy44MDAwMDAwMDAwMDAwMSIgd2lkdGg9Ijc5Ljc0MTAwMDAwMDAwMDAxIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjY1Ni45NDM1IiB5PSIxMzYuMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk1BVEg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik1JTkUiIGRhdGEtbGFiZWw9IuuCtCDrjbDsnbTthLAoMjBXKeunjArsj5kg6rOo65287IScIO2ajeuTnSDwn5+iIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9Ijc0NC44MTQiIHk9IjEwOS4zNTAwMDAwMDAwMDAwMSIgd2lkdGg9IjE1MS42MTgiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iODIwLjYyMjk5OTk5OTk5OTkiIHk9IjEzNi4yNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iODIwLjYyMjk5OTk5OTk5OTkiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7rgrQg642w7J207YSwKDIwVynrp4w8L3RzcGFuPjx0c3BhbiB4PSI4MjAuNjIyOTk5OTk5OTk5OSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7I+ZIOqzqOudvOyEnCDtmo3rk50g8J+fojwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 기존 4G(OMA)와의 뼈대 대조 및 NOMA의 2대 기술 전격 해부 (3단 표)**

이 기술이 기존 기술(직교)과 근본적으로 어떻게 다른지(비직교)와 기지국/스마트폰이 쓰는 \*\*2개의 키워드(SC, SIC)\*\*를 대조해야 합니다.

| **핵심 척도 (비교 잣대)**                  | **🛑 기존 4G 방식 : OMA (직교)**                                                                                 | **🚀 5G/6G 방식 : NOMA (비직교) 🚨**                                                                                                                            |
| :--------------------------------- | :--------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **자원 분배의 본질 (Orthogonal vs Non)**  | **'자원을 절대 겹치지 않게 칼로 쪼갬'.** 시간이나 주파수 축을 직교하게(수직으로) 쪼개어, 각 사용자에게 독립된 방(채널)을 부여함. (간섭은 없지만 수용 인원에 뚜렷한 한계 존재). | **'동일 자원에 여러 명을 마구 겹쳐 넣음'.** 시간/주파수를 쪼개지 않고, 다수의 사용자가 완벽히 같은 자원을 동시에 공유함(비직교). 대신 **'전력(Power)'의 크기로 사용자를 구분함.**                                           |
| **✨ 핵심 기술 1 (송신단) 기지국은 어떻게 쏘는가?**  | (기존 OFDMA는 사용자별로 주파수 부반송파를 따로따로 나눠줌)                                                                       | **\[중첩 코딩 (Superposition Coding, SC)]** 기지국이 전송할 때 채널 상태가 안 좋은(멀리 있는) 단말에는 **높은 전력**을, 가까운 단말에는 **낮은 전력**을 할당하여, 이 신호들을 **수학적으로 덧셈(+)하여 중첩된 하나의 신호로 전송함.** |
| **✨ 핵심 기술 2 (수신단) 스마트폰은 어떻게 푸는가?** | (자기 주파수만 읽으면 끝남)                                                                                           | **\[순차적 간섭 제거 (SIC)] 💯** 중첩된 신호를 받은 수신자(폰)가, 나보다 강한 전력으로 들어온 타인의 신호를 먼저 해독하여 원래 신호에서 **뺄셈(-)으로 제거해 버림**. 이 과정을 반복하여 순수하게 자기 신호만 복원해 냄.                    |
| **네트워크 도입 효과**                     | 속도는 좋으나 초연결(Massive IoT) 지원 불가.                                                                            | 기존 대비 주파수 효율성(Spectral Efficiency)과 시스템 수용 용량이 **2\~3배 획기적으로 뻥튀기됨.**                                                                                       |

#### **IV. \[결론/제언] 6G 테라헤르츠(THz) 시대, 공간 다중화(MIMO)와의 결합(NOMA-MIMO)**

* **(키워드 위주 2줄 마무리)** "NOMA 단독으로는 단말기의 배터리 소모(SIC 연산 부하)가 심하다는 치명적 약점이 있습니다. 이를 극복하고 6G의 초공간/초연결 요구사항을 완벽히 달성하기 위해, 안테나를 수백 개 박아 넣어 전파의 공간을 찢어버리는 **'대용량 다중 입출력(Massive MIMO)' 기술과 NOMA를 융합한 'NOMA-MIMO' 아키텍처 연구가 전 세계적으로 집중되고 있습니다.**"
