### **라이브 시스템 증거 수집의 철칙: 휘발성 순서 (Order of Volatility)**

**Ⅰ. 개요**

* 정의: RFC 3227(디지털 증거 수집·보관 가이드라인)에 근거해, 침해사고 대응 시 전원 차단·시간 경과에 따라 소실 속도가 빠른 휘발성 데이터부터 우선 수집하는 라이브 포렌식(Live Forensics)의 증거 수집 원칙
* 필요성: 정적 포렌식(Dead Forensics)처럼 전원부터 차단하고 디스크만 이미징하면 RAM에 상주하던 악성코드 프로세스, 활성 네트워크 연결, 암·복호화 키 등 휘발성 증거가 영구 소실되어 침해 원인 규명이 불가능해짐 — 5대 포렌식 원칙 중 **신속성·무결성**을 지키기 위한 절차적 철칙

**Ⅱ. 전체 수집 절차 흐름**\
`레지스터·캐시 → 네트워크·프로세스 상태정보 → 메인 메모리(RAM) → 임시 파일시스템 → 디스크 → 원격 로그·백업매체` (유실 속도가 빠른 순 → 느린 순)

**Ⅲ. 단계별 상세 수집 절차**

| 단계                | 목적                           | 주요 활동                              | 산출물 / 체크포인트                      |
| :---------------- | :--------------------------- | :--------------------------------- | :------------------------------- |
| 1. 레지스터·캐시        | 나노초 단위로 가장 먼저 소실되는 CPU 상태 확보 | CPU 레지스터·캐시 값 캡처                   | 실행 중 명령어 컨텍스트                    |
| 2. 네트워크·프로세스 상태   | 공격자 접속 경로·활성 프로세스 추적         | 라우팅테이블, ARP 캐시, 프로세스 테이블, 커널 통계 수집 | netstat/pslist 로그                |
| 3. 메인 메모리(RAM) 덤프 | 악성코드·복호화 키 등 핵심 휘발성 증거 확보    | 물리 메모리 풀 덤프(.raw/.dmp)             | `Volatility` 등 메모리 포렌식 도구 분석용 원본 |
| 4. 임시 파일시스템       | 재부팅 시 소멸되는 캐시성 데이터 확보        | /tmp, 스왑 영역 등 수집                   | 임시파일 목록·해시값                      |
| 5. 디스크 이미징        | 비휘발성 저장매체의 무결성 사본 확보         | Write-Blocker 적용 후 비트스트림 이미징       | 원본-사본 해시(MD5/SHA-256) 일치 증명      |
| 6. 원격 로그·백업매체     | 물리적 구성·장기 보관 이력 확보           | 원격 로깅서버, 네트워크 토폴로지, 아카이브 매체 수집     | 로그 원장, 백업 목록                     |

**Ⅳ. 수행 시 고려사항 및 성공요인**

* 무결성: 모든 단계에서 쓰기방지장치(Write Blocker)를 적용하고 원본-사본 해시값을 대조해 증거 오염 여부를 증명
* 정당성·연계보관성: 수집 명령어 자체가 메모리 상태를 일부 변경시키는 한계(Heisenberg 효과)를 인지하고, 수집 시각·담당자·명령어 로그를 연계보관성(Chain of Custody) 일지에 남겨 법정 증거능력(Admissibility)을 확보
* 잔존 위험: 라이브 수집 도구 구동 자체의 시스템 간섭은 완전히 제거할 수 없으므로, 도구 버전·절차를 표준화(Tool Validation)해 재현성을 확보
* 운영 고도화 방향: 침해대응(DFIR) 매뉴얼에 "RAM 덤프 선행"을 의무화하고, EDR과 연동한 자동 메모리 수집·해시 검증 파이프라인을 구축해 대응 속도와 신뢰성을 동시에 확보

🔑 \[레-네-메-임-디-원] 레지스터부터 네트워크상태, 메인메모리, 임시파일, 디스크, 원격로그 순으로 사라지기 쉬운 것부터 살려낸다!

# **I. 디지털 포렌식 증거 수집의 골든 타임, Order of Volatility의 개요**

사이버 침해사고 발생 시 대상 시스템의 전원을 무작정 끄거나 재부팅하면, 메모리에 상주하던 악성코드 조각, 무선 네트워크 연결 상태, 실행 중인 암호화 키 등 치명적인 증거가 영구히 소멸됩니다. \*\*Order of Volatility(휘발성 순서)\*\*는 국제 표준 가이드라인인 **RFC 3227**에 근거하여, **유실 위험이 가장 높은 최상위 휘발성 데이터(CPU 레지스터, RAM 등)부터 휘발성이 낮은 영구 저장 매체(SSD/HDD, 백업 테이프) 순으로 증거 수집의 우선순위를 강제하는 핵심 원칙**입니다.

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MzEuNzIzIDM3MS42IiB3aWR0aD0iNTMxLjcyMyIgaGVpZ2h0PSIzNzEuNiIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJIaWdoIiBkYXRhLXRvPSJSQU0iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjY1Ljg2MTUsNzYuOSAyNjUuODYxNSwxMjQuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUkFNIiBkYXRhLXRvPSJEaXNrIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjI2NS44NjE1LDE2MS44IDI2NS44NjE1LDIwOS44IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJEaXNrIiBkYXRhLXRvPSJMb2ciIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjY1Ljg2MTUsMjQ2LjcwMDAwMDAwMDAwMDAyIDI2NS44NjE1LDI5NC43MDAwMDAwMDAwMDAwNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iSGlnaCIgZGF0YS1sYWJlbD0iMS4g7LSI6rOg7ZyY67Cc7ISxIDogQ1BVIOugiOyngOyKpO2EsCAmYW1wOyBMMX5MMyDsupDsi5wg66mU66qo66asIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjkyLjk4MTQ5OTk5OTk5OTk1IiB5PSI0MCIgd2lkdGg9IjM0NS43NiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjY1Ljg2MTUiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij4xLiDstIjqs6DtnJjrsJzshLEgOiBDUFUg66CI7KeA7Iqk7YSwICZhbXA7IEwxfkwzIOy6kOyLnCDrqZTrqqjrpqw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJBTSIgZGF0YS1sYWJlbD0iMi4g6rOg7ZyY67Cc7ISxIDog66mU7J24IOuplOuqqOumrCBSQU0sIEFSUC/rnbzsmrDtjIUg7YWM7J2067iULCDtmZzshLEg7ZSE66Gc7IS47IqkIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwIiB5PSIxMjQuOSIgd2lkdGg9IjQ1MS43MjI5OTk5OTk5OTk5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjI2NS44NjE1IiB5PSIxNDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjIuIOqzoO2cmOuwnOyEsSA6IOuplOyduCDrqZTrqqjrpqwgUkFNLCBBUlAv65287Jqw7YyFIO2FjOydtOu4lCwg7Zmc7ISxIO2UhOuhnOyEuOyKpDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRGlzayIgZGF0YS1sYWJlbD0iMy4g7KCA7ZyY67Cc7ISxIDog67O07KGw6riw7Ja17J6l7LmYIFNTRC9IREQsIOyKpOyZkSDtjIzsnbwsIOyehOyLnCDtjIzsnbwiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNjQuNDUzIiB5PSIyMDkuOCIgd2lkdGg9IjQwMi44MTY5OTk5OTk5OTk5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjY1Ljg2MTUiIHk9IjIyOC4yNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+My4g7KCA7ZyY67Cc7ISxIDog67O07KGw6riw7Ja17J6l7LmYIFNTRC9IREQsIOyKpOyZkSDtjIzsnbwsIOyehOyLnCDtjIzsnbw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkxvZyIgZGF0YS1sYWJlbD0iNC4g67mE7ZyY67Cc7ISxIDog7JuQ6rKpIFN5c2xvZy9TSUVNIOuhnOq3uCwg67Cx7JeFIO2FjOydtO2UhCwg66y866as7KCBIOunpOyytCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI1My4zMzc5OTk5OTk5OTk5OTQiIHk9IjI5NC43MDAwMDAwMDAwMDAwNSIgd2lkdGg9IjQyNS4wNDY5OTk5OTk5OTk5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjY1Ljg2MTUiIHk9IjMxMy4xNTAwMDAwMDAwMDAwMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+NC4g67mE7ZyY67Cc7ISxIDog7JuQ6rKpIFN5c2xvZy9TSUVNIOuhnOq3uCwg67Cx7JeFIO2FjOydtO2UhCwg66y866as7KCBIOunpOyytDwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

***

### **II. RFC 3227 기준 휘발성 데이터 수집 우선순위 (7단계)**

| **수집 순위 🔑**    | **🏁 수집 대상 디지털 데이터 🚨**        | **데이터 유실 속도 및 무결성 특성 💯**                         |
| :-------------- | :----------------------------- | :------------------------------------------------ |
| **1순위 (최고 휘발)** | **CPU 레지스터, L1/L2/L3 캐시 메모리**  | 수 나노초(ns)\~수 마이크로초 내 변형/유실되는 최고 위험 데이터            |
| **2순위**         | **주기억장치(RAM), 커널 상태, ARP 캐시**  | 전원 차단 시 전량 유실. 실행 중인 악성코드 및 암호화 키 존재              |
| **3순위**         | **임시 파일시스템, 스왑 공간, 가상 메모리**    | `pagefile.sys`, `/tmp` 등 시스템 상태 전이 시 수분 내 덮어쓰기 발생 |
| **4순위**         | **보조기억장치 (SSD, HDD, NVMe)**    | 전원이 꺼져도 보존되는 비휘발성 저장 매체 (파일 시스템 분석)               |
| **5순위**         | **원격 시스템 로그, SIEM, 네트워크 토폴로지** | 로깅 서버나 네트워크 방화벽 장비에 상주하는 중앙 집계 데이터                |
| **6순위**         | **물리적 네트워크 배선, 컴퓨터 외형 상태**     | 시각적 장비 배치도 및 물리 라벨링 상태                            |
| **7순위 (최저 휘발)** | **백업 아카이브 매체 (백업 테이프, DVD)**   | 장기간 물리 보관소에 암거 보관되는 고정 영구 매체                      |

***

### **III. 휘발성 데이터(Volatile)와 비휘발성 데이터(Non-Volatile)의 상세 비교**

| **비교 항목**            | **⚡ 휘발성 데이터 (Volatile Data)**  | **💾 비휘발성 데이터 (Non-Volatile Data)**     |
| :------------------- | :----------------------------- | :-------------------------------------- |
| **보존 수명 (Lifespan)** | 전원 차단 시 즉시 소멸 (수 나노초 \~ 수 초)   | 전원 차단 후에도 물리 매체에 영구 보존 (수 년)            |
| **증거 수집 우선순위**       | **최우선 수집 대상 (1\~2순위 수집)**      | 후순위 수집 대상 (4\~7순위 수집)                   |
| **대표적인 데이터**         | CPU 레지스터, RAM, 활성 프로세스, ARP 표  | SSD/HDD, 페이징 파일, 백업 테이프, 원격 로그          |
| **수집 기법 (Capture)**  | 라이브 시스템 상에서 **메모리 덤프(FTK) 수집** | **쓰기 방지 장치(Write Blocker) 연결 후 이미지 복제** |
| **증거 오염 가능성**        | 덤프 도구 자체 실행으로 메모리 일부 변경 유발     | 사후 이미지 덤프 및 해시값 검증으로 무결성 완전 유지          |

***

### **IV. 휘발성 증거 수집 시 엔지니어링 포렌식 가이드라인**

**IMPORTANT**

1. **라이브 덤프 시 흔적 최소화 (Volatiles First)**: RAM 메모리 덤프 시 시스템에 포렌식 도구를 설치하면 메모리 영역이 오염(Artifact)됩니다. 따라서 사전 검증된 포터블 덤프 도구(FTK Imager Lite, WinPmem)를 USB 형태로 연결하여 최소한의 명령으로 덤프해야 합니다.
2. **무결성 입증을 위한 해시값(SHA-256) 수집 즉시 생성**: 메모리 및 디스크 증거 수집을 완료한 직후, 덤프 파일의 SHA-256 해시값을 즉시 추출하여 획득 일시와 함께 증거 연쇄 보관(Chain of Custody) 문서에 기록해야 법적 증거능력이 인정됩니다.
