// Spark Media site behaviour: header state, dropdown menus, mobile menu, scroll reveals.
(function () {
  var doc = document.documentElement;
  var header = document.querySelector('[data-header]');

  // Header border once the page scrolls
  function onScroll() { if (header) header.classList.toggle('scrolled', window.scrollY > 8); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Desktop dropdowns: hover on pointer devices, click/keyboard everywhere
  var items = Array.prototype.slice.call(document.querySelectorAll('[data-dropdown]'));
  function setOpen(item, open) {
    item.classList.toggle('open', open);
    var b = item.querySelector('button');
    if (b) b.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  function closeAll(except) { items.forEach(function (it) { if (it !== except) setOpen(it, false); }); }
  var canHover = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  items.forEach(function (item) {
    var btn = item.querySelector('button');
    var timer;
    btn.addEventListener('click', function () {
      var open = !item.classList.contains('open');
      closeAll(item);
      setOpen(item, open);
    });
    if (canHover) {
      item.addEventListener('mouseenter', function () { clearTimeout(timer); closeAll(item); setOpen(item, true); });
      item.addEventListener('mouseleave', function () { timer = setTimeout(function () { setOpen(item, false); }, 140); });
    }
    item.addEventListener('focusout', function (ev) {
      if (!item.contains(ev.relatedTarget)) setOpen(item, false);
    });
  });
  document.addEventListener('click', function (ev) {
    if (!ev.target.closest('[data-dropdown]')) closeAll();
  });
  document.addEventListener('keydown', function (ev) {
    if (ev.key !== 'Escape') return;
    var open = items.filter(function (it) { return it.classList.contains('open'); })[0];
    closeAll();
    if (open) open.querySelector('button').focus();
    if (doc.classList.contains('menu-open')) toggleMenu(false);
  });

  // Mobile menu
  var menuBtn = document.querySelector('[data-menu]');
  function toggleMenu(open) {
    doc.classList.toggle('menu-open', open);
    document.body.classList.toggle('menu-open', open);
    if (menuBtn) {
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
      menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }
  }
  if (menuBtn) {
    menuBtn.addEventListener('click', function () { toggleMenu(!doc.classList.contains('menu-open')); });
    window.addEventListener('resize', function () { if (window.innerWidth >= 960) toggleMenu(false); });
  }

  // Scroll reveals
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();
