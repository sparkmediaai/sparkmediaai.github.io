/* Minimal JS: sticky header background, mobile nav toggle, reveal on scroll */

(function () {
  const header = document.querySelector('[data-header]');
  const navToggle = document.querySelector('[data-nav-toggle]');

  // Year
  const y = document.querySelector('[data-year]');
  if (y) y.textContent = String(new Date().getFullYear());

  // Header solid on scroll
  const setHeader = () => {
    if (!header) return;
    const solid = window.scrollY > 10;
    header.dataset.solid = solid ? 'true' : 'false';
  };
  window.addEventListener('scroll', setHeader, { passive: true });
  setHeader();

  // Mobile nav
  if (navToggle) {
    navToggle.addEventListener('click', () => {
      const open = document.body.classList.toggle('nav-open');
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Reveal animations
  const revealEls = Array.from(document.querySelectorAll('.reveal'));
  if (revealEls.length) {
    const io = new IntersectionObserver(
      (entries) => {
        for (const e of entries) {
          if (e.isIntersecting) {
            e.target.classList.add('is-visible');
            io.unobserve(e.target);
          }
        }
      },
      { threshold: 0.12, rootMargin: '0px 0px -8% 0px' }
    );

    for (const el of revealEls) io.observe(el);
  }
})();
