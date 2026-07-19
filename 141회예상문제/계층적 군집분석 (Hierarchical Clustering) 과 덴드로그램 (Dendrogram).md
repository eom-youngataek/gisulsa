#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 "k를 미리 정하지 않아도" 군집화가 가능한가)
Ⅱ. 계층적 군집분석 핵심 원리 및 유형
Ⅲ. 덴드로그램 구조 및 해석
Ⅳ. k-means 등 타 군집 기법과의 비교
Ⅴ. 결론 및 활용 방안
```

포인트: 개요에서 **"앞서 다룬 ML 학습 방법의 비지도학습이 '레이블 없이 데이터 내부 구조를 발견'하는 것이라면, 계층적 군집분석은 그 중에서도 '군집 수(k)를 사전에 지정하지 않고 데이터 간 유사도를 기반으로 계층적 트리 구조를 생성해 다양한 수준의 군집을 동시에 탐색'하는 기법이다 — k-means가 k를 먼저 정해야 하는 한계를 극복하고, 덴드로그램이라는 시각적 도구로 군집 형성 과정 전체를 한눈에 파악할 수 있다는 것이 핵심 차별화 강점"**이라는 한 줄로 시작하면, 왜 이 답안이 앞서 다룬 비지도학습·클러스터링 시리즈 전체의 **계층적 접근 핵심**인지 드러납니다.

---

#### Ⅱ. 계층적 군집분석 핵심 원리 및 유형

**가. 2대 접근 방식**

| 구분      | ==응집형 (Agglomerative)== | ==분리형 (Divisive)==    |
| ------- | ------------------- | ----------------- |
| **방향**  | 상향식(Bottom-Up)      | 하향식(Top-Down)     |
| **시작**  | 각 데이터 포인트가 독립 군집    | 전체가 하나의 군집        |
| **과정**  | 가장 유사한 군집을 반복 병합    | 가장 이질적인 군집을 반복 분할 |
| **종료**  | 모든 데이터가 하나의 군집      | 각 데이터가 독립 군집      |
| **복잡도** | O(n²logn)           | O(2ⁿ)·계산 비용 매우 높음 |
| **활용**  | **대부분의 실무 적용** ✅    | 분류 문제 초기 탐색       |

---

**나. 응집형 군집분석 동작 과정**

```
[응집형 계층적 군집분석 단계별 동작]

초기: 각 데이터 포인트 = 독립 군집 (n개)
  {A} {B} {C} {D} {E}
       ↓
Step1: 가장 가까운 두 군집 병합
  거리 행렬 계산 → 최소 거리 쌍 선택
  {A,B} {C} {D} {E}
       ↓
Step2: 거리 행렬 업데이트 → 반복 병합
  {A,B} {C,D} {E}
       ↓
Step3: 계속 병합
  {A,B,C,D} {E}
       ↓
Step4: 최종 하나의 군집
  {A,B,C,D,E}
       ↓
덴드로그램으로 전체 과정 시각화
```

---

**다. 거리 측도 (Distance Measure)**

| 거리 측도           | 수식                | 특징           | 적합 데이터   |
| --------------- | ----------------- | ------------ | -------- |
| ==**유클리드 거리**== | √Σ(xᵢ-yᵢ)²        | 직선 거리·직관적    | 연속형·정규분포 |
| ==**맨해튼 거리**==  | Σ│xᵢ-yᵢ│          | 격자 이동 거리     | 이상치 강건   |
| ==**코사인 유사도**== | cos(θ)=A·B/‖A‖‖B‖ | 방향 유사성 측정    | 텍스트·고차원  |
| ==**상관계수 거리**== | 1-Pearson(x,y)    | 선형 관계 기반     | 시계열·유전자  |
| ==**민코프스키**==   | (Σ│xᵢ-yᵢ│ᵖ)^(1/p) | 유클리드·맨해튼 일반화 | p값 조정 활용 |

---

**라. 연결 방법 (Linkage Method)**

| 연결 방법                | 정의               | 특징                 | 한계                  |
| -------------------- | ---------------- | ------------------ | ------------------- |
| ==**단일 연결 (Single)**==   | 두 군집 간 **최소 거리** | 사슬 형태 군집 형성        | 체이닝(Chaining) 문제 🚨 |
| ==**완전 연결 (Complete)**== | 두 군집 간 **최대 거리** | 균일한 크기 군집          | 이상치 민감              |
| ==**평균 연결 (Average)**==  | 두 군집 간 **평균 거리** | 단일·완전의 절충          | UPGMA·WPGMA         |
| ==**Ward 연결**==          | **군집 내 분산 최소화**  | 균형잡힌 군집·가장 널리 사용 ✅ | 구형 군집 가정            |
| ==**중심 연결 (Centroid)**== | 군집 **중심 간 거리**   | 직관적 해석 가능          | 역전(Inversion) 문제    |

---

#### Ⅲ. 덴드로그램 구조 및 해석

**가. 덴드로그램 구조**

```
[덴드로그램 시각적 구조]

높이(Height)
  │                    ┌──────────────┐
4 │                    │              │
  │          ┌─────────┤              │
3 │          │         │              │
  │    ┌─────┤         │              │
2 │    │     │         │              │
  │  ┌─┤   ┌─┤       ┌─┤            │
1 │  │ │   │ │       │ │            │
  └──┴─┴───┴─┴───────┴─┴────────────┘
     A  B   C  D      E  F    →  데이터 포인트

구성요소:
  ① 리프 노드(Leaf Node): 개별 데이터 포인트
  ② 내부 노드(Internal Node): 군집 병합 지점
  ③ 높이(Height·Cophenetic Distance): 병합 시 거리값
  ④ 수평선(Horizontal Cut): 원하는 군집 수 결정 기준
```

**나. 덴드로그램 해석 방법**

```
[수평선(Cut) 위치에 따른 군집 수 결정]

높이
  │                    ──────Cut1: k=2 (2개 군집)
4 │────────────────────
  │
3 │──────────Cut2: k=3 (3개 군집)
  │
2 │──Cut3: k=4 (4개 군집)
  │
1 │
  └──A──B──C──D──E──F

→ Cut1(높이 4): {A,B,C,D}, {E,F} → 2개 군집
→ Cut2(높이 3): {A,B}, {C,D}, {E,F} → 3개 군집
→ Cut3(높이 2): {A,B}, {C}, {D}, {E,F} → 4개 군집

최적 Cut 위치: 가장 긴 수직선(Height 차이 최대) 지점
→ 군집 간 거리가 급격히 증가하는 변곡점 선택
```

**다. 최적 군집 수 결정 기준**

| 기준              | 방법                    | 핵심                |
| --------------- | --------------------- | ----------------- |
| ==**덴드로그램 시각 판단**== | 가장 긴 수직선 구간에서 Cut     | 직관적·주관적           |
| ==**코페네틱 상관계수**==   | 덴드로그램 거리 vs 실제 거리 상관  | 값이 높을수록 덴드로그램 적합  |
| ==**엘보우 방법**==      | 군집 내 분산(WCSS) 변화 관찰   | 변화율 급감 지점 선택      |
| ==**실루엣 계수**==      | (b-a)/max(a,b) / -1~1 | 1에 가까울수록 군집 품질 높음 |
| ==**갭 통계량**==       | 실제 WCSS vs 랜덤 WCSS 비교 | 격차 최대 지점이 최적 k    |

---

#### Ⅳ. k-means 등 타 군집 기법과의 비교

| 비교 항목          | ==계층적 군집분석==  | ==k-means==       | ==DBSCAN==    |
| -------------- | --------- | ------------- | --------- |
| **군집 수 사전 지정** | 불필요 ✅     | 필요 🚨         | 불필요 ✅     |
| **군집 형태**      | 제한 없음     | 구형(Spherical) | 임의 형태 ✅   |
| **이상치 처리**     | 취약 🚨     | 취약 🚨         | 강건 ✅      |
| **계산 복잡도**     | O(n²logn) | O(nkt)        | O(n logn) |
| **대규모 데이터**    | 비효율 🚨    | 효율 ✅          | 중간        |
| **결과 시각화**     | 덴드로그램 ✅   | 산점도           | 산점도       |
| **결정론성**       | 결정론적 ✅    | 초기값 의존 🚨     | 결정론적 ✅    |
| **해석 가능성**     | 매우 높음 ✅   | 중간            | 중간        |
| **적합 데이터**     | 소규모·계층 구조 | 대규모·구형        | 밀도 기반·노이즈 |

---

#### Ⅴ. 결론 및 활용 방안

**도메인별 적용 사례**

```
[계층적 군집분석 주요 활용 분야]

①생명정보학(Bioinformatics)
  유전자 발현 데이터 군집화
  → 유사 기능 유전자 그룹 식별
  → Ward 연결 + 유클리드 거리 주로 사용

②고객 세분화(Customer Segmentation)
  RFM 데이터(구매빈도·금액·최근성) 군집화
  → 마케팅 타깃 그룹 식별
  → 덴드로그램으로 세분화 수준 유연 결정

③문서·텍스트 군집화
  TF-IDF 벡터 + 코사인 거리
  → 유사 주제 문서 그룹핑
  → 뉴스 분류·특허 분류 적용

④이상 탐지(Anomaly Detection)
  정상 패턴과 거리가 먼 포인트 식별
  → 제조 불량·금융 사기 탐지
  → 덴드로그램 상단 단독 분기 = 이상치
```

**앞서 다룬 개념과의 연결**

|연계 개념|연결 내용|
|---|---|
|**비지도학습**|레이블 없이 데이터 구조 발견·군집 탐색|
|**차원 축소(PCA·t-SNE)**|고차원 데이터 시각화 후 계층적 군집 적용|
|**GNN 커뮤니티 탐지**|Leiden 알고리즘과 동일한 계층적 군집화 철학|
|**GraphRAG 커뮤니티**|문서 엔티티 그래프의 계층적 커뮤니티 요약 구조|
|**AI 학습데이터 품질**|군집 기반 데이터 대표성·다양성 검증 수단|

**한계점 및 보완 방향**

- **계산 복잡도**: O(n²logn)으로 대규모 데이터 적용 어려움 → BIRCH·CURE 등 확장 알고리즘으로 보완
- **되돌리기 불가(Irreversibility)**: 한번 병합된 군집은 수정 불가 → 초기 거리 측도·연결 방법 신중 선택
- **이상치 민감**: 이상치가 군집 구조를 왜곡 → 사전 이상치 제거 필수
- **고차원 저주**: 차원이 높아질수록 거리 측도 의미 퇴색 → PCA·UMAP 차원 축소 후 적용

---

#### 기술사 답안 포인트

**k 사전 지정 불필요 → 응집형(Bottom-Up)·분리형(Top-Down) 2대 방식 → 거리 측도(유클리드·코사인·맨해튼) → 연결 방법(단일·완전·평균·Ward) → 덴드로그램(리프·내부 노드·높이·수평선 Cut) → 최적 군집 수(실루엣계수·엘보우·코페네틱) → k-means·DBSCAN과 비교표 → 유전자·고객세분화·문서군집 활용** 흐름으로 서술하면 완성도 높은 답안이 됩니다. **덴드로그램의 수평선 Cut 위치 = 가장 긴 수직선 구간**이 핵심 차별화 포인트입니다.



#### **1. 답안 전개 스토리 (핵심 압축)**

> "처음부터 군집 수(K)를 지정하지 않고, 모든 데이터 노드가 자기 혼자만의 방에서 출발해 \*\*가장 가까운 놈끼리 엮어 올라가며 나무 모양의 계층 구조를 완성하는 '상향식 군집화 알고리즘'\*\*이다. 데이터 간의 거리를 계산해 합병하는 '연결법(Linkage)'이 핵심이다. 가장 가까운 점끼리 재는 **'단일 연결'**, 가장 먼 점끼리 재는 **'완전 연결'**, 두 군집의 무게중심을 재는 **'와드(Ward's) 연결 🚨'** 등이 있다. 이 결합 과정을 거꾸로 뒤집어 세운 나무 족보 그림을 \*\*'덴드로그램(Dendrogram)'\*\*이라고 부른다. 시각적으로 이 덴드로그램의 수평 가지를 가위로 싹둑 자르는 위치에 따라 최종 군집 개수가 2개, 3개 등으로 자유롭게 결정되는 직관적인 군집 모델이다."

#### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNjkyLjkxOTk5OTk5OTk5OTggNDAyLjMxNSIgd2lkdGg9IjE2OTIuOTE5OTk5OTk5OTk5OCIgaGVpZ2h0PSI0MDIuMzE1IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfX19BZ2dsb21lcmF0aXZlXyIgZGF0YS1sYWJlbD0i7J2R7KeR7ZiVIOqzhOy4teyggSDqtbDsp5HrtoTshJ0gKEFnZ2xvbWVyYXRpdmUpIO2UhOuhnOyEuOyKpCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMTYxMi45MTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjMyMi4zMTUiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIxNjEyLjkxOTk5OTk5OTk5OTgiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7snZHsp5HtmJUg6rOE7Li17KCBIOq1sOynkeu2hOyEnSAoQWdnbG9tZXJhdGl2ZSkg7ZSE66Gc7IS47IqkPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTVEFSVCIgZGF0YS10bz0iRElTVCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyNjkuODYxOTk5OTk5OTk5OTcsMjE1LjE1NzUgMzE3Ljg2MTk5OTk5OTk5OTk3LDIxNS4xNTc1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJESVNUIiBkYXRhLXRvPSJMSU5LIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjUxNC42ODA5OTk5OTk5OTk5LDIxNS4xNTc1IDU2Mi42ODA5OTk5OTk5OTk5LDIxNS4xNTc1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJMSU5LIiBkYXRhLXRvPSJTTCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i6rCA7J6lIOqwgOq5jOyatCDqsbDrpqwiIHBvaW50cz0iNzU5LjQxNzI1LDI4MC43MzYyNSA4MzYuOTk1OTk5OTk5OTk5OSwyODAuNzM2MjUgODM2Ljk5NTk5OTk5OTk5OTksMjgwLjM5Njg3NSAxMDcwLjA1Mjk5OTk5OTk5OTksMjgwLjM5Njg3NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTElOSyIgZGF0YS10bz0iQ0wiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuqwgOyepSDrqLwg6rGw66asIiBwb2ludHM9IjgyNC45OTU5OTk5OTk5OTk5LDIxNS4xNTc1IDEwNzAuMDUyOTk5OTk5OTk5OSwyMTUuMTU3NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTElOSyIgZGF0YS10bz0iV0wiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyYpOywqOygnOqzse2VqSDspp3qsIAg7LWc7IaM7ZmUIiBwb2ludHM9Ijc1OS40MTcyNSwxNDkuNTc4NzUgODM2Ljk5NTk5OTk5OTk5OTksMTQ5LjU3ODc1IDgzNi45OTU5OTk5OTk5OTk5LDE0OS45MTgxMjUgMTA1My4wMDk5OTk5OTk5OTk4LDE0OS45MTgxMjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlNMIiBkYXRhLXRvPSJERU5EIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjExODguMzI1OTk5OTk5OTk5OCwyODAuMzk2ODc1IDEyMTcuMzY5LDI4MC4zOTY4NzUgMTIxNy4zNjksMjI4LjYwNzUgMTI1My4zNjksMjI4LjYwNzUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkNMIiBkYXRhLXRvPSJERU5EIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjExODguMzI1OTk5OTk5OTk5OCwyMTUuMTU3NSAxMjUzLjM2OSwyMTUuMTU3NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iV0wiIGRhdGEtdG89IkRFTkQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTIwNS4zNjksMTQ5LjkxODEyNSAxMjE3LjM2OSwxNDkuOTE4MTI1IDEyMTcuMzY5LDIwMS43MDc0OTk5OTk5OTk5OCAxMjUzLjM2OSwyMDEuNzA3NDk5OTk5OTk5OTgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iTElOSyIgZGF0YS10bz0iU0wiIGRhdGEtbGFiZWw9IuqwgOyepSDqsIDquYzsmrQg6rGw66asIj4KICA8cmVjdCB4PSI4ODYuODE1OTk5OTk5OTk5OCIgeT0iMjY0LjM5Njg3NSIgd2lkdGg9IjEwNC4zNzQwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjkzOS4wMDI5OTk5OTk5OTk4IiB5PSIyNzkuNTQ2ODc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7qsIDsnqUg6rCA6rmM7Jq0IOqxsOumrDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJMSU5LIiBkYXRhLXRvPSJDTCIgZGF0YS1sYWJlbD0i6rCA7J6lIOuovCDqsbDrpqwiPgogIDxyZWN0IHg9Ijg5OC42OTU5OTk5OTk5OTk5IiB5PSIxOTkuMTU3NSIgd2lkdGg9IjgwLjYxNCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjkzOS4wMDI5OTk5OTk5OTk5IiB5PSIyMTQuMzA3NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+6rCA7J6lIOuovCDqsbDrpqw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iTElOSyIgZGF0YS10bz0iV0wiIGRhdGEtbGFiZWw9IuyYpOywqOygnOqzse2VqSDspp3qsIAg7LWc7IaM7ZmUIj4KICA8cmVjdCB4PSI4NjguOTk1OTk5OTk5OTk5OSIgeT0iMTMzLjkxODEyNSIgd2lkdGg9IjE0MC4wMTQiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI5MzkuMDAyOTk5OTk5OTk5OSIgeT0iMTQ5LjA2ODEyNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7Jik7LCo7KCc6rOx7ZWpIOymneqwgCDstZzshoztmZQ8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlNUQVJUIiBkYXRhLWxhYmVsPSLqsIEg642w7J207YSwIOuFuOuTnOqwgCDqsJzrs4Qg6rWw7KeRIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIxOTYuNzA3NDk5OTk5OTk5OTgiIHdpZHRoPSIyMTMuODYyIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTYyLjkzMDk5OTk5OTk5OTk4IiB5PSIyMTUuMTU3NDk5OTk5OTk5OTciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuqwgSDrjbDsnbTthLAg64W465Oc6rCAIOqwnOuzhCDqtbDsp5E8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkRJU1QiIGRhdGEtbGFiZWw9IuKcqCAxLiDsnKDsgqzrj4Qg6rGw66asIOqzhOyCsCDinKgK7Jyg7YG066as65OcIOqxsOumrCDtlonroKwg7J6R7ISxIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjMxNy44NjE5OTk5OTk5OTk5NyIgeT0iMTg4LjI1NzUiIHdpZHRoPSIxOTYuODE5IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDE2LjI3MTQ5OTk5OTk5OTk1IiB5PSIyMTUuMTU3NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNDE2LjI3MTQ5OTk5OTk5OTk1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+4pyoIDEuIOycoOyCrOuPhCDqsbDrpqwg6rOE7IKwIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjQxNi4yNzE0OTk5OTk5OTk5NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7Jyg7YG066as65OcIOqxsOumrCDtlonroKwg7J6R7ISxPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkxJTksiIGRhdGEtbGFiZWw9IuKcqCAyLiDsl7DqsrDrspUoTGlua2FnZSkg7KCB7JqpIPCfmqgg4pyoIiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjY5My44Mzg1LDg0IDgyNC45OTYsMjE1LjE1NzUgNjkzLjgzODUsMzQ2LjMxNSA1NjIuNjgwOTk5OTk5OTk5OSwyMTUuMTU3NSIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI2OTMuODM4NSIgeT0iMjE1LjE1NzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuKcqCAyLiDsl7DqsrDrspUoTGlua2FnZSkg7KCB7JqpIPCfmqgg4pyoPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTTCIgZGF0YS1sYWJlbD0i64uo7J28IOyXsOqysOuylSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMDcwLjA1Mjk5OTk5OTk5OTkiIHk9IjI2MS45NDY4NzUiIHdpZHRoPSIxMTguMjczIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTEyOS4xODk1IiB5PSIyODAuMzk2ODc0OTk5OTk5OTciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuuLqOydvCDsl7DqsrDrspU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkNMIiBkYXRhLWxhYmVsPSLsmYTsoIQg7Jew6rKw67KVIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjEwNzAuMDUyOTk5OTk5OTk5OSIgeT0iMTk2LjcwNzQ5OTk5OTk5OTk4IiB3aWR0aD0iMTE4LjI3MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjExMjkuMTg5NSIgeT0iMjE1LjE1NzQ5OTk5OTk5OTk3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7smYTsoIQg7Jew6rKw67KVPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJXTCIgZGF0YS1sYWJlbD0i7JmA65OcIOyXsOqysOuylSBXYXJkIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjEwNTMuMDA5OTk5OTk5OTk5OCIgeT0iMTMxLjQ2ODEyNSIgd2lkdGg9IjE1Mi4zNTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMTI5LjE4OTQ5OTk5OTk5OTciIHk9IjE0OS45MTgxMjQ5OTk5OTk5NyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7JmA65OcIOyXsOqysOuylSBXYXJkPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJERU5EIiBkYXRhLWxhYmVsPSLinKggMy4g642065Oc66Gc6re4656oIChEZW5kcm9ncmFtKSDsi5zqsIHtmZQg8J+SryDinKgK7KGx67O0IOq1rOyhsOyXkOyEnCDsm5DtlZjripQg64aS7J2066W8IOy7pO2Mhe2VmOyXrCDstZzsooUg6rWw7KeRIOu2hO2VoCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMjUzLjM2OSIgeT0iMTg4LjI1NzUiIHdpZHRoPSIzODMuNTUwOTk5OTk5OTk5OTMiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTQ0NS4xNDQ0OTk5OTk5OTk5IiB5PSIyMTUuMTU3NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTQ0NS4xNDQ0OTk5OTk5OTk5IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+4pyoIDMuIOuNtOuTnOuhnOq3uOueqCAoRGVuZHJvZ3JhbSkg7Iuc6rCB7ZmUIPCfkq8g4pyoPC90c3Bhbj48dHNwYW4geD0iMTQ0NS4xNDQ0OTk5OTk5OTk5IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7sobHrs7Qg6rWs7KGw7JeQ7IScIOybkO2VmOuKlCDrhpLsnbTrpbwg7Luk7YyF7ZWY7JesIOy1nOyihSDqtbDsp5Eg67aE7ZWgPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

| **핵심 척도**                | **📊 4대 연결법 (Linkage Methods) 🚨**                                                                                                                                   | **🔑 덴드로그램 (Dendrogram) 💯**                                                                                   | **🏁 비계층적 군집화 (K-means) 대조 💯**                                                                                                           |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **개념 / 알고리즘**            | **'군집 결합 가이드라인'.** 두 개별 군집의 거리를 어떠한 기준으로 측정하여 한 몸으로 합쳐나갈지 결정하는 수학 공식.                                                                                                | **'군집 결합 이력 나무 족보'.** 데이터 노드가 합쳐질 때마다의 거리 높이를 Y축으로 시각화한 트리 구조 그래프.                                             | 사전에 군집 개수 K*K*를 정하는 방식과, 데이터간의 거리에 의존해 계층을 쌓는 방식의 비교.                                                                                     |
| **핵심 세부 내용 (출제 포인트) 🚨** | **1. 단일연결(Single):** 최소 거리 기준. **2. 완전연결(Complete):** 최대 거리 기준. **3. 평균연결(Average):** 평균 거리 기준. **4. \[와드연결 (Ward's) 🚨]** 군집 내 오차제곱합(SSE)의 증가를 최소화하는 방향으로 결합 (정밀함). | **\[가위질을 통한 군집수 결정 💯]** - 사전에 군집 수 K*K*를 알 필요가 없음. - 완성된 덴드로그램 트리의 특정 **유사도 거리 높이선(수평선)을 컷팅**하여 유연한 군집 분할 완성. | **\[K-means]** 임의의 중심점 설정 필요. 군집 크기 예측 불가. 대용량 연산 빠름. **\[계층적 군집 💯]** **초기 중심점 불필요. 덴드로그램으로 시각적 의사결정 수월. 연산량 O(N3)*O*(*N*3) 로 대용량에 쥐약.** |

* **(제언)** "계층적 군집분석은 메모리에 모든 노드 간의 거리 행렬(Proximity Matrix)을 상주시켜야 하므로 데이터가 수만 건만 되어도 서버가 다운됩니다. 따라서 **대용량 빅데이터 클러스터링 시에는 가볍고 빠른 K-means로 1차 군집 구조를 조율한 뒤, 대표 표본들을 대상으로 계층적 군집과 덴드로그램을 얹어 검증하는 복합 아키텍처가 실무적입니다.**"
