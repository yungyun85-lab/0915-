// ==========================================================================
// Top Navigation View Switcher & Active Link Color Control
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {
  const navLinks = document.querySelectorAll('.top-nav .nav-item');
  const viewTriggers = document.querySelectorAll('[data-view-target]');
  const views = document.querySelectorAll('.page-view');
  const mobileToggle = document.getElementById('mobile-nav-toggle');
  const topNav = document.getElementById('top-nav');

  function activateView(targetId, markClicked = false) {
    const targetView = document.getElementById(`view-${targetId}`);
    if (!targetView) return;

    views.forEach((view) => {
      view.classList.toggle('active', view === targetView);
    });

    navLinks.forEach((link) => {
      const isMatch = link.getAttribute('data-view-target') === targetId;
      link.classList.toggle('active', isMatch);
      if (isMatch && markClicked) {
        link.classList.add('was-clicked');
      }
    });

    if (topNav && topNav.classList.contains('open')) {
      topNav.classList.remove('open');
      if (mobileToggle) {
        mobileToggle.setAttribute('aria-expanded', 'false');
      }
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  viewTriggers.forEach((trigger) => {
    trigger.addEventListener('click', (event) => {
      const targetId = trigger.getAttribute('data-view-target');
      if (!targetId) return;
      event.preventDefault();

      if (window.location.hash !== `#${targetId}`) {
        history.pushState(null, '', `#${targetId}`);
      }
      activateView(targetId, true);
    });
  });

  if (mobileToggle && topNav) {
    mobileToggle.addEventListener('click', () => {
      const isOpen = topNav.classList.toggle('open');
      mobileToggle.setAttribute('aria-expanded', String(isOpen));
    });
  }

  function syncFromHash() {
    const hashId = window.location.hash.replace('#', '');
    if (hashId && document.getElementById(`view-${hashId}`)) {
      activateView(hashId, false);
    } else {
      activateView('about', false);
    }
  }

  window.addEventListener('hashchange', syncFromHash);
  syncFromHash();
});
