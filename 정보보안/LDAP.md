### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (LDAP정의,디렉토리서비스와의관계) — 3~4줄
Ⅱ. 계층구조 - DIT (본론①, 도식 1개 필수)
Ⅲ. 핵심동작 - Bind와검색 (본론②, 핵심 배점)
Ⅳ. 활용사례및SSO연결
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬RBAC/ABAC가'사용자-역할-권한'매핑을계산하려면, 그정보(사용자목록,조직도,그룹)가어딘가에저장되어있어야한다 — 그저장소가디렉토리서비스이고,LDAP(LightweightDirectoryAccessProtocol)는 그디렉토리서비스에접근하는표준프로토콜"\*\*이라는한줄로시작하면, 왜LDAP가 접근통제답안들뒤에오는지논리가섭니다.

### Ⅱ. 계층구조 — DIT(디렉토리정보트리)

| 개념                                 | 내용                        |
| :--------------------------------- | :------------------------ |
| **DIT**(DirectoryInformationTree)  | 조직의 전체정보를 **계층적트리구조**로표현  |
| **DN**(DistinguishedName)          | 트리안의 **각항목을고유하게식별**하는전체경로 |
| **RDN**(RelativeDistinguishedName) | DN을구성하는 **각단계의이름조각**      |

→ 암기: **"회사조직도처럼계층적으로데이터를쌓아두고, 전체경로(DN)로 각사람·부서를고유하게찾는다"** — 앞서다룬 **"UML의패키지다이어그램"**(계층적그룹화)와 유사한 **트리구조**가, 여기서는 **실제조직의사람·자원**을담는용도로쓰입니다.

### 도식화 제안

```
[dc=company,dc=com]  ← 최상위(도메인)
        │
   [ou=Sales] [ou=Engineering]  ← 조직단위(부서)
        │            │
   [cn=김철수]    [cn=이영희]  ← 개별사용자

DN 예시: cn=김철수,ou=Sales,dc=company,dc=com
(이경로전체가 김철수를 고유하게가리키는 "주소")
```

### Ⅲ. 핵심동작 — Bind와검색, 핵심 배점

**함정 방지: "데이터를저장한다"고만답하면절반. 앞서다룬"식별/인증"이 LDAP에서구체적으로어떻게실행되는지 보여줘야완성됩니다.**

| 연산                    | 내용                                                                                   |
| :-------------------- | :----------------------------------------------------------------------------------- |
| **Bind**(바인드)         | 클라이언트가 **DN+비밀번호**로 **서버에인증** — 앞서다룬\*\*"식별(DN제시)+인증(비밀번호검증)"\*\*이 여기서 **한번의연산으로실행** |
| **Search**(검색)        | 특정 **필터조건**(예:"부서=Sales")으로 **디렉토리트리를조회**                                            |
| **Add/Modify/Delete** | 항목추가·수정·삭제                                                                           |

→ 암기: **"Bind로'나는누구고,비밀번호는이거다'를한번에증명하고, Search로 원하는정보를찾는다"** — 앞서다룬 \*\*"식별vs인증"\*\*의 두단계가, LDAP에서는 **Bind연산하나에압축**되어 실행됩니다: **"cn=김철수로바인드시도"** = 식별(DN제시)+인증(비밀번호대조) 동시수행.

### 도식화 제안

```
[클라이언트] ──Bind(DN="cn=김철수,ou=Sales,...", 비밀번호)──→ [LDAP서버]
                                                           ↓ (DN과비밀번호대조)
[클라이언트] ←──────────인증성공/실패──────────────────────
                ↓ (성공시)
[클라이언트] ──Search(필터:"부서=Sales")──→ [LDAP서버]
[클라이언트] ←──────검색결과(사용자목록)────
```

### Ⅳ. 활용사례및SSO연결

**함정 방지: "사용자정보저장소"로만끝내면절반. 실제로어떻게활용되는지, 앞서다룬여러답안과어떻게연결되는지보여줘야완성됩니다.**

| 활용                       | 내용                                                         |
| :----------------------- | :--------------------------------------------------------- |
| **중앙집중식인증**              | 여러시스템(이메일,사내포털,VPN등)이 **하나의LDAP서버**를공유해 **계정을일원화**         |
| **SSO(SingleSignOn) 연동** | 한번 **LDAP인증**을통과하면, **여러애플리케이션에재로그인없이접근**— 앞서다룬"토큰"기반흐름과결합 |
| **RBAC구현기반**             | 앞서다룬 **RBAC의역할정보**(예:"ou=Sales"그룹소속)를 LDAP의 **그룹속성**으로직접구현 |
| **대표구현체**                | **ActiveDirectory**(Microsoft),**OpenLDAP**                |

→ "앞서다룬RBAC답안에서 '역할에권한을매핑한다'고했는데, 실제로그'역할'정보(예:부서,그룹)가 바로LDAP의ou(조직단위)에저장되어있고, 접근통제시스템이 그정보를조회해서 RBAC를실행한다"는게 이답안의핵심실무연결입니다.

### Ⅴ. 결론 포인트 (보안 시리즈 최종연결)

LDAP는 \*\*"앞서다룬식별/인증(Bind)과RBAC/ABAC(역할·속성데이터)가 실제로작동하기위한 표준화된저장소및접근프로토콜"\*\*입니다 — 조직의모든사용자·그룹·권한정보를 \*\*계층적트리(DIT)\*\*로체계화하고, **Bind연산**으로 식별과인증을 한번에처리하며, 그정보를기반으로 앞서다룬 **RBAC의역할-권한매핑**이실제로구현됩니다 — 오늘하루다룬 대칭/비대칭암호→해시함수→PQC/QKD→ISMS-P→MAC/DAC/RBAC/ABAC→BLP/Biba→식별/인증→LDAP로이어지는 방대한암호·보안시리즈전체가, \*\*"이론적암호원리에서시작해, 실제조직이매일사용하는신원관리인프라"\*\*로 완결되는 하나의완전한이야기로마무리됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "당신이 직원 1만 명이 넘는 대기업에 입사했다. 회사 인트라넷, 사내 메일, 전자 결재, 사내 메신저, 심지어 회사 와이파이까지 수십 개의 시스템이 있다. 만약 이 시스템들이 각자 따로 회원가입을 받고 비밀번호를 DB에 저장한다면 어떻게 될까? 직원은 수십 개의 아이디와 비번을 외워야 하고, 인사이동이나 퇴사자가 발생할 때마다 전산 관리자는 수십 개의 DB를 돌아다니며 계정을 지우느라 미쳐버릴 것이다. 이 끔찍한 계정 파편화를 찢어버리기 위해 등장한 것이 바로 \*\*'디렉토리 서비스(Directory Service)'\*\*다. 전 직원의 아이디, 부서, 직급, 비밀번호를 거대한 중앙 '전화번호부' 서버 한 곳에 몰아넣는다. 그리고 모든 사내 시스템은 로그인 창에 입력이 들어올 때마다 이 중앙 전화번호부에 '이 직원 맞아요?'라고 물어본다. 이때, 수많은 시스템들이 중앙 전화번호부 서버에 빠르게 접속해서 정보를 검색(Search)하고 읽어올 수 있게 해주는 아주 가벼운 통신 규약(언어)이 바로 \*\*'LDAP'\*\*이다. 이름에 'Lightweight(경량)'가 붙은 이유는 과거 X.500이라는 무겁고 값비싼 통신 규약을 인터넷(TCP/IP)용으로 가볍게 다이어트 시켰기 때문이다. 일반적인 관계형 DB(Oracle 등)는 은행 계좌처럼 잦은 수정과 쓰기(트랜잭션)에 강하지만, LDAP은 전화번호부처럼 1년에 한 번 쓰일까 말까 한 수정 작업 대신, 하루에 수백만 번씩 일어나는 초고속 \*\*'검색/조회(Read)'\*\*에 극도로 최적화된 트리(Tree) 구조를 가진다. 현재 마이크로소프트의 Active Directory(AD)를 비롯해 전 세계 모든 기업의 중앙 로그인(SSO) 시스템의 핵심 심장으로 뛰고 있다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 파편화된 기업의 로그인 정보를 하나로 묶다, LDAP 개요**

* **정의:** 네트워크 상에 흩어져 있는 수많은 사용자, 시스템 자원, 부서(조직) 등의 **'디렉토리 정보'를 중앙에 모아두고, TCP/IP 위에서 아주 빠르고 가볍게 검색(조회) 및 접근할 수 있도록 설계된 인터넷 표준 프로토콜**.
* **탄생 배경:** 복잡하고 무거운 OSI 7계층 기반의 'X.500 디렉토리 서비스'를 인터넷 환경에 맞게 경량화(Lightweight)하여 탄생함.
* **주요 목적:** 기업 내 수많은 시스템의 **통합 계정 관리(IAM)**, 조직도/주소록 검색, **단일 로그인(SSO, Single Sign-On)** 인프라의 핵심 뼈대로 사용됨.

#### **II. \[본론 1] RDBMS를 압도하는 극강의 조회 속도, LDAP 계층 트리 구조 (도식화)**

관계형 표(Table)가 아닌, 조직도 같은 나무(Tree) 구조로 데이터를 저장하는 DIT(Directory Information Tree)를 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NzcuNTgxNSA2MzMuMiIgd2lkdGg9IjU3Ny41ODE1IiBoZWlnaHQ9IjYzMy4yIiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJMREFQX19fX0RJVF9fRE5fIiBkYXRhLWxhYmVsPSJMREFQ7J2YIOuUlOugie2GoOumrCDsoJXrs7Qg7Yq466asIChESVQpIOq1rOyhsOyZgCBETijqs6DsnKAg7Iud67OE66qFKSI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNDk3LjU4MTUiIGhlaWdodD0iNTUzLjIiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI0OTcuNTgxNSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPkxEQVDsnZgg65SU66CJ7Yag66asIOygleuztCDtirjrpqwgKERJVCkg6rWs7KGw7JmAIEROKOqzoOycoCDsi53rs4TrqoUpPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJST09UIiBkYXRhLXRvPSJEQzEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzg5LjMwODUsMTcwIDM4OS4zMDg1LDIxOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iREMxIiBkYXRhLXRvPSJEQzIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzg5LjMwODUsMjcxLjggMzg5LjMwODUsMzE5LjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkRDMiIgZGF0YS10bz0iT1UxIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjM4OS4zMDg1LDM3My42IDM4OS4zMDg1LDM5Ny42IDMxNi4xNzE5OTk5OTk5OTk5NywzOTcuNiAzMTYuMTcxOTk5OTk5OTk5OTcsNDIxLjYiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkRDMiIgZGF0YS10bz0iT1UyIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjM4OS4zMDg1LDM3My42IDM4OS4zMDg1LDM5Ny42IDQ2Mi40NDUsMzk3LjYgNDYyLjQ0NSw0MjEuNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iT1UxIiBkYXRhLXRvPSJDTjEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzE2LjE3MTk5OTk5OTk5OTk3LDQ3NS40MDAwMDAwMDAwMDAwMyAzMTYuMTcxOTk5OTk5OTk5OTcsNDk5LjQwMDAwMDAwMDAwMDEgMjIzLjM5ODk5OTk5OTk5OTk3LDQ5OS40MDAwMDAwMDAwMDAxIDIyMy4zOTg5OTk5OTk5OTk5Nyw1MjMuNDAwMDAwMDAwMDAwMSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iT1UxIiBkYXRhLXRvPSJDTjIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzE2LjE3MTk5OTk5OTk5OTk3LDQ3NS40MDAwMDAwMDAwMDAwMyAzMTYuMTcxOTk5OTk5OTk5OTcsNDk5LjQwMDAwMDAwMDAwMDEgNDA4Ljk0NTAwMDAwMDAwMDA1LDQ5OS40MDAwMDAwMDAwMDAxIDQwOC45NDUwMDAwMDAwMDAwNSw1MjMuNDAwMDAwMDAwMDAwMSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUk9PVCIgZGF0YS1sYWJlbD0iUm9vdCIgZGF0YS1zaGFwZT0iY2lyY2xlIj4KICA8Y2lyY2xlIGN4PSIzODkuMzA4NSIgY3k9IjEyNyIgcj0iNDMiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjM4OS4zMDg1IiB5PSIxMjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlJvb3Q8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkRDMSIgZGF0YS1sYWJlbD0iZGM9Y29tIArstZzsg4HsnIQg64+E66mU7J24IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjMyMi43NjE5OTk5OTk5OTk5NCIgeT0iMjE4IiB3aWR0aD0iMTMzLjA5MzAwMDAwMDAwMDAyIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzODkuMzA4NSIgeT0iMjQ0LjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjM4OS4zMDg1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+ZGM9Y29tIDwvdHNwYW4+PHRzcGFuIHg9IjM4OS4zMDg1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7stZzsg4HsnIQg64+E66mU7J24PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkRDMiIgZGF0YS1sYWJlbD0iZGM9bXljb21wYW55IArrj4TrqZTsnbgg7J2066aEIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjMyMS4yOCIgeT0iMzE5LjgiIHdpZHRoPSIxMzYuMDU3MDAwMDAwMDAwMDIiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjM4OS4zMDg1IiB5PSIzNDYuNyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMzg5LjMwODUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5kYz1teWNvbXBhbnkgPC90c3Bhbj48dHNwYW4geD0iMzg5LjMwODUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuuPhOuplOyduCDsnbTrpoQ8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iT1UxIiBkYXRhLWxhYmVsPSJvdT1EZXYgCuqwnOuwnO2MgCDrtoDshJwiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjU3LjAzNTQ5OTk5OTk5OTk2IiB5PSI0MjEuNiIgd2lkdGg9IjExOC4yNzMiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMzE2LjE3MTk5OTk5OTk5OTk3IiB5PSI0NDguNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMzE2LjE3MTk5OTk5OTk5OTk3IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+b3U9RGV2IDwvdHNwYW4+PHRzcGFuIHg9IjMxNi4xNzE5OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+6rCc67Cc7YyAIOu2gOyEnDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJPVTIiIGRhdGEtbGFiZWw9Im91PVNhbGVzIArsmIHsl4XtjIAg67aA7IScIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwMy4zMDg1IiB5PSI0MjEuNiIgd2lkdGg9IjExOC4yNzMiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQ2Mi40NDUiIHk9IjQ0OC41IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0NjIuNDQ1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+b3U9U2FsZXMgPC90c3Bhbj48dHNwYW4geD0iNDYyLjQ0NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7JiB7JeF7YyAIOu2gOyEnDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDTjEiIGRhdGEtbGFiZWw9ImNuPUhvbmcgCu2Zjeq4uOuPmSDsgqzsm5Ag8J+nkeKAjfCfkrsiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTQ0LjYyNTk5OTk5OTk5OTk4IiB5PSI1MjMuNDAwMDAwMDAwMDAwMSIgd2lkdGg9IjE1Ny41NDYiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMjIzLjM5ODk5OTk5OTk5OTk3IiB5PSI1NTAuMzAwMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMjIzLjM5ODk5OTk5OTk5OTk3IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+Y249SG9uZyA8L3RzcGFuPjx0c3BhbiB4PSIyMjMuMzk4OTk5OTk5OTk5OTciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPu2Zjeq4uOuPmSDsgqzsm5Ag8J+nkeKAjfCfkrs8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ04yIiBkYXRhLWxhYmVsPSJjbj1LaW0gCuq5gOyyoOyImCDsgqzsm5Ag8J+nkeKAjfCfkrsiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzMwLjE3MiIgeT0iNTIzLjQwMDAwMDAwMDAwMDEiIHdpZHRoPSIxNTcuNTQ2IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0MDguOTQ1MDAwMDAwMDAwMDUiIHk9IjU1MC4zMDAwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0MDguOTQ1MDAwMDAwMDAwMDUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5jbj1LaW0gPC90c3Bhbj48dHNwYW4geD0iNDA4Ljk0NTAwMDAwMDAwMDA1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7quYDssqDsiJgg7IKs7JuQIPCfp5HigI3wn5K7PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik5vdGUiIGRhdGEtbGFiZWw9Ik5vdGUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iNjguNjI2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iOTAuMzEzIiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk5vdGU8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 관계형 DB(RDBMS) vs LDAP 및 구형(X.500) 모델 전격 해부 (3단 표)**

LDAP이 \*\*어디에 강하고(조회), 어디에 약한지(트랜잭션)\*\*를 일반 DB와 대조하여 찌르는 것이 가장 확실한 득점 포인트입니다.

| **핵심 척도 (비교 잣대)**            | **📊 일반 관계형 데이터베이스 (RDBMS)**                                                                         | **📞 디렉토리 서비스 (LDAP)**                                                                                     |
| :--------------------------- | :--------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| **데이터 구조 및 관리 메커니즘**         | **'테이블(행과 열)' 구조.** 정규화를 통해 데이터 중복을 최소화하고, 복잡한 SQL 쿼리(JOIN 등)를 사용하여 데이터를 처리함.                        | **'트리(계층적 디렉토리)' 구조.** 기업의 실제 조직도와 똑같은 계층형 구조(DIT)를 가져, 직관적인 관리와 경로(DN) 탐색이 가능함.                           |
| **강점 (특화된 영역)**              | **'데이터 갱신(Write, Update)' 및 복잡한 트랜잭션.** 은행 송금 내역이나 재고 관리처럼 데이터가 수시로 변하고 원자성(ACID)이 극도로 중요한 시스템에 특화됨. | **'초고속 검색(Read, Search)' 특화.** 조직도나 비밀번호처럼 한 번 저장되면 잘 바뀌지 않는 대신, **하루에 수백만 번씩 발생하는 로그인(조회) 트래픽을 완벽히 감당함.** |
| **약점 및 통신 모델**               | 잦은 조회가 대량으로 발생하면 테이블 락(Lock)이나 병목 현상이 발생하여 퍼포먼스가 저하됨.                                                | 복잡한 트랜잭션 제어나 대량의 쓰기/수정 작업에는 매우 부적합함 (속도 저하 발생).                                                            |
| **구형 X.500과의 비교 및 포트(Port)** | -                                                                                                    | X.500이 OSI 7계층 전체를 써서 매우 무거웠던 반면, **LDAP은 TCP/IP 위에서 경량화되어 작동함. (기본 389, 보안 LDAPS 636 포트 사용).**            |

#### **IV. \[결론/제언] SSO(단일 로그인) 아키텍처와 마이크로소프트 Active Directory(AD)의 지배**

* **(키워드 위주 2줄 마무리)** "LDAP은 계정 파편화로 인한 관리 비용과 보안 위협(퇴사자 권한 누락 등)을 근본적으로 제거한 위대한 표준입니다. 오늘날 글로벌 기업의 90% 이상이 이 LDAP을 심장으로 삼는 **'마이크로소프트 Active Directory(AD)'를 도입하여 통합 인증(SSO)과 권한 관리를 구현하고 있으며, 나아가 클라우드 기반의 Entra ID(Azure AD)로 그 영토를 무한히 확장**해 나가고 있습니다."
