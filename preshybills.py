"""
Birthday Website Generator — Elegant Edition 🌷
================================================
Run:   python generate_birthday.py
Open:  birthday.html  in your browser

Edit the CONFIG block below — that's all you need!
"""

# ════════════════════════════════════════════════════════════
#  C O N F I G   —   edit everything here
# ════════════════════════════════════════════════════════════

CONFIG = {
    # ── Core
    "name": "madam p",
    "from": "Your SUPE HUMAN — Dojo",
    "tagline": "a celebration of my favourite human",
  
  




    # ── Hero text
    "hero_poem": [
        "Some people come into your life",
        "and just make everything a little bit better —",
        "the laughs louder, the hard days shorter,",
        "the ordinary ones worth remembering.",
        "You are absolutely that person.",
        "No feel yourself too much",
    ],

    # ── Music
    # Local file → put your .mp3 in the same folder and use:  "song.mp3"
    # Remote URL → direct .mp3 link (Dropbox: change ?dl=0 to ?raw=1)
    "music_url": "song.mp3",
    "music_title": "Play Song",

    # ── Memory chapters
    # layout: "left" | "right" | "center" 
    #
    # HOW TO ADD PHOTOS & VIDEOS:
    #   Local file  → put the file in a "photos/" folder next to this script,
    #                 then use:  "photos/filename.jpg"  or  "photos/clip.mp4"
    #   Remote URL  → paste a direct link:  "https://..."
    #   Leave blank → ""  shows a placeholder
    #
    # Supported image types: .jpg  .jpeg  .png  .gif  .webp  .avif
    # Supported video types: .mp4  .webm  .mov  .ogg  .m4v
    # Mix and match freely within the same chapter!
    #
    # TIP: keep videos short (5–20 sec loops work beautifully)
    "chapters": [
        {
            "title":    "The Beginning",
            "subtitle": "Where it all started",
            "quote":   "I knew pretty quickly that you were going to be one of those people I'd want around forever, (Maybe until your bad character does us apart (⁠•⁠‿⁠•⁠)""you are actually not cool for jamming ozeba during a scary movie",
            "caption":  "The origin story. Chaotic, probably. Perfect, definitely.",
            "photos":   ["pics/ones.jpg","pics/3d.mp4","pics/me80.mp4"],
            "layout":   "right",
        },
        {
            "title":    "The Adventures",
            "subtitle": "Miles covered, memories made",
            "quote":    "Every plan we've made has either gone perfectly or gone hilariously  wrong. But a swell time it is with you always.",
            "caption":  "Zero regrets. Many stories. A few we probably shouldn't repeat(like me always comin late ).",
            "photos":   ["pics/ad12.mp4", "pics/ade2.jpg", "pics/ade3.mp4"],
            "layout":   "left",
        },
        {
            "title":    "contagious",
            "subtitle": "the word for what your smile is ",
            "quote":    " there is this word-ambedo-,for that fleeting awareness that a moment is worth remebering,your smile is that.",
            "caption":  "photographic evidence attached, elonmother(stil confused why you think it is weird).",
            "photos":   ["pics/eeh.jpg", "pics/smile3.jpg"],
            "layout":   "center",
        },
        {
            "title":    "The Celebrations",
            "subtitle": "Every laugh, every cheer",
            "quote":    "thanks  for cheering me on  the way you do, Nobody celebrates people the way you do — and today it's your turn to be celebrated right back.",
            "caption":  "The moments so good they deserve to be written down.",
            "photos":   ["pics/cele2.mp4", "pics/smile.jpg", "pics/cele90.jpg"],
            "layout":   "right",
        }, 
        {
            "title":    "mini gallery",
            "subtitle": "funny moments i wanna display",
            "quote":    " ",
            "caption":  " you lil weirdo.",
            "photos":   ["pics/al1.mp4", "pics/al2.jpg", "pics/AL3.jpg" ,"pics/al4.jpg","pics/al5.jpg","pics/al6.mp4"],
            "layout":   "center",
        },
        {
            "title":    "Right Now",
            "subtitle": "This birthday, this year",
            "quote":    "You are doing better than you think, going further than you know, and I am cheering loudly the whole way. i hope beautiful things happen to you ",
             "caption":  "Here is to you — exactly as you are, right now, today.",
            "photos":   ["pics/now1.jpg", "pics/now2.jpg"],
            "layout":   "center",
        },
    ],

    # ── Final letter
    "letter_lines": [
        " belinda,funmi🦂, docp,prshybillz24,ransomkuti",
        "so many names to call you",
        "",
        "",
        "",
        "Right, here is the thing.",
        "",
        "You are one of those rare people who makes everyone (me) around them",
        "feel like things are going to be okay.",
        "Not because you pretend everything is fine,",
        "but because you actually show up — for the big stuff and the small stuff",
        "and all the in-between stuff that nobody else notices.",
        "",
        "I notice. I always notice.",
        "",
        "I am so glad you exist, and even more glad",
        "that somewhere along the way you decided to be my person.",
        "Lucky doesn't quite cover it.",
        "",
        "Happy birthday Baby. This year is going to be a good one.",
        "I'd bet on it.  i hope This makes you happy  .",
    ],

    "output_file": "birthday.html",
}


# ════════════════════════════════════════════════════════════
#  T U L I P   G A R D E N   (pure SVG + CSS animations)
# ════════════════════════════════════════════════════════════

def single_tulip(x, delay, scale=1.0, flip=False):
    """Returns SVG markup for one white tulip with staggered bloom animation."""
    sx = -scale if flip else scale
    d  = delay
    return f"""
    <g transform="translate({x},0) scale({sx},{scale})">
      <!-- stem -->
      <line x1="0" y1="0" x2="0" y2="-240"
        stroke="#d0e8a8" stroke-width="4" stroke-linecap="round"
        style="animation:stemGrow 1.8s {d:.2f}s cubic-bezier(.4,0,.2,1) both;transform-origin:0px 0px"/>
      <!-- broad leaf L -->
      <path d="M0,-120 Q-50,-155 -22,-195" fill="none"
        stroke="#b8d890" stroke-width="3.5" stroke-linecap="round"
        style="animation:leafOut 1s {d+0.9:.2f}s ease both;transform-origin:0px -120px"/>
      <!-- broad leaf R -->
      <path d="M0,-88 Q46,-125 20,-162" fill="none"
        stroke="#b8d890" stroke-width="3.5" stroke-linecap="round"
        style="animation:leafOut 1s {d+1.1:.2f}s ease both;transform-origin:0px -88px"/>
      <!-- outer petal L — wide cup shape -->
      <path d="M0,-242 Q-44,-298 -28,-358 Q-6,-308 0,-278"
        fill="rgba(255,255,255,0.88)" stroke="rgba(255,255,255,0.4)" stroke-width="1"
        style="animation:petalOpen 1.3s {d+1.4:.2f}s cubic-bezier(.34,1.3,.64,1) both;transform-origin:0px -242px"/>
      <!-- outer petal R -->
      <path d="M0,-242 Q44,-298 28,-358 Q6,-308 0,-278"
        fill="rgba(255,255,255,0.88)" stroke="rgba(255,255,255,0.4)" stroke-width="1"
        style="animation:petalOpen 1.3s {d+1.6:.2f}s cubic-bezier(.34,1.3,.64,1) both;transform-origin:0px -242px"/>
      <!-- inner petal L -->
      <path d="M0,-245 Q-22,-292 -12,-345 Q-2,-305 0,-280"
        fill="rgba(255,255,255,0.96)" stroke="rgba(230,240,255,0.3)" stroke-width="0.5"
        style="animation:petalOpen 1.1s {d+1.8:.2f}s cubic-bezier(.34,1.3,.64,1) both;transform-origin:0px -245px"/>
      <!-- inner petal R -->
      <path d="M0,-245 Q22,-292 12,-345 Q2,-305 0,-280"
        fill="rgba(255,255,255,0.96)" stroke="rgba(230,240,255,0.3)" stroke-width="0.5"
        style="animation:petalOpen 1.1s {d+2.0:.2f}s cubic-bezier(.34,1.3,.64,1) both;transform-origin:0px -245px"/>
      <!-- centre petal -->
      <path d="M-4,-248 Q0,-310 0,-355 Q0,-310 4,-248"
        fill="white"
        style="animation:petalOpen 0.9s {d+2.2:.2f}s ease both;transform-origin:0px -248px"/>
      <!-- stamen glow -->
      <ellipse cx="0" cy="-332" rx="5" ry="7"
        fill="rgba(255,248,180,0.85)"
        style="animation:stamenPop 0.5s {d+2.6:.2f}s ease both"/>
      <ellipse cx="0" cy="-332" rx="10" ry="12"
        fill="rgba(255,248,180,0.15)"
        style="animation:stamenPop 0.5s {d+2.6:.2f}s ease both"/>
    </g>"""


def tulip_garden():
    """Arrange a lush visible field of tulips across the hero bottom."""
    # (x, bloom_delay, scale, flip)  — denser, larger, no tiny outliers
    specs = [
        # back row — slightly smaller
        (-520, 0.2,  0.62, False),
        (-400, 0.5,  0.70, True),
        (-280, 0.8,  0.66, False),
        (-160, 0.3,  0.74, True),
        ( -55, 1.0,  0.70, False),
        (  55, 0.6,  0.72, True),
        ( 160, 0.1,  0.75, False),
        ( 280, 0.9,  0.67, True),
        ( 400, 0.4,  0.71, False),
        ( 520, 0.7,  0.63, True),
        # front row — full size, bloom later
        (-460, 1.2,  0.82, True),
        (-340, 1.5,  0.90, False),
        (-210, 1.3,  0.86, True),
        ( -95, 1.6,  0.94, False),
        (   0, 2.0,  1.00, False),  # hero centrepiece — tallest, last
        (  95, 1.4,  0.95, True),
        ( 210, 1.7,  0.87, False),
        ( 340, 1.1,  0.91, True),
        ( 460, 1.8,  0.83, False),
    ]
    tulips = "".join(single_tulip(x, d, s, f) for x, d, s, f in specs)

    return f"""<svg id="tulip-svg"
  viewBox="-600 -390 1200 390"
  preserveAspectRatio="xMidYMax meet"
  xmlns="http://www.w3.org/2000/svg"
  aria-hidden="true">
  <defs>
    <radialGradient id="gg" cx="50%" cy="100%" r="60%">
      <stop offset="0%" stop-color="rgba(255,255,255,0.12)"/>
      <stop offset="100%" stop-color="rgba(255,255,255,0)"/>
    </radialGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="softglow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="8" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <!-- ground shimmer -->
  <ellipse cx="0" cy="-4" rx="590" ry="22" fill="url(#gg)"/>
  <!-- back row slightly dimmer -->
  <g filter="url(#glow)" opacity="0.75">
    {"".join(single_tulip(x, d, s, f) for x, d, s, f in specs[:10])}
  </g>
  <!-- front row bright -->
  <g filter="url(#softglow)">
    {"".join(single_tulip(x, d, s, f) for x, d, s, f in specs[10:])}
  </g>
</svg>"""


# ════════════════════════════════════════════════════════════
#  H T M L   B U I L D E R S
# ════════════════════════════════════════════════════════════

VIDEO_EXTS = (".mp4", ".webm", ".mov", ".ogg", ".m4v")
IMAGE_EXTS = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif")

def is_video(url):
    return any(url.lower().split("?")[0].endswith(ext) for ext in VIDEO_EXTS)

def is_image(url):
    return any(url.lower().split("?")[0].endswith(ext) for ext in IMAGE_EXTS)

def build_photo(url, alt):
    """
    Accepts:
      - Local file path:  "photos/memory.jpg"  or  "photos/clip.mp4"
      - Remote URL:       "https://..."
      - Leave empty ""   to show a placeholder
    """
    if not url:
        # empty string → placeholder
        return """<div class="ph-slot">
      <svg viewBox="0 0 24 24"><path d="M21 19V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5z"/></svg>
      <span>Add your photo or video here</span>
    </div>"""

    if is_video(url):
        # work out MIME type for the <source> tag
        ext = url.lower().split("?")[0].rsplit(".", 1)[-1]
        mime = {"mp4": "video/mp4", "webm": "video/webm", "mov": "video/mp4",
                "ogg": "video/ogg", "m4v": "video/mp4"}.get(ext, "video/mp4")
        return f"""<video autoplay muted loop playsinline>
      <source src="{url}" type="{mime}"/>
    </video>"""

    # image (local or remote)
    return f'<img src="{url}" alt="{alt}" loading="lazy"/>'


def build_chapter(i, ch):
    layout = ch.get("layout", "right" if i % 2 == 0 else "left")
    photos = ch.get("photos", [])

    def slot(p):
        badge = '<span class="video-badge">▶ video</span>' if p and is_video(p) else ""
        return f'<div class="photo-slot">{build_photo(p, ch["title"])}{badge}</div>'

    photo_els = "".join(slot(p) for p in photos)
    text = f"""<div class="chapter-text">
      <span class="ch-number">0{i+1}</span>
      <h2 class="ch-title">{ch['title']}</h2>
      <p class="ch-subtitle">{ch['subtitle']}</p>
      <div class="ch-divider"><span></span><i>✦</i><span></span></div>
      <blockquote class="ch-quote">{ch['quote']}</blockquote>
      <p class="ch-caption">{ch['caption']}</p>
    </div>"""

    if layout == "center":
        inner = f'{text}<div class="photos-center">{photo_els}</div>'
        cls = "chapter-inner center-layout"
    elif layout == "right":
        inner = f'{text}<div class="photos-stack right-stack">{photo_els}</div>'
        cls = "chapter-inner"
    else:
        inner = f'<div class="photos-stack left-stack">{photo_els}</div>{text}'
        cls = "chapter-inner"

    return f"""
  <section class="chapter reveal" id="chapter-{i+1}">
    <div class="chapter-tag">Chapter {i+1}</div>
    <div class="{cls}">{inner}</div>
  </section>"""


def build_letter(lines, from_name):
    paras, buf = [], []
    for line in lines:
        if line == "":
            if buf:
                paras.append(f'<p>{"<br/>".join(buf)}</p>')
                buf = []
        else:
            buf.append(line)
    if buf:
        paras.append(f'<p>{"<br/>".join(buf)}</p>')
    return "\n".join(paras) + f'\n<p class="letter-sig">— {from_name}</p>'


def build_nav(chapters):
    items = "".join(
        f'<a href="#chapter-{i+1}" class="nav-dot" title="{ch["title"]}"><span></span></a>'
        for i, ch in enumerate(chapters)
    )
    return f'<nav id="chapter-nav">{items}</nav>'


# ════════════════════════════════════════════════════════════
#  M A I N   G E N E R A T O R
# ════════════════════════════════════════════════════════════

def generate(cfg):
    for i, ch in enumerate(cfg["chapters"]):
     print(i, ch.keys())
    chapters_html = "\n".join(build_chapter(i, ch) for i, ch in enumerate(cfg["chapters"]))
    letter_html   = build_letter(cfg["letter_lines"], cfg["from"])
    nav_html      = build_nav(cfg["chapters"])
    hero_lines    = "".join(f"<span>{l}</span><br/>" for l in cfg["hero_poem"])
    tulips        = tulip_garden()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Happy Birthday · {cfg['name']}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=EB+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Cinzel:wght@400;500&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --ink:#0c0a0b; --paper:#faf6f0; --cream:#f2ead8;
  --gold:#b8892a; --gold2:#d4a94a; --gold3:#eddcaa;
  --rose:#7a2535; --blush:#e8cdd3; --mist:#c8bfb0;
  --dark:#1a1108; --shadow:rgba(26,17,8,0.18);
}}
html{{scroll-behavior:smooth}}
body{{background:var(--paper);color:var(--ink);font-family:'EB Garamond',serif;overflow-x:hidden}}

/* grain overlay */
body::before{{content:'';position:fixed;inset:0;pointer-events:none;z-index:1000;opacity:0.4;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E")}}

/* cursor */
.cursor{{width:8px;height:8px;background:var(--gold);border-radius:50%;position:fixed;pointer-events:none;z-index:9999;mix-blend-mode:multiply}}
.cursor-ring{{width:32px;height:32px;border:1px solid var(--gold);border-radius:50%;position:fixed;pointer-events:none;z-index:9998;opacity:0.5}}

/* progress */
#progress{{position:fixed;top:0;left:0;height:2px;background:linear-gradient(90deg,var(--rose),var(--gold),var(--gold2));z-index:600;width:0%}}

/* music */
#player{{position:fixed;top:2rem;right:2rem;z-index:500;display:flex;align-items:center;gap:0.6rem;
  background:rgba(250,246,240,0.9);border:1px solid var(--gold);padding:0.55rem 1.1rem;
  border-radius:40px;backdrop-filter:blur(8px);cursor:pointer;
  box-shadow:0 2px 20px var(--shadow);transition:background 0.3s}}
#player:hover{{background:rgba(242,234,216,0.97)}}
#pi{{width:16px;height:16px;fill:var(--gold)}}
#pl{{font-family:'Cinzel',serif;font-size:0.6rem;letter-spacing:0.18em;color:var(--gold);text-transform:uppercase}}
#player audio{{display:none}}

/* nav dots */
#chapter-nav{{position:fixed;left:2rem;top:50%;transform:translateY(-50%);z-index:500;display:flex;flex-direction:column;gap:0.9rem}}
#chapter-nav a{{text-decoration:none}}
.nav-dot span{{display:block;width:7px;height:7px;border-radius:50%;border:1px solid var(--gold);transition:all 0.3s}}
.nav-dot.active span,.nav-dot:hover span{{background:var(--gold);transform:scale(1.4)}}

/* ═══ HERO ═══ */
#hero{{min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;padding:5rem 2rem 8rem;position:relative;overflow:hidden;background:var(--dark)}}
.hero-bg{{position:absolute;inset:0;background:
  radial-gradient(ellipse 100% 70% at 50% -10%,rgba(122,37,53,0.52),transparent 60%),
  radial-gradient(ellipse 70% 60% at 90% 90%,rgba(184,137,42,0.13),transparent 50%),
  radial-gradient(ellipse 60% 50% at 10% 80%,rgba(122,37,53,0.11),transparent 50%)}}
.hero-rings{{position:absolute;inset:0;overflow:hidden;pointer-events:none}}
.hero-rings::before,.hero-rings::after{{content:'';position:absolute;border:1px solid rgba(184,137,42,0.08);border-radius:50%}}
.hero-rings::before{{width:80vmax;height:80vmax;top:50%;left:50%;transform:translate(-50%,-50%)}}
.hero-rings::after{{width:60vmax;height:60vmax;top:50%;left:50%;transform:translate(-50%,-50%)}}

/* ═══ TULIPS ═══ */
#tulip-svg{{
  position:absolute;bottom:0;left:50%;transform:translateX(-50%);
  width:min(1400px,110%);height:460px;
  pointer-events:none;z-index:3;
}}

/* tulip bloom keyframes */
@keyframes stemGrow{{from{{transform:scaleY(0)}}to{{transform:scaleY(1)}}}}
@keyframes leafOut{{from{{transform:scale(0);opacity:0}}to{{transform:scale(1);opacity:1}}}}
@keyframes petalOpen{{from{{transform:scale(0) rotate(-18deg);opacity:0}}to{{transform:scale(1) rotate(0deg);opacity:1}}}}
@keyframes stamenPop{{from{{transform:scale(0);opacity:0}}to{{transform:scale(1);opacity:1}}}}

/* gentle breeze — applied via JS after bloom to avoid fighting bloom anims */
.sway-l{{animation:swayL 6s ease-in-out infinite alternate!important}}
.sway-r{{animation:swayR 6s 0.8s ease-in-out infinite alternate!important}}
@keyframes swayL{{from{{transform:rotate(-2deg)}}to{{transform:rotate(1deg)}}}}
@keyframes swayR{{from{{transform:rotate(2deg)}}to{{transform:rotate(-1deg)}}}}

.hero-content{{position:relative;z-index:4;max-width:700px}}
.hero-eyebrow{{font-family:'Cinzel',serif;font-size:0.65rem;letter-spacing:0.5em;color:var(--gold2);text-transform:uppercase;margin-bottom:2rem;opacity:0;animation:riseIn 1s 0.4s forwards}}
.hero-name{{font-family:'Playfair Display',serif;font-size:clamp(4rem,12vw,10rem);font-weight:700;line-height:0.9;
  color:transparent;background:linear-gradient(135deg,var(--gold3) 0%,var(--gold2) 35%,var(--gold) 65%,#7a5a15 100%);
  -webkit-background-clip:text;background-clip:text;opacity:0;animation:riseIn 1.2s 0.7s forwards;margin-bottom:0.2em}}
.hero-sub{{font-family:'EB Garamond',serif;font-style:italic;font-size:clamp(0.85rem,1.5vw,1rem);
  color:var(--mist);letter-spacing:0.2em;opacity:0;animation:riseIn 1s 1.0s forwards;margin-bottom:3rem}}
.hero-orn{{color:var(--gold);font-size:1.2rem;opacity:0;animation:riseIn 1s 1.2s forwards;margin-bottom:2.5rem;letter-spacing:0.5em}}
.hero-poem{{font-family:'EB Garamond',serif;font-style:italic;font-size:clamp(1rem,2vw,1.2rem);
  line-height:2.2;color:var(--cream);opacity:0;animation:riseIn 1s 1.5s forwards}}
.hero-scroll{{position:absolute;bottom:3rem;left:50%;transform:translateX(-50%);
  display:flex;flex-direction:column;align-items:center;gap:0.6rem;
  opacity:0;animation:riseIn 1s 2.2s forwards;z-index:5;cursor:pointer}}
.hero-scroll span{{font-family:'Cinzel',serif;font-size:0.55rem;letter-spacing:0.4em;color:var(--gold2);text-transform:uppercase}}
.scroll-line{{width:1px;height:50px;background:linear-gradient(to bottom,var(--gold),transparent);animation:breathe 2s ease-in-out infinite}}
@keyframes riseIn{{from{{opacity:0;transform:translateY(28px)}}to{{opacity:1;transform:translateY(0)}}}}
@keyframes breathe{{0%,100%{{opacity:0.4}}50%{{opacity:1}}}}

/* band transitions */
.band{{height:120px;background:linear-gradient(to bottom,var(--dark),var(--paper))}}
.band.inv{{background:linear-gradient(to bottom,var(--paper),var(--dark))}}

/* ═══ CHAPTERS ═══ */
.chapter{{padding:7rem 2rem;max-width:1200px;margin:0 auto;position:relative}}
.chapter-tag{{font-family:'Cinzel',serif;font-size:0.6rem;letter-spacing:0.4em;color:var(--mist);text-transform:uppercase;margin-bottom:3rem}}
.chapter-inner{{display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:start}}
.center-layout{{display:flex;flex-direction:column;align-items:center;text-align:center;gap:4rem}}
.chapter-text{{max-width:480px}}
.center-layout .chapter-text{{max-width:600px}}
.ch-number{{font-family:'Playfair Display',serif;font-style:italic;font-size:5rem;color:var(--cream);line-height:1;display:block;margin-bottom:-0.5rem;opacity:0.6}}
.ch-title{{font-family:'Playfair Display',serif;font-size:clamp(2rem,4vw,3.2rem);font-weight:400;color:var(--dark);line-height:1.1;margin-bottom:0.4rem}}
.ch-subtitle{{font-family:'EB Garamond',serif;font-style:italic;font-size:1.1rem;color:var(--mist);margin-bottom:2rem;letter-spacing:0.05em}}
.ch-divider{{display:flex;align-items:center;gap:0.8rem;margin-bottom:2rem}}
.ch-divider span{{flex:1;height:1px;background:var(--gold3)}}
.ch-divider i{{color:var(--gold);font-style:normal;font-size:0.7rem}}
.center-layout .ch-divider{{justify-content:center;max-width:200px;margin:0 auto 2rem}}
.ch-quote{{font-family:'EB Garamond',serif;font-style:italic;font-size:clamp(1.15rem,2vw,1.4rem);line-height:1.8;color:var(--rose);border-left:2px solid var(--gold3);padding-left:1.5rem;margin-bottom:1.8rem}}
.center-layout .ch-quote{{border-left:none;border-top:1px solid var(--gold3);padding:1.5rem 0 0;text-align:center}}
.ch-caption{{font-size:1rem;color:var(--ink);line-height:1.8;opacity:0.75}}

/* photos + videos */
.photos-stack{{display:flex;flex-direction:column;gap:1.2rem}}
.photo-slot{{overflow:hidden;border:1px solid var(--gold3);background:var(--cream);aspect-ratio:4/3;position:relative}}
.photo-slot img,
.photo-slot video{{width:100%;height:100%;object-fit:cover;display:block;transition:transform 0.6s ease;filter:sepia(8%) saturate(85%)}}
.photo-slot:hover img,
.photo-slot:hover video{{transform:scale(1.04)}}
/* video-specific: hide controls, remove outline */
.photo-slot video{{outline:none;cursor:default}}
/* small ▶ badge so viewer knows it's a video */
.photo-slot video::before{{content:''}}
.video-badge{{
  position:absolute;top:0.6rem;right:0.6rem;
  background:rgba(0,0,0,0.45);backdrop-filter:blur(4px);
  border:1px solid rgba(255,255,255,0.2);
  color:white;font-size:0.55rem;letter-spacing:0.1em;
  font-family:'Cinzel',serif;padding:0.2rem 0.5rem;
  border-radius:2px;pointer-events:none;
}}
.right-stack .photo-slot:nth-child(1){{aspect-ratio:3/2}}
.right-stack .photo-slot:nth-child(2){{aspect-ratio:1/1;align-self:flex-end;width:75%}}
.right-stack .photo-slot:nth-child(3){{aspect-ratio:16/9}}
.left-stack .photo-slot:nth-child(1){{aspect-ratio:16/9}}
.left-stack .photo-slot:nth-child(2){{aspect-ratio:1/1;width:70%}}
.left-stack .photo-slot:nth-child(3){{aspect-ratio:3/2}}
.photos-center{{display:flex;gap:1.2rem;justify-content:center;flex-wrap:wrap;width:100%}}
.photos-center .photo-slot{{flex:1;min-width:220px;max-width:320px}}
.ph-slot{{width:100%;height:100%;min-height:160px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:var(--mist);gap:0.6rem;font-family:'Cinzel',serif;font-size:0.55rem;letter-spacing:0.1em;text-align:center;padding:1rem}}
.ph-slot svg{{width:28px;height:28px;fill:currentColor;opacity:0.5}}

/* ═══ LETTER ═══ */
#letter{{background:var(--dark);padding:9rem 2rem;position:relative;overflow:hidden}}
.letter-bg{{position:absolute;inset:0;background:
  radial-gradient(ellipse 80% 60% at 30% 50%,rgba(122,37,53,0.25),transparent 60%),
  radial-gradient(ellipse 60% 60% at 75% 40%,rgba(184,137,42,0.08),transparent 60%)}}
.letter-inner{{position:relative;z-index:2;max-width:680px;margin:0 auto;text-align:center}}
.letter-eyebrow{{font-family:'Cinzel',serif;font-size:0.6rem;letter-spacing:0.45em;color:var(--gold2);text-transform:uppercase;margin-bottom:3rem}}
.letter-body{{font-family:'EB Garamond',serif;font-style:italic;font-size:clamp(1.1rem,2vw,1.4rem);line-height:2.1;color:var(--cream);margin-bottom:3rem}}
.letter-body p{{margin-bottom:1.2rem}}
.letter-sig{{font-family:'Playfair Display',serif;font-style:italic;font-size:1.3rem;color:var(--gold2);margin-top:2rem!important}}
.letter-orn{{font-size:2rem;color:var(--gold);display:block;margin-bottom:2rem;animation:glowFade 3s ease-in-out infinite}}
@keyframes glowFade{{0%,100%{{opacity:0.5}}50%{{opacity:1}}}}

/* footer */
footer{{background:var(--dark);border-top:1px solid rgba(184,137,42,0.15);text-align:center;padding:3rem 2rem 4rem}}
.footer-text{{font-family:'Cinzel',serif;font-size:0.6rem;letter-spacing:0.4em;color:var(--gold);opacity:0.4;text-transform:uppercase}}

/* reveal */
.reveal{{opacity:0;transform:translateY(40px);transition:opacity 0.9s ease,transform 0.9s ease}}
.reveal.visible{{opacity:1;transform:translateY(0)}}

/* ═══ BLANK PAGES SECTION ═══ */
#blank-pages{{
  padding:9rem 2rem;
  background:var(--dark);
  position:relative;overflow:hidden;
  text-align:center;
}}
.bp-bg{{
  position:absolute;inset:0;
  background:
    radial-gradient(ellipse 70% 50% at 20% 60%,rgba(184,137,42,0.08),transparent 55%),
    radial-gradient(ellipse 60% 50% at 80% 30%,rgba(122,37,53,0.12),transparent 55%);
}}
.bp-inner{{position:relative;z-index:2;max-width:780px;margin:0 auto}}
.bp-eyebrow{{
  font-family:'Cinzel',serif;font-size:0.6rem;
  letter-spacing:0.45em;color:var(--gold2);
  text-transform:uppercase;margin-bottom:3.5rem;
}}
.bp-pages{{
  display:flex;gap:2.5rem;justify-content:center;
  flex-wrap:wrap;margin-bottom:4rem;
}}
.bp-page{{
  flex:1;min-width:180px;max-width:240px;
  border:1px solid rgba(201,169,110,0.25);
  padding:2.5rem 1.5rem 3rem;
  position:relative;
  background:rgba(255,255,255,0.02);
}}
.bp-page::before{{
  content:'';position:absolute;
  top:0.6rem;left:0.6rem;right:0.6rem;bottom:0.6rem;
  border:1px solid rgba(201,169,110,0.1);
  pointer-events:none;
}}
.bp-lines{{display:flex;flex-direction:column;gap:0.9rem;margin-top:0.5rem}}
.bp-line{{height:1px;background:rgba(201,169,110,0.18)}}
.bp-pg-number{{
  font-family:'Cinzel',serif;font-size:0.55rem;
  letter-spacing:0.3em;color:rgba(201,169,110,0.3);
  margin-top:1.8rem;
}}
.bp-title{{
  font-family:'Playfair Display',serif;
  font-size:clamp(1.8rem,4vw,2.8rem);
  color:var(--gold3);
  line-height:1.2;margin-bottom:2rem;
  font-style:italic;
}}
.bp-body{{
  font-family:'EB Garamond',serif;font-style:italic;
  font-size:clamp(1rem,1.8vw,1.2rem);
  line-height:2;color:var(--mist);
  margin-bottom:2.5rem;
}}
.bp-wink{{
  font-family:'EB Garamond',serif;
  font-size:clamp(0.9rem,1.5vw,1.05rem);
  color:rgba(201,169,110,0.5);
  line-height:1.9;font-style:italic;
}}

@media(max-width:768px){{
  .chapter-inner{{grid-template-columns:1fr;gap:3rem}}
  .center-layout{{flex-direction:column}}
  .right-stack .photo-slot:nth-child(2),.left-stack .photo-slot:nth-child(2){{width:100%}}
  #chapter-nav{{display:none}}
  #player{{top:1rem;right:1rem}}
  .cursor,.cursor-ring{{display:none}}
  #tulip-svg{{height:260px}}
  .bp-pages{{gap:1.5rem}}
}}
</style>
</head>
<body>

<div class="cursor" id="cur"></div>
<div class="cursor-ring" id="curring"></div>
<div id="progress"></div>

<div id="player" onclick="toggleMusic()">
  <svg id="pi" viewBox="0 0 24 24"><path d="M12 3v10.55A4 4 0 1 0 14 17V7h4V3h-6z"/></svg>
  <span id="pl">{cfg['music_title']}</span>
  <audio id="audio" loop><source src="{cfg['music_url']}" type="audio/mpeg"/></audio>
</div>

{nav_html}

<!-- ════ HERO ════ -->
<section id="hero">
  <div class="hero-bg"></div>
  <div class="hero-rings"></div>

  <div class="hero-content">
    <p class="hero-eyebrow">In celebration Of</p>
    <h1 class="hero-name">{cfg['name']}</h1>
    <p class="hero-sub">{cfg['tagline']}</p>
    <p class="hero-orn">✦ &nbsp; ✦ &nbsp; ✦</p>
    <p class="hero-poem">{hero_lines}</p>
  </div>

  <!-- Blooming white tulips -->
  {tulips}

  <div class="hero-scroll" onclick="document.getElementById('chapter-1').scrollIntoView({{behavior:'smooth'}})">
    <span>Begin</span>
    <div class="scroll-line"></div>
  </div>
</section>

<div class="band"></div>

{chapters_html}

<div class="band inv"></div>

<div class="band inv"></div>

<!-- ════ BLANK PAGES ════ -->
<section id="blank-pages" class="reveal">
  <div class="bp-bg"></div>
  <div class="bp-inner">
    <p class="bp-eyebrow">The chapters still to come</p>
    <h2 class="bp-title">These pages are intentionally left blank.</h2>
    <p class="bp-body">
      Because the best stories aren't planned.<br/>
      They happen on a Tuesday, for no reason,<br/>
      when you least expect it.
    </p>
    <div class="bp-pages">
      <div class="bp-page">
        <div class="bp-lines">
          <div class="bp-line"></div><div class="bp-line"></div>
          <div class="bp-line"></div><div class="bp-line"></div>
          <div class="bp-line"></div><div class="bp-line"></div>
          <div class="bp-line"></div><div class="bp-line"></div>
        </div>
        <p class="bp-pg-number">— i —</p>
      </div>
      <div class="bp-page">
        <div class="bp-lines">
          <div class="bp-line"></div><div class="bp-line"></div>
          <div class="bp-line"></div><div class="bp-line"></div>
          <div class="bp-line"></div><div class="bp-line"></div>
          <div class="bp-line"></div><div class="bp-line"></div>
        </div>
        <p class="bp-pg-number">— ii —</p>
      </div>
      <div class="bp-page">
        <div class="bp-lines">
          <div class="bp-line"></div><div class="bp-line"></div>
          <div class="bp-line"></div><div class="bp-line"></div>
          <div class="bp-line"></div><div class="bp-line"></div>
          <div class="bp-line"></div><div class="bp-line"></div>
        </div>
        <p class="bp-pg-number">— iii —</p>
      </div>
    </div>
    <p class="bp-wink">
      (I'm leaving these here because we both know<br/>
      we haven't even gotten to the good parts yet.<br/>
      And honestly? I cannot wait. 🤍)
    </p>
  </div>
</section>

<!-- ════ LETTER ════ -->
<section id="letter" class="reveal">
  <div class="letter-bg"></div>
  <div class="letter-inner">
    <p class="letter-eyebrow">A note just for you</p>
    <span class="letter-orn">✦</span>
    <div class="letter-body">{letter_html}</div>
  </div>
</section>

<footer>
  <p class="footer-text">Happy Birthday, {cfg['name']} &nbsp;·&nbsp; Made with love</p>
</footer>

<script>
// cursor
const cur=document.getElementById('cur'),ring=document.getElementById('curring');
let mx=0,my=0,rx=0,ry=0;
document.addEventListener('mousemove',e=>{{mx=e.clientX;my=e.clientY;cur.style.cssText=`left:${{mx-4}}px;top:${{my-4}}px`}});
setInterval(()=>{{rx+=(mx-rx)*0.12;ry+=(my-ry)*0.12;ring.style.cssText=`left:${{rx-16}}px;top:${{ry-16}}px`}},16);

// progress
window.addEventListener('scroll',()=>{{
  document.getElementById('progress').style.width=(window.scrollY/(document.body.scrollHeight-window.innerHeight)*100)+'%';
}});

// music
const audio=document.getElementById('audio'),pi=document.getElementById('pi'),pl=document.getElementById('pl');
let playing=false;
function toggleMusic(){{
  if(playing){{audio.pause();pi.innerHTML='<path d="M12 3v10.55A4 4 0 1 0 14 17V7h4V3h-6z"/>';pl.textContent='{cfg['music_title']}'}}
  else{{audio.play().catch(()=>{{}});pi.innerHTML='<path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>';pl.textContent='Now Playing'}}
  playing=!playing;
}}

// tulip sway — start after longest bloom finishes (~5.5s)
setTimeout(()=>{{
  document.querySelectorAll('#tulip-svg g g').forEach((g,i)=>{{
    g.classList.add(i%2===0?'sway-l':'sway-r');
  }});
}}, 5600);

// reveal on scroll
const obs=new IntersectionObserver(e=>e.forEach(x=>{{if(x.isIntersecting)x.target.classList.add('visible')}}),{{threshold:0.12}});
document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));
document.querySelectorAll('.chapter').forEach(el=>{{el.classList.add('reveal');obs.observe(el)}});

// nav dots
document.querySelectorAll('.chapter').forEach(ch=>{{
  new IntersectionObserver(e=>e.forEach(x=>{{
    if(x.isIntersecting){{
      document.querySelectorAll('.nav-dot').forEach(d=>d.classList.remove('active'));
      const a=document.querySelector('.nav-dot[href="#'+x.target.id+'"]');
      if(a)a.classList.add('active');
    }}
  }}),{{threshold:0.4}}).observe(ch);
}});
</script>
</body>
</html>"""


# ════════════════════════════════════════════════════════════
#  M A I N
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    html = generate(CONFIG)
    out  = CONFIG["output_file"]
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅  Birthday website saved → {out}")
    print(f"    Mac:     open {out}")
    print(f"    Windows: start {out}")
    print()
    print("📁  Recommended folder structure:")
    print("      birthday/")
    print("      ├── generate_birthday.py")
    print("      ├── birthday.html          ← generated here")
    print("      ├── song.mp3               ← local music")
    print("      └── photos/")
    print("            ├── memory1.jpg")
    print("            ├── adventure.mp4   ← videos work too!")
    print("            └── moment.png")
    print()
    print("✏️   To customise:")
    print("    • Edit CONFIG at the top of this file")
    print("    • Drop photos/videos into a 'photos/' folder")
    print("    • Reference them as: \"photos/filename.jpg\"")
    print("    • Run again to regenerate instantly")
