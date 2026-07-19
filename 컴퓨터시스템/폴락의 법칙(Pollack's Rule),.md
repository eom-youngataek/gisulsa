### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (폴락의 법칙 정의, 멀티코어 전환의 배경) — 3~4줄
Ⅱ. 법칙의 수학적 관계 (본론①, 도식 1개 필수)
Ⅲ. 실제 역사적 사례 - 테자스(Tejas) 취소사건 (본론②, 핵심 배점)
Ⅳ. 멀티코어의 해법과 한계(암달의 법칙)
Ⅴ. 결론
```

포인트: 개요에서 \*\*"CPU 코어를 더 크고 복잡하게(트랜지스터 수↑) 만들면 성능이 오르긴 하는데, 그 증가율이 面적 증가율보다 훨씬 못하다 — 이 '수익감소'현상이 인텔 엔지니어 프레드 폴락이 발견한 경험법칙"\*\*이라는 한 줄로 시작하면, 왜 이게 산업의 방향을 바꾼 법칙인지 논리가 섭니다.

### Ⅱ. 법칙의 수학적 관계 — "면적 2배 → 성능 1.4배(√2)"

| 관계         | 수식                                       |
| :--------- | :--------------------------------------- |
| **성능**     | **면적(복잡도) 증가량의 제곱근**에 비례 — 성능 ∝ √(면적)    |
| **전력소모**   | **면적에 선형(1:1)비례** — 전력 ∝ 면적              |
| **역으로 보면** | 성능을 2배로 올리려면, **면적(트랜지스터수)은 4배**(성능²) 필요 |

→ 암기: **"면적을 2배 늘리면 성능은 1.4배(√2)만 늘고, 전력은 그대로 2배 다 든다"** — 즉 **면적투자 대비 성능수익은 갈수록 줄어들지만(제곱근), 전력이라는 비용은 정직하게 그대로(선형) 늘어난다**는 게 이 법칙의 핵심 통찰입니다.

### 도식화 제안

```
면적(트랜지스터수) →  1x    2x    4x
성능              →  1x   1.4x   2x    ← 제곱근으로 완만하게 증가
전력소모           →  1x    2x    4x    ← 선형으로 정직하게 증가

           (면적↑↑↑ 해도 성능은 조금씩만 오르고, 전력만 훨�씬 많이 든다)
```

→ "그래프로 그리면 성능곡선은 완만한 커브(√)로 휘어지지만, 전력곡선은 직선으로 쭉 올라간다"는 게 시각적 핵심입니다 — 면적을 늘릴수록 **"투자 대비 효율이 나빠지는" 수익감소구간**에 들어간다는 뜻입니다.

### Ⅲ. 실제 역사적 사례 — 테자스(Tejas) 취소사건, 핵심 배점

**함정 방지: 이론만 설명하면 절반. 실제로 이 법칙 때문에 산업의 방향이 바뀐 사례를 알아야 완성됩니다.**

인텔은 2005년 출시예정이었던 \*\*싱글코어 CPU '테자스(Tejas)'\*\*를 개발했는데, 이전세대(프레스캇)보다 **다이면적이 1.9배 커졌음에도 성능향상은 겨우 1.38배**에 그쳤습니다(이는 폴락의 법칙이 예측하는 √1.9≈1.38과 거의 정확히 일치). **전력소모는 면적에 비례해 그만큼 늘어나** 발열문제가 심각해졌고, 결국 인텔은 **테자스 출시를 취소**하고 **듀얼코어(펜티엄D/스미스필드)로 전략을 전환**했습니다.

→ "싱글코어를 극한으로 키우는 것보다, 같은 면적에 코어를 여러개 넣는 게 낫다"는 실증적 증거가 된 사건입니다.

### Ⅳ. 멀티코어의 해법과 한계 — 앞서 다룬 RISC-V/암달의 법칙과 연결

**함정 방지: "그래서 멀티코어가 만능해법"이라고 답하면 절반. 멀티코어에도 한계가 있다는 걸 짚어야 완성됩니다.**

| 접근            | 논리                                                                                       |
| :------------ | :--------------------------------------------------------------------------------------- |
| **멀티코어 전략**   | 트랜지스터 **1억개 코어 1개(성능 √배 증가)** 대신, **1억개 코어를 4개** 넣으면 **병렬처리시 최대 4배** 성능 기대 가능(폴락의 법칙 우회) |
| **전제조건(한계)**  | 프로그램이 **여러 코어를 병렬로 활용**할 수 있어야만 유효 — 병렬화 안 되는 작업(순차적 코드)은 코어를 늘려도 소용없음                   |
| **암달의 법칙 연결** | 프로그램 중 **병렬화 불가능한 부분(순차구간)이 전체성능의 상한을 결정** — 코어를 무한히 늘려도 그 순차구간만큼은 절대 빨라지지 않음            |

→ 암기: **"폴락의 법칙(면적↑→성능조금↑)을 피하려고 멀티코어로 갔지만, 이번엔 암달의 법칙(병렬화 안 되는 부분이 발목잡음)이라는 새로운 벽에 부딫힌다"** — 앞서 다룬 "RISC-V" 답안에서 코어수 경쟁(288코어 CPU 등)이 왜 계속되는지, 그리고 그게 왜 만능이 아닌지의 답이 여기 있습니다.

### Ⅴ. 결론 포인트 (오늘 컴퓨터구조 시리즈 대단원 완결)

폴락의 법칙은 \*\*"단일 자원(코어)을 더 크게 만드는 것에는 수익감소(제곱근)의 한계가 있다"\*\*는 걸 수학적으로 증명했고, 이것이 업계전체를 \*\*"하나를 거대하게 vs 여러개를 적당히"\*\*의 갈림길에서 후자(멀티코어)로 이끈 결정적 계기가 되었습니다 — 이는 오늘 하루 다룬 캐시매핑(직접↔완전연관), 세그멘테이션+페이징(혼합), SQMS/MQMS(통합↔분산), CoE(집중↔분산)에서 반복된 \*\*"하나를 극대화하는 것보다, 여러개로 나눠서 병렬화하는 것이 더 합리적인 경우가 많다"\*\*는 오늘 시리즈 전체를 관통하는 최종 설계원리이며, 이 하나의 물리법칙(폴락)이 현대 CPU산업 전체의 방향(멀티코어, 나아가 RISC-V의 모듈형 확장)을 결정했다는 결론으로, 오늘의 방대한 컴퓨터구조 시리즈를 완결할 수 있습니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "과거 인텔은 CPU 칩 하나에 트랜지스터를 무식하게 구겨 넣고 클럭 스피드를 높여 성능을 올리려 했다. 그런데 인텔의 엔지니어 '프레드 폴락'이 충격적인 법칙을 발표한다. '칩의 면적(트랜지스터 수)을 4배나 키워도 성능은 고작 루트 4, 즉 2배밖에 안 오릅니다.' 이것이 바로 \*\*'폴락의 법칙(Pollack's Rule)'\*\*이다. 성능은 제곱근으로 찔끔 오르는데 반해, 전기 먹는 하마인 전력 소모와 발열은 4배 정비례로 솟구치니 CPU가 녹아내리는 '발열 장벽(Power Wall)'에 부딪힌 것이다. 이 법칙은 반도체 업계에 엄청난 패러다임 전환을 가져왔다. 무식하게 거대한 코어 1개를 만들 바엔, 그 면적을 4등분으로 쪼개서 작고 효율적인 코어 4개를 넣는 **'멀티 코어(Multi-Core)'** 아키텍처로 넘어가야 성능을 배수로 올릴 수 있다는 강력한 이론적 근거가 된 것이다. 폴락의 법칙이 싱글 코어의 죽음을 선고한 덕분에 현재의 스마트폰 옥타 코어 시대가 열릴 수 있었다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 단일 코어 미세 공정의 비효율성 경고, 폴락의 법칙 개요**

* **정의:** 인텔의 수석 엔지니어 프레드 폴락(Fred Pollack)이 주창한 법칙으로, \*\*"마이크로프로세서의 성능(Performance) 향상은 칩의 면적(Area) 또는 트랜지스터 로직 복잡도 증가량의 '제곱근(x*x*​)'에 비례한다"\*\*는 하드웨어 아키텍처 경험 법칙.
* **수식:** Performance∝AreaPerformance∝Area​ (칩 면적이 4배 커지면 성능은 44​ 인 2배만 증가)
* **시사점:** 단일 코어(Single Core) 내에서 트랜지스터를 때려 박아 성능을 올리는 것은 가성비가 극악이며, 심각한 \*\*'전력 및 발열 장벽(Power/Thermal Wall)'\*\*을 초래함을 수학적으로 증명함.

#### **II. \[본론 1] 폴락의 딜레마와 멀티 코어(Multi-Core)로의 패러다임 전환 (도식화)**

왜 거대한 1개의 코어보다, 작은 4개의 쿼드코어가 압도적으로 좋은지 보여주는 도식입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMzAxLjMwMiA1MDMuOTQzIiB3aWR0aD0iMTMwMS4zMDIiIGhlaWdodD0iNTAzLjk0MyIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX19fX1NpbmdsZV9Db3JlXzEiIGRhdGEtbGFiZWw9IuqzvOqxsDog66y07Iud7ZWY6rKMIO2CpOyatCDqsbDrjIAgU2luZ2xlIENvcmUgMeqwnCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNTM2LjYyOTk5OTk5OTk5OTkiIGhlaWdodD0iNDIzLjk0MyIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjUzNi42Mjk5OTk5OTk5OTk5IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+6rO86rGwOiDrrLTsi53tlZjqsowg7YKk7Jq0IOqxsOuMgCBTaW5nbGUgQ29yZSAx6rCcPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX19fTXVsdGlDb3JlXzRfXyIgZGF0YS1sYWJlbD0i7ZiE7J6sOiDsnpHqs6Ag7Zqo7Jyo7KCB7J24IE11bHRpLUNvcmUgNOqwnCAo66m07KCBIOu2hO2VoCkiPgogIDxyZWN0IHg9IjYwNC42Mjk5OTk5OTk5OTk5IiB5PSI0MCIgd2lkdGg9IjY1Ni42NzIiIGhlaWdodD0iNDEzLjU2ODk5OTk5OTk5OTk2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNjA0LjYyOTk5OTk5OTk5OTkiIHk9IjQwIiB3aWR0aD0iNjU2LjY3MiIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjE2LjYyOTk5OTk5OTk5OTkiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPu2YhOyerDog7J6R6rOgIO2aqOycqOyggeyduCBNdWx0aS1Db3JlIDTqsJwgKOuptOyggSDrtoTtlaApPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBMSIgZGF0YS10bz0iQjEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjc3LjkzMzk5OTk5OTk5OTk3LDEyMC45IDI3Ny45MzM5OTk5OTk5OTk5NywxNjguOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQjEiIGRhdGEtdG89IkMxIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjI3Ny45MzM5OTk5OTk5OTk5NywzNjMuMDQzIDI3Ny45MzM5OTk5OTk5OTk5NywzODQuNDQ5NSAxNDQuNzc2NSwzODQuNDQ5NSAxNDQuNzc2NSw0MDUuODU2IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJCMSIgZGF0YS10bz0iRDEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjc3LjkzMzk5OTk5OTk5OTk3LDM2My4wNDMgMjc3LjkzMzk5OTk5OTk5OTk3LDM4NC40NDk1IDQxMS4wOTE1LDM4NC40NDk1IDQxMS4wOTE1LDQwNS44NTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkEyIiBkYXRhLXRvPSJCMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI5MzUuOTI5OTk5OTk5OTk5OCwxMjAuOSA5MzUuOTI5OTk5OTk5OTk5OCwxNjguOTAwMDAwMDAwMDAwMTIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkIyIiBkYXRhLXRvPSJDMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI5MzUuOTMsMzUyLjY2OSA5MzUuOTMsMzc5LjI2MjUgNzcyLjc2MiwzNzkuMjYyNSA3NzIuNzYyLDQwNS44NTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkIyIiBkYXRhLXRvPSJEMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI5MzUuOTMsMzUyLjY2OSA5MzUuOTMsMzc5LjI2MjUgMTA5OS4wOTgsMzc5LjI2MjUgMTA5OS4wOTgsNDA1Ljg1NiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQTEiIGRhdGEtbGFiZWw9Iu2KuOuenOyngOyKpO2EsCDroZzsp4Eg66m07KCBIDTrsLAg7Kad6rCAIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjE1OS44ODc5OTk5OTk5OTk5OCIgeT0iODQiIHdpZHRoPSIyMzYuMDkxOTk5OTk5OTk5OTgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyNzcuOTMzOTk5OTk5OTk5OTciIHk9IjEwMi40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7Yq4656c7KeA7Iqk7YSwIOuhnOyngSDrqbTsoIEgNOuwsCDspp3qsIA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkIxIiBkYXRhLWxhYmVsPSLtj7Trnb3snZgg67KV7LmZIOyggeyaqTog4oiaNCIgZGF0YS1zaGFwZT0iZGlhbW9uZCI+CiAgPHBvbHlnb24gcG9pbnRzPSIyNzcuOTMzOTk5OTk5OTk5OTcsMTY4Ljg5OTk5OTk5OTk5OTk4IDM3NS4wMDU1LDI2NS45NzE1IDI3Ny45MzM5OTk5OTk5OTk5NywzNjMuMDQzIDE4MC44NjI0OTk5OTk5OTk5NSwyNjUuOTcxNSIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIyNzcuOTMzOTk5OTk5OTk5OTciIHk9IjI2NS45NzE1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7tj7Trnb3snZgg67KV7LmZIOyggeyaqTog4oiaNDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQzEiIGRhdGEtbGFiZWw9IuyEseuKpeydgCDqsqjsmrAgMuuwsCDtlqXsg4EhIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI0MDUuODU2IiB3aWR0aD0iMTc3LjU1Mjk5OTk5OTk5OTk3IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTQ0Ljc3NjUiIHk9IjQyNC4zMDYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyEseuKpeydgCDqsqjsmrAgMuuwsCDtlqXsg4EhPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJEMSIgZGF0YS1sYWJlbD0i67Cc7Je06rO8IOyghOugpSDshozrqqjripQgNOuwsCDtj63spp0hIChQb3dlciBXYWxsKSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyNjEuNTUzIiB5PSI0MDUuODU2IiB3aWR0aD0iMjk5LjA3NyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQxMS4wOTE1IiB5PSI0MjQuMzA2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7rsJzsl7Tqs7wg7KCE66ClIOyGjOuqqOuKlCA067CwIO2PreymnSEgKFBvd2VyIFdhbGwpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBMiIgZGF0YS1sYWJlbD0i6rGw64yA7ZWcIOuptOyggeydhCA06rCc66GcIOyqvOqwrCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI4MzMuODE1NDk5OTk5OTk5OSIgeT0iODQiIHdpZHRoPSIyMDQuMjI5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iOTM1LjkzIiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuqxsOuMgO2VnCDrqbTsoIHsnYQgNOqwnOuhnCDsqrzqsKw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkIyIiBkYXRhLWxhYmVsPSLsnpHsnYAg7L2U7Ja0IDTqsJwg7YOR7J6sCihRdWFkLUNvcmUpIiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjkzNS45MywxNjguODk5OTk5OTk5OTk5OTggMTAyNy44MTQ1LDI2MC43ODQ1IDkzNS45MywzNTIuNjY5IDg0NC4wNDU1LDI2MC43ODQ1IiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjkzNS45MyIgeT0iMjYwLjc4NDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjkzNS45MyIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuyekeydgCDsvZTslrQgNOqwnCDtg5Hsnqw8L3RzcGFuPjx0c3BhbiB4PSI5MzUuOTMiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPihRdWFkLUNvcmUpPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkMyIiBkYXRhLWxhYmVsPSLsnbTroaDsg4EgMeuwsCDshLHriqUgKiA06rCcID0g7LSdIDTrsLAg7ISx64qlIO2WpeyDgSDwn5qAIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjYyMC42Mjk5OTk5OTk5OTk5IiB5PSI0MDUuODU2IiB3aWR0aD0iMzA0LjI2NCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9Ijc3Mi43NjIiIHk9IjQyNC4zMDYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuydtOuhoOyDgSAx67CwIOyEseuKpSAqIDTqsJwgPSDstJ0gNOuwsCDshLHriqUg7Zal7IOBIPCfmoA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkQyIiBkYXRhLWxhYmVsPSLsoITroKXqs7wg67Cc7Je07J2EIOqwgSDsvZTslrTroZwg67aE7IKwIO2GteygnCDqsIDriqUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iOTUyLjg5Mzk5OTk5OTk5OTkiIHk9IjQwNS44NTYiIHdpZHRoPSIyOTIuNDA4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTA5OS4wOTgiIHk9IjQyNC4zMDYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyghOugpeqzvCDrsJzsl7TsnYQg6rCBIOy9lOyWtOuhnCDrtoTsgrAg7Ya17KCcIOqwgOuKpTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMDY2LjA0NDUiIHk9Ijg0IiB3aWR0aD0iNjguNjI2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTEwMC4zNTc1IiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk5vdGU8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 폴락의 법칙이 가져온 아키텍처 패러다임 전격 비교표 (출제 포인트)**

하드웨어 설계 사상이 어떻게 바뀌었는지를 대조합니다.

| **패러다임 비교**    | **과거 (폴락의 법칙 이전)**                                   | **현대 (폴락의 법칙 이후)**                                              |
| :------------- | :--------------------------------------------------- | :-------------------------------------------------------------- |
| **코어 설계 전략**   | **단일 코어(Single Core) 집중 설계** 복잡한 파이프라이닝, 거대한 캐시 탑재   | **멀티 코어(Multi-Core) / 매니 코어** 단순하고 효율적인 여러 개의 코어 병렬 배치          |
| **성능 향상 타겟**   | 코어 1개의 **동작 클럭(Clock Speed, GHz)을 미친 듯이 극한으로 끌어올림.** | 클럭 향상을 포기하고, 다수 코어의 **동시 병렬 처리(Thread-Level Parallelism)에 집중.** |
| **직면한 물리적 한계** | 전력 소모가 면적에 정비례하여 폭증하는 **Power Wall (전력 장벽) 발생**      | 코어가 늘어날수록 소프트웨어 병렬화가 어려워지는 **암달의 법칙(Amdahl's Law)에 부딪힘.**       |
| **대표적 아키텍처**   | 과거 인텔 펜티엄 4 (프레스캇 등 발열 심각)                           | 현재 스마트폰 ARM big.LITTLE, 인텔 코어 i7 등                              |

#### **IV. \[결론/제언] 암달의 법칙(Amdahl's Law) 한계와 이기종(Heterogeneous) 코어로의 진화**

* **(키워드 위주 2줄 마무리)** "폴락의 법칙을 피해 멀티 코어로 넘어왔으나, 무작정 코어 수를 늘린다고 성능이 선형적으로 오르지 않는다는 소프트웨어 병렬화의 한계인 \*\*'암달의 법칙(Amdahl's Law)'\*\*에 다시 직면하게 되었습니다. 이를 극복하기 위해 최신 반도체 아키텍처는 똑같은 코어만 늘리는 동종 멀티코어를 넘어, CPU와 GPU, NPU(신경망처리장치) 등 서로 다른 특수 목적의 코어를 한 칩에 결합하여 연산 효율을 극대화하는 **'이기종(Heterogeneous) 아키텍처'** 시대로 완전히 진화하였습니다."
