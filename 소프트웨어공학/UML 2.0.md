### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (UML 2.0 정의, 2대분류기준) — 3~4줄
Ⅱ. 구조다이어그램 7종 (본론①, 도식 1개 필수)
Ⅲ. 행위다이어그램 7종 (본론②, 핵심 배점)
Ⅳ. 앞서다룬 유스케이스의 위치 및 활용전략
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬 유스케이스다이어그램은 UML14종중'행위'를보여주는다이어그램하나일뿐 — UML은 '시스템의생김새(구조)'와'시스템의움직임(행위)'을 각각7종씩,총14종의다이어그램으로표현하는통합모델링언어"\*\*라는한줄로시작하면, 유스케이스가 왜UML의일부로소개되는지논리가섭니다.

### Ⅱ. 구조다이어그램 7종 — "정적인 모습"

| 다이어그램              | 표현대상                              |
| :----------------- | :-------------------------------- |
| **클래스**            | 클래스,속성,메서드,클래스간관계                 |
| **객체**             | 특정시점의 **인스턴스상태**스냅샷               |
| **컴포넌트**           | 시스템을이루는 **컴포넌트간의존관계**(앞서다룬CBD와연결) |
| **배치(Deployment)** | 소프트웨어가 **어느하드웨어에배치**되는지           |
| **패키지**            | 클래스들을 **패키지단위로그룹화**               |
| **복합체구조**          | 클래스내부의 **세부구성요소**                 |
| **프로파일**           | UML자체를 **확장하는커스텀스테레오타입**          |

→ 암기: \*\*"클래스,객체,컴포넌트,배치,패키지"\*\*가핵심5종 — "정적인구조를보여준다"는공통점으로, 소스코드의클래스구조나서버배치도같은 \*\*"멈춰있는사진"\*\*을그립니다.

### 도식화 제안

```
[UML 2.0]
   ┌──────┴──────┐
[구조다이어그램]        [행위다이어그램]
(정적,생김새)           (동적,움직임)
클래스/객체/컴포넌트/     유스케이스/시퀀스/액티비티/
배치/패키지/복합체/       상태머신/커뮤니케이션/
프로파일                상호작용개요/타이밍
```

### Ⅲ. 행위다이어그램 7종 — "동적인 움직임", 핵심 배점

**함정 방지: 유스케이스만알고 나머지6종을모르면절반. 시퀀스·상태머신은시험에서매우자주나오는핵심다이어그램입니다.**

| 다이어그램      | 표현대상                                        |
| :--------- | :------------------------------------------ |
| **유스케이스**  | 앞서다룬 **액터-시스템간상호작용범위**(WHAT)                |
| **시퀀스**    | 객체들간 **시간순서에따른메시지교환**(HOW,순서중요)             |
| **액티비티**   | **업무흐름/알고리즘의단계별진행**(순서도유사)                  |
| **상태머신**   | 한객체가 **상태전이**하는과정(앞서다룬MESI의M/E/S/I전이와유사원리!) |
| **커뮤니케이션** | 객체간메시지교환을 **시퀀스보다구조중심으로표현**                 |
| **상호작용개요** | **여러시퀀스/상호작용을흐름도로연결**                       |
| **타이밍**    | 상태변화를 **시간축에따라정밀하게표현**(실시간시스템용)             |

→ 암기: \*\*"유스케이스,시퀀스,액티비티,상태머신"\*\*이핵심4종 — \*\*"시퀀스는순서,액티비티는흐름,상태머신은상태전이"\*\*로구분하면헷갈리지않습니다.

### 도식화 제안

```
[시퀀스다이어그램]                [상태머신다이어그램]
객체A → 객체B : 메시지1()           [대기중] ──로그인──→ [인증중]
객체B → 객체C : 메시지2()                              ↓성공
객체C → 객체B : 반환값                              [로그인완료]
(시간이 위에서아래로흐름)          (앞서다룬MESI의M/E/S/I전이와동일원리)
```

→ 앞서다룬 \*\*"캐시일관성(MESI)"\*\*의상태전이도가, 사실UML \*\*"상태머신다이어그램"\*\*의한사례라는점을보여주면심화연결이됩니다.

### Ⅳ. 앞서다룬 유스케이스의 위치 및 활용전략

**함정 방지: "다이어그램을다그려야한다"고생각하면오해. 프로젝트단계·목적에따라 필요한것만골라쓰는게실무입니다.**

| 프로젝트단계   | 주로쓰는다이어그램           |
| :------- | :------------------ |
| **요구분석** | 유스케이스(앞서다룬그것)       |
| **설계**   | 클래스,시퀀스,컴포넌트        |
| **구현직전** | 상태머신(복잡한상태를가진객체설계시) |
| **배포계획** | 배치다이어그램             |

→ 앞서다룬 "방법론테일러링"의논리처럼, \*\*"UML14종을다그리는게아니라, 프로젝트단계와의사소통목적에맞게필요한몇개만선택한다"\*\*는게실무의정답입니다.

### Ⅴ. 결론 포인트 (요구공학·모델링 시리즈 완결)

UML 2.0은 \*\*"시스템을설명하는방법이하나가아니라, 정적(구조)과동적(행위)관점에서각각여러층위로표현할수있게 표준화한도구상자"\*\*입니다 — 앞서다룬유스케이스(요구를보여줌)는이도구상자의 \*\*입구(요구분석용)\*\*였을뿐이며, 시퀀스·상태머신·클래스다이어그램등이 그뒤를이어 \*\*"요구가어떻게시스템내부구조와동작으로구현되는지"\*\*를단계적으로구체화합니다 — 이로써 오늘다룬요구공학시리즈(도출→페르소나→사용자스토리→유스케이스)가, UML이라는더큰모델링체계의 \*\*"입구에서출구까지"\*\*로자연스럽게이어지며완결됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "건축가가 집을 지을 때 배관도, 전기 도면, 정면 조감도 등 다양한 시점의 도면을 그리듯, 수백 명의 개발자가 소프트웨어를 만들 때도 기획자, 개발자, 고객이 한눈에 보고 딴소리하지 않도록 소통할 '표준 도면'이 필요하다. 이 세계 공통 표준 모델링 언어가 바로 \*\*'UML(Unified Modeling Language)'\*\*이다. UML은 버전 2.0으로 진화하면서 현대 시스템의 복잡성을 모두 담기 위해 총 14개의 다이어그램으로 촘촘히 체계화되었다. 이 14개는 크게 두 가지 뼈대로 나뉜다. 첫째, 시간이 멈춘 상태에서 건물의 뼈대와 기둥을 보여주는 \*\*'구조적(정적) 다이어그램'\*\*이다. 가장 기본인 클래스 다이어그램이나 하드웨어 랙을 그리는 배치도 등 7가지가 있다. 둘째, 시간이 흐르면서 시스템이 어떻게 움직이고 메시지를 주고받는지 동작의 흐름을 보여주는 \*\*'행위(동적) 다이어그램'\*\*이다. 유스케이스나 순차 다이어그램 등 7가지가 있다. 특히 2.0에서는 시간 제약을 엄격히 보는 '타이밍 다이어그램'이나 내부 구조를 쪼개보는 '복합체 구조 다이어그램'이 추가되어 현대 MSA나 실시간 시스템 설계에 강력한 무기가 되었다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 소프트웨어 건축을 위한 전 세계 공통 도면, UML 2.0 개요**

* **정의:** OMG(Object Management Group)에서 제정한 표준 객체지향 모델링 언어로, 소프트웨어 시스템의 산출물을 가시화, 명세화, 구축, 문서화하기 위해 사용하는 **14가지의 표준 그래픽(다이어그램) 언어 체계**.
* **버전 2.0의 의의:** 기존 1.x 버전의 한계를 극복하고, 모델 기반 아키텍처(MDA) 지원, 실시간 임베디드 시스템 표현(타이밍 다이어그램 등), 그리고 복잡한 컴포넌트 내부 구조 표현력(복합체 구조)을 대폭 확충함.

#### **II. \[본론 1] 정적 뼈대와 동적 흐름: UML 2.0 다이어그램 분류 체계 (도식화)**

시험에서 가장 많이 묻는 7대 7 분류(구조 vs 행위)의 거시적 아키텍처입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5MTkuMzk3OTk5OTk5OTk5OSA3MzQuMDk1OTk5OTk5OTk5OSIgd2lkdGg9IjkxOS4zOTc5OTk5OTk5OTk5IiBoZWlnaHQ9IjczNC4wOTU5OTk5OTk5OTk5IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJVTUxfMjBfX19fXzE0IiBkYXRhLWxhYmVsPSJVTUwgMi4wIOuLpOydtOyWtOq3uOueqCDqs4TsuLUg7LK06rOEICjstJ0gMTTsooUpIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI4MzkuMzk3OTk5OTk5OTk5OSIgaGVpZ2h0PSI2NTQuMDk1OTk5OTk5OTk5OSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjgzOS4zOTc5OTk5OTk5OTk5IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+VU1MIDIuMCDri6TsnbTslrTqt7jrnqgg6rOE7Li1IOyytOqzhCAo7LSdIDE07KKFKTwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVU1MIiBkYXRhLXRvPSJTIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQ1Ni41NzM2NjY2NjY2NjY2LDE5MSA0NTYuNTczNjY2NjY2NjY2NiwyMTUgMjA5Ljk4NDQ5OTk5OTk5OTk3LDIxNSAyMDkuOTg0NDk5OTk5OTk5OTcsMjM5IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJVTUwiIGRhdGEtdG89IkIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDU2LjU3MzY2NjY2NjY2NjYsMTkxIDQ1Ni41NzM2NjY2NjY2NjY2LDIxNSA2MjMuNzkzMjUsMjE1IDYyMy43OTMyNSwyMzkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlMiIGRhdGEtdG89IlMxIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjIwOS45ODQ0OTk5OTk5OTk5NywzMDkuNyAyMDkuOTg0NDk5OTk5OTk5OTcsMzU3LjciIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkIiIGRhdGEtdG89IkIxIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjYyMy43OTMyNSwzMDkuNyA2MjMuNzkzMjUsMzMzLjcgNTAwLjc1MjQ5OTk5OTk5OTk0LDMzMy43IDUwMC43NTI0OTk5OTk5OTk5NCwzNTcuNyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQiIgZGF0YS10bz0iSSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI2MjMuNzkzMjUsMzA5LjcgNjIzLjc5MzI1LDMzMy43IDc0Ni44MzQsMzMzLjcgNzQ2LjgzNCwzNTcuNyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iSSIgZGF0YS10bz0iSTEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNzQ2LjgzNCw1NzYuMjk1OTk5OTk5OTk5OSA3NDYuODM0LDYyNC4yOTU5OTk5OTk5OTk5IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJVTUwiIGRhdGEtbGFiZWw9IlVNTCAyLjAiIGRhdGEtc2hhcGU9ImNpcmNsZSI+CiAgPGNpcmNsZSBjeD0iNDU2LjU3MzY2NjY2NjY2NjYiIGN5PSIxMzcuNSIgcj0iNTMuNSIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0NTYuNTczNjY2NjY2NjY2NiIgeT0iMTM3LjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlVNTCAyLjA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlMiIGRhdGEtbGFiZWw9Iuq1rOyhsOyggSDri6TsnbTslrTqt7jrnqgg8J+Pm++4jwooU3RydWN0dXJhbCAvIOygleyggSkK7Iuc6rCEIO2dkOumhCDrrLTqtIAsIOyLnOyKpO2FnCDrvIjrjIAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTAxLjU3MTQ5OTk5OTk5OTk2IiB5PSIyMzkiIHdpZHRoPSIyMTYuODI2MDAwMDAwMDAwMDIiIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyMDkuOTg0NDk5OTk5OTk5OTciIHk9IjI3NC4zNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMjA5Ljk4NDQ5OTk5OTk5OTk3IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+6rWs7KGw7KCBIOuLpOydtOyWtOq3uOueqCDwn4+b77iPPC90c3Bhbj48dHNwYW4geD0iMjA5Ljk4NDQ5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj4oU3RydWN0dXJhbCAvIOygleyggSk8L3RzcGFuPjx0c3BhbiB4PSIyMDkuOTg0NDk5OTk5OTk5OTciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyLnOqwhCDtnZDrpoQg66y06rSALCDsi5zsiqTthZwg67yI64yAPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkIiIGRhdGEtbGFiZWw9Iu2WieychCDri6TsnbTslrTqt7jrnqgg8J+Pg+KAjeKZgu+4jwooQmVoYXZpb3JhbCAvIOuPmeyggSkK7Iuc6rCEIO2dkOumhOyXkCDrlLDrpbgg7IOB7YOcL+uplOyLnOyngCDrs4DtmZQiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDkyLjc3OTc0OTk5OTk5OTkiIHk9IjIzOSIgd2lkdGg9IjI2Mi4wMjciIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI2MjMuNzkzMjUiIHk9IjI3NC4zNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNjIzLjc5MzI1IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+7ZaJ7JyEIOuLpOydtOyWtOq3uOueqCDwn4+D4oCN4pmC77iPPC90c3Bhbj48dHNwYW4geD0iNjIzLjc5MzI1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj4oQmVoYXZpb3JhbCAvIOuPmeyggSk8L3RzcGFuPjx0c3BhbiB4PSI2MjMuNzkzMjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyLnOqwhCDtnZDrpoTsl5Ag65Sw66W4IOyDge2DnC/rqZTsi5zsp4Ag67OA7ZmUPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlMxIiBkYXRhLWxhYmVsPSLtgbTrnpjsiqQsIOqwneyytCwg7Lu07Y+s64SM7Yq4LCDrsLDsuZgsCuuzte2VqeyytCDqtazsobAoMi4wKSwg7Yyo7YKk7KeAKDIuMCksIO2UhOuhnO2MjOydvCgyLjApIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIzNTcuNyIgd2lkdGg9IjMwNy45Njg5OTk5OTk5OTk5NCIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjIwOS45ODQ0OTk5OTk5OTk5NyIgeT0iMzg0LjU5OTk5OTk5OTk5OTk3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIyMDkuOTg0NDk5OTk5OTk5OTciIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7tgbTrnpjsiqQsIOqwneyytCwg7Lu07Y+s64SM7Yq4LCDrsLDsuZgsPC90c3Bhbj48dHNwYW4geD0iMjA5Ljk4NDQ5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rs7XtlanssrQg6rWs7KGwKDIuMCksIO2MqO2CpOyngCgyLjApLCDtlITroZztjIzsnbwoMi4wKTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJCMSIgZGF0YS1sYWJlbD0i7Jyg7Iqk7LyA7J207IqkLCDtmZzrj5ksIOyDge2DnCDrqLjsi6AiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzkxLjk2ODk5OTk5OTk5OTk0IiB5PSIzNTcuNyIgd2lkdGg9IjIxNy41NjY5OTk5OTk5OTk5OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjUwMC43NTI0OTk5OTk5OTk5NCIgeT0iMzc2LjE1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7snKDsiqTsvIDsnbTsiqQsIO2ZnOuPmSwg7IOB7YOcIOuouOyLoDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iSSIgZGF0YS1sYWJlbD0i7IOB7Zi47J6R7JqpIOuLpOydtOyWtOq3uOueqCDwn5KsCihJbnRlcmFjdGlvbikiIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iNzQ2LjgzNCwzNTcuNyA4NTYuMTMyLDQ2Ni45OTggNzQ2LjgzNCw1NzYuMjk1OTk5OTk5OTk5OSA2MzcuNTM2LDQ2Ni45OTgiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNzQ2LjgzNCIgeT0iNDY2Ljk5OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNzQ2LjgzNCIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuyDge2YuOyekeyaqSDri6TsnbTslrTqt7jrnqgg8J+SrDwvdHNwYW4+PHRzcGFuIHg9Ijc0Ni44MzQiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPihJbnRlcmFjdGlvbik8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iSTEiIGRhdGEtbGFiZWw9IuyInOywqCwg7Ya17IugLArtg4DsnbTrsI0oMi4wKSwg7IOB7Zi47J6R7JqpIOqwnOyalCgyLjApIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjYzMC4yNyIgeT0iNjI0LjI5NTk5OTk5OTk5OTkiIHdpZHRoPSIyMzMuMTI4IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNzQ2LjgzNCIgeT0iNjUxLjE5NTk5OTk5OTk5OTkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9Ijc0Ni44MzQiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7siJzssKgsIO2GteyLoCw8L3RzcGFuPjx0c3BhbiB4PSI3NDYuODM0IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7tg4DsnbTrsI0oMi4wKSwg7IOB7Zi47J6R7JqpIOqwnOyalCgyLjApPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] UML 2.0의 14대 다이어그램 전격 분류 표 (3단 표 - 출제 1순위)**

핵심 다이어그램의 특징과 2.0에서 새로 추가된 항목들을 매칭합니다.

| **분류 체계**                       | **주요 다이어그램 명칭**                                                       | **상세 역할 및 모델링 대상**                                                                   |
| :------------------------------ | :-------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| **구조적(정적) 🏛️** *(시스템의 명사/뼈대)*  | **1. 클래스 (Class)** **2. 배치 (Deployment)** 3. 컴포넌트 (Component)         | 1. 객체의 속성, 메서드 및 클래스 간의 관계 (기본 뼈대). 2. 서버, DB 장비 등 **물리적인 하드웨어 구성 요소의 위치**.          |
| *(UML 2.0 추가됨)*                 | **4. 복합체 구조 (Composite)** **5. 패키지 (Package)**                        | 4. 복잡한 컴포넌트나 클래스의 **내부 구조를 쪼개어 표현.** 5. 연관된 요소들을 묶은 패키지 간의 의존성 표현.                   |
| **행위(동적) 🏃‍♂️** *(시스템의 동사/흐름)* | **1. 유스케이스 (Use Case)** **2. 상태 머신 (State Machine)** 3. 활동 (Activity) | 1. **사용자(Actor) 관점**에서 시스템이 제공하는 기능 상호작용. 2. 특정 객체가 이벤트에 의해 **어떤 상태(State)로 전이**되는지. |
| **상호작용 💬** *(동적 다이어그램 소분류 체계)* | **1. 순차 (Sequence)** 2. 통신 (Communication)                            | 1. 객체들이 시간을 기준으로 어떻게 **메시지를 주고받는지** 나열. (협력 객체의 흐름 파악).                              |
| *(UML 2.0 추가됨)*                 | **3. 타이밍 (Timing)** **4. 상호작용 개요 (Overview)**                         | 3. 실시간 시스템에서 **시간 제약 조건에 따른** 상태 변화 표현. 4. 활동도와 순차도를 결합하여 전체적인 제어 흐름 표현.             |

#### **IV. \[결론/제언] 아키텍처 중심 설계 지원 및 도메인 특화 모델링(SysML)으로의 확장**

* **(키워드 위주 2줄 마무리)** "UML 2.0은 '복합체 구조'와 '타이밍' 다이어그램을 추가함으로써, 단순한 웹 개발을 넘어 **대규모 컴포넌트 기반 분산 시스템(CBD/MSA)과 하드웨어 제어 시스템 설계에 완벽히 대응**하게 되었습니다. 나아가 UML의 프로파일 기능을 확장하여 항공우주, 자동차 시스템 공학에 특화된 범용 표준인 **'SysML(Systems Modeling Language)' 및 MBSE(모델 기반 시스템 공학)로 그 위상과 철학이 거대하게 확장**되고 있습니다."
