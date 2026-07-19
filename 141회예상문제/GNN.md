### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (CNN의한계, 왜그래프전용신경망이필요한가) — 3~4줄
Ⅱ. 핵심메커니즘 - 메시지패싱 (본론①, 도식 1개 필수)
Ⅲ. 다층집계와과평활화문제, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

앞서다룬 **CNN**은 **"격자모양(이미지)에서, 정해진크기의필터로 이웃을훑는"** 방식이었는데, 앞서다룬 \*\*"Graph DB"\*\*의 소셜네트워크나 분자구조같은데이터는 **"각노드마다이웃의수가다르고, 정해진순서도없는"** 불규칙한구조입니다 — CNN의필터를 그대로쓸수없어, GNN은 **"각노드가자신의이웃들로부터 정보를모아 자신을업데이트하는"** 새로운방식을씁니다.

### Ⅱ. 핵심메커니즘 — 메시지패싱

| 단계                 | 내용                                                 |
| :----------------- | :------------------------------------------------- |
| **메시지생성**(Message) | 각노드가 \*\*자신의현재상태(특징벡터)\*\*를 **이웃들에게전달할메시지**로 변환    |
| **집계**(Aggregate)  | 각노드가 **모든이웃으로부터받은메시지를 모음**(합,평균,최대값등— **순서에상관없이**) |
| **업데이트**(Update)   | 집계된정보와 **자신의기존상태**를합쳐 **새로운상태**로갱신                 |

→ 암기: **"이웃에게내정보를보내고,이웃들정보를모으고,그걸로내상태를갱신한다"** — 앞서다룬 \*\*"메시지패싱"\*\*이라는 이름자체가, 앞서다룬 \*\*"AODV(Ad-hoc라우팅의RREQ/RREP)"\*\*처럼 **"노드끼리메시지를주고받는"** 네트워크개념과 유사합니다.

### 도식화 제안

```
[GNN - 메시지패싱 1회전]
    [노드B]        [노드C]
       ↘           ↙
        [노드A] ← 메시지집계(B,C,D로부터)
       ↗
    [노드D]

노드A의새상태 = Update(노드A의기존상태, Aggregate(B,C,D의메시지))

(CNN의필터처럼 "정해진위치"가아니라, 
 "실제로연결된이웃"으로부터만 정보를모음)
```

### Ⅲ. 다층집계와 과평활화문제 — 핵심 배점

**함정 방지: "이웃정보를모은다"고만답하면절반. 층을쌓을수록"더넓은이웃"을보게되는원리와, 그것이왜문제가되는지(과평활화)보여줘야완성됩니다.**

| 개념                            | 내용                                                                                                          |
| :---------------------------- | :---------------------------------------------------------------------------------------------------------- |
| **층별수용범위확장**                  | **1층**은 \*\*직접이웃(1-hop)\*\*만, **2층**은 \*\*이웃의이웃(2-hop)\*\*까지, **층이깊어질수록** 더넓은범위의노드정보를 반영                    |
| **과평활화**(Over-smoothing,핵심문제) | 층을 **너무깊게쌓으면**, 모든노드가 **결국비슷비슷한값으로수렴**— 앞서다룬 \*\*"CNN의계층적특징(단순→복잡)"\*\*과달리, GNN은 **"너무깊으면오히려구별력을잃는"** 역설적문제 |
| **원인**                        | 그래프전체가 **연결되어있으면**, 층을반복할수록 **결국모든노드가 전체그래프의평균같은값**에 가까워짐                                                   |

→ 암기: **"층이깊어질수록 더넓은이웃을보는데,너무깊으면 결국모든노드가서로닮아가서 구별이안된다"** — 이는 앞서다룬 **CNN**에서는 \*\*"깊을수록더복잡하고정교한개념"\*\*을 학습했던것과 **정반대의현상**입니다: CNN은 격자구조라 \*\*"국소성이유지"\*\*되지만, GNN은 **그래프연결성때문에 정보가전체로퍼져 흐려지는것**입니다.

### 도식화 제안

```
[과평활화 문제]
[1층: 직접이웃만반영]        [3층: 이웃의이웃의이웃까지반영]
노드A: 고유한특징 유지         노드A: 그래프전체의 "평균"에가까워짐
노드B: 고유한특징 유지         노드B: 노드A와 거의비슷해짐
                            노드C: 노드A,B와 거의비슷해짐
                            
→ 층을너무깊게쌓으면(예:10층이상), 
  모든노드가 "구별불가능"해지는 과평활화발생
  (대응: GNN은 보통 2~4층 정도로 얕게설계)
```

**활용사례**: 앞서다룬 \*\*"Graph DB(Neo4j)"\*\*의 소셜네트워크추천,**분자구조예측**(신약개발),**교통네트워크예측**,**사기탐지**(계좌간송금관계분석)

### Ⅳ. 결론

GNN은 \*\*"CNN이이미지의격자구조에맞췄던것처럼, 그래프(Graph DB)의불규칙한관계구조에맞춰 메시지패싱(메시지생성→집계→업데이트)으로 이웃정보를반영"\*\*하는 신경망입니다 — 다만 CNN과달리, \*\*"층을너무깊게쌓으면 오히려모든노드가비슷해지는 과평활화문제"\*\*가 있어, **의도적으로얕은구조**로설계해야합니다 — 이는 앞서다룬 \*\*Graph DB(관계자체가1급데이터)\*\*의 개념을 신경망차원에서 실현한것이며, 오늘하루의신경망시리즈(피드포워드NN→CNN→GNN)가 \*\*"데이터의구조(격자냐,그래프냐)에맞춰 신경망의연산방식자체를설계해야한다"\*\*는 공통원리로 완결됩니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "이미지는 CNN이, 텍스트는 RNN이 정복했다. 하지만 세상의 진짜 핵심 데이터인 소셜 네트워크, 자금 세탁 흐름, 신약 개발 분자 구조는 격자무늬가 아니라 점(Node)과 선(Edge)으로 얽힌 비정형 '그래프(Graph) 데이터'다. 이를 직접 학습하기 위해 탄생한 신경망이 바로 GNN이다. 핵심 원리는 \*\*'메시지 패싱(Message Passing)'\*\*이다. '친구를 보면 그 사람을 안다'는 철학을 바탕으로, 나와 선으로 연결된 이웃들의 정보(특징)를 끌어모아(Aggregate) 나의 기존 상태에 더하여 나를 새롭게 업데이트(Update)하는 과정을 무한 반복한다. 모든 이웃의 정보를 똑같이 평균 내서 합치는 \*\*'GCN'\*\*이 기본 뼈대이며, 이웃 중에서도 나에게 더 큰 영향을 미치는 찐친에게 가중치(Attention)를 팍팍 주는 **'GAT'** 모델이 최신 트렌드다. 현재 AI 신약 개발과 핀테크 사기 탐지(FDS)의 심장 역할을 하고 있다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 비-유클리디안 공간 데이터의 정복자, GNN 개요**

* **정의:** 노드(Node, 객체)와 엣지(Edge, 관계)로 이루어진 그래프(Graph) 구조의 데이터를 입력받아, 객체 간의 위상학적 '연결 관계'와 '구조 정보'를 신경망을 통해 학습하는 차세대 딥러닝 아키텍처.
* **목적:** 기존 CNN과 RNN은 데이터가 격자(이미지 픽셀)나 선형(시계열)으로 고정된 유클리디안 공간에서만 동작하는 한계가 있음. 방향도, 크기도 제각각인 SNS 인맥망 같은 비-유클리디안(Non-Euclidean) 데이터를 파싱하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 친구를 보면 그 사람을 아는 메시지 패싱 루프**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NDAuMTUgMzgwLjUiIHdpZHRoPSI0NDAuMTUiIGhlaWdodD0iMzgwLjUiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IkdOTl9fX19fTWVzc2FnZV9QYXNzaW5nIiBkYXRhLWxhYmVsPSJHTk4g7ZW17IusIOybkOumrDog66mU7Iuc7KeAIO2MqOyLsSAoTWVzc2FnZSBQYXNzaW5nKSI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMzYwLjE1IiBoZWlnaHQ9IjMwMC41IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMzYwLjE1IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+R05OIO2VteyLrCDsm5Drpqw6IOuplOyLnOyngCDtjKjsi7EgKE1lc3NhZ2UgUGFzc2luZyk8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkFHRyIgZGF0YS10bz0iVVAiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjg5LjA3NSwyMzkuNjAwMDAwMDAwMDAwMDIgMjg5LjA3NSwyODcuNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTjIiIGRhdGEtdG89IkFHRyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzMzMuMDc1LDEyMC45IDMzMy4wNzUsMTQ0LjkgMjg5LjA3NSwxNDQuOSAyODkuMDc1LDE2OC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJOMyIgZGF0YS10bz0iQUdHIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjI0NS4wNzUsMTIwLjkgMjQ1LjA3NSwxNDQuOSAyODkuMDc1LDE0NC45IDI4OS4wNzUsMTY4LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik4xIiBkYXRhLWxhYmVsPSLrgpjsnZgg64W465OcIiBkYXRhLXNoYXBlPSJjaXJjbGUiPgogIDxjaXJjbGUgY3g9IjExNSIgY3k9IjE0MyIgcj0iNTkiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTE1IiB5PSIxNDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuuCmOydmCDrhbjrk5w8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkFHRyIgZGF0YS1sYWJlbD0i4pyoIDEuIOyImOynkSAoQWdncmVnYXRlKSDinKgK64KY7JmAIOyXsOqysOuQnCDsnbTsm4MgQSwgQuydmArtirnsp5Uo7KCV67O0KeydhCDrgYzslrTrqqjsnYwhIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjE5NCIgeT0iMTY4LjkiIHdpZHRoPSIxOTAuMTQ5OTk5OTk5OTk5OTgiIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyODkuMDc1IiB5PSIyMDQuMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjI4OS4wNzUiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj7inKggMS4g7IiY7KeRIChBZ2dyZWdhdGUpIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjI4OS4wNzUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuuCmOyZgCDsl7DqsrDrkJwg7J207JuDIEEsIELsnZg8L3RzcGFuPjx0c3BhbiB4PSIyODkuMDc1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7tirnsp5Uo7KCV67O0KeydhCDrgYzslrTrqqjsnYwhPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlVQIiBkYXRhLWxhYmVsPSJVUCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyNTkuMDc1IiB5PSIyODcuNiIgd2lkdGg9IjYwIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjI4OS4wNzUiIHk9IjMwNi4wNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+VVA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik4yIiBkYXRhLWxhYmVsPSJOMiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzMDMuMDc1IiB5PSI4NCIgd2lkdGg9IjYwIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzMzMuMDc1IiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk4yPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJOMyIgZGF0YS1sYWJlbD0iTjMiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjE1LjA3NSIgeT0iODQiIHdpZHRoPSI2MCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjQ1LjA3NSIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5OMzwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 그래프 학습 원리 및 2대 파생 모델 전격 해부 (3단 표)**

이 토픽은 그래프를 학습하는 '메시지 패싱'의 핵심과, 정보를 끌어올 때 차이를 두는 GCN과 GAT의 차이점을 대조하는 것이 완벽한 득점 포인트입니다.

| **핵심 척도**               | **🕸️ 그래프(Graph) 구조 특성**                                                                         | **🧬 메커니즘 (메시지 패싱) 🚨**                                                                          | **🚀 GCN vs GAT (파생 모델) 💯**                                                                                                                             |
| :---------------------- | :----------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **개념 / 차별성**            | **'연결성 자체가 지식이다'.** 단순한 속성 정보뿐만 아니라, "누구와 연결되어 있는가(Edge)"라는 구조적 정보를 수학적 행렬(인접 행렬)로 변환하여 딥러닝에 태움. | **'이웃의 정보를 흡수하라 💯'.** 노드 자신의 특징 벡터(Feature Vector)를 주변 이웃 노드들과 주고받으며 상태를 점진적으로 갱신하는 GNN의 절대 원칙. | **'이웃을 대하는 태도의 진화'.** 이웃의 정보를 수집(Aggregate)할 때, 어떤 수학적 연산을 쓰느냐에 따라 파생 모델이 나뉨.                                                                            |
| **동작 메커니즘 (출제 포인트) 🚨** | 인접 행렬(Adjacency Matrix)을 통해 이웃과의 연결 상태를 0과 1로 맵핑함.                                               | 메시지 패싱을 **1번 하면 1촌의 정보**를 알고, **2번(2-Layer) 하면 2촌의 정보**까지 나에게 전달됨 (넓은 시야 확보).                    | **\[GCN (합성곱) 💯]** CNN 돋보기 원리를 차용해, 연결된 **모든 이웃의 정보를 공평하게 평균** 내서 가져옴. **\[GAT (어텐션) 💯]** 트랜스포머의 어텐션 기법을 차용해, **나에게 영향력이 큰 이웃에게만 높은 가중치**를 줘서 정보를 흡수함. |
| **비즈니스 활용**             | \[핀테크 사기 탐지(FDS)] 정상인 계좌와 범죄자 대포통장의 비정상적 송금 거미줄 패턴을 잡아냄.                                         | \[추천 시스템] 넷플릭스 등에서 나와 비슷한 영화를 본 다른 유저(이웃)의 행동망을 분석해 추천함.                                         | **\[신약 개발 (AI 바이오) 💯]** 분자 구조 역시 원자(노드)와 결합(엣지)의 그래프 형태이므로, 약물 후보 물질의 독성/단백질 결합 구조를 모델링함.                                                               |

#### **IV. \[결론/제언] 과도한 층 쌓기로 인한 Oversmoothing의 한계 극복**

* **(키워드 위주 2줄 마무리)** "GNN은 정보를 멀리서 끌어오기 위해 층(Layer)을 너무 깊게 쌓으면, 모든 노드가 다 섞여버려서 특징이 비슷해져 버리는 **'Oversmoothing(과잉 평활화)' 문제**가 발생합니다. 따라서 실무에서는 깊이를 2\~3층으로 제한하거나, ResNet처럼 잔차 연결(Residual Connection)을 추가하여 기존 자기 정보의 소실을 막는 아키텍처 설계가 필수적입니다."
