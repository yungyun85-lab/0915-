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

  // Check saved theme preference - default to 'light'
  const savedTheme = localStorage.getItem('portfolio-theme') || 'light';
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
    icon.style.color = '#0284c7';
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
  document.getElementById('modal-project-desc').innerHTML = desc;
  openModal('project-modal');
}

/* Horizontal Timeline Scroll Controls */
function scrollTimeline(direction) {
  const track = document.getElementById('timeline-track');
  if (track) {
    const scrollAmount = 340;
    track.scrollBy({
      left: direction * scrollAmount,
      behavior: 'smooth'
    });
  }
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
  const email = "yungyun85@gmail.com";
  navigator.clipboard.writeText(email).then(() => {
    showToast("已複製電子郵件地址至剪貼簿！");
  }).catch(() => {
    showToast("複製失敗，請手動複製 yungyun85@gmail.com");
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

/* --------------------------------------------------------------------------
   7. In-Browser Live Edit Mode for Portfolio (線上即時編輯)
   -------------------------------------------------------------------------- */
let isPortfolioEditMode = false;
const PORTFOLIO_STORAGE_KEY = 'portfolio_custom_content_cache';

function togglePortfolioEdit() {
  isPortfolioEditMode = !isPortfolioEditMode;
  document.body.classList.toggle('portfolio-edit-active', isPortfolioEditMode);
  
  const toolbar = document.getElementById('portfolioEditToolbar');
  if (toolbar) toolbar.style.display = isPortfolioEditMode ? 'block' : 'none';

  const btn = document.getElementById('btn-live-edit');
  if (btn) {
    btn.innerHTML = isPortfolioEditMode 
      ? '<i class="fa-solid fa-xmark"></i> 結束編輯' 
      : '<i class="fa-solid fa-pen-to-square"></i> 線上編輯';
    btn.style.background = isPortfolioEditMode ? '#ef4444' : '#fef3c7';
    btn.style.color = isPortfolioEditMode ? '#ffffff' : '#b45309';
    btn.style.borderColor = isPortfolioEditMode ? '#dc2626' : '#f59e0b';
  }

  // Make all main textual elements editable
  const editableSelectors = [
    'h1', 'h2', 'h3', 'h4', 'p', 'li',
    '.hero-title', '.hero-subtitle', '.section-title', '.section-subtitle',
    '.project-title', '.project-desc', '.timeline-title', '.timeline-desc',
    '.about-highlight-box', '.stat-label'
  ];

  const elements = document.querySelectorAll(editableSelectors.join(','));
  elements.forEach(el => {
    if (!el.closest('.nav-actions') && !el.closest('#portfolioEditToolbar') && !el.closest('.btn-primary') && !el.closest('.project-link')) {
      el.setAttribute('contenteditable', isPortfolioEditMode ? 'true' : 'false');
    }
  });

  if (isPortfolioEditMode) {
    showPortfolioToast('✍️ 作品集即時編輯模式已啟動！點擊畫面上任何文字即可直接修改。');
  } else {
    showPortfolioToast('🔒 已退出編輯模式');
  }
}

function savePortfolioEdits() {
  const sections = document.querySelectorAll('section');
  const cache = {};
  sections.forEach(sec => {
    if (sec.id) cache[sec.id] = sec.innerHTML;
  });
  localStorage.setItem(PORTFOLIO_STORAGE_KEY, JSON.stringify(cache));
  showPortfolioToast('💾 修改已成功儲存至本機瀏覽器！重新整理不會消失。');
}

function resetPortfolioDefault() {
  if (confirm('確定要清除所有本機修改，恢復初始版本嗎？')) {
    localStorage.removeItem(PORTFOLIO_STORAGE_KEY);
    location.reload();
  }
}

function downloadPortfolioHtml() {
  const wasEdit = isPortfolioEditMode;
  if (wasEdit) togglePortfolioEdit();

  const htmlContent = '<!DOCTYPE html>\n' + document.documentElement.outerHTML;
  const blob = new Blob([htmlContent], { type: 'text/html;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'index.html';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);

  if (wasEdit) togglePortfolioEdit();
  showPortfolioToast('📥 最新修改後的 index.html 已下載至您的「下載」資料夾！');
}

function showPortfolioToast(msg) {
  let toast = document.getElementById('portfolio-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'portfolio-toast';
    toast.style.cssText = `
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #0f172a;
      color: #ffffff;
      padding: 12px 20px;
      border-radius: 10px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.3);
      font-size: 0.88rem;
      font-weight: 700;
      z-index: 9999;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      opacity: 0;
      transform: translateY(20px);
    `;
    document.body.appendChild(toast);
  }
  toast.innerHTML = msg;
  toast.style.opacity = '1';
  toast.style.transform = 'translateY(0)';
  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(20px)';
  }, 3500);
}

// Restore saved portfolio content on startup
window.addEventListener('DOMContentLoaded', () => {
  const savedCache = localStorage.getItem(PORTFOLIO_STORAGE_KEY);
  if (savedCache) {
    try {
      const cache = JSON.parse(savedCache);
      Object.keys(cache).forEach(id => {
        const sec = document.getElementById(id);
        if (sec) sec.innerHTML = cache[id];
      });
    } catch (e) {
      console.warn('Failed to restore portfolio cache', e);
    }
  }
});
