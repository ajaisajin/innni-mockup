# INNNI Website — HTML Mockup Prototype

Static HTML mock designs for the INNNI association website (public site + member portal).

**This is a design prototype only** — no real backend, authentication, or payments.

## Quick start

Open in a browser (recommended: local server for best results):

```bash
cd innni-mockups
python3 -m http.server 8080
```

Then visit: **http://localhost:8080**

Or open `index.html` (root only) directly in your browser (double-click).

## Demo flow

1. Start at **Home** (`index.html` (root only))
2. Browse public pages via top navigation
3. Click **Member Login** → use any credentials → redirects to **Dashboard**
4. Explore member portal via sidebar

## Pages included

### Public (20 pages under `pages/`)

| Page | File |
|------|------|
| Home | `index.html` (root only) |
| About Us | `pages/about.html` |
| Membership | `pages/membership.html` |
| Register | `pages/register.html` |
| News listing | `pages/news.html` |
| News article | `pages/news-article.html` |
| Events | `pages/events.html` |
| Event detail | `pages/event-detail.html` |
| Resources | `pages/resources.html` |
| Advocacy & Policy | `pages/advocacy.html` |
| Career Support | `pages/career.html` |
| Working Groups | `pages/working-groups.html` |
| Governance | `pages/governance.html` |
| Safeguarding | `pages/safeguarding.html` |
| Data Protection | `pages/data-protection.html` |
| Contact | `pages/contact.html` |
| Legal & Compliance | `pages/legal.html` |
| Privacy Policy | `pages/privacy.html` |
| Terms & Conditions | `pages/terms.html` |
| Cookie Policy | `pages/cookies.html` |

### Member portal (8 pages)

| Page | File |
|------|------|
| Login | `pages/member/login.html` |
| Forgot password | `pages/member/forgot-password.html` |
| Dashboard | `pages/member/dashboard.html` |
| Profile | `pages/member/profile.html` |
| Announcements | `pages/member/news.html` |
| Download centre | `pages/member/resources.html` |
| Events | `pages/member/events.html` |
| Working groups | `pages/member/working-groups.html` |

## Images

Placeholder photos are stored locally in `assets/img/` (sourced from [Unsplash](https://unsplash.com) for mockup use only). Replace with INNNI's own photography before go-live.

## Tech

- HTML5 + [Tailwind CSS CDN](https://tailwindcss.com)
- Shared layout via `assets/js/layout.js` (header, footer, member sidebar)
- Custom styles in `assets/css/styles.css`
- Inter font (Google Fonts)

## Design theme

- **Primary:** Navy `#1e3a5f`
- **Accent:** Teal `#0d9488`
- Professional healthcare / association aesthetic

## Next steps (real app)

After client approves these mockups:

1. Convert layouts to **Next.js** components
2. Replace mock forms with real API + **Auth.js**
3. Integrate **Stripe** for membership payments
4. Add **Payload CMS** or custom admin for content

## Regenerating content pages

Some legal/info pages were generated via `_gen_pages.py`. Edit that script and re-run if needed.
