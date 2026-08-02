\
# -*- coding: utf-8 -*-
import re

BASE64_IMG_RE = re.compile(r"!\[[^\]]*\]\(data:image[^)]*\)")
TRAILING_PROMPT_RE = re.compile(r"^.*(원하시면|만들어드릴까요|드릴까요|작성해드릴까요|필요하신가요)\??\s*$", re.MULTILINE)
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
MNEMONIC_LINE_RE = re.compile(r"(?:→\s*)?암기[:：]?\s*\**\"?(.+?)\"?\**\s*$", re.MULTILINE)
MNEMONIC_ARROW_RE = re.compile(r"암기용?\s*[\"“]?([^\n]{5,140})")

TOKEN_EN_RE = re.compile(r"[A-Za-z][A-Za-z0-9\-]{1,}")
TOKEN_KO_RE = re.compile(r"[가-힣]{2,}")

STOPWORDS_KO = set("""그리고 하지만 그러나 이것 저것 대한 대하여 대해 설명하시오 개념 정의 특징 방안 방법 종류 절차 구성 요소
비교 활용 도입 필요성 문제점 해결 위한 관리 시스템 기술 기법 서비스 기반 다음 내용 등에 등을 대응 전략 사업 사례
장점 단점 차이점 원리 구조 유형 모델 표준 정책 프로세스""".split())

STOPWORDS_EN = set("""the and for with that this from into your are was were will can may should must have has
설명 about""".split())


def strip_content(text: str) -> str:
    text = BASE64_IMG_RE.sub("", text)
    text = TRAILING_PROMPT_RE.sub("", text)
    return text.strip()


BAD_TITLE_MARKERS = ["답안 전개", "스토리", "핵심 압축", "숏폼", "머릿속 핵심", "핵심 요약", "요약 스토리", "실제 답안에 쓸", "암기용"]

def clean_filename_title(name_noext: str) -> str:
    t = name_noext.strip()
    t = re.sub(r"^\d+[\.\)]\s*", "", t)
    t = re.sub(r"_핵심키워드_정리$", "", t)
    t = re.sub(r"_키워드$", "", t)
    t = t.replace("_", " ").strip()
    return t or name_noext


def is_bad_title(t: str) -> bool:
    if any(b in t for b in BAD_TITLE_MARKERS):
        return True
    if re.match(r"^[IVXⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ]{1,4}[\.\s]", t):
        return True
    if len(t) > 60:
        return True
    return False


def extract_title(text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        t = m.group(1).strip()
        t = re.sub(r"^\*\*|\*\*$", "", t).strip()
        return t
    m2 = re.search(r"^###\s+\*\*(.+?)\*\*\s*$", text, re.MULTILINE)
    if m2:
        return m2.group(1).strip()
    return fallback


def extract_mnemonic(text: str, title: str) -> str:
    """본문에서 '암기' 라인을 찾아 2줄 이내로 압축"""
    candidates = []
    for m in re.finditer(r"암기[:：용]*\s*\**[\"“]?([^\n]{4,160})", text):
        c = m.group(1)
        c = c.replace("**", "").replace('"', "").replace(""", "").replace(""", "").strip()
        c = re.sub(r"\s*[-–—]\s*이.*$", "", c)
        if len(c) > 6:
            candidates.append(c)
    if candidates:
        # 가장 처음(보통 가장 핵심적인) + 필요시 두번째까지, 2줄 이내로 컷
        line1 = candidates[0][:110].strip()
        result = f"🔑 {line1}"
        if len(result) < 60 and len(candidates) > 1:
            line2 = candidates[1][:90].strip()
            result += f" / {line2}"
        return result.rstrip("/ ").strip()
    # fallback: 첫 문단 요약
    plain = re.sub(r"[#*>`_\[\]()]", "", text)
    plain = re.sub(r"\s+", " ", plain).strip()
    if plain:
        return f"🔑 {plain[:110]}"
    return f"🔑 {title} 핵심 개념을 압축 정리 (스토리 보강 필요)"


def tokenize(text: str):
    toks = set()
    for m in TOKEN_EN_RE.finditer(text):
        w = m.group(0).lower()
        if len(w) >= 2 and w not in STOPWORDS_EN:
            toks.add(w)
    for m in TOKEN_KO_RE.finditer(text):
        w = m.group(0)
        if w not in STOPWORDS_KO:
            toks.add(w)
    return toks
