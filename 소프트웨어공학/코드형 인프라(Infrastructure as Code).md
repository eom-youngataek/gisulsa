### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (IaC 등장배경 - 수동인프라구성의 문제) — 3~4줄
Ⅱ. 핵심원리 - 선언적 vs 명령적 (본론①, 도식 1개 필수)
Ⅲ. 주요기법 - 멱등성과 상태관리 (본론②, 핵심 배점)
Ⅳ. 도구체계 및 CI/CD와의 결합
Ⅴ. 결론
```

포인트: 개요에서 \*\*"전통적으로는 서버관리자가 콘솔에 직접 로그인해서 손으로 설정을 바꿨는데, 이러면 '어떤서버가 어떤설정인지' 아무도 정확히 모르는 스노우플레이크서버(눈송이처럼 다똑같이생겼지만 자세히보면 다다른) 문제가 생긴다 → 인프라구성을 코드로 작성해서, 소스코드처럼 버전관리·리뷰·재현이 가능하게 만든것"\*\*이라는 한 줄로 시작하면, 앞서 다룬 "CI/CD"·"방법론테일러링(코드로관리)"과 자연스럽게 이어집니다.

### Ⅱ. 핵심원리 — 선언적 vs 명령적

| 구분                   | 방식                            | 예시                                   |
| :------------------- | :---------------------------- | :----------------------------------- |
| **명령적(Imperative)**  | **"어떻게"할지 순서대로** 지시(스크립트)     | "서버생성→IP할당→방화벽설정" 순서대로명령             |
| **선언적(Declarative)** | **"무엇을"원하는지 최종상태만** 기술        | "서버1개, IP고정, 방화벽규칙X" 라고만선언, 도구가나머지처리 |
| **주류방식**             | **선언적이 현대IaC의표준**(Terraform등) | 현재상태와목표상태를 비교해 **차이만자동조정**           |

→ 암기: **"명령적은 요리순서를하나하나알려주고, 선언적은 완성된요리사진만보여주면 알아서만든다"** — 앞서 다룬 "SDLC의 폭포수(순서중시) vs 애자일(결과중시)"과 유사한 발상차이가 인프라관리에도 나타납니다.

### 도식화 제안

```
[명령적방식]                        [선언적방식]
1.서버생성                         "서버1개,메모리8GB,
2.OS설치                            네트워크X,방화벽Y"
3.네트워크설정                         ↓
4.방화벽규칙적용                   [IaC도구] 현재상태확인
(순서가틀리면실패)                      ↓
                                   차이나는부분만자동생성/수정
```

### Ⅲ. 주요기법 — 멱등성과 상태관리, 핵심 배점

**함정 방지: "코드로 인프라를 만든다"고만 답하면 절반. 왜 이게 신뢰할수있는지의 핵심기법을 보여줘야 완성됩니다.**

| 기법                                  | 내용                                                                 |
| :---------------------------------- | :----------------------------------------------------------------- |
| **멱등성(Idempotency)**                | 같은코드를 **몇번실행해도 결과가항상같음** — 앞서다룬 "CI/CD파이프라인의 멱등성원칙"이 여기서 인프라코드에 적용 |
| **상태관리(State Management)**          | 현재인프라의 **실제상태를파일로기록**, 코드(목표상태)와 **비교해 차이(diff)만 적용**              |
| **불변인프라(Immutable Infrastructure)** | 기존서버를 **수정하지않고**, 변경시 **새서버를만들어교체**(기존은폐기) — 스노우플레이크문제 원천봉쇄        |

→ 암기: **"몇번돌려도똑같고(멱등성), 지금상태와목표상태를비교해서차이만고치고(상태관리), 고치는대신통째로새로만든다(불변인프라)"** — 앞서 다룬 "블루그린배포"(기존환경은그대로두고새환경을통째로준비)가 바로 이 불변인프라철학의 실천사례입니다.

### Ⅳ. 도구체계 및 CI/CD와의 결합

| 구분           | 내용                                                     |
| :----------- | :----------------------------------------------------- |
| **프로비저닝도구**  | Terraform, CloudFormation — **인프라자체(서버,네트워크)를 생성**     |
| **구성관리도구**   | Ansible, Chef — **생성된서버내부의 설정**(패키지설치등) 관리             |
| **CI/CD와결합** | 인프라코드도 **Git에저장→PR리뷰→파이프라인에서자동적용**(앞서다룬 CI/CD5단계와동일패턴) |

→ 앞서 다룬 "멀티클라우드"·"CXL메모리풀링" 답안에서 여러이종환경을 다뤄야했던 문제가, IaC로 \*\*"코드하나로 AWS든Azure든동일하게배포"\*\*할수있다는 실무적해법으로 이어집니다.

### Ⅴ. 결론 포인트 (DevOps 시리즈 완결)

IaC의 본질은 \*\*"인프라도 소스코드와 동일한 규율(버전관리,리뷰,테스트,재현가능성)을 적용받아야한다"\*\*는 것이며, 이는 오늘 다룬 CI/CD(애플리케이션코드의자동화)가 **인프라영역까지확장**된 것입니다 — 앞서 다룬 DevOps(문화)·DevSecOps(보안내재화)·CI/CD(파이프라인)·IaC(인프라코드화)가 모두 \*\*"수동작업의불확실성을, 코드라는검증가능한형태로대체한다"\*\*는 하나의 철학으로 완결되며, 이로써 오늘 다룬 개발-운영 통합 시리즈전체가 마무리됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "과거에는 새로운 서비스를 오픈하려면 엔지니어가 직접 전산실에 들어가 무거운 철제 서버를 랙에 끼우고, 마우스를 수천 번 클릭하며 며칠 밤을 새워 방화벽과 OS를 세팅했다. 사람이 손으로 일일이 치다 보니 A 서버와 B 서버의 세팅이 미묘하게 달라서 에러가 터지는 일(설정 표류 현상)이 일상이었다. 이 '수작업 인프라 지옥'을 끝내버린 혁명이 바로 \*\*'코드형 인프라(IaC)'\*\*다. IaC는 서버, 네트워크, DB 세팅 등 모든 인프라를 마우스 클릭이 아닌 '텍스트 스크립트(코드)'로 짜버린다. 엔지니어가 파일에 '리눅스 서버 10대, 램 16GB 켜 줘'라고 코딩하고 엔터를 누르면, 테라폼(Terraform) 같은 툴이 불과 몇 분 만에 10대의 서버를 100% 똑같은 쌍둥이로 찍어낸다. 가장 위대한 점은 인프라가 텍스트 코드가 되었기 때문에, 소프트웨어 개발자처럼 \*\*'Git(형상 관리)'\*\*에 올려 버전을 관리할 수 있다는 것이다. 누가 언제 방화벽 코드를 바꿨는지 추적이 가능하고, 실수로 서버가 다 날아가도 어제 자 버전의 코드를 다시 실행하면 1분 만에 인프라가 완벽히 100% 복구된다. 클릭 노가다를 없애고 데브옵스 CI/CD를 지탱하는 거대한 뿌리가 바로 IaC다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 클릭 노가다의 종말, 코드로 붕어빵을 찍어내는 IaC 개요**

* **정의:** 물리적인 하드웨어 조립이나 클라우드 관리 콘솔(웹 UI)에서의 수동 클릭 세팅을 배제하고, **인프라(서버, 네트워크, OS 등)의 구성 정보를 머신이 읽을 수 있는 '스크립트 코드'로 작성하여 자동으로 프로비저닝(생성)하고 배포, 관리하는 기술 프랙티스**.
* **목적 및 가치:** 인프라 생성 시간을 극단적으로 단축(수일 ➔ 수 분)하고, 코드를 통한 자동화를 통해 사람의 실수(Human Error)를 없애며, 어떤 서버든 \*\*100% 동일한 설정 상태(멱등성)를 유지(일관성 보장)\*\*하기 위함.

#### **II. \[본론 1] 인프라 형상관리와 멱등성을 보장하는 IaC 자동화 메커니즘 (도식화)**

코드 작성에서부터 클라우드 인프라가 붕어빵처럼 찍혀 나오는 아키텍처입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NjIuODY3OTk5OTk5OTk5OSA5MzUuODA1IiB3aWR0aD0iNjYyLjg2Nzk5OTk5OTk5OTkiIGhlaWdodD0iOTM1LjgwNSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iSWFDX0luZnJhc3RydWN0dXJlX2FzX0NvZGVfXyIgZGF0YS1sYWJlbD0iSWFDIChJbmZyYXN0cnVjdHVyZSBhcyBDb2RlKSDsnpDrj5ntmZQg7JWE7YKk7YWN7LKYIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI1ODIuODY3OTk5OTk5OTk5OSIgaGVpZ2h0PSI4NTUuODA1IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNTgyLjg2Nzk5OTk5OTk5OTkiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5JYUMgKEluZnJhc3RydWN0dXJlIGFzIENvZGUpIOyekOuPme2ZlCDslYTtgqTthY3sspg8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkEiIGRhdGEtdG89IkIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iuy9lOuTnCBQdXNoIiBwb2ludHM9IjMzMS40MzM5OTk5OTk5OTk5NywxNjMuMTQ5OTk5OTk5OTk5OTggMzMxLjQzMzk5OTk5OTk5OTk3LDI3MSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQiIgZGF0YS10bz0iQyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzMzEuNDMzOTk5OTk5OTk5OTcsMzM4LjggMzMxLjQzMzk5OTk5OTk5OTk3LDM4Ni44IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDIiBkYXRhLXRvPSJEIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsnpDrj5kg7ZSE66Gc67mE7KCA64udIOyLpO2WiSIgcG9pbnRzPSIzMzEuNDMzOTk5OTk5OTk5OTcsNjQxLjcwNSAzMzEuNDMzOTk5OTk5OTk5OTcsNzU4LjAwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRCIgZGF0YS10bz0iUzEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzMxLjQzMzk5OTk5OTk5OTk3LDc5NC45MDUgMzMxLjQzMzk5OTk5OTk5OTk3LDgxOC45MDUgMzMxLjQzMzk5OTk5OTk5OTk3LDgxOC45MDUgMzMxLjQzMzk5OTk5OTk5OTk3LDg0Mi45MDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkQiIGRhdGEtdG89IlMyIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjMzMS40MzM5OTk5OTk5OTk5Nyw3OTQuOTA1IDMzMS40MzM5OTk5OTk5OTk5Nyw4MTguOTA1IDUyMy42NDg5OTk5OTk5OTk5LDgxOC45MDUgNTIzLjY0ODk5OTk5OTk5OTksODQyLjkwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRCIgZGF0YS10bz0iUzMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzMxLjQzMzk5OTk5OTk5OTk3LDc5NC45MDUgMzMxLjQzMzk5OTk5OTk5OTk3LDgxOC45MDUgMTM5LjIxOSw4MTguOTA1IDEzOS4yMTksODQyLjkwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJBIiBkYXRhLXRvPSJCIiBkYXRhLWxhYmVsPSLsvZTrk5wgUHVzaCI+CiAgPHJlY3QgeD0iMjk2LjkzMzk5OTk5OTk5OTk3IiB5PSIxOTcuNyIgd2lkdGg9IjY4LjE0IiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzMxLjAwMzk5OTk5OTk5OTk2IiB5PSIyMTIuODUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuy9lOuTnCBQdXNoPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkMiIGRhdGEtdG89IkQiIGRhdGEtbGFiZWw9IuyekOuPmSDtlITroZzruYTsoIDri50g7Iuk7ZaJIj4KICA8cmVjdCB4PSIyNjYuOTMzOTk5OTk5OTk5OTciIHk9IjY4NC43MDUiIHdpZHRoPSIxMjguMTM0MDAwMDAwMDAwMDEiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzMzEuMDAxIiB5PSI2OTkuODU1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7snpDrj5kg7ZSE66Gc67mE7KCA64udIOyLpO2WiTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQSIgZGF0YS1sYWJlbD0i7JeU7KeA64uI7Ja0IPCfkrsK7J247ZSE6528IOyDge2DnOulvArsvZTrk5zroZwg7J6R7ISxIChUZXJyYWZvcm0g65OxKSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyMjguNTc4NDk5OTk5OTk5OTYiIHk9IjkyLjQ1IiB3aWR0aD0iMjA1LjcxMDk5OTk5OTk5OTk4IiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzMxLjQzMzk5OTk5OTk5OTk3IiB5PSIxMjcuODAwMDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjMzMS40MzM5OTk5OTk5OTk5NyIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPuyXlOyngOuLiOyWtCDwn5K7PC90c3Bhbj48dHNwYW4geD0iMzMxLjQzMzk5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7snbjtlITrnbwg7IOB7YOc66W8PC90c3Bhbj48dHNwYW4geD0iMzMxLjQzMzk5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7svZTrk5zroZwg7J6R7ISxIChUZXJyYWZvcm0g65OxKTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJCIiBkYXRhLWxhYmVsPSJHaXQg7KCA7J6l7IaMIPCfk4EK7J247ZSE6528IOuyhOyghCDquLDroZ0g67CPIO2YleyDgSDqtIDrpqwiIGRhdGEtc2hhcGU9ImN5bGluZGVyIj4KICA8cmVjdCB4PSIyMTUuOTgxNDk5OTk5OTk5OTgiIHk9IjI3OCIgd2lkdGg9IjIzMC45MDUiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDEiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0ibm9uZSIgLz4KICA8bGluZSB4MT0iMjE1Ljk4MTQ5OTk5OTk5OTk4IiB5MT0iMjc4IiB4Mj0iMjE1Ljk4MTQ5OTk5OTk5OTk4IiB5Mj0iMzMxLjgiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDxsaW5lIHgxPSI0NDYuODg2NDk5OTk5OTk5OTYiIHkxPSIyNzgiIHgyPSI0NDYuODg2NDk5OTk5OTk5OTYiIHkyPSIzMzEuOCIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPGVsbGlwc2UgY3g9IjMzMS40MzM5OTk5OTk5OTk5NyIgY3k9IjMzMS44IiByeD0iMTE1LjQ1MjUiIHJ5PSI3IiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8ZWxsaXBzZSBjeD0iMzMxLjQzMzk5OTk5OTk5OTk3IiBjeT0iMjc4IiByeD0iMTE1LjQ1MjUiIHJ5PSI3IiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzMzEuNDMzOTk5OTk5OTk5OTciIHk9IjMwNC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIzMzEuNDMzOTk5OTk5OTk5OTciIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5HaXQg7KCA7J6l7IaMIPCfk4E8L3RzcGFuPjx0c3BhbiB4PSIzMzEuNDMzOTk5OTk5OTk5OTciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyduO2UhOudvCDrsoTsoIQg6riw66GdIOuwjyDtmJXsg4Eg6rSA66asPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkMiIGRhdGEtbGFiZWw9IkNJL0NEIO2MjOydtO2UhOudvOyduCDwn6SWCuy9lOuTnCDqsoDsgqwg67CPIOyekOuPmSDrsLDtj6wg7Yq466as6rGwIiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjMzMS40MzM5OTk5OTk5OTk5NywzODYuODAwMDAwMDAwMDAwMDcgNDU4Ljg4NjQ5OTk5OTk5OTk2LDUxNC4yNTI1IDMzMS40MzM5OTk5OTk5OTk5Nyw2NDEuNzA1IDIwMy45ODE0OTk5OTk5OTk5OCw1MTQuMjUyNSIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIzMzEuNDMzOTk5OTk5OTk5OTciIHk9IjUxNC4yNTI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIzMzEuNDMzOTk5OTk5OTk5OTciIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5DSS9DRCDtjIzsnbTtlITrnbzsnbgg8J+kljwvdHNwYW4+PHRzcGFuIHg9IjMzMS40MzM5OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7L2U65OcIOqygOyCrCDrsI8g7J6Q64+ZIOuwsO2PrCDtirjrpqzqsbA8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRCIgZGF0YS1sYWJlbD0iQVdTIC8gQXp1cmUg7YG065287Jqw65OcIO2ZmOqyvSDimIHvuI8iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjE0LjQ5OTQ5OTk5OTk5OTk1IiB5PSI3NTguMDA1IiB3aWR0aD0iMjMzLjg2OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzMxLjQzMzk5OTk5OTk5OTk3IiB5PSI3NzYuNDU1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5BV1MgLyBBenVyZSDtgbTrnbzsmrDrk5wg7ZmY6rK9IOKYge+4jzwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzEiIGRhdGEtbGFiZWw9IuybuSDshJzrsoQgMSAoMTAwJSDrj5nsnbwpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjI1MC40MzgiIHk9Ijg0Mi45MDUiIHdpZHRoPSIxNjEuOTkyIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzMxLjQzMzk5OTk5OTk5OTk3IiB5PSI4NjEuMzU1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7sm7kg7ISc67KEIDEgKDEwMCUg64+Z7J28KTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzIiIGRhdGEtbGFiZWw9IuybuSDshJzrsoQgMiAoMTAwJSDrj5nsnbwpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQ0MC40Mjk5OTk5OTk5OTk5NSIgeT0iODQyLjkwNSIgd2lkdGg9IjE2Ni40MzgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1MjMuNjQ4OTk5OTk5OTk5OSIgeT0iODYxLjM1NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7Ju5IOyEnOuyhCAyICgxMDAlIOuPmeydvCk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlMzIiBkYXRhLWxhYmVsPSLsm7kg7ISc67KEIDMgKDEwMCUg64+Z7J28KSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iODQyLjkwNSIgd2lkdGg9IjE2Ni40MzgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMzkuMjE5IiB5PSI4NjEuMzU1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7sm7kg7ISc67KEIDMgKDEwMCUg64+Z7J28KTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMzEuOTUyNSIgeT0iOTIuNDUiIHdpZHRoPSI2OC42MjYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNjYuMjY1NDk5OTk5OTk5OTciIHk9IjExMC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5Ob3RlPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] IaC를 지배하는 핵심 사상과 2가지 접근 방식 (3단 표 - 출제 1순위)**

IaC 도구들이 인프라를 찍어내는 두 가지의 전혀 다른 철학적 접근 방식입니다.

| **접근 철학 (방식)**                   | **개념 및 동작 원리**                                                                                                                            | **대표적인 IaC 도구**                                               |
| :------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------ |
| **1. 선언형 방식 🎯** *(Declarative)* | **"최종 목표 상태(What)"만 선언함.** 엔지니어가 "나는 최종적으로 웹 서버 3대가 켜진 상태를 원해"라고 코드에 목표만 적어두면, 도구가 알아서 현재 상태를 분석해(1대만 켜져 있다면) 부족한 2대를 자동으로 추가해 목표 상태를 맞춤. | **Terraform (테라폼)** AWS CloudFormation *(현대 IaC의 절대적인 대세 철학)* |
| **2. 명령형 방식 📜** *(Imperative)*  | **"실행할 순서와 절차(How)"를 명시함.** 마치 요리 레시피처럼 "1번 서버를 켜라, 그다음 방화벽을 80포트로 열어라, 그다음 Nginx를 깔아라"라며 실행할 스크립트 명령어와 절차를 하나씩 순서대로 명시함.                 | **Ansible (앤서블)** Chef, Puppet *(기존 서버 내부 환경 구성에 특화)*         |
| **공통 핵심 속성 멱등성 (Idempotency)**   | 선언형이든 명령형이든, **동일한 IaC 코드를 1번 실행하든 100번 실행하든 결과적으로 대상 서버는 항상 똑같은(동일한) 인프라 상태를 보장**해야 함. (설정 표류/Snowflake 방지)                              | 모든 IaC 도구의 기본 철학                                              |

#### **IV. \[결론/제언] 불변 인프라(Immutable Infrastructure)와 GitOps 사상으로의 진화**

* **(키워드 위주 2줄 마무리)** "IaC의 궁극적인 지향점은 서버에 접속해 설정을 고치는 짓을 금지하고, 서버를 통째로 폐기한 뒤 새 코드로 찍어내는 \*\*'불변 인프라(Immutable Infrastructure)'\*\*를 구축하는 것입니다. 나아가 최근에는 인프라의 운영 상태마저도 오직 Git 저장소의 코드(선언)와 싱크를 맞추어 100% 동일하게 유지시키는 **'GitOps (ArgoCD 등)' 패러다임으로 진화**하며, 쿠버네티스(K8s) 클라우드 환경의 핵심 지배자로 군림하고 있습니다."
