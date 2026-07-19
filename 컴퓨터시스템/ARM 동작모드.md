ARM동작모드는 앞서 다룬 "제어장치/레지스터" 답안에서 확장된, ARM 아키텍처만의 **보안·권한 관리체계**입니다. 구세대(ARMv7)와 신세대(ARMv8) 개념이 다르다는 게 핵심 함정이라, 이 구분을 먼저 명확히 잡겠습니다.

### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (동작모드 필요성, ARMv7→ARMv8 개념전환) — 3~4줄
Ⅱ. ARMv7 - 모드기반(Mode-based) 방식 (본론①)
Ⅲ. ARMv8 - Exception Level(EL) 방식 (본론②, 도식 1개 필수, 핵심)
Ⅳ. 권한 및 보안상태와의 관계
Ⅴ. 결론
```

포인트: 개요에서 \*\*"ARMv7까지는 '모드(Mode)'라는 이름의 여러 상태를 CPU가 전환하며 권한을 구분했는데, ARMv8(64비트)에서는 이를 'Exception Level(EL0\~EL3)'이라는 숫자체계로 재정리했다"\*\*는 한 줄로 시작하면, 왜 두 세대를 나눠 설명해야 하는지 논리가 섭니다.

### Ⅱ. ARMv7 — 모드기반(Mode-based) 방식

| 모드                  | 용도                                             |
| :------------------ | :--------------------------------------------- |
| **User**            | 일반 애플리케이션 실행(비특권)                              |
| **FIQ/IRQ**         | 고속/일반 인터럽트 처리 — 앞서 다룬 "인터럽트 3방식" 답안과 연결        |
| **Supervisor(SVC)** | OS커널 실행(특권)                                    |
| **Abort**           | 메모리접근 오류처리 — 앞서 다룬 "Segmentation Fault" 답안과 연결 |
| **Undefined**       | 정의되지 않은 명령어 처리                                 |
| **System**          | Supervisor와 동일권한이지만 User모드 레지스터공유              |
| **Hyp(Hypervisor)** | 가상화 지원(ARMv7 후기 추가)                            |

→ 암기: **"평범한 실행(User), 인터럽트대응(FIQ/IRQ), 커널모드(SVC), 오류처리(Abort/Undefined)"** — 각 모드는 앞서 다룬 오늘의 여러 답안(인터럽트, 세그멘테이션폴트)이 실제로 CPU에서 처리되는 "장소"였다는 연결이 핵심입니다.

### Ⅲ. ARMv8 — Exception Level(EL) 방식, 핵심 배점

**함정 방지: ARMv7의 모드이름을 그대로 ARMv8에 적용하면 감점. ARMv8은 "숫자기반 계층(EL0\~EL3)"으로 완전히 재구성됐습니다.**

| EL      | 용도                                    | 권한                          |
| :------ | :------------------------------------ | :-------------------------- |
| **EL0** | 일반 애플리케이션(**Userspace**)              | **최저**(비특권, 시스템레지스터 접근불가)   |
| **EL1** | **OS커널**(리치 OS의 커널코드)                 | 대부분 시스템레지스터 접근가능            |
| **EL2** | **하이퍼바이저**(가상화, KVM 등)                | EL1보다 높은 권한, **선택적 구현**(옵션) |
| **EL3** | **Secure Monitor**(TrustZone 보안전환 관리) | **최고권한**, 보안상태 전환의 유일한 주체   |

→ 암기: **"EL0=앱, EL1=OS, EL2=가상화관리자, EL3=보안관리자"** — 숫자가 커질수록 권한이 커진다는 단순한 규칙입니다. **EL0과 EL1은 필수구현**이지만 **EL2·EL3는 옵션**(구현 안 할 수도 있음)이라는 게 시험에 자주 나오는 포인트입니다.

### 도식화 제안

```
      [EL3] Secure Monitor         ← 최고권한, 보안전환 전담
         ↓ (Secure↔Non-secure 전환은 EL3만 가능)
      [EL2] Hypervisor              ← 가상화(선택적)
         ↓
      [EL1] OS Kernel               ← 게스트OS 커널
         ↓
      [EL0] Application             ← 일반 앱(최저권한)

  권한: EL0 < EL1 < EL2 < EL3
  전환: 예외(Exception) 발생시에만 상위로, 복귀시에만 하위로
```

→ "앞서 다룬 '페이징/세그멘테이션'에서 커널모드↔유저모드 2단계였던 권한구조가, ARM에서는 4단계(EL0\~EL3)로 더 세분화되어 가상화·보안까지 포함한다"는 게 확장된 지점입니다.

### Ⅳ. 권한 및 보안상태와의 관계 — TrustZone 연결 (심화)

**함정 방지: EL(권한레벨)과 Secure/Non-secure(보안상태)를 같은 것으로 혼동하면 감점. 서로 다른 두 축입니다.**

| 축                   | 내용                                                       |
| :------------------ | :------------------------------------------------------- |
| **권한(Privilege) 축** | EL0\~EL3 — "얼마나 강한 권한을 갖는가"                              |
| **보안(Security) 축**  | Secure World / Non-secure World(TrustZone) — "신뢰영역에 있는가" |

→ 이 두 축이 **교차**하면서, 예를 들어 \*\*Secure EL1(신뢰된 보안OS)\*\*과 \*\*Non-secure EL1(일반 게스트OS 커널)\*\*이 별도로 존재할 수 있습니다 — **EL3만이 이 두 보안상태를 전환**시킬 수 있는 유일한 권한을 가진다는 게 핵심입니다.

### Ⅴ. 결론 포인트 (오늘 컴퓨터구조 시리즈 최종연결)

ARM의 동작모드/Exception Level 체계는, 앞서 다룬 **"페이징의 유저모드/커널모드 2단계 보호"를 가상화(하이퍼바이저)와 보안(TrustZone)까지 포함해 4단계로 정교화**한 것입니다 — 이는 오늘 하루 다룬 캐시매핑(주소보호), 세그멘테이션(권한검증), Segmentation Fault(위반시 처리), 인터럽트(FIQ/IRQ가 실제 처리되는 모드) 전체가 \*\*"CPU가 누구에게 얼마나 신뢰를 줄 것인가"\*\*라는 하나의 큰 질문 안에서 서로 맞물려 작동한다는 결론으로, 오늘의 방대한 컴퓨터구조 시리즈를 완결할 수 있습니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "스마트폰의 두뇌인 ARM 프로세서는 철저한 '신분제 사회'로 굴러간다. 카카오톡이나 유튜브 같은 일반 앱이 실행될 때는 가장 권한이 낮은 \*\*'User(사용자) 모드'\*\*에서 논다. 이들은 하드웨어를 함부로 건드릴 수 없다(비특권). 그런데 만약 앱이 카메라를 켜달라고 운영체제에 부탁(SWI 시스템 콜)하거나, 갑자기 전화가 걸려 오거나(인터럽트), 잘못된 메모리를 건드리면(에러), ARM은 시스템을 꽉 통제하기 위해 즉각 신분을 \*\*'특권(Privileged) 모드'\*\*로 격상시킨다. 특권 모드는 OS 커널이 나서는 'Supervisor', 긴급 전화를 받는 'FIQ', 일반 알림을 받는 'IRQ', 뻑난 걸 수습하는 'Abort' 등 6개의 방위군으로 나뉜다. 이렇게 모드를 세세하게 나눈 핵심 이유는 바로 '속도' 때문이다. 각 모드는 위급 상황 전용 레지스터(서랍)를 각자 따로 가지고 있어서, 일반 모드에서 쓰던 데이터를 굳이 RAM에 백업하느라 시간을 버릴 필요 없이 그냥 자기 전용 서랍을 열고 즉시 일 처리를 할 수 있다(레지스터 뱅킹)."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 스마트폰 두뇌의 보호와 신속 처리, ARM 동작 모드 개요**

* **정의:** ARM 프로세서가 예외(Exception) 상황이나 인터럽트, 운영체제 커널의 시스템 콜을 처리할 때, **시스템 자원을 보호하고 응답 속도를 극대화하기 위해 프로세서의 권한 상태를 하드웨어적으로 전환**하는 메커니즘.
* **핵심 원리:** 모드를 크게 프로그램이 도는 \*\*'비특권 모드(User)'\*\*와 운영체제/예외 처리를 담당하는 \*\*'특권 모드(Privileged)'\*\*로 분리하여 샌드박싱(보안) 및 레지스터 뱅킹을 수행함.

#### **II. \[본론 1] 1개의 비특권 모드 vs 6개의 특권 모드 전격 해부표 (출제 1순위)**

전통적인 ARMv7 (32비트) 기준의 7가지 뼈대 모드입니다.

| **모드 그룹**                          | **동작 모드 명칭**               | **발생 원인 / 진입 시점 및 상세 역할**                                                    |
| :--------------------------------- | :------------------------- | :--------------------------------------------------------------------------- |
| **비특권 모드** (Unprivileged)          | 👤 **User (USR)**          | - 일반적인 **애플리케이션(사용자 프로그램)이 정상적으로 실행**되는 모드. - 제한된 권한만 가지며, 강제로 다른 모드로 변경 불가. |
| **특권 모드** (Privileged) 시스템 보호 및 제어 | 👑 **Supervisor (SVC)**    | - 시스템 부팅(Reset) 시 또는 **OS에게 시스템 콜(SWI)을 요청**할 때 진입하는 커널 보호 모드.               |
| <br />                             | ⚡ **FIQ (Fast Interrupt)** | - **초고속 데이터 전송이나 긴급한 하드웨어 인터럽트** 발생 시 진입. (레지스터 뱅킹이 가장 많아 속도 1위).            |
| <br />                             | 🔔 **IRQ (Interrupt)**     | - 키보드, 타이머 등 **일반적인 하드웨어 인터럽트** 발생 시 진입.                                     |
| <br />                             | 💥 **Abort (ABT)**         | - 허용되지 않은 메모리 영역을 건드리거나, 데이터를 못 읽어오는 **메모리 보호 에러(Page Fault 등)** 발생 시 진입.    |
| <br />                             | ❓ **Undefined (UND)**      | - 프로세서가 **해독할 수 없는 알 수 없는 명령어**를 만났을 때 진입. (코프로세서 에뮬레이션 용도).                 |
| <br />                             | 🛠️ **System (SYS)**       | - OS 권한을 가지지만, **User 모드와 레지스터를 완벽히 공유**하여 상태 정보만 제어하는 모드 (ARMv4 추가).        |

#### **III. \[본론 2] 예외 발생에 따른 상태 전이와 속도 혁신 '레지스터 뱅킹' (도식화)**

ARM이 왜 빠른가를 보여주는 핵심 다이어그램입니다. 일반 모드에서 인터럽트(IRQ)가 터지는 순간입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4NDkuODk2IDY1OS42NTYwMDAwMDAwMDAxIiB3aWR0aD0iODQ5Ljg5NiIgaGVpZ2h0PSI2NTkuNjU2MDAwMDAwMDAwMSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMV9Vc2VyX19fX18iIGRhdGEtbGFiZWw9IjEuIFVzZXIg66qo65OcICjsnbzrsJgg7JWxIOyLpO2WiSDspJEpIj4KICA8cmVjdCB4PSIxODcuMTk5MjUwMDAwMDAwMDYiIHk9IjQwIiB3aWR0aD0iNTMzLjk2MiIgaGVpZ2h0PSI5Ni45IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iMTg3LjE5OTI1MDAwMDAwMDA2IiB5PSI0MCIgd2lkdGg9IjUzMy45NjIiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjE5OS4xOTkyNTAwMDAwMDAwNiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+MS4gVXNlciDrqqjrk5wgKOydvOuwmCDslbEg7Iuk7ZaJIOykkSk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSIyX19fSVJRX18iIGRhdGEtbGFiZWw9IjIuIO2VmOuTnOybqOyWtCDsnbjthLDrn73tirggKElSUSkg67Cc7IOdISDwn5qoIj4KICA8cmVjdCB4PSIzNTguNTIyMjUwMDAwMDAwMDQiIHk9IjE5Ni45IiB3aWR0aD0iMjIwLjk1NjAwMDAwMDAwMDAyIiBoZWlnaHQ9IjI0OC45NTYwMDAwMDAwMDAwMiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjM1OC41MjIyNTAwMDAwMDAwNCIgeT0iMTk2LjkiIHdpZHRoPSIyMjAuOTU2MDAwMDAwMDAwMDIiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjM3MC41MjIyNTAwMDAwMDAwNCIgeT0iMjEwLjkiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+Mi4g7ZWY65Oc7Juo7Ja0IOyduO2EsOufve2KuCAoSVJRKSDrsJzsg50hIPCfmqg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSIzX0lSUV9fX19fIiBkYXRhLWxhYmVsPSIzLiBJUlEg7Yq56raMIOuqqOuTnCDsp4TsnoUgKOu5oOuluCDsspjrpqwpIj4KICA8cmVjdCB4PSI0MCIgeT0iNTA1Ljg1NiIgd2lkdGg9Ijc2OS44OTYiIGhlaWdodD0iMTEzLjgwMDAwMDAwMDAwMDAxIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjUwNS44NTYiIHdpZHRoPSI3NjkuODk2IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTE5Ljg1NiIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij4zLiBJUlEg7Yq56raMIOuqqOuTnCDsp4TsnoUgKOu5oOuluCDsspjrpqwpPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJSMCIgZGF0YS10bz0iSVJRX0V2ZW50IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQ4My44MjAyNTAwMDAwMDAwNCwxMjAuOSA0ODMuODIwMjUwMDAwMDAwMDQsMTgwLjkgNDY5LjAwMDI1MDAwMDAwMDA1LDE4MC45IDQ2OS4wMDAyNTAwMDAwMDAwNSwyNDAuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTFIiIGRhdGEtdG89IklSUV9FdmVudCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI2NDUuNjU0MjQ5OTk5OTk5OSwxMjAuOSA2NDUuNjU0MjQ5OTk5OTk5OSwxODAuOSA0NjkuMDAwMjUwMDAwMDAwMDUsMTgwLjkgNDY5LjAwMDI1MDAwMDAwMDA1LDI0MC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDUFNSIiBkYXRhLXRvPSJJUlFfRXZlbnQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjkyLjM0NjI1MDAwMDAwMDA1LDEyMC45IDI5Mi4zNDYyNTAwMDAwMDAwNSwxODAuOSA0NjkuMDAwMjUwMDAwMDAwMDUsMTgwLjkgNDY5LjAwMDI1MDAwMDAwMDA1LDI0MC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJJUlFfRXZlbnQiIGRhdGEtdG89IlIwX0lSUSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0NjkuMDAwMjUwMDAwMDAwMDUsNDI5Ljg1NiA0NjkuMDAwMjUwMDAwMDAwMDUsNDkxLjk2ODUgMjM0LjM2MzAwMDAwMDAwMDAzLDQ5MS45Njg1IDIzNC4zNjMwMDAwMDAwMDAwMyw1NTQuMDgxIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJJUlFfRXZlbnQiIGRhdGEtdG89IkxSX0lSUSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0NjkuMDAwMjUwMDAwMDAwMDUsNDI5Ljg1NiA0NjkuMDAwMjUwMDAwMDAwMDUsNDkxLjk2ODUgNDY0LjczOTUsNDkxLjk2ODUgNDY0LjczOTUsNTU0LjA4MSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iSVJRX0V2ZW50IiBkYXRhLXRvPSJTUFNSIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQ2OS4wMDAyNTAwMDAwMDAwNSw0MjkuODU2IDQ2OS4wMDAyNTAwMDAwMDAwNSw0OTEuOTY4NSA3MDMuNjM3NDk5OTk5OTk5OSw0OTEuOTY4NSA3MDMuNjM3NDk5OTk5OTk5OSw1NTQuMDgxIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJSMCIgZGF0YS1sYWJlbD0i67KU7JqpIFIwflIxMiDsgqzsmqkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDA5LjQ5MzI1MDAwMDAwMDA1IiB5PSI4NCIgd2lkdGg9IjE0OC42NTQiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0ODMuODIwMjUwMDAwMDAwMDQiIHk9IjEwMi40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+67KU7JqpIFIwflIxMiDsgqzsmqk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkxSIiBkYXRhLWxhYmVsPSJSMTQgLyBMUiDsgqzsmqkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTg2LjE0NzI1IiB5PSI4NCIgd2lkdGg9IjExOS4wMTQiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI2NDUuNjU0MjQ5OTk5OTk5OSIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5SMTQgLyBMUiDsgqzsmqk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkNQU1IiIGRhdGEtbGFiZWw9IkNQU1IgKOyDge2DnCDroIjsp4DsiqTthLApIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjIwMy4xOTkyNTAwMDAwMDAwNiIgeT0iODQiIHdpZHRoPSIxNzguMjkzOTk5OTk5OTk5OTgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyOTIuMzQ2MjUwMDAwMDAwMDUiIHk9IjEwMi40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Q1BTUiAo7IOB7YOcIOugiOyngOyKpO2EsCk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IklSUV9FdmVudCIgZGF0YS1sYWJlbD0i7Yq56raMIOuqqOuTnOuhnArtlZjrk5zsm6jslrQg7J6Q64+ZIOyghO2ZmCIgZGF0YS1zaGFwZT0iZGlhbW9uZCI+CiAgPHBvbHlnb24gcG9pbnRzPSI0NjkuMDAwMjUwMDAwMDAwMDUsMjQwLjkwMDAwMDAwMDAwMDAzIDU2My40NzgyNTAwMDAwMDAxLDMzNS4zNzgwMDAwMDAwMDAwNCA0NjkuMDAwMjUwMDAwMDAwMDUsNDI5Ljg1NjAwMDAwMDAwMDA1IDM3NC41MjIyNTAwMDAwMDAwNCwzMzUuMzc4MDAwMDAwMDAwMDQiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0NjkuMDAwMjUwMDAwMDAwMDUiIHk9IjMzNS4zNzgwMDAwMDAwMDAwNCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNDY5LjAwMDI1MDAwMDAwMDA1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7Yq56raMIOuqqOuTnOuhnDwvdHNwYW4+PHRzcGFuIHg9IjQ2OS4wMDAyNTAwMDAwMDAwNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7ZWY65Oc7Juo7Ja0IOyekOuPmSDsoITtmZg8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUjBfSVJRIiBkYXRhLWxhYmVsPSLrspTsmqkgUjB+UjEy64qUIOqzteycoCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxNTIuNjI2MDAwMDAwMDAwMDMiIHk9IjU1NC4wODEiIHdpZHRoPSIxNjMuNDc0IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjM0LjM2MzAwMDAwMDAwMDAzIiB5PSI1NzIuNTMxMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+67KU7JqpIFIwflIxMuuKlCDqs7XsnKA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkxSX0lSUSIgZGF0YS1sYWJlbD0i7J6Q7Iug66eM7J2YIOyghOyaqSDshIDrj4TsmrAg66CI7KeA7Iqk7YSwClIxNF9pcnEgKExSKSDsgqzsmqkhIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM0NC4xIiB5PSI1NTQuMDgxIiB3aWR0aD0iMjQxLjI3OSIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0NjQuNzM5NSIgeT0iNTgwLjk4MSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNDY0LjczOTUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7snpDsi6Drp4zsnZgg7KCE7JqpIOyEgOuPhOyasCDroIjsp4DsiqTthLA8L3RzcGFuPjx0c3BhbiB4PSI0NjQuNzM5NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+UjE0X2lycSAoTFIpIOyCrOyaqSE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU1BTUiIgZGF0YS1sYWJlbD0iU1BTUl9pcnEKKOq4sOyhtCBDUFNSIOyekOuPmSDrsLHsl4UpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjYxMy4zNzg5OTk5OTk5OTk5IiB5PSI1NTQuMDgxIiB3aWR0aD0iMTgwLjUxNyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNzAzLjYzNzQ5OTk5OTk5OTkiIHk9IjU4MC45ODEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjcwMy42Mzc0OTk5OTk5OTk5IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+U1BTUl9pcnE8L3RzcGFuPjx0c3BhbiB4PSI3MDMuNjM3NDk5OTk5OTk5OSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+KOq4sOyhtCBDUFNSIOyekOuPmSDrsLHsl4UpPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik5vdGUiIGRhdGEtbGFiZWw9Ik5vdGUiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9IjU1NC4wODEiIHdpZHRoPSI2OC42MjYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI5MC4zMTMiIHk9IjU3Mi41MzEwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5Ob3RlPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **IV. \[결론/제언] ARMv8(64비트)의 패러다임 전환: Exception Level(EL0\~EL3) 아키텍처**

* **(키워드 위주 2줄 마무리)** "과거의 7가지 동작 모드는 모바일 환경에는 적합했으나, 최신 클라우드 서버나 가상화(Virtualization) 환경을 통제하기에는 한계가 있었습니다. 이에 따라 현대의 **ARMv8(AArch64) 64비트 아키텍처**는 기존 모드들을 통폐합하고, \*\*EL0(앱) → EL1(OS) → EL2(하이퍼바이저) → EL3(보안 모니터/TrustZone)\*\*로 이어지는 4단계의 직관적인 \*\*'예외 수준(Exception Level) 권한 링(Ring) 아키텍처'\*\*로 완벽하게 진화하였습니다."
