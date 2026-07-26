#### **국내 데이터 인증 제도의 양대 축: DQC-V & DQC-M**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 "데이터 값"과 "관리 프로세스"를 별도로 인증하는가)
Ⅱ. DQC-V·DQC-M 핵심 구조
Ⅲ. 비교 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"ISO/IEC 25012가 데이터 품질의 국제 이론적 특성 체계를 제시한다면, DQC(Data Quality Certification)는 그 이론을 한국데이터산업진흥원(K-DATA)이 국내 실무에 맞게 구체화해 실제로 인증서를 발급하는 제도로, 데이터 그 자체의 값이 정확한가(DQC-V)와 그 값을 지속적으로 정확하게 관리하는 조직의 프로세스가 성숙한가(DQC-M)라는 서로 다른 두 질문에 각각 답하는 두 개의 독립된 인증 트랙"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5ODIuNTQ2OTk5OTk5OTk5NyAyMDEuOCIgd2lkdGg9Ijk4Mi41NDY5OTk5OTk5OTk3IiBoZWlnaHQ9IjIwMS44IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlJPT1QiIGRhdGEtdG89IkRRQ19WIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjUwMS4wOTE3NDk5OTk5OTk4LDc2LjkgNTAxLjA5MTc0OTk5OTk5OTgsMTAwLjkgMjY4LjQ1NDk5OTk5OTk5OTksMTAwLjkgMjY4LjQ1NDk5OTk5OTk5OTksMTI0LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlJPT1QiIGRhdGEtdG89IkRRQ19NIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjUwMS4wOTE3NDk5OTk5OTk4LDc2LjkgNTAxLjA5MTc0OTk5OTk5OTgsMTAwLjkgNzMzLjcyODQ5OTk5OTk5OTgsMTAwLjkgNzMzLjcyODQ5OTk5OTk5OTgsMTI0LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJPT1QiIGRhdGEtbGFiZWw9IuuNsOydtO2EsCDtkojsp4gg7J247KadIOyytOqzhCBEUUMiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzk1LjY0Mjc0OTk5OTk5OTgiIHk9IjQwIiB3aWR0aD0iMjEwLjg5OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjUwMS4wOTE3NDk5OTk5OTk4IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+642w7J207YSwIO2SiOyniCDsnbjspp0g7LK06rOEIERRQzwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRFFDX1YiIGRhdGEtbGFiZWw9IkRRQy1WIDog642w7J207YSwIOqwkiDsnbjspp0g4p6UIOyLpOygnCBEQiDqsJLsnZgg7Jik66WY7JyoIOuwjyDsoJXrsIDrj4Qg65Ox6riJIO2MkOyglSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MCIgeT0iMTI0LjkiIHdpZHRoPSI0NTYuOTA5OTk5OTk5OTk5OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjY4LjQ1NDk5OTk5OTk5OTkiIHk9IjE0My4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+RFFDLVYgOiDrjbDsnbTthLAg6rCSIOyduOymnSDinpQg7Iuk7KCcIERCIOqwkuydmCDsmKTrpZjsnKgg67CPIOygleuwgOuPhCDrk7HquIkg7YyQ7KCVPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJEUUNfTSIgZGF0YS1sYWJlbD0iRFFDLU0gOiDrjbDsnbTthLAg6rSA66as7LK06rOEIOyduOymnSDinpQg7ZSE66Gc7IS47IqkIOyEseyImeuPhCDroIjrsqgg7YyQ7KCVIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjUyNC45MDk5OTk5OTk5OTk5IiB5PSIxMjQuOSIgd2lkdGg9IjQxNy42MzY5OTk5OTk5OTk5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjczMy43Mjg0OTk5OTk5OTk4IiB5PSIxNDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkRRQy1NIDog642w7J207YSwIOq0gOumrOyytOqzhCDsnbjspp0g4p6UIO2UhOuhnOyEuOyKpCDshLHsiJnrj4Qg66CI67KoIO2MkOyglTwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

***

#### Ⅱ. DQC-V·DQC-M 핵심 구조

**가. DQC-V(Data Quality Certification - Value)**

```
[DQC-V: 데이터 값(Value) 자체의 정확성 인증]

심사 대상: DB에 실제로 저장된 데이터 값
심사 방법: 도메인·업무규칙 기반 데이터 프로파일링으로
           오류·불일치 값을 정량적으로 탐지

정합률(정확성 비율) 산출:
  정합률 = (전체 데이터 - 오류 데이터) / 전체 데이터 × 100

등급 부여(3단계):
  실버(Silver)    : 정합률 95.510% 이상
  골드(Gold)      : 정합률 97.700% 이상
  플래티넘(Platinum): 정합률 99.977% 이상 (최고 등급)
```

**나. DQC-M(Data Management Certification)**

```
[DQC-M: 데이터 품질관리 프로세스(Management)의 성숙도 인증]

심사 대상: 조직이 데이터 품질을 지속적으로 관리하는 절차·체계
심사 방법: 프로세스 영역(예: 데이터 처리작업 관리·인적자원 관리 등)을
           성숙도 레벨 관점에서 심사

성숙도 레벨(다단계, CMMI 유사 구조):
  Level 1~5로 구성
  레벨이 높을수록 심사 범위(요구 프로세스 영역)가 확장
  예) 특정 프로세스는 Level 2~5에서 상시 심사 대상
      특정 프로세스(인적자원 관리 등)는 Level 4~5에서만 심사 대상
```

**다. 핵심 체계 비교**

| 항목             | DQC-V                           | DQC-M                          |
| :------------- | :------------------------------ | :----------------------------- |
| **인증 대상**      | 데이터 **값(Value)** 자체             | 데이터 품질 **관리 프로세스**             |
| **핵심 질문**      | "이 데이터베이스 안의 값이 정확한가"           | "이 조직이 데이터 품질을 지속 관리할 역량이 있는가" |
| **측정 방식**      | 정량적 오류율(정합률) 측정                 | 프로세스 성숙도 레벨 평가                 |
| **등급 체계**      | 실버·골드·플래티넘(3단계)                 | 성숙도 레벨(다단계, 최대 5단계)            |
| **관계되는 국제 개념** | ISO/IEC 25012의 정확성(Accuracy) 특성 | CMMI류 프로세스 성숙도 모델과 유사한 철학      |

***

#### Ⅲ. 비교 및 적용 체계

**가. 인증 제도 전체 구조 내 위치**

| 구분                  | 주관기관                                                  | 근거                   |
| :------------------ | :---------------------------------------------------- | :------------------- |
| **DQC-V/DQC-M**     | 한국데이터산업진흥원(K-DATA), 지정 심사기관(예: 와이즈스톤·비투엔 등)이 실무 심사 수행 | 데이터산업진흥법 관련 규정       |
| **공공데이터 품질관리 수준평가** | 행정안전부·NIA(한국지능정보사회진흥원)                                | 공공데이터법 제22조·시행령 제17조 |

**나. 두 인증의 공공기관 활용 관계**

| 구분                         | 내용                                                                                        |
| :------------------------- | :---------------------------------------------------------------------------------------- |
| **공공데이터 품질관리 수준평가(별도 제도)** | 데이터 관리체계·데이터 값·품질진단 결과조치 3개 영역, 11개 지표로 기관 전체를 평가(DQC-V/M과는 별도의 법정 평가 체계)                 |
| **DQC-V/M과의 관계**           | 공공기관이 데이터 신뢰성을 대외적으로 증명하고자 할 때 DQC-V(값 정확성)를 별도로 취득해 활용하는 사례가 다수(예: 지자체 공공데이터 포털의 정합률 인증) |
| **실무적 조합**                 | 데이터 값 신뢰성은 DQC-V로, 그 값을 만들어내는 조직 역량은 DQC-M으로 증명하는 것이 상호 보완적                               |

**다. 적용 시나리오별 선택 기준**

| 시나리오                               | 권장 인증                   | 이유                                   |
| :--------------------------------- | :---------------------- | :----------------------------------- |
| **공공데이터 포털 개방 데이터의 신뢰도 홍보**        | **DQC-V**               | 대외적으로 정합률 수치(예: 99.9% 이상)를 명확히 제시 가능 |
| **데이터 거버넌스 체계 구축 증빙(내부 감사·계약 조건)** | **DQC-M**               | 일회성 값 검사가 아닌 지속 관리 역량을 증명            |
| **SI 사업 데이터 이관·마이그레이션 완료 검증**      | **DQC-V**               | 이관 후 데이터 정합성을 정량적으로 검증               |
| **장기 데이터 플랫폼 운영기관의 신뢰성 인증**        | **DQC-V + DQC-M 동시 취득** | 값의 정확성과 관리 프로세스 성숙도를 함께 증명           |

**라. 국제 표준·개념과의 대응 관계**

| DQC 인증    | 대응하는 국제 개념                                                    |
| :-------- | :------------------------------------------------------------ |
| **DQC-V** | ISO/IEC 25012의 정확성(Accuracy)·일관성(Consistency) 특성의 국내 정량 인증 버전 |
| **DQC-M** | 프로세스 성숙도 모델(CMMI류)의 데이터 품질관리 영역 특화 버전                         |

***

**(제언)** "DQC-V와 DQC-M을 나눠 운영하는 것의 실무적 의미는 '오늘 데이터가 깨끗한 것'과 '내일도 계속 깨끗할 수 있는 것'이 서로 다른 문제라는 인식에 있으며, 정합률 99.9%의 플래티넘 등급을 받은 데이터베이스라도 그 값을 만들어내는 입력·검증·정제 프로세스가 허술하다면 시간이 지나며 다시 오류가 누적될 수밖에 없으므로, 실무에서는 신규 시스템 오픈이나 대규모 데이터 이관 직후에는 DQC-V로 결과물의 정확성을 먼저 검증하고, 이후 그 품질 수준을 유지하기 위한 조직·프로세스 체계가 자리 잡았는지를 DQC-M으로 별도 검증하는 순차적·병행적 접근이 데이터 신뢰성을 지속가능하게 확보하는 핵심 전략이며, 공공기관이 대규모 데이터 플랫폼을 운영한다면 두 인증을 함께 취득해 '정확한 값'과 '지속 가능한 관리 역량'을 대외적으로 동시에 증명하는 것이 데이터 기반 행정 신뢰성 확보의 실질적 목표가 됩니다.

### **I. 국가 데이터 자산의 무결성 보장, DQC-V와 DQC-M의 개요**

AI 및 빅데이터 시대에 정제되지 않은 저품질 데이터(Garbage In)는 서비스 오류와 잘못된 의사결정(Garbage Out)을 유발합니다. \*\*데이터 품질 인증(DQC: Data Quality Certification)\*\*은 시스템 내에 저장된 \*\*실제 데이터 값의 정밀도를 산출해 등급화하는 DQC-V(Value)\*\*와, 이러한 고품질 데이터를 지속적으로 유지·관리할 수 있는 \*\*조직의 관리 프로세스 성숙도를 진단하는 DQC-M(Management)\*\*의 두 가지 축으로 이원화하여 인증을 부여합니다.

***

### **II. DQC-V(값 인증)와 DQC-M(관리체계 인증)의 인증 등급 체계**

#### **1. DQC-V (Data Quality Certification - Value) 인증 등급**

DB에 기록된 실제 데이터의 정밀도(정합률)에 따라 3단계 등급으로 구분합니다.

| **인증 등급 🔑**        | **🏁 정밀도(정합률) 수리 기준 💯**       | **의미 및 평가 수준**                 |
| :------------------ | :----------------------------- | :----------------------------- |
| **Platinum (플래티넘)** | **99.999% 이상** (오류율 0.001% 이하) | 최고 수준의 데이터 정밀도 (6 시그마급 무결성 확보) |
| **Gold (골드)**       | **99.9% 이상** (오류율 0.1% 이하)     | 우수한 수준의 데이터 정확성 보장             |
| **Silver (실버)**     | **95.0% 이상** (오류율 5.0% 이하)     | 기본적인 업무 수행이 가능한 최저 적합 정합 수준    |

#### **2. DQC-M (Data Quality Certification - Management) 인증 등급**

CMMI와 유사하게 조직의 데이터 관리 프로세스 성숙도를 5개 레벨로 평가합니다.

* **Level 5 (최적화 - Optimization)**: 데이터 품질 관리 프로세스가 자동화되고 지속적으로 개선되는 단계
* **Level 4 (정량적 관리 - Quantitatively Managed)**: 품질 측정 지표(KPI)에 따라 데이터 품질을 정량 통제하는 단계
* **Level 3 (정의 - Defined)**: 전사 차원의 공통 데이터 표준, 구조, 흐름 프로세스가 정립된 단계
* **Level 2 (도입 - Managed)**: 부서/프로젝트 단위로 최소한의 데이터 품질 관리가 이루어지는 단계
* **Level 1 (초기 - Initial)**: 일관된 프로세스 없이 비정형적으로 데이터가 관리되는 단계

***

### **III. 데이터 값 인증(DQC-V)과 데이터 관리체계 인증(DQC-M)의 상세 비교**

| **비교 항목**    | **📊 DQC-V (Data Quality Certification - Value)** | **🏢 DQC-M (Data Quality Certification - Management)** |
| :----------- | :------------------------------------------------ | :----------------------------------------------------- |
| **평가 핵심 대상** | 실제 DB 테이블 내에 저장된 **데이터 값(Value) 자체**              | 데이터를 수집·운영하는 **조직의 관리 프로세스 및 체계**                      |
| **인증 등급 체계** | **3단계 등급 (Platinum, Gold, Silver)**               | **5단계 성숙도 레벨 (Level 1 \~ Level 5)**                    |
| **핵심 정량 기준** | **데이터 정밀도(%)** (정확성, 완전성, 일관성 등 측정)               | 데이터 표준, 구조, 흐름 등 **프로세스 이행 적합성**                       |
| **주요 심사 기법** | 전수 데이터 프로파일링(Profiling) 및 검증 룰 수행                 | 현장 인터뷰, 표준 지침서/산출물 검토 및 프로세스 점검                        |
| **인증의 유효성**  | 정적 시점의 데이터 값 검증 (주기적 재인증 필요)                      | 고품질 데이터를 지속적으로 생산해내는 **체질 개선 입증**                      |

***

### **IV. 고품질 데이터 자산 확보를 위한 엔지니어링 가이드라인**

**IMPORTANT**

1. **자동화된 데이터 프로파일링 도구 도입**: DQC-V 인증 획득 및 유지를 위해 매일 밤 DB 전수 데이터에 대해 컬럼 타입, 범위, 패턴, 외래키 참조 무결성을 자동으로 진단하는 프로파일링 시스템(DQMS)을 연동해야 합니다.
2. **DQC-M 레벨 3 선행 수립**: DQC-V(값) 등급만 임시로 올리면 데이터가 금방 다시 오염됩니다. 따라서 표준 단어 사전, 표준 용어 사전, 데이터 아키텍처(DA) 구조를 정립하는 DQC-M 레벨 3 이상의 관리 프로세스를 먼저 고착화해야 고품질 값 유지가 가능합니다.
