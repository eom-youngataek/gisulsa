### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (양자위협의공통배경, 두철학의근본적차이) — 3~4줄
Ⅱ. PQC - 수학적난제기반 (본론①, 도식 1개 필수)
Ⅲ. QKD - 물리법칙기반, 핵심 배점
Ⅳ. 결론 - 국가전략선택의근거
```

### Ⅰ. 개요

앞서다룬 \*\*"양자컴퓨터의쇼어알고리즘"\*\*이 \*\*RSA/ECC의수학적기반(소인수분해)\*\*을 무너뜨린다는위협에대해, 두가지서로다른대응이나왔습니다 — PQC는 \*\*"양자컴퓨터도풀기어려운더어려운수학문제"\*\*로 바꾸는것이고, QKD는 \*\*"수학"\*\*자체를 버리고 \*\*"양자물리법칙(관측하면상태가바뀐다)"\*\*으로 키를분배하는것입니다.

### Ⅱ. PQC — 수학적난제기반(소프트웨어적해법)

| 항목        | 내용                                                                         |
| :-------- | :------------------------------------------------------------------------- |
| **원리**    | 기존RSA/ECC(소인수분해·이산대수)를 **양자컴퓨터도풀기어려운새수학문제**(격자기반등)로 대체                     |
| **구현방식**  | **기존네트워크·프로토콜에소프트웨어적으로적용**가능— TLS,PKI등에 **알고리즘만교체**                        |
| **표준화현황** | NIST **FIPS203(ML-KEM),204(ML-DSA),205(SLH-DSA)** 2024년승인,**HQC**2025년백업선정 |
| **적용범위**  | **범용적**— 인터넷전체,모든기기·서버에적용가능                                                |

→ 암기: **"문제를더어렵게바꿔서,기존인프라에소프트웨어로심는다"** — 앞서다룬 \*\*"PQC국가전환마스터플랜의암호자산인벤토리+하이브리드전환"\*\*전략이 바로 PQC도입의 **실무적접근**입니다.

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
| **적용범위**   | **제한적**— 특정지점간(예:정부기관간)의 **전용통신망구간**에만 적용가능           |

→ 암기: **"엿보면들킨다는물리법칙자체가보안"** — 수학문제를푸는게아니라, \*\*"관측하면양자상태가붕괴한다"\*\*는 자연법칙자체를 이용하기때문에, **미래의어떤컴퓨터(양자컴퓨터포함)로도 이론상깨뜨릴수없다**는게 QKD의 근본적강점입니다.

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

### Ⅳ. 결론 — 국가전략선택의근거

**함정 방지: "QKD가더안전하니QKD를써야한다"고답하면오해. 앞서다룬마스터플랜이 왜PQC를중심으로삼았는지 실제근거로연결해야완성됩니다.**

| 구분             | **PQC**                         | **QKD**                |
| :------------- | :------------------------------ | :--------------------- |
| **보안기반**       | 수학적난제(계산복잡도)                    | **물리법칙**(양자역학)         |
| **인프라요구**      | **기존인프라재사용**(소프트웨어교체)           | **전용하드웨어**(광섬유,특수장비)필요 |
| **적용범위**       | **광대**(인터넷전체)                   | **제한적**(지점간전용회선)       |
| **비용/확장성**     | 상대적으로 **저렴,확장용이**               | **고비용,국토전체커버어려움**      |
| **한국마스터플랜의선택** | **암호자산인벤토리→하이브리드전환의중심**(앞서다룬그것) | **금융·국방등특수보안구간에보조적검토** |

→ 앞서다룬 \*\*"PQC국가전환마스터플랜의4대전략(인벤토리,기술자립화,분야별시범전환,국제표준화참여)"\*\*이 모두 **PQC를중심**으로설계된이유는, \*\*"QKD로전국망을커버하려면 막대한전용광섬유인프라구축비용"\*\*이 들지만, **PQC는기존TLS/PKI에알고리즘만교체**하면 되기때문입니다 — 이는 앞서다룬 \*\*"미국의PQC-First전략(광대한국토인프라의한계)"\*\*과 **동일한현실적판단**입니다.

**결론**: PQC와QKD는 \*\*"양자컴퓨터위협에대응하는 두가지근본적으로다른철학"\*\*입니다 — PQC는 **"기존소프트웨어인프라를유지하며 문제자체를더어렵게만드는"** 실용적접근이고, QKD는 **"물리법칙으로원천적으로도청이불가능하게만드는"** 이론적으로가장강력하지만 **인프라제약이큰**접근입니다 — 앞서다룬 \*\*"PQC국가전환마스터플랜"\*\*이 \*\*"암호자산인벤토리→하이브리드전환"\*\*을 중심전략으로삼은것은, \*\*"이론적완벽함보다,현실적적용가능성과확장성을우선"\*\*한 결과이며, \*\*"QKD는특수한고보안구간(금융,국방)에만보조적으로검토"\*\*하는 방향으로 국가전략이 수립되었습니다.

### **1. 답안 전개 스토리 (핵심 압축)**

> "양자컴퓨터의 해킹 쓰나미에 대응하는 두 가지 핵심 보안 기술이자, \*\*'수학(소프트웨어) vs 물리학(하드웨어)'\*\*의 흥미진진한 대비다. 첫째, **'PQC(양자내성암호)'**. 양자컴퓨터도 풀기 힘든 수학적 난제(격자 퀴즈)에 기반한 암호 프로그램이다. 기존 랜선, 와이파이, 스마트폰 인프라를 그대로 쓰며 단순히 소프트웨어만 패치하면 끝나므로 가성비(구축비 초저렴)가 최고다. 둘째, **'QKD(양자암호키분배)'**. 수학이 아니라 빛의 최소 입자인 광자(Photon)의 물리학적 법칙(불확정성 원리 및 복제불가능성)에 기반해 비밀키를 쏜다. 해커가 중간에서 훔쳐보려고 광자를 관측하는 순간 정보가 마법처럼 뭉개져 해킹 사실이 100% 발각되고 키는 파괴된다. 다만 전용 광케이블과 비싼 송수신 장비를 새로 깔아야 해 막대한 돈이 든다. 가성비 좋은 소프트웨어 방어막(PQC)과 물리학 법칙에 기댄 절대적 하드웨어 성벽(QKD)의 상호 보완 융합이 정답이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 포스트 양자 시대의 보안 패러다임, PQC와 QKD 개요**

* **PQC(Post-Quantum Cryptography) 정의:** 양자컴퓨터의 연산 능력으로도 해독할 수 없는 고도의 수학적 복잡도(격자 난제 등)를 기반으로 설계된 소프트웨어적 공개키 암호 알고리즘.
* **QKD(Quantum Key Distribution) 정의:** 양자역학의 물리학적 법칙(하이젠베르크 불확정성, 단일 광자 복제 불가능 정리)을 기반으로, 송수신자 사이에 도청이 불가능한 대칭 암호키를 안전하게 분배하는 하드웨어 통신 기술.

#### **II. \[본론 1] (극단적 단순화 버전) 소프트웨어 패치 vs 하드웨어 전용망 구축**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2OTEuODk2IDQwNyIgd2lkdGg9IjY5MS44OTYiIGhlaWdodD0iNDA3IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfX19fUFFDX3ZzX1FLRCIgZGF0YS1sYWJlbD0i7JaR7J6QIOuztOyViOydmCDslpHrjIAg7IKw66elOiBQUUMgdnMgUUtEIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI2MTEuODk2IiBoZWlnaHQ9IjMyNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjYxMS44OTYiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij7slpHsnpAg67O07JWI7J2YIOyWkeuMgCDsgrDrp6U6IFBRQyB2cyBRS0Q8L3RleHQ+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMV9QUUNfX19fIiBkYXRhLWxhYmVsPSIxLiBQUUMgKOyImO2VmSAvIOyGjO2UhO2KuOybqOyWtCDwn5KvKSI+CiAgPHJlY3QgeD0iNTYiIHk9Ijg0IiB3aWR0aD0iMjYyLjkwNSIgaGVpZ2h0PSIyNTAuMSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjI2Mi45MDUiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjY4IiB5PSI5OCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij4xLiBQUUMgKOyImO2VmSAvIOyGjO2UhO2KuOybqOyWtCDwn5KvKTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IjJfUUtEX19fXyIgZGF0YS1sYWJlbD0iMi4gUUtEICjrrLzrpqwgLyDtlZjrk5zsm6jslrQg8J+aqCkiPgogIDxyZWN0IHg9IjMzOC45MDUiIHk9Ijg0IiB3aWR0aD0iMjk2Ljk5MSIgaGVpZ2h0PSIyNjciIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSIzMzguOTA1IiB5PSI4NCIgd2lkdGg9IjI5Ni45OTEiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjM1MC45MDUiIHk9Ijk4IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjIuIFFLRCAo66y866asIC8g7ZWY65Oc7Juo7Ja0IPCfmqgpPC90ZXh0Pgo8L2c+CjwvZz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlBfSU4iIGRhdGEtdG89IlBfT1VUIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLqsqnsnpAg7IiY7ZWZIOyVlO2YuCDtjKjsuZgiIHBvaW50cz0iMTg3LjQ1MjUsMTY0LjkgMTg3LjQ1MjUsMjg5LjY1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJRX0lOIiBkYXRhLXRvPSJRX09VVCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0i6rSR7J6QKFBob3Rvbikg7Ya17IugIO2OhOyKpCDshqHsiJjsi6AiIHBvaW50cz0iNDg3LjQwMDQ5OTk5OTk5OTk3LDE4MS44IDQ4Ny40MDA0OTk5OTk5OTk5NywyODkuNjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iUF9JTiIgZGF0YS10bz0iUF9PVVQiIGRhdGEtbGFiZWw9IuqyqeyekCDsiJjtlZkg7JWU7Zi4IO2MqOy5mCI+CiAgPHJlY3QgeD0iMTI3Ljk1MjUiIHk9IjIwNy45IiB3aWR0aD0iMTE4LjAzNjAwMDAwMDAwMDAzIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTg2Ljk3MDUwMDAwMDAwMDAyIiB5PSIyMjMuMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuqyqeyekCDsiJjtlZkg7JWU7Zi4IO2MqOy5mDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJRX0lOIiBkYXRhLXRvPSJRX09VVCIgZGF0YS1sYWJlbD0i6rSR7J6QKFBob3Rvbikg7Ya17IugIO2OhOyKpCDshqHsiJjsi6AiPgogIDxyZWN0IHg9IjQwMi40MDA0OTk5OTk5OTk5NyIgeT0iMjI0LjgiIHdpZHRoPSIxNjkuMTIwMDAwMDAwMDAwMDMiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI0ODYuOTYwNDk5OTk5OTk5OTciIHk9IjIzOS45NTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+6rSR7J6QKFBob3Rvbikg7Ya17IugIO2OhOyKpCDshqHsiJjsi6A8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlBfSU4iIGRhdGEtbGFiZWw9Iuq4sOyhtCDrnpzshKAgLyDrrLTshKAg7J247YSw64S3IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjkzLjQ4OSIgeT0iMTI4IiB3aWR0aD0iMTg3LjkyNyIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjE4Ny40NTI1IiB5PSIxNDYuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuq4sOyhtCDrnpzshKAgLyDrrLTshKAg7J247YSw64S3PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQX09VVCIgZGF0YS1sYWJlbD0i6rCA7ISx67mEIOuGkuydgCDrspTsmqkg67O07JWIIOyLpO2YhCDwn5qAIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjcyIiB5PSIyODkuNjUiIHdpZHRoPSIyMzAuOTA1IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxODcuNDUyNSIgeT0iMzA4LjA5OTk5OTk5OTk5OTk3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7qsIDshLHruYQg64aS7J2AIOuylOyaqSDrs7TslYgg7Iuk7ZiEIPCfmoA8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlFfSU4iIGRhdGEtbGFiZWw9IuKcqCDsoITsmqkg7JaR7J6QIOq0key8gOydtOu4lCDinKgKKyDslpHsnpAg7Iah7IiY7Iug6riwIOyepeu5hCDsnqXssKkiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzg0LjE3NDQ5OTk5OTk5OTk3IiB5PSIxMjgiIHdpZHRoPSIyMDYuNDUxOTk5OTk5OTk5OTQiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNDg3LjQwMDQ5OTk5OTk5OTk3IiB5PSIxNTQuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNDg3LjQwMDQ5OTk5OTk5OTk3IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+4pyoIOyghOyaqSDslpHsnpAg6rSR7LyA7J2067iUIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjQ4Ny40MDA0OTk5OTk5OTk5NyIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+KyDslpHsnpAg7Iah7IiY7Iug6riwIOyepeu5hCDsnqXssKk8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUV9PVVQiIGRhdGEtbGFiZWw9IvCflJIg66y866asIOuyley5mSDquLDrsJgg64+E7LKtIOybkOyynCDssKjri6gg8J+UkiIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzNTQuOTA1IiB5PSIyODkuNjUiIHdpZHRoPSIyNjQuOTkxIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjQ4Ny40MDA0OTk5OTk5OTk5NyIgeT0iMzA4LjA5OTk5OTk5OTk5OTk3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7wn5SSIOusvOumrCDrspXsuZkg6riw67CYIOuPhOyyrSDsm5Dsspwg7LCo64uoIPCflJI8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] PQC와 QKD 보안 원리, 전송 인프라 및 핵심 강약점 전격 대조 (3단 표)**

이 토픽은 수학적 알고리즘 교체 수준의 \*\*'PQC'\*\*와, 물리적 전용 광채널 구축 및 도청 불가(광자 상태 붕괴)의 \*\*'QKD'\*\*를 완벽하게 비교표로 채워 제출하는 것이 만점 포인트입니다.

| **핵심 척도**               | **📊 PQC (양자내성암호 / 수학) 🚨**                                                              | **🔑 QKD (양자암호키분배 / 물리) 🚨**                                                                                | **원천적 장단점 대조 💯**                                                    |
| :---------------------- | :--------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------- |
| **개념 / 보안 원리**          | **'수학적 난제 해결의 어려움'.** 양자 컴퓨터가 무제한 연산해도 우회 연산 궤적이 비선형적으로 꼬여 쉽게 풀지 못하는 복잡성에 의존.            | **'양자역학의 물리 법칙 💯'.** 빛의 알갱이를 관측(도청)하면 상태가 파괴(붕괴)되는 **불확정성 및 복제 불가능 정리**에 의존.                               | 소프트웨어를 튜닝하여 보안을 획득하는 기법과, 하드웨어 전송 방식 자체를 바꾸는 기술의 물리적 대조.             |
| **전송 인프라 / 비용 🚨**      | **\[기존 인프라 100% 활용 💯]** 기존 광케이블, 무선 5G/6G망, 데이터 서버 사용 가능. **\[구축비 초저렴]** 단순 알고리즘 교체 패치. | **\[전용 인프라 강제 🚨]** 기존 라우터를 통과할 수 없어 **전용 양자 광케이블 채널** 및 고가 양자 키 분배 장비 구축 필수. **\[구축비 천문학적]**               | PQC는 스마트폰 등 엣지 기기까지 배포가 쉬우나, QKD는 크고 무거워 기지국이나 서버 허브망 위주로만 제한 탑재됨.   |
| **장점 / 한계 (출제 포인트) 🚨** | **\[장점]** 뛰어난 가성비, 높은 이식성. **\[한계]** 향후 격자 문제를 푸는 천재적 수학 공식이 발명되면 **다시 해킹당할 수학적 맹점 존재.** | **\[장점 💯]** 어떤 양자컴퓨터가 나와도 **물리학 법칙상 도청이 원천 불가능(절대 보안).** **\[한계 🚨]** 광신호 감쇄로 인해 **전송 거리(약 100km 내외) 한계.** | PQC는 전 세계 데이터 전송 전반에 쓰이며, QKD는 국가 행정망/군사 백본망 등 국가 최고 중요 물길에 핀포인트 쓰임. |

#### **IV. \[결론/제언] 하이브리드 결합망 (QKD로 키 분배 + PQC로 채널 암호화)**

* **(키워드 위주 2줄 마무리)** "PQC와 QKD는 양자 택일의 경쟁 기술이 아닌, 상호 보완적인 보안 생태계 동반자입니다. 국가 기밀망 아키텍처 수립 시, **QKD로 백본망의 대칭키를 안전하게 분배하고, PQC 알고리즘으로 단말기 구간을 암호화하여 통신하는 '하이브리드 양자 보안 연동 표준망'을 구축해야 합니다.**"
