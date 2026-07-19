### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (Race Condition 정의, 발생원인) — 3~4줄
Ⅱ. 발생과정 - 카운터 증가 예제 (본론①, 도식 1개 필수)
Ⅲ. 임계구역(Critical Section) 3대 요구조건 (본론②)
Ⅳ. 해결기법 총정리 (본론③, 오늘 시리즈 연결)
Ⅴ. 결론
```

포인트: 개요에서 \*\*"여러 프로세스/스레드가 공유데이터에 동시에 접근하면서, 접근순서(타이밍)에 따라 결과가 달라지는 현상 — 오늘 다룬 세마포어/뮤텍스/모니터는 모두 이 Race Condition을 막기 위한 도구였다"\*\*는 한 줄로 시작하면, 오늘 시리즈 전체가 이 문제 하나를 풀기 위한 여정이었다는 게 드러납니다.

### Ⅱ. 발생과정 — 카운터 증가(count++) 예제, 가장 유명한 시나리오

**함정 방지: 개념만 설명하면 절반. 실제로 어떻게 결과가 틀어지는지 명령어 단위로 보여줘야 완성됩니다.**

`count++`라는 한 줄의 코드도 실제로는 3단계 기계어로 분해됩니다: **읽기(Load) → 계산(Add) → 쓰기(Store)**. 이 중간에 다른 스레드가 끼어들면 문제가 생깁니다.

| 시간 | Thread A       | Thread B       | count(실제값) |
| :- | :------------- | :------------- | :--------- |
| t1 | Load count(=5) | <br />         | 5          |
| t2 | <br />         | Load count(=5) | 5          |
| t3 | Add 1 → 6      | <br />         | 5          |
| t4 | Store 6        | <br />         | **6**      |
| t5 | <br />         | Add 1 → 6      | 6          |
| t6 | <br />         | Store 6        | **6**      |

→ 두 스레드가 각각 `count++`를 실행했는데, **최종값은 7이 아니라 6**입니다. B가 A의 결과를 못 보고 옛날 값(5)으로 계산했기 때문입니다.

### 도식화 제안

```
정상적(순차)이라면:        Race Condition 발생시:
count=5                    count=5
A: Load(5)→+1→Store(6)     A: Load(5)  B: Load(5) ← 둘다 옛값
count=6                                              (겹침!)
B: Load(6)→+1→Store(7)     A: +1→Store(6)
count=7                    B: +1→Store(6) ← A의 작업이 사라짐
결과: 7 (정상)              결과: 6 (하나의 증가가 유실됨!)
```

→ "타이밍이 겹치면 하나의 연산결과가 통째로 사라진다"는 게 Race Condition의 무서운 지점입니다 — 에러메시지도 없이 조용히 데이터가 틀어집니다.

### Ⅲ. 임계구역(Critical Section) 3대 요구조건 — 해결책이 만족해야 할 기준

**함정 방지: "세마포어 쓰면 됨"이라고 답을 바로 던지면 절반. "좋은 해결책의 기준이 뭔가"부터 짚어야 완성됩니다.**

| 조건                          | 내용                                                                                 |
| :-------------------------- | :--------------------------------------------------------------------------------- |
| **상호배제** (Mutual Exclusion) | 한번에 **하나의 프로세스만** 임계구역 진입 가능                                                       |
| **진행(Progress)**            | 임계구역이 비어있으면, **누군가는 반드시 들어갈 수 있어야** 함(무한정 막히면 안됨)                                  |
| **한계대기** (Bounded Waiting)  | 한 프로세스가 진입요청 후, **다른 프로세스들이 들어가는 횟수에 한계**가 있어야 함(무한정 밀리면 안됨 — 앞서 다룬 Starvation 방지) |

→ 암기: **"한명만 들어가고(상호배제), 비어있으면 누군가 들어가고(진행), 너무 오래 못 기다리게(한계대기)"** — 이 3조건이 세마포어/뮤텍스/모니터 등 **모든 해결기법을 평가하는 공통기준**입니다.

### Ⅳ. 해결기법 총정리 — 오늘 시리즈 완전연결

**함정 방지: Race Condition의 해법이 여러 개 흩어져 있던 오늘의 답안들이었다는 걸 여기서 명시적으로 통합해야 완성됩니다.**

| 계층               | 해결기법                                    | 오늘 다룬 답안          |
| :--------------- | :-------------------------------------- | :---------------- |
| **하드웨어수준**       | Test-and-Set, Compare-and-Swap(원자적 명령어) | 세마포어 답안의 "원자성" 부분 |
| **저수준 동기화도구**    | 세마포어(P/V), 뮤텍스                          | 바로 앞의 답안          |
| **고수준 언어구조**     | 모니터(캡슐화+조건변수)                           | 그 다음 답안           |
| **자원할당 자체의 재설계** | 공유메모리 대신 메시지패싱/파이프 사용                   | IPC 답안            |

→ "Race Condition이라는 하나의 병(원인)을 치료하기 위해, 하드웨어부터 언어구조, 통신방식 설계까지 계층별로 처방이 존재한다"는 게 이 정리의 핵심입니다.

### Ⅴ. 결론 포인트 (오늘 동시성 시리즈 대단원 완결)

Race Condition은 오늘 다룬 우선순위역전·데드락·Starvation·세마포어·뮤텍스·모니터·IPC 전체를 관통하는 \*\*근본원인(Root Cause)\*\*입니다 — "공유자원에 대한 동시접근을 통제하지 않으면, 접근순서(타이밍)라는 우연에 결과가 좌우된다"는 이 하나의 문제가, 통제방식에 따라 데드락(과도한 통제로 순환대기)이나 Starvation(불균등한 통제)이라는 부작용을 낳기도 하고, 세마포어·뮤텍스·모니터라는 점점 더 안전한 해결도구로 발전해왔습니다. \*\*"동시성 프로그래밍의 모든 문제는 결국 Race Condition을 안전하게 막으면서도, 데드락과 Starvation이라는 부작용 없이 처리하는 방법을 찾는 것"\*\*이라는 결론으로, 오늘 하루 다룬 방대한 컴퓨터구조·OS·동시성 시리즈 전체가 완결됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "공동 은행 계좌(공유 자원)에 잔액이 10만 원 있다. 아빠가 ATM에서 1만 원을 입금하려 하고, 동시에 엄마가 앱으로 1만 원을 출금하려 한다. 아빠 프로세스가 '잔액 10만 원'을 확인하고 11만 원으로 고치려 펜을 드는 찰나의 순간에(문맥 교환), 엄마 프로세스가 잽싸게 난입하여 아직 수정 안 된 '잔액 10만 원'을 확인하고 9만 원으로 덮어써 버린다. 그 직후 아빠가 원래 하려던 대로 11만 원으로 다시 덮어써 버리면, 결과적으로 잔액은 10만 원이 아니라 11만 원이 되는 대참사가 터진다. 이렇게 2개 이상의 스레드가 순서를 무시하고 공유 자원에 달려들어, 접근 타이밍에 따라 결과값이 비정상적으로 파괴되는 현상을 \*\*'경쟁 상태(Race Condition)'\*\*라고 부른다. 이를 막기 위해서는 누군가 장부를 볼 때 화장실 문을 걸어 잠그듯 다른 사람을 절대 못 들어오게 막는 **'상호배제(Mutual Exclusion)'** 원칙, 즉 앞서 배운 뮤텍스나 세마포어가 반드시 필요하다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 접근 타이밍이 낳은 데이터 무결성 파괴, 경쟁 상태(Race Condition) 개요**

* **정의:** 2개 이상의 프로세스나 스레드가 하나의 \*\*공유 자원(Shared Data)\*\*에 동시에 접근하여 읽고 쓰는 조작을 가할 때, **접근하는 순서나 타이밍에 따라 실행 결과가 비정상적으로 달라지거나 데이터의 일관성(Consistency)이 깨지는 치명적 현상**.
* **위험성:** 타이밍과 문맥 교환(Context Switching) 주기에 따라 간헐적으로 발생하므로, 디버깅이나 테스트로 잡아내기가 극도로 어려워 시스템에 숨겨진 시한폭탄이 됨.

#### **II. \[본론 1] 경쟁 상태의 발생 메커니즘 (Read-Modify-Write 꼬임 현상)**

가장 대표적인 데이터 덮어쓰기(Overwrite) 파괴 과정을 도식화한 내용입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2OTUuMjI0NSAzNDAiIHdpZHRoPSI2OTUuMjI0NSIgaGVpZ2h0PSIzNDAiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0ic2VxLWFycm93IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI4IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9InNlcS1hcnJvdy1vcGVuIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI4IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5bGluZSBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGxpbmUgY2xhc3M9ImxpZmVsaW5lIiBkYXRhLWFjdG9yPSJQMSIgeDE9IjE3NS44ODA5OTk5OTk5OTk5NyIgeTE9IjcwIiB4Mj0iMTc1Ljg4MDk5OTk5OTk5OTk3IiB5Mj0iMzEwIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtZGFzaGFycmF5PSI2IDQiIC8+CjxsaW5lIGNsYXNzPSJsaWZlbGluZSIgZGF0YS1hY3Rvcj0iTWVtIiB4MT0iMzgyLjA5OTQ5OTk5OTk5OTkiIHkxPSI3MCIgeDI9IjM4Mi4wOTk0OTk5OTk5OTk5IiB5Mj0iMzEwIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtZGFzaGFycmF5PSI2IDQiIC8+CjxsaW5lIGNsYXNzPSJsaWZlbGluZSIgZGF0YS1hY3Rvcj0iUDIiIHgxPSI1ODYuNDY1NSIgeTE9IjcwIiB4Mj0iNTg2LjQ2NTUiIHkyPSIzMTAiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1kYXNoYXJyYXk9IjYgNCIgLz4KPGcgY2xhc3M9Im1lc3NhZ2UiIGRhdGEtZnJvbT0iUDEiIGRhdGEtdG89Ik1lbSIgZGF0YS1sYWJlbD0iMS4gQ291bnQg7J296riwICjqsrDqs7w6IDEwKSIgZGF0YS1saW5lLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1oZWFkPSJmaWxsZWQiIGRhdGEtc2VsZj0iZmFsc2UiPgogIDxsaW5lIHgxPSIxNzUuODgwOTk5OTk5OTk5OTciIHkxPSI5MCIgeDI9IjM4Mi4wOTk0OTk5OTk5OTk5IiB5Mj0iOTAiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjc2VxLWFycm93KSIgLz4KICA8dGV4dCB4PSIyNzguOTkwMjQ5OTk5OTk5OTUiIHk9IjgwIiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1tdXRlZCkiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjEuIENvdW50IOydveq4sCAo6rKw6rO8OiAxMCk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im1lc3NhZ2UiIGRhdGEtZnJvbT0iUDIiIGRhdGEtdG89Ik1lbSIgZGF0YS1sYWJlbD0iMi4gQ291bnQg7J296riwICjslYTsp4Eg6rKw6rO8IDEwKSIgZGF0YS1saW5lLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1oZWFkPSJmaWxsZWQiIGRhdGEtc2VsZj0iZmFsc2UiPgogIDxsaW5lIHgxPSI1ODYuNDY1NSIgeTE9IjE0NSIgeDI9IjM4Mi4wOTk0OTk5OTk5OTk5IiB5Mj0iMTQ1IiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI3NlcS1hcnJvdykiIC8+CiAgPHRleHQgeD0iNDg0LjI4MjQ5OTk5OTk5OTk3IiB5PSIxMzUiIGZvbnQtc2l6ZT0iMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LW11dGVkKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+Mi4gQ291bnQg7J296riwICjslYTsp4Eg6rKw6rO8IDEwKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibWVzc2FnZSIgZGF0YS1mcm9tPSJQMiIgZGF0YS10bz0iTWVtIiBkYXRhLWxhYmVsPSIzLiBDb3VudCDsoIDsnqUgKENvdW50PTkg66GcIOuNruyWtOyUgCkiIGRhdGEtbGluZS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctaGVhZD0iZmlsbGVkIiBkYXRhLXNlbGY9ImZhbHNlIj4KICA8bGluZSB4MT0iNTg2LjQ2NTUiIHkxPSIyMDAiIHgyPSIzODIuMDk5NDk5OTk5OTk5OSIgeTI9IjIwMCIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNzZXEtYXJyb3cpIiAvPgogIDx0ZXh0IHg9IjQ4NC4yODI0OTk5OTk5OTk5NyIgeT0iMTkwIiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1tdXRlZCkiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjMuIENvdW50IOyggOyepSAoQ291bnQ9OSDroZwg642u7Ja07JSAKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibWVzc2FnZSIgZGF0YS1mcm9tPSJQMSIgZGF0YS10bz0iTWVtIiBkYXRhLWxhYmVsPSI0LiDslYTquYwg7ZWY642YIDExIOyggOyepSAoQ291bnQ9MTEg66GcIOuNruyWtOyUgCkiIGRhdGEtbGluZS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctaGVhZD0iZmlsbGVkIiBkYXRhLXNlbGY9ImZhbHNlIj4KICA8bGluZSB4MT0iMTc1Ljg4MDk5OTk5OTk5OTk3IiB5MT0iMjU1IiB4Mj0iMzgyLjA5OTQ5OTk5OTk5OTkiIHkyPSIyNTUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjc2VxLWFycm93KSIgLz4KICA8dGV4dCB4PSIyNzguOTkwMjQ5OTk5OTk5OTUiIHk9IjI0NSIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtbXV0ZWQpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij40LiDslYTquYwg7ZWY642YIDExIOyggOyepSAoQ291bnQ9MTEg66GcIOuNruyWtOyUgCk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vdGUiIGRhdGEtcG9zaXRpb249Im92ZXIiIGRhdGEtYWN0b3JzPSJQMSI+CiAgPHBvbHlnb24gcG9pbnRzPSIzMCw5OCAzMTUuNzYxOTk5OTk5OTk5OTQsOTggMzIxLjc2MTk5OTk5OTk5OTk0LDEwNCAzMjEuNzYxOTk5OTk5OTk5OTQsMTIxIDMwLDEyMSIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8cG9seWdvbiBwb2ludHM9IjMxNS43NjE5OTk5OTk5OTk5NCw5OCAzMjEuNzYxOTk5OTk5OTk5OTQsMTA0IDMxNS43NjE5OTk5OTk5OTk5NCwxMDQiIGZpbGw9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNzUuODgwOTk5OTk5OTk5OTciIHk9IjEwOS41IiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1tdXRlZCkiPjx0c3BhbiB4PSIxNzUuODgwOTk5OTk5OTk5OTciIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij7roIjsp4DsiqTthLAg7Jew7IKwIOykgOu5hCAoMTArMT0xMSk8L3RzcGFuPjx0c3BhbiB4PSIxNzUuODgwOTk5OTk5OTk5OTciIGR5PSIxNC4zIj7wn5qoIOyXrOq4sOyEnCDrrLjrp6XqtZDtmZgg67Cc7IOdITwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub3RlIiBkYXRhLXBvc2l0aW9uPSJvdmVyIiBkYXRhLWFjdG9ycz0iUDIiPgogIDxwb2x5Z29uIHBvaW50cz0iNTA3LjcwNjUsMTUzIDY1OS4yMjQ1LDE1MyA2NjUuMjI0NSwxNTkgNjY1LjIyNDUsMTc2IDUwNy43MDY1LDE3NiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8cG9seWdvbiBwb2ludHM9IjY1OS4yMjQ1LDE1MyA2NjUuMjI0NSwxNTkgNjU5LjIyNDUsMTU5IiBmaWxsPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNTg2LjQ2NTUiIHk9IjE2NC41IiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1tdXRlZCkiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuugiOyngOyKpO2EsCDsl7DsgrAg7JmE66OMICgxMC0xPTkpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub3RlIiBkYXRhLXBvc2l0aW9uPSJvdmVyIiBkYXRhLWFjdG9ycz0iUDEiPgogIDxwb2x5Z29uIHBvaW50cz0iMTE0LjA1MDk5OTk5OTk5OTk2LDIwOCAyMzEuNzEwOTk5OTk5OTk5OTYsMjA4IDIzNy43MTA5OTk5OTk5OTk5NiwyMTQgMjM3LjcxMDk5OTk5OTk5OTk2LDIzMSAxMTQuMDUwOTk5OTk5OTk5OTYsMjMxIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDxwb2x5Z29uIHBvaW50cz0iMjMxLjcxMDk5OTk5OTk5OTk2LDIwOCAyMzcuNzEwOTk5OTk5OTk5OTYsMjE0IDIzMS43MTA5OTk5OTk5OTk5NiwyMTQiIGZpbGw9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNzUuODgwOTk5OTk5OTk5OTciIHk9IjIxOS41IiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1tdXRlZCkiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPkNQVSDri6Tsi5wg7ZWg64u5IOuwm+ydjDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm90ZSIgZGF0YS1wb3NpdGlvbj0ib3ZlciIgZGF0YS1hY3RvcnM9Ik1lbSI+CiAgPHBvbHlnb24gcG9pbnRzPSIxNzMuNTUxNDk5OTk5OTk5OTgsMjYzIDU4NC42NDc0OTk5OTk5OTk5LDI2MyA1OTAuNjQ3NDk5OTk5OTk5OSwyNjkgNTkwLjY0NzQ5OTk5OTk5OTksMjg2IDE3My41NTE0OTk5OTk5OTk5OCwyODYiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHBvbHlnb24gcG9pbnRzPSI1ODQuNjQ3NDk5OTk5OTk5OSwyNjMgNTkwLjY0NzQ5OTk5OTk5OTksMjY5IDU4NC42NDc0OTk5OTk5OTk5LDI2OSIgZmlsbD0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjM4Mi4wOTk0OTk5OTk5OTk5IiB5PSIyNzQuNSIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtbXV0ZWQpIj48dHNwYW4geD0iMzgyLjA5OTQ5OTk5OTk5OTkiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij7sm5DrnpggKzEsIC0x7J2EIO2VmOuptCAxMOydtCDrkJjslrTslbwg7ZWY7KeA66eMPC90c3Bhbj48dHNwYW4geD0iMzgyLjA5OTQ5OTk5OTk5OTkiIGR5PSIxNC4zIj7stZzsooUg6rKw6rO86rCS7J2AIDEx7J20IOuQmOuKlCDrjbDsnbTthLAg7YyM6rS0IOuwnOyDnSE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iYWN0b3IiIGRhdGEtaWQ9IlAxIiBkYXRhLWxhYmVsPSLtlITroZzshLjsiqQgQSAoKzEg7Jew7IKwKSIgZGF0YS10eXBlPSJwYXJ0aWNpcGFudCI+CiAgPHJlY3QgeD0iOTcuNzczNDk5OTk5OTk5OTgiIHk9IjMwIiB3aWR0aD0iMTU2LjIxNDk5OTk5OTk5OTk3IiBoZWlnaHQ9IjQwIiByeD0iNCIgcnk9IjQiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxNzUuODgwOTk5OTk5OTk5OTciIHk9IjUwIiBmb250LXNpemU9IjEzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7tlITroZzshLjsiqQgQSAoKzEg7Jew7IKwKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iYWN0b3IiIGRhdGEtaWQ9Ik1lbSIgZGF0YS1sYWJlbD0i6rO17JygIOuplOuqqOumrCAoQ291bnQgPSAxMCkiIGRhdGEtdHlwZT0icGFydGljaXBhbnQiPgogIDxyZWN0IHg9IjI5My45ODg0OTk5OTk5OTk5MyIgeT0iMzAiIHdpZHRoPSIxNzYuMjIxOTk5OTk5OTk5OTgiIGhlaWdodD0iNDAiIHJ4PSI0IiByeT0iNCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjM4Mi4wOTk0OTk5OTk5OTk5IiB5PSI1MCIgZm9udC1zaXplPSIxMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+6rO17JygIOuplOuqqOumrCAoQ291bnQgPSAxMCk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImFjdG9yIiBkYXRhLWlkPSJQMiIgZGF0YS1sYWJlbD0i7ZSE66Gc7IS47IqkIEIgKC0xIOyXsOyCsCkiIGRhdGEtdHlwZT0icGFydGljaXBhbnQiPgogIDxyZWN0IHg9IjUxMC4yMTA1IiB5PSIzMCIgd2lkdGg9IjE1Mi41MSIgaGVpZ2h0PSI0MCIgcng9IjQiIHJ5PSI0IiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTg2LjQ2NTUiIHk9IjUwIiBmb250LXNpemU9IjEzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7tlITroZzshLjsiqQgQiAoLTEg7Jew7IKwKTwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 운영체제 관점에서의 경쟁 상태 유발 3대 핵심 원인 (출제 포인트)**

단순히 프로그램 짤 때뿐만 아니라, 커널 수준에서 발생하는 구조적 원인을 적어야 합니다.

| **발생 구간**                           | **경쟁 상태 유발 원인 및 상세 설명**                                                                            |
| :---------------------------------- | :------------------------------------------------------------------------------------------------- |
| **1. 커널 모드 진입 시 (Interrupt 발생)**    | 사용자 프로세스가 시스템 콜(System Call)을 호출하여 커널 데이터를 수정하는 도중 **하드웨어 인터럽트가 발생**하여 다른 커널 루틴이 해당 데이터를 덮어쓸 때 발생. |
| **2. 프로세스 간 자원 공유 시**               | IPC 기법 중 \*\*'공유 메모리(Shared Memory)'\*\*를 사용할 때, 상호배제 로직 없이 여러 프로세스가 동일한 변수에 무분별하게 접근할 때 발생.       |
| **3. 멀티 프로세서 (Multi-processor) 환경** | CPU 코어가 2개 이상일 때, **서로 다른 코어에서 실행되는 스레드들**이 공용 캐시나 메모리 구조체에 완벽히 동시에 접근할 때 발생.                      |

#### **IV. \[결론/제언] 경쟁 상태 극복을 위한 임계영역(Critical Section)의 3대 보호 원칙**

* **(키워드 위주 2줄 마무리)** "경쟁 상태를 타파하려면 공유 자원을 다루는 코드 영역을 \*\*'임계 영역(Critical Section)'\*\*으로 지정하고 철저히 보호해야 합니다. 이를 위해 운영체제는 어떠한 경우에도 두 프로세스가 동시에 들어가지 못하는 **상호배제(Mutual Exclusion)**, 문이 열려있으면 즉각 들어가게 해주는 **진행(Progress)**, 그리고 영원히 굶어 죽지 않도록 하는 \*\*한정된 대기(Bounded Waiting)\*\*라는 3대 원칙 하에 **뮤텍스, 세마포어, 모니터**라는 동기화 기법을 강제하고 있습니다."
