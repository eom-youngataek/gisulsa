### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (TLS의목적, 1.2→1.3의혁신) — 3~4줄
Ⅱ. 1-RTT 핸드셰이크 (본론①, 도식 1개 필수)
Ⅲ. 0-RTT - 재접속의혁신, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

TLS(전신SSL)는 앞서다룬 \*\*"전자봉투"\*\*의 실제인터넷구현체입니다 — 앞서다룬 \*\*디피헬만(키교환)\*\*과 \*\*RSA/ECC(신원인증)\*\*을 결합해, **웹사이트가 진짜인지확인**하고 **암호화된대칭키를 안전하게합의**합니다 — TLS1.3의핵심혁신은, 이과정을 \*\*더적은왕복(RTT)\*\*으로 끝내는 것입니다.

### Ⅱ. 1-RTT 핸드셰이크

| 단계                   | 내용                                               |
| :------------------- | :----------------------------------------------- |
| **①ClientHello**     | 클라이언트가 **지원가능한암호스위트+ECDHE키교환값**을 **미리한번에** 전송    |
| **②ServerHello+인증서** | 서버가 **자신의ECDHE값+인증서(신원증명)+Finished**를 **한번에** 응답 |
| **③Finished**        | 클라이언트가 최종확인 전송 → **암호화된데이터전송시작**                 |

→ 암기: **"클라이언트가한번에다던지고,서버도한번에다응답하니, 왕복1번(1-RTT)이면끝난다"** — 앞서다룬 **TLS1.2**는 \*\*"키교환따로,암호스위트협상따로"\*\*해서 **2-RTT**가 필요했는데, TLS1.3은 **"클라이언트가처음부터ECDHE키값을 추측해서 미리보내는"** 방식으로 **1번의왕복**으로 줄였습니다.

### 도식화 제안

```
[TLS1.2 - 2-RTT]                    [TLS1.3 - 1-RTT]
Client → ClientHello                Client → ClientHello+ECDHE키값(추측)
Server → ServerHello(암호스위트협상)   Server → ServerHello+ECDHE+인증서+Finished
Client → 키교환시작                  Client → Finished
Server → Finished                        ↓
     ↓                              [데이터전송시작] (1번왕복만에완료)
[데이터전송시작]
```

### Ⅲ. 0-RTT — 재접속의혁신, 핵심 배점

**함정 방지: "더빠르다"고만답하면절반. 왜"재접속"에만가능한지, 그리고치명적인보안위험(재생공격)을반드시보여줘야완성됩니다.**

| 항목              | 내용                                                                                            |
| :-------------- | :-------------------------------------------------------------------------------------------- |
| **적용조건**        | **이전에한번연결했던서버에 재접속**할때만가능(PSK,Pre-SharedKey 재사용)                                              |
| **동작**          | 클라이언트가 **첫패킷에 암호화된애플리케이션데이터까지 함께전송**— 왕복없이 **즉시데이터전송**                                        |
| **왜빠른가**        | 이전연결때 **합의했던키를재사용**해서, **새로키교환을할필요가없음**                                                       |
| **치명적위험**(핵심함정) | **재생공격**(ReplayAttack) — 공격자가 **암호화된0-RTT데이터를가로채 그대로재전송**하면, 서버가 \*\*"같은요청을또받은것"\*\*으로 처리할수있음 |

→ 암기: **"예전에만난사이라 인사없이바로용건부터말하는데, 그말을누가녹음해서다시틀면 서버가속을수있다"** — 이는 앞서다룬 \*\*"TOCTOU"\*\*와 유사한 \*\*"시간차를이용한취약점"\*\*입니다: \*\*"정상적인0-RTT요청"\*\*과 \*\*"녹음해서재전송한요청"\*\*을 서버가 **구별하기어렵습니다**.

### 도식화 제안

```
[0-RTT - 재접속시]
Client → ClientHello + 이전PSK로암호화된 애플리케이션데이터(즉시전송!)
     ↓ (왕복없이 바로데이터가 전달됨)
Server → 즉시응답

[재생공격위험]
공격자가 이 "ClientHello+암호화된데이터"를 그대로가로채
     ↓
동일한패킷을 서버에 다시전송
     ↓
서버가 "또같은요청이왔다"고 잘못처리할가능성
(예: "1000원결제" 요청이 재생되면 → 중복결제위험)
```

**대응**: **"멱등성이보장된요청(단순조회등)에만 0-RTT사용"**,서버측 **재생공격탐지캐시**운영 — 앞서다룬 \*\*"TOCTOU의원자적연산"\*\*원칙처럼, \*\*"결제,계좌이동같은비멱등적작업엔 0-RTT사용금지"\*\*가 실무권장사항입니다.

### Ⅳ. 결론

TLS1.3의1-RTT/0-RTT는 \*\*"앞서다룬디피헬만(키교환)과전자봉투(하이브리드암호화)의원리를, 최소한의왕복횟수로압축"\*\*한 것입니다 — 1-RTT는 \*\*"처음보는사이도 한번의왕복으로안전하게연결"\*\*하고, 0-RTT는 \*\*"이미아는사이라면 왕복자체를생략"\*\*하지만 **재생공격이라는대가**를 치를수있습니다 — 이는 오늘하루다룬 \*\*TCP3-wayhandshake(연결의신뢰성)→디피헬만(키합의)→전자봉투(하이브리드암호화)→TLS1.3(실전구현,속도와보안의트레이드오프)\*\*로 이어지는 네트워크·암호학시리즈전체를, **"보안과속도사이에서, 상황에맞는균형을선택하는"** 완결된하나의결론으로 마무리합니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "우리가 매일 쓰는 HTTPS 통신의 핵심인 TLS 암호화 프로토콜은, 과거 1.2 버전 시절 통신을 시작하기 전 인사(핸드셰이크)를 두 번이나 왕복(2-RTT)해야 해서 접속 속도가 느렸다. 이를 완전히 뜯어고친 혁신이 \*\*'TLS 1.3'\*\*이다. 핵심은 극단적인 접속 속도 향상이다. 처음 접속하는 서버라도 첫인사(Client Hello)에 암호 키 교환 정보까지 한꺼번에 묶어 던져버려 왕복 1번(**1-RTT**) 만에 인사를 끝낸다. 더 놀라운 건 재접속이다. 이전에 한 번 접속했던 서버라면, 예전에 발급받은 티켓(PSK)을 들이밀며 아예 인사 과정을 생략하고 첫 패킷부터 데이터를 쏴버린다(**0-RTT**). 지연 시간이 제로(0)다. 여기에 낡고 취약한 암호 알고리즘을 싹 다 폐기하여 속도와 보안 모두를 잡은 궁극의 웹 표준이 되었다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] HTTPS 속도와 보안의 대혁신, TLS 1.3 개요**

* **정의:** 인터넷 웹 통신(L4~L7)의 보안을 담당하는 표준 프로토콜로, 구버전(TLS 1.2)의 취약한 암호 알고리즘을 대거 폐기하고 **핸드셰이크(Handshake) 과정을 1-RTT 및 0-RTT로 단축**하여 지연시간(Latency)을 최소화한 최신 표준.
* **도입 목적 (보안 강화):** 기존 RSA 키 교환 방식의 취약점을 버리고, 해커가 서버의 마스터 키를 털어도 과거의 통신 내역을 해독할 수 없는 \*\*'완벽한 전방향 무결성(PFS, Perfect Forward Secrecy)'\*\*을 강제하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 인사 2번(과거) ➔ 1번(신규) ➔ 0번(재접속) 파이프라인**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NDQuNTk2IDQxNy44IiB3aWR0aD0iNjQ0LjU5NiIgaGVpZ2h0PSI0MTcuOCIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iVExTXzEzX19fXzFSVFRfXzBSVFQiIGRhdGEtbGFiZWw9IlRMUyAxLjMg7ZW465Oc7IWw7J207YGsIOyGjeuPhCDtmIHsi6AgKDEtUlRUICZhbXA7IDAtUlRUKSI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNTY0LjU5NiIgaGVpZ2h0PSIzMzcuOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjU2NC41OTYiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5UTFMgMS4zIO2VuOuTnOyFsOydtO2BrCDsho3rj4Qg7ZiB7IugICgxLVJUVCAmYW1wOyAwLVJUVCk8L3RleHQ+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMV9fXzFSVFRfIiBkYXRhLWxhYmVsPSIxLiDsi6Dqt5wg7KCR7IaNICgxLVJUVCkg4pqhIj4KICA8cmVjdCB4PSI1NiIgeT0iMjEzLjkiIHdpZHRoPSI1MzIuNTk2IiBoZWlnaHQ9IjE0Ny45IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNTYiIHk9IjIxMy45IiB3aWR0aD0iNTMyLjU5NiIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjgiIHk9IjIyNy45IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjEuIOyLoOq3nCDsoJHsho0gKDEtUlRUKSDimqE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSIyX18wUlRUXyIgZGF0YS1sYWJlbD0iMi4g7J6s7KCR7IaNICgwLVJUVCkg8J+agCI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iNTA0LjY3ODAwMDAwMDAwMDEiIGhlaWdodD0iMTA5LjkiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSI1MDQuNjc4MDAwMDAwMDAwMSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjgiIHk9Ijk4IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjIuIOyerOygkeyGjSAoMC1SVFQpIPCfmoA8L3RleHQ+CjwvZz4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQzEiIGRhdGEtdG89IlMxIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLssqvsnbjsgqzsl5Ag64K0ICftgqQoS2V5KeydmCDsoIjrsJgn64+EIOqwmeydtCDrs7Trg4QhIiBwb2ludHM9IjE4OC4wNSwzMTEuNDI1IDIwMC4wNSwzMTEuNDI1IDIwMC4wNSwzMzUuNSA0NjUuMDA2MDAwMDAwMDAwMDMsMzM1LjUgNDY1LjAwNjAwMDAwMDAwMDAzLDMxMS40MjUgNTAxLjAwNjAwMDAwMDAwMDAzLDMxMS40MjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlMxIiBkYXRhLXRvPSJDMSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7ISc67KEIO2CpCDshJ7slrTshJwg7JmE7ISxIOKelCDthrXsi6Ag7KSA67mEIOuBnSEiIHBvaW50cz0iNTAxLjAwNjAwMDAwMDAwMDAzLDMwMi4yIDE4OC4wNSwzMDIuMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQzEiIGRhdGEtdG89IlMxIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i4pyoIOyZleuztSAx67KIIOunjOyXkCDslZTtmLjtmZQg642w7J207YSwIOyghOyGoSDinKgiIHBvaW50cz0iMTg4LjA1LDI5Mi45NzUgMjAwLjA1LDI5Mi45NzUgMjAwLjA1LDI2OC45IDQ2NS4wMDYwMDAwMDAwMDAwMywyNjguOSA0NjUuMDA2MDAwMDAwMDAwMDMsMjkyLjk3NSA1MDEuMDA2MDAwMDAwMDAwMDMsMjkyLjk3NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDMiIgZGF0YS10bz0iUzIiIGRhdGEtc3R5bGU9InRoaWNrIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9ImZhbHNlIiBkYXRhLWxhYmVsPSLsnbjsgqwg7JWIIO2VqCEK7JiI7KCEIO2LsOy8kyhQU0spIOuTpOydtOuwgOupsArinKgg67CU66GcIOyyqyDtjKjtgrfsl5Ag642w7J207YSwIOyPtOuyhOumvCEg4pyoIiBwb2ludHM9IjE4OC4wNSwxNTMgNDczLjA4ODAwMDAwMDAwMDEsMTUzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIyIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJDMSIgZGF0YS10bz0iUzEiIGRhdGEtbGFiZWw9Iuyyq+yduOyCrOyXkCDrgrQgJ+2CpChLZXkp7J2YIOygiOuwmCfrj4Qg6rCZ7J20IOuztOuDhCEiPgogIDxyZWN0IHg9IjIzMi4wNSIgeT0iMzE5LjUiIHdpZHRoPSIyMjQuOTU2MDAwMDAwMDAwMDIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzNDQuNTI4IiB5PSIzMzQuNjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuyyq+yduOyCrOyXkCDrgrQgJiMzOTvtgqQoS2V5KeydmCDsoIjrsJgmIzM5O+uPhCDqsJnsnbQg67O064OEITwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJTMSIgZGF0YS10bz0iQzEiIGRhdGEtbGFiZWw9IuyEnOuyhCDtgqQg7ISe7Ja07IScIOyZhOyEsSDinpQg7Ya17IugIOykgOu5hCDrgZ0hIj4KICA8cmVjdCB4PSIyNDUuMTE4IiB5PSIyODYuMjAwMDAwMDAwMDAwMDUiIHdpZHRoPSIxOTguODIwMDAwMDAwMDAwMDIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzNDQuNTI4IiB5PSIzMDEuMzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuyEnOuyhCDtgqQg7ISe7Ja07IScIOyZhOyEsSDinpQg7Ya17IugIOykgOu5hCDrgZ0hPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkMxIiBkYXRhLXRvPSJTMSIgZGF0YS1sYWJlbD0i4pyoIOyZleuztSAx67KIIOunjOyXkCDslZTtmLjtmZQg642w7J207YSwIOyghOyGoSDinKgiPgogIDxyZWN0IHg9IjIzOS4xNzgiIHk9IjI1Mi45IiB3aWR0aD0iMjEwLjcwMDAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzQ0LjUyOCIgeT0iMjY4LjA1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7inKgg7JmV67O1IDHrsogg66eM7JeQIOyVlO2YuO2ZlCDrjbDsnbTthLAg7KCE7IahIOKcqDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJDMiIgZGF0YS10bz0iUzIiIGRhdGEtbGFiZWw9IuyduOyCrCDslYgg7ZWoIQrsmIjsoIQg7Yuw7LyTKFBTSykg65Ok7J2067CA66mwCuKcqCDrsJTroZwg7LKrIO2MqO2Ct+yXkCDrjbDsnbTthLAg7I+067KE66a8ISDinKgiPgogIDxyZWN0IHg9IjIzMi4wNSIgeT0iMTIyLjk5OTk5OTk5OTk5OTk5IiB3aWR0aD0iMTk3LjAzODAwMDAwMDAwMDA0IiBoZWlnaHQ9IjU4LjkwMDAwMDAwMDAwMDAwNiIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzMzAuNTY5IiB5PSIxNTIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSIzMzAuNTY5IiBkeT0iLTEwLjQ1MDAwMDAwMDAwMDAwMSI+7J247IKsIOyViCDtlaghPC90c3Bhbj48dHNwYW4geD0iMzMwLjU2OSIgZHk9IjE0LjMiPuyYiOyghCDti7DsvJMoUFNLKSDrk6TsnbTrsIDrqbA8L3RzcGFuPjx0c3BhbiB4PSIzMzAuNTY5IiBkeT0iMTQuMyI+4pyoIOuwlOuhnCDssqsg7Yyo7YK37JeQIOuNsOydtO2EsCDsj7TrsoTrprwhIOKcqDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDMSIgZGF0YS1sYWJlbD0i7YG065287J207Ja47Yq4IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjcyIiB5PSIyODMuNzUiIHdpZHRoPSIxMTYuMDUiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNjZmQ4ZGMiIHN0cm9rZT0iIzkwYTRhZSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEzMC4wMjUiIHk9IjMwMi4yIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7tgbTrnbzsnbTslrjtirg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlMxIiBkYXRhLWxhYmVsPSLshJzrsoQiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTAxLjAwNjAwMDAwMDAwMDAzIiB5PSIyODMuNzUiIHdpZHRoPSI3MS41OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNTM2LjgwMSIgeT0iMzAyLjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyEnOuyhDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQzIiIGRhdGEtbGFiZWw9Iu2BtOudvOydtOyWuO2KuCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3MiIgeT0iMTM0LjU1IiB3aWR0aD0iMTE2LjA1IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjEzMC4wMjUiIHk9IjE1MyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7YG065287J207Ja47Yq4PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTMiIgZGF0YS1sYWJlbD0i7ISc67KEIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQ3My4wODgwMDAwMDAwMDAxIiB5PSIxMzQuNTUiIHdpZHRoPSI3MS41OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI1MDguODgzMDAwMDAwMDAwMSIgeT0iMTUzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7shJzrsoQ8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] TLS 1.2 (2-RTT) vs TLS 1.3 (1-RTT/0-RTT) 핵심 스펙 비교 (3단 표)**

| **핵심 척도**               | **🛑 기존 TLS 1.2 (과거)**                                                    | **🚀 TLS 1.3 (현재) 🚨**                                                                                                                                   |
| :---------------------- | :------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **왕복 횟수 (RTT)**         | **2-RTT (초기 연결 매우 느림).** 인사하고(1), 암호화 방식 정하고, 키 교환(2)하느라 왕복 두 번의 시간이 버려짐. | **1-RTT (최초) / 0-RTT (재접속) 💯.** 첫인사(`Client Hello`) 때 키 교환용 매개변수까지 한 방에 던져서 연결 시간을 절반으로 깎아버림.                                                           |
| **0-RTT 동작 원리 (재접속 시)** | (지원하지 않음)                                                                 | **\[사전 공유 키 (PSK) 기반 조기 데이터]** 이전에 연결했던 서버라면 서버가 발급해 준 티켓(PSK)을 기억했다가, 재접속 시 **핸드셰이크 없이 바로 첫 패킷(`Early Data`)에 암호화된 데이터를 실어 보냄.**                        |
| **보안성 / 취약점 🚨**        | 낡은 알고리즘(RSA, MD5 등) 잔존.                                                   | **\[보안 극대화 vs Replay Attack 위험 ❌]** - 취약한 알고리즘(RSA 키교환) 삭제 및 PFS 보장. - 단, **0-RTT는 해커가 첫 번째 패킷을 통째로 복사해 서버에 다시 쏘는 '재전송 공격(Replay Attack)'의 치명적 취약점 존재.** |

#### **IV. \[결론/제언] 0-RTT 재전송 공격 방어 및 HTTP/3(QUIC)로의 완전한 통합**

* **(키워드 위주 2줄 마무리)** "TLS 1.3의 0-RTT는 접속 딜레이를 아예 없애는 기적을 보여주지만, 첫 패킷이 복사되어 결제가 중복 처리되는 재전송 공격(Replay Attack)을 막기 위해 멱등성(Idempotent)이 보장되는 GET 요청에만 제한적으로 사용해야 합니다. 현재 이 TLS 1.3 기술은 차세대 웹 표준인 **HTTP/3의 UDP 기반 'QUIC 프로토콜' 안에 통째로 내장되어, 인터넷 역사상 가장 빠르고 안전한 0-RTT 암호화 통신 생태계를 완성했습니다.**"
