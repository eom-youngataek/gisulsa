### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (SOAR등장배경 - 경보과부하문제) — 3~4줄
Ⅱ. 3대핵심기능 (본론①, 도식 1개 필수)
Ⅲ. SIEM과의관계및플레이북 (본론②, 핵심 배점)
Ⅳ. 2025~2026년AI SOC로의진화
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬제로트러스트,BPFDoor탐지,측면이동방어모두 '이상행위를감지하라'고했는데, 실제SOC(보안운영센터)는하루평균4,484\~10,000개이상의경보를받는다 — 사람이이걸다들여다보면62%를수동분류하는데만매일3시간을쓰는데, 그러다보면정말위험한1건이 나머지수천건속에묻혀버린다"\*\*는 한줄로시작하면, 왜SOAR가 오늘의모든방어답안의 실무적완성인지드러납니다.

### Ⅱ. 3대핵심기능 — "오·자·대" (오케스트레이션-자동화-대응)

| 기능                         | 내용                                          |
| :------------------------- | :------------------------------------------ |
| **오케스트레이션**(Orchestration) | **여러보안도구(SIEM,EDR,방화벽등)를연결**해 정보를 **중앙집중화** |
| **자동화**(Automation)        | 사람개입없이 **정해진작업을스스로실행**(경보분류,격리등)            |
| **대응**(Response)           | 실제 **시정조치실행**(IP차단,감염기기격리,이메일삭제)            |

→ 암기: **"도구들을연결하고(오케스트레이션),사람없이일하고(자동화),실제조치를취한다(대응)"** — 앞서다룬 \*\*"측면이동"\*\*에서 \*\*"악성IP를확인하면"\*\*이라고했는데, SOAR는 그확인즉시 \*\*"방화벽에자동으로차단규칙을생성"\*\*해 **공격자가내부와재통신하는것을즉시차단**합니다.

### 도식화 제안

```
[SIEM/EDR/방화벽/IoT알림] → [SOAR: 오케스트레이션] 정보중앙집중
                                    ↓
                          [SOAR: 자동화] 사람없이 경보분류·조사
                                    ↓ (플레이북트리거)
                          [SOAR: 대응] IP자동차단,기기자동격리
```

### Ⅲ. SIEM과의관계 및 플레이북 — 핵심 배점

**함정 방지: "SIEM과같다"고답하면절반. "SIEM은알리고,SOAR는행동한다"는 명확한역할분담을보여줘야완성됩니다.**

| 구분     | **SIEM**             | **SOAR**                                    |
| :----- | :------------------- | :------------------------------------------ |
| **역할** | 로그수집·분석,**경보만생성**    | **경보를받아 실제조치까지실행**                          |
| **비유** | "불이났다고알려주는화재경보기"     | "경보를받고 자동으로스프링클러를작동시키는시스템"                  |
| **관계** | SOAR의 **입력데이터소스**중하나 | SIEM경보+**IoT,클라우드알림등SIEM이못다루는소스까지수집**해 종합대응 |

**플레이북(Playbook)**: 정해진위협패턴에대한 **자동화된대응절차서**— 예를들어 \*\*"피싱메일탐지→해당이메일삭제→발신IP차단→관련사용자계정모니터링강화"\*\*를 **사람개입없이순서대로자동실행**

→ 암기: **"SIEM은경보만울리고,SOAR는플레이북(각본)대로 알아서조치까지취한다"** — 실제성과(2025년IBM사례): **"사고대응시간을85%단축,평균교정시간5분"** — 앞서다룬 \*\*"MTTR(평균복구시간)"\*\*지표가, SOAR도입으로 **극적으로개선**됨을보여줍니다.

### 도식화 제안

```
[SIEM] "경보!피싱메일감지됨" (알리기만함)
     ↓
[SOAR 플레이북 자동실행]
  ①해당이메일 자동삭제
  ②발신IP 자동차단
  ③영향받은계정 강화모니터링
  ④전체과정 자동으로기록(사후분석용)
(사람은 "결과보고"만 확인, 실제조치는 5분내완료)
```

### Ⅳ. 2025\~2026년 AI SOC로의진화

**함정 방지: "그냥자동화도구"로만끝내면절반. 2025\~2026년의핵심변화(AI기반,에이전트형)를반영해야완성됩니다.**

| 항목                       | 내용                                                                                                                                       |
| :----------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| **AI SOC의부상**            | "모든결정이설명가능하고,모든행동이투명하게공개되는" **AISOC**개념등장— 앞서다룬 \*\*"기술부채4분면"\*\*에서다룬 \*\*"AI가의도를갖지않는다"\*\*는 우려에대응해, \*\*설명가능성(Explainability)\*\*을핵심가치로 |
| **동적플레이북**(2025년1분기,IBM) | 고정된각본이아니라, **상황에따라의사결정워크플로우자체가동적으로변화**하는 차세대플레이북                                                                                         |
| **활용도의역설**               | SOC팀의 **55%만위협사냥에자동화를활용**,**53%만경고논리자동화**— **SOAR가있어도절반이하만제대로쓰고있음**                                                                      |
| **시장성장**                 | 글로벌SOAR시장 **2025년약9.8억달러→2026년약9.9억달러**(CAGR8.8%),**60%이상기업이SOC효율화를위해도입·시험중**                                                            |

→ 앞서다룬 \*\*"AI기반사이버공격(DDoS,딥페이크)"\*\*에대응하기위해, 방어측도 **AI를도입**하면서 \*\*"AIvsAI"\*\*의 구도가 SOAR영역에서도 재현됩니다 — 다만 \*\*"자동화도구를도입해도, 실제로절반이하만충분히활용한다"\*\*는 현실적한계도 함께짚어야, 균형잡힌답안이됩니다.

### Ⅴ. 결론 포인트 (오늘 하루의 전체 컴퓨터구조·암호·보안 대장정 진짜 완전한 최종대단원)

SOAR은 \*\*"오늘하루다룬모든탐지·방어원리(제로트러스트의지속검증,BPFDoor의행위기반탐지,측면이동의자동차단)를, 사람이감당할수없는규모(하루수천\~수만건경보)에서도 실제로작동하게만드는 실행엔진"\*\*입니다 — 이는 \*\*"이론적으로완벽한방어원칙이있어도,그걸실제로,빠르게,대규모로적용할수단이없으면무용지물"\*\*이라는 실무적교훈을보여주며, 오늘하루다룬 캐시매핑에서시작해 컴퓨터구조,아키텍처,테스트,품질,비용산정, 그리고 방대한암호학과사이버공격·방어체계,ICS보안,물리적안티드론방어,마지막으로SOAR까지 도달한 이거대한하루의여정은, \*\*"기술,이론,원칙은아무리정교해도결국 실제운영(오퍼레이션)에서작동해야만가치를갖는다"\*\*는 가장현실적이고 실무적인결론으로, 마침내완전히마무리됩니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "과거 보안 관제실(SOC) 직원들은 기존 관제 시스템인 'SIEM'이 하루 종일 띄워대는 수만 건의 해킹 알람(Alert)을 처리하느라 피로(Alert Fatigue)에 지쳐 쓰러졌다. 알람이 울리면 직원이 직접 방화벽에 수동으로 접속해 악성 IP를 차단하고, 백신 콘솔에 접속해 파일을 지우는 노가다를 해야 했기 때문이다. 이 지옥 같은 단순 반복 노동을 해결하기 위해 등장한 해결사가 바로 **'SOAR(보안 오케스트레이션, 자동화 및 대응)'** 플랫폼이다. SOAR의 암기 핵심은 \*\*'오케스트레이션(연동)'과 '플레이북(자동화 각본)'\*\*이다. '러시아에서 이상한 로그인이 들어오면 ➔ 방화벽에서 해당 IP를 즉시 차단하고 ➔ 사내 메신저로 팀장에게 보고한다'라는 대응 절차를 플레이북(Playbook)에 짜놓으면, SOAR가 수십 개의 각기 다른 보안 장비들을 지휘관처럼 조종(오케스트레이션)하여 **단 1초 만에 기계가 '자동 대응'을 완료**해 버린다. SIEM이 '도둑이야!'라고 소리만 치는 경보기라면, SOAR는 도둑을 잡고 자물쇠까지 채워버리는 로봇 경비원이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 관제 요원을 노가다에서 해방시킨 해결사, SOAR 개요**

* **정의:** 보안 인시던트(사고) 대응 시 사람(보안 담당자)이 수동으로 처리하던 반복적인 분석 및 조치 업무를, **사전에 정의된 플레이북(Playbook)을 통해 '오케스트레이션(연동)'하고 '자동화(Automation)'하여 '빠르게 대응(Response)'하는 통합 보안 플랫폼**.
* **도입 배경:** 기업 내에 방화벽, IPS, 백신 등 수십 개의 보안 솔루션이 난립하여 관리가 파편화되었고, 매일 쏟아지는 수만 건의 과잉 알람(Alert Fatigue)으로 인해 보안 인력의 피로도와 초동 대처 지연이 한계에 달했기 때문.

#### **II. \[본론 1] (단순화 버전) 기계가 스스로 조치하는 SOAR의 자동화 파이프라인 (도식화)**

SIEM이 던져준 알람을 받아 플레이북대로 1초 만에 장비들을 연동해 방어하는 흐름을 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4NDIuNzkzOTk5OTk5OTk5OSA2NDIiIHdpZHRoPSI4NDIuNzkzOTk5OTk5OTk5OSIgaGVpZ2h0PSI2NDIiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IlNPQVJfU2VjdXJpdHlfT3JjaGVzdHJhdGlvbl9BdXRvbWF0aW9uX2FuZF9SZXNwb25zZSIgZGF0YS1sYWJlbD0iU09BUiAoU2VjdXJpdHkgT3JjaGVzdHJhdGlvbiwgQXV0b21hdGlvbiBhbmQgUmVzcG9uc2UpIj4KICA8cmVjdCB4PSIxMzAuMTA4IiB5PSIxNDEuOCIgd2lkdGg9IjIwMC44NDIiIGhlaWdodD0iMjUwLjEiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSIxMzAuMTA4IiB5PSIxNDEuOCIgd2lkdGg9IjIwMC44NDIiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjE0Mi4xMDgiIHk9IjE1NS44IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPlNPQVIgKFNlY3VyaXR5IE9yY2hlc3RyYXRpb24sIEF1dG9tYXRpb24gYW5kIFJlc3BvbnNlKTwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQVVUTyIgZGF0YS10bz0iRklSRVdBTEwiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iuuwqe2ZlOuyvSBBUEkg7Zi47LacIiBwb2ludHM9IjM4My4xMjE5OTk5OTk5OTk5LDQ0OC43OTk5OTk5OTk5OTk5NSAzODMuMTIxOTk5OTk5OTk5OSw0NjAuNzk5OTk5OTk5OTk5OTUgMTQ4LjA0MjQ5OTk5OTk5OTksNDYwLjc5OTk5OTk5OTk5OTk1IDE0OC4wNDI0OTk5OTk5OTk5Myw1NTMuMDk5OTk5OTk5OTk5OSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQVVUTyIgZGF0YS10bz0iVkFDQ0lORSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i67Cx7IugIEFQSSDtmLjstpwiIHBvaW50cz0iNDAyLjUwMTQ5OTk5OTk5OTksNDQ4Ljc5OTk5OTk5OTk5OTk1IDQwMi41MDE0OTk5OTk5OTk5LDU1My4wOTk5OTk5OTk5OTk5IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBVVRPIiBkYXRhLXRvPSJNU0ciIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyKrOuemSBBUEkg7Zi47LacIiBwb2ludHM9IjQyMS44ODA5OTk5OTk5OTk5LDQ0OC43OTk5OTk5OTk5OTk5NSA0MjEuODgwOTk5OTk5OTk5ODYsNDYwLjc5OTk5OTk5OTk5OTk1IDY3NS44NTU5OTk5OTk5OTk5LDQ2MC43OTk5OTk5OTk5OTk5NSA2NzUuODU1OTk5OTk5OTk5OSw1NTMuMDk5OTk5OTk5OTk5OSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQUxFUlQiIGRhdGEtdG89IlNPQVIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjMwLjYwOCw5My44MDAwMDAwMDAwMDAwMSAyMzAuNjA4LDE0MS44IDIzMC42MDgsMTg1LjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlNPQVIiIGRhdGEtdG89IlBMQVlCT09LIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIxLiDsgqzsoITsl5Ag7KCV7J2Y65CcICftlIzroIjsnbTrtoEnIOyekeuPmSIgcG9pbnRzPSIyMzAuNjA4LDIyMi43MDAwMDAwMDAwMDAwMiAyMzAuNjA4LDMzOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJBVVRPIiBkYXRhLXRvPSJGSVJFV0FMTCIgZGF0YS1sYWJlbD0i67Cp7ZmU67K9IEFQSSDtmLjstpwiPgogIDxyZWN0IHg9Ijk5LjA0MjQ5OTk5OTk5OTg5IiB5PSI0NjcuNzk5OTk5OTk5OTk5OTUiIHdpZHRoPSI5Ny4yNDYwMDAwMDAwMDAwMSIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjE0Ny42NjU0OTk5OTk5OTk5IiB5PSI0ODIuOTQ5OTk5OTk5OTk5OTMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuuwqe2ZlOuyvSBBUEkg7Zi47LacPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkFVVE8iIGRhdGEtdG89IlZBQ0NJTkUiIGRhdGEtbGFiZWw9IuuwseyLoCBBUEkg7Zi47LacIj4KICA8cmVjdCB4PSIzNTkuNTAxNDk5OTk5OTk5OSIgeT0iNDkxLjc5OTk5OTk5OTk5OTk1IiB3aWR0aD0iODUuMzY2MDAwMDAwMDAwMDEiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI0MDIuMTg0NDk5OTk5OTk5OSIgeT0iNTA2Ljk0OTk5OTk5OTk5OTkzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7rsLHsi6AgQVBJIO2YuOy2nDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJBVVRPIiBkYXRhLXRvPSJNU0ciIGRhdGEtbGFiZWw9IuyKrOuemSBBUEkg7Zi47LacIj4KICA8cmVjdCB4PSI2MzIuODU1OTk5OTk5OTk5OSIgeT0iNDY3Ljc5OTk5OTk5OTk5OTk1IiB3aWR0aD0iODUuMzY2MDAwMDAwMDAwMDEiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI2NzUuNTM4OTk5OTk5OTk5OSIgeT0iNDgyLjk0OTk5OTk5OTk5OTkzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7siqzrnpkgQVBJIO2YuOy2nDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJTT0FSIiBkYXRhLXRvPSJQTEFZQk9PSyIgZGF0YS1sYWJlbD0iMS4g7IKs7KCE7JeQIOygleydmOuQnCAn7ZSM66CI7J2067aBJyDsnpHrj5kiPgogIDxyZWN0IHg9IjE0Mi4xMDgiIHk9IjI2NS43MDAwMDAwMDAwMDAwNSIgd2lkdGg9IjE3Ni44NDIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyMzAuNTI5IiB5PSIyODAuODUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjEuIOyCrOyghOyXkCDsoJXsnZjrkJwgJiMzOTvtlIzroIjsnbTrtoEmIzM5OyDsnpHrj5k8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkFMRVJUIiBkYXRhLWxhYmVsPSLquLDsobQgU0lFTSDsi5zsiqTthZwg8J+aqAon7JWF7ISxIElQIOy5qO2IrCDslYzrnowg67Cc7IOdISciIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTM1LjUzMzAwMDAwMDAwMDAyIiB5PSI0MCIgd2lkdGg9IjE5MC4xNDk5OTk5OTk5OTk5OCIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjMwLjYwOCIgeT0iNjYuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMjMwLjYwOCIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuq4sOyhtCBTSUVNIOyLnOyKpO2FnCDwn5qoPC90c3Bhbj48dHNwYW4geD0iMjMwLjYwOCIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+JiMzOTvslYXshLEgSVAg7Lmo7YisIOyVjOuejCDrsJzsg50hJiMzOTs8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQVVUTyIgZGF0YS1sYWJlbD0iQVVUTyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzNjMuNzQyNDk5OTk5OTk5OSIgeT0iNDExLjkiIHdpZHRoPSI3Ny41MTgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQwMi41MDE0OTk5OTk5OTk5IiB5PSI0MzAuMzQ5OTk5OTk5OTk5OTciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkFVVE88L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkZJUkVXQUxMIiBkYXRhLWxhYmVsPSLrsKntmZTrsr06IO2VtOuLuSBJUCDsponqsIEg7LCo64uoIPCfp7EiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzkuOTk5OTk5OTk5OTk5OTQiIHk9IjU1My4wOTk5OTk5OTk5OTk5IiB3aWR0aD0iMjE2LjA4NDk5OTk5OTk5OTk4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNDguMDQyNDk5OTk5OTk5OTMiIHk9IjU3MS41NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+67Cp7ZmU67K9OiDtlbTri7kgSVAg7KaJ6rCBIOywqOuLqCDwn6exPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJWQUNDSU5FIiBkYXRhLWxhYmVsPSLrsLHsi6A6IOyngeybkCBQQyDslYXshLHsvZTrk5wg7IKt7KCcIPCfkokiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjg0LjA4NDk5OTk5OTk5OTkiIHk9IjU1My4wOTk5OTk5OTk5OTk5IiB3aWR0aD0iMjM2LjgzMyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDAyLjUwMTQ5OTk5OTk5OTkiIHk9IjU3MS41NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+67Cx7IugOiDsp4Hsm5AgUEMg7JWF7ISx7L2U65OcIOyCreygnCDwn5KJPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJNU0ciIGRhdGEtbGFiZWw9IuuplOyLoOyggDog64u064u57J6Q7JeQ6rKMIOqysOqzvCDrs7Tqs6Ag4pyJ77iPIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU0OC45MTc5OTk5OTk5OTk5IiB5PSI1NTMuMDk5OTk5OTk5OTk5OSIgd2lkdGg9IjI1My44NzU5OTk5OTk5OTk5OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNjc1Ljg1NTk5OTk5OTk5OTkiIHk9IjU3MS41NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+66mU7Iug7KCAOiDri7Tri7nsnpDsl5Dqsowg6rKw6rO8IOuztOqzoCDinInvuI88L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9InN0eWxlIiBkYXRhLWxhYmVsPSJzdHlsZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI3MC4xMDgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI3NS4wNTQiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5zdHlsZTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU09BUiIgZGF0YS1sYWJlbD0iU09BUiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxOTEuODQ5IiB5PSIxODUuOCIgd2lkdGg9Ijc3LjUxOCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIyMzAuNjA4IiB5PSIyMDQuMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlNPQVI8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlBMQVlCT09LIiBkYXRhLWxhYmVsPSJQTEFZQk9PSyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxNzQuMDY1IiB5PSIzMzkiIHdpZHRoPSIxMTMuMDg2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjMwLjYwOCIgeT0iMzU3LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5QTEFZQk9PSzwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 경보기(SIEM) vs 해결사(SOAR) 전격 비교 해부 (3단 표)**

SOAR가 SIEM의 한계를 어떻게 극복하고 \*\*'대응의 자동화'\*\*를 이루어냈는지를 대조하는 것이 핵심입니다.

| **핵심 척도 (비교 잣대)**           | **🚨 SIEM (보안 정보 및 이벤트 관리)**                                                                                                                | **🤖 SOAR (보안 자동화 및 대응 플랫폼)**                                                                                                  |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------- |
| **플랫폼의 절대 목표 및 핵심 기능**      | **'로그 수집과 상관관계 분석을 통한 탐지(Detection)'.** 수많은 서버와 네트워크 장비의 로그를 한곳에 모아 빅데이터 기반으로 분석하여, "여기 이상한 트래픽이 있습니다!" 하고 관리자에게 **경고(Alert)를 띄워주는 역할**을 함. | **'수많은 보안 솔루션의 연동 및 자동 대응(Response)'.** SIEM이 띄운 경고를 넘겨받아, 사람이 하던 귀찮고 반복적인 조치(IP 차단, 메일 삭제 등)를 **기계가 대신 자동으로 수행해 주는 역할**을 함.   |
| **업무 처리 방식과 사람(보안 요원)의 역할** | **\[수동 (Manual) 조치]** SIEM이 알람을 주면, 결국 보안 담당자가 눈으로 확인하고 방화벽 콘솔에 직접 접속해서 차단 룰을 입력하는 **'사람의 수동 노동'이 필수적**임.                                   | **\[자동화 (Automation) 조치]** 표준화된 대응 시나리오인 \*\*'플레이북(Playbook)'\*\*에 따라, 90% 이상의 단순 알람은 사람의 개입(Zero-touch) 없이 기계가 1초 만에 알아서 처리함. |
| **타 시스템과의 상호 작용 및 연동성**     | 수많은 장비로부터 로그를 \*\*'일방적으로 받아오기(수집)'\*\*만 함.                                                                                                  | 수많은 보안 장비(방화벽, 백신 등)와 API로 양방향 연결되어, 해당 장비에 \*\*'직접 명령(Orchestration)을 내리고 조종'\*\*함.                                           |
| **운영 효과 및 장점**              | 심층적인 로그 분석과 침해 사고의 근본 원인(Root Cause) 추적에 탁월함.                                                                                               | **'보안 담당자의 알람 피로도(Alert Fatigue) 극적 해소'.** 사고 대응 시간(MTTR)을 수 시간에서 수 초 단위로 단축시킴.                                                |

#### **IV. \[결론/제언] CTI(위협 인텔리전스)와 결합한 차세대 SOC(보안 관제)의 완성**

* **(키워드 위주 2줄 마무리)** "SOAR는 SIEM을 대체하는 것이 아니라, SIEM의 '탐지 능력'에 '행동 능력'을 부여하는 완벽한 파트너입니다. 현대의 보안 관제(SOC)는 **SIEM(두뇌)과 SOAR(손발), 그리고 최신 해커의 동향을 알려주는 CTI(위협 인텔리전스)가 삼위일체로 결합되어 인공지능 기반의 자율 방어 체계로 진화하고 있습니다.**"
