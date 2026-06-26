/* Make Yourself Expensive — app logic.
   GPL-3.0, (C) 2026 Transparency Cascade Press.
   No network calls except loading the bundled broker list. No analytics. State = localStorage. */
"use strict";

const STORE = "mye.v1";
const state = JSON.parse(localStorage.getItem(STORE) || "{}");
const save = () => localStorage.setItem(STORE, JSON.stringify(state));
const $ = (s) => document.querySelector(s);

/* ---- the routing tree (sourced from the field-guide research; Tier A = everyone, B = higher-risk) ---- */
const MOVES = {
  A: [
    ["remove", "Remove your data from brokers", "The highest-leverage move — broker data is what feeds government surveillance and targeting. Use the list below.", null],
    ["signal", "Switch messaging to Signal", "Protects message content and metadata. Not anonymity.", "https://signal.org"],
    ["email", "Move email to Proton or Tuta", "Off Gmail's read-you business model. Protects content, not your identity.", "https://proton.me/mail"],
    ["browser", "Use Firefox (hardened)", "Independent, nonprofit, not Chromium. Turn on Enhanced Tracking Protection.", "https://www.mozilla.org/firefox/"],
    ["search", "Default search to DuckDuckGo or Startpage", "Off Google as your default.", "https://duckduckgo.com"],
    ["vpn", "Don't oversell a VPN to yourself", "A VPN is not anonymity. If you want one, the audited picks are Mullvad / IVPN / Mozilla VPN.", "https://mullvad.net"],
  ],
  B: [
    ["tor", "Use Tor Browser for anonymity", "Signal/Proton/VPN raise your baseline but don't make you anonymous. Tor does.", "https://www.torproject.org"],
    ["compartment", "Compartmentalize identities", "Separate accounts/devices/numbers for organizing vs. personal life. Signal usernames over phone numbers.", null],
    ["device", "Device discipline", "Full-disk encryption. Strong passcodes — not just biometrics (those can be compelled at a border or arrest). Carry a minimal phone to actions.", null],
    ["ssd", "Read EFF's Surveillance Self-Defense", "The canonical guide for at-risk people. Don't improvise this tier.", "https://ssd.eff.org"],
    ["ambient", "Know the ambient layer is political", "Doorbell cams and license-plate readers aren't a personal setting — push local ALPR ordinances and agencies off Flock/Ring.", null],
  ],
};
/* California gets an extra top move */
const CA_MOVE = ["ca-drop", "California: use the state DROP tool", "Free, government-run: one deletion request every registered broker must legally honor (processing from Aug 1, 2026).", "https://privacy.ca.gov/"];

let BROKERS = [], shown = 0, PAGE = 40, filterLink = false, query = "";

/* ---- triage ---- */
document.querySelectorAll("#triage .choice").forEach((b) =>
  b.addEventListener("click", () => { state.tier = b.dataset.tier; save(); renderPlan(); }));

$("#reset").addEventListener("click", () => {
  if (!confirm("Clear your progress on this device and start over?")) return;
  localStorage.removeItem(STORE); location.reload();
});

function renderPlan() {
  $("#triage").classList.add("hidden");
  $("#plan").classList.remove("hidden");
  const tier = state.tier || "A";
  let moves = [...MOVES.A];
  if (tier === "B") moves = [...MOVES.A.filter(m => m[0] === "remove"), ...MOVES.B, ...MOVES.A.filter(m => m[0] !== "remove")];
  const html = `<div class="mhead">Your plan · ${tier === "B" ? "high-risk file" : "standard file"}</div>` +
    moves.map(([id, title, desc, url]) => {
      const done = !!state["move:" + id];
      return `<div class="step ${done ? "done" : ""}">
        <input type="checkbox" id="m_${id}" data-move="${id}" ${done ? "checked" : ""}>
        <label for="m_${id}"><span class="t">${title}</span>
        <span class="d">${desc}${url ? ` <a class="go" href="${url}" target="_blank" rel="noopener">open &rarr;</a>` : ""}</span></label></div>`;
    }).join("");
  $("#moves").innerHTML = html;
  $("#moves").querySelectorAll("input[data-move]").forEach((i) =>
    i.addEventListener("change", () => { state["move:" + i.dataset.move] = i.checked; save(); renderPlan(); updateProgress(); }));
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
  shown = PAGE;
  renderBrokers();
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
    state.badbool_loaded = true; save();
    if (btn) btn.outerHTML = `<span class="ledger-meta">✓ BADBOOL loaded · ${added} added · ${improved} improved · Yael Grauer, CC BY-NC-SA</span>`;
    shown = PAGE; renderBrokers();
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

function renderBrokers() {
  const list = filtered();
  const slice = list.slice(0, shown);
  const doneN = list.filter(b => state["b:" + b.domain]).length;
  $("#broker-count").textContent =
    `${list.length} in register · ${doneN} struck · ${BROKERS.filter(b => b.has_link).length} one-click opt-outs available`;
  $("#brokers").innerHTML = slice.map((b, i) => {
    const done = !!state["b:" + b.domain];
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
    const idx = String(i + 1).padStart(2, "0");
    return `<label class="brk ${done ? "done" : ""}">
      <input type="checkbox" data-b="${esc(b.domain)}" ${done ? "checked" : ""}>
      <span class="ix">${idx}</span>
      <span class="body"><span class="nm">${esc(b.name)}</span> ${tag} ${ps}</span>
      <span class="act">${done ? "struck" : action}</span></label>`;
  }).join("");
  $("#brokers").querySelectorAll("input[data-b]").forEach((i) =>
    i.addEventListener("change", () => { state["b:" + i.dataset.b] = i.checked; save(); renderBrokers(); updateProgress(); }));
  $("#load-more-wrap").style.display = shown < list.length ? "" : "none";
  updateProgress();
}

$("#load-more").addEventListener("click", () => { shown += PAGE; renderBrokers(); });
$("#search").addEventListener("input", (e) => { query = e.target.value; shown = PAGE; renderBrokers(); });
$("#filter-link").addEventListener("click", () => { filterLink = true; shown = PAGE; renderBrokers(); });
$("#filter-all").addEventListener("click", () => { filterLink = false; shown = PAGE; renderBrokers(); });
$("#load-badbool")?.addEventListener("click", loadBadbool);

/* ---- progress (moves + the people-search-with-link brokers, the high-impact core) ---- */
function updateProgress() {
  // the tally counts brokers STRUCK from the register (the page's heartbeat)
  const struck = BROKERS.filter(b => state["b:" + b.domain]).length;
  const reg = BROKERS.length;
  const tier = state.tier || "A";
  const moveIds = (tier === "B" ? [...MOVES.A, ...MOVES.B] : MOVES.A).map(m => m[0]);
  const core = BROKERS.filter(b => b.people_search && b.has_link); // high-impact actionable set
  const total = moveIds.length + core.length;
  const done = moveIds.filter(id => state["move:" + id]).length +
               core.filter(b => state["b:" + b.domain]).length;
  const pct = total ? Math.round(100 * done / total) : 0;
  const tallyEl = $("#tally");
  if (tallyEl) tallyEl.innerHTML = reg
    ? `You have struck <b>${struck}</b> of <b>${reg}</b> brokers from your file.`
    : `Building your file…`;
  if ($("#bar")) $("#bar").style.width = pct + "%";
  if ($("#progress-label")) $("#progress-label").innerHTML = `<b>${struck}</b> struck · ${pct}% of high-impact steps`;
}

/* ---- boot ---- */
if (state.tier) renderPlan();
