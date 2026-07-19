### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (CBAM 정의, ATAM과의관계) — 3~4줄
Ⅱ. CBAM 핵심요소 (본론①, 도식 1개 필수)
Ⅲ. CBAM 절차 (본론②, 핵심 배점)
Ⅳ. ATAM과의 통합관계
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬여러아키텍처패턴(MSA,헥사고날등)은 '기술적트레이드오프'(성능↔복잡도등)를다루는데, 실제조직은 '이아키텍처전략에투자할돈이있는가,ROI가나오는가'라는경제적질문에도답해야한다 → ATAM이기술적트레이드오프를분석했다면,CBAM은그위에비용·효익·일정을더해 경제적의사결정을돕는기법"\*\*이라는한줄로시작하면, 왜"ATAM 다음에CBAM"인지논리가섭니다.

### Ⅱ. CBAM 핵심요소 — "전·비·편·위"

| 요소                      | 내용                                   |
| :---------------------- | :----------------------------------- |
| **아키텍처전략(AS)**          | 비교대상이되는 **여러설계대안**(예:MSA로전환 vs 현행유지) |
| **비용(Cost)**            | 각전략을실행하는데 **드는투자금액**                 |
| **편익(Benefit/Utility)** | 각전략이 **품질속성(성능,가용성등)에주는효용**          |
| **위험/불확실성**             | 편익추정치의 **신뢰도범위**(최선/보통/최악시나리오)       |

→ 암기: **"전략을세우고,비용얼마들지,편익얼마인지,불확실성까지고려한다"** — 앞서다룬"리스크관리답안"의 확률·영향평가가, 여기서는 **경제적수치(ROI)로환산**된다는연결이핵심입니다.

### 도식화 제안

```
[비즈니스목표] → [품질속성시나리오] ← (ATAM에서가져온입력)
       ↓
[아키텍처전략(AS) 후보들 도출]
       ↓
   ┌───┴───┐
[전략A]      [전략B]
비용:5억      비용:3억
편익:80점     편익:50점
       ↓
   [ROI 계산] = 편익/비용
       ↓
[가장ROI높은전략선택]
```

### Ⅲ. CBAM 절차 — 핵심 배점

**함정 방지: "비용대편익을계산한다"고만답하면절반. 정확한단계순서와 "효용-반응곡선"이라는핵심도구를보여줘야완성됩니다.**

| 단계                                       | 내용                                               |
| :--------------------------------------- | :----------------------------------------------- |
| ① 시나리오정리                                 | ATAM에서도출된 **품질속성시나리오**(성능,가용성등)정리                |
| ② 시나리오정제·우선순위화                           | 비즈니스임팩트기준으로 **투표/순위화**                           |
| ③ **효용-반응곡선(Utility-Response Curve)** 작성 | 각시나리오에서 **응답수준별효용을곡선으로표현**(예:응답시간이 몇ms일때효용이몇점인지) |
| ④ 아키텍처전략도출                               | 시나리오를충족시킬 **구체적설계전략**후보나열                        |
| ⑤ 전략별비용·편익·일정산정                          | 각전략의 **투자비용,기대편익,구현기간**추정                        |
| ⑥ ROI계산                                  | **편익/비용**비율로전략간 **투자효율성비교**                      |
| ⑦ 최종검토·결정                                | 계산결과를 **경험·직관으로재검토**후최종선택                        |

→ 암기: **"시나리오정하고,순위매기고,효용곡선그리고,전략뽑고,비용편익매기고,ROI계산하고,직관으로검증한다"** — 특히 \*\*"효용-반응곡선"\*\*이 CBAM의 가장독창적인도구입니다: 예를들어 "응답시간이1초일때효용90점,3초일때효용40점"처럼, **정성적품질속성을정량화된효용값으로변환**하는장치입니다.

### Ⅳ. ATAM과의 통합관계 — 변별력 포인트

**함정 방지: ATAM과CBAM을같은것으로혼동하면감점. "정성적트레이드오프분석"과 "정량적비용효익분석"이순서대로이어지는 관계임을보여줘야완성됩니다.**

| 구분     | **ATAM**(Architecture Trade-off Analysis Method) | **CBAM**(Cost Benefit Analysis Method) |
| :----- | :----------------------------------------------- | :------------------------------------- |
| **목적** | 아키텍처결정이 **품질속성간트레이드오프**에미치는영향분석(정성적)             | 그트레이드오프를 **비용·편익·ROI로정량화**해투자결정지원      |
| **출력** | 민감점,트레이드오프점,위험 목록                                | 전략별 **ROI수치**, 우선순위화된투자계획              |
| **순서** | **선행**(먼저기술적트레이드오프파악)                            | **후행**(ATAM결과를입력받아경제성분석)               |

→ 암기: **"ATAM은'어떤기술적선택이있고 무엇이상충하는가'를보여주고,CBAM은'그중어느것에투자하는게경제적으로남는가'를계산한다"** — 앞서다룬 "IT-ROI/IT투자평가"답안의 \*\*정량기법(ROI,NPV)\*\*이, 소프트웨어아키텍처라는특정영역에 적용된 구체적사례가바로CBAM입니다.

### Ⅴ. 결론 포인트 (아키텍처+투자평가 시리즈 완결)

CBAM의본질은 \*\*"아키텍처결정도결국투자결정이며, 기술적으로우아한선택이아니라경제적으로타당한선택을체계적으로찾아내는것"\*\*입니다 — 이는 앞서다룬 "IT-ROI/IT투자평가"의방법론이 **아키텍처설계라는구체적영역에특화되어재현된것**이며, 오늘하루다룬 CBD→MSA→헥사고날→GoF패턴→결합도/응집도→AOP까지의 \*\*"기술적으로좋은설계"\*\*논의가, CBAM을통해 마지막으로 \*\*"그래서이게돈값을하는가"\*\*라는경영진의질문에답하는단계로 완결됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "개발자들은 종종 '완벽한 기술적 아키텍처'에 집착한다. 해킹을 100% 막아내는 엄청난 보안 아키텍처를 설계하고 뿌듯해하지만, 사장님(투자자)은 차갑게 묻는다. '그 아키텍처 구축하는 데 100억이 들고, 해킹 막아서 우리가 아끼는 돈은 1억인데 이걸 왜 합니까?' 이처럼 기술적인 품질 속성(ATAM)만 따지다가 비즈니스적 타당성을 무시하여 프로젝트가 산으로 가는 것을 막기 위해 등장한 모델이 바로 \*\*'CBAM(비용-효익 분석 모델)'\*\*이다. CBAM은 개발자의 기술적 언어를 사장님의 언어, 즉 \*\*'돈과 투자 가치(경제성)'\*\*로 번역해 주는 통역기다. 과정은 명확하다. 먼저 A, B, C라는 여러 아키텍처 전략 대안들을 펼쳐놓는다. 그리고 각 전략을 도입했을 때 시스템 성능이 좋아져서 비즈니스적으로 얻게 되는 \*\*'효익(Benefit, Utility)'\*\*을 점수로 환산한다. 다음으로 그 전략을 개발하는 데 드는 \*\*'비용(Cost)'\*\*을 뽑아낸다. 마지막으로 효익을 비용으로 나누어 \*\*'ROI(투자 대비 수익률)'\*\*를 계산한다. 아무리 보안성이 세계 1위라도 개발 비용이 너무 비싸 ROI가 바닥을 친다면 그 아키텍처는 가차 없이 기각된다. 결국 CBAM은 제한된 예산 속에서 비즈니스 가치를 극대화하는 '가성비 1등 아키텍처'를 선택하는 경제적 평가의 교과서다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 기술의 언어를 '돈(경제성)'의 언어로 번역하다, CBAM 개요**

* **정의:** 카네기멜론 대학교 소프트웨어 공학 연구소(SEI)에서 개발한, 여러 아키텍처 설계 대안들에 대해 **비용(Cost)과 효익(Benefit)을 정량적으로 산정하여 경제적 관점에서 최적의 아키텍처를 선택하는 평가 방법론**.
* **등장 배경 및 목적:** 기존의 ATAM(Architecture Trade-off Analysis Method)은 아키텍처가 품질 속성(보안성, 성능 등)을 잘 만족하는지 \*\*'기술적 관점'\*\*에서만 평가했음. 하지만 기업은 예산이 한정되어 있으므로, 품질 향상 대비 돈이 얼마나 드는지 **'경제적 타당성(ROI)' 기반의 비즈니스 의사결정**을 지원하기 위해 등장함.

#### **II. \[본론 1] 최적의 가성비를 찾는 CBAM의 의사결정 메커니즘 (도식화)**

기술적 평가(ATAM)가 끝난 후, 돈(ROI)으로 아키텍처를 컷팅하는 과정입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2OTcuNjk0OTk5OTk5OTk5OSA5NzguMTg5IiB3aWR0aD0iNjk3LjY5NDk5OTk5OTk5OTkiIGhlaWdodD0iOTc4LjE4OSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX19fIiBkYXRhLWxhYmVsPSLslYTtgqTthY3sspgg7Y+J6rCA7J2YIOyDge2YuOuztOyZhOyggSDtjIzsnbTtlITrnbzsnbgiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjYxNy42OTQ5OTk5OTk5OTk5IiBoZWlnaHQ9Ijg5OC4xODkiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI2MTcuNjk0OTk5OTk5OTk5OSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPuyVhO2CpO2FjeyymCDtj4nqsIDsnZgg7IOB7Zi467O07JmE7KCBIO2MjOydtO2UhOudvOyduDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQSIgZGF0YS10bz0iQiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzNTYuMDMwNzQ5OTk5OTk5OTUsMTYzLjE0OTk5OTk5OTk5OTk4IDM1Ni4wMzA3NDk5OTk5OTk5NSwyMDIuNyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQiIgZGF0YS10bz0iUzEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzU2LjAzMDc0OTk5OTk5OTk1LDQ3NS4zODg5OTk5OTk5OTk5NSAzNTYuMDMwNzQ5OTk5OTk5OTUsNDk5LjM4ODk5OTk5OTk5OTkgNTQ5LjU4NCw0OTkuMzg4OTk5OTk5OTk5OSA1NDkuNTg0LDUyMy4zODg5OTk5OTk5OTk5IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJCIiBkYXRhLXRvPSJTMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzNTYuMDMwNzQ5OTk5OTk5OTUsNDc1LjM4ODk5OTk5OTk5OTk1IDM1Ni4wMzA3NDk5OTk5OTk5NSw0OTkuMzg4OTk5OTk5OTk5OSAzMzguODQzOTk5OTk5OTk5OTQsNDk5LjM4ODk5OTk5OTk5OTkgMzM4Ljg0Mzk5OTk5OTk5OTk0LDUyMy4zODg5OTk5OTk5OTk5IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJCIiBkYXRhLXRvPSJTMyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzNTYuMDMwNzQ5OTk5OTk5OTUsNDc1LjM4ODk5OTk5OTk5OTk1IDM1Ni4wMzA3NDk5OTk5OTk5NSw0OTkuMzg4OTk5OTk5OTk5OSAxMzguMTA3NSw0OTkuMzg4OTk5OTk5OTk5OSAxMzguMTA3NSw1MjMuMzg4OTk5OTk5OTk5OSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUzEiIGRhdGEtdG89IkMxIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iUk9JID0gMyIgcG9pbnRzPSI1NDkuNTg0LDU3Ny4xODkgNTQ5LjU4NCw2NjkuNDg4OTk5OTk5OTk5OSAzNDQuNDgwMzc1LDY2OS40ODg5OTk5OTk5OTk5IDM0NC40ODAzNzUsNjkzLjQ4ODk5OTk5OTk5OTkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUzIiIGRhdGEtdG89IkMxIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iUk9JID0gMTAiIHBvaW50cz0iMzM4Ljg0NCw1NzcuMTg5IDMzOC44NDM5OTk5OTk5OTk5NCw2NTcuNDg4OTk5OTk5OTk5OSAzMTYuOTgwMzc1LDY1Ny40ODg5OTk5OTk5OTk5IDMxNi45ODAzNzUsNjkzLjQ4ODk5OTk5OTk5OTkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUzMiIGRhdGEtdG89IkMxIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iUk9JID0gMC40IiBwb2ludHM9IjEzOC4xMDc1LDU3Ny4xODkgMTM4LjEwNzQ5OTk5OTk5OTk2LDY1Ny40ODg5OTk5OTk5OTk5IDI4OS40ODAzNzUsNjU3LjQ4ODk5OTk5OTk5OTkgMjg5LjQ4MDM3NSw2OTMuNDg4OTk5OTk5OTk5OSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDMSIgZGF0YS10bz0iRklOQUwiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzE2Ljk4MDM3NSw4MDMuNDg4OTk5OTk5OTk5OSAzMTYuOTgwMzc1LDg1MS40ODg5OTk5OTk5OTk5IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlMxIiBkYXRhLXRvPSJDMSIgZGF0YS1sYWJlbD0iUk9JID0gMyI+CiAgPHJlY3QgeD0iNTI0LjU4Mzk5OTk5OTk5OTgiIHk9IjYyMC4xODkiIHdpZHRoPSI0OS43MjYiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1NDkuNDQ2OTk5OTk5OTk5OSIgeT0iNjM1LjMzODk5OTk5OTk5OTkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPlJPSSA9IDM8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iUzIiIGRhdGEtdG89IkMxIiBkYXRhLWxhYmVsPSJST0kgPSAxMCI+CiAgPHJlY3QgeD0iMzEyLjM0Mzk5OTk5OTk5OTk0IiB5PSI2MjAuMTg5IiB3aWR0aD0iNTIuMTAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzM4LjM5NDk5OTk5OTk5OTkiIHk9IjYzNS4zMzg5OTk5OTk5OTk5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5ST0kgPSAxMDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJTMyIgZGF0YS10bz0iQzEiIGRhdGEtbGFiZWw9IlJPSSA9IDAuNCI+CiAgPHJlY3QgeD0iMTA4LjYwNzQ5OTk5OTk5OTk3IiB5PSI2MjAuMTg5IiB3aWR0aD0iNTguMDQyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTM3LjYyODQ5OTk5OTk5OTk3IiB5PSI2MzUuMzM4OTk5OTk5OTk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+Uk9JID0gMC40PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBIiBkYXRhLWxhYmVsPSJBVEFNIOq4sOyIoCDtj4nqsIAg8J+boO+4jwrshLHriqUsIOuztOyViCDrk7Eg7ZKI7KeIIOyGjeyEseydhCDrp4zsobHtlZjripQK7JWE7YKk7YWN7LKYIOuMgOyViCDsi5zrgpjrpqzsmKTrk6Qg64+E7LacIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjIyNC4yNzYyNDk5OTk5OTk5NSIgeT0iOTIuNDUiIHdpZHRoPSIyNjMuNTA5IiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzU2LjAzMDc0OTk5OTk5OTk1IiB5PSIxMjcuODAwMDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjM1Ni4wMzA3NDk5OTk5OTk5NSIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPkFUQU0g6riw7IigIO2PieqwgCDwn5ug77iPPC90c3Bhbj48dHNwYW4geD0iMzU2LjAzMDc0OTk5OTk5OTk1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7shLHriqUsIOuztOyViCDrk7Eg7ZKI7KeIIOyGjeyEseydhCDrp4zsobHtlZjripQ8L3RzcGFuPjx0c3BhbiB4PSIzNTYuMDMwNzQ5OTk5OTk5OTUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyVhO2CpO2FjeyymCDrjIDslYgg7Iuc64KY66as7Jik65OkIOuPhOy2nDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJCIiBkYXRhLWxhYmVsPSJDQkFNIOqyveygnOyEsSDtj4nqsIAg8J+SsArrj4TstpzrkJwg64yA7JWI65Ok7J20IOuPiOqwkuydhCDtlZjripTqsIA/IiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjM1Ni4wMzA3NDk5OTk5OTk5NSwyMDIuNyA0OTIuMzc1MjQ5OTk5OTk5OTQsMzM5LjA0NDQ5OTk5OTk5OTk3IDM1Ni4wMzA3NDk5OTk5OTk5NSw0NzUuMzg4OTk5OTk5OTk5OTUgMjE5LjY4NjI0OTk5OTk5OTk3LDMzOS4wNDQ0OTk5OTk5OTk5NyIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIzNTYuMDMwNzQ5OTk5OTk5OTUiIHk9IjMzOS4wNDQ0OTk5OTk5OTk5NyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMzU2LjAzMDc0OTk5OTk5OTk1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+Q0JBTSDqsr3soJzshLEg7Y+J6rCAIPCfkrA8L3RzcGFuPjx0c3BhbiB4PSIzNTYuMDMwNzQ5OTk5OTk5OTUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuuPhOy2nOuQnCDrjIDslYjrk6TsnbQg64+I6rCS7J2EIO2VmOuKlOqwgD88L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzEiIGRhdGEtbGFiZWw9IuyghOuetSBBOiDqs6DshLHriqUgREIg64+E7J6FCuu5hOyaqTogMeyWtSAvIO2aqOydtTogM+yWtSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0NTcuNDcyOTk5OTk5OTk5OTYiIHk9IjUyMy4zODg5OTk5OTk5OTk5IiB3aWR0aD0iMTg0LjIyMTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNTQ5LjU4NCIgeT0iNTUwLjI4ODk5OTk5OTk5OTkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjU0OS41ODQiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7soITrnrUgQTog6rOg7ISx64qlIERCIOuPhOyehTwvdHNwYW4+PHRzcGFuIHg9IjU0OS41ODQiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuu5hOyaqTogMeyWtSAvIO2aqOydtTogM+yWtTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTMiIgZGF0YS1sYWJlbD0i7KCE6561IEI6IOy6kOyLnCDshJzrsoQg7LaU6rCACuu5hOyaqTogMeyynOunjCAvIO2aqOydtTogMeyWtSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyNDguMjE0OTk5OTk5OTk5OTciIHk9IjUyMy4zODg5OTk5OTk5OTk5IiB3aWR0aD0iMTgxLjI1Nzk5OTk5OTk5OTk4IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzMzguODQzOTk5OTk5OTk5OTQiIHk9IjU1MC4yODg5OTk5OTk5OTk5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIzMzguODQzOTk5OTk5OTk5OTQiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7soITrnrUgQjog7LqQ7IucIOyEnOuyhCDstpTqsIA8L3RzcGFuPjx0c3BhbiB4PSIzMzguODQzOTk5OTk5OTk5OTQiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuu5hOyaqTogMeyynOunjCAvIO2aqOydtTogMeyWtTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTMyIgZGF0YS1sYWJlbD0i7KCE6561IEM6IDPspJHtmZQg67Cx7JeFCuu5hOyaqTogNeyWtSAvIO2aqOydtTogMuyWtSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iNTIzLjM4ODk5OTk5OTk5OTkiIHdpZHRoPSIxNjQuMjE0OTk5OTk5OTk5OTciIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMzguMTA3NSIgeT0iNTUwLjI4ODk5OTk5OTk5OTkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjEzOC4xMDc1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7KCE6561IEM6IDPspJHtmZQg67Cx7JeFPC90c3Bhbj48dHNwYW4geD0iMTM4LjEwNzUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuu5hOyaqTogNeyWtSAvIO2aqOydtTogMuyWtTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDMSIgZGF0YS1sYWJlbD0iUk9JIOyCsOyglSIgZGF0YS1zaGFwZT0iY2lyY2xlIj4KICA8Y2lyY2xlIGN4PSIzMTYuOTgwMzc1IiBjeT0iNzQ4LjQ4ODk5OTk5OTk5OTkiIHI9IjU1IiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzE2Ljk4MDM3NSIgeT0iNzQ4LjQ4ODk5OTk5OTk5OTkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlJPSSDsgrDsoJU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkZJTkFMIiBkYXRhLWxhYmVsPSLwn4+GIOy1nOyihSDshKDtg506IOyghOuetSBCCuuztOyViC/shLHriqUo7KCE6561IEMsQSnsnbQg7LWc6rOg64qUIOyVhOuLiOyngOunjArqsIDsnqUg64aS7J2AIFJPSSjqsIDshLHruYQp66W8IOygnOqzte2VqCEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTcyLjk5OTM3NSIgeT0iODUxLjQ4ODk5OTk5OTk5OTkiIHdpZHRoPSIyODcuOTYyIiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIzMTYuOTgwMzc1IiB5PSI4ODYuODM4OTk5OTk5OTk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMzE2Ljk4MDM3NSIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPvCfj4Yg7LWc7KKFIOyEoO2DnTog7KCE6561IEI8L3RzcGFuPjx0c3BhbiB4PSIzMTYuOTgwMzc1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rs7TslYgv7ISx64qlKOyghOuetSBDLEEp7J20IOy1nOqzoOuKlCDslYTri4jsp4Drp4w8L3RzcGFuPjx0c3BhbiB4PSIzMTYuOTgwMzc1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7qsIDsnqUg64aS7J2AIFJPSSjqsIDshLHruYQp66W8IOygnOqzte2VqCE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1MTUuNzg1MjQ5OTk5OTk5OSIgeT0iOTIuNDUiIHdpZHRoPSI2OC42MjYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1NTAuMDk4MjQ5OTk5OTk5OSIgeT0iMTEwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk5vdGU8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] CBAM 아키텍처 경제성 평가 6단계 프로세스 (3단 표 - 출제 1순위)**

단순히 비용만 뽑는 게 아니라, 보이지 않는 효익(Utility)을 정량화하는 절차입니다.

| **평가 단계 프로세스**                             | **수행하는 핵심 역할 (What)**                                                             | **산출물 및 특징 (How)**                           |
| :----------------------------------------- | :-------------------------------------------------------------------------------- | :------------------------------------------- |
| **1. 시나리오 정제** *(Collate Scenarios)*       | 이전 단계(ATAM 등)에서 도출된 수많은 아키텍처 시나리오 중, 비즈니스 목적에 부합하는 **상위 1/3의 핵심 시나리오만 1차로 필터링함.** | 핵심 비즈니스 시나리오 리스트 도출. (쓸데없는 평가 시간 낭비 방지).     |
| **2. 효익(Utility) 산정** *(Refine & Utility)* | 1단계에서 뽑힌 시나리오들이 시스템에 기여할 경우 뿜어내는 **'효익(기대 가치)'을 이해관계자들이 투표하여 정량적인 점수로 환산함.**      | 예: 응답속도 1초 단축 = 효익 80점, 보안성 1단계 상승 = 효익 40점. |
| **3. 아키텍처 전략 수립** *(Develop Strategies)*   | 해당 시나리오(목표)를 실제로 달성하기 위한 구체적인 **기술적 해결책(아키텍처 대안 전략)들을 마련함.**                      | 전략 A: 서버 이중화 구성 전략 B: 분산 캐시 아키텍처 도입          |
| **4. 전략별 효익 결정** *(Determine Utility)*     | 3단계에서 만든 '기술 전략'을 적용했을 때, **전체 시스템의 효익 점수가 얼마나 상승할 것인지 최종 결정함.**                  | 전략 A 도입 시 ➔ 총 효익 120점 전략 B 도입 시 ➔ 총 효익 150점  |
| **5. 비용/일정 산정** *(Determine Cost)*         | 각 아키텍처 전략을 실제 소프트웨어로 구현하고 도입하는 데 **투입되어야 할 비용(Cost)과 소요 일정을 추정함.**                | 아키텍처 엔지니어의 경험 기반 산정 (소프트웨어 규모 산정 기법 활용).     |
| **6. ROI 계산 및 선정** *(Calculate ROI)*       | **"ROI = 전략 도입으로 인한 효익 상승분 / 전략 도입 비용"** 공식을 통해 가장 경제성 높은 아키텍처를 최종 선정함.           | 가성비(ROI)가 가장 뛰어난 아키텍처 대안이 최종 베이스라인으로 확정됨.    |

#### **IV. \[결론/제언] ATAM(기술)과 CBAM(경제)의 절대적인 상호보완적 결합**

* **(키워드 위주 2줄 마무리)** "CBAM은 단독으로 쓰이기보다는, **반드시 ATAM을 선행하여 기술적인 품질 속성 검증이 끝난 대안들을 바탕으로 수행(ATAM ➔ CBAM)되어야만 진정한 가치를 발휘**합니다. 결국 훌륭한 아키텍트란 단순히 기술적 완벽함을 추구하는 엔지니어의 시각을 넘어, 기업의 제한된 자본 속에서 최대의 가치를 뽑아내는 비즈니스 파트너(투자자 시각)로 진화해야 함을 CBAM이 증명하고 있습니다."
