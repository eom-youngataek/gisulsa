### **AI 시스템 위협 인텔리전스 표준: MITRE ATLAS**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 기존 ATT&CK만으로는 AI 시스템을 방어할 수 없는가)
Ⅱ. ATLAS 핵심 구조
Ⅲ. 전술별 핵심 기법 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 AI 레드티밍이 'AI 시스템의 안전성을 능동적으로 공격 시뮬레이션해 검증'하는 실행 방법론이라면, MITRE ATLAS(Adversarial Threat Landscape for Artificial-Intelligence Systems)는 그 레드티밍이 참조해야 할 'AI 특화 공격 전술·기법을 체계적으로 분류한 위협 인텔리전스 지식 베이스'다 — MITRE가 전통 IT 시스템을 위해 구축한 ATT\&CK 프레임워크가 침입·횡적이동·데이터유출 같은 범용 사이버 공격 단계를 다뤘다면, 2021년 공개된 ATLAS는 그 위에 앞서 다룬 멤버십 추론 공격·AI 레드티밍의 탈옥 기법·프롬프트 인젝션 같은 AI 고유의 공격을 ATT\&CK와 동일한 전술(Tactics)-기법(Techniques) 매트릭스 구조로 통합해, 방어자가 '우리 AI 시스템의 어느 단계가 어떤 공격에 취약한가'를 표준화된 언어로 진단·공유할 수 있게 만든 프레임워크"\*\*라는 한 줄로 시작하면 전체 맥락이 드러납니다.
\
![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OTYuODk1OTk5OTk5OTk5OTYgMjg2LjcwMDAwMDAwMDAwMDA1IiB3aWR0aD0iNDk2Ljg5NTk5OTk5OTk5OTk2IiBoZWlnaHQ9IjI4Ni43MDAwMDAwMDAwMDAwNSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJSZWNvbiIgZGF0YS10bz0iQWNjZXNzIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjI0OC40NDc5OTk5OTk5OTk5OCw3Ni45IDI0OC40NDc5OTk5OTk5OTk5OCwxMjQuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQWNjZXNzIiBkYXRhLXRvPSJFeGZpbCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyNDguNDQ3OTk5OTk5OTk5OTgsMTYxLjggMjQ4LjQ0Nzk5OTk5OTk5OTk4LDIwOS44IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJSZWNvbiIgZGF0YS1sYWJlbD0iMS4gUmVjb24gJmFtcDsgTUwgU3RhZ2luZyA6IOuNsOydtO2EsCDsmKTsl7wg7KSA67mEIOuwjyDrqqjrjbgg7YOQ7IOJIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjY2LjY3NjAwMDAwMDAwMDAyIiB5PSI0MCIgd2lkdGg9IjM2My41NDM5OTk5OTk5OTk5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjQ4LjQ0Nzk5OTk5OTk5OTk4IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+MS4gUmVjb24gJmFtcDsgTUwgU3RhZ2luZyA6IOuNsOydtO2EsCDsmKTsl7wg7KSA67mEIOuwjyDrqqjrjbgg7YOQ7IOJPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBY2Nlc3MiIGRhdGEtbGFiZWw9IjIuIEluaXRpYWwgQWNjZXNzICZhbXA7IEV2YXNpb24gOiDtlITroaztlITtirgg7J247KCd7IWYIOuwjyDqsIDrk5zroIjsnbwg7Jqw7ZqMIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwIiB5PSIxMjQuOSIgd2lkdGg9IjQxNi44OTU5OTk5OTk5OTk5NiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjQ4LjQ0Nzk5OTk5OTk5OTk4IiB5PSIxNDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjIuIEluaXRpYWwgQWNjZXNzICZhbXA7IEV2YXNpb24gOiDtlITroaztlITtirgg7J247KCd7IWYIOuwjyDqsIDrk5zroIjsnbwg7Jqw7ZqMPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJFeGZpbCIgZGF0YS1sYWJlbD0iMy4gRXhmaWx0cmF0aW9uICZhbXA7IEltcGFjdCA6IOuqqOuNuCDqsIDspJHsuZgg7YOI7LeoIOuwjyDtmZjqsIEv7JWF7JqpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjY2LjY3NjAwMDAwMDAwMDAyIiB5PSIyMDkuOCIgd2lkdGg9IjM2My41NDM5OTk5OTk5OTk5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjI0OC40NDc5OTk5OTk5OTk5OCIgeT0iMjI4LjI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij4zLiBFeGZpbHRyYXRpb24gJmFtcDsgSW1wYWN0IDog66qo6424IOqwgOykkey5mCDtg4jst6gg67CPIO2ZmOqwgS/slYXsmqk8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

***

#### Ⅱ. ATLAS 핵심 구조

**가. ATT\&CK와의 관계**

```
[MITRE ATT&CK → ATLAS 확장 구조]

ATT&CK (전통 IT 위협):
  정찰 → 초기접근 → 실행 → 지속성 → 권한상승
  → 방어회피 → 자격증명접근 → 탐색 → 횡적이동
  → 수집 → 유출 → 영향

ATLAS (AI 특화 확장):
  ATT&CK의 전술 다수를 상속 + AI 고유 전술 추가
    ML 모델 접근(ML Model Access)
    ML 공급망 침해(ML Supply Chain Compromise)
    ML 모델 회피(Evasion)
    ML 공격 준비(ML Attack Staging)

→ 기존 ATT&CK 매트릭스에 AI 공격 표면을
  자연스럽게 이어붙인 확장판 구조
```

**나. ATLAS 매트릭스 핵심 구성**

| 구성요소                   | 내용                                          |
| :--------------------- | :------------------------------------------ |
| **전술(Tactics)**        | 공격자의 목적 단계(왜) / 정찰부터 영향까지 순차 배열             |
| **기법(Techniques)**     | 각 전술을 달성하는 구체적 방법(어떻게)                      |
| **사례연구(Case Studies)** | 실제 발생한 AI 공격 사고 기록(Tay 챗봇 조작·자율주행 표지판 회피 등) |
| **완화책(Mitigations)**   | 각 기법에 대응하는 방어 대책 매핑                         |

***

#### Ⅲ. 전술별 핵심 기법 및 적용 체계

**가. ATLAS 핵심 전술 및 대표 기법**

| 전술 단계                           | 대표 기법                              | 앞서 다룬 연계 개념                     |
| :------------------------------ | :--------------------------------- | :------------------------------ |
| **정찰(Reconnaissance)**          | 피해자 ML 시스템 정보 수집·모델 아키텍처 추정        | AI 레드티밍의 사전 정찰 단계               |
| **자원 개발(Resource Development)** | 공격용 적대적 데이터셋·프록시 모델 확보             | 그림자 모델(Shadow Model) 구축         |
| **ML 모델 접근(ML Model Access)**   | API를 통한 블랙박스 질의 접근 확보              | 멤버십 추론 공격의 블랙박스 전제조건            |
| **ML 공급망 침해**                   | 오픈소스 사전학습 모델에 백도어 삽입               | 앞서 다룬 **SLSA·SBOM** 공급망 무결성과 직결 |
| **초기 접근(Initial Access)**       | 프롬프트 인젝션으로 LLM 시스템 진입              | AI 레드티밍의 프롬프트 인젝션 공격 유형         |
| **ML 모델 회피(Evasion)**           | 적대적 예제(Adversarial Example)로 탐지 우회 | 이미지 분류기 오분류 유도                  |
| **탈취(Exfiltration)**            | 모델 추출(Model Extraction)로 지적재산 탈취   | 질의-응답 반복으로 모델 복제                |
| **영향(Impact)**                  | 모델 성능 저하·데이터 오염(Poisoning)         | 학습 데이터 오염으로 백도어 삽입              |

**나. 핵심 공격 기법 상세**

| 기법                          | 원리                           | 방어책(Mitigation)              |
| :-------------------------- | :--------------------------- | :--------------------------- |
| **데이터 오염(Data Poisoning)**  | 학습 데이터에 악의적 샘플 주입해 백도어 삽입    | 데이터 출처 검증·이상치 탐지             |
| **모델 추출(Model Extraction)** | 대량 질의-응답으로 대체 모델 학습해 지적재산 복제 | 쿼리 레이트 리미팅·워터마킹              |
| **회피 공격(Evasion Attack)**   | 입력에 미세 노이즈 추가해 오분류 유도        | 적대적 학습(Adversarial Training) |
| **프롬프트 인젝션**                | 악성 지시를 입력에 은닉해 LLM 통제권 탈취    | 입력 검증·시스템 프롬프트 격리            |
| **멤버십 추론**                  | 앞서 다룬 특정 데이터의 학습 포함 여부 역추론   | 앞서 다룬 **DP-SGD**·차분 프라이버시    |

**다. ATLAS vs ATT\&CK vs OWASP LLM Top 10 비교**

| 비교 항목        | ATT\&CK      | ATLAS                      | OWASP LLM Top 10           |
| :----------- | :----------- | :------------------------- | :------------------------- |
| **대상 범위**    | 전통 IT 시스템 전반 | **AI/ML 시스템 전체(모든 모델 유형)** | LLM 애플리케이션 특화              |
| **구조**       | 전술-기법 매트릭스   | **ATT\&CK 구조 확장 상속**       | 취약점 순위 목록                  |
| **주 사용자**    | SOC·위협 헌팅 팀  | **AI 보안팀·레드팀**             | LLM 앱 개발자                  |
| **실제 사고 매핑** | 있음           | **있음(사례연구 포함)**            | 제한적                        |
| **상호 관계**    | 기반 프레임워크     | ATT\&CK를 계승·확장             | ATLAS의 LLM 세부 영역과 상당 부분 중첩 |

**라. 실무 적용 체계**

| 활용 방식               | 내용                                             |
| :------------------ | :--------------------------------------------- |
| **위협 모델링**          | 자사 AI 시스템 아키텍처에 ATLAS 전술-기법을 매핑해 취약 지점 사전 식별   |
| **AI 레드티밍 시나리오 설계** | ATLAS 기법 목록을 레드팀 공격 시나리오의 체크리스트로 활용            |
| **보안 로드맵 우선순위화**    | 자사에 해당하는 기법 우선 완화책부터 투자 순위 결정                  |
| **사고 대응 사후분석**      | 발생한 AI 보안 사고를 ATLAS 전술-기법으로 분류해 조직 내 공통 언어로 보고 |

***

**(제언)** "MITRE ATLAS의 핵심 가치는 AI 보안이라는 신생 분야에서 각 조직·연구자가 제각각의 용어로 공격을 설명하던 파편화된 상황을, 이미 20년 가까이 검증된 ATT\&CK의 전술-기법 언어 체계 위에 자연스럽게 얹어 즉시 통용 가능한 공통 어휘를 제공했다는 점입니다. 다만 ATLAS는 위협을 분류하고 명명하는 지식 베이스일 뿐 그 자체로 방어를 자동화하지는 않으므로, 실무에서는 앞서 다룬 AI 레드티밍의 공격 시나리오 설계 단계에서 ATLAS 매트릭스를 체크리스트처럼 활용하고 공급망 관련 기법에 대해서는 앞서 다룬 SLSA·SBOM 체계와 결합해 사전학습 모델의 출처와 무결성을 검증하는 것이 이 프레임워크를 실질적 방어력으로 전환하는 핵심입니다.

***

**앞서 다룬 개념과의 연결**

| 연계 개념               | 연결 내용                                      |
| :------------------ | :----------------------------------------- |
| **AI 레드티밍**         | ATLAS 매트릭스가 레드티밍 공격 시나리오 설계의 표준 참조 목록 역할   |
| **멤버십 추론 공격**       | ATLAS의 정찰·수집 전술에 속하는 대표 기법으로 명시적 매핑        |
| **SLSA·SBOM**       | ML 공급망 침해 전술 방어를 위한 모델 출처·무결성 검증 체계        |
| **차분 프라이버시·DP-SGD** | 멤버십 추론·데이터 재구성 기법에 대한 ATLAS 완화책과 직접 연결     |
| **인공지능기본법 고영향 AI**  | ATLAS 기반 위협 모델링 결과가 AI 영향평가의 기술적 근거 자료로 활용 |
