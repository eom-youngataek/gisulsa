### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (FP정의,LOC방식과의차이) — 3~4줄
Ⅱ. 정밀법 - 5대기능유형 (본론①, 도식 1개 필수)
Ⅲ. 간이법 - 평균복잡도적용 (본론②, 핵심 배점)
Ⅳ. 정밀법vs간이법및비용산정연결
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서다룬McCabe(코드내부복잡도)나 Fan-in/Fan-out(모듈간관계)은 '이미짜여진코드'를측정했는데, FP는 코드를보지않고도 '사용자가보는기능' 관점에서 소프트웨어규모를측정 — 개발자중심(LOC)이아니라 사용자관점(User View)으로 규모를잰다는게 핵심"\*\*이라는한줄로시작하면, 왜FP가 개발비산정의표준이됐는지논리가섭니다.

### Ⅱ. 정밀법 — 5대기능유형(IFPUG표준)

| 구분         | 유형              | 내용                            |
| :--------- | :-------------- | :---------------------------- |
| **데이터기능**  | **ILF**(내부논리파일) | 시스템내부에서 **유지·관리**하는데이터그룹      |
| <br />     | **EIF**(외부연계파일) | **다른시스템이관리**하지만 우리시스템이참조하는데이터 |
| **트랜잭션기능** | **EI**(외부입력)    | 데이터를 **입력·수정·삭제**(CRUD중CUD)   |
| <br />     | **EO**(외부출력)    | **가공된결과**를출력(계산,파생데이터포함)      |
| <br />     | **EQ**(외부조회)    | **단순조회**(가공없이그대로꺼내옴)          |

→ 암기: **"데이터는안(ILF)과밖(EIF),트랜잭션은넣고(EI)내고(EO)보는것(EQ)"** — **"설계공정이후"** 상세한기능이확정된시점에 사용하며, 각기능의 \*\*개별복잡도(RET,DET수등)\*\*를따져 정확하게 점수를매기는게 정밀법의핵심입니다.

### 도식화 제안

```
[정밀법 - 5대기능유형]
   ┌────────┴────────┐
[데이터기능]              [트랜잭션기능]
ILF(내부논리파일)           EI(입력:CUD)
EIF(외부연계파일)           EO(출력:가공결과)
                          EQ(조회:단순출력)
   ↓ 각각개별복잡도(RET/DET,FTR/DET)측정
[정확한기능점수(UFP)]
```

### Ⅲ. 간이법 — 평균복잡도적용, 핵심 배점

**함정 방지: "정밀법을간단히한것"이라고만답하면절반. "왜간단해야하는가(적용시점의제약)"를보여줘야완성됩니다.**

| 항목       | 내용                                                  |
| :------- | :-------------------------------------------------- |
| **적용시점** | **기획,ISP,발주단계**— 아직 **상세설계가안나온상태**                  |
| **적용원리** | 개별기능의 **복잡도를판단하기어려우므로**, **평균복잡도가중치**를일괄적용          |
| **한계**   | 알려지지않은기능,복잡도에대한 **가정을허용**— 정밀도는떨어지지만 **초기에빠르게산정가능** |

→ 암기: **"아직세부설계가안나왔으니, 복잡도를일일이재지말고 평균값으로대충잡는다"** — 앞서다룬 \*\*"프로토타이핑"\*\*에서 요구사항이불확실할때 실물로먼저확인했던것처럼, 간이법도 \*\*"정보가부족한초기단계에서 실무적으로쓸수있는근사치측정법"\*\*입니다.

### 도식화 제안

```
[정밀법]                          [간이법]
설계단계이후                        기획/발주단계
개별기능마다                        평균복잡도가중치를
RET/DET등 세부복잡도측정              일괄적용(개별측정불필요)
     ↓                                ↓
정확하지만,                         빠르지만,
상세설계나와야가능                    정밀도는낮음
```

### Ⅳ. 정밀법vs간이법 및 비용산정연결

**함정 방지: FP산출로끝나면절반. 그FP가어떻게실제"개발비"로환산되는지보여줘야완성됩니다.**

| 단계          | 공식                                                      |
| :---------- | :------------------------------------------------------ |
| **보정전개발원가** | 기능점수(UFP) × **기능점수당단가**                                 |
| **보정후개발원가** | 보정전개발원가 × (**규모보정계수 × 연계복잡성 × 성능요구수준 × 운영환경호환성 × 보안성**) |

→ **2024년개정판(한국소프트웨어산업협회)** 기준, **기능점수(FP)당단가가 553,114원에서605,784원으로9.52%인상**됐습니다 — 앞서다룬 \*\*"IT-ROI/CBAM"\*\*답안에서 다룬 정량적비용산정논리가, FP에서는 \*\*"기능점수×단가×보정계수"\*\*라는 구체적공식으로실현된것입니다.

→ 암기: **"기능점수에단가곱하고,규모·연계·성능·호환성·보안성으로보정한다"** — 특히 \*\*"성능요구수준,보안성수준"\*\*같은 보정계수는, 앞서다룬 **"ISO25010의8대품질특성"**(성능효율성,보안성등)이 **비용산정에직접반영**된다는 흥미로운연결점입니다.

### Ⅴ. 결론 포인트 (설계·비용산정 시리즈 완결)

FP정밀법/간이법은 \*\*"소프트웨어규모를 코드가아니라 사용자기능관점에서, 프로젝트단계(초기/후기)에맞는정밀도로측정하는 실무표준"\*\*입니다 — 이는 오늘하루다룬 McCabe(내부복잡도),Fan-in/Fan-out(관계복잡도)이 \*\*"이미만들어진코드"\*\*를측정했던것과대비되며, FP는 \*\*"만들기전에,사용자가보는기능단위로 규모와비용을미리예측"\*\*한다는점에서, 앞서다룤 IT-ROI/CBAM(투자결정)의논리를 **한국공공SW사업의실제발주·계약금액**으로직접연결하는 실무적교량역할을합니다 — 이로써 오늘하루의 방대한소프트웨어공학·품질·비용산정시리즈전체가 **"설계에서품질로,품질에서비용으로"** 이어지는 하나의완결된실무흐름으로 마무리됩니다.

### **1. 답안 전개 스토리 (머릿속 핵심 흐름)**

> "공공기관에서 대규모 소프트웨어 프로젝트를 발주하려고 한다. '이거 개발비 얼마 주면 됩니까?' 과거에는 '음, 대충 코드가 10만 줄 나올 것 같으니 100억 주십쇼(LOC 기법)'라고 주먹구구식으로 예산을 짰다. 하지만 똑같은 게시판을 만들어도 초보자는 1,000줄로 짜고 고수는 100줄로 짜는 마당에 코드 길이로 돈을 주는 건 넌센스다. 그래서 코드 길이를 무시하고 '사용자에게 제공되는 화면(입/출력)과 DB 파일의 개수'를 세어 합리적으로 돈을 지불하자는 혁명적 기법이 등장했다. 이것이 대한민국 공공 SW 사업 대가의 표준인 \*\*'기능점수(Function Point, FP)'\*\*다. 그런데 이 FP를 세는 방식은 프로젝트의 '시기'에 따라 두 가지로 나뉜다. 첫째, 프로젝트 **기초 기획 단계**다. 아직 화면 디자인도 없고 DB 테이블 구조도 모른다. 이때는 그냥 '회원가입 기능 1개, 결제 기능 1개' 식으로 기능의 개수만 센 다음, 국가 가이드라인에서 정해둔 고정된 '평균 점수(가중치)'를 일괄적으로 곱해버린다. 이것이 빠르고 대략적인 예산 편성을 위한 \*\*'간이법'\*\*이다. 둘째, **설계가 모두 끝난 후**다. 이제 회원가입 화면에 사용자가 입력해야 할 텍스트 칸(DET)이 10개인지 50개인지 다 안다. 이때는 기능 하나하나를 현미경처럼 들여다보고 복잡도(낮음, 보통, 높음)를 정밀하게 분석하여 각기 다른 가중치를 곱해 최종 점수를 산출한다. 이것이 실제 개발 대가를 정산할 때 쓰이는 \*\*'정밀법'\*\*이다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 코드가 아닌 '비즈니스 가치(기능)'로 돈을 지불하라, 기능점수(FP) 개요**

* **정의:** 알란 알브레히트(Allan Albrecht)가 고안한 기법으로, 소프트웨어의 개발 규모를 프로그래밍 언어나 소스코드 라인 수(LOC)에 의존하지 않고, **'사용자 관점에서 제공되는 비즈니스 기능의 양과 복잡도'를 정량적인 점수(Point)로 산정**하는 소프트웨어 규모 산정 기법.
* **산정 대상 (5대 유형):** 내부논리파일(ILF), 외부연계파일(EIF), 외부입력(EI), 외부출력(EO), 외부조회(EQ).
* **제도적 위상:** 대한민국 조달청 및 공공기관의 'SW 사업 대가 산정 가이드'에서 **예산 수립 및 사업 정산의 유일한 표준 법적 잣대**로 사용됨.

#### **II. \[본론 1] 기획(간이법) ➔ 설계(정밀법)로 이어지는 비용 산정 파이프라인 (도식화)**

프로젝트 진행 시점에 따라 사용할 수 있는 무기가 다름을 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNzE3LjQ3NDAwMDAwMDAwMDIgNDI1LjEyOSIgd2lkdGg9IjE3MTcuNDc0MDAwMDAwMDAwMiIgaGVpZ2h0PSI0MjUuMTI5IiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJGUF9fU1dfX18iIGRhdGEtbGFiZWw9Iuq4sOuKpeygkOyImChGUCkg6riw67CYIFNXIOuMgOqwgCDsgrDsoJUg7YyM7J207ZSE65287J24Ij4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSIxNjM3LjQ3NDAwMDAwMDAwMDIiIGhlaWdodD0iMzQ1LjEyOSIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjE2MzcuNDc0MDAwMDAwMDAwMiIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPuq4sOuKpeygkOyImChGUCkg6riw67CYIFNXIOuMgOqwgCDsgrDsoJUg7YyM7J207ZSE65287J24PC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJQMSIgZGF0YS10bz0iTTEiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iMjcxLjM0NCwyNTkuMjM5NSAzMTkuMzQ0LDI1My4xNjE5OTk5OTk5OTk5OCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTTEiIGRhdGEtdG89IlAyIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLruaDrpbgg7LSI6riwIOyYiOyCsCDtmZXrs7QiIHBvaW50cz0iNTQwLjE2MywyNTMuMTYxOTk5OTk5OTk5OTggNzQ2LjE5OTAwMDAwMDAwMDEsMjU5LjIzOTUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IlAyIiBkYXRhLXRvPSJNMiIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgcG9pbnRzPSI5NjUuMjQ4LDI1OS4yMzk1IDEwMTMuMjQ4LDI1Ni44NjY5OTk5OTk5OTk5NiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iTTIiIGRhdGEtdG89IkYiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IuyYpOywqOycqCAwJSDrj4TsoIQiIHBvaW50cz0iMTI0MS40NzcsMjU2Ljg2Njk5OTk5OTk5OTk2IDE0MjMuMTU5LDI1MC43ODk1IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209Ik0xIiBkYXRhLXRvPSJQMiIgZGF0YS1sYWJlbD0i67mg66W4IOy0iOq4sCDsmIjsgrAg7ZmV67O0Ij4KICA8cmVjdCB4PSI1ODQuMTYzIiB5PSIyMzkuMDE0NSIgd2lkdGg9IjExOC4wMzYwMDAwMDAwMDAwMyIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjY0My4xODEiIHk9IjI1NC4xNjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7ruaDrpbgg7LSI6riwIOyYiOyCsCDtmZXrs7Q8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iTTIiIGRhdGEtdG89IkYiIGRhdGEtbGFiZWw9IuyYpOywqOycqCAwJSDrj4TsoIQiPgogIDxyZWN0IHg9IjEyODUuNDc3MDAwMDAwMDAwMyIgeT0iMjM5LjAxNDUiIHdpZHRoPSI5My42ODIwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjEzMzIuMzE4MDAwMDAwMDAwMiIgeT0iMjU0LjE2NDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPuyYpOywqOycqCAwJSDrj4TsoIQ8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlAxIiBkYXRhLWxhYmVsPSLtlITroZzsoJ3tirgg67Cc7KO8L+q4sO2ajSDri6jqs4Qg8J+TnArslYTsp4Eg64K067aAIOyEpOqzhOqwgCDslYgg64KY7Ji0IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSIyMzIuMzM5NTAwMDAwMDAwMDIiIHdpZHRoPSIyMTUuMzQ0IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjY2ZkOGRjIiBzdHJva2U9IiM5MGE0YWUiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxNjMuNjcyIiB5PSIyNTkuMjM5NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTYzLjY3MiIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPu2UhOuhnOygne2KuCDrsJzso7wv6riw7ZqNIOuLqOqzhCDwn5OcPC90c3Bhbj48dHNwYW4geD0iMTYzLjY3MiIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7JWE7KeBIOuCtOu2gCDshKTqs4TqsIAg7JWIIOuCmOyYtDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJNMSIgZGF0YS1sYWJlbD0iRlAg6rCE7J2067KVIOyggeyaqSDij7HvuI8K7Y+J6regIOuzteyeoeuPhCDqsIDspJHsuZgg6rOx7IWIIiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjQyOS43NTM1LDE0Mi43NTI1IDU0MC4xNjMsMjUzLjE2MTk5OTk5OTk5OTk4IDQyOS43NTM1LDM2My41NzE0OTk5OTk5OTk5NiAzMTkuMzQ0LDI1My4xNjE5OTk5OTk5OTk5OCIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI0MjkuNzUzNSIgeT0iMjUzLjE2MTk5OTk5OTk5OTk4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI0MjkuNzUzNSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPkZQIOqwhOydtOuylSDsoIHsmqkg4o+x77iPPC90c3Bhbj48dHNwYW4geD0iNDI5Ljc1MzUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPu2Pieq3oCDrs7XsnqHrj4Qg6rCA7KSR7LmYIOqzseyFiDwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQMiIgZGF0YS1sYWJlbD0i7ISk6rOEIOuLqOqzhCDsmYTro4wg8J+Pl++4jwrtmZTrqbQg7ZWt66qp7IiYKERFVCkg64+E7LacIOyZhOujjCEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNzQ2LjE5OTAwMDAwMDAwMDEiIHk9IjIzMi4zMzk1MDAwMDAwMDAwMiIgd2lkdGg9IjIxOS4wNDg5OTk5OTk5OTk5OCIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2NmZDhkYyIgc3Ryb2tlPSIjOTBhNGFlIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iODU1LjcyMzUwMDAwMDAwMDEiIHk9IjI1OS4yMzk1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSI4NTUuNzIzNTAwMDAwMDAwMSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuyEpOqzhCDri6jqs4Qg7JmE66OMIPCfj5fvuI88L3RzcGFuPjx0c3BhbiB4PSI4NTUuNzIzNTAwMDAwMDAwMSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7ZmU66m0IO2VreuqqeyImChERVQpIOuPhOy2nCDsmYTro4whPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9Ik0yIiBkYXRhLWxhYmVsPSJGUCDsoJXrsIDrspUg7KCB7JqpIPCflKwK6rCc67OEIOuzteyeoeuPhCDsg4Ev7KSRL+2VmCDsgrDstpwiIGRhdGEtc2hhcGU9ImRpYW1vbmQiPgogIDxwb2x5Z29uIHBvaW50cz0iMTEyNy4zNjI1LDE0Mi43NTI1IDEyNDEuNDc2OTk5OTk5OTk5OSwyNTYuODY3IDExMjcuMzYyNSwzNzAuOTgxNTAwMDAwMDAwMDQgMTAxMy4yNDc5OTk5OTk5OTk5LDI1Ni44NjciIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTEyNy4zNjI1IiB5PSIyNTYuODY3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiPjx0c3BhbiB4PSIxMTI3LjM2MjUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj5GUCDsoJXrsIDrspUg7KCB7JqpIPCflKw8L3RzcGFuPjx0c3BhbiB4PSIxMTI3LjM2MjUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuqwnOuzhCDrs7XsnqHrj4Qg7IOBL+ykkS/tlZgg7IKw7LacPC90c3Bhbj48L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkYiIGRhdGEtbGFiZWw9Iuy1nOyihSBTVyDqsJzrsJwg7KCV7IKwIOuMgOqwgCDtmZXsoJUg8J+SsCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIxNDIzLjE1OSIgeT0iMjMyLjMzOTUwMDAwMDAwMDAyIiB3aWR0aD0iMjM4LjMxNSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2U4ZjVlOSIgc3Ryb2tlPSIjMzg4ZTNjIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSIxNTQyLjMxNjUwMDAwMDAwMDEiIHk9IjI1MC43ODk1MDAwMDAwMDAwMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7LWc7KKFIFNXIOqwnOuwnCDsoJXsgrAg64yA6rCAIO2ZleyglSDwn5KwPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJOb3RlIiBkYXRhLWxhYmVsPSJOb3RlIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI4NCIgd2lkdGg9IjY4LjYyNiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjkwLjMxMyIgeT0iMTAyLjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5Ob3RlPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] FP 간이법 vs 정밀법 산정 메커니즘 전격 해부 (3단 표 - 출제 1순위)**

핵심 차이점인 \*\*'복잡도 가중치를 어떻게 매기는가'\*\*를 정확히 찔러야 합니다.

| **척도 (잣대)**             | **⏱️ 간이법 (평균 복잡도 가중치 적용법)**                                                                              | **🔬 정밀법 (상세 복잡도 가중치 적용법)**                                                                                        |
| :---------------------- | :------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| **적용 시점 (When)**        | 프로젝트 극초기인 **기획, 발주 단계.** (요구사항 정의 수준).                                                                   | 프로젝트의 데이터베이스 및 UI **설계가 모두 완료된 단계, 또는 구현 단계.**                                                                     |
| **적용 환경 조건**            | 기능을 5대 유형(ILF, EI 등)으로만 식별할 수 있고, **기능 내부의 세부 항목(DB 컬럼 수 등)까지는 아직 모를 때** 사용.                             | 기능의 세부 필드 수(DET), 레코드 수(RET), 참조 파일 수(FTR)를 **현미경처럼 전부 셀 수 있을 때** 사용.                                              |
| **복잡도 가중치 적용 방식 (How)** | 개별 기능의 실제 난이도를 무시하고, 소프트웨어 대가 산정 가이드가 제시하는 **'고정된 평균 복잡도 가중치'를 일괄적으로 곱함.** *(예: EI 기능이면 무조건 가중치 4.0 곱함)* | 각 기능별로 DET, RET, FTR의 개수를 직접 세어, 매트릭스 표에 따라 개별 기능의 **복잡도를 '낮음(Low), 보통(Average), 높음(High)' 3단계로 정밀하게 차등 판정하여 곱함.** |
| **장점과 단점**              | **\[장점]** 내부를 몰라도 되므로 산정 속도가 매우 빠름. **\[단점]** 고정값을 곱하므로 실제 개발 난이도와 오차가 발생할 수 있음.                         | **\[장점]** 실제 구현할 항목 수를 기반으로 하므로 오차율이 극히 적고 가장 정확함. **\[단점]** 설계가 끝날 때까지 기다려야 하고, 산정 시간이 오래 걸림.                     |

#### **IV. \[결론/제언] 대한민국 공공 SW 발주 표준과 데이터 수집(DET/RET)의 자동화 트렌드**

* **(키워드 위주 2줄 마무리)** "기능점수(FP)는 대한민국 공공 SW 사업의 예산 낭비를 막고 합리적인 대가를 보장하는 법적 보호막입니다. 과거 정밀법은 DET와 RET를 사람이 엑셀로 일일이 세어야 하는 막대한 수작업 노력이 필요했으나, 최근에는 **UML 설계 도구나 소스코드 파싱을 통해 DET를 자동으로 추출해 내는 'FP 자동 산정 솔루션'이 도입되며 정밀법의 시간적 한계를 혁신적으로 극복**해 나가고 있습니다."
