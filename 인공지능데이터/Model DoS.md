### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (정의, 앞서다룬DDoS와의차이) — 3~4줄
Ⅱ. 공격유형3종 (본론①, 도식 1개 필수)
Ⅲ. 왜LLM이특히취약한가및방어기법, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

앞서다룬 **DDoS**는 \*\*"네트워크대역폭이나서버연결자원"\*\*을 고갈시켰는데, ModelDoS(모델서비스거부공격)는 \*\*"AI모델의추론(연산)자원자체"\*\*를 고갈시킵니다 — 트래픽양이아니라, \*\*"모델이한번의요청을처리하는데드는연산비용"\*\*을 악용하는 것이 핵심입니다.

### Ⅱ. 공격유형 3종

| 유형                         | 내용                                                                  |
| :------------------------- | :------------------------------------------------------------------ |
| **긴프롬프트공격**(SpongeExample) | 모델이 **비정상적으로긴시간·많은연산**을소모하도록 **특수하게설계된입력**전송                        |
| **반복추론유도**(무한루프)           | 앞서다룬 \*\*"Chain-of-Thought"\*\*를 **악의적으로유도**해, 모델이 **끝없이추론을반복**하게만듦 |
| **대량동시요청**(전통DDoS의AI버전)    | 앞서다룬 **DDoS**처럼 **단순히요청을대량으로쏟아부어**, GPU/추론서버자체를 과부하                 |

→ 암기: **"입력자체를무겁게만들거나,계속반복추론하게하거나,그냥양으로밀어붙인다"** — 앞서다룬 \*\*"CAPTCHA의PoW(작업증명)"\*\*가 \*\*"연산부담을줘서공격을어렵게"\*\*했던것과 정반대로, ModelDoS는 \*\*"연산부담자체를무기화"\*\*합니다.

### 도식화 제안

```
[Model DoS 3유형]
①SpongeExample: "일부러복잡한입력" → 모델이 처리에 평소보다 100배시간소모
②반복추론유도: "계속더생각해봐,다시확인해봐" → CoT가 끝없이반복
③대량요청: 짧은시간에 수천건 동시요청 → GPU/추론서버 과부하

→ 공통점: "요청1건당연산비용"을 악용해 서버전체를마비
```

### Ⅲ. 왜LLM이특히취약한가 및 방어기법 — 핵심 배점

**함정 방지: "그냥DDoS의AI버전"이라고만답하면절반. LLM만의구조적취약점(토큰당비용,자기회귀생성)과, 앞서다룬MoE/양자화가어떻게방어에연결되는지보여줘야완성됩니다.**

| 취약점                | 내용                                                                                                    |
| :----------------- | :---------------------------------------------------------------------------------------------------- |
| **자기회귀생성구조**(핵심원인) | 앞서다룬 **Self-Attention**기반LLM은 **토큰을하나씩순차생성**— **출력이길어질수록**,이전토큰을 **모두다시참조**해야해 **연산량이제곱에가깝게증가**       |
| **비용비대칭성**         | 공격자는 **몇줄의악성프롬프트**만보내면되지만, 서버는 **막대한GPU연산**을 소모— 앞서다룬 \*\*"DDoS의공격자:방어자비용비율1:3000"\*\*과 유사한 **비대칭구조** |
| **에이전틱AI에서증폭**(최신) | 앞서다룬 \*\*"MAS(멀티에이전트시스템)"\*\*에서, 한에이전트가 공격받으면 **연쇄적으로다른에이전트도자원소모**                                    |

**방어기법**

| 기법                            | 내용                                                                                     |
| :---------------------------- | :------------------------------------------------------------------------------------- |
| **최대토큰수제한**                   | 입력·출력 **길이상한선**설정                                                                      |
| **타임아웃설정**                    | 일정시간초과시 **강제종료**                                                                       |
| **요청단위과금·속도제한**(RateLimiting) | 앞서다룬 \*\*"WFQ(가중치기반스케줄링)"\*\*처럼, 사용자별 **공정한자원배분**                                      |
| **MoE의부분적방어효과**               | 앞서다룬 \*\*MoE(조건부연산)\*\*는 \*\*"필요한전문가만활성화"\*\*해, 악의적입력이라도 **연산량이무한정폭증하지는않도록** 구조적으로일부완화 |

→ 암기: **"입력·출력길이를제한하고,시간초과하면끊고,사용자별로공정하게나누고, MoE같은구조자체가일부는막아준다"**

### 도식화 제안

```
[Model DoS 방어체계]
①최대토큰수제한 (입력/출력 상한선)
②타임아웃 (일정시간초과시 강제종료)
③속도제한(Rate Limiting) - 앞서다룬WFQ의공정배분원리
④MoE구조 - 조건부연산으로 폭증을일부완화

[비용비대칭성 문제]
공격자: 짧은악성프롬프트 몇줄만보내면됨
서버: 막대한GPU연산 소모(앞서다룬DDoS의1:3000비대칭과유사)
```

### Ⅳ. 결론

ModelDoS는 **"앞서다룬DDoS가네트워크자원을노렸다면, LLM의자기회귀생성구조(토큰당연산비용)와Chain-of-Thought반복추론을악용해 AI모델의연산자원자체를고갈시키는"** 새로운공격입니다 — 핵심취약점은 **"공격자의비용은매우낮은데, 서버의연산비용은막대한"** 비대칭성이며, 이는 앞서다룬 \*\*"DDoS의1:3000비용비대칭"\*\*과 동일한구조적문제입니다 — 방어는 **토큰수제한,타임아웃,속도제한**같은 전통적기법에더해, **MoE의조건부연산구조**가 일부완화효과를 제공합니다 — 이는 앞서다룬 **DDoS→모델전도공격→ModelDoS**로 이어지는 흐름에서, \*\*"AI시대에는전통적인공격기법(DDoS)이, AI고유의구조(자기회귀생성,MoE)를만나 새로운형태로재탄생한다"\*\*는 것을 보여주는 완결된사례입니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "챗GPT 같은 대형 AI 모델의 뇌(GPU와 VRAM 자원)에 과부하를 걸어 칩을 마비시키는 \*\*'AI 전용 서비스 거부(DoS) 공격'\*\*이자, OWASP LLM 10대 보안 위협(L07)이다. 네트워크 DoS가 단순 무식하게 쓰레기 패킷을 쏟아붓는다면, Model DoS는 연산량이 기하급수적으로 폭발하는 '악성 질문'을 던진다. 해커는 "원주율(Pi) 소수점 100만 자리까지 읊어줘"라고 지시하거나, 수만 줄짜리 텍스트를 프롬프트에 넣고 요약을 요구한다. LLM의 어텐션(Attention) 연산은 글자 수의 제곱(O(N2)*O*(*N*2)) 비례로 계산량이 늘어나므로, 단 몇 개의 쿼리만으로 서버 GPU 성능을 100% 점유해 서비스 먹통을 유발할 수 있다. 이를 막기 위해 프롬프트의 '최대 입력 길이'와 '답변 출력 토큰 수'를 강제로 칼질해 제한하고, IP/계정당 분당 토큰량(TPM)에 브레이크를 거는 **'자원 할당 통제 체계'** 구축이 필수적이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] GPU 자원의 비대칭성을 노리는 자원 고갈 위협, Model DoS 개요**

* **정의:** 사용자가 입력한 짧은 입력값 대비 모델이 생성해야 하는 연산(토큰 생성 및 Attention 연산)량이 비정상적으로 큰 취약점을 악용하여, AI 서버의 자원(GPU, VRAM)을 고갈시키고 정상 서비스를 중단시키는 공격 기법.
* **배경:** LLM 서비스는 인퍼런스(추론) 단계에서 대규모 행렬 곱 연산이 수반되어 컴퓨팅 비용이 매우 높고, 컨텍스트 윈도우가 커질수록 필요한 메모리가 폭증하는 구조적 특성이 존재하기 때문.

#### **II. \[본론 1] (극단적 단순화 버전) 적은 인풋으로 상대 GPU를 터뜨리는 비대칭 부하**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4NTcuMjg1IDE5My44IiB3aWR0aD0iODU3LjI4NSIgaGVpZ2h0PSIxOTMuOCIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iTW9kZWxfRG9TX19fXyIgZGF0YS1sYWJlbD0iTW9kZWwgRG9TIOqzteqyqSDrqZTsu6Tri4jsppjqs7wg7J6Q7JuQIOqzoOqwiCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNzc3LjI4NSIgaGVpZ2h0PSIxMTMuODAwMDAwMDAwMDAwMDEiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI3NzcuMjg1IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+TW9kZWwgRG9TIOqzteqyqSDrqZTsu6Tri4jsppjqs7wg7J6Q7JuQIOqzoOqwiDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iSU5QVVQiIGRhdGEtdG89IkFUVCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyNzQuMzA4LDExMC45IDMyMi4zMDgsMTEwLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkFUVCIgZGF0YS10bz0iR1BVIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjM5MC45MzM5OTk5OTk5OTk5NywxMTAuOSA0MzguOTMzOTk5OTk5OTk5OTcsMTEwLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkdQVSIgZGF0YS10bz0iRkFJTCIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNTA3LjU1OTk5OTk5OTk5OTk1LDExMC45IDU1NS41NiwxMTAuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJJTlBVVCIgZGF0YS1sYWJlbD0i7ZW07LukIOyduO2Siwon7JuQ7KO87JyoIDEwMOunjOyekOumrCDstpzroKXtlbTrnbwnIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjIxOC4zMDgiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE2NS4xNTQiIHk9IjExMC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNjUuMTU0IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7ZW07LukIOyduO2SizwvdHNwYW4+PHRzcGFuIHg9IjE2NS4xNTQiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPiYjMzk77JuQ7KO87JyoIDEwMOunjOyekOumrCDstpzroKXtlbTrnbwmIzM5OzwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBVFQiIGRhdGEtbGFiZWw9IkFUVCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzMjIuMzA4IiB5PSI5Mi40NSIgd2lkdGg9IjY4LjYyNTk5OTk5OTk5OTk5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjM1Ni42MjEiIHk9IjExMC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5BVFQ8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkdQVSIgZGF0YS1sYWJlbD0iR1BVIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQzOC45MzM5OTk5OTk5OTk5NyIgeT0iOTIuNDUiIHdpZHRoPSI2OC42MjU5OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0NzMuMjQ2OTk5OTk5OTk5OTYiIHk9IjExMC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5HUFU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkZBSUwiIGRhdGEtbGFiZWw9IuygleyDgSDsgqzsmqnsnpDsnZgg7LGX67SHIOygkeyGjSDqsbDrtoAg8J+aqyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NTUuNTYiIHk9IjkyLjQ1IiB3aWR0aD0iMjQ1LjcyNSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjY3OC40MjI0OTk5OTk5OTk5IiB5PSIxMTAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7KCV7IOBIOyCrOyaqeyekOydmCDssZfrtIcg7KCR7IaNIOqxsOu2gCDwn5qrPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] Model DoS 공격 방식 및 보안 대응 방안 전격 해부 (3단 표)**

이 토픽은 AI를 마비시키는 \*\*'공격 수법'\*\*을 정확하게 기술하고, 실무에서 이를 완벽히 필터링하는 \*\*'API 제한 정책(TPM/RPM 등)'\*\*을 방어 대책으로 제시하는 것이 핵심입니다.

| **핵심 척도**               | **🚨 공격 기법 (연산 부하) 🚨**                                                                                                                                                                      | **🛡️ 보안 대응 방안 💯**                                                                                                                                                                                                                    | **💼 전통적 DDoS와의 차이 💯**                                                                                                                                        |
| :---------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **핵심 위협 요인**            | **'자원 소비의 비대칭성'.** 단 한 줄의 짧은 악성 프롬프트로 인해, 무거운 딥러닝 서버 전체의 메모리를 고갈시켜 뻗게 만듦.                                                                                                                    | **'추론 라이프사이클의 통제'.** AI 모델 앞단에서 입력 글자 수를 칼같이 차단하고 출력 시간 제한(Timeout)을 거는 보안 장치.                                                                                                                                                         | 패킷의 양으로 공격하는 L4/L7 DDoS와 달리, 단 1개의 정상적인 HTTP 요청(가장 긴 텍스트)으로 시스템을 터뜨림.                                                                                          |
| **공격 메커니즘 (출제 포인트) 🚨** | **1. \[무한 루프 유도]** 계속해서 텍스트를 출력하도록 지시. **2. \[Attention 공격 🚨]** 컨텍스트 윈도우 한계치까지 긴 문서(소설책 수십 권)를 입력하여 **행렬 연산량을 O(N2)*O*(*N*2) 로 폭주**시킴. **3. \[재귀형 프롬프트]** 자기 자신을 계속해서 복사/참조하게 만드는 특수 쿼리 주입. | **1. \[입출력 토큰 제한 💯]** 단일 질의의 최대 입력 토큰 수(Max Input)와 AI가 뱉을 수 있는 출력 토큰 수(Max Output)를 코드로 엄격하게 강제함. **2. \[TPM / RPM 적용 🚨]** API 게이트웨이에서 분당 호출수(RPM)와 \*\*분당 토큰 소비량(TPM)\*\*을 사용자 권한별로 제한. **3. \[타임아웃]** 추론 연산이 30초를 초과하면 커넥션 강제 종료. | **\[네트워크 DDoS]** 수만 대의 좀비 PC가 트래픽 폭탄을 던짐 (웹 방화벽/WAF로 IP 대역 방어가 쉬움). **\[Model DoS 💯]** 단 한 대의 일반 PC에서 \*\*'매우 어려운 질문'\*\*을 합법적 경로로 던지기 때문에 방화벽 필터링이 극도로 까다로움. |

#### **IV. \[결론/제언] MLOps 서빙 최적화(vLLM)와 오토 스케일링의 결합**

* **(키워드 위주 2줄 마무리)** "Model DoS 위협을 근본적으로 상쇄하기 위해서는 입력값 제어와 더불어, GPU 메모리 조각화를 방지하여 서빙 효율을 극대화하는 **'vLLM(PagedAttention)' 엔진을 인프라에 올리고, 동시 다발적 연산 부하 감지 시 서버 노드를 긴급히 증설하는 '오토 스케일링(Auto-scaling)' 인프라 아키텍처 연계가 전제되어야 합니다.**"
