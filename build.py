"""Builds the static pages for the Golden Sparrow Patisserie website.

Edit the business details, hours, menu and FAQs below, then run:
    python3 build.py
Every page (index, menu, about, faq) is regenerated so header/footer stay consistent.
If you change opening hours, also update HOURS near the top of assets/main.js.
"""
import json, os

OUT = os.path.dirname(os.path.abspath(__file__))

BIZ = {
    "name": "Golden Sparrow Patisserie",
    "short": "golden sparrow",
    "tagline": "A little sweetness for every occasion",
    "street": "6B/2 Rhye Street, Building A, East Village",
    "suburb": "Sunbury",
    "state": "VIC",
    "postcode": "3429",
    "phone": "0452 209 929",
    "email": "admin@goldensparrowpatisserie.com.au",
    "url": "https://www.goldensparrowpatisserie.com.au",
    "maps": "https://www.google.com/maps/search/?api=1&query=Golden+Sparrow+Patisserie+East+Village+Sunbury",
}
ADDR = f'{BIZ["street"]}, {BIZ["suburb"]} {BIZ["state"]} {BIZ["postcode"]}'
# (day name, JS day number 0=Sun..6=Sat, label) — keep in sync with HOURS in assets/main.js
HOURS = [("Monday", 1, "7 am – 5 pm"), ("Tuesday", 2, "7 am – 5 pm"), ("Wednesday", 3, "7 am – 5 pm"),
         ("Thursday", 4, "7 am – 5 pm"), ("Friday", 5, "7 am – 5 pm"), ("Saturday", 6, "7 am – 5 pm"),
         ("Sunday", 0, "7 am – 4 pm")]

# Placeholder mark until the real logo file arrives
BIRD = ('<path d="M15 39c5-9 15-15 27-14 3-6 9-8 14-6-3 1-5 3-6 6 1 10-7 19-19 20-6 1-11-1-15-4l-9 6 3-9z" fill="currentColor"/>'
        '<circle cx="50" cy="22" r="1.6" fill="#fff"/>')
LOGO = f'<svg viewBox="0 0 64 64" aria-hidden="true">{BIRD}</svg>'

def hours_rows():
    return "".join(f'<tr data-day="{d}"><td>{n}</td><td>{h}</td></tr>' for n, d, h in HOURS)

def schema():
    data = {
        "@context": "https://schema.org", "@type": "CafeOrCoffeeShop", "name": BIZ["name"], "url": BIZ["url"],
        "slogan": BIZ["tagline"], "telephone": BIZ["phone"], "email": BIZ["email"],
        "servesCuisine": ["Coffee", "Patisserie", "Cakes", "Churros", "Sandwiches"],
        "address": {"@type": "PostalAddress", "streetAddress": BIZ["street"], "addressLocality": BIZ["suburb"],
                    "addressRegion": BIZ["state"], "postalCode": BIZ["postcode"], "addressCountry": "AU"},
        "openingHours": ["Mo-Sa 07:00-17:00", "Su 07:00-16:00"],
        "hasMenu": BIZ["url"] + "/menu.html",
        "paymentAccepted": "Card, Tap and go, Apple Pay, Google Pay, Cash",
        "acceptsReservations": False,
    }
    return '<script type="application/ld+json">' + json.dumps(data) + "</script>"

def head(title, desc, page, extra=""):
    return f'''<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#1c1f16">
<link rel="canonical" href="{BIZ["url"]}/{page}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BIZ["name"]}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{BIZ["url"]}/{page}">
<meta property="og:locale" content="en_AU">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cpath d='M15 39c5-9 15-15 27-14 3-6 9-8 14-6-3 1-5 3-6 6 1 10-7 19-19 20-6 1-11-1-15-4l-9 6 3-9z' fill='%23b8924a'/%3E%3C/svg%3E">
<link rel="preload" href="assets/fonts/CabinetGrotesk-Medium.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/style.css">
{schema()}{extra}
</head>
<body>
<div class="loader" aria-hidden="true">
  <div>
    <svg class="loader__mark" viewBox="0 0 64 64"><circle class="fill" cx="32" cy="32" r="30" fill="none" stroke="currentColor" stroke-width="2"/><g class="bean" transform="translate(4 4) scale(.875)">{BIRD}</g></svg>
    <div class="loader__word">{BIZ["short"]}</div>
  </div>
</div>
'''

def nav(active):
    links = [("index.html", "Home"), ("menu.html", "Menu"), ("about.html", "Our story"), ("faq.html", "FAQ")]
    def a(h, t):
        cur = ' aria-current="page"' if h == active else ""
        return f'<a href="{h}"{cur}>{t}</a>'
    desktop = "".join(a(h, t) for h, t in links[1:])
    mobile = "".join(a(h, t) for h, t in links)
    return f'''<header class="nav">
  <div class="wrap nav__in">
    <a class="logo" href="index.html" aria-label="{BIZ["name"]} home"><span class="gold">{LOGO}</span><span>{BIZ["short"]}</span></a>
    <nav class="nav__links" aria-label="Main">{desktop}<a class="btn" href="index.html#visit">Visit us <span class="arrow">→</span></a></nav>
    <button class="nav__toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span></button>
  </div>
</header>
<nav class="overlay" aria-label="Mobile">{mobile}<a class="btn" href="index.html#visit">Visit us <span class="arrow">→</span></a></nav>
'''

def footer():
    return f'''<footer class="footer">
  <div class="wrap">
    <div class="footer__top" data-stagger=".08">
      <div data-reveal>
        <p class="h3" style="max-width:16ch">{BIZ["tagline"]}.</p>
        <div class="pill" data-open><span class="dot"></span>Open today</div>
      </div>
      <div data-reveal>
        <h4>Visit</h4>
        <p>6B/2 Rhye Street, Building A<br>East Village, {BIZ["suburb"]} {BIZ["state"]} {BIZ["postcode"]}</p>
        <p style="margin-top:12px"><a href="tel:{BIZ["phone"].replace(" ", "")}">{BIZ["phone"]}</a><br><a href="mailto:{BIZ["email"]}">{BIZ["email"]}</a></p>
      </div>
      <div data-reveal>
        <h4>Explore</h4>
        <ul><li><a href="menu.html">Menu</a></li><li><a href="about.html">Our story</a></li><li><a href="faq.html">FAQ</a></li><li><a href="{BIZ["maps"]}">Get directions</a></li></ul>
      </div>
      <div data-reveal>
        <h4>Hours</h4>
        <table class="hours"><tbody>{hours_rows()}</tbody></table>
        <p class="small" style="color:var(--muted);margin-top:8px">Public holiday hours may vary.</p>
      </div>
    </div>
    <div class="footer__img" data-reveal="img"><div class="ph ph--scene alt"><span class="ph__label">Photo · shopfront</span></div></div>
  </div>
  <div class="wrap"><div class="footer__word" aria-hidden="true">golden sparrow</div></div>
  <div class="wrap footer__bottom">
    <span>© <span data-year>2026</span> {BIZ["name"]}. All rights reserved.</span>
    <span>Website by <a href="https://www.novalinkinnovations.com">NovaLink Innovations</a></span>
  </div>
</footer>
<script src="assets/main.js"></script>
</body>
</html>
'''

def card(cup, name, note, tags=(), scene=None):
    t = "".join(f'<span class="tag">{x}</span>' for x in tags)
    img = (f'<div class="ph" data-cup="{cup}" role="img" aria-label="{name}"></div>' if cup
           else f'<div class="ph ph--scene {scene or ""}" role="img" aria-label="{name}"><span class="ph__label">Photo · {name}</span></div>')
    return f'''<article class="card" data-reveal>
  <div class="card__img">{img}</div>
  <div class="card__row noprice"><h3 class="h3">{name}</h3></div>
  <p class="card__note">{note}</p>
  {f'<div class="card__tags">{t}</div>' if tags else ''}
</article>'''

def item(name, note, tags=()):
    t = "".join(f'<span class="tag">{x}</span>' for x in tags)
    return f'''<div class="list__item" data-reveal>
  <h3 class="h3">{name}</h3><span></span>
  <p class="card__note">{note}</p>
  {f'<div class="card__tags">{t}</div>' if tags else ''}
</div>'''

def visit_section():
    return f'''<section class="section section--cream" id="visit" aria-labelledby="visit-title">
  <div class="wrap visit">
    <div class="stack" data-stagger=".08">
      <p class="eyebrow" data-reveal>Visit us</p>
      <h2 class="h2" id="visit-title" data-reveal>Just outside Woolies at East Village</h2>
      <p class="body" data-reveal>Find us at {ADDR}. No booking needed, just walk in. Free parking right outside.</p>
      <div class="pill" data-open data-reveal><span class="dot"></span>Open today</div>
      <table class="hours" data-reveal><tbody>{hours_rows()}</tbody></table>
      <p class="small" style="color:var(--muted-2)" data-reveal>Public holiday hours may vary.</p>
      <div class="visit__btns" data-reveal>
        <a class="btn" href="{BIZ["maps"]}">Get directions <span class="arrow">→</span></a>
        <a class="btn btn--light" href="tel:{BIZ["phone"].replace(" ", "")}">Call {BIZ["phone"]}</a>
      </div>
    </div>
    <div class="map" data-reveal="img"><div class="ph ph--scene light"><span class="ph__label">Google Map · East Village Sunbury</span></div></div>
  </div>
</section>'''

# ------------------------------------------------------------------ HOME
home = head(f'{BIZ["name"]} · Café & patisserie in East Village, Sunbury',
            f'{BIZ["name"]} is a local café and patisserie at East Village, Sunbury. Coffee, cakes, golden churros, sandwiches and soft serve. Walk in, no booking needed.',
            "") + nav("index.html") + f'''<main>
<section class="hero" aria-labelledby="hero-title">
  <div class="wrap">
    <h1 class="sr-only" id="hero-title">{BIZ["name"]}, café and patisserie in Sunbury</h1>
    <div class="hero__grid">
      <p class="display hero__left" aria-hidden="true"><span class="line"><span>A little</span></span><span class="line"><span>sweetness</span></span></p>
      <div class="hero__img"><div class="ph" data-cup="cappuccino" role="img" aria-label="Cappuccino at Golden Sparrow"></div></div>
      <p class="display hero__right" aria-hidden="true"><span class="line"><span>for every</span></span><span class="line"><span class="gold">occasion</span></span></p>
    </div>
    <div class="hero__bottom">
      <p class="lead">Coffee, cakes, golden churros and a warm welcome, at East Village in Sunbury. Pull up a chair or take something sweet to go.</p>
      <div class="pill" data-open><span class="dot"></span>Open today</div>
    </div>
  </div>
</section>

<section class="section" style="overflow:hidden" aria-labelledby="intro-title">
  <svg class="watermark" viewBox="0 0 64 64" aria-hidden="true">{BIRD}</svg>
  <div class="wrap split">
    <h2 class="h2" id="intro-title" data-reveal>It's the little things that make life beautiful.</h2>
    <div class="stack" data-stagger=".1">
      <p class="body" data-reveal>A welcoming smile, a familiar cup of coffee and moments shared with the people who matter. After nearly ten years in hospitality, we opened Golden Sparrow as our own independent café, a place where everyone feels at home.</p>
      <p data-reveal><a class="link" href="about.html">Read our story</a></p>
    </div>
  </div>
</section>

<section class="section section--cream" aria-labelledby="start-title">
  <div class="wrap">
    <div class="head">
      <div class="stack" data-stagger=".08">
        <p class="eyebrow" data-reveal>Sip something special</p>
        <h2 class="h2" id="start-title" data-reveal>Our signature drinks</h2>
        <p class="body" data-reveal>Four favourites our regulars come back for. Indulge in every sip.</p>
      </div>
      <a class="link" href="menu.html" data-reveal>See the full menu</a>
    </div>
    <div class="cards" data-stagger=".1">
      {card("matcha", "Matcha Latte", "Smooth, creamy and beautifully green. A calm little moment in a cup.")}
      {card("raffaello", "Raffaello Hot Chocolate", "Creamy white chocolate, coconut and almond. Pure indulgence.")}
      {card("icedchoc", "Iced Chocolate", "Rich chocolate over ice, finished with cream. A sweet treat any time of day.")}
      {card("cappuccino", "Cappuccino", "Velvety foam and a dusting of chocolate, made just the way you like it.")}
    </div>
  </div>
</section>

<section class="section section--dark" aria-labelledby="room-title">
  <div class="wrap">
    <div class="split" data-stagger=".08">
      <h2 class="h2" id="room-title" data-reveal>Your local café at East Village</h2>
      <div data-reveal>
        <p class="body">Warm oak, soft light and a counter full of cakes and sweets. We've watched local families grow, and we know many of our regulars by name.</p>
        <div class="facts"><span>Dine in or takeaway</span><span>26 seats</span><span>Free parking</span><span>Dogs welcome outside</span></div>
      </div>
    </div>
    <div class="room">
      <div data-reveal="img"><div class="ph ph--scene"><span class="ph__label">Photo · café interior</span></div></div>
      <div data-reveal="img" style="--d:.12s"><div class="ph ph--scene alt"><span class="ph__label">Photo · cake display</span></div></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="known-title">
  <div class="wrap">
    <div class="head">
      <div class="stack" data-stagger=".08">
        <p class="eyebrow" data-reveal>What we're known for</p>
        <h2 class="h2" id="known-title" data-reveal>Made with care, served with a smile</h2>
      </div>
      <a class="link" href="about.html" data-reveal>Read our story</a>
    </div>
    <div class="steps" data-stagger=".1">
      <div class="step step--cream" data-reveal><span class="step__num">01</span><div><h3 class="h3">Golden churros</h3><p class="body">Crisp, golden and dusted with sugar. Our sweet signature.</p></div></div>
      <div class="step step--cream" data-reveal><span class="step__num">02</span><div><h3 class="h3">Cakes for every occasion</h3><p class="body">Birthdays, celebrations or just because. Ask us about special cakes.</p></div></div>
      <div class="step step--cream" data-reveal><span class="step__num">03</span><div><h3 class="h3">Catering &amp; platters</h3><p class="body">Customised platters for groups, events and the office.</p></div></div>
    </div>
  </div>
</section>

{visit_section()}
</main>
''' + footer()

# ------------------------------------------------------------------ MENU
# NOTE: sample items until Vani's menu PDF arrives — replace with the real menu. No prices (client request).
menu_cats = [
    ("hot", "Hot drinks", "Made fresh, just the way you like it.", [
        ("cappuccino", "Cappuccino", "Velvety foam with a dusting of chocolate."),
        ("latte", "Latte", "Smooth espresso with creamy steamed milk."),
        ("flatwhite", "Flat White", "Silky milk over a double shot."),
        ("matcha", "Matcha Latte", "Creamy, calming and beautifully green."),
        ("raffaello", "Raffaello Hot Chocolate", "White chocolate, coconut and almond."),
        ("chai", "Chai Latte", "Warm spices and steamed milk."),
    ]),
    ("cold", "Cold drinks", "Poured over ice, made to order.", [
        ("icedchoc", "Iced Chocolate", "Rich chocolate over ice with cream."),
        ("iced", "Iced Latte", "Espresso over ice with cold milk."),
        ("matcha", "Iced Matcha", "Matcha and milk over ice."),
    ]),
]
food_cats = [
    ("sandwiches", "Sandwiches", "Freshly made every day.", ["Sandwich", "Toastie", "Wrap"]),
    ("allday", "All day menu", "Something for every appetite, all day long.", ["All day breakfast", "Light meals", "Kids' options"]),
    ("churros", "Golden churros", "Our sweet signature, crisp and golden.", ["Classic churros", "Churros with chocolate", "Churros sharing box"]),
    ("fries", "Golden fries", "Crispy and perfectly seasoned.", ["Golden fries", "Loaded fries"]),
    ("softserve", "Soft serve", "A cool and creamy treat.", ["Soft serve cone", "Sundae", "Soft serve cup"]),
    ("sweets", "Cakes & sweets", "From our display cabinet, made for every occasion.", ["Cakes", "Individual sweets", "Celebration cakes (order ahead)"]),
]
tabs = "".join(f'<a href="#{k}"{" class=\"active\"" if i == 0 else ""}>{t}</a>' for i, (k, t, *_ ) in enumerate(menu_cats + food_cats))
menu_html = ""
for key, title, sub, items in menu_cats:
    cards = "".join(card(c, n, d) for c, n, d in items)
    menu_html += f'''<section class="menu-cat" id="{key}" aria-labelledby="{key}-h">
  <div class="wrap">
    <div class="head"><div class="stack"><h2 class="h2" id="{key}-h" data-reveal>{title}</h2><p class="body" data-reveal>{sub}</p></div></div>
    <div class="grid3" data-stagger=".08">{cards}</div>
  </div>
</section>'''
for key, title, sub, items in food_cats:
    rows = "".join(item(n, "") for n in items)
    menu_html += f'''<section class="menu-cat" id="{key}" aria-labelledby="{key}-h">
  <div class="wrap">
    <div class="head"><div class="stack"><h2 class="h2" id="{key}-h" data-reveal>{title}</h2><p class="body" data-reveal>{sub}</p></div></div>
    <div class="list">{rows}</div>
  </div>
</section>'''

menu = head(f'Menu · {BIZ["name"]}, Sunbury',
            f'The {BIZ["name"]} menu: coffee, matcha, Raffaello hot chocolate, iced drinks, sandwiches, all day menu, golden churros, golden fries, soft serve and cakes.',
            "menu.html") + nav("menu.html") + f'''<main>
<section class="page-head">
  <div class="wrap">
    <h1 class="h1" data-reveal>Our menu</h1>
    <div class="stack" data-stagger=".08">
      <p class="body" data-reveal>Coffee, sweet treats and something for every appetite. We cater for a range of dietary requirements, so just ask our team.</p>
    </div>
  </div>
</section>
<div class="tabs"><div class="wrap tabs__in">{tabs}</div></div>
{menu_html}
<section class="wrap" style="padding-bottom:clamp(56px,7vw,96px)">
  <p class="notice" data-reveal>Allergy notice: please let our team know about any allergies before ordering.</p>
</section>
</main>
''' + footer()

# ------------------------------------------------------------------ ABOUT
about = head(f'Our story · {BIZ["name"]}',
             f'The story behind {BIZ["name"]}, an independent café and patisserie at East Village, Sunbury.',
             "about.html") + nav("about.html") + f'''<main>
<section class="page-head">
  <div class="wrap">
    <h1 class="h1" data-reveal>Our story</h1>
    <p class="lead" data-reveal>Bringing a little warmth and happiness to every moment.</p>
  </div>
</section>

<section class="section" style="padding-top:0" aria-label="How it started">
  <div class="wrap split" style="align-items:start">
    <div class="about-imgs">
      <div data-reveal="img"><div class="ph" data-cup="cappuccino" role="img" aria-label="Cappuccino"></div></div>
      <div data-reveal="img" style="--d:.12s"><div class="ph ph--scene"><span class="ph__label">Photo · owners</span></div></div>
    </div>
    <div class="stack" data-stagger=".1">
      <hr class="rule" data-reveal>
      <h2 class="h2" data-reveal>How it started</h2>
      <p class="body" data-reveal>We've been in the hospitality business for nearly ten years as franchisees. Through all those years, we always dreamed of opening an independent café of our own, and that dream became Golden Sparrow Patisserie.</p>
      <p class="body" data-reveal>What makes us special is simple: our regular customers, genuine hospitality and the local families we've come to know and watched grow. Locals, seniors, families, tradies and the team from the centre all stop by, and every one of them is part of our story.</p>
    </div>
  </div>
</section>

<section class="section section--olive" aria-label="Our vision">
  <div class="wrap split">
    <p class="quote" data-reveal>“It's the little things that make life beautiful.”</p>
    <div class="stack" data-stagger=".1">
      <p class="body" data-reveal>Our vision is to create more than just a place to enjoy good food and drinks. We want to create a welcoming space where everyone feels at home.</p>
      <p class="body" data-reveal>Whether you're stopping by for your morning coffee, catching up with friends or treating yourself to something special, we're delighted to be part of your day.</p>
    </div>
  </div>
</section>

<section class="section section--cream" aria-labelledby="values-title">
  <div class="wrap">
    <div class="head"><h2 class="h2" id="values-title" data-reveal>What we care about</h2></div>
    <div class="steps" data-stagger=".1">
      <div class="step" data-reveal><span class="step__num">01</span><div><h3 class="h3">Genuine hospitality</h3><p class="body">A warm welcome and a familiar face, every visit.</p></div></div>
      <div class="step" data-reveal><span class="step__num">02</span><div><h3 class="h3">Our community</h3><p class="body">Proud to be part of East Village and the Sunbury community.</p></div></div>
      <div class="step" data-reveal><span class="step__num">03</span><div><h3 class="h3">Little moments</h3><p class="body">A little sweetness for every occasion, big or small.</p></div></div>
    </div>
  </div>
</section>

<section class="section cta">
  <div class="wrap stack" data-stagger=".1">
    <h2 class="h2" data-reveal>Come and say hello</h2>
    <p data-reveal><a class="btn btn--gold" href="index.html#visit">Visit us <span class="arrow">→</span></a></p>
  </div>
</section>
</main>
''' + footer()

# ------------------------------------------------------------------ FAQ
faqs = [
    ("Do you offer catering for large groups?", "Yes. We can organise customised platters for groups, events and the office. Get in touch to discuss your order."),
    ("Do you cater for dietary requirements?", "Yes, we have a range of options to choose from. Just ask our team and we'll help you find something."),
    ("Do I need to book a table?", "No booking required. Just walk in."),
    ("Where can I find Golden Sparrow Patisserie?", f"We're located at East Village Sunbury, just outside Woolies: {ADDR}."),
    ("Do you make special cakes?", "Yes. We can organise cakes for all special occasions. Please get in touch ahead of time."),
    ("Do you offer takeaway?", "Yes, everything on our menu is available to dine in or take away."),
    ("Is there parking nearby?", "Yes, there is free parking right outside at East Village."),
    ("Are dogs welcome?", "Dogs are welcome at our outdoor seating."),
    ("What payment methods do you accept?", "We accept card, tap and go, Apple Pay, Google Pay and cash."),
]
faq_html = "".join(f'''<details data-reveal>
  <summary aria-expanded="false">{q}<span class="plus" aria-hidden="true"></span></summary>
  <div class="faq__a"><p>{a}</p></div>
</details>''' for q, a in faqs)
faq_schema = '<script type="application/ld+json">' + json.dumps({
    "@context": "https://schema.org", "@type": "FAQPage",
    "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}) + "</script>"

faq = head(f'FAQ · {BIZ["name"]}',
           f'Answers to common questions about {BIZ["name"]} in Sunbury: catering, dietary requirements, special cakes, parking and more.',
           "faq.html", faq_schema) + nav("faq.html") + f'''<main>
<section class="page-head">
  <div class="wrap">
    <h1 class="h1" data-reveal>Good questions</h1>
    <p class="body" data-reveal>Everything you might want to know before you visit. Can't find your answer? Call us on {BIZ["phone"]}.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap"><div class="faq" data-stagger=".06">{faq_html}</div></div>
</section>
{visit_section()}
</main>
''' + footer()

for name, html in [("index.html", home), ("menu.html", menu), ("about.html", about), ("faq.html", faq)]:
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
print("built")
