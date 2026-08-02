### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (세경계선긋기의필요성) — 3~4줄
Ⅱ. 서브네팅 계산법 (본론①, 도식 1개 필수)
Ⅲ. VLSM - 크기가다른서브넷나누기 (본론②, 핵심 배점)
Ⅳ. 슈퍼네팅 및종합비교
Ⅴ. 결론
```

### Ⅰ. 개요

앞서다룬 **IP주소구조**에서 \*\*"네트워크부분/호스트부분"\*\*의 경계는 **고정된게아니라, 조직의필요에따라움직일수있습니다** — **서브네팅**은 **"하나의큰네트워크를여러개의작은네트워크로쪼개는것"**, **슈퍼네팅**은 반대로 **"여러작은네트워크를하나의큰단위로합치는것"**, **VLSM**은 그쪼갤때 **"크기를균등하지않게,필요한만큼씩쪼개는"** 정교한기법입니다.

### Ⅱ. 서브네팅 계산법

**기본공식**

| 항목              | 공식                                      |
| :-------------- | :-------------------------------------- |
| **서브넷개수**       | 2^(빌려온비트수)                              |
| **호스트개수**(서브넷당) | 2^(남은호스트비트수) **- 2**(네트워크주소,브로드캐스트주소제외) |

**계산예시**: `192.168.1.0/24`를 **4개서브넷**으로나누기

```
필요서브넷: 4개 → 2^n≥4 → n=2(비트2개필요)
     ↓
/24 → /26 (24+2=26)
     ↓
[서브넷마스크] 255.255.255.192 (11111111.11111111.11111111.11000000)
     ↓
호스트비트 = 32-26 = 6비트 → 호스트수 = 2^6-2 = 62개(서브넷당)
```

| 서브넷 | 네트워크주소               | 사용가능호스트범위  | 브로드캐스트 |
| :-- | :------------------- | :--------- | :----- |
| 1   | 192.168.1.**0**/26   | .1\~.62    | .63    |
| 2   | 192.168.1.**64**/26  | .65\~.126  | .127   |
| 3   | 192.168.1.**128**/26 | .129\~.190 | .191   |
| 4   | 192.168.1.**192**/26 | .193\~.254 | .255   |

→ 암기: **"필요한개수만큼2의거듭제곱으로비트를빌려오고, 남은비트로호스트수를계산한다"**

### 도식화 제안

```
[192.168.1.0/24] 원래네트워크(256개주소)
        ↓ 2비트를 호스트에서네트워크로이동(/24→/26)
┌────────┬────────┬────────┬────────┐
[서브넷1]  [서브넷2]  [서브넷3]  [서브넷4]
.0~.63    .64~.127  .128~.191 .192~.255
(각64개,실사용62개)
```

### Ⅲ. VLSM — 크기가다른서브넷나누기, 핵심 배점

**함정 방지: "똑같이나눈다"고만답하면절반. 부서마다필요호스트수가다를때, 어떻게낭비없이나누는지보여줘야완성됩니다.**

**시나리오**: `192.168.1.0/24`를 \*\*영업부(100명),개발부(50명),인사부(20명),서버실(2대)\*\*에할당

| 단계               | 원리                                              |
| :--------------- | :---------------------------------------------- |
| **①큰것부터먼저할당**    | 필요호스트수가 **가장많은부서부터** 순서대로배정(작은게먼저면 큰덩어리를못찾을수있음) |
| **②각부서에딱맞는크기부여** | 필요호스트수를 **초과하는최소한의블록**만할당(낭비최소화)                |

```
영업부(100명필요) → 2^n-2≥100 → n=7 → /25 사용(126개호스트)
   192.168.1.0/25 (0~127, 126개사용가능)

개발부(50명필요) → 2^n-2≥50 → n=6 → /26 사용(62개호스트)
   192.168.1.128/26 (128~191)

인사부(20명필요) → 2^n-2≥20 → n=5 → /27 사용(30개호스트)
   192.168.1.192/27 (192~223)

서버실(2대필요) → 2^n-2≥2 → n=2 → /30 사용(2개호스트)
   192.168.1.224/30 (224~227)
```

→ 암기: **"큰부서먼저,딱맞는만큼만할당"** — 앞서다룬 \*\*"서브네팅(균등분할)"\*\*과의핵심차이: **VLSM은 "가변길이(VariableLength)"** — 서브넷마다 **마스크길이가서로다르게** 설정됩니다.

### 도식화 제안

```
[VLSM 할당 - 크기가다른블록]
[영업부/25: 126개] [개발부/26: 62개] [인사부/27: 30개] [서버실/30: 2개]
큰블록먼저 → → → → → → → → → → → → → → → 작은블록나중(낭비최소화)
```

### Ⅳ. 슈퍼네팅 및 종합비교

**함정 방지: "합친다"고만답하면절반. 라우팅테이블효율화라는 실질적목적을보여줘야완성됩니다.**

**슈퍼네팅**: 여러개의 **작은네트워크를하나의큰경로로묶어**, 라우터가 **라우팅테이블항목을줄이는것**(CIDR의핵심원리)

```
192.168.0.0/24
192.168.1.0/24  → 이4개를 하나로묶으면
192.168.2.0/24
192.168.3.0/24
     ↓
192.168.0.0/22 (하나의라우팅항목으로표현, /24가4개모인것과동일)
```

→ 암기: **"서브네팅은쪼개서세밀하게관리,슈퍼네팅은합쳐서라우팅테이블을가볍게"**

| 구분     | **서브네팅**   | **VLSM**         | **슈퍼네팅**  |
| :----- | :--------- | :--------------- | :-------- |
| **방향** | 큰것→작은것(균등) | 큰것→작은것(**비균등**)  | 작은것→큰것    |
| **목적** | 네트워크분할·관리  | **호스트수맞춤,낭비최소화** | 라우팅테이블효율화 |

### Ⅴ. 결론

서브네팅·VLSM·슈퍼네팅은 모두 \*\*"네트워크/호스트경계선을 어디에그을지"\*\*를 다루는 동일한계산원리(2의거듭제곱)를 **서로다른목적**으로 적용한것입니다 — 서브네팅은 **균등분할**, VLSM은 **필요에맞춘비균등분할(낭비최소화)**, 슈퍼네팅은 **여러조각을합쳐라우팅효율화**를 추구합니다 — 이는 앞서다룬 \*\*IP주소구조(네트워크부분/호스트부분)\*\*의 경계가 **고정된것이아니라, 조직의필요에따라유연하게재설계**될수있다는 것을 실전계산으로 보여줍니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "IPv4 주소는 고갈되어 가는 금싸라기 땅이다. 낭비 없이 알뜰하게 쓰려면 칼질(쪼개기)과 합치기 기술이 필수다. 첫째, \*\*'서브네팅(Subnetting)'\*\*은 큰 땅(네트워크)을 작은 블록으로 쪼개는 기술이다. 256명이 사는 큰 아파트 단지를 64명씩 4개의 구역으로 쪼개어, 브로드캐스트(아파트 방송 소음) 구역을 분리하고 IP 낭비를 막는다. 둘째, \*\*'슈퍼네팅(Supernetting)'\*\*은 반대로 자잘한 땅들을 모아 하나의 거대한 블록으로 합치는 기술이다. 라우터(내비게이션)에 작은 주소를 일일이 다 적으면 메모리가 터지므로, 여러 주소를 묶어 하나의 큰 이정표로 퉁쳐서 적는(경로 요약) 마법이다. 셋째, 서브네팅의 끝판왕 \*\*'VLSM'\*\*이다. 기존에는 무조건 64명씩 '똑같은 크기'로만 땅을 잘라야 해서 인원이 적은 팀은 땅이 남아돌았다. VLSM은 각 부서 인원수에 딱 맞게 '서로 다른 크기'로 땅을 자유자재로 잘라 나눠주는 궁극의 알뜰 재단 기술이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] IP 주소 고갈을 막는 네트워크 재단 기술 개요**

* **핵심 목적:** IPv4 클래스(A/B/C) 체계의 고정된 크기 할당으로 인해 발생하는 막대한 IP 낭비를 막고, 라우팅 테이블(이정표)의 크기를 줄여 네트워크 전송 효율을 극대화하기 위함.
* **동작의 본질 (비트 빌려오기):** 서브넷 마스크(Subnet Mask)의 비트를 이동시켜, 네트워크 부분(동)과 호스트 부분(호수)의 경계를 자유롭게 조절하는 논리적 쪼개기/합치기 기법.

#### **II. \[본론 1] (극단적 단순화 버전) 쪼개고 합치고 다르게 자르는 3대 기술 (도식화)**

복잡한 수식과 선을 빼고, **큰 빵을 어떻게 조작하는지**에 대한 직관적 그림만 그렸습니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NTIuNTcyOTk5OTk5OTk5OSAzNDEuNDAwMDAwMDAwMDAwMDMiIHdpZHRoPSI0NTIuNTcyOTk5OTk5OTk5OSIgaGVpZ2h0PSIzNDEuNDAwMDAwMDAwMDAwMDMiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IklQX19fX18zX18iIGRhdGEtbGFiZWw9IklQIOyjvOyGjCDtmqjsnKgg6re564yA7ZmU66W8IOychO2VnCAz64yAIOyerOuLqCDquLDsiKAiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjM3Mi41NzI5OTk5OTk5OTk5IiBoZWlnaHQ9IjI2MS40MDAwMDAwMDAwMDAwMyIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjM3Mi41NzI5OTk5OTk5OTk5IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+SVAg7KO87IaMIO2aqOycqCDqt7nrjIDtmZTrpbwg7JyE7ZWcIDPrjIAg7J6s64uoIOq4sOyIoDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzEiIGRhdGEtbGFiZWw9IjEuIOyEnOu4jOuEpO2MhSAoU3VibmV0dGluZykg8J+UqgrtgbAg67m1IDHqsJzrpbwg4p6UIOuYkeqwmeydgCDtgazquLDsnZgg7J6R7J2AIOu5tSA06rCc66GcIOyqvOqwrCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iMTU3LjgiIHdpZHRoPSIzMzkuMDkxIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjIyNS41NDU1IiB5PSIxODQuNzAwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjIyNS41NDU1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+MS4g7ISc67iM64Sk7YyFIChTdWJuZXR0aW5nKSDwn5SqPC90c3Bhbj48dHNwYW4geD0iMjI1LjU0NTUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPu2BsCDrubUgMeqwnOulvCDinpQg65iR6rCZ7J2AIO2BrOq4sOydmCDsnpHsnYAg67m1IDTqsJzroZwg7Kq86rCsPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlMyIiBkYXRhLWxhYmVsPSIyLiDsiojtjbzrhKTtjIUgKFN1cGVybmV0dGluZykg8J+knQrsnpHsnYAg67m1IDTqsJzrpbwg4p6UIOqxsOuMgO2VnCDrubUgMeqwnOuhnCDtlansuaggKOyalOyVvSkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMzE0LjYzOCIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjEzLjMxOSIgeT0iMTEwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjIxMy4zMTkiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj4yLiDsiojtjbzrhKTtjIUgKFN1cGVybmV0dGluZykg8J+knTwvdHNwYW4+PHRzcGFuIHg9IjIxMy4zMTkiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyekeydgCDrubUgNOqwnOulvCDinpQg6rGw64yA7ZWcIOu5tSAx6rCc66GcIO2Vqey5qCAo7JqU7JW9KTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTMyIgZGF0YS1sYWJlbD0iMy4gVkxTTSAo6rCA67OAIOq4uOydtCDsnqzri6gpIOKcqArtgbAg67m1IDHqsJzrpbwg4p6UIOqwgeyekCDsnoUg7YGs6riw7JeQIOunnuy2sCAn64uk66W06rKMJyDsqrzqsKwhIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIyMzEuNjAwMDAwMDAwMDAwMDIiIHdpZHRoPSIzNDAuNTcyOTk5OTk5OTk5OSIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIyMjYuMjg2NDk5OTk5OTk5OTYiIHk9IjI1OC41IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIyMjYuMjg2NDk5OTk5OTk5OTYiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj4zLiBWTFNNICjqsIDrs4Ag6ri47J20IOyerOuLqCkg4pyoPC90c3Bhbj48dHNwYW4geD0iMjI2LjI4NjQ5OTk5OTk5OTk2IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7tgbAg67m1IDHqsJzrpbwg4p6UIOqwgeyekCDsnoUg7YGs6riw7JeQIOunnuy2sCAmIzM5O+uLpOultOqyjCYjMzk7IOyqvOqwrCE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 3대 주소 재단 기술의 메커니즘 전격 대조 및 계산법 (3단 표 - 1순위)**

각 기술이 서브넷 마스크의 '1' 비트를 늘리는지 줄이는지와, 왜 그런 짓을 하는지(목적) 대조해야 합니다.

| **핵심 척도 (비교 잣대)**               | **🔪 서브네팅 (Subnetting)**                                                                                           | **🤝 슈퍼네팅 / 📏 VLSM 🚨**                                                                                                                |
| :------------------------------ | :----------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **방향성 및 서브넷 마스크 비트의 이동 방향**     | **'큰 네트워크를 잘게 쪼개기'.** 호스트 부분의 '0'을 네트워크 부분의 '1'로 빌려옴. (마스크 길이가 길어짐. 예: `/24` ➔ `/26`)                              | **'슈퍼네팅: 합치기 / VLSM: 다르게 쪼개기'.** - **슈퍼네팅:** 네트워크의 '1'을 '0'으로 빌려줌 (마스크 짧아짐. 예: `/24` ➔ `/22`). - **VLSM:** 서브넷마다 마스크 길이를 다르게 적용.        |
| **기술 도입의 핵심 목적 (해결하려는 문제점)**    | **\[IP 낭비 방지 및 브로드캐스트 차단]** 회사에 PC가 50대뿐인데 256개짜리 C클래스를 주면 200개가 버려짐. 이를 쪼개서 낭비를 막고, 방송 소음(브로드캐스트) 구역을 나눠 트래픽을 줄임. | **\[슈퍼네팅: 라우터 부하(메모리) 감소 💯]** 여러 목적지 주소를 하나로 묶어 이정표(라우팅 테이블)를 줄여 라우터의 검색 속도를 높임. **\[VLSM: 낭비 제로화]** 부서별 인원수 편차 해결.                    |
| **🚨 호스트 수 계산 공식 (가용 호스트 산출법)** | - 남은 호스트 비트 수가 `n`일 때, - 쪼개진 서브넷당 총 IP 수 = **`2^n`** **개** - **가용 호스트(실제 PC에 줄 수 있는 수) =** **`2^n - 2`** **개 🚨**  | **\[왜 '-2'를 빼는가? 💯]** 네트워크에서 맨 첫 번째 IP는 \*\*'네트워크 주소(이름표)'\*\*로 쓰이고, 맨 마지막 IP는 \*\*'브로드캐스트 주소(방송용)'\*\*로 예약되어 있어 PC(호스트)에 부여할 수 없기 때문! |

**\[핵심 계산 예제]** 만약 서브넷 마스크가 **`/26`** 이라면?

1. 전체 32비트 중 앞 26비트가 네트워크, 남은 **호스트 비트는 6비트 (32 - 26 = 6).**
2. 서브넷당 들어가는 총 IP 수는 `2^6 = 64개`.
3. 실제 컴퓨터에 할당할 수 있는 **'가용 호스트 수'는** **`64 - 2 = 62개`**.

#### **IV. \[결론/제언] 복잡한 계산을 없애는 궁극적 해결책, IPv6 체계의 확산**

* **(키워드 위주 2줄 마무리)** "서브네팅과 VLSM, 그리고 사설 IP(NAT)는 부족한 IPv4 주소를 아껴 쓰기 위한 눈물겨운 꼼수이자 지연을 유발하는 복잡한 연산입니다. 128비트의 무한한 주소를 제공하여 서브네팅의 복잡한 계산이 아예 필요 없고 모든 IoT 기기에 공인 IP를 직접 부여할 수 있는 **'IPv6 체계'로의 전면적 패러다임 전환만이 근본적 해결책입니다.**"
