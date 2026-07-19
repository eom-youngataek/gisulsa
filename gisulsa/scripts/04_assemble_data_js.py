\
# -*- coding: utf-8 -*-
"""
4단계(최종): curated_keywords.json(수작업 정예 답안) + keyword_database_auto.json(자동수집 527) +
question_bank.json(실제 기출 991문항) 을 병합해 사이트 루트의 data.js 를 생성한다.

실행: python3 04_assemble_data_js.py
출력: <사이트 루트>/data.js  (기존 data.js를 덮어씀)
"""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(HERE, "build_output")

DOMAIN_STRUCTURE = [
    {"id": "mgt", "name": "1. 경영정보시스템", "subDomains": ["1.1 IT감리", "1.2 IT성과관리", "1.3 IT프로젝트관리", "1.4 경영혁신", "1.5 조직관리", "1.6 클라우드정책거버넌스"]},
    {"id": "net", "name": "2. 네트워크", "subDomains": ["2.1 SDN", "2.2 근거리무선통신", "2.3 네트워크 프토토콜", "2.4 이동통신기술", "2.5 네트워크품질", "2.6 네트워크인프라", "2.7 네트워크보안"]},
    {"id": "db", "name": "3. 데이터베이스", "subDomains": ["3.1 모델링", "3.2 무결성제약", "3.3 트랜잭션", "3.4 회복기법", "3.5 데이터품질", "3.6 NO-SQL", "3.7 분산DB", "3.8 데이터거버넌스", "3.9 데이터보안"]},
    {"id": "se", "name": "4. 소프트웨어공학", "subDomains": ["4.1 개발방법론", "4.2 SW아키텍쳐", "4.3 SW대가산정", "4.4 SW품질표준", "4.5 SW테스트", "4.6 요구공학", "4.7 SW보안", "4.8 AI개발"]},
    {"id": "sec", "name": "5. 정보보안", "subDomains": ["5.1 개인정보보호", "5.2 디지털포렌식", "5.3 보안과제", "5.4 암호화", "5.5 사이버위협", "5.6 산업보안", "5.7 보안인증", "5.8 신흥보안위협"]},
    {"id": "cs", "name": "6. 컴퓨터시스템", "subDomains": ["6.1 CPU제어", "6.2 IO저장장치", "6.3 메모리제어", "6.4 동기화", "6.5 차세대컴퓨팅", "6.6 프로세스스케쥴링"]},
    {"id": "ai", "name": "7. 인공지능데이터", "subDomains": ["7.1 AI거버넌스", "7.2 AI데이터운영", "7.3 AI보안위협", "7.4 생성형AI", "7.5 신경망아키텍처", "7.6 통계적추론 및 검정"]},
]

with open(os.path.join(HERE, "curated_keywords.json"), encoding="utf-8") as f:
    curated = json.load(f)
with open(os.path.join(OUT, "keyword_database_auto.json"), encoding="utf-8") as f:
    auto = json.load(f)
with open(os.path.join(OUT, "question_bank.json"), encoding="utf-8") as f:
    qbank = json.load(f)

for c in curated:
    c.setdefault("sourceFile", "curated")
    c["structured"] = True

merged = curated + auto

parts = [
    "// 정보처리기술사 120회~139회 기출 + 최신동향(전자신문/IT FIND/주간기술동향/위키독스) 기반 데이터베이스",
    "// 자동 생성 파일입니다. gisulsa/scripts 파이프라인(00~04)을 재실행하면 최신 원본 노트 기준으로 다시 생성됩니다.",
    "",
    "const DOMAIN_STRUCTURE = " + json.dumps(DOMAIN_STRUCTURE, ensure_ascii=False, indent=2) + ";",
    "",
    "const KEYWORD_DATABASE = " + json.dumps(merged, ensure_ascii=False) + ";",
    "",
    "const QUESTION_BANK = " + json.dumps(qbank, ensure_ascii=False) + ";",
    "",
]

out_path = os.path.join(ROOT, "data.js")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(parts))

print(f"완료: {out_path}")
print(f"  - KEYWORD_DATABASE: {len(merged)}개 (수작업 {len(curated)} + 자동수집 {len(auto)})")
print(f"  - QUESTION_BANK: {len(qbank)}개 (120~139회 실제 기출)")
