### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (CBD 정의, 등장배경) — 3~4줄
Ⅱ. 핵심개념 - 컴포넌트의 특성 (본론①, 도식 1개 필수)
Ⅲ. CBD 개발프로세스 (본론②, 핵심 배점)
Ⅳ. 장단점 및 재사용성 확보전략
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 폭포수·V모델은 '매 프로젝트마다 처음부터 새로 만든다'는 전제였는데, CBD는 '한번 잘 만든 독립적 조각(컴포넌트)을 여러 프로젝트에서 재사용하자'는 전제로 시작한다"\*\*는 한 줄로 시작하면, 왜 CBD가 완전히 다른 발상인지 논리가 섭니다.

### Ⅱ. 핵심개념 — 컴포넌트의 특성 "독·재·표"

| 특성          | 내용                                                                    |
| :---------- | :-------------------------------------------------------------------- |
| **독립성**     | 컴포넌트는 **자체완결적**(내부구현을 캡슐화), 다른부분과 느슨하게 연결                             |
| **재사용성**    | 한번 개발한 컴포넌트를 **여러 시스템에서 반복사용** 가능                                     |
| **표준인터페이스** | 컴포넌트간 연결은 \*\*정해진 인터페이스(API)\*\*로만 이루어짐 — 내부구현이 바뀌어도 인터페이스만 유지되면 문제없음 |

→ 암기: **"혼자서도 완결되고(독립), 여기저기 다시 쓸 수 있고(재사용), 정해진 규격으로만 이어붙인다(표준)"** — 앞서 다룬 "모듈러 아키텍처(RISC-V의 확장구조)"나 "CXL의 서브프로토콜"처럼, **레고블록처럼 조립하는 철학**이 소프트웨어개발방법론에 적용된 것입니다.

### 도식화 제안

```
[컴포넌트A]──표준인터페이스──[컴포넌트B]──표준인터페이스──[컴포넌트C]
(로그인모듈)                  (결제모듈)                  (알림모듈)

각 컴포넌트는 내부구현을 몰라도 되고, 
인터페이스만 맞으면 다른 프로젝트에서도 그대로 재사용가능
```

### Ⅲ. CBD 개발프로세스 — "요·식·개·조·시" (5단계)

| 단계            | 내용                                                               |
| :------------ | :--------------------------------------------------------------- |
| **요구분석**      | 시스템요구사항 정의(SDLC 공통단계와 동일)                                        |
| **컴포넌트식별**    | 요구사항을 \*\*재사용가능한 단위(컴포넌트)\*\*로 분해                                |
| **컴포넌트개발/구매** | 기존 \*\*재사용저장소(Repository)\*\*에서 가져오거나, 없으면 **신규개발**(COTS 구매도 포함) |
| **조립**        | 식별된 컴포넌트들을 **표준인터페이스로 연결**해 시스템구성                                |
| **시험**        | 조립된 전체시스템 테스트                                                    |

→ 암기: **"요구를 쪼개서 컴포넌트단위로 나누고, 있으면 가져오고 없으면 만들고, 이어붙이고, 검증한다"** — 핵심은 **"개발(Development)"이 아니라 "조립(Assembly)"이 중심동작**이라는 점입니다.

### Ⅳ. 장단점 및 재사용성 확보전략

| 구분            | 내용                                                                                       |
| :------------ | :--------------------------------------------------------------------------------------- |
| **장점**        | **개발기간·비용단축**(이미있는걸 재사용), **품질향상**(검증된컴포넌트 재사용), **유지보수용이**(컴포넌트단위로 독립교체가능)              |
| **단점**        | **초기구축비용 큼**(재사용가능한 컴포넌트저장소를 만드는 것 자체가 투자), 표준화부족시 **호환성문제**, 과도한 일반화는 **성능저하**(범용성의 대가) |
| **재사용성 확보전략** | **컴포넌트저장소(Repository) 구축·관리**, 조직차원의 **컴포넌트표준수립**, CBD성과를 위한 **거버넌스체계**(누가 만들고 누가 검증하는지) |

→ 앞서 다룬 "CoE"가 왜 필요했는지의 논리(표준을 만드는 조직)가 여기서 \*\*"컴포넌트저장소 관리 주체"\*\*로 다시 등장합니다 — 컴포넌트를 잘 재사용하려면, 결국 그걸 관장하는 CoE같은 조직이 필요하다는 연결입니다.

### Ⅴ. 결론 포인트 (오늘 SDLC 시리즈 최종연결)

CBD의 본질은 \*\*"매번 처음부터 만드는 대신, 검증된 조각을 재사용해 개발속도와 품질을 동시에 확보하는 것"\*\*입니다 — 이는 오늘 다룬 폭포수(순차개발)·나선형(반복개발)·V모델(단계별검증)이 모두 \*\*"어떻게 새로 만드는가"\*\*에 초점을 맞췄던 것과 달리, CBD는 \*\*"애초에 새로 만들지 않는 방법"\*\*을 추구한다는 점에서 SDLC 논의의 또 다른 차원을 열어줍니다 — 오늘 하루 다룬 개발방법론 시리즈가 결국 \*\*"어떻게 만드는가"\*\*부터 \*\*"굳이 만들지 말고 어떻게 재사용하는가"\*\*까지 확장되며 완결됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "자동차를 만들 때, 바퀴와 엔진을 매번 쇠를 녹여서 처음부터 새로 만들지 않는다. 이미 안전성이 검증된 '부품(Component)'들을 가져다 뼈대에 조립만 하면 튼튼한 자동차가 금방 완성된다. 제조업의 이 위대한 조립 철학을 소프트웨어 코딩에 그대로 가져온 것이 바로 \*\*'CBD(컴포넌트 기반 개발) 방법론'**이다. CBD는 바닥부터 코딩하는 대신, '로그인', '결제', '장바구니' 같은 독립적인 덩어리 블록(컴포넌트)들을 레고처럼 뚝딱 조립해 앱을 완성한다. 이 방법론은 철저하게 두 가지 공정(Two-Track)으로 돌아간다. 공장에서 쓸만한 부품을 깎아서 저장소(Repository)에 모아두는 과정**(CD 공정: For Reuse)**이 있고, 저장소에서 부품을 꺼내 조립하여 최종 제품을 완성하는 과정**(CBSD 공정: With Reuse)\*\*이 분리되어 있다. 이 방식은 개발 속도를 획기적으로 단축하고 이미 검증된 블록을 쓰므로 버그가 없다. 나중에 고장이 나도 그 부품만 쏙 빼서 새 버전으로 갈아 끼우면(플러그인) 되니 유지보수도 환상적이다. 하지만 처음에 이 완벽한 레고 블록들을 설계해서 저장소를 구축하는 초기 비용(Overhead)이 너무 크다는 치명적 한계가 있다. 이 조립 철학은 현대 클라우드의 마이크로서비스(MSA)로 완벽히 계승되었다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 바닥부터 짜지 마라, 레고 블록 조립의 마법 CBD 개요**

* **정의:** 어플리케이션을 맨바닥에서 코딩하는 대신, **사전에 개발되고 검증된 독립적인 기능 모듈(컴포넌트)들을 검색하여 레고 블록처럼 '조립'함으로써 새로운 소프트웨어를 구축하는 재사용 중심의 소프트웨어 공학 방법론**.
* **핵심 철학:** **'재사용성(Reusability) 극대화'**. 내부 로직은 철저히 숨기고(블랙박스), 명확하게 정의된 \*\*'인터페이스(Interface)'\*\*만을 통해 부품 간에 통신하며, 언제든 다른 부품으로 갈아 끼울 수 있는 '교체 가능성'을 지향함.

#### **II. \[본론 1] 공급자(CD)와 수요자(CBSD)의 투 트랙(Two-Track) 공정 (도식화)**

CBD의 가장 큰 특징인 '만드는 쪽'과 '조립하는 쪽'의 분리 아키텍처입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzOTguMDM1IDgyMy4zIiB3aWR0aD0iMzk4LjAzNSIgaGVpZ2h0PSI4MjMuMyIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMV9DRF9Db21wb25lbnRfRGV2ZWxvcG1lbnRfX18iIGRhdGEtbGFiZWw9IjEuIENEIChDb21wb25lbnQgRGV2ZWxvcG1lbnQpIDog6rO16riJ7J6QIOq0gOygkCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMzAzLjIxNTAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMxNC41IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMzAzLjIxNTAwMDAwMDAwMDAzIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+MS4gQ0QgKENvbXBvbmVudCBEZXZlbG9wbWVudCkgOiDqs7XquInsnpAg6rSA7KCQPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMl9DQlNEX0NCX1NvZnR3YXJlX0RldmVsb3BtZW50X19fIiBkYXRhLWxhYmVsPSIyLiBDQlNEIChDQiBTb2Z0d2FyZSBEZXZlbG9wbWVudCkgOiDsiJjsmpTsnpAg6rSA7KCQIj4KICA8cmVjdCB4PSIxMTQuMzk2MDAwMDAwMDAwMDIiIHk9IjQ4Mi44IiB3aWR0aD0iMjQzLjYzOSIgaGVpZ2h0PSIzMDAuNSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjExNC4zOTYwMDAwMDAwMDAwMiIgeT0iNDgyLjgiIHdpZHRoPSIyNDMuNjM5IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxMjYuMzk2MDAwMDAwMDAwMDIiIHk9IjQ5Ni44IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjIuIENCU0QgKENCIFNvZnR3YXJlIERldmVsb3BtZW50KSA6IOyImOyalOyekCDqtIDsoJA8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkMiIGRhdGEtdG89IkQiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLqsoDsg4kg67CPIOy2lOy2nCIgcG9pbnRzPSIyMzYuMjE1NTAwMDAwMDAwMDIsMzM4LjUgMjM2LjIxNTUwMDAwMDAwMDAyLDUyNi44IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkEiIGRhdGEtdG89IkIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjM2LjIxNTUwMDAwMDAwMDAyLDEyMC45IDIzNi4yMTU1MDAwMDAwMDAwMiwxNjguOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQiIgZGF0YS10bz0iQyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyMzYuMjE1NTAwMDAwMDAwMDIsMjIyLjcwMDAwMDAwMDAwMDAyIDIzNi4yMTU1MDAwMDAwMDAwMiwyNzAuNzAwMDAwMDAwMDAwMDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkQiIGRhdGEtdG89IkUiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjM2LjIxNTUwMDAwMDAwMDAyLDU4MC42IDIzNi4yMTU1MDAwMDAwMDAwMiw2MjguNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRSIgZGF0YS10bz0iRiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyMzYuMjE1NTAwMDAwMDAwMDIsNjgyLjQwMDAwMDAwMDAwMDEgMjM2LjIxNTUwMDAwMDAwMDAyLDczMC40MDAwMDAwMDAwMDAxIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkMiIGRhdGEtdG89IkQiIGRhdGEtbGFiZWw9IuqygOyDiSDrsI8g7LaU7LacIj4KICA8cmVjdCB4PSIxOTUuNzE1NTAwMDAwMDAwMDIiIHk9IjQwMy41IiB3aWR0aD0iODAuNjE0IiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjM2LjAyMjUwMDAwMDAwMDA0IiB5PSI0MTguNjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuqygOyDiSDrsI8g7LaU7LacPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBIiBkYXRhLWxhYmVsPSLrj4TrqZTsnbgg67aE7ISdIOuwjyDshKTqs4QiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTUyLjYyNiIgeT0iODQiIHdpZHRoPSIxNjcuMTc5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjM2LjIxNTUwMDAwMDAwMDAyIiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuuPhOuplOyduCDrtoTshJ0g67CPIOyEpOqzhDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQiIgZGF0YS1sYWJlbD0i7J6s7IKs7JqpIOqwgOuKpe2VnArsu7Ttj6zrhIztirgg7LaU7LacIOuwjyDqsJzrsJwiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTQ1LjIxNiIgeT0iMTY4LjkiIHdpZHRoPSIxODEuOTk5IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyMzYuMjE1NTAwMDAwMDAwMDIiIHk9IjE5NS44IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIyMzYuMjE1NTAwMDAwMDAwMDIiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7snqzsgqzsmqkg6rCA64ql7ZWcPC90c3Bhbj48dHNwYW4geD0iMjM2LjIxNTUwMDAwMDAwMDAyIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7su7Ttj6zrhIztirgg7LaU7LacIOuwjyDqsJzrsJw8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQyIgZGF0YS1sYWJlbD0i7Lu07Y+s64SM7Yq4IOyggOyepeyGjApSZXBvc2l0b3J5IOyXkCDrk7HroZ0iIGRhdGEtc2hhcGU9ImN5bGluZGVyIj4KICA8cmVjdCB4PSIxNTguMTgzNDk5OTk5OTk5OTgiIHk9IjI3Ny43MDAwMDAwMDAwMDAwNSIgd2lkdGg9IjE1Ni4wNjQwMDAwMDAwMDAwMiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMSIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0ibm9uZSIgLz4KICA8bGluZSB4MT0iMTU4LjE4MzQ5OTk5OTk5OTk4IiB5MT0iMjc3LjcwMDAwMDAwMDAwMDA1IiB4Mj0iMTU4LjE4MzQ5OTk5OTk5OTk4IiB5Mj0iMzMxLjUwMDAwMDAwMDAwMDA2IiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8bGluZSB4MT0iMzE0LjI0NzUiIHkxPSIyNzcuNzAwMDAwMDAwMDAwMDUiIHgyPSIzMTQuMjQ3NSIgeTI9IjMzMS41MDAwMDAwMDAwMDAwNiIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPGVsbGlwc2UgY3g9IjIzNi4yMTU1IiBjeT0iMzMxLjUwMDAwMDAwMDAwMDA2IiByeD0iNzguMDMyMDAwMDAwMDAwMDEiIHJ5PSI3IiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPGVsbGlwc2UgY3g9IjIzNi4yMTU1IiBjeT0iMjc3LjcwMDAwMDAwMDAwMDA1IiByeD0iNzguMDMyMDAwMDAwMDAwMDEiIHJ5PSI3IiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjM2LjIxNTUiIHk9IjMwNC42IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIyMzYuMjE1NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuy7tO2PrOuEjO2KuCDsoIDsnqXshow8L3RzcGFuPjx0c3BhbiB4PSIyMzYuMjE1NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+UmVwb3NpdG9yeSDsl5Ag65Ox66GdPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik5vdGUiIGRhdGEtbGFiZWw9Ik5vdGUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iNjguNjI2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iOTAuMzEzIiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk5vdGU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkQiIGRhdGEtbGFiZWw9IuyalOq1rOyCrO2VrSDrtoTshJ0g67CPCuyVhO2CpO2FjeyymCDshKTqs4QiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTYxLjE0NzUwMDAwMDAwMDA0IiB5PSI1MjYuOCIgd2lkdGg9IjE1MC4xMzYiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyMzYuMjE1NTAwMDAwMDAwMDIiIHk9IjU1My42OTk5OTk5OTk5OTk5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIyMzYuMjE1NTAwMDAwMDAwMDIiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7smpTqtazsgqztla0g67aE7ISdIOuwjzwvdHNwYW4+PHRzcGFuIHg9IjIzNi4yMTU1MDAwMDAwMDAwMiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7JWE7YKk7YWN7LKYIOyEpOqzhDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJFIiBkYXRhLWxhYmVsPSLsu7Ttj6zrhIztirgg7KGw66a9IOuwjyDqsrDtlakKQXNzZW1ibHkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTQ1LjIxNiIgeT0iNjI4LjYiIHdpZHRoPSIxODEuOTk5IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjIzNi4yMTU1MDAwMDAwMDAwMiIgeT0iNjU1LjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjIzNi4yMTU1MDAwMDAwMDAwMiIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuy7tO2PrOuEjO2KuCDsobDrpr0g67CPIOqysO2VqTwvdHNwYW4+PHRzcGFuIHg9IjIzNi4yMTU1MDAwMDAwMDAwMiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+QXNzZW1ibHk8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRiIgZGF0YS1sYWJlbD0i7LWc7KKFIOyVoO2UjOumrOy8gOydtOyFmCDsmYTshLEg8J+agCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMzAuMzk2MDAwMDAwMDAwMDIiIHk9IjczMC40MDAwMDAwMDAwMDAxIiB3aWR0aD0iMjExLjYzOSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjIzNi4yMTU1MDAwMDAwMDAwMiIgeT0iNzQ4Ljg1MDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuy1nOyihSDslaDtlIzrpqzsvIDsnbTshZgg7JmE7ISxIPCfmoA8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] CBD를 완성하는 3대 핵심 속성 및 장단점 (요청 3단 표)**

| **분류**              | **세부 항목**                  | **상세 설명 및 특징**                                                                                                                      |
| :------------------ | :------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| **컴포넌트의 핵심 속성**     | **1. 인터페이스(Interface) 중심** | 내부 소스코드를 몰라도(블랙박스), 밖으로 열려있는 인터페이스 규약만 맞추면 조립 가능.                                                                                   |
| <br />              | **2. 조립/교체 가능성**           | 특정 컴포넌트가 낡거나 고장 나면, 시스템 전체를 뜯지 않고 그 부품만 쏙 뽑아 업그레이드 가능.                                                                              |
| <br />              | **3. 독립적 배포 단위**           | 다른 모듈과 강하게 결합되지 않아 독립적으로 배포 및 실행이 가능한 완전한 기능 덩어리임.                                                                                  |
| **방법론의 양면성 (장/단점)** | **압도적인 장점 🚀**             | 1. **생산성/비용:** 다 만들어진 부품을 가져다 쓰므로 개발 속도가 비약적으로 단축됨. 2. **품질 보증:** 이미 남들이 써보고 에러를 잡은 검증된 부품이므로 결함 확률 극소화.                            |
| <br />              | **치명적인 단점 🚨**             | 1. **초기 비용 낭비:** 처음에 쓸만한 컴포넌트를 식별하고 저장소를 구축하는 데 돈과 시간이 과하게 듦. 2. **버전 충돌:** 내가 원하는 딱 맞는 부품이 없을 수 있으며, 컴포넌트 간 버전 호환성(의존성) 문제가 자주 터짐. |

#### **IV. \[결론/제언] CBD의 사상적 진화: 객체지향(OOP) ➔ CBD ➔ 마이크로서비스(MSA)**

* **(키워드 위주 2줄 마무리)** "과거의 객체지향(OOP)이 '클래스 단위'의 작은 재사용성에 머물렀다면, CBD는 이를 비즈니스 기능 단위의 거대한 '블록(컴포넌트) 재사용'으로 끌어올렸습니다. 이러한 느슨한 결합(Loose Coupling)과 독립적 배포라는 CBD의 위대한 철학은, 현대 클라우드 네이티브 환경에서 API로 통신하는 **마이크로서비스 아키텍처(MSA, Microservices Architecture)로 완벽하게 계승되어 진화**하였습니다."
