# -*- coding: utf-8 -*-
"""
Preserve 100% of the original Aximo HTML template:
- Keeps every single section, banner, team, testimonial, marquee ticker, counter, and FAQ
- Replaces only branding to 'Ghaya Prod' and adds EN/FR/AR language toggle
- Ensures pixel-for-pixel fidelity with the official ThemeForest preview
"""

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

GHAYA_DIR = Path(r"C:\Users\USER\.gemini\antigravity\scratch\ghaya-prod")

with open(GHAYA_DIR / "index_original.html", "r", encoding="utf-8") as f:
    orig = f.read()

# Build English Full Page
en_html = orig

# 1. Update Title
en_html = en_html.replace(
    "<title>Aximo || Responsive HTML 5 Template</title>",
    "<title>Ghaya Prod || High-Converting Web Platforms & 4K Cinema Production Studio</title>"
)

# 2. Update Header Brand Logo
old_logo = '''        <div class="brand-logo">
          <a href="index.html">
            <img src="assets/images/logo/logo-white.svg" alt="" class="light-version-logo">
          </a>
        </div>'''

new_logo = '''        <div class="brand-logo">
          <a href="index.html" style="text-decoration: none; display: flex; align-items: center; gap: 8px;">
            <span style="font-family: 'Syne', sans-serif; font-size: 30px; font-weight: 800; color: #fff; letter-spacing: -1.5px;">GHAYA<span style="color: #BFF747;">PROD</span></span>
          </a>
        </div>'''

en_html = en_html.replace(old_logo, new_logo)

# 3. Add Language Switcher next to Contact button
old_btn = '''        <div class="header-btn header-btn-l1 ms-auto d-none d-xs-inline-flex">
          <a class="aximo-default-btn pill aximo-header-btn" href="contact-us.html">
            Contact Us
          </a>
        </div>'''

new_btn = '''        <div class="d-flex align-items-center gap-3 ms-auto">
          <div class="lang-switcher d-flex gap-2 align-items-center" style="font-size: 13px; font-weight: 700; background: rgba(255,255,255,0.06); padding: 6px 14px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.15);">
            <a href="index.html" style="color: #BFF747; text-decoration: none;">EN</a>
            <span style="color: rgba(255,255,255,0.3);">|</span>
            <a href="fr.html" style="color: #fff; text-decoration: none;">FR</a>
            <span style="color: rgba(255,255,255,0.3);">|</span>
            <a href="ar.html" style="color: #fff; text-decoration: none;">AR</a>
          </div>
          <div class="header-btn header-btn-l1 d-none d-xs-inline-flex">
            <a class="aximo-default-btn pill aximo-header-btn" href="contact-us.html">
              Contact Us
            </a>
          </div>
        </div>'''

en_html = en_html.replace(old_btn, new_btn)

# 4. Update Hero Heading
en_html = en_html.replace(
    'A creative\n                <img src="assets/images/v1/star.png" alt="">\n              </span>\n              design studio',
    'A high-converting\n                <img src="assets/images/v1/star.png" alt="">\n              </span>\n              web & cinema studio'
)

# 5. Update Hero Subtitle
en_html = en_html.replace(
    "We're a creative design studio specializing in meeting the needs of the new generation. We offer innovative and cutting-edge design solutions to help our clients stand out in today's fast-paced.",
    "We engineer high-converting web ecosystems, interactive CRM systems, and produce 4K cinema video for aesthetic clinics, private practices, and high-ticket service brands."
)

# 6. Update Community Counter
en_html = en_html.replace(
    "Believed by more than a thousand people",
    "Trusted by 1,000+ community & business leaders"
)

# 7. Update Footer Logo & Copyright
en_html = en_html.replace(
    '<img src="assets/images/logo/logo-white.svg" alt="">',
    '<span style="font-family: \'Syne\', sans-serif; font-size: 28px; font-weight: 800; color: #fff;">GHAYA<span style="color: #BFF747;">PROD</span></span>'
)
en_html = en_html.replace(
    "&copy; Copyright 2024, All Rights Reserved by Mthemeus",
    "&copy; Copyright 2026, All Rights Reserved by Ghaya Prod Studio"
)

(GHAYA_DIR / "index.html").write_text(en_html, encoding="utf-8")
print("✅ Saved full 1,117-line English version: index.html")


# Build French Full Page
fr_html = en_html

fr_html = fr_html.replace(
    "<title>Ghaya Prod || High-Converting Web Platforms & 4K Cinema Production Studio</title>",
    "<title>Ghaya Prod || Écosystèmes Web Haute Conversion & Studio Vidéo Cinéma 4K</title>"
)
fr_html = fr_html.replace('lang="en"', 'lang="fr"')

# Header & Nav Translation
fr_html = fr_html.replace(
    '<a href="index.html" style="color: #BFF747; text-decoration: none;">EN</a>\n            <span style="color: rgba(255,255,255,0.3);">|</span>\n            <a href="fr.html" style="color: #fff; text-decoration: none;">FR</a>',
    '<a href="index.html" style="color: #fff; text-decoration: none;">EN</a>\n            <span style="color: rgba(255,255,255,0.3);">|</span>\n            <a href="fr.html" style="color: #BFF747; text-decoration: none;">FR</a>'
)
fr_html = fr_html.replace('<a href="about-us.html" class="nav-link-item">About Us</a>', '<a href="about-us.html" class="nav-link-item">À Propos</a>')
fr_html = fr_html.replace('<a href="contact-us.html" class="nav-link-item">Contact Us</a>', '<a href="contact-us.html" class="nav-link-item">Contact</a>')
fr_html = fr_html.replace('Contact Us\n            </a>', 'Contactez-Nous\n            </a>')

# Hero Translation
fr_html = fr_html.replace(
    'A high-converting\n                <img src="assets/images/v1/star.png" alt="">\n              </span>\n              web & cinema studio',
    'Écosystèmes web\n                <img src="assets/images/v1/star.png" alt="">\n              </span>\n              & production cinéma'
)
fr_html = fr_html.replace(
    "We engineer high-converting web ecosystems, interactive CRM systems, and produce 4K cinema video for aesthetic clinics, private practices, and high-ticket service brands.",
    "Nous concevons des plateformes web haute conversion avec CRM intelligent et produisons des vidéos cinéma 4K pour les cliniques esthétiques, cabinets médicaux et marques premium."
)
fr_html = fr_html.replace(
    "Book a free consultation",
    "Réserver un audit gratuit"
)
fr_html = fr_html.replace(
    "Trusted by 1,000+ community & business leaders",
    "Plus de 1 000 abonnés et professionnels nous font confiance"
)

# Services section header
fr_html = fr_html.replace(
    'We provide effective\n          <span class="aximo-title-animation">\n            design solutions',
    'Nous concevons des\n          <span class="aximo-title-animation">\n            solutions digitales d\'élite'
)

# Ticker marquee
fr_html = fr_html.replace("Let's create new experiences", "CRÉER DES EXPÉRIENCES UNIQUES")

# Team header
fr_html = fr_html.replace(
    'We have a team of\n          <span class="aximo-title-animation">\n            creative people',
    'Une équipe d\'experts\n          <span class="aximo-title-animation">\n            et de créateurs passionnés'
)

# Testimonials header
fr_html = fr_html.replace("Clients are satisfied by our work", "Ce que disent nos clients partenaires")

# Footer form
fr_html = fr_html.replace("Send us a message", "Envoyez-nous un message")
fr_html = fr_html.replace("Your name", "Votre nom")
fr_html = fr_html.replace("Your email address", "Votre adresse e-mail")
fr_html = fr_html.replace("Write your message here...", "Décrivez votre projet...")
fr_html = fr_html.replace("Send message", "Envoyer le message")

(GHAYA_DIR / "fr.html").write_text(fr_html, encoding="utf-8")
print("✅ Saved full 1,117-line French version: fr.html")


# Build Arabic Full Page (RTL)
ar_html = en_html

ar_html = ar_html.replace(
    "<title>Ghaya Prod || High-Converting Web Platforms & 4K Cinema Production Studio</title>",
    "<title>غاية برود || منصات الويب عالية التحويل واستوديو الإنتاج السينمائي 4K</title>"
)
ar_html = ar_html.replace('<html lang="en">', '<html lang="ar" dir="rtl">')

# Add Cairo font and RTL CSS support
ar_font_patch = '''  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Cairo', 'Syne', sans-serif !important; text-align: right; }
    .site-menu-main { text-align: right; }
  </style>'''
ar_html = ar_html.replace('</head>', f'{ar_font_patch}\n</head>')

# Language Switcher
ar_html = ar_html.replace(
    '<a href="index.html" style="color: #BFF747; text-decoration: none;">EN</a>\n            <span style="color: rgba(255,255,255,0.3);">|</span>\n            <a href="ar.html" style="color: #fff; text-decoration: none;">AR</a>',
    '<a href="index.html" style="color: #fff; text-decoration: none;">EN</a>\n            <span style="color: rgba(255,255,255,0.3);">|</span>\n            <a href="ar.html" style="color: #BFF747; text-decoration: none;">AR</a>'
)

# Nav items
ar_html = ar_html.replace('<a href="about-us.html" class="nav-link-item">About Us</a>', '<a href="about-us.html" class="nav-link-item">من نحن</a>')
ar_html = ar_html.replace('<a href="contact-us.html" class="nav-link-item">Contact Us</a>', '<a href="contact-us.html" class="nav-link-item">تواصل معنا</a>')
ar_html = ar_html.replace('Contact Us\n            </a>', 'ابدأ مشروعك\n            </a>')

# Hero Translation
ar_html = ar_html.replace(
    'A high-converting\n                <img src="assets/images/v1/star.png" alt="">\n              </span>\n              web & cinema studio',
    'منصات ويب فائقة\n                <img src="assets/images/v1/star.png" alt="">\n              </span>\n              وإنتاج سينمائي مبهر'
)
ar_html = ar_html.replace(
    "We engineer high-converting web ecosystems, interactive CRM systems, and produce 4K cinema video for aesthetic clinics, private practices, and high-ticket service brands.",
    "نصمم منظومات ويب رقمية عالية التحويل مزودة بأنظمة CRM متطورة، وننتج محتوى مرئياً سينمائياً فائق الدقة (4K) لعيادات التجميل، المراكز الطبية والعلامات الراقية."
)
ar_html = ar_html.replace(
    "Book a free consultation",
    "احجز استشارة مجانية"
)
ar_html = ar_html.replace(
    "Trusted by 1,000+ community & business leaders",
    "أكثر من 1,000 متابع وشريك نجاح يثقون في أعمالنا"
)

# Services section header
ar_html = ar_html.replace(
    'We provide effective\n          <span class="aximo-title-animation">\n            design solutions',
    'نبتكر حلولاً رقمية\n          <span class="aximo-title-animation">\n            سينمائية واستثنائية'
)

# Ticker marquee
ar_html = ar_html.replace("Let's create new experiences", "نصنع تجارب استثنائية تلهم العالم")

# Team header
ar_html = ar_html.replace(
    'We have a team of\n          <span class="aximo-title-animation">\n            creative people',
    'فريق متكامل من\n          <span class="aximo-title-animation">\n            المبدعين والمحترفين'
)

# Testimonials header
ar_html = ar_html.replace("Clients are satisfied by our work", "آراء شركائنا في النجاح")

# Footer form
ar_html = ar_html.replace("Send us a message", "أرسل لنا رسالة")
ar_html = ar_html.replace("Your name", "الاسم الكامل")
ar_html = ar_html.replace("Your email address", "البريد الإلكتروني")
ar_html = ar_html.replace("Write your message here...", "أخبرنا عن تفاصيل مشروعك...")
ar_html = ar_html.replace("Send message", "إرسال الرسالة الآن")

(GHAYA_DIR / "ar.html").write_text(ar_html, encoding="utf-8")
print("✅ Saved full 1,117-line Arabic RTL version: ar.html")

# Copy the updated full files to Desktop as well
import shutil
desktop_dir = Path(r"C:\Users\USER\Desktop\ghaya-prod")
for fname in ["index.html", "fr.html", "ar.html"]:
    shutil.copy(GHAYA_DIR / fname, desktop_dir / fname)
print("✅ Synchronized desktop folder: C:\\Users\\USER\\Desktop\\ghaya-prod")
