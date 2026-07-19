#### **자격증명 없는 횡적 이동 공격: 패스더해시 (Pass-the-Hash, PtH)**

---

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 "패스워드를 몰라도" 침투하는가) — 3~4줄
Ⅱ. PtH 동작 체계 (본론①, 도식 1개 필수)
Ⅲ. 변형 공격·탐지·대응 단계별 흐름 (핵심 배점)
Ⅳ. 결론
```

포인트: 개요에서 **"앞서 다룬 크리덴셜 스터핑이 '실제 패스워드를 다른 서비스에 대입하는 공격'이라면, PtH는 한 단계 더 나아가 '패스워드 자체를 몰라도 메모리에서 추출한 NTLM 해시를 인증 프로토콜에 직접 주입해 Windows 인증을 통과하는 공격'이다 — Windows의 NTLM 인증이 '해시 자체를 패스워드와 동등하게 취급하는 구조적 설계'를 악용한 것이며, 앞서 다룬 인포스틸러가 자격증명을 수평 탈취한다면 PtH는 도메인 관리자 권한까지 수직 상승(Privilege Escalation)해 Active Directory 전체를 장악하는 APT 공격의 핵심 기법"**이라는 한 줄로 시작하면, 왜 이 답안이 앞서 다룬 인포스틸러·크리덴셜 스터핑·제로트러스트·TPM 시리즈 전체의 **내부망 횡적 이동(Lateral Movement) 핵심**인지 드러납니다.

---

#### Ⅱ. PtH 동작 체계

|구성요소|내용|
|---|---|
|**NTLM 인증 구조적 취약점**|Windows NTLM 인증은 **패스워드→NTLM 해시(MD4)→챌린지-응답** 방식. 서버는 클라이언트가 올바른 해시를 알고 있으면 인증 통과 → **해시 = 패스워드 대리자** 구조. 패스워드를 몰라도 해시만 있으면 동일한 인증 효력|
|**해시 추출 (Dumping)**|앞서 다룬 **"인포스틸러의 DPAPI 복호화"**와 유사 — **lsass.exe(Local Security Authority Subsystem Service) 프로세스 메모리**에서 NTLM 해시 추출. Mimikatz·Impacket·CrackMapExec이 대표 도구. **로컬 관리자 권한**만 있으면 추출 가능|
|**해시 주입 (Injection)**|추출한 NTLM 해시를 **인증 세션에 직접 주입** → Windows가 해시를 검증하는 NTLM Challenge-Response 과정에 원래 패스워드 없이 해시만으로 응답 생성 → **인증 통과**|
|**횡적 이동 (Lateral Movement)**|앞서 다룬 **"MITRE ATT&CK T1550.002(PtH)"** — 획득한 해시로 **동일 도메인 내 다른 시스템(SMB·WMI·RDP·PSExec)에 인증** → 네트워크 전체 횡적 이동. 특히 **도메인 관리자 해시 획득 시 Active Directory 전체 장악**|
|**골든티켓 연계**|PtH로 도메인 컨트롤러 접근 후 **krbtgt 계정 NTLM 해시 탈취** → **골든티켓(Golden Ticket·Kerberos TGT 위조)** 생성 → **도메인 내 모든 서비스에 무기한 인증** 가능. APT 공격의 최종 목표|

→ 암기: **"lsass 메모리에서 NTLM 해시를 뽑아 인증 세션에 주입하면 패스워드 없이 Windows 인증을 통과하고, 도메인 관리자 해시까지 얻으면 골든티켓으로 AD 전체가 열린다 — 패스워드를 훔치는 게 아니라 패스워드의 증명서를 훔치는 것"** — 앞서 다룬 **"제로트러스트의 최소 권한 원칙"**이 PtH의 횡적 이동 범위를 제한하는 핵심 완화 수단입니다.

#### 도식화 제안

```
[PtH 전체 공격 흐름]

①초기 침투
  피싱·취약점 익스플로잇으로 일반 사용자 PC 장악
  로컬 관리자 권한 획득
       ↓
②해시 추출
  Mimikatz: sekurlsa::logonpasswords
  lsass.exe 메모리 덤프 → NTLM 해시 획득
  예) Administrator:500:NTLM_HASH_HERE
       ↓
③해시 주입·횡적 이동
  Impacket psexec.py -hashes NTLM_HASH 대상IP
  → SMB 인증 통과 (패스워드 불필요)
  → 도메인 내 서버A→서버B→서버C 횡적 이동
       ↓
④권한 상승
  도메인 컨트롤러 접근
  → krbtgt 해시 탈취
  → 골든티켓 생성
  → Active Directory 전체 장악 🚨
       ↓
⑤지속성 확보
  백도어 설치·스케줄 태스크 등록
  → 패스워드 변경해도 골든티켓은 유효 (기본 10년)
```

---

#### Ⅲ. 변형 공격·탐지·대응 단계별 흐름 — 핵심 배점

**함정 방지: "해시를 훔쳐서 인증한다"고만 답하면 절반. NTLM 챌린지-응답 프로토콜이 해시를 패스워드 대리자로 취급하는 구조적 원인, PtT(Pass-the-Ticket)·Overpass-the-Hash 변형과의 차이, lsass 보호 메커니즘과 PPL이 어떻게 해시 추출을 차단하는지를 단계별로 보여줘야 완성됩니다.**

| 단계                                | 활동                                                                                                                                                                                                                                      |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PtH 변형: PtT (Pass-the-Ticket)** | NTLM 해시 대신 **Kerberos TGT·서비스 티켓**을 추출·주입. Kerberos 환경에서 NTLM을 대체. **골든티켓(krbtgt 해시로 TGT 위조)·실버티켓(서비스 계정 해시로 서비스 티켓 위조)**이 대표 변형. 앞서 다룬 **"도메인 컨트롤러 전체 장악"**의 최종 수단                                                                     |
| **Overpass-the-Hash (OtH)**       | NTLM 해시를 사용해 **Kerberos TGT를 요청**하는 혼합 기법. NTLM이 비활성화된 환경에서 해시만으로 Kerberos 인증 우회. PtH와 PtT의 교량 역할                                                                                                                                       |
| **lsass 보호 우회**                   | Windows 10+ **PPL(Protected Process Light)** — lsass를 보호 프로세스로 실행해 관리자도 메모리 덤프 불가. 공격자 대응: **커널 드라이버 익스플로잇·BYOD(Bring Your Own Driver)** 취약 드라이버로 PPL 우회 시도 → 앞서 다룬 **"Secure Boot·TPM 측정"**으로 취약 드라이버 로드 차단                            |
| **탐지 방법**                         | 앞서 다룬 **"AI-SOC의 SIEM·UEBA"** 핵심 적용 — **이벤트 ID 4624(로그온 성공) 로그온 유형 3(네트워크)**: NTLM 인증 + 비정상 시간대·비정상 소스 조합 탐지. **이벤트 ID 10(Sysmon): lsass.exe에 대한 프로세스 접근** 탐지. **이벤트 ID 4769(Kerberos 서비스 티켓 요청)**: 비정상 암호화 유형(RC4-HMAC) 다량 요청 → PtT 징후 |
| **네트워크 분리 대응**                    | 앞서 다룬 **"제로트러스트 마이크로세그멘테이션"** — 서버 간 불필요한 SMB(445)·WMI·RPC 포트 차단. PtH로 해시를 얻어도 횡적 이동 경로 자체를 네트워크 레벨에서 차단. **LAPS(Local Administrator Password Solution)**: 각 서버의 로컬 관리자 패스워드를 자동·무작위 생성·주기 변경 → 동일 해시로 전체 서버 이동 불가                      |

→ 암기: **"PtH는 NTLM 해시, PtT는 Kerberos 티켓, OtH는 해시로 티켓을 뽑는 것 — 탐지는 이벤트 4624·10·4769, 방어는 PPL로 lsass 보호·LAPS로 해시 재사용 차단·마이크로세그멘테이션으로 이동 경로 차단"**

**LAPS와 PtH 방어 연결** (중요): 앞서 다룬 **"제로트러스트의 최소 권한"**에서 모든 서버가 동일한 로컬 관리자 패스워드를 공유하는 구조가 PtH의 최대 확산 원인이다 — **LAPS가 서버별로 다른 랜덤 패스워드를 자동 생성**하면 서버A의 로컬 관리자 해시로 서버B에 인증이 불가능해지고, 이는 앞서 다룬 **"크리덴셜 스터핑의 패스워드 재사용 악용"**과 동일한 구조적 문제를 **조직 내부 서버 레벨에서 해결**하는 것과 정확히 같은 원리입니다.

#### 도식화 제안

```
[PtH·PtT·OtH 변형 비교]

공격 기법      탈취 대상          주입 대상        환경
───────────────────────────────────────────────────────
PtH            NTLM 해시          NTLM 인증 세션   NTLM 활성화
PtT (골든티켓)  krbtgt NTLM 해시  Kerberos TGT    Kerberos 환경
PtT (실버티켓)  서비스 계정 해시   서비스 티켓     Kerberos 환경
OtH            NTLM 해시          Kerberos TGT 요청 혼합 환경

[PtH 탐지·대응 체계]

예방
  PPL: lsass 보호 프로세스 설정 (관리자도 덤프 불가)
  LAPS: 서버별 로컬 관리자 PW 자동 랜덤화 → 해시 재사용 차단
  Credential Guard (VBS): 해시를 가상 보안 경계 내 격리
  앞서 다룬 Secure Boot+TPM: 취약 드라이버 로드 차단

탐지 (SIEM 이벤트)
  ID 4624 (유형3·NTLM): 비정상 소스·시간대 필터링
  ID 10 (Sysmon): lsass 프로세스 접근 탐지
  ID 4769 (RC4-HMAC 다량): PtT 골든티켓 징후

대응 (SOAR 플레이북)
  lsass 접근 탐지 → 해당 단말 즉시 격리
  → 도메인 관리자 계정 전체 패스워드 리셋
  → krbtgt 계정 해시 2회 순차 변경 (골든티켓 무효화)
  → 마이크로세그멘테이션으로 SMB 445 포트 재검토
```

**앞서 다룬 인포스틸러·크리덴셜 스터핑·제로트러스트·AI-SOC와의 연결**: 이런 **"lsass 덤프·NTLM 해시 주입·횡적 이동·골든티켓"** 구조가 실제로는 앞서 다룬 **"인포스틸러가 초기 침투 도구로 PtH의 선행 단계"**가 되고, 앞서 다룬 **"AI-SOC의 MITRE ATT&CK T1550.002"** 탐지 룰셋이 이벤트 4624·Sysmon ID 10 상관분석으로 PtH를 탐지하며, 앞서 다룬 **"TPM의 Secure Boot"**가 Mimikatz 실행에 필요한 취약 드라이버 로드를 부팅 단계에서 차단하는 전 과정을 직접 연결합니다.

---

#### Ⅳ. 결론

패스더해시(PtH)는 **"Windows NTLM 인증이 해시를 패스워드 대리자로 취급하는 구조적 설계를 악용해 lsass 메모리에서 NTLM 해시를 추출하고 인증 세션에 직접 주입함으로써 패스워드 없이 도메인 내 횡적 이동과 권한 상승을 달성하는 내부망 공격 기법"**이며, 특히 **"PPL로 lsass를 보호 프로세스로 격리하고, LAPS로 서버별 로컬 관리자 해시를 무작위화해 재사용을 차단하고, Credential Guard로 해시를 가상 보안 경계 안에 격리하며, 마이크로세그멘테이션으로 SMB 횡적 이동 경로를 차단하는 4중 방어"**가 핵심입니다 — 이는 앞서 다룬 **인포스틸러(초기 침투·로컬 권한 획득) → PtH(해시 추출·횡적 이동) → 골든티켓(AD 전체 장악) → PPL·LAPS·Credential Guard(기술적 방어) → 제로트러스트 마이크로세그멘테이션(네트워크 방어) → AI-SOC SIEM 이벤트 상관분석(탐지)**을 하나로 잇는 내부망 공격 체인의 실무적 교량이며, **"패스워드를 바꿔도 해시가 메모리에 남는 한 PtH는 유효하며, 유일한 근본 해결책은 Credential Guard로 해시를 가상 격리하고 Kerberos만 허용해 NTLM 자체를 비활성화하는 것"**이라는 결론으로 이어집니다.




### **I. 윈도우 인증의 허점을 노린 측면 이동 기법, 패스더해시(PtH)의 개요**

**패스더해시(Pass the Hash, PtH)**는 공격자가 시스템 평문(Plaintext) 비밀번호를 해독하지 않고, 탈취한 사용자의 NTLM 암호화 해시값을 그대로 인증 시스템에 제출하여 원격 시스템의 접근 권한을 획득하는 측면 이동(Lateral Movement) 기법입니다. 주로 윈도우 환경에서 로컬 관리자 계정의 자격증명이 여러 시스템에 공유되어 있고, 인증 과정에서 해시값 자체를 비밀번호 대용으로 사용하는 취약점을 악용합니다.

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NjMuMzAwMTY2NjY2NjY2NyAxMTA0Ljg5OTk5OTk5OTk5OTkiIHdpZHRoPSI1NjMuMzAwMTY2NjY2NjY2NyIgaGVpZ2h0PSIxMTA0Ljg5OTk5OTk5OTk5OTkiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IkNvbXByb21pc2UiIGRhdGEtbGFiZWw9IjEuIOy0iOq4sCDsuajtiKwg67CPIO2VtOyLnCDtmo3rk50iPgogIDxyZWN0IHg9IjEwNy41IiB5PSI1OCIgd2lkdGg9IjM1My4yMzM0OTk5OTk5OTk5NCIgaGVpZ2h0PSI0MDMuMjk5OTk5OTk5OTk5OTUiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSIxMDcuNSIgeT0iNTgiIHdpZHRoPSIzNTMuMjMzNDk5OTk5OTk5OTQiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjExOS41IiB5PSI3MiIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij4xLiDstIjquLAg7Lmo7YisIOuwjyDtlbTsi5wg7ZqN65OdPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iQXV0aGVudGljYXRpb24iIGRhdGEtbGFiZWw9IjIuIOyduOymnSDsmrDtmowgKFBhc3MgdGhlIEhhc2gpIj4KICA8cmVjdCB4PSIyMTMuMDE4OTk5OTk5OTk5OTgiIHk9IjU4OS41OTk5OTk5OTk5OTk5IiB3aWR0aD0iMjQ1LjEyMDk5OTk5OTk5OTk4IiBoZWlnaHQ9Ijk2LjkiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSIyMTMuMDE4OTk5OTk5OTk5OTgiIHk9IjU4OS41OTk5OTk5OTk5OTk5IiB3aWR0aD0iMjQ1LjEyMDk5OTk5OTk5OTk4IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyMjUuMDE4OTk5OTk5OTk5OTgiIHk9IjYwMy41OTk5OTk5OTk5OTk5IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjIuIOyduOymnSDsmrDtmowgKFBhc3MgdGhlIEhhc2gpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iTGF0ZXJhbCIgZGF0YS1sYWJlbD0iMy4g7Lih66m0IOydtOuPmSAoTGF0ZXJhbCBNb3ZlbWVudCkiPgogIDxyZWN0IHg9IjIxOC44OTkxNjY2NjY2NjY2NyIgeT0iODE0LjgiIHdpZHRoPSIzMDQuNDAwOTk5OTk5OTk5OTUiIGhlaWdodD0iMjUwLjEiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSIyMTguODk5MTY2NjY2NjY2NjciIHk9IjgxNC44IiB3aWR0aD0iMzA0LjQwMDk5OTk5OTk5OTk1IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyMzAuODk5MTY2NjY2NjY2NjciIHk9IjgyOC44IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjMuIOy4oeuptCDsnbTrj5kgKExhdGVyYWwgTW92ZW1lbnQpPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJOVExNSGFzaCIgZGF0YS10bz0iVGFyZ2V0U2VydmVyIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsnbjspp0g7JqU7LKtIOuwnOyGoSIgcG9pbnRzPSIyOTkuMTk0ODMzMzMzMzMzMyw0NDUuMjk5OTk5OTk5OTk5OTUgMjk5LjE5NDgzMzMzMzMzMzM1LDUwMy4yOTk5OTk5OTk5OTk5NSAyNjkuODMyNSw1MDMuMjk5OTk5OTk5OTk5OTUgMjY5LjgzMjUsNTcxLjU5OTk5OTk5OTk5OTkgMzAwLjA1OTMzMzMzMzMzMzM3LDU3MS41OTk5OTk5OTk5OTk5IDMwMC4wNTkzMzMzMzMzMzMzLDYzMy41OTk5OTk5OTk5OTk5IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJUYXJnZXRTZXJ2ZXIiIGRhdGEtdG89Ik5UTE1IYXNoIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsnbjspp0g7KeI66y4IChDaGFsbGVuZ2UpIiBwb2ludHM9IjMwMC4wNTkzMzMzMzMzMzMzLDY3MC40OTk5OTk5OTk5OTk5IDMwMC4wNTkzMzMzMzMzMzMzNyw3OTYuNzk5OTk5OTk5OTk5OCA5Ny41LDc5Ni43OTk5OTk5OTk5OTk4IDk3LjUsNDAgNDA5LjYwNiw0MCA0MDkuNjA1OTk5OTk5OTk5OTQsMzcyLjQgMzcxLjk2NDE2NjY2NjY2NjY0LDM3Mi40IDM3MS45NjQxNjY2NjY2NjY2NCw0MDguNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTlRMTUhhc2giIGRhdGEtdG89IlRhcmdldFNlcnZlciIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7ZW07IucIOyXsOyCsCDtm4Qg7J2R64u1IChSZXNwb25zZSkiIHBvaW50cz0iMzcxLjk2NDE2NjY2NjY2NjY0LDQ0NS4yOTk5OTk5OTk5OTk5NSAzNzEuOTY0MTY2NjY2NjY2NjQsNTAzLjI5OTk5OTk5OTk5OTk1IDQwMS4zMjY1LDUwMy4yOTk5OTk5OTk5OTk5NSA0MDEuMzI2NSw1NzEuNTk5OTk5OTk5OTk5OSAzNzEuMDk5NjY2NjY2NjY2Niw1NzEuNTk5OTk5OTk5OTk5OSAzNzEuMDk5NjY2NjY2NjY2Niw2MzMuNTk5OTk5OTk5OTk5OSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVGFyZ2V0U2VydmVyIiBkYXRhLXRvPSJBY2Nlc3MiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyduOymnSDshLHqs7UiIHBvaW50cz0iMzcxLjA5OTY2NjY2NjY2NjYsNjcwLjQ5OTk5OTk5OTk5OTkgMzcxLjA5OTY2NjY2NjY2NjYsODU4LjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkF0dGFja2VyIiBkYXRhLXRvPSJMU0EiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IkxTQVNTIOuplOuqqOumrCDrjaTtlIQgLyBNaW1pa2F0eiIgcG9pbnRzPSIyNjEuNTUzLDEzOC45IDI2MS41NTMsMjU1LjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkxTQSIgZGF0YS10bz0iTlRMTUhhc2giIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9Ik5UTE0g7ZW07IucIO2ajeuTnSIgcG9pbnRzPSIyNjEuNTUzLDI5Mi4xIDI2MS41NTMsMzcyLjQgMjk5LjE5NDgzMzMzMzMzMzMsMzcyLjQgMjk5LjE5NDgzMzMzMzMzMzMsNDA4LjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkFjY2VzcyIgZGF0YS10bz0iRG9tYWluRG9taW5hbmNlIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLstpTqsIAg7Iuc7Iqk7YWcIOyepeyVhSIgcG9pbnRzPSIzNzEuMDk5NjY2NjY2NjY2Niw4OTUuNjk5OTk5OTk5OTk5OSAzNzEuMDk5NjY2NjY2NjY2NiwxMDEyIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209Ik5UTE1IYXNoIiBkYXRhLXRvPSJUYXJnZXRTZXJ2ZXIiIGRhdGEtbGFiZWw9IuyduOymnSDsmpTssq0g67Cc7IahIj4KICA8cmVjdCB4PSIyMjMuMzMyNDk5OTk5OTk5OTIiIHk9IjUxMC4yOTk5OTk5OTk5OTk5NSIgd2lkdGg9IjkyLjQ5NDAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMjY5LjU3OTQ5OTk5OTk5OTk0IiB5PSI1MjUuNDQ5OTk5OTk5OTk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7J247KadIOyalOyyrSDrsJzshqE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iVGFyZ2V0U2VydmVyIiBkYXRhLXRvPSJOVExNSGFzaCIgZGF0YS1sYWJlbD0i7J247KadIOyniOusuCAoQ2hhbGxlbmdlKSI+CiAgPHJlY3QgeD0iMzUuOTk5OTk5OTk5OTk5OTkiIHk9Ijc1OS41IiB3aWR0aD0iMTIyLjE5NDAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iOTcuMDk3MDAwMDAwMDAwMDEiIHk9Ijc3NC42NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7J247KadIOyniOusuCAoQ2hhbGxlbmdlKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJOVExNSGFzaCIgZGF0YS10bz0iVGFyZ2V0U2VydmVyIiBkYXRhLWxhYmVsPSLtlbTsi5wg7Jew7IKwIO2bhCDsnZHri7UgKFJlc3BvbnNlKSI+CiAgPHJlY3QgeD0iMzE5LjgyNjUiIHk9IjUxMC4yOTk5OTk5OTk5OTk5NSIgd2lkdGg9IjE2Mi41ODYwMDAwMDAwMDAwNCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjQwMS4xMTk1IiB5PSI1MjUuNDQ5OTk5OTk5OTk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7ZW07IucIOyXsOyCsCDtm4Qg7J2R64u1IChSZXNwb25zZSk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iVGFyZ2V0U2VydmVyIiBkYXRhLXRvPSJBY2Nlc3MiIGRhdGEtbGFiZWw9IuyduOymnSDshLHqs7UiPgogIDxyZWN0IHg9IjMzNy41OTk2NjY2NjY2NjY2IiB5PSI3MzUuNSIgd2lkdGg9IjY2Ljk1MiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjM3MS4wNzU2NjY2NjY2NjY2IiB5PSI3NTAuNjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuyduOymnSDshLHqs7U8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQXR0YWNrZXIiIGRhdGEtdG89IkxTQSIgZGF0YS1sYWJlbD0iTFNBU1Mg66mU66qo66asIOuNpO2UhCAvIE1pbWlrYXR6Ij4KICA8cmVjdCB4PSIxNzkuNTUyOTk5OTk5OTk5OTQiIHk9IjE4MS45IiB3aWR0aD0iMTYzLjc3NCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjI2MS40Mzk5OTk5OTk5OTk5NCIgeT0iMTk3LjA1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5MU0FTUyDrqZTrqqjrpqwg642k7ZSEIC8gTWltaWthdHo8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iTFNBIiBkYXRhLXRvPSJOVExNSGFzaCIgZGF0YS1sYWJlbD0iTlRMTSDtlbTsi5wg7ZqN65OdIj4KICA8cmVjdCB4PSIyMTEuNTUzIiB5PSIzMzUuMSIgd2lkdGg9Ijk5LjAyOCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjI2MS4wNjciIHk9IjM1MC4yNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+TlRMTSDtlbTsi5wg7ZqN65OdPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkFjY2VzcyIgZGF0YS10bz0iRG9tYWluRG9taW5hbmNlIiBkYXRhLWxhYmVsPSLstpTqsIAg7Iuc7Iqk7YWcIOyepeyVhSI+CiAgPHJlY3QgeD0iMzE4LjU5OTY2NjY2NjY2NjYiIHk9IjkzOC42OTk5OTk5OTk5OTk5IiB3aWR0aD0iMTA0LjM3NDAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzcwLjc4NjY2NjY2NjY2NjYzIiB5PSI5NTMuODQ5OTk5OTk5OTk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7LaU6rCAIOyLnOyKpO2FnCDsnqXslYU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkF0dGFja2VyIiBkYXRhLWxhYmVsPSLqs7XqsqnsnpAgKOuhnOy7rCDqtIDrpqzsnpAg6raM7ZWcIO2ajeuTnSkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTQzLjUwNjk5OTk5OTk5OTk4IiB5PSIxMDIiIHdpZHRoPSIyMzYuMDkxOTk5OTk5OTk5OTgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyNjEuNTUzIiB5PSIxMjAuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuqzteqyqeyekCAo66Gc7LusIOq0gOumrOyekCDqtoztlZwg7ZqN65OdKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTFNBIiBkYXRhLWxhYmVsPSJTQU0g642w7J207YSw67Kg7J207IqkIC8gTFNBU1Mg7ZSE66Gc7IS47IqkIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjEyMy41IiB5PSIyNTUuMiIgd2lkdGg9IjI3Ni4xMDU5OTk5OTk5OTk5NCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI2MS41NTMiIHk9IjI3My42NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+U0FNIOuNsOydtO2EsOuyoOydtOyKpCAvIExTQVNTIO2UhOuhnOyEuOyKpDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTlRMTUhhc2giIGRhdGEtbGFiZWw9Ik5UTE0g7ZW07IucIChQbGFpbnRleHQg67aI7ZWE7JqUKSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyMjYuNDI1NDk5OTk5OTk5OTciIHk9IjQwOC40IiB3aWR0aD0iMjE4LjMwOCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjYzYyODI4IiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIzMzUuNTc5NDk5OTk5OTk5OTQiIHk9IjQyNi44NDk5OTk5OTk5OTk5NyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+TlRMTSDtlbTsi5wgKFBsYWludGV4dCDrtojtlYTsmpQpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJUYXJnZXRTZXJ2ZXIiIGRhdGEtbGFiZWw9IuuMgOyDgSDsi5zsiqTthZwgKFRhcmdldCBTZXJ2ZXIpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjIyOS4wMTg5OTk5OTk5OTk5OCIgeT0iNjMzLjU5OTk5OTk5OTk5OTkiIHdpZHRoPSIyMTMuMTIwOTk5OTk5OTk5OTgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlY2VmZjEiIHN0cm9rZT0iIzM3NDc0ZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMzM1LjU3OTQ5OTk5OTk5OTk0IiB5PSI2NTIuMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuuMgOyDgSDsi5zsiqTthZwgKFRhcmdldCBTZXJ2ZXIpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBY2Nlc3MiIGRhdGEtbGFiZWw9IuuMgOyDgSDsi5zsiqTthZwg7JuQ6rKpIOygnOyWtCAoV01JIC8gUHNFeGVjKSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyMzQuODk5MTY2NjY2NjY2NjciIHk9Ijg1OC44IiB3aWR0aD0iMjcyLjQwMDk5OTk5OTk5OTk1IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzcxLjA5OTY2NjY2NjY2NjYiIHk9Ijg3Ny4yNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+64yA7IOBIOyLnOyKpO2FnCDsm5Dqsqkg7KCc7Ja0IChXTUkgLyBQc0V4ZWMpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJEb21haW5Eb21pbmFuY2UiIGRhdGEtbGFiZWw9IuuPhOuplOyduCDsnqXslYUgKERvbWFpbiBDb250cm9sbGVyKSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIyNTQuOTA2MTY2NjY2NjY2NjgiIHk9IjEwMTIiIHdpZHRoPSIyMzIuMzg2OTk5OTk5OTk5OTQiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzJlN2QzMiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMzcxLjA5OTY2NjY2NjY2NjYiIHk9IjEwMzAuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuuPhOuplOyduCDsnqXslYUgKERvbWFpbiBDb250cm9sbGVyKTwvdGV4dD4KPC9nPgo8L3N2Zz4=)

---

### **II. 패스더해시의 핵심 단계 및 메커니즘**

|**단계**|**🔑 해시 정보 수집 (Credential Dumping) 💾**|**📡 NTLM 프로토콜 인증 우회 🛡️**|**🚀 측면 이동 및 권한 상승 (Lateral Movement) 🎯**|
|---|---|---|---|
|**설명**|최초로 침투한 시스템의 로컬 메모리나 데이터베이스에서 계정의 암호화 해시(NTLM)를 추출하는 단계|획득한 해시값을 일반 텍스트 비밀번호 대신 인증 모듈에 입력하여 대상 서버와 인증 과정을 거치는 단계|인증에 성공한 세션을 기반으로 타 시스템에 원격 명령을 실행하여 네트워크 내 지배력을 넓히는 단계|
|**기술적 핵심**|LSASS 프로세스 메모리 접근 또는 SAM(Security Account Manager) 파일의 레지스트리 덤프 수행|NTLM Challenge-Response 프로토콜 인증 과정에서 비밀번호 원본 대신 수집된 NTLM 해시값을 사용해 Response 값 연산 및 전송|`Mimikatz`, `Impacket (psexec, wmiexec)` 등을 활용하여 원격 프로세스 실행 및 쉘 획득|
|**탐지 및 취약성**|LSASS 프로세스에 대한 디버그 권한 요청 등 비정상 메모리 접근 행위 탐지 가능|NTLMv1/v2 프로토콜을 비활성화하지 않았거나, 원격 인증 시 해시값만 요구하는 윈도우 인증 기본 취약점 악용|로컬 관리자(Administrator) 계정의 비밀번호가 모든 기기에서 동일하게 설정되어 있는 경우 급속도로 확산|

---

### **III. 패스더해시(PtH)와 유사 공격 기법의 비교**

|**비교 항목**|**💥 패스더해시 (Pass the Hash, PtH)**|**🎫 패스더티켓 (Pass the Ticket, PtT)**|**🔑 패스더키 (Pass the Key, PtK)**|
|---|---|---|---|
|**주요 타깃 대상**|윈도우 로컬 계정 및 액티브 디렉터리(AD) 도메인 계정|Kerberos 프로토콜을 사용하는 AD 도메인 서비스|Kerberos 프로토콜 환경의 암호화 키 인증 구조|
|**인증 프로토콜**|NTLM (NT Lan Manager) 프로토콜|Kerberos 프로토콜|Kerberos 프로토콜 (AES-256 키 등)|
|**필요한 자격 증명**|NTLM Hash (LM/NTLM 해시값)|Kerberos TGT (Ticket Granting Ticket) 또는 서비스 티켓|AES 또는 DES 암호화 키 (Kerberos Key)|
|**주요 공격 대상 위치**|SAM DB 및 LSASS 메모리 내부|LSASS 메모리 내에 캐싱된 티켓 정보|LSASS 메모리 및 레지스트리 내 저장된 마스터 암호 키|

---

### **IV. 패스더해시(PtH) 방어를 위한 기술 가이드라인**

**IMPORTANT**

1. **로컬 관리자 계정 격리 및 LAPS(Local Administrator Password Solution) 도입**: 공격자가 한 대의 PC에서 로컬 관리자(Administrator) 해시를 획득했을 때 다른 PC로 확산되는 것을 막아야 합니다. 마이크로소프트의 LAPS를 도입하여 각 호스트별로 로컬 관리자 비밀번호를 서로 다르게 자동 변경 및 관리해야 합니다.
2. **NTLM 인증 비활성화 및 Credential Guard 가동**: AD 환경에서 취약한 NTLM 인증 메커니즘을 그룹 정책을 통해 비활성화하고, 상호 인증 및 암호화가 보장되는 **Kerberos** 프로토콜로 완전히 전환해야 합니다. 또한, 윈도우의 가상화 기반 보안 기술인 **Credential Guard**를 활성화하여 LSASS 메모리에서 해시값이 무단 유출되는 것을 차단해야 합니다.