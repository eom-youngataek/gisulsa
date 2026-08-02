#### **MLP를 대체할 수 있는 새로운 신경망: KAN (Kolmogorov-Arnold Network)**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 MLP의 "고정 활성화 함수" 구조에 의문을 던지는가)
Ⅱ. KAN 핵심 원리
Ⅲ. MLP와의 비교 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 Mamba가 'Attention이라는 핵심 연산 자체를 SSM으로 대체'하는 아키텍처 혁신이었다면, KAN(Kolmogorov-Arnold Network)은 그보다 더 근본적인 지점 — 1957년 이후 모든 신경망(MLP·Transformer·CNN 포함)의 기본 구성 요소였던 '노드에 고정된 비선형 활성화 함수(ReLU·GELU 등)를 두고 엣지(가중치)는 단순 곱셈만 수행한다'는 퍼셉트론 이래의 설계 원칙 자체를 뒤집는다 — 2024년 MIT 연구팀이 제안한 KAN은 소련 수학자 콜모고로프와 아놀드가 1957년 증명한 '모든 다변수 연속함수는 유한 개의 단변수 함수의 합성으로 표현 가능하다'는 콜모고로프-아놀드 표현 정리를 신경망 구조로 구현해, 활성화 함수를 노드가 아닌 '엣지'에 위치시키고 그 함수 자체를 학습 가능한 스플라인(Spline)으로 만듦으로써 앞서 다룬 PINN처럼 과학·수학 문제에서 더 적은 파라미터로 더 해석 가능한 결과를 내는 MLP의 대안으로 주목받은 것"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.
![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNTI3LjM3NyAxMTcuNiIgd2lkdGg9IjE1MjcuMzc3IiBoZWlnaHQ9IjExNy42IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IklucHV0IiBkYXRhLXRvPSJFZGdlIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLtlZnsirUg6rCA64ql7ZWcIEItc3BsaW5lIO2ZnOyEse2ZlCDtlajsiJggcGhpIiBwb2ludHM9IjI0NC4yMjksNTguNDUgNTMwLjQ1NSw1OC40NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRWRnZSIgZGF0YS10bz0iTm9kZSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI4MjguMDUsNTguNDUgODc2LjA1LDU4LjQ1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJOb2RlIiBkYXRhLXRvPSJPdXRwdXQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTEwNy42OTYsNTguNDUgMTE1NS42OTYsNTguNDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iSW5wdXQiIGRhdGEtdG89IkVkZ2UiIGRhdGEtbGFiZWw9Iu2VmeyKtSDqsIDriqXtlZwgQi1zcGxpbmUg7Zmc7ISx7ZmUIO2VqOyImCBwaGkiPgogIDxyZWN0IHg9IjI4OC4yMjkwMDAwMDAwMDAwNCIgeT0iNDIuNDUiIHdpZHRoPSIxOTguMjI2MDAwMDAwMDAwMDMiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzODcuMzQyMDAwMDAwMDAwMDQiIHk9IjU3LjYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPu2VmeyKtSDqsIDriqXtlZwgQi1zcGxpbmUg7Zmc7ISx7ZmUIO2VqOyImCBwaGk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IklucHV0IiBkYXRhLWxhYmVsPSLsnoXroKUg64W465OcIDog64uo7IicIOyLoO2YuCDsoITri6wiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMjA0LjIyOSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE0Mi4xMTQ1MDAwMDAwMDAwMiIgeT0iNTguNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyeheugpSDrhbjrk5wgOiDri6jsiJwg7Iug7Zi4IOyghOuLrDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRWRnZSIgZGF0YS1sYWJlbD0i7Jej7KeAIOyXsOyCsCA6IOyKpOy5vOudvCDqsIDspJHsuZgg64yA7IugIO2VqOyImCDrsLDsuZgiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTMwLjQ1NSIgeT0iNDAiIHdpZHRoPSIyOTcuNTk0OTk5OTk5OTk5OTciIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjY3OS4yNTI1IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7Jej7KeAIOyXsOyCsCA6IOyKpOy5vOudvCDqsIDspJHsuZgg64yA7IugIO2VqOyImCDrsLDsuZg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik5vZGUiIGRhdGEtbGFiZWw9IuuFuOuTnCDsl7DsgrAgOiDri6jsiJwg642n7IWIIO2VqeyCsCBTdW0iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iODc2LjA1IiB5PSI0MCIgd2lkdGg9IjIzMS42NDYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iOTkxLjg3Mjk5OTk5OTk5OTkiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7rhbjrk5wg7Jew7IKwIDog64uo7IicIOuNp+yFiCDtlansgrAgU3VtPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJPdXRwdXQiIGRhdGEtbGFiZWw9Iuy1nOyihSDstpzroKUgOiDquLDtmLgg7ZqM6reAIO2Gte2VtCDsiJjtlZkg6rO17IudIOuPhOy2nCDqsIDriqUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTE1NS42OTYiIHk9IjQwIiB3aWR0aD0iMzMxLjY4MSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEzMjEuNTM2NSIgeT0iNTguNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuy1nOyihSDstpzroKUgOiDquLDtmLgg7ZqM6reAIO2Gte2VtCDsiJjtlZkg6rO17IudIOuPhOy2nCDqsIDriqU8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

***

#### Ⅱ. KAN 핵심 원리

**가. 콜모고로프-아놀드 표현 정리**

```
[수학적 근거: Kolmogorov-Arnold Representation Theorem]

임의의 다변수 연속함수 f(x1, x2, ..., xn)은
유한 개의 단변수 함수의 합성과 합으로 정확히 표현 가능:

f(x1,...,xn) = Σ(q=1→2n+1) Φq( Σ(p=1→n) φq,p(xp) )

  φq,p: 내부 단변수 함수(각 입력변수 처리)
  Φq  : 외부 단변수 함수(합산 결과 처리)

핵심 통찰:
  "복잡한 다차원 함수도 결국은
   단순한 1차원 함수들의 조합으로 완전히 분해된다"
  → 이 정리를 딥러닝 아키텍처로 구현한 것이 KAN
```

**나. MLP vs KAN 구조적 차이**

```
[MLP 구조: 노드에 활성화 함수]

입력 → [가중치 곱(선형)] → 노드[고정 활성화함수 σ] → 출력
       학습 대상: 가중치(스칼라) W
       활성화함수: 고정(ReLU 등), 학습 안 됨

[KAN 구조: 엣지에 학습 가능한 함수]

입력 → 엣지[학습 가능한 스플라인 함수 φ(x)] → 노드[단순 합산] → 출력
       학습 대상: 스플라인 함수 φ 자체(제어점들)
       노드: 활성화 없이 순수 덧셈만 수행

핵심 전환:
  MLP: "학습 대상=가중치, 비선형성=고정"
  KAN: "학습 대상=비선형 함수 자체, 합산=고정"
```

**다. KAN 핵심 구성요소**

| 구성요소                       | 내용                                         |
| :------------------------- | :----------------------------------------- |
| **엣지 함수(Edge Function)**   | 각 연결마다 독립적인 학습 가능 1차원 함수(B-스플라인 기반) 배치     |
| **B-스플라인 파라미터화**           | 함수를 제어점(Control Point) 집합으로 표현해 미분 가능하게 학습 |
| **그리드 확장(Grid Extension)** | 학습 중 스플라인의 격자 세밀도를 점진적으로 늘려 정밀도 향상         |
| **가지치기·시각화**               | 학습된 엣지 함수를 직접 그래프로 시각화 가능 → 해석가능성 확보       |

***

#### Ⅲ. MLP와의 비교 및 적용 체계

**가. MLP vs KAN 전면 비교**

| 비교 항목              | MLP                  | KAN                       |
| :----------------- | :------------------- | :------------------------ |
| **비선형성 위치**        | 노드(고정 활성화함수)         | **엣지(학습 가능한 함수)** ✅       |
| **학습 대상**          | 가중치(스칼라)             | **함수 자체(스플라인 제어점)**       |
| **파라미터 효율(과학 문제)** | 상대적으로 많이 필요          | **적은 파라미터로 근접 정확도** ✅     |
| **해석가능성**          | 블랙박스에 가까움 🚨         | **엣지 함수 시각화로 해석 가능** ✅    |
| **학습 속도(현재 구현)**   | 빠름(고도로 최적화됨) ✅       | **느림**(스플라인 연산 오버헤드) 🚨   |
| **대규모 언어모델 적용**    | 검증됨(Transformer 등) ✅ | 초기 연구 단계, 미검증 🚨          |
| **강점 분야**          | 범용(이미지·언어·전 영역)      | **과학 계산·수식 발견·저차원 함수 근사** |

**나. 적용 시나리오별 비교**

| 시나리오                   | 권장 아키텍처             | 이유                              |
| :--------------------- | :------------------ | :------------------------------ |
| **대규모 언어모델·이미지 인식**    | **MLP/Transformer** | 검증된 확장성·최적화된 하드웨어 커널            |
| **물리 방정식 근사(PINN 대체)** | **KAN 검토 가능**       | 앞서 다룬 PINN처럼 저차원 연속함수 근사에 적합    |
| **과학 데이터에서 수식 발견**     | **KAN 강점 영역**       | 학습된 엣지 함수를 해석해 숨겨진 수학 공식 역추정 가능 |
| **해석가능성이 규제상 필수인 도메인** | **KAN 검토 가능**       | 금융·의료처럼 설명 가능한 AI가 요구되는 영역      |
| **초대규모 파라미터·처리량 우선**   | **MLP**             | 현재 KAN은 연산 효율에서 MLP를 따라가지 못함    |

**다. 현재 KAN의 한계**

| 한계              | 내용                                                   |
| :-------------- | :--------------------------------------------------- |
| **연산 비용**       | 스플라인 함수 평가가 단순 행렬곱보다 훨씬 무거움                          |
| **하드웨어 최적화 부재** | GPU 커널이 MLP처럼 고도로 최적화되지 않음(앞서 다룬 CUDA 생태계 종속 문제와 유사) |
| **고차원 확장성 미검증** | 저차원 과학 문제에서는 강점이나 LLM급 초고차원에서는 검증 부족                 |
| **초기 연구 단계**    | 2024년 제안 이후 안정성·모범 사례가 아직 충분히 축적되지 않음                |

***

**(제언)** "KAN의 진정한 의의는 지금 당장 MLP를 대체하는 데 있는 것이 아니라, 1957년 순수 수학 정리가 70년 가까이 지나 신경망 설계의 근본 가정 자체를 재검토하게 만들었다는 점에서, 딥러닝이 여전히 수학 이론으로부터 새로운 아이디어를 발굴할 여지가 크다는 것을 보여준 사례입니다. 실무적으로는 현재 KAN을 대규모 언어모델이나 이미지 인식처럼 MLP·Transformer가 이미 고도로 최적화되고 검증된 영역에 무리하게 적용하기보다는, 앞서 다룬 PINN이 다루는 저차원 물리 방정식 근사나 과학 데이터에서 숨겨진 수식을 발견하는 것처럼 '해석가능성'과 '적은 데이터에서의 정밀한 함수 근사'가 핵심 가치인 좁고 특화된 영역부터 시범 적용하고, 연산 효율을 개선하는 하드웨어 커널과 하이브리드 아키텍처(일부 층은 KAN, 일부 층은 MLP)에 대한 후속 연구 동향을 지속적으로 관찰하는 것이 합리적인 접근입니다.

***

**앞서 다룬 개념과의 연결**

| 연계 개념              | 연결 내용                                                 |
| :----------------- | :---------------------------------------------------- |
| **PINN**           | KAN이 PINN의 신경망 백본을 대체해 더 적은 파라미터로 물리 방정식 근사 연구 진행 중   |
| **Mamba·SSM**      | 둘 다 Transformer/MLP 표준 구조의 근본 가정에 도전하는 아키텍처 혁신이라는 공통점 |
| **NAS(신경망 구조 탐색)** | KAN의 스플라인 그리드 크기·깊이 등 하이퍼파라미터 자동 탐색에 NAS 적용 가능        |
| **AI 반도체·이기종 컴퓨팅** | 스플라인 연산에 최적화된 전용 하드웨어 커널 개발이 향후 실용화의 관건               |
| **온디바이스 NPU**      | 해석가능하고 경량화된 KAN이 향후 규제 대응이 필요한 엣지 AI에 응용될 잠재력         |

### **I. 포스트 MLP의 강력한 후보, KAN의 개요**

기존의 다층 인공신경망(MLP)은 노드(Node)에 고정된 활성화 함수(ReLU, GELU 등)를 두고 엣지(Edge)에 스칼라 가중치(W*W*)를 곱하는 구조로, 블랙박스 특성이 강하고 많은 파라미터가 요구되었습니다. \*\*KAN(Kolmogorov-Arnold Network)\*\*은 수학적 정리인 콜모고로프-아놀드 표현 정리를 기반으로, 노드는 단순 덧셈만 수행하고 **엣지 상에 학습 가능한 1차원 스플라인(B-spline) 활성화 함수를 배치**하여, 뛰어난 해석 가능성(XAI)과 파라미터 효율성을 동시에 실현한 아키텍처입니다.

***

### **II. KAN의 수학적 정리 및 엣지 활성화 구조**

#### **1. 콜모고로프-아놀드 표현 정리 (Kolmogorov-Arnold Theorem)**

다변수 연속 함수 f(x1,…,xn)*f*(*x*1​,…,*xn*​)는 1변수 연속 함수들의 제한된 중첩과 덧셈의 조합으로 완벽히 표현할 수 있습니다. f(x1,…,xn)=∑q=12n+1Φq(∑p=1nϕq,p(xp))*f*(*x*1​,…,*xn*​)=∑*q*=12*n*+1​Φ*q*​(∑*p*=1*n*​*ϕq*,*p*​(*xp*​))

#### **2. KAN의 엣지 함수 파라미터화 (B-spline 결합)**

* KAN의 엣지 활성화 함수 ϕ(x)*ϕ*(*x*)는 기저 함수(SiLU)와 학습 가능한 \*\*B-스플라인(B-spline)\*\*의 선형 결합으로 구성됩니다. ϕ(x)=wb⋅SiLU(x)+ws⋅∑iciBi(x)*ϕ*(*x*)=*wb*​⋅SiLU(*x*)+*ws*​⋅∑*i*​*ci*​*Bi*​(*x*)
* **국소 제어성(Local Control)**: B-스플라인 특성상 격자(Grid) 단위로 국소적 변경이 일어나므로, 새로운 데이터를 연속 학습할 때 기존 지식이 유실되는 **파괴적 망각(Catastrophic Forgetting) 현상이 획기적으로 완화**됩니다.

***

### **III. 전통적 다층 신경망(MLP)과 차세대 콜모고로프-아놀드 네트워크(KAN)의 상세 비교**

| **비교 항목**        | **🏛️ 다층 인공신경망 (MLP)**              | **🧬 콜모고로프-아놀드 네트워크 (KAN)**              |
| :--------------- | :---------------------------------- | :--------------------------------------- |
| **이론적 기반**       | 보편적 근사 정리 (Universal Approximation) | **콜모고로프-아놀드 표현 정리 (K-A Theorem)**        |
| **활성화 함수 위치**    | **노드(Node)에 고정 함수 배치** (ReLU 등)     | **엣지(Edge)에 학습 가능한 1차원 함수(B-spline) 배치** |
| **엣지 가중치 특성**    | 스칼라 실수 가중치 (W*W*)                   | **가변 파라미터화된 1차원 함수 (ϕ(x)*ϕ*(*x*))**      |
| **설명 가능성 (XAI)** | 블랙박스 (내부 수식 복원 불가능)                 | **화이트박스 (기호 회귀 통해 명시적 수학 공식 도출)**        |
| **파라미터 및 망각**    | 파라미터 소요 많음, 파괴적 망각 심함               | **적은 파라미터로 고정밀 근사, 파괴적 망각 대폭 완화**        |

***

### **IV. KAN의 대표적 활용 분야 및 현단계 한계점**

**IMPORTANT**

1. **과학적 인공지능(AI for Science)에서의 혁신**: KAN은 학습된 엣지 함수들을 수학적 기호(Symbolic Regression)로 단순화하여 물리 법칙(편미분 방정식 PDE 해법 등)을 인간이 이해할 수 있는 수학 공식으로 직접 도출해 내는 데 독보적 성능을 보입니다.
2. **GPU 연산 속도 한계 극복 필요성**: 현단계 KAN은 엣지마다 B-스플라인을 계산해야 하므로, 행렬 곱셈(GEMM)에 극도로 최적화된 현세대 GPU 하드웨어 상에서 MLP 대비 학습 속도가 느린 단점이 있습니다. 이를 보완하기 위한 KAN 전용 CUDA 커널 최적화 작업이 활발히 진행 중입니다.
