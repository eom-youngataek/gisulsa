### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (디스크이미징정의, 원본불가침원칙과의연결) — 3~4줄
Ⅱ. D2D vs D2F 핵심차이 (본론①, 도식 1개 필수)
Ⅲ. 이미징절차및무결성검증 (본론②, 핵심 배점)
Ⅳ. 결론
```

### Ⅰ. 개요

앞서다룬 \*\*"포렌식절차의②수집단계"\*\*에서 \*\*"원본은절대건드리지않는다"\*\*는 원칙을 지키려면, 원본디스크를 **비트단위(bit-by-bit)로완전히복제**해야합니다 — 파일하나씩복사하는게아니라, **삭제된영역,여유공간까지포함한디스크전체**를 그대로옮기는것이 핵심입니다. 이때 \*\*"어디에담을지"\*\*에따라 D2D와D2F로 나뉩니다.

### Ⅱ. D2D vs D2F — 핵심차이

| 구분      | **D2D**(Disk-to-Disk)      | **D2F**(Disk-to-File)        |
| :------ | :------------------------- | :--------------------------- |
| **대상**  | 원본디스크를 **다른물리디스크**에 그대로복제  | 원본디스크를 **하나의이미지파일**로변환       |
| **결과물** | 원본과 **동일한형태의또다른디스크**       | **.dd,.E01,.raw**등 **파일하나**  |
| **장점**  | **즉시부팅·마운트가능**(실제디스크처럼사용)  | **저장·전송·백업이용이**(파일이라압축·분할가능) |
| **단점**  | 대상디스크 **크기가원본이상이어야**,보관부피큼 | 분석도구로 **마운트해야만내용확인가능**       |

→ 암기: **"D2D는디스크를디스크로(즉시쓸수있는사본), D2F는디스크를파일로(보관·전송하기좋은형태)"** — 실무에서는 \*\*E01(EnCase포맷)\*\*같이 **압축+해시값내장**까지지원하는 **D2F형식이더보편적**으로쓰입니다.

### 도식화 제안

```
[원본디스크]
     ↓
   ┌─────┴─────┐
[D2D]              [D2F]
원본→다른디스크로직접복제    원본→이미지파일(.E01등)로변환
    ↓                        ↓
[복제디스크]                [이미지파일]
(그대로부팅·마운트가능)      (분석도구로열어서확인)
```

### Ⅲ. 이미징절차및무결성검증 — 핵심 배점

**함정 방지: "복사하면끝"이라고답하면절반. 앞서다룬"해시값"이 왜여기서도필수인지, 그리고쓰기방지가왜중요한지보여줘야완성됩니다.**

| 단계            | 내용                                                                |
| :------------ | :---------------------------------------------------------------- |
| **①쓰기방지장치연결** | 앞서다룬 **WriteBlocker**로 원본에 **어떤변경도불가능**하게물리적차단                    |
| **②이미징수행**    | \*\*비트단위(bit-by-bit)\*\*로 **삭제영역·여유공간까지** 전체복제(dd,FTKImager등도구사용) |
| **③해시값산출**    | 원본과이미지 **각각의해시값(MD5/SHA-256)을계산**해 **일치여부확인**                     |
| **④CoC기록**    | 앞서다룬 **ChainofCustody**에 이미징수행자,시각,장비 기록                          |

→ 암기: **"쓰기를막고,전부(빈공간까지)복제하고,해시로증명하고,누가했는지남긴다"** — 앞서다룬 \*\*"포렌식의무결성보장기법"\*\*이 여기서 **구체적으로실행되는순서**로 재현됩니다 — 특히 **"해시값이하나라도다르면, 그이미지는법정에서원본과동일하다고인정받지못합니다"**.

### 도식화 제안

```
[원본디스크] ──WriteBlocker(쓰기차단)──→ [이미징도구]
                                              ↓
                                   비트단위전체복제
                                   (여유공간·삭제영역포함)
                                              ↓
                              [원본해시값] ?= [이미지해시값]
                                              ↓ 일치해야
                                   법적으로 "동일함" 인정
```

### Ⅳ. 결론

D2D와D2F는 \*\*"원본을절대손대지않고 완전히똑같은복제본을만든다"\*\*는 같은목표를, **"결과물을디스크로할지,파일로할지"** 다른형태로달성하는방법입니다 — 앞서다룬 **파일카빙**이 이미징된복제본(또는이미지파일) 안에서 **삭제된파일을찾는분석기법**이었다면, 디스크이미징은 그 **분석대상자체를 안전하게확보하는수집단계**입니다. 이두답안은 앞서다룬 \*\*"포렌식절차5단계"\*\*중 \*\*수집(이미징)→분석(카빙)\*\*으로 정확히 순서대로이어지는 실무흐름을 완성합니다.

### **1. 답안 전개 스토리 (암기 직결 숏폼)**

> "살인 사건 현장에서 경찰은 피 묻은 칼(증거 원본)을 비닐봉지에 넣고 봉인하지, 절대 그 칼로 종이를 썰어보며 테스트하지 않는다. 포렌식 수사관도 마찬가지다. 범죄자의 하드디스크(원본)를 확보하면 절대 자기 컴퓨터에 꽂아 부팅하거나 파일을 열어보지 않는다. 열어보는 순간 윈도우 로그가 기록되어 원본이 훼손(무결성 파괴)되고, 판사는 그 증거를 쓰레기통에 던져버리기 때문이다. 그래서 수사관은 원본 하드에 '쓰기 방지 장치(Write Blocker)'를 채워 자물쇠를 건 뒤, 똑같은 쌍둥이 복사본을 만들어 오직 그 복사본만 분석하는데 이를 \*\*'디스크 이미징'\*\*이라 한다. 이미징에는 두 가지 방식이 있다. 범인의 1TB 하드를 똑같이 생긴 새 1TB 하드디스크 '기계'에 1:1로 굽는 **'Disk to Disk (D2D)'** 방식과, 범인의 하드 전체를 압축해서 거대한 파일 1개(E01 포맷 등)로 똘똘 뭉쳐 내 USB에 파일 형태로 담아버리는 **'Disk to File (D2F)'** 방식이다. 현대 수사에서는 보관과 법정 전송이 압도적으로 편리한 D2F 방식이 산업 표준(De facto)으로 쓰인다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 무결성을 지키는 1:1 비트 복제 마술, 디스크 이미징 개요**

* **정의:** 포렌식 수사 시 증거 원본의 훼손(무결성 파괴)을 방지하기 위해, 원본 저장 매체의 **물리적인 0과 1의 구조를 비트 스트림(Bit-Stream) 단위로 100% 동일하게 복사하여 쌍둥이 사본(이미지)을 생성하는 작업**.
* **단순 파일 복사와의 차이점 (매우 중요 🚨):** 일반적인 복사(Ctrl+C)는 눈에 보이는 정상 파일만 복사한다. 하지만 이미징은 **'디스크의 빈 공간(비할당 영역, 삭제된 파일 조각, 슬랙 공간)'까지 모조리 퍼담아 완벽한 물리적 거울(Mirror)을 만들어 냄**.

#### **II. \[본론 1] (단순화 버전) 쓰기 방지 장치를 거친 이미징 파이프라인 (도식화)**

원본을 잠그고 두 가지 갈래(D2D, D2F)로 복제본을 뽑아내는 과정을 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxODg2LjMzNSAyODIuMjczIiB3aWR0aD0iMTg4Ni4zMzUiIGhlaWdodD0iMjgyLjI3MyIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iX19fQml0U3RyZWFtX0NvcHlfIiBkYXRhLWxhYmVsPSLtj6zroIzsi50g65SU7Iqk7YGsIOydtOuvuOynlSAoQml0LVN0cmVhbSBDb3B5KSDsoIjssKgiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjE4MDYuMzM1IiBoZWlnaHQ9IjIwMi4yNzMwMDAwMDAwMDAwMiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjE4MDYuMzM1IiBoZWlnaHQ9IjI4IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ncm91cC1oZHIpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI1MiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+7Y+s66CM7IudIOuUlOyKpO2BrCDsnbTrr7jsp5UgKEJpdC1TdHJlYW0gQ29weSkg7KCI7LCoPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJPUkciIGRhdGEtdG89IkJMT0NLIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIxLiDsk7DquLAg67Cp7KeAIOyepey5mCDsl7DqsrAKKOybkOuzuCDtm7zshpAgMTAwJSDsm5Dsspwg7LCo64uoKSIgcG9pbnRzPSIyMjMuMTc5LDE1NS4xMzY1IDQ1OC4zMjEsMTU1LjEzNjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkJMT0NLIiBkYXRhLXRvPSJDT1BZIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIyLiDrrLzrpqzsoIEg67mE7Yq4KDDqs7wgMSkg64uo7JyECuuqqOyhsOumrCDrs7XsoJwg7Iuc7J6RISIgcG9pbnRzPSI1OTcuMzQyMDAwMDAwMDAwMSwxNTUuMTM2NSA4MjcuNzMyMDAwMDAwMDAwMSwxNTUuMTM2NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQ09QWSIgZGF0YS10bz0iRDJEIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLquLDqs4Qg64yAIOq4sOqzhCDrs7XsgqwiIHBvaW50cz0iOTQ2LjI5MjgzMzMzMzMzMzQsMTc4Ljg0ODY2NjY2NjY2NjY1IDk4Mi4wMDUwMDAwMDAwMDAxLDE3OC44NDg2NjY2NjY2NjY2NSA5ODIuMDA1MDAwMDAwMDAwMSwxOTEuNTg2NSAxMTc0LjI1OSwxOTEuNTg2NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQ09QWSIgZGF0YS10bz0iRDJGIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLqsbDrjIDtlZwg7YyM7J2866GcIOyVley2lSIgcG9pbnRzPSI5NDYuMjkyODMzMzMzMzMzNCwxMzEuNDI0MzMzMzMzMzMzMzIgOTgyLjAwNTAwMDAwMDAwMDEsMTMxLjQyNDMzMzMzMzMzMzMyIDk4Mi4wMDUwMDAwMDAwMDAxLDExOC42ODY1IDE0MDQuMjU4LDExOC42ODY1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJEMkQiIGRhdGEtdG89IkFOQUxZWkUiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIzLiDsiJjsgqzqtIDsnYAg7JuQ67O47J2AIOq4iOqzoOyXkCDrhKPqs6AK7Jik7KeBIOydtCAn67O17IKs67O4J+ycvOuhnOunjCDrtoTshJ0g7KeE7ZaJISIgcG9pbnRzPSIxMzU2LjI1OCwxOTEuNTg2NSAxNjQ0LjE5OSwxOTEuNTg2NSAxNjQ0LjE5OSwxNjEuMjg2NSAxNjgwLjE5OSwxNjEuMjg2NSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCA0IiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJEMkYiIGRhdGEtdG89IkFOQUxZWkUiIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjE2MzIuMTk5LDExOC42ODY1IDE2NDQuMTk5LDExOC42ODY1IDE2NDQuMTk5LDE0OC45ODY0OTk5OTk5OTk5OCAxNjgwLjE5OSwxNDguOTg2NDk5OTk5OTk5OTgiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJPUkciIGRhdGEtdG89IkJMT0NLIiBkYXRhLWxhYmVsPSIxLiDsk7DquLAg67Cp7KeAIOyepey5mCDsl7DqsrAKKOybkOuzuCDtm7zshpAgMTAwJSDsm5Dsspwg7LCo64uoKSI+CiAgPHJlY3QgeD0iMjY3LjE3OSIgeT0iMTMyLjEzNjQ5OTk5OTk5OTk4IiB3aWR0aD0iMTQ3LjE0MjAwMDAwMDAwMDAyIiBoZWlnaHQ9IjQ0LjYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzQwLjc1IiB5PSIxNTQuNDM2NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSI+PHRzcGFuIHg9IjM0MC43NSIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPjEuIOyTsOq4sCDrsKnsp4Ag7J6l7LmYIOyXsOqysDwvdHNwYW4+PHRzcGFuIHg9IjM0MC43NSIgZHk9IjE0LjMiPijsm5Drs7gg7Zu87IaQIDEwMCUg7JuQ7LKcIOywqOuLqCk8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJCTE9DSyIgZGF0YS10bz0iQ09QWSIgZGF0YS1sYWJlbD0iMi4g66y866as7KCBIOu5hO2KuCgw6rO8IDEpIOuLqOychArrqqjsobDrpqwg67O17KCcIOyLnOyekSEiPgogIDxyZWN0IHg9IjY0MS4zNDIwMDAwMDAwMDAxIiB5PSIxMzIuMTM2NDk5OTk5OTk5OTgiIHdpZHRoPSIxNDIuMzkwMDAwMDAwMDAwMDEiIGhlaWdodD0iNDQuNiIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI3MTIuNTM3MDAwMDAwMDAwMSIgeT0iMTU0LjQzNjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSI3MTIuNTM3MDAwMDAwMDAwMSIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPjIuIOusvOumrOyggSDruYTtirgoMOqzvCAxKSDri6jsnIQ8L3RzcGFuPjx0c3BhbiB4PSI3MTIuNTM3MDAwMDAwMDAwMSIgZHk9IjE0LjMiPuuqqOyhsOumrCDrs7XsoJwg7Iuc7J6RITwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkNPUFkiIGRhdGEtdG89IkQyRCIgZGF0YS1sYWJlbD0i6riw6rOEIOuMgCDquLDqs4Qg67O17IKsIj4KICA8cmVjdCB4PSIxMDE5LjA1NDAwMDAwMDAwMDEiIHk9IjE3NS41ODY1IiB3aWR0aD0iMTA2LjE1NjAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTA3Mi4xMzIiIHk9IjE5MC43MzY1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7quLDqs4Qg64yAIOq4sOqzhCDrs7Xsgqw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQ09QWSIgZGF0YS10bz0iRDJGIiBkYXRhLWxhYmVsPSLqsbDrjIDtlZwg7YyM7J2866GcIOyVley2lSI+CiAgPHJlY3QgeD0iMTAxNC4wMDUwMDAwMDAwMDAxIiB5PSIxMDIuNjg2NSIgd2lkdGg9IjExNi4yNTQwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjEwNzIuMTMyIiB5PSIxMTcuODM2NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+6rGw64yA7ZWcIO2MjOydvOuhnCDslZXstpU8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iRDJEIiBkYXRhLXRvPSJBTkFMWVpFIiBkYXRhLWxhYmVsPSIzLiDsiJjsgqzqtIDsnYAg7JuQ67O47J2AIOq4iOqzoOyXkCDrhKPqs6AK7Jik7KeBIOydtCAn67O17IKs67O4J+ycvOuhnOunjCDrtoTshJ0g7KeE7ZaJISI+CiAgPHJlY3QgeD0iMTQyNS4wNTU1IiB5PSIxNjguNTg2NSIgd2lkdGg9IjE4Ni4zNDYiIGhlaWdodD0iNDQuNiIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxNTE4LjIyODUiIHk9IjE5MC44ODY1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIj48dHNwYW4geD0iMTUxOC4yMjg1IiBkeT0iLTMuMzAwMDAwMDAwMDAwMDAwNyI+My4g7IiY7IKs6rSA7J2AIOybkOuzuOydgCDquIjqs6Dsl5Ag64Sj6rOgPC90c3Bhbj48dHNwYW4geD0iMTUxOC4yMjg1IiBkeT0iMTQuMyI+7Jik7KeBIOydtCAmIzM5O+uzteyCrOuzuCYjMzk77Jy866Gc66eMIOu2hOyEnSDsp4TtlokhPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik9SRyIgZGF0YS1sYWJlbD0i67KU7KOE7J6QIOybkOuzuCDtlZjrk5wg8J+SviIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1NiIgeT0iMTM2LjY4NjUiIHdpZHRoPSIxNjcuMTc5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxMzkuNTg5NSIgeT0iMTU1LjEzNjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuuylOyjhOyekCDsm5Drs7gg7ZWY65OcIPCfkr48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkJMT0NLIiBkYXRhLWxhYmVsPSJXcml0ZSBCbG9ja2VyIPCflJIiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDU4LjMyMSIgeT0iMTM2LjY4NjUiIHdpZHRoPSIxMzkuMDIxMDAwMDAwMDAwMDIiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNTI3LjgzMTUiIHk9IjE1NS4xMzY1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5Xcml0ZSBCbG9ja2VyIPCflJI8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkNPUFkiIGRhdGEtbGFiZWw9IuydtOuvuOynlSDquLDrspUKMuqwgOyngCDqsIjrnpgiIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iODk4Ljg2ODUsODQuMDAwMDAwMDAwMDAwMDEgOTcwLjAwNSwxNTUuMTM2NSA4OTguODY4NSwyMjYuMjczMDAwMDAwMDAwMDIgODI3LjczMjAwMDAwMDAwMDEsMTU1LjEzNjUiIGZpbGw9IiNmZmYzZTAiIHN0cm9rZT0iI2Y1N2MwMCIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9Ijg5OC44Njg1IiB5PSIxNTUuMTM2NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iODk4Ljg2ODUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7snbTrr7jsp5Ug6riw67KVPC90c3Bhbj48dHNwYW4geD0iODk4Ljg2ODUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPjLqsIDsp4Ag6rCI656YPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkQyRCIgZGF0YS1sYWJlbD0iRDJEIChEaXNrIHRvIERpc2spCuyDiCDtlZjrk5zrlJTsiqTtgawg6riw6rOEIPCfkr0iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTE3NC4yNTkiIHk9IjE2NC42ODY0OTk5OTk5OTk5NyIgd2lkdGg9IjE4MS45OTkiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjEyNjUuMjU4NSIgeT0iMTkxLjU4NjQ5OTk5OTk5OTk3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxMjY1LjI1ODUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5EMkQgKERpc2sgdG8gRGlzayk8L3RzcGFuPjx0c3BhbiB4PSIxMjY1LjI1ODUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuyDiCDtlZjrk5zrlJTsiqTtgawg6riw6rOEIPCfkr08L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRDJGIiBkYXRhLWxhYmVsPSJEMkYgKERpc2sgdG8gRmlsZSkg8J+TgQrsnbTrr7jsp4Ag7YyM7J28IO2VmOuCmCDsg53shLEgKEUwMSDrk7EpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjE0MDQuMjU4IiB5PSI5MS43ODY0OTk5OTk5OTk5OSIgd2lkdGg9IjIyNy45NDA5OTk5OTk5OTk5NyIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxNTE4LjIyODUiIHk9IjExOC42ODY1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxNTE4LjIyODUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5EMkYgKERpc2sgdG8gRmlsZSkg8J+TgTwvdHNwYW4+PHRzcGFuIHg9IjE1MTguMjI4NSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7J2066+47KeAIO2MjOydvCDtlZjrgpgg7IOd7ISxIChFMDEg65OxKTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJBTkFMWVpFIiBkYXRhLWxhYmVsPSLtj6zroIzsi50g67aE7ISd7IukIPCflI4iIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTY4MC4xOTkiIHk9IjEzNi42ODY1IiB3aWR0aD0iMTUwLjEzNiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTc1NS4yNjciIHk9IjE1NS4xMzY1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7tj6zroIzsi50g67aE7ISd7IukIPCflI48L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

#### **III. \[본론 2] 디스크 이미징의 양대 산맥: D2D vs D2F 전격 비교 해부 (3단 표)**

물리적 기계로 복제하느냐, 논리적인 덩어리 파일로 압축하느냐에 따른 \*\*'보관성'과 '분석 도구 의존성'\*\*을 대조하는 것이 핵심입니다.

| **핵심 척도 (비교 잣대)**               | **💽 Disk to Disk (D2D) 기법**                                                                     | **📁 Disk to File (D2F) 기법 🚨**                                                                       |
| :------------------------------ | :----------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| **복제 결과물의 형태 및 물리적 특성**         | **'원본과 똑같은 물리적 하드 기계'.** 원본이 1TB 하드라면, 똑같은 빈 1TB 하드디스크(사본 매체)를 기계적으로 연결해서 0번 섹터부터 끝까지 1:1로 구워버림. | **'논리적인 하나의 거대한 압축 파일'.** 원본 하드의 모든 비트 정보를 똘똘 뭉쳐서 **'하나의 덩어리 파일(확장자: .dd, .E01 등)'** 형태로 만들어 냄.       |
| **수사관의 직관성 및 분석 소프트웨어 의존도**     | **\[전문 도구 불필요, 높은 직관성]** 그냥 복제된 사본 하드디스크를 다른 컴퓨터에 꽂으면 윈도우 부팅도 되고 C드라이브처럼 즉시 눈으로 볼 수 있음.          | **\[전용 포렌식 도구 반드시 필요]** 이것은 단일 '파일'이므로, 그 안을 들여다보려면 EnCase 같은 전문 포렌식 소프트웨어를 써서 가상으로 마운트(Mount) 시켜야 함. |
| **보관, 전송, 공유의 편의성 (현대 포렌식 관점)** | **매우 불편함.** 분석관이 3명이면 물리적인 하드 기계 3개가 필요함. 법정이나 타 기관으로 넘길 때 무거운 하드를 택배로 보내야 함.                    | **\[압도적으로 편리함 / 현대 수사 표준 💯]** 단순한 파일이므로 USB에 복사해서 주거나 사내 클라우드망을 통해 다른 수사관에게 1초 만에 배포(공유)할 수 있음.      |
| **무결성 검증 (해시값)**                | 디스크 전체를 다 읽어서 해시(Hash) 값을 계산해야 하므로 무결성 검증이 다소 번거로움.                                              | 이미지 파일 포맷(E01 등) **내부에 해시(Hash) 값과 메타데이터가 자체 내장**되어 있어 위변조 증명이 매우 빠르고 완벽함.                            |

#### **IV. \[결론/제언] SSD의 트림(TRIM) 기능과 전통적 디스크 이미징의 한계**

* **(키워드 위주 2줄 마무리)** "현대 포렌식에서는 HDD 시절의 1:1 디스크 이미징 공식이 깨지고 있습니다. 저장 매체가 SSD로 넘어가면서, 지워진 데이터를 칩셋이 스스로 영구 삭제해 버리는 **'TRIM' 기능과 자동 가비지 컬렉션(GC)으로 인해, 이미징을 뜨는 도중에도 원본의 해시값이 훼손될 수 있는 치명적 딜레마**에 대한 포렌식 업계의 기술적, 법적 대응 가이드가 절실합니다."
