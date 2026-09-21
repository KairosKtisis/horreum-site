# Venues, Members, Pricing (Home lives in home.py)
from icons import ICON
from shell import APP, VINE, ARR
from home import HOME, card, phone, shot

# ── VENUES ──────────────────────────────────────────────────────────────────
VENUES = f'''
<section class="hero">
  <div class="wrap">
    <div>
      <p class="eyebrow">For venues</p>
      <h1>Run the program you would be <em>proud to explain.</em></h1>
      <p class="lead">Restaurants, clubs and wine bars keep members’ bottles for the same reason: it brings them back. Horreum makes the keeping precise — and turns the program into something members talk about.</p>
      <div class="cta-row"><a class="btn btn--gold btn--lg" href="/contact?kind=demo">Request a demo</a><a class="btn btn--ghost btn--lg" href="/pricing">Pricing</a></div>
    </div>
    {phone("overview", "The venue overview: inventory value, bottles and lockers in the program, open requests", eager=True)}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">The ledger</p>
        <h2>One record. Everyone works from it.</h2>
        <p>Every member has a locker; every locker has its bottles; every bottle has a tag, a home, and a history. House-purchased bottles come from your catalog. Bottles a member brings in are recorded as their own, with whatever details you have. Nothing is a duplicate of anything, and nothing lives in someone’s head.</p>
        <ul>
          <li>Members and lockers per location, with contact details and a since date.</li>
          <li>Bottles grouped by wine, one line per physical bottle underneath.</li>
          <li>Storage spots: a bottle belongs to a locker and may sit in the bar cooler, the walk-in, or the cellar. Both are known.</li>
          <li>Alphabetical everywhere a list is drawn, so the eye lands where it expects to.</li>
        </ul>
      </div>
      <div>
        <p class="eyebrow">Labels</p>
        <h2>A label lifecycle that wastes nothing.</h2>
        <p>Codes are minted by the platform in batches and registered before the labels are made; Horreum ships them to your venue ready to use, so there is nothing to print. A code is unassigned until it is scanned onto a bottle, assigned while the bottle is in the locker, and pending return once the bottle is pulled, so a tag can be reclaimed and used again. The stocking screen checks each code before it saves: a taken, voided or foreign label is refused there, never mid-save.</p>
        <ul>
          <li>Ask for another batch when you run low; void a batch that goes missing.</li>
          <li>A check digit in every code catches a mistyped tag before it can be saved to the wrong bottle.</li>
          <li>Reclaiming tags is a permission you grant, like adding bottles.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="sec sec--paper">
  <div class="wrap">
    <div class="wrap--narrow center" style="margin-bottom:44px">
      <p class="eyebrow">Service</p>
      <h2>Find <em>my bottle.</em></h2>
      <p class="lead">A member taps a bottle in their collection and shows the server a code. The server scans it — in the app, or with the phone’s own camera — and this opens.</p>
    </div>
    <div class="split">
      {phone("hunt", "The Find-a-bottle screen: the wine, whose locker, each bottle’s storage spot and tag, and a live scanner")}
      <div>
        <ul>
          <li><b>The wine, whose locker,</b> and one row per bottle with where it sits and which tag it wears.</li>
          <li><b>A live scanner.</b> Scan a bottle’s tag: <i>This is it</i>, or <i>Not this one — that’s a different member’s Sancerre</i>. A wrong bottle never leaves the cooler.</li>
          <li><b>A bottle-exact pull.</b> The label that leaves is the label the system releases. Servers without approval rights submit the pull; a manager approves that exact bottle.</li>
          <li><b>Several of the same bottle?</b> Any of them satisfies the hunt. The code belongs to the wine in that locker, not to one bottle.</li>
          <li><b>It persists.</b> The screen stays until you close it; scanning a second member’s code simply replaces it.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="grid grid--3">
      {card("roles", "Roles and approvals", "Directors, managers, servers and bartenders — each account carries its own permissions: add bottles, log pulls, approve pulls, manage the catalog, manage labels, reclaim tags. Floor staff submit; managers approve. The database enforces every one of them.")}
      {card("log", "Activity, append-only", "Every add, pull, request, catalog change and staff edit, with the actor and the moment. Filter by today, this week, last month or your own range, and by kind. Nothing is edited after the fact; corrections are new entries.")}
      {card("notes", "Catalog and tasting notes", "Your list per location with vintages, varietals, regions and locker prices; search and filter it like a member would. Horreum writes the tasting note for every wine — long-form and guest-ready, in one voice across the platform — so the floor can recommend with confidence.")}
      {card("chat", "Members, invited properly", "Add a member, send the invitation, and they set up their account with a code from their email — no expiring links, no passwords in transit. Announcements go to everyone; conversations are one to one.")}
      {card("card", "Payments, if you want them", "Members can request bottles from your list. Turn on payments and they can pay in the app through your own Stripe account, with a receipt on the bottle. Or keep invoicing the way you already do.")}
      {card("brand", "Your brand, your locations", "Your logo and your themes on the member’s phone; your locker finishes in the app’s locker. Add locations as you grow — each keeps its own catalog, storage spots, staff and records, under one account.")}
    </div>
  </div>
</section>

<section class="sec sec--night">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">Getting set up</p>
        <h2>Members are imported. <em>Bottles are scanned in.</em></h2>
        <p class="lead">Your member and locker records — the spreadsheet, the binder, the PDF from the last count — are imported for you. The bottles themselves are not: every one is tagged and scanned into its locker by hand, wine by wine — the tag is scanned, then the wine is picked from your catalog or entered if it is new. That is the work, and it is the point — from that moment the record is exact, and it stays that way.</p>
        <ul>
          <li>Members and lockers imported and reconciled before you start.</li>
          <li>Your first label batches arrive registered to your venue; wines not yet in your catalog have their basics entered as they come up.</li>
          <li>Plan for the scan-in: a couple of minutes a bottle, more when a wine is new to the catalog. A program of several hundred bottles is a few afternoons for two people.</li>
          <li>Staff accounts created with the right roles; members invited when you say so.</li>
          <li>What you need: the phones your team already carries. The labels come from us.</li>
        </ul>
      </div>
      <div class="price-card price-card--night">
        <p class="eyebrow">Pricing</p>
        <h3 style="font-size:28px;margin:6px 0 4px">Priced to your program</h3>
        <div class="per">no per-seat fees · no per-member fees · no hardware</div>
        <ul>
          <li>Unlimited members, lockers and bottles</li>
          <li>Unlimited staff accounts and roles</li>
          <li>QR labels, shipped to your venue</li>
          <li>The member app, white-labelled</li>
          <li>Tasting notes written by Horreum</li>
          <li>Import of your member and locker records</li>
        </ul>
        <a class="btn btn--gold btn--block" href="/contact?kind=pricing">Ask about pricing</a>
      </div>
    </div>
  </div>
</section>
'''

# ── MEMBERS ─────────────────────────────────────────────────────────────────
MEMBERS = f'''
<section class="hero">
  <div class="wrap">
    <div>
      <p class="eyebrow">For members</p>
      <h1>Your cellar, <em>in your pocket.</em></h1>
      <p class="lead">If your venue keeps your bottles, Horreum is how you see them: every bottle with its story, the map of where they came from, and one tap to have one brought to your table.</p>
      <div class="cta-row"><a class="btn btn--gold btn--lg" href="{APP}">Sign in</a><a class="btn btn--ghost btn--lg" href="/support">Help getting started</a></div>
    </div>
    {phone("locker", "A member’s locker in the Horreum app: their bottles standing in a wooden cabinet", eager=True)}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="grid grid--3">
      {card("bottle", "The Collection", "Every bottle in your locker, drawn as a cellar sheet: Horreum’s tasting note up front, and the story of the people and the place one tap behind it. Print it or share it.")}
      {card("globe", "The Atlas", "An interactive globe of the world’s wine regions. Your own bottles are pinned to where they were made; tap a region to see what grows there and how far it is from your table.")}
      {card("history", "History", "What you have enjoyed and when, what came into your locker and how, and any requests you have made. Keep a line about the evening a bottle was opened, and a keepsake photo if your venue took one.")}
      {card("star", "Ratings", "Rate a bottle the moment you have enjoyed it — one tap on the stars, right in your history — and add a few words if you like. Your reviews live with the bottles they belong to.")}
      {card("find", "Show your server", "Tap a bottle in your collection and a code appears. Your server scans it and is walked straight to your bottle — no searching, no guessing.")}
      {card("chat", "Requests and messages", "Ask for a bottle from your venue’s list, or send the team a note. Announcements from the venue arrive in the app.")}
    </div>
  </div>
</section>

<section class="sec sec--night">
  <div class="wrap">
    <div class="split split--rev">
      {phone("history", "History: bottles enjoyed and rated, and bottles added to the locker")}
      <div>
        <p class="eyebrow">Getting started</p>
        <h2>Three steps, <em>one minute.</em></h2>
        <ul>
          <li><b>Your venue invites you.</b> An email arrives with a link to set up your account.</li>
          <li><b>Confirm it is you.</b> Enter your email and the six-digit code we send it; then choose a password.</li>
          <li><b>Put it on your phone.</b> Horreum is an app for iPhone and Android. It also runs in the browser: on iPhone, tap Share then <i>Add to Home Screen</i>; on Android, tap <i>Install app</i>.</li>
        </ul>
        <p class="small" style="margin-top:18px">Two themes — classic by day, midnight after dark — or let it follow the clock.</p>
        <div class="cta-row" style="margin-top:22px"><a class="btn btn--gold" href="{APP}">Open the app</a><a class="btn btn--ghost" href="/support">Support</a></div>
      </div>
    </div>
  </div>
</section>

<section class="sec day">
  <div class="wrap">
    <div class="wrap--narrow center" style="margin-bottom:56px">
      <p class="eyebrow">Inside the app</p>
      <h2>Four rooms, <em>one key.</em></h2>
    </div>
    <div class="phones">
      <figure>{phone("locker", "The Locker", small=True)}<figcaption>The Locker<span>The bottles held in your name</span></figcaption></figure>
      <figure>{phone("atlas", "The Atlas", small=True)}<figcaption>The Atlas<span>The cellar, region by region</span></figcaption></figure>
      <figure>{phone("bottle", "A wine’s card", small=True)}<figcaption>Browse<span>Every bottle, with its story</span></figcaption></figure>
      <figure>{phone("collection", "The Collection", small=True)}<figcaption>The Collection<span>Ready to print or share</span></figcaption></figure>
    </div>
  </div>
</section>

<section class="sec center">
  <div class="wrap--narrow">
    <p class="eyebrow">Not a member yet?</p>
    <h2>Ask your venue <em>about lockers.</em></h2>
    <p class="lead">Horreum is offered by the venues that keep members’ wine. If yours does not yet, we would be glad to talk to them.</p>
    <div class="cta-row" style="justify-content:center"><a class="btn btn--ghost" href="/contact">Introduce us</a></div>
  </div>
</section>
'''

# ── PRICING ─────────────────────────────────────────────────────────────────
PRICING = f'''
<section class="sec">
  <div class="wrap">
    <div class="wrap--narrow center" style="margin-bottom:44px">
      <p class="eyebrow">Pricing</p>
      <h1 style="font-size:clamp(44px,6.4vw,84px)">Priced according<br>to <em>your needs.</em></h1>
      <p class="lead">Every locker program is a different size, so the price follows yours. Tell us about it — how many lockers, how many locations — and you’ll have a number the same day. No per-seat fees, no per-member fees, no hardware to buy.</p>
      <div class="cta-row" style="justify-content:center"><a class="btn btn--gold btn--lg" href="/contact?kind=pricing">Ask about pricing</a><a class="btn btn--ghost btn--lg" href="/contact?kind=demo">Request a demo</a></div>
    </div>
    <div class="split" style="align-items:start">
      <div class="price-card">
        <p class="eyebrow">Included</p>
        <h3 style="font-size:28px;margin:6px 0 4px">What every venue gets</h3>
        <div class="per">one plan · no add-ons · no tiers</div>
        <ul>
          <li>Unlimited members, lockers and bottles</li>
          <li>Unlimited staff accounts, with roles and approvals</li>
          <li>QR labels, shipped to your venue</li>
          <li>Storage spots, find-my-bottle, bottle-exact pulls</li>
          <li>The member app, white-labelled with your brand</li>
          <li>Tasting notes written by Horreum for every wine</li>
          <li>Announcements, requests and member messaging</li>
          <li>Import of your member and locker records</li>
          <li>Support from the people who built it</li>
        </ul>
        <a class="btn btn--gold btn--block" href="/contact?kind=pricing">Ask about pricing</a>
      </div>
      <div>
        <h3>Never charged for</h3>
        <ul class="small" style="padding-left:20px;color:var(--text-dim)">
          <li>Seats. Every server, bartender and manager gets an account.</li>
          <li>Members. Invite all of them.</li>
          <li>Hardware. It runs on the phones your team already carries; scanning uses the camera.</li>
          <li>Updates. Every venue runs the latest Horreum.</li>
        </ul>
        <h3 style="margin-top:28px">More than one location?</h3>
        <p>Each location keeps its own catalog, storage spots, staff and members under one account with shared branding. <a href="/contact?kind=pricing">Tell us about the group</a> and it is priced as a whole.</p>
        <h3 style="margin-top:28px">What is not included</h3>
        <ul class="small" style="padding-left:20px;color:var(--text-dim)">
          <li>The scan-in. Your bottles are tagged and scanned into their lockers by your team, wine by wine. We walk the first batch with you and import your member and locker records; the bottles are the part only your hands can do.</li>
          <li>Card-processing fees, if you turn on in-app payments. Payments run through your own Stripe account at Stripe’s standard rates; Horreum adds nothing on top.</li>
          <li>Custom development. If your program needs something Horreum does not do, ask — the roadmap is written by venues.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="sec sec--paper">
  <div class="wrap--narrow">
    <p class="eyebrow">Questions</p>
    <h2>Pricing, <em>plainly.</em></h2>
    <div class="faq">
      <details><summary>Why isn’t the price on the page?</summary><div class="a"><p>Because it depends on the program. A single restaurant with fifty lockers and a group with four locations are different jobs, and one number would be wrong for one of them. Ask and you will have yours the same day — no sales call required unless you want one.</p></div></details>
      <details><summary>What does getting started involve?</summary><div class="a"><p>We import your member and locker records from whatever you keep them in today. Your first label batches arrive registered to your venue, and we walk the first stocking with you. Then your team tags and scans the bottles into their lockers — scan the tag, pick the wine or enter it if it is new — a couple of minutes a bottle, more when a wine needs its basics entered.</p></div></details>
      <details><summary>Do members pay anything?</summary><div class="a"><p>Not to Horreum. The member app is included in your subscription. What you charge members for the locker itself is between you and them.</p></div></details>
      <details><summary>What happens to our data if we stop?</summary><div class="a"><p>You receive a complete export — members, lockers, bottles, and the activity log — and your venue’s data is removed from the platform on the schedule set out in the <a href="/terms">terms</a>.</p></div></details>
      <details><summary>Can we run it on the phones we already have?</summary><div class="a"><p>Yes. The staff app runs in the browser on any recent iPhone or Android phone and installs to the home screen; scanning uses the phone’s camera. There is no hardware to buy.</p></div></details>
    </div>
  </div>
</section>
'''
