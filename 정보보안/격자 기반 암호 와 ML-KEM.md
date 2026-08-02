#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 "격자"가 양자컴퓨터도 못 푸는가)
Ⅱ. 격자 기반 암호의 수학적 원리
Ⅲ. ML-KEM 핵심 구조 및 동작
Ⅳ. 기존 공개키 암호와의 비교
Ⅴ. 결론 및 국내외 적용 현황
```

포인트: 개요에서 **"앞서 다룬 PQC 마스터플랜에서 CRQC가 RSA·ECC를 무력화하는 핵심 원리가 쇼어 알고리즘(소인수분해·이산대수 문제를 다항식 시간에 해결)이라면, 격자 기반 암호는 양자컴퓨터로도 다항식 시간에 해결할 수 없는 '격자 위 최단벡터 문제(SVP)와 최근벡터 문제(CVP)'를 안전성 근거로 삼는다 — NIST가 2024년 8월 FIPS-203으로 표준화한 ML-KEM(구 CRYSTALS-Kyber)이 격자 기반 암호의 대표 구현체이며, 국내 KpqC 공모전에서 선정된 SMAUG-T·HAETAE도 동일한 격자 문제 기반"**이라는 한 줄로 시작하면, 왜 이 답안이 앞서 다룬 PQC·양자보안·암호민첩성 시리즈 전체의 **수학적 핵심**인지 드러납니다.

---

#### Ⅱ. 격자 기반 암호의 수학적 원리

**가. 격자(Lattice) 정의**

```
[격자의 기하학적 구조]

기저 벡터 b₁·b₂ (2차원 예시):

    ·  ·  ·  ·  ·
  ·  ·  ·  ·  ·
b₂↗  ·  ·  ·  ·
·──→·  ·  ·  ·
   b₁

격자 L = {a₁b₁ + a₂b₂ | a₁,a₂ ∈ ℤ}
→ 정수 계수의 선형 결합으로 생성되는 이산 점들의 집합
→ 고차원(수백~수천 차원)에서 기하학적 구조 분석이 극도로 어려움
```

**나. 핵심 난제 3가지**

| 난제                                | 정의                                             | 암호 활용               |
| --------------------------------- | ---------------------------------------------- | ------------------- |
| **SVP (Shortest Vector Problem)** | 격자에서 **가장 짧은 벡터**를 찾는 문제                       | 격자 기반 암호 안전성 근거 핵심  |
| **CVP (Closest Vector Problem)**  | 임의 점에서 **가장 가까운 격자 점**을 찾는 문제                  | SVP보다 더 어려운 문제로 알려짐 |
| **LWE (Learning With Errors)**    | **노이즈가 섞인 선형 방정식** A·s + e = b에서 비밀벡터 s를 찾는 문제 | ML-KEM의 직접적 안전성 기반  |

**다. LWE(Learning With Errors) 상세**

```
[LWE 문제 구조]

공개: 행렬 A (m×n), 벡터 b = A·s + e (mod q)
비밀: s ∈ ℤqⁿ (비밀 벡터)
노이즈: e ∈ ℤqᵐ (작은 오차·가우시안 분포)

→ A·s를 알아도 노이즈 e 때문에 s 역산 불가
→ 양자컴퓨터도 다항식 시간 내 해결 불가(NP-hard 추정)
→ q를 모듈러스로 사용 → Module-LWE(MLWE) = ML-KEM 기반
```

**라. Ring-LWE → Module-LWE 진화**

| 유형             | 구조             | 특징          | 대표                   |
| -------------- | -------------- | ----------- | -------------------- |
| **LWE**        | 정수 행렬 기반       | 안전하나 키 크기 大 | 원형 격자 암호             |
| **Ring-LWE**   | 다항식 환(Ring) 기반 | 효율성↑·키 크기↓  | NTRU                 |
| **Module-LWE** | RLWE 모듈 확장     | 효율성+안전성 균형  | **ML-KEM(FIPS-203)** |

---

#### Ⅲ. ML-KEM 핵심 구조 및 동작

**가. ML-KEM 개요**

| 항목        | 내용                                     |
| --------- | -------------------------------------- |
| **표준명**   | FIPS-203 (NIST 2024.8 확정)              |
| **구 명칭**  | CRYSTALS-Kyber                         |
| **기반 문제** | Module-LWE (MLWE)                      |
| **용도**    | 키 캡슐화(KEM·Key Encapsulation Mechanism) |
| **파라미터**  | ML-KEM-512·768·1024 (보안 강도별)           |

**나. ML-KEM 3단계 동작**

```
[ML-KEM 동작 흐름]

==①키 생성 (KeyGen)==
  행렬 A ← 의사난수 생성기(SHAKE-128)
  비밀벡터 s, e ← 작은 노이즈 분포 샘플링
  공개키 pk = (A, t = A·s + e)
  비밀키 sk = s
       ↓
==②캡슐화 (Encapsulate) — 송신자==
  랜덤 메시지 m 생성
  r, e₁, e₂ ← 노이즈 샘플링
  u = Aᵀ·r + e₁  (암호문 1)
  v = tᵀ·r + e₂ + ⌊q/2⌋·m  (암호문 2)
  공유키 K = Hash(m)
  송신: 암호문 (u, v) 전달
       ↓
==③탈캡슐화 (Decapsulate) — 수신자==
  m' = v - sᵀ·u  (노이즈 제거·반올림)
  공유키 K' = Hash(m')
  → K = K' 성립 → 공유 비밀 키 수립 완료
```

**다. ML-KEM 파라미터 비교**

|파라미터|ML-KEM-512|ML-KEM-768|ML-KEM-1024|
|---|---|---|---|
|**보안 수준**|AES-128 동급|AES-192 동급|AES-256 동급|
|**공개키 크기**|800 바이트|1,184 바이트|1,568 바이트|
|**비밀키 크기**|1,632 바이트|2,400 바이트|3,168 바이트|
|**암호문 크기**|768 바이트|1,088 바이트|1,568 바이트|
|**적용 환경**|IoT·경량|범용 서비스|고보안 국방·금융|

---

#### Ⅳ. 기존 공개키 암호와의 비교

| 비교 항목      | RSA-2048      | ECC-256       | **ML-KEM-768**     |
| ---------- | ------------- | ------------- | ------------------ |
| **안전성 근거** | 소인수분해         | 타원곡선 이산대수     | **Module-LWE**     |
| **양자 위협**  | 쇼어 알고리즘 취약 🚨 | 쇼어 알고리즘 취약 🚨 | **양자내성 ✅**         |
| **공개키 크기** | 256 바이트       | 64 바이트        | 1,184 바이트          |
| **연산 속도**  | 느림            | 빠름            | **매우 빠름**          |
| **구현 용이성** | 높음            | 중간            | 중간                 |
| **표준화**    | PKCS#1·X.509  | SEC2·RFC      | **FIPS-203(2024)** |
| **용도**     | 암호화·서명        | 서명·키교환        | **키 캡슐화(KEM)**     |

**키 크기 증가 대응 전략**

```
RSA(256B) → ML-KEM(1,184B): 약 4.6배 증가
→ 대응: TLS 핸드셰이크 최적화·세션 재사용
→ 하이브리드 모드: RSA/ECC + ML-KEM 병행
  (전환 과도기 암호민첩성 확보 수단)
```

---

#### Ⅴ. 결론 및 국내외 적용 현황

**국내외 적용 현황**

| 구분                | 내용                                |
| ----------------- | --------------------------------- |
| **NIST FIPS-203** | ML-KEM 2024.8 최종 표준 확정            |
| **국내 KpqC**       | SMAUG-T(격자·키캡슐화)·HAETAE(격자·서명) 선정 |
| **전환 목표**         | 2035년 국가 암호체계 PQC 전환 완료           |
| **시범전환**          | 에너지·의료·행정 3개→통신·금융·교통 5개 분야 확대    |
| **하이브리드 전환**      | 기존 RSA·ECC + ML-KEM 병행 운영(과도기)    |

**앞서 다룬 개념과의 연결**

```
CRQC 위협(2035 예상)
    → HNDL 공격(지금 수집·나중 해독)
    → 격자 기반 LWE 난제(양자내성)
    → ML-KEM FIPS-203(키 캡슐화)
    → ML-DSA FIPS-204(서명·격자 기반)
    → SLH-DSA FIPS-205(서명·해시 기반)
    → 암호민첩성(Crypto-Agility): 알고리즘 교체 유연 설계
    → KCMVP 국내 검증·국가 2035 전환 완료
```

---

#### 기술사 답안 포인트

**격자(Lattice)·SVP·CVP·LWE의 수학적 원리 → Module-LWE로 진화 → ML-KEM KeyGen·Encapsulate·Decapsulate 3단계 → FIPS-203 파라미터(512·768·1024) → RSA·ECC 대비 키 크기 증가 한계·하이브리드 전환 → KpqC SMAUG-T·HAETAE 국내 연계 → 2035 PQC 전환 목표** 흐름으로 서술하면 수학적 원리·표준화·국내 정책을 아우르는 완성도 높은 답안이 됩니다. **LWE 수식(b = A·s + e)이 핵심 차별화 포인트**입니다.



#### **I. [도입] 양자 컴퓨터의 수학적 장벽, 격자 기반 암호(Lattice-based)와 표준 ML-KEM의 개요**

- **정의:** 격자 기반 암호는 nn차원 격자(Lattice) 공간 내 최단 벡터 탐색(SVP) 등 수학적 난제를 활용하여 양자 컴퓨터의 Shor(쇼어) 알고리즘 공격에 저항하도록 설계된 비대칭 키 암호 기술이며, **`ML-KEM (Module-Lattice Key Encapsulation Mechanism)`**은 NIST가 CRYSTALS-Kyber를 기반으로 표준화(FIPS 203)한 차세대 격자 기반 키 캡슐화 규격.
- **배경:** 양자 컴퓨터가 실현될 시 기존 소인수분해(RSA) 및 이산대수(ECC) 기반 비대칭 키 알고리즘이 다항 시간 내에 완전 붕괴할 위험에 대응하여, 전 세계 국가 암호망을 표준 양자내성암호(PQC) 체계로 신속 전환하기 위함.

#### **II. [본론 1] (극단적 단순화 버전) 표준 ML-KEM 기반의 안전한 키 캡슐화 및 합의 3단계 흐름**

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NTQuNjM3IDI1NyIgd2lkdGg9IjQ1NC42MzciIGhlaWdodD0iMjU3IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9InNlcS1hcnJvdyIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iOCIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJzZXEtYXJyb3ctb3BlbiIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iOCIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWxpbmUgcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxsaW5lIGNsYXNzPSJsaWZlbGluZSIgZGF0YS1hY3Rvcj0iQWxpY2UiIHgxPSIxNTguOTUyIiB5MT0iNzAiIHgyPSIxNTguOTUyIiB5Mj0iMjI3IiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtZGFzaGFycmF5PSI2IDQiIC8+CjxsaW5lIGNsYXNzPSJsaWZlbGluZSIgZGF0YS1hY3Rvcj0iQm9iIiB4MT0iMjk4Ljk1MiIgeTE9IjcwIiB4Mj0iMjk4Ljk1MiIgeTI9IjIyNyIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWRhc2hhcnJheT0iNiA0IiAvPgo8ZyBjbGFzcz0ibWVzc2FnZSIgZGF0YS1mcm9tPSJBbGljZSIgZGF0YS10bz0iQm9iIiBkYXRhLWxhYmVsPSIyLiDqs7XqsJztgqQgKFBLKSDsoITshqEiIGRhdGEtbGluZS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctaGVhZD0iZmlsbGVkIiBkYXRhLXNlbGY9ImZhbHNlIj4KICA8bGluZSB4MT0iMTU4Ljk1MiIgeTE9IjkwIiB4Mj0iMjk4Ljk1MiIgeTI9IjkwIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI3NlcS1hcnJvdykiIC8+CiAgPHRleHQgeD0iMjI4Ljk1MiIgeT0iODAiIGZvbnQtc2l6ZT0iMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LW11dGVkKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+Mi4g6rO16rCc7YKkIChQSykg7KCE7IahPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJtZXNzYWdlIiBkYXRhLWZyb209IkJvYiIgZGF0YS10bz0iQWxpY2UiIGRhdGEtbGFiZWw9IjQuIOyVlO2YuOusuCAoQykg7KCE7IahIiBkYXRhLWxpbmUtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LWhlYWQ9ImZpbGxlZCIgZGF0YS1zZWxmPSJmYWxzZSI+CiAgPGxpbmUgeDE9IjI5OC45NTIiIHkxPSIxNDUiIHgyPSIxNTguOTUyIiB5Mj0iMTQ1IiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI3NlcS1hcnJvdykiIC8+CiAgPHRleHQgeD0iMjI4Ljk1MiIgeT0iMTM1IiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1tdXRlZCkiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjQuIOyVlO2YuOusuCAoQykg7KCE7IahPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub3RlIiBkYXRhLXBvc2l0aW9uPSJvdmVyIiBkYXRhLWFjdG9ycz0iQm9iIj4KICA8cG9seWdvbiBwb2ludHM9IjE3My4yNjcsOTggNDE4LjYzNzAwMDAwMDAwMDA2LDk4IDQyNC42MzcwMDAwMDAwMDAwNiwxMDQgNDI0LjYzNzAwMDAwMDAwMDA2LDEyMSAxNzMuMjY3LDEyMSIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8cG9seWdvbiBwb2ludHM9IjQxOC42MzcwMDAwMDAwMDAwNiw5OCA0MjQuNjM3MDAwMDAwMDAwMDYsMTA0IDQxOC42MzcwMDAwMDAwMDAwNiwxMDQiIGZpbGw9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyOTguOTUyIiB5PSIxMDkuNSIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtbXV0ZWQpIj48dHNwYW4geD0iMjk4Ljk1MiIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPjMuIEVuY2Fwc3VsYXRlKFBLKTwvdHNwYW4+PHRzcGFuIHg9IjI5OC45NTIiIGR5PSIxNC4zIj4o6rO17Ya17YKkIEsgJmFtcDsg7JWU7Zi466y4IEMg7IOd7ISxKTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub3RlIiBkYXRhLXBvc2l0aW9uPSJvdmVyIiBkYXRhLWFjdG9ycz0iQWxpY2UiPgogIDxwb2x5Z29uIHBvaW50cz0iMzAsMTUzIDI4MS45MDQsMTUzIDI4Ny45MDQsMTU5IDI4Ny45MDQsMTc2IDMwLDE3NiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8cG9seWdvbiBwb2ludHM9IjI4MS45MDQsMTUzIDI4Ny45MDQsMTU5IDI4MS45MDQsMTU5IiBmaWxsPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTU4Ljk1MiIgeT0iMTY0LjUiIGZvbnQtc2l6ZT0iMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LW11dGVkKSI+PHRzcGFuIHg9IjE1OC45NTIiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij41LiBEZWNhcHN1bGF0ZShDLCBTSyk8L3RzcGFuPjx0c3BhbiB4PSIxNTguOTUyIiBkeT0iMTQuMyI+KOuPmeydvO2VnCDqs7XthrXtgqQgSyDrs7XtmLjtmZQpPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vdGUiIGRhdGEtcG9zaXRpb249Im92ZXIiIGRhdGEtYWN0b3JzPSJBbGljZSxCb2IiPgogIDxwb2x5Z29uIHBvaW50cz0iOTIuNTc0OTk5OTk5OTk5OTksMTgwIDM1OS4zMjksMTgwIDM2NS4zMjksMTg2IDM2NS4zMjksMjAzIDkyLjU3NDk5OTk5OTk5OTk5LDIwMyIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8cG9seWdvbiBwb2ludHM9IjM1OS4zMjksMTgwIDM2NS4zMjksMTg2IDM1OS4zMjksMTg2IiBmaWxsPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjI4Ljk1MiIgeT0iMTkxLjUiIGZvbnQtc2l6ZT0iMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LW11dGVkKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+7J6E7IucIOyEuOyFmCDtgqQoSykg7ZWp7J2YIOyZhOujjCAo7JaR7J6QIO2VtOuPhSDsoIDtla3shLEg7ZmV67O0KTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iYWN0b3IiIGRhdGEtaWQ9IkFsaWNlIiBkYXRhLWxhYmVsPSJBbGljZSIgZGF0YS10eXBlPSJwYXJ0aWNpcGFudCI+CiAgPHJlY3QgeD0iMTE4Ljk1MiIgeT0iMzAiIHdpZHRoPSI4MCIgaGVpZ2h0PSI0MCIgcng9IjQiIHJ5PSI0IiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTU4Ljk1MiIgeT0iNTAiIGZvbnQtc2l6ZT0iMTMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkFsaWNlPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJhY3RvciIgZGF0YS1pZD0iQm9iIiBkYXRhLWxhYmVsPSJCb2IiIGRhdGEtdHlwZT0icGFydGljaXBhbnQiPgogIDxyZWN0IHg9IjI1OC45NTIiIHk9IjMwIiB3aWR0aD0iODAiIGhlaWdodD0iNDAiIHJ4PSI0IiByeT0iNCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjI5OC45NTIiIHk9IjUwIiBmb250LXNpemU9IjEzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5Cb2I8L3RleHQ+CjwvZz4KPC9zdmc+)

#### **III. [본론 2] 격자 암호 아키텍처 및 표준 ML-KEM 상세 분석 (3단 표)**

이 토픽은 실무적 합격점 확보를 위해 **'M-LWE(모듈 에러학습)의 수학적 난제 아키텍처'**와 **'NIST FIPS 203의 표준 규격 파라미터(ML-KEM-512/768/1024)'**, 그리고 **'기존 RSA/ECC 대체 시 대역폭(키/시그니처 크기) 및 연산 오버헤드 최적화'**를 답안지에 구체적으로 기술하는 것이 합격의 고득점 열쇠입니다.

| **핵심 척도**                | **📊 격자 기반 암호 (Lattice-based) 🚨**                                                                                                    | **🔑 ML-KEM (FIPS 203 표준 KEM) 💯**                                                                                                                                                  | **💼 수학적 안전성 모델 (SVP/LWE) 💯**                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **개념 / 역할**              | **'양자 저항의 수학적 근간'.** 다차원 격자 공간 내 이산 기하학적 난제를 기반으로 하여, Shor 알고리즘으로도 해독 불가능한 공개키 암호 기반 모델.                                              | **'글로벌 표준 키 합의 알고리즘'.** NIST가 2024년 8월 공식 표준(FIPS 203)으로 공표한 모듈 격자 기반의 차세대 키 캡슐화 규격.                                                                                                | **'격자 난제의 연산 환원 모델'.** 암호키 유추를 격자 수학 난제(SVP/CVP)로 환원하여, 수학적으로 역산이 불가능함을 증명하는 모델.                                                                               |
| **핵심 세부 요건 (출제 포인트) 🚨** | **1. 높은 활용 범용성** (키 교환, 서명뿐 아니라 완전 동형암호(FHE)로도 파생).  <br>**2. 병렬 연산 적합성** (행렬 곱 기반 빠른 연산 속도).  <br>**3. 하드웨어 가속** (NTT 다항식 곱셈 변환 가속). | **1. M-LWE (Module-LWE) 기반** (일반 LWE의 키 크기 한계와 Ring-LWE의 보안 리스크 절충).  <br>**2. 3대 보안 파라미터 제공** (ML-KEM-512 / 768 / 1024 규격).  <br>**3. AES 암호 강도 동치** (각각 AES-128, 192, 256 등급 매핑). | **1. SVP (최단 벡터 문제)**: 격자 상 영이 아닌 가장 짧은 벡터 탐색 난제.  <br>**2. CVP (최근접 벡터 문제)**: 격자 밖 임의 점에서 가장 가까운 격자점 탐색 난제.  <br>**3. LWE / M-LWE**: 노이즈가 추가된 선형 연산의 해 유추 난제. |
| **핵심 고려 사항**             | 기존 RSA/ECC 대비 공개키 및 암호문 크기가 킬로바이트(KB) 수준으로 증가하여, 네트워크 **패킷 단편화(MTU 초과)** 유발 리스크 상존.                                                   | SSL/TLS 1.3 내에 기존 암호와 병행 기동하는 **하브리드 모드(Dual-key)** 연동 규격 수립 및 **국내 KCMVP 보안인증 개편**이 필수적임.                                                                                          | 격자 기하학 차원 감소 알고리즘인 **BKZ 알고리즘** 및 근사화 공격 기법에 대항하는 충분한 안전성 비트(Bit Security) 설정 필요.                                                                              |
|                          |                                                                                                                                       |                                                                                                                                                                                     |                                                                                                                                                                |

#### **IV. [결론/제언] 공공·금융 전산망의 안전한 전환을 위한 가이드라인 및 실무 검증 방안**

- **(키워드 위주 2줄 마무리)** "국내 PQC 암호 전환의 성공을 위해서는 NIST FIPS 203 규격을 충족하는 **ML-KEM 알고리즘의 공공 시스템 의무 탑재 가이드라인**을 신속히 배포해야 합니다. 이를 위해 **KCMVP 내 격자 기반 암호 평가 기준 수립을 가속하고, 기존 레거시 시스템과의 네트워크 대역폭 병목(MTU 조절) 및 CPU 연산 지연을 사전에 검증할 하이브리드 필드 테스트베드 활성화가 시급한 제언입니다.**"
