### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (BPFDoor정의,미라이와의대비) — 3~4줄
Ⅱ. 핵심기술 - BPF악용원리 (본론①, 도식 1개 필수)
Ⅲ. 은닉기법3중구조 (본론②, 핵심 배점)
Ⅳ. 국내실제사례및국가급위협
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬미라이봇넷은 '눈에보이는파괴'(DDoS트래픽폭주)를목표로했는데, BPFDoor는정반대 — '아무도눈치채지못하게, 몇년씩숨어서엿보는것'이목표 — 실제로2021년PwC보고서로처음발견됐지만, 그이전부터중동·아시아통신사를은밀히감시해왔다는사실이 나중에야드러났다"\*\*는한줄로시작하면, 왜이위협이 "포트리스(portless)백도어"라는 특이한이름으로불리는지 논리가섭니다.

### Ⅱ. 핵심기술 — BPF악용원리

| 개념                            | 내용                                                            |
| :---------------------------- | :------------------------------------------------------------ |
| **BPF**(BerkeleyPacketFilter) | 원래는 **네트워크패킷을효율적으로필터링**하기위한 리눅스커널의 **정상적인기능**(관측·보안도구에서널리활용)  |
| **BPFDoor의악용방식**              | 이 **정상기능을악용**해, **리슨포트를전혀열지않고도**(Portless) 특정패킷을감지·수신         |
| **매직패킷트리거**                   | 특정 **매직바이트**(0x7255,0x5293등)를포함한패킷이올때만 **활성화** — 평상시엔완전히잠들어있음 |

→ 암기: **"원래는좋은용도로쓰는BPF기능을, 몰래숨는용도로거꾸로쓴다"** — 앞서다룬 \*\*"AOP(관점지향프로그래밍)"\*\*에서 \*\*"횡단관심사를시스템에 자연스럽게끼워넣는것"\*\*이 정상적활용이었다면, BPFDoor는 **"악성기능을시스템깊숙이 자연스럽게끼워넣는"** 정반대의사례입니다.

### 도식화 제안

```
[일반적인네트워크방어]                    [BPFDoor]
[방화벽] ──리슨포트감시(22,80,443등)──     ──리슨포트없음(Portless)──
         ↓                                     ↓
   "열린포트가없으면 안전하다"고 판단        BPF필터가 매직패킷만조용히감지
                                          (기존보안도구가 아예"보지못함")
```

→ "일반적으로보안점검은 '어떤포트가열려있나'를확인하는데, BPFDoor는포트를전혀열지않아서 이가장기본적인점검법자체가 무력화된다"는게 핵심입니다.

### Ⅲ. 은닉기법3중구조 — 핵심 배점

**함정 방지: "숨어있다"고만답하면절반. 구체적으로3가지레이어에서 어떻게은폐하는지보여줘야완성됩니다.**

| 은닉기법         | 내용                                                                    |
| :----------- | :-------------------------------------------------------------------- |
| **프로세스이름위장** | 실행시 **정상시스템데몬처럼이름을바꿔** 프로세스목록에서 눈에안띄게함                                |
| **메모리기반실행**  | **디스크에파일로남기지않고메모리에서만실행** → **실행후자기자신을삭제**(파일시스템포렌식으로도 흔적을못찾음)         |
| **암호화통신**    | **RC4스트림암호**(앞서다룬대칭키암호의한종류)로 **명령패킷내용을암호화** → 네트워크로그상에서 **평문내용을식별불가** |

→ 암기: **"이름을바꾸고,흔적을안남기고,대화내용도암호화한다"** — 앞서다룬 \*\*RC4(대칭키암호)\*\*가 여기서는 \*\*"방어자의탐지를피하기위한공격자의도구"\*\*로 악용된다는 점이, 오늘하루다룬 여러암호기법의 **양면성**(선의로도악의로도쓰일수있음)을 다시보여줍니다.

### 도식화 제안

```
[BPFDoor 3중은닉]
①프로세스위장: "systemd-worker"처럼 정상데몬이름으로표시
②메모리실행: 디스크에안남기고 실행 → 실행후 자기파일삭제
③암호화통신: RC4로 명령·응답 암호화 (로그분석으로도 내용식별불가)

→ 결과: "포트없음+파일없음+평문없음" = 3중부재로 탐지회피
```

### Ⅳ. 국내실제사례및국가급위협

**함정 방지: "이론적위협"으로만끝내면절반. 2025년4월SKT사건과2026년최신동향을반영해야완성됩니다.**

**2025년4월 SKT유심해킹사건**: BPFDoor가 실제로 **국내통신사해킹**에활용되어, **유심정보대량유출**로이어진 국가적파장을일으킨사건입니다 — KISA가2025년5월 긴급 **점검가이드**를배포했고, 이후 **2차위협정보**까지추가공개했습니다.

**2026년3월 중국해킹조직정황**(래피드7분석): BPFDoor가 단순은닉형백도어를넘어, **통신백본내부에조용한접근계층**을만든것으로확인 — 일부변종은 **SCTP프로토콜지원**흔적까지있어, **가입자행동,위치정보,특정인물의이동흔적**까지 감시하려했을가능성이 제기됐습니다. 이조직은 **최소2021년부터** 중동·아시아통신사를 겨냥해활동해온것으로추적됩니다.

| 대응기법       | 내용                                                                    |
| :--------- | :-------------------------------------------------------------------- |
| **행위기반탐지** | 포트/파일기반탐지가무력화되므로, **메모리실행,AF\_PACKET소켓생성,iptables변조**같은 **행위신호를교차분석** |
| **국산대응도구** | 씨큐비스타의 \*\*"BPFDoor헌터"\*\*같은 전용탐지도구 개발·보급                             |

→ 앞서다룬 \*\*"제로트러스트(NeverTrust,AlwaysVerify)"\*\*답안의원칙이, 여기서는 \*\*"포트가안열려있어도, 행위자체를끊임없이감시해야한다"\*\*는 형태로 구체화됩니다 — 정적인점검(포트스캔)이아니라 **동적인행위관찰**만이 BPFDoor를 잡아낼수있습니다.

### Ⅴ. 결론 포인트 (오늘 하루 방대한 암호·보안 시리즈 최종대단원)

BPFDoor는 앞서다룬 \*\*미라이봇넷(시끄러운파괴,DDoS)\*\*과 정반대의철학 — **"조용히,오래,깊이숨어서정보를빼가는"** 국가급APT공격의전형입니다 — 오늘하루다룬 대칭/비대칭암호(RC4가공격자의은폐도구로악용)→해시함수→크리덴셜스터핑→랜섬웨어/RaaS→큐싱→딥페이크→스푸핑→DDoS→인포스틸러→미라이봇넷→BPFDoor로 이어지는 방대한암호·보안시리즈전체가, 결국 \*\*"공격은요란한것(DDoS,랜섬웨어)과조용한것(백도어,APT)두갈래로진화하며,방어역시가시적차단(포트감시)에서행위기반의지속적관찰(제로트러스트)로진화해야한다"\*\*는 최종결론으로 마무리됩니다 — 오늘하루의여정은, **기술이발전할수록공격과방어모두더정교해지지만, 그경쟁은결코끝나지않는다**는 사실을 보여주었습니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "리눅스 서버에 침투한 해커가 뒷문(백도어)을 열려면 보통 새로운 통로(포트)를 파야 한다. 하지만 포트를 새로 열면 방화벽이나 보안 담당자의 감시망(netstat 명령어 등)에 즉시 발각되고 만다. 그래서 해커들은 천재적이고 악랄한 방법을 고안해 냈다. '새로운 문을 만들지 말고, 이미 정상적으로 열려 있는 문(포트)을 몰래 같이 쓰자!' 이것이 바로 무려 5년 동안 통신사와 공공기관의 리눅스 서버를 유린하면서도 백신에 단 한 번도 걸리지 않은 최악의 투명인간 악성코드, \*\*'BPFdoor'\*\*다. 이 악성코드의 핵심 무기는 리눅스에 원래 깔려 있는 합법적인 패킷 감시 도구인 \*\*'BPF(Berkeley Packet Filter)'\*\*를 악용하는 것이다. BPFdoor는 감염된 서버에서 정상 시스템 프로세스(예: systemd)로 이름을 감쪽같이 속이고 숨어, BPF 필터를 이용해 서버로 들어오는 모든 인터넷 트래픽을 가장 밑바닥 계층에서 몰래 훔쳐본다(스니핑). 공격 방식은 기가 막힌다. 해커가 평소처럼 정상적으로 열려있는 80번(웹)이나 22번(SSH) 포트를 향해 자신들만의 '특정 암호(매직 패스워드)'가 담긴 패킷을 던진다. 그러면 리눅스의 방화벽(iptables)이 이 패킷을 검사하기도 전에, 밑바닥에 숨어있던 BPFdoor가 '어! 우리 해커 주인님이 보낸 패킷이네!' 하고 낚아채어 해커에게 서버의 최고 관리자(Root) 권한을 넘겨버린다. 방화벽도 정상, 포트도 정상이니 보안 담당자는 해킹당한 사실을 영영 눈치채지 못한다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 5년간 탐지되지 않은 완벽한 투명인간, BPFdoor 개요**

* **정의:** 리눅스(Linux) 및 솔라리스 기반 시스템을 표적으로, 리눅스 자체의 합법적 패킷 필터링 도구인 **BPF(Berkeley Packet Filter) 기능을 악용하여 방화벽을 우회하는 고도의 스텔스(은닉형) 백도어 악성코드**.
* **발견의 충격:** 2022년에 처음 발견되었으나 포렌식 결과 2017년부터 5년 이상 전 세계(통신, 교육, 정부 기관)에 퍼져 활동해 온 것으로 밝혀짐. 주로 중국계 해커 조직(Red Menshen)의 소행으로 추정됨.

#### **II. \[본론 1] (단순화 버전) 방화벽을 무시하고 매직 패스워드를 낚아채는 아키텍처 (도식화)**

방화벽(iptables)이 작동하기 전, 가장 밑단에서 패킷을 훔쳐 뒷문을 열어주는 과정을 직관적으로 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NTQuMzg2IDgxMi41ODIiIHdpZHRoPSI1NTQuMzg2IiBoZWlnaHQ9IjgxMi41ODIiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9fX19fXyIgZGF0YS1sYWJlbD0i6rCQ7Je865CcIOumrOuIheyKpCDshJzrsoQg64K067aAICjtg5Dsp4Ag7ZqM7ZS8IOuplOy7pOuLiOymmCkiPgogIDxyZWN0IHg9IjQwIiB5PSIyOTIuNCIgd2lkdGg9IjQ3NC4zODU5OTk5OTk5OTk5NyIgaGVpZ2h0PSI0ODAuMTgyIiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHJlY3QgeD0iNDAiIHk9IjI5Mi40IiB3aWR0aD0iNDc0LjM4NTk5OTk5OTk5OTk3IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iMzA2LjQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+6rCQ7Je865CcIOumrOuIheyKpCDshJzrsoQg64K067aAICjtg5Dsp4Ag7ZqM7ZS8IOuplOy7pOuLiOymmCk8L3RleHQ+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkhBQ0tFUiIgZGF0YS10bz0iU1JWIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIxLiDsoJXsg4HsoIHsnbggODDrsogg7Y+s7Yq466GcCifrp6Tsp4Eg7Yyo7Iqk7JuM65OcJyDtjKjtgrcg642Y7KeQIiBwb2ludHM9IjI3Ny45MzM5OTk5OTk5OTk5Nyw3Ni45IDI3Ny45MzM5OTk5OTk5OTk5NywyMDcuNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iU1JWIiBkYXRhLXRvPSJCUEYiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjc3LjkzMzk5OTk5OTk5OTk3LDI0NC40IDI3Ny45MzM5OTk5OTk5OTk5NywyOTIuNCAyNzcuOTMzOTk5OTk5OTk5OTcsMzM2LjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkJQRiIgZGF0YS10bz0iUk9PVCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iMy4gJ+yWtD8g7Jqw66asIOyjvOyduOuLmCDslZTtmLjri6QhJyDrgprslYTssZQhCuuwqe2ZlOuyveycvOuhnCDslYgg67O064K06rOgIOyasO2ajOyLnO2CtCIgcG9pbnRzPSIyMzUuODIwMzMzMzMzMzMzMzQsNTQ2Ljk2ODMzMzMzMzMzMzQgMjM1LjgyMDMzMzMzMzMzMzM0LDYwMS4wODIgMTYwLjMzNzQ5OTk5OTk5OTk4LDYwMS4wODIgMTYwLjMzNzQ5OTk5OTk5OTk4LDcxOS42ODIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkJQRiIgZGF0YS10bz0iRlciIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLso7zsnbjri5gg7JWU7Zi46rCAIOyXhuuKlCDsnbzrsJgg7Yyo7YK3IiBwb2ludHM9IjMyMC4wNDc2NjY2NjY2NjY2Niw1NDYuOTY4MzMzMzMzMzMzMiAzMjAuMDQ3NjY2NjY2NjY2NjYsNjAxLjA4MiAzOTUuNTMwNDk5OTk5OTk5OTYsNjAxLjA4MiAzOTUuNTMwNSw3MTkuNjgyIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iSEFDS0VSIiBkYXRhLXRvPSJTUlYiIGRhdGEtbGFiZWw9IjEuIOygleyDgeyggeyduCA4MOuyiCDtj6ztirjroZwKJ+unpOyngSDtjKjsiqTsm4zrk5wnIO2MqO2CtyDrjZjsp5AiPgogIDxyZWN0IHg9IjIwNC40MzM5OTk5OTk5OTk5NyIgeT0iMTE5LjkwMDAwMDAwMDAwMDAyIiB3aWR0aD0iMTQ2LjU0OCIgaGVpZ2h0PSI0NC42IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjI3Ny43MDc5OTk5OTk5OTk5NyIgeT0iMTQyLjIwMDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIj48dHNwYW4geD0iMjc3LjcwNzk5OTk5OTk5OTk3IiBkeT0iLTMuMzAwMDAwMDAwMDAwMDAwNyI+MS4g7KCV7IOB7KCB7J24IDgw67KIIO2PrO2KuOuhnDwvdHNwYW4+PHRzcGFuIHg9IjI3Ny43MDc5OTk5OTk5OTk5NyIgZHk9IjE0LjMiPiYjMzk766ek7KeBIO2MqOyKpOybjOuTnCYjMzk7IO2MqO2CtyDrjZjsp5A8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJCUEYiIGRhdGEtdG89IlJPT1QiIGRhdGEtbGFiZWw9IjMuICfslrQ/IOyasOumrCDso7zsnbjri5gg7JWU7Zi464ukIScg64Ka7JWE7LGUIQrrsKntmZTrsr3snLzroZwg7JWIIOuztOuCtOqzoCDsmrDtmozsi5ztgrQiPgogIDxyZWN0IHg9IjYzLjgzNzQ5OTk5OTk5OTk4IiB5PSI2MzIuMDgyMDAwMDAwMDAwMSIgd2lkdGg9IjE5Mi44OCIgaGVpZ2h0PSI0NC42IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjE2MC4yNzc0OTk5OTk5OTk5NyIgeT0iNjU0LjM4MjAwMDAwMDAwMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSIxNjAuMjc3NDk5OTk5OTk5OTciIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij4zLiAmIzM5O+yWtD8g7Jqw66asIOyjvOyduOuLmCDslZTtmLjri6QhJiMzOTsg64Ka7JWE7LGUITwvdHNwYW4+PHRzcGFuIHg9IjE2MC4yNzc0OTk5OTk5OTk5NyIgZHk9IjE0LjMiPuuwqe2ZlOuyveycvOuhnCDslYgg67O064K06rOgIOyasO2ajOyLnO2CtDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkJQRiIgZGF0YS10bz0iRlciIGRhdGEtbGFiZWw9IuyjvOyduOuLmCDslZTtmLjqsIAg7JeG64qUIOydvOuwmCDtjKjtgrciPgogIDxyZWN0IHg9IjMxMS41MzA0OTk5OTk5OTk5NiIgeT0iNjM5LjIzMiIgd2lkdGg9IjE2Ny4zMzgwMDAwMDAwMDAwNSIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjM5NS4xOTk1IiB5PSI2NTQuMzgyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7so7zsnbjri5gg7JWU7Zi46rCAIOyXhuuKlCDsnbzrsJgg7Yyo7YK3PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJIQUNLRVIiIGRhdGEtbGFiZWw9Iu2VtOy7pCDwn6W3IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjIzMy42MTc1IiB5PSI0MCIgd2lkdGg9Ijg4LjYzMyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjc3LjkzNCIgeT0iNTguNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPu2VtOy7pCDwn6W3PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTUlYiIGRhdGEtbGFiZWw9IuumrOuIheyKpCDshJzrsoQg64Sk7Yq47JuM7YGsIOyduO2EsO2OmOydtOyKpCDwn4yQIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjE0MS4zNjMiIHk9IjIwNy41IiB3aWR0aD0iMjczLjE0MiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjc3LjkzMzk5OTk5OTk5OTk3IiB5PSIyMjUuOTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuumrOuIheyKpCDshJzrsoQg64Sk7Yq47JuM7YGsIOyduO2EsO2OmOydtOyKpCDwn4yQPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJCUEYiIGRhdGEtbGFiZWw9IjIuIEJQRmRvb3Ig7JWF7ISx7L2U65OcIPCfkb4K67Cp7ZmU67K9IOyVnuuLqOyXkOyEnCDtjKjtgrcg6rCQ7IucIOykkSIgZGF0YS1zaGFwZT0iZGlhbW9uZCI+CiAgPHBvbHlnb24gcG9pbnRzPSIyNzcuOTMzOTk5OTk5OTk5OTcsMzM2LjQgNDA0LjI3NSw0NjIuNzQxIDI3Ny45MzM5OTk5OTk5OTk5Nyw1ODkuMDgyIDE1MS41OTI5OTk5OTk5OTk5Niw0NjIuNzQxIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjI3Ny45MzM5OTk5OTk5OTk5NyIgeT0iNDYyLjc0MSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMjc3LjkzMzk5OTk5OTk5OTk3IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+Mi4gQlBGZG9vciDslYXshLHsvZTrk5wg8J+RvjwvdHNwYW4+PHRzcGFuIHg9IjI3Ny45MzM5OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+67Cp7ZmU67K9IOyVnuuLqOyXkOyEnCDtjKjtgrcg6rCQ7IucIOykkTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJST09UIiBkYXRhLWxhYmVsPSI0LiDtlbTsu6Tsl5DqsowgUm9vdCDsiZgg7KCc6rO1IPCflJMiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTYiIHk9IjcxOS42ODIiIHdpZHRoPSIyMDguNjc0OTk5OTk5OTk5OTgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTYwLjMzNzQ5OTk5OTk5OTk4IiB5PSI3MzguMTMyMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+NC4g7ZW07Luk7JeQ6rKMIFJvb3Qg7ImYIOygnOqztSDwn5STPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJGVyIgZGF0YS1sYWJlbD0i66as64iF7IqkIOuwqe2ZlOuyvSBpcHRhYmxlcyDwn5uh77iPIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjI5Mi42NzUiIHk9IjcxOS42ODIiIHdpZHRoPSIyMDUuNzEwOTk5OTk5OTk5OTgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjM5NS41MzA1IiB5PSI3MzguMTMyMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+66as64iF7IqkIOuwqe2ZlOuyvSBpcHRhYmxlcyDwn5uh77iPPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 전통적 백도어 vs 최신 BPFdoor 전격 비교 해부 (3단 표)**

왜 기존 백도어는 쉽게 걸리고, BPFdoor는 \*\*'포트 미개방'\*\*과 \*\*'방화벽 스니핑'\*\*으로 안 걸렸는지를 대조하는 것이 핵심입니다.

| **핵심 척도 (비교 잣대)**                | **🚪 기존 전통적 백도어 (Trojan)**                                                                                       | **👾 BPFdoor (스텔스 백도어)**                                                                                                |
| :------------------------------- | :--------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| **통신을 위한 네트워크 포트(Port) 개방 여부**   | 해커와 통신하기 위해 서버에 **'새로운 비정상 포트(예: 4444번)'를 몰래 열어둠.** ➔ 관리자가 `netstat` 명령어를 치면 "어? 안 쓰던 4444번이 왜 열려있지?" 하고 즉시 발각됨. | **'새로운 포트를 아예 열지 않음!'** 서버에 원래 열려 있는 정상적인 포트(80 HTTP, 22 SSH)의 트래픽에 기생하여 통신함. ➔ **포트 스캐닝 도구에 절대 탐지되지 않음.**              |
| **리눅스 방화벽(iptables) 우회 및 통과 방법** | 해커의 비정상 포트로 들어오므로 방화벽 룰에 막혀 차단되기 쉬움. 그래서 방화벽 정책 자체를 변조해야 함.                                                      | OS가 제공하는 '합법적 BPF 소켓(Raw Socket)'을 사용하여, **방화벽(iptables)이 패킷을 검사하기도 전인 최하단 데이터링크 계층 근처에서 패킷을 먼저 낚아채어 훔쳐(Sniffing) 버림.** |
| **악성코드 은닉 방식**                   | 파일명이 대놓고 의심스럽거나 비정상적인 메모리 영역에 상주함.                                                                               | 리눅스 정상 프로세스인 \*\*`dbus-daemon`, `systemd-journald` 등의 이름으로 완벽히 위장(위임)\*\*하여 메모리에 숨어 있음.                                 |
| **해커의 공격 트리거**                   | 주기적으로 해커 서버(C\&C)에 신호를 보내서 명령을 달라고 함. (아웃바운드 트래픽 발생 ➔ 걸림).                                                       | **'매직 패스워드(Magic Password)'.** 해커가 특정 바이트 패턴을 담은 패킷(예: ICMP Ping)을 툭 던질 때까지 아무 행동도 안 하고 숨어있음.                           |

#### **IV. \[결론/제언] 합법적 도구 악용(LoL) 트렌드와 행위 기반 EDR의 필요성**

* **(키워드 위주 2줄 마무리)** "BPFdoor의 등장은 외부 악성 파일을 다운로드하지 않고 서버에 이미 설치된 정상 관리 도구를 흉기로 돌변시키는 \*\*'Living off the Land(LoL, 환경 기생형 공격)'\*\*의 끝판왕을 보여줍니다. 전통적인 파일 기반 백신(시그니처)으로는 이를 100% 막을 수 없으므로, **정상 프로세스의 비정상적인 '행위(Behavior)' 자체를 메모리 단에서 모니터링하는 차세대 EDR(엔드포인트 탐지 및 대응) 솔루션 도입이 필수적**입니다."
