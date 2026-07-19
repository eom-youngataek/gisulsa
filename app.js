// 정보처리기술사 학습 플랫폼 - app.js
// DOMAIN_STRUCTURE / KEYWORD_DATABASE / QUESTION_BANK 은 data.js 에서 로드됨

let state = {
  activeMainDomain: null,
  activeSubDomain: null,
  activeFilter: "all",
  searchTerm: "",
};

// ---------------- 유틸 ----------------
function escapeHtml(str) {
  return (str || "").replace(/[&<>"']/g, (c) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[c]));
}

function mdToHtml(md) {
  if (!md) return "";
  if (window.marked) {
    try {
      return marked.parse(md);
    } catch (e) {
      /* fallthrough */
    }
  }
  return `<pre class="raw-fallback">${escapeHtml(md)}</pre>`;
}

function countLabel(list) {
  return `총 ${list.length}개 검색됨`;
}

// ---------------- 사이드바: 도메인 계층 ----------------
function renderSidebar() {
  const root = document.getElementById("domain-accordion-list");
  root.innerHTML = "";
  DOMAIN_STRUCTURE.forEach((dom) => {
    const domCount = KEYWORD_DATABASE.filter((k) => k.mainDomain === dom.name).length;
    const domWrap = document.createElement("div");
    domWrap.className = "domain-group";

    const domBtn = document.createElement("button");
    domBtn.className = "domain-title" + (state.activeMainDomain === dom.name ? " active" : "");
    domBtn.innerHTML = `<span>${dom.name}</span><small>${domCount}</small>`;
    domBtn.addEventListener("click", () => {
      const willOpen = state.activeMainDomain !== dom.name;
      state.activeMainDomain = willOpen ? dom.name : null;
      state.activeSubDomain = null;
      renderSidebar();
      renderContent();
    });
    domWrap.appendChild(domBtn);

    if (state.activeMainDomain === dom.name) {
      const subList = document.createElement("div");
      subList.className = "subdomain-list";
      dom.subDomains.forEach((sub) => {
        const subCount = KEYWORD_DATABASE.filter((k) => k.mainDomain === dom.name && k.subDomain === sub).length;
        const subBtn = document.createElement("button");
        subBtn.className = "subdomain-item" + (state.activeSubDomain === sub ? " active" : "");
        subBtn.innerHTML = `<span>${sub}</span><small>${subCount}</small>`;
        subBtn.addEventListener("click", (e) => {
          e.stopPropagation();
          state.activeSubDomain = state.activeSubDomain === sub ? null : sub;
          renderSidebar();
          renderContent();
        });
        subList.appendChild(subBtn);
      });
      domWrap.appendChild(subList);
    }
    root.appendChild(domWrap);
  });
}

// ---------------- 필터링 로직 ----------------
function getFilteredList() {
  let list = KEYWORD_DATABASE;

  if (state.activeMainDomain) {
    list = list.filter((k) => k.mainDomain === state.activeMainDomain);
  }
  if (state.activeSubDomain) {
    list = list.filter((k) => k.subDomain === state.activeSubDomain);
  }
  if (state.activeFilter === "past") list = list.filter((k) => !k.isPredicted);
  if (state.activeFilter === "predicted") list = list.filter((k) => k.isPredicted);
  if (state.activeFilter === "type1") list = list.filter((k) => k.questionType === "1교시형");
  if (state.activeFilter === "type2") list = list.filter((k) => k.questionType === "2~4교시형");

  const term = state.searchTerm.trim().toLowerCase();
  if (term) {
    list = list.filter((k) => {
      return (
        (k.keyword || "").toLowerCase().includes(term) ||
        (k.mnemonic || "").toLowerCase().includes(term) ||
        (k.subDomain || "").toLowerCase().includes(term) ||
        (k.mainDomain || "").toLowerCase().includes(term) ||
        (k.rawContent || "").toLowerCase().includes(term) ||
        (k.questionText || "").toLowerCase().includes(term)
      );
    });
  }
  return list;
}

function renderContent() {
  const list = getFilteredList();
  const titleEl = document.getElementById("current-category-title");
  if (state.activeSubDomain) titleEl.textContent = state.activeSubDomain;
  else if (state.activeMainDomain) titleEl.textContent = state.activeMainDomain;
  else titleEl.textContent = "전체 모범답안 및 키워드 목록";

  document.getElementById("keyword-count-badge").textContent = countLabel(list);

  const grid = document.getElementById("keyword-card-grid");
  grid.innerHTML = "";

  if (list.length === 0) {
    grid.innerHTML = `<div class="empty-state">검색 결과가 없습니다. 다른 키워드로 시도해보세요.</div>`;
    return;
  }

  const frag = document.createDocumentFragment();
  list.slice(0, 300).forEach((k) => {
    const card = document.createElement("div");
    card.className = "keyword-card";
    card.innerHTML = `
      <div class="card-top">
        <span class="badge badge-sub">${escapeHtml(k.subDomain)}</span>
        ${k.isPredicted
          ? `<span class="badge badge-predicted"><i class="fa-solid fa-bolt"></i> 미출제 예상</span>`
          : `<span class="badge badge-past"><i class="fa-solid fa-check"></i> 기출</span>`}
      </div>
      <h3 class="card-title">${escapeHtml(k.keyword)}</h3>
      <p class="card-mnemonic">${escapeHtml(k.mnemonic || "")}</p>
      <div class="card-bottom">
        <span class="card-history">${escapeHtml(k.examHistory || "")}</span>
        <span class="card-qtype">${escapeHtml(k.questionType || "")}</span>
      </div>
    `;
    card.addEventListener("click", () => openDetailModal(k));
    frag.appendChild(card);
  });
  grid.appendChild(frag);
}

// ---------------- 상세 모달 ----------------
function openDetailModal(k) {
  document.getElementById("modal-domain-tag").textContent = k.mainDomain;
  document.getElementById("modal-subdomain-tag").textContent = k.subDomain;
  document.getElementById("modal-history-tag").textContent = k.examHistory || "";
  document.getElementById("modal-keyword-title").textContent = k.keyword;
  document.getElementById("modal-question-text").textContent =
    k.questionText && k.questionText.trim() ? k.questionText : `${k.keyword}에 대하여 설명하시오.`;
  document.getElementById("modal-mnemonic-text").textContent = k.mnemonic || "";

  const body = document.querySelector("#modal-answer-detail .answer-template");
  if (k.structured && k.solution) {
    body.innerHTML = `
      <div class="answer-section"><h3>Ⅰ. 개요 및 배경</h3><div class="section-content">${escapeHtml(k.solution.section1 || "").replace(/\n/g, "<br>")}</div></div>
      <div class="answer-section"><h3>Ⅱ. 핵심 기술 및 구성요소</h3><div class="section-content">${escapeHtml(k.solution.section2 || "").replace(/\n/g, "<br>")}</div></div>
      <div class="answer-section"><h3>Ⅲ. 구축 절차 및 프로세스 / 알고리즘</h3><div class="section-content">${escapeHtml(k.solution.section3 || "").replace(/\n/g, "<br>")}</div></div>
      <div class="answer-section"><h3>Ⅳ. 활용사례 및 고려사항 / 향후 발전방향</h3><div class="section-content">${escapeHtml(k.solution.section4 || "").replace(/\n/g, "<br>")}</div></div>
    `;
  } else {
    body.innerHTML = `
      <div class="answer-section raw-note">
        <span class="raw-note-tag"><i class="fa-solid fa-file-lines"></i> 원본 학습노트 (자동 수집 · 하네스로 지속 보강 예정)</span>
      </div>
      <div class="markdown-body">${mdToHtml(k.rawContent)}</div>
    `;
  }

  document.getElementById("btn-copy-answer").onclick = () => {
    const text = k.structured && k.solution
      ? [k.solution.section1, k.solution.section2, k.solution.section3, k.solution.section4].join("\n\n")
      : k.rawContent;
    navigator.clipboard && navigator.clipboard.writeText(text).catch(() => {});
  };

  document.getElementById("modal-answer-detail").classList.add("open");
}

// ---------------- 무작위 모의고사 생성기 ----------------
function pickRandom(arr, n) {
  const shuffled = [...arr].sort(() => 0.5 - Math.random());
  return shuffled.slice(0, n);
}

function generateExamPaper(examType) {
  if (examType === "1교시형") {
    // 실제 기출(1교시) + 예상 키워드(1교시형) 혼합 10문제
    const realQ = QUESTION_BANK.filter((q) => q.session === "1교시");
    const realPicks = pickRandom(realQ, 6).map((q) => ({
      kind: "기출",
      round: q.round,
      text: q.text,
    }));
    const kwPicks = pickRandom(
      KEYWORD_DATABASE.filter((k) => k.questionType === "1교시형"),
      4
    ).map((k) => ({
      kind: k.isPredicted ? "예상" : "기출연계",
      round: k.examHistory,
      text: k.questionText && k.questionText.trim() ? k.questionText : `${k.keyword}에 대하여 설명하시오.`,
    }));
    return [...realPicks, ...kwPicks].sort(() => 0.5 - Math.random());
  } else {
    // 2~4교시형: 실제 기출 에세이 2문항 + 예상 키워드 기반 2문항, 총 4문항
    const realQ = QUESTION_BANK.filter((q) => q.session !== "1교시");
    const realPicks = pickRandom(realQ, 2).map((q) => ({
      kind: "기출",
      round: `${q.round}회 ${q.session}`,
      text: q.text,
    }));
    const kwPicks = pickRandom(
      KEYWORD_DATABASE.filter((k) => k.questionType === "2~4교시형"),
      2
    ).map((k) => ({
      kind: k.isPredicted ? "예상" : "기출연계",
      round: k.examHistory,
      text: k.questionText && k.questionText.trim() ? k.questionText : `${k.keyword}에 대하여 다음을 설명하시오.`,
    }));
    return [...realPicks, ...kwPicks].sort(() => 0.5 - Math.random());
  }
}

function renderExamPaper(examType) {
  const items = generateExamPaper(examType);
  const container = document.getElementById("exam-paper-container");
  const scoreEach = examType === "1교시형" ? 10 : 25;
  container.innerHTML = `
    <div class="exam-paper-header">
      <h3>정보처리기술사 무작위 모의고사 (${escapeHtml(examType)})</h3>
      <p>문항당 배점 ${scoreEach}점 · 총 ${items.length}문항 · 실제 기출 + 최신 미출제 예상문제 혼합 출제</p>
    </div>
    <ol class="exam-item-list">
      ${items
        .map(
          (it, idx) => `
        <li class="exam-item">
          <div class="exam-item-head">
            <span class="exam-item-num">${idx + 1}</span>
            <span class="exam-item-badge badge-${it.kind === "예상" ? "predicted" : "past"}">${escapeHtml(it.kind)}${it.round ? " · " + escapeHtml(it.round) : ""}</span>
          </div>
          <p class="exam-item-text">${escapeHtml(it.text)}</p>
        </li>`
        )
        .join("")}
    </ol>
  `;
}

// ---------------- 이벤트 바인딩 ----------------
function bindEvents() {
  document.getElementById("btn-reset-filter").addEventListener("click", () => {
    state.activeMainDomain = null;
    state.activeSubDomain = null;
    renderSidebar();
    renderContent();
  });

  document.getElementById("search-input").addEventListener("input", (e) => {
    state.searchTerm = e.target.value;
    renderContent();
  });
  document.getElementById("search-clear-btn").addEventListener("click", () => {
    state.searchTerm = "";
    document.getElementById("search-input").value = "";
    renderContent();
  });

  document.querySelectorAll(".filter-pills .pill").forEach((pill) => {
    pill.addEventListener("click", () => {
      document.querySelectorAll(".filter-pills .pill").forEach((p) => p.classList.remove("active"));
      pill.classList.add("active");
      state.activeFilter = pill.dataset.filter;
      renderContent();
    });
  });

  document.getElementById("modal-close-btn").addEventListener("click", () => {
    document.getElementById("modal-answer-detail").classList.remove("open");
  });
  document.querySelector("#modal-answer-detail .modal-overlay").addEventListener("click", () => {
    document.getElementById("modal-answer-detail").classList.remove("open");
  });

  document.getElementById("btn-open-exam-modal").addEventListener("click", () => {
    document.getElementById("modal-mock-exam").classList.add("open");
    renderExamPaper(document.getElementById("exam-type-select").value);
  });
  document.getElementById("modal-exam-close-btn").addEventListener("click", () => {
    document.getElementById("modal-mock-exam").classList.remove("open");
  });
  document.querySelector("#modal-mock-exam .modal-overlay").addEventListener("click", () => {
    document.getElementById("modal-mock-exam").classList.remove("open");
  });
  document.getElementById("btn-generate-exam").addEventListener("click", () => {
    renderExamPaper(document.getElementById("exam-type-select").value);
  });

  document.getElementById("btn-harness-info").addEventListener("click", () => {
    document.getElementById("modal-harness").classList.add("open");
  });
  document.getElementById("modal-harness-close-btn").addEventListener("click", () => {
    document.getElementById("modal-harness").classList.remove("open");
  });
  document.querySelector("#modal-harness .modal-overlay").addEventListener("click", () => {
    document.getElementById("modal-harness").classList.remove("open");
  });

  // 실제 기출문제 원문 브라우저
  const examBrowseBtn = document.getElementById("btn-open-qbank-modal");
  if (examBrowseBtn) {
    examBrowseBtn.addEventListener("click", () => {
      document.getElementById("modal-qbank").classList.add("open");
      renderQBankRoundOptions();
      renderQBankList();
    });
    document.getElementById("modal-qbank-close-btn").addEventListener("click", () => {
      document.getElementById("modal-qbank").classList.remove("open");
    });
    document.querySelector("#modal-qbank .modal-overlay").addEventListener("click", () => {
      document.getElementById("modal-qbank").classList.remove("open");
    });
    document.getElementById("qbank-round-select").addEventListener("change", renderQBankList);
    document.getElementById("qbank-search-input").addEventListener("input", renderQBankList);
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      document.querySelectorAll(".modal.open").forEach((m) => m.classList.remove("open"));
    }
  });
}

function renderQBankRoundOptions() {
  const sel = document.getElementById("qbank-round-select");
  if (sel.dataset.filled) return;
  const rounds = [...new Set(QUESTION_BANK.map((q) => q.round))].sort((a, b) => b - a);
  sel.innerHTML = `<option value="">전체 회차 (120~139회)</option>` + rounds.map((r) => `<option value="${r}">${r}회</option>`).join("");
  sel.dataset.filled = "1";
}

function renderQBankList() {
  const round = document.getElementById("qbank-round-select").value;
  const term = document.getElementById("qbank-search-input").value.trim().toLowerCase();
  let list = QUESTION_BANK;
  if (round) list = list.filter((q) => q.round === round);
  if (term) list = list.filter((q) => q.text.toLowerCase().includes(term));

  const wrap = document.getElementById("qbank-list");
  wrap.innerHTML = `<div class="qbank-count">${list.length}개 문항</div>` + list
    .slice(0, 200)
    .map(
      (q) => `
      <div class="qbank-item">
        <span class="badge badge-past">${q.round}회 ${q.subjectTrack} · ${q.session} ${q.num}번</span>
        <p>${escapeHtml(q.text)}</p>
      </div>`
    )
    .join("");
}

// ---------------- 초기화 ----------------
document.addEventListener("DOMContentLoaded", () => {
  renderSidebar();
  renderContent();
  bindEvents();
});
