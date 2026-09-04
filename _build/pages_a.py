# Home, Venues, Members, Pricing
from icons import ICON
from shell import APP, VINE

def card(icon, title, text):
    return f'<div class="card"><span class="ico">{ICON[icon]}</span><h3>{title}</h3><p>{text}</p></div>'

def phone(src, alt, small=False):
    return f'<div class="phone{" phone--sm" if small else ""}"><img src="{src}" alt="{alt}" loading="lazy"></div>'

# ── HOME ────────────────────────────────────────────────────────────────────
HOME = f'''
<section class="hero">
  <div class="wrap">
    <div>
      <p class="eyebrow">Wine reserve &amp; locker management</p>
      <h1>Every bottle, accounted for.</h1>
      <p class="lead">Horreum runs a venue’s wine locker program end to end — the ledger, the labels, the pulls — and gives every member a collection worth showing off. Built on the floor of a fine-dining chophouse, where it runs today.</p>
      <div class="cta-row">
        <a class="btn btn--gold btn--lg" href="/contact?kind=demo">Request a demo</a>
        <a class="btn btn--ghost btn--lg" href="#how">See how it works</a>
      </div>
      <p class="hero-note">No hardware to buy · Runs on the phones your staff already carry · Members set up in a minute</p>
    </div>
    {phone("/assets/shots/collection.jpg", "A member’s collection in the Horreum app: bottles with tasting notes, drink windows and serving guidance")}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="wrap--narrow center" style="margin-bottom:44px">
      <p class="eyebrow">The problem</p>
      <h2>A locker program runs on trust. Trust runs on records.</h2>
      <p class="lead">Members leave bottles worth real money in your care. The program only works while everyone’s records agree — and a spreadsheet, a binder and someone’s memory rarely do.</p>
    </div>
    <div class="grid grid--3">
      {card("ledger", "Conflicting records", "Two lists, one bottle, and a member who remembers it differently. Every disagreement is a conversation you would rather not have.")}
      {card("log", "No chain of custody", "Who stocked it, who pulled it, when, and for whom. Without an append-only log, nobody can answer with certainty — and certainty is the product.")}
      {card("find", "The search during service", "A guest asks for their bottle at 7:45 on a Saturday. The server goes looking. The table waits, and the wrong bottle is one guess away.")}
    </div>
  </div>
</section>

<section class="sec sec--paper" id="how">
  <div class="wrap">
    <div class="wrap--narrow center" style="margin-bottom:44px">
      <p class="eyebrow">How it works</p>
      <h2>Label. Stock. Serve.</h2>
    </div>
    <div class="steps">
      <div class="step"><div class="num">I</div><h3>Label</h3><p>Print a batch of QR labels on standard 30-up Avery sheets. Every code is registered before it is ever used, so a label cannot be forged, duplicated, or orphaned by a misprint — and a tag comes back into circulation when its bottle leaves.</p></div>
      <div class="step"><div class="num">II</div><h3>Stock</h3><p>Adding a bottle to a locker is a scan and a tap: the wine, its label, and where it physically sits. The member’s collection updates that moment, and the activity log records who did it and when.</p></div>
      <div class="step"><div class="num">III</div><h3>Serve</h3><p>At the table, the member shows a code from their collection. The server scans it, is walked to the exact bottle and its storage spot, confirms it with a second scan, and logs the pull. The member gets a note — and a chance to rate the bottle.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="wrap--narrow center" style="margin-bottom:44px">
      <p class="eyebrow">For venues</p>
      <h2>The program you would be proud to explain.</h2>
      <p class="lead">Everything the floor, the bar and the office need, in one record that never disagrees with itself.</p>
    </div>
    <div class="grid grid--4">
      {card("ledger", "The ledger", "Every member, every locker, every bottle — house-purchased or brought in — with its vintage, where it sits, and its full history.")}
      {card("label", "Labels that last", "Codes minted in durable batches: reprint an identical sheet any time, void a batch that never printed, reclaim a tag when a bottle leaves.")}
      {card("spot", "Storage spots", "A locker is where a bottle belongs; the bar cooler is where it might sit tonight. Name your spots per location and every bottle knows both.")}
      {card("find", "Find my bottle", "The member shows a code; the server is walked to the exact bottle. A wrong bottle is refused before it ever leaves the cooler.")}
      {card("roles", "Roles and approvals", "Servers submit pulls; managers approve. Each account carries exactly the permissions you give it — enforced by the database, not the screen.")}
      {card("log", "Activity, append-only", "A full chain of custody: every add, pull, request and change, with who and when. Filter by day, week, month, or your own range.")}
      {card("notes", "Catalog and tasting notes", "Your list, per location, with prices and vintages. Horreum writes the tasting note for every wine — long-form, guest-ready, one voice.")}
      {card("brand", "Your brand, your locations", "White-label from the first screen: your logo, your themes, your locker finishes. Add locations as you grow; each keeps its own catalog, staff and records.")}
    </div>
    <div class="center" style="margin-top:36px"><a class="btn btn--ghost" href="/venues">Everything for venues</a></div>
  </div>
</section>

<section class="sec sec--night">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">For members</p>
        <h2>A collection worth showing off.</h2>
        <p class="lead">Members don’t get a spreadsheet. They get their cellar — with the story of every bottle in it.</p>
        <ul>
          <li><b>The Collection.</b> Every bottle with its tasting note, drink window and serving guidance, drawn as a cellar sheet they can print or share.</li>
          <li><b>The Atlas.</b> An interactive globe of the world’s wine regions, with the member’s own bottles pinned to where they were made.</li>
          <li><b>History and ratings.</b> What they have enjoyed, what they thought of it, and what came into the locker and how.</li>
          <li><b>Show your server.</b> One tap on a bottle shows the code that brings it to the table.</li>
          <li><b>Requests and messages.</b> Ask for a bottle from the list, or a word with the team, without picking up the phone.</li>
          <li><b>An app, not a website.</b> Installs on iPhone and Android in a minute; classic by day, midnight after dark.</li>
        </ul>
        <div class="cta-row" style="margin-top:26px"><a class="btn btn--ghost" href="/members">Everything for members</a></div>
      </div>
      {phone("/assets/shots/find.jpg", "The Show-your-server sheet: a large code the member shows their server to have a bottle brought out")}
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="wrap--narrow center" style="margin-bottom:44px">
      <p class="eyebrow">Screens</p>
      <h2>What the member sees. What the floor sees.</h2>
    </div>
    <div class="phones">
      <figure style="margin:0">{phone("/assets/shots/collection.jpg", "The Collection", True)}<figcaption>The Collection<span>The member’s cellar sheet</span></figcaption></figure>
      <figure style="margin:0">{phone("/assets/shots/history.jpg", "History", True)}<figcaption>History<span>Enjoyed, rated, added</span></figcaption></figure>
      <figure style="margin:0">{phone("/assets/shots/find.jpg", "Show your server", True)}<figcaption>Show your server<span>The code that fetches a bottle</span></figcaption></figure>
      <figure style="margin:0">{phone("/assets/shots/hunt.jpg", "Find a bottle (staff)", True)}<figcaption>Find a bottle<span>What the server sees after the scan</span></figcaption></figure>
    </div>
  </div>
</section>

<section class="sec sec--paper">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">Pricing</p>
        <h2>One subscription per location. Everything included.</h2>
        <p class="lead">Members, lockers, staff accounts, labels, the member app and Horreum’s tasting notes, in one monthly subscription per location. No per-member fees, no per-seat fees, no hardware. Ask, and you’ll have a number the same day.</p>
        <div class="cta-row"><a class="btn btn--gold" href="/contact?kind=pricing">Ask about pricing</a><a class="btn btn--ghost" href="/pricing">What’s included</a></div>
      </div>
      <div class="grid grid--2" style="gap:18px">
        <div class="stat"><b>0</b><span>Per-member fees</span></div>
        <div class="stat"><b>1</b><span>Record of truth</span></div>
        <div class="stat"><b>30</b><span>Labels per sheet</span></div>
        <div class="stat"><b>2</b><span>Themes, day and night</span></div>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="split split--rev">
      <div class="card" style="padding:32px">
        <span class="ico">{ICON["shield"]}</span>
        <h3>Built to be trusted with other people’s wine.</h3>
        <p>Each venue’s data is isolated by row-level security in Postgres. Staff permissions are enforced by the database itself. Card payments, when a venue turns them on, are handled by Stripe and never pass through Horreum. The activity log is append-only.</p>
        <p style="margin-top:14px"><a href="/security">How Horreum handles data →</a></p>
      </div>
      <div>
        <p class="eyebrow">Trust</p>
        <h2>Records that can be relied on.</h2>
        <p class="lead">A locker program is a promise to members. The software that runs it should be at least as careful as the people who make that promise.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec sec--night center">
  <div class="wrap--narrow">
    {VINE.replace('#7C5A36', '#E8CB84')}
    <h2>See it on your floor.</h2>
    <p class="lead">A thirty-minute walkthrough with the person who built it. Bring your binder.</p>
    <div class="cta-row" style="justify-content:center;margin-top:8px"><a class="btn btn--gold btn--lg" href="/contact?kind=demo">Request a demo</a><a class="btn btn--ghost btn--lg" href="mailto:hello@horreum.cloud" data-hz="email">hello@horreum.cloud</a></div>
  </div>
</section>
'''

# ── VENUES ──────────────────────────────────────────────────────────────────
VENUES = f'''
<section class="hero">
  <div class="wrap">
    <div>
      <p class="eyebrow">For venues</p>
      <h1>Run the program you would be proud to explain.</h1>
      <p class="lead">Restaurants, clubs and wine bars keep members’ bottles for the same reason: it brings them back. Horreum makes the keeping precise — and turns the program into something members talk about.</p>
      <div class="cta-row"><a class="btn btn--gold btn--lg" href="/contact?kind=demo">Request a demo</a><a class="btn btn--ghost btn--lg" href="/pricing">Pricing</a></div>
    </div>
    {phone("/assets/shots/hunt.jpg", "The staff Find-a-bottle screen: the wine, whose locker, each bottle’s storage spot and label, and a live scanner")}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">The ledger</p>
        <h2>One record. Everyone works from it.</h2>
        <p>Every member has a locker; every locker has its bottles; every bottle has a label, a home, and a history. House-purchased bottles come from your catalog. Bottles a member brings in are recorded as their own, with whatever details you have. Nothing is a duplicate of anything, and nothing lives in someone’s head.</p>
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
        <p>Codes are minted by the platform in batches of thirty — one 30-up Avery sheet — and registered before they are printed. A code is unassigned until it is scanned onto a bottle, assigned while the bottle is in the locker, and pending return once the bottle is pulled, so a tag can be reclaimed and used again. The stocking screen checks each code before it saves: a taken, voided or foreign label is refused there, never mid-save.</p>
        <ul>
          <li>Reprint an identical sheet any time; void a batch that never made it out of the printer.</li>
          <li>A check digit in every code catches a mistyped label before it can be saved to the wrong bottle.</li>
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
      <h2>Find my bottle.</h2>
      <p class="lead">A member taps a bottle in their collection and shows the server a code. The server scans it — in the app, or with the phone’s own camera — and this opens.</p>
    </div>
    <div class="split">
      {phone("/assets/shots/hunt.jpg", "The Find-a-bottle screen")}
      <div>
        <ul>
          <li><b>The wine, whose locker,</b> and one row per bottle with where it sits and which label it wears.</li>
          <li><b>A live scanner.</b> Scan a label: <i>This is it</i>, or <i>Not this one — that’s a different member’s Sancerre</i>. A wrong bottle never leaves the cooler.</li>
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
      {card("roles", "Roles and approvals", "Directors, managers, servers and bartenders — each account carries its own permissions: add bottles, log pulls, approve pulls, manage the catalog, print labels, reclaim tags. Floor staff submit; managers approve. The database enforces every one of them.")}
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
        <h2>Members are imported. Bottles are scanned in.</h2>
        <p class="lead">Your member and locker records — the spreadsheet, the binder, the PDF from the last count — are imported for you. The bottles themselves are not: every one is labelled and scanned into its locker by hand, wine by wine. That is the work, and it is the point — from that moment the record is exact, and it stays that way.</p>
        <ul>
          <li>Members and lockers imported and reconciled before you start.</li>
          <li>Your first label batches printed and registered with you; wines not yet in your catalog are entered as they come up.</li>
          <li>Plan for the scan-in: a couple of minutes a bottle, more when a wine is new to the catalog. A program of several hundred bottles is a few afternoons for two people.</li>
          <li>Staff accounts created with the right roles; members invited when you say so.</li>
          <li>What you need: a printer, 30-up Avery label sheets, and the phones your team already carries.</li>
        </ul>
      </div>
      <div class="price-card price-card--night">
        <p class="eyebrow">Per location</p>
        <h3 style="font-size:28px;margin:6px 0 4px">One subscription</h3>
        <div class="per">per month · everything included</div>
        <ul>
          <li>Unlimited members, lockers and bottles</li>
          <li>Unlimited staff accounts and roles</li>
          <li>Label batches, reprints and reclaims</li>
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
      <h1>Your cellar, in your pocket.</h1>
      <p class="lead">If your venue keeps your bottles, Horreum is how you see them: every bottle with its story, the map of where they came from, and one tap to have one brought to your table.</p>
      <div class="cta-row"><a class="btn btn--gold btn--lg" href="{APP}">Sign in</a><a class="btn btn--ghost btn--lg" href="/support">Help getting started</a></div>
    </div>
    {phone("/assets/shots/collection.jpg", "The Collection: a member’s bottles with tasting notes, drink windows and serving guidance")}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="grid grid--3">
      {card("bottle", "The Collection", "Every bottle in your locker, drawn as a cellar sheet: the tasting note, the drink window and whether it is at its peak, and how to serve it — temperature and decanting, worked out for that bottle. Print it or share it.")}
      {card("globe", "The Atlas", "An interactive globe of the world’s wine regions. Your own bottles are pinned to where they were made; tap a region to see what grows there and how far it is from your table.")}
      {card("history", "History", "What you have enjoyed and when, what came into your locker and how, and any requests you have made — with the receipt on any bottle you bought in the app.")}
      {card("star", "Ratings", "Rate a bottle after you enjoy it. Your reviews live with your history, and the bottles waiting for a word from you sit at the top of the page.")}
      {card("find", "Show your server", "Tap a bottle in your collection and a code appears. Your server scans it and is walked straight to your bottle — no searching, no guessing.")}
      {card("chat", "Requests and messages", "Ask for a bottle from your venue’s list, or send the team a note. Announcements from the venue arrive in the app.")}
    </div>
  </div>
</section>

<section class="sec sec--night">
  <div class="wrap">
    <div class="split split--rev">
      {phone("/assets/shots/history.jpg", "History: bottles enjoyed, waiting for a review, and added to the locker")}
      <div>
        <p class="eyebrow">Getting started</p>
        <h2>Three steps, one minute.</h2>
        <ul>
          <li><b>Your venue invites you.</b> An email arrives with a link to set up your account.</li>
          <li><b>Confirm it is you.</b> Enter your email and the six-digit code we send it; then choose a password.</li>
          <li><b>Install it.</b> On iPhone, tap Share then <i>Add to Home Screen</i>; on Android, tap <i>Install app</i>. It opens like any other app, and it remembers you.</li>
        </ul>
        <p class="small" style="margin-top:18px">Two themes — classic by day, midnight after dark — or let it follow the sun where you are.</p>
        <div class="cta-row" style="margin-top:22px"><a class="btn btn--gold" href="{APP}">Open the app</a><a class="btn btn--ghost" href="/support">Support</a></div>
      </div>
    </div>
  </div>
</section>

<section class="sec center">
  <div class="wrap--narrow">
    <p class="eyebrow">Not a member yet?</p>
    <h2>Ask your venue about lockers.</h2>
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
      <h1 style="font-size:clamp(36px,5vw,54px)">One subscription per location.<br>Everything included.</h1>
      <p class="lead">No per-member fees, no per-seat fees, no hardware. The price depends on the size of your program — how many lockers you keep and at how many locations — so ask, and you’ll have a number the same day.</p>
      <div class="cta-row" style="justify-content:center"><a class="btn btn--gold btn--lg" href="/contact?kind=pricing">Ask about pricing</a><a class="btn btn--ghost btn--lg" href="/contact?kind=demo">Request a demo</a></div>
    </div>
    <div class="split" style="align-items:start">
      <div class="price-card">
        <p class="eyebrow">Per location</p>
        <h3 style="font-size:28px;margin:6px 0 4px">What the subscription covers</h3>
        <div class="per">billed monthly · everything below</div>
        <ul>
          <li>Unlimited members, lockers and bottles</li>
          <li>Unlimited staff accounts, with roles and approvals</li>
          <li>QR label batches — print, reprint, void, reclaim</li>
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
        <h3>Groups and multi-location</h3>
        <p>Each location is its own record — catalog, storage spots, staff, members — under one account with shared branding. Groups should <a href="/contact?kind=pricing">talk to us</a> about a group rate.</p>
        <h3 style="margin-top:28px">What is not included</h3>
        <ul class="small" style="padding-left:20px;color:var(--text-dim)">
          <li>Label sheets and a printer. Any printer; standard 30-up Avery sheets.</li>
          <li>The scan-in. Your bottles are labelled and scanned into their lockers by your team, wine by wine. We walk the first batch with you and import your member and locker records; the bottles are the part only your hands can do.</li>
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
    <h2>Pricing, plainly.</h2>
    <div class="faq">
      <details><summary>Why isn’t the price on the page?</summary><div class="a"><p>Because it depends on the program. A single restaurant with fifty lockers and a group with four locations are different jobs, and one number would be wrong for one of them. Ask and you will have yours the same day — no sales call required unless you want one.</p></div></details>
      <details><summary>Is there a contract?</summary><div class="a"><p>Service is billed monthly per active location. The notice period and any term are set in your order form, and there is no fee to leave: your records are yours and are exported on request.</p></div></details>
      <details><summary>What does getting started involve?</summary><div class="a"><p>We import your member and locker records from whatever you keep them in today. Then your team labels and scans the bottles into their lockers — a couple of minutes a bottle, more when a wine is new to your catalog. We print and register your first label batches with you and walk the first stocking. There is no setup fee.</p></div></details>
      <details><summary>What counts as a location?</summary><div class="a"><p>One address where members’ bottles are kept. A restaurant with a bar cooler, a walk-in and a cellar is one location with three storage spots.</p></div></details>
      <details><summary>Do members pay anything?</summary><div class="a"><p>Not to Horreum. The member app is included in your subscription. What you charge members for the locker itself is between you and them.</p></div></details>
      <details><summary>What happens to our data if we stop?</summary><div class="a"><p>You receive a complete export — members, lockers, bottles, and the activity log — and your venue’s data is removed from the platform on the schedule set out in the <a href="/terms">terms</a>.</p></div></details>
      <details><summary>Can we run it on the phones we already have?</summary><div class="a"><p>Yes. The staff app runs in the browser on any recent iPhone or Android phone and installs to the home screen; scanning uses the phone’s camera. There is no hardware to buy.</p></div></details>
    </div>
  </div>
</section>
'''
