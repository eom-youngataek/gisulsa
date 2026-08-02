#!/usr/bin/env bash
# gisulsa 데이터 파이프라인 전체 재실행 스크립트
# 사용법: cd gisulsa/scripts && bash run_all.sh
set -e
cd "$(dirname "$0")"
echo "[0/4] 실제 기출문제(120~139회) 파싱..."
python3 00_parse_exam_questions.py
echo "[1/4] 도메인 폴더(7개) 파싱/분류..."
python3 01_parse_domains.py
echo "[2/4] 기출문제 도메인 분류 + 기출/예상 대조 태깅..."
python3 02_classify_and_tag.py
echo "[3/4] 최종 필드 정리(questionType/examHistory/source)..."
python3 03_finalize_and_tag.py
echo "[4/4] data.js 조립..."
python3 04_assemble_data_js.py
echo "완료! 사이트 루트의 data.js 가 갱신되었습니다."
