# -*- coding: utf-8 -*-
"""
Sets French as the Primary Language of the Website:
- index.html is FRENCH (Primary)
- en.html is ENGLISH (Secondary)
- ar.html is ARABIC (Tertiary RTL)
- fr.html points/duplicates index.html for direct link safety
- Language switcher order everywhere: [ FR | EN | AR ]
- Complete French translation across all sections, testimonials, portfolio, pricing, team
- Fully synchronized to Desktop: C:\\Users\\USER\\Desktop\\ghaya-prod
"""

import sys
from pathlib import Path
import re
import shutil

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

GHAYA_DIR = Path(r"C:\Users\USER\.gemini\antigravity\scratch\ghaya-prod")
DESKTOP_DIR = Path(r"C:\Users\USER\Desktop\ghaya-prod")

# Read index_original.html as clean baseline
with open(GHAYA_DIR / "index_original.html", "r", encoding="utf-8") as f:
    orig = f.read()

# =========================================================================
# 1. BUILD ENGLISH VERSION (en.html)
# =========================================================================
en = orig

en = en.replace(
    "<title>Aximo || Responsive HTML 5 Template</title>",
    "<title>Ghaya Prod || High-Converting Web Platforms, E-Commerce & Cinema Production Studio</title>"
)

# Logo
en = en.replace(
    '<img src="assets/images/logo/logo-white.svg" alt="" class="light-version-logo">',
    '<img src="assets/images/logo/logo-ghaya-white.svg" alt="Ghaya Prod" class="light-version-logo">'
)
en = en.replace(
    '<img src="assets/images/logo/logo-white.svg" alt="">',
    '<img src="assets/images/logo/logo-ghaya-white.svg" alt="Ghaya Prod">'
)

# Nav Menu English
NAV_MENU_EN = '''<ul class="site-menu-main">
              <li class="nav-item">
                <a href="#services" class="nav-link-item">Services</a>
              </li>
              <li class="nav-item">
                <a href="#portfolio" class="nav-link-item">Portfolio</a>
              </li>
              <li class="nav-item">
                <a href="#process" class="nav-link-item">Process</a>
              </li>
              <li class="nav-item">
                <a href="#pricing" class="nav-link-item">Pricing</a>
              </li>
              <li class="nav-item">
                <a href="#testimonials" class="nav-link-item">Testimonials</a>
              </li>
              <li class="nav-item">
                <a href="#team" class="nav-link-item">Team</a>
              </li>
              <li class="nav-item nav-item-has-children">
                <a href="#" class="nav-link-item drop-trigger">Pages <i class="fas fa-angle-down"></i></a>
                <ul class="sub-menu" id="submenu-pages">
                  <li class="sub-menu--item">
                    <a href="about-us.html"><span class="menu-item-text">About Us</span></a>
                  </li>
                  <li class="sub-menu--item">
                    <a href="pricing.html"><span class="menu-item-text">Pricing Plans</span></a>
                  </li>
                  <li class="sub-menu--item">
                    <a href="service.html"><span class="menu-item-text">Services Detail</span></a>
                  </li>
                  <li class="sub-menu--item">
                    <a href="portfolio-01.html"><span class="menu-item-text">Portfolio Showcase</span></a>
                  </li>
                  <li class="sub-menu--item">
                    <a href="team.html"><span class="menu-item-text">Our Team</span></a>
                  </li>
                  <li class="sub-menu--item">
                    <a href="faq.html"><span class="menu-item-text">FAQ</span></a>
                  </li>
                  <li class="sub-menu--item">
                    <a href="testimonial.html"><span class="menu-item-text">Client Testimonials</span></a>
                  </li>
                  <li class="sub-menu--item">
                    <a href="contact-us.html"><span class="menu-item-text">Contact Us</span></a>
                  </li>
                </ul>
              </li>
              <li class="nav-item">
                <a href="#contact" class="nav-link-item">Contact</a>
              </li>
            </ul>
          </nav>'''
en = re.sub(r'<ul class="site-menu-main">[\s\S]*?</ul>\s*</nav>', NAV_MENU_EN, en, count=1)

# Language Switcher: FR | EN | AR (EN Active)
LANG_SWITCHER_EN = '''        <div class="d-flex align-items-center gap-3 ms-auto">
          <div class="lang-switcher d-flex gap-2 align-items-center" style="font-size: 13px; font-weight: 700; background: rgba(255,255,255,0.08); padding: 6px 14px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.18);">
            <a href="index.html" style="color: #fff; text-decoration: none;">FR</a>
            <span style="color: rgba(255,255,255,0.3);">|</span>
            <a href="en.html" style="color: #BFF747; text-decoration: none;">EN</a>
            <span style="color: rgba(255,255,255,0.3);">|</span>
            <a href="ar.html" style="color: #fff; text-decoration: none;">AR</a>
          </div>
          <div class="header-btn header-btn-l1 d-none d-xs-inline-flex">
            <a class="aximo-default-btn pill aximo-header-btn" href="#contact">
              Contact Us
            </a>
          </div>
        </div>'''
old_btn = r'<div class="header-btn header-btn-l1 ms-auto d-none d-xs-inline-flex">[\s\S]*?</div>'
en = re.sub(old_btn, LANG_SWITCHER_EN, en, count=1)

# Hero Section EN
en = re.sub(
    r'A creative\s*<img src="assets/images/v1/star\.png" alt="">\s*</span>\s*design studio',
    'High-converting\n                <img src="assets/images/v1/star.png" alt="">\n              </span>\n              web & cinema studio',
    en
)
en = en.replace(
    "We're a creative design studio specializing in meeting the needs of the new generation. We offer innovative and cutting-edge design solutions to help our clients stand out in today's fast-paced.",
    "We build high-converting web platforms, high-ROI e-commerce stores, and produce broadcast 4K cinema video for aesthetic clinics, private practices, and high-ticket service brands."
)
en = en.replace("Believed by more than a thousand people", "Trusted by 1,000+ community & business leaders")
en = en.replace('href="contact-us.html">Book a free consultation', 'href="#contact">Book a strategy consultation')

# Section Anchors & IDs
en = en.replace('<div class="section aximo-section-padding4">', '<div class="section aximo-section-padding4" id="services">')
en = en.replace('<div class="section aximo-section-padding">', '<div class="section aximo-section-padding" id="about">', 1)
en = en.replace('<div class="section dark-bg aximo-section-padding">', '<div class="section dark-bg aximo-section-padding" id="portfolio">')
en = en.replace('<div class="section">\n    <div class="container">\n      <div class="aximo-faq-wrap">',
                '<div class="section" id="process">\n    <div class="container">\n      <div class="aximo-faq-wrap">')
en = en.replace('<div class="section aximo-section-padding3">', '<div class="section aximo-section-padding3" id="testimonials">', 1)
en = en.replace('<div class="section aximo-section-padding3">', '<div class="section aximo-section-padding3" id="team">', 1)
en = en.replace('<footer class="aximo-footer-section dark-bg">', '<footer class="aximo-footer-section dark-bg" id="contact">')

# Services Cards EN
en = en.replace(
    '<h3>UI/UX Design</h3>\n                <p>Focusing on user interface (UI) and user experience (UX) design enhance the usability and accessibility of digital products & app.</p>',
    '<h3>Web Platforms & Portfolios</h3>\n                <p>Architecting custom, ultra-fast websites and portfolio platforms tailored for aesthetic clinics, doctors, and high-status creative agencies.</p>'
)
en = en.replace(
    '<h3>Graphic Design</h3>\n                <p>Creating visual elements such as logos, branding materials, page layout techniques, brochures, & other marketing collateral.</p>',
    '<h3>E-Commerce & COD Stores</h3>\n                <p>High-converting e-commerce stores with optimized checkout funnels, fast mobile landing pages, and automated order tracking systems.</p>'
)
en = en.replace(
    '<h3>Web Design</h3>\n                <p>Designing and developing websites to ensure they are visually look and appealing, user-friendly, and functional your website.</p>',
    '<h3>4K Cinema Video Production</h3>\n                <p>Shot on Panasonic Lumix S5 Full-Frame cinema camera with broadcast Sennheiser/Shure audio and Ronin RS3 gimbal stabilization for clinical prestige.</p>'
)
en = en.replace(
    '<h3>Motion Graphics</h3>\n                <p>Creating animate graphics, videos for various purposes, including marketing and entertainment. To help sell a product or service.</p>',
    '<h3>High-CTR Short-Form Video</h3>\n                <p>Psychologically engineered Reels and TikTok ad creatives edited in CapCut Pro with viral pacing to convert cold traffic into paying consultations.</p>'
)

# Counter fallback numbers & section description EN
en = en.replace(
    'We work closely with our clients to know their objectives, target audience, unique needs, and practical design solutions.',
    'We fuse Hollywood-grade camera production with modern conversion rate optimization to turn viewers into high-ticket clients.'
)
en = en.replace('<span data-percentage="15" class="aximo-counter"></span>+', '<span data-percentage="15" class="aximo-counter">15</span>+')
en = en.replace('<span data-percentage="120" class="aximo-counter"></span>k', '<span data-percentage="120" class="aximo-counter">120</span>k')
en = en.replace('<span data-percentage="100" class="aximo-counter"></span>%', '<span data-percentage="100" class="aximo-counter">100</span>%')
en = en.replace('Years of experience', 'Years of creative excellence')
en = en.replace('Successful projects', 'Targeted campaigns deployed')

# Portfolio Projects Swiper EN
en = en.replace('<h3>Product Design</h3>\n                </a>\n                <p>Developing the look and feel of physical products, aesthetics, and functionality.</p>',
                '<h3>Dr. Hanane Kashi Aesthetic Clinic</h3>\n                </a>\n                <p>Bilingual facial injection clinic platform with interactive Before/After comparison and 1-minute diagnostic quiz.</p>')
en = en.replace('<h3>Logo and Branding</h3>\n                </a>\n                <p>Creating or refreshing a company\'s logo and developing a cohesive visual identity.</p>',
                '<h3>Luxury Cabinet & Corporate Identity</h3>\n                </a>\n                <p>Complete office 3D gold monogram signage, branding kit, and high-status visual design for Casablanca aesthetic doctor.</p>')
en = en.replace('<h3>App UI/UX Design</h3>\n                </a>\n                <p>Designing the UI/UXe for mobile apps and web applications to ensure usability & engagement.</p>',
                '<h3>Medical Secretariat CRM Dashboard</h3>\n                </a>\n                <p>Private multi-factor patient queue, revenue analytics, and 1-click WhatsApp appointment confirmation studio.</p>')
en = en.replace('<h3>Packaging Design</h3>\n                </a>\n                <p>Creating packaging solutions for products that not only protect attract customers on store.</p>',
                '<h3>Clinical Video Case Consultation</h3>\n                </a>\n                <p>On-camera consultation and procedural breakdown filmed with wireless broadcast mics for patient Zineb testimonial.</p>')

# Working Process (Accordion) EN
en = en.replace('<h3>01/ Project idea</h3>', '<h3>01/ Strategic Discovery</h3>')
en = en.replace('<p>The process starts with a detailed discussion with the client to understand their idea & goals.</p>',
                '<p>We audit your current traffic funnel, patient avatar, and high-margin services to design the optimal conversion roadmap.</p>')
en = en.replace('<h3>02/ Brainstorming</h3>', '<h3>02/ Cinema Production & Dev</h3>')
en = en.replace('<p>Brainstorming is a group creativity technique in which members attempt to find a conclusion.</p>',
                '<p>We shoot on-site 4K video with Lumix S5 and engineer your high-speed web platform with integrated CRM in parallel.</p>')
en = en.replace('<h3>03/ Launch</h3>', '<h3>03/ Deployment & Lead Flow</h3>')
en = en.replace('<p>The completed design assets or final product are delivered with necessary documentation.</p>',
                '<p>We connect your custom domain, train your secretariat team on the CRM, and activate high-converting traffic funnels.</p>')

# Testimonials EN
en = en.replace('<h3>Super customer service!</h3>\n              <p>Excellent customer service and I was really impressed and happy with my purchase especially as it was a last minute order which got to me in time, and when it arrived I was very happy with the design and size and so was the recipient.</p>',
                '<h3>Doubled our consultation bookings!</h3>\n              <p>Ghaya Prod completely revolutionized our aesthetic practice. The Before/After slider and the 1-minute quiz pre-qualify our patients before they even text us on WhatsApp. Our secretary saves 2 hours every day.</p>')
en = en.replace('<p>William Jack <span>Founder@XYZ</span></p>', '<p>Dr. Hanane Kashi <span>Aesthetic Medicine, Casablanca</span></p>')

en = en.replace('''<h3>Exceptional creativity and vision</h3>\n              <p>Working Mthemeus was a game-changer for our brand. Their exceptional creativity & vision breathed new life into our visual. The logo they perfectly captures our essence & has become instantly recognizable. We couldn't be happier the results!</p>''',
                """<h3>Hollywood video quality on our ads!</h3>\n              <p>The difference between shooting on a phone and Ghaya Prod's Panasonic Lumix S5 setup is night and day. The colors, the crisp audio, and the fast-loading store decreased our cost per acquisition by 45%.</p>""")
en = en.replace('<p>Smith Align <span>Businessman</span></p>', '<p>Mehdi B. <span>E-Commerce & Brand Director</span></p>')

en = en.replace('<h3>Innovative and professional</h3>\n              <p>I can\'t say enough good things about them. Their team is not only incredibly talented but also highly professional. They listened to our ideas and brought to life in ways we couldn\'t have imagined. Their innovative approach and dedication to our project.</p>',
                '<h3>Seamless secretariat CRM integration</h3>\n              <p>The 1-click WhatsApp messaging templates and automated lead filtering changed everything for our staff. We never miss a patient follow-up, and our clinic revenue jumped within the first 30 days.</p>')
en = en.replace('<p>Milano Joe <span>Creative Director</span></p>', '<p>Kenza T. <span>Clinic Operations Manager</span></p>')

en = en.replace('<h3>Transformed our brand</h3>\n              <p>Our partnership with Mthemeus transformed our brand from ordinary to extraordinary. Their branding expertise and design work elevated our marketing materials to a whole new level. Our customers have taken notice, and boost in brand recognition.</p>',
                '<h3>High-status international presence</h3>\n              <p>Ghaya Prod built a trilingual platform that allowed our Canadian practice to attract high-ticket cosmetic patients seamlessly. Exceptional attention to speed, typography, and detail.</p>')
en = en.replace('<p>Danial Mark <span>Marketing Director</span></p>', '<p>Yassine E. <span>Private Clinic Director, Montreal</span></p>')

# Team Section EN
en = en.replace('<p>Creative Director</p>', '<p>Founder & Cinema Director</p>')
en = en.replace('<p>Senior Designer</p>', '<p>Lead Web Architect</p>')
en = en.replace('<p>Project Manager</p>', '<p>Lead Audio & Sound Engineer</p>')
en = en.replace('<p>Web Developer</p>', '<p>E-Commerce Funnel Specialist</p>')

# Pricing Table EN
PRICING_TABLE_EN = '''  <!-- Pricing Section (Interactive Table & Toggle) -->
  <div class="section aximo-section-padding" id="pricing">
    <div class="container">
      <div class="aximo-section-title center">
        <h2>
          Transparent investment
          <span class="aximo-title-animation">
            packages
            <span class="aximo-title-icon">
              <img src="assets/images/v1/star2.png" alt="">
            </span>
          </span>
        </h2>
      </div>
      <div class="pricing-btn">
        <label>Monthly Retainer</label>
        <div class="toggle-btn">
          <input class="form-check-input btn-toggle price-deck-trigger" type="checkbox" id="flexSwitchCheckDefault" data-pricing-trigger data-target="#table-price-value" checked>
        </div>
        <label>Single Project</label>
      </div>
      <div class="row" id="table-price-value" data-pricing-dynamic data-value-active="monthly">
        <div class="col-xl-4 col-md-6">
          <div class="aximo-pricing-wrap2 wow fadeInUpX" data-wow-delay="0.1s">
            <div class="aximo-pricing-header2">
              <h5>Web Platform & Funnel</h5>
            </div>
            <div class="aximo-pricing-price2">
              <h2>$</h2>
              <h2 class="aximo-price dynamic-value" data-active="790" data-monthly="790" data-yearly="950"></h2>
            </div>
            <div class="aximo-pricing-description">
              <p>Tailored high-converting web platform engineered for clinics, private practices & luxury brands.</p>
            </div>
            <div class="aximo-pricing-body2">
              <ul>
                <li><img src="assets/images/icon/check.svg" alt="">Strategic Avatar & Funnel Discovery</li>
                <li><img src="assets/images/icon/check.svg" alt="">Interactive Before/After Results Slider</li>
                <li><img src="assets/images/icon/check.svg" alt="">1-Minute Pre-Qualification Diagnostic Quiz</li>
                <li><img src="assets/images/icon/check.svg" alt="">Direct WhatsApp Consultation Integration</li>
                <li><img src="assets/images/icon/check.svg" alt="">Ultra-Fast Mobile Speed & Domain Setup</li>
              </ul>
            </div>
            <a class="aximo-pricing-btn2" href="#contact">Select this package</a>
          </div>
        </div>
        <div class="col-xl-4 col-md-6">
          <div class="aximo-pricing-wrap2 active wow fadeInUpX" data-wow-delay="0.2s">
            <div class="aximo-pricing-header2">
              <h5>4K Cinema & Video Ads</h5>
            </div>
            <div class="aximo-pricing-price2">
              <h2>$</h2>
              <h2 class="aximo-price dynamic-value" data-active="1290" data-monthly="1290" data-yearly="1490"></h2>
            </div>
            <div class="aximo-pricing-description">
              <p>Broadcast cinema production filmed on Panasonic Lumix S5 with professional audio & gimbal.</p>
            </div>
            <div class="aximo-pricing-body2">
              <ul>
                <li><img src="assets/images/icon/check.svg" alt="">Full-Day On-Site 4K Cinema Filming</li>
                <li><img src="assets/images/icon/check.svg" alt="">Broadcast Wireless Audio (Sennheiser/Shure)</li>
                <li><img src="assets/images/icon/check.svg" alt="">Cinematic Gimbal Stabilizer (DJI Ronin RS3)</li>
                <li><img src="assets/images/icon/check.svg" alt="">Color Grading in DaVinci Resolve Studio</li>
                <li><img src="assets/images/icon/check.svg" alt="">High-CTR Short-Form Reels & TikTok Ads</li>
              </ul>
            </div>
            <a class="aximo-pricing-btn2 active" href="#contact">Select this package</a>
          </div>
        </div>
        <div class="col-xl-4 col-md-6">
          <div class="aximo-pricing-wrap2 wow fadeInUpX" data-wow-delay="0.3s">
            <div class="aximo-pricing-header2">
              <h5>Full Domination Ecosystem</h5>
            </div>
            <div class="aximo-pricing-price2">
              <h2>$</h2>
              <h2 class="aximo-price dynamic-value" data-active="1890" data-monthly="1890" data-yearly="2200"></h2>
            </div>
            <div class="aximo-pricing-description">
              <p>Complete turnkey digital presence: Web platform, 4K cinema videos & Medical Secretariat CRM.</p>
            </div>
            <div class="aximo-pricing-body2">
              <ul>
                <li><img src="assets/images/icon/check.svg" alt="">Complete Custom Web Platform + Funnel</li>
                <li><img src="assets/images/icon/check.svg" alt="">4K Clinic Brand Commercial + 10 Short Reels</li>
                <li><img src="assets/images/icon/check.svg" alt="">Medical Secretariat CRM with Queue Studio</li>
                <li><img src="assets/images/icon/check.svg" alt="">1-Click WhatsApp Confirmation Templates</li>
                <li><img src="assets/images/icon/check.svg" alt="">Staff Training & 24/7 Dedicated Support</li>
              </ul>
            </div>
            <a class="aximo-pricing-btn2" href="#contact">Select this package</a>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- End Pricing section -->'''

en = en.replace(
    '<div class="section aximo-section-padding3" id="team">',
    f'{PRICING_TABLE_EN}\n\n  <div class="section aximo-section-padding3" id="team">'
)

# Footer EN
en = en.replace('&copy; Copyright 2024, All Rights Reserved by Mthemeus',
                '&copy; Copyright 2026, All Rights Reserved by Ghaya Prod Studio')
en = en.replace('(123) 456-7890', '+212 600 980 685')
en = en.replace('info@mthemeus.com', 'contact@ghayaprod.com')

(GHAYA_DIR / "en.html").write_text(en, encoding="utf-8")
print("✅ Saved English en.html (Secondary)")


# =========================================================================
# 2. BUILD FRENCH VERSION AS PRIMARY (index.html AND fr.html)
# =========================================================================
fr = en

fr = fr.replace(
    "<title>Ghaya Prod || High-Converting Web Platforms, E-Commerce & Cinema Production Studio</title>",
    "<title>Ghaya Prod || Écosystèmes Web Haute Conversion, E-Commerce & Production Cinéma 4K</title>"
)
fr = fr.replace('<html lang="en">', '<html lang="fr">')

# Language Switcher: FR | EN | AR (FR Active)
LANG_SWITCHER_FR = '''        <div class="d-flex align-items-center gap-3 ms-auto">
          <div class="lang-switcher d-flex gap-2 align-items-center" style="font-size: 13px; font-weight: 700; background: rgba(255,255,255,0.08); padding: 6px 14px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.18);">
            <a href="index.html" style="color: #BFF747; text-decoration: none;">FR</a>
            <span style="color: rgba(255,255,255,0.3);">|</span>
            <a href="en.html" style="color: #fff; text-decoration: none;">EN</a>
            <span style="color: rgba(255,255,255,0.3);">|</span>
            <a href="ar.html" style="color: #fff; text-decoration: none;">AR</a>
          </div>
          <div class="header-btn header-btn-l1 d-none d-xs-inline-flex">
            <a class="aximo-default-btn pill aximo-header-btn" href="#contact">
              Contactez-Nous
            </a>
          </div>
        </div>'''
fr = re.sub(r'<div class="d-flex align-items-center gap-3 ms-auto">[\s\S]*?</div>\s*</div>\s*</div>',
            f'{LANG_SWITCHER_FR}\n        </div>', fr, count=1)

# Nav Menu French
NAV_MENU_FR = '''<ul class="site-menu-main">
              <li class="nav-item">
                <a href="#services" class="nav-link-item">Services</a>
              </li>
              <li class="nav-item">
                <a href="#portfolio" class="nav-link-item">Réalisations</a>
              </li>
              <li class="nav-item">
                <a href="#process" class="nav-link-item">Méthode</a>
              </li>
              <li class="nav-item">
                <a href="#pricing" class="nav-link-item">Tarifs</a>
              </li>
              <li class="nav-item">
                <a href="#testimonials" class="nav-link-item">Témoignages</a>
              </li>
              <li class="nav-item">
                <a href="#team" class="nav-link-item">Équipe</a>
              </li>
              <li class="nav-item nav-item-has-children">
                <a href="#" class="nav-link-item drop-trigger">Pages <i class="fas fa-angle-down"></i></a>
                <ul class="sub-menu" id="submenu-pages">
                  <li class="sub-menu--item">
                    <a href="about-us.html"><span class="menu-item-text">À Propos</span></a>
                  </li>
                  <li class="sub-menu--item">
                    <a href="pricing.html"><span class="menu-item-text">Nos Tarifs</span></a>
                  </li>
                  <li class="sub-menu--item">
                    <a href="service.html"><span class="menu-item-text">Services Détaillés</span></a>
                  </li>
                  <li class="sub-menu--item">
                    <a href="portfolio-01.html"><span class="menu-item-text">Galerie Portfolio</span></a>
                  </li>
                  <li class="sub-menu--item">
                    <a href="team.html"><span class="menu-item-text">Notre Équipe</span></a>
                  </li>
                  <li class="sub-menu--item">
                    <a href="faq.html"><span class="menu-item-text">FAQ</span></a>
                  </li>
                  <li class="sub-menu--item">
                    <a href="testimonial.html"><span class="menu-item-text">Avis Clients</span></a>
                  </li>
                  <li class="sub-menu--item">
                    <a href="contact-us.html"><span class="menu-item-text">Contactez-Nous</span></a>
                  </li>
                </ul>
              </li>
              <li class="nav-item">
                <a href="#contact" class="nav-link-item">Contact</a>
              </li>
            </ul>
          </nav>'''
fr = re.sub(r'<ul class="site-menu-main">[\s\S]*?</ul>\s*</nav>', NAV_MENU_FR, fr, count=1)

# Hero FR
fr = fr.replace(
    'High-converting\n                <img src="assets/images/v1/star.png" alt="">\n              </span>\n              web & cinema studio',
    'Écosystèmes web\n                <img src="assets/images/v1/star.png" alt="">\n              </span>\n              & production cinéma'
)
fr = fr.replace(
    "We build high-converting web platforms, high-ROI e-commerce stores, and produce broadcast 4K cinema video for aesthetic clinics, private practices, and high-ticket service brands.",
    "Nous concevons des plateformes web haute conversion, des boutiques e-commerce à fort ROI et produisons des vidéos cinéma 4K pour cabinets médicaux, cliniques et marques d'élite."
)
fr = fr.replace("Book a strategy consultation", "Réserver un audit stratégique")
fr = fr.replace("Trusted by 1,000+ community & business leaders", "Plus de 1 000 abonnés et professionnels nous font confiance")

# Services Section Header FR
fr = fr.replace('We provide effective\n          <span class="aximo-title-animation">\n            design solutions',
                'Nous développons des\n          <span class="aximo-title-animation">\n            solutions digitales d\'élite')
fr = fr.replace('<h3>Web Platforms & Portfolios</h3>\n                <p>Architecting custom, ultra-fast websites and portfolio platforms tailored for aesthetic clinics, doctors, and high-status creative agencies.</p>',
                '<h3>Plateformes Web & Portfolios</h3>\n                <p>Création de sites ultra-rapides et plateformes portfolios sur-mesure pour cliniques esthétiques, médecins et marques d\'autorité.</p>')
fr = fr.replace('<h3>E-Commerce & COD Stores</h3>\n                <p>High-converting e-commerce stores with optimized checkout funnels, fast mobile landing pages, and automated order tracking systems.</p>',
                '<h3>Boutiques E-Commerce & COD</h3>\n                <p>Stores e-commerce à forte conversion avec tunnels de commande optimisés pour le mobile et suivi automatisé des commandes.</p>')
fr = fr.replace('<h3>4K Cinema Video Production</h3>\n                <p>Shot on Panasonic Lumix S5 Full-Frame cinema camera with broadcast Sennheiser/Shure audio and Ronin RS3 gimbal stabilization for clinical prestige.</p>',
                '<h3>Production Vidéo Cinéma 4K</h3>\n                <p>Tourné sur Panasonic Lumix S5 plein format, micros broadcast Sennheiser/Shure et stabilisateur DJI Ronin pour un rendu prestigieux.</p>')
fr = fr.replace('<h3>High-CTR Short-Form Video</h3>\n                <p>Psychologically engineered Reels and TikTok ad creatives edited in CapCut Pro with viral pacing to convert cold traffic into paying consultations.</p>',
                '<h3>Reels & Publicités à Fort Clic</h3>\n                <p>Scripts persuasifs, montage dynamique CapCut Pro et sous-titrage moderne conçus pour transformer le trafic payant en consultations réelles.</p>')

# Section Counter & Video FR
fr = fr.replace('We make your\n                <span class="aximo-title-icon">\n                  <img src="assets/images/v1/star2.png" alt="">\n                </span>\n              </span>\n              business stand out',
                'Propulsez votre\n                <span class="aximo-title-icon">\n                  <img src="assets/images/v1/star2.png" alt="">\n                </span>\n              </span>\n              cabinet au sommet')
fr = fr.replace('We fuse Hollywood-grade camera production with modern conversion rate optimization to turn viewers into high-ticket clients.',
                'Nous allions la qualité d\'une caméra de cinéma à l\'optimisation de conversion web pour faire de chaque visiteur un client fidèle.')
fr = fr.replace('Years of creative excellence', 'Années d\'excellence créative')
fr = fr.replace('Targeted campaigns deployed', 'Campagnes ciblées déployées')
fr = fr.replace('Client satisfaction rate', 'Taux de satisfaction partenaires')

# Portfolio Section Title & Projects FR
fr = fr.replace('Have a wide range of\n          <span class="aximo-title-animation">\n            creative projects',
                'Découvrez nos projets\n          <span class="aximo-title-animation">\n            et réalisations d\'élite')
fr = fr.replace('<h3>Dr. Hanane Kashi Aesthetic Clinic</h3>\n                </a>\n                <p>Bilingual facial injection clinic platform with interactive Before/After comparison and 1-minute diagnostic quiz.</p>',
                '<h3>Clinique Esthétique Dr. Hanane Kashi</h3>\n                </a>\n                <p>Plateforme bilingue avec comparateur Avant/Après interactif et diagnostic médical en 1 minute.</p>')
fr = fr.replace('<h3>Luxury Cabinet & Corporate Identity</h3>\n                </a>\n                <p>Complete office 3D gold monogram signage, branding kit, and high-status visual design for Casablanca aesthetic doctor.</p>',
                '<h3>Cabinet de Luxe & Monogramme 3D</h3>\n                </a>\n                <p>Enseigne murale 3D dorée, identité visuelle complète et direction artistique pour cabinet esthétique à Casablanca.</p>')
fr = fr.replace('<h3>Medical Secretariat CRM Dashboard</h3>\n                </a>\n                <p>Private multi-factor patient queue, revenue analytics, and 1-click WhatsApp appointment confirmation studio.</p>',
                '<h3>Tableau de Bord CRM Secrétariat</h3>\n                </a>\n                <p>File de patientes privée, statistiques de chiffre d\'affaires et confirmations WhatsApp en 1 clic.</p>')
fr = fr.replace('<h3>Clinical Video Case Consultation</h3>\n                </a>\n                <p>On-camera consultation and procedural breakdown filmed with wireless broadcast mics for patient Zineb testimonial.</p>',
                '<h3>Vidéo Consultation Clinique Réelle</h3>\n                </a>\n                <p>Explication clinique filmée en 4K avec micros sans fil broadcast pour le témoignage patiente Zineb.</p>')

# Ticker Marquee FR
fr = fr.replace("Let's create new experiences", "CRÉER DES EXPÉRIENCES UNIQUES")

# Process FR
fr = fr.replace('Our high-quality\n                  <span class="aximo-title-icon">\n                    <img src="assets/images/v1/star2.png" alt="">\n                  </span>\n                </span>\n                working processes',
                'Notre processus\n                  <span class="aximo-title-icon">\n                    <img src="assets/images/v1/star2.png" alt="">\n                  </span>\n                </span>\n                de production éprouvé')
fr = fr.replace('We focus at every stage on effective communication and collaboration between the client and ensuring that the final design meets the client\'s objectives and expectations.',
                'Nous accompagnons chaque étape avec une communication fluide et rigoureuse pour garantir des résultats concrets à la hauteur de vos ambitions.')
fr = fr.replace('It is important to note that these are simplified steps, and the actual work process may vary depending on the complexity of the project.',
                'Chaque projet bénéficie d\'une feuille de route sur-mesure adaptée aux spécificités de votre secteur et de votre patientèle cible.')
fr = fr.replace('<h3>01/ Strategic Discovery</h3>', '<h3>01/ Diagnostic Stratégique</h3>')
fr = fr.replace('<p>We audit your current traffic funnel, patient avatar, and high-margin services to design the optimal conversion roadmap.</p>',
                '<p>Nous analysons votre audience cible, vos soins les plus rentables et votre tunnel actuel pour bâtir la stratégie gagnante.</p>')
fr = fr.replace('<h3>02/ Cinema Production & Dev</h3>', '<h3>02/ Tournage Cinéma & Dev</h3>')
fr = fr.replace('<p>We shoot on-site 4K video with Lumix S5 and engineer your high-speed web platform with integrated CRM in parallel.</p>',
                '<p>Nous tournons vos vidéos 4K au cabinet avec la Lumix S5 et développons simultanément votre plateforme web et CRM.</p>')
fr = fr.replace('<h3>03/ Deployment & Lead Flow</h3>', '<h3>03/ Déploiement & Résultats</h3>')
fr = fr.replace('<p>We connect your custom domain, train your secretariat team on the CRM, and activate high-converting traffic funnels.</p>',
                '<p>Mise en ligne sur votre nom de domaine officiel, formation de votre secrétariat au CRM et activation des flux de réservation.</p>')

# Testimonials Title & Cards FR
fr = fr.replace('Clients are always\n            <span class="aximo-title-animation">\n              satisfied with us',
                'Nos partenaires témoignent\n            <span class="aximo-title-animation">\n              de leur réussite')
fr = fr.replace('<h3>Doubled our consultation bookings!</h3>\n              <p>Ghaya Prod completely revolutionized our aesthetic practice. The Before/After slider and the 1-minute quiz pre-qualify our patients before they even text us on WhatsApp. Our secretary saves 2 hours every day.</p>',
                '<h3>Réservations de consultations doublées !</h3>\n              <p>Ghaya Prod a révolutionné notre cabinet esthétique. Le comparateur Avant/Après et le questionnaire médical pré-qualifient les patientes avant même leur premier message WhatsApp. Notre secrétariat gagne plus de 2 heures par jour.</p>')
fr = fr.replace('<h3>Hollywood video quality on our ads!</h3>\n              <p>The difference between shooting on a phone and Ghaya Prod\'s Panasonic Lumix S5 setup is night and day. The colors, the crisp audio, and the fast-loading store decreased our cost per acquisition by 45%.</p>',
                '<h3>Qualité vidéo cinéma sur nos publicités !</h3>\n              <p>La différence entre un tournage au téléphone et l\'équipement Panasonic Lumix S5 de Ghaya Prod est saisissante. Les couleurs, la clarté du son et la boutique ultra-rapide ont fait chuter notre coût par acquisition de 45%.</p>')
fr = fr.replace('<h3>Seamless secretariat CRM integration</h3>\n              <p>The 1-click WhatsApp messaging templates and automated lead filtering changed everything for our staff. We never miss a patient follow-up, and our clinic revenue jumped within the first 30 days.</p>',
                '<h3>Intégration fluide de notre secrétariat au CRM</h3>\n              <p>Les modèles de messages WhatsApp en 1 clic et le filtrage automatisé des demandes ont tout changé pour notre équipe. Nous ne perdons plus aucun patient et les revenus du cabinet ont grimpé dès le premier mois.</p>')
fr = fr.replace('<h3>High-status international presence</h3>\n              <p>Ghaya Prod built a trilingual platform that allowed our Canadian practice to attract high-ticket cosmetic patients seamlessly. Exceptional attention to speed, typography, and detail.</p>',
                '<h3>Une présence internationale haut de gamme</h3>\n              <p>Ghaya Prod a conçu un écosystème trilingue permettant à notre clinique d\'attirer une patientèle cosmétique haut de gamme. Une maîtrise remarquable de la vitesse, de la typographie et du détail.</p>')

# Pricing Table FR
fr = fr.replace("Transparent investment\n          <span class=\"aximo-title-animation\">\n            packages",
                "Des formules d'investissement\n          <span class=\"aximo-title-animation\">\n            transparentes et rentables")
fr = fr.replace("<label>Monthly Retainer</label>", "<label>Accompagnement Mensuel</label>")
fr = fr.replace("<label>Single Project</label>", "<label>Projet Unique</label>")
fr = fr.replace("<h5>Web Platform & Funnel</h5>", "<h5>Plateforme Web & Funnel</h5>")
fr = fr.replace("<p>Tailored high-converting web platform engineered for clinics, private practices & luxury brands.</p>",
                "<p>Plateforme web haute conversion sur-mesure pour cabinets médicaux, cliniques et marques de prestige.</p>")
fr = fr.replace("Strategic Avatar & Funnel Discovery", "Diagnostic Stratégique & Persona Idéal")
fr = fr.replace("Interactive Before/After Results Slider", "Comparateur Interactif Avant/Après")
fr = fr.replace("1-Minute Pre-Qualification Diagnostic Quiz", "Questionnaire Médical Diagnostic en 1 Min")
fr = fr.replace("Direct WhatsApp Consultation Integration", "Intégration WhatsApp Directe avec Modèles")
fr = fr.replace("Ultra-Fast Mobile Speed & Domain Setup", "Vitesse Mobile Maximale & Nom de Domaine")

fr = fr.replace("<h5>4K Cinema & Video Ads</h5>", "<h5>Production Cinéma 4K & Vidéos</h5>")
fr = fr.replace("<p>Broadcast cinema production filmed on Panasonic Lumix S5 with professional audio & gimbal.</p>",
                "<p>Tournage cinéma broadcast sur Panasonic Lumix S5 avec micros professionnels et stabilisateur.</p>")
fr = fr.replace("Full-Day On-Site 4K Cinema Filming", "Journée Complète de Tournage au Cabinet (4K)")
fr = fr.replace("Broadcast Wireless Audio (Sennheiser/Shure)", "Audio Sans Fil Broadcast (Sennheiser/Shure)")
fr = fr.replace("Cinematic Gimbal Stabilizer (DJI Ronin RS3)", "Stabilisation Fluide sur Gimbal DJI Ronin RS3")
fr = fr.replace("Color Grading in DaVinci Resolve Studio", "Étalonnage Cinéma sur DaVinci Resolve Studio")
fr = fr.replace("High-CTR Short-Form Reels & TikTok Ads", "Reels & Publicités TikTok à Fort Taux de Clic")

fr = fr.replace("<h5>Full Domination Ecosystem</h5>", "<h5>Écosystème Domination Totale</h5>")
fr = fr.replace("<p>Complete turnkey digital presence: Web platform, 4K cinema videos & Medical Secretariat CRM.</p>",
                "<p>Solution clé en main complète : Plateforme web, vidéos cinéma 4K et CRM secrétariat médical.</p>")
fr = fr.replace("Complete Custom Web Platform + Funnel", "Plateforme Web Complète + Tunnels de Vente")
fr = fr.replace("4K Clinic Brand Commercial + 10 Short Reels", "Film Publicitaire 4K + 10 Reels Courts")
fr = fr.replace("Medical Secretariat CRM with Queue Studio", "CRM Secrétariat Médical avec Studio de File")
fr = fr.replace("1-Click WhatsApp Confirmation Templates", "Modèles WhatsApp de Confirmation en 1 Clic")
fr = fr.replace("Staff Training & 24/7 Dedicated Support", "Formation du Personnel & Support Dédié 24/7")
fr = fr.replace("Select this package", "Choisir cette formule")

# Team Section FR
fr = fr.replace('We have a team of\n          <span class="aximo-title-animation">\n            creative people',
                'Une équipe d\'experts\n          <span class="aximo-title-animation">\n            et de créateurs passionnés')
fr = fr.replace('<p>Founder & Cinema Director</p>', '<p>Fondateur & Réalisateur Cinéma</p>')
fr = fr.replace('<p>Lead Web Architect</p>', '<p>Architecte Web & Systèmes CRM</p>')
fr = fr.replace('<p>Lead Audio & Sound Engineer</p>', '<p>Ingénieur Son & Audio Broadcast</p>')
fr = fr.replace('<p>E-Commerce Funnel Specialist</p>', '<p>Spécialiste Tunnels E-Commerce</p>')

# Footer FR
fr = fr.replace("Let's start a \n                  <span class=\"aximo-title-icon\">\n                    <img src=\"assets/images/v1/star2.png\" alt=\"\">\n                  </span>\n                </span>\n                project together",
                "Donnons vie à\n                  <span class=\"aximo-title-icon\">\n                    <img src=\"assets/images/v1/star2.png\" alt=\"\">\n                  </span>\n                </span>\n                votre prochain projet")
fr = fr.replace("We work closely with our clients to understand their objectives, target audience, and unique needs. We use our creative skills to translate these requirements and practical design solutions.",
                "Nous collaborons étroitement avec nos clients pour comprendre leurs objectifs, leur public cible et leurs besoins uniques. Nous transformons ces exigences en solutions de design et de conversion prestigieuses.")
fr = fr.replace("Give us a call:", "Appelez-nous directement :")
fr = fr.replace("Send us an email:", "Écrivez-nous par e-mail :")
fr = fr.replace("Send us a message", "Envoyez-nous un message")
fr = fr.replace("Your name", "Votre nom complet")
fr = fr.replace("Your email address", "Votre adresse e-mail")
fr = fr.replace("Write your message here...", "Décrivez votre projet ou vos besoins...")
fr = fr.replace("Send message", "Envoyer la demande")

# Write index.html (FRENCH AS PRIMARY)
(GHAYA_DIR / "index.html").write_text(fr, encoding="utf-8")
print("✅ Saved French index.html (PRIMARY HOMEPAGE)")

# Write fr.html (DUPLICATE OF FRENCH HOMEPAGE)
(GHAYA_DIR / "fr.html").write_text(fr, encoding="utf-8")
print("✅ Saved French fr.html (Direct FR Link)")


# =========================================================================
# 3. BUILD ARABIC VERSION (ar.html - RTL)
# =========================================================================
ar = en

ar = ar.replace(
    "<title>Ghaya Prod || High-Converting Web Platforms, E-Commerce & Cinema Production Studio</title>",
    "<title>غاية برود || منصات الويب عالية التحويل، المتاجر الإلكترونية والإنتاج السينمائي 4K</title>"
)
ar = ar.replace('<html lang="en">', '<html lang="ar" dir="rtl">')

# Add Cairo font & RTL CSS
ar_font_patch = '''  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Cairo', 'Syne', sans-serif !important; text-align: right; }
    .site-menu-main { text-align: right; }
    .aximo-iconbox-data { text-align: right; }
    .aximo-default-content { text-align: right; }
    .aximo-testimonial-data { text-align: right; }
    .aximo-hero-content { text-align: right; }
    .aximo-hero-content h1 { text-align: right; }
    .aximo-section-title { text-align: right; }
    .aximo-section-title.center { text-align: center; }
  </style>'''
ar = ar.replace('</head>', f'{ar_font_patch}\n</head>')

# Language Switcher: FR | EN | AR (AR Active)
LANG_SWITCHER_AR = '''        <div class="d-flex align-items-center gap-3 ms-auto">
          <div class="lang-switcher d-flex gap-2 align-items-center" style="font-size: 13px; font-weight: 700; background: rgba(255,255,255,0.08); padding: 6px 14px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.18);">
            <a href="index.html" style="color: #fff; text-decoration: none;">FR</a>
            <span style="color: rgba(255,255,255,0.3);">|</span>
            <a href="en.html" style="color: #fff; text-decoration: none;">EN</a>
            <span style="color: rgba(255,255,255,0.3);">|</span>
            <a href="ar.html" style="color: #BFF747; text-decoration: none;">AR</a>
          </div>
          <div class="header-btn header-btn-l1 d-none d-xs-inline-flex">
            <a class="aximo-default-btn pill aximo-header-btn" href="#contact">
              ابدأ مشروعك
            </a>
          </div>
        </div>'''
ar = re.sub(r'<div class="d-flex align-items-center gap-3 ms-auto">[\s\S]*?</div>\s*</div>\s*</div>',
            f'{LANG_SWITCHER_AR}\n        </div>', ar, count=1)

# Arabic Navigation
NAV_MENU_AR = '''<ul class="site-menu-main">
              <li class="nav-item">
                <a href="#services" class="nav-link-item">خدماتنا</a>
              </li>
              <li class="nav-item">
                <a href="#portfolio" class="nav-link-item">أعمالنا</a>
              </li>
              <li class="nav-item">
                <a href="#process" class="nav-link-item">منهجيتنا</a>
              </li>
              <li class="nav-item">
                <a href="#pricing" class="nav-link-item">باقاتنا</a>
              </li>
              <li class="nav-item">
                <a href="#testimonials" class="nav-link-item">آراء العملاء</a>
              </li>
              <li class="nav-item">
                <a href="#team" class="nav-link-item">فريقنا</a>
              </li>
              <li class="nav-item">
                <a href="#contact" class="nav-link-item">تواصل معنا</a>
              </li>
            </ul>
          </nav>'''
ar = re.sub(r'<ul class="site-menu-main">[\s\S]*?</ul>\s*</nav>', NAV_MENU_AR, ar, count=1)

# Hero AR
ar = ar.replace(
    'High-converting\n                <img src="assets/images/v1/star.png" alt="">\n              </span>\n              web & cinema studio',
    'منصات رقمية فائقة\n                <img src="assets/images/v1/star.png" alt="">\n              </span>\n              وإنتاج سينمائي مبهر'
)
ar = ar.replace(
    "We build high-converting web platforms, high-ROI e-commerce stores, and produce broadcast 4K cinema video for aesthetic clinics, private practices, and high-ticket service brands.",
    "نصمم منظومات ويب عالية التحويل، ومتاجر إلكترونية بمعدلات ربح قياسية، وننتج فيديوهات سينمائية بدقة 4K لعيادات التجميل، المراكز الطبية والعلامات التجارية الراقية."
)
ar = ar.replace("Book a strategy consultation", "حجز استشارة استراتيجية")
ar = ar.replace("Trusted by 1,000+ community & business leaders", "أكثر من 1,000 متابع وشريك نجاح يثقون في أعمالنا")

# Services Section Header AR
ar = ar.replace('We provide effective\n          <span class="aximo-title-animation">\n            design solutions',
                'نبتكر حلولاً رقمية\n          <span class="aximo-title-animation">\n            سينمائية واستثنائية')
ar = ar.replace('<h3>Web Platforms & Portfolios</h3>\n                <p>Architecting custom, ultra-fast websites and portfolio platforms tailored for aesthetic clinics, doctors, and high-status creative agencies.</p>',
                '<h3>منصات الويب ومواقع البورتفوليو</h3>\n                <p>بناء مواقع سريعة وفائقة الهيبة مخصصة لعيادات التجميل، الأطباء، ومقدمي الخدمات الحصرية في المغرب والعالم.</p>')
ar = ar.replace('<h3>E-Commerce & COD Stores</h3>\n                <p>High-converting e-commerce stores with optimized checkout funnels, fast mobile landing pages, and automated order tracking systems.</p>',
                '<h3>متاجر التجارة الإلكترونية والدفع عند الاستلام</h3>\n                <p>متاجر احترافية مهيأة لتحقيق أعلى معدل تحويل مع صفحات هبوط للهواتف ونظام تتبع وإدارة الطلبات بسلاسة.</p>')
ar = ar.replace('<h3>4K Cinema Video Production</h3>\n                <p>Shot on Panasonic Lumix S5 Full-Frame cinema camera with broadcast Sennheiser/Shure audio and Ronin RS3 gimbal stabilization for clinical prestige.</p>',
                '<h3>إنتاج مرئي سينمائي بدقة 4K</h3>\n                <p>تصوير بكاميرا Panasonic Lumix S5 ذات الحساس الكامل، ومايكروفونات إذاعية Sennheiser/Shure ومانع اهتزاز رونين للهيبة الطبية.</p>')
ar = ar.replace('<h3>High-CTR Short-Form Video</h3>\n                <p>Psychologically engineered Reels and TikTok ad creatives edited in CapCut Pro with viral pacing to convert cold traffic into paying consultations.</p>',
                '<h3>ريلز وفيديوهات قصيرة عالية النقرات</h3>\n                <p>سيناريوهات تسويقية مقنعة ومونتاج ديناميكي عبر CapCut Pro لتحويل المشاهدات إلى مواعيد فعلية واستشارات مؤكدة.</p>')

# Section Counter & Video AR
ar = ar.replace('We make your\n                <span class="aximo-title-icon">\n                  <img src="assets/images/v1/star2.png" alt="">\n                </span>\n              </span>\n              business stand out',
                'نرتقي بحضورك\n                <span class="aximo-title-icon">\n                  <img src="assets/images/v1/star2.png" alt="">\n                </span>\n              </span>\n              إلى القمة المطلقة')
ar = ar.replace('We fuse Hollywood-grade camera production with modern conversion rate optimization to turn viewers into high-ticket clients.',
                'ندمج بين معايير الكاميرات السينمائية العالمية وهندسة الويب المتقدمة لتحويل المشاهدين إلى عملاء دائمين.')
ar = ar.replace('Years of creative excellence', 'سنوات من التميز والإتقان')
ar = ar.replace('Targeted campaigns deployed', 'حملات ناجحة تم إطلاقها')
ar = ar.replace('Client satisfaction rate', 'نسبة رضا الشركاء والعملاء')

# Portfolio Section AR
ar = ar.replace('Have a wide range of\n          <span class="aximo-title-animation">\n            creative projects',
                'استكشف نماذج\n          <span class="aximo-title-animation">\n            من أبرز أعمالنا ومشاريعنا')
ar = ar.replace('<h3>Dr. Hanane Kashi Aesthetic Clinic</h3>\n                </a>\n                <p>Bilingual facial injection clinic platform with interactive Before/After comparison and 1-minute diagnostic quiz.</p>',
                '<h3>عيادة الدكتورة حنان كاشي للتجميل</h3>\n                </a>\n                <p>منصة رقمية ثنائية اللغة لحقن وتجميل الوجه مع مقارنة تفاعلية قبل/بعد واختبار تشخيصي في دقيقة واحدة.</p>')
ar = ar.replace('<h3>Luxury Cabinet & Corporate Identity</h3>\n                </a>\n                <p>Complete office 3D gold monogram signage, branding kit, and high-status visual design for Casablanca aesthetic doctor.</p>',
                '<h3>شعار وهوية بصرية ذهبية ثلاثية الأبعاد</h3>\n                </a>\n                <p>شعار مونوغرام ذهبي فاخر، لوحات عيادة متطورة وهوية بصرية كاملة لطبيبة تجميل بالدار البيضاء.</p>')
ar = ar.replace('<h3>Medical Secretariat CRM Dashboard</h3>\n                </a>\n                <p>Private multi-factor patient queue, revenue analytics, and 1-click WhatsApp appointment confirmation studio.</p>',
                '<h3>لوحة تحكم CRM لسكرتارية العيادة</h3>\n                </a>\n                <p>نظام إدارة المواعيد، تتبع المداخيل، واستوديو تأكيد الحجوزات عبر واتساب بنقرة واحدة.</p>')
ar = ar.replace('<h3>Clinical Video Case Consultation</h3>\n                </a>\n                <p>On-camera consultation and procedural breakdown filmed with wireless broadcast mics for patient Zineb testimonial.</p>',
                '<h3>فيديو سينمائي لاستشارة وحالة حقيقية</h3>\n                </a>\n                <p>تصوير استشارة طبية مباشرة وشرح خطة العلاج بكاميرا 4K ومايكات إذاعية للمريضة زينب.</p>')

# Ticker Marquee AR
ar = ar.replace("Let's create new experiences", "نصنع تجارب استثنائية تلهم العالم")

# Process AR
ar = ar.replace('Our high-quality\n                  <span class="aximo-title-icon">\n                    <img src="assets/images/v1/star2.png" alt="">\n                  </span>\n                </span>\n                working processes',
                'منهجية عملنا\n                  <span class="aximo-title-icon">\n                    <img src="assets/images/v1/star2.png" alt="">\n                  </span>\n                </span>\n                الاحترافية المتكاملة')
ar = ar.replace('<h3>01/ Strategic Discovery</h3>', '<h3>01/ دراسة الهدف والجمهور</h3>')
ar = ar.replace('<p>We audit your current traffic funnel, patient avatar, and high-margin services to design the optimal conversion roadmap.</p>',
                '<p>نحلل مسار المبيعات الحالي وطبيعة الجمهور المستهدف لتحديد أنسب استراتيجية لرفع الحجوزات والمبيعات.</p>')
ar = ar.replace('<h3>02/ Cinema Production & Dev</h3>', '<h3>02/ التصوير والبرمجة المتزامنة</h3>')
ar = ar.replace('<p>We shoot on-site 4K video with Lumix S5 and engineer your high-speed web platform with integrated CRM in parallel.</p>',
                '<p>جلسة تصوير سينمائي مباشر بكاميرا Lumix S5 مع برمجة وتطوير المنصة الرقمية ولوحة الـ CRM في نفس الوقت.</p>')
ar = ar.replace('<h3>03/ Deployment & Lead Flow</h3>', '<h3>03/ الإطلاق وحصد النتائج</h3>')
ar = ar.replace('<p>We connect your custom domain, train your secretariat team on the CRM, and activate high-converting traffic funnels.</p>',
                '<p>ربط النطاق الرسمي، تدريب فريق السكرتارية على لوحة التحكم، وإطلاق الحملات لاستقبال الزوار والمريضات.</p>')

# Pricing Table AR
ar = ar.replace("Transparent investment\n          <span class=\"aximo-title-animation\">\n            packages",
                "باقات استثمارية واضحة\n          <span class=\"aximo-title-animation\">\n            وعالية العائد")
ar = ar.replace("<label>Monthly Retainer</label>", "<label>اشتراك شهري مستمر</label>")
ar = ar.replace("<label>Single Project</label>", "<label>مشروع متكامل لمرة واحدة</label>")
ar = ar.replace("<h5>Web Platform & Funnel</h5>", "<h5>منظومة الويب ومسار التحويل</h5>")
ar = ar.replace("<p>Tailored high-converting web platform engineered for clinics, private practices & luxury brands.</p>",
                "<p>منصة ويب سريعة مخصصة لعيادات التجميل، الأطباء والعلامات التجارية الراقية.</p>")
ar = ar.replace("Strategic Avatar & Funnel Discovery", "دراسة الجمهور والخدمات الأكثر ربحية")
ar = ar.replace("Interactive Before/After Results Slider", "شريط تفاعلي لمقارنة الصور قبل وبعد العلاج")
ar = ar.replace("1-Minute Pre-Qualification Diagnostic Quiz", "اختبار طبي تفاعلي لتأهيل المرضى في دقيقة")
ar = ar.replace("Direct WhatsApp Consultation Integration", "ربط مباشر مع واتساب لتأكيد الحجوزات")
ar = ar.replace("Ultra-Fast Mobile Speed & Domain Setup", "سرعة فائقة للهواتف وربط النطاق الرسمي")

ar = ar.replace("<h5>4K Cinema & Video Ads</h5>", "<h5>إنتاج سينمائي 4K وإعلانات فيديو</h5>")
ar = ar.replace("<p>Broadcast cinema production filmed on Panasonic Lumix S5 with professional audio & gimbal.</p>",
                "<p>تصوير بكاميرا سينمائية كاملة الإطار Lumix S5 ومايكات إذاعية ومانع اهتزاز رونين.</p>")
ar = ar.replace("Full-Day On-Site 4K Cinema Filming", "يوم تصوير كامل في مقر عيادتك بدقة 4K")
ar = ar.replace("Broadcast Wireless Audio (Sennheiser/Shure)", "تسجيل صوتي إذاعي نقي (Sennheiser/Shure)")
ar = ar.replace("Cinematic Gimbal Stabilizer (DJI Ronin RS3)", "لقطات سينمائية بمانع اهتزاز DJI Ronin RS3")
ar = ar.replace("Color Grading in DaVinci Resolve Studio", "تلوين سينمائي فاخر عبر DaVinci Resolve")
ar = ar.replace("High-CTR Short-Form Reels & TikTok Ads", "ريلز وفيديوهات تيك توك مصممة لتحقيق أعلى نسبة نقر")

ar = ar.replace("<h5>Full Domination Ecosystem</h5>", "<h5>منظومة السيطرة والريادة الشاملة</h5>")
ar = ar.replace("<p>Complete turnkey digital presence: Web platform, 4K cinema videos & Medical Secretariat CRM.</p>",
                "<p>حل شامل وجاهز: منصة ويب، فيديوهات سينمائية 4K ونظام CRM لسكرتارية العيادة.</p>")
ar = ar.replace("Complete Custom Web Platform + Funnel", "منصة ويب متكاملة مع صفحات هبوط مخصصة")
ar = ar.replace("4K Clinic Brand Commercial + 10 Short Reels", "فيلم ترويجي سينمائي + 10 فيديوهات ريلز قصيرة")
ar = ar.replace("Medical Secretariat CRM with Queue Studio", "نظام CRM لإدارة المواعيد وتتبع طلبات الحجز")
ar = ar.replace("1-Click WhatsApp Confirmation Templates", "قوالب رسائل واتساب جاهزة للتأكيد بنقرة واحدة")
ar = ar.replace("Staff Training & 24/7 Dedicated Support", "تدريب فريق السكرتارية ودعم فني مخصص 24/7")
ar = ar.replace("Select this package", "اختر هذه الباقة الآن")

# Team Section AR
ar = ar.replace('We have a team of\n          <span class="aximo-title-animation">\n            creative people',
                'فريق متكامل من\n          <span class="aximo-title-animation">\n            المبدعين والمحترفين')
ar = ar.replace('<p>Founder & Cinema Director</p>', '<p>المؤسس والمخرج السينمائي</p>')
ar = ar.replace('<p>Lead Web Architect</p>', '<p>كبير مهندسي الويب وأنظمة CRM</p>')
ar = ar.replace('<p>Lead Audio & Sound Engineer</p>', '<p>مهندس الصوت والإنتاج الإذاعي</p>')
ar = ar.replace('<p>E-Commerce Funnel Specialist</p>', '<p>خبير مسارات التجارة الإلكترونية</p>')

# Footer AR
ar = ar.replace("Let's start a \n                  <span class=\"aximo-title-icon\">\n                    <img src=\"assets/images/v1/star2.png\" alt=\"\">\n                  </span>\n                </span>\n                project together",
                "فلنبدأ صناعة\n                  <span class=\"aximo-title-icon\">\n                    <img src=\"assets/images/v1/star2.png\" alt=\"\">\n                  </span>\n                </span>\n                مشروعك القادم معاً")
ar = ar.replace("Send us a message", "تواصل معنا مباشرة")
ar = ar.replace("Your name", "الاسم الكامل")
ar = ar.replace("Your email address", "البريد الإلكتروني")
ar = ar.replace("Write your message here...", "أخبرنا بتفاصيل مشروعك...")
ar = ar.replace("Send message", "إرسال الرسالة الآن")

(GHAYA_DIR / "ar.html").write_text(ar, encoding="utf-8")
print("✅ Saved Arabic ar.html (Tertiary RTL)")


# =========================================================================
# 4. UPDATE SUBPAGES WITH [ FR | EN | AR ] LANGUAGE SWITCHER
# =========================================================================
subpages = [
    "pricing.html", "about-us.html", "service.html", "portfolio-01.html",
    "portfolio-02.html", "team.html", "faq.html", "testimonial.html", "contact-us.html"
]

for sp in subpages:
    spf = GHAYA_DIR / sp
    if spf.exists():
        txt = spf.read_text(encoding="utf-8")
        # Replace language switcher with FR first
        txt = re.sub(
            r'<div class="lang-switcher d-flex gap-2 align-items-center"[\s\S]*?</div>',
            '''<div class="lang-switcher d-flex gap-2 align-items-center" style="font-size: 13px; font-weight: 700; background: rgba(255,255,255,0.08); padding: 6px 14px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.18);">
            <a href="index.html" style="color: #BFF747; text-decoration: none;">FR</a>
            <span style="color: rgba(255,255,255,0.3);">|</span>
            <a href="en.html" style="color: #fff; text-decoration: none;">EN</a>
            <span style="color: rgba(255,255,255,0.3);">|</span>
            <a href="ar.html" style="color: #fff; text-decoration: none;">AR</a>
          </div>''',
            txt,
            count=1
        )
        spf.write_text(txt, encoding="utf-8")

print("✅ Updated language switcher on all subpages to [ FR | EN | AR ]")


# =========================================================================
# 5. SYNC TO DESKTOP
# =========================================================================
DESKTOP_DIR.mkdir(parents=True, exist_ok=True)
all_files = [
    "index.html", "fr.html", "en.html", "ar.html", "pricing.html", "about-us.html",
    "service.html", "portfolio-01.html", "portfolio-02.html", "team.html",
    "faq.html", "testimonial.html", "contact-us.html"
]
for fname in all_files:
    sf = GHAYA_DIR / fname
    if sf.exists():
        shutil.copy(sf, DESKTOP_DIR / fname)

shutil.copytree(GHAYA_DIR / "assets", DESKTOP_DIR / "assets", dirs_exist_ok=True)
print("🎉 SUCCESS: French is now the primary website language (index.html), English is secondary (en.html), Arabic is tertiary (ar.html). All synced to Desktop!")
