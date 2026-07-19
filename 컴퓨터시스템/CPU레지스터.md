### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (레지스터 정의, 메모리계층구조상 위치) — 3~4줄
Ⅱ. 레지스터 종류 (본론①, 도식 1개 필수)
Ⅲ. 명령어 실행에서의 역할 (본론②)
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 메모리계층(레지스터→캐시→DRAM→디스크) 중 레지스터가 최상단인 이유는, CPU 내부에 직접 위치해 접근시간이 거의 0에 가깝기 때문"\*\*이라는 한 줄로 시작하면, 오늘 앞서 다룬 "DRAM vs SRAM" 답안과 자연스럽게 이어집니다.

### Ⅱ. 레지스터 종류 — "범·특" (범용 vs 특수목적)

| 구분                                           | 종류                       | 역할                                           |
| :------------------------------------------- | :----------------------- | :------------------------------------------- |
| **범용레지스터** (General Purpose)                 | AX, BX, CX, DX 등(x86 기준) | 연산 중 **임시데이터 저장**, 프로그래머/컴파일러가 자유롭게 활용       |
| **PC** (Program Counter)                     | 특수목적                     | **다음에 실행할 명령어의 주소**를 저장                      |
| **IR** (Instruction Register)                | 특수목적                     | **현재 실행중인 명령어**를 저장(디코딩 대상)                  |
| **MAR/MBR** (Memory Address/Buffer Register) | 특수목적                     | 메모리 **접근주소**(MAR)와 **읽어온/쓸 데이터**(MBR) 임시저장   |
| **SP** (Stack Pointer)                       | 특수목적                     | **스택의 최상단 위치** 저장(함수호출·복귀에 필수)               |
| **PSW/Flag Register** (Program Status Word)  | 특수목적                     | 연산결과의 **상태(Carry, Zero, Overflow 등) 플래그** 저장 |

→ 암기: **"범용은 자유롭게 쓰는 작업대, PC는 다음할일 메모, IR은 지금하는일 적어둔 것, MAR/MBR은 메모리와 주고받는 창구, SP는 스택의 높이표시, PSW는 결과상태 알림판"**

### 도식화 제안

```
        [CPU 내부]
   ┌──────────────┐
   │  범용레지스터    │ ← 연산 중 데이터 임시보관
   │  (AX,BX,CX,DX) │
   ├──────────────┤
   │  PC → 다음 명령어 주소     │
   │  IR → 현재 실행중인 명령어 │
   │  SP → 스택 최상단 위치     │
   │  PSW → 연산결과 상태(플래그) │
   ├──────────────┤
   │  MAR/MBR → 메모리와의 창구(주소/데이터)│
   └──────┬───────┘
          ↓ (버스를 통해 - 앞서 다룬 버스중재 답안과 연결)
      [캐시(SRAM)] → [주기억장치(DRAM)] → [보조기억장치]
```

### Ⅲ. 명령어 실행에서의 역할 — Fetch-Decode-Execute 사이클

**함정 방지: 레지스터를 개별로만 나열하면 절반. "명령어 하나가 실행되는 동안 이들이 어떻게 협업하는가"를 보여줘야 완성됩니다.**

| 단계               | 관여 레지스터             | 동작                                                                      |
| :--------------- | :------------------ | :---------------------------------------------------------------------- |
| **Fetch** (인출)   | PC → MAR → MBR → IR | PC가 가리키는 주소를 MAR에 넣고, 메모리에서 읽은 명령어를 MBR로 받아 IR에 저장. **PC는 다음 주소로 자동증가** |
| **Decode** (해독)  | IR                  | IR에 저장된 명령어를 해석해 **어떤 연산인지, 어떤 레지스터/주소가 필요한지** 판단                       |
| **Execute** (실행) | 범용레지스터, PSW         | ALU가 연산 수행, 결과를 범용레지스터에 저장하고 **PSW에 상태플래그 갱신**(예: 결과가 0이면 Zero플래그 set)  |

→ 앞서 다룬 "제어장치(하드와이어드/마이크로프로그램드)"가 바로 이 Fetch-Decode-Execute 각 단계에서 **필요한 제어신호를 생성**하는 주체였다는 연결 — 오늘 다룬 두 답안(제어장치, 레지스터)이 명령어실행이라는 하나의 사이클 안에서 함께 작동합니다.

**+ 함수호출과 SP/PC의 협업(심화)**: 함수를 호출하면 **현재 PC(복귀주소)를 스택에 저장**(SP가 그 위치를 가리킴)하고, 함수 종료시 **스택에서 복귀주소를 꺼내 PC에 복원**합니다 — 앞서 다룬 "데드락/세마포어"에서 봤던 "상태를 어딘가에 저장하고 나중에 복원한다"는 원리가 여기서도 반복됩니다.

### Ⅳ. 결론 포인트 (오늘 컴퓨터구조 시리즈 대단원)

레지스터는 오늘 다룬 메모리계층구조(SRAM/DRAM/Flash)의 **가장 빠르지만 가장 작은 최상단**이며, 앞서 다룬 제어장치가 이 레지스터들 사이의 데이터흐름을 지휘하고, 버스중재가 레지스터-메모리 간 통로사용권을 조정합니다 — 결국 오늘 하루 다룬 캐시매핑부터 버스중재까지의 모든 컴퓨터구조 주제는, \*\*"CPU 코어의 레지스터를 중심으로, 점점 더 크고 느린 저장장치(캐시→메모리→디스크)로 확장되는 계층구조를 어떻게 관리·보호·조정하는가"\*\*라는 하나의 큰 그림 안에 있었다는 결론으로, 오늘의 방대한 컴퓨터구조·OS 시리즈 전체를 마무리할 수 있습니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "도서관(하드디스크)에서 책을 잔뜩 빌려와 넓은 책상(RAM, 주기억장치)에 펼쳐놓고 공부를 한다. 그런데 CPU는 속도가 미친 듯이 빠르지만 손에 직접 쥐고 있지 않으면 당장 계산을 못 한다. 그래서 눈앞의 연습장 한 귀퉁이처럼 CPU 뇌 한가운데에 박아둔 가장 빠르고 작은 임시 저장 공간이 바로 \*\*'레지스터(Register)'\*\*다. 이 특수 목적 레지스터 군단에는 각자 명확한 역할이 있다. 가장 핵심은 길잡이인 \*\*'PC(프로그램 카운터)'\*\*다. 얘는 무조건 '다음에 가져올 책 페이지(주소)'만 가리킨다. 주소가 정해지면 그 주소를 \*\*'MAR'\*\*이라는 창구에 넘기고, 창구를 통해 메모리에서 데이터(책)를 통째로 뽑아오면 잠시 \*\*'MBR'\*\*에 둔다. 그리고 이 책이 무슨 명령인지 번역하기 위해 \*\*'IR(명령어 레지스터)'\*\*로 넘긴다. 연산이 돌아가면 그 중간 결괏값은 \*\*'AC(누산기)'\*\*에 적어둔다. 이 5개의 레지스터가 톱니바퀴처럼 맞물려 돌아가면서 컴퓨터의 모든 명령어 사이클이 완성된다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 메모리 계층 구조 최상위 피라미드, CPU 레지스터 개요**

* **정의:** CPU 내부에 위치하여, 산술 논리 연산장치(ALU)나 제어장치(CU)가 명령어를 처리하는 동안 필요한 **데이터나 메모리 주소, 혹은 중간 결괏값을 아주 짧은 순간(1\~2 클럭) 동안 임시로 보관하는 초고속 기억장치**.
* **특징:** 플립플롭(Flip-Flop)이나 래치(Latch) 회로들을 묶어서 구성하므로, 캐시(Cache) 메모리나 메인 메모리(RAM)와는 비교도 안 될 만큼 **처리 속도가 컴퓨터 부품 중 가장 빠르나 가격이 제일 비쌈**.

#### **II. \[본론 1] 명령어 인출(Fetch) 사이클에서의 4대 레지스터 협업 메커니즘 (도식화)**

메모리에서 명령어를 가져올 때 레지스터들이 어떻게 협력하는지 보여주는 필수 다이어그램입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3ODMuNDY3OTk5OTk5OTk5OCA4NDQuMiIgd2lkdGg9Ijc4My40Njc5OTk5OTk5OTk4IiBoZWlnaHQ9Ijg0NC4yIiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJDUFVfXyIgZGF0YS1sYWJlbD0iQ1BVIOuCtOu2gCAo7KCc7Ja07J6l7LmYKSI+CiAgPHJlY3QgeD0iODYuNSIgeT0iMjgzLjIwMDAwMDAwMDAwMDA1IiB3aWR0aD0iNjU2Ljk2Nzk5OTk5OTk5OTgiIGhlaWdodD0iNDk1IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iODYuNSIgeT0iMjgzLjIwMDAwMDAwMDAwMDA1IiB3aWR0aD0iNjU2Ljk2Nzk5OTk5OTk5OTgiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9Ijk4LjUiIHk9IjI5Ny4yMDAwMDAwMDAwMDAwNSIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5DUFUg64K067aAICjsoJzslrTsnqXsuZgpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX1JBTSIgZGF0YS1sYWJlbD0i7KO86riw7Ja17J6l7LmYIChSQU0pIj4KICA8cmVjdCB4PSIyOTcuNjEwNSIgeT0iNTgiIHdpZHRoPSIxMDIuODQ4OTk5OTk5OTk5OTkiIGhlaWdodD0iOTYuOSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjI5Ny42MTA1IiB5PSI1OCIgd2lkdGg9IjEwMi44NDg5OTk5OTk5OTk5OSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzA5LjYxMDUiIHk9IjcyIiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPuyjvOq4sOyWteyepey5mCAoUkFNKTwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTUFSIiBkYXRhLXRvPSJSQU0iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IkFkZHJlc3MgQnVzIiBwb2ludHM9IjYyNi4wOTQ0OTk5OTk5OTk5LDUzNC4yIDYyNi4wOTQ0OTk5OTk5OTk5LDc5Ni4yIDc2LjUsNzk2LjIgNzYuNSw0MCAzNDkuMDM0OTk5OTk5OTk5OTcsNDAgMzQ5LjAzNSwxMDIuMDAwMDAwMDAwMDAwMDMiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlJBTSIgZGF0YS10bz0iTUJSIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSJEYXRhIEJ1cyIgcG9pbnRzPSIzNDkuMDM0OTk5OTk5OTk5OTcsMTM4LjkgMzQ5LjAzNDk5OTk5OTk5OTk3LDMyNy4yMDAwMDAwMDAwMDAwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUEMiIGRhdGEtdG89Ik1BUiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7KO87IaMIOuzteyCrCIgcG9pbnRzPSI2MjYuMDk0NDk5OTk5OTk5OSwzODEuMDAwMDAwMDAwMDAwMDYgNjI2LjA5NDQ5OTk5OTk5OTksNDk3LjMwMDAwMDAwMDAwMDA3IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJNQlIiIGRhdGEtdG89IklSIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLrqoXroLnslrQg67O17IKsIiBwb2ludHM9IjM0OS4wMzQ5OTk5OTk5OTk5NywzODEuMDAwMDAwMDAwMDAwMDYgMzQ5LjAzNDk5OTk5OTk5OTk3LDQ5Ny4zMDAwMDAwMDAwMDAwNyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iSVIiIGRhdGEtdG89IkNVIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjM0OS4wMzQ5OTk5OTk5OTk5Nyw1MzQuMiAzNDkuMDM0OTk5OTk5OTk5OTcsNTgyLjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iTUFSIiBkYXRhLXRvPSJSQU0iIGRhdGEtbGFiZWw9IkFkZHJlc3MgQnVzIj4KICA8cmVjdCB4PSIzNiIgeT0iMjAzLjkwMDAwMDAwMDAwMDAzIiB3aWR0aD0iODAuMDIwMDAwMDAwMDAwMDEiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI3Ni4wMSIgeT0iMjE5LjA1MDAwMDAwMDAwMDA0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5BZGRyZXNzIEJ1czwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJSQU0iIGRhdGEtdG89Ik1CUiIgZGF0YS1sYWJlbD0iRGF0YSBCdXMiPgogIDxyZWN0IHg9IjMxOS4wMzQ5OTk5OTk5OTk5NyIgeT0iMjAzLjkiIHdpZHRoPSI1OS44MjQiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzNDguOTQ2OTk5OTk5OTk5OTUiIHk9IjIxOS4wNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+RGF0YSBCdXM8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iUEMiIGRhdGEtdG89Ik1BUiIgZGF0YS1sYWJlbD0i7KO87IaMIOuzteyCrCI+CiAgPHJlY3QgeD0iNTkyLjU5NDQ5OTk5OTk5OTkiIHk9IjQyNC4wMDAwMDAwMDAwMDAxIiB3aWR0aD0iNjYuOTUyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjI2LjA3MDQ5OTk5OTk5OTkiIHk9IjQzOS4xNTAwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7so7zshowg67O17IKsPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209Ik1CUiIgZGF0YS10bz0iSVIiIGRhdGEtbGFiZWw9IuuqheugueyWtCDrs7XsgqwiPgogIDxyZWN0IHg9IjMwOS41MzQ5OTk5OTk5OTk5NyIgeT0iNDI0LjAwMDAwMDAwMDAwMDEiIHdpZHRoPSI3OC44MzIwMDAwMDAwMDAwMSIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjM0OC45NTA5OTk5OTk5OTk5NiIgeT0iNDM5LjE1MDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuuqheugueyWtCDrs7Xsgqw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlBDIiBkYXRhLWxhYmVsPSIxLiBQQyAoUHJvZ3JhbSBDb3VudGVyKQrri6TsnYzsl5Ag7Iuk7ZaJ7ZWgICfso7zshownIOyggOyepSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1MjQuNzIwOTk5OTk5OTk5OSIgeT0iMzI3LjIwMDAwMDAwMDAwMDA1IiB3aWR0aD0iMjAyLjc0Njk5OTk5OTk5OTk2IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjYyNi4wOTQ0OTk5OTk5OTk5IiB5PSIzNTQuMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNjI2LjA5NDQ5OTk5OTk5OTkiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj4xLiBQQyAoUHJvZ3JhbSBDb3VudGVyKTwvdHNwYW4+PHRzcGFuIHg9IjYyNi4wOTQ0OTk5OTk5OTk5IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7ri6TsnYzsl5Ag7Iuk7ZaJ7ZWgICYjMzk77KO87IaMJiMzOTsg7KCA7J6lPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik1BUiIgZGF0YS1sYWJlbD0iTUFSIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU5MC42NyIgeT0iNDk3LjMwMDAwMDAwMDAwMDA3IiB3aWR0aD0iNzAuODQ5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNjI2LjA5NDQ5OTk5OTk5OTkiIHk9IjUxNS43NTAwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5NQVI8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJBTSIgZGF0YS1sYWJlbD0iUkFNIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjEwMi41IiB5PSIzMzUuNjUwMDAwMDAwMDAwMDMiIHdpZHRoPSI3MC44NDg5OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTM3LjkyNDUiIHk9IjM1NC4xIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5SQU08L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik1CUiIgZGF0YS1sYWJlbD0iMy4gTUJSIChNZW1vcnkgQnVmZmVyIFJlZykK66mU66qo66as7JeQ7IScIOq4geyWtOyYqCAn642w7J207YSwL+uqheugueyWtCcg67O06rSAIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjIwMS4zNDkiIHk9IjMyNy4yMDAwMDAwMDAwMDAwNSIgd2lkdGg9IjI5NS4zNzE5OTk5OTk5OTk5NiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjM0OS4wMzQ5OTk5OTk5OTk5NyIgeT0iMzU0LjEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjM0OS4wMzQ5OTk5OTk5OTk5NyIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPjMuIE1CUiAoTWVtb3J5IEJ1ZmZlciBSZWcpPC90c3Bhbj48dHNwYW4geD0iMzQ5LjAzNDk5OTk5OTk5OTk3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rqZTrqqjrpqzsl5DshJwg6riB7Ja07JioICYjMzk7642w7J207YSwL+uqheugueyWtCYjMzk7IOuztOq0gDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJJUiIgZGF0YS1sYWJlbD0iSVIiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzE5LjAzNDk5OTk5OTk5OTk3IiB5PSI0OTcuMzAwMDAwMDAwMDAwMDciIHdpZHRoPSI2MCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIzNDkuMDM0OTk5OTk5OTk5OTciIHk9IjUxNS43NTAwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5JUjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ1UiIGRhdGEtbGFiZWw9IuuqheugueyWtCDtlbTrj4Ug67CPIOyLpO2WiSIgZGF0YS1zaGFwZT0iY2lyY2xlIj4KICA8Y2lyY2xlIGN4PSIzNDkuMDM0OTk5OTk5OTk5OTciIGN5PSI2NzIuMiIgcj0iOTAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzNDkuMDM0OTk5OTk5OTk5OTciIHk9IjY3Mi4yIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7rqoXroLnslrQg7ZW064+FIOuwjyDsi6Ttlok8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJBTSIgZGF0YS1sYWJlbD0iUkFNIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjMxMy42MTA1IiB5PSIxMDIiIHdpZHRoPSI3MC44NDg5OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzQ5LjAzNDk5OTk5OTk5OTk3IiB5PSIxMjAuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlJBTTwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 제어 및 특수 목적(Special Purpose) 레지스터 전격 해부표 (출제 1순위)**

사용자(개발자)가 마음대로 조작할 수 없는 CPU 내부 통제용 핵심 레지스터 5가지입니다.

| **레지스터 명칭** | **영문 풀네임**           | **핵심 역할 및 특징 (키워드 암기)**                                                |
| :---------- | :------------------- | :--------------------------------------------------------------------- |
| **PC**      | Program Counter      | \*\*다음에 실행할 명령어의 '주소(Address)'\*\*를 기억함. 명령어 인출 후 자동으로 1(명령어 길이만큼) 증가. |
| **IR**      | Instruction Register | 주기억장치에서 방금 인출해 온 \*\*현재 실행 중인 '명령어 자체(코드)'\*\*를 보관하여 디코더(해독기)로 넘김.     |
| **MAR**     | Memory Address Reg   | 기억장치에 접근하기 위해 PC에서 넘겨받은 **주소 값을 버스에 태우기 전 임시 보관.**                     |
| **MBR**     | Memory Buffer Reg    | 기억장치에서 읽어 오거나 쓰려는 **데이터/명령어 자체를 버스에서 내려 임시 보관.** (MDR이라고도 함)           |
| **AC**      | Accumulator (누산기)    | 덧셈, 뺄셈 등 산술/논리 연산(ALU)을 수행한 **중간 결괏값**을 임시로 보관하는 레지스터.                 |
| **PSW**     | Program Status Word  | 연산 결과에 따른 \*\*상태(오버플로우, 제로, 부호, 인터럽트 가능 여부 등 플래그)\*\*를 저장하는 상태 레지스터.   |

#### **IV. \[결론/제언] 명령어 아키텍처(CISC vs RISC)에 따른 범용 레지스터 뱅크의 진화**

* **(키워드 위주 2줄 마무리)** "과거 CISC 아키텍처(x86)에서는 메모리에 직접 접근하는 복잡한 명령어 구조 탓에 특수 목적 레지스터의 비중이 절대적이었습니다. 하지만 현대의 속도 중심 \*\*RISC 아키텍처(ARM)\*\*에서는 메모리 접근(Load/Store)을 극도로 최소화하기 위해, 데이터를 메모리에 넣기 전 CPU 안에 잔뜩 쟁여둘 수 있는 **'다량의 범용 레지스터(General Purpose Register) 뱅크'** 구조로 아키텍처가 진화하고 있습니다."
