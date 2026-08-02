### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (VPN목적, 계층차이가핵심) — 3~4줄
Ⅱ. IPSec VPN (본론①, 도식 1개 필수)
Ⅲ. SSL VPN, 핵심 배점
Ⅳ. 결론
```

### Ⅰ. 개요

두VPN모두 \*\*"공용망(인터넷)위에 암호화된가상터널을만든다"\*\*는 목표는같지만, \*\*"어느OSI계층에서 터널을파는지"\*\*가 근본적으로다릅니다 — IPSec은 **3계층(네트워크)**, SSL은 \*\*4\~7계층(전송\~응용)\*\*에서 작동합니다.

### Ⅱ. IPSec VPN — 네트워크계층전체를암호화

| 항목       | 내용                                                     |
| :------- | :----------------------------------------------------- |
| **적용계층** | **3계층**— IP패킷자체를 암호화                                   |
| **키교환**  | **IKE**(InternetKeyExchange)— 앞서다룬 **디피헬만원리**로 안전하게키합의 |
| **적용범위** | **모든IP트래픽**(애플리케이션구분없이) 통째로터널링                         |
| **대표활용** | **본사-지사간전체망연결**(Site-to-SiteVPN)                       |

→ 암기: **"IP패킷자체를 봉투(IPSec헤더)로감싸서, 모든트래픽을 통째로 암호화터널로보낸다"** — 앞서다룬 \*\*전자봉투(대칭키로내용암호화+비대칭키로세션키교환)\*\*의구조가, IKE의 **디피헬만기반키교환+대칭키(AES)로실제데이터암호화**에 그대로재현됩니다.

### 도식화 제안

```
[본사] ══IPSec터널(전체IP트래픽)══→ [지사]
       (3계층에서, 모든애플리케이션구분없이 통째로암호화)
       
클라이언트PC에 별도소프트웨어(VPN클라이언트) 설치 필요
```

### Ⅲ. SSL VPN — 응용단위로선택적접근, 핵심 배점

**함정 방지: "브라우저로쓸수있다"고만답하면절반. IPSec과의근본적차이(전체vs선택적)를보여줘야완성됩니다.**

| 항목          | 내용                                              |
| :---------- | :---------------------------------------------- |
| **적용계층**    | **4\~7계층**— 앞서다룬 **TLS(대칭/비대칭암호,전자봉투원리)** 기반    |
| **접근방식**    | **웹브라우저만으로**접속가능(별도클라이언트불필요,ClientlessSSLVPN)   |
| **세밀한접근제어** | 앞서다룬 **RBAC/ABAC**처럼, **애플리케이션단위로** 접근허용/차단설정가능 |
| **대표활용**    | **원격근무자의개별서비스접근**(재택근무,협력사임시접근)                 |

→ 암기: **"브라우저만있으면 되고, 전체망이아니라 필요한서비스하나만 접근하게한다"** — 앞서다룬 \*\*"제로트러스트(NeverTrust,최소권한)"\*\*철학이, SSL VPN에서는 \*\*"전체네트워크가아니라 승인된특정애플리케이션에만접근"\*\*하는 형태로 구현됩니다.

### 도식화 제안

```
[원격근무자] ══SSL VPN(브라우저)══→ [특정웹서비스만접근]
            (전체사내망이아니라, 승인된애플리케이션단위로제한)

[IPSec VPN]                    [SSL VPN]
3계층,전체IP트래픽터널링          4~7계층,애플리케이션단위선택접근
클라이언트설치필요               브라우저만으로가능(Clientless)
Site-to-Site에적합              원격사용자개별접근에적합
```

### Ⅳ. 결론

IPSec과SSL VPN의핵심차이는 \*\*"터널을어느계층에서파는가(3계층전체vs4\~7계층선택적)"\*\*입니다 — IPSec은 **"본사-지사전체를하나의망처럼"** 연결하는데 강하고, SSL VPN은 \*\*"개별사용자가 필요한서비스에만 브라우저로간편하게접근"\*\*하는데 강합니다 — 이는 앞서다룬 **제로트러스트의최소권한원칙**이 \*\*"VPN을선택하는기준"\*\*으로 이어진다는 것을 보여주며, 실무에서는 \*\*"지사간전체연결은IPSec, 재택근무자의개별접근은SSL VPN"\*\*으로 **함께조합**하는 것이 일반적입니다.

### **1. 답안 전개 스토리**

> "공용 인터넷을 개인 전용선처럼 암호화해 쓰는 VPN에는 두 가지 파벌이 있다. 첫째, \*\*'IPSec VPN'\*\*은 본사와 지사(회사 대 회사)를 무겁고 튼튼하게 잇는다. 보안성이 막강하지만, PC마다 전용 프로그램을 무조건 깔아야 해서 유지보수가 지옥이다. 둘째, \*\*'SSL VPN'\*\*은 재택근무자를 위한 가벼운 VPN이다. 전용 프로그램 없이 평소 쓰던 '웹 브라우저' 하나만 있으면 카페든 집이든 즉시 회사 망에 접속할 수 있어, 현대 원격근무의 표준이 되었다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 인터넷을 전용선처럼, VPN의 양대 산맥 개요**

* **VPN 정의:** 공중망(인터넷) 상에서 터널링(Tunneling) 및 암호화 기법을 사용하여, 마치 사설 전용망(Leased Line)을 구축한 것과 같은 보안 효과를 제공하는 가상 통신망.
* **분류 목적:** 망과 망을 통째로 묶는 강력한 \*\*IPSec 방식(L3)\*\*과, 이동 근무자가 가볍게 웹으로 접속하는 \*\*SSL 방식(L4\~L7)\*\*으로 용도에 맞게 분리 운영함.

#### **II. \[본론 1] (극단적 단순화 버전) 라우터를 묶는 IPSec과 웹으로 들어가는 SSL**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3MDYuMzAzIDM1My44IiB3aWR0aD0iNzA2LjMwMyIgaGVpZ2h0PSIzNTMuOCIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iVlBOX19fXyIgZGF0YS1sYWJlbD0iVlBOIO2EsOuEkOungSDqtazshLEg67Cp7IudIOuMgOyhsCI+CiAgPHJlY3QgeD0iNDAiIHk9IjQwIiB3aWR0aD0iNjI2LjMwMyIgaGVpZ2h0PSIyNzMuOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjYyNi4zMDMiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjUyIiB5PSI1NCIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij5WUE4g7YSw64SQ66eBIOq1rOyEsSDrsKnsi50g64yA7KGwPC90ZXh0Pgo8ZyBjbGFzcz0ic3ViZ3JhcGgiIGRhdGEtaWQ9IjFfSVBTZWNfVlBOX1NpdGVfdG9fU2l0ZV8iIGRhdGEtbGFiZWw9IjEuIElQU2VjIFZQTiAoU2l0ZSB0byBTaXRlIPCfj6IpIj4KICA8cmVjdCB4PSI1NiIgeT0iODQiIHdpZHRoPSI1NzUuNzMiIGhlaWdodD0iOTYuOSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjU3NS43MyIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNjgiIHk9Ijk4IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPjEuIElQU2VjIFZQTiAoU2l0ZSB0byBTaXRlIPCfj6IpPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iMl9TU0xfVlBOX0NsaWVudF90b19TaXRlXyIgZGF0YS1sYWJlbD0iMi4gU1NMIFZQTiAoQ2xpZW50IHRvIFNpdGUg8J+SuykiPgogIDxyZWN0IHg9IjU2IiB5PSIyMDAuOSIgd2lkdGg9IjU5NC4zMDMiIGhlaWdodD0iOTYuOSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjU2IiB5PSIyMDAuOSIgd2lkdGg9IjU5NC4zMDMiIGhlaWdodD0iMjgiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWhkcikiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjY4IiB5PSIyMTQuOSIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9IjYwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjQuMTk5OTk5OTk5OTk5OTk5Ij4yLiBTU0wgVlBOIChDbGllbnQgdG8gU2l0ZSDwn5K7KTwvdGV4dD4KPC9nPgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJSMSIgZGF0YS10bz0iUjIiIGRhdGEtc3R5bGU9InRoaWNrIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9ImZhbHNlIiBkYXRhLWxhYmVsPSLinKggTDMgSVAg7Yyo7YK3IOyVlO2YuO2ZlCDinKgK66y06rKB6rOgIO2KvO2KvO2VnCDsnqXruYQg6rCEIO2EsOuEkCIgcG9pbnRzPSIyMjIuMTM2LDE0Ni40NSA0NjUuNTk0MDAwMDAwMDAwMDUsMTQ2LjQ1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIyIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUCIgZGF0YS10bz0iUyIgZGF0YS1zdHlsZT0iZG90dGVkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9ImZhbHNlIiBkYXRhLWxhYmVsPSLinKgg7Ju5IOu4jOudvOyasOyggCAoSFRUUFMpIOKcqArtlITroZzqt7jrnqgg7ISk7LmYIOyXhuydtCDqsIDrs43qsowg7KCR7IaNIiBwb2ludHM9IjIzNC43MzMsMjYzLjM1IDUwMS45NTEsMjYzLjM1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlIxIiBkYXRhLXRvPSJSMiIgZGF0YS1sYWJlbD0i4pyoIEwzIElQIO2MqO2CtyDslZTtmLjtmZQg4pyoCuustOqygeqzoCDtirztirztlZwg7J6l67mEIOqwhCDthLDrhJAiPgogIDxyZWN0IHg9IjI2Ni4xMzU5OTk5OTk5OTk5NyIgeT0iMTIzLjQ1IiB3aWR0aD0iMTU1LjQ1ODAwMDAwMDAwMDAzIiBoZWlnaHQ9IjQ0LjYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzQzLjg2NSIgeT0iMTQ1Ljc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIj48dHNwYW4geD0iMzQzLjg2NSIgZHk9Ii0zLjMwMDAwMDAwMDAwMDAwMDciPuKcqCBMMyBJUCDtjKjtgrcg7JWU7Zi47ZmUIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjM0My44NjUiIGR5PSIxNC4zIj7rrLTqsoHqs6Ag7Yq87Yq87ZWcIOyepeu5hCDqsIQg7YSw64SQPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iUCIgZGF0YS10bz0iUyIgZGF0YS1sYWJlbD0i4pyoIOybuSDruIzrnbzsmrDsoIAgKEhUVFBTKSDinKgK7ZSE66Gc6re4656oIOyEpOy5mCDsl4bsnbQg6rCA67ON6rKMIOygkeyGjSI+CiAgPHJlY3QgeD0iMjc4LjczMyIgeT0iMjQwLjM0OTk5OTk5OTk5OTk3IiB3aWR0aD0iMTc5LjIxODAwMDAwMDAwMDA1IiBoZWlnaHQ9IjQ0LjYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzY4LjM0MjAwMDAwMDAwMDA0IiB5PSIyNjIuNjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSIzNjguMzQyMDAwMDAwMDAwMDQiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij7inKgg7Ju5IOu4jOudvOyasOyggCAoSFRUUFMpIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjM2OC4zNDIwMDAwMDAwMDAwNCIgZHk9IjE0LjMiPu2UhOuhnOq3uOueqCDshKTsuZgg7JeG7J20IOqwgOuzjeqyjCDsoJHsho08L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUjEiIGRhdGEtbGFiZWw9IuyEnOyauCDrs7jsgqwg65287Jqw7YSwIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjcyIiB5PSIxMjgiIHdpZHRoPSIxNTAuMTM2IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjE0Ny4wNjc5OTk5OTk5OTk5OCIgeT0iMTQ2LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7shJzsmrgg67O47IKsIOudvOyasO2EsDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUjIiIGRhdGEtbGFiZWw9Iuu2gOyCsCDsp4Dsgqwg65287Jqw7YSwIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQ2NS41OTQwMDAwMDAwMDAwNSIgeT0iMTI4IiB3aWR0aD0iMTUwLjEzNiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI1NDAuNjYyIiB5PSIxNDYuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuu2gOyCsCDsp4Dsgqwg65287Jqw7YSwPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQIiBkYXRhLWxhYmVsPSLsnqztg53qt7zrrLTsnpAg64W47Yq467aBIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjcyIiB5PSIyNDQuOSIgd2lkdGg9IjE2Mi43MzMiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTUzLjM2NjUiIHk9IjI2My4zNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7J6s7YOd6re866y07J6QIOuFuO2KuOu2gTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUyIgZGF0YS1sYWJlbD0i7ZqM7IKsIFZQTiDshJzrsoQiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTAxLjk1MSIgeT0iMjQ0LjkiIHdpZHRoPSIxMzIuMzUyIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI1NjguMTI3MDAwMDAwMDAwMSIgeT0iMjYzLjM1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7tmozsgqwgVlBOIOyEnOuyhDwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

#### **III. \[본론 2] IPSec vs SSL VPN 핵심 스펙 전격 비교 (3단 표)**

| **핵심 척도**     | **🛡️ IPSec VPN (본사-지사 연결형)**                                                          | **🌐 SSL VPN (원격 근무형) 🚨**                                                            |
| :------------ | :------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------ |
| **동작 계층**     | **네트워크 계층 (L3).** IP 패킷 전체(헤더+데이터)를 통째로 암호화.                                           | **전송/응용 계층 (L4\~L7).** 애플리케이션의 데이터(Payload) 단만 암호화.                                   |
| **연결 주체**     | **Site-to-Site (망 대 망).** 서울 라우터 ↔ 부산 라우터 간의 터널.                                       | **Client-to-Site (단말 대 망).** 직원 노트북 ↔ 회사 서버 간의 터널.                                    |
| **S/W 설치 🚨** | **\[Client 설치 필수 (Client-based)]** 개인 PC마다 무거운 전용 VPN 프로그램을 깔고 복잡한 세팅을 해야 함 (유지보수 극악). | **\[Client 설치 불필요 (Clientless) 💯]** PC에 깔린 기본 **웹 브라우저(크롬, 엣지)**만 있으면 어디서든 즉시 접속 가능. |
| **접근 제어**     | 일단 뚫리면 회사 망 전체에 다 접속 가능.                                                               | 애플리케이션 단위로 세밀하게 권한 통제 가능.                                                             |
| **핵심 프로토콜**   | IKE (키 교환), ESP (암호화), AH (인증)                                                         | SSL / TLS (HTTPS 기반)                                                                  |

#### **IV. \[결론/제언] 원격근무 보안의 한계와 제로 트러스트(ZTNA)로의 진화**

* **(키워드 위주 2줄 마무리)** "SSL VPN은 원격근무의 훌륭한 도구지만, 일단 한 번 인증을 뚫고 들어오면 내부 망을 마음껏 헤집고 다니는 '수평적 이동(Lateral Movement)' 위협에 취약합니다. 이를 막기 위해 접속 후에도 사용자의 행동과 기기 상태를 1초마다 계속 의심하고 검증하는 **'제로 트러스트 네트워크 접속(ZTNA)' 모델로 VPN 아키텍처가 전면 교체되고 있습니다.**"
