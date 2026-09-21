# Home (v3, quiet). One theme, one background; space and hairlines do the structure.
from icons import ICON
from shell import APP, ARR

def card(icon, title, text, cls="", tag=""):
    return f'<div class="card {cls}"><span class="ico">{ICON[icon]}</span><h3>{title}</h3><p>{text}</p></div>'

# every screen is the phone's own 390:844 — the frame in site.css is drawn for exactly that shape
DIMS = {"find": ("jpg", 390, 844), "locker": ("webp", 924, 2000), "hunt": ("webp", 924, 2000),
        "a-overview": ("webp", 720, 1604), "a-scan": ("webp", 720, 1604), "a-lockers": ("webp", 720, 1604)}   # a-* are Android captures
def shot(name, alt, eager=False):
    ext, w, h = DIMS.get(name, ("webp", 654, 1415))
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<img src="/assets/shots/{name}.{ext}?v=2" alt="{alt}" width="{w}" height="{h}" {load} decoding="async">'

def phone(name, alt, small=False, eager=False):
    cls = "phone" + (" phone--sm" if small else "") + (" phone--android" if name.startswith("a-") else "")
    return f'<div class="{cls}"><div class="phone-body">{shot(name, alt, eager)}</div></div>'

TOUR = f'''
<section class="sec">
  <div class="wrap">
    <div class="wrap--narrow center" style="margin-bottom:64px">
      <p class="eyebrow">iPhone and Android</p>
      <h2>Every new account is <em>walked through it.</em></h2>
      <p class="lead">The first time someone signs in, Horreum takes them through the app stop by stop — the overview, the scanner, the lockers — on whichever phone they carry. It can be skipped at any time.</p>
    </div>
    <div class="trio trio--flat">
      {phone("a-overview", "The staff tour on an Android phone, stop one: the venue at a glance — inventory value, bottles on hand, active lockers, open requests")}
      {phone("a-scan", "The staff tour on an Android phone, stop two: scan a tag to open a bottle’s card and log a pull")}
      {phone("a-lockers", "The staff tour on an Android phone, stop three: the lockers list, and what is inside one")}
    </div>
  </div>
</section>
'''


HOME = f'''
<section class="h-hero">
  <div class="wrap">
    <p class="eyebrow">Wine reserve &amp; locker management</p>
    <h1>Every bottle, <em>accounted for.</em></h1>
    <p class="lead">Horreum runs a venue’s wine locker program end to end — the ledger, the labels, the pulls — and gives every member a collection worth showing off.</p>
    <div class="cta-row">
      <a class="btn btn--gold btn--lg" href="/contact?kind=demo">Request a demo {ARR}</a>
      <a class="btn btn--ghost btn--lg" href="#how">See how it works</a>
    </div>
    <p class="hero-note">Runs on the phones your staff already carry · iPhone and Android</p>
  </div>
  <div class="trio" aria-label="The Horreum member app">
    {phone("locker", "A member’s locker in the Horreum app: a dark wooden cabinet holding their bottles, with bottle and wine counts above", eager=True)}
    {phone("atlas", "The Atlas: a night globe with gold pins where the member’s wines were made", eager=True)}
    {phone("collection", "The Collection: a member’s cellar sheet, ready to print or share", eager=True)}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="wrap--narrow center" style="margin-bottom:64px">
      <p class="eyebrow">Why Horreum</p>
      <h2>A locker program runs on trust. <em>Horreum keeps the record behind it.</em></h2>
      <p class="lead">Venues put real care into looking after their members’ bottles. As a program grows, more of that care goes into the records — what is in each locker, where each bottle sits, what was opened and when. Horreum carries that part, so your team can stay with the guest.</p>
    </div>
    <div class="grid grid--3">
      {card("ledger", "One shared record", "Every member, locker and bottle in one place, so the floor, the bar and the office are always looking at the same thing.")}
      {card("log", "A history for every bottle", "Who stocked it, who pulled it, when and for whom — kept as the work happens, so the answer is there whenever a member asks.")}
      {card("find", "The right bottle, right away", "At 7:45 on a Saturday, the server is walked straight to the member’s bottle and where it sits. The table isn’t kept waiting.")}
    </div>
  </div>
</section>

<section class="sec" id="how">
  <div class="wrap">
    <div class="wrap--narrow center" style="margin-bottom:24px">
      <p class="eyebrow">How it works</p>
      <h2>Label. Stock. <em>Serve.</em></h2>
    </div>
    <div class="story">
      <div class="story-stage" aria-hidden="true">
        <div class="phone"><div class="phone-body"><div class="stack">
          {shot("scan", "")}
          {shot("overview", "")}
          {shot("hunt", "")}
        </div></div></div>
      </div>
      <div>
        <div class="chapter">
          <div class="num">01</div>
          <h3>Label</h3>
          <p>Your QR labels come from Horreum, minted in batches and registered before they ship, so a label cannot be forged, duplicated or lost to a misprint. Nothing to print. A tag comes back into circulation when its bottle leaves.</p>
          <div class="shot-m">{phone("scan", "The staff Scan page: one button to scan a bottle’s QR tag, or type the code")}</div>
        </div>
        <div class="chapter">
          <div class="num">02</div>
          <h3>Stock</h3>
          <p>Adding a bottle starts by scanning the QR tag that goes on it. Then the wine: pick it from your catalog, or enter its basics — producer, vintage, type — if it is not in the system yet. Then the locker, and where the bottle physically sits. The member’s collection updates that moment, and the activity log records who did it and when.</p>
          <div class="shot-m">{phone("overview", "The venue overview: inventory value, bottles and lockers in the program, open requests")}</div>
        </div>
        <div class="chapter">
          <div class="num">03</div>
          <h3>Serve</h3>
          <p>At the table, the member shows a code from their collection. The server scans it, is walked to the exact bottle and its storage spot, confirms it by scanning the bottle’s tag, and logs the pull. The member gets a note — and a chance to rate the bottle.</p>
          <div class="shot-m">{phone("hunt", "Find a bottle: the wine, whose locker, each bottle’s storage spot and tag")}</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="split" style="margin-bottom:72px;align-items:end">
      <div>
        <p class="eyebrow">For venues</p>
        <h2>The program you would be <em>proud to explain.</em></h2>
      </div>
      <div>
        <p class="lead">Everything the floor, the bar and the office need, in one record that never disagrees with itself.</p>
        <div class="cta-row"><a class="btn btn--ghost" href="/venues">Everything for venues {ARR}</a></div>
      </div>
    </div>
    <div class="grid grid--4">
      {card("ledger", "The ledger", "Every member, every locker, every bottle — house-purchased or brought in — with its vintage, where it sits, and its full history.")}
      {card("label", "Labels that last", "Durable QR labels, minted in batches and registered before they ship to you. Void a batch that goes missing; reclaim a tag when its bottle leaves.")}
      {card("spot", "Storage spots", "A locker is where a bottle belongs; the bar cooler is where it might sit tonight. Name your spots per location and every bottle knows both.")}
      {card("find", "Find my bottle", "The member shows a code; the server is walked to the exact bottle. A wrong bottle is refused before it ever leaves the cooler.")}
      {card("roles", "Roles and approvals", "Servers submit pulls; managers approve. Each account carries exactly the permissions you give it — enforced by the database, not the screen.")}
      {card("log", "Activity, append-only", "A full chain of custody: every add, pull, request and change, with who and when. Filter by day, week, month, or your own range.")}
      {card("notes", "Catalog and tasting notes", "Your list, per location, with prices and vintages. Horreum writes the tasting note for every wine — long-form, guest-ready, one voice.")}
      {card("brand", "Your brand, your locations", "White-label from the first screen: your logo, your themes, your locker finishes. Add locations as you grow; each keeps its own catalog, staff and records.")}
    </div>
  </div>
</section>

{TOUR}
<section class="atlas">
  <div class="wrap">
    <div class="copy">
      <p class="eyebrow">For members · The Atlas</p>
      <h2>The cellar, <em>region by region.</em></h2>
      <p class="lead">Members don’t get a spreadsheet. They get the world at night — and a gold pin wherever one of their bottles was made. Tap a region to see what grows there, and how far it travelled to their table.</p>
      <div class="cta-row" style="margin-top:28px"><a class="btn btn--ghost" href="/members">Everything for members {ARR}</a></div>
    </div>
    <div class="atlas-map" aria-hidden="true">
      <img src="/assets/img/atlas-night.webp" alt="" width="2049" height="1024" loading="lazy" decoding="async">
      <div class="pins">
        <span class="pin" style="left:25.7%;top:50.7%">22</span>
        <span class="pin" style="left:34.2%;top:40.5%">17</span>
        <span class="pin" style="left:45.3%;top:55.3%">9</span>
        <span class="pin" style="left:22.5%;top:59.5%">5</span>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="split">
      <div class="duo">
        {phone("history", "History: bottles enjoyed and rated, with a line about the evening")}
        {phone("bottle", "A wine’s card in Browse: Horreum’s tasting note, the story behind the wine, and a gold Request for my Locker button")}
      </div>
      <div>
        <p class="eyebrow">For members</p>
        <h2>A collection worth <em>showing off.</em></h2>
        <ul>
          <li><b>The Locker.</b> Their own cabinet, in a finish of their choosing, with every bottle standing in it.</li>
          <li><b>The Collection.</b> Every bottle with Horreum’s tasting note and the story behind it, drawn as a cellar sheet they can print or share.</li>
          <li><b>History, ratings and a journal.</b> What they enjoyed, what they thought of it, and a line about the evening it was opened.</li>
          <li><b>Show your server.</b> One tap on a bottle shows the code that brings it to the table.</li>
          <li><b>Requests and messages.</b> Ask for a bottle from the list, or a word with the team, without picking up the phone.</li>
          <li><b>Two faces.</b> Classic by day, midnight after dark — it follows the clock.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="sec center">
  <div class="wrap--narrow">
    <p class="eyebrow">Pricing</p>
    <h2>Contact us for pricing.</h2>
    <p class="lead">Tell us a little about your program and we’ll be in touch.</p>
    <div class="cta-row" style="margin-top:30px"><a class="btn btn--gold" href="/contact?kind=pricing">Contact us {ARR}</a></div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="split split--rev">
      <div class="card boxed">
        <span class="ico">{ICON["shield"]}</span>
        <h3>Built to be trusted with other people’s wine.</h3>
        <p>Each venue’s data is isolated by row-level security in Postgres. Staff permissions are enforced by the database itself. Card payments, when a venue turns them on, are handled by Stripe and never pass through Horreum. The activity log is append-only.</p>
        <p style="margin-top:18px"><a href="/security">How Horreum handles data →</a></p>
      </div>
      <div>
        <p class="eyebrow">Trust</p>
        <h2>Records that can be <em>relied on.</em></h2>
        <p class="lead">A locker program is a promise to members. The software that runs it should be at least as careful as the people who make that promise.</p>
      </div>
    </div>
  </div>
</section>

<section class="finale">
  <div class="wrap--narrow">
    <h2>See it on <em>your floor.</em></h2>
    <p class="lead">A thirty-minute walkthrough with the person who built it.</p>
    <div class="cta-row" style="margin-top:34px"><a class="btn btn--gold btn--lg" href="/contact?kind=demo">Request a demo {ARR}</a><a class="btn btn--ghost btn--lg" href="mailto:gabriel@horreum.cloud" data-hz="email">gabriel@horreum.cloud</a></div>
  </div>
</section>
'''
