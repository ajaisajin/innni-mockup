/**
 * INNNI Mockup - shared header, footer, mobile menu
 *
 * siteRoot = relative path from current page to mockup root (folder with index.html)
 *   index.html           -> siteRoot: ''
 *   pages/*.html         -> siteRoot: '../'
 *   pages/member/*.html  -> siteRoot: '../../'
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

function resolvePaths(siteRoot) {
  const root = siteRoot || '';
  return {
    home: root + 'index.html',
    pages: root + 'pages/',
    member: root + 'pages/member/',
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
      `<a href="${pageHref(paths, n.href)}" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 hover:text-teal-600">${n.label}</a>`
  ).join('');

  return `
  <header class="bg-white shadow-sm sticky top-0 z-50 border-b border-slate-100">
    <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <a href="${homeHref}" class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-lg innni-gradient flex items-center justify-center text-white font-bold text-sm">IN</div>
          <div class="hidden sm:block">
            <span class="font-bold text-slate-800 text-lg leading-tight block">INNNI</span>
            <span class="text-xs text-slate-500">Internationally Educated Nurses Network</span>
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
          <a href="${memberHref}" class="ml-3 inline-flex items-center px-4 py-2 rounded-lg text-sm font-medium text-white bg-teal-600 hover:bg-teal-500 transition-colors">Member Login</a>
        </div>
        <button id="mobile-menu-btn" class="lg:hidden p-2 rounded-lg text-slate-600 hover:bg-slate-100" aria-label="Menu">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
        </button>
      </div>
      <div id="mobile-menu" class="hidden lg:hidden pb-4 border-t border-slate-100">
        <div class="flex flex-col gap-1 pt-3">
          ${NAV_PUBLIC.map((n) => `<a href="${pageHref(paths, n.href)}" class="px-3 py-2 rounded-lg text-sm ${navClass(n.id, activePage)}">${n.label}</a>`).join('')}
          <p class="px-3 pt-2 text-xs font-semibold text-slate-400 uppercase">More</p>
          ${NAV_MORE.map((n) => `<a href="${pageHref(paths, n.href)}" class="px-3 py-2 rounded-lg text-sm text-slate-600">${n.label}</a>`).join('')}
          <a href="${memberHref}" class="mx-3 mt-2 text-center px-4 py-2 rounded-lg text-sm font-medium text-white bg-teal-600">Member Login</a>
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
      <div class="flex justify-between items-center h-16">
        <a href="${homeHref}" class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-lg innni-gradient flex items-center justify-center text-white font-bold text-sm">IN</div>
          <div>
            <span class="font-bold text-slate-800">Member Portal</span>
            <span class="badge-member ml-2">Logged in</span>
          </div>
        </a>
        <div class="flex items-center gap-4">
          <span class="hidden sm:block text-sm text-slate-600">Welcome, <strong>Priya Sharma</strong></span>
          <a href="${homeHref}" class="text-sm text-slate-500 hover:text-teal-600">Back to site</a>
          <a href="${paths.member}login.html" class="text-sm text-red-600 hover:text-red-700 font-medium">Logout</a>
        </div>
      </div>
    </nav>
  </header>`;
}

function renderFooter(paths) {
  return `
  <footer class="bg-slate-900 text-slate-300 mt-auto">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
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
      <div class="border-t border-slate-700 mt-8 pt-8 flex flex-col sm:flex-row justify-between items-center gap-4 text-sm text-slate-500">
        <p>&copy; 2026 INNNI. All rights reserved.</p>
        <p>Mock design prototype — not a live application</p>
      </div>
    </div>
  </footer>`;
}

function renderMemberSidebar(activePage) {
  const links = NAV_MEMBER.map((n) => {
    const active = activePage === n.id ? 'active' : '';
    return `
    <a href="${n.href}" class="flex items-center gap-3 px-4 py-3 text-sm border-l-4 border-transparent hover:bg-slate-50 ${active ? 'active' : 'text-slate-600'}">
      <svg class="w-5 h-5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="${n.icon}"/></svg>
      ${n.label}
    </a>`;
  }).join('');
  return `
  <aside class="member-sidebar w-full md:w-64 bg-white border-r border-slate-200 flex-shrink-0">
    <div class="p-4 border-b border-slate-100">
      <p class="text-xs font-semibold text-slate-400 uppercase tracking-wide">Member Area</p>
      <p class="text-sm font-medium text-slate-800 mt-1">Membership: <span class="text-teal-600">Active</span></p>
      <p class="text-xs text-slate-500">Renews: 15 Jan 2027</p>
    </div>
    <nav class="py-2">${links}</nav>
  </aside>`;
}

function initLayout(options = {}) {
  const { page = '', siteRoot = '', area = 'public' } = options;
  const paths = resolvePaths(siteRoot);
  const headerEl = document.getElementById('site-header');
  const footerEl = document.getElementById('site-footer');
  const sidebarEl = document.getElementById('member-sidebar');

  if (headerEl) {
    headerEl.innerHTML =
      area === 'member' ? renderMemberHeader(paths) : renderPublicHeader(paths, page);
  }
  if (footerEl) {
    footerEl.innerHTML = renderFooter(paths);
  }
  if (sidebarEl && area === 'member') {
    sidebarEl.innerHTML = renderMemberSidebar(page);
  }

  const menuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', () => mobileMenu.classList.toggle('hidden'));
  }

  const cookieBanner = document.getElementById('cookie-banner');
  const cookieAccept = document.getElementById('cookie-accept');
  if (cookieBanner && cookieAccept) {
    if (localStorage.getItem('innni-cookie-ok')) cookieBanner.classList.add('hidden');
    cookieAccept.addEventListener('click', () => {
      localStorage.setItem('innni-cookie-ok', '1');
      cookieBanner.classList.add('hidden');
    });
  }
}
