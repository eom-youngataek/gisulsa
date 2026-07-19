### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (표준의역사,ISO9126→25010) — 3~4줄
Ⅱ. 8대주특성 (본론①, 도식 1개 필수)
Ⅲ. 대표부특성심화 - 기능성/신뢰성/보안성 (본론②, 핵심 배점)
Ⅳ. 2023년개정사항 (최신성어필)
Ⅴ. 결론
```

포인트: 개요에서 \*\*"1991년ISO/IEC9126은 6개특성(기능성,신뢰성,사용성,효율성,유지보수성,이식성)만있었는데, 2011년25010으로통합되면서 인터넷/클라우드시대에중요해진 '보안성'과'호환성'이 새로독립된주특성으로추가되어 8개가됐다"\*\*는 한줄로시작하면, 왜숫자가8개인지역사적으로설명됩니다.

### Ⅱ. 8대주특성 — "기·성·호·사·신·보·유·이"

| 주특성       | 핵심질문         | 대표부특성          |
| :-------- | :----------- | :------------- |
| **기능적합성** | 필요한기능을제공하는가  | 완전성,정확성,적절성    |
| **성능효율성** | 자원을효율적으로쓰는가  | 시간반응성,자원활용성    |
| **호환성**   | 다른시스템과잘어울리는가 | 상호운용성,공존성      |
| **사용성**   | 쓰기쉬운가        | 학습용이성,접근성      |
| **신뢰성**   | 안정적으로계속동작하는가 | 가용성,결함허용성,복구성  |
| **보안성**   | 안전하게보호되는가    | 기밀성,무결성,부인방지   |
| **유지보수성** | 고치기쉬운가       | 모듈성,재사용성,수정용이성 |
| **이식성**   | 다른환경으로옮기기쉬운가 | 설치성,적응성        |

→ 암기: **"기능있고,빠르고,잘어울리고,쓰기쉽고,안죽고,안뚫리고,고치기쉽고,옮기기쉽다"** — 앞서다룬 \*\*"MTTR/MTBF"\*\*가 바로 **신뢰성**의 정량적측정지표이고, \*\*"결합도/응집도"\*\*는 **유지보수성**을높이는설계원리였다는연결이핵심입니다.

### 도식화 제안

```
[ISO/IEC 25010 - 8대주특성]
   ┌────────┬────────┬────────┬────────┐
  기능      성능      호환      사용
  적합성    효율성    성       성
   ├────────┼────────┼────────┼────────┤
  신뢰성    보안성    유지      이식성
                      보수성
   └────────┴────────┴────────┴────────┘
        (제품품질모델 - SQuaRE시리즈의핵심)
```

### Ⅲ. 대표부특성심화 — 핵심 배점

**함정 방지: 주특성8개만나열하면절반. 대표적인 하위(부)특성까지알아야 실제평가에쓸수있다는걸보여줘야완성됩니다.**

| 주특성       | 부특성   | 의미                                       |
| :-------- | :---- | :--------------------------------------- |
| **기능적합성** | 기능완전성 | **명시된요구사항**을얼마나구현했는가                     |
| <br />    | 기능정확성 | **정의된정밀도**로정확한결과를내는가                     |
| **신뢰성**   | 가용성   | 필요할때 **바로쓸수있는가**(앞서다룬SLA의가용성지표)          |
| <br />    | 결함허용성 | 결함이있어도 **의도한대로계속동작**하는가(앞서다룬RAID,서킷브레이커) |
| <br />    | 복구성   | 장애후 **직접데이터를복구**할수있는가(앞서다룬MTTR)          |
| **보안성**   | 기밀성   | **권한있는사람만**접근가능한가                        |
| <br />    | 무결성   | 데이터가 **인가되지않은변경없이**유지되는가                 |
| <br />    | 부인방지  | 행위나사건이 **발생했음을증명**할수있는가(로그,전자서명)         |

→ 앞서다룬 **"개인정보보호법의8원칙"**·\*\*"클라우드SLA의4대지표(가용성/성능/안정성/지원)"\*\*가 사실 이표준의 **신뢰성·보안성부특성을 각자의영역에서구체화한것**이었다는연결이 심화포인트입니다.

### Ⅳ. 2023년개정사항 — 최신성어필

**함정 방지: "지금도8개가맞다"고만답하면오래된정보일수있습니다. 2023년개정으로일부변화가있었다는걸짚어야 최신성을보여줄수있습니다.**

| 변경사항                     | 내용                                                                  |
| :----------------------- | :------------------------------------------------------------------ |
| **안전성(Safety) 신설**       | **9번째주특성**으로추가 — 운용제약,위험식별,안전장애,위험경고등 부특성포함                         |
| **사용성→상호작용역량**           | 명칭이 \*\*"Interaction Capability"\*\*로변경, **포용성(Inclusivity)** 부특성추가 |
| **이식성→유연성(Flexibility)** | 명칭변경, **확장성(Scalability)** 부특성추가                                    |
| **적용대상확장**               | 소프트웨어뿐아니라 **다양한ICT제품**까지대상범위확대                                      |

→ "시험에서'8대속성'으로배웠다면 2011년판기준이맞지만, 2023년개정판은 **안전성이추가되어실질적으로9개대특성체계**로바뀌었다"는점을 답안끝에 각주처럼붙이면 최신성과기존지식을둘다인정받을수있습니다 — 특히 **AI/자율주행등물리적위험이있는시스템**이늘면서 "안전성"이독립특성으로승격된맥락이 최신출제포인트입니다.

### Ⅴ. 결론 포인트 (테스트 시리즈 최종완결)

ISO/IEC 25010은 \*\*"좋은소프트웨어란무엇인가"**라는추상적질문에, 측정가능한8(또는2023년기준9)개축으로답하는 표준입니다 — 오늘하루다룬모든테스트기법(화이트박스/블랙박스,TDD/BDD,정적/동적분석,알파/베타/몽키테스트)은 결국 이8대특성중하나이상을검증하기위한구체적방법이었으며, 앞서다룬**ISO29119(어떻게테스트할지의프로세스표준)\*\*과 \*\*ISO25010(무엇을품질로볼지의품질모델표준)\*\*이 짝을이뤄, \*\*"무엇을,어떻게검증할것인가"\*\*라는 소프트웨어품질보증의 두축을완성한다는결론으로, 오늘하루의방대한테스트·품질시리즈전체를 마무리할수있습니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "개발팀장이 사장님에게 당당하게 보고한다. '우리가 만든 이번 소프트웨어, 품질이 진짜 끝내줍니다!' 그러자 사장님이 되묻는다. '품질이 좋다는 게 정확히 무슨 뜻인가? 처리 속도가 빠르다는 건가, 해킹에 안 뚫린다는 건가, 아니면 할머니도 쓰기 쉽다는 건가?' 이처럼 사람마다 기준이 다른 '품질'이라는 뜬구름 잡는 단어를 전 세계 누구나 고개를 끄덕일 수 있도록 8개의 객관적인 측정 잣대로 쪼개버린 국제 표준이 있다. 과거의 전설인 ISO 9126을 폐기하고 진화한 \*\*'ISO/IEC 25010'\*\*이다. 25010은 소프트웨어 제품 품질을 \*\*8대 주특성(기성호사신보유이)\*\*으로 나눈다. 먼저, 고객이 요구한 기능이 정확히 작동하는가(**1. 기능 적합성**). 아무리 기능이 좋아도 느려 터지면 안 되니 CPU 낭비 없이 빨라야 한다(**2. 성능 효율성**). 다른 시스템과 데이터 교환이 잘 되어야 하고(**3. 호환성**), 초보자도 척 보면 알 수 있게 쓰기 편해야 한다(**4. 사용성**). 또한 블랙 프라이데이에도 서버가 뻗지 않는 강인한 체력이 있어야 하고(**5. 신뢰성**), 해커의 맹공을 막아내야 하며(**6. 보안성**), 나중에 개발자가 버그를 고치기 쉽게 코드 내부 구조가 깔끔해야 한다(**7. 유지보수성**). 마지막으로 윈도우에서 돌던 앱을 리눅스나 모바일로 쉽게 이사 갈 수 있어야 한다(**8. 이식성**). 이 8개의 잔혹한 체력장을 모두 통과해야만 비로소 '고품질'이라는 훈장을 달 수 있다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] '품질'이라는 추상적인 뜬구름을 객관적 잣대로 부수다, ISO 25010 개요**

* **정의:** 소프트웨어 품질 평가의 통합 프레임워크인 **SQuaRE (ISO/IEC 25000 시리즈)** 프로젝트의 일환으로 제정된, **소프트웨어 '제품(Product)'이 갖추어야 할 품질 특성을 8가지 메인 잣대로 체계화한 국제 표준 모델**.
* **등장 배경:** 기존에 널리 쓰이던 구버전 표준인 **'ISO/IEC 9126 (6대 속성)'의 한계를 극복**하고, 현대 IT 환경에 맞게 '보안성(Security)'과 '호환성(Compatibility)'을 독립된 주특성으로 승격시켜 8대 속성으로 새롭게 진화함.

#### **II. \[본론 1] 구시대 9126에서 25010으로의 진화 및 아키텍처 (도식화)**

현대 보안의 중요성이 강조되면서 어떻게 모델이 진화했는지 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMTkxLjk0IDYzOC4zMTYiIHdpZHRoPSIxMTkxLjk0IiBoZWlnaHQ9IjYzOC4zMTYiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9fSVNPSUVDXzkxMjZfNl8iIGRhdGEtbGFiZWw9IuqzvOqxsOydmCDtkZzspIA6IElTTy9JRUMgOTEyNiAoNuuMgCDsho3shLEpIj4KICA8cmVjdCB4PSI0NDAuNjk0NzQ5OTk5OTk5OSIgeT0iNDAiIHdpZHRoPSIzNDMuOTY5OTk5OTk5OTk5OTciIGhlaWdodD0iMTEzLjgwMDAwMDAwMDAwMDAxIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDQwLjY5NDc0OTk5OTk5OTkiIHk9IjQwIiB3aWR0aD0iMzQzLjk2OTk5OTk5OTk5OTk3IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI0NTIuNjk0NzQ5OTk5OTk5OSIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+6rO86rGw7J2YIO2RnOykgDogSVNPL0lFQyA5MTI2ICg264yAIOyGjeyEsSk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfX19fSVNPSUVDXzI1MDEwXzhfIiBkYXRhLWxhYmVsPSLtmITrjIAg7ZKI7KeI7J2YIOygiOuMgCDshLHqsr06IElTTy9JRUMgMjUwMTAgKDjrjIAg7KO87Yq57ISxKSI+CiAgPHJlY3QgeD0iNDAiIHk9IjI4Mi4xIiB3aWR0aD0iMTExMS45NCIgaGVpZ2h0PSIzMTYuMjE2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjI4Mi4xIiB3aWR0aD0iMTExMS45NCIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjI5Ni4xIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPu2YhOuMgCDtkojsp4jsnZgg7KCI64yAIOyEseqyvTogSVNPL0lFQyAyNTAxMCAoOOuMgCDso7ztirnshLEpPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJPMSIgZGF0YS10bz0iVSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i67O07JWI6rO8IO2YuO2ZmOydmCDrj4Xrpr0g7Iq56rKpISIgcG9pbnRzPSI2NjAuOTkyNzQ5OTk5OTk5OSwxNDIuMDI1IDY2MC45OTI3NSwzMjYuMSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVSIgZGF0YS10bz0iUDEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNjYwLjk5Mjc1LDQ4NS40MTYwMDAwMDAwMDAwNSA2NjAuOTkyNzUsNTE1LjQxNiAyNzUuNDg4NSw1MTUuNDE2IDI3NS40ODg1LDU0NS40MTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlUiIGRhdGEtdG89IlAyIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjY2MC45OTI3NSw0ODUuNDE2MDAwMDAwMDAwMDUgNjYwLjk5Mjc1LDUxNS40MTYgNzMzLjU3MzUsNTE1LjQxNiA3MzMuNTczNSw1NDUuNDE2IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJVIiBkYXRhLXRvPSJQMyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI2NjAuOTkyNzUsNDg1LjQxNjAwMDAwMDAwMDA1IDY2MC45OTI3NSw1MTUuNDE2IDEyMi4xNzU5OTk5OTk5OTk5OSw1MTUuNDE2IDEyMi4xNzU5OTk5OTk5OTk5OSw1NDUuNDE2IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJVIiBkYXRhLXRvPSJQNCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI2NjAuOTkyNzUsNDg1LjQxNjAwMDAwMDAwMDA1IDY2MC45OTI3NSw1MTUuNDE2IDk3OC4zMjUsNTE1LjQxNiA5NzguMzI1LDU0NS40MTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlUiIGRhdGEtdG89IlA1IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjY2MC45OTI3NSw0ODUuNDE2MDAwMDAwMDAwMDUgNjYwLjk5Mjc1LDUxNS40MTYgMTA5Mi43MzUsNTE1LjQxNiAxMDkyLjczNSw1NDUuNDE2IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJVIiBkYXRhLXRvPSJQNiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI2NjAuOTkyNzUsNDg1LjQxNjAwMDAwMDAwMDA1IDY2MC45OTI3NSw1MTUuNDE2IDQzMi41MDYsNTE1LjQxNiA0MzIuNTA2LDU0NS40MTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlUiIGRhdGEtdG89IlA3IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjY2MC45OTI3NSw0ODUuNDE2MDAwMDAwMDAwMDUgNjYwLjk5Mjc1LDUxNS40MTYgNTg4LjQxMiw1MTUuNDE2IDU4OC40MTIsNTQ1LjQxNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVSIgZGF0YS10bz0iUDgiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNjYwLjk5Mjc1LDQ4NS40MTYwMDAwMDAwMDAwNSA2NjAuOTkyNzUsNTE1LjQxNiA4NjMuOTE1MDAwMDAwMDAwMSw1MTUuNDE2IDg2My45MTUwMDAwMDAwMDAxLDU0NS40MTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iTzEiIGRhdGEtdG89IlUiIGRhdGEtbGFiZWw9IuuztOyViOqzvCDtmLjtmZjsnZgg64+F66a9IOyKueqyqSEiPgogIDxyZWN0IHg9IjU4OC40OTI3NDk5OTk5OTk5IiB5PSIyMDIuOCIgd2lkdGg9IjE0NC4xNzIwMDAwMDAwMDAwMyIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjY2MC41Nzg3NDk5OTk5OTk5IiB5PSIyMTcuOTUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuuztOyViOqzvCDtmLjtmZjsnZgg64+F66a9IOyKueqyqSE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik8xIiBkYXRhLWxhYmVsPSLquLDriqXshLEsIOyLoOuisOyEsSwg7IKs7Jqp7ISxLArtmqjsnKjshLEsIOycoOyngOuztOyImOyEsSwg7J207Iud7ISxIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU1My4zMjA3NDk5OTk5OTk5IiB5PSI4OC4yMjUiIHdpZHRoPSIyMTUuMzQzOTk5OTk5OTk5OTciIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjY2MC45OTI3NDk5OTk5OTk5IiB5PSIxMTUuMTI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI2NjAuOTkyNzQ5OTk5OTk5OSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuq4sOuKpeyEsSwg7Iug66Kw7ISxLCDsgqzsmqnshLEsPC90c3Bhbj48dHNwYW4geD0iNjYwLjk5Mjc0OTk5OTk5OTkiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPu2aqOycqOyEsSwg7Jyg7KeA67O07IiY7ISxLCDsnbTsi53shLE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0NTYuNjk0NzQ5OTk5OTk5OSIgeT0iODguMjI1IiB3aWR0aD0iNjguNjI2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDkxLjAwNzc0OTk5OTk5OTkiIHk9IjEwNi42NzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk5vdGU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlUiIGRhdGEtbGFiZWw9IuygnO2SiCDtkojsp4gg66qo6424ClByb2R1Y3QgUXVhbGl0eSIgZGF0YS1zaGFwZT0iZGlhbW9uZCI+CiAgPHBvbHlnb24gcG9pbnRzPSI2NjAuOTkyNzUsMzI2LjEgNzQwLjY1MDc1LDQwNS43NTgwMDAwMDAwMDAwNCA2NjAuOTkyNzUsNDg1LjQxNjAwMDAwMDAwMDA1IDU4MS4zMzQ3NSw0MDUuNzU4MDAwMDAwMDAwMDQiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNjYwLjk5Mjc1IiB5PSI0MDUuNzU4MDAwMDAwMDAwMDQiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjY2MC45OTI3NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuygnO2SiCDtkojsp4gg66qo6424PC90c3Bhbj48dHNwYW4geD0iNjYwLjk5Mjc1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj5Qcm9kdWN0IFF1YWxpdHk8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUDEiIGRhdGEtbGFiZWw9Iuq4sOuKpSDsoIHtlanshLEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjE2LjM1MTk5OTk5OTk5OTk4IiB5PSI1NDUuNDE2IiB3aWR0aD0iMTE4LjI3MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI3NS40ODg1IiB5PSI1NjMuODY2MDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+6riw64qlIOygge2VqeyEsTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUDIiIGRhdGEtbGFiZWw9IuyEseuKpSDtmqjsnKjshLEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNjc0LjQzNyIgeT0iNTQ1LjQxNiIgd2lkdGg9IjExOC4yNzMiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI3MzMuNTczNSIgeT0iNTYzLjg2NjAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyEseuKpSDtmqjsnKjshLE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlAzIiBkYXRhLWxhYmVsPSLtmLjtmZjshLEg4pyoTkVXIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI1NDUuNDE2IiB3aWR0aD0iMTMyLjM1MTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjEyMi4xNzU5OTk5OTk5OTk5OSIgeT0iNTYzLjg2NjAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPu2YuO2ZmOyEsSDinKhORVc8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlA0IiBkYXRhLWxhYmVsPSLsgqzsmqnshLEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iOTM1LjEyIiB5PSI1NDUuNDE2IiB3aWR0aD0iODYuNDEiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI5NzguMzI1IiB5PSI1NjMuODY2MDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7IKs7Jqp7ISxPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQNSIgZGF0YS1sYWJlbD0i7Iug66Kw7ISxIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjEwNDkuNTMiIHk9IjU0NS40MTYiIHdpZHRoPSI4Ni40MSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEwOTIuNzM1IiB5PSI1NjMuODY2MDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7Iug66Kw7ISxPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQNiIgZGF0YS1sYWJlbD0i67O07JWI7ISxIPCfm6HvuI9ORVciIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzYyLjYyNSIgeT0iNTQ1LjQxNiIgd2lkdGg9IjEzOS43NjIiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNDMyLjUwNiIgeT0iNTYzLjg2NjAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuuztOyViOyEsSDwn5uh77iPTkVXPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQNyIgZGF0YS1sYWJlbD0i7Jyg7KeA67O07IiY7ISxIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjUzMC4zODcwMDAwMDAwMDAxIiB5PSI1NDUuNDE2IiB3aWR0aD0iMTE2LjA1IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNTg4LjQxMiIgeT0iNTYzLjg2NjAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuycoOyngOuztOyImOyEsTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUDgiIGRhdGEtbGFiZWw9IuydtOyLneyEsSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI4MjAuNzEiIHk9IjU0NS40MTYiIHdpZHRoPSI4Ni40MSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9Ijg2My45MTUwMDAwMDAwMDAxIiB5PSI1NjMuODY2MDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7J207Iud7ISxPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 제품 품질을 결정하는 8대 주특성 전격 해부 (3단 표 - 출제 1순위)**

암기법(**기/성/호/사/신/보/유/이**)과 함께 각 특성이 의미하는 바를 정확히 명시해야 합니다.

| **8대 주특성 명칭 (두음 암기)**                        | **주요 하위 특성 (Sub-characteristics)** | **평가하는 핵심 질문 및 실무적 의미**                                         |
| :------------------------------------------- | :--------------------------------- | :-------------------------------------------------------------- |
| **1. 기 (기능 적합성)** *(Functional Suitability)* | 완전성, 정확성, 적절성                      | "고객이 기획서에 요구한 그 기능(What)들이 **빠짐없이 올바르게 동작**하는가?"                |
| **2. 성 (성능 효율성)** *(Performance Efficiency)* | 시간 반응성, 자원 활용성, 수용성(Capacity)      | "CPU나 메모리를 쓸데없이 낭비하지 않고, 사용자가 클릭했을 때 **응답 속도가 빠른가?**"           |
| **3. 호 (호환성)** *(Compatibility)*             | 공존성, 상호운용성                         | "이 프로그램이 깔렸을 때 다른 프로그램과 충돌하지 않고, **타 시스템과 데이터 연동**이 잘 되는가?"     |
| **4. 사 (사용성)** *(Usability)*                 | 학습성, 운용성, 사용자 에러 방지, UI 미학성        | "메뉴얼을 안 봐도 초보자가 **배우기 쉽고**, 화면이 직관적이며 조작 실수를 막아주는가?"            |
| **5. 신 (신뢰성)** *(Reliability)*               | 성숙성, 가용성, 결함 허용성(Fault Tolerance)  | "서버가 뻗지 않고 365일 살아있는가? 만약 내부 에러가 터져도 **시스템 전체가 죽지 않고 버티는가?**"   |
| **6. 보 (보안성)** *(Security)*                  | 기밀성, 무결성, 부인 방지, 책임 추적성, 인증성       | "외부 해커의 침입으로부터 고객의 개인정보를 지키고, **권한 없는 자의 데이터 조작을 막아내는가?**"      |
| **7. 유 (유지보수성)** *(Maintainability)*         | 모듈성, 재사용성, 분석성, 변경성, 테스트 가능성       | "나중에 기능 추가나 버그 패치를 할 때, 스파게티 코드 없이 **개발자가 코드를 고치기(수정하기) 쉬운가?**" |
| **8. 이 (이식성)** *(Portability)*               | 적응성, 설치성, 대체성                      | "윈도우용으로 만든 프로그램을 리눅스나 모바일 환경으로 **가져가서 설치(이사)하기가 쉬운가?**"         |

#### **IV. \[결론/제언] 아키텍처 설계(ATAM) 지표와의 융합 및 클라우드 네이티브 시대의 조명**

* **(키워드 위주 2줄 마무리)** "ISO 25010의 8대 품질 속성은 단순히 테스트 단계에서만 쓰이는 체크리스트가 아닙니다. 프로젝트 초기 **소프트웨어 아키텍처를 설계하고 평가하는 ATAM 기법의 핵심 품질 속성 시나리오 잣대**로 그대로 활용되며, 최근 클라우드 네이티브 환경에서는 8대 속성 중 컨테이너의 핵심인 \*\*'이식성'\*\*과 무중단 배포를 위한 \*\*'신뢰성(가용성)'\*\*이 가장 치명적인 비즈니스 생존 지표로 격상되고 있습니다."
