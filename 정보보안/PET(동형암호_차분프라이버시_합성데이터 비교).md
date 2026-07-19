### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (PET 정의, 금융보안원 분류체계) — 3~4줄
Ⅱ. 3대 기술 원리 (본론①, 도식 1개 필수)
Ⅲ. 비교 - 원본유지vs통계보존vs완전가짜 (본론②, 핵심 배점)
Ⅳ. 조합전략 및 국내 실증현황
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬동형암호는'암호화된채로연산'하는것이었는데, 개인정보를보호하며데이터를활용하는방법은이것하나만있는게아니다 — 금융보안원은2025년11월,PET를 '개인식별성축소(합성데이터)','파생데이터생성(차분프라이버시,동형암호)','은닉차폐(영지식증명)','데이터분할(연합학습)' 4가지로분류했다"\*\*는한줄로시작하면, 앞서다룬동형암호가 이 큰분류체계중 하나였다는게드러납니다.

### Ⅱ. 3대 기술 원리

| 기술               | 원리                                              |
| :--------------- | :---------------------------------------------- |
| **동형암호**(앞서다룬그것) | 데이터를 **암호화한채로연산**,결과만복호화 — 원본은 **절대노출안됨**       |
| **차분프라이버시**      | 데이터에 **의도적으로노이즈(잡음)를추가**해, 특정개인이포함됐는지알수없게함      |
| **합성데이터**        | **원본과통계적특성은같지만**, 완전히 **새로만들어낸가짜데이터**(개인단위매핑없음) |

→ 암기: **"동형암호는숨기고연산,차분프라이버시는잡음으로흐리고,합성데이터는통째로새로만든다"**

### 도식화 제안

```
[동형암호]              [차분프라이버시]           [합성데이터]
Enc(원본) → 연산           원본+노이즈 → 결과          원본패턴학습 → 가짜데이터생성
   ↓복호화                    ↓                         ↓
원본연산결과와동일         "이사람이포함됐는지         원본과통계는같지만
(원본자체는안보임)          알수없음"(확률적보호)      실제개인은존재안함
```

### Ⅲ. 비교 — 핵심 배점

**함정 방지: "다프라이버시기술"이라고만하면절반. "원본을어떻게다루는가"라는 기준으로 3가지가 완전히 다른 전략이라는걸 보여줘야 완성됩니다.**

| 기준          | **동형암호**                | **차분프라이버시**                   | **합성데이터**               |
| :---------- | :---------------------- | :---------------------------- | :---------------------- |
| **원본존재여부**  | 원본은 **암호화되어존재**(복호화가능)  | 원본은 **존재하되노이즈로흐려짐**           | 원본은 **사라짐**(패턴만추출,새생성)  |
| **정확도**     | **정확**(암호문연산=평문연산과동일)   | **노이즈만큼부정확**(정확도-프라이버시트레이드오프) | 통계적으로유사하나 **개별레코드는다름**  |
| **연산비용**    | **매우무거움**(앞서다룬 전용가속기필요) | **가벼움**(노이즈추가만)               | 생성모델학습비용,이후 **활용은자유로움** |
| **재식별위험**   | 없음(암호화상태)               | **낮음**(수학적보장,ε값으로정량화)         | **낮음**(단,모델이원본을과적합하면위험) |
| **금융보안원분류** | 파생데이터생성                 | 파생데이터생성                       | 개인식별성축소                 |

→ 암기: **"동형암호는정확하지만무겁고,차분프라이버시는가볍지만부정확해지고,합성데이터는자유롭지만원본을얼마나잘흉내냈는지가관건"** — 앞서다룬 \*\*"암호화(대칭/비대칭)"\*\*답안의 \*\*"속도vs안전성"\*\*트레이드오프가, 여기서는 \*\*"정확도vs프라이버시vs비용"\*\*3중트레이드오프로 확장됩니다.

### Ⅳ. 조합전략 및 국내 실증현황

**함정 방지: "하나만골라쓴다"고하면절반. 금융보안원이강조한"기술간조합"이핵심포인트입니다.**

| 프로젝트                     | 내용                                                     |
| :----------------------- | :----------------------------------------------------- |
| **은행권공동FDS모델**(부정거래탐지)   | **연합학습+차분프라이버시**조합 — 각금융사데이터를 **공개하지않고**공동분석           |
| **합성데이터상용화**             | **익명성평가기준**마련중(현행가이드라인상 **익명데이터인정이현실적으로어려움**이라는 실무자지적) |
| **금융보안원핵심메시지**(2025년11월) | **"기술을개별단위로적용하는데집중했으나,기술간조합이중요"**                      |

→ 암기: **"혼자쓰지말고,조합해쓴다"** — 앞서다룬 \*\*"전자봉투(대칭+비대칭키의조합)"\*\*와 같은논리로, PET도 \*\*"연합학습(데이터분할)+차분프라이버시(노이즈)"\*\*처럼 **여러기술을겹쳐서 각자의약점을보완**하는 것이 실무의방향입니다.

### Ⅴ. 결론 포인트

동형암호·차분프라이버시·합성데이터는 \*\*"개인정보를보호하면서데이터를활용한다"\*\*는 같은목표를, **"원본을암호화해숨기거나(동형암호), 잡음으로흐리거나(차분프라이버시), 통째로새로만들거나(합성데이터)"** 서로다른전략으로달성합니다 — 앞서다룬 \*\*PbD의8대전략중"은닉(Hide)"과"집계(Aggregate)"\*\*가 바로 이 3가지기술의철학적뿌리이며, 금융보안원의최신로드맵이보여주듯 \*\*"AI시대데이터활용과프라이버시보호를동시에달성"\*\*하려면 이들을 **단독이아니라조합**해야한다는 것이 2025\~2026년 실무의핵심방향입니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "빅데이터와 AI 시대가 오면서 기업들은 고객의 개인정보를 씹고 뜯고 맛보고 싶어 안달이다. 하지만 원본을 함부로 분석했다간 '개인정보보호법(GDPR 등)' 철퇴를 맞는다. '정보를 철통같이 지키면서도 통계나 AI 학습에 마음껏 써먹을 방법은 없을까?' 이 불가능해 보이는 모순을 해결해 주는 궁극의 마법이 바로 \*\*'PET (Privacy Enhancing Technologies, 프라이버시 강화 기술)'\*\*이다. PET를 이끄는 3대장 무기는 다음과 같다. **① 동형암호:** 금고(암호)에 데이터를 넣고 잠근 상태 그대로, 밖에서 계산기를 두드릴 수 있는 마법이다. 연산 중에도 절대 원본이 노출되지 않지만, 속도가 너무 느린 게 흠이다. **② 차분 프라이버시:** 원본 데이터에 수학적인 가짜 쓰레기 값(노이즈)을 확 섞어버린다. 특정 개인(홍길동)이 누군지는 절대 추적할 수 없게 뭉개버리지만, 전체 통계나 평균값은 원본과 거의 똑같이 유지해 낸다. (애플/구글이 씀). **③ 합성 데이터 (재현 데이터):** 진짜 개인정보는 아예 버리고, AI(GAN 등)를 이용해 원본의 특성과 100% 똑같은 '완벽한 가짜 쌍둥이 데이터'를 창조한다. 진짜 사람이 단 1명도 없으므로 법적 규제에서 완벽하게 자유로워진다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 보호와 활용의 딜레마를 깨부수는 마법, PET 개요**

* **정의:** 개인정보의 노출 위험을 수학적/기술적으로 최소화하면서도, 데이터가 가진 원래의 가치(유용성, 통계, AI 학습 등)를 최대한 안전하게 활용할 수 있도록 지원하는 \*\*'차세대 프라이버시 보호 및 데이터 가공 기술'\*\*의 총칭. (PbD 철학을 구현하는 핵심 기술).
* **등장 배경:** 단순한 '비식별 조치(마스킹 등)'만으로는 다른 데이터와 결합했을 때 특정 개인이 다시 식별되는 재식별화(Re-identification) 공격을 막을 수 없기 때문임.

#### **II. \[본론 1] (단순화 버전) PET 3대장의 각기 다른 개인정보 보호 파이프라인 (도식화)**

각 기술이 원본 데이터를 어떻게 처리하여 안전하게 만드는지 직관적으로 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3MzYuOTY3OTk5OTk5OTk5OCA0NjUuNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSI3MzYuOTY3OTk5OTk5OTk5OCIgaGVpZ2h0PSI0NjUuNzAwMDAwMDAwMDAwMDUiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IlBFVF8zX19fX18iIGRhdGEtbGFiZWw9IlBFVCAz64yA7J6l7J2YIOqwnOyduOygleuztCDrs7TtmLgg67CPIO2ZnOyaqSDrqZTsu6Tri4jsppgiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjY1Ni45Njc5OTk5OTk5OTk4IiBoZWlnaHQ9IjM4NS43MDAwMDAwMDAwMDAwNSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjY1Ni45Njc5OTk5OTk5OTk4IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+UEVUIDPrjIDsnqXsnZgg6rCc7J247KCV67O0IOuztO2YuCDrsI8g7Zmc7JqpIOuplOy7pOuLiOymmDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iT1JHIiBkYXRhLXRvPSJIRSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iMS4g7JWU7Zi47ZmUIOyDge2DnOuhnCDqt7jrg6Ug7Jew7IKw7ZWoIiBwb2ludHM9IjM1NC45NjA3NDk5OTk5OTk5NiwxMzcuOCAzNTQuOTYwNzQ5OTk5OTk5OTYsMjU0LjEwMDAwMDAwMDAwMDAyIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJPUkciIGRhdGEtdG89IkRQIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIyLiDqsIDsp5wg64W47J207KaIKE5vaXNlKeulvCDrk6TsnbTrtoDsnYwiIHBvaW50cz0iMzkxLjkzODk5OTk5OTk5OTk2LDEzNy44IDM5MS45Mzg5OTk5OTk5OTk5NiwxNDkuOCA1ODguMTE1OTk5OTk5OTk5OSwxNDkuOCA1ODguMTE1OTk5OTk5OTk5OSwyNTQuMTAwMDAwMDAwMDAwMDIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209Ik9SRyIgZGF0YS10bz0iU1lOIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIzLiBBSeqwgCDtjKjthLTrp4wg67Kg6ru07IScIOqwgOynnOulvCDrp4zrk6YiIHBvaW50cz0iMzE3Ljk4MjQ5OTk5OTk5OTk2LDEzNy44IDMxNy45ODI0OTk5OTk5OTk5NiwxNDkuOCAxNDguMTExLDE0OS44IDE0OC4xMTEsMjU0LjEwMDAwMDAwMDAwMDAyIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJIRSIgZGF0YS10bz0iUkVTMSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzODAuNTI1MjQ5OTk5OTk5OSwzMDcuOTAwMDAwMDAwMDAwMDMgMzgwLjUyNTI0OTk5OTk5OTksMzU1LjkwMDAwMDAwMDAwMDAzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJEUCIgZGF0YS10bz0iUkVTMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI1ODguMTE1OTk5OTk5OTk5OSwzMDcuOTAwMDAwMDAwMDAwMDMgNTg4LjExNTk5OTk5OTk5OTksMzU1LjkwMDAwMDAwMDAwMDAzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTWU4iIGRhdGEtdG89IlJFUzMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTQ4LjExMSwzMDcuOTAwMDAwMDAwMDAwMDMgMTQ4LjExMSwzNTUuOTAwMDAwMDAwMDAwMDMiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iT1JHIiBkYXRhLXRvPSJIRSIgZGF0YS1sYWJlbD0iMS4g7JWU7Zi47ZmUIOyDge2DnOuhnCDqt7jrg6Ug7Jew7IKw7ZWoIj4KICA8cmVjdCB4PSIyODcuMjQyOTk5OTk5OTk5OTQiIHk9IjE4MC44IiB3aWR0aD0iMTYwLjIxIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzY3LjM0Nzk5OTk5OTk5OTk2IiB5PSIxOTUuOTUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjEuIOyVlO2YuO2ZlCDsg4Htg5zroZwg6re464OlIOyXsOyCsO2VqDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJPUkciIGRhdGEtdG89IkRQIiBkYXRhLWxhYmVsPSIyLiDqsIDsp5wg64W47J207KaIKE5vaXNlKeulvCDrk6TsnbTrtoDsnYwiPgogIDxyZWN0IHg9IjQ5Ni4xMTU5OTk5OTk5OTk5IiB5PSIxODAuOCIgd2lkdGg9IjE4My4zNzYwMDAwMDAwMDAwMyIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjU4Ny44MDM5OTk5OTk5OTk5IiB5PSIxOTUuOTUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjIuIOqwgOynnCDrhbjsnbTspogoTm9pc2Up66W8IOuTpOydtOu2gOydjDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJPUkciIGRhdGEtdG89IlNZTiIgZGF0YS1sYWJlbD0iMy4gQUnqsIAg7Yyo7YS066eMIOuyoOq7tOyEnCDqsIDsp5zrpbwg66eM65OmIj4KICA8cmVjdCB4PSI1NC42MTEwMDAwMDAwMDAwMDQiIHk9IjE4MC44IiB3aWR0aD0iMTg2Ljk0MDAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTQ4LjA4MTAwMDAwMDAwMDAyIiB5PSIxOTUuOTUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjMuIEFJ6rCAIO2MqO2EtOunjCDrsqDqu7TshJwg6rCA7Kec66W8IOunjOuTpjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iT1JHIiBkYXRhLWxhYmVsPSLsm5Drs7gg642w7J207YSwIPCfk4IK6rCc7J247KCV67O0IOqwgOuTne2VqCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyODEuMDA0MjQ5OTk5OTk5OTYiIHk9Ijg0IiB3aWR0aD0iMTQ3LjkxMyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzU0Ljk2MDc0OTk5OTk5OTk2IiB5PSIxMTAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMzU0Ljk2MDc0OTk5OTk5OTk2IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7JuQ67O4IOuNsOydtO2EsCDwn5OCPC90c3Bhbj48dHNwYW4geD0iMzU0Ljk2MDc0OTk5OTk5OTk2IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7qsJzsnbjsoJXrs7Qg6rCA65Od7ZWoPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkhFIiBkYXRhLWxhYmVsPSLrj5ntmJXslZTtmLgg8J+UkgpIb21vbW9ycGhpYyBFbmMiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjkzLjc4NjQ5OTk5OTk5OTkzIiB5PSIyNTQuMTAwMDAwMDAwMDAwMDIiIHdpZHRoPSIxNDcuOTEzIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjM2Ny43NDI5OTk5OTk5OTk5NCIgeT0iMjgxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIzNjcuNzQyOTk5OTk5OTk5OTQiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7rj5ntmJXslZTtmLgg8J+UkjwvdHNwYW4+PHRzcGFuIHg9IjM2Ny43NDI5OTk5OTk5OTk5NCIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+SG9tb21vcnBoaWMgRW5jPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkRQIiBkYXRhLWxhYmVsPSLssKjrtoQg7ZSE65287J2067KE7IucIPCfjKvvuI8KRGlmZmVyZW50aWFsIFByaXZhY3kiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTAxLjkzMjk5OTk5OTk5OTkiIHk9IjI1NC4xMDAwMDAwMDAwMDAwMiIgd2lkdGg9IjE3Mi4zNjU5OTk5OTk5OTk5OSIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI1ODguMTE1OTk5OTk5OTk5OSIgeT0iMjgxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI1ODguMTE1OTk5OTk5OTk5OSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuywqOu2hCDtlITrnbzsnbTrsoTsi5wg8J+Mq++4jzwvdHNwYW4+PHRzcGFuIHg9IjU4OC4xMTU5OTk5OTk5OTk5IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5EaWZmZXJlbnRpYWwgUHJpdmFjeTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTWU4iIGRhdGEtbGFiZWw9Iu2VqeyEsSDrjbDsnbTthLAg8J+klgpTeW50aGV0aWMgRGF0YSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI4MC40NTI5OTk5OTk5OTk5NyIgeT0iMjU0LjEwMDAwMDAwMDAwMDAyIiB3aWR0aD0iMTM1LjMxNiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxNDguMTExIiB5PSIyODEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE0OC4xMTEiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7tlanshLEg642w7J207YSwIPCfpJY8L3RzcGFuPjx0c3BhbiB4PSIxNDguMTExIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5TeW50aGV0aWMgRGF0YTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJSRVMxIiBkYXRhLWxhYmVsPSLqsrDqs7zqsJLrp4wg67O17Zi47ZmUCuuztOyViOyEsSAxMDAlLCDsho3rj4Qg64qQ66a8IPCfkKIiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjgxLjAwNDI0OTk5OTk5OTk2IiB5PSIzNTUuOTAwMDAwMDAwMDAwMDMiIHdpZHRoPSIxOTkuMDQxOTk5OTk5OTk5OTQiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzODAuNTI1MjQ5OTk5OTk5OSIgeT0iMzgyLjgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjM4MC41MjUyNDk5OTk5OTk5IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+6rKw6rO86rCS66eMIOuzte2YuO2ZlDwvdHNwYW4+PHRzcGFuIHg9IjM4MC41MjUyNDk5OTk5OTk5IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rs7TslYjshLEgMTAwJSwg7IaN64+EIOuKkOumvCDwn5CiPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJFUzIiIGRhdGEtbGFiZWw9IuqwnOyduCDsi53rs4Qg7KCI64yAIOu2iOqwgArsoITssrQg7Ya16rOEL+2Pieq3oCDsnKDsp4Ag8J+TiiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0OTUuMjYzOTk5OTk5OTk5OSIgeT0iMzU1LjkwMDAwMDAwMDAwMDAzIiB3aWR0aD0iMTg1LjcwMzk5OTk5OTk5OTk4IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNTg4LjExNTk5OTk5OTk5OTkiIHk9IjM4Mi44IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI1ODguMTE1OTk5OTk5OTk5OSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuqwnOyduCDsi53rs4Qg7KCI64yAIOu2iOqwgDwvdHNwYW4+PHRzcGFuIHg9IjU4OC4xMTU5OTk5OTk5OTk5IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7soITssrQg7Ya16rOEL+2Pieq3oCDsnKDsp4Ag8J+TijwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJSRVMzIiBkYXRhLWxhYmVsPSLsp4Tsp5wg642w7J207YSwIDAlCuuyleyggSDqt5zsoJwg7JmE7KCEIO2ajO2UvCDwn5qAIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIzNTUuOTAwMDAwMDAwMDAwMDMiIHdpZHRoPSIxODQuMjIxOTk5OTk5OTk5OTgiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNDguMTExIiB5PSIzODIuOCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTQ4LjExMSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuynhOynnCDrjbDsnbTthLAgMCU8L3RzcGFuPjx0c3BhbiB4PSIxNDguMTExIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rspXsoIEg6rec7KCcIOyZhOyghCDtmoztlLwg8J+agDwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 차세대 PET 3대 핵심 기술 전격 비교 해부 (3단 표 - 출제 1순위)**

세 기술의 **작동 원리**와 치명적인 \*\*단점(Trade-off)\*\*을 정확히 찌르는 것이 가장 중요합니다.

| **3대 핵심 PET 기술**                                   | **작동 원리 및 보호 메커니즘**                                                                                                                          | **한계점 및 치명적 단점 (Trade-off)**                                                                       |
| :------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- |
| **1. 동형암호 🔒** *(Homomorphic* *Encryption)*        | **'암호를 풀지 않고 그대로 연산한다.'** 평문을 암호화한 상태(금고) 그대로 덧셈이나 곱셈 같은 수학적 연산을 수행함. 그 연산 결과값을 나중에 복호화해서 열어보면 평문 상태로 연산한 결과와 100% 동일함. (클라우드 환경에 최적화됨).     | **'무지막지하게 느린 속도와 리소스'.** 연산을 위해 암호문의 크기가 기하급수적으로 커지므로(오버헤드 발생), 실시간 서비스에 적용하기엔 아직 연산 처리 속도가 너무 느림. |
| **2. 차분 프라이버시 🌫️** *(Differential* *Privacy, DP)* | **'가짜 노이즈를 섞어 특정인을 숨긴다.'** DB에 특정인(홍길동)의 정보가 있든 없든 쿼리(통계) 결과가 거의 같아지도록 수학적인 난수(Noise)를 삽입함. **개인의 식별은 완벽히 차단하면서 '전체 평균/분포'라는 통계적 유용성만 살려냄.** | **'보안과 정확도(유용성)의 반비례'.** 프라이버시를 높이려고 노이즈(입실론 ε 값 조절)를 너무 많이 섞으면, 통계 결과가 원본과 크게 달라져 데이터가 쓸모없어짐.     |
| **3. 합성/재현 데이터 🤖** *(Synthetic Data)*             | **'진짜를 모방한 100% 가짜를 창조한다.'** GAN(적대적 생성 신경망) 같은 AI 딥러닝을 이용해, 원본 DB의 통계적 특성 및 속성 간의 상관관계를 그대로 모방한 완전히 새로운 가상의(Fake) 데이터를 무한대로 찍어냄.            | **'아웃라이어(특이값) 분석 불가'.** 어디까지나 통계 패턴을 베낀 '가짜'이므로, 원본에만 존재하는 희귀한 특이 사례나 미세한 패턴 분석에는 부적합함.            |

#### **IV. \[결론/제언] 단일 기술의 한계 돌파를 위한 '하이브리드 PET' 모델 도입**

* **(키워드 위주 2줄 마무리)** "현재 단일 PET 기술만으로는 '보안성, 처리 속도, 데이터 유용성'이라는 세 마리 토끼를 동시에 잡을 수 없습니다. 다가오는 의료 및 금융 AI 빅데이터 융합 시대에는 데이터의 생성 단계에는 차분 프라이버시를 적용하고 클라우드 처리 단계에는 동형암호를 덧씌우는 **'하이브리드 PET 모델' 도입이 산업 표준으로 자리 잡을 것입니다.**"
