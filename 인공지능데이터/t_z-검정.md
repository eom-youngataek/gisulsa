### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (가설검정목적, z와t의근본적갈림길) — 3~4줄
Ⅱ. Z검정 - 모분산을아는경우 (본론①, 도식 1개 필수)
Ⅲ. t검정 - 모분산을모르는경우, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

앞서다룬 \*\*"A/B테스트의p-값"\*\*을 실제로 계산하려면, \*\*"관찰된차이가얼마나이례적인지"\*\*를 **표준화된점수**로 바꿔야합니다 — 그때 \*\*"모집단의분산을정확히아는지,모르는지"\*\*에따라 **z검정**과 **t검정**중 하나를 선택합니다.

### Ⅱ. Z검정 — 모분산을 아는경우

| 항목       | 내용                                       |
| :------- | :--------------------------------------- |
| **전제조건** | **모집단의분산(σ²)을정확히알고있음**— 실무에서는 **매우드문경우** |
| **분포**   | 앞서다룬 **중심극한정리**가보장하는 **표준정규분포(Z분포)** 사용  |
| **공식**   | Z = (표본평균-모평균) / (모표준편차/√n)              |

→ 암기: **"모집단의진짜분산을알고있을때만쓴다"** — 하지만 앞서다룬 \*\*"불편추정량"\*\*답안에서 다뤘듯, 현실에서는 \*\*"모분산자체가미지수"\*\*인경우가대부분이라, Z검정은 **이론적기준점**역할이 큽니다.

### 도식화 제안

```
[Z검정 - 모분산을알때]
Z = (표본평균 - 모평균) / (모표준편차/√n)
     ↓
표준정규분포(Z분포)에서 
"이Z값이 얼마나극단적인지" 확인 → p-값산출
```

### Ⅲ. t검정 — 모분산을 모르는경우, 핵심 배점

**함정 방지: "t검정을쓴다"고만답하면절반. 왜"모분산대신표본분산을쓰면 정규분포가아니라 더뚱뚱한t분포가되는지",그리고표본크기에따라t분포가어떻게변하는지보여줘야완성됩니다.**

| 항목                   | 내용                                                                               |
| :------------------- | :------------------------------------------------------------------------------- |
| **전제조건**(현실적)        | **모분산을모름**— 앞서다룬 \*\*"불편추정량(n-1로나눈표본분산)"\*\*으로 **대신추정**해서사용                      |
| **핵심문제**(왜다른분포가필요한가) | 모분산대신 \*\*추정치(표본분산)\*\*를쓰면, 그추정자체에 **추가적인불확실성**이생겨 **분포의양끝(꼬리)이더두꺼워짐**           |
| **t분포**(자유도의역할)      | 표본크기(n)가 **작을수록**꼬리가더두껍고,**"자유도"**(n-1)가 **커질수록**(표본이많아질수록) **점점Z분포(정규분포)에가까워짐** |

→ 암기: **"모분산을모르니표본분산으로대신추정하는데, 그추정자체가불확실해서 분포가더뚱뚱해진다 — 표본이많아지면 그불확실성도줄어들어 결국Z분포와같아진다"** — 앞서다룬 \*\*"불편추정량의n-1보정"\*\*이, 여기서는 \*\*"t분포의자유도(n-1)"\*\*로 **정확히같은개념**이 재사용됩니다.

### 도식화 제안

```
[Z분포 vs t분포 - 표본크기에따른변화]

[표본크기작을때(n=5)]           [표본크기클때(n=100)]
      Z분포                          Z분포
    ╱────╲                        ╱────╲
  ╱─t분포──╲  ← t분포꼬리가더두꺼움    ╱t분포╲  ← Z분포와거의같아짐
 ╱          ╲                    ╱        ╲
(모분산추정의불확실성 반영)         (표본이많아 불확실성감소,
                                   자유도(n-1)증가)

→ "표본이커질수록, t분포는Z분포로수렴한다"
```

**실무적사용기준**

\| 상황 | 검정선택 |\
\<br>\
| **표본크기충분히큼**(n≥30)+모분산모름 | **실무적으로는t검정도Z검정과거의동일**(t분포가Z분포에수렴) |\
| **표본크기작음**(n<30)+모분산모름 | **반드시t검정**사용 — Z검정을쓰면 **불확실성을과소평가**해 **잘못된결론**(위양성증가)위험 |

→ 앞서다룬 \*\*"A/B테스트의조기중단위험"\*\*이 바로 이 문제의 실전사례입니다: \*\*"표본이아직충분히모이지않은시점(작은n)"\*\*에서 **Z검정처럼단순계산**하면, **불확실성을과소평가해 성급하게'유의미하다'고오판**할 위험이있습니다.

### 도식화 제안

```
[검정선택 기준]
모분산을 아는가?
   ├─ Yes → Z검정(현실에서드묾)
   └─ No  → 표본크기는?
              ├─ n≥30(충분히큼) → t검정(사실상Z검정과유사)
              └─ n<30(작음) → 반드시t검정(Z검정쓰면위험)
```

### Ⅳ. 결론

Z검정과t검정의핵심차이는 \*\*"모집단의분산을정확히아는가(Z검정),아니면표본분산으로추정해야하는가(t검정)"\*\*입니다 — 앞서다룬 \*\*"불편추정량의n-1보정"\*\*이 t검정에서는 \*\*"자유도(n-1)"\*\*로 다시등장하며, **"표본분산이라는추가적추정의불확실성"** 때문에 t분포는 **Z분포보다꼬리가두껍지만, 표본크기가커질수록점점Z분포에수렴**합니다 — 실무에서는 **"표본이작을때 Z검정을잘못쓰면 불확실성을과소평가해 위양성이늘어나는"** 위험이 있어, 앞서다룬 \*\*"A/B테스트의조기중단위험"\*\*과 정확히같은맥락에서 \*\*"충분한표본크기확보전까지는신중해야한다"\*\*는 교훈이 재확인됩니다 — 이로써 오늘하루다룬 **중심극한정리→점추정/구간추정→불편추정량→t/z검정**으로 이어지는 통계적추론시리즈전체가, \*\*"불확실성의크기를정확히반영하는것이,올바른통계적판단의핵심"\*\*이라는 하나의결론으로 완결됩니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "두 집단의 평균 차이가 진짜 통계적으로 유의미한지, 아니면 단순한 우연인지 검증하는 가설 검정의 핵심 형제다. 구분하는 칼날은 \*\*'모표준편차(σ*σ*)를 아는가'\*\*와 \*\*'표본의 크기(n*n*)'\*\*다. 첫째, **'Z-검정'**. 모집단의 표준편차를 확실히 알고 있거나, 모르더라도 표본 크기가 30개 이상으로 넉넉할 때 쓴다. 예쁜 종 모양의 '표준정규분포'를 기준으로 가설을 검정한다. 둘째, **'T-검정'**. 모집단의 표준편차를 죽어도 모르고, 표본 크기도 30개 미만으로 작아서 불안할 때 쓴다. 표준정규분포보다 양쪽 꼬리가 더 두툼한 't-분포'를 사용하여 표본이 적어 생기는 불확실성을 깐깐하게 페널티로 반영한다. 현실 세계에서는 모집단의 표준편차를 아는 것이 불가능하므로, 실제 비즈니스 A/B 테스트나 데이터 과학 실무의 99%는 T-검정을 선택한다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 집단 간 차이 규명의 양대 기둥, Z-검정과 T-검정 개요**

* **정의:** 표본 통계량의 평균값을 바탕으로 모집단의 평균이 특정 값과 같은지, 혹은 두 모집단의 평균 간에 유의미한 차이가 존재하는지 정규분포(Z) 또는 t-분포를 활용해 판정하는 모수적 가설 검정 기법.
* **목적:** 단순히 평균 숫자가 다름을 넘어, 표본 오차에 의한 우연한 차이인지 모집단 고유의 본질적 차이인지를 유의수준(α*α*, p-value)에 의거해 통계적으로 선언하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 모집단의 정보량에 따른 분포의 분기**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4NDEuNDQ5IDk1NC4xMDQ5OTk5OTk5OTk5IiB3aWR0aD0iODQxLjQ0OSIgaGVpZ2h0PSI5NTQuMTA0OTk5OTk5OTk5OSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iWl92c19UX18iIGRhdGEtbGFiZWw9Ilot6rKA7KCVIHZzIFQt6rKA7KCVIOyEoO2DnSDrtoTquLDsoJAiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9Ijc2MS40NDkiIGhlaWdodD0iODc0LjEwNDk5OTk5OTk5OTkiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI3NjEuNDQ5IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+Wi3qsoDsoJUgdnMgVC3qsoDsoJUg7ISg7YOdIOu2hOq4sOygkDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iSU4iIGRhdGEtdG89IkNPTkQxIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjI3Mi45ODQ0OTk5OTk5OTk5LDEyMC45IDI3Mi45ODQ0OTk5OTk5OTk5LDE2OC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDT05EMSIgZGF0YS10bz0iWiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iWWVzIiBwb2ludHM9IjI0My41OTEzMzMzMzMzMzMyNywzMTUuODY1ODMzMzMzMzMzMzQgMjQzLjU5MTMzMzMzMzMzMzI3LDM1Ny4yNTkgMTU3Ljg2OTE2NjY2NjY2NjYyLDM1Ny4yNTkgMTU3Ljg2OTE2NjY2NjY2NjYyLDcyMy40MDUgMTY4Ljk5Njk5OTk5OTk5OTk2LDcyMy40MDUgMTY4Ljk5Njk5OTk5OTk5OTk5LDc1OS40MDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkNPTkQxIiBkYXRhLXRvPSJDT05EMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iTm8iIHBvaW50cz0iMzAyLjM3NzY2NjY2NjY2NjYsMzE1Ljg2NTgzMzMzMzMzMzM0IDMwMi4zNzc2NjY2NjY2NjY2LDM1Ny4yNTkgMzM5LjQ0OTk5OTk5OTk5OTkzLDM1Ny4yNTkgMzM5LjQ0OTk5OTk5OTk5OTkzLDQ2MS41NTkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkNPTkQyIiBkYXRhLXRvPSJaIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSJZZXMgKOykkeyLrOq3ue2VnOygleumrCBDTFQpIiBwb2ludHM9IjMwOS4xOTIzMzMzMzMzMzMzLDYxMi44NDczMzMzMzMzMzM0IDMwOS4xOTIzMzMzMzMzMzMzLDY1NS4xMDUgMjU3LjAxMTU4MzMzMzMzMzMsNjU1LjEwNSAyNTcuMDExNTgzMzMzMzMzMyw3MjMuNDA1IDIyMy4yNDEzMzMzMzMzMzMzMyw3MjMuNDA1IDIyMy4yNDEzMzMzMzMzMzMzMyw3NTkuNDA1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDT05EMiIgZGF0YS10bz0iVCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iTm8gKOyGjO2RnOuzuCAvIOuqqOu2hOyCsCDrrLTsp4ApIiBwb2ludHM9IjM2OS43MDc2NjY2NjY2NjY2LDYxMi44NDczMzMzMzMzMzMzIDM2OS43MDc2NjY2NjY2NjY2LDY1NS4xMDUgNDE5LjYxMjk5OTk5OTk5OTk0LDY1NS4xMDUgNDE5LjYxMjk5OTk5OTk5OTk0LDc1OS40MDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlQiIGRhdGEtdG89IlQxIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0MTkuNjEyOTk5OTk5OTk5OTQsODEzLjIwNDk5OTk5OTk5OTkgNDE5LjYxMjk5OTk5OTk5OTk0LDgzNy4yMDQ5OTk5OTk5OTk5IDQxOS42MTI5OTk5OTk5OTk5NCw4MzcuMjA0OTk5OTk5OTk5OSA0MTkuNjEyOTk5OTk5OTk5OTQsODYxLjIwNDk5OTk5OTk5OTkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVCIgZGF0YS10bz0iVDIiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQxOS42MTI5OTk5OTk5OTk5NCw4MTMuMjA0OTk5OTk5OTk5OSA0MTkuNjEyOTk5OTk5OTk5OTQsODM3LjIwNDk5OTk5OTk5OTkgMTcxLjgyMjk5OTk5OTk5OTk4LDgzNy4yMDQ5OTk5OTk5OTk5IDE3MS44MjI5OTk5OTk5OTk5OCw4NjEuMjA0OTk5OTk5OTk5OSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJUIiBkYXRhLXRvPSJUMyIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDE5LjYxMjk5OTk5OTk5OTk0LDgxMy4yMDQ5OTk5OTk5OTk5IDQxOS42MTI5OTk5OTk5OTk5NCw4MzcuMjA0OTk5OTk5OTk5OSA2NjguNTE0NDk5OTk5OTk5OSw4MzcuMjA0OTk5OTk5OTk5OSA2NjguNTE0NDk5OTk5OTk5OSw4NjEuMjA0OTk5OTk5OTk5OSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkNPTkQxIiBkYXRhLXRvPSJaIiBkYXRhLWxhYmVsPSJZZXMiPgogIDxyZWN0IHg9IjEzOS4zNjkxNjY2NjY2NjY2MiIgeT0iNTM3LjE4MiIgd2lkdGg9IjM2LjY1OCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjE1Ny42OTgxNjY2NjY2NjY2MiIgeT0iNTUyLjMzMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+WWVzPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkNPTkQxIiBkYXRhLXRvPSJDT05EMiIgZGF0YS1sYWJlbD0iTm8iPgogIDxyZWN0IHg9IjMyMy45NDk5OTk5OTk5OTk5MyIgeT0iMzg4LjI1OSIgd2lkdGg9IjMwLjcxODAwMDAwMDAwMDAwNCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjMzOS4zMDg5OTk5OTk5OTk5IiB5PSI0MDMuNDA5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5ObzwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJDT05EMiIgZGF0YS10bz0iWiIgZGF0YS1sYWJlbD0iWWVzICjspJHsi6zqt7ntlZzsoJXrpqwgQ0xUKSI+CiAgPHJlY3QgeD0iMTg3LjUxMTU4MzMzMzMzMzMiIHk9IjY4Ni4xMDUiIHdpZHRoPSIxMzguODI2MDAwMDAwMDAwMDIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyNTYuOTI0NTgzMzMzMzMzMyIgeT0iNzAxLjI1NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+WWVzICjspJHsi6zqt7ntlZzsoJXrpqwgQ0xUKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJDT05EMiIgZGF0YS10bz0iVCIgZGF0YS1sYWJlbD0iTm8gKOyGjO2RnOuzuCAvIOuqqOu2hOyCsCDrrLTsp4ApIj4KICA8cmVjdCB4PSIzNDguNjEyOTk5OTk5OTk5OTQiIHk9IjY4Ni4xMDUiIHdpZHRoPSIxNDEuNzk2MDAwMDAwMDAwMDUiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI0MTkuNTEwOTk5OTk5OTk5OTciIHk9IjcwMS4yNTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPk5vICjshoztkZzrs7ggLyDrqqjrtoTsgrAg66y07KeAKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iSU4iIGRhdGEtbGFiZWw9IuqwgOyEpCDqsoDsoJUg7Iuc7J6ROiDrkZAg7KeR64uoIO2Pieq3oCDruYTqtZAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTQ3LjUyODQ5OTk5OTk5OTk1IiB5PSI4NCIgd2lkdGg9IjI1MC45MTE5OTk5OTk5OTk5OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI3Mi45ODQ0OTk5OTk5OTk5IiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuqwgOyEpCDqsoDsoJUg7Iuc7J6ROiDrkZAg7KeR64uoIO2Pieq3oCDruYTqtZA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkNPTkQxIiBkYXRhLWxhYmVsPSLrqqjsp5Hri6gg7ZGc7KSA7Y647LCoCs+DIOulvCDslYzqs6Ag7J6I64qU6rCAPyIgZGF0YS1zaGFwZT0iZGlhbW9uZCI+CiAgPHBvbHlnb24gcG9pbnRzPSIyNzIuOTg0NDk5OTk5OTk5OSwxNjguOSAzNjEuMTYzOTk5OTk5OTk5OSwyNTcuMDc5NSAyNzIuOTg0NDk5OTk5OTk5OSwzNDUuMjU5IDE4NC44MDQ5OTk5OTk5OTk5MiwyNTcuMDc5NSIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjcyLjk4NDQ5OTk5OTk5OTkiIHk9IjI1Ny4wNzk1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIyNzIuOTg0NDk5OTk5OTk5OSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuuqqOynkeuLqCDtkZzspIDtjrjssKg8L3RzcGFuPjx0c3BhbiB4PSIyNzIuOTg0NDk5OTk5OTk5OSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+z4Mg66W8IOyVjOqzoCDsnojripTqsIA/PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IloiIGRhdGEtbGFiZWw9IuKcqCBaLeqygOyglSDsi6Ttlokg4pyoCu2RnOykgOygleq3nOu2hO2PrCDsgqzsmqkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTE0Ljc1MjY2NjY2NjY2NjY0IiB5PSI3NTkuNDA1IiB3aWR0aD0iMTYyLjczMyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTk2LjExOTE2NjY2NjY2NjY0IiB5PSI3ODYuMzA1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxOTYuMTE5MTY2NjY2NjY2NjQiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7inKggWi3qsoDsoJUg7Iuk7ZaJIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjE5Ni4xMTkxNjY2NjY2NjY2NCIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7ZGc7KSA7KCV6rec67aE7Y+sIOyCrOyaqTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDT05EMiIgZGF0YS1sYWJlbD0i7ZGc67O4IO2BrOq4sCBuIOydtAozMCDsnbTsg4HsnLzroZwg7YGw6rCAPyIgZGF0YS1zaGFwZT0iZGlhbW9uZCI+CiAgPHBvbHlnb24gcG9pbnRzPSIzMzkuNDQ5OTk5OTk5OTk5OTMsNDYxLjU1ODk5OTk5OTk5OTk3IDQzMC4yMjI5OTk5OTk5OTk5Niw1NTIuMzMyIDMzOS40NDk5OTk5OTk5OTk5Myw2NDMuMTA1IDI0OC42NzY5OTk5OTk5OTk5NCw1NTIuMzMyIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzMzkuNDQ5OTk5OTk5OTk5OTMiIHk9IjU1Mi4zMzIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjMzOS40NDk5OTk5OTk5OTk5MyIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPu2RnOuzuCDtgazquLAgbiDsnbQ8L3RzcGFuPjx0c3BhbiB4PSIzMzkuNDQ5OTk5OTk5OTk5OTMiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPjMwIOydtOyDgeycvOuhnCDtgbDqsIA/PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlQiIGRhdGEtbGFiZWw9IuKcqCBULeqygOyglSDsi6Ttlokg8J+aqCDinKgK6rys66as6rCAIOuRkOq6vOyatCB0Leu2hO2PrCDsgqzsmqkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzE3Ljg2ODk5OTk5OTk5OTk3IiB5PSI3NTkuNDA1IiB3aWR0aD0iMjAzLjQ4OCIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0MTkuNjEyOTk5OTk5OTk5OTQiIHk9Ijc4Ni4zMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjQxOS42MTI5OTk5OTk5OTk5NCIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuKcqCBULeqygOyglSDsi6Ttlokg8J+aqCDinKg8L3RzcGFuPjx0c3BhbiB4PSI0MTkuNjEyOTk5OTk5OTk5OTQiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuq8rOumrOqwgCDrkZDqurzsmrQgdC3rtoTtj6wg7IKs7JqpPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlQxIiBkYXRhLWxhYmVsPSIxLiDri6jsnbztkZzrs7g6IO2DgOq5gyDqsJLqs7wg67mE6rWQIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjMxNS42NDU5OTk5OTk5OTk5NiIgeT0iODYxLjIwNDk5OTk5OTk5OTkiIHdpZHRoPSIyMDcuOTM0IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDE5LjYxMjk5OTk5OTk5OTk0IiB5PSI4NzkuNjU1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij4xLiDri6jsnbztkZzrs7g6IO2DgOq5gyDqsJLqs7wg67mE6rWQPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJUMiIgZGF0YS1sYWJlbD0iMi4g64+F66a97ZGc67O4OiDrgqggdnMg7JesIO2Pieq3oCDruYTqtZAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg2MS4yMDQ5OTk5OTk5OTk5IiB3aWR0aD0iMjMxLjY0NiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE3MS44MjI5OTk5OTk5OTk5OCIgeT0iODc5LjY1NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Mi4g64+F66a97ZGc67O4OiDrgqggdnMg7JesIO2Pieq3oCDruYTqtZA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlQzIiBkYXRhLWxhYmVsPSIzLiDrjIDsnZHtkZzrs7g6IOyVvSDrs7Xsmqkg7KCEIHZzIO2bhCDwn5KvIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU1MS41Nzk5OTk5OTk5OTk5IiB5PSI4NjEuMjA0OTk5OTk5OTk5OSIgd2lkdGg9IjIzMy44NjkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI2NjguNTE0NDk5OTk5OTk5OSIgeT0iODc5LjY1NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+My4g64yA7J2R7ZGc67O4OiDslb0g67O17JqpIOyghCB2cyDtm4Qg8J+SrzwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] Z-검정 vs T-검정 핵심 조건 및 T-검정 3대 유형 전격 해부 (3단 표)**

이 토픽은 '모분산 앎의 여부'에 따른 분포의 꼬리 두께 차이를 쓰고, 실무 문제에서 툭하면 출제되는 \*\*'T-검정의 3대 세부 유형'\*\*을 명확히 분류해 내는 것이 합격을 굳히는 점수 포인트입니다.

| **핵심 척도**                | **📊 Z-검정 (Z-test) 🚨**                                                                  | **🔑 T-검정 (t-test) 🚨**                                                                                  | **🏁 T-검정 3대 유형 💯**                                                                                                                                                     |
| :----------------------- | :--------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **개념 / 확률분포**            | **'표준정규분포 적용'.** 모집단의 흩어짐(분산)을 명확히 파악하고 있거나 샘플이 충분하여, 가장 완벽한 종 모양 확률분포N(0,1)*N*(0,1)를 씀. | **'t-분포 적용'.** 표본이 부족해서 발생할 오차 한계를 인정하기 위해, **양쪽 꼬리가 정규분포보다 더 넓고 두꺼운(Heavy-tailed) 분포**를 씀.              | **'데이터 수집 구조에 따른 분류'.** 집단이 한 개인지, 무관한 두 개인지, 전/후 짝을 이루는지에 따라 수학 수식이 달라짐.                                                                                                |
| **사용 조건 🚨**             | 1. 모집단의 표준편차(σ*σ*)를 알고 있음. 2. 또는 모른다 해도 표본 크기가 대형일 때 **(n≥30*n*≥30)**.                   | 1. 모집단의 표준편차(σ*σ*)를 전혀 모름. 2. 동시에 표본 크기도 소형일 때 **(n<30*n*<30)**.                                         | t-분포는 표본 개수가 커질수록 자유도(df=n−1*df*=*n*−1)가 증가하여 **결국 Z-분포와 완벽히 똑같아짐.**                                                                                                     |
| **핵심 세부 내용 (출제 포인트) 🚨** | **\[Z-통계량 산출 식]** Z=Xˉ−μ0σ/n*Z*=*σ*/*n*​*X*ˉ−*μ*0​​                                      | **\[t-통계량 산출 식 💯]** t=Xˉ−μ0s/n*t*=*s*/*n*​*X*ˉ−*μ*0​​ (모표준편차 σ*σ* 대신 \*\*표본표준편차 s*s*\*\*를 사용해 불확실성 반영). | **1. \[단일표본 t-검정]** 한 그룹 평균 vs 기준치. **2. \[독립표본 t-test 💯]** 전혀 다른 두 그룹의 평균 차이 (예: A쇼핑몰 vs B쇼핑몰 매출). **3. \[대응표본 t-test 🚨]** 동일 대상의 사전/사후 짝지어진 비교 (예: 교육 전 vs 교육 후 성적). |

#### **IV. \[결론/제언] 3개 이상 집단 검정 시 ANOVA(분산분석)로의 아키텍처 확장**

* **(키워드 위주 2줄 마무리)** "T-검정은 단 '두 개' 집단의 평균 비교에만 가둘 수 있습니다. 만약 비교 대상 집단이 3개 이상(예: 서울, 부산, 대구 지점 매출 비교)으로 늘어난다면, T-검정을 여러 번 돌릴 때 생기는 1종 오류 누적 문제를 피하기 위해 **'분산분석(ANOVA, F-검정)'을 적용하고 사후 검정(Tukey 등)을 연계하여 다차원 의사결정을 수행해야 합니다.**"
