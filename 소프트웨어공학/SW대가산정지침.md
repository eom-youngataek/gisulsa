### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (지침의위상,발행기관) — 3~4줄
Ⅱ. 대가산정체계 - 사업유형별원칙 (본론①, 도식 1개 필수)
Ⅲ. SW개발비산정절차 (본론②, 핵심 배점)
Ⅳ. 2024년개정사항및예외규정
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬FP,COCOMOII가 '이론적으로어떻게규모와비용을계산하는가'였다면, SW대가산정가이드는 '한국공공기관이실제사업을발주할때 어떤기준으로,어떤절차로대가를산정해야하는가'를 표준화한실무지침 — 한국소프트웨어산업협회가 매년발행"\*\*이라는한줄로시작하면, 왜FP/COCOMOII답안다음에 이지침이오는지논리가섭니다.

### Ⅱ. 대가산정체계 — 사업유형별원칙

| 사업유형                | 산정방식                                 |
| :------------------ | :----------------------------------- |
| **SW개발비**(구현단계)     | **기능점수(FP)방식이원칙**— 앞서다룬**정밀법/간이법**적용 |
| **컨설팅(ISP,BPR,EA)** | **투입공수방식**(등급별인건비×투입기간)              |
| **운영/유지관리비**        | **요율제**(개발비대비%) 또는 **투입공수방식**        |
| **AI도입비**(2024년신설)  | 별도 **AI솔루션·서비스전문작업비항목**              |

→ 암기: **"만들때는FP,기획할때는투입공수,운영할때는요율,AI는따로"** — 앞서다룬 \*\*"IT투자분석"\*\*에서 사업단계마다 다른평가기법을썼던것처럼, 대가산정도 **사업유형·단계별로다른방식**을적용합니다.

### 도식화 제안

```
[기획단계]         [구현단계]          [운영단계]
투입공수           FP방식(원칙)         요율제/투입공수
(ISP,BPR,EA)      (간이법→정밀법)      (유지관리비)
                      ↓예외
              투입공수방식(콘텐츠,5천만원미만등)
```

### Ⅲ. SW개발비산정절차 — 핵심 배점

**함정 방지: "FP구하면끝"이라고생각하면절반. FP산출부터 최종계약금액까지의 전체흐름을보여줘야완성됩니다.**

| 단계              | 내용                                         |
| :-------------- | :----------------------------------------- |
| ① **기능점수산정**    | 간이법(기획단계) 또는 정밀법(설계단계)으로 **FP산출**(앞서다룬그방법) |
| ② **보정전개발원가계산** | FP × **기능점수당단가**(2024년기준 **605,784원**)     |
| ③ **보정계수적용**    | 규모,연계복잡성,성능요구수준,운영환경호환성,**보안성수준** 5가지곱함    |
| ④ **개발원가확정**    | 보정후개발원가 산출                                 |
| ⑤ **직접경비·이윤가산** | 출장비,인쇄비등 **직접경비**+ 개발비의 **25%이내이윤** 추가     |

→ 암기: **"FP구하고,단가곱하고,5가지로보정하고,경비와이윤더한다"** — 앞서다룬 \*\*"ISO25010의성능효율성,보안성"\*\*같은 품질특성이, ③단계의 **"성능요구수준,보안성수준"보정계수**로 **직접비용에반영**된다는연결이 실무적핵심입니다.

### 도식화 제안

```
[FP산정] → [보정전개발원가=FP×단가] → [5대보정계수적용]
                                          ↓
                                    [보정후개발원가]
                                          ↓
                              [+직접경비 +이윤(25%이내)]
                                          ↓
                                     [최종계약금액]
```

### Ⅳ. 2024년개정사항및예외규정 — 최신성어필

**함정 방지: 오래된단가나예외규정을 그대로쓰면 실무에서틀립니다. 최신개정치와, FP가안맞는예외상황을 짚어야완성됩니다.**

| 항목                                 | 내용                                                                   |
| :--------------------------------- | :------------------------------------------------------------------- |
| **2024년개정**                        | **기능점수당단가 9.52%인상**(553,114원→605,784원)                               |
| **AI도입비신설**                        | 앞서다룬 \*\*AX(AI전환)\*\*관련사업의 대가산정근거가처음마련됨                              |
| **FP적용예외**(앞서다룬COCOMOII를대신활용가능한경우) | 홈페이지디자인등콘텐츠사업,**5천만원미만사업**,기능점수측정이 불가능한 데이터튜닝·테스트전용사업등은 **투입공수방식**적용 |

→ 앞서다룬 \*\*"COCOMOII"\*\*가 언급됐듯, FP방식이 \*\*"기능규모에비해내부처리복잡도가현저히높은경우"\*\*등에는적용이어렵다고 인정되면, **예외적으로투입공수방식이나COCOMO류의추정을활용**할수있다는 유연성이 이지침안에 명시되어있습니다.

### Ⅴ. 결론 포인트 (설계·비용산정 시리즈 최종완결)

SW대가산정가이드는 \*\*"앞서다룬FP(규모측정)와COCOMOII(노력추정)라는이론적모델을, 한국공공SW사업발주라는실제제도에 표준화하여적용한실무규범"\*\*입니다 — 이는 \*\*"기능점수산정→단가적용→5대보정계수→직접경비/이윤"\*\*이라는 명확한절차로, 발주자와사업자간 **객관적이고예측가능한계약금액**을보장하며, 오늘하루다룬McCabe(코드복잡도)→FanIn/Out(관계복잡도)→FP(기능규모)→COCOMOII(노력추정)→SW대가산정가이드(실제계약금액)로이어지는 시리즈전체가, \*\*"소프트웨어의복잡도를측정하는이론에서시작해, 실제국가예산이집행되는계약금액까지 하나로연결되는 완결된실무흐름"\*\*으로 마무리됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "공공기관에서 대국민 복지 포털 사이트를 만들려고 한다. 예산을 짜야 하는데 담당 공무원이 임의로 '대충 100억 주면 되겠지'라고 정할 수 있을까? 절대 불가능하다. 대한민국에는 세금 낭비와 하도급 비리를 막기 위해 한국소프트웨어산업협회(KOSA)가 매년 발표하는 절대 엑셀 계산기이자 헌법인 \*\*'SW 사업 대가 산정 가이드'\*\*가 존재하기 때문이다. 이 가이드는 과거 IT 업계의 끔찍한 악습이었던 '투입된 개발자 머릿수 세기(Man/Month 방식)'를 척결하기 위해 진화했다. 개발자가 10명 투입되든 100명 투입되든 알 바 아니고, \*\*'최종 결과물로 고객에게 제공된 기능의 개수와 가치(기능점수, FP)'\*\*만큼만 정확하게 돈을 주겠다는 것이 이 지침의 핵심 철학이다. 이 가이드는 IT 사업의 생명주기에 따라 돈 계산법을 크게 3가지로 쪼갠다. 첫째, 아예 설계도도 없는 **기획(컨설팅) 단계**다. 이때는 기능을 셀 수 없으니 어쩔 수 없이 컨설턴트의 인건비를 계산하는 \*\*'투입공수(MM) 방식'\*\*을 쓴다. 둘째, 실제 코딩을 하는 **개발 구축 단계**다. 여기가 예산의 노른자이며 무조건 \*\*'기능점수(FP) 방식'\*\*을 강제한다. 화면과 데이터의 개수를 세고 단가를 곱해 철저하게 성과(결과물) 중심으로 대가를 지불한다. 셋째, 개발이 끝나고 시스템을 돌리는 **운영/유지관리 단계**다. 이때는 1년 치 유지보수비를 전체 개발비의 약 10\~15% 수준으로 고정해서 지급하는 \*\*'요율제 방식'\*\*을 적극 권장하여 시스템의 안정성을 담보한다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 개발자 머릿수가 아닌 '가치'에 돈을 지불하라, SW 대가 산정 가이드**

* **정의:** 국가, 공공기관 등이 소프트웨어 사업(기획, 구축, 운영 등)을 추진할 때, **예산을 수립하고 사업 대가를 산정하기 위해 활용하는 법적/공식적 표준 가이드라인** (한국SW산업협회 공표).
* **핵심 철학:** 투입 인력 수(M/M) 중심의 낡은 단가 계약 방식을 지양하고, 시스템의 사용자적 가치를 산정하는 \*\*'기능점수(Function Point, FP) 기반의 결과물(성과) 중심 대가 산정'\*\*을 국가 예산 편성의 절대 원칙으로 강제함.

#### **II. \[본론 1] 구시대 투입공수(M/M) vs 현대 기능점수(FP) 철학적 대립 (도식화)**

왜 대한민국이 M/M 방식을 버리고 FP 방식으로 넘어왔는지를 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNjIyLjcyMDAwMDAwMDAwMDMgMjY3LjYiIHdpZHRoPSIxNjIyLjcyMDAwMDAwMDAwMDMiIGhlaWdodD0iMjY3LjYiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IlNXX19fXzJfXyIgZGF0YS1sYWJlbD0iU1cg64yA6rCAIOyCsOyglSDrsKnsi53snZggMuuMgCDtjKjrn6zri6TsnoQg7KCE7ZmYIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIxNTQyLjcyMDAwMDAwMDAwMDMiIGhlaWdodD0iMTg3LjYwMDAwMDAwMDAwMDAyIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMTU0Mi43MjAwMDAwMDAwMDAzIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+U1cg64yA6rCAIOyCsOyglSDrsKnsi53snZggMuuMgCDtjKjrn6zri6TsnoQg7KCE7ZmYPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJNIiBkYXRhLXRvPSJFIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLqs7zqsbDsnZgg67OR7Y+QIiBwb2ludHM9IjI4NS40MjMsMTc2LjI1IDQ1Mi4yNTUsMTc2LjI1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJFIiBkYXRhLXRvPSJGIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLrspXsoIEg7KCc64+EIO2YgeyLoCDwn5qAIiBwb2ludHM9IjY5NS43NTcsMTc2LjI1IDg4OS45MTMsMTc2LjI1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJGIiBkYXRhLXRvPSJSIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLshKDsiJztmZgg6rWs7KGwIiBwb2ludHM9IjExMDYuNzM5LDE3Ni4yNSAxMjczLjU3MTAwMDAwMDAwMDEsMTc2LjI1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209Ik0iIGRhdGEtdG89IkUiIGRhdGEtbGFiZWw9IuqzvOqxsOydmCDrs5Htj5AiPgogIDxyZWN0IHg9IjMyOS40MjMiIHk9IjE2MC4yNSIgd2lkdGg9Ijc4LjgzMjAwMDAwMDAwMDAxIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzY4LjgzOSIgeT0iMTc1LjQiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuqzvOqxsOydmCDrs5Htj5A8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iRSIgZGF0YS10bz0iRiIgZGF0YS1sYWJlbD0i67KV7KCBIOygnOuPhCDtmIHsi6Ag8J+agCI+CiAgPHJlY3QgeD0iNzM5Ljc1NyIgeT0iMTYwLjI1IiB3aWR0aD0iMTA2LjE1NjAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNzkyLjgzNDk5OTk5OTk5OTkiIHk9IjE3NS40IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7rspXsoIEg7KCc64+EIO2YgeyLoCDwn5qAPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkYiIGRhdGEtdG89IlIiIGRhdGEtbGFiZWw9IuyEoOyInO2ZmCDqtazsobAiPgogIDxyZWN0IHg9IjExNTAuNzM5IiB5PSIxNjAuMjUiIHdpZHRoPSI3OC44MzIwMDAwMDAwMDAwMSIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjExOTAuMTU1IiB5PSIxNzUuNCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7ISg7Iic7ZmYIOq1rOyhsDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTSIgZGF0YS1sYWJlbD0i6rWs7Iuc64yAOiDtiKzsnoXqs7XsiJgg67Cp7IudIPCfkbfigI3imYLvuI8KSGVhZGNvdW50IChNYW4vTW9udGgpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIxNDkuMzUwMDAwMDAwMDAwMDIiIHdpZHRoPSIyMjkuNDIzIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNzAuNzExNSIgeT0iMTc2LjI1MDAwMDAwMDAwMDAzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNzAuNzExNSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuq1rOyLnOuMgDog7Yis7J6F6rO17IiYIOuwqeyLnSDwn5G34oCN4pmC77iPPC90c3Bhbj48dHNwYW4geD0iMTcwLjcxMTUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPkhlYWRjb3VudCAoTWFuL01vbnRoKTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJFIiBkYXRhLWxhYmVsPSLtlZjrj4TquIkg7KWQ7Ja07Kec6riwIOuwnOyDnQrriqXroKUg67aA7KGx7ZWcIOyCrOuejOunjCDsnpTrnKkg7Yis7J6F7ZWoCu2SiOyniCDstZzslYXsnLzroZwg6rOk65GQ67CV7KeI7LmoISIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0NTIuMjU1IiB5PSIxNDAuOSIgd2lkdGg9IjI0My41MDE5OTk5OTk5OTk5OCIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNTc0LjAwNiIgeT0iMTc2LjI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI1NzQuMDA2IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+7ZWY64+E6riJIOylkOyWtOynnOq4sCDrsJzsg508L3RzcGFuPjx0c3BhbiB4PSI1NzQuMDA2IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7riqXroKUg67aA7KGx7ZWcIOyCrOuejOunjCDsnpTrnKkg7Yis7J6F7ZWoPC90c3Bhbj48dHNwYW4geD0iNTc0LjAwNiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7ZKI7KeIIOy1nOyVheycvOuhnCDqs6TrkZDrsJXsp4jsuaghPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkYiIGRhdGEtbGFiZWw9Iu2YhOuMgCDtkZzspIA6IOq4sOuKpeygkOyImCDrsKnsi50g8J+OrwpGdW5jdGlvbiBQb2ludCAoRlApIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9Ijg4OS45MTMiIHk9IjE0OS4zNTAwMDAwMDAwMDAwMiIgd2lkdGg9IjIxNi44MjYiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iOTk4LjMyNiIgeT0iMTc2LjI1MDAwMDAwMDAwMDAzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI5OTguMzI2IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7ZiE64yAIO2RnOykgDog6riw64ql7KCQ7IiYIOuwqeyLnSDwn46vPC90c3Bhbj48dHNwYW4geD0iOTk4LjMyNiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+RnVuY3Rpb24gUG9pbnQgKEZQKTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJSIiBkYXRhLWxhYmVsPSLqsrDqs7zrrLwo6riw64qlIOqwnOyImCnrp4ztgbzrp4wg64+I7J2EIOykjCEK7LKc7J6sIOqwnOuwnOyekCAx66qF7J20IOqzoO2SiOyniOuhnCDruajrpqwg64Gd64K066m0CuqwnOuwnOyCrCDsnbTsnKQg6re564yA7ZmUIOKelCDtkojsp4gg7Zal7IOBISIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMjczLjU3MTAwMDAwMDAwMDEiIHk9IjE0MC45IiB3aWR0aD0iMjkzLjE0OSIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTQyMC4xNDU1IiB5PSIxNzYuMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE0MjAuMTQ1NSIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPuqysOqzvOusvCjquLDriqUg6rCc7IiYKeunjO2BvOunjCDrj4jsnYQg7KSMITwvdHNwYW4+PHRzcGFuIHg9IjE0MjAuMTQ1NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7LKc7J6sIOqwnOuwnOyekCAx66qF7J20IOqzoO2SiOyniOuhnCDruajrpqwg64Gd64K066m0PC90c3Bhbj48dHNwYW4geD0iMTQyMC4xNDU1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7qsJzrsJzsgqwg7J207JykIOq3ueuMgO2ZlCDinpQg7ZKI7KeIIO2WpeyDgSE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSI2OC42MjYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI5MC4zMTMiIHk9IjEwMi40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Tm90ZTwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 사업 생명주기에 따른 3대 대가 산정 체계 전격 해부 (3단 표 - 출제 1순위)**

SW 기획부터 유지보수까지, 각 단계마다 '어떤 엑셀 계산법'을 써야 하는지 매핑해야 합니다.

| **SW 사업 추진 단계**                      | **적용되는 핵심 대가 산정 방식 (명칭)**                     | **산정 방식의 적용 이유 및 세부 산출 논리**                                                                                                |
| :----------------------------------- | :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| **1. SW 기획 단계** *(컨설팅, ISP, EA 등)*   | **투입공수 (Man-Month) 방식** *(노력 기반 산정)*          | 아직 시스템의 화면이나 기능이 구체화되지 않아 FP를 잴 수 없는 상태임. 따라서 전략 수립에 투입되는 컨설턴트/설계자의 **인건비(직무별 단가 × 투입 개월 수)에 직접경비와 제경비, 기술료를 합산하여 도출함.**   |
| **2. SW 개발 구축 단계** *(신규 개발, 재개발)*    | **기능점수 (Function Point) 방식** *(결과물 규모 기반 산정)* | 예산이 가장 크게 들어가는 단계. 사용자 관점의 5대 데이터/트랜잭션 기능 개수를 세어 **개발 규모(FP)를 확정한 뒤, 기능점수당 단가(원/FP)를 곱하고 시스템 복잡도 보정 계수를 곱하여 최종 개발비를 도출함.** |
| **3. SW 운영 및 유지관리 단계** *(유지보수, 재설계)* | **요율제 방식 (또는 투입공수)** *(가치 및 비율 기반 산정)*        | 유지보수를 일일이 건건이 계산하기 어려우므로, 글로벌 표준 방식인 요율제를 도입함. **과거 개발비 산정액의 N% (보통 10\~15% 내외)를 매년 유지관리 대가로 고정 지급**하여 벤더의 안정적 지원을 보장함.    |

#### **IV. \[결론/제언] 유지보수 요율 현실화의 숙제와 상용 SW 분리 발주 의무화**

* **(키워드 위주 2줄 마무리)** "현재 SW 대가 산정 지침은 기능점수(FP)를 완벽히 정착시켰으나, 여전히 글로벌 평균(20% 수준)에 못 미치는 \*\*'낮은 공공 유지보수 요율의 현실화'\*\*라는 과제를 안고 있습니다. 이를 해결하기 위해 최근 정부는 통합 발주를 금지하고 데이터베이스(DBMS) 등의 **'상용 SW 분리 발주 의무화'를 통해 정당한 유지관리 대가를 보장하는 방향으로 지침을 지속적으로 고도화**하고 있습니다."
