(() => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  document.documentElement.classList.add("js-motion");

  // Mark current page in nav
  const here = location.pathname.replace(/index\.html$/, "");
  document.querySelectorAll(".nav-link").forEach((a) => {
    const href = a.getAttribute("href").replace(/index\.html$/, "");
    if (href !== "/" && here.startsWith(href.replace(/\.html$/, ""))) a.setAttribute("aria-current", "page");
  });

  // Auto-tag common blocks for reveal so pages don't need markup changes
  const auto = [
    ".panel:not(.hero) .eyebrow", ".panel:not(.hero) h2", ".panel:not(.hero) .section-lede",
    ".signal-board", ".flow-board", ".price-card", ".industry-card", ".faq-item",
    ".trade-tile", ".note", ".trade-example", ".close .btn"
  ];
  document.querySelectorAll(auto.join(",")).forEach((el) => {
    if (!el.closest(".hero") && !el.hasAttribute("data-reveal")) el.setAttribute("data-reveal", "");
  });

  // Stagger siblings inside grids
  document.querySelectorAll(".price-grid, .industry-grid, .faq-grid, .trade-tiles, [data-stagger]").forEach((grid) => {
    [...grid.children].forEach((child, i) => child.style.setProperty("--i", i));
  });

  const revealables = document.querySelectorAll("[data-reveal]");
  if (reduce || !("IntersectionObserver" in window)) {
    revealables.forEach((el) => el.classList.add("is-in"));
  } else {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add("is-in");
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    revealables.forEach((el) => io.observe(el));
  }

  // Header state + scroll progress
  const bar = document.createElement("div");
  bar.className = "scroll-progress";
  bar.setAttribute("aria-hidden", "true");
  document.body.appendChild(bar);
  const topbar = document.querySelector(".topbar");
  let ticking = false;
  const onScroll = () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      const max = document.documentElement.scrollHeight - innerHeight;
      bar.style.setProperty("--p", max > 0 ? (scrollY / max).toFixed(4) : 0);
      if (topbar) topbar.classList.toggle("is-scrolled", scrollY > 8);
      ticking = false;
    });
  };
  addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Cursor spotlight on cards
  document.addEventListener("pointermove", (e) => {
    const card = e.target.closest && e.target.closest(".price-card, .industry-card, [data-spotlight]");
    if (!card) return;
    const r = card.getBoundingClientRect();
    card.style.setProperty("--mx", `${e.clientX - r.left}px`);
    card.style.setProperty("--my", `${e.clientY - r.top}px`);
  });

  // Fade content when flow tabs / trade tiles swap text (signal.js swaps it)
  const pulse = (el) => {
    if (!el || reduce) return;
    el.classList.remove("is-swapping");
    void el.offsetWidth;
    el.classList.add("is-swapping");
  };
  const flowPanel = document.querySelector("[data-flow-panel]");
  let lastStep = null;
  document.querySelectorAll("[data-step]").forEach((tab) => {
    const go = () => {
      if (lastStep === tab.dataset.step) return;
      lastStep = tab.dataset.step;
      pulse(flowPanel);
    };
    ["mouseenter", "focus", "click"].forEach((ev) => tab.addEventListener(ev, go));
  });
  addEventListener("spark:trade", () => pulse(document.querySelector("[data-trade-example]")));

  // Live signal canvas: drifting emergency queries; one gets "captured" every few seconds
  const canvas = document.querySelector("[data-signal-canvas]");
  if (canvas && canvas.getContext) {
    const ctx = canvas.getContext("2d");
    const capture = document.querySelector("[data-signal-capture]");
    const QUERIES = {
      plumber: ["emergency plumber near me", "burst pipe", "water heater leaking", "toilet overflowing", "24 hour plumber", "sewer backup", "no hot water"],
      hvac: ["AC not cooling", "furnace not working", "AC repair near me", "emergency HVAC", "heater blowing cold air", "AC unit frozen"],
      electrician: ["emergency electrician", "power out half house", "sparking outlet", "breaker keeps tripping", "burning smell outlet"],
      locksmith: ["locksmith near me", "locked out of house", "locked keys in car", "broken key in lock", "24 hour locksmith"],
      garage: ["garage door won't open", "garage door spring broke", "garage door off track", "garage door repair near me"]
    };
    let pool = Object.values(QUERIES).flat();
    let W = 0, H = 0, dpr = 1, nodes = [], target = null, captureAt = 0, visible = true;

    const resize = () => {
      const r = canvas.getBoundingClientRect();
      dpr = Math.min(devicePixelRatio || 1, 2);
      W = r.width; H = r.height;
      canvas.width = W * dpr; canvas.height = H * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      seed();
    };
    const seed = () => {
      // jittered grid so labels start spread out instead of piling up
      const cols = W > 700 ? 3 : 2, rows = Math.max(4, Math.round((H - 60) / 70));
      const cw = W / cols, rh = (H - 70) / rows;
      nodes = [];
      for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) {
        if (Math.abs(c * cw + cw / 2 - W / 2) < cw / 2 && Math.abs(60 + r * rh + rh / 2 - H * 0.56) < rh) continue;
        nodes.push({
          text: pool[nodes.length % pool.length],
          x: c * cw + cw / 2 + (Math.random() - 0.5) * cw * 0.3,
          y: 64 + r * rh + rh / 2 + (Math.random() - 0.5) * rh * 0.3,
          vx: (Math.random() - 0.5) * 0.25,
          vy: (Math.random() - 0.5) * 0.18,
          a: 0.35 + Math.random() * 0.4,
          s: 11 + Math.random() * 3
        });
      }
    };
    const center = () => ({ x: W * 0.5, y: H * 0.56 });
    const pick = () => {
      target = nodes[Math.floor(Math.random() * nodes.length)];
      target.glow = 1;
      if (capture) capture.textContent = target.text;
      captureAt = performance.now();
    };
    addEventListener("spark:trade", (e) => {
      pool = QUERIES[e.detail] || pool;
      nodes.forEach((n, i) => { n.text = pool[i % pool.length]; });
      pick();
    });

    const draw = (t) => {
      if (visible) {
        ctx.clearRect(0, 0, W, H);
        const c = center();
        // radar rings
        for (let k = 0; k < 3; k++) {
          const rr = ((t / 40 + k * 90) % 270);
          ctx.beginPath();
          ctx.arc(c.x, c.y, rr, 0, Math.PI * 2);
          ctx.strokeStyle = `rgba(0,194,255,${0.18 * (1 - rr / 270)})`;
          ctx.lineWidth = 1;
          ctx.stroke();
        }
        // phone core
        ctx.beginPath();
        ctx.arc(c.x, c.y, 18, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(0,194,255,0.18)";
        ctx.fill();
        ctx.beginPath();
        ctx.arc(c.x, c.y, 7, 0, Math.PI * 2);
        ctx.fillStyle = "#4DE1FF";
        ctx.shadowColor = "#00C2FF"; ctx.shadowBlur = 18;
        ctx.fill();
        ctx.shadowBlur = 0;

        if (!target || t - captureAt > 3200) pick();
        const since = (t - captureAt) / 1000;

        for (const n of nodes) {
          if (!reduce) {
            n.x += n.vx; n.y += n.vy;
            const half = ctx.measureText(n.text).width / 2 + 12;
            if (n.x < half) n.vx = Math.abs(n.vx); if (n.x > W - half) n.vx = -Math.abs(n.vx);
            if (n.y < 64) n.vy = Math.abs(n.vy); if (n.y > H - 16) n.vy = -Math.abs(n.vy);
          }
          const on = n === target;
          ctx.font = `${on ? 700 : 500} ${n.s}px Inter, system-ui, sans-serif`;
          if (on) {
            // beam from query to phone
            const p = Math.min(1, since / 0.9);
            const bx = n.x + (c.x - n.x) * p, by = n.y + (c.y - n.y) * p;
            const g = ctx.createLinearGradient(n.x, n.y, bx, by);
            g.addColorStop(0, "rgba(0,194,255,0.0)");
            g.addColorStop(1, "rgba(77,225,255,0.9)");
            ctx.beginPath(); ctx.moveTo(n.x, n.y); ctx.lineTo(bx, by);
            ctx.strokeStyle = g; ctx.lineWidth = 2; ctx.stroke();
            ctx.beginPath(); ctx.arc(bx, by, 3.5, 0, Math.PI * 2); ctx.fillStyle = "#E8F7FF"; ctx.fill();
            const w = ctx.measureText(n.text).width;
            ctx.fillStyle = "rgba(0,194,255,0.14)";
            ctx.strokeStyle = "rgba(0,194,255,0.6)";
            ctx.beginPath();
            ctx.roundRect ? ctx.roundRect(n.x - w / 2 - 10, n.y - n.s - 6, w + 20, n.s + 14, 999) : ctx.rect(n.x - w / 2 - 10, n.y - n.s - 6, w + 20, n.s + 14);
            ctx.fill(); ctx.stroke();
            ctx.fillStyle = "#F3F6FB";
          } else {
            ctx.fillStyle = `rgba(147,160,181,${n.a})`;
          }
          ctx.textAlign = "center";
          ctx.fillText(n.text, n.x, n.y);
        }
      }
      if (!reduce) requestAnimationFrame(draw);
    };

    if ("IntersectionObserver" in window) {
      new IntersectionObserver(([e]) => { visible = e.isIntersecting; }).observe(canvas);
    }
    addEventListener("resize", resize);
    resize();
    if (reduce) { pick(); draw(performance.now()); } else requestAnimationFrame(draw);
  }
})();
