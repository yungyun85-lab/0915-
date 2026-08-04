// ==========================================================================
// Interactive Logic & Theme Control
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  initSkillTabs();
  initScrollAnimations();
  initContactForm();
  initMobileMenu();
});

/* --------------------------------------------------------------------------
   1. Theme Switcher (Dark / Light Mode)
   -------------------------------------------------------------------------- */
function initThemeToggle() {
  const toggleBtn = document.getElementById('theme-toggle');
  const htmlEl = document.documentElement;
  const icon = toggleBtn.querySelector('i');

  // Check saved theme preference
  const savedTheme = localStorage.getItem('portfolio-theme') || 'dark';
  htmlEl.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme, icon);

  toggleBtn.addEventListener('click', () => {
    const currentTheme = htmlEl.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    htmlEl.setAttribute('data-theme', newTheme);
    localStorage.setItem('portfolio-theme', newTheme);
    updateThemeIcon(newTheme, icon);
  });
}

function updateThemeIcon(theme, icon) {
  if (theme === 'dark') {
    icon.className = 'fa-solid fa-sun';
    icon.style.color = '#f59e0b';
  } else {
    icon.className = 'fa-solid fa-moon';
    icon.style.color = '#4f46e5';
  }
}

/* --------------------------------------------------------------------------
   2. Skill Category Filter & Progress Bar Animations
   -------------------------------------------------------------------------- */
function initSkillTabs() {
  const tabs = document.querySelectorAll('.tab-btn');
  const skillItems = document.querySelectorAll('.skill-item');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const category = tab.getAttribute('data-category');

      skillItems.forEach(item => {
        if (category === 'all' || item.getAttribute('data-category') === category) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
}

function initScrollAnimations() {
  const progressBars = document.querySelectorAll('.skill-bar-fill');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const targetWidth = entry.target.getAttribute('data-progress');
        entry.target.style.width = targetWidth;
      }
    });
  }, { threshold: 0.2 });

  progressBars.forEach(bar => observer.observe(bar));
}

/* --------------------------------------------------------------------------
   3. Modal Control (Resume & Project Modal)
   -------------------------------------------------------------------------- */
const resumeBtn = document.getElementById('open-resume-btn');
if (resumeBtn) {
  resumeBtn.addEventListener('click', () => {
    openModal('resume-modal');
  });
}

function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.add('active');
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.remove('active');
  }
}

function openProjectModal(title, subtitle, desc) {
  document.getElementById('modal-project-title').innerText = title;
  document.getElementById('modal-project-subtitle').innerText = subtitle;
  document.getElementById('modal-project-desc').innerText = desc;
  openModal('project-modal');
}

// Close modal when clicking on overlay
document.querySelectorAll('.modal-overlay').forEach(overlay => {
  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) {
      overlay.classList.remove('active');
    }
  });
});

/* --------------------------------------------------------------------------
   4. Copy Email & Toast Notification
   -------------------------------------------------------------------------- */
function copyEmail() {
  const email = "chen.yongyun@example.com";
  navigator.clipboard.writeText(email).then(() => {
    showToast("已複製電子郵件地址至剪貼簿！");
  }).catch(() => {
    showToast("複製失敗，請手動複製 chen.yongyun@example.com");
  });
}

function showToast(message) {
  const toast = document.getElementById('toast');
  toast.innerText = message;
  toast.classList.add('show');
  setTimeout(() => {
    toast.classList.remove('show');
  }, 3000);
}

/* --------------------------------------------------------------------------
   5. Contact Form Submission
   -------------------------------------------------------------------------- */
function initContactForm() {
  const form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('name').value;
      showToast(`謝謝您 ${name}！您的訊息已發送，我會盡快回覆。`);
      form.reset();
    });
  }
}

/* --------------------------------------------------------------------------
   6. Mobile Menu Toggle
   -------------------------------------------------------------------------- */
function initMobileMenu() {
  const mobileBtn = document.getElementById('mobile-menu-btn');
  const navLinks = document.querySelector('.nav-links');

  if (mobileBtn && navLinks) {
    mobileBtn.addEventListener('click', () => {
      if (navLinks.style.display === 'flex') {
        navLinks.style.display = 'none';
      } else {
        navLinks.style.display = 'flex';
        navLinks.style.flexDirection = 'column';
        navLinks.style.position = 'absolute';
        navLinks.style.top = '70px';
        navLinks.style.left = '0';
        navLinks.style.width = '100%';
        navLinks.style.background = 'var(--bg-secondary)';
        navLinks.style.padding = '20px';
        navLinks.style.borderRadius = 'var(--radius-md)';
        navLinks.style.border = '1px solid var(--border-color)';
      }
    });
  }
}
