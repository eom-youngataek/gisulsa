### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (두기술의근본적차이) — 3~4줄
Ⅱ. PQC - 수학적난제기반 (본론①, 도식 1개 필수)
Ⅲ. QKD - 물리법칙기반 (본론②, 핵심 배점)
Ⅳ. 비교및국가전략선택
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬양자컴퓨터가쇼어알고리즘으로 RSA/ECC의수학적기반을무너뜨린다는위협에대해, 두가지서로다른대응이나왔다 — PQC는'양자컴퓨터도풀기어려운더어려운수학문제'로바꾸는것이고, QKD는'수학'자체를버리고 '양자물리법칙(관측하면상태가바뀐다)'으로키를분배하는것"\*\*이라는한줄로시작하면, 왜접근방식자체가다른지드러납니다.

### Ⅱ. PQC — 수학적난제기반(소프트웨어적해법)

| 항목        | 내용                                                                         |
| :-------- | :------------------------------------------------------------------------- |
| **원리**    | 기존RSA/ECC(소인수분해·이산대수)를 **양자컴퓨터도풀기어려운새수학문제**(격자기반등)로대체                      |
| **구현방식**  | **기존네트워크·프로토콜에소프트웨어적으로적용**가능 — 앞서다룬**TLS,PKI**등에그대로교체                      |
| **표준화현황** | NIST **FIPS203(ML-KEM),204(ML-DSA),205(SLH-DSA)** 2024년승인,**HQC**2025년백업선정 |
| **적용범위**  | **범용적**— 인터넷전체,모든기기·서버에적용가능                                                |

→ 암기: **"문제를더어렵게바꿔서, 기존인프라에소프트웨어로심는다"** — 앞서다룬 \*\*"암호자산인벤토리+하이브리드전환"\*\*전략이 바로 PQC도입의 실무적접근입니다.

### 도식화 제안

```
[PQC 적용]
[기존RSA/ECC] ──교체──→ [격자기반등PQC알고리즘]
        ↓
   기존TLS/PKI/코드서명 등에 소프트웨어로 적용
   (인프라전체를 바꿀필요없이, 알고리즘만교체)
```

### Ⅲ. QKD — 물리법칙기반(하드웨어적해법), 핵심 배점

**함정 방지: "양자컴퓨터를막는양자기술"이라고만답하면절반. "왜도청이불가능한지"의 물리적원리를보여줘야완성됩니다.**

| 항목         | 내용                                                    |
| :--------- | :---------------------------------------------------- |
| **원리**     | **양자역학의관측자효과**— 광자(빛알갱이)의양자상태를 **측정(도청)하는순간 그상태가변형**됨 |
| **핵심메커니즘** | 송신자·수신자가 **양자상태로키를분배**,도청자가엿보면 **오류율이급증**해 즉시감지가능     |
| **구현방식**   | **전용광섬유/특수장비**필요(광자를전송할물리적통신선)                        |
| **적용범위**   | **제한적**— 특정지점간(예:정부기관간)의 **전용통신망구간**에만적용가능            |

→ 암기: **"엿보면들킨다는물리법칙자체가보안"** — 수학문제를푸는게아니라, \*\*"관측하면양자상태가붕괴한다"\*\*는 자연법칙자체를이용하기때문에, **미래의어떤컴퓨터(양자컴퓨터포함)로도 이론상깨뜨릴수없다**는게 QKD의 근본적강점입니다.

### 도식화 제안

```
[QKD 통신]
[송신자] ──광자(양자상태)──→ [수신자]
              ↑
         [도청자가엿보면]
              ↓
    양자상태가 변형됨(관측자효과)
              ↓
    오류율급증 → 도청사실 즉시감지
```

### Ⅳ. 비교및국가전략선택

**함정 방지: "QKD가더안전하니QKD를써야한다"고답하면오해. 앞서검색한자료에서 "미국은QKD보다PQC를우선한다"는 실제정책판단이있었다는걸 반영해야완성됩니다.**

| 구분         | **PQC**                                            | **QKD**                    |
| :--------- | :------------------------------------------------- | :------------------------- |
| **보안기반**   | 수학적난제(계산복잡도)                                       | **물리법칙**(양자역학)             |
| **인프라요구**  | **기존인프라재사용**(소프트웨어교체)                              | **전용하드웨어**(광섬유,특수장비)필요     |
| **적용범위**   | **광대**(인터넷전체)                                      | **제한적**(지점간전용회선)           |
| **비용/확장성** | 상대적으로 **저렴,확장용이**                                  | **고비용,국토전체커버어려움**          |
| **미국의선택**  | **"PQC-First"전략**— 양자컴퓨팅사이버보안준비법으로 **PQC전환을법적의무화** | 광대한국토인프라의한계로 **QKD는보조적검토** |

→ 앞서다룬 검색자료의핵심통찰: \*\*"광대한국토인프라의한계로 QKD보다PQC가더빠르고효율적인방어책"\*\*이라는게 미국의현실적판단이었습니다 — 이는 \*\*"이론적으로더완벽한기술(QKD)"\*\*이 항상 \*\*"실무적으로더나은선택"\*\*은아니라는 교훈을보여줍니다.

### Ⅴ. 결론 포인트 (암호·보안 시리즈 최종완결)

PQC와QKD는 \*\*"양자컴퓨터위협에대응하는 두가지근본적으로다른철학"\*\*입니다 — PQC는 **"기존소프트웨어인프라를유지하며 문제자체를더어렵게만드는"** 실용적접근이고, QKD는 **"물리법칙으로원천적으로도청이불가능하게만드는"** 이론적으로가장강력하지만 **인프라제약이큰**접근입니다 — 대부분국가·기업이 \*\*"PQC중심전환로드맵을먼저세우고, 특수한고보안구간에만QKD를보조적으로검토"\*\*하는 방향으로가는것은, 앞서다룬여러답안(RAID,캐시매핑,대칭/비대칭암호하이브리드)에서 반복된 \*\*"이론적완벽함보다,현실적적용가능성과확장성을우선하는설계철학"\*\*의 또다른사례입니다 — 이로써오늘하루다룬 대칭/비대칭암호→동형암호→PQC/QKD로이어지는 방대한암호·보안시리즈전체가, \*\*"양자시대에도데이터를안전하게지키기위한 인류의다각적노력"\*\*이라는 하나의완결된이야기로마무리됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "현재 우리의 인터넷 뱅킹과 공인인증서를 지키는 RSA 자물쇠는 수학적 난제(소인수분해)로 만들어졌다. 슈퍼컴퓨터로 수백 년이 걸리기에 안전했다. 하지만 머지않아 등장할 '양자 컴퓨터(Quantum Computer)'는 이 소인수분해를 불과 몇 분 만에 찢어버리는 무적의 마스터키(쇼어 알고리즘)를 가지고 있다. 이 전대미문의 재앙(양자 위협)을 막기 위해 인류는 두 가지 거대한 방패를 준비했다. 바로 소프트웨어 방패인 \*\*'PQC(양자 내성 암호)'\*\*와 하드웨어 방패인 \*\*'QKD(양자 키 분배)'\*\*다. \*\*'PQC(Post-Quantum Cryptography)'\*\*는 적의 양자 컴퓨터조차 뚫을 수 없는 \*\*'새로운 수학적 자물쇠'\*\*를 알고리즘으로 짜는 것이다. 뚫리기 쉬운 소인수분해 대신 '격자(Lattice)' 같은 엄청나게 복잡한 수학적 미로를 꼬아놓아 양자 컴퓨터조차 길을 잃게 만든다. 스마트폰이나 기존 통신망을 바꿀 필요 없이 소프트웨어 업데이트만 하면 되므로 매우 싸고 유연하다. 반면 \*\*'QKD(Quantum Key Distribution)'\*\*는 수학이 아니라 \*\*'우주의 물리 법칙(양자역학)'\*\*을 이용해 아예 훔쳐볼 수 없는 비밀키를 빛(광자)으로 쏴서 배달하는 거대한 통신 장비다. 중간에 해커가 도청하려고 선을 건드리는 순간, 양자 상태가 즉시 파괴되어(관측 붕괴) 도청 사실을 무조건 알아챈다. 해킹이 물리적으로 불가능하지만, 전용 광케이블을 새로 깔아야 하고 장비가 수억 원이라 스마트폰에는 당장 못 넣는다. 결국 미래의 보안은 우리 폰에는 PQC를, 은행 본점망에는 QKD를 설치하는 하이브리드 형태로 진화할 것이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] RSA를 찢어버릴 양자 컴퓨터의 위협과 인류의 2대 방어막 개요**

* **배경 (양자 위협, Y2Q):** 양자 컴퓨터의 큐비트 연산과 쇼어 알고리즘(Shor's Algorithm)이 상용화되면, 현재 전 세계 통신 인프라의 근간인 RSA 기반 비대칭키 암호 체계가 일거에 무너짐.
* **PQC (양자 내성 암호):** 양자 컴퓨터로도 풀기 극도로 어려운 '새로운 수학적 난제'를 적용하여 기존 암호 알고리즘(S/W)을 업그레이드하는 소프트웨어적 접근법.
* **QKD (양자 키 분배):** 양자역학의 불가해한 물리 법칙(복제 불가능, 관측 시 상태 붕괴)을 적용하여, 해커의 도청을 원천 차단하고 송수신자가 안전하게 암호키를 나눠 갖는 하드웨어 장비 접근법.

#### **II. \[본론 1] 소프트웨어(수학)로 막는 PQC vs 하드웨어(물리)로 막는 QKD (도식화)**

두 기술이 인프라 측면에서 어떻게 다르게 동작하는지 직관적으로 비교합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3MDYuNDE0IDYyNy42NTYiIHdpZHRoPSI3MDYuNDE0IiBoZWlnaHQ9IjYyNy42NTYiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9Il9fX19fX18iIGRhdGEtbGFiZWw9IuyWkeyekCDsnITtmJHsnYQg67Cp7Ja07ZWY64qUIOuRkCDqsIDsp4Ag7LKg7ZWZ7KCBIOygkeq3vCDrsKnsi50iPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjYyNi40MTQiIGhlaWdodD0iNTQ3LjY1NiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjYyNi40MTQiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7slpHsnpAg7JyE7ZiR7J2EIOuwqeyWtO2VmOuKlCDrkZAg6rCA7KeAIOyyoO2VmeyggSDsoJHqt7wg67Cp7IudPC90ZXh0Pgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IlBRQ19fX19fU1dfIiBkYXRhLWxhYmVsPSJQUUMgKOyWkeyekCDrgrTshLEg7JWU7Zi4KSDinpQgUy9XIOyXheuNsOydtO2KuCI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iNTE4LjM5MTAwMDAwMDAwMDEiIGhlaWdodD0iMTUzLjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSI1MTguMzkxMDAwMDAwMDAwMSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjgiIHk9Ijk4IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPlBRQyAo7JaR7J6QIOuCtOyEsSDslZTtmLgpIOKelCBTL1cg7JeF642w7J207Yq4PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iUUtEX19fX19IV19fX18iIGRhdGEtbGFiZWw9IlFLRCAo7JaR7J6QIO2CpCDrtoTrsLApIOKelCBIL1cg7J6l67mEIOuwjyDrp50g6rWs7LaVIj4KICA8cmVjdCB4PSI1NiIgeT0iMjU3LjgiIHdpZHRoPSI1OTQuNDE0IiBoZWlnaHQ9IjMxMy44NTYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI1NiIgeT0iMjU3LjgiIHdpZHRoPSI1OTQuNDE0IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI2OCIgeT0iMjcxLjgiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+UUtEICjslpHsnpAg7YKkIOu2hOuwsCkg4p6UIEgvVyDsnqXruYQg67CPIOunnSDqtazstpU8L3RleHQ+CjwvZz4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iVTEiIGRhdGEtdG89IlMxIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLquLDsobQg7J2867CYIOyduO2EsOuEt+unnSAoTFRFLCA1RykiIHBvaW50cz0iMjExLjc2MiwyMDMuMzUwMDAwMDAwMDAwMDIgNDYyLjM0OCwyMDMuMzUwMDAwMDAwMDAwMDIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlUyIiBkYXRhLXRvPSJTMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iUUtEIOyghOyaqSDslpHsnpAg6rSR7LyA7J2067iU66edIPCfkqEiIHBvaW50cz0iMjYwLjk1Niw1MzcuMjA2IDQ3Ny45MTgsNTM3LjIwNiA0NzcuOTE4LDQ3Mi44OTIwMDAwMDAwMDAwNSA1MTMuOTE4LDQ3Mi44OTIwMDAwMDAwMDAwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iSCIgZGF0YS10bz0iUzIiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLqtIDsuKEg67aV6rS0IOuwnOyDnSEiIHBvaW50cz0iMjYwLjk1NiwzOTYuMjc4IDQ3Ny45MTgsMzk2LjI3OCA0NzcuOTE4LDQ2MC41OTIwMDAwMDAwMDAwNCA1MTMuOTE4LDQ2MC41OTIwMDAwMDAwMDAwNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlUxIiBkYXRhLXRvPSJTMSIgZGF0YS1sYWJlbD0i6riw7KG0IOydvOuwmCDsnbjthLDrhLfrp50gKExURSwgNUcpIj4KICA8cmVjdCB4PSIyNTUuNzYyIiB5PSIxODcuMzUiIHdpZHRoPSIxNjIuNTg2IiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzM3LjA1NSIgeT0iMjAyLjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuq4sOyhtCDsnbzrsJgg7J247YSw64S366edIChMVEUsIDVHKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJVMiIgZGF0YS10bz0iUzIiIGRhdGEtbGFiZWw9IlFLRCDsoITsmqkg7JaR7J6QIOq0key8gOydtOu4lOunnSDwn5KhIj4KICA8cmVjdCB4PSIzMDQuOTU2IiB5PSI1MjEuMjA2IiB3aWR0aD0iMTY0Ljk2MjAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzg3LjQzNyIgeT0iNTM2LjM1NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+UUtEIOyghOyaqSDslpHsnpAg6rSR7LyA7J2067iU66edIPCfkqE8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iSCIgZGF0YS10bz0iUzIiIGRhdGEtbGFiZWw9Iuq0gOy4oSDrtpXqtLQg67Cc7IOdISI+CiAgPHJlY3QgeD0iMzQwLjAwMiIgeT0iMzgwLjI3OCIgd2lkdGg9Ijk0Ljg3MDAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzg3LjQzNyIgeT0iMzk1LjQyOCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+6rSA7LihIOu2leq0tCDrsJzsg50hPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJVMSIgZGF0YS1sYWJlbD0i7Iqk66eI7Yq47Y+wL1BDIPCfk7EiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNzIiIHk9IjE4NC45IiB3aWR0aD0iMTM5Ljc2MiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTQxLjg4MSIgeT0iMjAzLjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7siqTrp4jtirjtj7AvUEMg8J+TsTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzEiIGRhdGEtbGFiZWw9IuyEnOuyhCDimIHvuI8iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDYyLjM0OCIgeT0iMTg0LjkiIHdpZHRoPSI5Ni4wNDI5OTk5OTk5OTk5OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNTEwLjM2OTUiIHk9IjIwMy4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7ISc67KEIOKYge+4jzwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3MiIgeT0iMTI4IiB3aWR0aD0iNjguNjI2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTA2LjMxMyIgeT0iMTQ2LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5Ob3RlPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJVMiIgZGF0YS1sYWJlbD0i6rWt67CpL+q4iOyctSDrs7jsoJAg7J6l67mEIPCfj6IiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNzUuMjUyMDAwMDAwMDAwMDQiIHk9IjUxOC43NTYwMDAwMDAwMDAxIiB3aWR0aD0iMTg1LjcwMzk5OTk5OTk5OTk4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNjguMTA0MDAwMDAwMDAwMDQiIHk9IjUzNy4yMDYwMDAwMDAwMDAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7qta3rsKkv6riI7Jy1IOuzuOygkCDsnqXruYQg8J+PojwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUzIiIGRhdGEtbGFiZWw9IuyngOygkCDsnqXruYQg8J+PpiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1MTMuOTE4IiB5PSI0NDguMjkyMDAwMDAwMDAwMDMiIHdpZHRoPSIxMjAuNDk2MDAwMDAwMDAwMDEiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjU3NC4xNjYiIHk9IjQ2Ni43NDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyngOygkCDsnqXruYQg8J+PpjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iSCIgZGF0YS1sYWJlbD0i7ZW07LukIPCfpbcK6rSR7LyA7J2067iUIOuPhOyyrSDsi5zrj4QiIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iMTY2LjQ3OCwzMDEuOCAyNjAuOTU2LDM5Ni4yNzggMTY2LjQ3OCw0OTAuNzU2MDAwMDAwMDAwMDMgNzIsMzk2LjI3OCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTY2LjQ3OCIgeT0iMzk2LjI3OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTY2LjQ3OCIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPu2VtOy7pCDwn6W3PC90c3Bhbj48dHNwYW4geD0iMTY2LjQ3OCIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+6rSR7LyA7J2067iUIOuPhOyyrSDsi5zrj4Q8L3RzcGFuPjwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] 양자 내성 암호(PQC) vs 양자 키 분배(QKD) 전격 비교 (3단 표 - 핵심)**

두 기술을 **보안성(안전성의 근원), 경제성, 상용화 영역**의 척도로 명확히 쪼개야 합니다.

| **핵심 척도 (비교 잣대)**    | **💻 PQC (양자 내성 암호)**                                                                         | **💡 QKD (양자 키 분배)**                                                                            |
| :------------------- | :-------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| **방어의 본질 (안전성의 근거)** | **'수학적 복잡도' (알고리즘).** 양자 컴퓨터가 풀기 어려운 새로운 수학 난제(격자, 해시, 다변수 이차식 등)의 연산 복잡도에 의존함.               | **'물리학적 법칙' (양자역학).** 단일 광자(빛)에 데이터를 싣기 때문에, 해커가 훔쳐보면 '양자 상태가 붕괴'하여 도청 사실이 무조건 들통나는 물리 법칙에 의존함. |
| **인프라 종속성 및 경제성**    | **소프트웨어(앱)만 업데이트하면 끝.** 기존의 인터넷, 무선망(Wi-Fi, 5G), 스마트폰을 그대로 쓸 수 있어 구축 비용이 매우 저렴하고 빠름.          | **고가의 QKD 전용 하드웨어 및 광케이블 필수.** 기존 통신망을 쓸 수 없으며, 거리가 멀어지면 중간 노드가 필요하여 천문학적인 구축 비용이 듦.            |
| **안전성의 한계**          | **'이론적/계산적 안전성'.** 미래에 엄청난 천재 수학자가 나오거나, 상상을 초월하는 양자 알고리즘이 개발되면 또 뚫릴 수 있는 잠재적 불안감이 있음.        | **'무조건적(절대적) 안전성'.** 우주의 물리 법칙이 바뀌지 않는 한 원천적으로 해킹(도청)이 불가능함. (안전성 최강).                          |
| **현재 상용화 적용 타겟 분야**  | 범용적인 대국민 서비스. 웹 브라우저 통신, 스마트폰 뱅킹 앱, 메신저 앱 등 **소프트웨어 엔드포인트 보안** 영역. (현재 미국 NIST 주도 표준화 완료 단계). | 국가 안보 1급망, 은행 본점-지점 간 통신, 주요 클라우드 데이터센터 백본망 등 **인프라 최하단 물리 계층 보안** 영역.                          |

#### **IV. \[결론/제언] 상호 배타적이 아닌 보완재로서의 하이브리드(Hybrid) 양자 보안**

* **(키워드 위주 2줄 마무리)** "PQC와 QKD는 승패를 다루는 경쟁 기술이 아닙니다. 극강의 물리적 안전성을 자랑하지만 비용이 비싼 **QKD를 국가와 데이터센터의 백본(Backbone)망 구축에 사용하고**, 저렴하고 유연하지만 알고리즘이 무거운 \*\*PQC를 대국민 엣지(Edge) 디바이스와 웹 통신에 적용하는 '하이브리드(Hybrid) 양자 보안 아키텍처'\*\*가 미래 Y2Q(양자 위협) 시대를 돌파할 유일한 해답이 될 것입니다."
