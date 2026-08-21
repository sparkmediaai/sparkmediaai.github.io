(() => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  const root = document.documentElement;

  const clamp = (n, min, max) => Math.min(max, Math.max(min, n));
  const lerp = (a, b, t) => a + (b - a) * t;

  const spot = { x: innerWidth * 0.62, y: innerHeight * 0.28 };
  const ring = { x: spot.x, y: spot.y };
  const mouse = { x: spot.x, y: spot.y };
  const dotEl = document.querySelector(".cursor-dot");
  const ringEl = document.querySelector(".cursor-ring");

  if (fine && !reduce) {
    root.classList.add("has-cursor");

    window.addEventListener("pointermove", (e) => {
      mouse.x = e.clientX;
      mouse.y = e.clientY;
      root.style.setProperty("--spot-x", `${e.clientX}px`);
      root.style.setProperty("--spot-y", `${e.clientY}px`);
    }, { passive: true });

    const hoverables = "a, button, [data-goto], [role='slider'], .trade";
    document.addEventListener("pointerover", (e) => {
      if (e.target.closest(hoverables)) root.classList.add("is-hovering");
    });
    document.addEventListener("pointerout", (e) => {
      if (e.target.closest(hoverables)) root.classList.remove("is-hovering");
    });

    const tickCursor = () => {
      ring.x = lerp(ring.x, mouse.x, 0.16);
      ring.y = lerp(ring.y, mouse.y, 0.16);
      if (dotEl) dotEl.style.transform = `translate(${mouse.x}px, ${mouse.y}px) translate(-50%, -50%)`;
      if (ringEl) ringEl.style.transform = `translate(${ring.x}px, ${ring.y}px) translate(-50%, -50%)`;
      requestAnimationFrame(tickCursor);
    };
    requestAnimationFrame(tickCursor);
  }

  if (fine && !reduce) {
    document.querySelectorAll(".magnetic").forEach((btn) => {
      const strength = 18;
      btn.addEventListener("pointermove", (e) => {
        const r = btn.getBoundingClientRect();
        const x = ((e.clientX - r.left) / r.width - 0.5) * strength;
        const y = ((e.clientY - r.top) / r.height - 0.5) * strength;
        btn.style.transform = `translate3d(${x}px, ${y}px, 0)`;
      });
      btn.addEventListener("pointerleave", () => {
        btn.style.transform = "translate3d(0,0,0)";
      });
    });
  }

  if (fine && !reduce) {
    document.querySelectorAll("[data-tilt]").forEach((el) => {
      el.addEventListener("pointermove", (e) => {
        const r = el.getBoundingClientRect();
        const px = (e.clientX - r.left) / r.width;
        const py = (e.clientY - r.top) / r.height;
        const rx = (0.5 - py) * 8;
        const ry = (px - 0.5) * 10;
        el.style.transform = `perspective(900px) rotateX(${rx}deg) rotateY(${ry}deg)`;
      });
      el.addEventListener("pointerleave", () => {
        el.style.transform = "perspective(900px) rotateX(0) rotateY(0)";
      });
    });
  }

  const pipeline = document.querySelector("[data-pipeline]");
  const cards = [...document.querySelectorAll("[data-step]")];
  const ticks = [...document.querySelectorAll("[data-goto]")];
  const fill = document.querySelector("[data-fill]");
  const playhead = document.querySelector("[data-playhead]");
  const track = document.querySelector("[data-playhead-track]");
  const stageIndex = document.querySelector("[data-stage-index]");
  let step = 0;
  let dragging = false;

  const setStep = (next, fromUser) => {
    const i = clamp(Math.round(next), 0, 3);
    step = i;
    cards.forEach((card) => {
      const on = Number(card.dataset.step) === i;
      card.hidden = !on;
      card.classList.toggle("is-active", on);
    });
    ticks.forEach((t, idx) => t.classList.toggle("is-active", idx === i));
    const pct = (i / 3) * 100;
    if (fill) fill.style.width = `${pct}%`;
    if (playhead) playhead.style.left = `${pct}%`;
    if (track) track.setAttribute("aria-valuenow", String(i + 1));
    if (stageIndex) stageIndex.textContent = String(i + 1).padStart(2, "0");
    if (fromUser) lastUser = performance.now();
  };

  let lastUser = 0;
  setStep(0);

  ticks.forEach((t) => {
    const go = () => setStep(Number(t.dataset.goto), true);
    t.addEventListener("mouseenter", go);
    t.addEventListener("click", go);
    t.addEventListener("focus", go);
  });

  const posFromEvent = (e) => {
    const r = track.getBoundingClientRect();
    const x = (e.clientX ?? e.touches?.[0]?.clientX ?? 0) - r.left;
    return clamp(x / r.width, 0, 1) * 3;
  };

  if (track) {
    const start = (e) => { dragging = true; setStep(posFromEvent(e), true); };
    const move = (e) => { if (dragging) setStep(posFromEvent(e), true); };
    const end = () => { dragging = false; };
    track.addEventListener("pointerdown", start);
    window.addEventListener("pointermove", move);
    window.addEventListener("pointerup", end);
    track.addEventListener("keydown", (e) => {
      if (e.key === "ArrowRight") setStep(step + 1, true);
      if (e.key === "ArrowLeft") setStep(step - 1, true);
      if (e.key === "Home") setStep(0, true);
      if (e.key === "End") setStep(3, true);
    });
  }

  if (pipeline && !reduce) {
    const onScroll = () => {
      if (dragging || performance.now() - lastUser < 900) return;
      const r = pipeline.getBoundingClientRect();
      const view = innerHeight * 0.65;
      const start = view - r.height * 0.15;
      const progress = clamp((start - r.top) / (r.height * 0.55), 0, 1);
      setStep(progress * 3);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  const nums = document.querySelectorAll("[data-count]");
  const easeOut = (t) => 1 - Math.pow(1 - t, 3);

  const runCount = (el) => {
    const end = Number(el.dataset.count);
    const suffix = el.dataset.suffix || "";
    if (reduce) {
      el.textContent = `${end.toLocaleString()}${suffix}`;
      return;
    }
    const dur = 1100;
    const t0 = performance.now();
    const frame = (now) => {
      const t = clamp((now - t0) / dur, 0, 1);
      const val = Math.round(end * easeOut(t));
      el.textContent = `${val.toLocaleString()}${suffix}`;
      if (t < 1) requestAnimationFrame(frame);
    };
    requestAnimationFrame(frame);
  };

  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        runCount(entry.target);
        io.unobserve(entry.target);
      });
    }, { threshold: 0.45 });
    nums.forEach((n) => io.observe(n));
  } else {
    nums.forEach(runCount);
  }
})();
