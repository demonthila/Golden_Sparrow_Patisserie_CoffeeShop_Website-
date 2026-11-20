"""Builds the static pages for the Golden Sparrow Patisserie website.

Edit the business details, hours, menu and FAQs below, then run:
    python3 build.py
Every page (index, menu, about, faq) is regenerated so header/footer stay consistent.
If you change opening hours, also update HOURS near the top of assets/main.js.
"""
import json, os

OUT = os.path.dirname(os.path.abspath(__file__))

BIZ = {
    "instagram": "https://www.instagram.com/invites/contact/?utm_content=4iaiwdz&fqnt=200skti3hcl2",
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

# Stock photos from Unsplash (free licence). Swap for Vani's own photos when they arrive:
# replace the value with a local path like "assets/img/cappuccino.jpg".
U = "https://images.unsplash.com/"
IMG = {
    "hero": "photo-1512568400610-62da28bc8a13",
    "cappuccino": "photo-1509042239860-f550ce710b93",
    "latte": "photo-1485808191679-5f86510681a2",
    "flatwhite": "photo-1514432324607-a09d9b4aefdd",
    "matcha": "photo-1515823064-d6e0c04616a7",
    "icedmatcha": "photo-1717603545758-88cc454db69b",
    "raffaello": "photo-1762411245614-e0f145ba7183",
    "icedchoc": "photo-1559329187-79d04171a646",
    "icedlatte": "photo-1461023058943-07fcbe16d735",
    "chai": "photo-1561336526-2914f13ceb36",
    "churros": "photo-1767489386700-cb3dbcbab13d",
    "churroscoffee": "photo-1702896287488-0a83b9baaab9",
    "fries": "photo-1630384060421-cb20d0e0649d",
    "softserve": "photo-1697125138277-962ef4126de4",
    "sundae": "photo-1695886855588-47117bca2fe6",
    "sandwich": "photo-1528736235302-52922df5c122",
    "cakedisplay": "photo-1583338917451-face2751d8d5",
    "cake": "photo-1571115177098-24ec42ed204d",
    "macarons": "photo-1558326567-98ae2405596b",
    "pastries": "photo-1707289424585-66b799af6375",
    "interior": "photo-1555396273-367ea4eb4db5",
    "barista": "photo-1532713107108-dfb5d8d2fc42",
    "shopfront": "photo-1521017432531-fbd92d768814",
    "footer": "photo-1762686852371-763b689910b2",
    "espresso": "photo-1475296204602-08d15839e95f",
    "mango": "photo-1623065422902-30a2d299bbe4",
    "tropical": "photo-1778449270554-3e5b17cfebc6",
    "strawberrysm": "photo-1579954115545-a95591f28bfc",
    "frappe": "photo-1718267050202-9b1b6bfb8545",
    "chocfrappe": "photo-1696487773677-c0c8061fe3d2",
    "cookiefrappe": "photo-1572490122747-3968b75cc699",
    "caramelfrappe": "photo-1761673930163-8d3d6d73cd7a",
    "milkshake": "photo-1553787499-6f9133860278",
    "griller": "photo-1655279562015-047c3da9a271",
    "griller2": "photo-1621852004158-f3bc188ace2d",
    "hccroissant": "photo-1530610476181-d83430b64dcd",
    "bananabread": "photo-1767065887793-f68f736ea9d6",
    "scones": "photo-1589114471223-dec0d8d572c6",
    "pies": "photo-1545668855-b923f0176935",
    "almondcroissant": "photo-1759303380903-11154bc5d5bf",
    "raisintoast": "photo-1782846105211-5543693408ce",
    "affogato": "photo-1696522692156-7340b681c3bb",
    "tea": "photo-1544787219-7f47ccb76574",
    "icedcoffee": "photo-1517701550927-30cf4ba1dba5",
    "icedmocha": "photo-1549652127-2e5e59e86a7a",
    "shortblack": "photo-1579992357154-faf4bde95b3d",
    "longblack": "photo-1510591509098-f4fdc6d0ff04",
    "hotchoc": "photo-1517578239113-b03992dcdd25",
    "whitemocha": "photo-1475759697283-38cc56e4455a",
    "piccolo": "photo-1610889556528-9a770e32642f",
    "vienna": "photo-1627777620905-53a332869051",
    "icedchai": "photo-1559496417-e7f25cb247f3",
    "icedlongblack": "photo-1578314675249-a6910f80cc4e",
    "mocha": "photo-1542990253-0d0f5be5f0ed",
    "whitechoc": "photo-1762411238451-b90dd1c74238",
    "beans": "photo-1447933601403-0c6688de566e",
    "latteart": "photo-1541167760496-1628856ab772",
    "croissantcoffee": "photo-1565252556328-92ee4a9a0983",  # coffee plantation hillside
}
def src(key, w=1200):
    v = IMG[key]
    return v if "/" in v else f"{U}{v}?auto=format&fit=crop&w={w}&q=80"

def photo(key, alt, w=1200, eager=False, cls=""):
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<div class="ph {cls}"><img src="{src(key, w)}" srcset="{src(key, w // 2)} {w // 2}w, {src(key, w)} {w}w" '
            f'sizes="(max-width: 760px) 100vw, 50vw" alt="{alt}" {load}></div>')

IG_ICON = '<svg class="ig-icon" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1.1" class="ig-dot"/></svg>'
def ig_link(text="Follow us on Instagram", cls="ig"):
    return f'<a class="{cls}" href="{BIZ["instagram"]}" target="_blank" rel="noopener">{IG_ICON}<span>{text}</span></a>'

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
<link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">
<link rel="apple-touch-icon" href="assets/img/favicon.png">
<meta property="og:image" content="{BIZ["url"]}/assets/img/logo-full.png">
<link rel="preload" href="assets/fonts/CabinetGrotesk-Medium.woff2" as="font" type="font/woff2" crossorigin>
<script>try{{var n=(performance.getEntriesByType('navigation')[0]||{{}}).type,r=document.referrer,i=n==='reload'||!r||new URL(r).origin!==location.origin;if(!i)document.documentElement.classList.add('intro-done')}}catch(e){{}}</script>
<link rel="stylesheet" href="assets/style.css?v=17">
{schema()}{extra}
</head>
<body>
<div class="intro" aria-hidden="true"><img class="intro__logo" src="assets/img/logo-wordmark.webp" alt=""></div>
'''

def nav(active):
    links = [("menu.html", "Menu"), ("about.html", "Our story"), ("faq.html", "FAQ"), ("contact.html", "Contact")]
    def a(h, t):
        cur = ' aria-current="page"' if h == active else ""
        return f'<a href="{h}"{cur}>{t}</a>'
    desktop = "".join(a(h, t) for h, t in links)
    mobile = a("index.html", "Home") + desktop
    return f'''<header class="nav">
  <div class="wrap nav__in">
    <nav class="nav__links" aria-label="Main">{desktop}</nav>
    <a class="logo" href="index.html" aria-label="{BIZ["name"]} home"><img src="assets/img/logo-wordmark.webp" alt="{BIZ["name"]}" width="190" height="33"></a>
    <div class="nav__cta"><a class="btn" href="contact.html">Visit us</a></div>
    <button class="nav__toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span></button>
  </div>
</header>
<nav class="overlay" aria-label="Mobile">{mobile}<a class="btn" href="contact.html">Visit us <span class="arrow">→</span></a>{ig_link("Instagram", "ig ig--nav")}</nav>
'''

def footer():
    return f'''<footer class="footer">
  <div class="wrap footer__top">
    <div class="footer__intro" data-reveal>
      <p class="footer__tag">A little café and patisserie at East Village in Sunbury.</p>
      <p class="status" data-open><span class="dot"></span>Open today</p>
      {ig_link()}
    </div>
    <div class="footer__col" data-reveal>
      <h4>Visit</h4>
      <p>{BIZ["street"]}, {BIZ["suburb"]} {BIZ["state"]} {BIZ["postcode"]}</p>
      <p><a href="tel:{BIZ["phone"].replace(" ", "")}">{BIZ["phone"]}</a></p>
      <p><a href="mailto:{BIZ["email"]}">{BIZ["email"]}</a></p>
    </div>
    <div class="footer__col" data-reveal>
      <h4>Explore</h4>
      <ul><li><a href="menu.html">Menu</a></li><li><a href="about.html">Our story</a></li><li><a href="faq.html">FAQ</a></li><li><a href="contact.html">Contact</a></li><li><a href="{BIZ["maps"]}">Get directions</a></li></ul>
    </div>
    <div class="footer__col footer__hours" data-reveal>
      <h4>Opening hours</h4>
      <table class="hours"><tbody>{hours_rows()}</tbody></table>
      <p class="small footer__note">Public holiday hours may vary.</p>
    </div>
  </div>
  <div class="footer__hero">
    <img class="footer__bg" src="{src("footer", 2000)}" alt="" loading="lazy" decoding="async">
    <div class="footer__word" aria-hidden="true"><span data-fit data-letters>golden sparrow</span></div>
  </div>
  <div class="wrap footer__bottom">
    <span>© <span data-year>2026</span> {BIZ["name"]}. All rights reserved.</span>
    <span class="footer__links"><a href="{BIZ["instagram"]}" target="_blank" rel="noopener">Instagram</a><a href="contact.html">Contact</a><a href="https://www.novalinkinnovations.com">Website by NovaLink</a></span>
  </div>
</footer>
<script src="assets/js/lenis.min.js"></script>
<script src="assets/main.js?v=15"></script>
</body>
</html>
'''

def card(key, name, note, tags=()):
    t = "".join(f'<span class="tag">{x}</span>' for x in tags)
    img = photo(key, f"{name} at {BIZ['name']}", 900)
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
    return f'''<section class="section visit-sec" id="visit" aria-labelledby="visit-title">
  <img class="visit__mark" src="assets/img/logo-bird.webp" alt="" aria-hidden="true">
  <div class="wrap visit3">
    <div class="visit3__info">
      <h2 class="h2" id="visit-title" data-reveal>Find us at East Village</h2>
      <p class="visit3__addr" data-reveal><a href="{BIZ["maps"]}">{BIZ["street"]}, {BIZ["suburb"]}</a></p>
      <p class="visit3__text" data-reveal>Just outside Woolies at East Village Sunbury, with free parking right outside. No booking needed.</p>
      <div class="visit3__btns" data-reveal>
        <a class="btn btn--lg" href="{BIZ["maps"]}">Get directions</a>
        <a class="link link--lg" href="contact.html">Contact and FAQ</a>
      </div>
    </div>
    <div class="visit3__hours" data-reveal>
      <p class="visit3__label">Opening hours</p>
      <table class="hours hours--lg"><tbody>{hours_rows()}</tbody></table>
    </div>
    <div class="visit3__img" data-reveal="img">{photo("cakedisplay", "Cakes and sweets in the display cabinet at Golden Sparrow", 900, cls="par")}</div>
  </div>
</section>'''

MARQ = "".join(f'<span>{t}</span><img src="assets/img/logo-bird.webp" alt="">' for t in ['Freshly brewed coffee', 'Golden churros', 'Raffaello hot chocolate', 'Smoothies', 'Frappes', 'Milkshakes', 'Grillers', 'Sparrow fries', 'Soft serve sundaes', 'Bakery favourites'])

def gallery():
    items = [("latteart", "Latte art, poured by hand"), ("espresso", "Espresso, pulled fresh"), ("croissantcoffee", "Coffee &amp; something sweet"), ("beans", "Locally roasted beans"), ("macarons", "Little treats from the cabinet")]
    cards = "".join(f'''<figure class="gal__item" data-reveal>{photo(k, cap.replace("&amp;", "and"), 900, cls="par")}<figcaption>{cap}</figcaption></figure>''' for k, cap in items)
    return f'''<section class="section gal" aria-labelledby="gal-title">
  <div class="wrap head3">
    <h2 class="h2" id="gal-title" data-reveal>From our counter</h2>
    <div class="head3__side"><p class="body" data-reveal>The smell of fresh coffee, the hiss of the milk and a cabinet full of sweets. Drag to look around.</p><p data-reveal>{ig_link("See more on Instagram", "ig ig--link")}</p></div>
  </div>
  <div class="gal__track" data-stagger=".08">{cards}</div>
</section>'''

# ------------------------------------------------------------------ HOME
home = head(f'{BIZ["name"]} · Café & patisserie in East Village, Sunbury',
            f'{BIZ["name"]} is a local café and patisserie at East Village, Sunbury. Coffee, cakes, golden churros, sandwiches and soft serve. Walk in, no booking needed.',
            "") + nav("index.html") + f'''<main>
<section class="hero" aria-labelledby="hero-title">
  <div class="wrap">
    <h1 class="sr-only" id="hero-title">{BIZ["name"]}, café and patisserie in Sunbury</h1>
    <div class="hero__grid">
      <p class="display hero__left from-left" aria-hidden="true"><span class="line"><span>A little</span></span><span class="line"><span>sweetness</span></span></p>
      <div class="hero__img"><div class="ph"><video class="hero__video" autoplay muted loop playsinline preload="auto" poster="{src("hero", 900)}" data-loop-start="0.3" data-loop-end="7.0" aria-label="Espresso pouring from the coffee machine at Golden Sparrow Patisserie">
          <source src="https://videos.pexels.com/video-files/30284611/12981829_720_1680_24fps.mp4" type="video/mp4"></video></div></div>
      <p class="display hero__right from-right" aria-hidden="true"><span class="line"><span>for every</span></span><span class="line"><span class="gold">occasion</span></span></p>
    </div>
    <div class="hero__bottom">
      <div><p class="eyebrow" style="margin-bottom:12px">Café &amp; Patisserie · East Village, Sunbury</p>
      <p class="lead">Freshly brewed coffee, cakes, golden churros and a warm welcome. Pull up a chair or take something sweet to go.</p></div>
      <div class="pill" data-open><span class="dot"></span>Open today</div>
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee__track">{MARQ}{MARQ}</div></div>

<section class="section" style="overflow:hidden" aria-labelledby="intro-title">
  <img class="watermark" src="assets/img/logo-bird.webp" alt="" aria-hidden="true">
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
    <div class="head3">
      <h2 class="h2" id="start-title" data-reveal>Where to start</h2>
      <div class="head3__side" data-stagger=".08">
        <p class="body" data-reveal>Four signature drinks we would pour for you on a first visit. Sip something special and indulge in every sip.</p>
        <p data-reveal><a class="link" href="menu.html">See the full menu</a></p>
      </div>
    </div>
    <div class="cards" data-stagger=".1">
      {card("matcha", "Matcha Latte", "Smooth, creamy and beautifully green. A calm little moment in a cup.")}
      {card("raffaello", "Raffaello Hot Chocolate", "Creamy white chocolate, coconut and almond. Pure indulgence.")}
      {card("icedchoc", "Iced Chocolate", "Rich chocolate over ice, finished with cream. A sweet treat any time of day.")}
      {card("cappuccino", "Cappuccino", "Velvety foam and a dusting of chocolate, made just the way you like it.")}
    </div>
  </div>
</section>


<section class="vid" aria-label="Espresso being made">
  <div class="vid__frame">
    <video class="vid__video" muted loop playsinline preload="metadata" poster="{src("espresso", 1600)}"
      data-src-lg="https://videos.pexels.com/video-files/7457398/7457398-hd_1920_1080_30fps.mp4"
      data-src-sm="https://videos.pexels.com/video-files/7457398/7457398-hd_1280_720_30fps.mp4"></video>
    <div class="vid__overlay">
      <p class="eyebrow">Pulled fresh, every morning</p>
      <h2 class="h2">Every cup, made with care</h2>
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
      <div data-reveal="img">{photo("interior", "Warm café interior with wooden tables", 1600, cls="par")}</div>
      <div data-reveal="img" style="--d:.12s">{photo("cakedisplay", "Cakes and tarts in the display cabinet", 900, cls="par")}</div>
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
    <div class="cards cards--3" data-stagger=".1">
      {card("churroscoffee", "Golden churros", "Crisp, golden and dusted with sugar. Our sweet signature, best with a coffee.")}
      {card("cake", "Cakes for every occasion", "Birthdays, celebrations or just because. Ask us about special occasion cakes.")}
      {card("pastries", "Catering &amp; platters", "Customised platters for groups, events and the office.")}
    </div>
  </div>
</section>

{gallery()}

{visit_section()}
</main>
''' + footer()

# ------------------------------------------------------------------ MENU
# NOTE: sample items until Vani's menu PDF arrives — replace with the real menu. No prices (client request).
# Real menu from Golden Sparrow Patisserie (Nov 2026). No prices on the website (client request).
menu_cats = [
    ("hot", "Hot drinks", "Made fresh to order, just the way you like it.", [
        ("cappuccino", "Cappuccino", "Velvety foam with a dusting of chocolate.", ["Coffee"]),
        ("latte", "Caffè Latte", "Smooth espresso with creamy steamed milk.", ["Coffee"]),
        ("flatwhite", "Flat White", "Silky milk over a double shot.", ["Coffee"]),
        ("longblack", "Long Black", "Espresso over hot water. Bold and clean.", ["Coffee"]),
        ("shortblack", "Short Black", "A short, rich shot of espresso.", ["Coffee"]),
        ("mocha", "Mocha", "Espresso, chocolate and steamed milk.", ["Coffee", "Chocolate"]),
        ("hotchoc", "Hot Chocolate", "Rich, creamy and comforting.", ["Chocolate"]),
        ("chai", "Chai Latte", "Warm spices and steamed milk.", ["Spiced"]),
        ("affogato", "Affogato", "Vanilla ice cream drowned in a shot of espresso.", ["Coffee", "Sweet treat"]),
        ("vienna", "Vienna", "Espresso topped with whipped cream.", ["Coffee"]),
        ("piccolo", "Piccolo", "A ristretto shot with a little silky milk.", ["Coffee"]),
        ("shortblack", "Short Macchiato", "Espresso marked with a touch of milk foam.", ["Coffee"]),
        ("piccolo", "Long Macchiato", "A double shot marked with milk foam.", ["Coffee"]),
        ("tea", "Tea", "A selection of flavours.", ["Tea"]),
    ]),
    ("signature", "Signature drinks", "Our house favourites. Sip something special and indulge in every sip.", [
        ("whitemocha", "White Mocha", "Espresso with creamy white chocolate.", ["Signature", "Coffee"]),
        ("whitechoc", "White Chocolate", "Velvety white chocolate and steamed milk.", ["Signature"]),
        ("raffaello", "Raffaello Hot Chocolate", "White chocolate, coconut and almond. Pure indulgence.", ["Signature"]),
        ("matcha", "Matcha", "Creamy, calming and beautifully green.", ["Signature"]),
        ("chai", "Dirty Chai", "Spiced chai with a shot of espresso.", ["Signature", "Coffee"]),
    ]),
    ("cold", "Cold drinks", "Poured over ice, made to order. Perfect for warm Sunbury afternoons.", [
        ("icedcoffee", "Iced Coffee", "Chilled coffee over ice.", ["Iced", "Coffee"]),
        ("icedchoc", "Iced Chocolate", "Rich chocolate over ice, finished with cream.", ["Iced", "Chocolate"]),
        ("icedchai", "Iced Chai", "Spiced chai over ice.", ["Iced"]),
        ("icedlatte", "Iced Latte", "Espresso over ice with cold milk.", ["Iced", "Coffee"]),
        ("icedmocha", "Iced Mocha", "Espresso, chocolate and milk over ice.", ["Iced", "Coffee"]),
        ("icedmatcha", "Iced Matcha", "Matcha and milk over ice.", ["Iced"]),
        ("icedlongblack", "Iced Long Black", "Espresso over ice and cold water.", ["Iced", "Coffee"]),
    ]),
    ("smoothies", "Smoothies", "Blended to order with fruit, milk and ice cream.", [
        ("mango", "Mango Paradise", "Mango, coconut, milk and ice cream.", ["Fruity"]),
        ("tropical", "Tropical Sunset", "Mango, passionfruit, milk and ice cream.", ["Fruity"]),
        ("strawberrysm", "Strawberry Bliss", "Strawberry, banana, milk and ice cream.", ["Fruity"]),
    ]),
    ("frappes", "Frappes", "Icy, creamy and blended until smooth.", [
        ("frappe", "Latte Dream", "A creamy blended coffee frappe.", ["Coffee", "Blended"]),
        ("chocfrappe", "Choco Delight", "Blended chocolate, rich and frosty.", ["Chocolate", "Blended"]),
        ("strawberrysm", "Strawberry Velvet", "Sweet strawberry, blended smooth.", ["Fruity", "Blended"]),
        ("cookiefrappe", "Cookies and Cream", "Crushed cookies blended with cream.", ["Blended"]),
        ("caramelfrappe", "Caramel Crush", "Golden caramel, blended and icy.", ["Blended"]),
        ("caramelfrappe", "Salted Caramel", "Sweet and salty caramel, blended smooth.", ["Blended"]),
    ]),
    ("milkshakes", "Milkshakes", "Classic shakes in your favourite flavour.", [
        ("milkshake", "Milkshake", "Vanilla, caramel, strawberry, chocolate, blue heaven, banana, coffee or lime.", ["Classic"]),
    ], [("Add malt", "Available"), ("Extra flavour", "Available"), ("Make it a thick shake", "Available")]),
    ("toasties", "Toasties &amp; bakery", "Freshly made, every day. Toasties available on white or wholemeal bread.", [
        ("sandwich", "Ham &amp; Cheese Toastie", "Ham and melted cheese, toasted golden.", ["Toasted"]),
        ("griller2", "Ham, Cheese &amp; Tomato Toastie", "Ham, cheese and tomato, toasted golden.", ["Toasted"]),
        ("sandwich", "Cheese Toastie", "Simple, melty and golden.", ["Toasted"]),
        ("hccroissant", "Ham &amp; Cheese Croissant", "A buttery croissant filled with ham and cheese.", ["Bakery"]),
    ]),
    ("grillers", "Grillers", "Hearty fillings with melted tasty cheese in a toasted Turkish roll.", [
        ("griller", "Chipotle Chicken Griller", "Diced chicken marinated in southwest chipotle sauce, with avocado spread and melted tasty cheese in a Turkish roll.", ["Turkish roll"]),
        ("griller2", "Turkey Cranberry Griller", "Sliced turkey with honey mustard and cranberry sauce, with melted tasty cheese in a Turkish roll.", ["Turkish roll"]),
        ("griller", "Pulled Beef Griller", "Pulled beef with caramelised onion sauce, southwest chipotle sauce and melted tasty cheese in a Turkish roll.", ["Turkish roll"]),
    ]),
    ("churros", "Golden churros", "Our sweet signature. Crisp, golden and made to be shared.", [
        ("churroscoffee", "Churros &amp; dip", "3 churros + 1 dip, 4 churros + 1 dip, 6 churros + 2 dips or 9 churros + 2 dips.", ["Signature", "Great to share"]),
        ("churroscoffee", "Golden Churro Basket", "A basket of golden churros, served with vanilla ice cream.", ["Great to share"]),
    ], [("Dipping sauces", "Milk chocolate · White chocolate · Strawberry cream"), ("Add a little extra", "Biscoff or Nutella")]),
    ("fries", "Sparrow fries", "Crispy, golden and seasoned your way.", [
        ("fries", "Sparrow Fries", "Regular or large.", ["Great to share"]),
    ], [("Season with", "Herb salt · Chicken salt · Sea salt"), ("Add a sauce", "Available")]),
    ("softserve", "Soft serve", "A cool and creamy treat.", [
        ("softserve", "Classic Vanilla Cone", "Creamy vanilla soft serve in a cone.", ["Sweet treat"]),
        ("sundae", "Sundae", "Choose from chocolate, caramel, strawberry or Biscoff.", ["Sweet treat"]),
    ]),
    ("bakery", "Bakery favourites", "From our cabinet, baked and ready to enjoy.", [
        ("pies", "Pies &amp; savouries", "A selection of pies and savouries.", ["Savoury"]),
        ("bananabread", "Banana Bread", "A café classic.", ["Sweet"]),
        ("raisintoast", "Raisin Toast", "A café favourite.", ["Sweet"]),
        ("scones", "Scones", "Freshly baked scones.", ["Sweet"]),
        ("almondcroissant", "Almond Croissant", "Flaky and filled with almond cream.", ["Sweet", "Contains nuts"]),
    ]),
]
good_to_know = [("Takeaway", "Everything on the menu"), ("Dietary requirements", "Just ask, we have options"),
                ("Celebration cakes", "Order ahead"), ("Catering platters", "Customised for groups"),
                ("Bookings", "Not needed, walk in")]

def mitem(key, name, note, tags):
    t = "".join(f'<span class="tag">{x}</span>' for x in tags)
    return f'''<article class="mi" data-reveal>
  <div class="mi__img">{photo(key, f"{name} at {BIZ['name']}", 300)}</div>
  <div class="mi__copy">
    <h3 class="mi__name">{name}</h3>
    <p class="mi__note">{note}</p>
    <div class="mi__tags">{t}</div>
  </div>
</article>'''

MENU_GROUPS = [("all", "All"), ("hot", "Hot drinks"), ("cold", "Iced &amp; cold"), ("shakes", "Smoothies &amp; shakes"),
               ("food", "Food"), ("sweet", "Sweets &amp; bakery")]
CAT_GROUP = {"hot": "hot", "signature": "hot", "cold": "cold", "smoothies": "shakes", "frappes": "shakes",
             "milkshakes": "shakes", "toasties": "food", "grillers": "food", "fries": "food",
             "churros": "sweet", "softserve": "sweet", "bakery": "sweet"}
chips = "".join(f'<button type="button" class="mf__chip{" is-active" if k == "all" else ""}" data-group="{k}" aria-pressed="{"true" if k == "all" else "false"}">{t}</button>' for k, t in MENU_GROUPS)
menu_filter = f'''<div class="mf" role="search">
  <div class="wrap mf__inner">
    <label class="mf__search">
      <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <span class="sr-only">Search the menu</span>
      <input type="search" id="menu-search" placeholder="Search, e.g. matcha, churros, chicken" autocomplete="off">
      <button type="button" class="mf__clear" aria-label="Clear search" hidden>&times;</button>
    </label>
    <div class="mf__chips" role="group" aria-label="Filter by category">{chips}</div>
  </div>
</div>
<p class="mf__empty wrap" hidden>No matches. Try another word, or just ask our team, we're happy to help.</p>'''

menu_html = ""
for cat in menu_cats:
    key, title, sub, items = cat[:4]
    extras = cat[4] if len(cat) > 4 else []
    extra_html = ('<div class="kvlist kvlist--extras">' + "".join(f'<div class="kv"><span>{k}</span><span>{v}</span></div>' for k, v in extras) + '</div>') if extras else ""
    menu_html += f'''<section class="mcat" id="{key}" data-group="{CAT_GROUP[key]}" aria-labelledby="{key}-h">
  <div class="wrap mcat__grid">
    <div class="mcat__left">
      <h2 class="mcat__title" id="{key}-h" data-reveal>{title}</h2>
      <p class="mcat__text" data-reveal>{sub}</p>
    </div>
    <div class="mcat__list">{"".join(mitem(*i) for i in items)}{extra_html}</div>
  </div>
</section>'''
gtk_rows = "".join(f'<div class="kv" data-reveal><span>{k}</span><span>{v}</span></div>' for k, v in good_to_know)
menu_html += f'''<section class="mcat mcat--info" id="good-to-know" aria-labelledby="gtk-h">
  <div class="wrap mcat__grid">
    <div class="mcat__left">
      <h2 class="mcat__title" id="gtk-h" data-reveal>Good to know</h2>
      <p class="mcat__text" data-reveal>A few things our regulars ask about.</p>
    </div>
    <div class="mcat__list">
      <div class="kvlist">{gtk_rows}</div>
      <p class="notice" data-reveal>Allergy notice: please let our team know about any allergies before ordering. Our kitchen handles common allergens.</p>
    </div>
  </div>
</section>'''

menu = head(f'Menu · {BIZ["name"]}, Sunbury',
            f'The {BIZ["name"]} menu: coffee, signature drinks, iced drinks, smoothies, frappes, milkshakes, toasties, grillers, golden churros, Sparrow fries, soft serve and bakery favourites.',
            "menu.html") + nav("menu.html") + f'''<main>
<section class="mhead">
  <div class="wrap mhead__grid">
    <div>
      <h1 class="mhead__title" data-reveal>The menu</h1>
      <p class="mhead__intro" data-reveal>Coffee, sweet treats and something for every appetite. We cater for a range of dietary requirements, so just ask our team, we're happy to help.</p>
    </div>
    <div class="mhead__img" data-reveal="img">{photo("cappuccino", "Cappuccino at Golden Sparrow Patisserie", 700)}</div>
  </div>
</section>
{menu_filter}
{menu_html}
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
      <div data-reveal="img">{photo("barista", "Barista pouring latte art", 900, cls="par")}</div>
      <div data-reveal="img" style="--d:.12s">{photo("pastries", "Pastries in the display case", 900, cls="par")}</div>
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


# ------------------------------------------------------------------ CONTACT
contact = head(f'Contact · {BIZ["name"]}, Sunbury',
               f'Contact {BIZ["name"]} at East Village, Sunbury. Call {BIZ["phone"]}, email us, or send an enquiry about catering, platters and special occasion cakes.',
               "contact.html") + nav("contact.html") + f'''<main>
<section class="page-head">
  <div class="wrap">
    <h1 class="h1" data-reveal>Get in touch</h1>
    <p class="lead" data-reveal>Questions, catering platters or a cake for a special occasion? Send us a message and we'll get back to you.</p>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap contact">
    <form class="contact__form" action="contact.php" method="post" data-reveal novalidate>
      <div class="form__msg" role="status" aria-live="polite" hidden></div>
      <div class="field"><label for="name">Your name</label><input id="name" name="name" type="text" autocomplete="name" required></div>
      <div class="field-row">
        <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="phone">Phone <span>(optional)</span></label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
      </div>
      <div class="field-row">
        <div class="field"><label for="topic">What's it about?</label>
          <select id="topic" name="topic"><option>General enquiry</option><option>Catering &amp; platters</option><option>Special occasion cake</option><option>Feedback</option></select></div>
        <div class="field"><label for="date">Date needed <span>(optional)</span></label><input id="date" name="date" type="date"></div>
      </div>
      <div class="field"><label for="message">Message</label><textarea id="message" name="message" rows="6" required></textarea></div>
      <div class="hp" aria-hidden="true"><label for="website">Website</label><input id="website" name="website" type="text" tabindex="-1" autocomplete="off"></div>
      <button class="btn btn--gold" type="submit">Send message <span class="arrow">→</span></button>
    </form>

    <aside class="contact__info" data-stagger=".08">
      <div data-reveal><h2 class="eyebrow">Visit</h2><p>{ADDR}</p><p class="small" style="color:var(--muted-2)">Just outside Woolies. Free parking.</p></div>
      <div data-reveal><h2 class="eyebrow">Call</h2><p><a href="tel:{BIZ["phone"].replace(" ", "")}">{BIZ["phone"]}</a></p></div>
      <div data-reveal><h2 class="eyebrow">Email</h2><p><a href="mailto:{BIZ["email"]}">{BIZ["email"]}</a></p></div>
      <div data-reveal><h2 class="eyebrow">Follow us</h2><p>{ig_link("Golden Sparrow on Instagram")}</p><p class="small" style="color:var(--muted-2);margin-top:6px">New treats, specials and behind the counter.</p></div>
      <div data-reveal><h2 class="eyebrow">Opening hours</h2><table class="hours"><tbody>{hours_rows()}</tbody></table><p class="small" style="color:var(--muted-2);margin-top:10px">Public holiday hours may vary.</p></div>
    </aside>
  </div>
</section>

<section class="wrap" style="padding-bottom:clamp(72px,10vw,140px)">
  <div class="map map--wide" data-reveal="img"><iframe title="Map to {BIZ["name"]}" src="https://www.google.com/maps?q=East+Village+Sunbury+VIC+3429&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</section>
</main>
''' + footer()

for name, html in [("index.html", home), ("menu.html", menu), ("about.html", about), ("faq.html", faq), ("contact.html", contact)]:
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
print("built")
