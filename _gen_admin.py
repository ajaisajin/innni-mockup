#!/usr/bin/env python3
"""Generate admin mockup pages. Dev only — do not share with client."""
from pathlib import Path

ROOT = Path(__file__).parent / "pages" / "admin"
ASSETS = "../../assets"
INIT = '<script src="{}/js/layout.js"></script>'.format(ASSETS)

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | INNNI Admin</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{assets}/css/styles.css">
</head>"""

ADMIN_SHELL = """
<body class="bg-slate-100 min-h-screen flex flex-col">
  <div id="site-header"></div>
  <div class="admin-layout">
    <div id="admin-sidebar"></div>
    <main class="admin-main">
{body}
    </main>
  </div>
  <div id="site-footer"></div>
  {init}
  <script>initLayout({{ page: '{page}', siteRoot: '../../', area: 'admin' }});</script>
</body>
</html>"""


def admin_page(title, page_id, body):
    return (
        HEAD.format(title=title, assets=ASSETS)
        + ADMIN_SHELL.format(body=body, init=INIT, page=page_id)
    )


PAGES = {
    "login.html": HEAD.format(title="Admin Login", assets=ASSETS)
    + """
<body class="bg-slate-900 min-h-screen flex flex-col">
  <div class="flex-grow flex items-center justify-center py-6 sm:py-12 px-4">
    <div class="w-full max-w-md">
      <div class="text-center mb-8">
        <div class="w-14 h-14 rounded-xl bg-slate-700 text-white font-bold text-lg flex items-center justify-center mx-auto mb-4">IN</div>
        <h1 class="text-xl sm:text-2xl font-bold text-white">INNNI Admin</h1>
        <p class="text-slate-400 mt-2 text-sm">Sign in to manage the website and membership</p>
      </div>
      <div class="card">
        <form class="space-y-4" onsubmit="event.preventDefault(); window.location.href='dashboard.html';">
          <div class="form-group"><label>Email</label><input type="email" value="admin@innni.org.uk" required></div>
          <div class="form-group"><label>Password</label><input type="password" value="password" required></div>
          <button type="submit" class="btn-admin-primary w-full">Sign In</button>
        </form>
        <p class="text-center text-xs text-slate-500 mt-6">Restricted access — authorised INNNI staff only</p>
      </div>
      <p class="text-center text-sm mt-6"><a href="../../index.html" class="text-slate-500 hover:text-teal-400">&larr; Back to public website</a></p>
    </div>
  </div>
</body>
</html>""",
    "dashboard.html": admin_page(
        "Dashboard",
        "admin-dashboard",
        """
      <div class="admin-page-header">
        <div>
          <h1 class="text-xl sm:text-2xl font-bold text-slate-800">Dashboard</h1>
          <p class="text-sm text-slate-500 mt-1">Overview of membership, content, and activity</p>
        </div>
        <a href="members.html" class="btn-admin-primary text-sm">Review pending members (3)</a>
      </div>
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4 mb-6">
        <div class="admin-stat"><div class="value text-teal-600">512</div><div class="label">Active members</div></div>
        <div class="admin-stat"><div class="value text-amber-600">3</div><div class="label">Pending approval</div></div>
        <div class="admin-stat"><div class="value">GBP 428</div><div class="label">Revenue this month</div></div>
        <div class="admin-stat"><div class="value">5</div><div class="label">Unread messages</div></div>
      </div>
      <div class="grid lg:grid-cols-2 gap-6">
        <section class="card">
          <h2 class="font-bold text-slate-800 mb-4">Recent registrations</h2>
          <div class="admin-table-wrap border-0">
            <table class="admin-table">
              <thead><tr><th>Name</th><th>Status</th><th>Date</th></tr></thead>
              <tbody>
                <tr><td><a href="member-detail.html" class="text-teal-600 hover:underline font-medium">Anita Kaur</a></td><td><span class="status-badge status-pending">Pending</span></td><td class="text-slate-500">2 Jul 2026</td></tr>
                <tr><td><a href="member-detail.html" class="text-teal-600 hover:underline font-medium">James Okonkwo</a></td><td><span class="status-badge status-pending">Pending</span></td><td class="text-slate-500">1 Jul 2026</td></tr>
                <tr><td><a href="member-detail.html" class="text-teal-600 hover:underline font-medium">Maria Santos</a></td><td><span class="status-badge status-active">Active</span></td><td class="text-slate-500">30 Jun 2026</td></tr>
              </tbody>
            </table>
          </div>
          <a href="members.html" class="text-sm text-teal-600 mt-4 inline-block hover:underline">View all members</a>
        </section>
        <section class="card">
          <h2 class="font-bold text-slate-800 mb-4">Quick actions</h2>
          <div class="grid sm:grid-cols-2 gap-3">
            <a href="news-edit.html" class="p-4 rounded-lg border border-slate-200 hover:border-teal-300 hover:bg-teal-50 transition-colors"><p class="font-medium text-slate-800">Create news article</p><p class="text-xs text-slate-500 mt-1">Public or member-only</p></a>
            <a href="event-edit.html" class="p-4 rounded-lg border border-slate-200 hover:border-teal-300 hover:bg-teal-50 transition-colors"><p class="font-medium text-slate-800">Add event</p><p class="text-xs text-slate-500 mt-1">Workshop, meeting, social</p></a>
            <a href="resources.html" class="p-4 rounded-lg border border-slate-200 hover:border-teal-300 hover:bg-teal-50 transition-colors"><p class="font-medium text-slate-800">Upload resource</p><p class="text-xs text-slate-500 mt-1">PDF, DOCX, links</p></a>
            <a href="contacts.html" class="p-4 rounded-lg border border-slate-200 hover:border-teal-300 hover:bg-teal-50 transition-colors"><p class="font-medium text-slate-800">View messages</p><p class="text-xs text-slate-500 mt-1">5 unread enquiries</p></a>
          </div>
        </section>
        <section class="card lg:col-span-2">
          <h2 class="font-bold text-slate-800 mb-4">Recent payments</h2>
          <div class="admin-table-wrap">
            <table class="admin-table">
              <thead><tr><th>Member</th><th>Plan</th><th>Amount</th><th>Status</th><th>Date</th></tr></thead>
              <tbody>
                <tr><td>Maria Santos</td><td>Annual</td><td>GBP 12.00</td><td><span class="status-badge status-active">Succeeded</span></td><td class="text-slate-500">30 Jun 2026</td></tr>
                <tr><td>Priya Sharma</td><td>Monthly</td><td>GBP 1.00</td><td><span class="status-badge status-active">Succeeded</span></td><td class="text-slate-500">28 Jun 2026</td></tr>
                <tr><td>David Chen</td><td>Annual</td><td>GBP 12.00</td><td><span class="status-badge status-active">Succeeded</span></td><td class="text-slate-500">25 Jun 2026</td></tr>
              </tbody>
            </table>
          </div>
          <a href="payments.html" class="text-sm text-teal-600 mt-4 inline-block hover:underline">View all transactions</a>
        </section>
      </div>""",
    ),
    "members.html": admin_page(
        "Members",
        "admin-members",
        """
      <div class="admin-page-header">
        <div>
          <h1 class="text-xl sm:text-2xl font-bold text-slate-800">Membership Management</h1>
          <p class="text-sm text-slate-500 mt-1">Approve, renew, and manage member accounts</p>
        </div>
        <button type="button" class="btn-admin-secondary text-sm" onclick="alert('Mock: export CSV')">Export CSV</button>
      </div>
      <div class="admin-toolbar">
        <div class="admin-search">
          <input type="search" placeholder="Search by name or email...">
          <button type="button" class="btn-admin-secondary text-sm px-4">Search</button>
        </div>
        <div class="flex flex-wrap gap-2">
          <select class="w-auto text-sm"><option>All statuses</option><option selected>Pending approval</option><option>Active</option><option>Expired</option></select>
          <select class="w-auto text-sm"><option>All plans</option><option>Annual</option><option>Monthly</option></select>
        </div>
      </div>
      <div class="admin-table-wrap">
        <table class="admin-table">
          <thead><tr><th>Member</th><th>Trust</th><th>Plan</th><th>Status</th><th>Joined</th><th>Actions</th></tr></thead>
          <tbody>
            <tr>
              <td><div class="font-medium text-slate-800">Anita Kaur</div><div class="text-xs text-slate-500">anita.kaur@example.com</div></td>
              <td>Belfast HSC Trust</td><td>Annual</td>
              <td><span class="status-badge status-pending">Pending</span></td>
              <td class="text-slate-500">2 Jul 2026</td>
              <td class="space-x-2 whitespace-nowrap"><a href="member-detail.html" class="text-teal-600 text-sm font-medium hover:underline">Review</a></td>
            </tr>
            <tr>
              <td><div class="font-medium text-slate-800">James Okonkwo</div><div class="text-xs text-slate-500">j.okonkwo@example.com</div></td>
              <td>Southern HSC Trust</td><td>Monthly</td>
              <td><span class="status-badge status-pending">Pending</span></td>
              <td class="text-slate-500">1 Jul 2026</td>
              <td><a href="member-detail.html" class="text-teal-600 text-sm font-medium hover:underline">Review</a></td>
            </tr>
            <tr>
              <td><div class="font-medium text-slate-800">Priya Sharma</div><div class="text-xs text-slate-500">priya.sharma@example.com</div></td>
              <td>South Eastern HSC Trust</td><td>Annual</td>
              <td><span class="status-badge status-active">Active</span></td>
              <td class="text-slate-500">15 Jan 2025</td>
              <td><a href="member-detail.html" class="text-teal-600 text-sm font-medium hover:underline">View</a></td>
            </tr>
            <tr>
              <td><div class="font-medium text-slate-800">David Chen</div><div class="text-xs text-slate-500">d.chen@example.com</div></td>
              <td>Northern HSC Trust</td><td>Annual</td>
              <td><span class="status-badge status-active">Active</span></td>
              <td class="text-slate-500">3 Mar 2024</td>
              <td><a href="member-detail.html" class="text-teal-600 text-sm font-medium hover:underline">View</a></td>
            </tr>
            <tr>
              <td><div class="font-medium text-slate-800">Elena Popescu</div><div class="text-xs text-slate-500">e.popescu@example.com</div></td>
              <td>Western HSC Trust</td><td>Monthly</td>
              <td><span class="status-badge status-expired">Expired</span></td>
              <td class="text-slate-500">10 Aug 2023</td>
              <td><a href="member-detail.html" class="text-teal-600 text-sm font-medium hover:underline">View</a></td>
            </tr>
          </tbody>
        </table>
      </div>
      <p class="text-sm text-slate-500 mt-4">Showing 5 of 512 members</p>""",
    ),
    "member-detail.html": admin_page(
        "Member Detail",
        "admin-members",
        """
      <a href="members.html" class="text-sm text-teal-600 hover:underline">&larr; Back to members</a>
      <div class="admin-page-header mt-4">
        <div>
          <h1 class="text-xl sm:text-2xl font-bold text-slate-800">Anita Kaur</h1>
          <p class="text-sm text-slate-500 mt-1">Registered 2 July 2026 · Awaiting administrator approval</p>
        </div>
        <div class="flex flex-wrap gap-2">
          <button type="button" class="btn-admin-primary text-sm" onclick="alert('Mock: member approved')">Approve membership</button>
          <button type="button" class="btn-admin-danger text-sm" onclick="alert('Mock: registration rejected')">Reject</button>
        </div>
      </div>
      <div class="grid lg:grid-cols-3 gap-6">
        <div class="lg:col-span-2 space-y-6">
          <section class="card">
            <h2 class="font-bold text-slate-800 mb-4">Personal details</h2>
            <dl class="grid sm:grid-cols-2 gap-4 text-sm">
              <div><dt class="text-slate-500">Email</dt><dd class="font-medium text-slate-800 mt-0.5">anita.kaur@example.com</dd></div>
              <div><dt class="text-slate-500">Phone</dt><dd class="font-medium text-slate-800 mt-0.5">+44 7700 900123</dd></div>
              <div><dt class="text-slate-500">NMC PIN</dt><dd class="font-medium text-slate-800 mt-0.5">21A4567E</dd></div>
              <div><dt class="text-slate-500">Trust / Employer</dt><dd class="font-medium text-slate-800 mt-0.5">Belfast Health & Social Care Trust</dd></div>
              <div><dt class="text-slate-500">Country of training</dt><dd class="font-medium text-slate-800 mt-0.5">India</dd></div>
              <div><dt class="text-slate-500">Email verified</dt><dd class="font-medium text-green-600 mt-0.5">Yes · 2 Jul 2026</dd></div>
            </dl>
          </section>
          <section class="card">
            <h2 class="font-bold text-slate-800 mb-4">Activity</h2>
            <ul class="space-y-3 text-sm">
              <li class="flex gap-3"><span class="text-slate-400 whitespace-nowrap">2 Jul</span><span>Completed registration form</span></li>
              <li class="flex gap-3"><span class="text-slate-400 whitespace-nowrap">2 Jul</span><span>Email verification confirmed</span></li>
              <li class="flex gap-3"><span class="text-slate-400 whitespace-nowrap">2 Jul</span><span>Payment received — GBP 12.00 (Annual)</span></li>
            </ul>
          </section>
        </div>
        <div class="space-y-6">
          <section class="card">
            <h2 class="font-bold text-slate-800 mb-4">Membership</h2>
            <p class="text-sm text-slate-500 mb-2">Status</p>
            <span class="status-badge status-pending mb-4">Pending approval</span>
            <p class="text-sm text-slate-500 mb-1">Plan</p>
            <p class="font-medium text-slate-800 mb-4">Annual — GBP 12/year</p>
            <label class="text-sm text-slate-500 block mb-1">Admin notes</label>
            <textarea rows="3" class="text-sm" placeholder="Internal notes (not visible to member)..."></textarea>
          </section>
          <section class="card">
            <h2 class="font-bold text-slate-800 mb-4">Actions</h2>
            <div class="space-y-2">
              <button type="button" class="btn-admin-secondary w-full text-sm" onclick="alert('Mock: reset password email sent')">Send password reset</button>
              <button type="button" class="btn-admin-secondary w-full text-sm" onclick="alert('Mock: membership suspended')">Suspend account</button>
            </div>
          </section>
        </div>
      </div>""",
    ),
    "events.html": admin_page(
        "Events",
        "admin-events",
        """
      <div class="admin-page-header">
        <div>
          <h1 class="text-xl sm:text-2xl font-bold text-slate-800">Event Management</h1>
          <p class="text-sm text-slate-500 mt-1">Create and manage workshops, meetings, and social events</p>
        </div>
        <a href="event-edit.html" class="btn-admin-primary text-sm">+ Add event</a>
      </div>
      <div class="admin-table-wrap">
        <table class="admin-table">
          <thead><tr><th>Event</th><th>Date</th><th>Type</th><th>Registrations</th><th>Status</th><th>Actions</th></tr></thead>
          <tbody>
            <tr>
              <td><div class="font-medium text-slate-800">CV & Interview Skills Workshop</div><div class="text-xs text-slate-500">Belfast · In person</div></td>
              <td>15 Jul 2026</td><td>Workshop</td><td>18 / 30</td>
              <td><span class="status-badge status-published">Published</span></td>
              <td class="whitespace-nowrap"><a href="event-edit.html" class="text-teal-600 text-sm font-medium hover:underline">Edit</a></td>
            </tr>
            <tr>
              <td><div class="font-medium text-slate-800">Education Working Group Meeting</div><div class="text-xs text-slate-500">Online</div></td>
              <td>22 Jul 2026</td><td>Meeting</td><td>24 / 50</td>
              <td><span class="status-badge status-published">Published</span></td>
              <td><a href="event-edit.html" class="text-teal-600 text-sm font-medium hover:underline">Edit</a></td>
            </tr>
            <tr>
              <td><div class="font-medium text-slate-800">Summer Social & Networking Evening</div><div class="text-xs text-slate-500">Belfast</div></td>
              <td>5 Aug 2026</td><td>Social</td><td>0 / 60</td>
              <td><span class="status-badge status-draft">Draft</span></td>
              <td><a href="event-edit.html" class="text-teal-600 text-sm font-medium hover:underline">Edit</a></td>
            </tr>
          </tbody>
        </table>
      </div>""",
    ),
    "event-edit.html": admin_page(
        "Edit Event",
        "admin-events",
        """
      <a href="events.html" class="text-sm text-teal-600 hover:underline">&larr; Back to events</a>
      <div class="admin-page-header mt-4">
        <div>
          <h1 class="text-xl sm:text-2xl font-bold text-slate-800">Edit Event</h1>
          <p class="text-sm text-slate-500 mt-1">CV & Interview Skills Workshop</p>
        </div>
        <div class="flex flex-wrap gap-2">
          <button type="button" class="btn-admin-secondary text-sm">Save draft</button>
          <button type="button" class="btn-admin-primary text-sm" onclick="alert('Mock: event published')">Publish</button>
        </div>
      </div>
      <form class="grid lg:grid-cols-3 gap-6" onsubmit="event.preventDefault(); alert('Mock: event saved');">
        <div class="lg:col-span-2 space-y-4">
          <div class="card space-y-4">
            <div class="form-group"><label>Event title *</label><input type="text" value="CV & Interview Skills Workshop" required></div>
            <div class="form-group"><label>Description</label>
              <div class="rich-editor-mock">
                <div class="rich-editor-toolbar">
                  <button type="button">B</button><button type="button">I</button><button type="button">Link</button><button type="button">List</button>
                </div>
                <div class="rich-editor-body">A practical half-day workshop designed for internationally educated nurses preparing for interviews within Northern Ireland's Health and Social Care Trusts.</div>
              </div>
            </div>
            <div class="grid sm:grid-cols-2 gap-4">
              <div class="form-group"><label>Date *</label><input type="date" value="2026-07-15"></div>
              <div class="form-group"><label>Time</label><input type="text" value="10:00 AM - 1:00 PM"></div>
            </div>
            <div class="form-group"><label>Venue</label><input type="text" value="Belfast City Centre"></div>
          </div>
        </div>
        <div class="space-y-4">
          <div class="card space-y-4">
            <div class="form-group"><label>Status</label><select><option selected>Published</option><option>Draft</option><option>Cancelled</option></select></div>
            <div class="form-group"><label>Event type</label><select><option selected>Workshop</option><option>Meeting</option><option>Social</option></select></div>
            <div class="form-group"><label>Capacity</label><input type="number" value="30"></div>
            <label class="flex items-center gap-2 text-sm"><input type="checkbox" checked class="w-4 h-4 rounded"> Members only registration</label>
            <label class="flex items-center gap-2 text-sm"><input type="checkbox" checked class="w-4 h-4 rounded"> Send confirmation email</label>
          </div>
          <div class="card">
            <label class="block text-sm font-medium text-slate-700 mb-2">Featured image</label>
            <img src="../../assets/img/workshop.jpg" alt="" class="w-full h-32 object-cover rounded-lg mb-2">
            <button type="button" class="btn-admin-secondary w-full text-sm" onclick="alert('Mock: open media library')">Choose from library</button>
          </div>
        </div>
      </form>""",
    ),
    "news.html": admin_page(
        "News",
        "admin-news",
        """
      <div class="admin-page-header">
        <div>
          <h1 class="text-xl sm:text-2xl font-bold text-slate-800">News & Announcements</h1>
          <p class="text-sm text-slate-500 mt-1">Manage public news and member-only announcements</p>
        </div>
        <a href="news-edit.html" class="btn-admin-primary text-sm">+ Create article</a>
      </div>
      <div class="flex flex-wrap gap-2 mb-4">
        <button class="px-3 py-1.5 rounded-full bg-teal-600 text-white text-sm">All</button>
        <button class="px-3 py-1.5 rounded-full bg-white border text-slate-600 text-sm">Public news</button>
        <button class="px-3 py-1.5 rounded-full bg-white border text-slate-600 text-sm">Member announcements</button>
        <button class="px-3 py-1.5 rounded-full bg-white border text-slate-600 text-sm">Drafts</button>
      </div>
      <div class="admin-table-wrap">
        <table class="admin-table">
          <thead><tr><th>Title</th><th>Category</th><th>Audience</th><th>Status</th><th>Date</th><th>Actions</th></tr></thead>
          <tbody>
            <tr>
              <td class="font-medium text-slate-800">INNNI response to regional nursing workforce plan</td>
              <td>Policy</td><td>Public</td>
              <td><span class="status-badge status-published">Published</span></td>
              <td class="text-slate-500">28 Jun 2026</td>
              <td><a href="news-edit.html" class="text-teal-600 text-sm font-medium hover:underline">Edit</a></td>
            </tr>
            <tr>
              <td class="font-medium text-slate-800">Member AGM date confirmed — 20 September</td>
              <td>Internal</td><td>Members only</td>
              <td><span class="status-badge status-published">Published</span></td>
              <td class="text-slate-500">30 Jun 2026</td>
              <td><a href="news-edit.html" class="text-teal-600 text-sm font-medium hover:underline">Edit</a></td>
            </tr>
            <tr>
              <td class="font-medium text-slate-800">Summer wellbeing programme for members</td>
              <td>Wellbeing</td><td>Public</td>
              <td><span class="status-badge status-draft">Draft</span></td>
              <td class="text-slate-500">—</td>
              <td><a href="news-edit.html" class="text-teal-600 text-sm font-medium hover:underline">Edit</a></td>
            </tr>
          </tbody>
        </table>
      </div>""",
    ),
    "news-edit.html": admin_page(
        "Edit News",
        "admin-news",
        """
      <a href="news.html" class="text-sm text-teal-600 hover:underline">&larr; Back to news</a>
      <div class="admin-page-header mt-4">
        <div>
          <h1 class="text-xl sm:text-2xl font-bold text-slate-800">Edit Article</h1>
        </div>
        <div class="flex flex-wrap gap-2">
          <button type="button" class="btn-admin-secondary text-sm">Save draft</button>
          <button type="button" class="btn-admin-primary text-sm" onclick="alert('Mock: article published')">Publish</button>
        </div>
      </div>
      <form class="grid lg:grid-cols-3 gap-6" onsubmit="event.preventDefault();">
        <div class="lg:col-span-2 space-y-4">
          <div class="card space-y-4">
            <div class="form-group"><label>Title *</label><input type="text" value="INNNI response to regional nursing workforce plan"></div>
            <div class="form-group"><label>Content</label>
              <div class="rich-editor-mock">
                <div class="rich-editor-toolbar">
                  <button type="button">B</button><button type="button">I</button><button type="button">H2</button><button type="button">Link</button><button type="button">Image</button>
                </div>
                <div class="rich-editor-body">INNNI has submitted a formal response to the Department of Health's regional nursing workforce consultation, highlighting the vital contribution of internationally educated nurses across Northern Ireland's Trusts.</div>
              </div>
            </div>
          </div>
        </div>
        <div class="space-y-4">
          <div class="card space-y-4">
            <div class="form-group"><label>Category</label><select><option selected>Policy</option><option>Wellbeing</option><option>Events</option><option>Workforce</option></select></div>
            <div class="form-group"><label>Audience</label><select><option selected>Public (website news)</option><option>Members only (portal announcement)</option></select></div>
            <div class="form-group"><label>Status</label><select><option selected>Published</option><option>Draft</option></select></div>
            <div class="form-group"><label>Publish date</label><input type="date" value="2026-06-28"></div>
          </div>
          <div class="card">
            <label class="block text-sm font-medium text-slate-700 mb-2">Featured image</label>
            <img src="../../assets/img/policy.jpg" alt="" class="w-full h-32 object-cover rounded-lg mb-2">
            <button type="button" class="btn-admin-secondary w-full text-sm">Choose from library</button>
          </div>
        </div>
      </form>""",
    ),
    "resources.html": admin_page(
        "Resources",
        "admin-resources",
        """
      <div class="admin-page-header">
        <div>
          <h1 class="text-xl sm:text-2xl font-bold text-slate-800">Resource Management</h1>
          <p class="text-sm text-slate-500 mt-1">Upload and manage downloadable documents</p>
        </div>
        <button type="button" class="btn-admin-primary text-sm" onclick="alert('Mock: upload dialog')">+ Upload resource</button>
      </div>
      <div class="admin-table-wrap">
        <table class="admin-table">
          <thead><tr><th>Resource</th><th>Type</th><th>Access</th><th>Downloads</th><th>Updated</th><th>Actions</th></tr></thead>
          <tbody>
            <tr>
              <td><div class="font-medium text-slate-800">NMC Registration Guide for IENs</div><div class="text-xs text-slate-500">PDF · 2.4 MB</div></td>
              <td>PDF</td><td>Public</td><td>342</td><td class="text-slate-500">May 2026</td>
              <td class="whitespace-nowrap"><button class="text-teal-600 text-sm font-medium hover:underline">Edit</button> · <button class="text-red-600 text-sm hover:underline">Delete</button></td>
            </tr>
            <tr>
              <td><div class="font-medium text-slate-800">Trust Onboarding Checklist 2026</div><div class="text-xs text-slate-500">PDF · 340 KB</div></td>
              <td>PDF</td><td>Members only</td><td>89</td><td class="text-slate-500">Jun 2026</td>
              <td><button class="text-teal-600 text-sm font-medium hover:underline">Edit</button> · <button class="text-red-600 text-sm hover:underline">Delete</button></td>
            </tr>
            <tr>
              <td><div class="font-medium text-slate-800">CV Template — UK Nursing Roles</div><div class="text-xs text-slate-500">DOCX · 156 KB</div></td>
              <td>DOCX</td><td>Public</td><td>218</td><td class="text-slate-500">Apr 2026</td>
              <td><button class="text-teal-600 text-sm font-medium hover:underline">Edit</button> · <button class="text-red-600 text-sm hover:underline">Delete</button></td>
            </tr>
          </tbody>
        </table>
      </div>""",
    ),
    "media.html": admin_page(
        "Media Library",
        "admin-media",
        """
      <div class="admin-page-header">
        <div>
          <h1 class="text-xl sm:text-2xl font-bold text-slate-800">Media Library</h1>
          <p class="text-sm text-slate-500 mt-1">Images and files used across the website</p>
        </div>
        <button type="button" class="btn-admin-primary text-sm" onclick="alert('Mock: upload files')">Upload files</button>
      </div>
      <div class="admin-toolbar">
        <div class="admin-search">
          <input type="search" placeholder="Search media...">
        </div>
        <select class="w-auto text-sm"><option>All types</option><option>Images</option><option>PDFs</option></select>
      </div>
      <div class="media-grid">
        <div class="media-item"><img src="../../assets/img/hero-nurses.jpg" alt=""><div class="media-meta">hero-nurses.jpg</div></div>
        <div class="media-item"><img src="../../assets/img/workshop.jpg" alt=""><div class="media-meta">workshop.jpg</div></div>
        <div class="media-item"><img src="../../assets/img/policy.jpg" alt=""><div class="media-meta">policy.jpg</div></div>
        <div class="media-item"><img src="../../assets/img/team-healthcare.jpg" alt=""><div class="media-meta">team-healthcare.jpg</div></div>
        <div class="media-item"><img src="../../assets/img/conference.jpg" alt=""><div class="media-meta">conference.jpg</div></div>
        <div class="media-item"><img src="../../assets/img/wellbeing.jpg" alt=""><div class="media-meta">wellbeing.jpg</div></div>
        <div class="media-item"><img src="../../assets/img/education.jpg" alt=""><div class="media-meta">education.jpg</div></div>
        <div class="media-item"><img src="../../assets/img/networking.jpg" alt=""><div class="media-meta">networking.jpg</div></div>
      </div>
      <p class="text-sm text-slate-500 mt-4">14 files · 8.2 MB total</p>""",
    ),
    "pages.html": admin_page(
        "Pages",
        "admin-pages",
        """
      <div class="admin-page-header">
        <div>
          <h1 class="text-xl sm:text-2xl font-bold text-slate-800">Page Management</h1>
          <p class="text-sm text-slate-500 mt-1">Edit static website pages and menu structure</p>
        </div>
      </div>
      <div class="admin-table-wrap">
        <table class="admin-table">
          <thead><tr><th>Page</th><th>URL slug</th><th>In menu</th><th>Last updated</th><th>Actions</th></tr></thead>
          <tbody>
            <tr><td class="font-medium">About Us</td><td class="text-slate-500">/about</td><td>Main nav</td><td class="text-slate-500">12 May 2026</td><td><button class="text-teal-600 text-sm font-medium hover:underline">Edit content</button></td></tr>
            <tr><td class="font-medium">Membership</td><td class="text-slate-500">/membership</td><td>Main nav</td><td class="text-slate-500">8 Jun 2026</td><td><button class="text-teal-600 text-sm font-medium hover:underline">Edit content</button></td></tr>
            <tr><td class="font-medium">Advocacy & Policy</td><td class="text-slate-500">/advocacy</td><td>More menu</td><td class="text-slate-500">3 Apr 2026</td><td><button class="text-teal-600 text-sm font-medium hover:underline">Edit content</button></td></tr>
            <tr><td class="font-medium">Safeguarding</td><td class="text-slate-500">/safeguarding</td><td>More menu</td><td class="text-slate-500">20 Mar 2026</td><td><button class="text-teal-600 text-sm font-medium hover:underline">Edit content</button></td></tr>
            <tr><td class="font-medium">Privacy Policy</td><td class="text-slate-500">/privacy</td><td>Footer</td><td class="text-slate-500">1 Jan 2026</td><td><button class="text-teal-600 text-sm font-medium hover:underline">Edit content</button></td></tr>
          </tbody>
        </table>
      </div>
      <section class="card mt-6">
        <h2 class="font-bold text-slate-800 mb-4">Main navigation order</h2>
        <p class="text-sm text-slate-600 mb-4">Drag to reorder menu items (mock — not functional in prototype).</p>
        <ol class="space-y-2 text-sm">
          <li class="p-3 bg-slate-50 rounded-lg border flex justify-between"><span>Home</span><span class="text-slate-400">Fixed</span></li>
          <li class="p-3 bg-white rounded-lg border flex justify-between"><span>About Us</span><span class="text-slate-400">↕</span></li>
          <li class="p-3 bg-white rounded-lg border flex justify-between"><span>Membership</span><span class="text-slate-400">↕</span></li>
          <li class="p-3 bg-white rounded-lg border flex justify-between"><span>News</span><span class="text-slate-400">↕</span></li>
          <li class="p-3 bg-white rounded-lg border flex justify-between"><span>Events</span><span class="text-slate-400">↕</span></li>
        </ol>
      </section>""",
    ),
    "contacts.html": admin_page(
        "Contact Messages",
        "admin-contacts",
        """
      <div class="admin-page-header">
        <div>
          <h1 class="text-xl sm:text-2xl font-bold text-slate-800">Contact Form Messages</h1>
          <p class="text-sm text-slate-500 mt-1">Enquiries submitted via the public contact form</p>
        </div>
      </div>
      <div class="flex flex-wrap gap-2 mb-4">
        <button class="px-3 py-1.5 rounded-full bg-teal-600 text-white text-sm">Unread (5)</button>
        <button class="px-3 py-1.5 rounded-full bg-white border text-slate-600 text-sm">Read</button>
        <button class="px-3 py-1.5 rounded-full bg-white border text-slate-600 text-sm">Archived</button>
      </div>
      <div class="space-y-3">
        <div class="card border-l-4 border-l-teal-500">
          <div class="flex flex-col sm:flex-row sm:justify-between sm:items-start gap-2 mb-2">
            <div>
              <p class="font-semibold text-slate-800">Membership enquiry — Annual plan</p>
              <p class="text-sm text-slate-500">From: Rachel Murphy · rachel.m@example.com · 2 Jul 2026, 09:14</p>
            </div>
            <span class="status-badge status-pending shrink-0">Unread</span>
          </div>
          <p class="text-sm text-slate-600">Hi, I'm an IEN recently registered with the NMC. Can you confirm whether student nurses are eligible for membership before full registration?</p>
          <div class="flex flex-wrap gap-2 mt-4">
            <button type="button" class="btn-admin-primary text-sm">Mark as read</button>
            <button type="button" class="btn-admin-secondary text-sm">Reply via email</button>
            <button type="button" class="btn-admin-secondary text-sm">Archive</button>
          </div>
        </div>
        <div class="card border-l-4 border-l-teal-500">
          <div class="flex flex-col sm:flex-row sm:justify-between sm:items-start gap-2 mb-2">
            <div>
              <p class="font-semibold text-slate-800">Event registration question</p>
              <p class="text-sm text-slate-500">From: Tom Walsh · 1 Jul 2026, 16:42</p>
            </div>
            <span class="status-badge status-pending shrink-0">Unread</span>
          </div>
          <p class="text-sm text-slate-600">Is the CV workshop open to non-members, or do I need to join INNNI first?</p>
          <div class="flex flex-wrap gap-2 mt-4">
            <button type="button" class="btn-admin-primary text-sm">Mark as read</button>
            <button type="button" class="btn-admin-secondary text-sm">Reply via email</button>
          </div>
        </div>
        <div class="card opacity-75">
          <div class="flex flex-col sm:flex-row sm:justify-between sm:items-start gap-2 mb-2">
            <div>
              <p class="font-semibold text-slate-800">General enquiry</p>
              <p class="text-sm text-slate-500">From: Helen O'Brien · 28 Jun 2026</p>
            </div>
            <span class="status-badge status-active shrink-0">Read</span>
          </div>
          <p class="text-sm text-slate-600">Thank you for the quick response regarding working group participation.</p>
        </div>
      </div>""",
    ),
    "payments.html": admin_page(
        "Payments",
        "admin-payments",
        """
      <div class="admin-page-header">
        <div>
          <h1 class="text-xl sm:text-2xl font-bold text-slate-800">Payment Transactions</h1>
          <p class="text-sm text-slate-500 mt-1">Stripe payment history and membership renewals</p>
        </div>
        <button type="button" class="btn-admin-secondary text-sm" onclick="alert('Mock: export report')">Export report</button>
      </div>
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4 mb-6">
        <div class="admin-stat"><div class="value text-teal-600">GBP 4,892</div><div class="label">Total revenue (2026)</div></div>
        <div class="admin-stat"><div class="value">428</div><div class="label">Transactions</div></div>
        <div class="admin-stat"><div class="value text-green-600">99.3%</div><div class="label">Success rate</div></div>
        <div class="admin-stat"><div class="value text-red-600">3</div><div class="label">Failed payments</div></div>
      </div>
      <div class="admin-toolbar">
        <select class="w-full sm:w-auto text-sm"><option>All time</option><option selected>This month</option><option>Last 30 days</option></select>
        <select class="w-full sm:w-auto text-sm"><option>All statuses</option><option>Succeeded</option><option>Failed</option><option>Refunded</option></select>
      </div>
      <div class="admin-table-wrap">
        <table class="admin-table">
          <thead><tr><th>Transaction ID</th><th>Member</th><th>Plan</th><th>Amount</th><th>Status</th><th>Date</th></tr></thead>
          <tbody>
            <tr><td class="font-mono text-xs text-slate-500">pi_3Nx8k2LkdIw...</td><td>Maria Santos</td><td>Annual</td><td>GBP 12.00</td><td><span class="status-badge status-active">Succeeded</span></td><td class="text-slate-500">30 Jun 2026</td></tr>
            <tr><td class="font-mono text-xs text-slate-500">pi_3Nx7j1LkdIw...</td><td>Priya Sharma</td><td>Monthly</td><td>GBP 1.00</td><td><span class="status-badge status-active">Succeeded</span></td><td class="text-slate-500">28 Jun 2026</td></tr>
            <tr><td class="font-mono text-xs text-slate-500">pi_3Nx6i0LkdIw...</td><td>David Chen</td><td>Annual</td><td>GBP 12.00</td><td><span class="status-badge status-active">Succeeded</span></td><td class="text-slate-500">25 Jun 2026</td></tr>
            <tr><td class="font-mono text-xs text-slate-500">pi_3Nx5h9LkdIw...</td><td>Elena Popescu</td><td>Monthly</td><td>GBP 1.00</td><td><span class="status-badge status-expired">Failed</span></td><td class="text-slate-500">20 Jun 2026</td></tr>
          </tbody>
        </table>
      </div>
      <p class="text-xs text-slate-400 mt-4">Payments processed securely via Stripe. PCI compliance handled by Stripe-hosted checkout.</p>""",
    ),
    "settings.html": admin_page(
        "Users & Roles",
        "admin-settings",
        """
      <div class="admin-page-header">
        <div>
          <h1 class="text-xl sm:text-2xl font-bold text-slate-800">Users & Roles</h1>
          <p class="text-sm text-slate-500 mt-1">Manage admin accounts and permissions</p>
        </div>
        <button type="button" class="btn-admin-primary text-sm" onclick="alert('Mock: invite admin user')">+ Invite admin</button>
      </div>
      <div class="admin-table-wrap mb-8">
        <table class="admin-table">
          <thead><tr><th>User</th><th>Role</th><th>Last login</th><th>Status</th><th>Actions</th></tr></thead>
          <tbody>
            <tr>
              <td><div class="font-medium text-slate-800">Sarah O'Neill</div><div class="text-xs text-slate-500">admin@innni.org.uk</div></td>
              <td>Super Admin</td><td class="text-slate-500">Today, 08:32</td>
              <td><span class="status-badge status-active">Active</span></td>
              <td><button class="text-teal-600 text-sm font-medium hover:underline">Edit</button></td>
            </tr>
            <tr>
              <td><div class="font-medium text-slate-800">Michael Byrne</div><div class="text-xs text-slate-500">m.byron@innni.org.uk</div></td>
              <td>Content Editor</td><td class="text-slate-500">Yesterday</td>
              <td><span class="status-badge status-active">Active</span></td>
              <td><button class="text-teal-600 text-sm font-medium hover:underline">Edit</button></td>
            </tr>
            <tr>
              <td><div class="font-medium text-slate-800">Claire Devlin</div><div class="text-xs text-slate-500">c.devlin@innni.org.uk</div></td>
              <td>Membership Admin</td><td class="text-slate-500">3 days ago</td>
              <td><span class="status-badge status-active">Active</span></td>
              <td><button class="text-teal-600 text-sm font-medium hover:underline">Edit</button></td>
            </tr>
          </tbody>
        </table>
      </div>
      <section class="card">
        <h2 class="font-bold text-slate-800 mb-4">Role permissions</h2>
        <div class="admin-table-wrap border-0">
          <table class="admin-table">
            <thead><tr><th>Permission</th><th>Super Admin</th><th>Content Editor</th><th>Membership Admin</th></tr></thead>
            <tbody class="text-center">
              <tr><td class="text-left font-medium">Manage members</td><td>✓</td><td>—</td><td>✓</td></tr>
              <tr><td class="text-left font-medium">Manage content & events</td><td>✓</td><td>✓</td><td>—</td></tr>
              <tr><td class="text-left font-medium">View payments</td><td>✓</td><td>—</td><td>✓</td></tr>
              <tr><td class="text-left font-medium">Manage admin users</td><td>✓</td><td>—</td><td>—</td></tr>
            </tbody>
          </table>
        </div>
      </section>
      <section class="card mt-6">
        <h2 class="font-bold text-slate-800 mb-2">Membership settings</h2>
        <label class="flex items-start gap-3 text-sm mt-4"><input type="checkbox" checked class="w-4 h-4 rounded mt-0.5"> Require administrator approval for new registrations</label>
        <label class="flex items-start gap-3 text-sm mt-3"><input type="checkbox" checked class="w-4 h-4 rounded mt-0.5"> Send email notification when new member registers</label>
        <label class="flex items-start gap-3 text-sm mt-3"><input type="checkbox" checked class="w-4 h-4 rounded mt-0.5"> Auto-send renewal reminder 30 days before expiry</label>
        <button type="button" class="btn-admin-primary text-sm mt-4" onclick="alert('Mock: settings saved')">Save settings</button>
      </section>""",
    ),
}

if __name__ == "__main__":
    ROOT.mkdir(parents=True, exist_ok=True)
    for name, html in PAGES.items():
        (ROOT / name).write_text(html.strip() + "\n")
        print("wrote", name)
    print(f"Done — {len(PAGES)} admin pages")
