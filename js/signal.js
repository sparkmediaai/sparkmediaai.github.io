(() => {
  const STEPS = [
    { kicker: "They are in a panic", title: "Search", body: "Dead AC. Burst pipe. Locked out. They Google it right now \u2014 not later, not on Facebook.", points: ["Emergency, call-now queries only", "Tight geo. Your service area."] },
    { kicker: "Call-only Google Ads", title: "Ad", body: "A call-only ad shows. They tap Call. No brochure site. No SEO wait.", points: ["Google Search, not social", "Ad spend is yours, extra"] },
    { kicker: "$249 / month", title: "Ring", body: "The call hits your phone. That is the offer: we run the ads so the emergency call rings through.", points: ["Call-only campaigns to your phone", "Month-to-month. No long contract."] },
    { kicker: "$399 adds follow-up", title: "Follow-up", body: "Missed-call text, job follow-up, review ask. So a missed ring does not become a missed job.", points: ["GoHighLevel: missed-call text-back", "Follow-up after the job + review ask"] }
  ];
  const TRADES = {
    plumber: "emergency plumber near me",
    hvac: "AC not cooling",
    electrician: "emergency electrician",
    locksmith: "locksmith near me",
    garage: "garage door won't open"
  };

  const btn = document.querySelector("[data-menu]");
  const drawer = document.querySelector("[data-drawer]");
  if (btn && drawer) {
    btn.addEventListener("click", () => {
      const open = drawer.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", String(open));
    });
  }

  const root = document.querySelector("[data-flow]");
  if (root) {
    const tabs = [...root.querySelectorAll("[data-step]")];
    const panel = root.querySelector("[data-flow-panel]");
    const kicker = root.querySelector("[data-flow-kicker]");
    const title = root.querySelector("[data-flow-title]");
    const body = root.querySelector("[data-flow-body]");
    const points = root.querySelector("[data-flow-points]");
    const paint = (index) => {
      const step = STEPS[index];
      if (!step) return;
      tabs.forEach((tab, i) => {
        const on = i === index;
        tab.classList.toggle("is-active", on);
        tab.setAttribute("aria-selected", String(on));
        tab.tabIndex = on ? 0 : -1;
      });
      if (kicker) kicker.textContent = step.kicker;
      if (title) title.textContent = step.title;
      if (body) body.textContent = step.body;
      if (points) {
        points.replaceChildren(...step.points.map((item) => {
          const li = document.createElement("li");
          li.textContent = item;
          return li;
        }));
      }
      if (panel && tabs[index]) panel.setAttribute("aria-labelledby", tabs[index].id);
    };
    tabs.forEach((tab, index) => {
      const go = () => paint(index);
      tab.addEventListener("mouseenter", go);
      tab.addEventListener("focus", go);
      tab.addEventListener("click", go);
    });
  }

  const row = document.querySelector("[data-trades]");
  const example = document.querySelector("[data-trade-example]");
  if (row) {
    const chips = [...row.querySelectorAll("[data-trade]")];
    const select = (id) => {
      chips.forEach((chip) => {
        const on = chip.dataset.trade === id;
        chip.classList.toggle("is-active", on);
        chip.setAttribute("aria-pressed", String(on));
      });
      if (example) example.textContent = `\u201c${TRADES[id] || TRADES.plumber}\u201d`;
      window.dispatchEvent(new CustomEvent("spark:trade", { detail: id }));
    };
    chips.forEach((chip) => chip.addEventListener("click", () => select(chip.dataset.trade)));
  }
})();
