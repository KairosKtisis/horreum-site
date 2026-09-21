# Horreum — horreum.cloud page shell (v2). Run build.py to regenerate the HTML pages.
# The output is plain HTML (no client-side includes), so search engines and the
# App Store reviewer both see complete pages.
import datetime, html

SITE = "https://horreum.cloud"
APP  = "https://app.horreum.cloud"
YEAR = datetime.date.today().year
V    = "21"   # asset stamp: bump when site.css / site.js change, so a CDN never serves the old pair

GLYPH = '<img src="/assets/img/glyph-cream.svg" alt="" width="28" height="28">'
GLYPH_CREAM = GLYPH
VINE = ''
ARR = '<svg class="arr" width="14" height="10" viewBox="0 0 14 10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M1 5h12M9 1l4 4-4 4"/></svg>'

NAV = [("/venues", "Venues"), ("/members", "Members"), ("/pricing", "Pricing"), ("/about", "About"), ("/support", "Support")]

def header():
    links = "".join('<a href="%s">%s</a>' % (h, t) for h, t in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/" aria-label="Horreum — home">{GLYPH}<span>Horreum</span></a>
    <nav class="nav" aria-label="Primary">{links}</nav>
    <div class="header-cta">
      <a class="btn btn--ghost" href="{APP}">Sign in</a>
      <a class="btn btn--gold" href="/contact?kind=demo">Request a demo</a>
    </div>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M4 8h16M4 16h16"/></svg></button>
  </div>
</header>'''

def footer():
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="brand" href="/">{GLYPH}<span>Horreum</span></a>
        <p class="small" style="color:#B3A991;max-width:340px">The storehouse for your members’ wine. Reserve and locker management for restaurants, clubs and wine bars.</p>
        <p class="small" style="color:#857C68">HORREUM LLC · Grand Rapids, Michigan</p>
      </div>
      <div><h4>Product</h4><a href="/venues">For venues</a><a href="/members">For members</a><a href="/pricing">Pricing</a><a href="/security">Security</a><a href="{APP}">Sign in</a></div>
      <div><h4>Company</h4><a href="/about">About</a><a href="/contact">Contact</a><a href="/contact?kind=demo">Request a demo</a></div>
      <div><h4>Support</h4><a href="/support">Help &amp; FAQ</a><a href="mailto:gabriel@horreum.cloud" data-hz="support">gabriel@horreum.cloud</a><a href="/privacy">Privacy policy</a><a href="/terms">Terms of service</a><a href="/delete-account">Delete your account</a></div>
    </div>
    <div class="fine"><span>© <span data-hz="year">{YEAR}</span> HORREUM LLC. All rights reserved.</span><span><a href="/privacy">Privacy</a> · <a href="/terms">Terms</a> · <a href="/security">Security</a></span></div>
  </div>
  <div class="wordmark" aria-hidden="true">HORREUM</div>
</footer>
<script src="/assets/site.js?v={V}"></script>'''

def page(slug, title, description, body, og_type="website", jsonld=None, noindex=False):
    path = "/" if slug == "index" else "/" + slug
    canon = SITE + path
    t = html.escape(title); d = html.escape(description)
    ld = ""
    if jsonld:
        ld = '<script type="application/ld+json">' + jsonld + '</script>'
    robots = '<meta name="robots" content="noindex">' if noindex else ''
    return f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{canon}">
{robots}
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Horreum">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/img/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{SITE}/assets/img/og.png">
<meta name="theme-color" content="#06070A">
<meta name="color-scheme" content="dark light">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/playfair-display-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/cormorant-garamond-500-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/josefin-sans-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/fonts.css">
<link rel="stylesheet" href="/assets/site.css?v={V}">
<script>document.documentElement.className='js';</script>
{ld}
</head>
<body>
{header()}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
'''
