### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (시계열분석의목표, AR vs MA의근본적차이) — 3~4줄
Ⅱ. AR모형 - 과거값자체를기억 (본론①, 도식 1개 필수)
Ⅲ. MA모형 - 과거의충격을기억, 핵심 배점
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서다룬가설검정,t/z검정은 '독립적인표본들'을전제했는데, 주가나기온같은시계열데이터는 '어제값이오늘값에영향을주는'서로연결된데이터 — AR과MA는 '무엇이과거와현재를연결하는지'에대한 두가지다른답"\*\*이라는 한줄로시작하면, 왜시계열모형이 앞서다룬 \*\*"독립시행전제(이항분포등)"\*\*와 다른차원인지드러납니다.

### Ⅱ. AR모형 — 과거값자체를기억

| 항목          | 내용                                               |
| :---------- | :----------------------------------------------- |
| **핵심발상**    | **"오늘의값은,어제(또는며칠전)의값자체에직접의존한다"**                 |
| **AR(p)공식** | 현재값 = **c + φ₁×(1시점전값) + φ₂×(2시점전값) + ... + 오차** |
| **직관적사례**   | **"오늘기온은어제기온과비슷하다"**— 관성,추세가있는데이터                |

→ 암기: **"오늘값을예측하려면, 과거의실제값들을직접가져다쓴다"** — 앞서다룬 \*\*"의사결정나무의Boosting(이전결과를순차적으로반영)"\*\*과 유사하게, AR도 \*\*"이전시점의실제결과값이,다음시점계산에직접재료로쓰인다"\*\*는 순차적의존구조입니다.

### 도식화 제안

```
[AR(1) 모형 - 어제값이오늘에영향]
Y(오늘) = c + φ×Y(어제) + 오차

예: φ=0.8 이라면
어제기온20도 → 오늘예측기온 = c + 0.8×20 + 오차
(어제값이 크게작용,관성이강한시계열)

[시각화]
어제  오늘  내일
 20 → 18(예측:0.8×20+c) → 16(예측:0.8×18+c)
(과거값이 사슬처럼 다음값에 직접전달됨)
```

### Ⅲ. MA모형 — 과거의충격을기억, 핵심 배점

**함정 방지: "과거값을쓴다"고AR과혼동하면절반. MA는"과거의실제값"이아니라"과거의예측오차(충격)"를 사용한다는 근본적차이를 구체적으로보여줘야완성됩니다.**

| 항목                  | 내용                                                                    |
| :------------------ | :-------------------------------------------------------------------- |
| **핵심발상**(AR과의결정적차이) | **"오늘의값은, 과거의'예측이빗나간정도(오차,충격)'에영향을받는다"**— **과거의값자체가아니라 과거에놀랐던정도**를 기억 |
| **MA(q)공식**         | 현재값 = **평균 + θ₁×(1시점전오차) + θ₂×(2시점전오차) + ... + 현재오차**                 |
| **직관적사례**           | **"어제갑작스러운뉴스(충격)가있었다면, 그여파가오늘조금남아있다"**— 일회성사건의잔향                      |

→ 암기: **"AR은'어제값'을직접가져다쓰고,MA는'어제내가얼마나틀렸는지(오차)'를가져다쓴다"** — 이것이 두모형의 **근본적차이**입니다: AR은 \*\*"관성"\*\*을,MA는 \*\*"충격의잔향(여파)"\*\*을 모델링합니다.

### 도식화 제안

```
[AR vs MA - 근본적차이]

[AR모형] "과거의 실제값"을 기억
어제값(20도) ──직접전달──→ 오늘값예측에반영

[MA모형] "과거의 예측오차(충격)"를 기억
어제예측: 18도 / 어제실제: 25도 → 오차=+7(예상밖충격!)
     ↓ 이"+7의충격"이
오늘값예측에 일부(θ×7만큼) 반영
(실제값20이아니라, "놀랐던정도7"이전달됨)
```

**앞서다룬"랜덤워크,화이트노이즈"와의연결**(구분포인트)

| 구분             | 특징                                                 |
| :------------- | :------------------------------------------------- |
| **AR**         | 과거값의 **가중치(φ)가지속적으로누적**되어, **장기적추세·관성**형성          |
| **MA**         | 특정시점의충격이 **q시점이지나면완전히사라짐**(유한한기억) — **단기적잔향만**     |
| **ARMA**(결합모형) | 실무에서는 **AR과MA를결합**해 \*\*"관성"\*\*과 **"충격의잔향"** 둘다반영 |

→ 암기: **"AR은기억이오래가고(누적),MA는기억이금방사라진다(유한잔향) — 실무에선 둘을합친ARMA를주로쓴다"** — 앞서다룬 \*\*"앙상블(여러모델의장점결합)"\*\*과 유사한 논리로, \*\*ARMA(p,q)\*\*는 \*\*"관성모델링(AR)+충격잔향모델링(MA)"\*\*을 **함께써서** 시계열을 더정교하게예측합니다.

### Ⅳ. 결론

AR모형은 \*\*"과거의실제값자체가현재에직접영향을미치는관성(추세)"\*\*을 모델링하고, MA모형은 **"과거에예측이빗나갔던정도(충격)의여파가현재에남아있는"** 것을 모델링합니다 — 이 근본적차이(실제값 vs 오차값)는 실무에서 **ARMA모형**으로 **결합**되어 함께쓰이며, 이는 앞서다룤 \*\*"앙상블(여러접근의장점을조합)"\*\*과 같은 원리입니다 — 이는 오늘하루다룬 통계학시리즈(중심극한정리→점추정/구간추정→불편추정량→t/z검정→다중공선성→이항/포아송분포→가설검정5단계→AR/MA)전체가, \*\*"독립적인표본"\*\*을전제로한 고전통계학에서 \*\*"시간적으로연결된데이터"\*\*를다루는 시계열분석으로 확장되며, \*\*"세상의데이터는서로독립적이지않고,과거가현재에다양한방식(값자체또는충격의잔향)으로영향을미친다"\*\*는 것을 보여주며 완결됩니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "시간의 흐름에 따라 요동치는 시계열 데이터(주가, 기온 등)의 미래를 예측하는 고전 통계학의 양대 모델이다. 첫째, **'AR 모형(자기회귀)'**. "나의 오늘 모습(Yt*Yt*​)은 어제(Yt−1*Yt*−1​)와 그저께 나의 과거 행동이 쌓인 유산이다"라는 관점이다. 내 과거 실제 값들의 선형 결합으로 현재를 예측하며, 과거의 영향력이 약해질지언정 영구적으로 꼬리를 물고 유입된다. 둘째, **'MA 모형(이동평균)'**. "나의 오늘 모습(Yt*Yt*​)은 어제 발생한 예상치 못한 외부 돌발 충격(오차, ϵt−1*ϵt*−1​)들의 잔상이다"라는 관점이다. 돌발 충격은 특정 시차(q)가 지나면 영향력이 0으로 뚝 끊어지고 소멸한다. 차수를 정하는 핵심 킬러 암기가 \*\*'ACF/PACF 절단 법칙'\*\*이다. **AR은 부분자기상관(PACF)이 시차 p 이후 뚝 끊기고(절단)**, **MA는 자기상관(ACF)이 시차 q 이후 뚝 끊긴다.** 이 둘을 합치고 추세(차분)까지 얹으면 시계열 예측의 왕좌인 \*\*'ARIMA'\*\*가 된다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 시간의 궤적을 설명하는 시계열 모형, AR과 MA 개요**

* **자기회귀(AR: Autoregressive) 정의:** 변수의 현재 시점 값이 과거 자신의 이전 값(시차 값)들에 종속되어 선형적으로 결정된다고 가정하는 시계열 모델.
* **이동평균(MA: Moving Average) 정의:** 변수의 현재 시점 값이 과거에 발생한 무작위 오차(백색 잡음, White Noise)의 가중합으로 구성된다고 가정하는 시계열 모델.
* **공통점:** 둘 다 정상성(Stationarity)을 만족하는 시계열 데이터에만 적용 가능함.

#### **II. \[본론 1] (극단적 단순화 버전) 모델 적합 차수를 결정하는 절단 법칙의 도식**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMTIuNjYxIDM1My44IiB3aWR0aD0iMzEyLjY2MSIgaGVpZ2h0PSIzNTMuOCIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iQVJfdnNfTUFfX19fXyIgZGF0YS1sYWJlbD0iQVIgdnMgTUEg7Iud67OEIOuwjyDssKjsiJgg6rKw7KCVIOq3nOy5mSI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMjMyLjY2MSIgaGVpZ2h0PSIyNzMuOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjIzMi42NjEiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5BUiB2cyBNQSDsi53rs4Qg67CPIOywqOyImCDqsrDsoJUg6rec7LmZPC90ZXh0Pgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IkFSX18iIGRhdGEtbGFiZWw9IkFSICjsnpDquLDtmozqt4ApIOyLneuzhCI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMTYyLjEyOSIgaGVpZ2h0PSI5Ni45IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMTYyLjEyOSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjgiIHk9Ijk4IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPkFSICjsnpDquLDtmozqt4ApIOyLneuzhDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Ik1BX18iIGRhdGEtbGFiZWw9Ik1BICjsnbTrj5ntj4nqt6ApIOyLneuzhCI+CiAgPHJlY3QgeD0iNTYiIHk9IjIwMC45IiB3aWR0aD0iMjAwLjY2MSIgaGVpZ2h0PSI5Ni45IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNTYiIHk9IjIwMC45IiB3aWR0aD0iMjAwLjY2MSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjgiIHk9IjIxNC45IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPk1BICjsnbTrj5ntj4nqt6ApIOyLneuzhDwvdGV4dD4KPC9nPgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBQ0ZfQVIiIGRhdGEtbGFiZWw9IkFDRiDsnpDquLDsg4HqtIAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNzIiIHk9IjEyOCIgd2lkdGg9IjEzMC4xMjkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMzcuMDY0NSIgeT0iMTQ2LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5BQ0Yg7J6Q6riw7IOB6rSAPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQQUNGX01BIiBkYXRhLWxhYmVsPSJQQUNGIOu2gOu2hOyekOq4sOyDgeq0gCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3MiIgeT0iMjQ0LjkiIHdpZHRoPSIxNjguNjYxIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTU2LjMzMDUiIHk9IjI2My4zNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+UEFDRiDrtoDrtoTsnpDquLDsg4HqtIA8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] AR vs MA 수식, 성질 및 융합 ARIMA 모델 전격 해부 (3단 표)**

이 토픽은 두 모델의 \*\*'기본 수식'\*\*과 함께 차수를 결정하는 \*\*'ACF/PACF의 절단 성질'\*\*을 명확히 크로스하여 대조하는 것이 합격 정답의 정석입니다.

| **핵심 척도**                    | **📊 AR 모형 (자기회귀) 🚨**                                                                                                                                         | **🔑 MA 모형 (이동평균) 🚨**                                                                                                                                         | **융합 진화 모형 (ARIMA) 💯**                                                                                                |
| :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| **개념 / 핵심 관점**               | **'내 과거가 나를 지배한다'.** 현재의 상태를 설명하는 변수가 바로 \*\*'나 자신의 과거 관측치'\*\*임. 영향이 점진적으로 길게 전파됨.                                                                            | **'돌발 충격의 잔상이 지배한다 💯'.** 현재의 상태를 요동치게 만드는 것은 \*\*'과거에 맞추지 못한 오차(충격)'\*\*의 가중합임.                                                                               | **'추세와 두 엔진의 대합체'.** 정상성을 가지지 않는 현실 데이터의 추세(Trend)를 해결하고 AR과 MA를 다 섞어버린 끝판왕.                                           |
| **수식 및 절단 성질 (ACF/PACF) 🚨** | **\[AR(p) 공식]** Yt=c+ϕ1Yt−1+...+ϕpYt−p+ϵt*Yt*​=*c*+*ϕ*1​*Yt*−1​+...+*ϕp*​*Yt*−*p*​+*ϵt*​ **\[절단 특성 🚨]** - ACF: 지수적으로 서서히 감소. - **PACF: 시차 p 이후 절단 (0으로 수렴).** | **\[MA(q) 공식]** Yt=μ+ϵt−θ1ϵt−1−...−θqϵt−q*Yt*​=*μ*+*ϵt*​−*θ*1​*ϵt*−1​−...−*θq*​*ϵt*−*q*​ **\[절단 특성 🚨]** - **ACF: 시차 q 이후 절단 (0으로 수렴).** - PACF: 지수적으로 서서히 감소. | **\[ARIMA(p, d, q) 구성 💯]** - **p**: AR 차수 (PACF로 확인). - **d**: 차분(Difference) 횟수 (정상성 확보용). - **q**: MA 차수 (ACF로 확인). |
| **모델의 한계**                   | 시간이 멀어질수록 과거의 기억 영향력(ϕ*ϕ*)이 줄어들지만, 완전히 소멸하기까지 긴 시간 지속됨.                                                                                                        | 충격이 시차 q를 지나는 순간 과거의 에러가 더 이상 현재 값에 일절 관여하지 않고 완전 소멸함.                                                                                                         | 계절성(Seasonality)이 있는 데이터의 경우 ARIMA에 계절 성분을 덧붙인 **SARIMA** 모델로 확장해야 함.                                                  |

#### **IV. \[결론/제언] 딥러닝 시계열(LSTM, GRU) 및 Transformer 기반 예측의 현대화**

* **(키워드 위주 2줄 마무리)** "전통적 통계 기반 ARIMA 계열 모형은 장기 시계열 패턴이나 비선형적 관계를 포착하는 데 수학적 한계가 큽니다. 최근 실무 시계열 예측은 전통 모델을 넘어 문맥의 상관관계를 다차원으로 학습하는 **'LSTM/GRU'나 시계열용 '트랜스포머(예: PatchTST, Patch-based Time Series Transformer)' 모델을 하이브리드로 연동하여 예측 강건성을 확보하는 추세입니다.**"
