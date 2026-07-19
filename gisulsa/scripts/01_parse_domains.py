\
# -*- coding: utf-8 -*-
import os, re, json, sys, math
from collections import defaultdict, Counter

sys.path.insert(0, os.path.dirname(__file__))
from classify import DOMAIN_STRUCTURE, classify_subdomain
from parse_utils import strip_content, extract_title, extract_mnemonic, tokenize, is_bad_title, clean_filename_title

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # gisulsa/scripts -> site root
SRC = ROOT  # 사이트 루트 (경영정보시스템/, 네트워크/, ... 141회예상문제/, 정보처리기술사_120~139회 기출문제.md 위치)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_output")
os.makedirs(OUT, exist_ok=True)

DOMAIN_BY_FOLDER = {d["folder"]: d for d in DOMAIN_STRUCTURE}
FOLDER_LIST = [d["folder"] for d in DOMAIN_STRUCTURE]

# ---------- 1. 도메인 폴더 파싱 ----------
domain_entries = []
uid = 0
for folder in FOLDER_LIST:
    dom = DOMAIN_BY_FOLDER[folder]
    fdir = os.path.join(SRC, folder)
    for fname in sorted(os.listdir(fdir)):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(fdir, fname)
        with open(path, encoding="utf-8") as f:
            raw = f.read()
        name_noext = fname[:-3]
        content = strip_content(raw)
        title = extract_title(content, name_noext)
        title = re.sub(r"\s*핵심\s*키워드\s*$", "", title).strip() or name_noext
        if is_bad_title(title):
            title = clean_filename_title(name_noext)
        mnemonic = extract_mnemonic(content, title)
        subdomain = classify_subdomain(folder, name_noext)
        uid += 1
        domain_entries.append({
            "id": f"dm-{uid:04d}",
            "mainDomain": dom["name"],
            "subDomain": subdomain,
            "keyword": title,
            "sourceFile": f"{folder}/{fname}",
            "rawContent": content,
            "mnemonic": mnemonic,
            "tokens": tokenize(title + " " + name_noext),
        })

print("domain_entries:", len(domain_entries))

# ---------- 2. 141회예상문제 폴더 파싱 ----------
pred_dir = os.path.join(SRC, "141회예상문제")
SKIP_FILES = {"141회 예상문제.md", "141회 예상출제 분석.md", "141회대비_신규트렌드키워드_정리.md", "Untitled.md"}

pred_raw = []
for fname in sorted(os.listdir(pred_dir)):
    if not fname.endswith(".md") or fname in SKIP_FILES:
        continue
    path = os.path.join(pred_dir, fname)
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    name_noext = fname[:-3]
    content = strip_content(raw)
    title = extract_title(content, name_noext)
    title = re.sub(r"^\d+\.\s*", "", title).strip() or name_noext
    if is_bad_title(title):
        title = clean_filename_title(name_noext)
    mnemonic = extract_mnemonic(content, title)
    pred_raw.append({
        "fname": fname,
        "name_noext": name_noext,
        "title": title,
        "content": content,
        "mnemonic": mnemonic,
        "tokens": tokenize(title + " " + name_noext),
    })

print("predicted_raw:", len(pred_raw))

# ---------- 3. 도메인 판별용 토큰 인덱스 (도메인폴더 항목 기반, IDF 가중치) ----------
token_domain_count = defaultdict(Counter)  # token -> Counter(domain_id -> count)
for e in domain_entries:
    dom_id = DOMAIN_BY_FOLDER[e["mainDomain"].split(". ", 1)[1]]["id"] if False else None

# mainDomain 저장은 name(dom["name"]) 이므로 folder 재조회 위해 name->folder 매핑
NAME_TO_FOLDER = {d["name"]: d["folder"] for d in DOMAIN_STRUCTURE}

for e in domain_entries:
    folder = NAME_TO_FOLDER[e["mainDomain"]]
    for t in e["tokens"]:
        token_domain_count[t][folder] += 1

def vote_domain(tokens):
    scores = Counter()
    for t in tokens:
        dc = token_domain_count.get(t)
        if not dc:
            continue
        total = sum(dc.values())
        # 특정 도메인에 편중된 토큰일수록 가중치 ↑ (총 등장 도메인 수가 적을수록 신뢰)
        weight = 1.0 / math.log(2 + total)
        for folder, c in dc.items():
            scores[folder] += weight * c
    if not scores:
        return None
    return scores.most_common(1)[0][0]

# ---------- 4. 예상문제 폴더 도메인/하위도메인 배정 ----------
# 토큰 투표로 못 잡는 신조어/표준명은 수동 오버라이드 (제목 부분일치)
PRED_OVERRIDE = [
    ("C2PA", "정보보안", "5.8 신흥보안위협"),
    ("DPO (Direct Preference", "인공지능데이터", "7.4 생성형AI"),
    ("PagedAttention", "인공지능데이터", "7.5 신경망아키텍처"),
    ("QLoRA", "인공지능데이터", "7.4 생성형AI"),
    ("ROC 곡선과 AUC", "인공지능데이터", "7.6 통계적추론 및 검정"),
    ("Uptime Institute", "네트워크", "2.6 네트워크인프라"),
    ("가명정보 결합", "정보보안", "5.1 개인정보보호"),
    ("격자 기반 암호", "정보보안", "5.4 암호화"),
    ("계층적 군집분석", "인공지능데이터", "7.6 통계적추론 및 검정"),
    ("데이터센터 전력수급", "경영정보시스템", "1.6 클라우드정책거버넌스"),
    ("멀티암드 밴딧", "인공지능데이터", "7.6 통계적추론 및 검정"),
    ("메타데이터 등록소", "데이터베이스", "3.8 데이터거버넌스"),
    ("순환 중복 검사", "네트워크", "2.3 네트워크 프토토콜"),
    ("숨겨진 노드", "네트워크", "2.2 근거리무선통신"),
    ("업데이트 가능 뷰", "데이터베이스", "3.1 모델링"),
    ("이중 쓰기 버퍼", "데이터베이스", "3.4 회복기법"),
    ("인과 추론", "인공지능데이터", "7.6 통계적추론 및 검정"),
    ("일관성 해싱", "데이터베이스", "3.7 분산DB"),
    ("피처 스토어", "인공지능데이터", "7.2 AI데이터운영"),
    ("허니팟", "정보보안", "5.5 사이버위협"),
    ("6G 표준화", "네트워크", "2.4 이동통신기술"),
    ("CapEx와 OpEx", "경영정보시스템", "1.6 클라우드정책거버넌스"),
    ("DCGAN", "인공지능데이터", "7.5 신경망아키텍처"),
    ("Demographic Parity", "인공지능데이터", "7.1 AI거버넌스"),
    ("ES(Earned Schedule)", "경영정보시스템", "1.3 IT프로젝트관리"),
    ("FID (", "인공지능데이터", "7.5 신경망아키텍처"),
    ("GraphRAG", "인공지능데이터", "7.4 생성형AI"),
    ("HNSW", "인공지능데이터", "7.4 생성형AI"),
    ("JSD (", "인공지능데이터", "7.6 통계적추론 및 검정"),
    ("Shift-Left", "소프트웨어공학", "4.5 SW테스트"),
    ("뉴로모픽 반도체", "컴퓨터시스템", "6.5 차세대컴퓨팅"),
    ("디지털서비스 전문계약제도", "경영정보시스템", "1.6 클라우드정책거버넌스"),
    ("라우터 버퍼 혼잡", "네트워크", "2.3 네트워크 프토토콜"),
    ("메모리 예외 처리", "컴퓨터시스템", "6.3 메모리제어"),
    ("바이브 코딩", "소프트웨어공학", "4.1 개발방법론"),
    ("사이버보안 공시", "정보보안", "5.3 보안과제"),
    ("순환 중복 검사", "네트워크", "2.3 네트워크 프토토콜"),
    ("스플릿 브레인", "컴퓨터시스템", "6.4 동기화"),
    ("심리적 안전감", "경영정보시스템", "1.5 조직관리"),
    ("에이전틱 코딩", "소프트웨어공학", "4.8 AI개발"),
    ("온디바이스 NPU", "컴퓨터시스템", "6.5 차세대컴퓨팅"),
    ("저전력 리프레시", "컴퓨터시스템", "6.3 메모리제어"),
    ("전력반도체", "컴퓨터시스템", "6.5 차세대컴퓨팅"),
    ("콘텐츠 워터마킹", "정보보안", "5.8 신흥보안위협"),
    ("휴머노이드로봇", "컴퓨터시스템", "6.5 차세대컴퓨팅"),
]

def override_lookup(title):
    for key, folder, sub in PRED_OVERRIDE:
        if key in title:
            return folder, sub
    return None, None

pred_entries = []
uid = 0
unresolved = []
for p in pred_raw:
    ov_folder, ov_sub = override_lookup(p["title"])
    folder = ov_folder or vote_domain(p["tokens"])
    if folder is None:
        unresolved.append(p["title"])
        folder = "인공지능데이터"  # 최신기술 예상문제는 기본적으로 AI/신기술 비중이 높아 fallback
    dom = DOMAIN_BY_FOLDER[folder]
    subdomain = ov_sub or classify_subdomain(folder, p["name_noext"])
    uid += 1
    pred_entries.append({
        "id": f"pd-{uid:04d}",
        "mainDomain": dom["name"],
        "subDomain": subdomain,
        "keyword": p["title"],
        "sourceFile": f"141회예상문제/{p['fname']}",
        "rawContent": p["content"],
        "mnemonic": p["mnemonic"],
        "tokens": p["tokens"],
    })

print("predicted_entries:", len(pred_entries))
print("unresolved domain count:", len(unresolved))
print("sample unresolved:", unresolved[:15])

with open(os.path.join(OUT, "domain_entries.json"), "w", encoding="utf-8") as f:
    json.dump([{k: v for k, v in e.items() if k != "tokens"} for e in domain_entries], f, ensure_ascii=False, indent=1)
with open(os.path.join(OUT, "predicted_entries.json"), "w", encoding="utf-8") as f:
    json.dump([{k: v for k, v in e.items() if k != "tokens"} for e in pred_entries], f, ensure_ascii=False, indent=1)

# 토큰 정보는 다음 단계(기출대조)에서 재사용해야 하므로 pickle로 저장
import pickle
with open(os.path.join(OUT, "state.pkl"), "wb") as f:
    pickle.dump({
        "domain_entries": domain_entries,
        "pred_entries": pred_entries,
        "token_domain_count": dict(token_domain_count),
    }, f)

print("done stage1")
