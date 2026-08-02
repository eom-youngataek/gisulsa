### **IT 투자 비용 분류 체계: CapEx vs OpEx**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 IT 투자를 CapEx와 OpEx로 구분하는가)
Ⅱ. CapEx·OpEx 핵심 비교
Ⅲ. 클라우드·AI 시대의 CapEx→OpEx 전환
Ⅳ. 결론
```

포인트: 개요에서 **"앞서 다룬 IT거버넌스의 가치 전달·ROI 측정에서 IT 투자 비용을 어떻게 회계 처리하느냐가 재무제표·세금·현금흐름에 직접 영향을 미친다 — CapEx(Capital Expenditure·자본적 지출)는 '미래 수익을 위해 자산을 취득하는 일회성 대규모 투자로 감가상각을 통해 여러 해에 걸쳐 비용 인식'하고, OpEx(Operational Expenditure·운영적 지출)는 '서비스를 유지하기 위한 반복적 지출로 발생 즉시 비용 인식'하는 차이이며, 앞서 다룬 클라우드 퍼스트·디지털서비스 전문계약이 공공 IT 조달을 CapEx 중심에서 OpEx 중심으로 전환하는 핵심 동인"**이라는 한 줄로 시작하면 전체 맥락이 드러납니다.
\
![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5ODQuMDI4OTk5OTk5OTk5OSAyODYuNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSI5ODQuMDI4OTk5OTk5OTk5OSIgaGVpZ2h0PSIyODYuNzAwMDAwMDAwMDAwMDUiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iSVQiIGRhdGEtdG89IkNhcEV4IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjQ4Mi4xOTYyNDk5OTk5OTk5Niw3Ni45IDQ4Mi4xOTYyNDk5OTk5OTk5NiwxMDAuOSAyNDkuMTg4OTk5OTk5OTk5OTYsMTAwLjkgMjQ5LjE4ODk5OTk5OTk5OTk2LDEyNC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJJVCIgZGF0YS10bz0iT3BFeCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI0ODIuMTk2MjQ5OTk5OTk5OTYsNzYuOSA0ODIuMTk2MjQ5OTk5OTk5OTYsMTAwLjkgNzE1LjIwMzQ5OTk5OTk5OTgsMTAwLjkgNzE1LjIwMzQ5OTk5OTk5OTgsMTI0LjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209Ik9wRXgiIGRhdGEtdG89IkZpbk9wcyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI3MTUuMjAzNDk5OTk5OTk5OCwxNjEuOCA3MTUuMjAzNDk5OTk5OTk5OCwyMDkuOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iSVQiIGRhdGEtbGFiZWw9IklUIO2IrOyekCDsnqzrrLQg66qo6424IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQwNy40OTg3NSIgeT0iNDAiIHdpZHRoPSIxNDkuMzk0OTk5OTk5OTk5OTgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI0ODIuMTk2MjQ5OTk5OTk5OTYiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5JVCDtiKzsnpAg7J6s66y0IOuqqOuNuDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ2FwRXgiIGRhdGEtbGFiZWw9IkNhcEV4IDog66y866asIOyekOyCsCDrp6TsnoUg4p6UIOuMgOywqOuMgOyhsO2RnCDrk7HroZ0g4p6UIOuLpOuFhCDqsJDqsIDsg4HqsIEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDAiIHk9IjEyNC45IiB3aWR0aD0iNDE4LjM3Nzk5OTk5OTk5OTkzIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyNDkuMTg4OTk5OTk5OTk5OTYiIHk9IjE0My4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+Q2FwRXggOiDrrLzrpqwg7J6Q7IKwIOunpOyehSDinpQg64yA7LCo64yA7KGw7ZGcIOuTseuhnSDinpQg64uk64WEIOqwkOqwgOyDgeqwgTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iT3BFeCIgZGF0YS1sYWJlbD0iT3BFeCA6IO2BtOudvOyasOuTnCDshJzruYTsiqQg6rWs64+FIOKelCDshpDsnbXqs4TsgrDshJwg67CY7JiBIOKelCDri7nquLAg67mE7JqpIOyymOumrCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0ODYuMzc3OTk5OTk5OTk5OTMiIHk9IjEyNC45IiB3aWR0aD0iNDU3LjY1MDk5OTk5OTk5OTk1IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjcxNS4yMDM0OTk5OTk5OTk4IiB5PSIxNDMuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPk9wRXggOiDtgbTrnbzsmrDrk5wg7ISc67mE7IqkIOq1rOuPhSDinpQg7IaQ7J216rOE7IKw7IScIOuwmOyYgSDinpQg64u56riwIOu5hOyaqSDsspjrpqw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkZpbk9wcyIgZGF0YS1sYWJlbD0iRmluT3BzIDog6rCA67OA67mE7JqpIOyLpOyLnOqwhCDqtIDsoJwgJmFtcDsg64Kt67mEIOyekOybkCDstZzsoIHtmZQiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNTQwLjEwMDQ5OTk5OTk5OTkiIHk9IjIwOS44IiB3aWR0aD0iMzUwLjIwNiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjcxNS4yMDM0OTk5OTk5OTk4IiB5PSIyMjguMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPkZpbk9wcyA6IOqwgOuzgOu5hOyaqSDsi6Tsi5zqsIQg6rSA7KCcICZhbXA7IOuCreu5hCDsnpDsm5Ag7LWc7KCB7ZmUPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

***

#### Ⅱ. CapEx·OpEx 핵심 비교

**가. 정의 및 회계 처리**

| 항목           | CapEx                             | OpEx                    |
| :----------- | :-------------------------------- | :---------------------- |
| **정의**       | 자산 취득·인프라 구축을 위한 자본적 지출           | 서비스 운영·유지를 위한 반복적 지출    |
| **회계 처리**    | 자산으로 계상 후 **감가상각** (수년에 걸쳐 비용 인식) | 발생 즉시 **전액 비용** 인식      |
| **재무제표**     | 대차대조표(자산) 반영                      | 손익계산서(비용) 반영            |
| **IT 대표 사례** | 서버·스토리지 구매·IDC 구축·SW 영구 라이선스      | 클라우드 구독료·SaaS 이용료·유지보수비 |

***

**나. CapEx vs OpEx 전면 비교**

| **핵심 척도**  | **📊 CapEx (자본적 지출) 🚨**                           | **🔑 OpEx (운영적 지출) 🚨**                                | **🏁 선택 기준 💯**                                 |
| :--------- | :------------------------------------------------- | :----------------------------------------------------- | :---------------------------------------------- |
| **비용 구조**  | 초기 대규모 일회성 투자 / 감가상각 5\~10년 분산 / 자산 보유·관리 비용 추가    | 월정액·구독·종량제 / 발생 즉시 전액 비용 / 사용량 비례 탄력 정산                | 초기 자본 여력 낮음 → OpEx 유리 / 장기 안정 운영 예정 → CapEx 유리  |
| **재무 영향**  | 초기 현금 유출 집중 🚨 / 자산 계상으로 부채비율 영향 / 감가상각으로 세금 혜택 분산 | 초기 부담 낮음 ✅ / 비용 즉시 인식으로 세금 혜택 즉각 / 현금흐름 예측 용이          | 앞서 다룬 **IT-ROI·NPV** 산정 시 두 방식 재무 효과 비교 필수      |
| **유연성·위험** | 기술 변화 시 자산 陳腐化 위험 🚨 / 과잉 투자·과소 투자 위험 / 벤더 종속 위험   | 수요 변화 즉각 대응 ✅ / 계약 종료로 유연 전환 / 앞서 다룬 **공급자 종속** 위험은 존재 | 기술 변화 빠른 AI·클라우드 → OpEx / 안정적 코어 시스템 → CapEx 혼합 |

***

#### Ⅲ. 클라우드·AI 시대의 CapEx→OpEx 전환

**가. 전환 동인**

```
[CapEx→OpEx 전환 가속 배경]

기존 (CapEx 중심):
  IDC 서버 구매 → 5년 감가상각
  SW 영구 라이선스 → 자산 계상
  → 초기 비용↑·유연성↓

클라우드·AI 시대 (OpEx 중심):
  AWS·Azure·GCP → 월정액·종량제
  SaaS·AI API → 구독료·토큰 과금
  앞서 다룬 디지털서비스 전문계약 → 이용량 기반 정산
  → 초기 비용↓·유연성↑·민첩성↑
```

**나. 혼합(Hybrid) 전략**

| 구분         | CapEx 적합                  | OpEx 적합                    |
| :--------- | :------------------------ | :------------------------- |
| **시스템 유형** | 코어 뱅킹·ERP 등 안정적 레거시       | AI API·분석 플랫폼·협업 도구        |
| **규모**     | 대규모·장기 안정 수요              | 수요 변동성 높은 서비스              |
| **공공기관**   | 보안 민감 내부 시스템(CSAP 상등급)    | 앞서 다룬 **CSAP 하등급** 공개 SaaS |
| **AI 인프라** | GPU 서버 구매(앞서 다룬 **AIDC**) | AI API 구독·클라우드 GPU 임차      |

***

**다. 도식화**

```
[CapEx vs OpEx 재무 흐름 비교]

CapEx (서버 10억 구매·5년 감가상각):
연도:   0년    1년    2년    3년    4년    5년
현금:  -10억    0     0      0      0      0
비용:    0    -2억  -2억   -2억   -2억   -2억
(감가상각 연 2억씩 비용 인식)

OpEx (클라우드 월 1천만·연 1.2억):
연도:   0년    1년    2년    3년    4년    5년
현금:  -1.2억 -1.2억 -1.2억 -1.2억 -1.2억 -1.2억
비용:  -1.2억 -1.2억 -1.2억 -1.2억 -1.2억 -1.2억
(발생 즉시 전액 비용 인식)

→ 초기 현금: CapEx 불리 / 장기 총비용: TCO 분석 필수
→ 앞서 다룬 IT-ROI: NPV·IRR로 두 방식 재무 우열 판단
```

***

**(제언)** "CapEx·OpEx 선택은 단순한 회계 분류가 아니라 재무 전략·기술 민첩성·리스크 관리를 동시에 결정하는 IT 거버넌스의 핵심 의사결정입니다. **클라우드·AI 시대에는 코어 시스템은 CapEx로 안정성을 확보하고 혁신·분석·AI 서비스는 OpEx로 민첩성을 확보하는 하이브리드 전략이 최적이며, 앞서 다룬 IT-ROI·TCO 분석으로 두 방식의 장기 재무 효과를 비교하고 앞서 다룬 디지털서비스 전문계약·공공 SaaS 거버넌스와 연계해 공공기관의 OpEx 전환을 제도적으로 지원하는 것이 핵심입니다.**"
