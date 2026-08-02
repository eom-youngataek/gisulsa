### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (기존RAG의한계, GraphRAG의발상전환) — 3~4줄
Ⅱ. 구축과정 - 지식그래프인덱싱 (본론①, 도식 1개 필수)
Ⅲ. 커뮤니티요약과글로벌질의응답, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

앞서다룬 \*\*"Advanced RAG"\*\*는 \*\*"문서를청크로쪼개고,벡터유사도로검색"\*\*했는데, 이방식은 **"A와B와C가서로어떻게연결되는지"** 같은 **관계전체를아우르는질문**에는 취약합니다 — GraphRAG는 앞서다룬 \*\*"GraphDB(관계자체가1급데이터)"\*\*의 철학을 RAG에 적용해, **문서에서엔티티·관계를추출해지식그래프로엮은뒤** 검색합니다.

### Ⅱ. 구축과정 — 지식그래프인덱싱

| 단계            | 내용                                         |
| :------------ | :----------------------------------------- |
| **①엔티티·관계추출** | 문서에서 **인물,조직,사건같은개체**와 **그들간의관계**를 LLM으로추출 |
| **②지식그래프구축**  | 추출된것을 앞서다룬 \*\*"노드(개체)+엣지(관계)"\*\*구조로 저장   |
| **③커뮤니티탐지**   | 그래프안에서 \*\*밀접하게연결된하위집단(커뮤니티)\*\*을 자동으로찾아냄  |

→ 암기: **"문서에서인물·조직·관계를뽑아내서, 노드와엣지로엮고, 서로가까운그룹끼리묶는다"** — 앞서다룬 \*\*"K-means/DBSCAN(군집화)"\*\*와 유사하게, GraphRAG도 \*\*"관련된정보끼리자동으로그룹화"\*\*하지만, 그기준이 \*\*"벡터거리"\*\*가아니라 \*\*"그래프상의연결성"\*\*입니다.

### 도식화 제안

```
[GraphRAG 구축 과정]
[원본문서] → LLM으로 엔티티·관계추출
     ↓
[지식그래프] 
[회사A]──투자──[스타트업B]──창업자──[인물C]──이전직장──[회사D]
     ↓ 커뮤니티탐지(밀접히연결된그룹자동식별)
[커뮤니티1: 스타트업생태계] [커뮤니티2: 대기업네트워크]
```

### Ⅲ. 커뮤니티요약과 글로벌질의응답 — 핵심 배점

**함정 방지: "그래프로검색한다"고만답하면절반. 앞서다룬"Advanced RAG"가 못푸는 "전체를아우르는질문"을 GraphRAG가 어떻게해결하는지 구체적으로보여줘야완성됩니다.**

| 개념                | 내용                                                               |
| :---------------- | :--------------------------------------------------------------- |
| **커뮤니티요약**        | 각커뮤니티(그룹)마다 **LLM이미리요약본생성**— **"이그룹은전반적으로무엇에관한것인지"**             |
| **글로벌질의응답**(핵심장점) | \*\*"전체문서집합의핵심주제는무엇인가"\*\*같은 질문에, **개별청크검색으로는불가능**했던 **전체적조망제공** |
| **로컬vs글로벌**       | **로컬질의**(구체적사실)는 기존RAG처럼,**글로벌질의**(전체적패턴,주제)는 **커뮤니티요약**을 활용     |

→ 암기: **"각그룹마다미리요약해두면, '전체적으로뭐가중요한가'같은 큰질문에도답할수있다"** — 앞서다룬 \*\*"Advanced RAG"\*\*는 \*\*"특정사실하나를찾는것"\*\*엔 강하지만, \*\*"이문서전체가어떤이야기를하는지"\*\*같은 **거시적질문**엔 약했는데, GraphRAG의 **계층적커뮤니티요약**이 이문제를 해결합니다.

### 도식화 제안

```
[기존 RAG vs GraphRAG - 질문유형별비교]

질문: "김철수의이메일주소는?"
→ 기존RAG(청크검색)로 충분히해결(로컬질의)

질문: "이회사네트워크전체에서 가장영향력있는핵심인물은누구인가?"
→ 기존RAG: 청크하나하나로는 전체패턴을못봄(실패)
→ GraphRAG: 커뮤니티요약+그래프연결성분석으로 답변가능(글로벌질의)
```

**Microsoft의실제구현**(핵심): Microsoft Research가 2024년발표한 **GraphRAG**는, \*\*"계층적커뮤니티탐지(Leiden알고리즘등)"\*\*로 그래프를 **여러레벨의그룹으로나누고**, 각레벨마다 요약을생성해 \*\*"세부적질문부터전체적질문까지 계층적으로대응"\*\*합니다.

### Ⅳ. 결론

GraphRAG는 **"앞서다룬Advanced/ModularRAG가벡터유사도로문서청크를검색했던것과달리, 문서에서엔티티·관계를추출해지식그래프로엮고, 커뮤니티요약을통해 '전체를아우르는질문'까지답할수있게하는"** 차세대RAG기법입니다 — 핵심가치는 \*\*"로컬질의(구체적사실)는기존방식,글로벌질의(전체적패턴·주제)는계층적커뮤니티요약"\*\*으로 **두종류의질문모두에대응**한다는 점이며, 이는 앞서다룬 \*\*GNN(관계자체를1급데이터로다룸)\*\*의 철학이 **RAG검색기법**에 실제로 적용된 구체적사례입니다 — 오늘하루다룬 **GNN(그래프신경망)→AdvancedRAG→ModularRAG→GraphRAG**로 이어지는 흐름은, \*\*"검색기술도결국,데이터의구조(그래프)에맞춰 계속진화해간다"\*\*는 것을 보여주며 완결됩니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "조각난 문서 조각만 띡 던져주던 기존 RAG(검색 증강 생성)의 시야 한계를 깨부순 마이크로소프트(MS) 주도의 차세대 RAG 아키텍처다. 기존 벡터(Vector) RAG는 텍스트를 단순 조각(Chunk)으로 쪼개 유사도 검색만 하므로 "이 보고서 전체의 핵심 흐름과 인물 관계도를 요약해 줘" 같은 **전역적(Global)인 통합 추론 질문에 헛소리(환각)를 하거나 무너졌다.** GraphRAG는 다르다. 문서에서 엔티티(인물, 개념)와 관계(연결선)를 추출하여 거미줄 같은 \*\*'지식 그래프(Knowledge Graph)'\*\*를 먼저 설계한다. 그리고 **Leiden 알고리즘**을 돌려 친한 노드끼리 묶은 커뮤니티별 요약서(Summary)를 미리 작성해 둔다. 질문이 들어오면 지식의 족보와 요약본을 동시에 LLM에 공급하여, 복잡한 인과관계 추적과 전체 맥락 요약을 신들린 듯 수행해 낸다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 파편화된 검색의 극복과 전역적 추론, GraphRAG 개요**

* **정의:** 입력 문서 데이터에서 개체(Entity)와 이들의 위상학적 관계(Relationship)를 모델링하여 지식 그래프를 구성한 후, 군집(Community) 단위 요약 정보와 LLM을 결합하여 복잡한 질문에 대응하는 RAG 솔루션 (MS 오픈소스화).
* **목적:** 기존 Vector DB 기반 검색이 직면한 '전체 맥락 요약 불가(Global Query 취약)' 및 '맥락 연결성 결여'라는 페널티를 기술적으로 해결하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 텍스트에서 관계망을 뽑아 미리 요약하는 프로세스**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNjEzLjIzIDM2MC44MTg5OTk5OTk5OTk5NiIgd2lkdGg9IjE2MTMuMjMiIGhlaWdodD0iMzYwLjgxODk5OTk5OTk5OTk2IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJHcmFwaFJBR19fX18iIGRhdGEtbGFiZWw9IkdyYXBoUkFH7J2YIO2VteyLrCDrjbDsnbTthLAg7LKY66asIO2MjOydtO2UhOudvOyduCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMTUzMy4yMyIgaGVpZ2h0PSIyODAuODE4OTk5OTk5OTk5OTYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIxNTMzLjIzIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+R3JhcGhSQUfsnZgg7ZW17IusIOuNsOydtO2EsCDsspjrpqwg7YyM7J207ZSE65287J24PC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJET0MiIGRhdGEtdG89IklORCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyMDYuMTM2LDE5MC4xODQ0OTk5OTk5OTk5OSAyNTQuMTM2LDE5MC4xODQ0OTk5OTk5OTk5OSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iSU5EIiBkYXRhLXRvPSJHUkFQSCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0NDIuODA0LDE5NC40MDk0OTk5OTk5OTk5OCA0OTAuODA0LDE5NC40MDk0OTk5OTk5OTk5OCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iR1JBUEgiIGRhdGEtdG89IkNPTSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI2ODcuNjIyOTk5OTk5OTk5OSwxOTQuNDA5NDk5OTk5OTk5OTggNzM1LjYyMjk5OTk5OTk5OTksMTk0LjQwOTQ5OTk5OTk5OTk4IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDT00iIGRhdGEtdG89IlNVTSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI5NTYuNDQxOTk5OTk5OTk5OSwxOTQuNDA5NDk5OTk5OTk5OTggMTAwNC40NDE5OTk5OTk5OTk5LDE5NC40MDk0OTk5OTk5OTk5OCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iU1VNIiBkYXRhLXRvPSJPVVQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTI1MC45MDgsMTk4LjYzNDQ5OTk5OTk5OTk3IDEyOTguOTA4LDE5OC42MzQ0OTk5OTk5OTk5NyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRE9DIiBkYXRhLWxhYmVsPSLrsKnrjIDtlZwg7IKs64K0IOusuOyEnCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iMTcxLjczNDUiIHdpZHRoPSIxNTAuMTM2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTMxLjA2Nzk5OTk5OTk5OTk4IiB5PSIxOTAuMTg0NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+67Cp64yA7ZWcIOyCrOuCtCDrrLjshJw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IklORCIgZGF0YS1sYWJlbD0i4pyoIDEuIOyduOuNseyLsSAoSW5kZXhpbmcpIOKcqApMTE3snLzroZwg6rCc7LK0KE5vZGUp7JmACuq0gOqzhChFZGdlKSDsi7kg64ukIOy2lOy2nCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyNTQuMTM2IiB5PSIxNTkuMDU5NDk5OTk5OTk5OTkiIHdpZHRoPSIxODguNjY4IiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzQ4LjQ3IiB5PSIxOTQuNDA5NDk5OTk5OTk5OTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjM0OC40NyIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPuKcqCAxLiDsnbjrjbHsi7EgKEluZGV4aW5nKSDinKg8L3RzcGFuPjx0c3BhbiB4PSIzNDguNDciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPkxMTeycvOuhnCDqsJzssrQoTm9kZSnsmYA8L3RzcGFuPjx0c3BhbiB4PSIzNDguNDciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuq0gOqzhChFZGdlKSDsi7kg64ukIOy2lOy2nDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJHUkFQSCIgZGF0YS1sYWJlbD0i4pyoIDIuIOyngOyLnSDqt7jrnpjtlIQg6rWs7LaVIOKcqArqt7jrrLzrp50g6rWs7KGw66GcIOuzgO2ZmCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0OTAuODA0IiB5PSIxNjcuNTA5NSIgd2lkdGg9IjE5Ni44MTkiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1ODkuMjEzNSIgeT0iMTk0LjQwOTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjU4OS4yMTM1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+4pyoIDIuIOyngOyLnSDqt7jrnpjtlIQg6rWs7LaVIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjU4OS4yMTM1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7qt7jrrLzrp50g6rWs7KGw66GcIOuzgO2ZmDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDT00iIGRhdGEtbGFiZWw9IuKcqCAzLiDsu6TrrqTri4jti7Ag6rCQ7KeAIPCfmqgg4pyoCkxlaWRlbiDslYzqs6Drpqzsppgg7KCB7JqpCuyjvOygnOuzhC/qtbDsp5Hrs4Qg6re466O57ZWRIiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9Ijg0Ni4wMzI0OTk5OTk5OTk5LDgzLjk5OTk5OTk5OTk5OTk5IDk1Ni40NDE5OTk5OTk5OTk5LDE5NC40MDk0OTk5OTk5OTk5OCA4NDYuMDMyNDk5OTk5OTk5OSwzMDQuODE4OTk5OTk5OTk5OTYgNzM1LjYyMjk5OTk5OTk5OTksMTk0LjQwOTQ5OTk5OTk5OTk4IiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9Ijg0Ni4wMzI0OTk5OTk5OTk5IiB5PSIxOTQuNDA5NDk5OTk5OTk5OTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9Ijg0Ni4wMzI0OTk5OTk5OTk5IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+4pyoIDMuIOy7pOuupOuLiO2LsCDqsJDsp4Ag8J+aqCDinKg8L3RzcGFuPjx0c3BhbiB4PSI4NDYuMDMyNDk5OTk5OTk5OSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+TGVpZGVuIOyVjOqzoOumrOymmCDsoIHsmqk8L3RzcGFuPjx0c3BhbiB4PSI4NDYuMDMyNDk5OTk5OTk5OSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7KO87KCc67OEL+q1sOynkeuzhCDqt7jro7ntlZE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU1VNIiBkYXRhLWxhYmVsPSLinKggNC4g7ISg7KCc7KCBIOyalOyVvSAoU3VtbWFyeSkg8J+SryDinKgK6rCBIOy7pOuupOuLiO2LsOuzhCDsmpTslb3rs7gg7IKs7KCEIOyDneyEsSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMDA0LjQ0MTk5OTk5OTk5OTkiIHk9IjE2Ny41MDk1IiB3aWR0aD0iMjQ2LjQ2NTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjExMjcuNjc1IiB5PSIxOTQuNDA5NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTEyNy42NzUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7inKggNC4g7ISg7KCc7KCBIOyalOyVvSAoU3VtbWFyeSkg8J+SryDinKg8L3RzcGFuPjx0c3BhbiB4PSIxMTI3LjY3NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+6rCBIOy7pOuupOuLiO2LsOuzhCDsmpTslb3rs7gg7IKs7KCEIOyDneyEsTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJPVVQiIGRhdGEtbGFiZWw9Iuq4gOuhnOuyjCDsp4jrrLgg7J6F66ClIOyLnArsu6TrrqTri4jti7Ag7JqU7JW97IScIOyhsO2Vqe2VmOyXrCDri7Xrs4Ag8J+agCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMjk4LjkwOCIgeT0iMTcxLjczNDUiIHdpZHRoPSIyNTguMzIyIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTQyOC4wNjkiIHk9IjE5OC42MzQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNDI4LjA2OSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuq4gOuhnOuyjCDsp4jrrLgg7J6F66ClIOyLnDwvdHNwYW4+PHRzcGFuIHg9IjE0MjguMDY5IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7su6TrrqTri4jti7Ag7JqU7JW97IScIOyhsO2Vqe2VmOyXrCDri7Xrs4Ag8J+agDwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 기존 Vector RAG vs 차세대 GraphRAG 전격 대조 (3단 표)**

이 토픽은 '유사도 기반 벡터 검색'과 '지식 그래프 기반 추론'의 아키텍처적 차이를 쓰고, GraphRAG의 핵심 심장인 **'Leiden 알고리즘을 통한 커뮤니티 요약'** 단계를 정확히 설명하는 것이 핵심 고득점 득점 포인트입니다.

| **핵심 척도**         | **📊 Vector RAG (유사도 검색)**                                                    | **🔑 GraphRAG (지식 그래프) 🚨**                                                            | **🏁 GraphRAG 핵심 단계 (Leiden) 💯**                                                                                                             |
| :---------------- | :---------------------------------------------------------------------------- | :------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| **개념 / 차별성**      | **'점 검색 (Point Lookups)'.** 사용자 질문 벡터와 코사인 유사도가 가장 높은 문서 조각(Top-K)만 콕 집어 가져옴. | **'그물 검색 (Graph-based Context)'.** 엔티티 관계망을 타고 내려가며, 서로 연관성 있는 맥락 데이터들을 다차원 취합함.       | **'Leiden 알고리즘과 계층적 군집화'.** 복잡한 지식 그래프를 의미적 동질성에 따라 중소형 그룹(Community)으로 묶어냄.                                                                  |
| **핵심 기술 및 한계 🚨** | **\[글로벌 쿼리의 무덤]** "이 기업의 재무 리스크 요인 3가지를 요약해 줘" 같은 문서 전체를 훑어야 하는 질문에 오작동.      | **\[Global & Local Query 모두 완벽 💯]** 로컬 질문(특정 객체 정보)과 글로벌 질문(전체 주제 요약)을 최적의 경로로 동시 제공. | **1. \[Community Detection 💯]** Leiden 알고리즘으로 대규모 그래프를 계층 구조로 클러스터링. **2. \[Pre-Summarization 🚨]** 각 군집 요약본을 미리 생성해 두어, 질문 시 실시간 쿼리 연산량 급감. |
| **비용 / 한계점**      | 벡터 임베딩 및 DB 검색 비용이 저렴하고 아키텍처가 단순함.                                            | 지식 그래프를 구성하는 인덱싱 단계에서 **수많은 LLM 호출이 일어나 토큰 비용이 초기에 매우 비싸게 듦.**                         | Neo4j 등 지식 그래프 전문 저장소와의 아키텍처 연동 및 메타데이터 정제가 필요함.                                                                                              |

#### **IV. \[결론/제언] 하이브리드 RAG (Vector + Graph) 설계로의 수렴**

* **(키워드 위주 2줄 마무리)** "GraphRAG는 전역 추론에 강하지만 인덱싱 비용이 무겁다는 Trade-off가 뚜렷합니다. 실무에서는 단순 팩트 검색은 저렴한 \*\*'Vector RAG'\*\*를 태우고, 복잡한 인과관계나 통합 보고서 생성은 **'GraphRAG'** 모듈로 분기하는 **'하이브리드 RAG 라우팅' 아키텍처를 도입하여 비용 효율성을 완성해야 합니다.**"
