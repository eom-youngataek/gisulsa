### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (LLM코드생성의부상,2026년현황) — 3~4줄
Ⅱ. 핵심리스크 (본론①, 도식 1개 필수)
Ⅲ. 검증체계 - 기존기법의재적용 (본론②, 핵심 배점)
Ⅳ. 거버넌스체계및오늘시리즈총연결
Ⅴ. 결론
```

포인트: 개요에서 \*\*"2026년현재,LLM기반코딩어시스턴트(ClaudeCode등)는 SWE-bench같은실전벤치마크에서 최상위성과를내며, 이미상당한비중의프로덕션코드가AI로생성되고있다 — 다만 코드생성속도가빨라진만큼, 앞서다룬모든품질관리기법(테스트,리팩토링,정적분석)이 AI시대에맞게재조정되어야한다"\*\*는 한줄로시작하면, 오늘하루의모든답안이 이답안으로수렴되는구조가됩니다.

### Ⅱ. 핵심리스크 — "환·의·과"

| 리스크                   | 내용                                                                               |
| :-------------------- | :------------------------------------------------------------------------------- |
| **환각(Hallucination)** | 그럴듯하지만 **사실과다른코드/API를확신하며생성** — 존재하지않는함수를호출하는코드를만들수있음                            |
| **의도부재**              | 앞서다룬 \*\*"기술부채4분면"\*\*의핵심통찰 — **AI는의도를갖지않아**, 무모(Reckless)한지신중(Prudent)한지 판단하지않음 |
| **과도한의존**             | 개발자가 **AI출력을충분히평가하지않고그대로수용** — 검토를생략하기로한선택자체가 새로운위험                              |

→ 암기: **"사실이아닌걸사실처럼말하고,의도라는게없고,사람이검토를건너뛴다"** — 앞서다룬 \*\*"AI생성부채는개발자가검토를생략하기로선택한 새로운형태의무모함"\*\*이라는 기술부채4분면답안의결론이, 여기서 **핵심리스크의근원**으로다시등장합니다.

### 도식화 제안

```
[LLM코드생성]
   ↓
[환각가능성] "이함수는존재하지않는데,있는것처럼생성"
   ↓
[의도부재] AI는"신중했는지무모했는지"판단안함
   ↓
[개발자의선택] 검토함(안전) or 검토안함(위험,새로운기술부채)
```

### Ⅲ. 검증체계 — 기존기법의재적용, 핵심 배점

**함정 방지: "AI코드는위험하니안쓴다"고답하면오해. 오늘다룬기존기법들을 AI시대에어떻게재적용하는지 보여줘야완성됩니다.**

| 오늘다룬기법          | AI코드생성시대의적용                                                       |
| :-------------- | :---------------------------------------------------------------- |
| **정적분석(SAST)**  | 앞서다룬 DevSecOps의**ShiftLeft**원칙— AI생성코드도 **즉시정적분석통과**를 파이프라인관문으로설정 |
| **TDD**         | **"AI가코드짜기전에, 사람이먼저테스트를쓴다"**— 테스트가 **AI출력의검증기준**역할                |
| **코드리뷰**        | AI생성코드도 **반드시사람리뷰**필수(자동승인금지)                                     |
| **뮤테이션테스트**     | AI가작성한 **테스트케이스자체의품질**도 검증(AI가부실한테스트만생성했을가능성)                     |
| **McCabe순환복잡도** | AI가생성한코드의 **복잡도를자동측정**,과도하게복잡하면반려                                 |

→ 암기: **"AI가짜기전에테스트를먼저정하고,짠뒤에는정적분석+사람리뷰+복잡도측정을 반드시통과시킨다"** — 앞서다룬 **모든검증기법이 여전히유효하며, 오히려AI시대에더엄격하게적용해야한다**는게 이답안의핵심메시지입니다.

### 도식화 제안

```
[사람] 테스트먼저작성(TDD) → [AI] 코드생성
                                  ↓
                          [정적분석(SAST)] 자동통과필수
                                  ↓
                          [McCabe복잡도측정] 임계치이하
                                  ↓
                          [사람코드리뷰] 필수(자동승인금지)
                                  ↓
                          [뮤테이션테스트] 테스트품질검증
                                  ↓
                              [병합승인]
```

### Ⅳ. 거버넌스체계 및 오늘시리즈총연결

**함정 방지: 개별기법나열만하면절반. 조직차원의거버넌스체계까지가야완성됩니다.**

| 체계               | 내용                                                      |
| :--------------- | :------------------------------------------------------ |
| **AI코드기여도추적**    | 커밋마다 **AI생성비중을기록**(어떤코드가AI산출물인지추적성확보,앞서다룬**RTM**의철학과유사) |
| **CMMI/프로세스성숙도** | 앞서다룬 **CMMI**의 프로세스개선영역에 \*\*"AI활용가이드라인"\*\*을 조직표준으로반영  |
| **기술부채모니터링강화**   | 앞서다룬 **기술부채4분면**중 **"의도적+무모"부채발생빈도**를 AI코드영역에서 특히주시     |

→ "오늘하루다룬McCabe(복잡도측정)→기술부채4분면(판단기준)→코드스멜(증상)→리팩토링(해법)→CMMI(조직성숙도)→테스트시리즈전체(검증)가, 사실AI코드생성시대에 오히려더중요해진다"는게 이답안의최종통합포인트입니다.

### Ⅴ. 결론 포인트 (오늘의모든소프트웨어공학시리즈 대단원)

LLM코드생성은 \*\*"코드를누가짜는가"\*\*를 바꿨을뿐, \*\*"그코드가좋은코드인지어떻게판단하는가"\*\*라는 근본질문은 전혀바뀌지않았습니다 — 오늘하루다룬 McCabe순환복잡도,결합도/응집도,코드스멜,리팩토링,TDD/BDD,정적/동적분석,테스트7대원칙,ISO25010,CMMI,기술부채4분면같은 모든 \*\*"품질을측정하고관리하는도구들"\*\*은, AI가코드를짜는시대에 **오히려더필수적**입니다 — \*\*"AI는속도를주지만,의도와판단은여전히사람의몫"\*\*이라는 이결론으로, 오늘하루의 방대하고깊이있었던 소프트웨어공학·컴퓨터구조·아키텍처·테스트·품질·비용산정·공공제도전체시리즈를 마무리합니다.

### **I. \[개요] 2026년, 코드를 짜는 주체의 변화와 품질 관리의 재조정**

2026년 현재, LLM 기반 코딩 어시스턴트(GitHub Copilot, Claude Code 등)는 SWE-bench 같은 실전 벤치마크에서 최상위 성과를 내며, 이미 상당한 비중의 프로덕션 코드가 AI로 생성되고 있습니다. **다만 코드 생성 속도가 폭발적으로 빨라진 만큼, 우리가 그동안 다루어 온 모든 소프트웨어 품질 관리 기법(TDD, 리팩토링, 정적 분석 등)이 이 거대한 AI의 속도에 휩쓸리지 않도록 시대에 맞게 재조정**되어야만 합니다.

***

### **II. \[핵심 리스크] 환각, 의도의 부재, 그리고 새로운 기술 부채 (도식화)**

앞서 다룬 \*\*'기술 부채 4분면'\*\*의 핵심 통찰을 떠올려 보십시오. AI가 짜내는 코드의 가장 무서운 점은 바로 \*\*'의도(Intent)가 없다'\*\*는 것입니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NzkuMzIxIDk0Mi43MzY5OTk5OTk5OTk5IiB3aWR0aD0iNjc5LjMyMSIgaGVpZ2h0PSI5NDIuNzM2OTk5OTk5OTk5OSIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iTExNX19fM19fX18iIGRhdGEtbGFiZWw9IkxMTSDsvZTrk5wg7IOd7ISx7J2YIDPrjIAg7ZW17IusIOumrOyKpO2BrCDtjIzsnbTtlITrnbzsnbggKO2ZmMK37J2Ywrfqs7wpIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI1OTkuMzIxIiBoZWlnaHQ9Ijg2Mi43MzY5OTk5OTk5OTk5IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNTk5LjMyMSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPkxMTSDsvZTrk5wg7IOd7ISx7J2YIDPrjIAg7ZW17IusIOumrOyKpO2BrCDtjIzsnbTtlITrnbzsnbggKO2ZmMK37J2Ywrfqs7wpPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJMTE0iIGRhdGEtdG89IkgiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzk3LjEyNjI1LDEzNy44IDM5Ny4xMjYyNSwxODUuOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iSCIgZGF0YS10bz0iSSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIzOTcuMTI2MjUsMjU2LjUgMzk3LjEyNjI1LDMwNC41IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJJIiBkYXRhLXRvPSJEIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjM5Ny4xMjYyNSwzNzUuMiAzOTcuMTI2MjUsNDIzLjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkQiIGRhdGEtdG89IkJPTUIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuqygO2GoCDsg53rnrXtlZjqs6Ag67CU66GcIOuzke2VqSIgcG9pbnRzPSIzNDguMjIwMDgzMzMzMzMzMyw2NjcuNzMwODMzMzMzMzMzMyAzNDguMjIwMDgzMzMzMzMzNCw3MjguNjM3IDI3MC40NTI1LDcyOC42MzcgMjcwLjQ1MjUsODMyLjkzNjk5OTk5OTk5OTkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkQiIGRhdGEtdG89IlNBRkUiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iuq5kOq5kO2VnCDqsoDspp0g7YyM7J207ZSE65287J24IO2GteqzvCIgcG9pbnRzPSI0NDYuMDMyNDE2NjY2NjY2Nyw2NjcuNzMwODMzMzMzMzMzMyA0NDYuMDMyNDE2NjY2NjY2Nyw3MjguNjM3IDUyMy44MDAwMDAwMDAwMDAxLDcyOC42MzcgNTIzLjgsODMyLjkzNjk5OTk5OTk5OTkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iRCIgZGF0YS10bz0iQk9NQiIgZGF0YS1sYWJlbD0i6rKA7YagIOyDneuete2VmOqzoCDrsJTroZwg67OR7ZWpIj4KICA8cmVjdCB4PSIxOTkuNDUyNSIgeT0iNzU5LjYzNyIgd2lkdGg9IjE0MS43OTYwMDAwMDAwMDAwNSIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjI3MC4zNTA1IiB5PSI3NzQuNzg2OTk5OTk5OTk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+6rKA7YagIOyDneuete2VmOqzoCDrsJTroZwg67OR7ZWpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkQiIGRhdGEtdG89IlNBRkUiIGRhdGEtbGFiZWw9Iuq5kOq5kO2VnCDqsoDspp0g7YyM7J207ZSE65287J24IO2GteqzvCI+CiAgPHJlY3QgeD0iNDQwLjgwMDAwMDAwMDAwMDA3IiB5PSI3NTkuNjM3IiB3aWR0aD0iMTY1LjU1NjAwMDAwMDAwMDA0IiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIzLjU3ODAwMDAwMDAwMDEiIHk9Ijc3NC43ODY5OTk5OTk5OTk5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7quZDquZDtlZwg6rKA7KadIO2MjOydtO2UhOudvOyduCDthrXqs7w8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkxMTSIgZGF0YS1sYWJlbD0iTExNIOq4sOuwmCDsvZTrk5wg7IOd7ISxIPCfpJYK7JeE7LKt64KcIOyGjeuPhOuhnCDsj5/slYTsp4DripQg7L2U65OcIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjI4My44OTY3NSIgeT0iODQiIHdpZHRoPSIyMjYuNDU5IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjM5Ny4xMjYyNSIgeT0iMTEwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjM5Ny4xMjYyNSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPkxMTSDquLDrsJgg7L2U65OcIOyDneyEsSDwn6SWPC90c3Bhbj48dHNwYW4geD0iMzk3LjEyNjI1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7sl4Tssq3rgpwg7IaN64+E66GcIOyPn+yVhOyngOuKlCDsvZTrk5w8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iSCIgZGF0YS1sYWJlbD0iMS4g7ZmY6rCBIO2YhOyDgSBIYWxsdWNpbmF0aW9uIPCfkbsKJnF1b3Q77KG07J6s7ZWY7KeAIOyViuuKlCBBUEnrgpgg7ZWo7IiY66W8CuyeiOuKlCDqsoPsspjrn7wg7ZmV7Iug7ZWY66mwIOu7lOu7lO2VmOqyjCDsg53shLEmcXVvdDsiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjU4LjcwMjc1MDAwMDAwMDA0IiB5PSIxODUuOCIgd2lkdGg9IjI3Ni44NDciIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzOTcuMTI2MjUiIHk9IjIyMS4xNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMzk3LjEyNjI1IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+MS4g7ZmY6rCBIO2YhOyDgSBIYWxsdWNpbmF0aW9uIPCfkbs8L3RzcGFuPjx0c3BhbiB4PSIzOTcuMTI2MjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPiZxdW90O+yhtOyerO2VmOyngCDslYrripQgQVBJ64KYIO2VqOyImOulvDwvdHNwYW4+PHRzcGFuIHg9IjM5Ny4xMjYyNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7J6I64qUIOqyg+yymOufvCDtmZXsi6DtlZjrqbAg67uU67uU7ZWY6rKMIOyDneyEsSZxdW90OzwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJJIiBkYXRhLWxhYmVsPSIyLiDsnZjrj4TsnZgg67aA7J6sIE5vIEludGVudCDwn6S34oCN4pmC77iPCiZxdW90O0FJ64qUIOyLoOykke2VnOyngCwg66y066qo7ZWc7KeAIO2MkOuLqO2VmOyngCDslYrsnYwuCuq3uOyggCDtmZXrpaDsoIHsnLzroZwg6re465+065Ov7ZWcIOy9lOuTnOulvCDrsYnsnYQg67+QJnF1b3Q7IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjI0Mi43NzEyNSIgeT0iMzA0LjUiIHdpZHRoPSIzMDguNzEiIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIzOTcuMTI2MjUiIHk9IjMzOS44NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMzk3LjEyNjI1IiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+Mi4g7J2Y64+E7J2YIOu2gOyerCBObyBJbnRlbnQg8J+kt+KAjeKZgu+4jzwvdHNwYW4+PHRzcGFuIHg9IjM5Ny4xMjYyNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+JnF1b3Q7QUnripQg7Iug7KSR7ZWc7KeALCDrrLTrqqjtlZzsp4Ag7YyQ64uo7ZWY7KeAIOyViuydjC48L3RzcGFuPjx0c3BhbiB4PSIzOTcuMTI2MjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuq3uOyggCDtmZXrpaDsoIHsnLzroZwg6re465+065Ov7ZWcIOy9lOuTnOulvCDrsYnsnYQg67+QJnF1b3Q7PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkQiIGRhdGEtbGFiZWw9IjMuIOqzvOuPhO2VnCDsnZjsobQgT3Zlci1yZWxpYW5jZSDwn5W177iP4oCN4pmC77iPCuqwnOuwnOyekOqwgCDqsoDthqDrpbwg7IOd65617ZWgIOqyg+yduOqwgD8iIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iMzk3LjEyNjI1LDQyMy4yMDAwMDAwMDAwMDAwNSA1NDMuODQ0NzUsNTY5LjkxODUgMzk3LjEyNjI1LDcxNi42MzcgMjUwLjQwNzc1MDAwMDAwMDA1LDU2OS45MTg1IiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjM5Ny4xMjYyNSIgeT0iNTY5LjkxODUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjM5Ny4xMjYyNSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPjMuIOqzvOuPhO2VnCDsnZjsobQgT3Zlci1yZWxpYW5jZSDwn5W177iP4oCN4pmC77iPPC90c3Bhbj48dHNwYW4geD0iMzk3LjEyNjI1IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7qsJzrsJzsnpDqsIAg6rKA7Yag66W8IOyDneuete2VoCDqsoPsnbjqsIA/PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkJPTUIiIGRhdGEtbGFiZWw9IuyDiOuhnOyatCAn66y066qo7ZWcIOq4sOyIoCDrtoDssYQnIO2PreuwnCDwn5KlCuuztOyViCDqsrDtlagsIOyKpO2MjOqyjO2LsCDsvZTrk5wg7JaR7IKwISIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxNDQuNjI2IiB5PSI4MzIuOTM2OTk5OTk5OTk5OSIgd2lkdGg9IjI1MS42NTMiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMjcwLjQ1MjUiIHk9Ijg1OS44MzY5OTk5OTk5OTk5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIyNzAuNDUyNSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuyDiOuhnOyatCAmIzM5O+ustOuqqO2VnCDquLDsiKAg67aA7LGEJiMzOTsg7Y+t67CcIPCfkqU8L3RzcGFuPjx0c3BhbiB4PSIyNzAuNDUyNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+67O07JWIIOqysO2VqCwg7Iqk7YyM6rKM7YuwIOy9lOuTnCDslpHsgrAhPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlNBRkUiIGRhdGEtbGFiZWw9IuyViOyghO2VnCDtgbTrprAg7L2U65OcIOyViOywqSDinKgiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDI0LjI3OSIgeT0iODMyLjkzNjk5OTk5OTk5OTkiIHdpZHRoPSIxOTkuMDQyIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1MjMuOCIgeT0iODUxLjM4NyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7JWI7KCE7ZWcIO2BtOumsCDsvZTrk5wg7JWI7LCpIOKcqDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSI2OC42MjYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI5MC4zMTMiIHk9IjEwMi40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Tm90ZTwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

***

### **III. \[검증 체계] 기존 소프트웨어 공학 기법의 강력한 재적용 (3단 표)**

"AI 코드는 위험하니 쓰지 말자"가 아닙니다. 우리가 오늘 다루었던 **위대한 품질 검증 기법들을 AI 시대에 어떻게 더 가혹하게 들이대야 하는지**를 증명해야 합니다. (AI가 짜기 전에 테스트를 먼저 정하고, 짠 뒤에는 정적분석+사람리뷰+복잡도를 반드시 통과시킵니다.)

| **오늘 다룬 품질 검증 기법**           | **AI 코드 생성 시대에서의 역할 재정의 및 적용 방안**                                                                                            | **실무적 방어 효과**                        |
| :--------------------------- | :--------------------------------------------------------------------------------------------------------------------------- | :----------------------------------- |
| **1. TDD** *(테스트 주도 개발)*     | **"AI가 코드를 짜기 전에, 사람이 먼저 테스트를 짠다."** 자연어 프롬프트에 의존하지 않고, 인간이 명확히 정의한 단위 테스트 코드가 AI 출력물의 절대적 검증(Pass/Fail) 기준 역할을 수행함.         | AI의 환각(없는 함수 호출 등)을 실행 단계에서 즉각 차단.   |
| **2. McCabe 순환 복잡도**         | AI가 뱉어낸 코드가 겉으론 멀쩡해 보여도 내부가 지옥일 수 있음. **AI 생성 코드의 McCabe 복잡도(V(G))를 자동 측정하여, 수치가 10(임계치)을 넘어가면 즉각 병합 반려(Reject) 및 리팩토링 지시.** | 스파게티 코드의 은밀한 유입을 수학적으로 차단.           |
| **3. 정적 분석 (SAST)**          | DevSecOps의 Shift-Left 사상 적용. AI가 코드를 생성하자마자 CI 파이프라인에서 **보안 취약점(SQL 인젝션 등)과 코드 스멜을 스캔하여, 통과해야만 다음 단계로 이동.**                  | AI가 과거 데이터에서 학습한 낡은 보안 결함의 유입 차단.    |
| **4. 코드 리뷰 (Peer Review)**   | AI가 짠 코드라도 **반드시 '인간' 시니어 개발자의 수동 리뷰(Approve)를 거쳐야만 반영**되도록 거버넌스 강제. (자동 승인 절대 금지).                                          | '의도'가 없는 AI 코드에 인간의 비즈니스 '의도'를 불어넣음. |
| **5. 뮤테이션 테스트** *(돌연변이 테스트)* | AI가 본인 코드를 변호하기 위해 '허술한 단위 테스트'를 짰을 가능성 검증. **AI가 짠 테스트 케이스에 일부러 버그(뮤턴트)를 던져서, AI 테스트 케이스 자체가 건강한지 품질을 감시함.**                | 테스트 커버리지 100%라는 AI의 거짓된 착각 타파.       |

***

### **IV. \[거버넌스 체계] 무너지는 품질을 막기 위한 조직적 통제 (오늘 시리즈 총연결)**

위의 기법들을 파편적으로 쓰는 것이 아니라, 조직 전체의 룰로 엮어내야 합니다.

* **AI 코드 기여도 추적 체계 (RTM 철학):** 요구사항 추적 매트릭스(RTM)처럼, 커밋(Commit)마다 AI가 생성한 코드 비중을 기록하여 훗날 라이선스 침해나 치명적 버그 발생 시 '이 코드가 인간의 것인지 AI의 산출물인지' 즉각 추적할 수 있는 가시성을 확보합니다.
* **CMMI 성숙도 레벨 3(조직 표준) 반영:** 회사 전체의 개발 표준 프로세스(CMMI Level 3) 지침서에 \*\*'AI 활용 보안 가이드라인 및 리뷰 절차'\*\*를 공식적으로 못 박아, 구멍가게 수준이 아닌 5성급 팩토리 수준의 AI 통제를 이룹니다.
* **기술 부채 4분면 기반의 모니터링:** AI가 짜준 코드를 검토 없이 배포하는 행위를 기술 부채 매트릭스의 \*\*'무모하고 고의적인 부채(Reckless & Deliberate)'\*\*로 엄격히 규정하고, 정기적인 리팩토링 스프린트를 통해 AI가 싼 똥(부채)을 치워나갑니다.

***

### **V. \[결론] 대단원: AI는 속도를 주지만, 의도와 판단은 영원히 사람의 몫이다.**

* "LLM 코드 생성 기술은 소프트웨어 공학에서 단지 \*\*'코드를 타자 치는 주체가 누구인가'\*\*를 기계로 바꾸었을 뿐입니다. \*\*'그 코드가 정말 좋은 아키텍처인가? 유지보수하기 쉬운가? 보안에 안전한가?'\*\*라는 근본적인 질문은 단 하나도 바뀌지 않았습니다.
* 오히려 무서운 속도로 코드가 쏟아지는 이 시대야말로, 오늘 우리가 다루었던 **McCabe 순환 복잡도, 모듈의 결합도/응집도, 코드 스멜과 리팩토링, TDD 십자선 검증, ISO 25010 품질 속성, CMMI 인증 체계, 기술 부채의 철학** 같은 위대한 소프트웨어 공학의 '측정 및 관리 도구'들이 과거 그 어느 때보다도 뼈저리게 필요한 시점입니다.
* 결국, 기술이 아무리 발전해도 \*\*'AI는 압도적인 속도를 제공할 뿐, 그 코드의 올바른 비즈니스적 의도(Intent)를 부여하고 품질을 판단하는 최종 책임은 영원히 인간 소프트웨어 엔지니어의 몫'\*\*입니다."
