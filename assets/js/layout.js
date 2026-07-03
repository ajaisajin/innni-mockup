/**
 * INNNI Mockup - shared header, footer, mobile menu
 *
 * siteRoot = relative path from current page to mockup root (folder with index.html)
 *   index.html           -> siteRoot: ''
 *   pages/*.html         -> siteRoot: '../'
 *   pages/member/*.html  -> siteRoot: '../../'
 *   pages/admin/*.html   -> siteRoot: '../../'
 */

const NAV_PUBLIC = [
  { id: 'home', label: 'Home', href: 'index.html' },
  { id: 'about', label: 'About Us', href: 'about.html' },
  { id: 'membership', label: 'Membership', href: 'membership.html' },
  { id: 'news', label: 'News', href: 'news.html' },
  { id: 'events', label: 'Events', href: 'events.html' },
  { id: 'resources', label: 'Resources', href: 'resources.html' },
  { id: 'working-groups', label: 'Working Groups', href: 'working-groups.html' },
  { id: 'contact', label: 'Contact', href: 'contact.html' },
];

const NAV_MORE = [
  { id: 'advocacy', label: 'Advocacy & Policy', href: 'advocacy.html' },
  { id: 'career', label: 'Career Support', href: 'career.html' },
  { id: 'governance', label: 'Governance', href: 'governance.html' },
  { id: 'safeguarding', label: 'Safeguarding', href: 'safeguarding.html' },
  { id: 'data-protection', label: 'Data Protection', href: 'data-protection.html' },
  { id: 'legal', label: 'Legal & Compliance', href: 'legal.html' },
];

const NAV_MEMBER = [
  { id: 'dashboard', label: 'Dashboard', href: 'dashboard.html', icon: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6' },
  { id: 'profile', label: 'My Profile', href: 'profile.html', icon: 'M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z' },
  { id: 'member-news', label: 'Announcements', href: 'news.html', icon: 'M11 5.882V19.24a1.76 1.76 0 01-3.417.592l-2.147 6.15M18 13a3 3 0 100-6M5.436 13.683A4.001 4.001 0 017 6h1.832c4.1 0 7.625-1.234 9.168-3v14c-1.543-1.766-5.067-3-9.168-3H7a3.988 3.988 0 01-1.564-.317z' },
  { id: 'member-resources', label: 'Resources', href: 'resources.html', icon: 'M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z' },
  { id: 'member-events', label: 'Events', href: 'events.html', icon: 'M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z' },
  { id: 'member-groups', label: 'Working Groups', href: 'working-groups.html', icon: 'M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z' },
];

const NAV_ADMIN = [
  { id: 'admin-dashboard', label: 'Dashboard', href: 'dashboard.html', icon: 'M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z' },
  { id: 'admin-members', label: 'Members', href: 'members.html', icon: 'M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z', badge: '3' },
  { id: 'admin-events', label: 'Events', href: 'events.html', icon: 'M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z' },
  { id: 'admin-news', label: 'News & Announcements', href: 'news.html', icon: 'M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z' },
  { id: 'admin-resources', label: 'Resources', href: 'resources.html', icon: 'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z' },
  { id: 'admin-media', label: 'Media Library', href: 'media.html', icon: 'M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z' },
  { id: 'admin-pages', label: 'Pages', href: 'pages.html', icon: 'M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z' },
  { id: 'admin-contacts', label: 'Contact Messages', href: 'contacts.html', icon: 'M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z', badge: '5' },
  { id: 'admin-payments', label: 'Payments', href: 'payments.html', icon: 'M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z' },
  { id: 'admin-settings', label: 'Users & Roles', href: 'settings.html', icon: 'M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z M15 12a3 3 0 11-6 0 3 3 0 016 0z' },
];

function resolvePaths(siteRoot) {
  const root = siteRoot || '';
  return {
    home: root + 'index.html',
    pages: root + 'pages/',
    member: root + 'pages/member/',
    admin: root + 'pages/admin/',
  };
}

function pageHref(paths, filename) {
  if (filename === 'index.html') return paths.home;
  return paths.pages + filename;
}

function navClass(id, active) {
  return active === id
    ? 'nav-link-active text-teal-600'
    : 'text-slate-600 hover:text-teal-600';
}

function renderPublicHeader(paths, activePage) {
  const memberHref = paths.member + 'login.html';
  const homeHref = paths.home;
  const publicLinks = NAV_PUBLIC.map(
    (n) =>
      `<a href="${pageHref(paths, n.href)}" class="${navClass(n.id, activePage)} px-2 py-2 text-sm font-medium">${n.label}</a>`
  ).join('');
  const moreLinks = NAV_MORE.map(
    (n) =>
      `<a href="${pageHref(paths, n.href)}" class="block px-4 py-3 text-sm text-slate-600 hover:bg-slate-50 hover:text-teal-600">${n.label}</a>`
  ).join('');

  return `
  <header class="bg-white shadow-sm sticky top-0 z-50 border-b border-slate-100">
    <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-14 sm:h-16">
        <a href="${homeHref}" class="flex items-center gap-2 sm:gap-3 min-w-0">
          <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg innni-gradient flex items-center justify-center text-white font-bold text-sm flex-shrink-0">IN</div>
          <div class="min-w-0">
            <span class="font-bold text-slate-800 text-base sm:text-lg leading-tight block">INNNI</span>
            <span class="text-xs text-slate-500 hidden sm:block truncate">Internationally Educated Nurses</span>
          </div>
        </a>
        <div class="hidden lg:flex items-center gap-1">
          ${publicLinks}
          <div class="relative group ml-1">
            <button class="text-slate-600 hover:text-teal-600 px-2 py-2 text-sm font-medium flex items-center gap-1">
              More
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
            </button>
            <div class="absolute right-0 mt-1 w-52 bg-white rounded-lg shadow-lg border border-slate-100 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all py-1">
              ${moreLinks}
            </div>
          </div>
          <a href="${memberHref}" class="ml-3 inline-flex items-center px-4 py-2 rounded-lg text-sm font-medium text-white bg-teal-600 hover:bg-teal-500 transition-colors btn-touch">Member Login</a>
        </div>
        <button id="mobile-menu-btn" type="button" class="lg:hidden p-2 rounded-lg text-slate-600 hover:bg-slate-100" aria-label="Open menu" aria-expanded="false">
          <svg id="menu-icon-open" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
          <svg id="menu-icon-close" class="w-6 h-6 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>
      <div id="mobile-menu" class="hidden lg:hidden pb-4 border-t border-slate-100">
        <div class="flex flex-col gap-0.5 pt-2">
          ${NAV_PUBLIC.map((n) => `<a href="${pageHref(paths, n.href)}" class="mobile-nav-link px-3 py-3 rounded-lg text-sm ${navClass(n.id, activePage)}">${n.label}</a>`).join('')}
          <p class="px-3 pt-3 pb-1 text-xs font-semibold text-slate-400 uppercase">More</p>
          ${NAV_MORE.map((n) => `<a href="${pageHref(paths, n.href)}" class="mobile-nav-link px-3 py-3 rounded-lg text-sm text-slate-600">${n.label}</a>`).join('')}
          <a href="${memberHref}" class="mx-3 mt-3 text-center px-4 py-3 rounded-lg text-sm font-medium text-white bg-teal-600 btn-touch">Member Login</a>
        </div>
      </div>
    </nav>
  </header>`;
}

function renderMemberHeader(paths) {
  const homeHref = paths.home;
  return `
  <header class="bg-white shadow-sm sticky top-0 z-50 border-b border-slate-100">
    <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-14 sm:h-16 gap-2">
        <a href="${homeHref}" class="flex items-center gap-2 min-w-0">
          <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg innni-gradient flex items-center justify-center text-white font-bold text-sm flex-shrink-0">IN</div>
          <div class="min-w-0">
            <span class="font-bold text-slate-800 text-sm sm:text-base block truncate">Member Portal</span>
            <span class="badge-member text-xs">Active</span>
          </div>
        </a>
        <div class="flex items-center gap-2 sm:gap-4 flex-shrink-0">
          <span class="hidden md:block text-sm text-slate-600">Welcome, <strong>Priya</strong></span>
          <a href="${homeHref}" class="text-xs sm:text-sm text-slate-500 hover:text-teal-600 whitespace-nowrap">Back to site</a>
          <a href="${paths.member}login.html" class="text-xs sm:text-sm text-red-600 hover:text-red-700 font-medium whitespace-nowrap">Logout</a>
        </div>
      </div>
    </nav>
  </header>`;
}

function renderAdminHeader(paths) {
  const homeHref = paths.home;
  return `
  <header class="admin-header sticky top-0 z-50">
    <nav class="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-14 sm:h-16 gap-2">
        <a href="${paths.admin}dashboard.html" class="flex items-center gap-2 min-w-0">
          <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-slate-700 flex items-center justify-center text-white font-bold text-sm flex-shrink-0">IN</div>
          <div class="min-w-0">
            <span class="font-bold text-white text-sm sm:text-base block truncate">Admin Panel</span>
            <span class="badge-admin text-xs">INNNI</span>
          </div>
        </a>
        <div class="flex items-center gap-2 sm:gap-4 flex-shrink-0">
          <span class="hidden md:block text-sm text-slate-300">Signed in as <strong class="text-white">Sarah O'Neill</strong></span>
          <a href="${homeHref}" class="text-xs sm:text-sm text-slate-400 hover:text-white whitespace-nowrap">View site</a>
          <a href="${paths.admin}login.html" class="text-xs sm:text-sm text-red-400 hover:text-red-300 font-medium whitespace-nowrap">Logout</a>
        </div>
      </div>
    </nav>
  </header>`;
}

function renderFooter(paths) {
  return `
  <footer class="bg-slate-900 text-slate-300 mt-auto">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <div class="md:col-span-1">
          <div class="flex items-center gap-2 mb-4">
            <div class="w-9 h-9 rounded-lg innni-gradient flex items-center justify-center text-white font-bold text-xs">IN</div>
            <span class="font-bold text-white">INNNI</span>
          </div>
          <p class="text-sm text-slate-400">Supporting internationally educated nurses across Northern Ireland through advocacy, career development, and community.</p>
        </div>
        <div>
          <h4 class="font-semibold text-white mb-3">Quick Links</h4>
          <ul class="space-y-2 text-sm">
            <li><a href="${paths.pages}about.html" class="hover:text-teal-400">About Us</a></li>
            <li><a href="${paths.pages}membership.html" class="hover:text-teal-400">Membership</a></li>
            <li><a href="${paths.pages}events.html" class="hover:text-teal-400">Events</a></li>
            <li><a href="${paths.pages}resources.html" class="hover:text-teal-400">Resources</a></li>
          </ul>
        </div>
        <div>
          <h4 class="font-semibold text-white mb-3">Support</h4>
          <ul class="space-y-2 text-sm">
            <li><a href="${paths.pages}contact.html" class="hover:text-teal-400">Contact & Support</a></li>
            <li><a href="${paths.pages}safeguarding.html" class="hover:text-teal-400">Safeguarding</a></li>
            <li><a href="${paths.pages}career.html" class="hover:text-teal-400">Career Support</a></li>
            <li><a href="${paths.member}login.html" class="hover:text-teal-400">Member Portal</a></li>
          </ul>
        </div>
        <div>
          <h4 class="font-semibold text-white mb-3">Legal</h4>
          <ul class="space-y-2 text-sm">
            <li><a href="${paths.pages}privacy.html" class="hover:text-teal-400">Privacy Policy</a></li>
            <li><a href="${paths.pages}terms.html" class="hover:text-teal-400">Terms & Conditions</a></li>
            <li><a href="${paths.pages}cookies.html" class="hover:text-teal-400">Cookie Policy</a></li>
            <li><a href="${paths.pages}data-protection.html" class="hover:text-teal-400">Data Protection (GDPR)</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-slate-700 mt-8 pt-8 space-y-4">
        <p class="text-center text-xs text-slate-500">Designed by <span class="text-slate-400 font-medium">Vertex Business Solutions</span></p>
        <div class="flex flex-col sm:flex-row justify-between items-center gap-4 text-sm text-slate-500">
        <p>&copy; 2026 INNNI. All rights reserved.</p>
        <p class="flex flex-col sm:flex-row items-center gap-2 sm:gap-4 text-center">
          <span>Mock design prototype — not a live application</span>
          <a href="${paths.admin}login.html" class="text-slate-500 hover:text-teal-400 underline underline-offset-2">Staff login</a>
        </p>
        </div>
      </div>
    </div>
  </footer>`;
}

function renderAdminFooter() {
  return `
  <footer class="admin-footer mt-auto">
    <div class="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-8 py-4 space-y-3">
      <p class="text-center text-xs text-slate-500">Designed by <span class="text-slate-400 font-medium">Vertex Business Solutions</span></p>
      <div class="flex flex-col sm:flex-row justify-between items-center gap-2 text-xs text-slate-500">
        <p>&copy; 2026 INNNI Administration</p>
        <p>Mock admin prototype — not connected to live data</p>
      </div>
    </div>
  </footer>`;
}

function renderMemberSidebar(activePage) {
  const links = NAV_MEMBER.map((n) => {
    const active = activePage === n.id ? 'active' : '';
    return `
    <a href="${n.href}" class="${active}">
      <svg class="w-4 h-4 md:w-5 md:h-5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="${n.icon}"/></svg>
      <span>${n.label}</span>
    </a>`;
  }).join('');
  return `
  <aside class="member-sidebar">
    <div class="member-sidebar-info p-4 border-b border-slate-100">
      <p class="text-xs font-semibold text-slate-400 uppercase tracking-wide">Member Area</p>
      <p class="text-sm font-medium text-slate-800 mt-1">Membership: <span class="text-teal-600">Active</span></p>
      <p class="text-xs text-slate-500">Renews: 15 Jan 2027</p>
    </div>
    <nav class="member-nav">${links}</nav>
  </aside>`;
}

function renderAdminSidebar(activePage) {
  const links = NAV_ADMIN.map((n) => {
    const active = activePage === n.id ? 'active' : '';
    const badge = n.badge
      ? `<span class="admin-nav-badge">${n.badge}</span>`
      : '';
    return `
    <a href="${n.href}" class="${active}">
      <svg class="w-4 h-4 md:w-5 md:h-5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="${n.icon}"/></svg>
      <span class="flex-grow">${n.label}</span>${badge}
    </a>`;
  }).join('');
  return `
  <aside class="admin-sidebar">
    <div class="admin-sidebar-info p-4 border-b border-slate-700">
      <p class="text-xs font-semibold text-slate-400 uppercase tracking-wide">Administration</p>
      <p class="text-sm font-medium text-white mt-1">Role: <span class="text-teal-400">Super Admin</span></p>
    </div>
    <nav class="admin-nav">${links}</nav>
  </aside>`;
}

function setupMobileMenu() {
  const menuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const iconOpen = document.getElementById('menu-icon-open');
  const iconClose = document.getElementById('menu-icon-close');

  if (!menuBtn || !mobileMenu) return;

  const setOpen = (open) => {
    mobileMenu.classList.toggle('hidden', !open);
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    if (iconOpen) iconOpen.classList.toggle('hidden', open);
    if (iconClose) iconClose.classList.toggle('hidden', !open);
    document.body.style.overflow = open ? 'hidden' : '';
  };

  menuBtn.addEventListener('click', () => {
    setOpen(mobileMenu.classList.contains('hidden'));
  });

  mobileMenu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => setOpen(false));
  });
}

function initLayout(options = {}) {
  const { page = '', siteRoot = '', area = 'public' } = options;
  const paths = resolvePaths(siteRoot);
  const headerEl = document.getElementById('site-header');
  const footerEl = document.getElementById('site-footer');
  const sidebarEl = document.getElementById('member-sidebar') || document.getElementById('admin-sidebar');

  if (headerEl) {
    if (area === 'member') {
      headerEl.innerHTML = renderMemberHeader(paths);
    } else if (area === 'admin') {
      headerEl.innerHTML = renderAdminHeader(paths);
    } else {
      headerEl.innerHTML = renderPublicHeader(paths, page);
    }
  }
  if (footerEl) {
    footerEl.innerHTML = area === 'admin' ? renderAdminFooter() : renderFooter(paths);
  }
  if (sidebarEl && area === 'member') {
    sidebarEl.innerHTML = renderMemberSidebar(page);
  }
  if (sidebarEl && area === 'admin') {
    sidebarEl.innerHTML = renderAdminSidebar(page);
  }

  setupMobileMenu();

  const cookieBanner = document.getElementById('cookie-banner');
  const cookieAccept = document.getElementById('cookie-accept');
  if (cookieBanner && cookieAccept) {
    if (localStorage.getItem('innni-cookie-ok')) {
      cookieBanner.classList.add('hidden');
    } else {
      document.body.classList.add('has-cookie-banner');
    }
    cookieAccept.addEventListener('click', () => {
      localStorage.setItem('innni-cookie-ok', '1');
      cookieBanner.classList.add('hidden');
      document.body.classList.remove('has-cookie-banner');
    });
  }
}
