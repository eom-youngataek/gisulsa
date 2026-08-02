#### **합성데이터 품질의 두 축: Fidelity & Diversity 검증**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 합성데이터는 "그럴듯함"만으로 부족한가)
Ⅱ. Fidelity·Diversity 핵심 원리
Ⅲ. 검증 지표 비교 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"차분 프라이버시가 '합성데이터를 만드는 과정에서 프라이버시를 수학적으로 보장'하는 기법이라면, Fidelity·Diversity 검증은 그렇게 만들어진 합성데이터가 '실제로 원본 데이터를 대체해 쓸 만한가'를 사후적으로 판정하는 품질 검증 체계다 — CTGAN·Diffusion 모델로 생성한 합성데이터는 겉보기에 원본과 비슷해 보이는 것만으로는 부족한데, 충실도(Fidelity)가 낮으면 통계적 특성이 왜곡되어 그 데이터로 학습한 모델의 성능이 저하되고, 다양성(Diversity)이 낮으면 원본의 소수 사례(Minority Case)나 극단값이 사라져 실제로는 원본 일부만 복제한 것에 불과해지므로, 이 두 축을 동시에 정량적으로 검증하지 않은 합성데이터는 앞서 다룬 AI 학습데이터 품질관리의 요건을 충족하지 못하는 것"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjE2LjI1Nzk5OTk5OTk5OTggMjg2LjcwMDAwMDAwMDAwMDA1IiB3aWR0aD0iMTIxNi4yNTc5OTk5OTk5OTk4IiBoZWlnaHQ9IjI4Ni43MDAwMDAwMDAwMDAwNSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTeW50aGV0aWMiIGRhdGEtdG89IlZhbCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI2MzkuNjIxNSw3Ni45IDYzOS42MjE1LDEyNC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJWYWwiIGRhdGEtdG89IkZpZGVsaXR5IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjYzOS42MjE1LDE2MS44IDYzOS42MjE1LDE3OS44IDIzMi44ODY5OTk5OTk5OTk5NywxNzkuOCAyMzIuODg2OTk5OTk5OTk5OTcsMTk3LjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlZhbCIgZGF0YS10bz0iRGl2ZXJzaXR5IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjYzOS42MjE1LDE2MS44IDYzOS42MjE1LDE3OS44IDYzOS42MjE1LDE3OS44IDYzOS42MjE1LDE5Ny44IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJWYWwiIGRhdGEtdG89IlV0aWxpdHkiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNjM5LjYyMTUsMTYxLjggNjM5LjYyMTUsMTc5LjggMTAxNC44NjM0OTk5OTk5OTk3LDE3OS44IDEwMTQuODYzNDk5OTk5OTk5NywxOTcuOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU3ludGhldGljIiBkYXRhLWxhYmVsPSLsg53shLEg66qo6424IDogQ1RHQU4gLyBEaWZmdXNpb24gLyBMTE0iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTE0LjE2NTUiIHk9IjQwIiB3aWR0aD0iMjUwLjkxMTk5OTk5OTk5OTk1IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNjM5LjYyMTUiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7sg53shLEg66qo6424IDogQ1RHQU4gLyBEaWZmdXNpb24gLyBMTE08L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlZhbCIgZGF0YS1sYWJlbD0i7ZWp7ISxIOuNsOydtO2EsCDsoIHtlanshLEg6rKA7KadIO2MjOydtO2UhOudvOyduCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1MDMuMDUwNDk5OTk5OTk5OTQiIHk9IjEyNC45IiB3aWR0aD0iMjczLjE0MiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNjM5LjYyMTUiIHk9IjE0My4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7ZWp7ISxIOuNsOydtO2EsCDsoIHtlanshLEg6rKA7KadIO2MjOydtO2UhOudvOyduDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRmlkZWxpdHkiIGRhdGEtbGFiZWw9IjEuIOyLoOuisOuPhCBGaWRlbGl0eSA6IOybkOuzuCDsnKDsgqzshLEg4p6UIEtTLVRlc3QgLyBGSUQgLyBQcmVjaXNpb24iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDAiIHk9IjE5Ny44IiB3aWR0aD0iMzg1Ljc3Mzk5OTk5OTk5OTk0IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjMyLjg4Njk5OTk5OTk5OTk3IiB5PSIyMTYuMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjEuIOyLoOuisOuPhCBGaWRlbGl0eSA6IOybkOuzuCDsnKDsgqzshLEg4p6UIEtTLVRlc3QgLyBGSUQgLyBQcmVjaXNpb248L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkRpdmVyc2l0eSIgZGF0YS1sYWJlbD0iMi4g64uk7JaR7ISxIERpdmVyc2l0eSA6IOuqqOuTnCDsu6TrsoTrpqzsp4Ag4p6UIFRhaWwgUmF0aW8gLyBSZWNhbGwiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDUzLjc3NCIgeT0iMTk3LjgiIHdpZHRoPSIzNzEuNjk0OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjYzOS42MjE1IiB5PSIyMTYuMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjIuIOuLpOyWkeyEsSBEaXZlcnNpdHkgOiDrqqjrk5wg7Luk67KE66as7KeAIOKelCBUYWlsIFJhdGlvIC8gUmVjYWxsPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJVdGlsaXR5IiBkYXRhLWxhYmVsPSIzLiDsnKDsmqnshLEgJmFtcDsg6rCc7J247KCV67O0IDogVFNUUiDrsI8gRENSIOqxsOumrCDqsoDspp0iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iODUzLjQ2ODk5OTk5OTk5OTgiIHk9IjE5Ny44IiB3aWR0aD0iMzIyLjc4ODk5OTk5OTk5OTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTAxNC44NjM0OTk5OTk5OTk3IiB5PSIyMTYuMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjMuIOycoOyaqeyEsSAmYW1wOyDqsJzsnbjsoJXrs7QgOiBUU1RSIOuwjyBEQ1Ig6rGw66asIOqygOymnTwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

***

#### Ⅱ. Fidelity·Diversity 핵심 원리

**가. 두 축의 정의와 트레이드오프**

```
[Fidelity vs Diversity 개념도]

Fidelity(충실도):
  "생성된 데이터가 원본 데이터의 통계적 특성·분포를
   얼마나 정확히 재현하는가"
  → 원본과 합성데이터의 분포가 겹치는 정도

Diversity(다양성):
  "생성된 데이터가 원본 데이터의 전체 변동 범위·
   희소 패턴까지 폭넓게 포괄하는가"
  → 특정 패턴에 치우치지 않고 원본의 전체 스펙트럼을 커버

[두 극단의 실패 사례]

Case 1: 높은 Fidelity, 낮은 Diversity (모드 붕괴·Mode Collapse)
  생성 모델이 가장 흔한 패턴 몇 가지만 반복 생성
  → 원본과 통계적으로는 비슷해 보이나
    실제로는 다양성 없는 반복 데이터 🚨
  → 희귀 질환·이상 거래 같은 소수 사례가 합성데이터에서 사라짐

Case 2: 높은 Diversity, 낮은 Fidelity
  다양한 값을 생성하나 원본의 실제 분포·상관관계와 무관
  → 통계적으로 비현실적인 조합 발생
    (예: 나이 5세에 소득 1억)
  → 모델 학습에 사용 시 오히려 성능 저하 🚨

→ 두 지표를 반드시 함께, 균형 있게 검증해야 함
```

**나. 검증 접근 방식 3대 유형**

| 접근 방식                 | 원리                                              | 예시 지표                                       |
| :-------------------- | :---------------------------------------------- | :------------------------------------------ |
| **통계적 유사도 검증**        | 원본·합성 데이터의 분포·상관관계를 직접 비교                       | KS 검정·상관행렬 차이·PSI(앞서 다룬 데이터 드리프트 지표와 동일 원리) |
| **머신러닝 효용성 검증(TSTR)** | Train-on-Synthetic, Test-on-Real 방식으로 실사용 성능 검증 | 합성데이터로 학습한 모델의 실데이터 정확도                     |
| **임베딩 공간 기반 검증**      | 데이터를 저차원 임베딩으로 변환 후 분포 간 거리 측정                  | FID·Precision-Recall(생성모델 특화)               |

***

#### Ⅲ. 검증 지표 비교 및 적용 체계

**가. 정형(Tabular) 데이터 검증 지표**

| 지표                            | 측정 대상                   | 산출 방식                                |
| :---------------------------- | :---------------------- | :----------------------------------- |
| **KS 검정(Kolmogorov-Smirnov)** | 단일 컬럼의 분포 일치도(Fidelity) | 원본·합성 컬럼의 누적분포함수(CDF) 최대 차이          |
| **상관관계 유사도**                  | 컬럼 간 관계 보존 여부(Fidelity) | 원본·합성 데이터의 상관행렬 차이(Frobenius Norm 등) |
| **범주 분포 커버리지**                | 범주형 값의 다양성(Diversity)   | 원본에 존재하는 범주값이 합성데이터에도 등장하는 비율        |
| **TSTR 정확도 격차**               | 실사용 효용성(Fidelity 종합)    | 합성데이터 학습 모델 vs 원본데이터 학습 모델의 성능 차이    |

**나. 이미지·생성모델 특화 지표**

| 지표                                  | 측정 대상                                                                                      | 특징                           |
| :---------------------------------- | :----------------------------------------------------------------------------------------- | :--------------------------- |
| **FID(Fréchet Inception Distance)** | 원본·생성 이미지 분포 간 거리(Fidelity 중심)                                                             | 값이 낮을수록 원본과 유사               |
| **Precision & Recall(생성모델)**        | **Precision**: 생성 샘플이 원본 분포 내에 있는가(Fidelity) / **Recall**: 원본 분포를 얼마나 폭넓게 커버하는가(Diversity) | FID 하나로는 놓치는 두 축을 분리 측정      |
| **Density & Coverage**              | Precision·Recall의 개선판, 이상치에 덜 민감                                                           | 최근 GAN·Diffusion 평가의 표준으로 확산 |

**다. Fidelity 중심 vs Diversity 중심 지표 비교**

| 비교 항목        | Fidelity 중심 지표                     | Diversity 중심 지표              |
| :----------- | :--------------------------------- | :--------------------------- |
| **핵심 질문**    | "생성된 데이터가 원본과 통계적으로 닮았는가"          | "생성된 데이터가 원본의 전체 범위를 포괄하는가"  |
| **대표 지표**    | KS 검정·상관관계 유사도·FID·Precision       | 범주 커버리지·Recall·엔트로피 기반 지표    |
| **낮을 때 위험**  | 비현실적 데이터로 모델 학습 왜곡                 | 소수 사례·이상치 소실, 편향 심화          |
| **프라이버시 관계** | Fidelity가 지나치게 높으면 원본 재식별 위험 증가 🚨 | Diversity가 충분하면 프라이버시 보호에 유리 |

**라. 실무 적용 시 검증 절차**

| 단계                   | 내용                                                              |
| :------------------- | :-------------------------------------------------------------- |
| **①통계적 사전 검증**       | KS 검정·상관관계 비교로 1차 스크리닝, 명백한 왜곡 여부 조기 발견                         |
| **②TSTR 성능 검증**      | 실제 다운스트림 태스크(분류·회귀 등)에서 합성데이터 학습 모델의 성능 확인                      |
| **③다양성·소수 사례 검증**    | 희귀 클래스·이상치가 합성데이터에도 일정 비율 보존되는지 별도 확인                           |
| **④프라이버시 위험 재검토**    | Fidelity가 과도하게 높은 개별 레코드가 원본과 지나치게 유사한지 재식별 위험 점검(멤버십 추론 공격 관점) |
| **⑤MLOps 품질 게이트 연계** | 위 지표들에 임계값을 설정해 합성데이터 배포 파이프라인에 자동 검증 단계로 내재화                   |

***

**(제언)** "Fidelity와 Diversity 검증의 근본적 의의는 합성데이터를 '원본과 비슷해 보이는 가짜'가 아니라 '실제 분석·모델 학습에 대체 투입 가능한 신뢰할 수 있는 자산'으로 격상시키는 데 있으며, 두 지표는 종종 상충되는 관계에 있어 어느 한쪽만 최적화하면 반대편이 희생되는 근본적 트레이드오프가 존재하므로 도메인 요구사항에 따라 우선순위를 다르게 설정해야 합니다. 예컨대 금융 이상거래 탐지 모델을 학습시킬 합성데이터라면 극소수 사기 패턴이 소실되지 않도록 Diversity(특히 희귀 클래스 보존)를 Fidelity보다 우선해야 하고, 반대로 통계 보고서 작성용 합성데이터라면 전체 분포의 정확한 재현(Fidelity)이 더 중요하며, 실무에서는 KS 검정·상관관계 비교 같은 통계적 검증을 1차 필터로, TSTR 같은 실사용 성능 검증을 최종 판단 기준으로 삼는 이중 검증 체계를 구축하고 Fidelity가 과도하게 높아 원본 개별 레코드와 지나치게 유사해지는 경우는 오히려 프라이버시 위험 신호로 간주해 재차 점검하는 것이 합성데이터 파이프라인 설계의 핵심 전략입니다.

***

**앞서 다룬 개념과의 연결**

| 연계 개념               | 연결 내용                                               |
| :------------------ | :-------------------------------------------------- |
| **차분 프라이버시·DP-GAN** | 프라이버시 보장 노이즈 추가와 Fidelity 사이의 트레이드오프 관리             |
| **멤버십 추론 공격**       | 지나치게 높은 Fidelity가 개별 레코드 재식별 위험으로 이어지는 연결고리         |
| **AI 학습데이터 품질관리**   | Fidelity·Diversity 검증이 합성데이터 품질관리의 핵심 하위 절차         |
| **데이터 드리프트(PSI)**   | 원본-합성 분포 비교에 사용하는 PSI 지표가 드리프트 탐지와 동일한 통계적 원리       |
| **가명정보 결합**         | 결합 데이터의 통계적 유용성 검증에도 Fidelity·Diversity 검증 개념 적용 가능 |

#### **I. 합성 데이터 활용의 안전성 관문, 적합성 검증의 개요**

개인정보보호 규제(GDPR, ISMS-P) 대응 및 학습 데이터 부족 극복을 위해 합성 데이터 활용이 급증하고 있으나, 검증되지 않은 합성 데이터는 환각(Hallucination) 또는 모드 붕괴(Mode Collapse)로 인해 AI 모델의 성능을 붕괴시킬 수 있습니다. 따라서 합성 데이터가 \*\*실제 데이터의 물리적·통계적 특징을 얼마나 진짜처럼 모사하는지 검증하는 신뢰도(Fidelity)\*\*와, \*\*원본의 희귀 케이스까지 전체 분포를 빠짐없이 표현해 내는지 검증하는 다양성(Diversity)\*\*을 포함한 정량적 적합성 검증 체계 수립이 필수적입니다.

***

### **II. 신뢰도(Fidelity)와 다양성(Diversity)의 2대 검증 지표 체계**

#### **1. 신뢰도 (Fidelity: 충실도 및 표면 유사성)**

* **개념**: 합성된 데이터 개별 샘플 하나하나가 원본 데이터의 분포 규칙을 위배하지 않고 얼마나 노이즈 없이 진짜 같은가(Realism)를 측정합니다.
* **정량 지표**:
  * **수치형/테이블 데이터**: **KS-Test (Kolmogorov-Smirnov Test)** p-value, **Wasserstein Distance**, 상호정보량 차이
  * **이미지/비전 데이터**: **FID (Fréchet Inception Distance)** (낮을수록 우수), **Precision** (생성 분포 중 진짜 데이터 영역에 속한 비율)

#### **2. 다양성 (Diversity: 분포 커버리지 및 표현력)**

* **개념**: 생성 모델이 특정 우세한 패턴만 반복 생성하지 않고, 원본 데이터의 모든 클래스와 \*\*소수 꼬리 분포(Tail Distribution)\*\*까지 빠짐없이 다채롭게 생성하는가를 측정합니다.
* **정량 지표**:
  * **수치형/테이블 데이터**: **Tail Distribution Ratio** (극단값 비율 검증), 범주형 변수의 **샤논 엔트로피(Entropy)** 대조
  * **이미지/비전 데이터**: **Recall** (진짜 데이터 분포 중 합성 데이터가 커버하는 비율), **Coverage Metric**

***

### **III. 신뢰도(Fidelity)와 다양성(Diversity)의 상세 비교**

| **평가 축**          | **🎯 신뢰도 (Fidelity / 유사성)**                       | **🌐 다양성 (Diversity / 커버리지)**                  |
| :---------------- | :------------------------------------------------ | :--------------------------------------------- |
| **핵심 검증 목적**      | 개별 합성 샘플이 원본 데이터처럼 진짜 같은지 검증                      | 원본의 전체 통계 공간과 꼬리(Tail) 영역을 커버하는지 검증            |
| **결함 발생 시 현상**    | **낮은 신뢰도**: 비현실적 이상치 및 비논리적 가짜 데이터 생성             | **낮은 다양성**: 모드 붕괴(Mode Collapse) 및 특정 클래스 쏠림   |
| **수치형 정량 지표**     | **KS-Test (p > 0.05), Wasserstein Distance, FID** | **Tail Distribution Ratio, 범주형 엔트로피(Entropy)** |
| **생성 모델 지표 (비전)** | **Precision (생성 데이터의 정밀도)**                       | **Recall (원본 데이터 공간의 재현율)**                    |
| **다운스트림 영향**      | 모델 추론 시 물리적 법칙 및 문맥 정합성 보장                        | 학습 데이터의 편향(Bias) 방지 및 희귀 케이스 훈련 가능             |

***

### **IV. 엔드-투-엔드 합성 데이터 검증 수행 가이드라인**

**IMPORTANT**

1. **다운스트림 실효성 검증 (TSTR: Train on Synthetic, Test on Real)**: 지표 검증과 병행하여, 합성 데이터로만 ML 모델을 훈련시킨 뒤 정답인 실제 데이터(Real)에 테스트하여 기존 모델 대비 성능(F1-Score, RMSE 등)이 **90\~95% 이상 유지되는지 TSTR 검증**을 필수로 통과시켜야 합니다.
2. **개인정보 침해 방지를 위한 DCR (Distance to Closest Record) 검증**: 신뢰도(Fidelity)가 100%에 가깝다는 것은 원본 데이터를 그대로 템플릿 복사(Overfitting)했을 위험이 있습니다. 최단 거리 데이터 측정인 **DCR 검증**을 수행하여 원본 데이터와의 물리적 이격거리가 안전 기준치 이상 확보되었는지 확인해야 합니다.
