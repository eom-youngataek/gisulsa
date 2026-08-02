### **데이터베이스 무중단 전환 핵심: CDC 기반 마이그레이션**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 "중단 없이" 마이그레이션이 필요한가)
Ⅱ. CDC 핵심 원리 및 구조
Ⅲ. CDC 기반 무중단 마이그레이션 단계별 흐름
Ⅳ. 결론
```

포인트: 개요에서 **"앞서 다룬 ARIES 회복 알고리즘이 '장애 후 WAL 로그로 DB를 복원'한다면, CDC(Change Data Capture)는 그 WAL 로그를 실시간으로 캡처해 '원본 DB 변경 사항을 타깃 DB에 지속 동기화함으로써 서비스 중단 없이 이기종 DB 간 마이그레이션을 가능하게 하는 기술'이다 — 24시간 서비스 중단이 불가능한 금융·커머스·공공 시스템에서 Oracle→PostgreSQL, 온프레미스→클라우드, 레거시→MSA 전환의 핵심 수단이며, 앞서 다룬 데이터 계약·MLOps 파이프라인의 실시간 데이터 공급 기반이기도 하다"**라는 한 줄로 시작하면 전체 맥락이 드러납니다.
\
![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNTQ3Ljc1OTk5OTk5OTk5OTggMTE2LjkiIHdpZHRoPSIxNTQ3Ljc1OTk5OTk5OTk5OTgiIGhlaWdodD0iMTE2LjkiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iU291cmNlIiBkYXRhLXRvPSJDREMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzM2LjExMjk5OTk5OTk5OTk0LDU4LjQ1IDM4NC4xMTI5OTk5OTk5OTk5NCw1OC40NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQ0RDIiBkYXRhLXRvPSJUYXJnZXQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNzI2LjE2Nzk5OTk5OTk5OTksNTguNDUgNzc0LjE2Nzk5OTk5OTk5OTksNTguNDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlRhcmdldCIgZGF0YS10bz0iQ3V0b3ZlciIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxMDkzLjI1Miw1OC40NSAxMTQxLjI1Miw1OC40NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU291cmNlIiBkYXRhLWxhYmVsPSLshozsiqQgREIgOiBSZWRvL0JpbmxvZyDtirjrnpzsnq3shZgg66Gc6re4IOuwnOyDnSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIyOTYuMTEyOTk5OTk5OTk5OTQiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxODguMDU2NDk5OTk5OTk5OTciIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7shozsiqQgREIgOiBSZWRvL0JpbmxvZyDtirjrnpzsnq3shZgg66Gc6re4IOuwnOyDnTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ0RDIiBkYXRhLWxhYmVsPSJDREMg7LaU7LacIOyXlOynhCA6IERlYmV6aXVtIC8gQVdTIERNUyAvIEdvbGRlbkdhdGUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzg0LjExMjk5OTk5OTk5OTk0IiB5PSI0MCIgd2lkdGg9IjM0Mi4wNTQ5OTk5OTk5OTk5NSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNTU1LjE0MDUiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5DREMg7LaU7LacIOyXlOynhCA6IERlYmV6aXVtIC8gQVdTIERNUyAvIEdvbGRlbkdhdGU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlRhcmdldCIgZGF0YS1sYWJlbD0i7YOA6rKfIERCIDog7J207KKFL+uPmeyihSDtg4Dqsp8g7Iuk7Iuc6rCEIOyLpOyLnOqwhCDsoIHsmqkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNzc0LjE2Nzk5OTk5OTk5OTkiIHk9IjQwIiB3aWR0aD0iMzE5LjA4Mzk5OTk5OTk5OTk1IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iOTMzLjcwOTk5OTk5OTk5OTgiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7tg4Dqsp8gREIgOiDsnbTsooUv64+Z7KKFIO2DgOqynyDsi6Tsi5zqsIQg7Iuk7Iuc6rCEIOyggeyaqTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ3V0b3ZlciIgZGF0YS1sYWJlbD0i7Lu37Jik67KEIDog7KeA7Jew7Iuc6rCEIDAg7Iuc7KCQIOyLnOyKpO2FnCDrrLTspJHri6gg7ISc67mE7IqkIOyghO2ZmCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMTQxLjI1MiIgeT0iNDAiIHdpZHRoPSIzNjYuNTA3OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxMzI0LjUwNTk5OTk5OTk5OTkiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7su7fsmKTrsoQgOiDsp4Dsl7Dsi5zqsIQgMCDsi5zsoJAg7Iuc7Iqk7YWcIOustOykkeuLqCDshJzruYTsiqQg7KCE7ZmYPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

***

#### Ⅱ. CDC 핵심 원리 및 구조

**가. CDC 3대 구현 방식**

| 방식                    | 원리                              | 장점             | 한계             |
| :-------------------- | :------------------------------ | :------------- | :------------- |
| **로그 기반 (Log-Based)** | DB WAL·Redo 로그 직접 파싱            | 성능 영향 최소·실시간 ✅ | DB 권한·로그 접근 필요 |
| **트리거 기반 (Trigger)**  | INSERT·UPDATE·DELETE 트리거로 변경 캡처 | DB 독립적         | 성능 오버헤드 🚨     |
| **타임스탬프 기반**          | updated\_at 컬럼 주기적 폴링           | 구현 단순          | 삭제 탐지 불가·지연 🚨 |

→ **현대 실무 표준: 로그 기반 CDC** (Debezium·AWS DMS·Oracle GoldenGate)

***

**나. CDC 핵심 구성요소**

| **핵심 척도**  | **📊 변경 캡처 계층 🚨**                                                                                                                                       | **🔑 전달·변환 계층 🚨**                                                                                           | **🏁 적재·동기화 계층 💯**                                                                                 |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| **핵심 기술**  | **WAL 파싱**: PostgreSQL WAL·Oracle Redo·MySQL Binlog 실시간 읽기 / **LSN 추적**: 앞서 다룬 **ARIES LSN** 기반 변경 위치 추적 / **이벤트 생성**: INSERT·UPDATE·DELETE·DDL 이벤트 스트림화 | **메시지 큐**: Kafka·Kinesis로 변경 이벤트 버퍼링·순서 보장 / **스키마 변환**: 이기종 DB 간 데이터 타입·컬럼명 매핑 / **필터링**: 민감 데이터 마스킹·PII 제거 | **타깃 DB 적재**: 이벤트 순서대로 타깃 DB에 적용 / **멱등성 보장**: 중복 이벤트 재처리 시 동일 결과 / **지연 모니터링**: 소스-타깃 간 Lag 실시간 측정 |
| **대표 도구**  | **Debezium**: 오픈소스·Kafka Connect 기반 / PostgreSQL·MySQL·Oracle·MongoDB 지원 / **Oracle GoldenGate**: 엔터프라이즈 표준 / **AWS DMS**: 클라우드 관리형 서비스                  | **Apache Kafka**: 변경 이벤트 중간 버퍼·순서 보장 / **Kafka Connect**: 소스·싱크 커넥터 표준화 / **Flink·Spark**: 변환·집계·실시간 처리      | **타깃**: PostgreSQL·Aurora·Redshift·BigQuery·Snowflake / **검증**: 앞서 다룬 **데이터 계약** 품질 기준으로 적재 검증      |
| **무결성 보장** | **트랜잭션 경계 보존**: 다중 테이블 변경을 트랜잭션 단위로 묶어 전달 / 부분 커밋 방지                                                                                                     | **Exactly-Once**: Kafka 트랜잭션으로 중복·유실 없는 정확히 한 번 전달                                                           | **체크섬 검증**: 소스-타깃 행 수·합계 주기적 비교 / 불일치 탐지 시 자동 재동기화                                                  |

***

#### Ⅲ. CDC 기반 무중단 마이그레이션 단계별 흐름

**가. 5단계 무중단 마이그레이션**

```
[CDC 기반 무중단 마이그레이션 전체 흐름]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1단계: 초기 적재 (Initial Load)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
소스 DB 스냅샷 전체 덤프
→ 타깃 DB에 벌크 적재
→ 스냅샷 시점 LSN 기록 (CDC 시작점)
서비스: 계속 운영 중 ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2단계: 실시간 CDC 동기화 (Catch-Up)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
초기 적재 중 발생한 변경 → CDC로 캡처
→ LSN 기준으로 타깃에 순차 적용
→ 소스-타깃 간 Lag 점점 감소
서비스: 계속 운영 중 ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3단계: 동기화 완료·검증 (Validation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Lag ≈ 0 달성 확인
소스-타깃 행 수·체크섬 비교 검증
앞서 다룬 데이터 계약 품질 기준 적용
서비스: 계속 운영 중 ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4단계: 트래픽 전환 (Cutover)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
앞서 다룬 Canary/Blue-Green 배포
→ 쓰기 트래픽 타깃 DB로 전환
→ 전환 시간: 수초~수분 (최소 중단)
→ 소스 DB: 읽기 전용 전환

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5단계: 안정화·소스 폐기 (Decommission)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
타깃 DB 정상 운영 확인
롤백 기간(수일~수주) 경과 후
소스 DB 폐기
```

***

**나. CDC 한계 및 대응**

| 한계             | 내용                                     | 대응 방안                   |
| :------------- | :------------------------------------- | :---------------------- |
| **DDL 변경 처리**  | 스키마 변경(ALTER TABLE) CDC 처리 복잡          | Schema Registry·버전 관리   |
| **대용량 초기 적재**  | 수십 TB 스냅샷 적재 시간 과다                     | 파티션 병렬 적재·오프피크 수행       |
| **이기종 데이터 타입** | Oracle NUMBER→PostgreSQL NUMERIC 변환 오류 | 타입 매핑 테이블 사전 정의         |
| **Lag 급증**     | 대량 배치 처리 시 Lag 폭증                      | Kafka 파티션 확장·소비자 그룹 병렬화 |

***

**(제언)** "CDC 기반 무중단 마이그레이션은 '서비스를 멈추지 않고 DB를 교체하는 외과 수술'로, 앞서 다룬 WAL·LSN·ARIES의 로그 기반 회복 원리가 실시간 동기화로 확장된 것입니다. **핵심 성공 요인은 세 가지 — 초기 적재 시점 LSN 정확한 기록(재동기화 기준), Kafka Exactly-Once로 중복·유실 없는 이벤트 전달, 전환 전 행 수·체크섬 검증으로 데이터 무결성 확인 — 이며, 앞서 다룬 데이터 계약의 품질 기준을 CDC 파이프라인 검증 기준으로 연동하고 Blue-Green 배포와 결합해 롤백 경로를 사전 확보하는 것이 무중단 마이그레이션 리스크 최소화의 핵심입니다.**"
