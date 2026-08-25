const SCORE_LABEL = {
  unscored: "Pending Maps",
  keep: "Keep",
  kill: "Kill",
};

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function formatAsOf(iso) {
  const date = new Date(`${iso}T12:00:00`);
  if (Number.isNaN(date.getTime())) return iso;
  return new Intl.DateTimeFormat("en-US", {
    weekday: "long",
    month: "long",
    day: "numeric",
    year: "numeric",
  }).format(date);
}

function scoreClass(score) {
  if (score === "keep" || score === "kill") return score;
  return "unscored";
}

function scoreLabel(score) {
  return SCORE_LABEL[score] ?? SCORE_LABEL.unscored;
}

function renderTicket(shop) {
  const score = scoreClass(shop.score);
  return `
    <article class="ticket ticket--${score}" data-id="${escapeHtml(shop.id)}">
      <span class="ticket__stub" aria-hidden="true"></span>
      <div class="ticket__body">
        <h4 class="ticket__name">${escapeHtml(shop.name)}</h4>
        <p class="stamp stamp--${score}">${escapeHtml(scoreLabel(score))}</p>
      </div>
    </article>
  `;
}

function renderTrade(trade) {
  return `
    <div class="lane">
      <h3 class="lane__title">${escapeHtml(trade.label)}</h3>
      <div class="lane__list">
        ${trade.names.map(renderTicket).join("")}
      </div>
    </div>
  `;
}

function renderPipeline(ghl) {
  const stages = ghl.stages
    .map(
      (label) => `
        <li class="rail__stage">
          <span class="rail__count" title="No opportunities counted yet">empty</span>
          <span class="rail__label">${escapeHtml(label)}</span>
        </li>
      `,
    )
    .join("");

  return `
    <ol class="rail">
      ${stages}
    </ol>
  `;
}

function renderBoard(data) {
  const asOf = formatAsOf(data.asOf);
  const scored = data.firstWave.trades
    .flatMap((trade) => trade.names)
    .filter((shop) => shop.score === "keep" || shop.score === "kill").length;
  const total = data.firstWave.trades.reduce((sum, trade) => sum + trade.names.length, 0);

  return `
    <a class="skip" href="#today">Skip to today</a>

    <header class="mast">
      <div class="mast__meta">
        <p class="mast__site">${escapeHtml(data.company.site)}</p>
        <p class="mast__city">${escapeHtml(data.company.city)}</p>
      </div>
      <div class="mast__brand">
        <p class="neon-badge">24 HR</p>
        <h1 class="wordmark">${escapeHtml(data.company.name)}</h1>
        <p class="mast__offer">Ads-to-phone for Vegas trades. ${escapeHtml(data.offer.adsToPhone)} · ${escapeHtml(data.offer.withGhl)} with GHL. ${escapeHtml(data.offer.adSpend)}</p>
      </div>
    </header>

    <section class="today" id="today">
      <div class="ringer" aria-hidden="true">
        <span class="ringer__ring ringer__ring--a"></span>
        <span class="ringer__ring ringer__ring--b"></span>
        <span class="ringer__handset">
          <svg viewBox="0 0 64 64" fill="none" aria-hidden="true">
            <path d="M24 18h8l2.6 8.4-5 3.6c2.4 4.6 6.2 8.4 10.8 10.8l3.6-5 8.4 2.6v8c0 2-1.6 3.8-3.6 4.1C32.4 53.2 16.8 37.6 19.5 21.6 19.8 19.6 21.6 18 23.6 18H24z" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/>
          </svg>
        </span>
      </div>

      <div class="today__copy">
        <p class="today__kicker">Today · ${escapeHtml(asOf)}</p>
        <h2 class="today__priority">${escapeHtml(data.today.priority)}</h2>
        <p class="today__win"><span>Win tonight.</span> ${escapeHtml(data.today.winTonight)}</p>
        <p class="today__hold">${escapeHtml(data.today.standDown)}</p>

        <dl class="facts">
          <div>
            <dt>GHL location</dt>
            <dd>${escapeHtml(String(data.ghl.contactsRemaining))} contacts remaining</dd>
          </div>
          <div>
            <dt>Housekeeping</dt>
            <dd>${escapeHtml(data.ghl.clearedNote)}</dd>
          </div>
          <div>
            <dt>${escapeHtml(data.ghl.calendarName)}</dt>
            <dd>Calendar that morning: ${escapeHtml(data.ghl.calendarThatMorning)}</dd>
          </div>
          <div>
            <dt>Scored so far</dt>
            <dd>${scored === 0 ? "None. All 12 pending Maps." : `${scored} of ${total} marked.`}</dd>
          </div>
        </dl>
      </div>
    </section>

    <section class="rules" aria-label="Standing rules">
      ${data.rules
        .map(
          (rule) => `
            <p class="chip" data-rule="${escapeHtml(rule.id)}">
              <span class="chip__label">${escapeHtml(rule.label)}</span>
              <span class="chip__detail">${escapeHtml(rule.detail)}</span>
            </p>
          `,
        )
        .join("")}
    </section>

    <section class="board" id="twelve">
      <header class="section-head">
        <h2>${escapeHtml(data.firstWave.label)}</h2>
        <p>${escapeHtml(data.firstWave.scoreNote)}</p>
      </header>
      <div class="lanes">
        ${data.firstWave.trades.map(renderTrade).join("")}
      </div>
      <aside class="parked">
        <h3>Parked</h3>
        <ul>
          ${data.parked
            .map(
              (item) => `
                <li>
                  <strong>${escapeHtml(item.label)}</strong>
                  <span>${escapeHtml(item.reason)}</span>
                </li>
              `,
            )
            .join("")}
        </ul>
      </aside>
    </section>

    <section class="pipeline" id="pipeline">
      <header class="section-head">
        <h2>GHL ${escapeHtml(data.ghl.pipelineName)}</h2>
        <p>Stage labels only. Counts stay empty until real opportunities exist. Booking calendar: ${escapeHtml(data.ghl.calendarName)}.</p>
      </header>
      ${renderPipeline(data.ghl)}
    </section>

    <section class="brief" id="brief">
      <article class="brief__icp">
        <h2>${escapeHtml(data.icp.label)}</h2>
        <dl>
          <div><dt>Who</dt><dd>${escapeHtml(data.icp.who)}</dd></div>
          <div><dt>HQ</dt><dd>${escapeHtml(data.icp.hq)}</dd></div>
          <div><dt>Size</dt><dd>${escapeHtml(data.icp.size)}</dd></div>
          <div><dt>Titles</dt><dd>${data.icp.titles.map(escapeHtml).join(" / ")}</dd></div>
          <div><dt>Trades first</dt><dd>${data.icp.tradesFirst.map(escapeHtml).join(", ")}</dd></div>
          <div><dt>Maps pass</dt><dd>${escapeHtml(data.icp.mapsPass)}</dd></div>
        </dl>
        <p class="skip-row">
          <span>Skip</span>
          ${data.icp.skip.map((item) => `<em>${escapeHtml(item)}</em>`).join("")}
        </p>
      </article>

      <article class="brief__track">
        <h2>Contact tracking</h2>
        <p>Fields and tags already on the record. Empty until a send is approved.</p>
        <h3>Fields</h3>
        <ul class="codes">
          ${data.tracking.fields.map((field) => `<li><code>${escapeHtml(field)}</code></li>`).join("")}
        </ul>
        <h3>Tags</h3>
        <ul class="codes">
          ${data.tracking.tags.map((tag) => `<li><code>${escapeHtml(tag)}</code></li>`).join("")}
        </ul>
      </article>
    </section>

    <footer class="colophon">
      <p>${escapeHtml(data.company.name)} · ${escapeHtml(data.company.city)} · ${escapeHtml(data.company.site)}</p>
      <p>Board as of ${escapeHtml(data.asOf)}. Refresh <code>board.json</code> when a name is scored or David says go.</p>
    </footer>
  `;
}

function renderError(message) {
  return `
    <main class="fail">
      <p class="neon-badge">BOARD</p>
      <h1>Spark Media</h1>
      <p>${escapeHtml(message)}</p>
      <p>The keep/kill list lives in <code>board.json</code> at the repo root. COS can edit that file and reload.</p>
    </main>
  `;
}

async function boot() {
  const root = document.getElementById("app");
  try {
    const response = await fetch("./board.json", { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`board.json returned ${response.status}`);
    }
    const data = await response.json();
    root.innerHTML = renderBoard(data);
  } catch (error) {
    root.innerHTML = renderError(
      error instanceof Error ? error.message : "Board data did not load.",
    );
  }
}

boot();
