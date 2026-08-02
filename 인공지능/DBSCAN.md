### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (K-means의한계, DBSCAN의발상전환) — 3~4줄
Ⅱ. 핵심개념 - 3가지점의분류 (본론①, 도식 1개 필수)
Ⅲ. 알고리즘동작및장단점, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

앞서다룬 **K-means**는 \*\*"K를미리정해야하고, 클러스터가원형이라가정"\*\*하는 한계가있었습니다 — DBSCAN(Density-BasedSpatialClusteringofApplicationswithNoise)은 **"중심점을찾는게아니라, 데이터가촘촘하게몰려있는영역(밀도)을따라 자연스럽게경계를그리는"** 완전히다른접근입니다.

### Ⅱ. 핵심개념 — 3가지점의분류

| 개념                   | 내용                               |
| :------------------- | :------------------------------- |
| **eps(반경)**          | 한점을중심으로 **"이웃"으로인정할거리범위**        |
| **MinPts**           | 그반경안에 **최소몇개의점이있어야"밀집"으로인정할지**   |
| **핵심점**(CorePoint)   | 반경eps안에 **MinPts개이상의점**이있는점      |
| **경계점**(BorderPoint) | 자신은밀집기준을못채우지만, **핵심점의반경안에는속하는**점 |
| **잡음점**(NoisePoint)  | 어느핵심점의반경에도 **속하지않는점**(이상치)       |

→ 암기: **"주변에친구가많으면핵심점,핵심점옆에붙어있으면경계점,아무데도안속하면잡음"** — 앞서다룬 \*\*"K-means"\*\*가 \*\*"모든점을반드시어느그룹에든소속"\*\*시켰던것과달리, DBSCAN은 \*\*"소속될수없는점(잡음)"\*\*을 **처음부터인정**합니다.

### 도식화 제안

```
[DBSCAN - 점의 3분류]
        ●─●     (핵심점: 반경안에 MinPts=3개이상)
       /│ │\
      ● │ │ ●   (경계점: 핵심점반경안에는있지만, 자기반경은부족)
        ●─●
              
    ·  (잡음점: 아무핵심점의반경에도안속함,고립된점)
```

### Ⅲ. 알고리즘동작 및 장단점 — 핵심 배점

**함정 방지: "밀도로나눈다"고만답하면절반. K-means와정반대의장단점을 구체적으로대비해서보여줘야완성됩니다.**

**알고리즘동작**: 임의의핵심점에서시작해, \*\*"이웃의이웃의이웃..."\*\*으로 **연결된모든점을하나의클러스터로확장**— 더이상연결된핵심점이없으면 그클러스터를 완성하고, 다른미방문점에서 새클러스터탐색을 반복합니다.

```
[클러스터확장과정]
핵심점A 발견 → A의이웃(핵심점B) 확인 → B도핵심점이므로 클러스터에편입
     ↓
B의이웃(핵심점C) 확인 → C도편입 ... (연쇄적으로계속확장)
     ↓
더이상연결된핵심점없음 → 클러스터1완성
     ↓
아직방문안한점에서 → 클러스터2 새로시작(또는잡음점으로분류)
```

**K-means vs DBSCAN 비교**

| 구분             | **K-means**                | **DBSCAN**                                |
| :------------- | :------------------------- | :---------------------------------------- |
| **K값(클러스터개수)** | **미리지정해야함**                | **자동으로결정됨**(밀도에따라)                        |
| **클러스터모양**     | **원형만가능**(중심점기반)           | **불규칙한모양도가능**(연결기반)                       |
| **이상치처리**      | **모든점을강제로소속**(이상치도어느그룹에속함) | **잡음점으로명시적분류**(이상치탐지에강함)                  |
| **파라미터민감도**    | K값,초기중심점위치                 | **eps,MinPts설정에민감**(잘못설정시전부하나로묶이거나전부잡음처리) |

→ 암기: **"K-means는몇개로나눌지사람이정하고 원형만가능,DBSCAN은밀도로알아서정하고 어떤모양도가능하지만,대신반경·최소점수설정이까다롭다"** — 앞서다룬 \*\*"R-Tree(MBR로영역을감싸는)"\*\*와 달리, DBSCAN은 \*\*"점들간의연결성"\*\*만으로 영역을 규정한다는 점에서, **더유연하지만더불안정할수있는** 트레이드오프를 보여줍니다.

### 도식화 제안

```
[K-means가 실패하는 경우 - 불규칙모양]
   ●●●●●        ●●●●●
  ●     ●      ●     ●     ← 초승달모양 두군집
   ●●●●●        ●●●●●

K-means: 원형가정으로 잘못나눔(가운데를기준으로 반반씩섞어버림)
DBSCAN: 밀도연결을따라가 초승달모양 그대로 정확히구분
```

### Ⅳ. 결론

DBSCAN은 **"K값을미리정하지않고, 데이터의밀도가연결된영역을따라 자연스럽게클러스터경계를그리며, 어디에도속하지못하는점은잡음으로인정하는"** 방식으로, 앞서다룬 \*\*K-means의두가지근본적한계(K값사전지정,원형가정)\*\*를 동시에해결합니다 — 다만 \*\*"eps와MinPts설정에민감하다"\*\*는 새로운파라미터튜닝의어려움이 대가로남습니다 — 이는 \*\*"이상치탐지,불규칙한형태의데이터군집화"\*\*에 K-means보다 훨씬적합하며, 두알고리즘은 \*\*"데이터의모양과목적에따라선택하는 상호보완적도구"\*\*입니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "K-means 알고리즘이 절대 해결하지 못하는 '초승달 모양 묶기'와 '이상치(노이즈) 제거'를 완벽하게 해결해 내는 밀도(Density) 기반의 천재적인 비지도 군집화 알고리즘이다. 인간이 K값을 미리 정해줄 필요가 없다. 이 알고리즘은 오직 두 가지 파라미터, \*\*'탐색 반경(Eps)'\*\*과 그 반경 안에 있어야 할 \*\*'최소 인원수(MinPts)'\*\*만 가지고 스스로 군집을 늘려나간다. 핵심 원리는 모든 데이터를 3가지 계급으로 나누는 것이다. 반경 안에 인원이 꽉 찬 인싸 **'코어(Core)'**, 코어에 걸쳐있는 **'경계(Border)'**, 아무 데도 못 낀 아싸 \*\*'노이즈(Noise)'\*\*다. 노이즈를 알아서 버려주기 때문에 이상치에 극도로 강하며, 촘촘하게 엮여(밀도)만 있으면 도넛 모양이든 불규칙한 모양이든 기가 막히게 다 묶어버리는 것이 최고의 무기다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 복잡한 군집과 노이즈를 제압하는 밀도 기반 모델, DBSCAN 개요**

* **정의:** 반경(Epsilon)과 최소 데이터 수(MinPts)를 기준으로, 데이터가 촘촘하게 몰려 있는 밀도(Density)를 계산하여 군집을 스스로 확장해 나가는 밀도 기반 공간 클러스터링 알고리즘.
* **목적:** K-means가 구형(원형) 군집만 찾고 이상치에 박살 나는 한계를 극복하여, 불규칙하고 기하학적인 모양의 군집을 찾아내고 쓰레기 데이터(Outlier)를 자동으로 걸러내기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 인싸(코어)를 중심으로 퍼져나가는 전염병**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NjMuMjM2IDMzMi41IiB3aWR0aD0iNDYzLjIzNiIgaGVpZ2h0PSIzMzIuNSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iREJTQ0FOX0Vwc19NaW5QdHMzXyIgZGF0YS1sYWJlbD0iREJTQ0FOOiDrsJjqsr0oRXBzKeqzvCDstZzshozsnbjsm5AoTWluUHRzPTMp7J2YIOuniOuylSI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMzgzLjIzNiIgaGVpZ2h0PSIyNTIuNSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjM4My4yMzYiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5EQlNDQU46IOuwmOqyvShFcHMp6rO8IOy1nOyGjOyduOybkChNaW5QdHM9MynsnZgg66eI67KVPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDIiBkYXRhLXRvPSJCIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjIyMS42OTcsMjI1LjYgMjQ1LjY5NywyMjUuNiAyNDUuNjk3LDE5My4xNDk5OTk5OTk5OTk5OCAyNjkuNjk3LDE5My4xNDk5OTk5OTk5OTk5OCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQyIgZGF0YS10bz0iQzIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjIxLjY5NywyMjUuNiAyNDUuNjk3LDIyNS42IDI0NS42OTcsMjU4LjA1IDI2OS42OTcsMjU4LjA1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDIiBkYXRhLWxhYmVsPSLinKgg7L2U7Ja0IOygkCAoQ29yZSkg4pyoCuuCtCDrsJjqsr0g7JWI7JeQCjPrqoUg7J207IOBIOyeiOuEpCEg7J247Iu4ISIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iMTkwLjI1IiB3aWR0aD0iMTY1LjY5NyIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTM4Ljg0ODUiIHk9IjIyNS42IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxMzguODQ4NSIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPuKcqCDsvZTslrQg7KCQIChDb3JlKSDinKg8L3RzcGFuPjx0c3BhbiB4PSIxMzguODQ4NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+64K0IOuwmOqyvSDslYjsl5A8L3RzcGFuPjx0c3BhbiB4PSIxMzguODQ4NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+M+uqhSDsnbTsg4Eg7J6I64SkISDsnbjsi7ghPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkIiIGRhdGEtbGFiZWw9IkIiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjY5LjY5NyIgeT0iMTc0LjciIHdpZHRoPSI2MCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjk5LjY5NyIgeT0iMTkzLjE0OTk5OTk5OTk5OTk4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5CPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDMiIgZGF0YS1sYWJlbD0i65iQIOuLpOuluCDsvZTslrQg7KCQIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjI2OS42OTciIHk9IjIzOS42MDAwMDAwMDAwMDAwMiIgd2lkdGg9IjEzNy41MzkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjMzOC40NjY1IiB5PSIyNTguMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuuYkCDri6Trpbgg7L2U7Ja0IOygkDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTiIgZGF0YS1sYWJlbD0i4pyoIOuFuOydtOymiCAoTm9pc2UpIPCfkqUK7KO867OA7JeQIOyVhOustOuPhCDsl4bripQg7JWE7Iu4LgotJmd0OyDrsoTroKTsp5AgKOydtOyDgey5mCDsoJzqsbApIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjE5OS43ODMiIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjE1NS44OTE1IiB5PSIxMTkuMzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE1NS44OTE1IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+4pyoIOuFuOydtOymiCAoTm9pc2UpIPCfkqU8L3RzcGFuPjx0c3BhbiB4PSIxNTUuODkxNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7KO867OA7JeQIOyVhOustOuPhCDsl4bripQg7JWE7Iu4LjwvdHNwYW4+PHRzcGFuIHg9IjE1NS44OTE1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj4tJmd0OyDrsoTroKTsp5AgKOydtOyDgey5mCDsoJzqsbApPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 작동 파라미터 및 K-means와의 비교 장단점 전격 해부 (3단 표)**

이 토픽은 작동을 위한 '2대 파라미터'와 '3대 포인트 분류'를 명시한 뒤, K-means의 약점을 어떻게 후벼파고(장점) 본인은 무엇이 취약한지(단점) 대조하는 것이 완벽한 득점 포인트입니다.

| **핵심 척도**            | **⚙️ 작동 원리 (핵심 파라미터)**                                                                                                          | **🔴 데이터 포인트의 3대 분류 🚨**                                                                                                                                                                              | **⚖️ K-means와 비교 장단점 💯**                                                                                              |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| **개념 및 역할**          | **'밀도를 판단하는 2가지 기준'.** 알고리즘이 동작하기 위해 인간이 세팅해 줘야 하는 절대 기준값.                                                                      | **'데이터의 계급 나누기'.** 파라미터 기준에 따라 모든 점들을 3가지 상태로 판별하여 묶거나 버림.                                                                                                                                            | **'형태의 유연성과 파라미터 민감도'.** K-means가 못하는 걸 다 해내지만, 세팅이 잘못되면 싹 다 뭉치거나 흩어짐.                                                 |
| **세부 요소 및 분류 기준 🚨** | **\[1. Epsilon (Eps, 입실론)]** 특정 점을 기준으로 탐색할 원의 '반경(거리)' 지정. **\[2. MinPts (최소 포인트)]** 그 반경 안에 최소한 '몇 개의 데이터'가 있어야 군집으로 인정할지 지정. | **\[1. 코어 점 (Core Point) 💯]** 자기 반경(Eps) 안에 최소 인원(MinPts)을 채운 군집의 대장. **\[2. 경계 점 (Border Point)]** 인원은 못 채웠지만, 대장(Core)의 원 안에 걸쳐있는 가장자리 점. **\[3. 노이즈 점 (Noise Point) 💯]** 코어도 안 되고 경계도 안 되는 튀는 값. | **\[장점 1 💯]** K값 설정 필요 없음. **\[장점 2 💯]** 도넛 모양, 초승달 모양 등 **비선형(기하학적) 군집 완벽 탐지.** **\[장점 3]** 노이즈를 스스로 제거하므로 이상치에 강함. |
| **한계 / 약점**          | 둘 중 하나라도 잘못 설정되면 알고리즘이 붕괴됨.                                                                                                     | 노이즈(이상치)를 사전에 걸러주므로 데이터 전처리에 짱 좋음.                                                                                                                                                                    | **\[단점 🚨]** 밀도가 다양한 군집이 섞여 있으면, 반경(Eps) 하나로는 다 못 묶음 (HDBSCAN 필요). **차원의 저주**에 취약함.                                    |

#### **IV. \[결론/제언] HDBSCAN을 통한 다중 밀도(Varying Density) 한계 극복**

* **(키워드 위주 2줄 마무리)** "DBSCAN은 전역적인 하나의 반경(Eps)만 사용하므로, 빽빽한 군집과 듬성듬성한 군집이 섞여 있을 때 군집화에 실패하는 치명적 단점이 있습니다. 최근 머신러닝 업계에서는 계층적(Hierarchical) 기법을 융합하여 다양한 밀도의 군집을 반경(Eps) 없이도 알아서 찾아내는 **'HDBSCAN'으로 진화하여 클러스터링의 성능을 극대화하고 있습니다.**"
