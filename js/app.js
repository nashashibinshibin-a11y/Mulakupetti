/**
 * MULAKUPETTI — Homepage Hero Logic
 */

document.addEventListener('DOMContentLoaded', () => {
  // Mobile Navigation Toggle
  const mobileToggle = document.getElementById('mobile-toggle');
  const navMenu = document.getElementById('nav-menu');

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      navMenu.classList.toggle('open');
    });

    navMenu.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
      });
    });

    document.addEventListener('click', (e) => {
      if (!navMenu.contains(e.target) && !mobileToggle.contains(e.target)) {
        navMenu.classList.remove('open');
      }
    });
  }

  // Smooth Anchor Navigation
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#' || targetId === '') return;
      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        e.preventDefault();
        targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // ========================================================================
  // "Meet Our Laddu" Interactive Explosion Animation
  // ========================================================================
  initMeetLadduExplosion();
});

function initMeetLadduExplosion() {
  const displayArea = document.getElementById('laddu-display-area');
  const stage = document.getElementById('laddu-stage');
  const triggerBtn = document.getElementById('laddu-trigger');
  const replayBtn = document.getElementById('replay-btn');
  const instructionText = document.getElementById('laddu-instruction-text');
  const tapIcon = document.getElementById('laddu-tap-icon');

  const frame1 = document.getElementById('frame-1');
  const frame2 = document.getElementById('frame-2');
  const frame3 = document.getElementById('frame-3');
  const frame4 = document.getElementById('frame-4');

  if (!stage || !triggerBtn || !frame1 || !frame2 || !frame3 || !frame4) return;

  const frames = [frame1, frame2, frame3, frame4];

  // Preload frames to guarantee instant response
  ['laddu anime/1.png', 'laddu anime/2.png', 'laddu anime/3.png', 'laddu anime/4.png'].forEach(src => {
    const img = new Image();
    img.src = src;
  });

  // State: 'idle' | 'exploding' | 'revealed' | 'resetting'
  let currentState = 'idle';
  let animationTimeouts = [];

  function clearAllTimeouts() {
    animationTimeouts.forEach(t => clearTimeout(t));
    animationTimeouts = [];
  }

  function setActiveFrame(index) {
    frames.forEach((frame, i) => {
      if (i === index) {
        frame.classList.add('is-active');
      } else {
        frame.classList.remove('is-active');
      }
    });
  }

  function playExplosion() {
    if (currentState === 'exploding' || currentState === 'resetting') return;
    currentState = 'exploding';
    clearAllTimeouts();

    triggerBtn.setAttribute('aria-expanded', 'true');
    stage.classList.remove('is-revealed');
    if (displayArea) displayArea.classList.remove('is-revealed');
    stage.classList.add('is-exploding');
    stage.classList.add('is-anticipating');

    if (tapIcon) tapIcon.style.opacity = '0';
    if (instructionText) {
      instructionText.textContent = 'Discovering handcrafted ingredients...';
    }

    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (prefersReducedMotion) {
      const tReduce = setTimeout(() => {
        stage.classList.remove('is-anticipating');
        setActiveFrame(3);
        stage.classList.remove('is-exploding');
        stage.classList.add('is-revealed');
        if (displayArea) displayArea.classList.add('is-revealed');
        currentState = 'revealed';
        triggerBtn.setAttribute('aria-label', 'Laddu ingredients revealed: Jaggery, Nuts, and Seeds. Click to replay.');
        if (instructionText) {
          instructionText.textContent = 'Handcrafted with jaggery, nuts & seeds';
        }
      }, 200);
      animationTimeouts.push(tReduce);
      return;
    }

    // Standard high-fidelity 4-stage explosion sequence (~1000ms total)
    // 1. Anticipation scale: 0ms -> 130ms
    // 2. First crack (frame 2): 130ms
    const t1 = setTimeout(() => {
      stage.classList.remove('is-anticipating');
      setActiveFrame(1);
    }, 130);

    // 3. Breaking further into chunks (frame 3): 380ms
    const t2 = setTimeout(() => {
      setActiveFrame(2);
    }, 380);

    // 4. Spread outward to full burst (frame 4): 660ms
    const t3 = setTimeout(() => {
      setActiveFrame(3);
    }, 660);

    // 5. Reveal ingredient labels & connector lines: 920ms
    const t4 = setTimeout(() => {
      stage.classList.remove('is-exploding');
      stage.classList.add('is-revealed');
      if (displayArea) displayArea.classList.add('is-revealed');
      currentState = 'revealed';
      triggerBtn.setAttribute('aria-label', 'Laddu exploded showing jaggery, nuts, and seeds. Tap anywhere to reassemble and replay.');
      if (instructionText) {
        instructionText.textContent = 'Handcrafted with jaggery, nuts & seeds';
      }
    }, 920);

    animationTimeouts.push(t1, t2, t3, t4);
  }

  function replayAnimation() {
    if (currentState === 'exploding' || currentState === 'resetting') return;
    currentState = 'resetting';
    clearAllTimeouts();

    // 1. Hide labels, connectors, replay button smoothly
    stage.classList.remove('is-revealed');
    if (displayArea) displayArea.classList.remove('is-revealed');

    // 2. Smoothly restore whole laddu resting state
    setActiveFrame(0);
    if (instructionText) {
      instructionText.textContent = 'Reassembling our laddu...';
    }

    // 3. Short pause for reassembled whole laddu before initiating explosion again
    const tReset = setTimeout(() => {
      currentState = 'idle';
      playExplosion();
    }, 350);

    animationTimeouts.push(tReset);
  }

  // Click on the interactive laddu button
  triggerBtn.addEventListener('click', (e) => {
    e.preventDefault();
    if (currentState === 'idle') {
      playExplosion();
    } else if (currentState === 'revealed') {
      replayAnimation();
    }
  });

  // Click on the dedicated replay button
  if (replayBtn) {
    replayBtn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      replayAnimation();
    });
  }

  // Keyboard accessibility (Space / Enter)
  triggerBtn.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      if (currentState === 'idle') {
        playExplosion();
      } else if (currentState === 'revealed') {
        replayAnimation();
      }
    }
  });
}
