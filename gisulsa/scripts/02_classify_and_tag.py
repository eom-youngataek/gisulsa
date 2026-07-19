\
# -*- coding: utf-8 -*-
import os, re, json, sys, math, pickle
from collections import defaultdict, Counter

sys.path.insert(0, os.path.dirname(__file__))
from parse_utils import tokenize

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_output")

with open(os.path.join(OUT, "state.pkl"), "rb") as f:
    st = pickle.load(f)
domain_entries = st["domain_entries"]
pred_entries = st["pred_entries"]
token_domain_count = st["token_domain_count"]

with open(os.path.join(OUT, "questions_raw.json"), encoding="utf-8") as f:
    questions = json.load(f)

def vote_domain(tokens):
    scores = Counter()
    for t in tokens:
        dc = token_domain_count.get(t)
        if not dc:
            continue
        total = sum(dc.values())
        weight = 1.0 / math.log(2 + total)
        for folder, c in dc.items():
            scores[folder] += weight * c
    if not scores:
        return None
    return scores.most_common(1)[0][0]

# ---------- 1. 기출문제 도메인 분류 ----------
for q in questions:
    q["tokens"] = list(tokenize(q["text"]))
    q["domain"] = vote_domain(q["tokens"])

dom_cnt = Counter(q["domain"] for q in questions)
print("question domain distribution:", dom_cnt)

# ---------- 2. 기출문제 역색인 (token -> question idx 목록) ----------
q_token_index = defaultdict(list)
for i, q in enumerate(questions):
    for t in q["tokens"]:
        q_token_index[t].append(i)

def match_questions(entry_tokens, min_score=2):
    cand = Counter()
    for t in entry_tokens:
        for qi in q_token_index.get(t, []):
            cand[qi] += 1
    results = []
    for qi, score in cand.items():
        if score >= min_score or (score == 1 and any(len(t) >= 4 for t in entry_tokens)):
            results.append((score, qi))
    results.sort(key=lambda x: -x[0])
    return results[:3]


def core_title(title):
    # 괄호/구분자 이전의 핵심 명칭 추출 (예: "세마포어 (Semaphore) vs 뮤텍스" -> "세마포어")
    t = re.split(r"[\(\)/·,]| vs | & ", title)[0].strip()
    return t


def tag_exam_history(entry):
    toks = entry["tokens"]
    ct = core_title(entry["keyword"])
    matches = []
    if len(ct) >= 2:
        for i, q in enumerate(questions):
            if ct.lower() in q["text"].lower():
                matches.append((99, i))
    if not matches:
        matches = match_questions(toks, min_score=2)
    if not matches:
        return None
    out = []
    for score, qi in matches:
        q = questions[qi]
        out.append(f"{q['round']}회 {q['session']}")
    # 중복 회차 제거, 최대 2개
    seen = []
    for m in out:
        if m not in seen:
            seen.append(m)
    return ", ".join(seen[:2]) + " 기출"

all_entries = domain_entries + pred_entries
matched_count = 0
for e in all_entries:
    hist = tag_exam_history(e)
    if hist:
        e["examHistory"] = hist
        e["isPredicted"] = False
        matched_count += 1
    else:
        e["examHistory"] = None
        e["isPredicted"] = True

print(f"matched to real exam: {matched_count} / {len(all_entries)}")

with open(os.path.join(OUT, "questions_tagged2.json"), "w", encoding="utf-8") as f:
    json.dump([{k: v for k, v in q.items() if k != "tokens"} for q in questions], f, ensure_ascii=False, indent=1)

with open(os.path.join(OUT, "state2.pkl"), "wb") as f:
    pickle.dump({"domain_entries": domain_entries, "pred_entries": pred_entries, "questions": questions}, f)

# 샘플 확인
import random
random.seed(1)
sample_matched = [e for e in all_entries if e["isPredicted"] is False]
sample_unmatched = [e for e in all_entries if e["isPredicted"] is True]
print("\n--matched sample--")
for e in random.sample(sample_matched, min(8, len(sample_matched))):
    print(e["keyword"], "->", e["examHistory"])
print("\n--unmatched sample--")
for e in random.sample(sample_unmatched, min(8, len(sample_unmatched))):
    print(e["keyword"])
