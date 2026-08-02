### **현대 웹 인증·인가의 표준: OAuth 2.0 & OIDC**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 "로그인"과 "권한 위임"을 구분해야 하는가)
Ⅱ. OAuth 2.0 핵심 원리
Ⅲ. OIDC 핵심 원리 및 관계
Ⅳ. 비교 및 적용 체계
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 SDP·제로트러스트가 '연결 전 신원을 명시적으로 검증'하는 아키텍처 원칙이라면, OAuth 2.0과 OIDC는 그 신원 검증을 웹·API 생태계에서 표준화된 프로토콜로 구현하는 기술이다 — OAuth 2.0(RFC 6749)은 본래 '인증(Authentication)'이 아닌 '인가(Authorization)' 프로토콜로, 사용자가 자신의 비밀번호를 제3자 앱에 직접 넘기지 않고도 특정 리소스에 대한 제한된 접근 권한만 위임하는 것이 목적이며, OIDC(OpenID Connect)는 그 OAuth 2.0 위에 '이 사용자가 누구인지'를 증명하는 신원 계층(ID Token)을 얹어 '로그인'이라는 인증 문제까지 표준화한 것으로, 구글·페이스북 소셜 로그인부터 앞서 다룬 SDP 컨트롤러의 IdP 연동까지 현대 SSO(Single Sign-On)의 사실상 표준 기반"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.
\
![Mermaid diagram](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1OTguMDc5IDQyMy4zIiB3aWR0aD0iNTk4LjA3OSIgaGVpZ2h0PSI0MjMuMyIgc3R5bGU9Ii0tYmc6I0ZGRkZGRjstLWZnOiMzQjNCM0I7LS1saW5lOiMzQjNCM0I7LS1hY2NlbnQ6IzAwNUZCODstLW11dGVkOiMzQjNCM0JDQzstLXN1cmZhY2U6I0Y4RjhGODstLWJvcmRlcjojM0IzQjNCO2JhY2tncm91bmQ6dmFyKC0tYmcpIj4KPHN0eWxlPgogIEBpbXBvcnQgdXJsKCdodHRwczovL2ZvbnRzLmdvb2dsZWFwaXMuY29tL2NzczI/ZmFtaWx5PUludGVyOndnaHRANDAwOzUwMDs2MDA7NzAwJmFtcDtkaXNwbGF5PXN3YXAnKTsKICB0ZXh0IHsgZm9udC1mYW1pbHk6ICdJbnRlcicsIHN5c3RlbS11aSwgc2Fucy1zZXJpZjsgfQogIHN2ZyB7CiAgICAvKiBEZXJpdmVkIGZyb20gLS1iZyBhbmQgLS1mZyAob3ZlcnJpZGFibGUgdmlhIC0tbGluZSwgLS1hY2NlbnQsIGV0Yy4pICovCiAgICAtLV90ZXh0OiAgICAgICAgICB2YXIoLS1mZyk7CiAgICAtLV90ZXh0LXNlYzogICAgICB2YXIoLS1tdXRlZCwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA2MCUsIHZhcigtLWJnKSkpOwogICAgLS1fdGV4dC1tdXRlZDogICAgdmFyKC0tbXV0ZWQsIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgNDAlLCB2YXIoLS1iZykpKTsKICAgIC0tX3RleHQtZmFpbnQ6ICAgIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMjUlLCB2YXIoLS1iZykpOwogICAgLS1fbGluZTogICAgICAgICAgdmFyKC0tbGluZSwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1MCUsIHZhcigtLWJnKSkpOwogICAgLS1fYXJyb3c6ICAgICAgICAgdmFyKC0tYWNjZW50LCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDg1JSwgdmFyKC0tYmcpKSk7CiAgICAtLV9ub2RlLWZpbGw6ICAgICB2YXIoLS1zdXJmYWNlLCBjb2xvci1taXgoaW4gc3JnYiwgdmFyKC0tZmcpIDMlLCB2YXIoLS1iZykpKTsKICAgIC0tX25vZGUtc3Ryb2tlOiAgIHZhcigtLWJvcmRlciwgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAyMCUsIHZhcigtLWJnKSkpOwogICAgLS1fZ3JvdXAtZmlsbDogICAgdmFyKC0tYmcpOwogICAgLS1fZ3JvdXAtaGRyOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSA1JSwgdmFyKC0tYmcpKTsKICAgIC0tX2lubmVyLXN0cm9rZTogIGNvbG9yLW1peChpbiBzcmdiLCB2YXIoLS1mZykgMTIlLCB2YXIoLS1iZykpOwogICAgLS1fa2V5LWJhZGdlOiAgICAgY29sb3ItbWl4KGluIHNyZ2IsIHZhcigtLWZnKSAxMCUsIHZhcigtLWJnKSk7CiAgfQo8L3N0eWxlPgo8ZGVmcz4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjciIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvIj4KICAgIDxwb2x5Z29uIHBvaW50cz0iMCAwLCA4IDIuNSwgMCA1IiBmaWxsPSJ2YXIoLS1fYXJyb3cpIiBzdHJva2U9InZhcigtLV9hcnJvdykiIHN0cm9rZS13aWR0aD0iMC43NSIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgLz4KICA8L21hcmtlcj4KICA8bWFya2VyIGlkPSJhcnJvd2hlYWQtc3RhcnQiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjUiIHJlZlg9IjEiIHJlZlk9IjIuNSIgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiPgogICAgPHBvbHlnb24gcG9pbnRzPSI4IDAsIDAgMi41LCA4IDUiIGZpbGw9InZhcigtLV9hcnJvdykiIHN0cm9rZT0idmFyKC0tX2Fycm93KSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiBzdHJva2UtbGluZWpvaW49InJvdW5kIiAvPgogIDwvbWFya2VyPgo8L2RlZnM+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJVc2VyIiBkYXRhLXRvPSJDbGllbnQiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIHBvaW50cz0iNDYxLjE1MTUwMDAwMDAwMDA2LDE2OS4yIDQ2MS4xNTE1MDAwMDAwMDAwNiwxODEuMiAzMTAuNzM5MjUsMTgxLjIgMzEwLjczOTI1LDE5My4yIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+Cjxwb2x5bGluZSBjbGFzcz0iZWRnZSIgZGF0YS1mcm9tPSJDbGllbnQiIGRhdGEtdG89IkF1dGhTZXJ2ZXIiIGRhdGEtc3R5bGU9InNvbGlkIiBkYXRhLWFycm93LXN0YXJ0PSJmYWxzZSIgZGF0YS1hcnJvdy1lbmQ9InRydWUiIGRhdGEtbGFiZWw9IjEuIE9JREMg7J246rCAL+yduOymnSDsmpTssq0iIHBvaW50cz0iMjc3LjQ2NiwxOTMuMiAyNzcuNDY2LDExMi45IDIyNy43Mjg2NjY2NjY2NjY2NywxMTIuOSAyMjcuNzI4NjY2NjY2NjY2NjcsNzYuOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQXV0aFNlcnZlciIgZGF0YS10bz0iQ2xpZW50IiBkYXRhLXN0eWxlPSJzb2xpZCIgZGF0YS1hcnJvdy1zdGFydD0iZmFsc2UiIGRhdGEtYXJyb3ctZW5kPSJ0cnVlIiBkYXRhLWxhYmVsPSIyLiBJRCBUb2tlbiArIEFjY2VzcyBUb2tlbiDrsJzquIkiIHBvaW50cz0iMTczLjIzNzMzMzMzMzMzMzM0LDc2LjkgMTczLjIzNzMzMzMzMzMzMzM0LDExMi45IDEyMy41LDExMi45IDEyMy41LDE4MS4yIDI0NC4xOTI3NTAwMDAwMDAwNSwxODEuMiAyNDQuMTkyNzUwMDAwMDAwMDUsMTkzLjIiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tX2xpbmUpIiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyb3doZWFkKSIgLz4KPHBvbHlsaW5lIGNsYXNzPSJlZGdlIiBkYXRhLWZyb209IkNsaWVudCIgZGF0YS10bz0iT0lEQyIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iMy4gSUQgVG9rZW4gKEpXVCkg6rKA7KadIiBwb2ludHM9IjI1NS4yODM4MzMzMzMzMzMzOCwyMzAuMTAwMDAwMDAwMDAwMDIgMjU1LjI4MzgzMzMzMzMzMzM4LDI2Ni4xIDE4MC40NzIwMDAwMDAwMDAwNCwyNjYuMSAxODAuNDcyLDM0Ni40MDAwMDAwMDAwMDAwMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS1fbGluZSkiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnJvd2hlYWQpIiAvPgo8cG9seWxpbmUgY2xhc3M9ImVkZ2UiIGRhdGEtZnJvbT0iQ2xpZW50IiBkYXRhLXRvPSJSZXNvdXJjZVNlcnZlciIgZGF0YS1zdHlsZT0ic29saWQiIGRhdGEtYXJyb3ctc3RhcnQ9ImZhbHNlIiBkYXRhLWFycm93LWVuZD0idHJ1ZSIgZGF0YS1sYWJlbD0iNC4gQWNjZXNzIFRva2VuIOygnOy2nCIgcG9pbnRzPSIyOTkuNjQ4MTY2NjY2NjY2NywyMzAuMTAwMDAwMDAwMDAwMDIgMjk5LjY0ODE2NjY2NjY2NjcsMjY2LjEgNDA0LjE3OTUsMjY2LjEgNDA0LjE3OTUsMzQ2LjQwMDAwMDAwMDAwMDAzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLV9saW5lKSIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2Fycm93aGVhZCkiIC8+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkNsaWVudCIgZGF0YS10bz0iQXV0aFNlcnZlciIgZGF0YS1sYWJlbD0iMS4gT0lEQyDsnbjqsIAv7J247KadIOyalOyyrSI+CiAgPHJlY3QgeD0iMjE0LjQ2NiIgeT0iMTE5LjkiIHdpZHRoPSIxMjUuNzU4MDAwMDAwMDAwMDEiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIyNzcuMzQ1IiB5PSIxMzUuMDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjEuIE9JREMg7J246rCAL+yduOymnSDsmpTssq08L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQXV0aFNlcnZlciIgZGF0YS10bz0iQ2xpZW50IiBkYXRhLWxhYmVsPSIyLiBJRCBUb2tlbiArIEFjY2VzcyBUb2tlbiDrsJzquIkiPgogIDxyZWN0IHg9IjM2IiB5PSIxMTkuOSIgd2lkdGg9IjE3NC40NjYwMDAwMDAwMDAwNCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjEyMy4yMzMwMDAwMDAwMDAwMiIgeT0iMTM1LjA1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNDAwIiBmaWxsPSJ2YXIoLS1fdGV4dC1zZWMpIiBkeT0iMy44NDk5OTk5OTk5OTk5OTk2Ij4yLiBJRCBUb2tlbiArIEFjY2VzcyBUb2tlbiDrsJzquIk8L3RleHQ+CjwvZz4KPGcgY2xhc3M9ImVkZ2UtbGFiZWwiIGRhdGEtZnJvbT0iQ2xpZW50IiBkYXRhLXRvPSJPSURDIiBkYXRhLWxhYmVsPSIzLiBJRCBUb2tlbiAoSldUKSDqsoDspp0iPgogIDxyZWN0IHg9IjExNi45NzIwMDAwMDAwMDAwNCIgeT0iMjczLjEiIHdpZHRoPSIxMjYuMzUyMDAwMDAwMDAwMDIiIGhlaWdodD0iMzAuMyIgcng9IjIiIHJ5PSIyIiBmaWxsPSJ2YXIoLS1iZykiIHN0cm9rZT0idmFyKC0tX2lubmVyLXN0cm9rZSkiIHN0cm9rZS13aWR0aD0iMSIgLz4KICA8dGV4dCB4PSIxODAuMTQ4MDAwMDAwMDAwMDUiIHk9IjI4OC4yNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjQwMCIgZmlsbD0idmFyKC0tX3RleHQtc2VjKSIgZHk9IjMuODQ5OTk5OTk5OTk5OTk5NiI+My4gSUQgVG9rZW4gKEpXVCkg6rKA7KadPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJlZGdlLWxhYmVsIiBkYXRhLWZyb209IkNsaWVudCIgZGF0YS10bz0iUmVzb3VyY2VTZXJ2ZXIiIGRhdGEtbGFiZWw9IjQuIEFjY2VzcyBUb2tlbiDsoJzstpwiPgogIDxyZWN0IHg9IjM0Mi42Nzk1IiB5PSIyNzMuMSIgd2lkdGg9IjEyMi43ODgwMDAwMDAwMDAwNCIgaGVpZ2h0PSIzMC4zIiByeD0iMiIgcnk9IjIiIGZpbGw9InZhcigtLWJnKSIgc3Ryb2tlPSJ2YXIoLS1faW5uZXItc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIxIiAvPgogIDx0ZXh0IHg9IjQwNC4wNzM1IiB5PSIyODguMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI0MDAiIGZpbGw9InZhcigtLV90ZXh0LXNlYykiIGR5PSIzLjg0OTk5OTk5OTk5OTk5OTYiPjQuIEFjY2VzcyBUb2tlbiDsoJzstpw8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlVzZXIiIGRhdGEtbGFiZWw9IuyCrOyaqeyekCA6IFJlc291cmNlIE93bmVyIiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9IjM2NC4yMjQwMDAwMDAwMDAwNSIgeT0iMTMyLjMiIHdpZHRoPSIxOTMuODU1IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDYxLjE1MTUwMDAwMDAwMDA2IiB5PSIxNTAuNzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI1MDAiIGZpbGw9InZhcigtLV90ZXh0KSIgZHk9IjQuNTUiPuyCrOyaqeyekCA6IFJlc291cmNlIE93bmVyPC90ZXh0Pgo8L2c+CjxnIGNsYXNzPSJub2RlIiBkYXRhLWlkPSJDbGllbnQiIGRhdGEtbGFiZWw9Iu2BtOudvOydtOyWuO2KuCDslbEiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMjEwLjkxOTUwMDAwMDAwMDAzIiB5PSIxOTMuMiIgd2lkdGg9IjEzMy4wOTMwMDAwMDAwMDAwMiIgaGVpZ2h0PSIzNi45MDAwMDAwMDAwMDAwMDYiIHJ4PSIwIiByeT0iMCIgZmlsbD0idmFyKC0tX25vZGUtZmlsbCkiIHN0cm9rZT0idmFyKC0tX25vZGUtc3Ryb2tlKSIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjI3Ny40NjYiIHk9IjIxMS42NDk5OTk5OTk5OTk5OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+7YG065287J207Ja47Yq4IOyVsTwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iQXV0aFNlcnZlciIgZGF0YS1sYWJlbD0i7J246rCAL+yduOymnSDshJzrsoQgOiBJZFAiIGRhdGEtc2hhcGU9InJlY3RhbmdsZSI+CiAgPHJlY3QgeD0iMTE4Ljc0NjAwMDAwMDAwMDAxIiB5PSI0MCIgd2lkdGg9IjE2My40NzQiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNmZmViZWUiIHN0cm9rZT0iI2QzMmYyZiIgc3Ryb2tlLXdpZHRoPSIwLjc1IiAvPgogIDx0ZXh0IHg9IjIwMC40ODMiIHk9IjU4LjQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij7snbjqsIAv7J247KadIOyEnOuyhCA6IElkUDwvdGV4dD4KPC9nPgo8ZyBjbGFzcz0ibm9kZSIgZGF0YS1pZD0iT0lEQyIgZGF0YS1sYWJlbD0iT0lEQyA6IOyCrOyaqeyekCDsi6Dsm5Ag7ZmV7J24IiBkYXRhLXNoYXBlPSJyZWN0YW5nbGUiPgogIDxyZWN0IHg9Ijg2Ljg3OTAwMDAwMDAwMDAyIiB5PSIzNDYuNDAwMDAwMDAwMDAwMDMiIHdpZHRoPSIxODcuMTg1OTk5OTk5OTk5OTgiIGhlaWdodD0iMzYuOTAwMDAwMDAwMDAwMDA2IiByeD0iMCIgcnk9IjAiIGZpbGw9IiNlOGY1ZTkiIHN0cm9rZT0iIzM4OGUzYyIgc3Ryb2tlLXdpZHRoPSIycHgiIC8+CiAgPHRleHQgeD0iMTgwLjQ3MiIgeT0iMzY0Ljg1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNTAwIiBmaWxsPSJ2YXIoLS1fdGV4dCkiIGR5PSI0LjU1Ij5PSURDIDog7IKs7Jqp7J6QIOyLoOybkCDtmZXsnbg8L3RleHQ+CjwvZz4KPGcgY2xhc3M9Im5vZGUiIGRhdGEtaWQ9IlJlc291cmNlU2VydmVyIiBkYXRhLWxhYmVsPSJPQXV0aCAyLjAgOiBBUEkg66as7IaM7IqkIOygkeq3vCIgZGF0YS1zaGFwZT0icmVjdGFuZ2xlIj4KICA8cmVjdCB4PSIzMDIuMDY1IiB5PSIzNDYuNDAwMDAwMDAwMDAwMDMiIHdpZHRoPSIyMDQuMjI5IiBoZWlnaHQ9IjM2LjkwMDAwMDAwMDAwMDAwNiIgcng9IjAiIHJ5PSIwIiBmaWxsPSJ2YXIoLS1fbm9kZS1maWxsKSIgc3Ryb2tlPSJ2YXIoLS1fbm9kZS1zdHJva2UpIiBzdHJva2Utd2lkdGg9IjAuNzUiIC8+CiAgPHRleHQgeD0iNDA0LjE3OTUiIHk9IjM2NC44NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMyIgZm9udC13ZWlnaHQ9IjUwMCIgZmlsbD0idmFyKC0tX3RleHQpIiBkeT0iNC41NSI+T0F1dGggMi4wIDogQVBJIOumrOyGjOyKpCDsoJHqt7w8L3RleHQ+CjwvZz4KPC9zdmc+ "Mermaid diagram")

***

#### Ⅱ. OAuth 2.0 �심 원리

**가. 핵심 역할 및 용어**

| 역할                       | 정의                                | 예시            |
| :----------------------- | :-------------------------------- | :------------ |
| **Resource Owner**       | 리소스의 소유자(보통 사용자)                  | 나(사용자)        |
| **Client**               | 리소스에 접근하려는 제3자 애플리케이션             | 캘린더 연동 앱      |
| **Authorization Server** | 인가 처리·토큰 발급 서버                    | 구글 계정 서버      |
| **Resource Server**      | 실제 보호된 리소스를 보유한 서버(API)           | 구글 캘린더 API    |
| **Access Token**         | Client가 리소스에 접근할 때 사용하는 제한된 권한 증표 | 만료시간·Scope 포함 |

**나. Authorization Code Flow (가장 표준적인 흐름)**

```
[OAuth 2.0 Authorization Code Flow]

①사용자 → Client: "구글 캘린더 연동해줘"
②Client → Authorization Server: 인가 요청(리다이렉트)
③사용자 → Authorization Server: 로그인 + 권한 동의
④Authorization Server → Client: Authorization Code 발급
⑤Client → Authorization Server: Code + Client Secret 제출
⑥Authorization Server → Client: Access Token(+Refresh Token) 발급
⑦Client → Resource Server: Access Token으로 API 호출
⑧Resource Server → Client: 리소스(캘린더 데이터) 응답

핵심: 비밀번호는 오직 ③단계에서 Authorization Server에만 입력
      Client는 비밀번호를 절대 보지 못함 ✅
```

**다. 4대 그랜트 타입(Grant Type)**

| 그랜트 타입                 | 적용 대상                 | 특징                             |
| :--------------------- | :-------------------- | :----------------------------- |
| **Authorization Code** | 서버 사이드 웹 앱            | 가장 안전·표준 / Client Secret 사용    |
| **PKCE 확장**            | 모바일·SPA(퍼블릭 클라이언트)    | Secret 저장 불가 환경에서 코드 탈취 방어     |
| **Client Credentials** | 서버 간 통신(사용자 개입 없음)    | M2M(Machine-to-Machine) API 인증 |
| **Refresh Token**      | Access Token 만료 시 재발급 | 재로그인 없이 세션 연장                  |

***

#### Ⅲ. OIDC 핵심 원리 및 관계

**가. OAuth 2.0 위에 얹힌 신원 계층**

```
[OAuth 2.0과 OIDC의 관계]

OAuth 2.0: "이 앱이 내 캘린더에 접근해도 됨" (인가)
  → Access Token 발급
  → 토큰만으로는 "누가 로그인했는지" 표준적으로 알 수 없음 🚨

OIDC: OAuth 2.0 흐름에 신원 증명 계층 추가
  → openid Scope 요청 시 ID Token 함께 발급
  → ID Token = "이 사용자는 홍길동이 맞다"는 서명된 증명서

동일한 Authorization Code Flow 위에서:
  Access Token  : 리소스 접근 권한(인가)
  ID Token      : 사용자 신원 증명(인증) ← OIDC의 핵심 추가
  UserInfo Endpoint: 추가 프로필 정보 조회
```

**나. ID Token 구조 (JWT 기반)**

| 항목                | 내용                                                        |
| :---------------- | :-------------------------------------------------------- |
| **형식**            | JWT(JSON Web Token) / Header.Payload.Signature 3부분        |
| **필수 클레임(Claim)** | iss(발급자)·sub(사용자 고유ID)·aud(대상 Client)·exp(만료)·iat(발급시각)   |
| **서명 검증**         | Authorization Server의 공개키로 서명 검증 → 위변조 여부 확인              |
| **Discovery**     | `.well-known/openid-configuration` 엔드포인트로 IdP 메타데이터 자동 탐색 |

***

#### Ⅳ. 비교 및 적용 체계

**가. OAuth 2.0 vs OIDC 핵심 비교**

| 비교 항목         | OAuth 2.0             | OIDC                               |
| :------------ | :-------------------- | :--------------------------------- |
| **주 목적**      | **인가(Authorization)** | **인증(Authentication)** + 인가        |
| **핵심 산출물**    | Access Token          | **ID Token** + Access Token        |
| **토큰 형식**     | 형식 자유(불투명 토큰 가능)      | **JWT 표준 강제**                      |
| **사용자 정보 조회** | 표준화 안 됨(API마다 다름)     | **UserInfo Endpoint 표준화**          |
| **적용 예시**     | "이 앱이 내 사진에 접근 허용"    | "구글 계정으로 로그인"                      |
| **표준 문서**     | RFC 6749              | OpenID Foundation 표준(OAuth 2.0 확장) |

**나. 그랜트 타입별 적용 시나리오**

| 시나리오                | 권장 방식                         | 이유                     |
| :------------------ | :---------------------------- | :--------------------- |
| **전통 서버 웹앱 로그인**    | Authorization Code + OIDC     | Secret 안전 보관 가능        |
| **모바일·SPA 앱**       | Authorization Code + **PKCE** | Secret 노출 위험 방어        |
| **서버 간 배치 작업 인증**   | Client Credentials            | 사용자 개입 없는 M2M          |
| **레거시 서드파티 통합**     | Client Credentials + 짧은 TTL   | 최소 권한 원칙 준수            |
| **SDP·SASE 통합 SSO** | OIDC + SAML 병행                | 앞서 다룬 SDP 컨트롤러의 IdP 연동 |

**다. 보안 위협 및 대응**

| 위협                        | 내용                       | 대응                                        |
| :------------------------ | :----------------------- | :---------------------------------------- |
| **Authorization Code 탈취** | 리다이렉트 URI 가로채기           | **PKCE**(Proof Key for Code Exchange) 필수화 |
| **토큰 재생 공격**              | 탈취된 Access Token 재사용     | 짧은 만료시간 + Refresh Token 로테이션              |
| **오픈 리다이렉트**              | redirect\_uri 조작으로 토큰 탈취 | 사전 등록된 URI만 화이트리스트 허용                     |
| **CSRF**                  | 인가 요청 위조                 | state 파라미터 필수 검증                          |

***

**(제언)** "OAuth 2.0과 OIDC는 '비밀번호를 절대 제3자에게 넘기지 않는다'는 원칙 위에서 각각 권한 위임과 신원 증명이라는 서로 다른 문제를 해결하며, 실무에서는 항상 OIDC가 OAuth 2.0을 포함하는 상위 계층으로 함께 구현됩니다. 다만 모바일·SPA 환경에서는 Client Secret을 안전하게 보관할 수 없으므로 반드시 PKCE를 적용해야 하며, ID Token은 서명 검증 없이 페이로드만 신뢰해서는 안 되고 매 요청마다 Authorization Server의 공개키로 서명을 검증하는 것이 필수이며, Access Token은 가능한 짧은 유효기간으로 설정하고 Refresh Token 로테이션을 통해 탈취 시 피해 범위를 최소화하는 것이 프로덕션 환경 설계의 핵심입니다.

***

**앞서 다룬 개념과의 연결**

| 연계 개념           | 연결 내용                                                 |
| :-------------- | :---------------------------------------------------- |
| **SDP·제로트러스트**  | SDP 컨트롤러의 신원 검증 단계에서 OIDC IdP 연동으로 사용자 인증 수행          |
| **CASB**        | 클라우드 앱 접근 시 OAuth 토큰 오남용 탐지가 CASB의 핵심 모니터링 대상         |
| **TPM·HSM**     | Client Secret·서명용 개인키를 하드웨어 보안 모듈에 저장해 탈취 방어          |
| **패스더해시·골든 티켓** | 온프레미스 Kerberos의 대안으로 클라우드 환경에서는 OIDC가 유사한 신원 증명 역할 수행 |
| **API 게이트웨이**   | Access Token 검증을 게이트웨이 계층에서 중앙화해 마이크로서비스 전체에 일괄 적용    |
