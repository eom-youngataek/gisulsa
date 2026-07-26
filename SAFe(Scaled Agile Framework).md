### **대규모 조직의 애자일 확장: SAFe (Scaled Agile Framework)**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 팀 단위 애자일이 조직 전체로 확장되지 못하는가)
Ⅱ. SAFe 핵심 구조 및 4계층 체계
Ⅲ. 비교 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 심리적 안전감·DORA 지표가 '단일 개발팀의 성과'를 다룬다면, SAFe(Scaled Agile Framework)는 '수십\~수백 개의 애자일 팀이 하나의 기업 전략 아래 정렬되어 동시에 가치를 전달하도록 조율하는 대규모 애자일 확장 프레임워크'다 — Scrum이 단일 팀에는 효과적이나 수백 명 규모의 조직에서는 팀 간 의존성·우선순위 충돌·거버넌스 공백이라는 확장의 벽에 부딪히며, SAFe는 Team(팀)·Program(프로그램)·Large Solution(대규모 솔루션)·Portfolio(포트폴리오)의 4계층으로 이 벽을 허물고 앞서 다룬 IT거버넌스의 전략적 정렬(Strategic Alignment)을 애자일 실행 방식으로 구현하는 세계에서 가장 널리 채택된 확장 애자일 프레임워크"\*\*라는 한 줄로 시작하면 전체 맥락이 드러납니다.

***

#### Ⅱ. SAFe 핵심 구조 및 4계층 체계

**가. SAFe 4계층 구조**

| 계층                 | 명칭         | 핵심 단위                     | 역할                   |
| :----------------- | :--------- | :------------------------ | :------------------- |
| **Team**           | 팀 계층       | Agile Team (Scrum/Kanban) | 개별 팀의 스프린트 실행        |
| **Program**        | 프로그램 계층    | ART (Agile Release Train) | 5\~12개 팀 묶음·PI 단위 조율 |
| **Large Solution** | 대규모 솔루션 계층 | Solution Train            | 다수 ART 조율(초대형 시스템)   |
| **Portfolio**      | 포트폴리오 계층   | Lean Portfolio Management | 전략·예산·투자 우선순위 결정     |

***

**나. SAFe 핵심 개념**

```
[ART (Agile Release Train) 구조]

ART = 5~12개 애자일 팀의 가상 조직
  하나의 제품/솔루션에 함께 기여
  공통 미션·비전 공유
  동일한 PI(Program Increment) 주기로 동기화

[PI (Program Increment)]
  8~12주(보통 5개 스프린트) 단위 계획 주기
  일반 Scrum 스프린트의 상위 개념

PI 계획 흐름:
  ①PI Planning (2일 워크숍)
    ART 전체 팀이 한 자리에 모여
    다음 PI의 기능·목표·의존성 계획
       ↓
  ②5개 스프린트 실행
    각 팀 독립적 스프린트 진행
    2주마다 Scrum of Scrums로 동기화
       ↓
  ③System Demo
    매 스프린트 종료 시 통합 데모
       ↓
  ④Inspect & Adapt (I&A)
    PI 종료 시 전체 회고·개선
```

***

#### Ⅲ. 비교 및 적용 체계

**가. SAFe vs 단일 Scrum vs 기타 확장 프레임워크 비교**

| 비교 항목      | 단일 Scrum      | SAFe                                 | LeSS (Large-Scale Scrum) |
| :--------- | :------------ | :----------------------------------- | :----------------------- |
| **적용 규모**  | 1개 팀 (5\~9명)  | **수백\~수천 명**                         | 수십\~수백 명                 |
| **계층 구조**  | 없음            | 4계층(Team\~Portfolio)                 | 2계층(단순화 지향)              |
| **거버넌스**   | 팀 자율          | Lean Portfolio Management            | 최소 거버넌스                  |
| **역할 복잡도** | 단순(PO·SM·개발자) | **복잡**(RTE·STE·Solution Architect 등) | 단순 유지                    |
| **표준화 수준** | 낮음(자율적)       | **높음**(상세 가이드)                       | 중간                       |
| **채택 용이성** | 즉시 가능         | 조직 변화 관리 필요                          | 상대적 용이                   |

***

**나. SAFe 4계층별 핵심 역할·산출물**

| 계층                 | 핵심 역할                                            | 핵심 산출물                      |
| :----------------- | :----------------------------------------------- | :-------------------------- |
| **Team**           | Scrum Master·Product Owner·개발팀                   | 스프린트 백로그·증분(Increment)      |
| **Program**        | RTE(Release Train Engineer)·Product Management   | PI 목표·Program Backlog       |
| **Large Solution** | STE(Solution Train Engineer)·Solution Management | Solution Backlog·Capability |
| **Portfolio**      | Lean Portfolio Management·Epic Owner             | Strategic Themes·Epic·예산 배분 |

***

**다. 앞서 다룬 개념과의 연결**

| 연계 개념             | 연결 내용                                       |
| :---------------- | :------------------------------------------ |
| **DORA 지표**       | ART 단위로 배포 빈도·변경 실패율 집계·비교                  |
| **심리적 안전감**       | PI Planning의 솔직한 의존성 공유가 심리적 안전감 전제         |
| **IT거버넌스 전략적 정렬** | Lean Portfolio Management = 거버넌스의 애자일 실행 버전 |
| **플랫폼 엔지니어링**     | Solution Train의 공통 플랫폼 팀 = Platform ART     |
| **AIDLC**         | AI 에이전트가 여러 팀의 PI 목표 자동 조율·의존성 탐지 지원 가능     |

***

**라. SAFe 도입 시 주요 리스크**

| 리스크                | 내용                  | 대응 방향                             |
| :----------------- | :------------------ | :-------------------------------- |
| **관료화 위험**         | 계층·역할 과다로 애자일 정신 퇴색 | 최소 실행 가능 SAFe(Essential SAFe)로 시작 |
| **PI Planning 비용** | 수백 명 2일 워크숍 물리적 비용  | 원격 PI Planning 도구 활용              |
| **역할 오버헤드**        | RTE·STE 등 신규 역할 인건비 | 조직 규모에 맞는 SAFe 구성 레벨 선택           |
| **문화 변화 저항**       | 기존 조직 구조·평가 체계 충돌   | 리더십 스폰서십·단계적 전환                   |

***

**(제언)** "SAFe는 '작은 팀의 민첩성을 유지하면서 수백 명 조직의 전략적 일관성을 확보한다'는 상충되는 목표를 계층적 리듬(PI)으로 조율하는 프레임워크입니다. **앞서 다룬 심리적 안전감이 PI Planning에서 팀 간 의존성을 솔직하게 드러내는 전제 조건이 되고, DORA 지표를 ART 단위로 집계해 여러 팀의 배포 성과를 비교·개선하며, Lean Portfolio Management를 통해 앞서 다룬 IT거버넌스의 전략적 정렬을 애자일 실행 리듬으로 구현하는 것이 SAFe 도입의 핵심 가치이나, 관료화 위험을 경계해 조직 규모에 맞는 최소 구성(Essential SAFe)부터 단계적으로 도입하는 것이 실무 성공의 핵심 전략입니다.**"
