\
# -*- coding: utf-8 -*-
import os, re, json, sys, pickle

sys.path.insert(0, os.path.dirname(__file__))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_output")

with open(os.path.join(OUT, "state2.pkl"), "rb") as f:
    st = pickle.load(f)
domain_entries = st["domain_entries"]
pred_entries = st["pred_entries"]
questions = st["questions"]

# ---------- questionType 판정을 위해 examHistory 매칭 시 세션정보도 함께 저장하도록 재계산 ----------
import math
from collections import defaultdict, Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_utils import tokenize

q_token_index = defaultdict(list)
for i, q in enumerate(questions):
    for t in q.get("tokens", []):
        q_token_index[t].append(i)

def core_title(title):
    t = re.split(r"[\(\)/·,]| vs | & ", title)[0].strip()
    return t

def find_matches(entry):
    ct = core_title(entry["keyword"])
    matches = []
    if len(ct) >= 2:
        for i, q in enumerate(questions):
            if ct.lower() in q["text"].lower():
                matches.append(i)
    if not matches:
        cand = Counter()
        for t in entry["tokens"]:
            for qi in q_token_index.get(t, []):
                cand[qi] += 1
        for qi, score in cand.items():
            if score >= 2 or (score == 1 and any(len(t) >= 4 for t in entry["tokens"])):
                matches.append(qi)
    return matches[:3]

def build_final(entries, source_kind):
    out = []
    for e in entries:
        matches = find_matches(e)
        content_len = len(e["rawContent"])
        if matches:
            rounds = []
            sessions = []
            for qi in matches:
                q = questions[qi]
                tag = f"{q['round']}회 {q['session']}"
                if tag not in rounds:
                    rounds.append(tag)
                sessions.append(q["session"])
            exam_history = ", ".join(rounds[:2]) + " 기출"
            is_predicted = False
            source = "실제 기출문제 (120~139회)"
            session1 = sessions[0] if sessions else "2교시"
            question_type = "1교시형" if session1 == "1교시" else "2~4교시형"
        else:
            exam_history = "미출제 예상"
            is_predicted = True
            if source_kind == "predicted":
                source = "전자신문·IT FIND·주간기술동향·위키독스 조사"
            else:
                source = "핵심키워드 정리 노트(자체 리서치)"
            question_type = "2~4교시형" if content_len > 1400 else "1교시형"

        out.append({
            "id": e["id"],
            "mainDomain": e["mainDomain"],
            "subDomain": e["subDomain"],
            "keyword": e["keyword"],
            "examHistory": exam_history,
            "isPredicted": is_predicted,
            "source": source,
            "mnemonic": e["mnemonic"],
            "questionType": question_type,
            "structured": False,
            "rawContent": e["rawContent"],
            "sourceFile": e["sourceFile"],
        })
    return out

final_domain = build_final(domain_entries, "domain")
final_pred = build_final(pred_entries, "predicted")

all_final = final_domain + final_pred
print("total final entries:", len(all_final))
from collections import Counter
print("by mainDomain:", Counter(e["mainDomain"] for e in all_final))
print("by isPredicted:", Counter(e["isPredicted"] for e in all_final))
print("by questionType:", Counter(e["questionType"] for e in all_final))

with open(os.path.join(OUT, "keyword_database_auto.json"), "w", encoding="utf-8") as f:
    json.dump(all_final, f, ensure_ascii=False, indent=1)

# 실제 기출문제 뱅크 (검색/모의고사용, 도메인 태그 포함)
qbank = []
for i, q in enumerate(questions):
    qbank.append({
        "id": f"q-{i+1:04d}",
        "round": q["round"],
        "subjectTrack": q["subject"],
        "session": q["session"],
        "num": q["num"],
        "text": q["text"],
        "domain": q.get("domain"),
    })
with open(os.path.join(OUT, "question_bank.json"), "w", encoding="utf-8") as f:
    json.dump(qbank, f, ensure_ascii=False, indent=1)

print("question bank:", len(qbank))
