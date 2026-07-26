### **Mamba & 상태 공간 모델 (SSM: State Space Model)**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 Attention의 O(n²)이 긴 시퀀스의 한계가 되는가)
Ⅱ. SSM 핵심 원리
Ⅲ. Mamba 핵심 혁신 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 VLM 커넥터·PagedAttention이 'Transformer 아키텍처의 효율성을 주변부에서 개선'하는 접근이라면, Mamba는 'Transformer의 핵심인 Self-Attention 자체를 상태 공간 모델(SSM)로 대체'하는 근본적 아키텍처 전환이다 — Transformer의 Attention 연산은 모든 토큰 쌍의 관계를 계산하므로 시퀀스 길이(n)에 대해 O(n²)의 연산량과 메모리가 필요해 긴 문서·유전체 서열·오디오처럼 초장문 시퀀스에서 급격히 비효율적이 되는데, 2023년 카네기멜론·프린스턴 연구팀이 제안한 Mamba는 제어이론의 오래된 도구인 상태 공간 모델을 딥러닝에 이식하고 '선택적 메커니즘(Selective SSM)'이라는 핵심 혁신을 더해 O(n)의 선형 연산량으로 Transformer급 성능을 달성하며 앞서 다룬 KV 캐싱이 필요 없는 고정 크기 상태(State)만으로 무한에 가까운 문맥을 처리할 잠재력을 보여준 것"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.
![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MDQuMzA1OTk5OTk5OTk5OSAzNzEuNiIgd2lkdGg9IjUwNC4zMDU5OTk5OTk5OTk5IiBoZWlnaHQ9IjM3MS42IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IklucHV0IiBkYXRhLXRvPSJTZWxlY3QiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjUyLjE1Mjk5OTk5OTk5OTk2LDc2LjkgMjUyLjE1Mjk5OTk5OTk5OTk2LDEyNC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTZWxlY3QiIGRhdGEtdG89IlNjYW4iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjUyLjE1Mjk5OTk5OTk5OTk2LDE2MS44IDI1Mi4xNTI5OTk5OTk5OTk5NiwyMDkuOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iU2NhbiIgZGF0YS10bz0iT3V0cHV0IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjI1Mi4xNTI5OTk5OTk5OTk5NiwyNDYuNzAwMDAwMDAwMDAwMDIgMjUyLjE1Mjk5OTk5OTk5OTk2LDI5NC43MDAwMDAwMDAwMDAwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iSW5wdXQiIGRhdGEtbGFiZWw9IuyeheugpSDsi5ztgIDsiqQgWCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxODcuNDU4OTk5OTk5OTk5OTUiIHk9IjQwIiB3aWR0aD0iMTI5LjM4OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI1Mi4xNTI5OTk5OTk5OTk5NiIgeT0iNTguNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyeheugpSDsi5ztgIDsiqQgWDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU2VsZWN0IiBkYXRhLWxhYmVsPSIxLiDshKDtg53soIEg66mU7Luk64uI7KaYIDog7J6F66ClIOqwgOuzgCDtjIzrnbzrr7jthLAgQiwgQywgRGVsdGEg6rOE7IKwIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjYyLjk3MSIgeT0iMTI0LjkiIHdpZHRoPSIzNzguMzYzOTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjUyLjE1Mjk5OTk5OTk5OTk2IiB5PSIxNDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjEuIOyEoO2DneyggSDrqZTsu6Tri4jsppggOiDsnoXroKUg6rCA67OAIO2MjOudvOuvuO2EsCBCLCBDLCBEZWx0YSDqs4TsgrA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlNjYW4iIGRhdGEtbGFiZWw9IjIuIEhhcmR3YXJlLUF3YXJlIFBhcmFsbGVsIFNjYW4gOiBHUFUgU1JBTSDrgrQg6rOg7IaNIOuzkeugrCDsiqTsupQiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDAiIHk9IjIwOS44IiB3aWR0aD0iNDI0LjMwNTk5OTk5OTk5OTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMjUyLjE1Mjk5OTk5OTk5OTk2IiB5PSIyMjguMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjIuIEhhcmR3YXJlLUF3YXJlIFBhcmFsbGVsIFNjYW4gOiBHUFUgU1JBTSDrgrQg6rOg7IaNIOuzkeugrCDsiqTsupQ8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik91dHB1dCIgZGF0YS1sYWJlbD0iMy4g7Lac66ClIFkgOiDshKDtmJUg67O17J6h64+EIE8gTiDrsI8gS1Yg7LqQ7IucIOuplOuqqOumrCDshozrqqgg7KCc66GcIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjYxLjg1OTUiIHk9IjI5NC43MDAwMDAwMDAwMDAwNSIgd2lkdGg9IjM4MC41ODY5OTk5OTk5OTk5MyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI1Mi4xNTI5OTk5OTk5OTk5NiIgeT0iMzEzLjE1MDAwMDAwMDAwMDAzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij4zLiDstpzroKUgWSA6IOyEoO2YlSDrs7XsnqHrj4QgTyBOIOuwjyBLViDsupDsi5wg66mU66qo66asIOyGjOuqqCDsoJzroZw8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

***

#### Ⅱ. SSM 핵심 원리

**가. 상태 공간 모델의 수학적 기원**

```
[제어이론의 연속 시간 SSM]

원래 제어이론(1960년대, 칼만 필터 계열)의 방정식:
  h'(t) = A·h(t) + B·x(t)   ← 상태 갱신
  y(t)  = C·h(t)            ← 출력

  h(t): 은닉 상태(시스템 내부 상태)
  x(t): 입력 신호
  y(t): 출력 신호
  A,B,C: 학습 가능한 파라미터 행렬

핵심 직관:
  현재 상태(h)만 알면 과거 전체를 다시 볼 필요 없이
  다음 상태를 순차적으로 계산 가능
  → RNN과 유사한 순차 처리 구조
```

**나. 이산화(Discretization) 및 병렬 학습**

| 개념                      | 원리                                                               |
| :---------------------- | :--------------------------------------------------------------- |
| **이산화(Discretization)** | 연속 시간 방정식을 이산 토큰 시퀀스에 적용하기 위해 샘플링 간격(Δ)으로 변환                     |
| **합성곱(Convolution) 표현** | 학습 시 SSM을 하나의 거대한 합성곱 커널로 전개해 **GPU 병렬 학습** 가능(RNN의 순차 학습 한계 극복) |
| **순환(Recurrence) 표현**   | 추론 시에는 RNN처럼 상태 하나만 유지하며 토큰마다 O(1)로 순차 처리                        |
| **이중 표현의 이점**           | 학습은 병렬(합성곱)로 빠르게, 추론은 순차(순환)로 메모리 효율적으로 수행하는 두 얼굴 구조             |

***

#### Ⅲ. Mamba 핵심 혁신 및 적용 체계

**가. 기존 SSM(S4)의 한계와 Mamba의 해법**

```
[S4(기존 SSM)의 한계]

A, B, C 파라미터가 입력(x)과 무관하게 고정
  → 모든 토큰을 동일한 방식으로 처리(Time-Invariant)
  → 문맥에 따라 "이 정보는 중요하니 기억, 저건 무시"
    같은 선택적 판단 불가 🚨
  → Attention의 핵심 강점(선택적 집중)을 재현 못함

[Mamba의 해법: Selective SSM]

A, B, C를 입력(x)의 함수로 만듦
  B(x), C(x), Δ(x) ← 입력에 따라 동적으로 변화

효과:
  토큰마다 "이 정보를 상태에 반영할지 말지"를
  입력 내용에 따라 선택적으로 결정 ✅
  → 관련 없는 정보는 걸러내고 핵심만 압축 저장
  → Attention 없이도 선택적 정보 처리 재현
```

**나. Mamba 핵심 아키텍처 요소**

| 요소                                | 내용                                                                                                    |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------- |
| **선택적 메커니즘(Selective Mechanism)** | 입력 의존적 파라미터화로 토큰별 정보 취사선택                                                                             |
| **하드웨어 인식 알고리즘**                  | Selective SSM이 병렬 합성곱 트릭을 못 쓰게 되자, GPU 메모리 계층(SRAM/HBM) 특성을 고려한 커스텀 병렬 스캔(Parallel Scan) 알고리즘으로 속도 확보 |
| **고정 크기 은닉 상태**                   | 시퀀스 길이와 무관하게 상태 크기 일정 → 앞서 다룬 **KV 캐시**처럼 시퀀스 길이에 비례해 커지는 메모리 문제 원천 회피                                |
| **Mamba 블록**                      | SSM + 게이팅 + 짧은 합성곱을 하나의 블록으로 결합, Transformer 블록을 대체                                                   |

**다. Transformer vs SSM(S4) vs Mamba 비교**

| 비교 항목          | Transformer            | S4(기존 SSM)            | Mamba                 |
| :------------- | :--------------------- | :-------------------- | :-------------------- |
| **연산 복잡도(학습)** | O(n²) 🚨               | O(n log n)            | **O(n)** ✅            |
| **추론 메모리**     | 시퀀스 길이 비례 증가(KV 캐시) 🚨 | 고정 크기 ✅               | **고정 크기** ✅           |
| **선택적 정보 처리**  | Attention으로 우수 ✅       | 불가(Time-Invariant) 🚨 | **가능(Selective)** ✅   |
| **병렬 학습**      | 완전 병렬 가능 ✅             | 합성곱으로 병렬 가능           | 커스텀 병렬 스캔으로 가능        |
| **초장문 처리**     | 비효율적(메모리 폭증) 🚨        | 효율적                   | **효율적** ✅             |
| **성능(언어 모델링)** | 최고 수준                  | Transformer 대비 열위 🚨  | **Transformer급 달성** ✅ |

**라. 적용 및 하이브리드 아키텍처 동향**

| 적용 분야                 | 내용                                                              |
| :-------------------- | :-------------------------------------------------------------- |
| **초장문 언어 모델**         | 수십만 토큰 문맥을 고정 메모리로 처리하는 차세대 LLM 연구                              |
| **유전체·생물학적 서열**       | DNA·단백질 서열처럼 매우 긴 시퀀스 분석에 적합                                    |
| **오디오·시계열 처리**        | 원시 오디오 파형 등 초장문 신호 데이터                                          |
| **하이브리드 모델(Jamba 등)** | Mamba 레이어와 Attention 레이어를 섞어 각각의 강점(효율성+정밀한 검색)을 결합하는 방향으로 발전 중 |

***

**(제언)** "Mamba의 진정한 기여는 단순히 빠른 아키텍처를 만든 것이 아니라, 제어이론이라는 반세기 전 다른 학문 분야의 수학적 도구를 딥러닝에 재도입하면서 '선택성(Selectivity)'이라는 한 가지 핵심 아이디어만 추가해 RNN 계열이 오랫동안 도달하지 못했던 Transformer급 성능을 O(n)으로 달성했다는 이론적 의의에 있습니다. 다만 현재 Mamba가 모든 Attention을 완전히 대체했다고 보기는 이르며, 텍스트 내 정확한 사실 검색(Needle-in-a-Haystack)처럼 특정 토큰을 정밀하게 되짚어야 하는 과제에서는 여전히 순수 Attention이 강점을 보이므로, 실무 관점에서는 Jamba처럼 Mamba 레이어(효율적 문맥 압축)와 Attention 레이어(정밀 검색)를 하이브리드로 결합하는 아키텍처가 당분간 가장 현실적인 선택지이며, 초장문 문서 요약이나 유전체 분석처럼 시퀀스 길이가 극단적으로 긴 도메인부터 우선 도입을 검토하는 것이 합리적입니다.

***

**앞서 다룬 개념과의 연결**

| 연계 개념                    | 연결 내용                                          |
| :----------------------- | :--------------------------------------------- |
| **PagedAttention·KV 캐싱** | Mamba의 고정 크기 상태가 KV 캐시 메모리 문제를 아키텍처 수준에서 원천 회피 |
| **VLM 커넥터**              | Mamba 기반 비전-언어 모델(VL-Mamba 등) 연구로 커넥터 구조에도 영향  |
| **QLoRA**                | Mamba 계열 모델의 경량 파인튜닝에도 저랭크 어댑터 기법 적용 가능        |
| **AI 반도체·이기종 컴퓨팅**       | 병렬 스캔 알고리즘이 GPU 메모리 계층 특성에 최적화된 하드웨어 인식 설계     |
| **온디바이스 NPU**            | 고정 메모리 상태 특성이 메모리 제약이 큰 엣지 디바이스 배포에 유리         |

#### **I. 포스트 트랜스포머 아키텍처의 혁신, Mamba 및 SSM의 개요**

트랜스포머 아키텍처는 시퀀스 길이(N*N*)가 길어질수록 계산량과 메모리가 제곱(O(N2)*O*(*N*2))으로 증가하고 추론 시 KV 캐시 보존으로 인해 고비용이 유발됩니다. 전통적인 상태 공간 모델(SSM)은 연속적인 신호 제어 이론을 이산화하여 선형 시간(O(N)*O*(*N*))으로 처리하지만 입력 데이터에 따라 문맥을 선택적으로 수용하지 못하는 한계(시불변성)가 있었습니다. **Mamba**는 파라미터를 입력값에 연동시키는 \*\*선택적 매커니즘(Selective SSM)\*\*과 **하드웨어 최적화 병렬 스캔(Parallel Scan)** 알고리즘을 결합하여, 트랜스포머 수준의 표현력과 선형 시간 추론 속도를 동시에 달성한 모델입니다.

```
```

***

### **II. Mamba(Selective SSM)의 2대 핵심 기술 혁신**

#### **1. 선택적 메커니즘 (Selective Mechanism)**

* **데이터 가변 파라미터화**: 기존 SSM의 시불변 행렬(B,C,Δ*B*,*C*,Δ)을 입력값 xt*xt*​의 함수로 동적 변화시킵니다.
* **선택적 기억과 망각**: 입력 텍스트의 중요도에 따라 상태 공간(State)에 특정 정보를 선택적으로 기억하거나 불필요한 노이즈를 무시(Forget)하여, 트랜스포머의 어텐션과 동등한 문맥 맥락 파악 능력을 확보합니다.

#### **2. 하드웨어 인지 알고리즘 (Hardware-Aware Parallel Scan)**

* **커널 융합 (Kernel Fusion)**: 선택적 메커니즘 적용 시 전통적 순차 연산(RNN 방식)으로 인한 전송 병목을 막기 위해, GPU의 느린 HBM 메모리 대신 고속 **SRAM 내부에서 연산을 하나로 융합**하여 처리합니다.
* **병렬 스캔 (Parallel Scan)**: 접두사 합(Prefix Sum) 방식의 하드웨어 병렬 스캔을 가동하여, RNN 형태의 순차 전이 구조임에도 \*\*GPU 병렬 학습 속도(O(N)*O*(*N*))\*\*를 완벽 구현합니다.

***

### **III. 기존 트랜스포머(Transformer)와 차세대 맘바(Mamba - Selective SSM)의 상세 비교**

| **비교 항목**             | **🤖 트랜스포머 (Transformer)**                   | **🐍 맘바 (Mamba - Selective SSM)**   |
| :-------------------- | :------------------------------------------- | :---------------------------------- |
| **시간/메모리 복잡도**        | 시퀀스 길이(N*N*)에 대해 **제곱 복잡도 (O(N2)*O*(*N*2))** | **선형 복잡도 (O(N)*O*(*N*))**           |
| **추론 방식 및 KV 캐시**     | KV 캐시 메모리 소모 극심 (Long Context 시 OOM)         | **상태 공간(State) 전이 기반 추론 (KV 캐시 0)** |
| **컨텍스트 필터링**          | 셀프 어텐션 기반 전체 토큰 행렬 비교                        | **선택적 메커니즘 기반 중요 정보 동적 필터링**        |
| **초장문(Long-Context)** | 32K\~128K 이상 확장 시 연산 인프라 기하급수 폭증             | **100만(1M) 토큰 이상의 초장문도 선형 연산 처리**   |

***

### **IV. Mamba 아키텍처의 한계 및 하이브리드 발전 방향**

**IMPORTANT**

1. **인-컨텍스트 프롬프팅 복사 한계 보완**: Mamba는 장문 연산에 강하지만, 본문 내의 구체적 텍스트를 그대로 복사해서 출력하는 솜씨(In-Context Retrieval / Needle in a Haystack)는 트랜스포머보다 다소 미흡할 수 있습니다.
2. **트랜스포머-맘바 하이브리드(Hybrid) 아키텍처**: 이를 보완하기 위해 Mamba 레이어 중간중간에 어텐션 레이어를 소량 섞어 배치하는 \*\*하이브리드 아키텍처(예: Jamba 모델)\*\*로 진화하고 있으며, 추론 메모리는 획기적으로 줄이면서 복사 정확도를 보존하는 방향으로 확산 중입니다.**성과 정확도를 모두 잡아야 합니다.**"
