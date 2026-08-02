SCM은 오늘 처음 다루는 주제이니, \*\*"예측이 틀리니까 안전재고가 필요하다"\*\*는 인과관계로 두 파트를 하나의 스토리로 엮겠습니다. 따로 외우면 14개(7+7) 항목이지만, 이렇게 엮으면 훨�다 가볍습니다.

### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (수요예측과 안전재고의 인과관계) — 3~4줄
Ⅱ. 수요예측 7단계 (본론①, 도식 1개)
Ⅲ. 안전재고 산정 (본론②, 계산예시 포함)
Ⅳ. 결론
```

포인트: 개요에서 \*\*"수요예측은 항상 오차(예측오차)를 수반하고, 그 오차에 대비하는 완충장치가 안전재고"\*\*라는 한 줄을 먼저 던지면, 왜 두 주제가 같은 답안에 묶여 나오는지 논리가 섭니다.

### Ⅱ. 수요예측 7단계 — "목·범·기·수·모·검·환" (계획→실행→환류)

| 단계             | 내용                                                     |
| :------------- | :----------------------------------------------------- |
| ① **목적정의**     | 예측 목적(재고관리/생산계획/재무계획 등) 명확화                            |
| ② **범위/수준결정**  | 예측대상(품목/지역/시간단위), 예측기간(단기/중기/장기)                       |
| ③ **기초자료수집**   | 과거 판매데이터, 시장동향, 외부요인(계절성/경쟁사)                          |
| ④ **수요유형 파악**  | 추세(Trend)/계절성(Seasonality)/주기성(Cyclic)/불규칙성(Random) 식별 |
| ⑤ **모델선정/예측**  | 정량기법(시계열, 회귀) + 정성기법(델파이, 시장조사) 선택·적용                  |
| ⑥ **검증(오차분석)** | MAPE, MAD 등으로 예측정확도 측정                                 |
| ⑦ **환류(수정)**   | 실제 판매결과와 비교해 모델 지속 보정                                  |

→ 암기: **"목적 정하고, 범위 잡고, 자료 모으고, 패턴 파악하고, 모델로 예측하고, 검증하고, 고쳐나간다"** — 앞서 다룬 "IT투자분석 절차(계측평환재)"와 마찬가지로 **PDCA 사이클**에 얹으면 새로 외울 게 줄어듭니다.

**+ 정량기법 대표 2가지 (심화)**

| 기법        | 특징                                     |
| :-------- | :------------------------------------- |
| **시계열분석** | 이동평균법, 지수평활법 — 과거 데이터의 패턴 연장           |
| **인과형모델** | 회귀분석 — 수요에 영향을 주는 변수(가격, 광고 등)와의 관계 분석 |

### Ⅲ. 안전재고 산정 — "왜 필요한가 → 어떻게 계산하는가"

**함정 방지: 공식만 던지면 이해 없이 외운 것처럼 보임. "무엇의 불확실성에 대비하는가"부터 짚어야 합니다.**

안전재고가 필요한 이유는 2가지 불확실성 때문입니다:

* **수요의 불확실성**: 예측이 틀려서 실제수요가 예측보다 많을 수 있음
* **조달기간(Lead Time)의 불확실성**: 공급업체 배송이 늦어질 수 있음

**기본 공식 (수요 표준편차 기반)**

```
안전재고 = Z × σd × √L
```

| 변수     | 의미                                           |
| :----- | :------------------------------------------- |
| **Z**  | 서비스수준에 대응하는 표준정규분포 값 (예: 95%→1.65, 99%→2.33) |
| **σd** | 일별 수요의 표준편차                                  |
| **L**  | 조달기간(Lead Time, 일)                           |

→ 암기: **"서비스수준(Z) × 수요변동성(σd) × 조달기간의 제곱근(√L)"** — 조달기간이 길어질수록 불확실성이 누적되니 제곱근으로 증폭된다는 논리를 이해하면 공식이 암기가 아니라 감각으로 남습니다.

**계산 예시 (실전 감각)**

> 일별수요 표준편차(σd)=10개, 조달기간(L)=4일, 서비스수준 95%(Z=1.65)\
> 안전재고 = 1.65 × 10 × √4 = 1.65 × 10 × 2 = **33개**

**조달기간도 불확실한 경우 (심화공식)**

```
안전재고 = Z × √(L×σd² + d²×σL²)
```

| 추가변수   | 의미         |
| :----- | :--------- |
| **d**  | 평균 일별수요    |
| **σL** | 조달기간의 표준편차 |

→ "수요만 불확실한 경우"와 "조달기간도 불확실한 경우"를 구분해서 답하면 훨씬 정교한 답안이 됩니다.

### 도식화 제안

```
[수요예측] → 예측오차(불가피) → [안전재고]로 완충
                                    ↓
                  안전재고 = Z(서비스수준) × σd(수요변동) × √L(조달기간)
                                    ↓
                  서비스수준↑ 또는 변동성↑ 또는 조달기간↑ → 안전재고↑
```

### Ⅳ. 결론 포인트 (차별화 한 줄)

안전재고는 "무조건 많이 쌓아두는 것"이 아니라 **서비스수준(재고부족 허용확률)과 재고보유비용 사이의 트레이드오프**입니다. 서비스수준을 99%→99.9%로 올리면 안전재고는 비례가 아니라 **Z값이 급격히 커지는 비선형 증가**를 보인다는 점 — 앞서 다룬 "IT-ROI"의 비용-효과 트레이드오프 논리와 같은 구조라는 한 줄로 마무리하면 좋습니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "공급망 관리(SCM)의 성패는 결국 '얼마나 팔릴 것인가(수요예측)'와 '만약의 사태에 대비해 창고에 얼마나 더 쌓아둘 것인가(안전재고)'에 달려 있다. 과거처럼 감으로 찍어 맞추던 시대는 끝났다. \*\*목적 설정부터 데이터 수집, 기법 선택, 결과 검증에 이르는 체계적인 '수요예측 7단계 프로세스'\*\*를 밟아야만 오차를 줄일 수 있다. 하지만 아무리 예측을 잘해도 변수(물류 대란, 급작스런 유행)는 발생하기 마련이며, 이때 품절을 막아주는 최후의 보루가 \*\*'안전재고'\*\*다. 이 안전재고는 무턱대고 창고에 많이 쌓아두는 것이 아니라, 기업이 약속한 \*\*서비스 수준(Z값)\*\*과 **수요 변동성(표준편차)**, \*\*조달 기간(리드타임)\*\*을 수학 공식으로 치밀하게 계산해 비용을 최소화하는 확률 게임이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 공급망 최적화의 첫 단추, 수요예측과 안전재고 개요**

* **배경:** 다품종 소량 생산 시대와 글로벌 물류 환경의 불확실성 증가로 인해, 재고 부족(품절)과 과잉 재고(악성 재고)의 딜레마를 해결하는 것이 SCM의 지상 과제가 됨.
* **개념의 관계:** 과학적 \*\*'수요예측'\*\*을 통해 적정 재고의 기준선을 잡고, 예측을 벗어나는 불확실성에 대비하여 통계적으로 산출된 여유분인 \*\*'안전재고'\*\*를 얹어 최종 발주량을 결정.

#### **II. \[본론 1] 데이터 기반의 체계적인 수요예측 7단계 프로세스**

답안지에 프로세스 흐름도(블록 다이어그램)를 그려주면 가시성이 매우 뛰어납니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMzM0LjQ3OCAxMTYuOSIgd2lkdGg9IjEzMzQuNDc4IiBoZWlnaHQ9IjExNi45IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkEiIGRhdGEtdG89IkIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTUxLjYwMzk5OTk5OTk5OTk4LDU4LjQ1IDE5OS42MDM5OTk5OTk5OTk5OCw1OC40NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQiIgZGF0YS10bz0iQyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzNDcuNTE3LDU4LjQ1IDM5NS41MTcsNTguNDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkMiIGRhdGEtdG89IkQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNTU4LjI1LDU4LjQ1IDYwNi4yNSw1OC40NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRCIgZGF0YS10bz0iRSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI3NTQuMTYzLDU4LjQ1IDgwMi4xNjMsNTguNDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkUiIGRhdGEtdG89IkYiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iOTMzLjAzMyw1OC40NSA5ODEuMDMzLDU4LjQ1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJGIiBkYXRhLXRvPSJHIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjEwOTcuMDgzLDU4LjQ1IDExNDUuMDgzLDU4LjQ1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBIiBkYXRhLWxhYmVsPSIxLiDrqqnsoIEg7ISk7KCVIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjExMS42MDM5OTk5OTk5OTk5OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UzZjJmZCIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iOTUuODAxOTk5OTk5OTk5OTkiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij4xLiDrqqnsoIEg7ISk7KCVPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJCIiBkYXRhLWxhYmVsPSIyLiDrjIDsg4Eg7ZKI66qpIOyEoO2DnSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxOTkuNjAzOTk5OTk5OTk5OTgiIHk9IjQwIiB3aWR0aD0iMTQ3LjkxMyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI3My41NjA1IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Mi4g64yA7IOBIO2SiOuqqSDshKDtg508L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkMiIGRhdGEtbGFiZWw9IjMuIOyYiOy4oSDsi5zqsITrjIAg6rKw7KCVIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM5NS41MTciIHk9IjQwIiB3aWR0aD0iMTYyLjczMyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQ3Ni44ODM1IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+My4g7JiI7LihIOyLnOqwhOuMgCDqsrDsoJU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkQiIGRhdGEtbGFiZWw9IjQuIOyYiOy4oSDquLDrspUg7ISg7YOdIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjYwNi4yNSIgeT0iNDAiIHdpZHRoPSIxNDcuOTEzIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjY4MC4yMDY1IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+NC4g7JiI7LihIOq4sOuylSDshKDtg508L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkUiIGRhdGEtbGFiZWw9IjUuIOuNsOydtO2EsCDsiJjsp5EiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iODAyLjE2MyIgeT0iNDAiIHdpZHRoPSIxMzAuODciIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI4NjcuNTk4IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+NS4g642w7J207YSwIOyImOynkTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRiIgZGF0YS1sYWJlbD0iNi4g7JiI7LihIOyImO2WiSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI5ODEuMDMzIiB5PSI0MCIgd2lkdGg9IjExNi4wNSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEwMzkuMDU4IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Ni4g7JiI7LihIOyImO2WiTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRyIgZGF0YS1sYWJlbD0iNy4g6rKw6rO8IOqygOymnS/thrXsoJwiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTE0NS4wODMiIHk9IjQwIiB3aWR0aD0iMTQ5LjM5NDk5OTk5OTk5OTk4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMjE5Ljc4MDUiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij43LiDqsrDqs7wg6rKA7KadL+2GteygnDwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

| **단계**             | **수행 핵심 내용 및 수험용 키워드**                                                                                      |
| :----------------- | :---------------------------------------------------------------------------------------------------------- |
| **1\~3단계** (기획)    | - 예측 결과가 공장 생산용인지, 재무 예산용인지 **'목적'** 명확화 - 예측의 \*\*대상(SKU)\*\*과 **시간대**(단기/중기/장기) 결정                        |
| **4\~5단계** (모델링)   | - 정성적 기법(델파이 기법 등) vs 정량적 기법(시계열 분석, 이동평균법 등) 중 적절한 **예측 모델 선택** - 과거 판매 데이터 및 시장 거시 경제 지표 등 **데이터 수집/전처리** |
| **6\~7단계** (실행/통제) | - 알고리즘을 통한 **실제 예측 수행** - 예측 오차(MAD, MSE, MAPE 등)를 계산하여 **결과를 검증**하고 피드백 적용                                 |

#### **III. \[본론 2] 품절 방어의 최후 보루, 안전재고(Safety Stock) 산정 메커니즘**

* **안전재고의 정의:** 수요의 변동이나 리드타임(조달 기간)의 지연 등 예기치 못한 불확실성으로부터 품절(Stock-out)을 방지하기 위해 추가로 보유하는 재고.
* **안전재고 산정 공식 (시험장 필살기):**
  > **안전재고 (SS) = Z×σ×L*Z*×*σ*×*L*​** *(리드타임은 고정, 수요만 변동할 경우)*
* **공식의 3대 핵심 결정 요인 (이 요소들이 커지면 안전재고도 많이 필요함):**
  1. **Z (목표 서비스 수준):** 회사가 품절을 허용하지 않겠다는 강력한 의지. (예: 99% 서비스 수준을 원하면 Z값 증가 → 안전재고 급증)
  2. **σ*σ*** **(수요의 표준편차):** 과거 판매량 데이터의 들쭉날쭉한 정도. (수요가 불규칙할수록 안전재고 증가)
  3. **L (리드타임):** 발주 후 물건이 창고에 도착하기까지 걸리는 시간. (물류가 느릴수록 불안하므로 안전재고 증가)

#### **IV. \[결론/제언] 채찍효과(Bullwhip Effect) 방지와 AI 기반의 지능형 SCM**

* **(키워드 위주 2줄 마무리)** "잘못된 수요예측과 과도한 안전재고 설정은 공급망을 거슬러 올라갈수록 재고가 눈덩이처럼 불어나는 \*\*'채찍효과(Bullwhip Effect)'\*\*를 유발하여 기업의 현금흐름을 악화시킵니다. 이를 방지하기 위해서는 딥러닝 기반의 AI 예측 모델을 도입하고, 협력사 간에 실시간으로 판매 정보를 공유하는 **CPFR(협력적 기획/예측/보충)** 체계를 구축하는 것이 궁극적인 해결책입니다."
