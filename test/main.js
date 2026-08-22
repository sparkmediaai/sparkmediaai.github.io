(() => {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const MAGENTA = "#FF005C";
  const CYAN = "#00C2FF";
  const PURPLE = "#7A5CFF";

  const STEPS = [
    {
      kicker: "High-intent trigger",
      title: "Search",
      body: "We only bid on \u201ccall-now\u201d keywords inside your exact service radius and daypart budgets.",
      points: ["Signals: burst searches, emergency modifiers", "Response goal: < 150ms ad delivery"]
    },
    {
      kicker: "Instant pickup",
      title: "Answer",
      body: "Calls, forms, and chats hit an always-on AI receptionist that greets the homeowner by name.",
      points: ["Pickup: 24/7, 12-second SLA", "Routing: smart agent \u2192 dispatcher \u2192 tech"]
    },
    {
      kicker: "Lead intelligence",
      title: "Qualify",
      body: "OpenClaw workflows confirm service area, urgency, and job type \u2014 then score the lead before anyone rolls.",
      points: ["Qualification: 8+ data points captured", "Accuracy: 94% qualification target"]
    },
    {
      kicker: "On the calendar",
      title: "Book",
      body: "The job lands on your calendar with SMS confirmation and full context. Spend stays on the queries that book.",
      points: ["Booking: calendar + SMS confirmation", "Loop: booked jobs feed the next day\u2019s bids"]
    }
  ];

  const TRADES = {
    plumber: "plumber near me",
    hvac: "AC repair Las Vegas",
    electrician: "emergency electrician",
    roofer: "roof leak repair",
    garage: "garage door stuck"
  };

  const SIGNALS = [
    { text: "plumber near me", trade: "plumber", color: MAGENTA },
    { text: "AC repair Las Vegas", trade: "hvac", color: CYAN },
    { text: "emergency electrician", trade: "electrician", color: MAGENTA },
    { text: "roof leak repair", trade: "roofer", color: CYAN },
    { text: "garage door stuck", trade: "garage", color: MAGENTA },
    { text: "water heater install", trade: "plumber", color: CYAN },
    { text: "no cool Summerlin", trade: "hvac", color: MAGENTA },
    { text: "burst pipe Henderson", trade: "plumber", color: CYAN },
    { text: "panel upgrade", trade: "electrician", color: PURPLE },
    { text: "storm damage roof", trade: "roofer", color: MAGENTA }
  ];

  function initOrbs() {
    const magenta = document.querySelector('[data-orb="magenta"]');
    const cyan = document.querySelector('[data-orb="cyan"]');
    if (!magenta || !cyan || reduceMotion) return;

    let mx = 0.5;
    let my = 0.4;
    let t = 0;

    window.addEventListener("pointermove", (event) => {
      mx = event.clientX / window.innerWidth;
      my = event.clientY / window.innerHeight;
    }, { passive: true });

    const tick = () => {
      t += 0.007;
      const xPull = (mx - 0.5) * 56;
      const yPull = (my - 0.5) * 48;
      magenta.style.transform = `translate(${Math.sin(t) * 28 + xPull}px, ${Math.cos(t * 0.85) * 22 - yPull}px)`;
      cyan.style.transform = `translate(${Math.cos(t * 0.9) * -30 - xPull}px, ${Math.sin(t * 1.05) * 24 + yPull}px)`;
      requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }

  function initSignal() {
    const root = document.querySelector("[data-signal]");
    const canvas = document.querySelector("[data-signal-canvas]");
    const capture = document.querySelector("[data-signal-capture]");
    if (!root || !canvas) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const pointer = { x: -9999, y: -9999, active: false };
    let width = 0;
    let height = 0;
    let nodes = [];
    let running = false;
    let visible = false;
    let frameId = 0;
    let activeTrade = "plumber";
    let captureIndex = 0;

    const count = () => (width < 640 ? 6 : SIGNALS.length);

    function seed() {
      const n = count();
      nodes = SIGNALS.slice(0, n).map((signal, i) => {
        const angle = (i / n) * Math.PI * 2;
        const radius = Math.min(width, height) * (0.22 + (i % 3) * 0.08);
        return {
          ...signal,
          x: width * 0.5 + Math.cos(angle) * radius + (Math.random() - 0.5) * 40,
          y: height * 0.54 + Math.sin(angle) * radius * 0.72 + (Math.random() - 0.5) * 30,
          vx: (Math.random() - 0.5) * 0.28,
          vy: (Math.random() - 0.5) * 0.28,
          phase: Math.random() * Math.PI * 2,
          r: 4 + (i % 3)
        };
      });
    }

    function resize() {
      const rect = canvas.getBoundingClientRect();
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      width = Math.max(1, rect.width);
      height = Math.max(1, rect.height);
      canvas.width = Math.floor(width * dpr);
      canvas.height = Math.floor(height * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      seed();
    }

    function draw(staticOnly) {
      ctx.clearRect(0, 0, width, height);

      const now = performance.now() / 1000;
      const linkDist = Math.min(width, height) * 0.34;

      for (let i = 0; i < nodes.length; i += 1) {
        for (let j = i + 1; j < nodes.length; j += 1) {
          const a = nodes[i];
          const b = nodes[j];
          const dx = a.x - b.x;
          const dy = a.y - b.y;
          const dist = Math.hypot(dx, dy);
          if (dist > linkDist) continue;
          const midX = (a.x + b.x) / 2;
          const midY = (a.y + b.y) / 2;
          const toPointer = Math.hypot(pointer.x - midX, pointer.y - midY);
          const boost = pointer.active && toPointer < 90 ? 0.35 : 0;
          const alpha = (1 - dist / linkDist) * 0.28 + boost;
          const grad = ctx.createLinearGradient(a.x, a.y, b.x, b.y);
          grad.addColorStop(0, a.color);
          grad.addColorStop(1, b.color);
          ctx.globalAlpha = alpha;
          ctx.strokeStyle = grad;
          ctx.lineWidth = 1.2;
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.stroke();
        }
      }

      nodes.forEach((node) => {
        const pulse = staticOnly ? 0.7 : 0.55 + 0.45 * Math.sin(now * 2.1 + node.phase);
        const focused = node.trade === activeTrade;
        const dPointer = Math.hypot(pointer.x - node.x, pointer.y - node.y);
        const near = pointer.active && dPointer < 86;
        const size = node.r + pulse * 2.4 + (focused ? 2 : 0) + (near ? 2.5 : 0);

        ctx.globalAlpha = 0.22 + pulse * 0.25;
        ctx.fillStyle = node.color;
        ctx.beginPath();
        ctx.arc(node.x, node.y, size * 3.2, 0, Math.PI * 2);
        ctx.fill();

        ctx.globalAlpha = 0.95;
        ctx.beginPath();
        ctx.arc(node.x, node.y, size, 0, Math.PI * 2);
        ctx.fill();

        const showLabel = near || focused || pulse > 0.92 || staticOnly;
        if (showLabel) {
          ctx.globalAlpha = near || focused ? 1 : 0.72;
          ctx.font = "600 12px Inter, system-ui, sans-serif";
          ctx.fillStyle = "#FFFFFF";
          ctx.fillText(node.text, node.x + 12, node.y - 10);
        }
      });

      ctx.globalAlpha = 1;
    }

    function step() {
      if (!running) return;
      const now = performance.now() / 1000;
      nodes.forEach((node) => {
        if (pointer.active) {
          const dx = pointer.x - node.x;
          const dy = pointer.y - node.y;
          const dist = Math.hypot(dx, dy) || 1;
          if (dist < 160) {
            node.vx += (dx / dist) * 0.035;
            node.vy += (dy / dist) * 0.035;
          }
        }
        node.vx += Math.sin(now + node.phase) * 0.004;
        node.vy += Math.cos(now * 0.8 + node.phase) * 0.004;
        node.vx *= 0.96;
        node.vy *= 0.96;
        node.x += node.vx;
        node.y += node.vy;
        const pad = 28;
        if (node.x < pad || node.x > width - pad) node.vx *= -1;
        if (node.y < 56 || node.y > height - 24) node.vy *= -1;
        node.x = Math.min(width - pad, Math.max(pad, node.x));
        node.y = Math.min(height - 24, Math.max(56, node.y));
      });
      draw(false);
      frameId = requestAnimationFrame(step);
    }

    function start() {
      if (running || reduceMotion || !visible) return;
      running = true;
      frameId = requestAnimationFrame(step);
    }

    function stop() {
      running = false;
      cancelAnimationFrame(frameId);
    }

    function setPointer(event, active) {
      const rect = canvas.getBoundingClientRect();
      pointer.x = event.clientX - rect.left;
      pointer.y = event.clientY - rect.top;
      pointer.active = active;
      if (reduceMotion) draw(true);
    }

    canvas.addEventListener("pointermove", (event) => setPointer(event, true));
    canvas.addEventListener("pointerdown", (event) => setPointer(event, true));
    canvas.addEventListener("pointerleave", () => {
      pointer.active = false;
      pointer.x = -9999;
      pointer.y = -9999;
      if (reduceMotion) draw(true);
    });

    window.addEventListener("spark:trade", (event) => {
      activeTrade = event.detail;
      if (capture) capture.textContent = TRADES[activeTrade] || SIGNALS[0].text;
      if (reduceMotion) draw(true);
    });

    if (capture && !reduceMotion) {
      window.setInterval(() => {
        const pool = nodes.length ? nodes : SIGNALS;
        captureIndex = (captureIndex + 1) % pool.length;
        const node = pool[captureIndex];
        if (node) capture.textContent = node.text;
      }, 2600);
    }

    const io = new IntersectionObserver((entries) => {
      visible = entries.some((entry) => entry.isIntersecting);
      if (visible) {
        resize();
        if (reduceMotion) draw(true);
        else start();
      } else {
        stop();
      }
    }, { threshold: 0.2 });
    io.observe(root);

    window.addEventListener("resize", () => {
      resize();
      if (reduceMotion) draw(true);
    });

    document.addEventListener("visibilitychange", () => {
      if (document.hidden) stop();
      else if (visible && !reduceMotion) start();
    });

    resize();
    draw(true);
  }

  function initFlow() {
    const root = document.querySelector("[data-flow]");
    if (!root) return;
    const tabs = [...root.querySelectorAll("[data-step]")];
    const panel = root.querySelector("[data-flow-panel]");
    const kicker = root.querySelector("[data-flow-kicker]");
    const title = root.querySelector("[data-flow-title]");
    const body = root.querySelector("[data-flow-body]");
    const points = root.querySelector("[data-flow-points]");
    if (!tabs.length || !panel) return;

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
      panel.setAttribute("aria-labelledby", tabs[index].id);
    };

    tabs.forEach((tab, index) => {
      const go = () => paint(index);
      tab.addEventListener("mouseenter", go);
      tab.addEventListener("focus", go);
      tab.addEventListener("click", go);
      tab.addEventListener("keydown", (event) => {
        if (event.key !== "ArrowRight" && event.key !== "ArrowLeft") return;
        event.preventDefault();
        const next = event.key === "ArrowRight"
          ? (index + 1) % tabs.length
          : (index - 1 + tabs.length) % tabs.length;
        tabs[next].focus();
        paint(next);
      });
    });
  }

  function initTrades() {
    const row = document.querySelector("[data-trades]");
    const example = document.querySelector("[data-trade-example]");
    if (!row) return;
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

    chips.forEach((chip) => {
      chip.addEventListener("click", () => select(chip.dataset.trade));
    });
  }

  initOrbs();
  initSignal();
  initFlow();
  initTrades();
})();
