### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (CMMI정의,12207과의관계) — 3~4줄
Ⅱ. 5대성숙도레벨 (본론①, 도식 1개 필수)
Ⅲ. 프로세스영역(전통구조) 및표현방법 (본론②, 핵심 배점)
Ⅳ. V3.0 최신개편사항
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬ISO/IEC12207이 '어떤프로세스가필요한가(What)'를정의했다면, CMMI는 '그프로세스를조직이얼마나잘,얼마나성숙하게수행하는가'를 5단계로평가 — 카네기멜론대학SEI가개발했고,여러개별CMM모델(SW,시스템엔지니어링등)을 하나로통합(Integration)했다"\*\*는한줄로시작하면, 왜 "Integration"이라는이름이붙었는지와 12207과의관계가명확해집니다.

### Ⅱ. 5대성숙도레벨 — "초·관·정·정·최"

| 레벨    | 명칭                            | 특징                              |
| :---- | :---------------------------- | :------------------------------ |
| **1** | 초기(Initial)                   | **임시적,혼란스러움**— 개인역량에의존,예측불가능    |
| **2** | 관리(Managed)                   | **프로젝트단위**로계획·관리됨(반복가능성확보시작)    |
| **3** | 정의(Defined)                   | **조직표준프로세스**존재,프로젝트마다맞춤적용(테일러링) |
| **4** | 정량적관리(Quantitatively Managed) | **통계적기법**으로프로세스성과를수치로관리         |
| **5** | 최적화(Optimizing)               | **지속적개선**이조직문화로정착,혁신을능동적으로추구    |

→ 암기: **"혼란(1)→관리(2)→표준화(3)→숫자로관리(4)→스스로개선(5)"** — 앞서다룬 \*\*"방법론테일러링"\*\*이 정확히 \*\*레벨3(정의)\*\*에서요구되는활동이며, \*\*"CBAM/IT-ROI의ROI계산"\*\*같은정량적기법이 \*\*레벨4(정량적관리)\*\*에서 조직전체차원으로 요구된다는연결이핵심입니다.

### 도식화 제안

```
[레벨5] 최적화        ← 스스로계속개선(문화화)
[레벨4] 정량적관리      ← 숫자(통계)로프로세스관리
[레벨3] 정의(표준화)    ← 조직표준프로세스+테일러링
[레벨2] 관리           ← 프로젝트단위계획·관리
[레벨1] 초기           ← 혼란,개인역량의존

(위로갈수록: 예측가능성↑,반복가능성↑,비용변동↓)
```

### Ⅲ. 프로세스영역(전통구조) 및표현방법 — 핵심 배점

**함정 방지: "5단계만있다"고답하면절반. 각레벨에 구체적으로 무엇을해야하는지(프로세스영역)와, 접근방식2종(단계적/연속적)을보여줘야완성됩니다.**

전통적CMMI(1.3 등)는 **성숙도레벨1\~5**에 걸쳐 **총22개프로세스영역(Process Area),431개프랙티스**로구성되며, \*\*"레벨3까지의18개프로세스영역"\*\*을충족해야 \*\*"CMMI레벨3인증"\*\*을받을수있었습니다.

| 표현방법                  | 내용                                                                     |
| :-------------------- | :--------------------------------------------------------------------- |
| **단계적표현(Staged)**     | 성숙도레벨별로 **프로세스영역을미리정해둠**(순서/우선순위고정) — 국내에서주로활용되는방식                     |
| **연속적표현(Continuous)** | **개별프로세스영역마다별도로능력수준평가**(앞서다룬\*\*SPICE(ISO/IEC15504)\*\*가이방식과유사한 2차원구조) |

→ 암기: **"단계적은전체를한덩어리로줄세우고,연속적은영역별로따로점수매긴다"** — 앞서다룬 \*\*"12207이SPICE의기본틀"\*\*이라고했던연결이, 여기서 **CMMI의연속적표현방식과SPICE가 유사한철학을공유**한다는것으로 이어집니다.

### Ⅳ. V3.0 최신개편사항 — 최신성어필

**함정 방지: "예전CMMI"만알고있으면 오래된정보일수있습니다. 2023년개편내용을짚어야 최신성을보여줄수있습니다.**

**2023년4월, CMMI V3.0이 출시**되며 **모델아키텍처자체가개편**되고 \*\*새로운실천영역(Practice Area)\*\*이 도입됐습니다 — 기존의 "프로세스영역(Process Area)"이라는 용어대신 \*\*"실천영역(Practice Area)"\*\*중심으로 구조가재편되어, **더유연하게조직의실제업무방식(애자일,DevOps등)에맞춰적용**할수있도록 개선됐다는게핵심변화입니다.

→ "예전CMMI가 '고정된22개프로세스영역'을 다소경직되게 요구했다면, V3.0은 앞서다룬\*\*'방법론테일러링'철학\*\*을 표준자체에더깊이반영해, 조직마다다른개발방식(애자일포함)에 유연하게맞출수있게진화했다"는점이 최신출제포인트입니다.

### Ⅴ. 결론 포인트 (표준 시리즈 최종완결)

CMMI는 \*\*"ISO/IEC12207이정의한프로세스뼈대를,조직이얼마나성숙하게수행하는지 5단계로평가하고개선방향을제시하는 성숙도잣대"\*\*입니다 — 이는 앞서다룬 ISO29119(테스팅프로세스),ISO25010(품질모델),McCabe(코드복잡도),기술부채4분면(관리판단)이 모두 **"개별기법·개별지표"** 차원이었다면, CMMI는 \*\*"조직전체가이모든것을 얼마나체계적이고성숙하게운영하는가"\*\*를 평가하는 **최상위관리성숙도척도**라는점에서, 오늘하루다룬방대한소프트웨어공학·품질·표준시리즈전체(McCabe→기술부채→코드스멜→리팩토링→12207→CMMI)를 \*\*"개별코드부터조직전체까지, 품질을체계적으로관리하는하나의완결된피라미드"\*\*로 마무리할수있습니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "동네 구멍가게 식당과 전국 체인을 가진 5성급 호텔 주방의 차이는 무엇일까? 구멍가게는 요리사의 그날 컨디션에 따라 김치찌개 맛이 매일 바뀌지만(개인에 의존), 5성급 호텔은 누가 주방에 서든 완벽한 레시피와 매뉴얼(프로세스)에 의해 항상 똑같은 맛을 보장한다. 소프트웨어 개발 조직도 완전히 똑같다. 해당 회사의 개발 수준이 주먹구구식 구멍가게인지, 아니면 체계적인 매뉴얼을 갖춘 5성급 호텔인지를 심사하고 1\~5등급의 인증 스티커를 붙여주는 세계 최고 권위의 품질 인증 마크가 바로 카네기멜론 대학이 만든 \*\*'CMMI(능력 성숙도 통합 모델)'\*\*다. CMMI는 조직의 성숙도를 5단계로 잔인하게 평가한다. 아무런 매뉴얼 없이 '천재 개발자 1명'의 철야 야근에만 모든 걸 기대는 수준은 \*\*레벨 1(초기)\*\*이다. 영웅이 퇴사하면 프로젝트도 망한다. 부서별로 프로젝트 관리 매뉴얼을 갖추어 과거의 성공을 반복할 수 있게 되면 **레벨 2(관리)**, 이것이 전사적인 회사 통합 표준 매뉴얼로 굳어지면 \*\*레벨 3(정의)\*\*다. 이 레벨 3부터가 글로벌 및 공공기관 입찰에 참여할 수 있는 진짜 IT 회사의 마지노선이다. 여기서 멈추지 않고, 소프트웨어 개발 속도와 버그 발생률을 통계적인 '숫자(데이터)'로 통제하기 시작하면 \*\*레벨 4(정량적 관리)\*\*에 오르며, 마지막으로 AI 같은 신기술을 선제적으로 도입하여 매뉴얼 자체를 끊임없이 스스로 파괴하고 혁신하는 궁극의 경지에 이르면 꿈의 \*\*레벨 5(최적화)\*\*를 달성하게 된다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 구멍가게인가, 5성급 팩토리인가? CMMI 모델 개요**

* **정의:** 카네기멜론 대학의 소프트웨어 공학 연구소(SEI)가 미 국방성의 의뢰로 개발한, 조직의 **소프트웨어 개발 및 유지보수 프로세스의 능력과 성숙도 수준을 평가하고 개선하기 위한 글로벌 통합 가이드라인(인증 모델)**.
* **제정 목적:** CMM, SECM 등 흩어져 있던 과거의 심사 모델들을 하나로 통합(Integration)하여, 발주자(고객)가 시스템을 수주받을 개발사(공급자)의 역량을 \*\*객관적인 1\~5 레벨의 숫자로 평가하고 보증(심사)\*\*하기 위함.

#### **II. \[본론 1] CMMI를 평가하는 2가지 잣대: 단계적 vs 연속적 표현 (도식화)**

조직 전체를 한 번에 심사할 것인가, 특정 부서의 영역만 심사할 것인가의 구조적 차이입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3NTkuODYyOTk5OTk5OTk5OSAyNjcuNiIgd2lkdGg9Ijc1OS44NjI5OTk5OTk5OTk5IiBoZWlnaHQ9IjI2Ny42IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJDTU1JXzJfX19fUmVwcmVzZW50YXRpb24iIGRhdGEtbGFiZWw9IkNNTUnsnZggMuqwgOyngCDslYTtgqTthY3sspgg7ZGc7ZiEIOuqqOuNuCAoUmVwcmVzZW50YXRpb24pIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI2NzkuODYyOTk5OTk5OTk5OSIgaGVpZ2h0PSIxODcuNjAwMDAwMDAwMDAwMDIiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI2NzkuODYyOTk5OTk5OTk5OSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPkNNTUnsnZggMuqwgOyngCDslYTtgqTthY3sspgg7ZGc7ZiEIOuqqOuNuCAoUmVwcmVzZW50YXRpb24pPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTIiBkYXRhLXRvPSJTMSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7KGw7KeBIOyghOyytCDsi6zsgqwiIHBvaW50cz0iMzIwLjY5NywxMTAuOSA1MDEuMTkxMDAwMDAwMDAwMDMsMTEwLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkMiIGRhdGEtdG89IkMxIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLtirnsoJUg7JiB7Jet66eMIO2VgOyFiyDsi6zsgqwiIHBvaW50cz0iMjU3LjI2NDk5OTk5OTk5OTkzLDE4NC43MDAwMDAwMDAwMDAwMiA0NzUuMTgwOTk5OTk5OTk5OSwxODQuNzAwMDAwMDAwMDAwMDIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iUyIgZGF0YS10bz0iUzEiIGRhdGEtbGFiZWw9IuyhsOyngSDsoITssrQg7Ius7IKsIj4KICA8cmVjdCB4PSIzNjQuNjk3IiB5PSI5NC45IiB3aWR0aD0iOTIuNDk0MDAwMDAwMDAwMDMiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI0MTAuOTQ0IiB5PSIxMTAuMDUwMDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuyhsOyngSDsoITssrQg7Ius7IKsPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkMiIGRhdGEtdG89IkMxIiBkYXRhLWxhYmVsPSLtirnsoJUg7JiB7Jet66eMIO2VgOyFiyDsi6zsgqwiPgogIDxyZWN0IHg9IjMwMS4yNjQ5OTk5OTk5OTk5MyIgeT0iMTY4LjcwMDAwMDAwMDAwMDAyIiB3aWR0aD0iMTI5LjkxNjAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzY2LjIyMjk5OTk5OTk5OTk2IiB5PSIxODMuODUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPu2KueyglSDsmIHsl63rp4wg7ZWA7IWLIOyLrOyCrDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUyIgZGF0YS1sYWJlbD0i64uo6rOE7KCBIO2RnO2YhCDrqqjrjbgKU3RhZ2VkIFJlcHJlc2VudGF0aW9uIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjE0NC42MjYiIHk9Ijg0IiB3aWR0aD0iMTc2LjA3MDk5OTk5OTk5OTk3IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjIzMi42NjE1IiB5PSIxMTAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMjMyLjY2MTUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7ri6jqs4TsoIEg7ZGc7ZiEIOuqqOuNuDwvdHNwYW4+PHRzcGFuIHg9IjIzMi42NjE1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5TdGFnZWQgUmVwcmVzZW50YXRpb248L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQyIgZGF0YS1sYWJlbD0i7Jew7IaN7KCBIO2RnO2YhCDrqqjrjbgKQ29udGludW91cyBSZXByZXNlbnRhdGlvbiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iMTU3LjgiIHdpZHRoPSIyMDEuMjY0OTk5OTk5OTk5OTMiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTU2LjYzMjQ5OTk5OTk5OTk2IiB5PSIxODQuNzAwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjE1Ni42MzI0OTk5OTk5OTk5NiIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuyXsOyGjeyggSDtkZztmIQg66qo6424PC90c3Bhbj48dHNwYW4geD0iMTU2LjYzMjQ5OTk5OTk5OTk2IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5Db250aW51b3VzIFJlcHJlc2VudGF0aW9uPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlMxIiBkYXRhLWxhYmVsPSLsobDsp4Eg7KCE7LK07J2YIOyEseyImeuPhCDsuKHsoJUKTWF0dXJpdHkgTGV2ZWwgMX41IOuLqOqzhCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1MDEuMTkxMDAwMDAwMDAwMDMiIHk9Ijg0IiB3aWR0aD0iMTk2LjgxOSIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjU5OS42MDA1IiB5PSIxMTAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNTk5LjYwMDUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7sobDsp4Eg7KCE7LK07J2YIOyEseyImeuPhCDsuKHsoJU8L3RzcGFuPjx0c3BhbiB4PSI1OTkuNjAwNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+TWF0dXJpdHkgTGV2ZWwgMX41IOuLqOqzhDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDMSIgZGF0YS1sYWJlbD0i6rCc67OEIO2UhOuhnOyEuOyKpCDri6jsnIQg7Jet65+JIOy4oeyglQpDYXBhYmlsaXR5IExldmVsIDB+MyDri6jqs4QiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDc1LjE4MDk5OTk5OTk5OTkiIHk9IjE1Ny44IiB3aWR0aD0iMjI4LjY4MiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjU4OS41MjE5OTk5OTk5OTk5IiB5PSIxODQuNzAwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjU4OS41MjE5OTk5OTk5OTk5IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+6rCc67OEIO2UhOuhnOyEuOyKpCDri6jsnIQg7Jet65+JIOy4oeyglTwvdHNwYW4+PHRzcGFuIHg9IjU4OS41MjE5OTk5OTk5OTk5IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5DYXBhYmlsaXR5IExldmVsIDB+MyDri6jqs4Q8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSI2OC42MjYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI5MC4zMTMiIHk9IjEwMi40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Tm90ZTwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] CMMI 단계적 표현의 성숙도 5단계 전격 해부 (3단 표 - 출제 1순위)**

암기법(**초/관/정/정/최**)을 통해 각 레벨이 의미하는 바와 핵심 특징을 완벽하게 매핑해야 합니다.

| **성숙도 레벨 *(Maturity Level)*** | **수준 명칭 (영문) 및 핵심 상태**                                  | **레벨별 핵심 특징 및 실무적 의미 (프로세스 변화)**                                                                    |
| :---------------------------- | :------------------------------------------------------ | :-------------------------------------------------------------------------------------------------- |
| **레벨 1** 🥉                   | **초기 (Initial)** *(무계획, 혼돈 상태)*                         | 프로세스나 매뉴얼이 아예 없음. 프로젝트의 성공이 운이나 **'소수 천재 개발자(영웅)의 개인기'에 전적으로 의존함.** 영웅이 퇴사하면 조직은 붕괴됨.               |
| **레벨 2** 🥈                   | **관리 (Managed)** *(반복 가능 상태)*                           | 프로젝트(부서) 단위의 기본적인 관리 체계가 구축됨. 요구사항 관리, 형상 관리 등을 통해 **'과거의 유사한 프로젝트 성공 경험을 반복(Repeatable)'할 수 있음.**  |
| **레벨 3** 🥇                   | **정의 (Defined)** *(조직 표준화 상태)*                          | 레벨 2의 부서별 매뉴얼들이 통합되어 **'회사 전체(조직 차원)의 일관된 통합 표준 프로세스'가 확립됨.** 각 프로젝트는 이 전사 표준을 테일러링(재단)하여 사용함.      |
| **레벨 4** 💎                   | **정량적 관리** **(Quantitatively Managed)** *(수치 기반 제어 상태)* | 모든 프로세스의 성과(버그 발생률, 속도 등)를 주먹구구가 아닌 **'통계적 품질 제어(SPC) 기법과 정량적인 수치 데이터'로 측정하고 엄격하게 통제**함.            |
| **레벨 5** 👑                   | **최적화 (Optimizing)** *(지속적 혁신 상태)*                      | 정량적 데이터를 바탕으로 결함의 근본 원인을 분석하여 싹을 자름. 변화하는 비즈니스에 맞춰 **새로운 신기술이나 프로세스를 선제적으로 도입하며 스스로 끊임없이 개선(혁신)함.** |

#### **IV. \[결론/제언] CMMI 인증의 한계(문서화의 늪)와 애자일(Agile) 철학과의 융합**

* **(키워드 위주 2줄 마무리)** "CMMI 레벨 3 이상의 인증 획득은 글로벌 IT 입찰의 필수 스펙이 되었으나, 심사 통과만을 목적으로 하는 \*\*'보여주기식 문서화의 늪(과잉 프로세스)'\*\*에 빠지는 부작용을 낳기도 했습니다. 이에 대한 반동으로 가벼운 실용주의를 추구하는 애자일(Agile) 사상이 대두되었으며, 현대의 CMMI v2.0 모델은 경직된 프로세스를 버리고 **애자일의 빠르고 유연한 가치(가치 중심 인도)를 전격 수용하여 혁신적인 융합**을 이루어냈습니다."
