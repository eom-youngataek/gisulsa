### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (측면이동정의,킬체인상의위치) — 3~4줄
Ⅱ. 핵심기법3대유형 (본론①, 도식 1개 필수)
Ⅲ. 골든티켓/실버티켓 - 최종병기 (본론②, 핵심 배점)
Ⅳ. 탐지및방어체계
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬BPFDoor는 '한대의서버에 몰래숨어들어가는것'까지였는데, 공격자의진짜목표(중요데이터,관리자권한)는 대부분 그서버가아니라 내부망의 다른곳에있다 — 첫침투지점에서시작해, 내부네트워크를옆으로,위로이동하며 최종목표에도달하는과정이측면이동"\*\*이라는한줄로시작하면, BPFDoor답안과바로이어집니다.

### Ⅱ. 핵심기법3대유형 — "훔·뿌·전"

| 기법                       | 원리                                                           |
| :----------------------- | :----------------------------------------------------------- |
| **Pass-the-Hash**(PtH)   | 비밀번호평문없이, **탈취한NTLM해시값자체**를 그대로인증에사용— 해시를 **복호화할필요조차없음**     |
| **Pass-the-Ticket**(PtT) | Kerberos \*\*인증티켓(TGT/ST)\*\*을탈취해 **재사용**,정당한사용자로가장          |
| **RDP/원격관리도구악용**         | 정상적인 **원격데스크톱,PsExec,WMI**등 **관리도구를그대로악용**해 이동 — 정상행위와구별이어려움 |

→ 암기: **"해시자체를훔쳐쓰고,티켓을훔쳐쓰고,정상관리도구를 그대로타고이동한다"** — 앞서다룬 \*\*"해시함수"\*\*답안에서 \*\*"해시는되돌릴수없다"\*\*고했는데,PtH공격은 \*\*"되돌릴필요도없이,해시값자체를열쇠처럼재사용"\*\*한다는 점에서 해시함수의 안전성전제자체를 우회하는 교묘한기법입니다.

### 도식화 제안

```
[초기침투(BPFDoor 등)] → [서버A]
     ↓ PtH: 서버A의 관리자 NTLM해시탈취
[서버B] ← 그해시로 그대로인증(비밀번호모른채)
     ↓ PtT: 서버B에서 Kerberos티켓탈취
[서버C] ← 그티켓으로인증
     ↓ (반복하며 내부망전체를옆으로,위로이동)
[도메인컨트롤러] ← 최종목표(전체장악)
```

### Ⅲ. 골든티켓/실버티켓 — 최종병기, 핵심 배점

**함정 방지: "티켓을훔친다"고만답하면절반. 골든티켓이왜"영구적"위협인지,실버티켓과의차이를보여줘야완성됩니다.**

| 티켓유형                   | 위조대상                                          | 특징                                                       |
| :--------------------- | :-------------------------------------------- | :------------------------------------------------------- |
| **골든티켓**(GoldenTicket) | **KRBTGT계정**(도메인전체인증의핵심계정)의 **해시**를탈취해 **위조** | **어떤계정으로든,어떤권한으로든** 위조가능— **10년짜리티켓**도만들수있어 **거의영구적지속성** |
| **실버티켓**(SilverTicket) | **특정서비스계정**의해시로 **그서비스에한정된**티켓위조              | 골든티켓보다 **범위가좁음**,도메인컨트롤러접촉없이생성가능해 **더은밀**                |

→ 암기: **"골든티켓은도메인전체의만능키(KRBTGT탈취),실버티켓은특정서비스만여는키"** — 앞서다룬 \*\*"LDAP"\*\*답안에서 \*\*"AD(ActiveDirectory)가조직전체인증의중심"\*\*이라고했는데, KRBTGT계정이 바로 **그AD인증체계의최상위신뢰뿌리**입니다 — 이게뚫리면 \*\*"관리자가비밀번호를전부바꿔도, 공격자는여전히위조티켓으로들어올수있다"\*\*는 것이 골든티켓의 무서운점입니다.

### 도식화 제안

```
[골든티켓 공격]
공격자가 [도메인컨트롤러]의 KRBTGT계정해시 탈취
     ↓
[위조된TGT생성] "나는도메인관리자다" (실제인증절차없이)
     ↓
모든서버·서비스에 무제한접근 (비밀번호변경으로도 막을수없음)
→ 해결책: KRBTGT계정 자체의 암호를 2번연속변경해야만 무효화
```

### Ⅳ. 탐지및방어체계

**함정 방지: "탐지하기어렵다"고만하면절반. 앞서다룬제로트러스트/ABAC와 연결해 구체적방어원칙을보여줘야완성됩니다.**

| 방어원칙                     | 내용                                                          |
| :----------------------- | :---------------------------------------------------------- |
| **최소권한(LeastPrivilege)** | 앞서다룬 **RBAC/ABAC**원칙 — 관리자계정이 **모든서버에로그인가능한상태를최소화**         |
| **네트워크분할(Segmentation)** | 앞서다룬 **MSA의서비스간경계**개념을 네트워크레벨로— 한구역이뚫려도 **다른구역으로전파차단**      |
| **행위기반탐지**               | 앞서다룬 **BPFDoor탐지**처럼, **비정상적인내부이동패턴**(평소안쓰던서버간연결등) 자체를 모니터링 |
| **KRBTGT정기갱신**           | 골든티켓의 근본대응— **KRBTGT계정암호정기변경**(이중갱신)으로 오래된위조티켓 무효화          |

→ 앞서다룬 \*\*"제로트러스트성숙도"\*\*의 **"네트워크,신원"기둥**이, 여기서는 \*\*"내부에침투했다고해서 그다음도자유롭게이동할수있게해서는안된다"\*\*는 원칙으로 구체화됩니다 — 이것이 바로 **"경계보안(외부만막음)에서제로트러스트(내부이동도매번검증)로"** 전환해야하는 실질적이유입니다.

### Ⅴ. 결론 포인트 (오늘의 방대한 암호·보안 시리즈 대단원)

측면이동은 \*\*"침투(BPFDoor)는시작일뿐, 진짜피해는내부에서옆으로,위로이동하며확산되는과정에서발생한다"\*\*는것을보여주며, 골든티켓처럼 **"한번의핵심계정탈취가, 이후모든방어를무력화시키는"** 근본적취약점의위험성을 일깨웁니다 — 이는앞서다룬 \*\*RBAC/ABAC(권한최소화),MSA(경계분할),제로트러스트(지속적검증)\*\*가 **"침투이후의확산을막기위한"** 핵심방어선이라는걸 보여주며, 오늘하루다룬방대한암호·보안시리즈전체(대칭/비대칭암호부터측면이동까지)가, \*\*"침입을완전히막을수없다면, 침입후의확산속도를늦추고범위를좁히는것이 현실적인최선의방어"\*\*라는 결론으로 완결됩니다 — 이것이 바로 오늘하루계속반복된 \*\*"완벽한예방은없으니, 탐지와격리, 회복력을함께준비하라"\*\*는 보안의근본철학입니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "성벽(기업 방화벽)을 넘어 성 안에 침투하는 데 성공한 도둑(해커)이 있다고 치자. 도둑이 처음 발을 디딘 곳은 성 외곽의 '말단 병사의 방(말단 직원의 감염된 PC)'이다. 하지만 도둑의 진짜 목표는 왕의 침소에 있는 '황금(Active Directory 서버와 기밀 DB)'이다. 도둑은 말단 병사의 옷을 훔쳐 입고(비밀번호 탈취), 경비병의 눈을 속이며 성 안의 방과 방 사이를 은밀하게 건너가기 시작한다. 이처럼 해커가 내부망(LAN)에 침투한 후 최종 타겟을 향해 시스템과 시스템 사이를 점프(이동)하며 권한을 점점 높여가는 과정을 \*\*'측면 이동(Lateral Movement)'\*\*이라고 부른다. 최근 전 세계를 강타하는 APT(지능형 지속 위협) 공격이나 대규모 랜섬웨어 사태의 99%는 바로 이 측면 이동 단계를 거친다. 이 측면 이동이 끔찍하게 막기 힘든 이유가 있다. 해커가 요란한 해킹 툴을 쓰는 것이 아니라, 방금 훔친 '과장님의 진짜 아이디'를 가지고 윈도우에 원래 깔려 있는 정상적인 '원격 접속 프로그램(RDP, PowerShell)'을 써서 옆자리 PC로 넘어간다(이를 LoL 기법이라 부름). 내부 보안 시스템 입장에서는 '아, 과장님이 야근하면서 다른 PC에 원격 접속을 하시는구나'라고 착각하고 문을 열어버리는 것이다. 이 끔찍한 횡적 감염을 막는 유일한 방법은, '성 안(내부망)에 한 번 들어왔다고 해서 무조건 믿지 말고 방과 방 사이에도 모두 촘촘하게 자물쇠를 달자'는 **'마이크로 세그멘테이션(Micro-segmentation)'과 제로 트러스트 철학**을 도입하는 것뿐이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 말단 직원 PC에서 왕의 침소(AD)로 향하는 길, 측면 이동 개요**

* **정의:** 공격자가 조직의 내부 네트워크에 최초로 침투(거점 확보)한 후, 최종 목표(중앙 관리 서버, DB 등)에 도달하기 위해 **내부 시스템 간을 은밀하게 넘나들며(수평적 이동) 권한을 점진적으로 탈취하고 확장해 나가는 해킹 공격의 핵심 단계 (MITRE ATT\&CK 프레임워크 기준).**
* **목적:** 최초로 감염된 말단 직원의 PC(단순한 일반 권한)만으로는 할 수 있는 게 없기 때문에, 최고 관리자(Domain Admin) 권한을 얻기 위해 다른 고위급 PC나 서버를 찾아 다니는 것.

#### **II. \[본론 1] (단순화 버전) 훔친 신분증으로 내부망을 점프하는 파이프라인 (도식화)**

외부에서 수직으로 뚫고 들어온 뒤, 내부에서 수평(측면)으로 기어가는 흐름을 직관적으로 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNzU5LjYzNzAwMDAwMDAwMDIgMjQyLjcwMDAwMDAwMDAwMDAyIiB3aWR0aD0iMTc1OS42MzcwMDAwMDAwMDAyIiBoZWlnaHQ9IjI0Mi43MDAwMDAwMDAwMDAwMiIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMl9fX0xhdGVyYWxfTW92ZW1lbnRfIiBkYXRhLWxhYmVsPSIyLiDrgrTrtoDrp50gJ+y4oeuptCDsnbTrj5koTGF0ZXJhbCBNb3ZlbWVudCknIOuLqOqzhCI+CiAgPHJlY3QgeD0iMzgyLjc4MyIgeT0iNDAiIHdpZHRoPSI5MTguMDk2IiBoZWlnaHQ9IjExMy44MDAwMDAwMDAwMDAwMSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjM4Mi43ODMiIHk9IjQwIiB3aWR0aD0iOTE4LjA5NiIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzk0Ljc4MyIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+Mi4g64K067aA66edICYjMzk77Lih66m0IOydtOuPmShMYXRlcmFsIE1vdmVtZW50KSYjMzk7IOuLqOqzhDwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iSEFDS0VSIiBkYXRhLXRvPSJQQzEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjEuIOy0iOq4sCDsuajtiKwgKO2UvOyLsSDrqZTsnbwpCuyImOyngSDtlZjqsJUg6rO16rKpIiBwb2ludHM9IjE1OC4yNzMsMTEwLjkgMzk4Ljc4MywxMTAuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iU0VSVkVSIiBkYXRhLXRvPSJBRCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iMy4g7LWc7KKFIOuqqe2RnCDri6zshLEhIiBwb2ludHM9IjEyODQuODc5LDExMC45IDE0OTkuODQ3MDAwMDAwMDAwMiwxMTAuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUEMxIiBkYXRhLXRvPSJQQzIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iu2blOy5nCDruYTrsojsnLzroZwgUkRQIOybkOqyqSDsoJHsho0hCuygleyDgSDsl4XrrLTroZwg7JyE7J6l7ZWoIiBwb2ludHM9IjQ2MS40ODEsMTEwLjkgNzE2LjgxOSwxMTAuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUEMyIiBkYXRhLXRvPSJTRVJWRVIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Iu2DiOy3qO2VnCDqtIDrpqzsnpAg6raM7ZWc7Jy866GcIOygkO2UhCEiIHBvaW50cz0iODY5LjE3OCwxMTAuOSAxMTI1LjExMDAwMDAwMDAwMDEsMTEwLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iSEFDS0VSIiBkYXRhLXRvPSJQQzEiIGRhdGEtbGFiZWw9IjEuIOy0iOq4sCDsuajtiKwgKO2UvOyLsSDrqZTsnbwpCuyImOyngSDtlZjqsJUg6rO16rKpIj4KICA8cmVjdCB4PSIyMDIuMjczMDAwMDAwMDAwMDIiIHk9Ijg3LjkiIHdpZHRoPSIxMzAuNTEwMDAwMDAwMDAwMDIiIGhlaWdodD0iNDQuNiIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyNjcuNTI4IiB5PSIxMTAuMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSI+PHRzcGFuIHg9IjI2Ny41MjgiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij4xLiDstIjquLAg7Lmo7YisICjtlLzsi7Eg66mU7J28KTwvdHNwYW4+PHRzcGFuIHg9IjI2Ny41MjgiIGR5PSIxNC4zIj7siJjsp4Eg7ZWY6rCVIOqzteqyqTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlNFUlZFUiIgZGF0YS10bz0iQUQiIGRhdGEtbGFiZWw9IjMuIOy1nOyihSDrqqntkZwg64us7ISxISI+CiAgPHJlY3QgeD0iMTM1MC44NzkiIHk9Ijk0LjkiIHdpZHRoPSIxMDQuOTY4MDAwMDAwMDAwMDIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxNDAzLjM2Mjk5OTk5OTk5OTgiIHk9IjExMC4wNTAwMDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+My4g7LWc7KKFIOuqqe2RnCDri6zshLEhPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlBDMSIgZGF0YS10bz0iUEMyIiBkYXRhLWxhYmVsPSLtm5TsuZwg67mE67KI7Jy866GcIFJEUCDsm5Dqsqkg7KCR7IaNIQrsoJXsg4Eg7JeF66y066GcIOychOyepe2VqCI+CiAgPHJlY3QgeD0iNTA1LjQ4MTAwMDAwMDAwMDEiIHk9Ijg3LjkiIHdpZHRoPSIxNjcuMzM4MDAwMDAwMDAwMDIiIGhlaWdodD0iNDQuNiIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1ODkuMTUwMDAwMDAwMDAwMSIgeT0iMTEwLjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSI1ODkuMTUwMDAwMDAwMDAwMSIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPu2blOy5nCDruYTrsojsnLzroZwgUkRQIOybkOqyqSDsoJHsho0hPC90c3Bhbj48dHNwYW4geD0iNTg5LjE1MDAwMDAwMDAwMDEiIGR5PSIxNC4zIj7soJXsg4Eg7JeF66y066GcIOychOyepe2VqDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlBDMiIgZGF0YS10bz0iU0VSVkVSIiBkYXRhLWxhYmVsPSLtg4jst6jtlZwg6rSA66as7J6QIOq2jO2VnOycvOuhnCDsoJDtlIQhIj4KICA8cmVjdCB4PSI5MTMuMTc4IiB5PSI5NC45IiB3aWR0aD0iMTY3LjkzMjAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iOTk3LjE0NCIgeT0iMTEwLjA1MDAwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7tg4jst6jtlZwg6rSA66as7J6QIOq2jO2VnOycvOuhnCDsoJDtlIQhPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJIQUNLRVIiIGRhdGEtbGFiZWw9Iu2VtOy7pCDwn6W3CuyZuOu2gCDsnbjthLDrhLciIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDAiIHk9Ijg0IiB3aWR0aD0iMTE4LjI3MyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iOTkuMTM2NSIgeT0iMTEwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9Ijk5LjEzNjUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7tlbTsu6Qg8J+ltzwvdHNwYW4+PHRzcGFuIHg9Ijk5LjEzNjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyZuOu2gCDsnbjthLDrhLc8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQUQiIGRhdGEtbGFiZWw9Iu2ajOyCrCDspJHslZkgQUQg7ISc67KEIOyepeyVhSDwn5GRCuyghOyCrCBQQyDrnpzshKzsm6jslrQg7J287KCcIOqwkOyXvCEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTQ5OS44NDcwMDAwMDAwMDAyIiB5PSI4NCIgd2lkdGg9IjIxOS43ODk5OTk5OTk5OTk5NiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxNjA5Ljc0MjAwMDAwMDAwMDIiIHk9IjExMC45IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNjA5Ljc0MjAwMDAwMDAwMDIiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7tmozsgqwg7KSR7JWZIEFEIOyEnOuyhCDsnqXslYUg8J+RkTwvdHNwYW4+PHRzcGFuIHg9IjE2MDkuNzQyMDAwMDAwMDAwMiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7KCE7IKsIFBDIOuenOyErOybqOyWtCDsnbzsoJwg6rCQ7Je8ITwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJOb3RlIiBkYXRhLWxhYmVsPSJOb3RlIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjI2MC4xNTcwMDAwMDAwMDAwNCIgeT0iMTY1LjgiIHdpZHRoPSI2OC42MjYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyOTQuNDciIHk9IjE4NC4yNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Tm90ZTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUEMxIiBkYXRhLWxhYmVsPSJQQzEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzk4Ljc4MyIgeT0iOTIuNDUiIHdpZHRoPSI2Mi42OTc5OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDMwLjEzMiIgeT0iMTEwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlBDMTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUEMyIiBkYXRhLWxhYmVsPSLqs7zsnqXri5ggUEMg8J+SuwrrjZQg64aS7J2AIOq2jO2VnCDthLjrprwiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNzE2LjgxOSIgeT0iODQiIHdpZHRoPSIxNTIuMzU5IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI3OTIuOTk4NDk5OTk5OTk5OSIgeT0iMTEwLjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9Ijc5Mi45OTg0OTk5OTk5OTk5IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+6rO87J6l64uYIFBDIPCfkrs8L3RzcGFuPjx0c3BhbiB4PSI3OTIuOTk4NDk5OTk5OTk5OSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+642UIOuGkuydgCDqtoztlZwg7YS466a8PC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlNFUlZFUiIgZGF0YS1sYWJlbD0i7IKs64K0IO2MjOydvCDshJzrsoQg8J+XhO+4jyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMTI1LjExMDAwMDAwMDAwMDEiIHk9IjkyLjQ1IiB3aWR0aD0iMTU5Ljc2OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTIwNC45OTQ1MDAwMDAwMDAyIiB5PSIxMTAuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7IKs64K0IO2MjOydvCDshJzrsoQg8J+XhO+4jzwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 초기 침투(수직) vs 측면 이동(수평) 전격 비교 해부 (3단 표)**

방화벽을 부수는 초기 침투와, 신분을 훔쳐 내부를 돌아다니는 측면 이동의 \*\*'공격 기법 차이'\*\*를 찌르는 것이 핵심입니다.

| **핵심 척도 (비교 잣대)**             | **🚀 1단계: 초기 침투 (Initial Access)**                                          | **🦀 2단계: 측면 이동 (Lateral Movement)**                                                                           |
| :---------------------------- | :-------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| **네트워크 이동 방향과 방어선(경계)의 위치**   | **'외부(인터넷) ➔ 내부(사내망)'의 수직 이동.** 기업을 지키는 가장 강력하고 단단한 '외부 경계 방화벽'을 뚫고 들어와야 함. | **'내부 ➔ 내부' 간의 수평(측면) 이동.** 이미 방화벽 안에 들어온 상태이므로, 부서 간 이동을 제어하는 내부망 통제가 허술할 경우 프리패스로 이동함.                       |
| **주로 사용되는 공격 스킬 및 기법**        | - 사회공학적 피싱 이메일 첨부파일. - 운영체제나 서버의 제로데이 취약점 공격. - USB를 통한 악성코드 감염.            | - 메모리에서 남의 비번 훔치기 (Mimikatz). - **훔친 자격 증명(Pass-the-Hash)을 사용.** - **OS 정상 도구 악용 (LoL, Living off the Land).** |
| **사내 보안 시스템이 해킹을 탐지하기 힘든 이유** | 백신이나 방화벽에 알려지지 않은 '신종 악성코드(제로데이)'를 사용하면 탐지를 회피할 수 있음.                       | 악성코드를 전혀 쓰지 않고, 훔친 진짜 계정으로 **정상 관리자 도구(RDP, SSH, PowerShell)를 켜서 접속하므로 '정상적인 직원의 야근/업무'로 간주됨.**                |
| **대응 및 방어 수단 (가장 중요 🚨)**     | 외부 방화벽(IPS) 강화, 스팸 메일 모의훈련.                                                 | **'마이크로 세그멘테이션(Micro-segmentation)'.** 같은 사무실 PC끼리도 접근을 통제하고, 원격 접속 시 폰으로 **다중 요소 인증(MFA)을 강제**해야 함.           |

#### **IV. \[결론/제언] 레거시 내부망의 한계 붕괴와 제로 트러스트(Zero Trust)의 완성**

* **(키워드 위주 2줄 마무리)** "측면 이동 공격의 대성공은 '성벽만 통과하면 내부는 모두 신뢰한다'는 과거 경계 기반 보안 철학이 완전히 파탄 났음을 증명합니다. 현대 기업은 내부망이라 할지라도 서버와 서버, PC와 PC 사이를 논리적으로 잘게 쪼개어(Micro-segmentation) 매 순간 권한을 검증하는 **'제로 트러스트 아키텍처'로 전환해야만 랜섬웨어의 전사적 재앙을 막을 수 있습니다.**"
