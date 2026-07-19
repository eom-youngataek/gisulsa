### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (사이버대피소정의, 등장배경) — 3~4줄
Ⅱ. 동작원리 - 트래픽우회 (본론①, 도식 1개 필수)
Ⅲ. 이용절차및제공기능 (본론②, 핵심 배점)
Ⅳ. 한계및확장(안심존 등)
Ⅴ. 결론
```

### Ⅰ. 개요

앞서다룬DDoS답안에서 \*\*"31.4Tbps급공격을견디려면 449Tbps급네트워크용량이필요하다"\*\*고했는데, 이런방어력을 **중소기업·소상공인이자체적으로갖추는건불가능**합니다. **KISA(한국인터넷진흥원)가무료로제공하는DDoS방어인프라**가바로사이버대피소입니다.

### Ⅱ. 동작원리 — 트래픽우회

| 단계         | 내용                              |
| :--------- | :------------------------------ |
| **DNS변경**  | 공격받는웹사이트의 **도메인을KISA대피소의IP로변경** |
| **대피소경유**  | 모든트래픽이 **KISA의대용량인프라를통과**       |
| **필터링**    | 대피소에서 **공격트래픽을걸러내고**, 정상트래픽만    |
| **정상서버전달** | 걸러진 **정상트래픽만원래서버로전달**           |

→ 암기: **"주소를대피소로바꿔서, 공격은거기서다맞고, 정상요청만골라서돌려보낸다"** — 앞서다룬 \*\*"리버스프록시"\*\*의원리가, 국가차원의 **긴급방어서비스**로확장된형태입니다.

### 도식화 제안

```
[정상시]  사용자 → 원래서버(직접)

[공격시]
사용자 → [DNS변경] → [KISA사이버대피소]
                          ↓ 필터링(공격트래픽차단)
                     [원래서버] (정상트래픽만수신)
```

### Ⅲ. 이용절차및제공기능 — 핵심 배점

| 항목        | 내용                                                               |
| :-------- | :--------------------------------------------------------------- |
| **대상**    | **중소기업,소상공인**(자체DDoS방어인프라가없는곳)                                   |
| **비용**    | **무료**(국가예산으로운영)                                                 |
| **신청**    | KISA **보호나라**사이트를통해 **사전신청·등록** — 공격당한후신청하면대응이늦어질수있어 **사전가입이핵심** |
| **부가서비스** | 웹방화벽,**안심존**(변조탐지)등 함께제공하는경우있음                                   |

→ 암기: **"미리가입해둬야, 공격왔을때바로대피소로숨을수있다"** — 앞서다룬 \*\*"CTEM"\*\*의 \*\*"사전대비"\*\*철학과같은맥락: 사고가난뒤대응책을찾는게아니라, **미리등록해두는것**이핵심입니다.

### Ⅳ. 한계및확장

| 한계          | 내용                                                                                                      |
| :---------- | :------------------------------------------------------------------------------------------------------ |
| **트래픽제한**   | 무료서비스이므로 **초대형(Tbps급)공격**은완전방어가어려울수있음— 앞서다룬 **31.4Tbps급공격**같은 규모에는 \*\*상용DDoS방어서비스(Cloudflare등)\*\*가더적합 |
| **DNS전환지연** | 공격 **발생후신청**하면 DNS전파시간동안 **일부피해불가피**                                                                    |
| **연계서비스**   | **웹방화벽서비스**등 KISA가함께제공하는 다른무료보안서비스와 **병행이용권장**                                                          |

### Ⅴ. 결론

사이버대피소는 \*\*"자체DDoS방어인프라를갖추기어려운중소기업을위해, 국가가대신방어자원을제공하는공공안전망"\*\*입니다. 앞서다룬 \*\*"DDoS공격의비대칭성(공격자:방어자비용비율1:3,000)"\*\*을고려하면, 이런 **공적방어인프라의존재자체가중소기업생태계의생존에필수적**이라는걸알수있습니다. 다만 최근처럼 **Tbps급공격이일상화**되는추세에서는, 사전등록과 함께 **상용CDN/방어서비스와의병행**도고려해야합니다.


**1. 답안 전개 스토리 (암기 직결 숏폼)**

> "동네의 작은 빵집(중소기업 웹 서버)에 1만 명의 깡패(DDoS 좀비 PC)가 한꺼번에 몰려오면 빵집 앞 도로는 꽉 막히고 영업은 그날로 끝장난다. 빵집 사장님이 문 앞에 작은 경호원(방화벽)을 세워봤자 1만 명의 융단폭격 앞에서는 무용지물이다. 이때 국가(KISA)나 클라우드 기업이 만들어둔 거대한 방어 요새가 바로 \*\*'DDoS 사이버 대피소(Scrubbing Center, 정제 센터)'\*\*다. 작동 방식은 기가 막힌다. 빵집 사장님은 공격이 시작되면 네비게이션(DNS 주소)을 조작하여, 빵집으로 향하던 트래픽을 거대한 '사이버 대피소' 쪽으로 확 꺾어버린다. 그러면 1만 명의 깡패와 진짜 손님 10명이 모두 사이버 대피소로 몰려간다. 대피소에 구축된 막강한 방어 시스템은 1만 명의 깡패 쓰레기 트래픽은 그 자리에서 걸러내어(Scrubbing, 정제/세척) 폐기하고, 진짜 손님 10명만 안전한 비밀 통로(터널링)를 통해 원래 빵집으로 무사히 배달해 준다. 기업은 수억 원짜리 방어 장비를 사지 않고도 서버 다운(가용성 파괴)을 완벽하게 막아내는 것이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 거대한 트래픽 세탁기, DDoS 사이버 대피소 개요**

* **정의:** 중소기업이나 일반 인프라가 감당할 수 없는 대규모 DDoS 공격이 발생했을 때, 타겟으로 향하는 트래픽을 외부의 거대한 방어 센터로 우회시켜 **악성 트래픽은 필터링(세척)하고 정상 트래픽만 원본 서버로 전달해 주는 '트래픽 정제소(Scrubbing Center)'**.
* **운영 체계:** 국내에서는 KISA(한국인터넷진흥원)가 중소기업을 위해 무료 사이버 대피소를 운영 중이며, 민간에서는 Cloudflare, AWS(Shield) 같은 거대 CDN 클라우드 기업들이 글로벌 규모로 제공함.

#### **II. \[본론 1] (단순화 버전) 쓰레기를 걸러내는 사이버 대피소 우회 파이프라인 (도식화)**

공격이 발생했을 때 트래픽의 방향이 어떻게 꺾이고 정제되는지를 직관적으로 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDc1LjQyOSA1NDkuNDAwMDAwMDAwMDAwMSIgd2lkdGg9IjEwNzUuNDI5IiBoZWlnaHQ9IjU0OS40MDAwMDAwMDAwMDAxIiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJERG9TX19fU2NydWJiaW5nX0NlbnRlcl9fIiBkYXRhLWxhYmVsPSJERG9TIOyCrOydtOuyhCDrjIDtlLzshowgKFNjcnViYmluZyBDZW50ZXIpIOyekeuPmSDrqZTsu6Tri4jsppgiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9Ijk2Ny40MjkwMDAwMDAwMDAxIiBoZWlnaHQ9IjQ2MS40MDAwMDAwMDAwMDAwMyIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9Ijk2Ny40MjkwMDAwMDAwMDAxIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+RERvUyDsgqzsnbTrsoQg64yA7ZS87IaMIChTY3J1YmJpbmcgQ2VudGVyKSDsnpHrj5kg66mU7Luk64uI7KaYPC90ZXh0Pgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9fX1NjcnViYmluZ19DZW50ZXJfIiBkYXRhLWxhYmVsPSLqsbDrjIAg7IKs7J2067KEIOuMgO2UvOyGjCAoU2NydWJiaW5nIENlbnRlcikg7J247ZSE6528Ij4KICA8cmVjdCB4PSI2NiIgeT0iMTk3LjgiIHdpZHRoPSI1NzkuODEzMDAwMDAwMDAwMSIgaGVpZ2h0PSIxNjEuOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjY2IiB5PSIxOTcuOCIgd2lkdGg9IjU3OS44MTMwMDAwMDAwMDAxIiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI3OCIgeT0iMjExLjgiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+6rGw64yAIOyCrOydtOuyhCDrjIDtlLzshowgKFNjcnViYmluZyBDZW50ZXIpIOyduO2UhOudvDwvdGV4dD4KPC9nPgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJETlMiIGRhdGEtdG89IlNIRUxURVIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjk0LjQwNjUwMDAwMDAwMDA1LDQ1Mi45NSAyOTQuNDA2NTAwMDAwMDAwMDUsNDczLjQwMDAwMDAwMDAwMDAzIDI3MS43NTAwMDAwMDAwMDAwNiw0NzMuNDAwMDAwMDAwMDAwMDMgMjcxLjc1MDAwMDAwMDAwMDA2LDUwMS40MDAwMDAwMDAwMDAwMyAxMDI3LjQyOSw1MDEuNDAwMDAwMDAwMDAwMDMgMTAyNy40MjksNDMzLjQwMDAwMDAwMDAwMDAzIDIzMS43NTAwMDAwMDAwMDAwNiw0MzMuNDAwMDAwMDAwMDAwMDMgMTYsNDMzLjQwMDAwMDAwMDAwMDAzIDE2LDI1Mi43MDAwMDAwMDAwMDAwMiAyNiwyNTIuNzAwMDAwMDAwMDAwMDIgMTAyNy40MjksMjUyLjcwMDAwMDAwMDAwMDAyIDEwMjcuNDI5LDI5Mi43MDAwMDAwMDAwMDAwNSA4MiwyOTIuNzAwMDAwMDAwMDAwMDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkNMRUFOIiBkYXRhLXRvPSJPUklHSU4iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjQuIOyViOyghO2VnCDruYTrsIAg7Ya166GcIChHUkUg7YSw64SQ66eBL+2UhOuhneyLnCkiIHBvaW50cz0iNjI5LjgxMzAwMDAwMDAwMDEsMzI1LjE1MDAwMDAwMDAwMDAzIDY0NS44MTMwMDAwMDAwMDAxLDMyNS4xNTAwMDAwMDAwMDAwMyAyMCwzMjUuMTUwMDAwMDAwMDAwMDMgMjAsMjg1LjE1MDAwMDAwMDAwMDAzIDYxNS44MTMwMDAwMDAwMDAxLDI4NS4xNTAwMDAwMDAwMDAwMyA2MTUuODEzMDAwMDAwMDAwMSw0MzMuNDAwMDAwMDAwMDAwMDMgNzMzLjExOTUwMDAwMDAwMDEsNDMzLjQwMDAwMDAwMDAwMDAzIDczMy4xMTk1MDAwMDAwMDAxLDQ2MS40MDAwMDAwMDAwMDAwMyAyMCw0NjEuNDAwMDAwMDAwMDAwMDMgMjAsNDczLjQwMDAwMDAwMDAwMDAzIDc3My4xMTk1MDAwMDAwMDAxLDQ3My40MDAwMDAwMDAwMDAwMyA4OTAuNDI2MDAwMDAwMDAwMiw0NzMuNDAwMDAwMDAwMDAwMDMgODkwLjQyNjAwMDAwMDAwMDIsNDY5Ljg1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTSEVMVEVSIiBkYXRhLXRvPSJEUk9QIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIyLiDsk7DroIjquLAg7Yq4656Y7ZS9IO2PkOq4sCEiIHBvaW50cz0iMTg2LjE5NDAwMDAwMDAwMDAyLDI4Ni41NSAxOTguMTk0MDAwMDAwMDAwMDIsMjg2LjU1IDE5OC4xOTQwMDAwMDAwMDAwMiwyNjAuMjUgNDcwLjA0NDAwMDAwMDAwMDA0LDI2MC4yNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iU0hFTFRFUiIgZGF0YS10bz0iQ0xFQU4iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjMuIOygleyDgSDtirjrnpjtlL3rp4wg7IK066Ck64OEIChTY3J1YmJpbmcpIiBwb2ludHM9IjE4Ni4xOTQwMDAwMDAwMDAwMiwyOTguODUgMTk4LjE5NDAwMDAwMDAwMDAyLDI5OC44NSAxOTguMTk0MDAwMDAwMDAwMDIsMzI1LjE1MDAwMDAwMDAwMDAzIDQ3MC4wNDQwMDAwMDAwMDAwNCwzMjUuMTUwMDAwMDAwMDAwMDMiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQ0xFQU4iIGRhdGEtdG89Ik9SSUdJTiIgZGF0YS1sYWJlbD0iNC4g7JWI7KCE7ZWcIOu5hOuwgCDthrXroZwgKEdSRSDthLDrhJDrp4Ev7ZSE66Gd7IucKSI+CiAgPHJlY3QgeD0iNjA1LjEzMjk5OTk5OTk5OTgiIHk9IjQ0Ni4yNTAwMDAwMDAwMDAwNiIgd2lkdGg9IjIxOS42MSIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjcxNC45Mzc5OTk5OTk5OTk5IiB5PSI0NjEuNDAwMDAwMDAwMDAwMDMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjQuIOyViOyghO2VnCDruYTrsIAg7Ya166GcIChHUkUg7YSw64SQ66eBL+2UhOuhneyLnCk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iU0hFTFRFUiIgZGF0YS10bz0iRFJPUCIgZGF0YS1sYWJlbD0iMi4g7JOw66CI6riwIO2KuOuemO2UvSDtj5DquLAhIj4KICA8cmVjdCB4PSIyNjMuNzU1IiB5PSIyNDQuMjUwMDAwMDAwMDAwMDMiIHdpZHRoPSIxMjguNzI4IiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzI4LjExOSIgeT0iMjU5LjQwMDAwMDAwMDAwMDAzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij4yLiDsk7DroIjquLAg7Yq4656Y7ZS9IO2PkOq4sCE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iU0hFTFRFUiIgZGF0YS10bz0iQ0xFQU4iIGRhdGEtbGFiZWw9IjMuIOygleyDgSDtirjrnpjtlL3rp4wg7IK066Ck64OEIChTY3J1YmJpbmcpIj4KICA8cmVjdCB4PSIyMzAuMTk0MDAwMDAwMDAwMDIiIHk9IjMwOS4xNTAwMDAwMDAwMDAwMyIgd2lkdGg9IjE5NS44NTAwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjMyOC4xMTkiIHk9IjMyNC4zIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij4zLiDsoJXsg4Eg7Yq4656Y7ZS966eMIOyCtOugpOuDhCAoU2NydWJiaW5nKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQVRUQUNLIiBkYXRhLWxhYmVsPSJERG9TIOyigOu5hCDqtbDri6gg8J+RviArIOygleyDgSDsnKDsoIAg8J+nkSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSIyNDcuMjA3IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNzkuNjAzNSIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5ERG9TIOyigOu5hCDqtbDri6gg8J+RviArIOygleyDgSDsnKDsoIAg8J+nkTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRE5TIiBkYXRhLWxhYmVsPSJETlMiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjYwLjA5MzUwMDAwMDAwMDA2IiB5PSI0MTYuMDUiIHdpZHRoPSI2OC42MjU5OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIyOTQuNDA2NTAwMDAwMDAwMDUiIHk9IjQzNC41IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5ETlM8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlNIRUxURVIiIGRhdGEtbGFiZWw9IlNIRUxURVIiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9IjE0MC45IiB3aWR0aD0iMTA0LjE5NCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxMDguMDk3MDAwMDAwMDAwMDEiIHk9IjE1OS4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+U0hFTFRFUjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iT1JJR0lOIiBkYXRhLWxhYmVsPSLquLDsl4XsnZgg7JuQ656YIOybuSDshJzrsoQg8J+PogrshJzrsoQg64uk7Jq0IOyXhuydtCDsoJXsg4Eg7JiB7JeFISIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3ODkuNDIzMDAwMDAwMDAwMSIgeT0iNDE2LjA1IiB3aWR0aD0iMjAyLjAwNTk5OTk5OTk5OTk3IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9Ijg5MC40MjYwMDAwMDAwMDAyIiB5PSI0NDIuOTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9Ijg5MC40MjYwMDAwMDAwMDAyIiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+6riw7JeF7J2YIOybkOuemCDsm7kg7ISc67KEIPCfj6I8L3RzcGFuPjx0c3BhbiB4PSI4OTAuNDI2MDAwMDAwMDAwMiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7ISc67KEIOuLpOyatCDsl4bsnbQg7KCV7IOBIOyYgeyXhSE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iU0hFTFRFUiIgZGF0YS1sYWJlbD0iU0hFTFRFUiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI4MiIgeT0iMjc0LjI1IiB3aWR0aD0iMTA0LjE5NCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxMzQuMDk3IiB5PSIyOTIuNyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+U0hFTFRFUjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRFJPUCIgZGF0YS1sYWJlbD0i7JWF7ISxIO2MqO2CtyDrsoTrprwg4p2MIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQ3MC4wNDQwMDAwMDAwMDAwNCIgeT0iMjQxLjgiIHdpZHRoPSIxNTIuMzU5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1NDYuMjIzNTAwMDAwMDAwMSIgeT0iMjYwLjI1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7slYXshLEg7Yyo7YK3IOuyhOumvCDinYw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkNMRUFOIiBkYXRhLWxhYmVsPSLquajrgZftlZwg7KCV7IOBIO2MqO2CtyDwn5+iIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQ3MC4wNDQwMDAwMDAwMDAwNCIgeT0iMzA2LjcwMDAwMDAwMDAwMDA1IiB3aWR0aD0iMTU5Ljc2OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNTQ5LjkyODUiIHk9IjMyNS4xNTAwMDAwMDAwMDAwMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+6rmo64GX7ZWcIOygleyDgSDtjKjtgrcg8J+fojwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 사내 자체 방어(On-Premise) vs 외부 사이버 대피소 방어 전격 비교 (3단 표)**

왜 기업의 방화벽으로는 막을 수 없고, 반드시 **'네트워크 밖에서(우회하여)'** 걸러내야 하는지를 대조하는 것이 핵심입니다.

| **핵심 척도 (비교 잣대)**                  | **🧱 자체 방어 (기업 내 방화벽 / Anti-DDoS 장비)**                                                                             | **🛡️ 외부 사이버 대피소 (KISA / Cloudflare)**                                                           |
| :--------------------------------- | :----------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| **대규모 대역폭 고갈 (Volume) 공격 방어력**     | **'회선(파이프) 자체가 막혀버림 (방어 불가)'.** 아무리 방화벽 성능이 좋아도, 회사 앞 도로(인터넷 회선) 10Gbps 대역폭 자체가 100Gbps 공격에 가득 차버리므로 100% 서버가 다운됨. | **'거대한 인프라로 무제한 흡수 (방어 성공)'.** 테라급(Tbps) 트래픽을 모두 수용할 수 있는 초거대 네트워크망과 대피소 클러스터를 통해 트래픽을 가뿐히 빨아들임. |
| **트래픽 우회(Redirection) 방식 및 작동 원리** | 꺾을 필요 없이 그냥 앞단에서 차단함. (In-line 방식).                                                                                | 공격 발생 시 10분 내에 **'DNS 레코드(A Record)'를 대피소 IP로 변경**하거나, **BGP 라우팅을 조작**하여 트래픽의 물줄기를 대피소로 꺾음.      |
| **정제(Scrubbing) 후 정상 패킷 전달 방식**    | -                                                                                                                  | 대피소에서 깨끗하게 씻어낸 정상 트래픽만 \*\*'GRE 터널링'\*\*이나 \*\*'리버스 프록시(Reverse Proxy)'\*\*를 통해 원래 기업 서버로 배달함.   |
| **도입 비용 및 타겟**                     | 대기업 중심. 장비 구축에 수억\~수십억 원이 듬.                                                                                       | 중소기업 특화. **(KISA 사이버 대피소는 신청 시 전액 무료 서비스 제공)**. 장비 구매 비용 0원.                                     |

#### **IV. \[결론/제언] CDN(클라우드 딜리버리 네트워크)과 결합한 상시 대피소(Always-On)의 대중화**

* **(키워드 위주 2줄 마무리)** "과거 사이버 대피소는 공격이 터진 후에야 DNS를 꺾어 대응하는 사후 약방문(On-Demand) 방식이 많아 초동 대처에 10분의 공백이 발생했습니다. 오늘날에는 글로벌 CDN(클라우드플레어, 아카마이 등)을 활용하여 **평상시에도 모든 트래픽이 대피소(클라우드 엣지)를 거쳐 가도록 설계하는 상시 방어(Always-On) 아키텍처로 진화하며 가용성을 극한으로 끌어올리고 있습니다.**"
