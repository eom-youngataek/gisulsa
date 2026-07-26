### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (메모리풀링의필요성, 앞서다룬CXL3.0과의연결) — 3~4줄
Ⅱ. 메모리풀링동작원리 (본론①, 도식 1개 필수)
Ⅲ. TCO절감효과및한계, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

앞서다룬 \*\*"CXL2.0의메모리풀링"\*\*을 이번엔 **"왜필요하고,실제로얼마나이득인지"** 관점에서 깊게파겠습니다 — 데이터센터에서 각서버는 **"자기전용메모리"**를 갖는데, 어떤서버는 **메모리가남아돌고**, 다른서버는 **메모리가부족해서** 작업을못하는 **"메모리불균형"**이 항상발생합니다 — 메모리풀링은 **"이여러서버의메모리를 하나의공유풀로묶어, 필요한서버가필요한만큼가져다쓰게"** 합니다.
![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MzkuODM4OTk5OTk5OTk5OTQgMjg2LjcwMDAwMDAwMDAwMDA1IiB3aWR0aD0iNDM5LjgzODk5OTk5OTk5OTk0IiBoZWlnaHQ9IjI4Ni43MDAwMDAwMDAwMDAwNSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJIb3N0QSIgZGF0YS10bz0iU3dpdGNoIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0idHJ1ZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTQyLjcwNzQ5OTk5OTk5OTk4LDc2LjkgMTQyLjcwNzQ5OTk5OTk5OTk4LDEwMC45IDIxOS45MTk0OTk5OTk5OTk5NywxMDAuOSAyMTkuOTE5NDk5OTk5OTk5OTcsMTI0LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgbWFya2VyLXN0YXJ0PSJ1cmwoI2Fycm93aGVhZC1zdGFydCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJIb3N0QiIgZGF0YS10bz0iU3dpdGNoIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0idHJ1ZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjk3LjEzMTQ5OTk5OTk5OTk2LDc2LjkgMjk3LjEzMTQ5OTk5OTk5OTk2LDEwMC45IDIxOS45MTk0OTk5OTk5OTk5NywxMDAuOSAyMTkuOTE5NDk5OTk5OTk5OTcsMTI0LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgbWFya2VyLXN0YXJ0PSJ1cmwoI2Fycm93aGVhZC1zdGFydCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTd2l0Y2giIGRhdGEtdG89Ik1MRCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9InRydWUiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjIxOS45MTk0OTk5OTk5OTk5NywxNjEuOCAyMTkuOTE5NDk5OTk5OTk5OTcsMjA5LjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgbWFya2VyLXN0YXJ0PSJ1cmwoI2Fycm93aGVhZC1zdGFydCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJIb3N0QSIgZGF0YS1sYWJlbD0i7Zi47Iqk7Yq4IENQVSBBIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9Ijc5LjQ5NTQ5OTk5OTk5OTk5IiB5PSI0MCIgd2lkdGg9IjEyNi40MjM5OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE0Mi43MDc0OTk5OTk5OTk5OCIgeT0iNTguNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPu2YuOyKpO2KuCBDUFUgQTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU3dpdGNoIiBkYXRhLWxhYmVsPSJDWEwgMi4wIOyKpOychOy5mCAmYW1wOyBGYWJyaWMgTWFuYWdlciIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI5OC4xNjg1IiB5PSIxMjQuOSIgd2lkdGg9IjI0My41MDE5OTk5OTk5OTk5NSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjE5LjkxOTQ5OTk5OTk5OTk3IiB5PSIxNDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkNYTCAyLjAg7Iqk7JyE7LmYICZhbXA7IEZhYnJpYyBNYW5hZ2VyPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJIb3N0QiIgZGF0YS1sYWJlbD0i7Zi47Iqk7Yq4IENQVSBCIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjIzMy45MTk0OTk5OTk5OTk5NyIgeT0iNDAiIHdpZHRoPSIxMjYuNDIzOTk5OTk5OTk5OTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyOTcuMTMxNDk5OTk5OTk5OTYiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7tmLjsiqTtirggQ1BVIEI8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik1MRCIgZGF0YS1sYWJlbD0iTUxEIOuplOuqqOumrCDtkoAgOiDstZzrjIAgMTbqsJwg64W866asIOyYgeyXrSDrj5nsoIEg67aE7ZWgL+2VoOuLuSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MCIgeT0iMjA5LjgiIHdpZHRoPSIzNTkuODM4OTk5OTk5OTk5OTQiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMjE5LjkxOTQ5OTk5OTk5OTk3IiB5PSIyMjguMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk1MRCDrqZTrqqjrpqwg7ZKAIDog7LWc64yAIDE26rCcIOuFvOumrCDsmIHsl60g64+Z7KCBIOu2hO2VoC/tlaDri7k8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

### Ⅱ. 메모리풀링동작원리

| 구성                      | 역할                                            |
| :---------------------- | :-------------------------------------------- |
| **CXL스위치**(핵심하드웨어)      | 여러서버와 **여러메모리모듈사이를 동적으로연결**해주는 **중개장치**       |
| **CXL.mem프로토콜**(앞서다룬그것) | CPU가 **풀에있는메모리를,자신의로컬메모리처럼직접접근**              |
| **동적할당**                | 서버A가 메모리부족해지면 → **풀에서추가할당**,서버B가 남으면 → **반납** |

→ 암기: **"CXL스위치가여러서버와여러메모리를이어주고, CXL.mem으로 마치자기메모리처럼쓰고, 필요에따라동적으로늘리고줄인다"** — 앞서다룬 **"메모리인터리빙"**이 **"고정된여러뱅크"**를 병렬화했다면, 메모리풀링은 **"고정이아니라동적으로,필요한만큼"** 나눠쓴다는 점이 근본적차이입니다.

### 도식화 제안

```
[메모리풀링 구조]
[서버A: 메모리부족] ─┐
[서버B: 메모리남음] ─┼──CXL스위치──[공유메모리풀]
[서버C: 메모리부족] ─┘

[동적할당]
서버A → 풀에서메모리추가할당요청 → 즉시할당
서버B → 안쓰는메모리반납 → 풀로회수
     ↓
"각서버가 고정된자기메모리만쓰는게아니라,
 전체풀에서 필요한만큼유연하게가져다쓴다"
```

### Ⅲ. TCO절감효과 및 한계 — 핵심 배점

**함정 방지: "메모리를공유한다"고만답하면절반. 구체적으로얼마나비용을절감하는지, 그리고레이턴시(지연시간)라는대가를 균형있게보여줘야완성됩니다.**

| 항목                    | 내용                                                                                                                   |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------- |
| **메모리활용률개선**(핵심가치)    | 기존에는 서버마다 **"혹시몰라서"과다장착**했던 메모리를, 풀링으로 **"실제필요한만큼만"**공유해 **전체메모리구매량자체를절감**                                           |
| **TCO절감**(총소유비용)      | **DRAM자체가고가**인데다, 앞서다룬 **HBM보다는저렴하지만** 여전히비싼자원— **활용률을높이면 서버증설비용자체를늦출수있음**                                           |
| **한계①레이턴시**(핵심트레이드오프) | CXL스위치를 거쳐야하므로, **로컬메모리(DRAM직결)보다 접근속도가느림**— 앞서다룬 **"메모리계층구조"**에서 \*\*"CXL확장메모리"\*\*가 **"로컬DRAM과보조기억장치사이"**에 위치하는 이유 |
| **한계②소프트웨어지원**        | OS·애플리케이션이 **"이메모리가로컬인지,풀에서온것인지"**를 구분해 **최적화된방식으로활용**하려면 **추가적인소프트웨어스택**이 필요                                        |

→ 암기: **"메모리를덜사도되니TCO는줄지만,스위치를거치는만큼조금느려지고,소프트웨어도이를인식하도록만들어야한다"** — 앞서다룬 \*\*"RAID의스트라이핑(속도)vs미러링(안전)"\*\*과 유사하게, 메모리풀링도 **"비용절감vs속도"**라는 트레이드오프를 가집니다.

### 도식화 제안

```
[TCO 절감 vs 레이턴시 트레이드오프]

[풀링없이 - 기존방식]
서버마다 최대치로메모리장착(혹시몰라서과다구매)
→ 비용↑,활용률낮음(평소엔남아돎),하지만속도는빠름(로컬DRAM직결)

[풀링적용]
전체메모리를 공유풀로 운영,필요한만큼만할당
→ 비용↓(TCO절감),활용률↑,하지만 CXL스위치경유로 약간의레이턴시추가

[메모리계층에서의위치(앞서다룬그것)]
레지스터→캐시(SRAM)→로컬DRAM→[CXL풀메모리]→보조기억장치
                                  ↑
                    "로컬보다느리지만,보조기억보다훨씬빠른" 중간계층
```

**앞서다룬"HBM과의역할분담"재확인**: 앞서다룬 \*\*"HBM=성능우선(대역폭),CXL=용량·가성비우선(풀링)"\*\*이라는 구분이, 실제AI서버설계에서 **"연산에직접필요한데이터는HBM에,대용량이지만상대적으로덜급한데이터는CXL풀메모리에"** 배치하는 **계층적자원배분전략**으로 구현됩니다.

###

### **I. 데이터센터 자원 효율화의 핵심, CXL 2.0 메모리 풀링의 개요**

CXL 1.1은 단일 호스트 CPU에 1:1로 메모리를 추가 확장하는 방식(SLD)에 머물러, 특정 서버의 메모리가 낭비되더라도 타 서버가 이를 끌어다 쓰지 못하는 **메모리 가두리(Memory Stranding) 현상**이 발생했습니다. **CXL 2.0 메모리 풀링**은 CXL 스위치와 **MLD(Multi-Logical Device)** 아키텍처를 도입하여, **하나의 CXL 메모리 자원을 여러 대의 호스트가 소프트웨어적으로 동적 할당받고 사용 후 반납**할 수 있게 만든 차세대 클라우드 메모리 공유 기술입니다.

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MzkuODM4OTk5OTk5OTk5OTQgMjg2LjcwMDAwMDAwMDAwMDA1IiB3aWR0aD0iNDM5LjgzODk5OTk5OTk5OTk0IiBoZWlnaHQ9IjI4Ni43MDAwMDAwMDAwMDAwNSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJIb3N0QSIgZGF0YS10bz0iU3dpdGNoIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0idHJ1ZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMTQyLjcwNzQ5OTk5OTk5OTk4LDc2LjkgMTQyLjcwNzQ5OTk5OTk5OTk4LDEwMC45IDIxOS45MTk0OTk5OTk5OTk5NywxMDAuOSAyMTkuOTE5NDk5OTk5OTk5OTcsMTI0LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgbWFya2VyLXN0YXJ0PSJ1cmwoI2Fycm93aGVhZC1zdGFydCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJIb3N0QiIgZGF0YS10bz0iU3dpdGNoIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0idHJ1ZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjk3LjEzMTQ5OTk5OTk5OTk2LDc2LjkgMjk3LjEzMTQ5OTk5OTk5OTk2LDEwMC45IDIxOS45MTk0OTk5OTk5OTk5NywxMDAuOSAyMTkuOTE5NDk5OTk5OTk5OTcsMTI0LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgbWFya2VyLXN0YXJ0PSJ1cmwoI2Fycm93aGVhZC1zdGFydCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTd2l0Y2giIGRhdGEtdG89Ik1MRCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9InRydWUiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjIxOS45MTk0OTk5OTk5OTk5NywxNjEuOCAyMTkuOTE5NDk5OTk5OTk5OTcsMjA5LjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgbWFya2VyLXN0YXJ0PSJ1cmwoI2Fycm93aGVhZC1zdGFydCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJIb3N0QSIgZGF0YS1sYWJlbD0i7Zi47Iqk7Yq4IENQVSBBIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9Ijc5LjQ5NTQ5OTk5OTk5OTk5IiB5PSI0MCIgd2lkdGg9IjEyNi40MjM5OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE0Mi43MDc0OTk5OTk5OTk5OCIgeT0iNTguNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPu2YuOyKpO2KuCBDUFUgQTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU3dpdGNoIiBkYXRhLWxhYmVsPSJDWEwgMi4wIOyKpOychOy5mCAmYW1wOyBGYWJyaWMgTWFuYWdlciIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI5OC4xNjg1IiB5PSIxMjQuOSIgd2lkdGg9IjI0My41MDE5OTk5OTk5OTk5NSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjE5LjkxOTQ5OTk5OTk5OTk3IiB5PSIxNDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkNYTCAyLjAg7Iqk7JyE7LmYICZhbXA7IEZhYnJpYyBNYW5hZ2VyPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJIb3N0QiIgZGF0YS1sYWJlbD0i7Zi47Iqk7Yq4IENQVSBCIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjIzMy45MTk0OTk5OTk5OTk5NyIgeT0iNDAiIHdpZHRoPSIxMjYuNDIzOTk5OTk5OTk5OTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyOTcuMTMxNDk5OTk5OTk5OTYiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7tmLjsiqTtirggQ1BVIEI8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik1MRCIgZGF0YS1sYWJlbD0iTUxEIOuplOuqqOumrCDtkoAgOiDstZzrjIAgMTbqsJwg64W866asIOyYgeyXrSDrj5nsoIEg67aE7ZWgL+2VoOuLuSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MCIgeT0iMjA5LjgiIHdpZHRoPSIzNTkuODM4OTk5OTk5OTk5OTQiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMjE5LjkxOTQ5OTk5OTk5OTk3IiB5PSIyMjguMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk1MRCDrqZTrqqjrpqwg7ZKAIDog7LWc64yAIDE26rCcIOuFvOumrCDsmIHsl60g64+Z7KCBIOu2hO2VoC/tlaDri7k8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

***

### **II. CXL 2.0 메모리 풀링의 3대 핵심 기술 구성요소**

| **🔑 핵심 구성 요소 🚨**                | **🏁 역할 및 상세 동작 메커니즘 💯**                                              |
| :-------------------------------- | :--------------------------------------------------------------------- |
| **1. CXL 스위치 (Switch)**           | 단일 레벨 CXL 스위치로, 다중 호스트 CPU와 다중 CXL 메모리 장치 사이에서 패킷을 가상 라우팅              |
| **2. MLD (Multi-Logical Device)** | 하나의 물리적 CXL 메모리를 \*\*최대 16개의 독립된 논리 디바이스(LD)\*\*로 분할하여 이종 호스트에 각각 할당   |
| **3. 패브릭 매니저 (Fabric Manager)**   | 데이터센터 관리 소프트웨어와 연동하여, 호스트의 자원 요청 시 재부팅 없이 메모리를 동적 핫플러그(Hot-Plug) 할당/회수 |

***

### **III. CXL 1.1 메모리 확장과 CXL 2.0 메모리 풀링의 상세 비교**

| **비교 항목**             | **🔌 CXL 1.1 (1:1 메모리 확장)**       | **🌐 CXL 2.0 (메모리 풀링)**                       |
| :-------------------- | :-------------------------------- | :-------------------------------------------- |
| **연결 토폴로지**           | 1:1 점대점 (Point-to-Point) 단일 연결    | **CXL 스위치 기반 N:M 다중 호스트 연결**                  |
| **메모리 장치 유형**         | SLD (Single-Logical Device) 단일 장치 | **MLD (Multi-Logical Device) 지원 (최대 16개 분할)** |
| **가두리(Stranding) 예방** | 불가능 (특정 서버 유휴 메모리 낭비)             | **완벽 해결 (중앙 풀에서 동적 대여/반납으로 TCO 절감)**          |
| **동적 용량 변경 (DCT)**    | 서버 재부팅 시에만 메모리 구성 변경 가능           | **서버 가동 중 무재부팅 핫플러그(Hot-Plug) 동적 할당**         |
| **제어 관리 주체**          | 단순 하드웨어 레지스터 제어                   | **Fabric Manager (FM) 기반 소프트웨어 정의 제어**        |
| **보안/데이터 파기**         | 단일 서버 종속으로 단순 파기                  | **메모리 반납 시 타 호스트 재할당 전 완전 영구 삭제 필수**          |

***

### **IV. CXL 2.0 메모리 풀링 도입 시 엔지니어링 고려사항**

1. **메모리 반납 시 데이터 완전 소거 (Zeroing)**: MLD 환경에서 호스트 A가 사용하다 반납한 메모리 영역이 호스트 B에 재할당될 때 이전 잔재 데이터가 유출될 위험(Memory Leak)이 있습니다. 하드웨어 스위치 차원에서 **반납 즉시 해당 영역을 0으로 덮어쓰는 자동 영구 소거(Sanitization)** 메커니즘을 적용해야 합니다.
2. **Fabric Manager 고가용성(HA) 구성**: CXL 스위치 및 Fabric Manager가 마비되면 전사 메모리 풀 조율이 정지됩니다. 이중화(Active-Standby) 관제 파이프라인을 구축하여 신품 메모리 동적 확장 신호 유실을 방지해야 합니다.
