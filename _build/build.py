# Build horreum.cloud:  python3 _build/build.py   (from the site folder)
import os, sys, json, datetime
sys.path.insert(0, os.path.dirname(__file__))
from shell import page, SITE, APP
import pages_a, pages_b

OUT = os.path.join(os.path.dirname(__file__), '..')
PRICE = 500

org_ld = json.dumps({
  "@context": "https://schema.org", "@type": "Organization", "name": "Horreum", "legalName": "HORREUM LLC",
  "url": SITE, "logo": SITE + "/assets/img/icon-512.png", "email": "hello@horreum.cloud",
  "address": {"@type": "PostalAddress", "addressLocality": "Grand Rapids", "addressRegion": "MI", "addressCountry": "US"},
  "sameAs": []
})
app_ld = json.dumps({
  "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Horreum",
  "applicationCategory": "BusinessApplication", "operatingSystem": "Web, iOS, Android",
  "description": "Wine reserve and locker management for restaurants, clubs and wine bars, with a member app.",
  "url": APP,
  "publisher": {"@type": "Organization", "name": "HORREUM LLC"}
})
faq_ld = json.dumps({
  "@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": "Why isn't the price on the page?", "acceptedAnswer": {"@type": "Answer", "text": "It depends on the size of the program — how many lockers, at how many locations. Ask and you will have a number the same day."}},
    {"@type": "Question", "name": "Is there a contract?", "acceptedAnswer": {"@type": "Answer", "text": "Service is billed monthly per active location. The notice period and any term are set in your order form, and there is no fee to leave; your records are exported on request."}},
    {"@type": "Question", "name": "What counts as a location?", "acceptedAnswer": {"@type": "Answer", "text": "One address where members' bottles are kept. A restaurant with a bar cooler, a walk-in and a cellar is one location with three storage spots."}},
    {"@type": "Question", "name": "Do members pay anything?", "acceptedAnswer": {"@type": "Answer", "text": "Not to Horreum. The member app is included in the venue's subscription."}}
  ]
})

PAGES = [
  ("index",    "Horreum — Wine reserve & locker management for venues", "Horreum runs a venue’s wine locker program end to end — the ledger, the labels, the pulls — and gives every member a collection worth showing off.", pages_a.HOME, "website", org_ld + '</script><script type="application/ld+json">' + app_ld, False),
  ("venues",   "Horreum for venues — the locker program you’d be proud to explain", "One record for every member, locker and bottle; QR labels that last; find-my-bottle at the table; roles, approvals and an append-only activity log.", pages_a.VENUES, "website", None, False),
  ("members",  "Horreum for members — your cellar, in your pocket", "Every bottle with its story, an atlas of where they came from, your history and ratings, and one tap to have a bottle brought to your table.", pages_a.MEMBERS, "website", None, False),
  ("pricing",  "Horreum pricing — one subscription per location, everything included", "One monthly subscription per location covers unlimited members, lockers, staff accounts, labels, the member app and Horreum’s tasting notes. Ask for a number and have it the same day.", pages_a.PRICING, "website", faq_ld, False),
  ("about",    "About Horreum — built on the floor", "Horreum was built by a floor manager at a fine-dining chophouse who saw what conflicting locker records cost. HORREUM LLC, Grand Rapids, Michigan.", pages_b.ABOUT, "website", None, False),
  ("contact",  "Contact Horreum — request a demo", "A thirty-minute walkthrough with the person who built it. Bring your binder.", pages_b.CONTACT, "website", None, False),
  ("support",  "Horreum support — help for members and venue staff", "Signing in, installing the app, labels, pulls, storage spots, and how to reach us.", pages_b.SUPPORT, "website", None, False),
  ("security", "Security at Horreum", "Where data lives, how venues are isolated, how permissions are enforced, and how payments and sign-in are handled.", pages_b.SECURITY, "website", None, False),
  ("privacy",  "Horreum privacy policy", "What Horreum collects to keep records of members’ wine, what it does with it, and what you can ask of us.", pages_b.PRIVACY, "website", None, False),
  ("terms",    "Horreum terms of service", "The terms that govern venues’ subscriptions and members’ use of Horreum.", pages_b.TERMS, "website", None, False),
  ("404",      "Not found — Horreum", "That page is not in the storehouse.", pages_b.NOTFOUND, "website", None, True),
]

for slug, title, desc, body, og, ld, noindex in PAGES:
    html = page(slug, title, desc, body, og, ld, noindex)
    with open(os.path.join(OUT, slug + '.html'), 'w', encoding='utf-8') as f: f.write(html)
    print('wrote', slug + '.html', len(html))

# sitemap + robots
today = datetime.date.today().isoformat()
urls = [s for s, *_ in PAGES if s != '404']
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
  '  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>\n' % (
    SITE + ('/' if s == 'index' else '/' + s), today, 'weekly' if s in ('index','pricing') else 'monthly', '1.0' if s == 'index' else ('0.8' if s in ('venues','members','pricing') else '0.5'))
  for s in urls) + '</urlset>\n'
open(os.path.join(OUT, 'sitemap.xml'), 'w').write(sm)
open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\nDisallow: /_build/\nSitemap: %s/sitemap.xml\n' % SITE)
open(os.path.join(OUT, 'CNAME'), 'w').write('horreum.cloud\n')
open(os.path.join(OUT, '.nojekyll'), 'w').write('')
open(os.path.join(OUT, 'site.webmanifest'), 'w').write(json.dumps({
  "name": "Horreum", "short_name": "Horreum", "start_url": "/", "display": "browser",
  "background_color": "#F2EBDC", "theme_color": "#F2EBDC",
  "icons": [{"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]
}, indent=2))
print('sitemap, robots, CNAME, manifest written')
