### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 SaaS 시대에 새로운 보안 관문이 필요한가)
Ⅱ. CASB 핵심 구조 및 4대 기능
Ⅲ. 배포 모델 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 **"앞서 다룬 공공 SaaS 거버넌스·CSAP 3등급제가 '클라우드 도입의 제도적 기준'이라면, CASB(Cloud Access Security Broker)는 직원들이 Salesforce·Microsoft 365·Slack 같은 수백 개의 SaaS를 사용할 때 기업 데이터가 어디로 흘러가는지 가시성을 확보하고 정책을 집행하는 클라우드 보안 관문이다 — 전통적 방화벽·DLP가 온프레미스 경계를 지킨다면 CASB는 경계가 사라진 SaaS 환경에서 앞서 다룬 제로트러스트의 '절대 신뢰하지 말고 항상 검증' 원칙을 클라우드 접근 계층에서 구현하는 핵심 도구이며, Gartner가 정의한 CASB 4대 기둥(가시성·컴플라이언스·데이터 보안·위협 보호)이 전사 데이터 유출 방지의 기술적 기반"**이라는 한 줄로 시작하면 전체 맥락이 드러납니다.
\
![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDQ2LjU2OSAyNzAuMSIgd2lkdGg9IjEwNDYuNTY5IiBoZWlnaHQ9IjI3MC4xIiBzdHlsZT0iLS1iZzojRkZGRkZGOy0tZmc6IzNCM0IzQjstLWxpbmU6IzNCM0IzQjstLWFjY2VudDojMDA1RkI4Oy0tbXV0ZWQ6IzNCM0IzQkNDOy0tc3VyZmFjZTojRjhGOEY4Oy0tYm9yZGVyOiMzQjNCM0I7YmFja2dyb3VuZDp2YXIoLS1iZykiPgo8c3R5bGU+CiAgQGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SW50ZXI6d2dodEA0MDA7NTAwOzYwMDs3MDAmYW1wO2Rpc3BsYXk9c3dhcCcpOwogIHRleHQgeyBmb250LWZhbWlseTogJ0ludGVyJywgc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyB9CiAgc3ZnIHsKICAgIC8qIERlcml2ZWQgZnJvbSAtLWJnIGFuZCAtLWZnIChvdmVycmlkYWJsZSB2aWEgLS1saW5lLCAtLWFjY2VudCwgZXRjLikgKi8KICAgIC0tX3RleHQ6ICAgICAgICAgIHZhcigtLWZnKTsKICAgIC0tX3RleHQtc2VjOiAgICAgIHZhcigtLW11dGVkLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDYwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV90ZXh0LW11dGVkOiAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA0MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1mYWludDogICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyNSUsIHZhcigtLWJnKSk7CiAgICAtLV9saW5lOiAgICAgICAgICB2YXIoLS1saW5lLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9hcnJvdzogICAgICAgICB2YXIoLS1hY2NlbnQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgODUlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtZmlsbDogICAgIHZhcigtLXN1cmZhY2UsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMyUsIHZhcigtLWJnKSkpOwogICAgLS1fbm9kZS1zdHJva2U6ICAgdmFyKC0tYm9yZGVyLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDIwJSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ncm91cC1maWxsOiAgICB2YXIoLS1iZyk7CiAgICAtLV9ncm91cC1oZHI6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDUlLCB2YXIoLS1iZykpOwogICAgLS1faW5uZXItc3Ryb2tlOiAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMiUsIHZhcigtLWJnKSk7CiAgICAtLV9rZXktYmFkZ2U6ICAgICBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDEwJSwgdmFyKC0tYmcpKTsKICB9Cjwvc3R5bGU+CjxkZWZzPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iNyIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8iPgogICAgPHBvbHlnb24gcG9pbnRzPSIwIDAsIDggMi41LCAwIDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgogIDxtYXJrZXIgaWQ9ImFycm93aGVhZC1zdGFydCIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNSIgcmVmWD0iMSIgcmVmWT0iMi41IiBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSI+CiAgICA8cG9seWdvbiBwb2ludHM9IjggMCwgMCAyLjUsIDggNSIgZmlsbD0idmFyKC0tX2Fycm93KSIgc3Ryb2tlPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2Utd2lkdGg9IjAuNzUiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIC8+CiAgPC9tYXJrZXI+CjwvZGVmcz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkNsaWVudCIgZGF0YS10bz0iRlAiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IkZvcndhcmQgUHJveHkgOiBQQUMvQWdlbnQg7ISk7LmYIiBwb2ludHM9IjE4MC4yNzYsNzYuOSAxODAuMjc2LDE5My4yIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJCWU9EIiBkYXRhLXRvPSJSUCIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iUmV2ZXJzZSBQcm94eSA6IElkUCBTQU1ML09JREMg7Jew64+ZIiBwb2ludHM9IjQ5NS4xMjY1LDc2LjkgNDk1LjEyNjUsMTkzLjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkNsb3VkIiBkYXRhLXRvPSJBUEkiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJ0cnVlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iQVBJIE1vZGUgOiBPQXV0aC9SRVNUIEFQSSDsl7Drj5kiIHBvaW50cz0iODM4LjEzNSw3Ni45IDgzOC4xMzUsMTkzLjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgbWFya2VyLXN0YXJ0PSJ1cmwoI2Fycm93aGVhZC1zdGFydCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkNsaWVudCIgZGF0YS10bz0iRlAiIGRhdGEtbGFiZWw9IkZvcndhcmQgUHJveHkgOiBQQUMvQWdlbnQg7ISk7LmYIj4KICA8cmVjdCB4PSI5My4yNzYwMDAwMDAwMDAwNCIgeT0iMTE5LjkiIHdpZHRoPSIxNzMuODcyIiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iMTgwLjIxMjAwMDAwMDAwMDA1IiB5PSIxMzUuMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPkZvcndhcmQgUHJveHkgOiBQQUMvQWdlbnQg7ISk7LmYPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkJZT0QiIGRhdGEtdG89IlJQIiBkYXRhLWxhYmVsPSJSZXZlcnNlIFByb3h5IDogSWRQIFNBTUwvT0lEQyDsl7Drj5kiPgogIDxyZWN0IHg9IjM5Ni42MjY1IiB5PSIxMTkuOSIgd2lkdGg9IjE5Ni40NDQiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSI0OTQuODQ4NSIgeT0iMTM1LjA1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5SZXZlcnNlIFByb3h5IDogSWRQIFNBTUwvT0lEQyDsl7Drj5k8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQ2xvdWQiIGRhdGEtdG89IkFQSSIgZGF0YS1sYWJlbD0iQVBJIE1vZGUgOiBPQXV0aC9SRVNUIEFQSSDsl7Drj5kiPgogIDxyZWN0IHg9Ijc1MS42MzUiIHk9IjExOS45IiB3aWR0aD0iMTcyLjY4Mzk5OTk5OTk5OTk3IiBoZWlnaHQ9IjMwLjMiIHJ4PSIyIiByeT0iMiIgZmlsbD0idmFyKC0tYmcpIiBzdHJva2U9InZhcigtLV9pbm5lci1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjEiIC8+CiAgPHRleHQgeD0iODM3Ljk3NyIgeT0iMTM1LjA1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij5BUEkgTW9kZSA6IE9BdXRoL1JFU1QgQVBJIOyXsOuPmTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ2xpZW50IiBkYXRhLWxhYmVsPSLsgqzsmqnsnpAg64uo66eQIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjEyMS4xMzk1IiB5PSI0MCIgd2lkdGg9IjExOC4yNzMiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9InZhcigtLV9ub2RlLWZpbGwpIiBzdHJva2U9InZhcigtLV9ub2RlLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMC43NSIgLz4KICA8dGV4dCB4PSIxODAuMjc2IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7IKs7Jqp7J6QIOuLqOunkDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iRlAiIGRhdGEtbGFiZWw9IkZvcndhcmQgUHJveHkgOiDqtIDrpqwg64uo66eQIOyduOudvOyduCDqsJDsi5wiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDAiIHk9IjE5My4yIiB3aWR0aD0iMjgwLjU1MiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0iI2ZmZWJlZSIgc3Ryb2tlPSIjZDMyZjJmIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iMTgwLjI3NiIgeT0iMjExLjY0OTk5OTk5OTk5OTk4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5Gb3J3YXJkIFByb3h5IDog6rSA66asIOuLqOunkCDsnbjrnbzsnbgg6rCQ7IucPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJCWU9EIiBkYXRhLWxhYmVsPSJCWU9EIOqwnOyduCDri6jrp5AiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iNDI0LjUwNDUiIHk9IjQwIiB3aWR0aD0iMTQxLjI0NCIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQ5NS4xMjY1IiB5PSI1OC40NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+QllPRCDqsJzsnbgg64uo66eQPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJSUCIgZGF0YS1sYWJlbD0iUmV2ZXJzZSBQcm94eSA6IOu5hOq0gOumrCDri6jrp5Ag6rKM7J207Yq47Juo7J20IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM0OC41NTIiIHk9IjE5My4yIiB3aWR0aD0iMjkzLjE0OSIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjQ5NS4xMjY1IiB5PSIyMTEuNjQ5OTk5OTk5OTk5OTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPlJldmVyc2UgUHJveHkgOiDruYTqtIDrpqwg64uo66eQIOqyjOydtO2KuOybqOydtDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQ2xvdWQiIGRhdGEtbGFiZWw9IuyZuOu2gCDtgbTrnbzsmrDrk5wgU2FhUyIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSI3NTQuMTc1IiB5PSI0MCIgd2lkdGg9IjE2Ny45MiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjgzOC4xMzUiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7smbjrtoAg7YG065287Jqw65OcIFNhYVM8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IkFQSSIgZGF0YS1sYWJlbD0iQVBJIE1vZGUgOiDsoIDsnqUg642w7J207YSwIOyVhOybg+yYpOu4jOuwtOuTnCDsoJXrsIAg7KeE64uoIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjY2OS43MDEiIHk9IjE5My4yIiB3aWR0aD0iMzM2Ljg2Nzk5OTk5OTk5OTk0IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSIjZThmNWU5IiBzdHJva2U9IiMzODhlM2MiIHN0cm9rZS13aWR0aD0iMnB4IiAvPgogIDx0ZXh0IHg9IjgzOC4xMzUiIHk9IjIxMS42NDk5OTk5OTk5OTk5OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+QVBJIE1vZGUgOiDsoIDsnqUg642w7J207YSwIOyVhOybg+yYpOu4jOuwtOuTnCDsoJXrsIAg7KeE64uoPC90ZXh0Pgo8L2c+Cjwvc3ZnPg== "Mermaid diagram")

***

#### Ⅱ. CASB 핵심 구조 및 4대 기능

**가. CASB 4대 기능(Gartner 정의)**

| 기능                            | 내용                           | 핵심 키워드                                               |
| :---------------------------- | :--------------------------- | :--------------------------------------------------- |
| **가시성 (Visibility)**          | 기업 내 모든 클라우드 서비스 사용 현황 탐지·분류 | Shadow IT 탐지 / 앱별 위험도 평가 / 사용자·데이터 흐름 가시화            |
| **컴플라이언스 (Compliance)**       | 클라우드 사용이 법령·정책을 준수하는지 검증     | 앞서 다룬 **CSAP·개인정보보호법·GDPR** 준수 / 감사 로그               |
| **데이터 보안 (Data Security)**    | 클라우드로 이동하는 데이터의 유출 방지        | DLP 정책 / 암호화 / 토큰화 / 앞서 다룬 **LINDDUN Disclosure** 방어 |
| **위협 보호 (Threat Protection)** | 클라우드 기반 악성 행위·계정 탈취 탐지       | 앞서 다룬 **UEBA** 연계 / 인포스틸러·크리덴셜 스터핑 대응                |

***

**나. CASB 4대 기능 핵심 비교**

| **핵심 척도**   | **📊 가시성·컴플라이언스 🚨**                                                                                               | **🔑 데이터 보안 🚨**                                                                                                 | **🏁 위협 보호 💯**                                                                                                          |
| :---------- | :----------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- |
| **핵심 기능**   | **Shadow IT 탐지**: 비승인 SaaS 앱 자동 탐지·위험도 분류 / **클라우드 앱 카탈로그**: 수만 개 SaaS 위험 점수화 / **사용 현황 리포트**: 부서·사용자별 클라우드 사용 가시화 | **클라우드 DLP**: 중요 데이터(개인정보·기밀문서) 클라우드 업로드 차단 / **암호화·토큰화**: 클라우드 저장 데이터 암호화 키 기업 보유 / **공유 제어**: 외부 공유·다운로드 정책 적용 | **UEBA 연계**: 비정상 접근·대량 다운로드·불가능 여행 탐지 / **계정 탈취 탐지**: 앞서 다룬 **인포스틸러·크리덴셜 스터핑** 피해 세션 탐지 / **멀웨어 탐지**: 클라우드 저장소 내 악성파일 스캔 |
| **대표 시나리오** | 마케팅팀이 개인 Dropbox에 고객 DB 업로드 → Shadow IT 탐지·차단 🚨 / 규정 위반 앱 사용 감사 로그 자동 기록                                          | 개발자가 GitHub에 DB 패스워드 포함 코드 Push → DLP 실시간 차단 ✅ / 계약서를 외부 Gmail로 전송 시 암호화 강제 적용                                   | 퇴직 예정 직원이 대량 파일 다운로드 → UEBA 이상 행위 탐지·HR 알림 ✅ / 탈취된 세션 쿠키로 클라우드 접근 → 비정상 위치·행동 탐지                                         |
| **규제 연계**   | 앞서 다룬 **개인정보보호법**: PII 포함 파일 클라우드 이동 통제 / **CSAP 등급**: 데이터 민감도별 허용 클라우드 제한                                         | **GDPR Article 32**: 클라우드 데이터 암호화·접근통제 / 앞서 다룬 **LINDDUN Non-Compliance** 방어                                     | 앞서 다룬 **AI-SOC·SOAR**: CASB 경보 → SOAR 플레이북 자동 대응 / 계정 즉시 차단·조사 자동화                                                       |

***

#### Ⅲ. 배포 모델 및 적용 체계

**가. CASB 3대 배포 모델**

```
[CASB 배포 모델 3가지]

①API 연동 방식 (API Mode)
  SaaS 앱 API로 직접 연결
  → 저장 데이터 스캔·공유 설정 제어
  → 트래픽 우회 없음·빠른 배포
  → 실시간 차단 불가 (사후 대응) 🚨
  적합: Microsoft 365·Google Workspace·Salesforce

②프록시 방식 (Proxy Mode)
  모든 SaaS 트래픽을 CASB 경유
  → 실시간 정책 적용·차단 가능 ✅
  → 인라인(Inline) 방식으로 지연 발생
  ├─ 포워드 프록시: 에이전트 설치 (관리 기기)
  └─ 리버스 프록시: 에이전트 불필요 (BYOD)

③로그 분석 방식 (Log Mode)
  방화벽·프록시 로그 수집·분석
  → Shadow IT 탐지 특화
  → 기존 인프라 활용·저비용
  → 실시간 제어 불가 (가시성 중심)
```

***

**나. CASB·제로트러스트·SASE 연계**

```
[현대 클라우드 보안 통합 아키텍처]

사용자 (재택·모바일·사무실)
       ↓
ZTNA (Zero Trust Network Access)
  신원·기기 신뢰 검증 (앞서 다룬 제로트러스트)
       ↓
CASB (Cloud Access Security Broker)
  SaaS 접근 정책·DLP·위협 탐지
       ↓
SaaS 앱 (Microsoft 365·Slack·Salesforce)
  + Shadow IT 탐지

→ CASB + ZTNA + SWG + SDWAN = SASE
  (Secure Access Service Edge)
  앞서 다룬 제로트러스트 아키텍처의 클라우드 구현체
```

***

**다. 기존 DLP vs CASB 비교**

| 비교 항목         | 기존 온프레미스 DLP  | CASB          |
| :------------ | :------------ | :------------ |
| **적용 범위**     | 내부 네트워크·엔드포인트 | 클라우드·SaaS 전체  |
| **Shadow IT** | 탐지 불가 🚨      | 탐지·차단 ✅       |
| **BYOD 지원**   | 제한적           | 리버스 프록시로 지원 ✅ |
| **실시간 제어**    | 가능            | 배포 모델에 따라 상이  |
| **클라우드 암호화**  | 불가            | 키 관리 포함 가능 ✅  |
| **위협 탐지**     | 시그니처 기반       | UEBA·AI 행동 분석 |

***

**(제언)** "CASB는 경계가 사라진 SaaS 시대에 '데이터가 클라우드로 이동하는 모든 경로를 통제하는 전사 데이터 유출 방지의 마지막 관문'입니다. **앞서 다룬 공공 SaaS 거버넌스의 위험관리 4대 원칙(데이터 주권·서비스 연속성·공급자 종속·컴플라이언스) 중 데이터 주권과 컴플라이언스를 기술적으로 집행하는 수단이 CASB이며, 제로트러스트·SASE 아키텍처와 통합해 신원 검증(ZTNA)→클라우드 접근 제어(CASB)→위협 탐지(AI-SOC) 3단계 클라우드 보안 체계를 구축하는 것이 SaaS 전환 시대 기업 보안의 핵심 전략입니다.**"
