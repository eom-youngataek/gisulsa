
#### **인프라 자동화의 핵심: IaC (Infrastructure as Code)**

---

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 "클릭"이 아니라 "코드"로 인프라를 관리하는가) — 3~4줄
Ⅱ. IaC 4대 핵심 원칙 체계 (본론①, 도식 1개 필수)
Ⅲ. 주요 도구 비교·IaC 적용 단계별 흐름 (핵심 배점)
Ⅳ. 결론
```

포인트: 개요에서 **"앞서 다룬 플랫폼 엔지니어링(IDP)의 Golden Path가 '개발자에게 표준 파이프라인을 셀프서비스로 제공'한다면, IaC는 그 파이프라인이 동작하는 클라우드·서버·네트워크 인프라 전체를 코드로 선언하고 Git으로 버전 관리해 수동 클릭·SSH 설정의 불일치(Configuration Drift)를 원천 차단하는 인프라 관리 패러다임이다 — 앞서 다룬 DORA의 변경 리드타임·변경 실패율을 동시에 개선하는 가장 직접적 수단이며, 앞서 다룬 DevSecOps의 Shift-Left가 인프라 보안 설정에까지 확장된 것이 IaC 보안(Infrastructure Security as Code)"**이라는 한 줄로 시작하면, 왜 이 답안이 앞서 다룬 DevOps·플랫폼 엔지니어링·DORA·AIDLC 시리즈 전체의 **인프라 자동화 기반**인지 드러납니다.

---

#### Ⅱ. IaC 4대 핵심 원칙 체계

|원칙|내용|위반 시 문제|
|---|---|---|
|**선언적 정의 (Declarative)**|"어떻게(How)"가 아닌 **"무엇이(What) 되어야 하는가"** 를 코드로 선언. Terraform·Kubernetes YAML이 대표. 도구가 현재 상태와 목표 상태의 차이를 자동 계산·적용|명령형(Imperative) 스크립트는 실행 순서·멱등성 관리가 복잡|
|**멱등성 (Idempotency)**|동일 코드를 **몇 번 적용해도 결과가 항상 동일**. 이미 원하는 상태라면 변경 없이 통과. 앞서 다룬 **"Raft의 로그 재적용"**과 동일한 안전성 원칙|비멱등 스크립트 반복 실행 → 중복 리소스 생성·충돌|
|**버전 관리 (Version Control)**|인프라 코드를 **Git으로 관리** → 변경 이력·롤백·코드 리뷰·브랜치 전략 적용. 앞서 다룬 **"GitOps·ArgoCD"**가 IaC 버전 관리의 실천 패턴|수동 설정은 변경 이력 없음 → 누가 언제 무엇을 바꿨는지 불명|
|**불변 인프라 (Immutable Infrastructure)**|서버를 수정(Mutable)하지 않고 **새 버전으로 교체(Replace)** → 설정 드리프트(Configuration Drift) 원천 차단. 앞서 다룬 **"컨테이너·AMI(Amazon Machine Image) 기반 배포"**가 대표 구현|기존 서버 직접 수정 → 눈송이 서버(Snowflake Server) 문제|

→ 암기: **"선언으로 목표를 말하고(Declarative)·몇 번 써도 같은 결과(Idempotency)·Git으로 이력 관리(Version Control)·고치지 말고 교체(Immutable) — 4원칙이 Configuration Drift를 원천 차단"** — 앞서 다룬 **"LINDDUN의 Non-Compliance 위협"**이 IaC로 보안 설정을 코드화하면 감사(Audit) 추적이 자동으로 확보됩니다.

#### 도식화 제안

```
[IaC 핵심 구조: 선언 → 계획 → 적용 → 검증]

개발자/운영자
    ↓ 코드 작성 (HCL·YAML·Python CDK)
Git 저장소 (단일 진실의 원천, SSOT)
    ↓ PR · 코드 리뷰 · 승인
CI 파이프라인
    ├─ IaC 린트(tflint·cfn-lint) → 문법 검사
    ├─ 보안 스캔(tfsec·Checkov) → 보안 정책 위반 탐지
    └─ Plan(dry-run) → 변경 사항 사전 미리보기
         ↓ 승인(HITL)
CD 파이프라인
    └─ Apply → 실제 인프라 생성·변경·삭제
         ↓
실제 인프라 (Cloud·On-Premise·Hybrid)
    ↓ 상태 모니터링 (Drift Detection)
피드백 루프 → 드리프트 발생 시 자동 교정
```

---

#### Ⅲ. 주요 도구 비교·IaC 적용 단계별 흐름 — 핵심 배점

**함정 방지: "코드로 인프라를 관리한다"고만 답하면 절반. Terraform의 State 파일이 왜 단일 장애점이 되는지, Ansible과 Terraform의 역할이 어떻게 나뉘는지, GitOps가 IaC를 풀(Pull) 방식으로 어떻게 실현하는지, 그리고 Policy as Code가 DevSecOps와 어떻게 결합하는지를 단계별로 보여줘야 완성됩니다.**

|단계|활동|
|---|---|
|**Terraform (프로비저닝)**|HashiCorp 개발. HCL(HashiCorp Configuration Language)로 **클라우드 리소스(EC2·VPC·RDS·IAM)를 선언**. **Plan → Apply** 2단계 워크플로. **State 파일**(.tfstate)로 현재 인프라 상태 추적 → S3+DynamoDB 원격 공유로 팀 협업. 멀티 클라우드(AWS·Azure·GCP) 단일 코드베이스 관리|
|**Ansible (구성 관리)**|Red Hat 개발. YAML 플레이북으로 **서버 내부 소프트웨어 설치·설정·패치**를 자동화. **에이전트리스(Agentless)** — SSH만으로 동작. Terraform이 서버를 만들면 Ansible이 그 서버를 설정하는 **역할 분담**. 앞서 다룬 **"IBN의 정책 활성화(Activation)"**와 동일한 구성 자동화 철학|
|**Pulumi (범용 언어 IaC)**|Python·TypeScript·Go·C#으로 인프라 코드 작성. **기존 프로그래밍 언어의 조건문·반복문·함수를 인프라 코드에 직접 활용**. 앞서 다룬 **"에이전틱 코딩"** 도구가 Pulumi 코드를 자동 생성하는 AIDLC 연계에 최적|
|**CDK (Cloud Development Kit)**|AWS·Terraform CDK. Python·TypeScript로 고수준 추상화 컨스트럭트(Construct)를 조합해 인프라 정의. 내부적으로 CloudFormation·Terraform 코드로 합성(Synthesize). **개발자 친화적** — 기존 IDE·테스트 프레임워크 그대로 활용|
|**GitOps (ArgoCD·Flux)**|**Git이 인프라의 단일 진실의 원천(SSOT)**. 앞서 다룬 **"Kubernetes·ArgoCD"**가 Git 저장소를 지속 감시 → 클러스터 상태가 Git과 다르면 **자동 교정(Pull 방식)**. 푸시(Push) 방식 CI/CD와 달리 **클러스터가 Git에서 원하는 상태를 당겨오는 구조**|
|**Policy as Code (OPA·Sentinel)**|앞서 다룬 **"플랫폼 엔지니어링의 OPA"** — IaC 코드에 보안·컴플라이언스 정책을 코드로 내장. **"모든 S3 버킷은 암호화 필수"·"퍼블릭 SSH 포트 개방 금지"** 정책을 Plan 단계에서 자동 검사. 앞서 다룬 **"DevSecOps의 Shift-Left"**가 인프라 계층까지 확장된 형태|

→ 암기: **"Terraform은 클라우드 리소스를 만들고·Ansible은 그 안에 소프트웨어를 설치하고·Pulumi/CDK는 범용 언어로 코딩하고·GitOps는 Git이 클러스터를 당겨 교정하고·OPA는 정책을 코드로 검사한다"**

**Configuration Drift 탐지와 GitOps 연결** (중요): 앞서 다룬 **"DORA의 변경 실패율(CFR)"**이 높아지는 가장 큰 원인이 바로 Configuration Drift — 수동으로 서버를 수정하면 코드와 실제 인프라 상태가 어긋나고, 이 불일치가 배포 실패·예상치 못한 장애를 유발한다. GitOps는 **ArgoCD가 지속적으로 Git(원하는 상태) vs 클러스터(실제 상태)를 비교**해 차이가 생기면 자동 교정하는 **폐루프(Closed-Loop) Drift 방지 메커니즘**이며, 이는 앞서 다룬 **"IBN의 보장(Assurance)·BBR의 RTprop 지속 측정"**과 동일한 지속 검증·자동 교정 철학의 인프라 레이어 구현입니다.

#### 도식화 제안

```
[IaC 도구 역할 분담 및 GitOps 흐름]

역할 분담:
  Terraform  : 클라우드 리소스 프로비저닝 (VM·네트워크·DB)
  Ansible    : 서버 내부 구성 관리 (OS·미들웨어·앱 설치)
  Pulumi/CDK : 범용 언어 기반 IaC (개발자 친화)
  OPA/Sentinel: 정책 검사 (Plan 단계 보안 게이트)
  ArgoCD/Flux : GitOps 기반 Drift 자동 교정

GitOps 폐루프 흐름:
  PR 작성 → 코드 리뷰 → 승인 → Git 병합
       ↓
  ArgoCD: Git 상태 감시 (30초마다)
       ↓
  클러스터 상태 ≠ Git 상태? → 자동 Apply (Pull 방식)
  클러스터 상태 = Git 상태? → Pass (변경 없음)
       ↓
  Drift 발생 시 알림 + 자동 교정 ✅

IaC 보안 게이트 (Shift-Left):
  코드 작성
    → tflint(린트) → tfsec(보안 스캔) → Plan(미리보기)
    → OPA 정책 검사 → 승인 → Apply
  프로덕션 도달 전 보안 위반 100% 차단 목표
```

**앞서 다룬 DORA·DevSecOps·AIDLC·플랫폼 엔지니어링·Raft와의 연결**: 이런 **"선언적 코드·멱등성·Git 버전 관리·불변 인프라·GitOps 폐루프"** 구조가 실제로는 앞서 다룬 **"DORA의 변경 리드타임·변경 실패율"**을 Terraform Plan·ArgoCD 자동 배포로 직접 단축하고, 앞서 다룬 **"에이전틱 코딩의 HITL"**이 Terraform Plan → 인간 승인 → Apply 워크플로에서 구현되며, 앞서 다룬 **"Raft의 단일 진실(SSOT)"**이 Git 저장소가 인프라의 유일한 진실의 원천이 되는 GitOps 원칙과 동일한 철학을 공유하는 전 과정을 직접 연결합니다.

---

#### Ⅳ. 결론

IaC는 **"클라우드·온프레미스·하이브리드 인프라를 선언적 코드로 정의하고 Git으로 버전 관리해 멱등성·불변 인프라 원칙으로 Configuration Drift를 원천 차단하며, Terraform(프로비저닝)·Ansible(구성관리)·OPA(정책 검사)·ArgoCD GitOps(폐루프 교정)의 역할 분담으로 인프라 전 생애주기를 자동화하는 인프라 관리 패러다임"**이며, 특히 **"GitOps의 Pull 방식 폐루프가 DORA의 변경 실패율을 낮추고, Policy as Code가 DevSecOps의 Shift-Left를 인프라 계층까지 확장해 보안이 기본값으로 동작하게 하는 것"**이 핵심입니다 — 이는 앞서 다룬 **수동 인프라(클릭·SSH·Snowflake Server) → IaC(선언·멱등·버전) → GitOps(Git=SSOT·폐루프 교정) → Policy as Code(보안 게이트) → AIDLC·에이전틱 코딩(AI가 IaC 코드 자동 생성)**을 하나로 잇는 인프라 자동화의 실무적 교량이며, **"인프라도 코드다 — 코드니까 리뷰하고, 테스트하고, 버전을 관리하고, 자동으로 배포하고, 틀리면 Git으로 롤백하는 것이 IaC의 본질"**이라는 결론으로 이어집니다.

### **I. 현대 클라우드 인프라 운영의 자동화 패러다임, IaC의 개요**

**IaC(Infrastructure as Code, 코드 기반 인프라 정의)**는 수동 작업이나 그래픽 사용자 인터페이스 대신, 컴퓨터가 읽을 수 있는 선언적 코드를 사용해 가상 머신, 네트워크, 스토리지 등 인프라 자원을 프로비저닝하고 관리하는 방법론입니다. 인프라 구성을 소프트웨어 코드화함으로써 버전을 관리하고, 테스트를 자동화하며, 개발 환경부터 상용 환경까지 동일한 구성을 신속하게 재현할 수 있어 현대 DevOps 및 GitOps의 근간이 됩니다.

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MzkuMDEyIDc2OS40MDAwMDAwMDAwMDAxIiB3aWR0aD0iNjM5LjAxMiIgaGVpZ2h0PSI3NjkuNDAwMDAwMDAwMDAwMSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iRGV2ZWxvcGVyIiBkYXRhLWxhYmVsPSIxLiDsnbjtlITrnbwg7KCV7J2YIOuLqOqzhCI+CiAgPHJlY3QgeD0iMTAzIiB5PSI1OCIgd2lkdGg9IjE5Ny42OTciIGhlaWdodD0iMjUwLjEiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSIxMDMiIHk9IjU4IiB3aWR0aD0iMTk3LjY5NyIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTE1IiB5PSI3MiIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij4xLiDsnbjtlITrnbwg7KCV7J2YIOuLqOqzhDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IlZlcnNpb25Db250cm9sIiBkYXRhLWxhYmVsPSIyLiDtmJXsg4Eg6rSA66asIOuwjyDtjIzsnbTtlITrnbzsnbgiPgogIDxyZWN0IHg9IjE4OS4yNDU5OTk5OTk5OTk5OCIgeT0iNDM2LjQwMDAwMDAwMDAwMDAzIiB3aWR0aD0iMjU2LjkwMzQ5OTk5OTk5OTk1IiBoZWlnaHQ9IjI2NyIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjE4OS4yNDU5OTk5OTk5OTk5OCIgeT0iNDM2LjQwMDAwMDAwMDAwMDAzIiB3aWR0aD0iMjU2LjkwMzQ5OTk5OTk5OTk1IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyMDEuMjQ1OTk5OTk5OTk5OTgiIHk9IjQ1MC40MDAwMDAwMDAwMDAwMyIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij4yLiDtmJXsg4Eg6rSA66asIOuwjyDtjIzsnbTtlITrnbzsnbg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJUYXJnZXRJbmZyYSIgZGF0YS1sYWJlbD0iMy4g64yA7IOBIOyduO2UhOudvCDqtazshLEiPgogIDxyZWN0IHg9IjMyOC42OTciIHk9IjU4IiB3aWR0aD0iMjcwLjMxNDk5OTk5OTk5OTk0IiBoZWlnaHQ9IjI1MC4xIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iMzI4LjY5NyIgeT0iNTgiIHdpZHRoPSIyNzAuMzE0OTk5OTk5OTk5OTQiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjM0MC42OTciIHk9IjcyIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjMuIOuMgOyDgSDsnbjtlITrnbwg6rWs7ISxPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDb2RlIiBkYXRhLXRvPSJHaXQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IkdpdCBQdXNoIiBwb2ludHM9IjIwMS44NDg1LDI5Mi4xIDIwMS44NDg1LDQxOC40MDAwMDAwMDAwMDAwMyAyODYuOTgyOTk5OTk5OTk5OTUsNDE4LjQwMDAwMDAwMDAwMDAzIDI4Ni45ODI5OTk5OTk5OTk5NSw0ODAuNDAwMDAwMDAwMDAwMDMiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlBpcGVsaW5lIiBkYXRhLXRvPSJDbG91ZCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i65Oc65287J2067KEIC8gQVBJIO2YuOy2nCIgcG9pbnRzPSIzMzIuODUxNSw2ODcuNDAwMDAwMDAwMDAwMSAzMzIuODUxNSw3MjEuNDAwMDAwMDAwMDAwMSA5Myw3MjEuNDAwMDAwMDAwMDAwMSA5Myw0MCA0NjMuODU0NSw0MCA0NjMuODU0NSwxMDIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlN0YXRlIiBkYXRhLXRvPSJQaXBlbGluZSIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iuygle2VqeyEsSDqsoDspp0iIHBvaW50cz0iNDYzLjg1NDUsMjkyLjEgNDYzLjg1NDUsNDE4LjQwMDAwMDAwMDAwMDAzIDM3OC43MTk5OTk5OTk5OTk5Nyw0MTguNDAwMDAwMDAwMDAwMDMgMzc4LjcxOTk5OTk5OTk5OTk3LDU5Ny42IDM2NS4yODQxNjY2NjY2NjY2NCw1OTcuNiAzNjUuMjg0MTY2NjY2NjY2NjQsNjMzLjYiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRGV2IiBkYXRhLXRvPSJDb2RlIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSJJYUMg7L2U65OcIOyekeyEsSAoSENMIC8gWUFNTCkiIHBvaW50cz0iMjAxLjg0ODUsMTM4LjkgMjAxLjg0ODUsMjU1LjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkdpdCIgZGF0YS10bz0iUGlwZWxpbmUiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IkNJL0NEIO2KuOumrOqxsCIgcG9pbnRzPSIyODYuOTgyOTk5OTk5OTk5OTUsNTE3LjMwMDAwMDAwMDAwMDEgMjg2Ljk4Mjk5OTk5OTk5OTk1LDU5Ny42IDMwMC40MTg4MzMzMzMzMzMzLDU5Ny42IDMwMC40MTg4MzMzMzMzMzMzLDYzMy42IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDbG91ZCIgZGF0YS10bz0iU3RhdGUiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyDge2DnCDtjIzsnbwg7ZS865Oc67CxIiBwb2ludHM9IjQ2My44NTQ1LDEzOC45IDQ2My44NTQ1LDI1NS4yIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkNvZGUiIGRhdGEtdG89IkdpdCIgZGF0YS1sYWJlbD0iR2l0IFB1c2giPgogIDxyZWN0IHg9IjE3My4zNDg1IiB5PSIzNTcuMSIgd2lkdGg9IjU2LjI2IiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjAxLjQ3ODUiIHk9IjM3Mi4yNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+R2l0IFB1c2g8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iUGlwZWxpbmUiIGRhdGEtdG89IkNsb3VkIiBkYXRhLWxhYmVsPSLrk5zrnbzsnbTrsoQgLyBBUEkg7Zi47LacIj4KICA8cmVjdCB4PSIzNiIgeT0iNjg0LjEwMDAwMDAwMDAwMDEiIHdpZHRoPSIxMTMuODc4MDAwMDAwMDAwMDQiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI5Mi45MzkwMDAwMDAwMDAwMiIgeT0iNjk5LjI1MDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuuTnOudvOydtOuyhCAvIEFQSSDtmLjstpw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iU3RhdGUiIGRhdGEtdG89IlBpcGVsaW5lIiBkYXRhLWxhYmVsPSLsoJXtlanshLEg6rKA7KadIj4KICA8cmVjdCB4PSI0MjQuMzU0NSIgeT0iMzU3LjEiIHdpZHRoPSI3OC44MzIwMDAwMDAwMDAwMSIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjQ2My43NzA0OTk5OTk5OTk5NyIgeT0iMzcyLjI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7soJXtlanshLEg6rKA7KadPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkRldiIgZGF0YS10bz0iQ29kZSIgZGF0YS1sYWJlbD0iSWFDIOy9lOuTnCDsnpHshLEgKEhDTCAvIFlBTUwpIj4KICA8cmVjdCB4PSIxMjYuMzQ4NDk5OTk5OTk5OTkiIHk9IjE4MS45IiB3aWR0aD0iMTUwLjExMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjIwMS40MDQ0OTk5OTk5OTk5OCIgeT0iMTk3LjA1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5JYUMg7L2U65OcIOyekeyEsSAoSENMIC8gWUFNTCk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iR2l0IiBkYXRhLXRvPSJQaXBlbGluZSIgZGF0YS1sYWJlbD0iQ0kvQ0Qg7Yq466as6rGwIj4KICA8cmVjdCB4PSIyNDUuOTgzIiB5PSI1NjAuMzAwMDAwMDAwMDAwMSIgd2lkdGg9IjgxLjgwMjAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjg2Ljg4NCIgeT0iNTc1LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5DSS9DRCDtirjrpqzqsbA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQ2xvdWQiIGRhdGEtdG89IlN0YXRlIiBkYXRhLWxhYmVsPSLsg4Htg5wg7YyM7J28IO2UvOuTnOuwsSI+CiAgPHJlY3QgeD0iNDExLjM1NDUiIHk9IjE4MS45IiB3aWR0aD0iMTA0LjM3NDAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNDYzLjU0MTUiIHk9IjE5Ny4wNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7IOB7YOcIO2MjOydvCDtlLzrk5zrsLE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkRldiIgZGF0YS1sYWJlbD0i7JeU7KeA64uI7Ja0IChFbmdpbmVlcikiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTE5IiB5PSIxMDIiIHdpZHRoPSIxNjUuNjk3IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTNmMmZkIiBzdHJva2U9IiMxZTg4ZTUiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjIwMS44NDg1IiB5PSIxMjAuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyXlOyngOuLiOyWtCAoRW5naW5lZXIpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDb2RlIiBkYXRhLWxhYmVsPSJJYUMg7IaM7IqkIOy9lOuTnCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMzkuMzc3NSIgeT0iMjU1LjIiIHdpZHRoPSIxMjQuOTQyIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjAxLjg0ODUiIHk9IjI3My42NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+SWFDIOyGjOyKpCDsvZTrk5w8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkdpdCIgZGF0YS1sYWJlbD0iVkNTIChHaXRIdWIgLyBHaXRMYWIpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjIwNS4yNDU5OTk5OTk5OTk5OCIgeT0iNDgwLjQwMDAwMDAwMDAwMDAzIiB3aWR0aD0iMTYzLjQ3NCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2VjZWZmMSIgc3Ryb2tlPSIjMzc0NzRmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIyODYuOTgyOTk5OTk5OTk5OTUiIHk9IjQ5OC44NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+VkNTIChHaXRIdWIgLyBHaXRMYWIpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQaXBlbGluZSIgZGF0YS1sYWJlbD0iR2l0T3BzIC8gQ0kgUGlwZWxpbmUKVGVycmFmb3JtIENsb3VkIC8gQXJnb0NEIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjIzNS41NTM0OTk5OTk5OTk5OSIgeT0iNjMzLjYiIHdpZHRoPSIxOTQuNTk1OTk5OTk5OTk5OTUiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzMzIuODUxNSIgeT0iNjYwLjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjMzMi44NTE1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+R2l0T3BzIC8gQ0kgUGlwZWxpbmU8L3RzcGFuPjx0c3BhbiB4PSIzMzIuODUxNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+VGVycmFmb3JtIENsb3VkIC8gQXJnb0NEPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkNsb3VkIiBkYXRhLWxhYmVsPSLtgbTrnbzsmrDrk5wg66as7IaM7IqkIChWTSwgVlBDLCBLOHMpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM0NC42OTciIHk9IjEwMiIgd2lkdGg9IjIzOC4zMTQ5OTk5OTk5OTk5NCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMmU3ZDMyIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0NjMuODU0NSIgeT0iMTIwLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7tgbTrnbzsmrDrk5wg66as7IaM7IqkIChWTSwgVlBDLCBLOHMpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTdGF0ZSIgZGF0YS1sYWJlbD0i7IOB7YOcIOq0gOumrCDtjIzsnbwgKFN0YXRlIEZpbGUpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM2NC4zMzM1IiB5PSIyNTUuMiIgd2lkdGg9IjE5OS4wNDE5OTk5OTk5OTk5NCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQ2My44NTQ1IiB5PSIyNzMuNjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyDge2DnCDqtIDrpqwg7YyM7J28IChTdGF0ZSBGaWxlKTwvdGV4dD4KPC9nPgo8L3N2Zz4=)

---

### **II. IaC의 두 가지 핵심 접근 방식 비교**

|**비교 항목**|**📢 선언적 접근 방식 (Declarative) 🛠️**|**🏃 명령적 접근 방식 (Imperative) 🏃**|
|---|---|---|
|**개념 정의**|인프라의 최종 도달해야 할 **'목표 상태(What)'**를 정의하면 시스템이 이를 알아서 구성하는 방식|인프라를 구축하기 위해 수행해야 할 **'절차와 순서(How)'**를 하나씩 스크립트로 나열하는 방식|
|**상태 보존(State)**|실시간 인프라의 상태를 기록(State File 등)하여 코드와의 편차(Drift)를 지속 감시|인프라 상태를 직접 추적하지 않으며, 매번 스크립트를 재실행해 상태 변화 유도|
|**동작 방식 특징**|**멱등성(Idempotency)** 보장이 매우 용이하며 코드의 가독성이 높음|코드 작성이 유연하지만, 순서 오류나 실행 도중 실패 시 정합성이 깨질 위험 높음|
|**대표적 기술**|Terraform, CloudFormation, Ansible, Kubernetes Manifest|AWS CLI, Bash Script, Pulumi|

---

### **III. 대표적인 IaC 도구 비교**

|**도구명**|**📦 Terraform**|**⚙️ Ansible**|**🌐 Pulumi**|
|---|---|---|---|
|**유형 및 주요 역할**|프로비저닝 (인프라 자체 구축 및 생성)|구성 관리 (OS 설정 및 소프트웨어 설치/배포)|프로비저닝 (프로그래밍 언어 기반 인프라 구축)|
|**언어 및 가독성**|HCL (HashiCorp Configuration Language)|YAML 형식 (간결하고 가독성 우수)|일반 프로그래밍 언어 (Python, TS, Go 등)|
|**인프라 상태 관리**|State File(tfstate)을 통해 인프라와 1:1 매핑 관리|별도의 상태 파일이 없으며 멱등성 기반으로 매회 실행|Pulumi Service 또는 로컬 파일로 상태 관리|
|**에이전트 유무**|Agentless (클라우드 API 직접 호출)|Agentless (SSH 또는 WinRM 원격 접속 방식)|Agentless (클라우드 API 직접 호출)|

---

### **IV. 안정적인 IaC 운영을 위한 엔터프라이즈 가이드라인**

**IMPORTANT**

1. **상태 파일(State File)의 중앙 관리 및 동시성 락(State Locking) 설정**: Terraform 등의 도구에서 사용되는 상태 파일(`tfstate`)은 인프라의 민감 정보와 비밀번호를 담고 있으므로 로컬에 방치해서는 안 됩니다. 보안이 적용된 원격 저장소(S3 등)에 백업하고, 여러 엔지니어가 동시에 수정할 때 상태 파일이 손상되지 않도록 DynamoDB 등을 이용한 **상태 락(Locking)**을 반드시 연동해야 합니다.
2. **수동 변경(Configuration Drift) 통제**: IaC를 도입했음에도 콘솔이나 터미널을 통해 수동으로 리소스를 임의 조작하면 코드와의 정합성이 깨집니다. 이 편차를 정기적으로 검사하고 차단하는 자동화 도구(Driftctl 등)를 도입하거나, 콘솔의 쓰기 권한을 원천 제한하고 오직 Git PR 및 파이프라인을 통해서만 인프라 변경을 승인하는 **GitOps 거버넌스**를 확립해야 합니다.


