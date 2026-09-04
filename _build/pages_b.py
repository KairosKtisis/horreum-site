# About, Contact, Support, Security, Privacy, Terms, 404
from icons import ICON
from shell import APP, VINE

EFFECTIVE = "September 4, 2026"

def card(icon, title, text):
    return f'<div class="card"><span class="ico">{ICON[icon]}</span><h3>{title}</h3><p>{text}</p></div>'

# ── ABOUT ───────────────────────────────────────────────────────────────────
ABOUT = f'''
<section class="sec">
  <div class="wrap--narrow prose">
    <p class="eyebrow">About</p>
    <h1 style="font-size:clamp(36px,5vw,54px)">Built on the floor.</h1>
    <p class="lead">Horreum was not designed in a conference room. It was built by someone carrying a tray.</p>

    <h2>The story</h2>
    <p>Gabriel Collins has worked the front of house at a fine-dining chophouse in East Grand Rapids, Michigan for four years — server, bartender, expo, host, and now floor manager. The restaurant keeps wine lockers for its members: bottles bought from the list or brought from home, stored and served on request. The program is run by the wine program lead, and it is a good program. Gabe has helped keep it, and he has seen up close what it costs when the records disagree.</p>
    <p>A locker program is a promise: your bottles are here, and we know exactly what they are. Keeping that promise with a spreadsheet, a binder and a good memory means conflicting records, unlabelled bottles, and a server searching a cooler while a table waits. Every disagreement is a conversation with a member that nobody wants to have. That is the cost — in time, in trust, and occasionally in wine.</p>
    <p>So he built the thing he wished existed: one record that everyone works from, labels that cannot be confused, a pull that is tied to the exact bottle that left, and a member app that makes the program something worth talking about. He built it himself, outside of service, and it runs on that floor today.</p>

    <blockquote>The record is the product. Everything else is how you show it.</blockquote>

    <h2>The name</h2>
    <p>A <i>horreum</i> was a Roman storehouse — a fortified building for grain, oil and wine, run on ledgers so careful that some survive two thousand years later. The glyph is a storehouse’s front: a pediment, two columns, and the bar across the door.</p>

    <h2>What we believe</h2>
    <ul>
      <li><b>Members’ bottles are members’ property.</b> The software exists to keep that fact unarguable.</li>
      <li><b>Restraint is a feature.</b> Every screen was cut down until only what the floor needs is left. Phones are small and service is fast.</li>
      <li><b>Tasting notes are ours to write.</b> Every wine on the platform gets a long-form, guest-ready note in one voice, so a venue never has to staff that job.</li>
      <li><b>Nothing edits the past.</b> The activity log is append-only. A correction is a new entry, not a changed one.</li>
      <li><b>Built by request.</b> Every feature was asked for by someone doing the work. The roadmap is written by venues.</li>
    </ul>

    <h2>The company</h2>
    <p>Horreum is made by HORREUM LLC, a Michigan company based in Grand Rapids and founded in 2026. It is independent and founder-owned.</p>
    <p><a href="/contact">Get in touch</a> · <a href="mailto:hello@horreum.cloud" data-hz="email">hello@horreum.cloud</a></p>
  </div>
</section>
'''

# ── CONTACT ─────────────────────────────────────────────────────────────────
CONTACT = f'''
<section class="sec">
  <div class="wrap">
    <div class="split" style="align-items:start">
      <div>
        <p class="eyebrow">Contact</p>
        <h1 style="font-size:clamp(36px,5vw,54px)">See it on your floor.</h1>
        <p class="lead">A thirty-minute walkthrough with the person who built it — on a call, or at your venue if you are in West Michigan. Bring your binder. Ask about pricing and you’ll have a number the same day.</p>
        <p class="small">Prefer email? <a href="mailto:hello@horreum.cloud" data-hz="email">hello@horreum.cloud</a>. Already a member or on staff at a venue? <a href="/support">Support is this way</a>.</p>
        <p class="small muted">HORREUM LLC · Grand Rapids, Michigan · Replies within one business day.</p>
      </div>
      <form class="form" data-lead="demo" novalidate>
        <label class="field"><span>I would like to</span>
          <select name="kind"><option value="demo">Request a demo</option><option value="pricing">Ask about pricing</option><option value="contact">Ask a question</option></select></label>
        <div class="row2">
          <label class="field"><span>Your name</span><input name="name" autocomplete="name" required></label>
          <label class="field"><span>Email</span><input name="email" type="email" autocomplete="email" required></label>
        </div>
        <div class="row2">
          <label class="field"><span>Venue</span><input name="venue" autocomplete="organization" placeholder="Restaurant, club or wine bar"></label>
          <label class="field"><span>City</span><input name="city" autocomplete="address-level2"></label>
        </div>
        <div class="row2">
          <label class="field"><span>Locations</span><select name="locations"><option value="1">One</option><option value="2">Two</option><option value="3">Three</option><option value="5">Four to five</option><option value="6">Six or more</option></select></label>
          <label class="field"><span>Your role</span><input name="role" placeholder="Owner, GM, wine director…"></label>
        </div>
        <label class="field"><span>Anything we should know</span><textarea name="message" placeholder="How many lockers, how you keep them today, what is not working…"></textarea></label>
        <label class="hp" aria-hidden="true">Website<input name="website" tabindex="-1" autocomplete="off"></label>
        <div class="form-msg" aria-live="polite"></div>
        <button class="btn btn--gold btn--lg" type="submit">Send</button>
        <p class="small muted" style="margin:0">By sending, you agree to the <a href="/privacy">privacy policy</a>. No newsletters, no lists.</p>
      </form>
    </div>
  </div>
</section>
'''

# ── SUPPORT ─────────────────────────────────────────────────────────────────
SUPPORT = f'''
<section class="sec">
  <div class="wrap--narrow">
    <p class="eyebrow">Support</p>
    <h1 style="font-size:clamp(36px,5vw,54px)">Help, from people who use it.</h1>
    <p class="lead">The quickest way to reach us from inside the app is <b>Report a bug</b> in your profile menu — it arrives with the details we need. Otherwise, everything below.</p>
    <div class="cta-row"><a class="btn btn--gold" href="{APP}">Open the app</a><a class="btn btn--ghost" href="mailto:support@horreum.cloud" data-hz="support">support@horreum.cloud</a></div>
  </div>
</section>

<section class="sec sec--paper">
  <div class="wrap--narrow">
    <h2>For members</h2>
    <div class="faq">
      <details><summary>How do I sign in for the first time?</summary><div class="a"><p>Open the app, tap <b>Set up your account</b>, and enter the email address your venue has on file. We email you a six-digit code; enter it, choose a password, and you are in. Nothing in the invitation email can expire — the code is sent fresh when you ask for it.</p></div></details>
      <details><summary>I forgot my password.</summary><div class="a"><p>Tap <b>Forgot password</b> on the sign-in screen. We send a code to your email; enter it and choose a new password. To change your password while signed in, open your profile, tap <b>Change password</b>, and confirm with a code the same way.</p></div></details>
      <details><summary>How do I install it on my phone?</summary><div class="a"><p>On iPhone, open the app in Safari, tap <b>Share</b>, then <b>Add to Home Screen</b>. On Android, tap <b>Install app</b> when prompted, or choose it from the browser menu. The app then opens from your home screen like any other and remembers you.</p></div></details>
      <details><summary>How do I have a bottle brought to my table?</summary><div class="a"><p>Open your collection, tap the bottle, and show the code to your server. They scan it and are walked straight to your bottle. If you have several of the same wine, any of them satisfies it.</p></div></details>
      <details><summary>Where do tasting notes and drink windows come from?</summary><div class="a"><p>Horreum writes the tasting note for every wine on the platform. Drink windows and serving guidance are worked out for the bottle from its type, style and vintage.</p></div></details>
      <details><summary>The venue has my name wrong.</summary><div class="a"><p>Open your profile and change the name you go by; that is the name your app shows. Your venue keeps its own record for its ledger.</p></div></details>
      <details><summary>Can I request a bottle?</summary><div class="a"><p>Yes — from the venue’s list in Browse, tap <b>Request</b>. The team confirms it and settles it the usual way, or in the app if your venue has turned on payments.</p></div></details>
    </div>

    <h2 style="margin-top:56px">For venue staff</h2>
    <div class="faq">
      <details><summary>A label code is refused when I add a bottle.</summary><div class="a"><p>Every code is checked before it saves. <i>Already on a bottle</i> means that label is assigned; <i>failed its check digit</i> means a typo; <i>not a registered label</i> means the code was never minted for your venue. Use a code from one of your printed batches.</p></div></details>
      <details><summary>The printer jammed. Are those labels lost?</summary><div class="a"><p>No. Reprint the batch — the codes are identical — or void the batch if it never printed. Codes only enter circulation when they are scanned onto a bottle.</p></div></details>
      <details><summary>A bottle was pulled and the tag came back. Can we reuse it?</summary><div class="a"><p>Yes. A pulled bottle’s tag is <i>pending return</i>. Anyone with the reclaim permission can reclaim it and it becomes available again.</p></div></details>
      <details><summary>I logged a pull but cannot approve it.</summary><div class="a"><p>Servers and bartenders submit pulls; managers, directors and admins approve them. The bottle stays in the locker until it is approved. Your manager can grant approval rights per account.</p></div></details>
      <details><summary>Where do I set up bar coolers and the walk-in?</summary><div class="a"><p>Storage spots live under <b>Locations</b> in the management console. Add a spot per place a bottle can physically sit; choose it when adding a bottle, or move a bottle from the locker view.</p></div></details>
      <details><summary>A member never received their invitation.</summary><div class="a"><p>Check the email on their record, then <b>Resend invite</b>. They can also simply open the app and tap <b>Set up your account</b> with the email on file — the invitation itself is not required.</p></div></details>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap--narrow">
    <p class="eyebrow">Still stuck?</p>
    <h2>Write to support.</h2>
    <form class="form" data-lead="support" novalidate>
      <div class="row2">
        <label class="field"><span>Your name</span><input name="name" autocomplete="name" required></label>
        <label class="field"><span>Email</span><input name="email" type="email" autocomplete="email" required></label>
      </div>
      <div class="row2">
        <label class="field"><span>Venue</span><input name="venue" placeholder="Which venue’s program"></label>
        <label class="field"><span>You are a</span><select name="role"><option>Member</option><option>Venue staff</option><option>Venue owner or manager</option></select></label>
      </div>
      <label class="field"><span>What is happening</span><textarea name="message" placeholder="What you tapped, what you expected, what happened instead"></textarea></label>
      <label class="hp" aria-hidden="true">Website<input name="website" tabindex="-1" autocomplete="off"></label>
      <div class="form-msg" aria-live="polite"></div>
      <button class="btn btn--gold" type="submit">Send to support</button>
    </form>
  </div>
</section>
'''

# ── SECURITY ────────────────────────────────────────────────────────────────
SECURITY = f'''
<section class="sec">
  <div class="wrap--narrow prose">
    <p class="eyebrow">Security</p>
    <h1 style="font-size:clamp(36px,5vw,54px)">Careful with other people’s wine.</h1>
    <p class="lead">Horreum holds records that venues make promises on. This page says plainly how those records are kept.</p>

    <h2>Where data lives</h2>
    <p>Horreum runs on Supabase, a managed Postgres platform hosted on Amazon Web Services. Data is encrypted in transit with TLS and encrypted at rest by the hosting provider. Automated daily backups are kept by the hosting provider.</p>

    <h2>Tenant isolation</h2>
    <p>Every row in the database belongs to a venue, and Postgres row-level security decides who can read or write it. A member sees their own locker; staff see the locations they are assigned to; a venue never sees another venue. These rules are enforced by the database on every query — not by the app, and not by a screen that could be bypassed.</p>

    <h2>Permissions, enforced in the database</h2>
    <p>Actions that change records — adding a bottle, logging a pull, approving one, printing labels, reclaiming tags, editing the catalog — run as guarded database functions that check the caller’s role and permissions before doing anything. Hiding a button is a courtesy; the database is the control.</p>

    <h2>Sign-in</h2>
    <p>Accounts are set up and recovered with one-time codes sent to the account’s email, and protected with a password the account holder chooses. Passwords are stored only as salted hashes by the authentication provider. Changing a password requires a fresh code, even from a signed-in device.</p>

    <h2>Payments</h2>
    <p>If a venue turns on in-app payments, cards are collected and charged by Stripe under the venue’s own Stripe account. Card numbers never touch Horreum’s servers; Horreum records the amount, the last four digits and a reference for the receipt.</p>

    <h2>The record itself</h2>
    <p>The activity log is append-only. Adds, pulls, requests and changes are recorded with the actor and the moment, and are never edited afterward. Labels carry a check digit so a mistyped code cannot be saved against the wrong bottle, and every label is registered before it can be used.</p>

    <h2>Access and operations</h2>
    <p>Production access is limited to the platform operator, uses individual credentials, and is used for support and maintenance only. Edge functions that need elevated access run server-side with keys that are never shipped to a device.</p>

    <h2>Your data, your call</h2>
    <p>A venue can request a complete export of its records at any time and receives one on leaving the platform. Members can ask their venue, or us, to correct or delete their personal information — see the <a href="/privacy">privacy policy</a>.</p>

    <h2>Reporting a concern</h2>
    <p>If you believe you have found a security issue, write to <a href="mailto:support@horreum.cloud" data-hz="support">support@horreum.cloud</a> with the subject line <i>Security</i>. We read those first, and we will not pursue anyone who reports a problem in good faith.</p>
  </div>
</section>
'''

# ── PRIVACY ─────────────────────────────────────────────────────────────────
PRIVACY = f'''
<section class="sec">
  <div class="wrap--narrow prose">
    <p class="eyebrow">Legal</p>
    <h1 style="font-size:clamp(36px,5vw,54px)">Privacy policy</h1>
    <p class="meta">Effective {EFFECTIVE} · HORREUM LLC</p>
    <p class="lead">Horreum keeps records of wine kept for members by venues. This policy explains what we collect to do that, what we do with it, and what you can ask of us. It is written to be read.</p>

    <h2>Who we are</h2>
    <p>Horreum is operated by HORREUM LLC, a Michigan limited liability company (“Horreum”, “we”). The service consists of this website (horreum.cloud) and the Horreum application (app.horreum.cloud), which venues use to manage members’ wine and members use to see it.</p>

    <h2>Two roles</h2>
    <p>For a <b>venue</b> (a restaurant, club or bar that subscribes to Horreum), Horreum processes the venue’s records on the venue’s behalf. For a <b>member</b> (a person whose wine a venue keeps), the venue is the party that decides to keep records about you and what those records say; Horreum stores and displays them for the venue and for you. Questions about why a venue holds particular information about you are best put to the venue; we will help with anything about how it is stored and shown.</p>

    <h2>What we collect</h2>
    <ul>
      <li><b>Account information.</b> Your email address, the name you use, and, if a venue provides it, a phone number. Passwords are stored only as salted hashes by our authentication provider.</li>
      <li><b>Locker records.</b> The bottles kept for you — wine, vintage, how and when each arrived, where it is stored, when it was pulled and by whom — and any requests you make. Venues may attach a photo when logging a pull.</li>
      <li><b>Things you write.</b> Ratings and reviews, notes on your own bottles, and messages to the venue’s team.</li>
      <li><b>Preferences.</b> Your theme and locker finish, stored with your account so they follow you between devices.</li>
      <li><b>Technical information.</b> Standard server logs (IP address, browser, time) kept by our hosting provider for security and reliability, and, when you send a form on this website, the page you sent it from and your browser’s user-agent string.</li>
    </ul>

    <h2>What the app asks your device for</h2>
    <ul>
      <li><b>Camera</b> — only when staff scan a label or a member’s code. Images are processed on the device to read the code and are not stored.</li>
      <li><b>Location</b> — only if you choose the automatic day-and-night theme, which needs sunrise and sunset times for where you are. Your coordinates are stored on your device and are not sent to Horreum.</li>
      <li><b>Local storage</b> — to keep you signed in and remember your theme. This website itself sets no cookies and uses no analytics or advertising trackers.</li>
    </ul>

    <h2>How we use it</h2>
    <p>To run the service: showing venues and members the same records, sending the one-time codes that sign you in, notifying you when a bottle is added or pulled, and answering support requests. We do not sell personal information, and we do not use it for advertising.</p>

    <h2>Who else sees it</h2>
    <ul>
      <li><b>Your venue</b> and its staff, according to the permissions the venue sets.</li>
      <li><b>Supabase</b>, which hosts the database and authentication on Amazon Web Services in the United States.</li>
      <li><b>Stripe</b>, if your venue turns on in-app payments: Stripe collects and charges your card under the venue’s account, and we receive the amount, the last four digits and a reference.</li>
      <li><b>Google Fonts</b>, from which the application loads its typefaces; Google receives your IP address when the fonts load. This website hosts its own fonts and makes no such request.</li>
      <li><b>Open-Meteo</b>, which provides the weather shown in the Atlas for wine regions. Requests carry the coordinates of a wine region, never yours.</li>
      <li>Authorities, if the law requires it, and successors, if Horreum is ever sold — under this same policy.</li>
    </ul>

    <h2>How long we keep it</h2>
    <p>For as long as your venue’s program keeps records about you, and as the venue’s ledger requires afterward; a locker program’s history is part of its record. When a venue leaves Horreum, its data is exported to the venue and deleted from the platform within ninety days. Server logs are kept for a limited period by our hosting provider.</p>

    <h2>Your choices</h2>
    <ul>
      <li>See and correct your account details in the app’s profile.</li>
      <li>Ask us, or your venue, to correct or delete personal information. Some records — a bottle that was pulled on a given night — may be kept as part of the venue’s ledger with your name removed.</li>
      <li>Choose the fixed theme instead of the automatic one, and location is never requested.</li>
    </ul>
    <p>Residents of states with privacy laws that grant specific rights (including California) may exercise them by writing to us; we do not sell or share personal information for advertising, so there is nothing to opt out of on that front.</p>

    <h2>Age</h2>
    <p>Horreum is about wine and is offered to venues that serve adults. It is not directed to anyone under the legal drinking age, and we do not knowingly collect information from anyone under 18.</p>

    <h2>Changes</h2>
    <p>If this policy changes in a way that matters, we will say so in the app and update the date above. Continuing to use Horreum after a change means the new policy applies.</p>

    <h2>Contact</h2>
    <p>HORREUM LLC, Grand Rapids, Michigan · <a href="mailto:support@horreum.cloud" data-hz="support">support@horreum.cloud</a></p>
  </div>
</section>
'''

# ── TERMS ───────────────────────────────────────────────────────────────────
TERMS = f'''
<section class="sec">
  <div class="wrap--narrow prose">
    <p class="eyebrow">Legal</p>
    <h1 style="font-size:clamp(36px,5vw,54px)">Terms of service</h1>
    <p class="meta">Effective {EFFECTIVE} · HORREUM LLC</p>
    <p class="lead">These terms govern the use of Horreum by venues that subscribe to it and by members whose venues use it. By creating an account or using the service you agree to them.</p>

    <h2>1. Definitions</h2>
    <p>“Horreum”, “we” and “us” mean HORREUM LLC, a Michigan limited liability company. The “Service” means the horreum.cloud website and the Horreum application. A “Venue” is a business that subscribes to the Service to manage wine it keeps for its members. A “Member” is a person whose wine a Venue keeps and who is given access to the Service by that Venue. “You” means whichever of these you are.</p>

    <h2>2. The relationship</h2>
    <p>Horreum provides software. A Venue is the custodian of the bottles in its program and is responsible for its members, its staff, its records and its compliance with the laws that apply to serving and storing alcohol. Horreum does not take possession of, sell, or serve wine, and is not a party to any arrangement between a Venue and a Member. A Member’s bottles remain the Member’s property, subject to the Venue’s own terms.</p>

    <h2>3. Accounts</h2>
    <p>Accounts are personal. Keep your password to yourself, use the one-time codes we send only for your own sign-in, and tell your Venue or us if you believe your account has been used without your permission. Venues are responsible for the accounts they create for their staff and for the permissions they grant.</p>

    <h2>4. Venue subscriptions</h2>
    <ul>
      <li><b>Fees.</b> The Service is billed per active location at the rate on the pricing page or in your order form, monthly in advance, plus any applicable taxes.</li>
      <li><b>Changes.</b> We may change the rate with at least thirty days’ written notice; the new rate applies from your next billing period after the notice.</li>
      <li><b>Payments.</b> If a Venue enables in-app payments, those payments are processed by Stripe under the Venue’s own Stripe account and Stripe’s terms. Horreum does not hold funds.</li>
      <li><b>Term and ending.</b> The subscription continues month to month until either party ends it with the notice set out in the order form, or thirty days if none is stated. On ending, the Venue receives a complete export of its records, and the Venue’s data is deleted from the platform within ninety days.</li>
      <li><b>Non-payment.</b> If an invoice is more than thirty days overdue we may suspend the Venue’s access until it is settled; records are kept during suspension.</li>
    </ul>

    <h2>5. Acceptable use</h2>
    <p>Do not use the Service to break the law, to access records that are not yours, to probe or disrupt the platform, or to send anything abusive through it. Do not resell or white-label the Service to third parties except as agreed in writing. We may suspend an account that does any of these while we look into it.</p>

    <h2>6. Content</h2>
    <p>Ratings, reviews, notes and messages you write remain yours; you give Horreum and your Venue a licence to store and display them as part of the Service. Tasting notes, bottle artwork, the Atlas and the software itself are Horreum’s property and are licensed to you for use within the Service only. A Venue’s name, logo and branding remain the Venue’s, licensed to Horreum only to display them within the Venue’s program.</p>

    <h2>7. Availability and support</h2>
    <p>We aim to keep the Service available at all times and to tell you in advance of planned maintenance. Support is provided by email and from within the app. The Service may change as it improves; we will not remove a capability a Venue relies on without notice.</p>

    <h2>8. Disclaimers</h2>
    <p>The Service is provided as it is and as available. We do not promise that it will be uninterrupted or free of error. Drink windows, serving guidance and tasting notes are editorial guidance, not a warranty about any bottle. Horreum is not responsible for the condition, storage, loss or service of any bottle, which is between the Venue and the Member.</p>

    <h2>9. Limitation of liability</h2>
    <p>To the extent the law allows, Horreum is not liable for indirect, incidental, special or consequential losses, or for loss of profit, data or goodwill, arising from the Service. Horreum’s total liability for any claim in connection with the Service is limited to the fees the Venue paid to Horreum in the twelve months before the claim, or one hundred dollars for a Member.</p>

    <h2>10. Indemnity</h2>
    <p>A Venue will defend and indemnify Horreum against claims arising from the Venue’s program, its service of alcohol, its members and its staff, except to the extent caused by Horreum’s own breach of these terms.</p>

    <h2>11. Privacy</h2>
    <p>Our <a href="/privacy">privacy policy</a> is part of these terms. Venues are responsible for having a lawful basis to give Horreum the personal information of their members and staff.</p>

    <h2>12. Governing law</h2>
    <p>These terms are governed by the laws of the State of Michigan. Any dispute will be brought in the state or federal courts sitting in Kent County, Michigan, and both parties consent to that venue.</p>

    <h2>13. Changes to these terms</h2>
    <p>We may update these terms. Material changes will be announced in the app and dated above; a Venue that does not accept a change may end its subscription before the change takes effect.</p>

    <h2>14. Contact</h2>
    <p>HORREUM LLC, Grand Rapids, Michigan · <a href="mailto:hello@horreum.cloud" data-hz="email">hello@horreum.cloud</a></p>
  </div>
</section>
'''

# ── 404 ─────────────────────────────────────────────────────────────────────
NOTFOUND = f'''
<section class="sec center" style="min-height:60vh;display:flex;align-items:center">
  <div class="wrap--narrow">
    {VINE}
    <p class="eyebrow">404</p>
    <h1 style="font-size:clamp(36px,5vw,54px)">Not in the storehouse.</h1>
    <p class="lead">That page is not on our shelves. The entrance is this way.</p>
    <div class="cta-row" style="justify-content:center"><a class="btn btn--gold" href="/">Home</a><a class="btn btn--ghost" href="{APP}">Open the app</a></div>
  </div>
</section>
'''
