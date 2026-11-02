/* ============================================================
   00.LINK 零界弦译 — site interactions
   ============================================================ */
(function () {
  "use strict";

  /* ---------- static review mode (?static=1) ---------- */
  if (/[?&]static=1/.test(location.search)) {
    document.documentElement.classList.add("static");
    var m = location.search.match(/[?&]scroll=(\d+)/);
    if (m) {
      window.addEventListener("load", function () {
        window.scrollTo(0, Number(m[1]));
      });
    }
  }

  /* ---------- nav ---------- */
  var nav = document.querySelector(".nav");
  var onScroll = function () {
    if (!nav) return;
    if (window.scrollY > 24) nav.classList.add("solid");
    else nav.classList.remove("solid");
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- mobile menu ---------- */
  var menuBtn = document.querySelector(".menu-btn");
  var mobileMenu = document.querySelector(".mobile-menu");
  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener("click", function () {
      menuBtn.classList.toggle("open");
      mobileMenu.classList.toggle("show");
    });
    mobileMenu.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        menuBtn.classList.remove("open");
        mobileMenu.classList.remove("show");
      });
    });
  }

  /* ---------- reveal on scroll ---------- */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            e.target.classList.add("in");
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
    );
    revealEls.forEach(function (el, i) {
      el.style.transitionDelay = Math.min(i % 4, 3) * 70 + "ms";
      io.observe(el);
    });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- card hover video ---------- */
  document.querySelectorAll(".card[data-video]").forEach(function (card) {
    var v = card.querySelector("video");
    if (!v) return;
    var play = function () {
      card.classList.add("playing");
      try { v.currentTime = 0; var p = v.play(); if (p && p.catch) p.catch(function () {}); } catch (e) {}
    };
    var stop = function () {
      card.classList.remove("playing");
      try { v.pause(); } catch (e) {}
    };
    card.addEventListener("mouseenter", play);
    card.addEventListener("mouseleave", stop);
    card.addEventListener("focus", play);
    card.addEventListener("blur", stop);
    // touch: tap once plays, tap again navigates
    card.addEventListener("touchstart", function () {
      if (!card.classList.contains("playing")) { play(); }
    }, { passive: true });
  });

  /* ---------- gallery ---------- */
  var galleryMain = document.querySelector(".gallery-main img");
  if (galleryMain) {
    var thumbs = document.querySelectorAll(".thumb");
    thumbs.forEach(function (t) {
      t.addEventListener("click", function () {
        var src = t.getAttribute("data-src");
        if (!src) return;
        thumbs.forEach(function (x) { x.classList.remove("active"); });
        t.classList.add("active");
        var box = galleryMain.parentElement;
        box.classList.add("switching");
        setTimeout(function () {
          galleryMain.src = src;
          box.classList.remove("switching");
        }, 200);
      });
    });
  }

  /* ---------- buy modal ---------- */
  var modal = document.getElementById("buyModal");
  var lastFocus = null;
  window.openBuy = function (name, price, img) {
    if (!modal) return;
    lastFocus = document.activeElement;
    var n = modal.querySelector("[data-buy-name]");
    var p = modal.querySelector("[data-buy-price]");
    var i = modal.querySelector("[data-buy-img]");
    if (n && name) n.textContent = name;
    if (p && price) p.textContent = "¥" + price;
    if (i && img) i.src = img;
    modal.classList.add("show");
    document.body.style.overflow = "hidden";
  };
  window.closeBuy = function () {
    if (!modal) return;
    modal.classList.remove("show");
    document.body.style.overflow = "";
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  };
  if (modal) {
    modal.addEventListener("click", function (e) {
      if (e.target === modal) window.closeBuy();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") window.closeBuy();
    });
  }

  /* ---------- copy wechat ---------- */
  window.copyText = function (text) {
    var i18n = window.LINK_I18N || {};
    var done = function () {
      var t = document.getElementById("toast");
      if (t) {
        t.textContent = (i18n.copied || "已复制") + " · " + text;
        t.classList.add("show");
        setTimeout(function () { t.classList.remove("show"); }, 2000);
      }
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, done);
    } else {
      var ta = document.createElement("textarea");
      ta.value = text;
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand("copy"); } catch (e) {}
      document.body.removeChild(ta);
      done();
    }
  };

  /* ---------- marquee: duplicate track for seamless loop ---------- */
  document.querySelectorAll(".marquee-track").forEach(function (track) {
    track.innerHTML = track.innerHTML + track.innerHTML;
  });

  /* ---------- smooth anchor with nav offset ---------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener("click", function (e) {
      var id = a.getAttribute("href");
      if (!id || id === "#") return;
      var el = document.querySelector(id);
      if (!el) return;
      e.preventDefault();
      var y = el.getBoundingClientRect().top + window.scrollY - 70;
      window.scrollTo({ top: y, behavior: "smooth" });
    });
  });

  /* ---------- year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
