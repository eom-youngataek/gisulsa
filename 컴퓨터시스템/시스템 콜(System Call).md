### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (시스템콜 필요성 - 유저/커널모드 분리) — 3~4줄
Ⅱ. 시스템콜 처리과정 (본론①, 도식 1개 필수)
Ⅲ. 시스템콜 유형 (본론②)
Ⅳ. 함수호출과의 차이 및 오버헤드
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 ARM동작모드(EL0=유저, EL1=커널)처럼, 유저프로세스는 파일읽기·메모리할당 같은 하드웨어자원에 직접 접근할 권한이 없다 → 커널에게 '대신 해달라'고 정식으로 요청하는 관문이 시스템콜"\*\*이라는 한 줄로 시작하면, 오늘 다룬 ARM/보호모드 답안과 자연스럽게 이어집니다.

### Ⅱ. 시스템콜 처리과정 — "요·전·수·복" (요청→전환→수행→복귀)

| 단계         | 내용                                                                                                   |
| :--------- | :--------------------------------------------------------------------------------------------------- |
| ① **요청**   | 유저프로그램이 `read()`, `write()` 같은 **라이브러리함수** 호출 → 내부적으로 **트랩(Trap)명령어**(x86: `syscall`, ARM: `svc`) 실행 |
| ② **모드전환** | CPU가 **유저모드→커널모드**로 전환(앞서 다룬 EL0→EL1 전환과 동일원리)                                                       |
| ③ **수행**   | 커널이 **시스템콜테이블**에서 요청된 서비스번호를 찾아 해당 커널함수 실행                                                           |
| ④ **복귀**   | 작업완료 후 **커널모드→유저모드**로 복귀, 결과값 반환                                                                     |

→ 암기: **"유저가 트랩을 걸어 커널을 부르고(요청), 모드가 바뀌고(전환), 커널이 대신 처리하고(수행), 다시 유저로 돌아온다(복귀)"** — 앞서 다룬 "레지스터" 답안의 "인터럽트처리(PC저장→처리→PC복원)"와 정확히 같은 패턴입니다. 사실 시스템콜은 \*\*"소프트웨어가 스스로 발생시키는 인터럽트(트랩)"\*\*입니다.

### 도식화 제안

```
[유저모드(EL0)]                    [커널모드(EL1)]
read() 호출
   ↓
syscall/svc 명령어 실행 ──(트랩)──→ 모드전환
                                     ↓
                              시스템콜테이블 조회
                              (번호→해당 커널함수)
                                     ↓
                              실제 파일읽기 수행
                                     ↓
결과값 수신 ←──────────(복귀)────── 유저모드로 복귀
```

→ "유저 프로그램은 커널 내부코드를 직접 실행하는 게 아니라, '번호'로 요청하고 커널이 그 번호에 맞는 코드를 대신 실행해준다"는 게 핵심 — 앞서 다룬 세그멘테이션의 "보호(읽기전용/권한검증)"가 여기서도 관철됩니다.

### Ⅲ. 시스템콜 유형 — "프·파·장·통" (4대 범주)

| 유형         | 예시                                  |
| :--------- | :---------------------------------- |
| **프로세스제어** | fork(), exec(), exit() — 프로세스 생성/종료 |
| **파일관리**   | open(), read(), write(), close()    |
| **장치관리**   | ioctl() — 하드웨어장치 제어                 |
| **통신**     | socket(), send(), recv() — 네트워크통신   |

→ 앞서 다룬 "IPC 3대기법"에서 메시지패싱·파이프를 실제로 코드에서 쓰려면, 바로 이 시스템콜(pipe(), msgsnd() 등)을 통해야 한다는 연결이 핵심입니다.

### Ⅳ. 함수호출과의 차이 및 오버헤드 — 핵심 배점

**함정 방지: "시스템콜도 그냥 함수호출"이라고 오해하면 절반. 일반함수호출과 근본적으로 다른 비용구조를 보여줘야 완성.**

| 구분       | **일반 함수호출**            | **시스템콜**                        |
| :------- | :--------------------- | :------------------------------ |
| **권한전환** | 없음(유저모드 내에서 계속 실행)     | **있음**(유저↔커널 모드전환)              |
| **비용**   | 저렴(스택에 복귀주소push, jump) | **비쌈**(모드전환+컨텍스트 일부 저장/복원 오버헤드) |
| **실행위치** | 유저프로세스 주소공간            | **커널 주소공간**(별도의 코드영역)           |

→ 암기: **"일반함수호출은 같은 나라 안에서 사무실만 옮기는 것, 시스템콜은 국경을 넘어 다른 나라(커널) 공무원에게 일을 맡기고 오는 것"** — 국경통과(모드전환)에 드는 비용(오버헤드) 때문에, **시스템콜을 너무 자주 호출하면 성능이 떨어진다**는 게 실무적 시사점입니다(예: 파일을 1바이트씩 여러번 read()하는 대신 버퍼링해서 한번에 크게 읽는 이유).

### Ⅴ. 결론 포인트 (오늘 OS/컴퓨터구조 시리즈 총연결)

시스템콜은 오늘 다룬 **ARM동작모드(EL0/EL1 권한분리)**, **세그멘테이션(권한검증)**, **인터럽트(하드웨어트랩)**, \*\*레지스터(PC저장/복원)\*\*가 모두 함께 작동해야 성립하는 종합적 메커니즘입니다 — "유저프로그램이 자유롭게(범용성) 실행되면서도, 위험한 자원접근만큼은 커널이 반드시 통제한다(안전성)"는, 오늘 하루 다룬 전체 시리즈를 관통한 \*\*"자유와 통제 사이의 균형"\*\*이라는 설계원리가 시스템콜이라는 하나의 관문에서 압축적으로 실현된다는 결론으로 마무리할 수 있습니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "일반 카카오톡 같은 앱(사용자 프로세스)은 스마트폰의 하드웨어(카메라, 마이크, 파일 등)를 직접 건드릴 권한이 없다. 무조건 운영체제라는 '절대 군주(Kernel)'의 허락을 받아야 한다. 일반 백성이 왕의 창고에서 물건을 꺼내려면 직접 자물쇠를 따는 게 아니라, 담당 관리에게 '상소문'을 올려 허가를 받아야 하는 것과 같다. 이 상소문을 올리는 통로가 바로 \*\*'시스템 콜(System Call)'\*\*이다. 운영체제는 엉망으로 짜인 앱이나 바이러스가 시스템을 박살 내는 것을 막기 위해 일반인 구역인 \*\*'사용자 모드(User Mode)'\*\*와 왕의 구역인 \*\*'커널 모드(Kernel Mode)'\*\*를 철저히 분리해 두었다. 앱이 파일을 읽기 위해 `read()`라는 시스템 콜을 호출하면, 내부적으로 '소프트웨어 인터럽트(Trap)'가 터지면서 CPU의 권한 비트가 즉시 커널 모드로 바뀐다. 커널이 안전하게 디스크에서 파일을 읽어온 뒤, 다시 권한 비트를 평민으로 강등시키고 앱에게 데이터를 넘겨주며 복귀한다. 결국 시스템 콜은 시스템 전체의 붕괴를 막는 OS의 가장 철저한 방어막이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 하드웨어 자원을 빌려 쓰는 상소문, 시스템 콜(System Call) 개요**

* **정의:** 운영체제의 **이중 모드(Dual Mode)** 환경에서, 권한이 없는 응용 프로그램(사용자 프로세스)이 운영체제의 커널(Kernel)이 제공하는 서비스나 하드웨어 자원(디스크, 메모리, 네트워크 등)에 접근하기 위해 운영체제에게 요청하는 **소프트웨어적 프로그래밍 인터페이스(API)**.
* **목적:** 악의적인 해킹이나 잘못 짜인 코드로부터 메모리, I/O 장치 등 **핵심 시스템 하드웨어 자원을 안전하게 보호(보안)하기 위한 샌드박스 역할**.

#### **II. \[본론 1] 사용자 ↔ 커널 권한 전환, 시스템 콜 동작 메커니즘 (도식화)**

사용자 구역과 커널 구역을 가로지르는 흐름을 도식으로 명확히 보여줍니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MDcuMzUzNDk5OTk5OTk5OSA3ODEuMSIgd2lkdGg9IjYwNy4zNTM0OTk5OTk5OTk5IiBoZWlnaHQ9Ijc4MS4xIiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfX19Vc2VyX01vZGVfTW9kZV9CaXRfXzEiIGRhdGEtbGFiZWw9IvCfkaQg7IKs7Jqp7J6QIOuqqOuTnCAoVXNlciBNb2RlLCBNb2RlIEJpdCA9IDEpIj4KICA8cmVjdCB4PSIxOTIuMjYxNSIgeT0iNDUwLjcwMDAwMDAwMDAwMDA1IiB3aWR0aD0iMzc1LjA5MiIgaGVpZ2h0PSIyNjQuNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjE5Mi4yNjE1IiB5PSI0NTAuNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSIzNzUuMDkyIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyMDQuMjYxNSIgeT0iNDY0LjcwMDAwMDAwMDAwMDA1IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPvCfkaQg7IKs7Jqp7J6QIOuqqOuTnCAoVXNlciBNb2RlLCBNb2RlIEJpdCA9IDEpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX19fS2VybmVsX01vZGVfTW9kZV9CaXRfXzAiIGRhdGEtbGFiZWw9IvCfkZEg7Luk64SQIOuqqOuTnCAoS2VybmVsIE1vZGUsIE1vZGUgQml0ID0gMCkiPgogIDxyZWN0IHg9IjEzMi4xODIwMDAwMDAwMDAwMiIgeT0iNTgiIHdpZHRoPSIyMDUuNzE4MDAwMDAwMDAwMDIiIGhlaWdodD0iMjUwLjEiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSIxMzIuMTgyMDAwMDAwMDAwMDIiIHk9IjU4IiB3aWR0aD0iMjA1LjcxODAwMDAwMDAwMDAyIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxNDQuMTgyMDAwMDAwMDAwMDIiIHk9IjcyIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPvCfkZEg7Luk64SQIOuqqOuTnCAoS2VybmVsIE1vZGUsIE1vZGUgQml0ID0gMCk8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkIiIGRhdGEtdG89IkMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjIuIFRyYXAg67Cc7IOdIQrshoztlITtirjsm6jslrQg7J247YSw65+97Yq4IChpbnQgMHg4MCkiIHBvaW50cz0iNDYwLjM1NDAwMDAwMDAwMDA0LDY5OS4xIDQ2MC4zNTQwMDAwMDAwMDAwNCw3MzMuMSAxMjEuNSw3MzMuMSAxMjEuNSw0MCAyNzQuODA4LDQwIDI3NC44MDgsMTAyIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJEIiBkYXRhLXRvPSJFIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSI1LiBSZXR1cm4gKOygnOyWtOq2jCDrsJjtmZgpCk1vZGUgQml0ID0gMSDrs7XqtawiIHBvaW50cz0iMjc0LjgwOCwyOTIuMSAyNzQuODA4MDAwMDAwMDAwMDUsNDk0LjcwMDAwMDAwMDAwMDA1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBIiBkYXRhLXRvPSJCIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIxLiDtjIzsnbwg7J296riwIOyalOyyrQpyZWFkKCkg7Zi47LacIiBwb2ludHM9IjQ2MC4zNTQwMDAwMDAwMDAwNCw1MzEuNiA0NjAuMzU0MDAwMDAwMDAwMDQsNjYyLjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkMiIGRhdGEtdG89IkQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjQuIOy7pOuEkCDro6jti7Qg7Iuk7ZaJIiBwb2ludHM9IjI3NC44MDgsMTM4LjkgMjc0LjgwOCwyNTUuMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJCIiBkYXRhLXRvPSJDIiBkYXRhLWxhYmVsPSIyLiBUcmFwIOuwnOyDnSEK7IaM7ZSE7Yq47Juo7Ja0IOyduO2EsOufve2KuCAoaW50IDB4ODApIj4KICA8cmVjdCB4PSIzNS45OTk5OTk5OTk5OTk5NyIgeT0iMzU3LjEiIHdpZHRoPSIxNzAuMzA4MDAwMDAwMDAwMDIiIGhlaWdodD0iNDQuNiIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxMjEuMTUzOTk5OTk5OTk5OTgiIHk9IjM3OS40MDAwMDAwMDAwMDAwMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSI+PHRzcGFuIHg9IjEyMS4xNTM5OTk5OTk5OTk5OCIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPjIuIFRyYXAg67Cc7IOdITwvdHNwYW4+PHRzcGFuIHg9IjEyMS4xNTM5OTk5OTk5OTk5OCIgZHk9IjE0LjMiPuyGjO2UhO2KuOybqOyWtCDsnbjthLDrn73tirggKGludCAweDgwKTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkQiIGRhdGEtdG89IkUiIGRhdGEtbGFiZWw9IjUuIFJldHVybiAo7KCc7Ja06raMIOuwmO2ZmCkKTW9kZSBCaXQgPSAxIOuzteq1rCI+CiAgPHJlY3QgeD0iMjEwLjMwODAwMDAwMDAwMDAyIiB5PSIzNTcuMSIgd2lkdGg9IjEyOC43MjgiIGhlaWdodD0iNDQuNiIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyNzQuNjcyIiB5PSIzNzkuNDAwMDAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSIyNzQuNjcyIiBkeT0iLTMuMzAwMDAwMDAwMDAwMDAwNyI+NS4gUmV0dXJuICjsoJzslrTqtowg67CY7ZmYKTwvdHNwYW4+PHRzcGFuIHg9IjI3NC42NzIiIGR5PSIxNC4zIj5Nb2RlIEJpdCA9IDEg67O16rWsPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQSIgZGF0YS10bz0iQiIgZGF0YS1sYWJlbD0iMS4g7YyM7J28IOydveq4sCDsmpTssq0KcmVhZCgpIO2YuOy2nCI+CiAgPHJlY3QgeD0iNDEwLjM1NDAwMDAwMDAwMDA0IiB5PSI1NzQuNjAwMDAwMDAwMDAwMSIgd2lkdGg9Ijk5LjAyOCIgaGVpZ2h0PSI0NC42IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjQ1OS44NjgwMDAwMDAwMDAwNSIgeT0iNTk2LjkwMDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSI0NTkuODY4MDAwMDAwMDAwMDUiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij4xLiDtjIzsnbwg7J296riwIOyalOyyrTwvdHNwYW4+PHRzcGFuIHg9IjQ1OS44NjgwMDAwMDAwMDAwNSIgZHk9IjE0LjMiPnJlYWQoKSDtmLjstpw8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJDIiBkYXRhLXRvPSJEIiBkYXRhLWxhYmVsPSI0LiDsu6TrhJAg66Oo7Yu0IOyLpO2WiSI+CiAgPHJlY3QgeD0iMjIzLjMwODAwMDAwMDAwMDA1IiB5PSIxODEuOSIgd2lkdGg9IjEwMi41OTIwMDAwMDAwMDAwMSIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjI3NC42MDQwMDAwMDAwMDAwNCIgeT0iMTk3LjA1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij40LiDsu6TrhJAg66Oo7Yu0IOyLpO2WiTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQSIgZGF0YS1sYWJlbD0i7J2R7JqpIO2UhOuhnOq3uOueqCDsi6Ttlokg7KSRIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM2OS4zNTQ1MDAwMDAwMDAwMyIgeT0iNDk0LjcwMDAwMDAwMDAwMDA1IiB3aWR0aD0iMTgxLjk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDYwLjM1NDAwMDAwMDAwMDA0IiB5PSI1MTMuMTUwMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7J2R7JqpIO2UhOuhnOq3uOueqCDsi6Ttlokg7KSRPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJCIiBkYXRhLWxhYmVsPSJDIOudvOydtOu4jOufrOumrCAoQVBJKSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzODEuNTgxIiB5PSI2NjIuMiIgd2lkdGg9IjE1Ny41NDYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0NjAuMzU0MDAwMDAwMDAwMDQiIHk9IjY4MC42NTAwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5DIOudvOydtOu4jOufrOumrCAoQVBJKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRSIgZGF0YS1sYWJlbD0i7ZSE66Gc6re4656oIOyerOqwnCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyMDguMjYxNSIgeT0iNDk0LjcwMDAwMDAwMDAwMDA1IiB3aWR0aD0iMTMzLjA5MzAwMDAwMDAwMDAyIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyNzQuODA4IiB5PSI1MTMuMTUwMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7ZSE66Gc6re4656oIOyerOqwnDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQyIgZGF0YS1sYWJlbD0iQyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyNDQuODA4MDAwMDAwMDAwMDIiIHk9IjEwMiIgd2lkdGg9IjYwIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjI3NC44MDgiIHk9IjEyMC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+QzwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRCIgZGF0YS1sYWJlbD0iRCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyNDQuODA4MDAwMDAwMDAwMDIiIHk9IjI1NS4yIiB3aWR0aD0iNjAiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI3NC44MDgiIHk9IjI3My42NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+RDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxNDguMTgyMDAwMDAwMDAwMDIiIHk9IjEwMiIgd2lkdGg9IjY4LjYyNiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE4Mi40OTUiIHk9IjEyMC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Tm90ZTwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 운영체제 통제를 위한 시스템 콜 5대 핵심 유형 (분류표)**

| **분류 유형**                     | **목적 및 기능**                              | **대표적인 시스템 콜 함수 (Unix/Linux 기준)**                              |
| :---------------------------- | :--------------------------------------- | :------------------------------------------------------------- |
| **프로세스 제어** (Process Control) | 프로세스의 생성, 실행, 대기, 메모리 할당 및 종료 등의 생명주기 관리 | `fork()`: 자식 프로세스 복제 생성 `exec()`: 새 프로그램 실행 `exit()`, `wait()` |
| **파일 조작** (File Manipulation) | 하드디스크 내부의 파일을 열고, 읽고, 쓰고, 닫는 일련의 조작      | `open()`, `read()`, `write()`, `close()`                       |
| **장치 관리** (Device Mgmt)       | 마우스, 키보드, 프린터 등의 I/O 장치 접근 및 제어 권한 요구    | `ioctl()`: 하드웨어 파라미터 제어 `read()`, `write()`                    |
| **정보 유지** (Info Maintenance)  | 시스템 시간 확인, 운영체제 버전 등 시스템 정보 설정 및 조회      | `getpid()`: 프로세스 ID 가져오기 `alarm()`, `time()`                   |
| **통신** (Communication)        | 서로 다른 프로세스 간의 데이터 교환 (IPC 3대 기법 지원)      | `pipe()`: 파이프 생성 `shmget()`: 공유 메모리 할당                         |

#### **IV. \[결론/제언] 잦은 권한 전환(Mode Switch) 오버헤드와 API 래퍼(Wrapper)를 통한 추상화**

* **(키워드 위주 2줄 마무리)** "응용 프로그램이 하드웨어를 통제하려면 필수적으로 시스템 콜을 거쳐야 하지만, 잦은 시스템 콜은 사용자 모드와 커널 모드를 오가는 \*\*'모드 스위치(Mode Switch) 오버헤드'\*\*를 극심하게 유발합니다. 따라서 현대의 소프트웨어 개발은 어셈블리어 수준의 날것(Raw) 시스템 콜을 직접 호출하기보다는, 내부적으로 버퍼링을 수행하여 시스템 콜 횟수를 줄여주는 **표준 라이브러리 API (POSIX, Win32 API 등)를 통해 추상화되고 최적화된 방식으로 접근하는 것이 표준 프랙티스**입니다."
