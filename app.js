/* Make Yourself Expensive — app logic.
   GPL-3.0, (C) 2026 Transparency Cascade Press.
   No network calls except loading the bundled broker list. No analytics. State = localStorage. */
"use strict";

const STORE = "mye.v1";
const state = JSON.parse(localStorage.getItem(STORE) || "{}");
const save = () => localStorage.setItem(STORE, JSON.stringify(state));
const $ = (s) => document.querySelector(s);

// Privacy-respecting aggregate event (Plausible). No user/PII — just a count, to answer the
// one Phase-2 question: is the tool being USED, not just visited. No-op if Plausible isn't loaded.
const track = (event, props) => { try { window.plausible && window.plausible(event, props ? {props} : undefined); } catch (e) {} };

/* ---- the three batches (the long list, made finishable). The tool does ONE job: broker opt-out.
   Device/comms hardening lives in the Harden Your Device series, linked from the page. ---- */
const TIERS = [
  {key: "crucial", label: "Start here — the ones that matter most",
   blurb: "People-search sites that resell your home address. Clearing these does most of the work. If you only do one batch, do this one."},
  {key: "high", label: "Next — other one-click opt-outs",
   blurb: "More brokers with a working opt-out link. Quick wins once the crucial batch is done."},
  {key: "tail", label: "Going deeper — the long tail",
   blurb: "Hundreds more brokers with no one-click link — opt out by their listed method, or search their name. Optional, and never-ending by design. Do as many as you like; you don't have to finish."},
];

let BROKERS = [], filterLink = false, query = "", openTail = false;
const TAIL_PAGE = 50; let tailShown = TAIL_PAGE;

/* ---- triage (tailors emphasis; still useful — higher-risk people prioritize the address-resellers) ---- */
document.querySelectorAll("#triage .choice").forEach((b) =>
  b.addEventListener("click", () => { state.tier = b.dataset.tier; save(); track("triage", {tier: b.dataset.tier}); startTool(); }));

$("#reset").addEventListener("click", () => {
  if (!confirm("Clear your progress on this device and start over?")) return;
  localStorage.removeItem(STORE); location.reload();
});

function startTool() {
  $("#triage").classList.add("hidden");
  $("#plan").classList.remove("hidden");
  loadBrokers();
}

/* ---- broker list ---- */
async function loadBrokers() {
  if (!BROKERS.length) {
    try {
      const r = await fetch("data/brokers.json");
      const d = await r.json();
      BROKERS = d.brokers || [];
    } catch (e) {
      $("#brokers").innerHTML = `<p class="ledger-meta">Couldn&rsquo;t load the register. You can still use <a href="https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List" style="color:var(--seal)">Yael Grauer&rsquo;s list</a> directly.</p>`;
      return;
    }
  }
  renderBatches();
}

/* ---- optional: load Yael Grauer's BADBOOL list (CC BY-NC-SA) at the user's choice.
   We do NOT bundle it (license incompatibility with GPL); the user fetches our maintained
   structured fork of it. This merges its higher-quality opt-out links over the roster. ---- */
const BADBOOL_URL = "https://raw.githubusercontent.com/markramm/Big-Ass-Data-Broker-Opt-Out-List/structured-data/data/badbool.json";
async function loadBadbool() {
  const btn = $("#load-badbool");
  if (btn) { btn.disabled = true; btn.textContent = "Loading…"; }
  try {
    const r = await fetch(BADBOOL_URL);
    const d = await r.json();
    const byName = {};
    BROKERS.forEach(b => { byName[(b.name || "").toLowerCase()] = b; byName[(b.domain || "").toLowerCase()] = b; });
    let added = 0, improved = 0;
    (d.brokers || []).forEach(e => {
      const key = (e.name || "").toLowerCase();
      const dom = (e.opt_out_url || "").replace(/^https?:\/\//, "").split("/")[0].toLowerCase();
      const match = byName[key] || byName[dom];
      const norm = {
        name: e.name, domain: dom || key, category: e.section || "People Search",
        people_search: /people|search|directory/i.test(e.section || ""),
        opt_out_url: e.opt_out_url || "", opt_out_method: e.instructions ? "see instructions" : "",
        crucial: e.crucial, requires_id: e.requires_id, charges_money: e.charges_money,
        has_link: !!e.opt_out_url, has_method: !!(e.opt_out_url || e.instructions),
        source: "badbool",
      };
      if (match) {
        if (norm.opt_out_url && norm.opt_out_url !== match.opt_out_url) { match.opt_out_url = norm.opt_out_url; match.has_link = true; match.source += " + badbool"; match.crucial = norm.crucial; improved++; }
      } else { BROKERS.push(norm); added++; }
    });
    // re-sort: crucial + linked first
    BROKERS.sort((a, b) => (Number(!(a.crucial && a.has_link)) - Number(!(b.crucial && b.has_link)))
      || (Number(!a.has_link) - Number(!b.has_link)) || (a.name || "").localeCompare(b.name || ""));
    // re-tier any newly added/improved brokers
    BROKERS.forEach(b => { b.tier = (b.has_link && b.people_search) ? "crucial" : b.has_link ? "high" : "tail"; });
    state.badbool_loaded = true; save();
    if (btn) btn.outerHTML = `<span class="ledger-meta">✓ BADBOOL loaded · ${added} added · ${improved} improved · Yael Grauer, CC BY-NC-SA</span>`;
    renderBatches();
  } catch (e) {
    if (btn) { btn.disabled = false; btn.textContent = "Couldn't load — open the list directly"; btn.onclick = () => window.open("https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List"); }
  }
}

function filtered() {
  let list = BROKERS;
  if (filterLink) list = list.filter(b => b.has_link);
  if (query) {
    const q = query.toLowerCase();
    list = list.filter(b => (b.name + " " + b.domain + " " + b.category).toLowerCase().includes(q));
  }
  return list;
}

function esc(s){ return String(s||"").replace(/[<>&"]/g, c=>({"<":"&lt;",">":"&gt;","&":"&amp;",'"':"&quot;"}[c])); }

const isDone = (b) => !!state["b:" + b.domain];
const tierBrokers = (key) => {
  let list = BROKERS.filter(b => b.tier === key);
  if (query) { const q = query.toLowerCase(); list = list.filter(b => (b.name + " " + b.domain + " " + b.category).toLowerCase().includes(q)); }
  return list;
};

function brokerRow(b) {
  const done = isDone(b);
  const usableLink = b.opt_out_url && b.link_status !== "broken";
  const unconfirmed = b.link_status === "tcp-unconfirmed";
  const action = (usableLink || unconfirmed) && b.opt_out_url
    ? `<a href="${esc(b.opt_out_url)}" target="_blank" rel="noopener">opt out &rarr;</a>`
    : (b.opt_out_method || b.phone
        ? `<span class="note">${esc(b.opt_out_method || ("call " + b.phone))}</span>`
        : `<span class="note">search it</span>`);
  const tag = unconfirmed ? `<span class="tag manual">unverified link</span>`
            : usableLink ? `<span class="tag${b.crucial ? " crucial" : ""}">${b.crucial ? "crucial" : "1-click"}</span>`
            : b.has_method ? `<span class="tag manual">manual</span>` : "";
  const ps = b.people_search ? `<span class="ps">people-search</span>` : "";
  return `<div class="brk ${done ? "done" : ""}">
    <button class="strike-btn" data-b="${esc(b.domain)}" aria-pressed="${done}"
      title="${done ? "Un-strike" : "Strike this broker off once you've opted out"}">${done ? "✕" : ""}</button>
    <span class="body">
      <button class="nm-btn" data-b="${esc(b.domain)}"><span class="nm">${esc(b.name)}</span></button>
      ${tag} ${ps}</span>
    <span class="act">${done ? "struck" : action}</span></div>`;
}

function renderBatches() {
  const total = BROKERS.length, struck = BROKERS.filter(isDone).length;
  if ($("#tally")) $("#tally").innerHTML = total
    ? `You have struck <b>${struck}</b> of <b>${total}</b> brokers from your file.`
    : `Building your file…`;

  $("#brokers").innerHTML = TIERS.map(t => {
    const all = tierBrokers(t.key);
    if (!all.length) return "";
    const done = all.filter(isDone).length;
    const pct = all.length ? Math.round(100 * done / all.length) : 0;
    const cleared = done === all.length && all.length > 0;
    // the tail is collapsible + paginated; crucial/high render in full (small enough)
    const isTail = t.key === "tail";
    const rows = isTail
      ? (openTail ? all.slice(0, tailShown).map(brokerRow).join("") : "")
      : all.map(brokerRow).join("");
    const milestone = cleared
      ? `<span class="milestone">✓ batch cleared — nice work</span>`
      : `<span class="batch-count">${done} of ${all.length} done</span>`;
    const tailToggle = isTail
      ? `<button class="tail-toggle" data-tail="1">${openTail ? "Hide" : "Show"} the long list (${all.length})</button>`
      : "";
    const tailMore = (isTail && openTail && tailShown < all.length)
      ? `<p><button class="load-more" data-more="1">Show more (${all.length - tailShown} left)</button></p>` : "";
    return `<section class="batch ${cleared ? "cleared" : ""}">
      <div class="batch-head">
        <h3>${t.label}</h3>
        ${milestone}
      </div>
      <p class="batch-blurb">${t.blurb} ${tailToggle}</p>
      <div class="batch-bar"><span style="width:${pct}%"></span></div>
      ${rows}${tailMore}
    </section>`;
  }).join("");

  // wire strike toggles
  const toggle = (dom) => { state["b:" + dom] = !state["b:" + dom]; save(); renderBatches(); };
  $("#brokers").querySelectorAll("[data-b]").forEach(el =>
    el.addEventListener("click", e => { e.preventDefault(); toggle(el.dataset.b); }));
  $("#brokers").querySelectorAll(".act a").forEach(a =>
    a.addEventListener("click", () => track("opt-out-click")));
  $("#brokers").querySelector("[data-tail]")?.addEventListener("click", () => { openTail = !openTail; tailShown = TAIL_PAGE; renderBatches(); });
  $("#brokers").querySelector("[data-more]")?.addEventListener("click", () => { tailShown += TAIL_PAGE; renderBatches(); });

  if ($("#progress-label")) $("#progress-label").innerHTML = `<b>${struck}</b> struck`;
}

$("#search")?.addEventListener("input", (e) => { query = e.target.value; renderBatches(); });
$("#load-badbool")?.addEventListener("click", loadBadbool);

/* ---- boot ---- */
if (state.tier) startTool();
