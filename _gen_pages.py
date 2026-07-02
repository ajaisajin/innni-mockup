#!/usr/bin/env python3
"""Generate simple content pages for INNNI mockups."""
from pathlib import Path

BASE = Path(__file__).parent

PAGES = [
    ("resources.html", "resources", "Resources & Publications", "Guidance documents, professional resources, and career information.", [
        ("NMC Registration Guide for IENs", "PDF · 2.4 MB · Updated May 2026"),
        ("CV Template — UK Nursing Roles", "DOCX · 156 KB"),
        ("Trust Interview Preparation Handbook", "PDF · 1.1 MB"),
        ("Continuing Professional Development Directory", "Web resource · Member access"),
        ("Wellbeing & Peer Support Resources", "PDF · 890 KB"),
    ], "resources"),
    ("advocacy.html", "advocacy", "Advocacy & Policy", "Representing internationally educated nurses at Trust, NIPEC, and regional policy level.", None, "advocacy"),
    ("career.html", "career", "Career Support", "Professional development, interview preparation, CV guidance, and education signposting.", None, "career"),
    ("working-groups.html", "working-groups", "Working Groups", "Education, Wellbeing, and Governance groups — purpose, leads, and how to join.", None, "working-groups"),
    ("governance.html", "governance", "Governance", "Constitution, Terms of Reference, Code of Conduct, and EDI statement.", None, "governance"),
    ("safeguarding.html", "safeguarding", "Safeguarding", "Our commitment to safeguarding members and guidance on raising concerns.", None, "safeguarding"),
    ("data-protection.html", "data-protection", "Data Protection (GDPR)", "How we manage personal data, consent, and confidentiality.", None, "data-protection"),
    ("legal.html", "legal", "Legal & Compliance", "Legal documentation and compliance information for INNNI.", None, "legal"),
    ("privacy.html", "privacy", "Privacy Policy", "How INNNI collects, uses, and protects your personal information.", None, "privacy"),
    ("terms.html", "terms", "Terms & Conditions", "Terms governing use of the INNNI website and membership services.", None, "terms"),
    ("cookies.html", "cookies", "Cookie Policy", "Information about cookies used on this website.", None, "cookies"),
]

BODY = {
    "advocacy": """<p>INNNI plays a vital role in representing internationally educated nurses across Northern Ireland. We engage with Health and Social Care Trusts, NIPEC, and regional policy forums to ensure your voice shapes workforce planning and professional standards.</p><h2>Our advocacy work includes</h2><ul><li>Formal consultation responses on nursing workforce policy</li><li>Representation at regional stakeholder meetings</li><li>Partnership with Trust equality and diversity leads</li><li>Evidence-based recommendations for onboarding and retention</li></ul>""",
    "career": """<p>Whether you are newly registered or an experienced practitioner, INNNI provides practical career support tailored to internationally educated nurses.</p><h2>Support available</h2><ul><li>Career pathway guidance for NI healthcare settings</li><li>CV reviews and UK-format templates</li><li>Mock interview sessions and preparation workshops</li><li>Leadership development opportunities</li><li>Signposting to education, training, and CPD programmes</li></ul><p><a href="events.html" class="text-teal-600 font-medium">View upcoming career workshops</a></p>""",
    "working-groups": """<p>INNNI working groups drive our activity across key areas. Each group has a defined purpose, elected lead, and open pathways for member involvement.</p>
<div class="grid md:grid-cols-1 gap-4 not-prose my-6">
<div class="card"><h3 class="font-bold text-slate-800">Education Working Group</h3><p class="text-sm text-teal-600">Lead: Maria Santos</p><p class="text-sm text-slate-600 mt-2">Focuses on CPD, training pathways, and professional development for IENs.</p><a href="contact.html" class="text-sm text-teal-600 font-medium mt-2 inline-block">Express interest &rarr;</a></div>
<div class="card"><h3 class="font-bold text-slate-800">Wellbeing Working Group</h3><p class="text-sm text-teal-600">Lead: Amara Okonkwo</p><p class="text-sm text-slate-600 mt-2">Peer support, mental health initiatives, and wellbeing programmes.</p><a href="contact.html" class="text-sm text-teal-600 font-medium mt-2 inline-block">Express interest &rarr;</a></div>
<div class="card"><h3 class="font-bold text-slate-800">Governance Working Group</h3><p class="text-sm text-teal-600">Lead: Dr. Sarah O'Brien</p><p class="text-sm text-slate-600 mt-2">Organisational governance, policy, and strategic planning.</p><a href="contact.html" class="text-sm text-teal-600 font-medium mt-2 inline-block">Express interest &rarr;</a></div>
</div>""",
    "governance": """<p>INNNI operates under a clear governance framework ensuring transparency, accountability, and member representation.</p><h2>Key documents</h2><ul><li><a href="#" class="text-teal-600">Constitution (PDF)</a></li><li><a href="#" class="text-teal-600">Terms of Reference (PDF)</a></li><li><a href="#" class="text-teal-600">Code of Conduct (PDF)</a></li><li><a href="#" class="text-teal-600">Equality, Diversity & Inclusion Statement (PDF)</a></li></ul>""",
    "safeguarding": """<p>INNNI is committed to safeguarding the welfare of our members, volunteers, and all those we engage with. We take all concerns seriously and provide clear pathways for reporting.</p><h2>Raising a concern</h2><p>If you have a safeguarding concern, contact our designated safeguarding lead at <strong>safeguarding@innni.org.uk</strong> or use our <a href="contact.html" class="text-teal-600">contact form</a> (select Safeguarding concern).</p><h2>External support</h2><ul><li>NSPCC Helpline: 0808 800 5000</li><li>Adult Social Care Gateway (via your Trust)</li><li>Police: 999 (emergency) or 101 (non-emergency)</li></ul>""",
    "data-protection": """<p>INNNI complies with UK GDPR and the Data Protection Act 2018. We are committed to handling member information securely and transparently.</p><h2>Your rights</h2><ul><li>Right to access your personal data</li><li>Right to rectification and erasure</li><li>Right to restrict or object to processing</li><li>Right to data portability</li></ul><p>See our <a href="privacy.html" class="text-teal-600">Privacy Policy</a> for full details. Contact <strong>dpo@innni.org.uk</strong> for data protection queries.</p>""",
    "legal": """<p>This section contains legal and compliance documentation relevant to INNNI operations and membership.</p><ul><li><a href="privacy.html" class="text-teal-600">Privacy Policy</a></li><li><a href="terms.html" class="text-teal-600">Terms & Conditions</a></li><li><a href="cookies.html" class="text-teal-600">Cookie Policy</a></li><li><a href="data-protection.html" class="text-teal-600">Data Protection (GDPR)</a></li><li><a href="governance.html" class="text-teal-600">Governance Documents</a></li></ul>""",
    "privacy": """<p><em>Mock legal text for design purposes only.</em></p><p>INNNI ("we", "us") is the data controller for personal information collected through this website and membership services. We collect information you provide during registration, event booking, and contact form submissions.</p><h2>How we use your data</h2><ul><li>To manage your membership and account</li><li>To send service-related communications</li><li>To improve our services and comply with legal obligations</li></ul>""",
    "terms": """<p><em>Mock legal text for design purposes only.</em></p><p>By using the INNNI website and becoming a member, you agree to these terms. Membership fees are non-refundable except where required by law. Members must comply with our Code of Conduct.</p>""",
    "cookies": """<p>We use essential cookies to operate the website and optional analytics cookies to understand usage. You can manage preferences via our cookie banner.</p><h2>Cookie types</h2><ul><li><strong>Essential:</strong> Session and authentication cookies</li><li><strong>Analytics:</strong> Google Analytics / Plausible (with consent)</li><li><strong>Preferences:</strong> Cookie consent choices</li></ul>""",
}

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | INNNI</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body class="bg-slate-50 min-h-screen flex flex-col">
  <div id="site-header"></div>
  <main>
    <section class="page-hero py-12">
      <div class="max-w-7xl mx-auto px-4"><h1 class="text-3xl font-bold">{title}</h1><p class="text-slate-200 mt-2">{subtitle}</p></div>
    </section>
    <div class="max-w-4xl mx-auto px-4 py-12 prose-innni">{content}</div>
  </main>
  <div id="site-footer"></div>
  <script src="assets/js/layout.js"></script>
  <script>initLayout({{ page: '{page_id}', base: '' }});</script>
</body>
</html>
'''

for fname, page_id, title, subtitle, resources, key in PAGES:
    if resources:
        items = "".join(
            f'<div class="card flex justify-between items-center not-prose mb-3"><div><h3 class="font-semibold text-slate-800">{r[0]}</h3><p class="text-sm text-slate-500">{r[1]}</p></div><button class="px-4 py-2 text-sm rounded-lg border border-teal-600 text-teal-600 hover:bg-teal-50">Download</button></div>'
            for r in resources
        )
        content = f"<p>Browse our library of professional materials. Some resources require membership.</p>{items}"
    else:
        content = BODY[key]
    html = TEMPLATE.format(title=title, subtitle=subtitle, content=content, page_id=page_id)
    (BASE / fname).write_text(html)
    print(f"Wrote {fname}")
