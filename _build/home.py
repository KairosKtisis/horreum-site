# Home (v2). The page is the app's own night, with daylight where the venue works.
from icons import ICON
from shell import APP, ARR

def card(icon, title, text, cls="", tag=""):
    t = f'<div class="tag">{tag}</div>' if tag else ''
    return f'<div class="card {cls}"><span class="ico">{ICON[icon]}</span><h3>{title}</h3><p>{text}</p>{t}</div>'

# every screen is the phone's own 390:844 — the frame in site.css is drawn for exactly that shape
DIMS = {"find": ("jpg", 390, 844), "locker": ("webp", 924, 2000), "hunt": ("webp", 924, 2000)}
def shot(name, alt, eager=False):
    ext, w, h = DIMS.get(name, ("webp", 654, 1415))
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<img src="/assets/shots/{name}.{ext}?v=2" alt="{alt}" width="{w}" height="{h}" {load} decoding="async">'

def phone(name, alt, small=False, eager=False):
    return f'<div class="phone{" phone--sm" if small else ""}"><div class="phone-body">{shot(name, alt, eager)}</div></div>'

BAND = "".join(f"<span>{w}</span>" for w in ["The ledger", "The labels", "The pulls", "The atlas", "The collection", "The history", "The storehouse"])

HOME = f'''
<section class="h-hero">
  <canvas class="sky" aria-hidden="true"></canvas>
  <div class="wrap">
    <p class="kicker fade"><i></i>Wine reserve &amp; locker management</p>
    <h1><span class="ln"><span>Every bottle,</span></span><span class="ln"><span><em>accounted for.</em></span></span></h1>
    <p class="lead fade">Horreum runs a venue’s wine locker program end to end — the ledger, the labels, the pulls — and gives every member a collection worth showing off. Built on the floor of a fine-dining chophouse, where it runs today.</p>
    <div class="cta-row fade">
      <a class="btn btn--gold btn--lg" href="/contact?kind=demo">Request a demo {ARR}</a>
      <a class="btn btn--ghost btn--lg" href="#how">See how it works</a>
    </div>
    <p class="hero-note fade">No hardware to buy · Runs on the phones your staff already carry · iPhone and Android</p>
  </div>
  <div class="fan fade" aria-label="The Horreum member app">
    {phone("locker", "A member’s locker in the Horreum app: a wooden cabinet holding their bottles, with bottle and wine counts above", eager=True)}
    {phone("atlas", "The Atlas: a night globe with gold pins where the member’s wines were made", eager=True)}
    {phone("collection", "The Collection: a member’s cellar sheet, ready to print or share", eager=True)}
  </div>
</section>

<div class="band" aria-hidden="true"><div class="band-track">{BAND}{BAND}</div></div>

<section class="sec">
  <div class="wrap">
    <div class="wrap--narrow center" style="margin-bottom:64px">
      <p class="eyebrow">The problem</p>
      <h2>A locker program runs on trust. <em>Trust runs on records.</em></h2>
      <p class="lead">Members leave bottles worth real money in your care. The program only works while everyone’s records agree — and a spreadsheet, a binder and someone’s memory rarely do.</p>
    </div>
    <div class="grid grid--3">
      {card("ledger", "Conflicting records", "Two lists, one bottle, and a member who remembers it differently. Every disagreement is a conversation you would rather not have.")}
      {card("log", "No chain of custody", "Who stocked it, who pulled it, when, and for whom. Without an append-only log, nobody can answer with certainty — and certainty is the product.")}
      {card("find", "The search during service", "A guest asks for their bottle at 7:45 on a Saturday. The server goes looking. The table waits, and the wrong bottle is one guess away.")}
    </div>
  </div>
</section>

<section class="sec sec--night" id="how">
  <div class="wrap">
    <div class="wrap--narrow center" style="margin-bottom:24px">
      <p class="eyebrow">How it works</p>
      <h2>Label. Stock. <em>Serve.</em></h2>
    </div>
    <div class="story">
      <div class="story-stage" aria-hidden="true">
        <div class="halo"></div>
        <div class="phone"><div class="phone-body"><div class="stack">
          {shot("scan", "")}
          {shot("overview", "")}
          {shot("hunt", "")}
        </div></div></div>
      </div>
      <div>
        <div class="chapter">
          <div class="num">I</div>
          <h3>Label</h3>
          <p>Your QR labels come from Horreum, minted in batches and registered before they ship, so a label cannot be forged, duplicated or lost to a misprint. Nothing to print. A tag comes back into circulation when its bottle leaves.</p>
          <div class="shot-m">{phone("scan", "The staff Scan page: one button to scan a bottle’s QR tag, or type the code")}</div>
        </div>
        <div class="chapter">
          <div class="num">II</div>
          <h3>Stock</h3>
          <p>Adding a bottle starts by scanning the QR tag that goes on it. Then the wine: pick it from your catalog, or enter its basics — producer, vintage, type — if it is not in the system yet. Then the locker, and where the bottle physically sits. The member’s collection updates that moment, and the activity log records who did it and when.</p>
          <div class="shot-m">{phone("overview", "The venue overview: inventory value, bottles and lockers in the program, open requests")}</div>
        </div>
        <div class="chapter">
          <div class="num">III</div>
          <h3>Serve</h3>
          <p>At the table, the member shows a code from their collection. The server scans it, is walked to the exact bottle and its storage spot, confirms it by scanning the bottle’s tag, and logs the pull. The member gets a note — and a chance to rate the bottle.</p>
          <div class="shot-m">{phone("hunt", "Find a bottle: the wine, whose locker, each bottle’s storage spot and tag")}</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec day">
  <div class="wrap">
    <div class="split" style="margin-bottom:64px;align-items:end">
      <div>
        <p class="eyebrow">For venues</p>
        <h2>The program you would be <em>proud to explain.</em></h2>
      </div>
      <div>
        <p class="lead">Everything the floor, the bar and the office need, in one record that never disagrees with itself.</p>
        <div class="cta-row"><a class="btn btn--ghost" href="/venues">Everything for venues {ARR}</a></div>
      </div>
    </div>
    <div class="bento">
      {card("ledger", "The ledger", "Every member, every locker, every bottle — house-purchased or brought in — with its vintage, where it sits, and its full history.", "w4 feature", "One record of truth")}
      {card("label", "Labels that last", "Durable QR labels, minted in batches and registered before they ship to you. Void a batch that goes missing; reclaim a tag when its bottle leaves.")}
      {card("spot", "Storage spots", "A locker is where a bottle belongs; the bar cooler is where it might sit tonight. Name your spots per location and every bottle knows both.")}
      {card("find", "Find my bottle", "The member shows a code; the server is walked to the exact bottle. A wrong bottle is refused before it ever leaves the cooler.")}
      {card("roles", "Roles and approvals", "Servers submit pulls; managers approve. Each account carries exactly the permissions you give it — enforced by the database, not the screen.")}
      {card("log", "Activity, append-only", "A full chain of custody: every add, pull, request and change, with who and when. Filter by day, week, month, or your own range.", "w3")}
      {card("notes", "Catalog and tasting notes", "Your list, per location, with prices and vintages. Horreum writes the tasting note for every wine — long-form, guest-ready, one voice.", "w3")}
      {card("brand", "Your brand, your locations", "White-label from the first screen: your logo, your themes, your locker finishes. Add locations as you grow; each keeps its own catalog, staff and records.", "w4 feature", "White-label")}
      <div class="card shotcard"><div>{phone("requests", "The venue’s request queue: a member’s purchase request with Fulfil and Dismiss")}</div></div>
    </div>
  </div>
</section>

<section class="atlas">
  <div class="atlas-map" aria-hidden="true">
    <img src="/assets/img/atlas-night.webp" alt="" width="2049" height="1024" loading="lazy" decoding="async">
    <span class="pin" style="left:25.7%;top:50.7%">22</span>
    <span class="pin" style="left:34.2%;top:40.5%">17</span>
    <span class="pin" style="left:45.3%;top:55.3%">9</span>
    <span class="pin" style="left:22.5%;top:59.5%">5</span>
  </div>
  <div class="wrap">
    <div class="copy">
      <p class="eyebrow">For members · The Atlas</p>
      <h2>The cellar, <em>region by region.</em></h2>
      <p class="lead">Members don’t get a spreadsheet. They get the world at night — and a gold pin wherever one of their bottles was made. Tap a region to see what grows there, and how far it travelled to their table.</p>
      <div class="cta-row" style="margin-top:30px"><a class="btn btn--ghost" href="/members">Everything for members {ARR}</a></div>
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

<section class="sec day">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">Pricing</p>
        <h2>Priced according to <em>your needs.</em></h2>
        <p class="lead">No per-seat fees, no per-member fees, no hardware to buy. Every locker program is a different size, so the price follows yours — tell us about it and you’ll have a number the same day.</p>
        <div class="cta-row"><a class="btn btn--gold" href="/contact?kind=pricing">Ask about pricing {ARR}</a><a class="btn btn--ghost" href="/pricing">What’s included</a></div>
      </div>
      <div class="grid grid--2" style="gap:16px">
        <div class="stat"><b>0</b><span>Per-seat fees</span></div>
        <div class="stat"><b>0</b><span>Per-member fees</span></div>
        <div class="stat"><b>0</b><span>Hardware to buy</span></div>
        <div class="stat"><b>1</b><span>Record of truth</span></div>
      </div>
    </div>
  </div>
</section>

<section class="sec sec--night">
  <div class="wrap">
    <div class="split split--rev">
      <div class="card" style="padding:40px">
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
  <canvas class="sky" aria-hidden="true"></canvas>
  <div class="wrap--narrow" style="position:relative;z-index:1">
    <img class="glyph" src="/assets/img/glyph-cream.svg" alt="" width="64" height="64">
    <h2>See it on <em>your floor.</em></h2>
    <p class="lead">A thirty-minute walkthrough with the person who built it. Bring your binder.</p>
    <div class="cta-row" style="margin-top:34px"><a class="btn btn--gold btn--lg" href="/contact?kind=demo">Request a demo {ARR}</a><a class="btn btn--ghost btn--lg" href="mailto:gabriel@horreum.cloud" data-hz="email">gabriel@horreum.cloud</a></div>
  </div>
</section>
'''
