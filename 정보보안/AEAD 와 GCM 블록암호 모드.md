### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (앞서다룬4모드의공통한계, AEAD의등장배경) — 3~4줄
Ⅱ. AEAD 핵심개념 (본론①, 도식 1개 필수)
Ⅲ. GCM의구체적동작원리, 핵심 배점
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서다룬ECB/CBC/CFB/OFB는모두'기밀성(암호화)'만신경썼지, '이암호문이중간에조작되지않았는지(무결성)'는전혀검증하지않았다 — 앞서다룬CCA(선택암호문공격)답안에서'패딩오라클공격'이가능했던이유가바로이무결성검증부재때문 — AEAD는암호화와무결성검증을동시에하는설계"\*\*라는한줄로시작하면, 왜AEAD가 앞서다룬두답안의 실무적해결책인지드러납니다.

### Ⅱ. AEAD 핵심개념 — 기밀성+무결성동시확보

| 구성요소                      | 역할                                              |
| :------------------------ | :---------------------------------------------- |
| **암호화**(Encryption)       | 앞서다룬 **대칭키암호**로 평문을 암호문으로변환(기밀성)                |
| **인증**(Authentication)    | \*\*인증태그(Tag)\*\*를생성해, 암호문이 **변조되지않았음을증명**(무결성) |
| **연관데이터**(AssociatedData) | **암호화는안하지만, 인증은해야하는데이터**(예:패킷헤더) — **AAD**      |

→ 암기: **"암호화로내용을숨기고,인증태그로변조여부를증명하고,헤더처럼암호화는불필요하지만인증은필요한부분도함께처리한다"** — 앞서다룬 \*\*"CCA공격"\*\*에서 \*\*"암호문을조금씩바꿔가며서버반응을관찰"\*\*했던 공격이, AEAD의 **인증태그검증**앞에서는 \*\*"태그가안맞으면즉시거부"\*\*되어 **원천차단**됩니다.

### 도식화 제안

```
[AEAD 구조]
[평문] + [AAD(헤더등,암호화불필요)]
     ↓
[암호화] → [암호문] + [인증태그(Tag)]
     ↓
[전송] 암호문+태그+AAD 모두전달
     ↓
[수신측검증]
"인증태그가일치하는가?" 
   ├─ 일치 → 정상복호화
   └─ 불일치 → 즉시거부(변조탐지!앞서다룬CCA공격차단)
```

### Ⅲ. GCM의구체적동작원리 — 핵심 배점

**함정 방지: "AEAD의한종류"라고만답하면절반. 왜"CTR모드+GHASH"의결합인지, 그리고앞서다룬CTR모드의병렬성이GCM에서어떻게활용되는지보여줘야완성됩니다.**

| 구성                   | 내용                                                                                      |
| :------------------- | :-------------------------------------------------------------------------------------- |
| **CTR모드기반**(암호화부분)   | 앞서다룬 **블록암호모드**중 \*\*CTR(카운터모드)\*\*를사용— **카운터값을암호화해키스트림생성**,평문과XOR                      |
| **GHASH함수**(인증부분,핵심) | 암호문전체를 **갈루아필드(GF(2^128))상의곱셈**으로 **하나의인증태그로압축**                                        |
| **병렬처리가능**(핵심장점)     | CTR모드는 앞서다룬 **"각블록이독립적으로카운터값만다르면"** 되므로, **암호화와인증계산을동시에,병렬로수행가능**— **소프트웨어·하드웨어양쪽에서고속** |

→ 암기: **"CTR모드로빠르게암호화하고,GHASH로암호문전체를하나의태그로압축해인증하는데,이둘을동시에병렬로처리할수있어서매우빠르다"** — 앞서다룬 \*\*"블록암호4모드"\*\*답안에서 CBC/CFB가 \*\*"순차적으로만처리가능(병렬화어려움)"\*\*했던 것과달리, GCM은 CTR기반이라 \*\*"암호화도인증도모두병렬화가능"\*\*합니다.

### 도식화 제안

```
[GCM 동작원리 - 병렬처리]

[CTR 모드 - 암호화(병렬가능)]
카운터1 → 암호화 → 키스트림1 ⊕ 평문블록1 = 암호문블록1
카운터2 → 암호화 → 키스트림2 ⊕ 평문블록2 = 암호문블록2  (동시에계산가능!)
카운터3 → 암호화 → 키스트림3 ⊕ 평문블록3 = 암호문블록3

[GHASH - 인증(병렬가능)]
암호문블록1,2,3 → 갈루아필드곱셈으로 → 하나의인증태그(Tag)로압축

→ "암호화도, 인증도 모두 병렬로 동시처리" = GCM이 실무표준인이유
```

**앞서다룬"TLS1.3"과의연결**: 앞서다룬 \*\*"TLS1.3의1-RTT핸드셰이크"\*\*이후 실제데이터전송구간에서, **AES-GCM**이 **가장널리쓰이는암호스위트**입니다 — 앞서다룬 **"디피헬만으로키교환"** 후, 실제 \*\*"메시지를암호화+인증하는것"\*\*이 바로 이 GCM모드입니다.

**앞서다룬"패딩오라클공격"과의직접비교**

| 구분          | **CBC(앞서다룬그것)**      | **GCM**                        |
| :---------- | :------------------- | :----------------------------- |
| **무결성검증**   | 없음(별도MAC필요)          | **내장**(인증태그자동생성)               |
| **패딩오라클공격** | **취약**(패딩오류메시지로정보누출) | **원천불가**(태그불일치시 즉시거부,세부정보노출안함) |
| **병렬처리**    | **불가**(순차적체이닝)       | **가능**(CTR기반)                  |

### Ⅳ. 결론

AEAD는 \*\*"앞서다룬대칭키암호모드들이기밀성만신경썼던한계를넘어, 암호화(기밀성)와인증태그(무결성)를동시에제공"\*\*하는 설계이며, GCM은 그 \*\*"CTR모드의병렬성"\*\*과 \*\*"GHASH의효율적인증"\*\*을 결합한 **가장널리쓰이는AEAD구현체**입니다 — 앞서다룬 \*\*"CCA(선택암호문공격),패딩오라클공격"\*\*이 **CBC모드의무결성검증부재**를 악용했던것과달리, GCM은 \*\*"인증태그불일치시즉시거부"\*\*하여 이런공격을 **원천적으로차단**합니다 — 이는 앞서다룬 \*\*"블록암호4모드→암호문공격유형→TLS1.3"\*\*으로 이어지는 오늘의암호학시리즈가, \*\*"실무에서왜ECB/CBC가아니라GCM이표준이됐는지"\*\*를 완결짓는 답이며, \*\*"암호화는기밀성만이아니라,반드시무결성과함께가야한다"\*\*는 현대암호학의 핵심원칙을 보여줍니다.

### **AEAD 와 GCM 블록암호 모드**

#### **1. 답안 전개 스토리 (핵심 압축)**

> "기존 블록암호 모드(CBC 등)의 치명적 결함인 '암호문 위변조 취약성'을 격파하고, **'암호화(기밀성)와 메시지 인증(무결성)을 단 하나의 연산 단계로 결합하여 동시에 완벽 처리하는 인증암호화(AEAD) 표준 모드'**이다. (TLS 1.3의 기본 권장 규격이다). 기존에는 암호화 따로, 무결성 해시(MAC) 따로 계산해서 속도가 느리고 해킹(패딩 오라클 공격)에 취약했다. **GCM (Galois/Counter Mode) 🚨**은 카운터(CTR) 모드로 고속 병렬 암호화를 수행하면서, 갈루아 필드 곱셈 연산(GHASH)을 통해 위변조 방지용 인증 태그(Tag)를 동시에 유도해 붙인다. 하드웨어 가속(AES-NI)과 완벽 호환되어 속도가 비약적으로 빠르며 암호문 변조를 입구에서 원천 차단하는 현대 블록 암호의 대세 기술이다."

#### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMTU0LjY4OSAzMzIuNjYxIiB3aWR0aD0iMTE1NC42ODkiIGhlaWdodD0iMzMyLjY2MSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iR0NNX0dhbG9pc0NvdW50ZXJfTW9kZV9BRUFEX18iIGRhdGEtbGFiZWw9IkdDTSAoR2Fsb2lzL0NvdW50ZXIgTW9kZSkgQUVBRCDsnbjspp3slZTtmLjtmZQg6rWs7KGwIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIxMDc0LjY4OSIgaGVpZ2h0PSIyNTIuNjYxIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMTA3NC42ODkiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5HQ00gKEdhbG9pcy9Db3VudGVyIE1vZGUpIEFFQUQg7J247Kad7JWU7Zi47ZmUIOq1rOyhsDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUExBSU4iIGRhdGEtdG89IkdDTSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIxODcuNjExLDE4MC4zMzA1IDIzNS42MTEsMTgwLjMzMDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkdDTSIgZGF0YS10bz0iRU5DIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIxLiBDVFIg66qo65OcIOyXsOyCsCIgcG9pbnRzPSIzOTYuMTYxODMzMzMzMzMzMzMsMjEyLjQ0MDY2NjY2NjY2NjcgNDQwLjI3MiwyMTIuNDQwNjY2NjY2NjY2NyA0NDAuMjcyLDIyMS4yMzA1IDY3Ni41MDIyNSwyMjEuMjMwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iR0NNIiBkYXRhLXRvPSJUQUciIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjIuIEdIQVNIIOqwiOujqOyVhCDtlYTrk5wg7Jew7IKwIiBwb2ludHM9IjM5Ni4xNjE4MzMzMzMzMzMzMywxNDguMjIwMzMzMzMzMzMzMzQgNDQwLjI3MiwxNDguMjIwMzMzMzMzMzMzMzQgNDQwLjI3MiwxMzkuNDMwNSA2NzYuNTAyMjUsMTM5LjQzMDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkVOQyIgZGF0YS10bz0iT1VUIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9Ijg3My4zMjEyNSwyMjEuMjMwNTAwMDAwMDAwMDMgOTI2LjQ5ODEyNTAwMDAwMDEsMjIxLjIzMDUwMDAwMDAwMDAzIDkyNi40OTgxMjUwMDAwMDAxLDE4MC4zMzA1MDAwMDAwMDAwMyA5NDYuMzMsMTgwLjMzMDUwMDAwMDAwMDAzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJUQUciIGRhdGEtdG89Ik9VVCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI5MDYuNjY2MjUsMTM5LjQzMDUgOTI2LjQ5ODEyNTAwMDAwMDEsMTM5LjQzMDUgOTI2LjQ5ODEyNTAwMDAwMDEsMTgwLjMzMDUwMDAwMDAwMDAzIDk0Ni4zMywxODAuMzMwNTAwMDAwMDAwMDMiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iR0NNIiBkYXRhLXRvPSJFTkMiIGRhdGEtbGFiZWw9IjEuIENUUiDrqqjrk5wg7Jew7IKwIj4KICA8cmVjdCB4PSI0OTkuODkzMDAwMDAwMDAwMDMiIHk9IjIwNS4yMzA1IiB3aWR0aD0iOTYuNjUyMDAwMDAwMDAwMDIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1NDguMjE5IiB5PSIyMjAuMzgwNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+MS4gQ1RSIOuqqOuTnCDsl7DsgrA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iR0NNIiBkYXRhLXRvPSJUQUciIGRhdGEtbGFiZWw9IjIuIEdIQVNIIOqwiOujqOyVhCDtlYTrk5wg7Jew7IKwIj4KICA8cmVjdCB4PSI0NzIuMjcyMDAwMDAwMDAwMDUiIHk9IjEyMy40MzA1MDAwMDAwMDAwMiIgd2lkdGg9IjE1MS44OTQwMDAwMDAwMDAwMyIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjU0OC4yMTkiIHk9IjEzOC41ODA1MDAwMDAwMDAwMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+Mi4gR0hBU0gg6rCI66Oo7JWEIO2VhOuTnCDsl7DsgrA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlBMQUlOIiBkYXRhLWxhYmVsPSLtj4nrrLgg642w7J207YSwIE0iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9IjE2MS44ODA0OTk5OTk5OTk5OCIgd2lkdGg9IjEzMS42MTEiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMjEuODA1NSIgeT0iMTgwLjMzMDQ5OTk5OTk5OTk3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7tj4nrrLgg642w7J207YSwIE08L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkdDTSIgZGF0YS1sYWJlbD0i4pyoIEdDTSDslZTtmLjtmZQg8J+aqCDinKgiIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iMzMxLjk0MTUsODQgNDI4LjI3MjAwMDAwMDAwMDA1LDE4MC4zMzA1IDMzMS45NDE1LDI3Ni42NjEgMjM1LjYxMTAwMDAwMDAwMDAyLDE4MC4zMzA1IiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjMzMS45NDE1IiB5PSIxODAuMzMwNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+4pyoIEdDTSDslZTtmLjtmZQg8J+aqCDinKg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkVOQyIgZGF0YS1sYWJlbD0i4pyoIOyVlO2YuOusuCBDaXBoZXJ0ZXh0IOKcqArtlZjrk5zsm6jslrQg67OR66CsIOqwgOyGjSDsl7DsgrAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNjc2LjUwMjI1IiB5PSIxOTQuMzMwNTAwMDAwMDAwMDMiIHdpZHRoPSIxOTYuODE5IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNzc0LjkxMTc1IiB5PSIyMjEuMjMwNTAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9Ijc3NC45MTE3NSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuKcqCDslZTtmLjrrLggQ2lwaGVydGV4dCDinKg8L3RzcGFuPjx0c3BhbiB4PSI3NzQuOTExNzUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPu2VmOuTnOybqOyWtCDrs5HroKwg6rCA7IaNIOyXsOyCsDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJUQUciIGRhdGEtbGFiZWw9IuKcqCDsnbjspp0g7YOc6re4IFRhZyDwn5KvIOKcqArrrLTqsrDshLEv7Iah7Iug7LKYIOuzgOyhsCDrsKnsp4Ag6rKA7KadIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjY3Ni41MDIyNSIgeT0iMTEyLjUzMDUiIHdpZHRoPSIyMzAuMTY0IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9Ijc5MS41ODQyNSIgeT0iMTM5LjQzMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9Ijc5MS41ODQyNSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuKcqCDsnbjspp0g7YOc6re4IFRhZyDwn5KvIOKcqDwvdHNwYW4+PHRzcGFuIHg9Ijc5MS41ODQyNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+66y06rKw7ISxL+yGoeyLoOyymCDrs4DsobAg67Cp7KeAIOqygOymnTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJPVVQiIGRhdGEtbGFiZWw9Iuy1nOyihSDsoITshqEg7Yyo7YK3IPCfmoAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iOTQ2LjMzIiB5PSIxNjEuODgwNSIgd2lkdGg9IjE1Mi4zNTkiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMDIyLjUwOTUiIHk9IjE4MC4zMzA1MDAwMDAwMDAwMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7LWc7KKFIOyghOyGoSDtjKjtgrcg8J+agDwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

| **핵심 척도**    | **📊 기존 블록암호 (CBC Mode)**                                        | **🔑 인증암호화 (AEAD / GCM Mode) 🚨**                                     | **🏁 TLS 1.3 보안 표준 연계 💯**                                                 |
| :----------- | :--------------------------------------------------------------- | :-------------------------------------------------------------------- | :------------------------------------------------------------------------- |
| **제공 보안성**   | **기밀성(암호화)만 제공.** 암호문이 중간에 위변조되어도 수신자가 복호화 오류를 보기 전까지 변조 여부를 모름. | **기밀성 + 무결성 + 인증 동시 보장 💯.** 복호화 전에 인증 태그를 먼저 스캔해 변조 적발 시 즉각 트래픽 차단.  | 보안 위협이 증명된 구형 암호 스위트(CBC 계열)를 퇴출하고 오직 **AEAD 전용 Suite**만 승인함.              |
| **동작 특징 🚨** | 이전 블록의 연산 결과가 다음 블록에 영향을 주는 체이닝 구조 ➔ 순차 연산만 가능 (병목).             | **완벽한 병렬 연산 (Parallel) 🚨.** 카운터(CTR) 값으로 병렬 암호화하고 GHASH로 하드웨어 가속 인증. | **\[대표 AEAD 스위트 💯]** 1. AES-GCM (하드웨어 우수). 2. ChaCha20-Poly1305 (모바일 우수). |

* **(제언)** "서버 보안성 심의 시 CBC 모드는 패딩 오라클 공격에 취약하므로 지양해야 합니다. **따라서 HTTPS 웹 서비스 및 가상 사설망(VPN) 설정 시 암호화 알고리즘 스위트를 반드시 'AES-GCM'이나 'ChaCha20-Poly1305' 같은 AEAD 규격으로만 잠가두도록 강력히 통제해야 합니다.**"

  <!-- pagebreak -->
