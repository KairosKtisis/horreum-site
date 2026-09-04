# horreum.cloud — the Horreum business site

A static site: plain HTML, one stylesheet, one script, self-hosted fonts. No framework, no build
step required to serve it. It is designed to sit on a CDN (GitHub Pages, Cloudflare Pages, Netlify)
and take any amount of traffic; the only dynamic piece is the contact/demo/support form, which posts
to a guarded function on the Horreum platform (`submit_site_lead`) and shows up in the operator
console under **Requests → Website leads**.

## Layout

```
index.html        Home                 support.html    Help & FAQ (App Store support URL)
venues.html       For venues           security.html   How data is handled
members.html      For members          privacy.html    Privacy policy (App Store privacy URL)
pricing.html      Pricing              terms.html      Terms of service
about.html        Founder story        404.html        Not found
contact.html      Demo / contact form
assets/site.css   assets/site.js   assets/fonts.css + assets/fonts/   assets/img/   assets/shots/
sitemap.xml  robots.txt  site.webmanifest  CNAME  .nojekyll  favicon.png  apple-touch-icon.png
_build/           the page generator (optional — see below)
```

Links are extensionless (`/pricing`); GitHub Pages, Cloudflare Pages and Netlify all serve
`pricing.html` for that path.

## Editing

Two ways:

1. **Edit the HTML directly.** Each page is complete. The header and footer are repeated in every
   file — search for `site-header` / `site-footer` to change them everywhere.
2. **Regenerate from the templates.** `python3 _build/build.py` (from this folder) rewrites every
   page from `_build/pages_a.py`, `_build/pages_b.py` and `_build/shell.py`. If you edit the HTML by
   hand, don't run the generator afterwards (it will overwrite your edits).

Pricing is by inquiry (no number on the site). The one address the site quotes (`gabriel@horreum.cloud`)
lives in `assets/site.js`; change it there and every page follows.

## Deploy — GitHub Pages at the apex (recommended)

1. This folder (`C:\dev\horreum-site`) is its own repository, tracking
   `github.com/KairosKtisis/horreum-site` on branch `main`. Commit and push from here (never from
   inside horreum-platform); the `CNAME` file containing `horreum.cloud` and the empty `.nojekyll`
   are part of the tree and must stay.
2. Repository → Settings → Pages → Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
   Under *Custom domain* enter `horreum.cloud` and tick *Enforce HTTPS* once the certificate issues.
3. DNS — horreum.cloud is served by Cloudflare (henrik/mallory.ns.cloudflare.com). In the zone's DNS
   records add the rows below with **Proxy status: DNS only** (grey cloud) so GitHub can verify the
   domain and issue the certificate. The apex has no records today:

   | Type  | Name | Value                          |
   |-------|------|--------------------------------|
   | A     | @    | 185.199.108.153                |
   | A     | @    | 185.199.109.153                |
   | A     | @    | 185.199.110.153                |
   | A     | @    | 185.199.111.153                |
   | AAAA  | @    | 2606:50c0:8000::153            |
   | AAAA  | @    | 2606:50c0:8001::153            |
   | AAAA  | @    | 2606:50c0:8002::153            |
   | AAAA  | @    | 2606:50c0:8003::153            |
   | CNAME | www  | kairosktisis.github.io          |

   `app` is already a DNS-only CNAME to `kairosktisis.github.io` for the app repo and is untouched.
   With the `www` CNAME in place, GitHub redirects `www.horreum.cloud` to the apex automatically.
4. Wait for DNS (minutes to an hour), then check https://horreum.cloud/ and https://horreum.cloud/privacy.

Cloudflare Pages / Netlify: point the project at the same repo, root directory `/`, no build
command, publish directory `/`. Add the custom domain in their dashboard and follow their DNS
prompt instead of the table above.

## App Store links

- Privacy policy URL: `https://horreum.cloud/privacy`
- Support URL: `https://horreum.cloud/support`
- Marketing URL: `https://horreum.cloud`

## Forms

`assets/site.js` posts to `submit_site_lead` with the public anon key. The function validates,
rejects bots via a hidden field, and rate-limits (5 per address per hour, 300 site-wide per hour).
Submissions appear in the operator console; there is no email notification yet (that needs an email
provider key — Resend or similar — wired to a database webhook).
