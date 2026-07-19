
---

#### 답안 전개 스토리 (핵심 압축)

> "데이터베이스가 트랜잭션을 처리할 때 '언제 버퍼의 더러운 페이지를 디스크에 내리는가'와 '커밋 시 반드시 디스크에 써야 하는가'라는 두 가지 정책 선택이 회복 알고리즘 전체의 설계를 결정한다. **STEAL·FORCE는 이 두 축의 이진 선택**이다. **STEAL(훔치기)**: 미커밋 트랜잭션의 Dirty Page를 다른 트랜잭션이 버퍼가 필요할 때 디스크에 내릴 수 있는가 — STEAL이면 버퍼 효율이 높지만 미커밋 데이터가 디스크에 내려갈 수 있어 **Undo가 필요**해진다. **FORCE(강제)**: 커밋 시 해당 트랜잭션의 모든 Dirty Page를 반드시 디스크에 기록해야 하는가 — No-Force이면 커밋 후에도 데이터가 버퍼에만 있을 수 있어 장애 시 **Redo가 필요**해진다. **현대 RDBMS(Oracle·PostgreSQL·MySQL InnoDB)는 모두 Steal·No-Force 조합을 선택한다** — 버퍼 효율(Steal)과 커밋 성능(No-Force)을 동시에 극대화하는 대신 Undo·Redo가 모두 필요해지며, 이 Undo·Redo를 안전하게 수행하기 위한 전제가 바로 **WAL(Write-Ahead Logging)** 이다 — '페이지를 디스크에 쓰기 전에 반드시 로그를 먼저 써야 한다'는 단 하나의 황금률이 회복 가능성 전체를 보장"

---

#### 핵심 내용 (암기용)

**4가지 정책 조합 매핑**

|정책 조합|Undo 필요|Redo 필요|특징|
|---|---|---|---|
|**Steal + No-Force**|✅ 필요|✅ 필요|현대 RDBMS 표준·최고 성능|
|**Steal + Force**|✅ 필요|❌ 불필요|커밋 I/O 비용 높음|
|**No-Steal + No-Force**|❌ 불필요|✅ 필요|버퍼 부족 위험|
|**No-Steal + Force**|❌ 불필요|❌ 불필요|구현 단순·성능 최저|

---

|**핵심 척도**|**📊 STEAL 정책 🚨**|**🔑 FORCE 정책 🚨**|**🏁 WAL 프로토콜 💯**|
|---|---|---|---|
|**정의**|**미커밋 Dirty Page를 버퍼 부족 시 디스크에 내릴 수 있는가** / STEAL=가능 / No-Steal=불가|**커밋 시 해당 트랜잭션 Dirty Page를 즉시 디스크에 강제 기록하는가** / Force=강제 / No-Force=선택|**"로그 먼저·페이지 나중"** / 페이지 디스크 기록 전 반드시 해당 로그 레코드 먼저 디스크에 기록|
|**회복 영향 🚨**|**STEAL → Undo 필요** / 미커밋 데이터가 디스크에 있을 수 있음 / 장애 시 롤백 불가능하면 ACID 원자성 위반 🚨|**No-Force → Redo 필요** / 커밋 데이터가 버퍼에만 있을 수 있음 / 장애 시 커밋 데이터 유실 → ACID 지속성 위반 🚨|**WAL 규칙 1**: 페이지 디스크 쓰기 전 Undo 로그 먼저 (STEAL 대응) / **WAL 규칙 2**: 커밋 전 모든 Redo 로그 먼저 (No-Force 대응)|
|**성능·설계 💯**|**STEAL 장점**: 버퍼 효율 극대화 / 버퍼 부족 시 미커밋 페이지도 희생 가능 / 버퍼 크기 제약 극복|**No-Force 장점**: 커밋 시 I/O 최소화 / 그룹 커밋(Group Commit)으로 로그 I/O 일괄 처리 / 높은 TPS 달성|**WAL 효과**: 페이지(랜덤 I/O) 대신 로그(순차 I/O) 먼저 → I/O 비용 최소화 / LSN으로 로그·페이지 동기화 / ARIES 3단계 회복의 전제|

---

#### 도식화

```
[STEAL·No-Force 조합의 위험과 WAL 해결]

①STEAL 위험 시나리오:
  T1(미커밋): 페이지P 수정 (버퍼에 Dirty)
  T2: 버퍼 필요 → P를 디스크에 강제 방출
       ↓
  장애 발생 → T1은 커밋 안 됨
  그런데 P는 이미 디스크에! → Undo 필요 🚨
  WAL 규칙1: P 디스크 쓰기 전 Undo 로그 먼저 기록
  → 장애 시 로그로 역산하여 P 원복 ✅

②No-Force 위험 시나리오:
  T2 커밋 완료 → 그러나 Dirty Page가 버퍼에만 존재
       ↓
  장애 발생 → 버퍼 소멸 → 커밋 데이터 유실! 🚨
  WAL 규칙2: 커밋 전 모든 Redo 로그 디스크에 기록
  → 장애 시 로그로 재실행하여 복원 ✅

[WAL + STEAL·No-Force 전체 흐름]

트랜잭션 실행
  ↓
페이지 수정 (버퍼)
  ↓ WAL 규칙1 적용
로그 레코드 디스크 기록 (LSN 부여)
  ↓
커밋 요청
  ↓ WAL 규칙2 적용
Commit 로그 레코드 디스크 기록 (fsync)
  ↓
커밋 완료 응답 (Dirty Page는 버퍼에 남아도 OK)
  ↓
백그라운드 체크포인트
  → 버퍼 Dirty Page 디스크에 비동기 기록

장애 발생 시:
  ARIES 3단계 (Analysis→Redo→Undo)로 완전 복구 ✅
```

---

**(제언)** "STEAL·No-Force 조합은 버퍼 효율과 커밋 성능을 동시에 극대화하는 최선의 정책이지만, Undo·Redo가 모두 필요해진다는 대가를 치릅니다. WAL은 이 대가를 '순차 로그 I/O'라는 저비용으로 해결하는 황금 열쇠이며, **앞서 다룬 ARIES의 LSN·ATT·DPT가 모두 WAL 위에서 동작하고, 분산 DB·클라우드 환경에서는 WAL 로그를 Raft 합의 프로토콜과 결합해 복수 노드에 동기 복제함으로써 단일 장애점 없는 고가용성 회복 체계를 구현해야 합니다.**"

#### **1. 답안 전개 스토리 (핵심 압축)**

> "메모리(버퍼 풀)가 꽉 찼을 때 **'커밋 안 된 가짜 데이터를 디스크에 마음대로 쓸지(STEAL)'와 '커밋되는 순간 디스크에 무조건 쥐어짤지(FORCE)'를 결정하는 메모리-스토리지Persistence 정책의 사분면**이다. 성능을 극대화하려면 메모리 관리자가 자유로워야 한다. 그래서 현대 DBMS는 **'STEAL'** 정책(아직 안 끝난 트랜잭션의 더티 페이지라도 메모리가 모자라면 디스크에 쫓아내어 버림)과 **'NO-FORCE'** 정책(커밋되었다고 디스크에 굳이 바로 안 쓰고 나중에 몰아 씀)을 채택한다. 이 **\[STEAL + NO-FORCE]** 조합이 속도는 제일 빠르지만, 복구 입장에선 지옥이다. 커밋 안 된 놈이 디스크에 기어들어갔으니 취소해야 하고(**UNDO 필요**), 커밋된 놈이 디스크에 안 씌졌으니 다시 써야 한다(**REDO 필요**). 이 개차반 상태를 질서정연하게 사수하기 위해, 실제 데이터를 쓰기 전에 로그부터 디스크에 영구 배출하는 **'미리 쓰기 로깅(WAL)'** 프로토콜이 물리학적 철칙으로 강제되는 이유다."

#### **2. 실제 답안에 쓸 핵심 내용 (암기용)**

```
```

![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5MTQuNTEzOTk5OTk5OTk5OSA1NTUuMzcyMDAwMDAwMDAwMSIgd2lkdGg9IjkxNC41MTM5OTk5OTk5OTk5IiBoZWlnaHQ9IjU1NS4zNzIwMDAwMDAwMDAxIiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPGcgY2xhc3M9InN1YmdyYXBoIiBkYXRhLWlkPSJfX19CdWZmZXJfUG9saWN5X19fIiBkYXRhLWxhYmVsPSLrsoTtjbwg6rSA66asIOygleyxhSAoQnVmZmVyIFBvbGljeSkg66ek7Yq466at7Iqk7JmAIOuzteq1rCDrp6TtlZEiPgogIDxyZWN0IHg9IjQwIiB5PSI0MCIgd2lkdGg9IjgzNC41MTM5OTk5OTk5OTk5IiBoZWlnaHQ9IjQ3NS4zNzIiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX2dyb3VwLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8cmVjdCB4PSI0MCIgeT0iNDAiIHdpZHRoPSI4MzQuNTEzOTk5OTk5OTk5OSIgaGVpZ2h0PSIyOCIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fZ3JvdXAtaGRyKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTIiIHk9IjU0IiBmb250LXNpemU9IjEyIiBmb250LXdlaWdodD0iNjAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iNC4xOTk5OTk5OTk5OTk5OTkiPuuyhO2NvCDqtIDrpqwg7KCV7LGFIChCdWZmZXIgUG9saWN5KSDrp6Ttirjrpq3siqTsmYAg67O16rWsIOunpO2VkTwvdGV4dD4KPC9nPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iU1RFQUxfUCIgZGF0YS10bz0iUkVRX1VORE8iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjEuIFNURUFMIO2XiOyaqSDwn5qoIiBwb2ludHM9IjI0MS45MzM1ODMzMzMzMzMzMywyNzYuMDQzMzMzMzMzMzMzMyAyNDEuOTMzNTgzMzMzMzMzMywzMjYuNDUxOTk5OTk5OTk5OTQgMTc1LjUyOCwzMjYuNDUxOTk5OTk5OTk5OTQgMTc1LjUyOCw0MzguMTYyIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJTVEVBTF9QIiBkYXRhLXRvPSJOT19VTkRPIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIyLiBOTy1TVEVBTCDqsbDrtoAiIHBvaW50cz0iMzE4Ljc1MDkxNjY2NjY2NjYsMjc2LjA0MzMzMzMzMzMzMzMgMzE4Ljc1MDkxNjY2NjY2NjYsMzI2LjQ1MTk5OTk5OTk5OTk0IDM4NS4xNTY1MDAwMDAwMDAwNSwzMjYuNDUxOTk5OTk5OTk5OTQgMzg1LjE1NjUwMDAwMDAwMDA1LDQzOC4xNjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkZPUkNFX1AiIGRhdGEtdG89IlJFUV9SRURPIiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIxLiBOTy1GT1JDRSDtl4jsmqkg8J+aqCIgcG9pbnRzPSI2NTAuNzIwNTgzMzMzMzMzMywyODguMzkzMzMzMzMzMzMzNCA2NTAuNzIwNTgzMzMzMzMzMywzNDEuMjcyIDU4Ni43ODUsMzQxLjI3MiA1ODYuNzg1LDQzOC4xNjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkZPUkNFX1AiIGRhdGEtdG89Ik5PX1JFRE8iIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjIuIEZPUkNFIOqwleygnCIgcG9pbnRzPSI3MzIuNDc3OTE2NjY2NjY2NiwyODguMzkzMzMzMzMzMzMzMyA3MzIuNDc3OTE2NjY2NjY2NiwzNDEuMjcyIDc5Ni40MTM0OTk5OTk5OTk5LDM0MS4yNzIgNzk2LjQxMzQ5OTk5OTk5OTksNDM4LjE2MiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJTVEVBTF9QIiBkYXRhLXRvPSJSRVFfVU5ETyIgZGF0YS1sYWJlbD0iMS4gU1RFQUwg7ZeI7JqpIPCfmqgiPgogIDxyZWN0IHg9IjEyNS41Mjc5OTk5OTk5OTk5OSIgeT0iMzU3LjQ1MTk5OTk5OTk5OTk0IiB3aWR0aD0iOTkuMDI4MDAwMDAwMDAwMDIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxNzUuMDQyIiB5PSIzNzIuNjAxOTk5OTk5OTk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+MS4gU1RFQUwg7ZeI7JqpIPCfmqg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iU1RFQUxfUCIgZGF0YS10bz0iTk9fVU5ETyIgZGF0YS1sYWJlbD0iMi4gTk8tU1RFQUwg6rGw67aAIj4KICA8cmVjdCB4PSIzMzEuNjU2NTAwMDAwMDAwMDUiIHk9IjM1Ny40NTE5OTk5OTk5OTk5NCIgd2lkdGg9IjEwNi4xNTYiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIzODQuNzM0NSIgeT0iMzcyLjYwMTk5OTk5OTk5OTkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjIuIE5PLVNURUFMIOqxsOu2gDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJGT1JDRV9QIiBkYXRhLXRvPSJSRVFfUkVETyIgZGF0YS1sYWJlbD0iMS4gTk8tRk9SQ0Ug7ZeI7JqpIPCfmqgiPgogIDxyZWN0IHg9IjUyOC4yODUwMDAwMDAwMDAxIiB5PSIzNzIuMjcyIiB3aWR0aD0iMTE2LjI1NDAwMDAwMDAwMDAyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iNTg2LjQxMiIgeT0iMzg3LjQyMTk5OTk5OTk5OTk3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij4xLiBOTy1GT1JDRSDtl4jsmqkg8J+aqDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0iZWRnZS1sYWJlbCIgZGF0YS1mcm9tPSJGT1JDRV9QIiBkYXRhLXRvPSJOT19SRURPIiBkYXRhLWxhYmVsPSIyLiBGT1JDRSDqsJXsoJwiPgogIDxyZWN0IHg9Ijc1MS45MTM0OTk5OTk5OTk5IiB5PSIzNzIuMjcyIiB3aWR0aD0iODguOTMiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI3OTYuMzc4NDk5OTk5OTk5OSIgeT0iMzg3LjQyMTk5OTk5OTk5OTk3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij4yLiBGT1JDRSDqsJXsoJw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlNURUFMX1AiIGRhdGEtbGFiZWw9IuKcqCBTVEVBTCAvIE5PLVNURUFMIOKcqArsu6TrsIsg7KCEIOuUlOyKpO2BrCDrsKnstpwg7ZeI7JqpPyIgZGF0YS1zaGFwZT0iZGlhbW9uZCI+CiAgPHBvbHlnb24gcG9pbnRzPSIyODAuMzQyMjUsODQgMzk1LjU2ODI0OTk5OTk5OTksMTk5LjIyNTk5OTk5OTk5OTk3IDI4MC4zNDIyNSwzMTQuNDUxOTk5OTk5OTk5OTQgMTY1LjExNjI1LDE5OS4yMjU5OTk5OTk5OTk5NyIgZmlsbD0iI2ZmZjNlMCIgc3Ryb2tlPSIjZjU3YzAwIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMjgwLjM0MjI1IiB5PSIxOTkuMjI1OTk5OTk5OTk5OTciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjI4MC4zNDIyNSIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuKcqCBTVEVBTCAvIE5PLVNURUFMIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjI4MC4zNDIyNSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7Luk67CLIOyghCDrlJTsiqTtgawg67Cp7LacIO2XiOyaqT88L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRk9SQ0VfUCIgZGF0YS1sYWJlbD0i4pyoIEZPUkNFIC8gTk8tRk9SQ0Ug4pyoCuy7pOuwiyDsponsi5wg65SU7Iqk7YGsIOqwleygnCDsk7DquLA/IiBkYXRhLXNoYXBlPSJkaWFtb25kIj4KICA8cG9seWdvbiBwb2ludHM9IjY5MS41OTkyNDk5OTk5OTk5LDg0IDgxNC4yMzUyNDk5OTk5OTk4LDIwNi42MzYgNjkxLjU5OTI0OTk5OTk5OTksMzI5LjI3MiA1NjguOTYzMjQ5OTk5OTk5OSwyMDYuNjM2IiBmaWxsPSIjZmZmM2UwIiBzdHJva2U9IiNmNTdjMDAiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSI2OTEuNTk5MjQ5OTk5OTk5OSIgeT0iMjA2LjYzNiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iNjkxLjU5OTI0OTk5OTk5OTkiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7inKggRk9SQ0UgLyBOTy1GT1JDRSDinKg8L3RzcGFuPjx0c3BhbiB4PSI2OTEuNTk5MjQ5OTk5OTk5OSIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7Luk67CLIOymieyLnCDrlJTsiqTtgawg6rCV7KCcIOyTsOq4sD88L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iUkVRX1VORE8iIGRhdGEtbGFiZWw9IuKcqCBVTkRPIOuzteq1rCDsl7DsgrAg7ZWE7IiY7ZmUIPCfkq8g4pyoCuy7pOuwiyDslYgg65CcIOyYpOyXvCDrjbDsnbTthLAg7JuQ67O17JqpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjU2IiB5PSI0MzguMTYyIiB3aWR0aD0iMjM5LjA1NTk5OTk5OTk5OTk4IiBoZWlnaHQ9IjUzLjgwMDAwMDAwMDAwMDAwNCIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZmZlYmVlIiBzdHJva2U9IiNkMzJmMmYiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjE3NS41MjgiIHk9IjQ2NS4wNjE5OTk5OTk5OTk5NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIj48dHNwYW4geD0iMTc1LjUyOCIgZHk9Ii0zLjkwMDAwMDAwMDAwMDAwMTIiPuKcqCBVTkRPIOuzteq1rCDsl7DsgrAg7ZWE7IiY7ZmUIPCfkq8g4pyoPC90c3Bhbj48dHNwYW4geD0iMTc1LjUyOCIgZHk9IjE2LjkwMDAwMDAwMDAwMDAwMiI+7Luk67CLIOyViCDrkJwg7Jik7Je8IOuNsOydtO2EsCDsm5Drs7Xsmqk8L3RzcGFuPjwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iTk9fVU5ETyIgZGF0YS1sYWJlbD0iVU5ETyDrtojtlYTsmpQiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMzIzLjA1NjAwMDAwMDAwMDA0IiB5PSI0MzguMTYyIiB3aWR0aD0iMTI0LjIwMDk5OTk5OTk5OTk4IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMzg1LjE1NjUwMDAwMDAwMDA1IiB5PSI0NTYuNjExOTk5OTk5OTk5OTciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlVORE8g67aI7ZWE7JqUPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJSRVFfUkVETyIgZGF0YS1sYWJlbD0i4pyoIFJFRE8g67O16rWsIOyXsOyCsCDtlYTsiJjtmZQg8J+SryDinKgK7Luk67CL65CcIOycoOyLpCDrjbDsnbTthLAg7J6s7Iuk7ZaJ7JqpIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjQ2Ny4yNTY5OTk5OTk5OTk5NSIgeT0iNDM4LjE2MiIgd2lkdGg9IjIzOS4wNTU5OTk5OTk5OTk5OCIgaGVpZ2h0PSI1My44MDAwMDAwMDAwMDAwMDQiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2UxZjVmZSIgc3Ryb2tlPSIjMDI4OGQxIiBzdHJva2Utd2lkdGg9IjJweCIgLz4KICA8dGV4dCB4PSI1ODYuNzg1IiB5PSI0NjUuMDYxOTk5OTk5OTk5OTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSI+PHRzcGFuIHg9IjU4Ni43ODUiIGR5PSItMy45MDAwMDAwMDAwMDAwMDEyIj7inKggUkVETyDrs7Xqtawg7Jew7IKwIO2VhOyImO2ZlCDwn5KvIOKcqDwvdHNwYW4+PHRzcGFuIHg9IjU4Ni43ODUiIGR5PSIxNi45MDAwMDAwMDAwMDAwMDIiPuy7pOuwi+uQnCDsnKDsi6Qg642w7J207YSwIOyerOyLpO2WieyaqTwvdHNwYW4+PC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJOT19SRURPIiBkYXRhLWxhYmVsPSJSRURPIOu2iO2VhOyalCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3MzQuMzEyOTk5OTk5OTk5OSIgeT0iNDM4LjE2MiIgd2lkdGg9IjEyNC4yMDA5OTk5OTk5OTk5OCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9Ijc5Ni40MTM0OTk5OTk5OTk5IiB5PSI0NTYuNjExOTk5OTk5OTk5OTciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlJFRE8g67aI7ZWE7JqUPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

| **핵심 척도**       | **📊 STEAL (버퍼 대피) vs NO-STEAL**                                                                | **🔑 FORCE (커밋 즉시 쓰기) vs NO-FORCE 🚨**                                                          | **🏁 WAL (Write-Ahead Logging) 연계 💯**                                                                           |
| :-------------- | :---------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| **정책 정의**       | **- STEAL 🚨**: 커밋 전이라도 메모리 공간 확보를 위해 dirty page를 디스크에 내보냄. **- NO-STEAL**: 커밋 전엔 디스크 방출 절대 금지. | **- FORCE**: 트랜잭션 커밋 완료 시점에 변경 페이지들을 디스크에 100% 씀. **- NO-FORCE 🚨**: 커밋 시점에 디스크 쓰지 않고 버퍼 풀에 놔둠. | 실제 데이터 페이지보다 변경 로그(Redo/Undo Log)를 디스크에 먼저 영구 기록(Flush)해야 하는 규칙.                                                 |
| **복구 연산 요구 🚨** | **\[STEAL]** ➔ **UNDO 필요 💯** (가짜 데이터 취소). **\[NO-STEAL]** ➔ UNDO 불필요 (디스크 오염 없음).              | **\[NO-FORCE]** ➔ **REDO 필요 💯** (유실 데이터 재실행). **\[FORCE]** ➔ REDO 불필요 (디스크에 이미 다 쓰임).          | **\[STEAL 정책의 WAL 필수 조건 🚨]** STEAL에 의해 더러워진 페이지를 디스크에 내보내기 전, **반드시 해당 로그가 먼저 디스크에 가 있어야만** 장애 시 원복(UNDO)이 가능함. |

* **(제언)** "현대 대용량 RDBMS의 엔진 표준은 성능이 극대화되는 \*\*\[STEAL / NO-FORCE]\*\*를 뼈대로 합니다. **이 최적의 성능을 데이터 유실 없이 누리려면, 트랜잭션 커밋 로그를 디스크에 기록할 때 비동기 그룹 커밋(Group Commit) 기술을 적용해 로그 디스크 I/O 횟수를 최소화하는 튜닝을 병행해야 합니다.**"
