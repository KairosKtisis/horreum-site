# About, Contact, Support, Security, Privacy, Terms, 404
from icons import ICON
from shell import APP, VINE

EFFECTIVE = "September 21, 2026"

def card(icon, title, text):
    return f'<div class="card"><span class="ico">{ICON[icon]}</span><h3>{title}</h3><p>{text}</p></div>'

# ── ABOUT ───────────────────────────────────────────────────────────────────
ABOUT = f'''
<section class="sec">
  <div class="wrap--narrow prose">
    <p class="eyebrow">About</p>
    <h1>About Horreum.</h1>
    <p class="lead">Horreum is reserve and locker management software for restaurants, clubs and wine bars, made by an independent company in Grand Rapids, Michigan.</p>

    <h2>The story</h2>
    <p>Horreum was founded by Gabriel Collins. He has worked in fine dining for four years — serving, bartending, running expo and the host stand — and has been a floor manager for the last year and a half.</p>
    <p>Working around a wine locker program, he saw how much care goes into looking after members’ bottles, and how much of that care goes into the records: what is in each locker, where each bottle sits, what was opened and when. He also saw that most members never get to see their own collection.</p>
    <p>Horreum is his answer to both. He designed and built it independently, on his own time and as its own company, for any venue that keeps wine for its members. It gives the venue one precise record to work from, and gives members an app that makes their collection something to enjoy.</p>

    <h2>The name</h2>
    <p>A <i>horreum</i> was a Roman storehouse — a fortified building for grain, oil and wine, run on careful ledgers. The glyph is a storehouse’s front: a pediment, two columns, and the bar across the door.</p>

    <h2>The company</h2>
    <p>Horreum is made by HORREUM LLC, a Michigan company based in Grand Rapids and founded in 2026. It is independent and founder-owned.</p>
    <p><a href="/contact">Get in touch</a> · <a href="mailto:gabriel@horreum.cloud" data-hz="email">gabriel@horreum.cloud</a></p>
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
        <p class="lead">A thirty-minute walkthrough with the person who built it — on a call, or at your venue if you are in West Michigan.</p>
        <p class="small">Prefer email? <a href="mailto:gabriel@horreum.cloud" data-hz="email">gabriel@horreum.cloud</a>. Already a member or on staff at a venue? <a href="/support">Support is this way</a>.</p>
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
    <div class="cta-row"><a class="btn btn--gold" href="{APP}">Open the app</a><a class="btn btn--ghost" href="mailto:gabriel@horreum.cloud" data-hz="support">gabriel@horreum.cloud</a></div>
  </div>
</section>

<section class="sec sec--paper">
  <div class="wrap--narrow">
    <h2>For members</h2>
    <div class="faq">
      <details><summary>How do I sign in for the first time?</summary><div class="a"><p>Open the app, tap <b>Set up your account</b>, and enter the email address your venue has on file. We email you a six-digit code; enter it, choose a password, and you are in. Nothing in the invitation email can expire — the code is sent fresh when you ask for it.</p></div></details>
      <details><summary>I forgot my password.</summary><div class="a"><p>Tap <b>Forgot password</b> on the sign-in screen. We send a code to your email; enter it and choose a new password. To change your password while signed in, open your profile, tap <b>Change password</b>, and confirm with a code the same way.</p></div></details>
      <details><summary>How do I get it on my phone?</summary><div class="a"><p>Horreum is an app for iPhone and Android. It also runs in the browser at app.horreum.cloud: on iPhone, open it in Safari, tap <b>Share</b>, then <b>Add to Home Screen</b>. On Android, tap <b>Install app</b> when prompted, or choose it from the browser menu. The app then opens from your home screen like any other and remembers you.</p></div></details>
      <details><summary>How do I have a bottle brought to my table?</summary><div class="a"><p>Open your collection, tap the bottle, and show the code to your server. They scan it and are walked straight to your bottle. If you have several of the same wine, any of them satisfies it.</p></div></details>
      <details><summary>Where do the tasting notes come from?</summary><div class="a"><p>Horreum writes the tasting note for every wine on the platform — the palate first, and the story of the people and the place behind it — so the notes read in one voice wherever you keep your wine.</p></div></details>
      <details><summary>The venue has my name wrong.</summary><div class="a"><p>Open your profile and change the name you go by; that is the name your app shows. Your venue keeps its own record for its ledger.</p></div></details>
      <details><summary>Can I request a bottle?</summary><div class="a"><p>Yes — from the venue’s list in Browse, tap <b>Request</b>. The team confirms it and settles it the usual way, or in the app if your venue has turned on payments.</p></div></details>
    </div>

    <h2 style="margin-top:56px">For venue staff</h2>
    <div class="faq">
      <details><summary>A tag’s code is refused when I add a bottle.</summary><div class="a"><p>Every code is checked before it saves. <i>Already on a bottle</i> means that label is assigned; <i>failed its check digit</i> means a typo; <i>not a registered label</i> means the code was never minted for your venue. Use a tag from one of the batches shipped to your venue.</p></div></details>
      <details><summary>We are running low on labels.</summary><div class="a"><p>Write to us and another batch ships. Codes are registered before they leave and only enter circulation when they are scanned onto a bottle, so a batch that goes missing is simply voided.</p></div></details>
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
    <p>Actions that change records — adding a bottle, logging a pull, approving one, minting labels, reclaiming tags, editing the catalog — run as guarded database functions that check the caller’s role and permissions before doing anything. Hiding a button is a courtesy; the database is the control.</p>

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
    <p>If you believe you have found a security issue, write to <a href="mailto:gabriel@horreum.cloud" data-hz="support">gabriel@horreum.cloud</a> with the subject line <i>Security</i>. We read those first, and we will not pursue anyone who reports a problem in good faith.</p>
  </div>
</section>
'''

# ── PRIVACY ─────────────────────────────────────────────────────────────────
PRIVACY = f'''
<section class="sec">
  <div class="wrap--narrow prose">
    <p class="eyebrow">Legal</p>
    <h1>Privacy policy</h1>
    <p class="meta">Effective {EFFECTIVE} · HORREUM LLC</p>
    <p class="lead">Horreum keeps records of wine kept for members by venues. This policy explains what we keep to do that, why, who can see it, and how to remove it. It is written to be read, and it is the same policy the app shows.</p>
    <p><b>In short:</b> Horreum keeps only what it takes to run your locker and to learn how the app itself is used. Nothing is sold, no advertising network touches it, and the app does not track you across other apps or websites. You can delete your account from inside the app.</p>

    <h2>Who we are</h2>
    <p>Horreum is operated by HORREUM LLC, a Michigan limited liability company (“Horreum”, “we”). The service consists of this website (horreum.cloud) and the Horreum application (app.horreum.cloud), which venues use to manage members’ wine and members use to see it.</p>

    <h2>Two roles</h2>
    <p>For a <b>venue</b> (a restaurant, club or bar that subscribes to Horreum), Horreum processes the venue’s records on the venue’s behalf. For a <b>member</b> (a person whose wine a venue keeps), the venue is the party that decides to keep records about you and what those records say; Horreum stores and displays them for the venue and for you. Questions about why a venue holds particular information about you are best put to the venue; we will help with anything about how it is stored and shown.</p>

    <h2>What the app keeps</h2>
    <ul>
      <li><b>Your account.</b> Your name, email address and phone number, as your venue entered them when it set up your locker and as you edit them in Profile settings; a sign-in password you choose; the one-time codes emailed to you to confirm it's you.</li>
      <li><b>Your locker.</b> The bottles stocked for you and the ones you brought in, when they arrived, when a bottle was pulled and how (at the table or off site), the requests you send the team, and your ratings and notes.</li>
      <li><b>Messages.</b> Conversations between you and the venue's team inside the app.</li>
      <li><b>Keepsake photos.</b> When a bottle comes to your table, the venue's team may offer to take a photo of you with it. Only if you say yes: the photo is taken inside the app with the device's camera (it cannot be saved to the staff member's phone or gallery), held in private storage, checked by a manager, and then shown to you — and only you — on your History page. You can delete it there at any time, and deletion is permanent.</li>
      <li><b>Preferences.</b> Your theme and locker finish, saved to your account so they follow you between devices.</li>
      <li><b>Payments, only where your venue has turned them on.</b> If your venue accepts cards through the app, your card details go directly to Stripe, our payment processor; Horreum never sees the number and keeps only the card's brand, its last four digits and a payment reference for your receipts.</li>
      <li><b>Bug reports.</b> If you report a problem, we keep what you wrote, which screen you were on and the app version, so it can be reproduced.</li>
      <li><b>How the app is used.</b> Which screens and features are opened and how often — for example whether a request began on the atlas or the list, or whether a bottle was rated — together with the app version and the kind of device. It is kept in Horreum's own database, tied to your account only so it can be removed with it, never sold or shared, and never includes what you wrote in a note, a journal entry or a message. We use it to decide what to build and fix.</li>
      <li><b>Technical records.</b> To keep the app reliable we record when a loading screen misbehaves (which page, which version, your device's browser string) and standard server logs.</li>
    </ul>
    <p><b>Location.</b> The app never asks for, reads or stores your location. Its day and night looks follow the clock: sunrise and sunset are estimated from your device's time zone, nothing more precise than that.</p>
    <p><b>Camera.</b> The camera is used by venue staff, in the staff app, for two things: reading bottle labels and tags, where the code is read from the frame on the device and no image is kept; and keepsake photos, described above, which are only ever taken with your agreement.</p>

<h2>Why</h2>
    <p>To run your locker and show it to you; to let the venue stock it, pull bottles for you and answer your requests; to send you the emails you've asked for (codes, invitations and, if you've left them on, notices about your bottles); to issue receipts where the venue takes payment in the app; to find and fix faults; and to see which parts of the app are used, so we know what to improve. That is the whole list. Horreum does not use your information for advertising, does not sell or rent it, and does not build profiles of you for anyone else.</p>

<h2>Who can see it</h2>
    <ul>
      <li><b>Your venue.</b> The team at the venue that holds your locker sees your locker, your requests and your messages — they need them to serve you. Staff with no permission to read messages cannot.</li>
      <li><b>Service providers working for Horreum.</b> Supabase hosts the database, file storage and sign-in; Stripe handles payments for venues that use them; an email service delivers codes and notices. Each processes data only to provide its service to us.</li>
      <li><b>Ordinary web requests.</b> A few things load straight from other services as any web page would, and those services see your device's network address in the process, nothing else: fonts a venue has chosen for its branding (Google Fonts), the label-reading library used in the staff app (jsDelivr), and the weather shown over a wine region in the atlas (Open-Meteo, which is sent the region's coordinates, never yours).</li>
      <li><b>When the law requires it</b>, or to protect the safety of members, venues or the service.</li>
    </ul>
    <p>Nobody else. Your information is not shared with other venues on the platform.</p>

<h2>Your choices</h2>
    <ul>
      <li><b>Edit</b> your name, email, phone and notification preferences any time in Profile settings.</li>
      <li><b>Delete your account</b> from Profile settings → Close account, or follow the steps at <a href="/delete-account">horreum.cloud/delete-account</a>. Your sign-in, personal details, preferences, messages and keepsake photos are removed. Records of past purchases and pulls remain with the venue as its own business records, as the law requires of it; they are no longer tied to a live account.</li>
      <li><b>Remove a keepsake photo</b> from its entry on your History page whenever you like.</li>
      <li><b>Ask us</b> for a copy of what we hold, or to correct or erase it, at <a href="mailto:gabriel@horreum.cloud">gabriel@horreum.cloud</a>.</li>
    </ul>

<h2>How long it's kept</h2>
    <p>For as long as your account is open. After you delete it, personal details are removed promptly; server logs and diagnostic records age out on their own within a year; the venue keeps its purchase records for as long as its books require.</p>

<h2>Security</h2>
    <p>Everything travels encrypted between your device and our servers. Access to the database is controlled row by row, so a member can only ever read their own locker and a venue can only ever read its own members. Photos and attachments live in private storage that is reachable only through short-lived signed links issued to people the rules above allow. Passwords are stored hashed; card numbers are never stored by Horreum at all.</p>

    <h2>This website</h2>
    <p>horreum.cloud sets no cookies and runs no analytics or advertising trackers, and it hosts its own fonts. If you send a form here — a demo request, a pricing question, a support message — we keep what you typed, the page you sent it from and your browser’s user-agent string, so that a person can answer you. Our hosting provider keeps standard server logs (IP address, browser, time) for security and reliability.</p>

    <h2>Where you live</h2>
    <p>Residents of states with privacy laws that grant specific rights (including California) may exercise them by writing to us; we do not sell or share personal information for advertising, so there is nothing to opt out of on that front.</p>

    <h2>Age</h2>
    <p>Horreum is built around wine. It is not directed to anyone under the legal drinking age where they live, venues may only open lockers for adults, and we do not knowingly keep information about anyone younger. If you believe we have, write to us and it will be removed.</p>

    <h2>Changes</h2>
    <p>If this policy changes in a way that matters, the app will say so the next time you open it, and the date at the top will move.</p>

    <h2>Contact</h2>
    <p>HORREUM LLC, Grand Rapids, Michigan · <a href="mailto:gabriel@horreum.cloud" data-hz="support">gabriel@horreum.cloud</a></p>
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
      <li><b>Fees.</b> The Service is billed at the rate in your order form, monthly in advance, plus any applicable taxes.</li>
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
    <p>The Service is provided as it is and as available. We do not promise that it will be uninterrupted or free of error. Tasting notes and the stories behind the wines are editorial guidance, not a warranty about any bottle. Horreum is not responsible for the condition, storage, loss or service of any bottle, which is between the Venue and the Member.</p>

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
    <p>HORREUM LLC, Grand Rapids, Michigan · <a href="mailto:gabriel@horreum.cloud" data-hz="email">gabriel@horreum.cloud</a></p>
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

# ── DELETE ACCOUNT (the URL both stores ask for) ────────────────────────────
DELETE = '''

<section class="sec">
  <div class="wrap--narrow">
    <p class="eyebrow">Your account</p>
    <h1 style="font-size:clamp(44px,6vw,80px)">Delete <em>your account.</em></h1>
    <p class="lead">Two ways to close your <b>Horreum</b> account and remove the information attached to it. Either one works, and neither needs you to speak to your venue first.</p>
    <div class="cta-row"><a class="btn btn--gold" href="https://app.horreum.cloud">Open the app</a><a class="btn btn--ghost" href="mailto:gabriel@horreum.cloud?subject=Delete%20my%20account" data-hz="support">gabriel@horreum.cloud</a></div>
  </div>
</section>

<section class="sec sec--paper">
  <div class="wrap--narrow">
    <h2>How to do it</h2>
    <div class="faq">
      <details open><summary>In the app</summary><div class="a"><p>Open Horreum, go to <b>Profile settings</b>, and choose <b>Close account</b>. You will be asked to type DELETE, enter your password and confirm a one-time code we email you; then your account closes straight away.</p></div></details>
      <details><summary>By email</summary><div class="a"><p>Write to <a href="mailto:gabriel@horreum.cloud?subject=Delete%20my%20account" data-hz="support">gabriel@horreum.cloud</a> from the address on your account and ask us to close it. We answer within a few days and confirm when it is done.</p></div></details>
      <details><summary>Removing something without closing your account</summary><div class="a"><p>You can ask us to erase particular information and keep your account open &mdash; a journal entry, a photo, a message thread. Write to the same address and say what you would like removed.</p></div></details>
    </div>

    <h2 style="margin-top:56px">What is deleted</h2>
    <ul>
      <li>Your sign-in and the credentials behind it.</li>
      <li>Your name, email, phone and notification preferences.</li>
      <li>Your journal entries, ratings and request notes.</li>
      <li>Photos you added to a pull.</li>
      <li>Your messages with the venue.</li>
    </ul>

    <h2 style="margin-top:56px">What your venue keeps, and why</h2>
    <p>Records of past purchases and pulls stay with your venue as its own business records, because the law requires a business to keep them. They are no longer tied to a live account and no longer identify you within Horreum.</p>

    <h2 style="margin-top:56px">How long it takes</h2>
    <p>Personal details are removed promptly &mdash; immediately when you close the account in the app, and within thirty days of an emailed request. Server logs and diagnostic records age out on their own within a year. Your venue keeps its purchase records for as long as its books require.</p>

    <p style="margin-top:32px">The full picture of what Horreum holds and why is in the <a href="/privacy">privacy policy</a>.</p>
  </div>
</section>

'''
DELETE_META = ('Delete your Horreum account', 'How to delete your Horreum account and the data attached to it, what is removed, what your venue keeps, and how long it takes.')
