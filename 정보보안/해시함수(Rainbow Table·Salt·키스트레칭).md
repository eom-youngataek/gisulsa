### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (해시함수정의,암호화와의근본적차이) — 3~4줄
Ⅱ. Rainbow Table - 공격기법 (본론①, 도식 1개 필수)
Ⅲ. Salt - 1차방어 (본론②, 핵심 배점)
Ⅳ. 키스트레칭 - 2차방어(시간지연)
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬대칭/비대칭암호는 '키가있으면반드시원본으로되돌릴수있다'는게전제였는데, 해시함수는 '어떤키로도절대되돌릴수없다'는게목적 — 비밀번호를저장할때 원본을저장하는대신 해시값만저장해, 서버가털려도비밀번호원본은알수없게하는것"\*\*이라는한줄로시작하면, 왜해시가암호화와 다른카테고리인지드러납니다.

### Ⅱ. Rainbow Table — 공격기법

| 개념                | 내용                                                                         |
| :---------------- | :------------------------------------------------------------------------- |
| **문제상황**          | 해시는 **되돌릴수없지만**, 공격자는 **"평문→해시값"의방대한대응표를미리만들어두면**, 해시값만보고 **역으로평문을찾아낼수있음** |
| **Rainbow Table** | 가능한모든평문(비밀번호후보)의 **해시값을미리계산해저장한거대한사전**                                     |
| **공격방식**          | 탈취한 **해시값을Rainbow Table에서검색**만하면 → 원본비밀번호를 **즉시역추적**                       |

→ 암기: **"해시를못풀지만, 미리모든답을계산해둔사전을찾아보면풀린다"** — 이는 앞서다룬 \*\*"McCabe순환복잡도"\*\*의계산가능성과는 다른차원의문제: \*\*"계산자체는쉬운데, 그계산을미리엄청많이해두면 무차별대입보다훨씬빨라진다"\*\*는 시간-저장공간트레이드오프를 악용하는공격입니다.

### 도식화 제안

```
[Rainbow Table 공격]
[사전준비] "123456"→해시값A, "password"→해시값B, ... (수십억개미리계산)
[탈취한해시값] = 해시값A
[테이블조회] 해시값A → "123456" (즉시매칭,역산불필요)
```

### Ⅲ. Salt — 1차방어, 핵심 배점

**함정 방지: "Salt를추가한다"고만답하면절반. Salt가 Rainbow Table을 왜무력화시키는지원리를보여줘야완성됩니다.**

| 개념       | 내용                                                            |
| :------- | :------------------------------------------------------------ |
| **Salt** | 비밀번호마다 **고유한무작위값**을붙여서 **함께해시화**                              |
| **동작원리** | `Hash(비밀번호+Salt)` — 같은비밀번호("123456")라도 **Salt가다르면완전히다른해시값**생성 |
| **저장방식** | Salt는 **암호화되지않은채로 해시값과함께저장**(비밀이아님,단지고유성만필요)                  |

→ 암기: **"같은비밀번호라도, 사람마다다른소금을쳐서 완전히다른맛(해시값)이나오게한다"** — Rainbow Table은 **"평문→해시"의고정된대응관계**를전제로만들어지는데, Salt가있으면 **사용자마다다른대응관계**가되어 **"미리계산해둔사전표자체가무의미**해집니다 — **공격자가Salt값마다 별도의Rainbow Table을새로만들어야하는데, 이는사실상불가능**합니다.

### 도식화 제안

```
[Salt없이]                          [Salt적용]
"123456" → 해시값A (모든사용자동일)     "123456"+Salt1(사용자1) → 해시값X
                                    "123456"+Salt2(사용자2) → 해시값Y
Rainbow Table로 즉시역산가능           (같은비밀번호도사용자마다완전히다른해시값
                                     → 미리계산한테이블이무용지물)
```

### Ⅳ. 키스트레칭 — 2차방어(시간지연)

**함정 방지: "Salt만있으면충분하다"고생각하면절반. Salt도 무차별대입(Brute-force)자체는못막는다는걸짚고, 키스트레칭이 왜필요한지보여줘야완성됩니다.**

| 개념         | 내용                                                                                                                    |
| :--------- | :-------------------------------------------------------------------------------------------------------------------- |
| **문제상황**   | Salt가있어도, 공격자가 **특정사용자한명의Salt를알면**, 그Salt로 \*\*직접무차별대입(Brute-force)\*\*시도가능 — 일반해시(SHA-256등)는 **연산이너무빨라서** 초당수십억번시도가능 |
| **키스트레칭**  | 해시연산을 **의도적으로수천\~수만번반복**시켜, **한번의시도자체를느리게만듦**                                                                         |
| **대표알고리즘** | **PBKDF2,bcrypt,scrypt,Argon2** — 반복횟수(cost factor)를조절가능                                                              |

→ 암기: **"한번추측하는데걸리는시간을 일부러늘려서, 무차별대입전체소요시간을감당못하게만든다"** — 앞서다룬 \*\*"암호비트강도"\*\*논리와유사하게, **"공격자의시도횟수자체는못막아도,시도당비용(시간)을높여 전체공격을비현실적으로만드는"** 전략입니다.

### 도식화 제안

```
[일반해시(SHA-256)]                    [키스트레칭(bcrypt등)]
1회해시연산 = 0.000001초                 1회해시연산 = 반복1만번 = 0.1초
초당10억번시도가능                        초당10번시도만가능
     ↓                                      ↓
전체비밀번호공간 대입 = 수시간              전체비밀번호공간 대입 = 수백년
```

### Ⅴ. 결론 포인트 (암호·보안 시리즈 완결)

Rainbow Table→Salt→키스트레칭은 **"공격자가시간을줄이려는시도"와 "방어자가그시간을다시늘리려는대응"의 3단계공방전**입니다 — Rainbow Table(미리계산으로시간단축)→Salt(그미리계산자체를무효화)→키스트레칭(설령직접시도해도,시도자체를느리게만듦)으로 이어지는 이흐름은, 앞서다룬 \*\*"쇼어알고리즘(계산복잡도를낮추는공격) vs PQC(다시복잡도를높이는방어)"\*\*와 동일한 **"공격기술과방어기술이서로를무력화하려경쟁하는"** 암호학전반의근본구조를 보여줍니다 — 오늘하루다룬 대칭/비대칭암호→동형암호→PQC/QKD→ECC→블록암호모드→해시함수(Rainbow Table/Salt/키스트레칭)로이어지는 방대한암호·보안시리즈전체가, \*\*"완벽한암호는없고, 공격과방어가끝없이서로를앞지르려경쟁하는 살아있는전쟁터"\*\*라는 결론으로 마무리됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "우리가 웹사이트에 가입할 때 입력한 비밀번호 '1234'는 해시함수를 거쳐 알 수 없는 암호문으로 변환되어 서버 DB에 저장된다. 해시함수는 일방향(단방향)이라 절대 원래 글자로 복호화(해독)할 수 없으니 안전할까? 천만의 말씀이다. 전 세계의 해커들은 바보가 아니다. 그들은 이미 '1234', 'password' 같은 수십억 개의 흔한 비밀번호를 미리 해시값으로 변환해 둔 거대한 엑셀 표, \*\*'레인보우 테이블(Rainbow Table)'\*\*을 훈장처럼 들고 다닌다. 만약 서버 DB가 털리면, 해커는 굳이 해독할 필요 없이 이 엑셀 표에서 'Ctrl+F' 검색만으로 내 비밀번호를 단 1초 만에 찾아내 버린다. 이 무서운 레인보우 테이블 공격을 박살 내기 위해 보안 전문가들은 두 가지 위대한 방어막을 고안했다. 첫 번째 방패는 \*\*'솔팅(Salting)'\*\*이다. 요리할 때 소금을 치듯, 내 비밀번호 '1234' 뒤에 'X9!q' 같은 랜덤한 잡동사니 문자열(Salt)을 억지로 이어 붙여서 해시를 돌리는 것이다. 이렇게 되면 값이 완전히 틀어지므로 해커가 미리 만들어둔 엑셀 표는 완벽히 쓸모없는 휴지조각이 된다. 두 번째 방패는 \*\*'키 스트레칭(Key Stretching)'\*\*이다. 해시를 1번만 돌리고 끝내는 게 아니라, 10만 번, 20만 번 연속으로 뺑뺑이를 돌리는 것이다. 정상적인 사용자는 로그인할 때 0.1초만 기다리면 되지만, 해커가 이 시스템을 뚫으려고 새로운 레인보우 표를 만들기 위해 수십억 개의 단어를 10만 번씩 돌리려면 슈퍼컴퓨터로도 수십 년이 걸린다. 즉, 해커를 늙어 죽게 만드는 '시간 지연 전술'이다. 이 솔팅과 스트레칭을 하나로 융합한 기술이 바로 현대 비밀번호 저장의 헌법인 'bcrypt'다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 복호화가 안 되는데 왜 털리는가? 해시함수와 레인보우 테이블의 위협**

* **해시함수의 맹점:** 입력값이 같으면 항상 동일한 출력값(해시값)을 뱉어내는 결정론적 특성 때문에, 해커가 유추하기 쉬운 짧은 비밀번호는 매우 위험함.
* **레인보우 테이블 공격 (Rainbow Table Attack):** 해커가 수십억 개의 평문(비밀번호)과 그에 대응하는 해시값의 쌍을 **미리 엑셀 표(사전, Dictionary)처럼 구축**해 둔 뒤, 탈취한 DB의 해시값을 이 표에서 1초 만에 매칭(검색)하여 원본 비밀번호를 역추적해 내는 치명적인 해킹 기법.

#### **II. \[본론 1] 레인보우 테이블을 찢어버리는 방패: Salt와 Stretching (도식화)**

단순히 비밀번호만 넣는 것이 아니라, 소금을 치고 뺑뺑이를 돌리는 과정을 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NDYuNDAxOTk5OTk5OTk5OSAxMjc0LjcxNjk5OTk5OTk5OTkiIHdpZHRoPSI1NDYuNDAxOTk5OTk5OTk5OSIgaGVpZ2h0PSIxMjc0LjcxNjk5OTk5OTk5OTkiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9fX19fX18iIGRhdGEtbGFiZWw9Iu2VtOy7pOydmCDroIjsnbjrs7TsmrAg7YWM7J2067iU7J2EIO2MjOq0tO2VmOuKlCDtmITrjIAg67mE67CA67KI7Zi4IOyVlO2YuO2ZlCDtjIzsnbTtlITrnbzsnbgiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjQ2Ni40MDE5OTk5OTk5OTk5MyIgaGVpZ2h0PSIxMTk0LjcxNjk5OTk5OTk5OTkiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI0NjYuNDAxOTk5OTk5OTk5OTMiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7tlbTsu6TsnZgg66CI7J2467O07JqwIO2FjOydtOu4lOydhCDtjIzqtLTtlZjripQg7ZiE64yAIOu5hOuwgOuyiO2YuCDslZTtmLjtmZQg7YyM7J207ZSE65287J24PC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJQIiBkYXRhLXRvPSJTMSIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0MDAuNTE0LDIyMiA0MDAuNTE0LDIzNCAzMzkuNTUwNjY2NjY2NjY2NjQsMjM0IDMzOS41NTA2NjY2NjY2NjY2NCwzMDIuNDgwNjY2NjY2NjY2NjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlNBTFQiIGRhdGEtdG89IlMxIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSIyMTMuNjI2LDIyMiAyMTMuNjI2LDIzNCAyNzQuNTg5MzMzMzMzMzMzMzQsMjM0IDI3NC41ODkzMzMzMzMzMzMzNCwzMDIuNDgwNjY2NjY2NjY2NjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUzEiIGRhdGEtdG89IkgxIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSInMTIzNGs5I1EnIOyDneyEsQrtlbTsu6TsnZgg6riw7KG0IOyXkeyFgO2RnCDrsJXsgrQhIiBwb2ludHM9IjMwNy4wNyw0NjQuODg0IDMwNy4wNyw1OTUuNDg0IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJIMSIgZGF0YS10bz0iUzIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMzA3LjA3LDYzMi4zODQgMzA3LjA3LDY4MC4zODQiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlMyIiBkYXRhLXRvPSJIMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i64KY7JioIOqysOqzvOulvCDrmJAg7ZW07Iuc7ZWoIQpIKEgoSCguLi4pKSkiIHBvaW50cz0iMzA3LjA3LDg2Ny4xMTcgMzA3LjA3LDk5Ny43MTciIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkgyIiBkYXRhLXRvPSJEQiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i7ZW07Luk64qUIOydtCDsl7DsgrAg7ZWY64uk6rCAIOuKmeyWtOyjveydjCIgcG9pbnRzPSIzMDcuMDcsMTAzNC42MTcgMzA3LjA3LDExNTAuOTE3IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlMxIiBkYXRhLXRvPSJIMSIgZGF0YS1sYWJlbD0iJzEyMzRrOSNRJyDsg53shLEK7ZW07Luk7J2YIOq4sOyhtCDsl5HshYDtkZwg67CV7IK0ISI+CiAgPHJlY3QgeD0iMjM0LjU3IiB5PSI1MDcuODgzOTk5OTk5OTk5OTYiIHdpZHRoPSIxNDQuMTcyMDAwMDAwMDAwMDMiIGhlaWdodD0iNDQuNiIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzMDYuNjU2IiB5PSI1MzAuMTg0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIj48dHNwYW4geD0iMzA2LjY1NiIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPiYjMzk7MTIzNGs5I1EmIzM5OyDsg53shLE8L3RzcGFuPjx0c3BhbiB4PSIzMDYuNjU2IiBkeT0iMTQuMyI+7ZW07Luk7J2YIOq4sOyhtCDsl5HshYDtkZwg67CV7IK0ITwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlMyIiBkYXRhLXRvPSJIMiIgZGF0YS1sYWJlbD0i64KY7JioIOqysOqzvOulvCDrmJAg7ZW07Iuc7ZWoIQpIKEgoSCguLi4pKSkiPgogIDxyZWN0IHg9IjI0MC41NyIgeT0iOTEwLjExNyIgd2lkdGg9IjEzMi4yOTIwMDAwMDAwMDAwMyIgaGVpZ2h0PSI0NC42IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjMwNi43MTYiIHk9IjkzMi40MTY5OTk5OTk5OTk5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIj48dHNwYW4geD0iMzA2LjcxNiIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPuuCmOyYqCDqsrDqs7zrpbwg65iQIO2VtOyLnO2VqCE8L3RzcGFuPjx0c3BhbiB4PSIzMDYuNzE2IiBkeT0iMTQuMyI+SChIKEgoLi4uKSkpPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iSDIiIGRhdGEtdG89IkRCIiBkYXRhLWxhYmVsPSLtlbTsu6TripQg7J20IOyXsOyCsCDtlZjri6TqsIAg64qZ7Ja07KO97J2MIj4KICA8cmVjdCB4PSIyMTcuMDciIHk9IjEwNzcuNjE3IiB3aWR0aD0iMTc5LjIxODAwMDAwMDAwMDA1IiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzA2LjY3OTAwMDAwMDAwMDAzIiB5PSIxMDkyLjc2NyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7ZW07Luk64qUIOydtCDsl7DsgrAg7ZWY64uk6rCAIOuKmeyWtOyjveydjDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUCIgZGF0YS1sYWJlbD0i7IKs7Jqp7J6QIOu5hOuwgOuyiO2YuCDtj4nrrLgKJzEyMzQnIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjMxMC42MjYiIHk9IjE2OC4yIiB3aWR0aD0iMTc5Ljc3NTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0MDAuNTEzOTk5OTk5OTk5OTUiIHk9IjE5NS4xIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0MDAuNTEzOTk5OTk5OTk5OTUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7sgqzsmqnsnpAg67mE67CA67KI7Zi4IO2PieusuDwvdHNwYW4+PHRzcGFuIHg9IjQwMC41MTM5OTk5OTk5OTk5NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+JiMzOTsxMjM0JiMzOTs8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzEiIGRhdGEtbGFiZWw9Iuuwqe2MqCAxOiDshpTtjIUgU2FsdGluZyDwn6eCIiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjMwNy4wNywyNzAgNDA0LjUxMiwzNjcuNDQyIDMwNy4wNyw0NjQuODg0IDIwOS42MjgsMzY3LjQ0MiIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIzMDcuMDciIHk9IjM2Ny40NDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuuwqe2MqCAxOiDshpTtjIUgU2FsdGluZyDwn6eCPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJTQUxUIiBkYXRhLWxhYmVsPSLrnpzrjaQg7IaM6riI6rCSCuyYiDogJ2s5I1EnIiBkYXRhLXNoYXBlPSJjaXJjbGUiPgogIDxjaXJjbGUgY3g9IjIxMy42MjYiIGN5PSIxNTMiIHI9IjY5IiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyMTMuNjI2IiB5PSIxNTMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjIxMy42MjYiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7rnpzrjaQg7IaM6riI6rCSPC90c3Bhbj48dHNwYW4geD0iMjEzLjYyNiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7JiIOiAmIzM5O2s5I1EmIzM5OzwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJIMSIgZGF0YS1sYWJlbD0i7ZW07IucIDHrsogg7Iuk7ZaJIPCflJIiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjM2LjgxODUiIHk9IjU5NS40ODQiIHdpZHRoPSIxNDAuNTAzIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzA3LjA3IiB5PSI2MTMuOTM0MDAwMDAwMDAwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7ZW07IucIDHrsogg7Iuk7ZaJIPCflJI8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlMyIiBkYXRhLWxhYmVsPSLrsKntjKggMjog7YKkIOyKpO2KuOugiOy5rQpLZXkgU3RyZXRjaGluZyDij7MiIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iMzA3LjA3LDY4MC4zODQgNDAwLjQzNjUsNzczLjc1MDUgMzA3LjA3LDg2Ny4xMTcgMjEzLjcwMzUsNzczLjc1MDUiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMzA3LjA3IiB5PSI3NzMuNzUwNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMzA3LjA3IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+67Cp7YyoIDI6IO2CpCDsiqTtirjroIjsua08L3RzcGFuPjx0c3BhbiB4PSIzMDcuMDciIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPktleSBTdHJldGNoaW5nIOKPszwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJIMiIgZGF0YS1sYWJlbD0i7ZW07IucIDEwMCwwMDDrsogg67CY67O1ISDimb7vuI8iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjExLjYyNDUiIHk9Ijk5Ny43MTciIHdpZHRoPSIxOTAuODkxIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzA3LjA3IiB5PSIxMDE2LjE2NyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7ZW07IucIDEwMCwwMDDrsogg67CY67O1ISDimb7vuI88L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkRCIiBkYXRhLWxhYmVsPSLshJzrsoQgREIg7KCA7J6lCuy1nOyihSDslYjsoITtlZwg7ZW07Iuc6rCSIiBkYXRhLXNoYXBlPSJjeWxpbmRlciI+CiAgPHJlY3QgeD0iMjI0LjU5MTk5OTk5OTk5OTk4IiB5PSIxMTU3LjkxNyIgd2lkdGg9IjE2NC45NTYwMDAwMDAwMDAwMiIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMSIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSJub25lIiAvPgogIDxsaW5lIHgxPSIyMjQuNTkxOTk5OTk5OTk5OTgiIHkxPSIxMTU3LjkxNyIgeDI9IjIyNC41OTE5OTk5OTk5OTk5OCIgeTI9IjEyMTEuNzE2OTk5OTk5OTk5OSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8bGluZSB4MT0iMzg5LjU0OCIgeTE9IjExNTcuOTE3IiB4Mj0iMzg5LjU0OCIgeTI9IjEyMTEuNzE2OTk5OTk5OTk5OSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8ZWxsaXBzZSBjeD0iMzA3LjA3IiBjeT0iMTIxMS43MTY5OTk5OTk5OTk5IiByeD0iODIuNDc4MDAwMDAwMDAwMDEiIHJ5PSI3IiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDxlbGxpcHNlIGN4PSIzMDcuMDciIGN5PSIxMTU3LjkxNyIgcng9IjgyLjQ3ODAwMDAwMDAwMDAxIiByeT0iNyIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIzMDcuMDciIHk9IjExODQuODE3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIzMDcuMDciIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7shJzrsoQgREIg7KCA7J6lPC90c3Bhbj48dHNwYW4geD0iMzA3LjA3IiBkeT0iMTYuOTAwMDAwMDAwMDAwMDAyIj7stZzsooUg7JWI7KCE7ZWcIO2VtOyLnOqwkjwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJOb3RlIiBkYXRhLWxhYmVsPSJOb3RlIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjY4LjYyNiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjkwLjMxMyIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5Ob3RlPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 솔팅(Salting) vs 키 스트레칭(Key Stretching) 전격 해부 (3단 표)**

해커의 무기(레인보우 테이블)를 방어하는 두 가지 척도가 \*\*'값의 틀어짐'\*\*과 \*\*'시간 지연'\*\*이라는 점을 명확히 대조해야 합니다.

| **방어막 명칭**                                   | **기술적 동작 원리 및 메커니즘**                                                                                        | **해커를 절망시키는 실무적 방어 효과**                                                                                                     |
| :------------------------------------------- | :---------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| **1. 솔팅 🧂** *(Salting)* \[공간적 방어]           | **"원본에 쓰레기 문자열 섞기."** 사용자의 원본 비밀번호 앞이나 뒤에, 서버가 생성한 '무작위 임의의 문자열(Salt 값)'을 덧붙인(XOR 또는 Concat) 다음 해시함수를 통과시킴. | 똑같은 비밀번호('1234')를 쓰는 A와 B가 있어도, 서로 부여된 Salt 값이 다르므로 최종 해시값은 완전히 다르게 나옴. ➔ **해커가 평생 모아둔 '기존 레인보우 테이블'을 단숨에 무력화시킴.**          |
| **2. 키 스트레칭 ⏳** *(Key Stretching)* \[시간적 방어] | **"해시를 수십만 번 반복해서 돌리기."** 단방향 해시를 1번만 하고 끝내는 것이 아니라, 산출된 해시값을 다시 입력값으로 넣어 수천\~수십만 번(Iteration) 뺑뺑이를 반복 돌림.  | 일반 사용자의 1번 로그인에는 0.1초가 걸려 문제없지만, **해커가 무차별 대입(Brute-force)으로 수십억 개를 뚫으려 할 때는 연산 시간이 수백 년으로 뻥튀기됨.** ➔ **해커의 해킹 '시간'을 고갈시킴.** |

#### **IV. \[결론/제언] 두 방패를 하나로 융합한 비밀번호의 성배: PBKDF2와 bcrypt**

* **(키워드 위주 2줄 마무리)** "단순히 SHA-256 같은 해시함수 하나만 믿고 비밀번호를 저장하는 시대는 끝났습니다. 현대 인증 및 인가 시스템의 절대 표준은, **무작위 솔트(Salt)와 수만 번의 해시 반복(Stretching)을 하나의 알고리즘으로 완벽히 융합하여 레인보우 테이블 공격을 원천 봉쇄하는 'PBKDF2', 'bcrypt', 'scrypt' 등의 전용 Key Derivation Function(키 유도 함수)을 의무적으로 도입하는 것**입니다."
