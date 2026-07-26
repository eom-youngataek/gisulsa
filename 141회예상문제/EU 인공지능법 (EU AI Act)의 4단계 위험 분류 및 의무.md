#### **AI 규제의 글로벌 표준: EU AI Act 4단계 위험 분류 체계**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 EU가 위험 기반 접근으로 AI를 규제하는가)
Ⅱ. 4단계 위험 분류 핵심 체계
Ⅲ. 단계별 의무 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 인공지능기본법이 '국내 AI 규제의 고영향 AI 개념'을 다뤘다면, EU AI Act(2024년 8월 발효)는 그 고영향 AI 개념의 원조이자 전 세계 AI 규제 입법의 사실상 참조 표준이다 — GDPR이 개인정보 규제에서 그랬듯 EU AI Act도 '역외적용(Extraterritorial Effect)' 조항으로 EU 역내에서 서비스되는 AI라면 개발사의 국적과 무관하게 적용되며, 핵심은 '모든 AI를 동일하게 규제하지 않고 위험 수준에 비례해 규제 강도를 차등화한다'는 위험 기반 접근(Risk-Based Approach)으로, 금지(Unacceptable)-고위험(High)-제한적 위험(Limited)-최소 위험(Minimal)의 4단계 피라미드로 AI를 분류해 앞서 다룬 알고리즘 공정성 지표·AI 레드티밍·데이터 계보 등이 실제로 어느 수준에서 법적 의무가 되는지를 결정하는 글로벌 AI 거버넌스의 뼈대"\*\*라는 한 줄로 시작하면 전체 맥락이 드러납니다.

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjczLjMxNSAyNjIuNzAwMDAwMDAwMDAwMDUiIHdpZHRoPSIxMjczLjMxNSIgaGVpZ2h0PSIyNjIuNzAwMDAwMDAwMDAwMDUiIHN0eWxlPSItLWJnOiNGRkZGRkY7LS1mZzojM0IzQjNCOy0tbGluZTojM0IzQjNCOy0tYWNjZW50OiMwMDVGQjg7LS1tdXRlZDojM0IzQjNCQ0M7LS1zdXJmYWNlOiNGOEY4Rjg7LS1ib3JkZXI6IzNCM0IzQjtiYWNrZ3JvdW5kOnZhcigtLWJnKSI+CjxzdHlsZT4KICBAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1JbnRlcjp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZhbXA7ZGlzcGxheT1zd2FwJyk7CiAgdGV4dCB7IGZvbnQtZmFtaWx5OiAnSW50ZXInLCBzeXN0ZW0tdWksIHNhbnMtc2VyaWY7IH0KICBzdmcgewogICAgLyogRGVyaXZlZCBmcm9tIC0tYmcgYW5kIC0tZmcgKG92ZXJyaWRhYmxlIHZpYSAtLWxpbmUsIC0tYWNjZW50LCBldGMuKSAqLwogICAgLS1fdGV4dDogICAgICAgICAgdmFyKC0tZmcpOwogICAgLS1fdGV4dC1zZWM6ICAgICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtbXV0ZWQ6ICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDQwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LWZhaW50OiAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDI1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2xpbmU6ICAgICAgICAgIHZhcigtLWxpbmUsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNTAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2Fycm93OiAgICAgICAgIHZhcigtLWFjY2VudCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA4NSUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1maWxsOiAgICAgdmFyKC0tc3VyZmFjZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAzJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLXN0cm9rZTogICB2YXIoLS1ib3JkZXIsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjAlLCB2YXIoLS1iZykpKTsKICAgIC0tX2dyb3VwLWZpbGw6ICAgIHZhcigtLWJnKTsKICAgIC0tX2dyb3VwLWhkcjogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNSUsIHZhcigtLWJnKSk7CiAgICAtLV9pbm5lci1zdHJva2U6ICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEyJSwgdmFyKC0tYmcpKTsKICAgIC0tX2tleS1iYWRnZTogICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTAlLCB2YXIoLS1iZykpOwogIH0KPC9zdHlsZT4KPGRlZnM+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSI3IiByZWZZPSIyLjUiIG9yaWVudD0iYXV0byI+CiAgICA8cG9seWdvbiBwb2ludHM9IjAgMCwgOCAyLjUsIDAgNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CiAgPG1hcmtlciBpZD0iYXJyb3doZWFkLXN0YXJ0IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI1IiByZWZYPSIxIiByZWZZPSIyLjUiIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iOCAwLCAwIDIuNSwgOCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KPC9kZWZzPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUk9PVCIgZGF0YS10bz0iTGV2ZWwxIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjYxMC43MjI1LDc2LjkgNjEwLjcyMjUsOTQuOSAyMDIuNTA2LDk0LjkgMjAyLjUwNiwxMTIuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUk9PVCIgZGF0YS10bz0iTGV2ZWwyIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjYxMC43MjI1LDc2LjkgNjEwLjcyMjUsOTQuOSA2MTAuNzIyNSw5NC45IDYxMC43MjI1LDExMi45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJST09UIiBkYXRhLXRvPSJMZXZlbDMiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNjEwLjcyMjUsNzYuOSA2MTAuNzIyNSw5NC45IDEwNDQuODc0LDk0LjkgMTA0NC44NzQsMTEyLjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkxldmVsMyIgZGF0YS10bz0iTGV2ZWw0IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBwb2ludHM9IjEwNDQuODc0LDE0OS44IDEwNDQuODc0LDE4NS44IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJST09UIiBkYXRhLWxhYmVsPSJFVSBBSSBBY3QgNOuLqOqzhCDsnITtl5gg67aE66WYIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjUxMS41NzIiIHk9IjQwIiB3aWR0aD0iMTk4LjMwMSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjYxMC43MjI1IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+RVUgQUkgQWN0IDTri6jqs4Qg7JyE7ZeYIOu2hOulmDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTGV2ZWwxIiBkYXRhLWxhYmVsPSIxLiBVbmFjY2VwdGFibGUgUmlzayA6IOyCrO2ajOyggSDtlbTslYUg4p6UIOyghOuptCDquIjsp4AiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDAiIHk9IjExMi45IiB3aWR0aD0iMzI1LjAxMiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjAyLjUwNiIgeT0iMTMxLjM1MDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij4xLiBVbmFjY2VwdGFibGUgUmlzayA6IOyCrO2ajOyggSDtlbTslYUg4p6UIOyghOuptCDquIjsp4A8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkxldmVsMiIgZGF0YS1sYWJlbD0iMi4gSGlnaCBSaXNrIDog6riw67O46raML+yViOyghCDsmIHtlqUg4p6UIOyCrOyghCDsoIHtlanshLEg7Y+J6rCAIOuwjyDsl4Tqsqkg7J2Y66y0IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM5My4wMTIiIHk9IjExMi45IiB3aWR0aD0iNDM1LjQyMDk5OTk5OTk5OTk0IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjYxMC43MjI1IiB5PSIxMzEuMzUwMDAwMDAwMDAwMDIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjIuIEhpZ2ggUmlzayA6IOq4sOuzuOq2jC/slYjsoIQg7JiB7ZalIOKelCDsgqzsoIQg7KCB7ZWp7ISxIO2PieqwgCDrsI8g7JeE6rKpIOydmOustDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTGV2ZWwzIiBkYXRhLWxhYmVsPSIzLiBTcGVjaWZpYyAvIExpbWl0ZWQgUmlzayA6IO2YvOuPmSDsmrDroKQg4p6UIO2IrOuqheyEsSDqs7Xsp4Ag7J2Y66y0IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9Ijg1Ni40MzMiIHk9IjExMi45IiB3aWR0aD0iMzc2Ljg4MTk5OTk5OTk5OTk1IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTA0NC44NzQiIHk9IjEzMS4zNTAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+My4gU3BlY2lmaWMgLyBMaW1pdGVkIFJpc2sgOiDtmLzrj5kg7Jqw66CkIOKelCDtiKzrqoXshLEg6rO17KeAIOydmOustDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTGV2ZWw0IiBkYXRhLWxhYmVsPSI0LiBNaW5pbWFsIFJpc2sgOiDri6jsiJwg7Jyg7Yu466as7YuwIOKelCDsnpDsnKgg6rec7KCcIOy9lOuTnCDspIDsiJgiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iODU5Ljc2NzQ5OTk5OTk5OTkiIHk9IjE4NS44IiB3aWR0aD0iMzcwLjIxMjk5OTk5OTk5OTk3IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTA0NC44NzM5OTk5OTk5OTk4IiB5PSIyMDQuMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPjQuIE1pbmltYWwgUmlzayA6IOuLqOyInCDsnKDti7jrpqzti7Ag4p6UIOyekOycqCDqt5zsoJwg7L2U65OcIOykgOyImDwvdGV4dD4KPC9nPgo8L3N2Zz4= "Mermaid diagram")

***

#### Ⅱ. 4단계 위험 분류 핵심 체계

**가. 위험 피라미드 구조**

```
[EU AI Act 4단계 위험 분류 피라미드]

        ▲
       /금\     ①금지된 AI(Unacceptable Risk)
      /지 \      해당 AI 자체가 EU 내 시장 출시·사용 전면 금지
     /────\
    /고위험\    ②고위험 AI(High-Risk)
   / 의무多 \    엄격한 사전·사후 규제 준수 의무
  /──────\
 / 제한적위험 \  ③제한적 위험 AI(Limited Risk)
/ 투명성 의무 \  이용자에게 AI임을 고지하는 투명성 의무만
──────────
  최소 위험 AI   ④최소 위험 AI(Minimal Risk)
  규제 거의 없음   대다수의 일반 AI(스팸필터·게임 AI 등)

→ 아래로 갈수록 대상 범위는 넓고 규제 강도는 낮음
→ 위로 갈수록 대상 범위는 좁고 규제 강도는 매우 높음
```

**나. 4단계별 핵심 정의 및 예시**

| 위험 단계          | 정의                               | 대표 예시                                                                 |
| :------------- | :------------------------------- | :-------------------------------------------------------------------- |
| **①금지된 AI**    | 인간의 기본권을 용납 불가능한 수준으로 침해하는 AI 관행 | 사회적 신용점수(Social Scoring)·잠재의식 조작·실시간 원격 생체인식(공공장소, 예외적 허용 케이스 제한적 존재) |
| **②고위험 AI**    | 안전·기본권에 중대한 영향을 미치는 AI 시스템       | 채용·신용평가·의료기기·핵심 인프라 제어·법 집행·교육 평가                                     |
| **③제한적 위험 AI** | 조작·기만의 소지가 있어 투명성이 필요한 AI        | 챗봇·딥페이크·감정인식 시스템                                                      |
| **④최소 위험 AI**  | 위 3단계에 해당하지 않는 대다수 AI            | 스팸 필터·AI 게임 캐릭터·추천 알고리즘(일부)                                           |

***

#### Ⅲ. 단계별 의무 및 적용 체계

**가. 단계별 핵심 의무 비교**

| 위험 단계          | 핵심 의무                                                                                 | 시행(발효 기준)               |
| :------------- | :------------------------------------------------------------------------------------ | :---------------------- |
| **①금지된 AI**    | 시장 출시·서비스 제공 자체 **전면 금지**                                                             | 2025년 2월부터 적용(가장 먼저 시행) |
| **②고위험 AI**    | 위험관리시스템 구축·데이터 거버넌스·기술문서화·인간 감독(Human Oversight)·정확성/견고성/사이버보안 확보·**CE 마킹**을 통한 적합성평가 | 2026년 8월부터 본격 적용        |
| **③제한적 위험 AI** | AI와 상호작용하고 있음을 이용자에게 고지, 딥페이크 등 AI 생성물임을 표시                                           | 2025년 8월부터 적용           |
| **④최소 위험 AI**  | 법적 의무 없음, 자율적 행동강령(Code of Conduct) 권고                                                | 별도 시행일 없음(즉시 자율 적용)     |

**나. 고위험 AI 6대 핵심 의무 상세**

| 의무                         | 내용                             | 앞서 다룬 연계 개념                         |
| :------------------------- | :----------------------------- | :---------------------------------- |
| **위험관리시스템**                | 전체 생명주기에 걸친 지속적 위험 식별·평가·완화 절차 | 앞서 다룬 **AI 레드티밍**의 정기 수행 근거         |
| **데이터 거버넌스**               | 학습·검증·테스트 데이터의 품질·대표성·편향 관리    | 앞서 다룬 **ISO/IEC 25012·알고리즘 공정성 지표** |
| **기술문서화**                  | 시스템 설계·개발·검증 과정 전체를 문서로 기록·보관  | 앞서 다룬 **데이터 계보(Lineage)**           |
| **인간 감독(Human Oversight)** | 인간이 AI 결정을 이해·개입·중단할 수 있는 장치   | 앞서 다룬 **HITL(Human-in-the-Loop)**   |
| **투명성·정보제공**               | 사용자에게 시스템의 능력·한계를 명확히 고지       | 앞서 다룬 **AI 생성물 표시(C2PA)**           |
| **정확성·견고성·사이버보안**          | 성능 지표 유지 및 적대적 공격에 대한 강건성 확보   | 앞서 다룬 **멤버십 추론 공격 방어·MITRE ATLAS**  |

**다. EU AI Act vs 국내 인공지능기본법 비교**

| 비교 항목        | EU AI Act                         | 인공지능기본법(국내)             |
| :----------- | :-------------------------------- | :---------------------- |
| **접근 방식**    | **위험 기반 4단계 피라미드**(금지-고위험-제한적-최소) | 고영향 AI 중심(단일 임계 개념)     |
| **법적 지위**    | 직접 적용 규정(Regulation)              | 기본법(원칙 중심, 하위 법령 위임 다수) |
| **금지 AI 명시** | **명확한 금지 목록 존재**(사회적 신용점수 등)      | 명시적 금지 목록 상대적으로 제한적     |
| **역외 적용**    | **강력한 역외 적용**(GDPR과 유사)           | 국내 사업자 중심               |
| **벌금 수준**    | **최대 전 세계 매출의 7%**(가장 무거운 위반 기준)  | 상대적으로 낮은 과태료 체계         |
| **투명성 의무**   | 딥페이크·챗봇 명시 고지 의무(3단계)             | 유사한 취지의 표시 의무 조항 존재     |

**라. 실무 대응 체계**

| 활용 영역                       | EU AI Act 연계                                             |
| :-------------------------- | :------------------------------------------------------- |
| **AI 서비스 대가산정**             | 고위험 AI 분류 시 앞서 다룬 **적합성평가(CE 마킹)** 비용을 대가산정 항목에 반영 필요    |
| **AI 레드티밍**                 | 고위험 AI의 위험관리시스템 요구사항 이행을 위한 정기 수행 근거                     |
| **AI 서비스 대가산정·SaaS 도입 감리**  | 국내 기업이 EU 대상 AI 서비스 수출 시 감리·계약 조건에 EU AI Act 준수 여부 필수 검토 |
| **KIPRIS Plus 등 공공 IP 플랫폼** | AI 기반 특허 분석·추천 기능이 고위험 분류 대상인지 사전 자체 진단 필요               |

***

**(제언)** "EU AI Act 4단계 분류의 실무적 함의는 '모든 AI에 동일하게 무거운 규제를 적용하면 혁신이 질식한다'는 문제의식과 '위험한 AI는 예외 없이 엄격히 통제해야 한다'는 문제의식을 동시에 만족시키기 위해 규제 자원을 위험도에 비례해 선택적으로 집중시켰다는 점이며, 이는 GDPR이 전 세계 개인정보 규제의 사실상 표준이 됐듯 EU AI Act도 미국·영국·아시아 각국의 AI 입법에 참조 모델로 작용하고 있어 국내 기업이 국내법만 준수하는 것으로는 부족하고 글로벌 사업 확장을 염두에 둔다면 처음부터 이 4단계 프레임워크를 전사 AI 거버넌스 설계의 기준으로 삼는 것이 합리적입니다. 특히 채용·신용평가·의료처럼 고위험으로 분류될 가능성이 높은 영역의 AI 서비스를 개발한다면 앞서 다룬 위험관리시스템·데이터 거버넌스·인간 감독·기술문서화라는 4대 핵심 의무를 설계 단계부터 내재화해야 사후에 대응하는 것보다 훨씬 낮은 비용으로 규제를 충족할 수 있으며, 국내 인공지능기본법과의 이중 규제 리스크를 최소화하기 위해 두 법제의 요구사항을 통합한 단일 컴플라이언스 체크리스트를 구축하는 것이 실무의 핵심 전략입니다.

***

**앞서 다룬 개념과의 연결**

| 연계 개념              | 연결 내용                                         |
| :----------------- | :-------------------------------------------- |
| **인공지능기본법·고영향 AI** | EU AI Act의 고위험 AI 개념이 국내 고영향 AI 입법의 직접적 참조 모델 |
| **AI 레드티밍**        | 고위험 AI의 위험관리시스템 이행을 위한 실행 방법론으로 직결            |
| **MITRE ATLAS**    | 고위험 AI의 사이버보안·견고성 요건 충족을 위한 위협 인텔리전스 참조       |
| **알고리즘 공정성 지표**    | 데이터 거버넌스 의무의 편향 관리 요건을 정량적으로 충족하는 도구          |
| **HITL**           | 인간 감독(Human Oversight) 의무의 기술적 구현 방식          |

### **I. 세계 최초의 입법적 AI 규제 표준, EU AI Act의 개요**

유럽연합(EU)은 AI 기술 혁신과 인간의 기본권 보호 간의 균형을 도모하기 위해 위험 기반 접근법(Risk-based Approach)에 입각한 **EU AI Act**를 제정했습니다. 이 법안은 AI 시스템을 위험도에 따라 \*\*1) 수용 불가능한 위험(금지), 2) 고위험(엄격 규제), 3) 제한적 위험(투명성 의무), 4) 최소 위험(자율 규제)\*\*의 4단계로 체계화하고, 글로벌 파운더리 모델(GPAI)에 대해서도 별도의 시스템적 위험 통제 의무를 부과합니다.

***

### **II. EU AI Act 4단계 위험 분류별 세부 정의 및 이행 의무**

| **위험 등급 🔑**                            | **🏁 대상 시스템 예시 💯**                                                | **⚖️ 법적 규제 및 기업의 이행 의무**                                                                                                    |
| :-------------------------------------- | :----------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| **1. 수용 불가능한 위험** (Unacceptable Risk)   | · 정부의 개인 소셜 스코어링 · 공공장소 실시간 원격 생체 인식 · 취약계층 인지 조작 및 바이오 인식 분류      | **EU 역내 출시 및 서비스 전면 금지** (위반 시 최대 3,500만 유로 또는 전 세계 매출의 7% 과징금)                                                             |
| **2. 고위험** (High Risk)                  | · 의료기기, 교통/전력 등 핵심 인프라 · 채용/인사 평가, 신용 점수 산정 · 입학 평가, 사법/출입국 통제 시스템 | **엄격한 이행 의무 적용**: 1. 사전 적합성 평가 및 CE 마킹 2. 데이터 거버넌스(편향 제거) 및 위험 관리 3. **인간 감독(Human Oversight) 장치 강제** 4. 로깅 및 사이버 보안/견고성 보장 |
| **3. 제한적 위험** (Specific / Limited Risk) | · 고객 응대 챗봇 · 감정 인식 시스템 · 딥페이크 및 AI 생성 텍스트/이미지                      | **투명성(Transparency) 의무 부과**: 1. 사용자가 AI와 대화 중임을 명시 공지 2. 딥페이크/합성 콘텐츠에 **식별 워터마크(Watermark) 표시 의무화**                         |
| **4. 최소 위험** (Minimal / Low Risk)       | · AI 비디오 게임, 스팸 필터 · 단순 검색 및 추천 알고리즘                               | **법적 의무 부과 없음** (자율적 행동 강령 준수 권고)                                                                                           |

***

### **III. 생성형 AI (GPAI - 범용 인공지능) 모델 특화 규제**

* **GPAI (General Purpose AI) 기본 의무**: 저작권법 준수, 학습 데이터 요약본 공개, 투명성 보고서 작성.
* **시스템적 위험(Systemic Risk) GPAI 의무**: 연산량이 10251025 FLOPs 이상인 초거대 모델(예: GPT-4급 이상)은 **적대적 평가(Red Teaming)**, 시스템적 위험 평가, 사이버 보안 수준 보고 및 에너지 소비량 공개가 추가로 의무화됩니다.

***

### **IV. AI 개발 및 서비스 기업의 엔지니어링 컴플라이언스 대응 전략**

**IMPORTANT**

1. **고위험 AI에 대한 Human-in-the-Loop (HITL) 설계**: 채용이나 신용 평가 AI 개발 시, AI의 출력을 오프라인 최종 결정으로 자동 연결하지 않고 인간 평가자가 수동 개입(Override)하여 판정을 수정할 수 있는 제어판 인터페이스를 아키텍처에 내재화해야 합니다.
2. **AI 데이터 워터마킹(Watermarking) 내재화**: 생성형 AI 서비스 개발 시 C2PA 등 국제 기술 표준에 기반한 암호화 메타데이터 워터마크를 이미지/텍스트 오디오 출력물에 비가시성으로 강제 삽입하는 기술 적용이 필수적입니다.
