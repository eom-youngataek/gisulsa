## 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (공급망보안필요성,SBOM등장배경) — 3~4줄
Ⅱ. SBOM 핵심구성요소 (본론①, 도식 1개 필수)
Ⅲ. 공급망공격유형 (본론②, 핵심 배점)
Ⅳ. 국내외제도화현황
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬CI/CD파이프라인,오픈소스생태계는수많은 '남이만든컴포넌트(라이브러리,패키지)'를가져다쓰는데, 그중하나만악성이거나취약해도 전체시스템이위험해진다 — 음식점이재료의원산지를표시하듯, 소프트웨어도'이코드에어떤재료(컴포넌트)가들어갔는지' 목록화한것이SBOM"\*\*이라는 한줄로시작하면, 왜 "식품안전"에 비유되는지 논리가섭니다.

### Ⅱ. SBOM 핵심구성요소 — "SoftwareBillOfMaterials(소프트웨어자재명세서)"

| 항목         | 내용                                      |
| :--------- | :-------------------------------------- |
| **컴포넌트정보** | 사용된 **모든오픈소스·서드파티라이브러리명,버전**            |
| **의존성관계**  | 어떤컴포넌트가 **어떤다른컴포넌트에의존**하는지(중첩구조)        |
| **라이선스정보** | 각컴포넌트의 **오픈소스라이선스**(GPL,MIT등)           |
| **표준형식**   | **SPDX,CycloneDX**등 표준화된포맷으로 기계가읽을수있게작성 |

→ 암기: **"무엇이들어갔고,서로어떻게연결됐고,법적으로어떤라이선스인지 기계가읽을수있게적어놓은것"** — 앞서다룬 \*\*"LLM코드생성"\*\*답안에서 다룬 \*\*"AI코드기여도추적"\*\*개념이, 여기서는 \*\*"AI가가져다쓴오픈소스컴포넌트까지도추적"\*\*하는 것으로확장됩니다.

### 도식화 제안

```
[우리앱]
   ├─ 라이브러리A(v2.1) ── 의존 ── 라이브러리A-1(v1.0)
   ├─ 라이브러리B(v3.5)
   └─ 라이브러리C(v1.2) ── 의존 ── 라이브러리C-1(v0.9,MIT라이선스)
                                         ↑
                              (만약이버전에 알려진취약점CVE있다면?)

→ SBOM이 있으면 "우리앱이 그취약한컴포넌트를쓰는지" 즉시확인가능
```

### Ⅲ. 공급망공격유형 — 핵심 배점

**함정 방지: "취약점이있는라이브러리를쓴다"고만답하면절반. 앞서다룬미라이/오픈소스생태계답안과연결되는 구체적공격유형을보여줘야완성됩니다.**

| 유형              | 내용                                                                            |
| :-------------- | :---------------------------------------------------------------------------- |
| **의존성하이재킹**     | 인기패키지의 **오래된계정을탈취**하거나, **비슷한이름의악성패키지**(타이포스쿼팅)를배포                            |
| **빌드시스템침투**     | 앞서다룬 **BPFDoor,Lazarus의GitHooks/JenkinsCI/CD악용**— **빌드과정자체에악성코드주입**           |
| **알려진취약점방치**    | 앞서다룬 **CTEM**에서다룬 **"2025년악용취약점의61%가공개후48시간내무기화"**— 패치를못따라가면 방치된취약점이 공급망전체를위협 |
| **오픈소스유지관리자공격** | 소규모오픈소스프로젝트의 **관리자권한을소셜엔지니어링으로탈취**후 악성코드삽입                                    |

→ 암기: **"이름을비슷하게해서속이거나,빌드과정에몰래심거나,알려진구멍을방치하거나,관리자를직접노린다"** — 앞서다룬 \*\*"인포스틸러"\*\*답안의 \*\*"Lazarus의GitHooks·JenkinsCI/CD악용"\*\*사례가 정확히 \*\*"빌드시스템침투형공급망공격"\*\*의실제사례였습니다.

### 도식화 제안

```
[공급망공격 지점]
[오픈소스개발자] ──(계정탈취/타이포스쿼팅)──→ [악성패키지배포]
        ↓
[CI/CD파이프라인] ──(GitHooks/Jenkins악용)──→ [빌드과정에악성코드주입]
        ↓
[우리앱에통합] → 우리도모르게 악성코드가 프로덕션에배포됨
```

### Ⅳ. 국내외제도화현황

**함정 방지: "SBOM이좋다"는 원칙만말하면절반. 실제법제화·의무화흐름을보여줘야완성됩니다.**

| 항목           | 내용                                                                                   |
| :----------- | :----------------------------------------------------------------------------------- |
| **미국**       | 행정명령(EO14028)이후 **연방정부납품SW에SBOM의무화**                                                 |
| **한국동향**     | 앞서검색자료에서확인된 \*\*"CI분리보관"**규제 시행시점이 당초계획보다당겨짐,**"SBOM제도화,투명한공급망이신뢰를만든다"\*\*는 보안칼럼논조확산 |
| **CTEM과의연계** | 앞서다룬 **CTEM의"발견(Discovery)"단계**에서, SBOM은 **"우리시스템에무엇이있는지"** 파악하는 **가장기초적인자산인벤토리**    |

→ 앞서다룬 **CTEM**답안의 \*\*"범위설정→발견"\*\*단계가, SBOM없이는 **애초에불가능**하다는 연결이 핵심입니다 — \*\*"내시스템에어떤컴포넌트가있는지도모르면서, 무엇을보호할지 정할수없다"\*\*는 것입니다.

### Ⅴ. 결론 포인트

SBOM은 \*\*"우리가직접작성한코드는전체시스템의일부일뿐이며, 나머지대부분은신뢰여부를검증하지않은외부컴포넌트로이루어져있다"\*\*는 불편한진실에대한 **가장기초적인해법**입니다 — 앞서다룬 \*\*미라이봇넷(소스코드유출의영속성),인포스틸러(빌드시스템침투),CTEM(자산가시성)\*\*이 모두 \*\*"내시스템을구성하는요소를제대로알아야만 방어할수있다"\*\*는 하나의결론으로 수렴하며, 오늘하루다룬 방대한사이버보안시리즈전체가 \*\*"보이지않는것은지킬수없다"\*\*는 가장근본적인원칙으로 마무리됩니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "해커가 철통 보안을 자랑하는 거대 기업을 정면으로 뚫기는 너무 어렵다. 그래서 꼼수를 썼다. 기업이 납품받아 사용하는 조그만 하청업체(오픈소스 라이브러리, 업데이트 서버)를 몰래 털어서 부품에 악성코드를 심어놓은 것이다. 기업은 아무 의심 없이 정상적인 업데이트인 줄 알고 다운받았다가 전산망 전체가 좀비가 되어버렸다(솔라윈즈 사태). 이것이 무시무시한 \*\*'소프트웨어 공급망 공격'\*\*이다. 현대 소프트웨어는 개발자가 100% 다 짜는 것이 아니라, 80% 이상을 외부 오픈소스(부품)를 가져와 레고처럼 조립해서 만든다. 따라서 이 공격을 막으려면 내 소프트웨어 안에 '어느 회사의, 어떤 부품, 무슨 버전'이 들어갔는지 빼곡히 적혀있는 \*\*'원산지 성분표'\*\*가 무조건 필요하다. 이것이 바로 \*\*'SBOM (소프트웨어 자산 명세서)'\*\*이다. 특정 오픈소스(Log4j 등)에 치명적 취약점이 터졌다는 뉴스가 나오면, 기업은 자기 서비스의 SBOM(성분표)만 딱 검색해 보고 1초 만에 '우리 A서버에 저 부품이 들어있네! 당장 패치해!'라고 즉각 대처할 수 있게 해주는 마법의 명세서다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 성 밖의 우물에 독을 푸는 트로이 목마, 공급망 보안과 SBOM 개요**

* **공급망 공격 (Supply Chain Attack):** 타겟 기업을 직접 공격하는 대신, 그 기업이 사용하는 **소프트웨어의 개발, 배포, 업데이트 과정(공급망)에 침투**하여 오픈소스 패키지나 업데이트 파일에 악성코드를 은닉하여 유포하는 우회 공격 기법.
* **SBOM (Software Bill of Materials):** 소프트웨어를 구성하는 모든 오픈소스, 서드파티 라이브러리, 패키지의 이름, 버전, 라이선스, 의존성 관계 등을 상세히 기록해 둔 **'소프트웨어 자산(원산지) 명세서'**. 미국 바이든 행정부의 행정명령으로 전 세계 의무화 추세.

#### **II. \[본론 1] (단순화 버전) 공급망 해킹의 흐름과 SBOM의 방어 파이프라인 (도식화)**

해커가 어디를 노리는지, 그리고 SBOM이 어떻게 그 투명성을 밝혀내는지 직관적으로 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNTg2LjI0ODUwMDAwMDAwMDEgNzMwLjMwMDAwMDAwMDAwMDEiIHdpZHRoPSIxNTg2LjI0ODUwMDAwMDAwMDEiIGhlaWdodD0iNzMwLjMwMDAwMDAwMDAwMDEiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9fXyIgZGF0YS1sYWJlbD0i7IaM7ZSE7Yq47Juo7Ja0IOqzteq4ieunnSDtlbTtgrkg6rO87KCVIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIxMzAxLjgxMTAwMDAwMDAwMDEiIGhlaWdodD0iMTEzLjgwMDAwMDAwMDAwMDAxIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iMTMwMS44MTEwMDAwMDAwMDAxIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+7IaM7ZSE7Yq47Juo7Ja0IOqzteq4ieunnSDtlbTtgrkg6rO87KCVPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX19TQk9NX1NvZnR3YXJlX0JpbGxfb2ZfTWF0ZXJpYWxzIiBkYXRhLWxhYmVsPSLrsKnslrQg66y06riwOiBTQk9NIChTb2Z0d2FyZSBCaWxsIG9mIE1hdGVyaWFscykiPgogIDxyZWN0IHg9IjExNTcuMzczNTAwMDAwMDAwMSIgeT0iMjcwLjEiIHdpZHRoPSIzODguODc0OTk5OTk5OTk5OSIgaGVpZ2h0PSI0MjAuMjAwMDAwMDAwMDAwMDUiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSIxMTU3LjM3MzUwMDAwMDAwMDEiIHk9IjI3MC4xIiB3aWR0aD0iMzg4Ljg3NDk5OTk5OTk5OTkiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjExNjkuMzczNTAwMDAwMDAwMSIgeT0iMjg0LjEiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+67Cp7Ja0IOustOq4sDogU0JPTSAoU29mdHdhcmUgQmlsbCBvZiBNYXRlcmlhbHMpPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJUQVJHRVQiIGRhdGEtdG89IlNCT00iIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLrsKnslrQiIHBvaW50cz0iMTMyNS44MTEwMDAwMDAwMDAxLDExNS4xMjUgMTM0MS44MTEwMDAwMDAwMDAxLDExNS4xMjUgMTM1MS44MTEwMDAwMDAwMDAxLDExMC45IDEzNTEuODExMDAwMDAwMDAwMSwyNzAuMSAxMzUxLjgxMTAwMDAwMDAwMDEsMzE0LjEiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iSEFDS0VSIiBkYXRhLXRvPSJPU1MiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iuq4sOyXheydtCDslYTri4jrnbwK7ZWY7LKtKOyYpO2UiOyGjOyKpCnsnYQg7YS064ukISIgcG9pbnRzPSIxNDQuNjMyOTk5OTk5OTk5OTgsMTA2LjY3NSAzNjcuMzAxLDEwNi42NzUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209Ik9TUyIgZGF0YS10bz0iREVWIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLslYTrrLQg7J2Y7IusIOyXhuydtArsoJXsg4Eg67aA7ZKI7J24IOykhCDslYzqs6Ag7KGw66a9IiBwb2ludHM9IjU5OS42ODgsMTEwLjkgODMxLjI2NjAwMDAwMDAwMDEsMTEwLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkRFViIgZGF0YS10bz0iVEFSR0VUIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsl4XrjbDsnbTtirgg67Cw7Y+sIiBwb2ludHM9Ijk3OS4xNzkwMDAwMDAwMDAxLDExNS4xMjUgMTE1Ny44OTEsMTE1LjEyNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iU0JPTSIgZGF0YS10bz0iU0VBUkNIIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSJMb2c0aiDtlbTtgrkg64m07IqkIOuwnOyDnSDsi5wiIHBvaW50cz0iMTM1MS44MTEwMDAwMDAwMDAxLDM2Ny45MDAwMDAwMDAwMDAwMyAxMzUxLjgxMTAwMDAwMDAwMDEsNDg0LjIwMDAwMDAwMDAwMDA1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTRUFSQ0giIGRhdGEtdG89IlBBVENIIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIx7LSIIOunjOyXkCDsi53rs4Qg67CPIOyhsOy5mCIgcG9pbnRzPSIxMzUxLjgxMTAwMDAwMDAwMDEsNTIxLjEgMTM1MS44MTEwMDAwMDAwMDAxLDYzNy40MDAwMDAwMDAwMDAxIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlRBUkdFVCIgZGF0YS10bz0iU0JPTSIgZGF0YS1sYWJlbD0i67Cp7Ja0Ij4KICA8cmVjdCB4PSIxMzMwLjgxMTAwMDAwMDAwMDEiIHk9IjE5Ni44IiB3aWR0aD0iNDEuNDEiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxMzUxLjUxNiIgeT0iMjExLjk1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7rsKnslrQ8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iSEFDS0VSIiBkYXRhLXRvPSJPU1MiIGRhdGEtbGFiZWw9Iuq4sOyXheydtCDslYTri4jrnbwK7ZWY7LKtKOyYpO2UiOyGjOyKpCnsnYQg7YS064ukISI+CiAgPHJlY3QgeD0iMTg4LjYzMjk5OTk5OTk5OTk4IiB5PSI4Ny45IiB3aWR0aD0iMTM0LjY2OCIgaGVpZ2h0PSI0NC42IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjI1NS45NjY5OTk5OTk5OTk5OCIgeT0iMTEwLjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSIyNTUuOTY2OTk5OTk5OTk5OTgiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij7quLDsl4XsnbQg7JWE64uI6528PC90c3Bhbj48dHNwYW4geD0iMjU1Ljk2Njk5OTk5OTk5OTk4IiBkeT0iMTQuMyI+7ZWY7LKtKOyYpO2UiOyGjOyKpCnsnYQg7YS064ukITwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209Ik9TUyIgZGF0YS10bz0iREVWIiBkYXRhLWxhYmVsPSLslYTrrLQg7J2Y7IusIOyXhuydtArsoJXsg4Eg67aA7ZKI7J24IOykhCDslYzqs6Ag7KGw66a9Ij4KICA8cmVjdCB4PSI2NDMuNjg4IiB5PSI4Ny45IiB3aWR0aD0iMTQzLjU3ODAwMDAwMDAwMDAzIiBoZWlnaHQ9IjQ0LjYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNzE1LjQ3NyIgeT0iMTEwLjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSI3MTUuNDc3IiBkeT0iLTMuMzAwMDAwMDAwMDAwMDAwNyI+7JWE66y0IOydmOyLrCDsl4bsnbQ8L3RzcGFuPjx0c3BhbiB4PSI3MTUuNDc3IiBkeT0iMTQuMyI+7KCV7IOBIOu2gO2SiOyduCDspIQg7JWM6rOgIOyhsOumvTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkRFViIgZGF0YS10bz0iVEFSR0VUIiBkYXRhLWxhYmVsPSLsl4XrjbDsnbTtirgg67Cw7Y+sIj4KICA8cmVjdCB4PSIxMDIzLjE3OTAwMDAwMDAwMDEiIHk9Ijk0LjkiIHdpZHRoPSI5MC43MTIwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjEwNjguNTM1IiB5PSIxMTAuMDUwMDAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuyXheuNsOydtO2KuCDrsLDtj6w8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iU0JPTSIgZGF0YS10bz0iU0VBUkNIIiBkYXRhLWxhYmVsPSJMb2c0aiDtlbTtgrkg64m07IqkIOuwnOyDnSDsi5wiPgogIDxyZWN0IHg9IjEyODMuODExIiB5PSI0MTAuOTAwMDAwMDAwMDAwMSIgd2lkdGg9IjEzNS4yNjIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxMzUxLjQ0MiIgeT0iNDI2LjA1MDAwMDAwMDAwMDA3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5Mb2c0aiDtlbTtgrkg64m07IqkIOuwnOyDnSDsi5w8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iU0VBUkNIIiBkYXRhLXRvPSJQQVRDSCIgZGF0YS1sYWJlbD0iMey0iCDrp4zsl5Ag7Iud67OEIOuwjyDsobDsuZgiPgogIDxyZWN0IHg9IjEyOTAuMzExMDAwMDAwMDAwMSIgeT0iNTY0LjEiIHdpZHRoPSIxMjIuMTk0MDAwMDAwMDAwMDMiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxMzUxLjQwODAwMDAwMDAwMDEiIHk9IjU3OS4yNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+Mey0iCDrp4zsl5Ag7Iud67OEIOuwjyDsobDsuZg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkhBQ0tFUiIgZGF0YS1sYWJlbD0i7ZW07LukIPCfpbciIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg4LjIyNSIgd2lkdGg9Ijg4LjYzMyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxMDAuMzE2NDk5OTk5OTk5OTkiIHk9IjEwNi42NzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPu2VtOy7pCDwn6W3PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJPU1MiIGRhdGEtbGFiZWw9IuyYpO2UiOyGjOyKpCAvIOyZuOu2gCDrnbzsnbTruIzrn6zrpqwg8J+TpgrslYXshLHsvZTrk5wg7J2A64uJIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM2Ny4zMDEiIHk9Ijg0IiB3aWR0aD0iMjMyLjM4Njk5OTk5OTk5OTk3IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0ODMuNDk0NDk5OTk5OTk5OTYiIHk9IjExMC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0ODMuNDk0NDk5OTk5OTk5OTYiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7smKTtlIjshozsiqQgLyDsmbjrtoAg65287J2067iM65+s66asIPCfk6Y8L3RzcGFuPjx0c3BhbiB4PSI0ODMuNDk0NDk5OTk5OTk5OTYiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyVheyEsey9lOuTnCDsnYDri4k8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iREVWIiBkYXRhLWxhYmVsPSLquLDsl4Ug6rCc67Cc7YyAIPCfkrsK7IaM7ZSE7Yq47Juo7Ja0IOu5jOuTnCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI4MzEuMjY2MDAwMDAwMDAwMSIgeT0iODQiIHdpZHRoPSIxNDcuOTEzIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iOTA1LjIyMjUwMDAwMDAwMDEiIHk9IjExMC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI5MDUuMjIyNTAwMDAwMDAwMSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuq4sOyXhSDqsJzrsJztjIAg8J+SuzwvdHNwYW4+PHRzcGFuIHg9IjkwNS4yMjI1MDAwMDAwMDAxIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7shoztlITtirjsm6jslrQg67mM65OcPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlRBUkdFVCIgZGF0YS1sYWJlbD0i7YOA6rKfIOq4sOyXhSDsoITsgrDrp50g8J+SpQrsoITssrQg656c7ISs7Juo7Ja0IOqwkOyXvCEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTE1Ny44OTEiIHk9Ijg4LjIyNSIgd2lkdGg9IjE2Ny45MiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxMjQxLjg1MSIgeT0iMTE1LjEyNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTI0MS44NTEiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7tg4Dqsp8g6riw7JeFIOyghOyCsOunnSDwn5KlPC90c3Bhbj48dHNwYW4geD0iMTI0MS44NTEiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyghOyytCDrnpzshKzsm6jslrQg6rCQ7Je8ITwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTQk9NIiBkYXRhLWxhYmVsPSLinKggU0JPTSA6IOyGjO2UhO2KuOybqOyWtCDshLHrtoQg66qF7IS47IScIPCfk5wK7IKs7Jqp65CcIOuqqOuToCDsmKTtlIjshozsiqTsnZgg7J2066aELCDrsoTsoIQsIOy2nOyymCAxMDAlIOq4sOuhnSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMTczLjM3MzUwMDAwMDAwMDEiIHk9IjMxNC4xIiB3aWR0aD0iMzU2Ljg3NDk5OTk5OTk5OTkiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTM1MS44MTEwMDAwMDAwMDAxIiB5PSIzNDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjEzNTEuODExMDAwMDAwMDAwMSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuKcqCBTQk9NIDog7IaM7ZSE7Yq47Juo7Ja0IOyEseu2hCDrqoXshLjshJwg8J+TnDwvdHNwYW4+PHRzcGFuIHg9IjEzNTEuODExMDAwMDAwMDAwMSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7IKs7Jqp65CcIOuqqOuToCDsmKTtlIjshozsiqTsnZgg7J2066aELCDrsoTsoIQsIOy2nOyymCAxMDAlIOq4sOuhnTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTRUFSQ0giIGRhdGEtbGFiZWw9IuyasOumrCDtmozsgqwg7ISx67aE7ZGcKFNCT00pIOymieyLnCDqsoDsg4kg8J+UjiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMjEzLjc1OCIgeT0iNDg0LjIwMDAwMDAwMDAwMDA1IiB3aWR0aD0iMjc2LjEwNiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTM1MS44MTEwMDAwMDAwMDAxIiB5PSI1MDIuNjUwMDAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyasOumrCDtmozsgqwg7ISx67aE7ZGcKFNCT00pIOymieyLnCDqsoDsg4kg8J+UjjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUEFUQ0giIGRhdGEtbGFiZWw9Iuy3qOyVve2VnCDrtoDtkogo67KE7KCEKSDsg4nstpwg7ZuEIOymieqwgSDtjKjsuZgg8J+boe+4jyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMjA1LjYwNyIgeT0iNjM3LjQwMDAwMDAwMDAwMDEiIHdpZHRoPSIyOTIuNDA4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjEzNTEuODExIiB5PSI2NTUuODUwMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7Leo7JW97ZWcIOu2gO2SiCjrsoTsoIQpIOyDiey2nCDtm4Qg7KaJ6rCBIO2MqOy5mCDwn5uh77iPPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 기존 보안 한계 vs SBOM의 전격 도입 효과 비교 해부 (3단 표)**

왜 기존의 보안 스캐너로는 막을 수 없고 **'투명한 명세서(SBOM)'** 체계가 필요한지를 대조하는 것이 핵심입니다.

| **핵심 척도 (비교 잣대)**                  | **❌ 기존 보안의 한계 (SBOM 부재 시)**                                                                                            | **📜 차세대 방어 체계 (SBOM 도입 시) 🚨**                                                                                   |
| :--------------------------------- | :--------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------- |
| **소프트웨어 내부 구성의 가시성(Visibility)**   | **'깜깜이 블랙박스'.** 완성된 앱(App) 안에 개발자가 인터넷에서 긁어온 어떤 오픈소스가 몇 버전으로 섞여 있는지 관리자나 보안팀이 전혀 알 길이 없음.                              | **'100% 투명한 유리 상자'.** 식품 뒷면의 성분표처럼, 소프트웨어 뼈대를 구성하는 1만 개의 오픈소스 **트리(Tree, 의존성 관계)가 투명하게 기록 및 관리됨.**                |
| **치명적 취약점(Log4j 등) 발생 시 초동 대응 속도** | **'전수 조사로 인한 골든타임 증발'.** 뉴스에서 취약점이 터지면, 우리 회사 수백 대의 서버를 일일이 스캐닝하며 "여기 혹시 Log4j 있나?" 하고 수작업으로 찾느라 며칠이 소요됨 (그 사이에 해킹당함). | **'SBOM 명세서 검색으로 1초 만에 색출 💯'.** 중앙화된 SBOM 관리 시스템에 취약점 버전을 검색만 하면, **해당 부품이 사용된 서버 목록이 즉시 도출되어 1시간 내에 패치가 가능해짐.** |
| **오픈소스 라이선스 법적 분쟁(컴플라이언스)**        | 개발자가 무단으로 GPL 라이선스 코드를 갖다 써서, 나중에 회사 기밀 소스코드를 강제로 공개해야 하는 끔찍한 법적 분쟁에 휘말림.                                              | SBOM에 각 부품의 **라이선스(GPL, MIT 등) 정보가 명확히 기재**되므로, 법적 충돌 위험을 배포 전에 사전에 차단함.                                          |
| **글로벌 표준 데이터 포맷 (어떻게 작성하는가?)**     | 통일된 양식이 없어 엑셀로 대충 관리함.                                                                                                 | 전 세계 시스템이 기계적으로 읽고 공유할 수 있도록 **SPDX(리눅스 재단), CycloneDX(OWASP)** 같은 표준화된 데이터 포맷을 사용함.                              |

#### **IV. \[결론/제언] 제로 트러스트(Zero Trust)와 DevSecOps 파이프라인의 완성**

* **(키워드 위주 2줄 마무리)** "SBOM은 단순히 목록을 적어두는 엑셀 파일이 아닙니다. 소프트웨어 개발 주기(SDLC)에 보안을 내재화하는 **DevSecOps 파이프라인 안에서 CI/CD 과정 중 SBOM 생성을 100% 자동화**해야 하며, 외부에서 들어온 코드는 무조건 의심하고 검증하는 **'제로 트러스트(Zero Trust)' 아키텍처의 필수 기반 데이터로 활용되어야 합니다.**"
