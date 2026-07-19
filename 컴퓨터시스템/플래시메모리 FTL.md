FTL은 오늘 다룬 "ROM종류(Flash)"와 "RAID"를 결합한 지점입니다. \*\*"Flash는 SSD로 쓰려면 왜 이렇게 복잡한 소프트웨어계층이 필요한가"\*\*라는 질문 하나로 스토리를 짜겠습니다.

### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (FTL 필요성 - Flash의 근본적 제약) — 3~4줄
Ⅱ. FTL 핵심기능 (본론①, 도식 1개 필수)
Ⅲ. 웨어레벨링과 가비지컬렉션 (본론②, 핵심 배점)
Ⅳ. 성능이슈 - Write Amplification
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 Flash메모리는 EEPROM의 발전형으로 '블록단위로만 지울 수 있고, 지우지 않고는 덮어쓸 수 없다'는 물리적 제약이 있다 — 그런데 OS는 파일을 마치 하드디스크처럼 '아무 위치나 자유롭게 읽고쓰기'할 수 있다고 기대한다 → 이 간극을 메우는 소프트웨어계층이 FTL"\*\*이라는 인과관계로 시작하면, 앞서 다룬 Flash 답안과 자연스럽게 이어집니다.

### Ⅱ. FTL 핵심기능 — "매·웨·가·바" (매핑/웨어레벨링/가비지컬렉션/배드블록관리)

| 기능                              | 내용                                                                                        |
| :------------------------------ | :---------------------------------------------------------------------------------------- |
| **주소매핑** (Address Mapping)      | OS가 요청하는 \*\*논리주소(LBA)\*\*를 실제 \*\*물리 플래시위치(PBA)\*\*로 변환·관리 — 앞서 다룬 "페이징"의 논리↔물리 매핑과 동일원리 |
| **웨어레벨링** (Wear Leveling)       | 특정 블록만 집중적으로 지우고쓰면 **먼저 닳으므로**, 쓰기작업을 **모든 블록에 균등분산**                                     |
| **가비지컬렉션** (Garbage Collection) | 지워야 할 낡은데이터를 **모아서 정리**, 사용가능한 빈 블록을 미리 확보                                                |
| **배드블록관리**                      | 물리적으로 손상된 블록을 **감지·격리**, 대체블록으로 매핑                                                        |

→ 암기: **"어디있는지 알려주고(매핑), 골고루 닳게하고(웨어레벨링), 쓰레기를 치우고(가비지컬렉션), 고장난곳은 피해간다(배드블록)"** — 앞서 다룬 "페이징(주소매핑)"과 "은행가알고리즘(자원관리)"이 결합된 형태가 FTL입니다.

### 도식화 제안

```
[OS] "논리주소 100번을 읽어줘"
   ↓
[FTL] 매핑테이블 조회: 논리100번 → 물리블록37, 페이지5
   ↓
[실제 Flash칩] 물리적 위치에서 데이터 반환

(쓰기 요청시)
[OS] "논리주소 100번에 새 값을 써줘"
   ↓
[FTL] 기존물리위치(37,5)는 지우지 않고,
      새 빈페이지(예: 블록52,페이지2)에 기록 후
      매핑테이블을 갱신(논리100 → 물리52,2)
      기존위치(37,5)는 "무효(invalid)"로 표시 → 나중에 가비지컬렉션 대상
```

→ "덮어쓰기가 안 되니, 새 위치에 쓰고 매핑만 바꿔치기한다"는 게 FTL의 핵심 트릭입니다 — 이걸 \*\*Out-of-place Update(우회쓰기)\*\*라고 합니다.

### Ⅲ. 웨어레벨링과 가비지컬렉션 — 핵심 배점, 서로 맞물린 관계

**함정 방지: 두 기능을 따로 설명하면 절반. "왜 이 둘이 항상 같이 다니는가"를 보여줘야 완성됩니다.**

**웨어레벨링의 필요성**: Flash셀은 **지우기/쓰기 횟수에 한계**(P/E Cycle, 예: TLC는 약 1,000\~3,000회)가 있습니다 — 앞서 다룬 "DRAM vs SRAM vs Flash" 비교에서 Flash의 낮은 내구성 문제가 여기서 실제로 관리대상이 됩니다.

| 방식           | 내용                                                    |
| :----------- | :---------------------------------------------------- |
| **동적 웨어레벨링** | **자주 변경되는(hot) 데이터**의 위치를 계속 옮겨 특정블록 집중을 방지           |
| **정적 웨어레벨링** | **거의 안바뀌는(cold) 데이터**도 가끔 이동시켜, 그 블록도 "닳는 순환"에 포함되게 함 |

**가비지컬렉션과의 연결**: Out-of-place update로 데이터를 옮기고 나면, 기존 위치는 "무효(invalid)"로 남습니다 — 이 무효데이터가 쌓인 블록을 **통째로 지우고(erase) 재사용가능하게** 만드는 게 가비지컬렉션입니다. 그런데 **이 지우기 작업 자체도 웨어레벨링 대상**(어느 블록을 지울지 선택)이므로, 두 기능은 **항상 함께 작동**합니다.

→ 암기: **"웨어레벨링이 '누구를 쓰고 누구를 지울지' 정하고, 가비지컬렉션이 실제로 '지우고 정리'한다"** — 앞서 다룬 "페이지교체알고리즘(누구를 내보낼지 선택)"과 같은 문제의식이 여기서도 반복됩니다.

### Ⅳ. 성능이슈 — Write Amplification (심화, 실무 배점)

**함정 방지: FTL이 다 해결해준다고만 생각하면 절반. FTL 자체가 유발하는 부작용을 알아야 완성됩니다.**

| 개념                             | 내용                                                                                                            |
| :----------------------------- | :------------------------------------------------------------------------------------------------------------ |
| **쓰기증폭** (Write Amplification) | OS가 **1MB를 쓰려고 요청**했는데, 가비지컬렉션 과정에서 **기존데이터 이동·재정리** 때문에 실제 Flash에는 **그보다 훨씬 많은 양(예: 3MB)이 물리적으로 다시 쓰여지는** 현상 |
| **영향**                         | 실제쓰기량 증가 → **셀 마모가속화**(수명단축) + **성능저하**(불필요한 쓰기작업 증가)                                                         |
| **완화기법**                       | **Over-provisioning**(여분공간 확보로 GC여유 확보), **TRIM명령**(OS가 "이 데이터는 이제 안 써도 돼"라고 미리 알려줘서 GC효율화)                   |

→ 암기: **"1을 쓰려고 했는데 뒷정리 때문에 3을 쓰게 되는 것"** — 앞서 다룬 "체크포인팅(인터미턴트컴퓨팅)"에서 상태저장 자체가 오버헤드였던 것과 같은 구조: **정합성을 지키려는 관리작업 자체가 새로운 비용**이 된다는 원리의 재현입니다.

### Ⅴ. 결론 포인트 (오늘 메모리/스토리지 시리즈 최종연결)

FTL은 \*\*"Flash라는 하드웨어의 물리적 제약(블록단위 삭제, 제한된 내구성)을, OS가 기대하는 자유로운 읽기쓰기 인터페이스로 변환해주는 번역계층"\*\*입니다 — 이는 오늘 다룬 페이징(논리↔물리 주소변환), 은행가알고리즘(자원의 안전한 배분), RAID(여러 저장장치를 하나처럼 추상화)에서 반복된 \*\*"하드웨어의 복잡한 제약을 소프트웨어 계층이 흡수해 단순한 인터페이스로 제공한다"\*\*는 설계원리의 스토리지 최전선 사례이며, 그 대가로 쓰기증폭이라는 새로운 오버헤드가 생긴다는 점에서 \*\*"완벽한 추상화는 없고, 어딘가에서 반드시 비용을 지불한다"\*\*는 오늘 하루 다룬 전체 시리즈의 결론을 다시 한번 확인시켜 줍니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "기존 하드디스크(HDD)는 낡은 노트와 같아서 글씨(데이터) 위에 언제든 지우개로 빡빡 지우고 제자리에 바로 '덮어쓰기'를 하면 됐다. 하지만 SSD를 만드는 '낸드 플래시'는 매우 까다롭다. 무조건 도화지를 아예 찢어버린(블록 지우기, Erase) 뒤에만 깨끗한 곳에 새 글씨를 쓸 수 있다(제자리 덮어쓰기 불가). 운영체제(Windows/Linux)는 이 사실을 전혀 모르고 하드디스크를 대하듯 '1번 줄 지우고 거기에 바로 덮어써!'라고 계속 무식하게 명령을 내린다. 이 사이에서 OS를 감쪽같이 속여주는 마법의 통역사 소프트웨어가 바로 SSD 컨트롤러 속의 \*\*'FTL'\*\*이다. OS가 1번 방에 덮어쓰라고 하면, FTL은 1번 방을 지우는 대신 아주 깨끗한 빈 5번 방에 새 데이터를 쓰고 몰래 주소록(매핑 테이블)에서 1번을 5번으로 연결해버린다 **(주소 매핑)**. 그러다 보면 원래 1번 방에 있던 데이터는 쓰레기가 되는데, 이런 쓰레기들을 싹 모아서 유효한 것만 빼내고 블록을 통째로 태워버려 새 공간을 만드는 청소부 역할 \*\*(가비지 컬렉션)\*\*을 한다. 마지막으로, 한 블록만 너무 많이 썼다 지우면 닳아서 SSD가 죽어버리니까, 모든 블록이 골고루 닳도록 평준화해 주는 생명 연장술 \*\*(웨어 레벨링)\*\*까지 도맡아 하는 명실상부한 SSD의 진짜 두뇌다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] SSD의 약점을 가려주는 마법의 통역사, FTL(Flash Translation Layer)**

* **정의:** 운영체제의 파일 시스템과 물리적인 낸드 플래시 메모리 칩 사이에 위치하여, **플래시 메모리의 하드웨어적 한계를 숨기고 마치 하드디스크(HDD)처럼 제자리 덮어쓰기가 되는 것처럼 논리적으로 번역 및 관리해 주는 핵심 소프트웨어(펌웨어) 계층**.
* **플래시 메모리의 3대 치명적 약점 (FTL 탄생의 원인):**
  1. **제자리 덮어쓰기 불가 (Erase-before-write):** 데이터가 있는 셀에 무조건 '지우기(Erase)'를 수행해야만 '쓰기(Program)'가 가능함.
  2. **단위의 불일치:** 읽기와 쓰기는 작은 **'페이지(Page)'** 단위지만, 지우기는 엄청나게 큰 **'블록(Block)'** 단위로만 수행됨 (병목의 원인).
  3. **수명 제한 (Wear-out):** 각 블록은 지우기(P/E Cycle) 횟수가 정해져 있어 많이 쓰면 죽어버림.

#### **II. \[본론 1] FTL의 핵심, 감쪽같은 '주소 매핑(Address Mapping)' 원리 (도식화)**

OS가 덮어쓰기를 명령했을 때 FTL이 빈 공간으로 몰래 바꿔치기하는 과정입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NDUuNjk0IDcxMy4xMzYiIHdpZHRoPSI1NDUuNjk0IiBoZWlnaHQ9IjcxMy4xMzYiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IjFfT1NfIiBkYXRhLWxhYmVsPSIxLiBPUyAo7Jq07JiB7LK07KCcKSI+CiAgPHJlY3QgeD0iMTA0LjA2NTUwMDAwMDAwMDAxIiB5PSI0MCIgd2lkdGg9IjI0NS4xMjA5OTk5OTk5OTk5NSIgaGVpZ2h0PSIxMTMuODAwMDAwMDAwMDAwMDEiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSIxMDQuMDY1NTAwMDAwMDAwMDEiIHk9IjQwIiB3aWR0aD0iMjQ1LjEyMDk5OTk5OTk5OTk1IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxMTYuMDY1NTAwMDAwMDAwMDEiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjEuIE9TICjsmrTsmIHssrTsoJwpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMl9fRlRMX0ZsYXNoX1RyYW5zbGF0aW9uX0xheWVyIiBkYXRhLWxhYmVsPSIyLiDwn6egIEZUTCAoRmxhc2ggVHJhbnNsYXRpb24gTGF5ZXIpIj4KICA8cmVjdCB4PSIxMjMuNTU4IiB5PSIyMTMuOCIgd2lkdGg9IjM4Mi4xMzU5OTk5OTk5OTk5NyIgaGVpZ2h0PSIyMzQuMTM2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iMTIzLjU1OCIgeT0iMjEzLjgiIHdpZHRoPSIzODIuMTM1OTk5OTk5OTk5OTciIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjEzNS41NTgiIHk9IjIyNy44IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjIuIPCfp6AgRlRMIChGbGFzaCBUcmFuc2xhdGlvbiBMYXllcik8L3RleHQ+CjwvZz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSIzX19fX05BTkQiIGRhdGEtbGFiZWw9IjMuIOusvOumrOyggSDtlIzrnpjsi5wg66mU66qo66asIChOQU5EKSI+CiAgPHJlY3QgeD0iNDAiIHk9IjU3Ni4yMzYiIHdpZHRoPSIyNzYuNjI2IiBoZWlnaHQ9Ijk2LjkiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNTc2LjIzNiIgd2lkdGg9IjI3Ni42MjYiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1OTAuMjM2IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjMuIOusvOumrOyggSDtlIzrnpjsi5wg66mU66qo66asIChOQU5EKTwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTyIgZGF0YS10bz0iTSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyMjYuNjI1OTk5OTk5OTk5OTgsMTM3LjggMjI2LjYyNiwyNTcuODAwMDAwMDAwMDAwMDciIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209Ik0iIGRhdGEtdG89IlAxIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i6riw7KG0IOyXsOqysCDrgYrsnYwiIHBvaW50cz0iMTk3LjYwMzMzMzMzMzMzMzMyLDQwMi45MTMzMzMzMzMzMzMzNiAxOTcuNjAzMzMzMzMzMzMzMyw0ODkuOTM2MDAwMDAwMDAwMDQgMTY1LjYyODk5OTk5OTk5OTk2LDQ4OS45MzYwMDAwMDAwMDAwNCAxNjUuNjI4OTk5OTk5OTk5OTYsNTU4LjIzNjAwMDAwMDAwMDEgMTgyLjYyNTk5OTk5OTk5OTk4LDU1OC4yMzYwMDAwMDAwMDAxIDE4Mi42MjU5OTk5OTk5OTk5OCw2MjAuMjM2MDAwMDAwMDAwMSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJNIiBkYXRhLXRvPSJQMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i66qw656YIOu5iCDqs7PsnLzroZwg7Jew6rKwIOyImOyglSIgcG9pbnRzPSIyNTUuNjQ4NjY2NjY2NjY2NjYsNDAyLjkxMzMzMzMzMzMzMzM2IDI1NS42NDg2NjY2NjY2NjY2Niw0ODkuOTM2MDAwMDAwMDAwMDQgMjg3LjYyMyw0ODkuOTM2MDAwMDAwMDAwMDQgMjg3LjYyMyw1NTguMjM2MDAwMDAwMDAwMSAyNzAuNjI2LDU1OC4yMzYwMDAwMDAwMDAxIDI3MC42MjYsNjIwLjIzNjAwMDAwMDAwMDEiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iTSIgZGF0YS10bz0iUDEiIGRhdGEtbGFiZWw9Iuq4sOyhtCDsl7DqsrAg64GK7J2MIj4KICA8cmVjdCB4PSIxMTkuMTI4OTk5OTk5OTk5OTYiIHk9IjQ5Ni45MzYwMDAwMDAwMDAwNCIgd2lkdGg9IjkyLjQ5NDAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTY1LjM3NTk5OTk5OTk5OTk4IiB5PSI1MTIuMDg2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7quLDsobQg7Jew6rKwIOuBiuydjDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJNIiBkYXRhLXRvPSJQMiIgZGF0YS1sYWJlbD0i66qw656YIOu5iCDqs7PsnLzroZwg7Jew6rKwIOyImOyglSI+CiAgPHJlY3QgeD0iMjE1LjYyMyIgeT0iNDk2LjkzNjAwMDAwMDAwMDA0IiB3aWR0aD0iMTQzLjU3OCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjI4Ny40MTIiIHk9IjUxMi4wODYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuuqsOuemCDruYgg6rOz7Jy866GcIOyXsOqysCDsiJjsoJU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik8iIGRhdGEtbGFiZWw9Ik9TIOuqheuguTog64W866asIOyjvOyGjCAnTEJBIDEn7JeQCuuNsOydtO2EsCAnQifroZwg642u7Ja07I2o6528ISIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMjAuMDY1NTAwMDAwMDAwMDEiIHk9Ijg0IiB3aWR0aD0iMjEzLjEyMDk5OTk5OTk5OTk1IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyMjYuNjI1OTk5OTk5OTk5OTgiIHk9IjExMC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIyMjYuNjI1OTk5OTk5OTk5OTgiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5PUyDrqoXroLk6IOuFvOumrCDso7zshowgJiMzOTtMQkEgMSYjMzk77JeQPC90c3Bhbj48dHNwYW4geD0iMjI2LjYyNTk5OTk5OTk5OTk4IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7rjbDsnbTthLAgJiMzOTtCJiMzOTvroZwg642u7Ja07I2o6528ITwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJNIiBkYXRhLWxhYmVsPSLrp6TtlZEg7YWM7J2067iUIOuyiOyXrQpNYXBwaW5nIFRhYmxlIiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjIyNi42MjU5OTk5OTk5OTk5OCwyNTcuOCAzMTMuNjkzOTk5OTk5OTk5OTYsMzQ0Ljg2OCAyMjYuNjI1OTk5OTk5OTk5OTgsNDMxLjkzNiAxMzkuNTU4LDM0NC44NjgiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMjI2LjYyNTk5OTk5OTk5OTk4IiB5PSIzNDQuODY4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIyMjYuNjI1OTk5OTk5OTk5OTgiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7rp6TtlZEg7YWM7J2067iUIOuyiOyXrTwvdHNwYW4+PHRzcGFuIHg9IjIyNi42MjU5OTk5OTk5OTk5OCIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+TWFwcGluZyBUYWJsZTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQMSIgZGF0YS1sYWJlbD0iUDEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzQxLjY5Mzk5OTk5OTk5OTk2IiB5PSIzMjYuNDE4IiB3aWR0aD0iNjAiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjM3MS42OTM5OTk5OTk5OTk5NiIgeT0iMzQ0Ljg2OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+UDE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlAyIiBkYXRhLWxhYmVsPSJQMiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MjkuNjkzOTk5OTk5OTk5OTYiIHk9IjMyNi40MTgiIHdpZHRoPSI2MCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDU5LjY5Mzk5OTk5OTk5OTk2IiB5PSIzNDQuODY4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5QMjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUDEiIGRhdGEtbGFiZWw9IlAxIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjE1Mi42MjYiIHk9IjYyMC4yMzYiIHdpZHRoPSI2MCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTgyLjYyNiIgeT0iNjM4LjY4NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+UDE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlAyIiBkYXRhLWxhYmVsPSJQMiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyNDAuNjI2IiB5PSI2MjAuMjM2IiB3aWR0aD0iNjAiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI3MC42MjYiIHk9IjYzOC42ODYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlAyPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJOb3RlIiBkYXRhLWxhYmVsPSJOb3RlIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI2MjAuMjM2IiB3aWR0aD0iNjguNjI2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iOTAuMzEzIiB5PSI2MzguNjg2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5Ob3RlPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] FTL을 완성하는 3대 핵심 모듈 아키텍처 전격 해부표 (출제 1순위)**

| **FTL 핵심 모듈**                       | **주요 역할 및 상세 알고리즘**                                                                             | **한계 및 특징**                                                          |
| :---------------------------------- | :---------------------------------------------------------------------------------------------- | :------------------------------------------------------------------- |
| **1. 주소 매핑** (Address Mapping)      | 파일 시스템의 논리 블록 주소(LBA)를 플래시 메모리의 물리 블록 주소(PBA)로 연결표를 갱신함.                                        | 성능과 램(RAM) 용량 타협을 위해 **Page 매핑, Block 매핑, Hybrid 매핑** 기법 사용.         |
| **2. 가비지 컬렉션** (Garbage Collection) | 매핑 과정에서 덮어써지며 버려진 찌꺼기 '무효(Invalid) 페이지'가 가득 찬 블록을 청소. 유효 데이터만 딴 데로 복사하고 블록을 통째로 지움(Erase).      | 청소하는 동안 SSD의 응답 속도가 현저히 느려지는 **'성능 저하의 주범'**.                        |
| **3. 웨어 레벨링** (Wear Leveling)       | 특정 블록만 자주 지워져서 수명이 일찍 닳아버리지 않도록, 저장된 데이터들을 여기저기 옮겨가며 \*\*모든 블록의 수명을 골고루 평준화(Leveling)\*\*하는 마법. | 자주 바뀌는 데이터는 **동적(Dynamic)**, 얌전한 OS 데이터는 **정적(Static)** 웨어 레벨링으로 통제. |

#### **IV. \[결론/제언] 가비지 컬렉션의 딜레마 극복: TRIM 명령어와 오버 프로비저닝(OP)**

* **(키워드 위주 2줄 마무리)** "FTL이 아무리 뛰어나도 SSD를 꽉 채워 쓰면 가비지 컬렉션(청소)을 하느라 쓰기 성능이 급격히 추락합니다(Write Amplification). 이를 극복하기 위해, OS가 파일 삭제 시 SSD에게 '여기 청소해 둬!'라고 미리 알려주는 **'TRIM 명령어'를 활성화**하고, SSD 제조 시 10~20%의 여유 공간을 몰래 숨겨두어 청소 공간으로 쓰는 **'오버 프로비저닝(Over-Provisioning)' 기술을 설계에 융합하는 것이 현대 SSD 아키텍처의 필수 생존 전략**입니다."
