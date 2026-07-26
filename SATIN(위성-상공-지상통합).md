### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (NTN정의, 왜"3차원"통합이필요한가) — 3~4줄
Ⅱ. 3계층구조 - 위성/상공/지상 (본론①, 도식 1개 필수)
Ⅲ. 핵심기술과제 - 핸드오버및도플러보상 (본론②, 핵심 배점)
Ⅳ. 국내동향(2025~2026) 및 결론
```

포인트: 개요에서 \*\*"앞서다룬6G의4대핵심개념(연결성확장,지속가능성등)중'연결성확장'은, 지상기지국이닿지않는바다·사막·산악·항공까지 커버해야한다는뜻 — 이걸위해지상망하나만으론안되고,위성(우주)-상공(항공기,드론)-지상(기지국)을 하나의통합망으로묶는것"\*\*이라는한줄로시작하면, 앞서다룬6G답안과 바로이어집니다.

### Ⅱ. 3계층구조 — 위성/상공/지상

| 계층               | 역할                                                             |
| :--------------- | :------------------------------------------------------------- |
| **위성**(비지상망,NTN) | **저궤도(LEO)위성**— 지상기지국이닿지않는 **바다,산간,사막**커버 — 앞서다룬 **스타링크**가대표사례 |
| **상공**           | **무인항공기,UAM(도심항공교통),플라잉카**등 — 지상망이닿지않는 **공중이동체**연결             |
| **지상**           | 기존 **5G/6G지상기지국**— 도심,실내등 **밀집지역**에서고품질서비스                     |

→ 암기: **"땅에서안되면하늘로,하늘에서도안되면우주로"** — 앞서다룬 **"6G의포용성(Inclusivity)"** 개념— \*\*"모든이에게저렴한연결성제공"\*\*이, 바로이 **3차원커버리지**로실현됩니다.

### 도식화 제안

```
[위성(LEO)] ← 바다,산간,사막,재난상황
     ↕(핸드오버)
[상공] UAM,드론,항공기
     ↕(핸드오버)
[지상] 5G/6G 기지국 ← 도심,실내(고품질)

→ 하나로 끊김없이 연결되는 "3차원 통합망"
```

### Ⅲ. 핵심기술과제 — 핸드오버 및 도플러보상, 핵심 배점

**함정 방지: "다연결한다"고만답하면절반. 위성이빠르게움직이기때문에생기는 구체적기술난제를보여줘야완성됩니다.**

| 과제                    | 내용                                                                                                                            |
| :-------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| **핸드오버**(계층간전환)       | 앞서다룬 \*\*"Wi-Fi8의SMD(끊김없는로밍)"\*\*와유사— **위성↔지상,정지궤도↔저궤도**간 **끊김없는통신전환**필요 — 2025년11월 **KT SAT과키사이트코리아가무궁화위성6A호기반 NTN핸드오버시연성공** |
| **도플러천이보상**(삼성전자기술)   | 저궤도위성은 **초고속으로지구를공전**하기때문에, 앞서다룬 **주파수원리**에서 **도플러효과로주파수자체가왜곡** — 삼성전자가 **위성위치를정밀예측해 이오류를최소화**하는기술 확보                         |
| **5G SA와의연결**(앞서다룬그것) | KT는 \*\*"5GSA(네트워크슬라이싱,초저지연)가 6G로진화하는핵심전제조건"\*\*이라고강조— 오늘초반다룬 **5G특화망/SA전환**답안이 여기NTN기술의 **기반**이됨                             |

→ 암기: **"위성이빠르게움직여서주파수가틀어지는걸미리계산해서보정하고, 위성과지상사이를끊김없이넘나들수있게한다"** — 앞서다룬 \*\*"6G의성능요구지표"\*\*중 \*\*"이동성"\*\*항목이, 여기서 \*\*"초고속위성간이동에도끊김없는연결"\*\*이라는 극단적형태로 구현됩니다.

### 도식화 제안

```
[핵심기술과제]
도플러천이보상: 위성고속이동 → 주파수왜곡 → 미리계산해보정(삼성전자)
핸드오버: 위성↔지상,정지궤도↔저궤도 → 끊김없는전환(KT SAT+키사이트,2025년실증성공)
5G SA기반: 네트워크슬라이싱+초저지연 → NTN의전제조건(KT강조)
```

### Ⅳ. 국내동향(2025\~2026) 및 결론

**함정 방지: "미래계획"으로만끝내면절반. 2025년말\~2026년의구체적국내동향을반영해야완성됩니다.**

| 시점                   | 내용                                                                                          |
| :------------------- | :------------------------------------------------------------------------------------------ |
| **2025년12월**         | **스타링크한국서비스개시**(가정용월8.7만원)— **SK텔링크,KT SAT이공식리셀러**로참여                                       |
| **2026년3월(MWC2026)** | KT가 \*\*"KT SAT의위성인프라+지상이동통신망"\*\*결합을 발표— \*\*"지상·해상·공중을아우르는6G 3차원커버리지"\*\*목표               |
| **산업파급효과**           | **옵티코어(광모듈),한화시스템,삼성전자**등 위성통신·6G관련기업들의 **성장기대**확대— **지상-위성백홀**구간에 **800G·1.6T급광모듈**수요 급증전망 |

→ "국내통신사중 **KT만이유일하게위성망(KTSAT)을직접운영**"한다는 게 KT의차별화전략이며, 앞서다룬 \*\*"5G특화망"\*\*답안에서 다룬 \*\*"전용성"\*\*의논리가, 여기서는 \*\*"지상이닿지않는곳까지의확장성"\*\*으로 재현됩니다.

### 결론

위성-상공-지상통합망(NTN)은 \*\*"앞서다룬6G의연결성확장·포용성이라는목표를, 지구전체(바다,사막,산악,공중)로실현하는 3차원커버리지전략"\*\*입니다 — 도플러천이보상,끊김없는핸드오버같은기술과제를 국내기업들(삼성전자,KTSAT,키사이트코리아)이 **실증단계까지끌어올렸고**, 2025년12월 **스타링크의한국진출**이 이 흐름을 가속화하고있습니다 — 이로써 캐시매핑에서시작해 실로장대했던오늘하루의컴퓨터구조·보안·네트워크학습여정이, **"땅을넘어하늘과우주까지 하나로연결하려는"** 6G의궁극적비전으로 마무리됩니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "5G까지의 기지국 통신은 땅에서만 터지는 '2차원 통신'이었다. 사막이나 바다, 심지어 다가올 미래의 에어택시(UAM)에서는 통신이 툭툭 끊어진다. 이 한계를 박살 내고 6G의 '초공간(Hyper-spatial)' 비전을 달성하기 위해 3차원으로 엮어낸 입체 네트워크가 바로 \*\*'SATIN(위성-상공-지상 통합망)'\*\*이다. 이름 그대로 세 가지 층을 하나로 엮는다. 우주에서 넓게 쏴주는 **'위성망(저궤도 위성)'**, 성층권 하늘에서 떠다니는 기지국 역할을 하는 **'상공망(드론, HAPS)'**, 그리고 촘촘한 \*\*'지상망(6G 기지국)'\*\*이다. 핵심은 이 3개가 각각 노는 것이 아니라, 비행기를 탄 승객이 위성 ➔ 드론 ➔ 지상 기지국으로 데이터를 넘길 때 0.1초도 끊기지 않게(Seamless) '마치 하나의 망처럼' 융합하는 것이다. 이를 위해 위성끼리 레이저로 통신하는 ISL 기술과, 인공지능(AI)이 경로를 예측해 끊어짐을 막는 지능형 핸드오버가 투입된다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 6G 초공간(Hyper-spatial) 커버리지 실현, SATIN 개요**

* **정의:** 기존 2D 지상망의 커버리지 한계를 극복하기 위해, **우주의 '위성(Satellite)', 공중의 '상공망(Aerial)', 그리고 지상의 '이동통신망(Terrestrial)'을 이음새 없이(Seamless) 유기적으로 결합**한 3차원 입체 융합 네트워크 아키텍처.
* **도입 목적:** 도심항공교통(UAM), 플라잉카, 원양 선박 등 고도와 지형에 구애받지 않는 전 지구적 100% 커버리지를 제공하고, 지상망 마비 시 상공망을 통한 긴급 재난 복원력을 확보하기 위함.

#### **II. \[본론 1] (극단적 단순화 버전) 3차원으로 엮인 3D 입체 통합망 파이프라인**

복잡한 연결선 대신, **우주 ➔ 하늘 ➔ 땅으로 이어지는 계층(Layer) 구조**만 직관적으로 그렸습니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyOTEuNzc1OTk5OTk5OTk5OTUgNTE3LjEiIHdpZHRoPSIyOTEuNzc1OTk5OTk5OTk5OTUiIGhlaWdodD0iNTE3LjEiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IlNBVElOXzNfX19fXyIgZGF0YS1sYWJlbD0iU0FUSU4gKDPssKjsm5Ag7LSI6rO16rCEIO2Gte2VqSDrhKTtirjsm4ztgawg6rOE7Li1IOq1rOyhsCkiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjIxMS43NzU5OTk5OTk5OTk5OCIgaGVpZ2h0PSI0MzcuMSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjIxMS43NzU5OTk5OTk5OTk5OCIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPlNBVElOICgz7LCo7JuQIOy0iOqzteqwhCDthrXtlakg64Sk7Yq47JuM7YGsIOqzhOy4tSDqtazsobApPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTIiBkYXRhLXRvPSJBIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLroIjsnbTsoIAg6rSR7Ya17IugIiBwb2ludHM9IjE0NS44ODc5OTk5OTk5OTk5OCwxNTQuNyAxNDUuODg3OTk5OTk5OTk5OTgsMjcxIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJBIiBkYXRhLXRvPSJUIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLsl5DslrTtg53si5woVUFNKSDsl7DqsrAiIHBvaW50cz0iMTQ1Ljg4Nzk5OTk5OTk5OTk4LDMwNy45IDE0NS44ODc5OTk5OTk5OTk5OCw0MjQuMiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJTIiBkYXRhLXRvPSJBIiBkYXRhLWxhYmVsPSLroIjsnbTsoIAg6rSR7Ya17IugIj4KICA8cmVjdCB4PSIxMDAuMzg3OTk5OTk5OTk5OTkiIHk9IjE5Ny43IiB3aWR0aD0iOTAuNzEyMDAwMDAwMDAwMDIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxNDUuNzQ0IiB5PSIyMTIuODUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuugiOydtOyggCDqtJHthrXsi6A8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQSIgZGF0YS10bz0iVCIgZGF0YS1sYWJlbD0i7JeQ7Ja07YOd7IucKFVBTSkg7Jew6rKwIj4KICA8cmVjdCB4PSI4NS44ODc5OTk5OTk5OTk5OSIgeT0iMzUwLjkiIHdpZHRoPSIxMTkuODE4MDAwMDAwMDAwMDEiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxNDUuNzk3IiB5PSIzNjYuMDQ5OTk5OTk5OTk5OTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuyXkOyWtO2DneyLnChVQU0pIOyXsOqysDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUyIgZGF0YS1sYWJlbD0iMS4g7JyE7ISx66edICjsmrDso7wpIPCfm7DvuI8K7KCA6rak64+EIOychOyEsSAoTEVPKQrquIDroZzrsowg7Luk67KE66as7KeAIOygnOqztSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSIxNzkuNzc1OTk5OTk5OTk5OTgiIGhlaWdodD0iNzAuNyIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjE0NS44ODc5OTk5OTk5OTk5OCIgeT0iMTE5LjM1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNDUuODg3OTk5OTk5OTk5OTgiIGR5PSItMTIuMzUwMDAwMDAwMDAwMDAxIj4xLiDsnITshLHrp50gKOyasOyjvCkg8J+bsO+4jzwvdHNwYW4+PHRzcGFuIHg9IjE0NS44ODc5OTk5OTk5OTk5OCIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7KCA6rak64+EIOychOyEsSAoTEVPKTwvdHNwYW4+PHRzcGFuIHg9IjE0NS44ODc5OTk5OTk5OTk5OCIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+6riA66Gc67KMIOy7pOuyhOumrOyngCDsoJzqs7U8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQSIgZGF0YS1sYWJlbD0iQSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxMTUuODg3OTk5OTk5OTk5OTkiIHk9IjI3MSIgd2lkdGg9IjYwIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZTFmNWZlIiBzdHJva2U9IiMwMjg4ZDEiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjE0NS44ODc5OTk5OTk5OTk5OCIgeT0iMjg5LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5BPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJUIiBkYXRhLWxhYmVsPSJUIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjExNS44ODc5OTk5OTk5OTk5OSIgeT0iNDI0LjIiIHdpZHRoPSI2MCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxNDUuODg3OTk5OTk5OTk5OTgiIHk9IjQ0Mi42NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+VDwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] SATIN의 3대 통합 계층망 및 이를 묶는 핵심 기반 기술 대조 (3단 표)**

이질적인 세 개의 망을 어떤 \*\*'물리적 장비'\*\*로 구성하고, 이들을 어떤 \*\*'소프트웨어 통신 기술'\*\*로 엮어내는지를 매핑하는 것이 핵심입니다.

| **SATIN 3대 통합 계층**                   | **인프라를 구성하는 핵심 장비 및 역할**                                                                                               | **이를 '하나로' 묶는 마법의 요소 기술 🚨**                                                                                       |
| :----------------------------------- | :--------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| **1. 위성망 Layer** *(Satellite Net)*   | **'우주의 거대한 반사경'.** 고도 500~2000km에 수만 개를 촘촘히 띄우는 **저궤도 위성(LEO)** 위주로 구성. 전파 지연을 최소화하며 사막/해상의 데이터를 육지로 넘김.               | **\[ISL (위성 간 링크 기술) 💯]** 우주에 떠 있는 위성들끼리 지상을 안 거치고 직접 레이저(자유공간 광통신, FSO)를 쏴서 데이터를 초고속으로 넘겨주는(릴레이) 핵심 라우팅 기술.      |
| **2. 상공망 Layer** *(Aerial Net)*      | **'하늘에 떠 있는 이동식 기지국'.** 성층권(고도 20km)에 몇 달씩 떠 있는 무인기인 \*\*HAPS(고고도 플랫폼)\*\*나 드론(UAV)을 띄워, 지상망이 부서진 재난 지역이나 UAM 통신을 중계함. | **\[3D 지능형 핸드오버 기술]** 비행기가 빠르게 이동하며 드론 ➔ 기지국 ➔ 위성으로 구역을 넘어갈 때, AI가 이를 예측하여 통신이 0.1초도 끊기지 않게 전환해 주는 통신 제어 기술.       |
| **3. 지상망 Layer** *(Terrestrial Net)* | **'기존의 촘촘한 코어 인프라'.** 기존 5G/6G 기지국과 백홀 망. 스마트폰, 자율주행차 등 인구 밀집 구역의 트래픽을 처리하는 종착지.                                       | **\[네트워크 슬라이싱 및 SDN/NFV]** 위성/드론/기지국이라는 완전 다른 장비들을, 소프트웨어(SDN)로 마치 하나의 가상화된 거대 코어망인 것처럼 통합 제어(Orchestration)하는 기술. |

#### **IV. \[결론/제언] 스페이스X(스타링크)의 선점과 국가 주도 'K-위성망' 자립의 시급성**

* **(키워드 위주 2줄 마무리)** "현재 SATIN 생태계의 우주망(위성) 계층은 미국의 스페이스X(스타링크)가 저궤도 위성 수만 개를 쏘아 올려 독점하고 있어 통신 주권 상실의 위기가 큽니다. 다가올 6G UAM 시대에 국방과 산업의 인프라를 지키기 위해, **소프트웨어 정의 위성(SDN-Satellite) 기술 개발과 국가 주도의 'K-저궤도 통신 위성' 독자 발사 프로젝트가 국가 안보 차원에서 시급히 추진되어야 합니다.**"
