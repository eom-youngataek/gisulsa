### **I. 비동기 이벤트 제어의 양대 축, EDA 토폴로지의 개요**

이벤트 기반 아키텍처(EDA)에서 대량의 비동기 메시지 흐름을 통제하기 위해 두 가지 물리적 토폴로지를 사용합니다. 중앙 집중형 조율을 통해 다단계 비즈니스 워크플로우를 통제하는 **중재자(Mediator) 패턴**과, 개별 컴포넌트 간 반응형 흐름을 유도해 결합도를 극도로 낮추는 **브로커(Broker) 패턴**이 존재하며 시스템 요건에 따른 상호 선택적 적용이 필요합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3MTMuNTYzOTk5OTk5OTk5OSAyMDEuOCIgd2lkdGg9IjcxMy41NjM5OTk5OTk5OTk5IiBoZWlnaHQ9IjIwMS44IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlJPT1QiIGRhdGEtdG89Ik1lZGlhdG9yIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjM2MC40ODcsNzYuOSAzNjAuNDg3LDEwMC45IDE5NS4wOTU5OTk5OTk5OTk5OCwxMDAuOSAxOTUuMDk1OTk5OTk5OTk5OTgsMTI0LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlJPT1QiIGRhdGEtdG89IkJyb2tlciIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzNjAuNDg3LDc2LjkgMzYwLjQ4NywxMDAuOSA1MjUuODc3OTk5OTk5OTk5OSwxMDAuOSA1MjUuODc3OTk5OTk5OTk5OSwxMjQuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUk9PVCIgZGF0YS1sYWJlbD0iRURBIO2GoO2PtOuhnOyngCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyOTUuNDIyNSIgeT0iNDAiIHdpZHRoPSIxMzAuMTI5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzNjAuNDg3IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+RURBIO2GoO2PtOuhnOyngDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTWVkaWF0b3IiIGRhdGEtbGFiZWw9IuykkeyerOyekCDtjKjthLQgOiDspJHslZkg7KGw7JyoIOuwjyDsmKTsvIDsiqTtirjroIjsnbTshZgiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDAiIHk9IjEyNC45IiB3aWR0aD0iMzEwLjE5MTk5OTk5OTk5OTk1IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTk1LjA5NTk5OTk5OTk5OTk4IiB5PSIxNDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuykkeyerOyekCDtjKjthLQgOiDspJHslZkg7KGw7JyoIOuwjyDsmKTsvIDsiqTtirjroIjsnbTshZg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkJyb2tlciIgZGF0YS1sYWJlbD0i67iM66Gc7LukIO2MqO2EtCA6IOu2hOyCsCDrsJjsnZEg67CPIOy9lOugiOyYpOq3uOuemO2UvCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzNzguMTkxOTk5OTk5OTk5OSIgeT0iMTI0LjkiIHdpZHRoPSIyOTUuMzcxOTk5OTk5OTk5OTYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNTI1Ljg3Nzk5OTk5OTk5OTkiIHk9IjE0My4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+67iM66Gc7LukIO2MqO2EtCA6IOu2hOyCsCDrsJjsnZEg67CPIOy9lOugiOyYpOq3uOuemO2UvDwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

***

### **II. 중재자(Mediator) 및 브로커(Broker) 토폴로지의 핵심 메커니즘**

| **분류**       | **🔑 중재자 토폴로지 (Mediator) 🚨**                      | **🏁 브로커 토폴로지 (Broker) 💯**                      |
| :----------- | :------------------------------------------------- | :----------------------------------------------- |
| **이벤트 흐름**   | 시작 이벤트 ➔ 중재자 ➔ 개별 프로세서 분배                          | 시작 이벤트 ➔ 브로커 ➔ 채널 구독자 반응 자율 체인                   |
| **핵심 컴포넌트**  | **Event Mediator**, Event Channel, Event Processor | **Event Broker**, Event Channel, Event Processor |
| **트랜잭션 제어**  | 중재자가 전체 단계의 성공/실패 추적 관리                            | 개별 프로세서가 다음 이벤트를 발행하여 연쇄 진행                      |
| **주요 사용 사례** | 주문 프로세스(재고 확인 ➔ 결제 ➔ 배송 완료)                        | 실시간 로그 분석, 알림 푸시, 단순 데이터 복제 연동                   |

***

### **III. 중재자 토폴로지와 브로커 토폴로지의 아키텍처 비교**

| **비교 항목**    | **🏢 중재자 토폴로지 (Mediator)**    | **⚡ 브로커 토폴로지 (Broker)**      |
| :----------- | :---------------------------- | :--------------------------- |
| **제어 메커니즘**  | **오케스트레이션(Orchestration)** 제어 | **코레오그래피(Choreography)** 제어  |
| **아키텍처 결합도** | 중재자 컴포넌트에 대한 결합도 발생           | 컴포넌트 간 상호 인지 없는 완전 느슨한 결합    |
| **트랜잭션 가시성** | 중재자를 통한 일관성 모니터링 및 복구 용이      | 분산 체인 구조로 엔드투엔드 경로 추적 난이도 높음 |
| **성능 및 병목**  | 중재자 엔진 과부하 시 전체 시스템 성능 병목     | 이벤트 채널을 통한 분산 처리로 고성능/대역폭 확보 |

***

### **IV. EDA 도입 시 성능 및 가용성 확보를 위한 가이드라인**

**IMPORTANT**

1. **멱등성(Idempotency)의 설계**: 비동기 브로커 환경에서 메시지가 네트워크 지연으로 인해 재전송(At-least-once)되더라도, 수신측 프로세서에서 동일 요청이 중복 실행되지 않도록 유니크 키(Idempotent Key)를 통한 검증 로직을 구현해야 합니다.
2. **하이브리드 적용 전략**: 핵심 복잡 비즈니스 도메인(주문/결제 등)에는 중재자(Saga Orchestration)를 적용하고, 마이크로서비스 간의 느슨한 연계 및 실시간 데이터 싱크에는 브로커(Saga Choreography)를 혼합 수립하는 아키텍처 정렬이 필수적입니다.
