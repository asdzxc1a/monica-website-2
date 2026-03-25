const finaleChapter = document.querySelector(".finale-chapter");

if (finaleChapter) {
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const motionTargets = Array.from(
    finaleChapter.querySelectorAll(
      ".finale-chapter__hero-image, .finale-card, .finale-chapter__boxes, .finale-chapter__statement, .finale-chapter__outro, .finale-chapter__ghost"
    )
  );

  const targetFactors = new Map([
    ["finale-chapter__hero-image--left", { shift: -28, tilt: -1.2 }],
    ["finale-chapter__hero-image--right", { shift: 28, tilt: 1.2 }],
    ["finale-card--pearls", { shift: -12, tilt: -0.8 }],
    ["finale-card--boxing", { shift: 16, tilt: -1.1 }],
    ["finale-card--swing", { shift: -18, tilt: 1.1 }],
    ["finale-chapter__boxes", { shift: -10, tilt: -0.6 }],
    ["finale-chapter__statement", { shift: 14, tilt: 0.5 }],
    ["finale-chapter__outro", { shift: 8, tilt: 0 }],
    ["finale-chapter__ghost", { shift: -22, tilt: 0 }]
  ]);

  let ticking = false;

  const getFactors = (element) => {
    for (const [className, factors] of targetFactors.entries()) {
      if (element.classList.contains(className)) {
        return factors;
      }
    }

    return { shift: 0, tilt: 0 };
  };

  const updateParallax = () => {
    ticking = false;

    if (prefersReducedMotion.matches) {
      finaleChapter.style.setProperty("--finale-shift", "0px");
      finaleChapter.style.setProperty("--finale-tilt", "0deg");
      for (const target of motionTargets) {
        target.style.setProperty("--parallax-y", "0px");
        target.style.setProperty("--parallax-tilt", "0deg");
      }
      return;
    }

    const rect = finaleChapter.getBoundingClientRect();
    const viewportHeight = window.innerHeight || 1;
    const midpoint = rect.top + rect.height / 2;
    const viewportMidpoint = viewportHeight / 2;
    const depth = (viewportMidpoint - midpoint) / viewportHeight;

    finaleChapter.style.setProperty("--finale-shift", `${depth * 20}px`);
    finaleChapter.style.setProperty("--finale-tilt", `${depth * 0.85}deg`);

    for (const target of motionTargets) {
      const factors = getFactors(target);
      target.style.setProperty("--parallax-y", `${depth * factors.shift}px`);
      target.style.setProperty("--parallax-tilt", `${depth * factors.tilt}deg`);
    }
  };

  const requestParallax = () => {
    if (ticking) {
      return;
    }

    ticking = true;
    window.requestAnimationFrame(updateParallax);
  };

  const activateFinale = () => {
    finaleChapter.classList.add("finale-chapter--active");
    requestParallax();
  };

  if (prefersReducedMotion.matches) {
    activateFinale();
  } else {
    if ("IntersectionObserver" in window) {
      const observer = new IntersectionObserver(
        (entries) => {
          for (const entry of entries) {
            if (entry.isIntersecting) {
              activateFinale();
              observer.disconnect();
              break;
            }
          }
        },
        {
          threshold: 0.22,
          rootMargin: "0px 0px -12% 0px"
        }
      );

      observer.observe(finaleChapter);
    } else {
      activateFinale();
    }

    window.addEventListener("scroll", requestParallax, { passive: true });
    window.addEventListener("resize", requestParallax);
    prefersReducedMotion.addEventListener("change", requestParallax);
    requestParallax();
  }
}
