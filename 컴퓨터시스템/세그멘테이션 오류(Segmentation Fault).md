### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (Segmentation Fault 정의, 이름의 유래와 오해) — 3~4줄
Ⅱ. 발생원리 (본론①, 도식 1개 필수)
Ⅲ. 발생원인 유형 4가지 (본론②, 핵심 배점)
Ⅳ. Page Fault와의 비교
Ⅴ. 결론
```

포인트: 개요에서 \*\*"이름은 '세그멘테이션'오류지만, 실제로는 페이징을 쓰는 현대시스템에서도 발생 — '유효하지 않은 메모리주소에 접근했을 때 MMU가 이를 감지하고 커널에 신호(SIGSEGV)를 보내는 것'이 진짜 정의"\*\*라는 한 줄로 시작하면, 오늘 다룬 페이징/세그멘테이션 답안의 오해를 정정하며 시작할 수 있습니다.

### Ⅱ. 발생원리 — MMU의 주소검증 실패

| 단계               | 내용                                                                     |
| :--------------- | :--------------------------------------------------------------------- |
| ① **주소변환 시도**    | 프로세스가 메모리에 접근 → **MMU**가 논리주소를 물리주소로 변환 시도(앞서 다룬 페이징/세그멘테이션 답안의 그 MMU) |
| ② **검증실패**       | 해당 주소가 **자신에게 할당되지 않은 영역**이거나, \*\*권한(읽기전용에 쓰기시도 등)\*\*을 위반            |
| ③ **하드웨어 예외 발생** | MMU가 \*\*폴트(Fault)\*\*를 발생시켜 CPU가 커널로 제어권 넘김                           |
| ④ **커널의 신호전달**   | 커널이 해당 프로세스에 **SIGSEGV**(Signal Segmentation Violation) 신호 전달          |
| ⑤ **프로세스 강제종료**  | 대부분 핸들러가 없으면 **프로세스 비정상종료**(Core dump)                                 |

→ 암기: **"MMU가 주소를 검사하다 '이건 네 땅이 아니야' 또는 '거긴 못 건드려'라고 판단하면, 커널이 SIGSEGV를 날려 프로세스를 끝낸다"** — 앞서 다룬 "페이지폴트"(정상적인, 처리가능한 상황)와 이름은 비슷하지만 성격이 완전히 다릅니다.

### 도식화 제안

```
[프로세스] → 메모리주소 접근시도
     ↓
[MMU] 주소검증
     ↓                    ↓
  유효(내영역,권한OK)      무효(남의영역 or 권한위반)
     ↓                    ↓
  정상접근                [하드웨어 예외] → 커널
                             ↓
                        [SIGSEGV 신호]
                             ↓
                        [프로세스 강제종료]
```

### Ⅲ. 발생원인 유형 4가지 — "널·범·읽·해" (실무형 배점 핵심)

**함정 방지: "메모리를 잘못 건드려서 생긴다"고만 답하면 절반. 구체적으로 어떤 코드패턴이 원인인지 나열해야 완성됩니다.**

| 원인              | 코드패턴                                | 설명                                                       |
| :-------------- | :---------------------------------- | :------------------------------------------------------- |
| **널포인터 역참조**    | `int *p = NULL; *p = 5;`            | 가리키는 곳이 없는데(주소0) 접근시도 — **가장 흔한 원인**                     |
| **범위초과 접근**     | `int arr[10]; arr[100] = 1;`        | 배열경계를 벗어난 메모리 침범(Buffer Overflow의 일종)                    |
| **읽기전용영역 쓰기시도** | 코드영역(Text segment, 읽기전용)에 값을 쓰려는 시도 | 앞서 다룬 세그멘테이션의 "코드=읽기전용" 보호가 정상동작한 것                      |
| **해제된 메모리 접근**  | `free(p); *p = 5;` (Use-after-free) | 이미 반납한 메모리를 계속 쓰려는 경우 — **댕글링 포인터(Dangling Pointer)** 문제 |

→ 암기: **"없는곳(널), 넘어간곳(범위초과), 못건드리는곳(읽기전용), 이미버린곳(해제후접근)"** — 4개 모두 결국 \*\*"내 것이 아니거나, 더 이상 유효하지 않은 메모리를 건드린 것"\*\*으로 요약됩니다.

### Ⅳ. Page Fault와의 비교 — 오늘 답안과의 정확한 구분 (핵심 변별력)

**함정 방지: "폴트"라는 이름 때문에 앞서 다룬 페이지폴트와 같은 것으로 오해하면 심각한 감점 포인트입니다.**

| 구분          | **Page Fault** (앞서 다룬 정상 메커니즘)                        | **Segmentation Fault** (오늘 다룬 오류)       |
| :---------- | :---------------------------------------------------- | :-------------------------------------- |
| **성격**      | **정상적**이고 **예상된** 상황(페이지가 디스크에 있어서 못 찾은 것)            | **비정상적** 오류(접근 자체가 잘못됨)                 |
| **처리방식**    | 커널이 **디스크에서 페이지를 가져와** 해결(앞서 다룬 5단계 처리) 후 **명령어 재실행** | 커널이 **SIGSEGV**를 보내고 **프로세스 종료**(복구 안됨) |
| **결과**      | 프로세스는 **계속 실행**(사용자는 지연도 못 느낌)                        | 프로세스는 **강제종료**                          |
| **유효비트 상태** | 유효비트=0이지만 **페이지테이블에 매핑정보는 존재**(디스크 위치 등)              | 매핑정보 자체가 **없거나 권한이 안 맞음**               |

→ 암기: **"Page Fault는 '잠깐 없으니 가져올게(정상,복구가능)', Segmentation Fault는 '네가 접근하면 안되는 곳이야(비정상,복구불가)'"** — 이름이 비슷하다고 성격까지 같다고 생각하면 큰 오해입니다.

### Ⅴ. 결론 포인트 (오늘 메모리/OS 시리즈 최종연결)

Segmentation Fault는 오늘 다룬 **페이징/세그멘테이션의 "주소검증" 메커니즘이 정상적으로 작동해서 나온 결과**입니다 — 즉, 이 오류가 발생한다는 것은 **보호기법이 제대로 일하고 있다는 증거**이기도 합니다(보호가 없었다면 잘못된 메모리를 조용히 덮어써서 더 큰 문제로 이어졌을 것). 오늘 다룬 Race Condition(공유자원 동시접근의 문제)과 Segmentation Fault(개별 프로세스의 잘못된 접근)는 서로 다른 층위의 문제이지만, 둘 다 \*\*"메모리 접근이라는 근본행위를 얼마나 정교하게 통제하는가"\*\*의 문제라는 공통점으로 오늘 하루의 메모리·OS 시리즈를 마무리할 수 있습니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "C/C++ 개발자들을 공포로 몰아넣는 콘솔 에러 창의 단골손님, 'Core Dumped'의 정체가 바로 \*\*'세그멘테이션 오류(Segfault)'\*\*다. 프로그램은 각자 자기만의 방(논리적 메모리 세그먼트)을 배정받는다. 그런데 코딩 실수로 어떤 프로세스가 자기 방의 벽(Limit)을 뚫고 남의 방에 들어가려 하거나, 건드려서는 안 되는 읽기 전용 영역(Read-only)의 글자를 고치려 시도하면, 이를 24시간 감시하던 경찰(운영체제와 MMU 하드웨어)이 즉각 호루라기를 불어(트랩 발생) 그 프로그램을 사살(강제 종료)해버리는 강력한 보안 메커니즘이다. 주로 허공을 가리키는 널(Null) 포인터를 잘못 참조하거나, 배열의 크기를 뚫고 지나가는 버퍼 오버플로우를 낼 때 발생한다. 이는 시스템 전체가 해킹당하거나 망가지는 것을 막기 위한 OS의 필수 방어막이지만 개발자에겐 디버깅 지옥이다. 이 지옥을 벗어나기 위해 Valgrind 같은 분석 도구를 쓰거나, 최근에는 메모리 관리를 알아서 해주는 Java, 그리고 컴파일 단계에서 메모리 소유권을 강제하는 **Rust** 언어가 각광받고 있다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 허가받지 않은 메모리 침범에 대한 OS의 즉각 처단, Segfault 개요**

* **정의:** 실행 중인 프로세스가 **자신에게 허용되지 않은 메모리 영역에 접근**하려 하거나, \*\*허용되지 않은 방식(예: 읽기 전용 영역에 쓰기 시도)\*\*으로 메모리에 접근할 때 하드웨어(MMU)가 이를 감지하고 운영체제가 프로세스를 강제 종료시키는 메모리 보호 결함.
* **목적:** 한 프로그램의 버그나 악의적인 접근(해킹)이 운영체제 커널이나 다른 정상적인 프로세스의 메모리 데이터를 오염시키는 것을 원천 차단하기 위한 샌드박스(Sandbox) 방어 체계. (리눅스는 `SIGSEGV` 시그널을 보냄).

#### **II. \[본론 1] 세그멘테이션 오류를 발생시키는 4대 치명적 원인 (출제 포인트)**

개발자의 어떤 실수가 경찰(OS)을 출동하게 만드는지 명확히 적어야 합니다.

| **발생 원인 (C언어 기준)**                 | **에러 발생 상황 및 상세 설명**                                                                     |
| :--------------------------------- | :--------------------------------------------------------------------------------------- |
| **1. 널(Null) 포인터 역참조**             | 포인터가 실제 메모리 주소가 아닌 `NULL (0)`을 가리키고 있는데, **거기에 억지로 값을 넣거나 읽으려고 시도할 때.** (가장 빈번한 실수)      |
| **2. 댕글링 포인터 (해제된 메모리 사용)**        | `free()` 함수를 통해 운영체제에 \*\*이미 반납해 버린 메모리 주소(허공)\*\*를 포인터가 잊지 않고 다시 찾아가서 조작하려 할 때.         |
| **3. 배열 인덱스 초과 (Buffer Overflow)** | 10칸짜리 배열을 만들어 놓고, \*\*11번째나 100번째 인덱스 위치(남의 메모리 영역)\*\*에 강제로 데이터를 써넣으려 할 때.              |
| **4. 읽기 전용 메모리에 쓰기(Write) 시도**     | 소스코드 세그먼트에 박혀있는 상수 문자열(String Literal) 등, **수정이 금지된 메모리 영역(Read-only)의 값을 변조하려고 시도**할 때. |

#### **III. \[본론 2] 메모리 보호 감시 메커니즘 (MMU와 Limit Register 도식화)**

앞서 '세그멘테이션' 파트에서 배운 주소 변환 과정에서, 에러가 터지는 정확한 시점을 보여주는 도식입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NzYuMTA4NSA4MjUuNDgzIiB3aWR0aD0iNTc2LjEwODUiIGhlaWdodD0iODI1LjQ4MyIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBIiBkYXRhLXRvPSJCIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLrhbzrpqwg7KO87IaMIOyalOyyrQrshLjqt7jrqLztirggUywg7Jik7ZSE7IWLIGQiIHBvaW50cz0iMjgzLjk3ODc1LDc2LjkgMjgzLjk3ODc1LDIwNy41IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJCIiBkYXRhLXRvPSJDIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSJZZXMgKOygleyDgSDsoJHqt7wpIiBwb2ludHM9IjI0Ni42ODE1ODMzMzMzMzMzMiwzOTMuOTg1ODMzMzMzMzMzMzUgMjQ2LjY4MTU4MzMzMzMzMzMyLDQ2Ny4yODMwMDAwMDAwMDAxMyAxNTUuNDUyNSw0NjcuMjgzMDAwMDAwMDAwMTMgMTU1LjQ1MjUsNTU0LjczMzAwMDAwMDAwMDIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkMiIGRhdGEtdG89IkQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTU1LjQ1MjUsNTkxLjYzMzAwMDAwMDAwMDIgMTU1LjQ1MjUsNjM5LjYzMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQiIgZGF0YS10bz0iRSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iTm8gKO2VnOqzhCDstIjqs7whKQrrgqjsnZgg66mU66qo66asIOy5qOuylCDsi5zrj4QiIHBvaW50cz0iMzIxLjI3NTkxNjY2NjY2NjYsMzkzLjk4NTgzMzMzMzMzMzQgMzIxLjI3NTkxNjY2NjY2NjYsNDY3LjI4MyA0MTIuNTA1LDQ2Ny4yODMgNDEyLjUwNSw1NTQuNzMzMDAwMDAwMDAwMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRSIgZGF0YS10bz0iRiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0MTIuNTA1LDU5MS42MzMwMDAwMDAwMDAyIDQxMi41MDUsNjM5LjYzMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iRiIgZGF0YS10bz0iRyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0MTIuNTA1LDY3Ni41MzMgNDEyLjUwNSw3MzEuNjgzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkEiIGRhdGEtdG89IkIiIGRhdGEtbGFiZWw9IuuFvOumrCDso7zshowg7JqU7LKtCuyEuOq3uOuovO2KuCBTLCDsmKTtlITshYsgZCI+CiAgPHJlY3QgeD0iMjIyLjk3ODc1IiB5PSIxMTkuOTAwMDAwMDAwMDAwMDIiIHdpZHRoPSIxMjEuNjAwMDAwMDAwMDAwMDIiIGhlaWdodD0iNDQuNiIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyODMuNzc4NzUiIHk9IjE0Mi4yMDAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSI+PHRzcGFuIHg9IjI4My43Nzg3NSIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPuuFvOumrCDso7zshowg7JqU7LKtPC90c3Bhbj48dHNwYW4geD0iMjgzLjc3ODc1IiBkeT0iMTQuMyI+7IS46re466i87Yq4IFMsIOyYpO2UhOyFiyBkPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQiIgZGF0YS10bz0iQyIgZGF0YS1sYWJlbD0iWWVzICjsoJXsg4Eg7KCR6re8KSI+CiAgPHJlY3QgeD0iMTA4LjQ1MjQ5OTk5OTk5OTk5IiB5PSI0NzQuMjgzMDAwMDAwMDAwMTMiIHdpZHRoPSI5My42ODIwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjE1NS4yOTM1IiB5PSI0ODkuNDMzMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+WWVzICjsoJXsg4Eg7KCR6re8KTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJCIiBkYXRhLXRvPSJFIiBkYXRhLWxhYmVsPSJObyAo7ZWc6rOEIOy0iOqzvCEpCuuCqOydmCDrqZTrqqjrpqwg7Lmo67KUIOyLnOuPhCI+CiAgPHJlY3QgeD0iMzQ3LjUwNSIgeT0iNDc0LjI4MyIgd2lkdGg9IjEyOS45MTYwMDAwMDAwMDAwMyIgaGVpZ2h0PSI0NC42IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjQxMi40NjMiIHk9IjQ5Ni41ODMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSI0MTIuNDYzIiBkeT0iLTMuMzAwMDAwMDAwMDAwMDAwNyI+Tm8gKO2VnOqzhCDstIjqs7whKTwvdHNwYW4+PHRzcGFuIHg9IjQxMi40NjMiIGR5PSIxNC4zIj7rgqjsnZgg66mU66qo66asIOy5qOuylCDsi5zrj4Q8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQSIgZGF0YS1sYWJlbD0iQ1BVIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjI0OS42NjU3NDk5OTk5OTk5NyIgeT0iNDAiIHdpZHRoPSI2OC42MjU5OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI4My45Nzg3NSIgeT0iNTguNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkNQVTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQiIgZGF0YS1sYWJlbD0iTU1V7J2YIO2VnOqzhCDqsoDsgqwK7Jik7ZSE7IWLKGQpICZsdDsgTGltaXQgUmVnaXN0ZXI/IiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjI4My45Nzg3NSwyMDcuNSAzOTUuODcwMjUsMzE5LjM5MTUgMjgzLjk3ODc1LDQzMS4yODMgMTcyLjA4NzI0OTk5OTk5OTk4LDMxOS4zOTE1IiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjI4My45Nzg3NSIgeT0iMzE5LjM5MTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjI4My45Nzg3NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPk1NVeydmCDtlZzqs4Qg6rKA7IKsPC90c3Bhbj48dHNwYW4geD0iMjgzLjk3ODc1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7smKTtlITshYsoZCkgJmx0OyBMaW1pdCBSZWdpc3Rlcj88L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQyIgZGF0YS1sYWJlbD0i64W866asIOyjvOyGjCArIEJhc2UgUmVnaXN0ZXIg642U7ZWoIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwIiB5PSI1NTQuNzMzMDAwMDAwMDAwMiIgd2lkdGg9IjIzMC45MDQ5OTk5OTk5OTk5NyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE1NS40NTI1IiB5PSI1NzMuMTgzMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+64W866asIOyjvOyGjCArIEJhc2UgUmVnaXN0ZXIg642U7ZWoPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJEIiBkYXRhLWxhYmVsPSLrrLzrpqwg66mU66qo66asIFJBTQrsoJXsg4Eg7KCR6re8IOuwjyDsnb3quLAv7JOw6riwIiBkYXRhLXNoYXBlPSJjeWxpbmRlciI+CiAgPHJlY3QgeD0iNjIuNjAwNTAwMDAwMDAwMDEiIHk9IjY0Ni42MzMiIHdpZHRoPSIxODUuNzAzOTk5OTk5OTk5OTgiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDEiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9Im5vbmUiIC8+CiAgPGxpbmUgeDE9IjYyLjYwMDUwMDAwMDAwMDAxIiB5MT0iNjQ2LjYzMyIgeDI9IjYyLjYwMDUwMDAwMDAwMDAxIiB5Mj0iNzAwLjQzMyIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPGxpbmUgeDE9IjI0OC4zMDQ1IiB5MT0iNjQ2LjYzMyIgeDI9IjI0OC4zMDQ1IiB5Mj0iNzAwLjQzMyIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPGVsbGlwc2UgY3g9IjE1NS40NTI1IiBjeT0iNzAwLjQzMyIgcng9IjkyLjg1MTk5OTk5OTk5OTk5IiByeT0iNyIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDxlbGxpcHNlIGN4PSIxNTUuNDUyNSIgY3k9IjY0Ni42MzMiIHJ4PSI5Mi44NTE5OTk5OTk5OTk5OSIgcnk9IjciIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNTUuNDUyNSIgeT0iNjczLjUzMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTU1LjQ1MjUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7rrLzrpqwg66mU66qo66asIFJBTTwvdHNwYW4+PHRzcGFuIHg9IjE1NS40NTI1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7soJXsg4Eg7KCR6re8IOuwjyDsnb3quLAv7JOw6riwPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkUiIGRhdGEtbGFiZWw9IvCfmqggVFJBUCAo64K067aAIOyduO2EsOufve2KuCDrsJzsg50pIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjI5OC45MDUiIHk9IjU1NC43MzMwMDAwMDAwMDAyIiB3aWR0aD0iMjI3LjIwMDAwMDAwMDAwMDAyIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjQxMi41MDUiIHk9IjU3My4xODMwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7wn5qoIFRSQVAgKOuCtOu2gCDsnbjthLDrn73tirgg67Cc7IOdKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRiIgZGF0YS1sYWJlbD0i7Jq07JiB7LK07KCcKE9TKSDstpzrj5kiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzMzLjM2MTUiIHk9IjYzOS42MzMiIHdpZHRoPSIxNTguMjg2OTk5OTk5OTk5OTgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0MTIuNTA1IiB5PSI2NTguMDgzMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7Jq07JiB7LK07KCcKE9TKSDstpzrj5k8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkciIGRhdGEtbGFiZWw9Iu2UhOuhnOyEuOyKpCDsponsi5wg6rCV7KCcIOyiheujjAooU2VnbWVudGF0aW9uIEZhdWx0IC8gQ29yZSBEdW1wZWQpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjI4OC45MDE1IiB5PSI3MzEuNjgzIiB3aWR0aD0iMjQ3LjIwNyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iIzIxMjEyMSIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDEyLjUwNSIgeT0iNzU4LjU4MyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0iI2ZmZiI+PHRzcGFuIHg9IjQxMi41MDUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7tlITroZzshLjsiqQg7KaJ7IucIOqwleygnCDsooXro4w8L3RzcGFuPjx0c3BhbiB4PSI0MTIuNTA1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj4oU2VnbWVudGF0aW9uIEZhdWx0IC8gQ29yZSBEdW1wZWQpPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **IV. \[결론/제언] C/C++ 메모리 한계 극복을 위한 현대적 해결책 (Valgrind와 Rust)**

* **(키워드 위주 2줄 마무리)** "세그멘테이션 오류는 C/C++처럼 개발자에게 메모리 직접 통제권을 주는 언어에서 숙명처럼 발생합니다. 이를 극복하기 위해 실무에서는 **'Valgrind'나 'AddressSanitizer'** 같은 동적 메모리 분석 도구를 CI 파이프라인에 필수적으로 연동하고 있으며, 최근에는 컴파일러 단에서 메모리 소유권(Ownership) 규칙을 강제하여 이 오류를 원천 차단하는 **'Rust' 언어**로 시스템 프로그래밍 패러다임이 이동하고 있습니다."
