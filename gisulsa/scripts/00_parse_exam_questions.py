\
# -*- coding: utf-8 -*-
"""
0단계: '정보처리기술사_120~139회 기출문제.md' (992문항 합본)을
회차/종목/교시/문항번호 구조로 파싱하여 questions_raw.json 생성.

실행: python3 00_parse_exam_questions.py
출력: ./build_output/questions_raw.json
"""
import os, re, json

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # gisulsa/scripts -> 사이트 루트
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_output")
os.makedirs(OUT, exist_ok=True)

src = os.path.join(ROOT, "정보처리기술사_120~139회 기출문제.md")

with open(src, encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")
questions = []
cur_round = cur_subject = cur_session = cur_q = None


def flush():
    global cur_q
    if cur_q is not None and cur_q["text"].strip():
        questions.append(cur_q)
    cur_q = None


for line in lines:
    m_round = re.match(r"^## 회 (\d+)회", line)
    m_subject = re.match(r"^### 🎯 종목: (.+)", line)
    m_session = re.match(r"^#### 📖 (\d)교시", line)
    m_q = re.match(r"^- \*\*(\d+)\.\s*(.*)", line)
    if m_round:
        flush(); cur_round = m_round.group(1); continue
    if m_subject:
        flush(); cur_subject = m_subject.group(1); continue
    if m_session:
        flush(); cur_session = m_session.group(1) + "교시"; continue
    if m_q:
        flush()
        cur_q = {"round": cur_round, "subject": cur_subject, "session": cur_session,
                  "num": m_q.group(1), "text": m_q.group(2).rstrip("*").strip()}
        continue
    m_cont = re.match(r"^\s*>\s?(.*)", line)
    if m_cont and cur_q is not None:
        cont = m_cont.group(1).strip()
        if cont:
            cur_q["text"] += " " + cont
        continue

flush()

print("총 파싱된 문항 수:", len(questions))
with open(os.path.join(OUT, "questions_raw.json"), "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=1)
print("저장 완료:", os.path.join(OUT, "questions_raw.json"))
