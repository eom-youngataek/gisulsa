### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (파일슬랙정의, 발생원인) — 3~4줄
Ⅱ. 슬랙의 2단계구조 (본론①, 도식 1개 필수)
Ⅲ. 포렌식적가치 및 안티포렌식악용 (본론②, 핵심 배점)
Ⅳ. 결론
```

### Ⅰ. 개요

파일시스템은 디스크를 **클러스터(섹터의묶음)** 단위로할당합니다. 그런데 실제파일크기가 클러스터크기보다작으면, \*\*"할당은됐지만실제로안쓰이는남는공간"\*\*이생깁니다 — 이게바로 **파일슬랙**입니다. 앞서다룬 \*\*"파일카빙"\*\*이 삭제된파일의 **본체데이터**를복구하는것이었다면, 파일슬랙은 그 \*\*"미묘한여백공간"\*\*에 남은 흔적을찾는것입니다.

### Ⅱ. 슬랙의 2단계구조 — 핵심

| 구분         | 발생위치         | 내용                                               |
| :--------- | :----------- | :----------------------------------------------- |
| **RAM슬랙**  | **마지막섹터안**   | 파일의마지막데이터가 **섹터를다못채운부분**— OS가 **메모리(RAM)의값으로채움** |
| **드라이브슬랙** | **마지막클러스터안** | 마지막섹터 **이후남은섹터들**— **디스크의이전내용(과거삭제된데이터)이그대로남음**  |

→ 암기: **"RAM슬랙은메모리의찌꺼기,드라이브슬랙은디스크의찌꺼기"** — 오래된윈도우시스템에서는 RAM슬랙에 \*\*"메모리에떠있던비밀번호,암호화키같은민감정보"\*\*가 섞여들어간사례가 유명합니다.

### 도식화 제안

```
[클러스터(4KB) 할당]
┌────────────────────────────┐
│[실제파일데이터(3KB)]│[섹터끝까지](RAM슬랙)│[남은섹터들](드라이브슬랙)│
└────────────────────────────┘
      ↑실제사용            ↑메모리값으로채워짐      ↑과거삭제된데이터흔적
```

### Ⅲ. 포렌식적가치 및 안티포렌식악용 — 핵심 배점

**함정 방지: "여백일뿐"이라고답하면절반. 왜조사관에게는금광이고,공격자에게는은신처가되는지 양면을보여줘야완성됩니다.**

| 관점             | 활용                                                                         |
| :------------- | :------------------------------------------------------------------------- |
| **포렌식조사관**     | **드라이브슬랙에서과거삭제된파일의조각**발견 — 앞서다룬 \*\*"파일카빙"\*\*이 못찾는 **작은흔적**까지 슬랙분석으로보완가능  |
| **공격자(안티포렌식)** | 슬랙공간에 **악성코드일부를은닉**(정상파일사이의빈공간에 조각조각숨김) — 앞서다룬 \*\*"안티포렌식의은닉기법"\*\*의 구체적사례 |

→ 암기: **"조사관에겐과거의증거창고,공격자에겐숨기좋은틈새"** — 앞서다룬 \*\*"안티포렌식대응컴플라이언스"\*\*답안에서 다룬 \*\*"은닉(Steganography)"\*\*의 대표적기법중하나가 바로 \*\*"슬랙공간에데이터를숨기는것(SlackSpaceHiding)"\*\*입니다.

### 도식화 제안

```
[정상파일A - 3KB사용,클러스터4KB]
     └─슬랙공간(1KB)─┘
              ↓
      [공격자가 이1KB에 악성코드조각 숨김]
      (파일탐색기에는 파일A만 보이고, 
       슬랙속내용은 일반도구로안보임)
```

### Ⅳ. 결론

파일슬랙은 \*\*"할당된공간과실제사용공간사이의틈"\*\*이며, 이틈은 \*\*"삭제된과거데이터의흔적을담은포렌식의금맥"\*\*이자 \*\*"공격자가데이터를숨기는은신처"\*\*라는 양면성을가집니다 — 이는 앞서다룬 \*\*파일카빙(본체데이터복구)\*\*과 \*\*디스크이미징(전체보존)\*\*이 왜 \*\*"단순히파일을복사하는것"\*\*을넘어 \*\*"클러스터·섹터수준까지비트단위로전부복제해야하는지"\*\*의 이유를보여줍니다 — 결국 오늘하루다룬 디지털포렌식시리즈전체가 \*\*"디스크에는눈에보이는파일목록보다훨씬많은정보가 숨겨져있다"\*\*는 하나의결론으로 수렴합니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "4명짜리 호텔 방(클러스터)을 예약했는데 손님이 3명(파일)만 들어왔다. 침대 1개가 남는다. 운영체제(OS)는 융통성이 없어서 남는 침대 1개를 다른 사람에게 주지 않고 그냥 빈 채로 방 문을 잠가버린다. 이처럼 파일을 하드디스크에 저장할 때, 디스크의 고정된 할당 단위(클러스터, 4KB)와 실제 파일의 크기(3KB)가 딱 떨어지지 않아서 발생하는 \*\*'자투리 잉여 공간'을 '슬랙 공간(Slack Space)'\*\*이라고 한다. 일반인에겐 버려진 낭비 공간이지만 포렌식에서는 최고의 보물창고다. 해커는 OS가 이 공간을 건드리지 않는다는 점을 악용해, 자투리 공간에 악성코드나 기밀 데이터를 몰래 숨긴다(데이터 은닉). 반대로 수사관은 예전에 지워졌던 엑셀 파일의 흔적(찌꺼기)이 이 자투리 공간에 덮어씌워지지 않고 고스란히 남아있다는 것을 알고, 디스크 이미징 후 슬랙 공간만 박박 긁어내어 결정적 범죄 증거를 획득한다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 버려진 자투리 공간의 역습, 파일 슬랙 개요**

* **정의:** 운영체제가 파일 시스템에 데이터를 기록할 때 할당하는 '고정된 논리적 단위(클러스터 등)'의 크기보다 '실제 저장하려는 파일의 크기'가 작아서 생기는 **빈 물리적 잉여 공간(자투리 공간)**.
* **포렌식적 의미 (은닉과 증거):** 논리적 파일 사이즈에는 잡히지 않는 유령 공간이므로, 범죄자는 이곳에 데이터를 숨기고(Data Hiding, 안티 포렌식), 수사관은 덮어씌워지지 않은 과거 파일의 파편(증거)을 찾아내는 디지털 과학 수사의 핵심 조사 영역임.

#### **II. \[본론 1] (단순화 버전) 클러스터 내에서 발생하는 슬랙 구조 파이프라인 (도식화)**

섹터 2개(1024바이트)로 이루어진 클러스터에 600바이트 파일을 넣었을 때 발생하는 두 가지 슬랙을 직관적으로 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4OTguNTE2OTk5OTk5OTk5OSA1MzAuMyIgd2lkdGg9Ijg5OC41MTY5OTk5OTk5OTk5IiBoZWlnaHQ9IjUzMC4zIiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfMV9fXzEwMjRfQnl0ZV9fIiBkYXRhLWxhYmVsPSLtlZjrk5zrlJTsiqTtgazsnZggMeqwnCDtgbTrn6zsiqTthLAgKOy0nSAxMDI0IEJ5dGUg7ZWg64u5IOq1rOyXrSkiPgogIDxyZWN0IHg9IjQ4NC4zMjUiIHk9IjQwIiB3aWR0aD0iMzc0LjE5MTk5OTk5OTk5OTk1IiBoZWlnaHQ9IjQ1MC4zIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDg0LjMyNSIgeT0iNDAiIHdpZHRoPSIzNzQuMTkxOTk5OTk5OTk5OTUiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjQ5Ni4zMjUiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPu2VmOuTnOuUlOyKpO2BrOydmCAx6rCcIO2BtOufrOyKpO2EsCAo7LSdIDEwMjQgQnl0ZSDtlaDri7kg6rWs7JetKTwvdGV4dD4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfX181MTJfQnl0ZSIgZGF0YS1sYWJlbD0i7LKrIOuyiOynuCDshLnthLAgKDUxMiBCeXRlKSI+CiAgPHJlY3QgeD0iNTAwLjMyNSIgeT0iODQiIHdpZHRoPSIxNjQuMzUyIiBoZWlnaHQ9IjExMy44MDAwMDAwMDAwMDAwMSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjUwMC4zMjUiIHk9Ijg0IiB3aWR0aD0iMTY0LjM1MiIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTEyLjMyNSIgeT0iOTgiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+7LKrIOuyiOynuCDshLnthLAgKDUxMiBCeXRlKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9fXzUxMl9CeXRlIiBkYXRhLWxhYmVsPSLssqsg67KI7Ke4IOyEue2EsCAoNTEyIEJ5dGUpIj4KICA8cmVjdCB4PSI1MDAuMzI1IiB5PSIyMTcuOCIgd2lkdGg9IjM0Mi4xOTE5OTk5OTk5OTk5NSIgaGVpZ2h0PSIyNTYuNSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjUwMC4zMjUiIHk9IjIxNy44IiB3aWR0aD0iMzQyLjE5MTk5OTk5OTk5OTk1IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MTIuMzI1IiB5PSIyMzEuOCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7ssqsg67KI7Ke4IOyEue2EsCAoNTEyIEJ5dGUpPC90ZXh0Pgo8L2c+CjwvZz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfXyIgZGF0YS1sYWJlbD0i64uk7J2MIOu5hOyWtOyeiOuKlCDtgbTrn6zsiqTthLAiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjM1MS44MjUiIGhlaWdodD0iMTMwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIzNTEuODI1IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+64uk7J2MIOu5hOyWtOyeiOuKlCDtgbTrn6zsiqTthLA8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlJBTSIgZGF0YS10bz0iUkVDT1ZFUiIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuydgOuLiS/rs7Xsm5Ag7JiB7JetIiBwb2ludHM9IjcyMy4xMTk2NjY2NjY2NjY2LDQzNC4zIDcyMy4xMTk2NjY2NjY2NjY2LDQ0Ni4zIDYxOS43MjIzMzMzMzMzMzMzLDQ0Ni4zIDYxOS43MjIzMzMzMzMzMzMzLDQ2MS43IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkRSSVZFIiBkYXRhLXRvPSJSRUNPVkVSIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i6rO86rGwIOymneqxsCDrsK0iIHBvaW50cz0iMzc1LjgyNSwxMTkuMzUgMzkxLjgyNSwxMTkuMzUgNDAxLjgyNSwxMTkuMzUgNDAxLjgyNSwyNzQuNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJEMiIgZGF0YS10bz0iUkFNIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjY1MS43MDg4MzMzMzMzMzM0LDMyOC4yIDY1MS43MDg4MzMzMzMzMzM0LDMyNy42IDYxOS43MjIzMzMzMzMzMzMzLDMyNy42IDYxOS43MjIzMzMzMzMzMzMzLDM2My42IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlJBTSIgZGF0YS10bz0iUkVDT1ZFUiIgZGF0YS1sYWJlbD0i7J2A64uJL+uzteybkCDsmIHsl60iPgogIDxyZWN0IHg9Ii00IiB5PSItNSIgd2lkdGg9IjkzLjY4MjAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNDIuODQxMDAwMDAwMDAwMDEiIHk9IjEwLjE1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7snYDri4kv67O17JuQIOyYgeyXrTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJEUklWRSIgZGF0YS10bz0iUkVDT1ZFUiIgZGF0YS1sYWJlbD0i6rO86rGwIOymneqxsCDrsK0iPgogIDxyZWN0IHg9IjM2MS4zMjUiIHk9IjIxMy43IiB3aWR0aD0iODAuNjE0MDAwMDAwMDAwMDIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI0MDEuNjMyIiB5PSIyMjguODUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuqzvOqxsCDspp3qsbAg67CtPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJSRUNPVkVSIiBkYXRhLWxhYmVsPSLtj6zroIzsi50K67aE7ISd6rSAIPCflI4iIGRhdGEtc2hhcGU9ImNpcmNsZSI+CiAgPGNpcmNsZSBjeD0iNDAxLjgyNSIgY3k9IjMzNi45IiByPSI2Mi41IiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0MDEuODI1IiB5PSIzMzYuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNDAxLjgyNSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPu2PrOugjOyLnTwvdHNwYW4+PHRzcGFuIHg9IjQwMS44MjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuu2hOyEneq0gCDwn5SOPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkQxIiBkYXRhLWxhYmVsPSLtjIzsnbwg642w7J207YSwCjUxMiBCeXRlIOq9iSDssLgg8J+fqSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1MTYuMzI1IiB5PSIxMjgiIHdpZHRoPSIxMzIuMzUyIiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1ODIuNTAxMDAwMDAwMDAwMSIgeT0iMTU0LjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjU4Mi41MDEwMDAwMDAwMDAxIiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7YyM7J28IOuNsOydtO2EsDwvdHNwYW4+PHRzcGFuIHg9IjU4Mi41MDEwMDAwMDAwMDAxIiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj41MTIgQnl0ZSDqvYkg7LC4IPCfn6k8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRDIiIGRhdGEtbGFiZWw9Iu2MjOydvCDrjbDsnbTthLAKODggQnl0ZSDwn5+pIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjYxMi4yODQ1IiB5PSIyNzQuNCIgd2lkdGg9IjExOC4yNzMiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjY3MS40MjA5OTk5OTk5OTk5IiB5PSIzMDEuMjk5OTk5OTk5OTk5OTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjY3MS40MjA5OTk5OTk5OTk5IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+7YyM7J28IOuNsOydtO2EsDwvdHNwYW4+PHRzcGFuIHg9IjY3MS40MjA5OTk5OTk5OTk5IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj44OCBCeXRlIPCfn6k8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUkFNIiBkYXRhLWxhYmVsPSLinKggUkFNIOyKrOuemSAoNDI0IEJ5dGUpIPCfn6gK7IS57YSwIO2VmOuCmOulvCDqvYkg7LGE7Jqw7KeAIOuqu+2VtCDrsJzsg53tlZwg7J6Q7Yis66asIQpSQU3snZgg7JOw66CI6riwIOuNsOydtO2EsOuCmCAwKE51bGwp7Jy866GcIOyxhOybjOynkCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1MTYuMzI1IiB5PSIzNjMuNiIgd2lkdGg9IjMxMC4xOTE5OTk5OTk5OTk5NSIgaGVpZ2h0PSI3MC43IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNjcxLjQyMSIgeT0iMzk4Ljk1MDAwMDAwMDAwMDA1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI2NzEuNDIxIiBkeT0iLTEyLjM1MDAwMDAwMDAwMDAwMSI+4pyoIFJBTSDsiqzrnpkgKDQyNCBCeXRlKSDwn5+oPC90c3Bhbj48dHNwYW4geD0iNjcxLjQyMSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7IS57YSwIO2VmOuCmOulvCDqvYkg7LGE7Jqw7KeAIOuqu+2VtCDrsJzsg53tlZwg7J6Q7Yis66asITwvdHNwYW4+PHRzcGFuIHg9IjY3MS40MjEiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPlJBTeydmCDsk7DroIjquLAg642w7J207YSw64KYIDAoTnVsbCnsnLzroZwg7LGE7JuM7KeQPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkRSSVZFIiBkYXRhLWxhYmVsPSLinKgg65Oc65287J2067iMIOyKrOuemSAvIO2MjOydvCDsiqzrnpkg8J+fpQrslYTsmIgg64Ko7JWE7IScIO2GteynuOuhnCDrsoTroKTsp4Qg7IS57YSw65OkIQrqs7zqsbDsl5Ag7KeA7JuM7KeEIO2MjOydvCDtnZTsoIHsnbQg6re464yA66GcIOuCqOyVhOyeiOydjCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSIzMTkuODI1IiBoZWlnaHQ9IjcwLjciIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIyMTUuOTEyNSIgeT0iMTE5LjM1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIyMTUuOTEyNSIgZHk9Ii0xMi4zNTAwMDAwMDAwMDAwMDEiPuKcqCDrk5zrnbzsnbTruIwg7Iqs656ZIC8g7YyM7J28IOyKrOuemSDwn5+lPC90c3Bhbj48dHNwYW4geD0iMjE1LjkxMjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyVhOyYiCDrgqjslYTshJwg7Ya17Ke466GcIOuyhOugpOynhCDshLnthLDrk6QhPC90c3Bhbj48dHNwYW4geD0iMjE1LjkxMjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuqzvOqxsOyXkCDsp4Dsm4zsp4Qg7YyM7J28IO2dlOyggeydtCDqt7jrjIDroZwg64Ko7JWE7J6I7J2MPC90c3Bhbj48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 슬랙 공간의 2대 유형 전격 비교 해부 (3단 표 - 출제 1순위)**

섹터 내부의 자투리인 \*\*'램 슬랙'\*\*과, 아예 남아서 버려진 섹터 덩어리인 \*\*'드라이브 슬랙'\*\*에 무엇이 남아있는지 대조하는 것이 핵심입니다.

| **슬랙 공간 유형**                                | **발생 원리 (왜 생기는가?)**                                                                                                                   | **포렌식 관점에서의 증거 가치 (무엇이 남나?) 🚨**                                                                                                                               |
| :------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. 램 슬랙** *(RAM Slack)*                   | **'하나의 섹터(Sector)를 다 채우지 못해 남는 공간'.** 파일의 마지막 끝부분이 저장될 때, 하드디스크의 최소 물리적 기록 단위인 '1개 섹터(보통 512 Byte)'의 용량을 다 채우지 못하고 남은 자투리 공간.         | **\[RAM 메모리의 찌꺼기 또는 패스워드]** 과거 윈도우(Win 98 등)는 이 빈 공간을 채우기 위해 램(RAM)에 있던 쓰레기 데이터를 끌어다 덮었음. 운이 좋으면 **메모리에 있던 암호나 기밀 데이터가 여기에 기록**되어 있음. *(최신 OS는 보안을 위해 0으로 채움)* |
| **2. 드라이브 슬랙** *(Drive Slack)* *(또는 파일 슬랙)* | **'클러스터(Cluster) 안에서 통째로 남은 빈 섹터들'.** 파일이 저장되고 섹터 단위로는 정리가 끝났으나, 논리적 단위인 '클러스터(예: 4KB = 섹터 8개)' 전체를 다 쓰지 못해 **아예 빈 방으로 남겨진 나머지 섹터들**. | **\[과거에 지워진 다른 파일의 파편 (보물창고) 💯]** 운영체제는 이 공간을 굳이 0으로 밀어버리지 않고 그냥 방치함. 따라서 이 공간에는 현재 파일이 아니라, **아주 옛날에 지워졌던 엑셀 파일이나 사진 조각이 덮어씌워지지 않은 채 그대로 남아있음.**             |
| **(참고) 볼륨 슬랙** *(Volume Slack)*             | 파티션(C드라이브, D드라이브)을 나누고 디스크 끝부분에 할당할 수 없어 통째로 버려진 잉여 메가바이트 공간.                                                                         | 공간이 꽤 크기 때문에, 해커들이 별도의 파티션을 숨기거나 대용량 악성코드를 통째로 숨기는(Data Hiding) 은신처로 악용함.                                                                                      |

#### **IV. \[결론/제언] 파일 단위 분석의 한계 극복과 비트 단위(Bit-Stream) 이미징의 절대성**

* **(키워드 위주 2줄 마무리)** "운영체제의 논리적인 복사(Ctrl+C)는 오직 눈에 보이는 파일 구조(논리적 크기)만 가져오므로 슬랙 공간의 귀중한 증거를 모두 놓치게 됩니다. 따라서 디지털 포렌식 수사관은 반드시 \*\*슬랙 공간과 지워진 비할당 영역까지 100% 긁어오는 '비트 단위 디스크 이미징(Bit-Stream Copy)'\*\*을 수행해야만 숨겨진 진실을 밝혀낼 수 있습니다."
