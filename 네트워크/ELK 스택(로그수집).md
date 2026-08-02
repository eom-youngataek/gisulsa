### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (ELK정의, SIEM과의관계) — 3~4줄
Ⅱ. 3대구성요소 - 수집·저장·시각화 (본론①, 도식 1개 필수)
Ⅲ. Beats/Logstash 데이터흐름, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

ELK스택은 **Elasticsearch,Logstash,Kibana** 세오픈소스도구의조합으로, 앞서다룬 \*\*"SIEM의4단계(수집-정규화-분석-경보)"\*\*를 **실제로구현하는 대표적방법**입니다 — 상용SIEM제품과달리 **오픈소스라비용부담이적고 유연성이높아**, 많은조직이 **자체SIEM구축**에 활용합니다.

### Ⅱ. 3대구성요소 — 수집·저장·시각화

| 구성                | 역할                                                                 |
| :---------------- | :----------------------------------------------------------------- |
| **Elasticsearch** | **분산검색·저장엔진**— 대량의로그데이터를 **빠르게색인·검색**                              |
| **Logstash**      | **데이터수집·가공파이프라인**— 앞서다룬 \*\*"SIEM의정규화단계"\*\*를 담당,다양한형식의로그를 **표준화** |
| **Kibana**        | **시각화대시보드**— 로그데이터를 **그래프,차트로 한눈에**분석                              |

→ 암기: **"모으고가공하는건Logstash,저장하고검색하는건Elasticsearch,보여주는건Kibana"** — 앞서다룬 **"SIEM의수집-정규화-분석-경보"** 4단계중, **수집·정규화는Logstash,저장·분석은Elasticsearch,경보/시각화는Kibana**가 각각담당합니다.

### 도식화 제안

```
[각종서버/장비의로그]
     ↓
[Logstash] 수집+정규화(다양한형식→표준화)
     ↓
[Elasticsearch] 저장+색인(빠른검색가능)
     ↓
[Kibana] 시각화 대시보드(그래프,경보확인)
```

### Ⅲ. Beats/Logstash 데이터흐름 — 핵심 배점

**함정 방지: "Logstash가다한다"고만답하면절반. 왜Beats라는경량에이전트가별도로필요한지, 그리고실제데이터흐름을보여줘야완성됩니다.**

| 구성                   | 내용                                                                                        |
| :------------------- | :---------------------------------------------------------------------------------------- |
| **Beats**(경량에이전트)    | 각서버에 **가볍게설치**되어 **로그를수집만해서전달**— Logstash보다 **훨씬적은리소스소모**                                 |
| **왜Logstash를직접안쓰는가** | Logstash는 **가공기능이무거워서**, 수천대서버에 **직접설치하면부담**— Beats로 **가볍게수집만하고**, 중앙의Logstash가 **가공을전담** |
| **대표Beats종류**        | **Filebeat**(파일로그),**Metricbeat**(시스템지표),**Packetbeat**(네트워크패킷)                           |

→ 암기: **"각서버엔가벼운Beats만설치해서보내기만하고, 무거운가공작업(파싱,필터링)은 중앙의Logstash가전담한다"** — 앞서다룬 \*\*"MODBUS의마스터-슬레이브"\*\*와 유사하게, \*\*"현장(Beats,가벼움)-중앙처리(Logstash,무거움)"\*\*의 역할분담이 여기서도 나타납니다.

### 도식화 제안

```
[서버1] [서버2] [서버3] ... [서버1000대]
   ↓Filebeat  ↓Filebeat  ↓Filebeat      (각서버엔 가벼운Beats만)
   └──────────┴──────────┘
              ↓
        [Logstash] (중앙에서 무거운가공작업 전담)
              ↓
        [Elasticsearch] 저장
              ↓
          [Kibana] 시각화
```

**앞서다룬SOAR와의연계**: ELK가 로그를 수집·분석해 \*\*이상패턴(경보)\*\*을 발견하면, 그 경보를 앞서다룬 **SOAR플레이북**이 **받아서자동대응**을실행합니다 — \*\*ELK(보고,분석)→SOAR(행동)\*\*의 조합이, 앞서다룬 \*\*"SIEM+SOAR"\*\*의 오픈소스버전실무구현입니다.

### Ⅳ. 결론

ELK스택은 \*\*"Beats(경량수집)→Logstash(가공)→Elasticsearch(저장·검색)→Kibana(시각화)"\*\*로 이어지는 파이프라인을 통해, 앞서다룬 \*\*SIEM의4단계(수집-정규화-분석-경보)\*\*를 **오픈소스로실제구현**하는 대표적방법입니다 — 이는 앞서다룬 \*\*"SIEM은개념,ELK는실무도구"\*\*라는 관계를 명확히보여주며, 오늘하루다룬 방대한 보안운영시리즈(SIEM→SOAR→ELK)가 \*\*"이론적프레임워크가, 실제로어떤구체적기술스택으로구현되는지"\*\*를 완결짓는 답안입니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "수백 대의 서버에서 쏟아지는 에러 로그들을 엔지니어가 일일이 텍스트로 까보지 않고, 한곳에 모아 0.1초 만에 검색하고 예쁜 차트로 그려주는 '오픈소스 빅데이터 로그 분석의 대명사'다. 첫째, 서버 끝단에 딱 붙어서 가볍게 로그를 퍼 나르는 배달부 **'Beats'**. 둘째, 날것의 쓰레기 로그를 받아서 쓸모 있는 데이터로 정제하고 필터링하는 가공 공장 **'Logstash'**. 셋째, 수십 테라바이트의 데이터를 저장하고 'Error'라는 단어를 빛의 속도로 찾아내는 ELK의 심장 **'Elasticsearch'**. 마지막으로 넷째, 찾아낸 로그 통계를 직관적인 그래프 대시보드로 띄워주는 프론트엔드 모니터 화면 \*\*'Kibana'\*\*까지 4단계 파이프라인이 톱니바퀴처럼 돌아간다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 분산 환경 로그 통합 분석의 표준, ELK 스택 개요**

* **정의:** 방대한 양의 비정형 데이터(서버 시스템 로그, 웹 트래픽 등)를 실시간으로 수집, 정제, 검색, 분석, 시각화하기 위한 오픈소스 기반의 엔드투엔드(End-to-End) 데이터 파이프라인.
* **발전 방향:** 원래 Elasticsearch, Logstash, Kibana의 앞 글자를 딴 ELK였으나, 경량 수집기인 Beats가 편입되면서 현재는 \*\*'Elastic Stack'\*\*이라는 공식 명칭으로 불림.

#### **II. \[본론 1] (극단적 단순화 버전) 수집부터 대시보드까지 4단계 파이프라인**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMTEzLjYxNiAxOTMuOCIgd2lkdGg9IjExMTMuNjE2IiBoZWlnaHQ9IjE5My44IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJFTEtfRWxhc3RpY19TdGFja19fXyIgZGF0YS1sYWJlbD0iRUxLIChFbGFzdGljIFN0YWNrKSDrjbDsnbTthLAg7Z2Q66aEIO2MjOydtO2UhOudvOyduCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMTAzMy42MTYiIGhlaWdodD0iMTEzLjgwMDAwMDAwMDAwMDAxIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMTAzMy42MTYiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5FTEsgKEVsYXN0aWMgU3RhY2spIOuNsOydtO2EsCDtnZDrpoQg7YyM7J207ZSE65287J24PC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTUlYiIGRhdGEtdG89IkIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjEuIEJlYXRzIOyEpOy5mCIgcG9pbnRzPSIxOTEuMzE2LDExMC45IDM1Ni4zNjYsMTEwLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkIiIGRhdGEtdG89IkwiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDE2LjM2NiwxMTAuOSA0NjQuMzY2LDExMC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJMIiBkYXRhLXRvPSJFIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSJKU09OIOuzgO2ZmCIgcG9pbnRzPSI1MjQuMzY2LDExMC45IDY4NC4wNjk5OTk5OTk5OTk5LDExMC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJFIiBkYXRhLXRvPSJLIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9Ijc0NC4wNjk5OTk5OTk5OTk5LDExMC45IDc5Mi4wNjk5OTk5OTk5OTk5LDExMC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJLIiBkYXRhLXRvPSJVU0VSIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9Ijg1Mi4wNjk5OTk5OTk5OTk5LDExMC45IDkwMC4wNjk5OTk5OTk5OTk5LDExMC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlNSViIgZGF0YS10bz0iQiIgZGF0YS1sYWJlbD0iMS4gQmVhdHMg7ISk7LmYIj4KICA8cmVjdCB4PSIyMzUuMzE2IiB5PSI5NC45IiB3aWR0aD0iNzcuMDUwMDAwMDAwMDAwMDEiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyNzMuODQxIiB5PSIxMTAuMDUwMDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjEuIEJlYXRzIOyEpOy5mDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJMIiBkYXRhLXRvPSJFIiBkYXRhLWxhYmVsPSJKU09OIOuzgO2ZmCI+CiAgPHJlY3QgeD0iNTY4LjM2NiIgeT0iOTQuOSIgd2lkdGg9IjcxLjcwNDAwMDAwMDAwMDAxIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjA0LjIxOCIgeT0iMTEwLjA1MDAwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5KU09OIOuzgO2ZmDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU1JWIiBkYXRhLWxhYmVsPSLsm7kg7ISc67KE65OkCuyXkOufrCDtjpHtjpEg7YSw7KeQIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjEzNS4zMTYiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMjMuNjU4IiB5PSIxMTAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTIzLjY1OCIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuybuSDshJzrsoTrk6Q8L3RzcGFuPjx0c3BhbiB4PSIxMjMuNjU4IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7sl5Drn6wg7Y6R7Y6RIO2EsOynkDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJCIiBkYXRhLWxhYmVsPSJCIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM1Ni4zNjYiIHk9IjkyLjQ1IiB3aWR0aD0iNjAiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjM4Ni4zNjYiIHk9IjExMC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5CPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJMIiBkYXRhLWxhYmVsPSJMIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQ2NC4zNjYiIHk9IjkyLjQ1IiB3aWR0aD0iNjAiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQ5NC4zNjYiIHk9IjExMC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5MPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJFIiBkYXRhLWxhYmVsPSJFIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjY4NC4wNjk5OTk5OTk5OTk5IiB5PSI5Mi40NSIgd2lkdGg9IjYwIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjcxNC4wNjk5OTk5OTk5OTk5IiB5PSIxMTAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+RTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iSyIgZGF0YS1sYWJlbD0iSyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3OTIuMDY5OTk5OTk5OTk5OSIgeT0iOTIuNDUiIHdpZHRoPSI2MCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI4MjIuMDY5OTk5OTk5OTk5OSIgeT0iMTEwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPks8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlVTRVIiIGRhdGEtbGFiZWw9Iuq0gOygnCDri7Tri7nsnpAg8J+nkeKAjfCfkrsiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iOTAwLjA2OTk5OTk5OTk5OTkiIHk9IjkyLjQ1IiB3aWR0aD0iMTU3LjU0NiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9Ijk3OC44NDMiIHk9IjExMC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7qtIDsoJwg64u064u57J6QIPCfp5HigI3wn5K7PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] ELK 스택 핵심 구성 요소별 기능 전격 해부 (3단 표)**

이 토픽은 각 알파벳이 맡은 정확한 역할(수집가공 -> 저장검색 -> 시각화)을 분리하여 설명하는 것이 완벽한 득점 포인트입니다.

| **핵심 척도**            | **📥 수집 / 가공 (Beats & Logstash)**                                                                                                                           | **🔍 저장 / 검색 (Elasticsearch) 🚨**                                                                                                           | **📊 시각화 (Kibana)**                                                                      |
| :------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------- |
| **핵심 역할**            | **'데이터 수집 배달부와 정제 공장'.** 수많은 서버에서 발생하는 날것(Raw)의 로그 텍스트를 끌어모아, 검색하기 좋은 JSON 형태로 변환함.                                                                         | **'ELK의 심장이자 뇌 💯'.** 정제된 데이터를 분산 저장하고, 사용자가 쿼리를 날렸을 때 빛의 속도로 텍스트를 찾아냄.                                                                     | **'데이터 모니터링 프론트엔드'.** 검색된 결과를 인간이 보기 편하게 시각화 대시보드로 만들어줌.                                 |
| **동작 원리 및 주요 기술 🚨** | **\[Beats: 경량 수집]** Logstash가 너무 무거워서, 서버에 부하를 안 주는 Filebeat 등을 엣지에 설치함. **\[Logstash: Grok 필터 💯]** 정규표현식(Grok)을 이용해 한 줄짜리 로그에서 '시간', 'IP', '에러명'을 분리 추출함. | **\[초고속 역인덱싱 (Inverted Index) 💯]** 책 맨 뒤의 색인(Index) 페이지처럼, 단어를 쪼개어 '어떤 문서에 이 단어가 있는지'를 미리 다 저장해 둬서(역인덱스) **RDBMS의 LIKE 검색과는 비교도 안 되게 빠름.** | **\[직관적 대시보드]** 시간대별 에러 발생량 그래프, 특정 IP 접속 위치 지도 표기 등. **\[알림 기능]** 에러 임계치 초과 시 Slack 통보. |
| **한계 / 보완**          | 데이터가 폭주하면 Logstash가 뻗어버리므로, 중간에 완충 지대인 **'Kafka(메시지 큐)'를 달아주는 것이 필수 아키텍처임.**                                                                                | 메모리를 엄청나게 잡아먹음 (Java 힙 메모리 튜닝 필수).                                                                                                          | X-Pack 같은 추가 플러그인을 달아야 머신러닝이나 보안 기능 사용 가능.                                               |

#### **IV. \[결론/제언] 마이크로서비스(MSA) 관제 필수품, 통합 로깅(Centralized Logging)**

* **(키워드 위주 2줄 마무리)** "과거 거대한 모놀리식 환경에서는 서버 한 대에 들어가 로그(tail -f)를 까보면 됐지만, 수백 개의 컨테이너가 떴다 사라지는 현대의 MSA 환경에서는 불가능합니다. 따라서 모든 도커/쿠버네티스 컨테이너의 표준 출력을 ELK(또는 EFK-Fluentd) 스택으로 강제 수집하는 **'중앙집중형 통합 로깅(Centralized Logging)' 아키텍처 구현이 클라우드 네이티브 관제의 필수 전제 조건입니다.**"
