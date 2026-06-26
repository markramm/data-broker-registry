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
  // (CA move surfaced inside the broker section header; kept simple for v1)
  const html = `<div class="card"><h2 style="margin-top:0">Your plan</h2>` +
    moves.map(([id, title, desc, url]) => {
      const done = !!state["move:" + id];
      return `<div class="step ${done ? "done" : ""}">
        <input type="checkbox" data-move="${id}" ${done ? "checked" : ""}>
        <label><strong>${title}</strong><br><span class="muted">${desc}</span>
        ${url ? ` <a class="txt" href="${url}" target="_blank" rel="noopener">open &rarr;</a>` : ""}</label></div>`;
    }).join("") + `</div>`;
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
      $("#brokers").innerHTML = `<p class="muted">Couldn't load the broker list. You can still use
        <a class="txt" href="https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List">Yael Grauer's list</a> directly.</p>`;
      return;
    }
  }
  shown = PAGE;
  renderBrokers();
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

function renderBrokers() {
  const list = filtered();
  const slice = list.slice(0, shown);
  $("#broker-count").textContent =
    `${list.length} brokers shown · ${list.filter(b => state["b:" + b.domain]).length} done · ` +
    `${BROKERS.filter(b => b.has_link).length} have one-click opt-outs`;
  $("#brokers").innerHTML = slice.map((b) => {
    const done = !!state["b:" + b.domain];
    const action = b.opt_out_url
      ? `<a href="${b.opt_out_url}" target="_blank" rel="noopener">opt out &rarr;</a>`
      : (b.opt_out_method || b.phone
          ? `<span class="note">${b.opt_out_method || ("call " + b.phone)}</span>`
          : `<span class="note">search "${b.name} opt out"</span>`);
    const pill = b.has_link ? `<span class="pill">1-click</span>`
               : b.has_method ? `<span class="pill method">manual</span>` : "";
    return `<div class="broker ${done ? "done" : ""}">
      <input type="checkbox" data-b="${b.domain}" ${done ? "checked" : ""}>
      <span class="name">${b.name} ${pill} ${b.people_search ? '<span class="note">· people-search</span>' : ""}</span>
      ${action}</div>`;
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

/* ---- progress (moves + the people-search-with-link brokers, the high-impact core) ---- */
function updateProgress() {
  const tier = state.tier || "A";
  const moveIds = (tier === "B" ? [...MOVES.A, ...MOVES.B] : MOVES.A).map(m => m[0]);
  const core = BROKERS.filter(b => b.people_search && b.has_link); // the high-impact actionable set
  const total = moveIds.length + core.length;
  const done = moveIds.filter(id => state["move:" + id]).length +
               core.filter(b => state["b:" + b.domain]).length;
  const pct = total ? Math.round(100 * done / total) : 0;
  $("#bar").style.width = pct + "%";
  $("#progress-label").textContent = `${done} of ${total} high-impact steps done (${pct}%)`;
}

/* ---- boot ---- */
if (state.tier) renderPlan();
