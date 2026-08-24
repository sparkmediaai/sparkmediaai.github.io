(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var video = document.getElementById("standInFilm");
  var stills = document.getElementById("reelStills");
  var title = document.getElementById("titleCard");
  var frames = stills ? stills.querySelectorAll("img") : [];
  var i = 0;

  function showStill(n) {
    frames.forEach(function (img, idx) { img.classList.toggle("on", idx === n); });
  }

  function startStills() {
    if (!frames.length) return;
    showStill(0);
    if (reduce) return;
    window.setInterval(function () {
      i = (i + 1) % frames.length;
      showStill(i);
    }, 6500);
  }

  function revealTitle() {
    window.requestAnimationFrame(function () { title.classList.add("in"); });
  }

  function playFilm() {
    if (reduce || !video) {
      startStills();
      revealTitle();
      return;
    }
    var played = video.play();
    if (played && played.then) {
      played.then(function () {
        video.classList.add("is-live");
        revealTitle();
      }).catch(function () {
        startStills();
        revealTitle();
      });
    } else {
      startStills();
      revealTitle();
    }
    video.addEventListener("error", function () {
      video.classList.remove("is-live");
      startStills();
    });
  }

  playFilm();

  var btn = document.getElementById("menuBtn");
  var menu = document.getElementById("menu");
  if (btn && menu) {
    btn.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    menu.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        document.body.classList.remove("nav-open");
        btn.setAttribute("aria-expanded", "false");
      });
    });
  }

  var form = document.getElementById("qualify");
  var thanks = document.getElementById("thanks");
  if (form && thanks) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      form.hidden = true;
      thanks.hidden = false;
      thanks.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "center" });
    });
  }
})();
