#### **분산 시스템 통신 아키텍처: EDA(Event-Driven Architecture) 토폴로지의 양대 축**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 동기 호출로는 대규모 분산 시스템을 감당 못 하는가)
Ⅱ. EDA 2대 토폴로지 핵심 원리
Ⅲ. 비교 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 트리거 vs 어설션이 'DB 내부에서 이벤트에 반응하는 무결성 제어'였다면, EDA(Event-Driven Architecture)는 그 이벤트 기반 사고방식을 시스템 전체, 특히 MSA(마이크로서비스 아키텍처) 환경의 서비스 간 통신으로 확장한 것이다 — 서비스 A가 서비스 B를 직접 호출하는 동기 방식(Request-Response)은 B의 장애가 즉시 A로 전파되는 강한 결합(Tight Coupling)의 문제를 낳는데, EDA는 '이벤트가 발생했다는 사실만 비동기로 알리고 그것을 누가 어떻게 처리할지는 수신자에게 맡기는' 방식으로 이 결합을 끊으며, 그 구현 방식은 크게 '이벤트를 특정 수신자 없이 브로드캐스트하는 브로커 토폴로지(Broker Topology)'와 '이벤트의 흐름 자체를 오케스트레이터가 중앙에서 지휘하는 미디에이터 토폴로지(Mediator Topology)'의 양대 축으로 나뉘며, 이 선택이 앞서 다룬 CDC·Kafka 기반 아키텍처의 설계 방향을 근본적으로 결정하는 것"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3NTguMDIzOTk5OTk5OTk5OSAyMDEuOCIgd2lkdGg9Ijc1OC4wMjM5OTk5OTk5OTk5IiBoZWlnaHQ9IjIwMS44IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlJPT1QiIGRhdGEtdG89Ik1lZGlhdG9yIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjM4Mi43MTcsNzYuOSAzODIuNzE3LDEwMC45IDIwNi4yMTA5OTk5OTk5OTk5OCwxMDAuOSAyMDYuMjEwOTk5OTk5OTk5OTgsMTI0LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlJPT1QiIGRhdGEtdG89IkJyb2tlciIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzODIuNzE3LDc2LjkgMzgyLjcxNywxMDAuOSA1NTkuMjIzLDEwMC45IDU1OS4yMjMsMTI0LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJPT1QiIGRhdGEtbGFiZWw9IkVEQSDthqDtj7TroZzsp4DsnZgg7JaR64yAIOy2lSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyODUuNzg5NSIgeT0iNDAiIHdpZHRoPSIxOTMuODU1IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzODIuNzE3IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+RURBIO2GoO2PtOuhnOyngOydmCDslpHrjIAg7LaVPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJNZWRpYXRvciIgZGF0YS1sYWJlbD0i7KSR7J6s7J6QIO2GoO2PtOuhnOyngCA6IOykkeyVmSDsoJzslrQgJmFtcDsg7Jik7LyA7Iqk7Yq466CI7J207IWYIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwIiB5PSIxMjQuOSIgd2lkdGg9IjMzMi40MjE5OTk5OTk5OTk5NyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjIwNi4yMTA5OTk5OTk5OTk5OCIgeT0iMTQzLjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7spJHsnqzsnpAg7Yag7Y+066Gc7KeAIDog7KSR7JWZIOygnOyWtCAmYW1wOyDsmKTsvIDsiqTtirjroIjsnbTshZg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkJyb2tlciIgZGF0YS1sYWJlbD0i67iM66Gc7LukIO2GoO2PtOuhnOyngCA6IOu2hOyCsCDrsJjsnZEgJmFtcDsg7L2U66CI7Jik6re4656Y7ZS8IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwMC40MjE5OTk5OTk5OTk5IiB5PSIxMjQuOSIgd2lkdGg9IjMxNy42MDIiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNTU5LjIyMyIgeT0iMTQzLjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7ruIzroZzsu6Qg7Yag7Y+066Gc7KeAIDog67aE7IKwIOuwmOydkSAmYW1wOyDsvZTroIjsmKTqt7jrnpjtlLw8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

***

#### Ⅱ. EDA 2대 토폴로지 핵심 원리

**가. 브로커 토폴로지(Broker Topology)**

```
[브로커 토폴로지: 중앙 오케스트레이터 없이 분산된 흐름]

주문서비스 → [이벤트 브로커(Kafka 등)] → 재고서비스
                      │                  → 결제서비스
                      │                  → 알림서비스
                      ↓
                 (구독자들이 각자 알아서 반응)

핵심 동작:
  ①주문서비스: "주문생성됨" 이벤트를 브로커에 발행(Publish)만 함
  ②재고·결제·알림서비스: 각자 관심있는 이벤트를 구독(Subscribe)
  ③각 서비스가 이벤트를 받으면 자율적으로 처리
     처리 후 필요하면 또 다른 이벤트를 발행(연쇄 반응)

→ 발행자는 누가 구독하는지 전혀 모름(완전한 분리)
→ 이벤트 흐름 전체를 파악할 단일 지점이 없음(체인 형태로 전파)
```

**나. 미디에이터 토폴로지(Mediator Topology)**

```
[미디에이터 토폴로지: 중앙 오케스트레이터가 흐름 지휘]

주문서비스 → [이벤트 큐] → [미디에이터(오케스트레이터)]
                                    │
                    ┌───────────────┼───────────────┐
                    ↓               ↓               ↓
               재고서비스        결제서비스        알림서비스
              (호출 후 결과 반환)(호출 후 결과 반환)(호출 후 결과 반환)
                    │               │               │
                    └───────────────┴───────────────┘
                              (미디에이터가 순서·상태 관리)

핵심 동작:
  ①주문서비스: "주문생성됨" 이벤트 발생
  ②미디에이터: 이 이벤트에 대한 전체 처리 절차(워크플로우)를 알고 있음
     "재고확인 → 결제 → 배송준비 → 알림" 순서를 직접 지휘
  ③각 단계 서비스는 미디에이터의 지시에 따라 작업 후 결과를 미디에이터에 반환
  ④미디에이터가 전체 트랜잭션의 성공/실패·보상(Compensation)을 총괄 관리

→ 앞서 다룬 Saga 패턴의 오케스트레이션 방식과 사실상 동일한 구조
```

**다. 2대 토폴로지 핵심 체계**

| 항목            | 브로커 토폴로지                             | 미디에이터 토폴로지                     |
| :------------ | :----------------------------------- | :----------------------------- |
| **제어 흐름**     | **분산형**(중앙 통제자 없음)                   | **중앙집중형**(오케스트레이터가 지휘)         |
| **결합도**       | **매우 낮음**(발행자-구독자 상호 무지) ✅           | 상대적으로 높음(오케스트레이터가 각 서비스 인지)    |
| **워크플로우 가시성** | 낮음(전체 흐름 추적 어려움) 🚨                  | **높음**(중앙에서 전체 프로세스 파악 가능) ✅   |
| **장애 처리**     | 각 서비스가 개별적으로 재시도·보상 처리               | **미디에이터가 전체 트랜잭션의 보상 로직 총괄** ✅ |
| **확장성**       | **매우 우수**(새 구독자 추가가 기존 서비스에 영향 없음) ✅ | 오케스트레이터 자체가 병목·단일장애점 가능성 🚨    |
| **복잡한 순서 제어** | 어려움(순서 보장이 이벤트 체인에 암묵적으로 분산) 🚨      | **용이**(명시적 워크플로우 정의) ✅         |

***

#### Ⅲ. 비교 및 적용 체계

**가. 브로커 vs 미디에이터 상세 비교**

| 비교 항목          | 브로커 토폴로지                        | 미디에이터 토폴로지                                   |
| :------------- | :------------------------------ | :------------------------------------------- |
| **적합 시나리오**    | 단순 알림·팬아웃(Fan-out)성 이벤트 전파      | **다단계 트랜잭션·복잡한 비즈니스 프로세스**                   |
| **대표 구현 기술**   | Kafka·RabbitMQ(Pub/Sub 모델)      | Saga Orchestrator·Camunda·AWS Step Functions |
| **디버깅 난이도**    | 이벤트 체인이 길수록 원인 추적 어려움 🚨        | 중앙 로그 하나로 전체 흐름 파악 용이 ✅                      |
| **팀 자율성**      | **각 팀이 독립적으로 구독 로직 개발 가능** ✅    | 오케스트레이터 변경 시 여러 팀 조율 필요                      |
| **Saga 패턴 대응** | **코레오그래피(Choreography) 방식**과 대응 | **오케스트레이션(Orchestration) 방식**과 대응            |

**나. Saga 패턴과의 관계**

| Saga 구현 방식                 | 대응 토폴로지    | 특징                                  |
| :------------------------- | :--------- | :---------------------------------- |
| **코레오그래피(Choreography)**   | 브로커 토폴로지   | 각 서비스가 이벤트를 발행·구독하며 자율적으로 다음 단계 트리거 |
| **오케스트레이션(Orchestration)** | 미디에이터 토폴로지 | 중앙 오케스트레이터가 각 서비스를 명시적으로 호출·상태 관리   |

**다. 하이브리드 및 실무 선택 기준**

| 판단 기준               | 브로커 권장                           | 미디에이터 권장                   |
| :------------------ | :------------------------------- | :------------------------- |
| **트랜잭션 참여 서비스 수**   | 적음(2\~3개, 단순 흐름)                 | **많음(4개 이상, 복잡한 순서)**      |
| **보상 트랜잭션 복잡도**     | 낮음                               | **높음**(여러 단계의 롤백 로직 필요)    |
| **비즈니스 요구사항 변경 빈도** | 낮음                               | **높음**(중앙에서 워크플로우만 수정하면 됨) |
| **조직 구조**           | 팀별 독립성이 중요한 대규모 조직(Conway's Law) | 프로세스 전체를 한 팀이 책임지는 구조      |

***

**(제언)** "브로커와 미디에이터 토폴로지의 근본적 차이는 '지능을 어디에 둘 것인가'라는 설계 철학의 문제로, 브로커 토폴로지는 지능을 각 서비스 가장자리(Edge)에 분산시켜 개별 팀의 자율성과 확장성을 극대화하는 대신 전체 흐름의 가시성을 희생하고, 미디에이터 토폴로지는 지능을 중앙에 집중시켜 복잡한 비즈니스 프로세스의 명확한 통제와 디버깅 용이성을 얻는 대신 오케스트레이터 자체가 새로운 병목과 강한 결합의 원천이 될 위험을 감수하는 트레이드오프입니다. 실무에서는 두 방식을 배타적으로 선택하기보다 조직 전체의 이벤트 발행-구독은 Kafka 기반 브로커 토폴로지로 느슨하게 유지하면서, 그 안에서 결제-배송-정산처럼 명확한 순서와 보상 트랜잭션이 필요한 복잡한 비즈니스 프로세스에 한해서만 국소적으로 미디에이터(오케스트레이터)를 도입하는 계층적 하이브리드 전략이 대규모 마이크로서비스 환경에서 가장 실용적인 접근입니다.

***

**앞서 다룬 개념과의 연결**

| 연계 개념                   | 연결 내용                                                 |
| :---------------------- | :---------------------------------------------------- |
| **트리거 vs 어설션**          | DB 내부의 이벤트 기반 무결성 제어(트리거)가 시스템 전체 규모로 확장된 것이 EDA      |
| **CDC 기반 무중단 마이그레이션**   | Kafka가 CDC 이벤트 전달의 핵심 인프라로 브로커 토폴로지와 직접 연계            |
| **Raft 합의 알고리즘**        | Kafka의 최신 KRaft 모드가 파티션 리더 선출에 Raft 계열 합의를 활용         |
| **와이드 컬럼 스토어·LSM-Tree** | Kafka 로그 세그먼트의 append-only 저장 구조가 LSM-Tree 철학과 상통     |
| **SAFe**                | 미디에이터(오케스트레이터) 소유권을 대규모 조직의 Platform ART가 담당하는 구조적 연계 |

### **I. 비동기 마이크로서비스 연계의 핵심, EDA 토폴로지의 개요**

이벤트 기반 아키텍처(EDA: Event-Driven Architecture)는 이벤트의 생성과 소비를 통해 컴포넌트 간 결합도를 낮추고 비동기 응답성을 극대화합니다. 이러한 EDA 환경에서 복잡한 비즈니스 트랜잭션 수명주기를 제어하기 위해, **중앙의 중재자가 전체 처리 순서를 일괄 조율하는 중재자(Mediator) 토폴로지**와, **중앙 제어자 없이 각 마이크로서비스가 브로커 채널에 반응하여 연쇄 동작하는 브로커(Broker) 토폴로지**가 양대 축으로 사용됩니다.

***

### **II. EDA 2대 토폴로지의 세부 메커니즘 분석**

#### **1. 중재자 토폴로지 (Mediator Topology / Orchestration)**

* **동작 프로세스**: `시작 이벤트` ➔ `이벤트 중재자(Mediator)` ➔ `이벤트 채널` ➔ `이벤트 프로세서`
* **특징**: 주문-결제-배송과 같이 **다단계 복잡한 비즈니스 워크플로우**가 존재할 때 사용합니다. 중재자(Mediator)가 오케스트레이터 역할을 수행하며, 실패 시 보상 트랜잭션(Compensating Tx)을 일괄 제어합니다.
* **MSA Saga 매핑**: **Saga Orchestration 패턴**에 해당합니다.

#### **2. 브로커 토폴로지 (Broker Topology / Choreography)**

* **동작 프로세스**: `시작 이벤트` ➔ `이벤트 브로커(Pub-Sub)` ➔ `이벤트 프로세서` ➔ `신규 이벤트 발행` ➔ `다음 프로세서 반응`
* **특징**: 중앙 관리자 없이 이벤트 브로커(Kafka, RabbitMQ 등)를 매개로 이벤트 프로세서들이 \*\*자율적으로 이벤트를 발행 및 구독(Pub-Sub)\*\*하며 반응형으로 동작합니다.
* **MSA Saga 매핑**: **Saga Choreography 패턴**에 해당합니다.

***

### **III. 중재자(Mediator) 토폴로지와 브로커(Broker) 토폴로지의 상세 비교**

| **비교 항목**     | **🏢 중재자 토폴로지 (Mediator)**       | **⚡ 브로커 토폴로지 (Broker)**          |
| :------------ | :------------------------------- | :------------------------------- |
| **제어 메커니즘**   | **중앙 오케스트레이션 (Orchestration)**   | **분산 코레오그래피 (Choreography)**     |
| **이벤트 흐름 주체** | 중앙의 이벤트 중재자(Mediator)가 흐름 통제     | 개별 프로세서가 브로커 채널로 반응 및 발행         |
| **컴포넌트 결합도**  | 중재자 엔진에 대한 결합도 존재                | **컴포넌트 간 상호 인지 없는 완전 느슨한 결합**    |
| **트랜잭션 가시성**  | **높음 (중재자에서 전체 처리/실패 상태 추적 용이)** | 낮음 (분산 이벤트 체인으로 엔드투엔드 추적 난이도 높음) |
| **성능 및 확장성**  | 중재자 엔진 병목 가능성 (상태 관리 오버헤드)       | **극도로 높음 (브로커 기반 고속 분산 스트리밍)**   |
| **적합 유스케이스**  | 다단계 주문 처리, 금융 대출 승인 워크플로우        | 실시간 로그 처리, 알림 푸시, 데이터 동기화        |

***

### **IV. EDA 토폴로지 선택 및 구동을 위한 엔지니어링 가이드라인**

1. **브로커 토폴로지의 분산 트레이싱(OpenTelemetry) 필수 적용**: 브로커 토폴로지는 특정 마이크로서비스에서 장애가 발생하거나 이벤트가 유실되었을 때 원인 파악이 어렵습니다. 따라서 패킷 헤더에 Trace ID를 주입하여 전체 체인을 시각화하는 **OpenTelemetry / Jaeger 트레이싱**을 필수로 배포해야 합니다.
2. **도메인 복잡도에 따른 하이브리드 구성**: 핵심 비즈니스 도메인(결제, 재고)은 중재자 패턴으로 모니터링 가용성을 확보하고, 외곽의 보조 서비스(메일 발송, 마일리지 적립, 통계 산출)는 브로커 패턴으로 처리하는 혼합 아키텍처 구성이 바람직합니다.
