import './style.css';
import mermaid from 'mermaid';

// --- Target-specific text overrides ---
const TARGET_TEXTS = {
  oliveyoung: {
    'meta-desc': { attr: 'content', value: '복잡한 비즈니스 로직을 시스템으로 자동화하는 플랫폼 PM 정윤상. 운영 정책 설계, 프로세스 표준화, 데이터 기반 효율화 포트폴리오.' },
    'og-title': { attr: 'content', value: '플랫폼 운영 PM 정윤상 | 포트폴리오' },
    'og-desc': { attr: 'content', value: '복잡한 비즈니스 로직을 시스템으로 자동화하는 플랫폼 PM. 운영 정책 무결성, 협력사 온보딩, 정산 표준화 프로젝트 성과.' },
    'hero-badge': { html: '<span class="material-symbols-rounded text-[16px]">info</span> Platform Operations PM' },
    'hero-headline': { html: '복잡한 비즈니스 로직을<br/>시스템으로 자동화하는<br/><span class="text-[#059669]">플랫폼 PM</span>입니다.' },
    'hero-sub': { text: '수천 협력사의 운영 비용을 줄이고, 정책의 무결성을 시스템으로 보장합니다. 수기 업무를 자동화하고, 예외 없는 프로세스를 설계합니다.' },
    'impact-0-num': { text: '100%' },
    'impact-0-label': { text: '정책 무결성' },
    'impact-1-num': { text: '226개' },
    'impact-1-label': { text: '협력사 셀프서비스 전환' },
    'impact-2-num': { text: '20+' },
    'impact-2-label': { text: '페이지 정산 정책 통합' },
    'impact-3-num': { text: '40%' },
    'impact-3-label': { text: '운영 리소스 절감' },
    'proj-bmad': { text: '파편화된 기획 프로세스를 5단계 표준화 파이프라인으로 전환하여 부서 간 병목 제거' },
    'proj-deploy': { text: '정책 위반을 시스템으로 원천 차단하는 5단계 검증 게이트 및 자동 롤백 체계 구축' },
    'proj-oauth': { text: '수천 고객사 대상 셀프서비스 온보딩 자동화 및 예외 시나리오 사전 정의' },
    'proj-payment': { text: '관리자·주문·환불·정산·CRM 20+ 페이지를 관통하는 정산 정책 표준화 아키텍처 설계' },
    'proj-erns': { text: '500여 개의 수기 운영 양식을 단일 웹 표준으로 통합하고 데이터 검증 자동화 체계 구축' },
    'cta-title': { text: '운영 효율화, 함께 설계하고 싶으신가요?' },
    'cta-sub': { text: '복잡한 비즈니스 룰의 시스템화와 데이터 기반 운영 개선에 관심이 있으시다면, 편하게 연락주세요.' },
  },
  celimax: {
    'meta-desc': { attr: 'content', value: '실무자 옆에 앉아 비효율을 직접 시스템화하는 PM 정윤상. 토스페이/OAuth/BMAD/Dooray/SSOT-Guard 등 어드민·바이브 코딩·AI 도구 직접 개발 포트폴리오.' },
    'og-title': { attr: 'content', value: 'PM 정윤상 | 어드민 시스템 + 바이브 코딩' },
    'og-desc': { attr: 'content', value: '실무자 페인포인트를 발굴해 시스템화하는 PM. 어드민·B2B 백오피스·이커머스·바이브 코딩 — 직접 만든 결과물로 입증.' },
    'hero-badge': { html: '<span class="material-symbols-rounded text-[16px]">info</span> PM for 셀리맥스 테크셀 · 바이브 코딩 / AI-Native' },
    'hero-headline': { html: '실무자 옆에 앉아 비효율을<br/><span class="text-[#059669]">직접 시스템화</span>하는 PM입니다.' },
    'hero-sub': { text: '어드민·B2B·이커머스·바이브 코딩 — 모두 직접 만든 결과물로 입증합니다. AI 도구는 슬로건이 아니라 제 일상의 작동 원칙입니다.' },
  }
};

// Apply target-specific overrides
const targetMeta = document.querySelector('meta[name="portfolio-target"]');
if (targetMeta) {
  const target = targetMeta.content;
  const texts = TARGET_TEXTS[target];
  if (texts) {
    // Update page title
    if (target === 'oliveyoung') {
      document.title = '플랫폼 운영 PM 정윤상 | Portfolio';
    } else if (target === 'celimax') {
      document.title = 'PM 정윤상 | 셀리맥스 테크셀 지원';
    }
    // Apply text replacements
    Object.entries(texts).forEach(([key, config]) => {
      const el = document.querySelector(`[data-t="${key}"]`);
      if (!el) return;
      if (config.attr) {
        el.setAttribute(config.attr, config.value);
      } else if (config.html) {
        el.innerHTML = config.html;
      } else if (config.text) {
        el.textContent = config.text;
      }
    });
  }
}

// Initialize mermaid — startOnLoad: false to prevent rendering inside hidden tabs
mermaid.initialize({
  startOnLoad: false,
  theme: 'dark',
  themeVariables: {
    primaryColor: '#34d399',
    primaryBorderColor: '#059669',
    primaryTextColor: '#dee5ff',
    lineColor: '#059669',
    secondaryColor: '#192540',
    tertiaryColor: '#091328'
  }
});

// Save original mermaid source before any rendering
const mermaidSources = new Map();
document.querySelectorAll('.mermaid').forEach((el, i) => {
  mermaidSources.set(el, el.textContent.trim());
});

document.addEventListener('DOMContentLoaded', () => {
  // Only render mermaid in the initially visible tab
  mermaid.run({
    querySelector: '.tab-content:not(.hidden) .mermaid',
  }).catch(e => console.error(e));

  // --- Mobile Menu Toggle ---
  const menuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const menuIcon = document.getElementById('menu-icon');

  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', () => {
      const isOpen = !mobileMenu.classList.contains('hidden');
      mobileMenu.classList.toggle('hidden');
      menuIcon.textContent = isOpen ? 'menu' : 'close';
      menuBtn.setAttribute('aria-expanded', String(!isOpen));
    });

    // Close menu on link click
    mobileMenu.querySelectorAll('[data-mobile-link]').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.add('hidden');
        menuIcon.textContent = 'menu';
        menuBtn.setAttribute('aria-expanded', 'false');
      });
    });

    // Close menu on outside click
    document.addEventListener('click', (e) => {
      if (!mobileMenu.classList.contains('hidden') && !menuBtn.contains(e.target) && !mobileMenu.contains(e.target)) {
        mobileMenu.classList.add('hidden');
        menuIcon.textContent = 'menu';
        menuBtn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // --- Tab Scroll Hint ---
  const tabsContainer = document.getElementById('project-tabs');
  const scrollHint = document.getElementById('tab-scroll-hint');

  function updateScrollHint() {
    if (!tabsContainer || !scrollHint) return;
    const atEnd = tabsContainer.scrollLeft + tabsContainer.clientWidth >= tabsContainer.scrollWidth - 8;
    scrollHint.style.opacity = atEnd ? '0' : '1';
    scrollHint.style.transition = 'opacity 0.3s';
  }

  if (tabsContainer) {
    tabsContainer.addEventListener('scroll', updateScrollHint, { passive: true });
    updateScrollHint();
  }

  // --- Scroll Spy for Navigation ---
  const navLinks = document.querySelectorAll('[data-nav-link]');
  const sections = Array.from(navLinks).map(link => document.querySelector(link.getAttribute('href'))).filter(Boolean);

  function updateScrollSpy() {
    const scrollY = window.scrollY + 150;
    let activeId = '';

    sections.forEach(section => {
      if (section.offsetTop <= scrollY) {
        activeId = section.id;
      }
    });

    navLinks.forEach(link => {
      const href = link.getAttribute('href');
      if (href === `#${activeId}`) {
        link.style.color = '#059669';
        link.style.fontWeight = '800';
      } else {
        link.style.color = '';
        link.style.fontWeight = '';
      }
    });
  }

  window.addEventListener('scroll', updateScrollSpy, { passive: true });
  updateScrollSpy();

  // --- Tab Switching Logic (with fade animation, ARIA & keyboard nav) ---
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  function activateTab(btn) {
    const targetId = btn.getAttribute('data-target');
    const targetContent = document.getElementById(targetId);

    // Remove active state from all tabs (both desktop & mobile)
    tabBtns.forEach(b => {
      b.classList.remove('active', 'text-[#059669]', 'border-[#059669]', 'font-bold',
        'bg-[#ecfdf5]', 'ring-[#059669]');
      b.classList.add('text-[#6b7684]', 'border-transparent', 'font-medium');
      // Restore mobile default styles
      if (!b.closest('#project-tabs')) {
        b.classList.add('bg-white', 'ring-[#e5e8eb]');
      }
      b.setAttribute('aria-selected', 'false');
    });

    // Fade out current visible tab, then switch
    const currentVisible = document.querySelector('.tab-content:not(.hidden)');

    if (currentVisible && targetContent && currentVisible !== targetContent) {
      currentVisible.style.opacity = '0';
      currentVisible.style.transition = 'opacity 0.15s ease-out';

      setTimeout(() => {
        tabContents.forEach(c => c.classList.add('hidden'));
        targetContent.classList.remove('hidden');
        targetContent.style.opacity = '0';

        void targetContent.offsetHeight;
        targetContent.style.transition = 'opacity 0.2s ease-in';
        targetContent.style.opacity = '1';

        const pending = targetContent.querySelectorAll('.mermaid:not([data-processed])');
        if (pending.length > 0) {
          mermaid.run({ nodes: pending }).catch(e => console.error(e));
        }
      }, 150);
    } else if (targetContent) {
      tabContents.forEach(c => c.classList.add('hidden'));
      targetContent.classList.remove('hidden');
      targetContent.style.opacity = '1';

      const pending = targetContent.querySelectorAll('.mermaid:not([data-processed])');
      if (pending.length > 0) {
        mermaid.run({ nodes: pending }).catch(e => console.error(e));
      }
    }

    // Add active state to ALL matching tabs (desktop + mobile sync)
    tabBtns.forEach(b => {
      if (b.getAttribute('data-target') === targetId) {
        b.classList.add('active', 'text-[#059669]', 'font-bold');
        b.classList.remove('text-[#6b7684]', 'font-medium');
        b.setAttribute('aria-selected', 'true');
        // Desktop-specific styles
        if (b.closest('#project-tabs')) {
          b.classList.add('border-[#059669]');
          b.classList.remove('border-transparent');
        } else {
          // Mobile-specific styles
          b.classList.add('bg-[#ecfdf5]', 'ring-[#059669]');
          b.classList.remove('bg-white', 'ring-[#e5e8eb]');
        }
      }
    });
  }

  if (tabBtns.length > 0) {
    tabBtns.forEach(btn => {
      btn.addEventListener('click', () => activateTab(btn));
    });

    // Target-specific default tab (BMAD로 바꾸려면 'tab-payment' → 'tab-bmad')
    const TARGET_DEFAULT_TAB = {
      celimax: 'tab-payment',
    };
    const portfolioTarget = document.querySelector('meta[name="portfolio-target"]')?.content;
    const defaultTabId = portfolioTarget && TARGET_DEFAULT_TAB[portfolioTarget];
    if (defaultTabId) {
      const defaultTabBtn = document.querySelector(`[data-target="${defaultTabId}"]`);
      if (defaultTabBtn) activateTab(defaultTabBtn);
    }

    // Keyboard navigation: Arrow keys to move between tabs
    tabBtns.forEach(btn => {
      btn.addEventListener('keydown', (e) => {
        const tablist = btn.closest('[role="tablist"]');
        if (!tablist) return;
        const tabs = Array.from(tablist.querySelectorAll('[role="tab"]'));
        const index = tabs.indexOf(btn);
        let target = null;

        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
          e.preventDefault();
          target = tabs[(index + 1) % tabs.length];
        } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
          e.preventDefault();
          target = tabs[(index - 1 + tabs.length) % tabs.length];
        } else if (e.key === 'Home') {
          e.preventDefault();
          target = tabs[0];
        } else if (e.key === 'End') {
          e.preventDefault();
          target = tabs[tabs.length - 1];
        }

        if (target) {
          target.focus();
          activateTab(target);
        }
      });
    });
  }

  // --- Diagram Pinch-Zoom ---
  document.querySelectorAll('.diagram-zoom-wrap').forEach(wrap => {
    const mermaidEl = wrap.querySelector('.mermaid');
    if (!mermaidEl) return;

    let scale = 1;
    let startDist = 0;
    let startScale = 1;

    function getDistance(touches) {
      const dx = touches[0].clientX - touches[1].clientX;
      const dy = touches[0].clientY - touches[1].clientY;
      return Math.sqrt(dx * dx + dy * dy);
    }

    wrap.addEventListener('touchstart', (e) => {
      if (e.touches.length === 2) {
        startDist = getDistance(e.touches);
        startScale = scale;
      }
    }, { passive: true });

    wrap.addEventListener('touchmove', (e) => {
      if (e.touches.length === 2) {
        const dist = getDistance(e.touches);
        scale = Math.min(Math.max(startScale * (dist / startDist), 0.5), 3);
        mermaidEl.style.transform = `scale(${scale})`;
        mermaidEl.style.transformOrigin = 'center top';
      }
    }, { passive: true });

    // Double-tap to reset zoom
    let lastTap = 0;
    wrap.addEventListener('touchend', (e) => {
      const now = Date.now();
      if (now - lastTap < 300 && e.touches.length === 0) {
        scale = 1;
        mermaidEl.style.transform = 'scale(1)';
        const hint = wrap.querySelector('.diagram-zoom-hint');
        if (hint) hint.style.display = 'none';
      }
      lastTap = now;
    });

    // Hide hint on first pinch
    wrap.addEventListener('touchmove', () => {
      const hint = wrap.querySelector('.diagram-zoom-hint');
      if (hint && hint.style.display !== 'none') {
        hint.style.opacity = '0';
        hint.style.transition = 'opacity 0.3s';
        setTimeout(() => { hint.style.display = 'none'; }, 300);
      }
    }, { passive: true, once: true });
  });
});
