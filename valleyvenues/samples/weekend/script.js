(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var video = document.getElementById("standInFilm");
  var stills = document.getElementById("reelStills");
  var frames = stills ? stills.querySelectorAll("img") : [];
  function show(n) {
    frames.forEach(function (img, idx) { img.classList.toggle("on", idx === n); });
  }
  show(0);
  if (!reduce && video) {
    var p = video.play();
    if (p && p.then) {
      p.then(function () { video.classList.add("is-live"); }).catch(function () {});
    }
    video.addEventListener("error", function () { video.classList.remove("is-live"); });
  }
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
      if (!form.checkValidity()) { form.reportValidity(); return; }
      form.hidden = true;
      thanks.hidden = false;
      thanks.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "center" });
    });
  }
})();
