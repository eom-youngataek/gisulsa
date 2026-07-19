### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (TOCTOU정의,Race Condition과의관계) — 3~4줄
Ⅱ. 발생원리 (본론①, 도식 1개 필수)
Ⅲ. 대표공격사례 (본론②, 핵심 배점)
Ⅳ. 방어기법
Ⅴ. 결론
```

### Ⅰ. 개요

TOCTOU(Time-of-Check to Time-of-Use)는 \*\*"검사(Check)한시점"\*\*과 **"실제사용(Use)하는시점"** 사이에 **시간차가존재**하고, 그틈을공격자가노려 **검사통과후상태를바꿔버리는** 취약점입니다. 앞서다룬 \*\*"Race Condition"\*\*의한 특수한형태이지만, \*\*"보안검증을무력화한다"\*\*는 점에서 별도로다뤄야하는 고전적인 공격기법입니다.

### Ⅱ. 발생원리

| 단계            | 내용                      |
| :------------ | :---------------------- |
| **Check(검사)** | 프로그램이 **파일권한,경로,값등을확인** |
| **시간간격**      | 검사와사용사이 **아주짧지만존재하는틈**  |
| **Use(사용)**   | 검사결과를믿고 **실제작업수행**      |
| **공격지점**      | 그틈에 **다른프로세스가상태를변경**    |

→ 암기: **"확인했을때는안전했는데, 쓸때는이미바뀌어있다"**

### 도식화 제안

```
[정상프로세스]                    [공격자프로세스]
Check: "이파일은일반파일,권한OK"
        ↓ (시간간격)
                                파일을 심볼릭링크로교체
                                (예: /etc/passwd로연결)
Use: "OK했으니 그대로연다"
        ↓
     실제로는 /etc/passwd에 쓰기발생! (검사와사용대상이달라짐)
```

### Ⅲ. 대표공격사례 — 핵심 배점

**함정 방지: "이론적문제"로만끝내면절반. 실제로어떤형태로나타나는지 구체적사례를보여줘야완성됩니다.**

| 사례                   | 내용                                                                 |
| :------------------- | :----------------------------------------------------------------- |
| **심볼릭링크공격**          | 파일권한을 **검사한후**, 그파일을 **심볼릭링크로교체**해 다른(민감한)파일을가리키게함                 |
| **은행ATM류시나리오**       | **잔액확인(Check)** 후 **출금실행(Use)** 사이에, **동시에다른거래를요청**해 잔액이 실제보다많이출금됨 |
| **파일시스템경쟁**(CWE-367) | 임시파일생성시 **존재여부검사후생성**하는사이, 공격자가 **먼저같은이름의파일을심볼릭링크로선점**             |

→ 앞서다룬 \*\*"Race Condition의카운터증가예제"\*\*와 원리는같지만, TOCTOU는 특히 \*\*"보안검사(권한,신원,잔액등)를속이는데초점"\*\*을둔다는 점이 구별됩니다.

### Ⅳ. 방어기법

**함정 방지: "빨리처리하면된다"로만끝내면절반. 근본적해법(원자적연산)을보여줘야완성됩니다.**

| 기법                          | 내용                                             |
| :-------------------------- | :--------------------------------------------- |
| **원자적연산**(Atomic Operation) | 검사와사용을 **하나의쪼갤수없는단일연산**으로처리(중간에끼어들틈자체를제거)      |
| **락(Lock) 사용**              | 앞서다룬 **세마포어/뮤텍스**로 검사-사용구간전체를 **상호배제**         |
| **파일디스크립터기반접근**             | 경로(이름)로다시찾지않고, **이미열어둔파일디스크립터를그대로사용**(경로재탐색생략) |

→ 암기: **"확인과사용을분리하지말고, 한번에묶어서처리한다"** — 앞서다룬 \*\*"세마포어의P/V연산"\*\*이 바로 이 **"검사와사용사이에아무도못끼어들게만드는"** 원리의 실제도구입니다.

### Ⅴ. 결론

TOCTOU는 \*\*"보안검사를믿을수없게만드는 시간차공격"\*\*이며, 앞서다룬 **Race Condition**이 데이터의 **정확성**을깨뜨렸다면, TOCTOU는 **보안검증절차자체**를 무력화합니다. 근본해법은 \*\*"검사와사용을하나의원자적연산으로만들어, 그사이에끼어들틈을없애는것"\*\*이며, 이는 오늘하루다룬 \*\*세마포어(상호배제)\*\*개념이 **동시성문제뿐아니라보안검증의신뢰성확보**에도 필수적이라는것을 보여줍니다.

### **1. 답안 전개 스토리**

> "클럽 입구에서 기도(가드)가 신분증을 검사(Check)했다. 성인임이 확인되어 '통과' 도장을 찍어주었다. 그런데 이 손님이 문을 열고 클럽 안으로 들어가려는 찰나의 순간(Use), 문틈으로 자기 신분증을 미성년자 동생에게 휙 던져주고 동생이 쏙 들어가 버린다. 가드는 이미 검사가 끝났다고 생각해 미성년자가 들어가는 걸 막지 않는다. 이처럼 프로그램이 파일(자원)에 접근할 권한이 있는지 **'검사(Check)'하는 시점과 실제로 그 파일을 '사용(Use)'하는 시점 사이의 찰나의 틈(시간차)을 노려, 진짜 파일을 악성 파일로 쓱 바꿔치기하는 기법을 'TOCTOU' 취약점**이라고 부른다. 여러 프로그램이 동시에 달리는 멀티태스킹 OS 환경에서 발생하는 \*\*'경쟁 상태(Race Condition)'\*\*의 전형적인 범죄다. 이를 막으려면 신분증을 검사하자마자 그 사람을 다른 누구와도 자리를 바꾸지 못하게 수갑을 채워(Lock) 안으로 집어넣을 때까지 한 덩어리로 처리하는 \*\*'원자적 연산(Atomic Operation)'\*\*을 코드에 적용해야만 한다."

***

### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

#### **I. \[도입] 시간차를 노린 바꿔치기 마술, TOCTOU 개요**

* **정의:** 소프트웨어가 자원(파일, 메모리 등)의 상태나 권한을 \*\*검사하는 시점(Time of Check)\*\*과 실제로 그 자원을 **사용하는 시점(Time of Use)** 사이의 시간적 간극을 악용하여, 검사 통과 후 자원을 악의적으로 변조하는 보안 취약점.
* **발생 근본 원인 (Race Condition):** 운영체제(OS)가 여러 프로세스나 스레드를 번갈아 가며 실행(Context Switching)하기 때문에, 검사와 사용 사이에 해커의 악성 스레드가 끼어들 수 있는 '경쟁 상태'가 필연적으로 발생함.

#### **II. \[본론 1] (단순화 버전) 찰나의 순간을 노린 파일 바꿔치기 파이프라인 (도식화)**

검사(Check)와 사용(Use) 사이에 해커가 심볼릭 링크(바로가기)로 파일을 바꿔치기하는 과정을 직관적으로 시각화합니다.

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NzcuNDU4IDUyOC44IiB3aWR0aD0iNjc3LjQ1OCIgaGVpZ2h0PSI1MjguOCIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+CjxnIGNsYXNzPSJzdWJncmFwaCIgZGF0YS1pZD0iVE9DVE9VX19fX19fX19fIiBkYXRhLWxhYmVsPSJUT0NUT1UgKOqygOyCrCDsi5zsoJAgLyDsgqzsmqkg7Iuc7KCQKSDtjIzsnbwg67CU6r+U7LmY6riwIOqzteqyqSDrqZTsu6Tri4jsppgiPgogIDxyZWN0IHg9IjEyOC42MjYiIHk9IjQwIiB3aWR0aD0iNTA4LjgzMiIgaGVpZ2h0PSI0NDguOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDxyZWN0IHg9IjEyOC42MjYiIHk9IjQwIiB3aWR0aD0iNTA4LjgzMiIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTQwLjYyNiIgeT0iNTQiIGZvbnQtc2l6ZT0iMTIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSI0LjE5OTk5OTk5OTk5OTk5OSI+VE9DVE9VICjqsoDsgqwg7Iuc7KCQIC8g7IKs7JqpIOyLnOygkCkg7YyM7J28IOuwlOq/lOy5mOq4sCDqs7Xqsqkg66mU7Luk64uI7KaYPC90ZXh0Pgo8L2c+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJQUk9HIiBkYXRhLXRvPSJGSUxFX0EiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjEuIOqygOyCrCDsi5zsoJAgKENoZWNrKQpB7YyM7J28IOydveq4sCDqtoztlZwg7J6I64KYPyIgcG9pbnRzPSIyODcuNDc4NjY2NjY2NjY2NjQsMjUxLjUgMjg3LjQ3ODY2NjY2NjY2NjY0LDIxNS41IDMyNi4yODYsMjE1LjUgMzI2LjI4NiwxMzIuOSAyODQuMzkxMTY2NjY2NjY2NjYsMTMyLjkgMjg0LjM5MTE2NjY2NjY2NjY2LDEyMC45IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJGSUxFX0EiIGRhdGEtdG89IlBST0ciIGRhdGEtc3R5bGU9ImRvdHRlZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSLqsrDqs7w6IOq2jO2VnCBPSywg7Ya16rO8ISIgcG9pbnRzPSIyNDAuNTIwODMzMzMzMzMzMzQsMTIwLjkgMjQwLjUyMDgzMzMzMzMzMzM0LDEzMi45IDE5OC42MjYsMTMyLjkgMTk4LjYyNiwyMTUuNSAyMzcuNDMzMzMzMzMzMzMzMzQsMjE1LjUgMjM3LjQzMzMzMzMzMzMzMzM0LDI1MS41IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSI0IDQiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkhBQ0tFUiIgZGF0YS10bz0iRklMRV9CIiBkYXRhLXN0eWxlPSJkb3R0ZWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iMi4g7LCw64KY7J2YIOyLnOqwhOywqCAoUmFjZSBDb25kaXRpb24pIOuwnOyDnSEKQe2MjOydvOydhCDsgq3soJztlZjqs6AsIELtjIzsnbzroZwg7Jew6rKw65CY64qUIOqwgOynnCBB66W8IOunjOuTpiIgcG9pbnRzPSI0ODYuNjM1OTk5OTk5OTk5OTcsMjg4LjQgNDg2LjYzNTk5OTk5OTk5OTk3LDM4MyA0MDIuNjU2MTY2NjY2NjY2NjUsMzgzIDQwMi42NTYxNjY2NjY2NjY2NSw0MTkiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjQgNCIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iUFJPRyIgZGF0YS10bz0iRklMRV9CIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIzLiDsgqzsmqkg7Iuc7KCQIChVc2UpCuq2jO2VnCDtmZXsnbjtlojsnLzri4ggQe2MjOydvCDsl7TsnpAhIiBwb2ludHM9IjI2Mi40NTYsMjg4LjQgMjYyLjQ1NiwzODMgMzQ2LjQzNTgzMzMzMzMzMzMzLDM4MyAzNDYuNDM1ODMzMzMzMzMzMzMsNDE5IiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlBST0ciIGRhdGEtdG89IkZJTEVfQSIgZGF0YS1sYWJlbD0iMS4g6rKA7IKsIOyLnOygkCAoQ2hlY2spCkHtjIzsnbwg7J296riwIOq2jO2VnCDsnojrgpg/Ij4KICA8cmVjdCB4PSIyNjAuMjg2MDAwMDAwMDAwMDYiIHk9IjE2My45IiB3aWR0aD0iMTMxLjEwNDAwMDAwMDAwMDA0IiBoZWlnaHQ9IjQ0LjYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMzI1LjgzODAwMDAwMDAwMDEiIHk9IjE4Ni4yMDAwMDAwMDAwMDAwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSI+PHRzcGFuIHg9IjMyNS44MzgwMDAwMDAwMDAxIiBkeT0iLTMuMzAwMDAwMDAwMDAwMDAwNyI+MS4g6rKA7IKsIOyLnOygkCAoQ2hlY2spPC90c3Bhbj48dHNwYW4geD0iMzI1LjgzODAwMDAwMDAwMDEiIGR5PSIxNC4zIj5B7YyM7J28IOydveq4sCDqtoztlZwg7J6I64KYPzwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkZJTEVfQSIgZGF0YS10bz0iUFJPRyIgZGF0YS1sYWJlbD0i6rKw6rO8OiDqtoztlZwgT0ssIO2GteqzvCEiPgogIDxyZWN0IHg9IjE0MC42MjYiIHk9IjE3MS4wNSIgd2lkdGg9IjExNS42NjAwMDAwMDAwMDAwMSIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjE5OC40NTYwMDAwMDAwMDAwMiIgeT0iMTg2LjIwMDAwMDAwMDAwMDAyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij7qsrDqs7w6IOq2jO2VnCBPSywg7Ya16rO8ITwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJIQUNLRVIiIGRhdGEtdG89IkZJTEVfQiIgZGF0YS1sYWJlbD0iMi4g7LCw64KY7J2YIOyLnOqwhOywqCAoUmFjZSBDb25kaXRpb24pIOuwnOyDnSEKQe2MjOydvOydhCDsgq3soJztlZjqs6AsIELtjIzsnbzroZwg7Jew6rKw65CY64qUIOqwgOynnCBB66W8IOunjOuTpiI+CiAgPHJlY3QgeD0iMzQ3LjYzNjAwMDAwMDAwMDEiIHk9IjMzMS40IiB3aWR0aD0iMjc3LjgyMTk5OTk5OTk5OTk1IiBoZWlnaHQ9IjQ0LjYiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNDg2LjU0NyIgeT0iMzUzLjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSI0ODYuNTQ3IiBkeT0iLTMuMzAwMDAwMDAwMDAwMDAwNyI+Mi4g7LCw64KY7J2YIOyLnOqwhOywqCAoUmFjZSBDb25kaXRpb24pIOuwnOyDnSE8L3RzcGFuPjx0c3BhbiB4PSI0ODYuNTQ3IiBkeT0iMTQuMyI+Qe2MjOydvOydhCDsgq3soJztlZjqs6AsIELtjIzsnbzroZwg7Jew6rKw65CY64qUIOqwgOynnCBB66W8IOunjOuTpjwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IlBST0ciIGRhdGEtdG89IkZJTEVfQiIgZGF0YS1sYWJlbD0iMy4g7IKs7JqpIOyLnOygkCAoVXNlKQrqtoztlZwg7ZmV7J247ZaI7Jy864uIIEHtjIzsnbwg7Je07J6QISI+CiAgPHJlY3QgeD0iMTgwLjQ1NjAwMDAwMDAwMDA1IiB5PSIzMzEuNCIgd2lkdGg9IjE2My4xOCIgaGVpZ2h0PSI0NC42IiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjI2Mi4wNDYwMDAwMDAwMDAwNSIgeT0iMzUzLjciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiPjx0c3BhbiB4PSIyNjIuMDQ2MDAwMDAwMDAwMDUiIGR5PSItMy4zMDAwMDAwMDAwMDAwMDA3Ij4zLiDsgqzsmqkg7Iuc7KCQIChVc2UpPC90c3Bhbj48dHNwYW4geD0iMjYyLjA0NjAwMDAwMDAwMDA1IiBkeT0iMTQuMyI+6raM7ZWcIO2ZleyduO2WiOycvOuLiCBB7YyM7J28IOyXtOyekCE8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTm90ZSIgZGF0YS1sYWJlbD0iTm90ZSIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI2OC42MjYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI3NC4zMTMiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5Ob3RlPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJQUk9HIiBkYXRhLWxhYmVsPSLsoJXsg4Eg7ZSE66Gc6re4656oIPCfkrsiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTg3LjM4ODAwMDAwMDAwMDAzIiB5PSIyNTEuNSIgd2lkdGg9IjE1MC4xMzYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlMWY1ZmUiIHN0cm9rZT0iIzAyODhkMSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI2Mi40NTYiIHk9IjI2OS45NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7KCV7IOBIO2UhOuhnOq3uOueqCDwn5K7PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJGSUxFX0EiIGRhdGEtbGFiZWw9IuygleyDgSDtjIzsnbwgQSDwn5OEIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjE5Ni42NTA1MDAwMDAwMDAwMiIgeT0iODQiIHdpZHRoPSIxMzEuNjExIiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIyNjIuNDU2IiB5PSIxMDIuNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuygleyDgSDtjIzsnbwgQSDwn5OEPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJIQUNLRVIiIGRhdGEtbGFiZWw9Iu2VtOy7pOydmCDsiqTroIjrk5wg8J+ltyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI0MTEuNTY4IiB5PSIyNTEuNSIgd2lkdGg9IjE1MC4xMzYiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iNDg2LjYzNTk5OTk5OTk5OTk3IiB5PSIyNjkuOTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPu2VtOy7pOydmCDsiqTroIjrk5wg8J+ltzwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRklMRV9CIiBkYXRhLWxhYmVsPSLro6jtirgg6raM7ZWcIELtjIzsnbwg4pig77iPCuyYiDogL2V0Yy9wYXNzd2QiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjkwLjIxNTUiIHk9IjQxOSIgd2lkdGg9IjE2OC42NjEiIGhlaWdodD0iNTMuODAwMDAwMDAwMDAwMDA0IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMzc0LjU0NjAwMDAwMDAwMDA1IiB5PSI0NDUuOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMzc0LjU0NjAwMDAwMDAwMDA1IiBkeT0iLTMuOTAwMDAwMDAwMDAwMDAxMiI+66Oo7Yq4IOq2jO2VnCBC7YyM7J28IOKYoO+4jzwvdHNwYW4+PHRzcGFuIHg9IjM3NC41NDYwMDAwMDAwMDAwNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7JiIOiAvZXRjL3Bhc3N3ZDwvdHNwYW4+PC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

#### **III. \[본론 2] 시큐어 코딩: 취약한 코드 vs 원자적 연산(Atomic) 방어 전격 비교 (3단 표)**

개발자가 코드를 짤 때 범하는 \*\*'분리된 연산'\*\*의 실수와, 이를 막는 **'한 덩어리(원자적) 묶음'** 방어책을 대조하는 것이 핵심 출제 포인트입니다.

| **핵심 척도 (비교 잣대)**                    | **❌ 취약한 코드 (TOCTOU 발생)**                                                                                        | **🛡️ 방어 코드 (시큐어 코딩 적용)**                                                                   |
| :----------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| **자원에 대한 검사와 사용의 논리적 처리 흐름**         | **'검사와 사용이 분리되어 있음 (Non-Atomic)'.** 코드 라인 상 `if(접근 권한 확인)` 코드와 `file.open()` 코드가 각각 독립적인 명령어로 나뉘어 있어 찰나의 틈이 생김. | **'검사와 사용을 하나로 묶음 (Atomic)'.** 원자적(Atomic) 연산을 사용하여, 권한을 확인하는 즉시 중간에 아무도 끼어들지 못하게 자원을 열어버림. |
| **운영체제 스케줄링 (Context Switching) 관점** | 검사(Check) 명령어와 사용(Use) 명령어 사이에 OS가 CPU 제어권을 다른 프로세스(해커)에게 넘겨버릴 수 있음.                                            | 프로세스가 자원에 접근하는 순간 \*\*'Lock(잠금)이나 Mutex(상호배제)'\*\*를 걸어버려, 작업이 끝날 때까지 CPU가 해커에게 권한을 안 줌.     |
| **대표적인 악용 기법 (해커의 무기)**              | 리눅스의 **'심볼릭 링크(Symbolic Link, 바로가기)'** 공격. 진짜 파일을 지우고 시스템 중요 파일로 링크를 걸어버림.                                      | 심볼릭 링크 생성을 차단하거나, 파일을 열 때 절대 경로와 파일의 고유 값(Inode)을 다시 한번 검증함.                                |
| **개발자 방어 대책 (시큐어 코딩 🚨)**            | `access()` 함수로 먼저 검사하고, 그다음 `open()` 함수로 파일을 여는 안일한 코딩.                                                         | `access()`를 쓰지 말고 \*\*그냥 바로 `open()`을 때린 후 에러 예외 처리(Exception)\*\*로 권한 없음을 튕겨내는 방식이 훨씬 안전함. |

#### **IV. \[결론/제언] 마이크로서비스(MSA)와 분산 환경에서의 TOCTOU 위험성 증대**

* **(키워드 위주 2줄 마무리)** "과거 단일 PC의 파일 시스템에서 주로 발생하던 TOCTOU 취약점은, 오늘날 클라우드 및 마이크로서비스(MSA) 환경에서 수많은 분산 API가 동시에 자원을 호출하면서 **API 단위의 '비즈니스 로직 Race Condition'으로 진화하고 있으므로, 분산 락(Distributed Lock) 등 아키텍처 수준의 동시성 제어가 필수적입니다.**"
