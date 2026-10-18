# -*- coding: utf-8 -*-
"""
Builder for Ghaya Prod Agency Website (EN, FR, AR)
Built on ThemeForest Aximo Elite Creative Agency Template.
"""

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

GHAYA_DIR = Path(r"C:\Users\USER\.gemini\antigravity\scratch\ghaya-prod")

def get_page_html(lang):
    is_ar = (lang == "ar")
    html_dir = 'dir="rtl"' if is_ar else ''
    font_family = "'Cairo', 'Syne', sans-serif" if is_ar else "'Syne', sans-serif"
    
    # Text contents per language
    if lang == "en":
        t = {
            "title": "Ghaya Prod | High-Converting Web Systems & Cinema Production",
            "nav_home": "Home",
            "nav_services": "Solutions",
            "nav_gear": "Studio & Gear",
            "nav_portfolio": "Case Studies",
            "nav_pricing": "Packages",
            "nav_contact": "Contact",
            "btn_contact": "Book Strategy Call",
            "hero_badge": "Next-Gen Creative Agency & Video Production Studio",
            "hero_h1_1": "We engineer",
            "hero_h1_2": "high-converting web ecosystems",
            "hero_h1_3": "& cinematic video production.",
            "hero_p": "We help aesthetic clinics, private practices, and ambitious brands turn attention into high-ticket clients with Hollywood-grade video production and smart web conversion platforms.",
            "hero_metric_1": "1,000+",
            "hero_metric_1_label": "Facebook & Community Reach",
            "hero_metric_2": "4K ProRes",
            "hero_metric_2_label": "Cinema Standard Production",
            "hero_metric_3": "100%",
            "hero_metric_3_label": "Custom-Built Conversion Systems",
            "services_sub": "Our Core Disciplines",
            "services_h2": "Comprehensive Growth Solutions for High-Ticket Services",
            "s1_title": "Bespoke Web Platforms & CRM",
            "s1_desc": "Ultra-fast custom platforms with interactive diagnostic quizzes, before/after comparison sliders, and 1-click WhatsApp secretariat lead management.",
            "s2_title": "4K Cinema Video Production",
            "s2_desc": "Filmed on Panasonic Lumix S5 Full-Frame Cinema camera with broadcast Sennheiser/Shure microphones and Godox studio lighting for unmatched medical and brand prestige.",
            "s3_title": "Short-Form High-CTR Reels & Ads",
            "s3_desc": "Psychologically engineered scripts, CapCut Pro dynamic captioning, and hook optimization built specifically to convert paid traffic into booked appointments.",
            "s4_title": "Bilingual & Trilingual Scale",
            "s4_desc": "Native Arabic RTL, French, and English adaptation to dominate both the North African and international remote markets (Canada, Europe, Gulf).",
            "gear_sub": "Broadcast Production Arsenal",
            "gear_h2": "We Don't Shoot on Phones. We Deliver Cinema Quality.",
            "gear_p": "Your reputation deserves surgical precision. Our in-house production setup guarantees crystal-clear visuals and broadcast audio.",
            "g1_name": "Panasonic Lumix S5 Full-Frame",
            "g1_desc": "10-bit V-Log 4K cinematic depth of field for glowing skin tones and procedural precision.",
            "g2_name": "Sennheiser MK4 & Shure KSM27",
            "g2_desc": "Broadcast-grade condenser audio capturing authority with zero clinical room echo.",
            "g3_name": "Hollyland Lark M2 Wireless",
            "g3_desc": "Discreet button-sized lapel mics for doctor and patient live consultations.",
            "g4_name": "DJI Ronin RS3 Mini Gimbal",
            "g4_desc": "Ultra-smooth stabilization for clinic walkthroughs, macro procedure angles, and prestige B-roll.",
            "case_sub": "Featured Live Case Study",
            "case_h2": "Dr. Hanane Kashi — Aesthetic Medical Clinic",
            "case_badge": "Live Transformation & CRM System",
            "case_p": "We built a luxury bilingual clinic platform featuring an interactive Before/After facial volume slider, a 1-minute personalized assessment quiz, and an integrated Secretariat WhatsApp CRM dashboard.",
            "case_cta": "Explore Live Clinic System",
            "pricing_sub": "Transparent Investment",
            "pricing_h2": "Turnkey Packages Built for High ROI",
            "p1_name": "Launchpad System",
            "p1_price": "1,500 DH / $150",
            "p1_desc": "Perfect for solo doctors & boutique practices launching their official presence.",
            "p1_f1": "Complete Custom Landing Page",
            "p1_f2": "Interactive Before/After Slider",
            "p1_f3": "1-Minute Diagnostic Quiz",
            "p1_f4": "1-Click WhatsApp CRM Dashboard",
            "p1_f5": "Mobile Responsive & SSL Setup",
            "p2_badge": "Most Popular",
            "p2_name": "Cinema Growth Retainer",
            "p2_price": "3,500 DH / $350",
            "p2_desc": "The complete media and web takeover for ambitious clinics and brands.",
            "p2_f1": "Everything in Launchpad System",
            "p2_f2": "1x Monthly On-Site Cinema Shoot (Lumix S5)",
            "p2_f3": "4 to 8 High-CTR Edited Reels / Ads",
            "p2_f4": "Broadcast Audio with Wireless Mics",
            "p2_f5": "Monthly CRM & Case Study Updates",
            "p3_name": "International Scale",
            "p3_price": "Custom / Remote",
            "p3_desc": "For international medical practices and agencies in Canada, France & Gulf.",
            "p3_f1": "Trilingual (EN / FR / AR Native RTL)",
            "p3_f2": "Advanced Automated Booking Funnels",
            "p3_f3": "Ad Creative & Hook Production",
            "p3_f4": "Priority 24/7 Dedicated Support",
            "contact_sub": "Let's Collaborate",
            "contact_h2": "Ready to Transform Your Clinic's Online Authority?",
            "contact_p": "Drop us a message directly on WhatsApp or schedule a free 15-minute diagnostic walkthrough of your current online conversion funnel.",
            "contact_wa_btn": "Chat Directly on WhatsApp",
            "contact_phone": "+212 600 980 685",
            "contact_loc": "Casablanca, Morocco — Remote Worldwide (Canada & Europe)"
        }
    elif lang == "fr":
        t = {
            "title": "Ghaya Prod | Écosystèmes Web Haute Conversion & Production Cinéma",
            "nav_home": "Accueil",
            "nav_services": "Solutions",
            "nav_gear": "Matériel & Studio",
            "nav_portfolio": "Études de Cas",
            "nav_pricing": "Formules",
            "nav_contact": "Contact",
            "btn_contact": "Réserver un Audit",
            "hero_badge": "Agence Digitale Nouvelle Génération & Studio Vidéo Cinéma",
            "hero_h1_1": "Nous concevons des",
            "hero_h1_2": "écosystèmes web à haute conversion",
            "hero_h1_3": "& des productions vidéo cinématographiques.",
            "hero_p": "Nous aidons les cabinets médicaux, cliniques esthétiques et marques exigeantes à transformer l'attention en consultations privées grâce à une production vidéo cinéma et des plateformes web intelligentes.",
            "hero_metric_1": "1 000+",
            "hero_metric_1_label": "Abonnés Page Facebook Active",
            "hero_metric_2": "4K ProRes",
            "hero_metric_2_label": "Standard Cinéma Plein Format",
            "hero_metric_3": "100%",
            "hero_metric_3_label": "Systèmes Développés Sur-Mesure",
            "services_sub": "Nos Domaines d'Excellence",
            "services_h2": "Des Solutions Clés en Main pour Praticiens et Marques Premium",
            "s1_title": "Plateformes Web Sur-Mesure & CRM",
            "s1_desc": "Sites ultra-rapides avec quiz diagnostique interactif, comparateur Avant/Après fluide et tableau de bord CRM WhatsApp 1-clic pour le secrétariat.",
            "s2_title": "Production Vidéo Cinéma 4K",
            "s2_desc": "Tournage sur Panasonic Lumix S5 plein format, micros broadcast Sennheiser/Shure et éclairage studio Godox pour valoriser le geste médical et la crédibilité.",
            "s3_title": "Reels & Publicités à Fort Taux de Clic",
            "s3_desc": "Scripts persuasifs, montage dynamique CapCut Pro et sous-titrage moderne optimisés pour convertir le trafic payant en rendez-vous confirmés.",
            "s4_title": "Déploiement Bilingue & Trilingue",
            "s4_desc": "Adaptation native Arabe (RTL), Français et Anglais pour dominer le marché marocain local et exporter vos services vers le Canada et l'Europe.",
            "gear_sub": "Arsenal Audiovisuel Professionnel",
            "gear_h2": "Nous Ne Filmons Pas Au Téléphone. Nous Livrons du Cinéma.",
            "gear_p": "Votre standing exige une précision chirurgicale. Notre équipement studio garantit un piqué d'image exceptionnel et un son broadcast sans réverbération.",
            "g1_name": "Panasonic Lumix S5 Plein Format",
            "g1_desc": "Capteur 10-bit V-Log 4K pour un rendu cinématographique et des teintes de peau naturelles.",
            "g2_name": "Sennheiser MK4 & Shure KSM27",
            "g2_desc": "Micros statiques broadcast capturant une voix claire et rassurante sans écho de cabinet.",
            "g3_name": "Hollyland Lark M2 Sans Fil",
            "g3_desc": "Micros cravates ultra-discrets clipsables directement sur la blouse pour les consultations réelles.",
            "g4_name": "Stabilisateur DJI Ronin RS3 Mini",
            "g4_desc": "Mouvements fluides pour les visites du cabinet, plans macro sur les soins et B-rolls élégants.",
            "case_sub": "Étude de Cas Réelle",
            "case_h2": "Docteur Hanane Kashi — Médecine Esthétique Casablanca",
            "case_badge": "Plateforme Bilingue & CRM Secrétariat",
            "case_p": "Conception d'une plateforme médicale d'élite avec comparateur Avant/Après pour les cernes et pommettes, diagnostic en 1 minute et CRM privé WhatsApp pour la gestion sans friction des patientes.",
            "case_cta": "Voir le Système Clinique en Direct",
            "pricing_sub": "Investissement Transparent",
            "pricing_h2": "Des Formules Conçues pour un Retour sur Investissement Immédiat",
            "p1_name": "Pack Implantation Web",
            "p1_price": "1 500 DH",
            "p1_desc": "Idéal pour un praticien souhaitant une vitrine d'autorité et un flux WhatsApp optimisé.",
            "p1_f1": "Landing Page Complète & Design Prestige",
            "p1_f2": "Comparateur Interactif Avant / Après",
            "p1_f3": "Quiz Diagnostic Personnalisé en 1 Min",
            "p1_f4": "CRM Secrétariat & Studio WhatsApp 1-Clic",
            "p1_f5": "Optimisation Mobile & Sécurité SSL",
            "p2_badge": "Le Plus Populaire",
            "p2_name": "Pack Croissance & Tournage",
            "p2_price": "3 500 DH / mois",
            "p2_desc": "La formule complète alliant production vidéo en cabinet et gestion technique.",
            "p2_f1": "Tout le Pack Implantation Web inclus",
            "p2_f2": "1 Tournage Mensuel au Cabinet (Lumix S5)",
            "p2_f3": "4 à 8 Vidéos Reels / Ads Montées & Sous-titrées",
            "p2_f4": "Prise de Son Broadcast Sans Fil",
            "p2_f5": "Mises à jour mensuelles du CRM & Nouveaux Cas",
            "p3_name": "Expansion Internationale",
            "p3_price": "Sur Devis / Remote",
            "p3_desc": "Pour cliniques et entreprises ciblant le Canada, la France et le Golfe.",
            "p3_f1": "Trilingue (FR / EN / Arabe RTL)",
            "p3_f2": "Funnels de Prise de RDV Automatisés",
            "p3_f3": "Création de Publicités Vidéo Ciblées",
            "p3_f4": "Support Technique & Stratégique Dédié 7j/7",
            "contact_sub": "Passons à l'Action",
            "contact_h2": "Prêt à Transformer la Présence Digitale de Votre Cabinet ?",
            "contact_p": "Échangez directement avec nous sur WhatsApp pour une analyse personnalisée et gratuite de votre tunnel de conversion actuel.",
            "contact_wa_btn": "Discuter sur WhatsApp",
            "contact_phone": "06 00 98 06 85",
            "contact_loc": "Casablanca, Maroc — Prestations Remote (Canada & Europe)"
        }
    else: # ar
        t = {
            "title": "غاية برود | أنظمة الويب عالية التحويل والإنتاج السينمائي",
            "nav_home": "الرئيسية",
            "nav_services": "حلولنا",
            "nav_gear": "عتاد الاستوديو",
            "nav_portfolio": "دراسات الحالة",
            "nav_pricing": "الباقات",
            "nav_contact": "تواصل معنا",
            "btn_contact": "حجز استشارة استراتيجية",
            "hero_badge": "وكالة رقمية واستوديو إنتاج سينمائي متكامل للجيل الجديد",
            "hero_h1_1": "نصمم ونبني",
            "hero_h1_2": "منظومات ويب عالية التحويل",
            "hero_h1_3": "وإنتاجاً مرئياً سينمائياً فائق الدقة.",
            "hero_p": "نساعد العيادات الطبية، أطباء التجميل والعلامات الطموحة على تحويل المشاهدات إلى مواعيد واستشارات مؤكدة عبر تصوير سينمائي احترافي ومنصات رقمية ذكية مزودة بأنظمة CRM متطورة.",
            "hero_metric_1": "+1,000",
            "hero_metric_1_label": "متابع متفاعل على فيسبوك",
            "hero_metric_2": "4K ProRes",
            "hero_metric_2_label": "معيار التصوير السينمائي الكامل",
            "hero_metric_3": "100%",
            "hero_metric_3_label": "أنظمة مخصصة لرفع المبيعات",
            "services_sub": "مجالات تخصصنا",
            "services_h2": "حلول نمو شاملة للخدمات الراقية والاستشارات الخاصة",
            "s1_title": "منصات الويب المتطورة وإدارة المريضات CRM",
            "s1_desc": "منصات فائقة السرعة مع اختبار تشخيصي تفاعلي، ومقارنة تفاعلية قبل وبعد، ولوحة تحكم سريعة للواتساب بنقرة واحدة للسكرتارية.",
            "s2_title": "إنتاج فيديو سينمائي 4K هوليوود",
            "s2_desc": "تصوير بكاميرا Panasonic Lumix S5 ذات الحساس الكامل، مع مايكروفونات إذاعية Sennheiser/Shure وإضاءة Godox لترسيخ الهيبة الطبية.",
            "s3_title": "ريلز وإعلانات قصيرة عالية النقرات",
            "s3_desc": "سيناريوهات مقنعة، ومونتاج ديناميكي عبر CapCut Pro مع ترجمات بصرية عصرية لتحويل الإعلانات الممولة إلى مواعيد مؤكدة.",
            "s4_title": "تطوير متعدد اللغات (عربي أصيل، فرنسي، إنجليزي)",
            "s4_desc": "دعم كامل للغة العربية من اليمين لليتمين (RTL) بالإضافة للفرنسية والإنجليزية للتوسع محلياً في المغرب وعالمياً في كندا وأوروبا والخليج.",
            "gear_sub": "عتاد الإنتاج الإذاعي والسينمائي",
            "gear_h2": "لا نصور بالهواتف.. نقدم معيار السينما والتلفزيون",
            "gear_p": "مكانة عيادتك وعلامتك تستحق دقة متناهية. عتادنا الاحترافي يضمن وضوحاً فائقاً وصوتاً نقياً تماماً بدون أي صدى داخل العيادة.",
            "g1_name": "كاميرا Panasonic Lumix S5 Full-Frame",
            "g1_desc": "حساس 10-bit V-Log 4K لعزل سينمائي فاخر وإظهار نضارة البشرة والتفاصيل الدقيقة.",
            "g2_name": "مايكروفونات Sennheiser MK4 & Shure KSM27",
            "g2_desc": "صوت إذاعي دافئ وواضح يمنح المشاهد شعوراً فورياً بالثقة والاحترافية.",
            "g3_name": "مايكروفونات Hollyland Lark M2 اللاسلكية",
            "g3_desc": "مايكروفونات زرية خفيفة تثبت على وزرة الطبيب أثناء الكشف والاستشارة الحية.",
            "g4_name": "مانع الاهتزاز DJI Ronin RS3 Mini",
            "g4_desc": "حركات كاميرا انسيابية لتصوير جولات العيادة وتفاصيل الإجراءات الطبية الراقية.",
            "case_sub": "دراسة حالة واقعية حية",
            "case_h2": "الدكتورة حنان كاشي — طب التجميل بالدار البيضاء",
            "case_badge": "منصة ثنائية اللغة ونظام CRM سكرتارية",
            "case_p": "بناء منصة طبية متكاملة لعيادة الدكتورة حنان كاشي مع مقارن قبل وبعد لحقن الفيلر، واختبار تشخيصي في دقيقة واحدة، ونظام CRM لإدارة المواعيد عبر واتساب.",
            "case_cta": "معاينة المنصة الحية مباشرة",
            "pricing_sub": "استثمار شفاف ومدروس",
            "pricing_h2": "باقات مصممة لتحقيق عائد فوري وملموس",
            "p1_name": "باقة إطلاق المنصة الرقمية",
            "p1_price": "1,500 درهم",
            "p1_desc": "الخيار الأمثل للطبيب الراغب في واجهة هيبة رقمية ومسار حجز ذكي عبر واتساب.",
            "p1_f1": "صفحة هبوط كاملة بتصميم فاخر",
            "p1_f2": "مقارن تفاعلي لحالات قبل / بعد",
            "p1_f3": "اختبار تشخيصي مخصص في دقيقة",
            "p1_f4": "لوحة CRM واستوديو واتساب بنقرة واحدة",
            "p1_f5": "توافق تام مع الهواتف وحماية SSL",
            "p2_badge": "الأكثر طلباً",
            "p2_name": "باقة النمو والتصوير الشهري",
            "p2_price": "3,500 درهم / شهرياً",
            "p2_desc": "الحل الكامل يجمع بين التواجد الرقمي والإنتاج السينمائي الاحترافي داخل العيادة.",
            "p2_f1": "جميع مزايا باقة إطلاق المنصة",
            "p2_f2": "جلسة تصوير سينمائي شهرية داخل العيادة (Lumix S5)",
            "p2_f3": "مونتاج 4 إلى 8 فيديوهات ريلز وإعلانات جاهزة للنشر",
            "p2_f4": "تسجيل صوت إذاعي عبر مايكات لاسلكية",
            "p2_f5": "تحديث مستمر للوحة CRM وإضافة الحالات الجديدة",
            "p3_name": "التوسع الدولي (عن بعد)",
            "p3_price": "حسب المشروع",
            "p3_desc": "مخصص للمراكز الطبية والشركات في كندا وفرنسا ودول الخليج العربي.",
            "p3_f1": "منصات ثلاثية اللغة (عربي، فرنسي، إنجليزي)",
            "p3_f2": "مسارات حجز ومبيعات مؤتمتة بالكامل",
            "p3_f3": "إنتاج إعلانات مرئية موجهة للمغتربين والعملاء الدوليين",
            "p3_f4": "دعم فني واستراتيجي متواصل 7 أيام في الأسبوع",
            "contact_sub": "دعنا نبدأ الآن",
            "contact_h2": "هل أنت مستعد لنقل حضور عيادتك إلى مستوى استثنائي؟",
            "contact_p": "تواصل معنا مباشرة عبر واتساب للحصول على تدقيق مجاني لمسار تحويل عيادتك الحالي ومناقشة مشروعك القادم.",
            "contact_wa_btn": "محادثة مباشرة عبر واتساب",
            "contact_phone": "0600980685",
            "contact_loc": "الدار البيضاء، المغرب — خدمات عن بعد (كندا وأوروبا والخليج)"
        }

    # Brand Header Nav
    nav_links_html = f'''
    <div class="brand-logo">
      <a href="{lang if lang != 'en' else 'index'}.html" style="display: flex; align-items: center; gap: 10px; text-decoration: none;">
        <span style="font-family: {font_family}; font-size: 26px; font-weight: 800; color: #fff; letter-spacing: -1px;">GHAYA<span style="color: #BFF747;">PROD</span></span>
      </a>
    </div>
    <div class="menu-block-wrapper">
      <div class="menu-overlay"></div>
      <nav class="menu-block" id="append-menu-header">
        <div class="mobile-menu-head">
          <div class="go-back"><i class="fa fa-angle-left"></i></div>
          <div class="current-menu-title"></div>
          <div class="mobile-menu-close">&times;</div>
        </div>
        <ul class="site-menu-main">
          <li class="nav-item"><a href="#home" class="nav-link-item active">{t['nav_home']}</a></li>
          <li class="nav-item"><a href="#services" class="nav-link-item">{t['nav_services']}</a></li>
          <li class="nav-item"><a href="#equipment" class="nav-link-item">{t['nav_gear']}</a></li>
          <li class="nav-item"><a href="#portfolio" class="nav-link-item">{t['nav_portfolio']}</a></li>
          <li class="nav-item"><a href="#pricing" class="nav-link-item">{t['nav_pricing']}</a></li>
          <li class="nav-item"><a href="#contact" class="nav-link-item">{t['nav_contact']}</a></li>
        </ul>
      </nav>
    </div>
    <div class="d-flex align-items-center gap-3 ms-auto">
      <div class="lang-switcher d-flex gap-2 align-items-center" style="font-size: 13px; font-weight: 700; background: rgba(255,255,255,0.06); padding: 6px 12px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.12);">
        <a href="index.html" style="color: {'#BFF747' if lang == 'en' else '#fff'}; text-decoration: none;">EN</a>
        <span style="color: rgba(255,255,255,0.3);">|</span>
        <a href="fr.html" style="color: {'#BFF747' if lang == 'fr' else '#fff'}; text-decoration: none;">FR</a>
        <span style="color: rgba(255,255,255,0.3);">|</span>
        <a href="ar.html" style="color: {'#BFF747' if lang == 'ar' else '#fff'}; text-decoration: none;">عربي</a>
      </div>
      <div class="header-btn header-btn-l1 d-none d-sm-inline-flex">
        <a class="aximo-default-btn pill aximo-header-btn" href="#contact" style="background: #BFF747; color: #000; font-weight: 700; border: none; padding: 12px 24px;">
          {t['btn_contact']}
        </a>
      </div>
      <div class="mobile-menu-trigger light">
        <span></span>
      </div>
    </div>
    '''

    # Complete page assembly
    html = f'''<!DOCTYPE html>
<html lang="{lang}" {html_dir}>
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t['title']}</title>
  <link rel="shortcut icon" href="assets/images/favicon.ico" type="image/x-icon">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Syne:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- Stylesheets -->
  <link rel="stylesheet" href="assets/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/css/magnific-popup.css">
  <link rel="stylesheet" href="assets/css/swiper-bundle.min.css">
  <link rel="stylesheet" href="assets/css/animate.css">
  <link rel="stylesheet" href="assets/css/custom-font.css">
  <link rel="stylesheet" href="assets/css/fontawesome.css">
  <link rel="stylesheet" href="assets/css/aos.css">
  <link rel="stylesheet" href="assets/css/icomoon.css">
  <link rel="stylesheet" href="assets/css/main.css">
  <link rel="stylesheet" href="assets/css/app.min.css">

  <style>
    body {{
      font-family: {font_family};
      background-color: #0c0d0e;
      color: #e2e8f0;
      {'text-align: right;' if is_ar else ''}
    }}
    .dark-bg {{
      background-color: #0c0d0e !important;
    }}
    .accent-lime {{
      color: #BFF747 !important;
    }}
    .bg-accent-lime {{
      background-color: #BFF747 !important;
      color: #000 !important;
    }}
    .gear-card {{
      background: #141618;
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 20px;
      padding: 30px;
      transition: all 0.3s ease;
      height: 100%;
    }}
    .gear-card:hover {{
      transform: translateY(-5px);
      border-color: #BFF747;
      box-shadow: 0 15px 35px rgba(191, 247, 71, 0.12);
    }}
    .gear-icon-box {{
      width: 56px;
      height: 56px;
      border-radius: 14px;
      background: rgba(191, 247, 71, 0.1);
      color: #BFF747;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      margin-bottom: 20px;
    }}
    .case-card {{
      background: #141618;
      border: 1px solid rgba(191, 247, 71, 0.25);
      border-radius: 24px;
      overflow: hidden;
      transition: all 0.3s ease;
    }}
    .case-card:hover {{
      border-color: #BFF747;
      box-shadow: 0 20px 45px rgba(0,0,0,0.5);
    }}
    .pricing-card {{
      background: #141618;
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 24px;
      padding: 40px 32px;
      transition: all 0.3s ease;
      position: relative;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .pricing-card.popular {{
      border-color: #BFF747;
      background: linear-gradient(180deg, rgba(191, 247, 71, 0.08) 0%, #141618 100%);
    }}
    .btn-lime {{
      background: #BFF747;
      color: #0c0d0e !important;
      font-weight: 700;
      border-radius: 50px;
      padding: 14px 28px;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      transition: all 0.2s ease;
      border: none;
    }}
    .btn-lime:hover {{
      transform: translateY(-2px);
      box-shadow: 0 10px 25px rgba(191, 247, 71, 0.4);
      background: #cbf964;
    }}
    .btn-wa-ghaya {{
      background: #25D366;
      color: #fff !important;
      font-weight: 700;
      border-radius: 50px;
      padding: 15px 30px;
      display: inline-flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      font-size: 16px;
      box-shadow: 0 10px 25px rgba(37, 211, 102, 0.3);
      transition: all 0.2s ease;
    }}
    .btn-wa-ghaya:hover {{
      transform: translateY(-2px);
      box-shadow: 0 12px 30px rgba(37, 211, 102, 0.45);
    }}
  </style>
</head>

<body class="dark-bg">

  <!-- Header -->
  <header class="site-header aximo-header-section aximo-header1 dark-bg" id="sticky-menu" style="border-bottom: 1px solid rgba(255,255,255,0.06); padding: 18px 0;">
    <div class="container">
      <nav class="navbar site-navbar">
        {nav_links_html}
      </nav>
    </div>
  </header>

  <!-- Hero Section -->
  <div class="aximo-hero-section dark-bg" id="home" style="padding: 100px 0 80px;">
    <div class="container position-relative">
      <div class="row align-items-center">
        <div class="col-lg-8">
          <div class="aximo-hero-content">
            <span class="badge px-3 py-2 text-uppercase mb-4" style="background: rgba(191, 247, 71, 0.12); color: #BFF747; border: 1px solid #BFF747; border-radius: 30px; font-size: 13px; font-weight: 700;">
              ⚡ {t['hero_badge']}
            </span>
            <h1 style="font-size: 54px; line-height: 1.15; font-weight: 800; color: #fff; margin-bottom: 24px;">
              {t['hero_h1_1']} <br>
              <span class="accent-lime">{t['hero_h1_2']}</span> <br>
              {t['hero_h1_3']}
            </h1>
            <p style="font-size: 18px; color: #94a3b8; max-width: 650px; line-height: 1.7; margin-bottom: 35px;">
              {t['hero_p']}
            </p>

            <div class="d-flex flex-wrap gap-3 align-items-center mb-5">
              <a href="https://wa.me/212600980685?text=Hello%20Ghaya%20Prod,%20I%20would%20like%20to%20discuss%20a%20production%20or%20web%20project." target="_blank" class="btn-wa-ghaya">
                <i class="fab fa-whatsapp fa-lg"></i> {t['contact_wa_btn']}
              </a>
              <a href="#portfolio" class="btn btn-outline-light font-weight-bold" style="border-radius: 50px; padding: 14px 28px; border-color: rgba(255,255,255,0.2);">
                {t['nav_portfolio']} <i class="fas fa-arrow-down ms-2"></i>
              </a>
            </div>

            <!-- Authority Metrics -->
            <div class="row pt-4 border-top" style="border-color: rgba(255,255,255,0.08) !important;">
              <div class="col-4">
                <h3 class="accent-lime mb-0" style="font-weight: 800; font-size: 32px;">{t['hero_metric_1']}</h3>
                <small class="text-muted">{t['hero_metric_1_label']}</small>
              </div>
              <div class="col-4">
                <h3 class="accent-lime mb-0" style="font-weight: 800; font-size: 32px;">{t['hero_metric_2']}</h3>
                <small class="text-muted">{t['hero_metric_2_label']}</small>
              </div>
              <div class="col-4">
                <h3 class="accent-lime mb-0" style="font-weight: 800; font-size: 32px;">{t['hero_metric_3']}</h3>
                <small class="text-muted">{t['hero_metric_3_label']}</small>
              </div>
            </div>

          </div>
        </div>
        <div class="col-lg-4 text-center mt-5 mt-lg-0">
          <div class="position-relative d-inline-block">
            <div style="width: 320px; height: 420px; border-radius: 28px; background: linear-gradient(135deg, rgba(191, 247, 71, 0.2) 0%, rgba(20, 22, 24, 0.9) 100%); border: 2px solid #BFF747; padding: 25px; display: flex; flex-direction: column; justify-content: space-between; text-align: left; box-shadow: 0 20px 50px rgba(0,0,0,0.6);">
              <div>
                <span class="badge bg-accent-lime font-weight-bold mb-3 px-3 py-1">PRODUCTION READY</span>
                <h4 class="text-white font-weight-bold mb-2">Panasonic Lumix S5 & Sennheiser</h4>
                <p class="text-muted small">In-House Studio Rig: Full-Frame 4K, Wireless Audio, Gimbal Stabilisation & High-Speed Web Infrastructure.</p>
              </div>
              <div class="p-3 rounded-lg" style="background: rgba(0,0,0,0.4); border: 1px solid rgba(255,255,255,0.08);">
                <div class="d-flex justify-content-between text-muted small mb-1">
                  <span>Camera Standard</span>
                  <span class="text-white font-weight-bold">4K V-Log 10-bit</span>
                </div>
                <div class="d-flex justify-content-between text-muted small mb-1">
                  <span>Audio Fidelity</span>
                  <span class="text-white font-weight-bold">Broadcast Studio</span>
                </div>
                <div class="d-flex justify-content-between text-muted small">
                  <span>Web Stack</span>
                  <span class="accent-lime font-weight-bold">Ultra-Fast + CRM</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Services Section -->
  <section id="services" class="py-5" style="border-top: 1px solid rgba(255,255,255,0.06); background: #0e1012;">
    <div class="container py-4">
      <div class="text-center max-w-700 mx-auto mb-5">
        <span class="text-uppercase accent-lime font-weight-bold" style="letter-spacing: 2px; font-size: 13px;">{t['services_sub']}</span>
        <h2 class="text-white mt-2" style="font-size: 38px; font-weight: 800;">{t['services_h2']}</h2>
      </div>

      <div class="row g-4">
        <div class="col-md-6 col-lg-3">
          <div class="gear-card">
            <div class="gear-icon-box"><i class="fas fa-laptop-code"></i></div>
            <h4 class="text-white font-weight-bold mb-3">{t['s1_title']}</h4>
            <p class="text-muted small mb-0" style="line-height: 1.6;">{t['s1_desc']}</p>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="gear-card">
            <div class="gear-icon-box"><i class="fas fa-video"></i></div>
            <h4 class="text-white font-weight-bold mb-3">{t['s2_title']}</h4>
            <p class="text-muted small mb-0" style="line-height: 1.6;">{t['s2_desc']}</p>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="gear-card">
            <div class="gear-icon-box"><i class="fas fa-fire"></i></div>
            <h4 class="text-white font-weight-bold mb-3">{t['s3_title']}</h4>
            <p class="text-muted small mb-0" style="line-height: 1.6;">{t['s3_desc']}</p>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="gear-card">
            <div class="gear-icon-box"><i class="fas fa-globe"></i></div>
            <h4 class="text-white font-weight-bold mb-3">{t['s4_title']}</h4>
            <p class="text-muted small mb-0" style="line-height: 1.6;">{t['s4_desc']}</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Studio & Gear Section -->
  <section id="equipment" class="py-5" style="border-top: 1px solid rgba(255,255,255,0.06); background: #0c0d0e;">
    <div class="container py-4">
      <div class="row align-items-center mb-5">
        <div class="col-lg-6">
          <span class="text-uppercase accent-lime font-weight-bold" style="letter-spacing: 2px; font-size: 13px;">{t['gear_sub']}</span>
          <h2 class="text-white mt-2" style="font-size: 38px; font-weight: 800;">{t['gear_h2']}</h2>
        </div>
        <div class="col-lg-6 mt-3 mt-lg-0">
          <p class="text-muted mb-0" style="font-size: 16px; line-height: 1.7;">{t['gear_p']}</p>
        </div>
      </div>

      <div class="row g-4">
        <div class="col-md-6 col-lg-3">
          <div class="gear-card">
            <div class="gear-icon-box"><i class="fas fa-camera"></i></div>
            <h5 class="text-white font-weight-bold mb-2">{t['g1_name']}</h5>
            <p class="text-muted small mb-0">{t['g1_desc']}</p>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="gear-card">
            <div class="gear-icon-box"><i class="fas fa-microphone-alt"></i></div>
            <h5 class="text-white font-weight-bold mb-2">{t['g2_name']}</h5>
            <p class="text-muted small mb-0">{t['g2_desc']}</p>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="gear-card">
            <div class="gear-icon-box"><i class="fas fa-broadcast-tower"></i></div>
            <h5 class="text-white font-weight-bold mb-2">{t['g3_name']}</h5>
            <p class="text-muted small mb-0">{t['g3_desc']}</p>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="gear-card">
            <div class="gear-icon-box"><i class="fas fa-arrows-alt"></i></div>
            <h5 class="text-white font-weight-bold mb-2">{t['g4_name']}</h5>
            <p class="text-muted small mb-0">{t['g4_desc']}</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Live Case Study: Dr. Hanane Kashi -->
  <section id="portfolio" class="py-5" style="border-top: 1px solid rgba(255,255,255,0.06); background: #0e1012;">
    <div class="container py-4">
      <div class="text-center max-w-700 mx-auto mb-5">
        <span class="text-uppercase accent-lime font-weight-bold" style="letter-spacing: 2px; font-size: 13px;">{t['case_sub']}</span>
        <h2 class="text-white mt-2" style="font-size: 38px; font-weight: 800;">{t['case_h2']}</h2>
      </div>

      <div class="case-card p-4 p-lg-5">
        <div class="row align-items-center">
          <div class="col-lg-6 mb-4 mb-lg-0">
            <div class="overflow-hidden rounded-lg" style="border: 2px solid rgba(191, 247, 71, 0.4); max-height: 380px;">
              <img src="assets/images/portfolio/dr-kashi-desk.png" alt="Cabinet Dr Hanane Kashi" class="img-fluid w-100 h-100" style="object-fit: cover;">
            </div>
          </div>
          <div class="col-lg-6 ps-lg-5">
            <span class="badge bg-accent-lime font-weight-bold mb-3 px-3 py-1">{t['case_badge']}</span>
            <h3 class="text-white font-weight-bold mb-3">Cabinet de Médecine Esthétique & Laser (Casablanca)</h3>
            <p class="text-muted mb-4" style="line-height: 1.7;">{t['case_p']}</p>

            <div class="d-flex flex-wrap gap-2 mb-4">
              <span class="badge border border-secondary text-light px-3 py-2">Slider Avant / Après 60fps</span>
              <span class="badge border border-secondary text-light px-3 py-2">Quiz Diagnostic 1 Min</span>
              <span class="badge border border-secondary text-light px-3 py-2">CRM Secrétariat & WhatsApp Studio</span>
              <span class="badge border border-secondary text-light px-3 py-2">Bilingue FR / AR RTL</span>
            </div>

            <div class="d-flex flex-wrap gap-3">
              <a href="http://localhost:8080/index.html" target="_blank" class="btn-lime">
                <i class="fas fa-external-link-alt"></i> {t['case_cta']} (FR)
              </a>
              <a href="http://localhost:8080/admin.html" target="_blank" class="btn btn-outline-light" style="border-radius: 50px; padding: 12px 24px; border-color: rgba(255,255,255,0.25);">
                <i class="fas fa-lock me-1"></i> CRM Démo
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Pricing & Packages -->
  <section id="pricing" class="py-5" style="border-top: 1px solid rgba(255,255,255,0.06); background: #0c0d0e;">
    <div class="container py-4">
      <div class="text-center max-w-700 mx-auto mb-5">
        <span class="text-uppercase accent-lime font-weight-bold" style="letter-spacing: 2px; font-size: 13px;">{t['pricing_sub']}</span>
        <h2 class="text-white mt-2" style="font-size: 38px; font-weight: 800;">{t['pricing_h2']}</h2>
      </div>

      <div class="row g-4 align-items-stretch">
        <!-- Tier 1 -->
        <div class="col-lg-4">
          <div class="pricing-card">
            <div>
              <h4 class="text-white font-weight-bold mb-2">{t['p1_name']}</h4>
              <p class="text-muted small mb-4">{t['p1_desc']}</p>
              <h2 class="accent-lime font-weight-bold mb-4">{t['p1_price']}</h2>
              <ul class="list-unstyled text-muted small" style="line-height: 2.2;">
                <li><i class="fas fa-check accent-lime me-2"></i> {t['p1_f1']}</li>
                <li><i class="fas fa-check accent-lime me-2"></i> {t['p1_f2']}</li>
                <li><i class="fas fa-check accent-lime me-2"></i> {t['p1_f3']}</li>
                <li><i class="fas fa-check accent-lime me-2"></i> {t['p1_f4']}</li>
                <li><i class="fas fa-check accent-lime me-2"></i> {t['p1_f5']}</li>
              </ul>
            </div>
            <a href="#contact" class="btn btn-outline-light btn-block w-100 font-weight-bold mt-4" style="border-radius: 50px; padding: 12px 0;">{t['btn_contact']}</a>
          </div>
        </div>

        <!-- Tier 2 (Popular) -->
        <div class="col-lg-4">
          <div class="pricing-card popular">
            <span class="badge bg-accent-lime position-absolute top-0 end-0 m-3 px-3 py-1 font-weight-bold">{t['p2_badge']}</span>
            <div>
              <h4 class="text-white font-weight-bold mb-2">{t['p2_name']}</h4>
              <p class="text-muted small mb-4">{t['p2_desc']}</p>
              <h2 class="accent-lime font-weight-bold mb-4">{t['p2_price']}</h2>
              <ul class="list-unstyled text-muted small" style="line-height: 2.2;">
                <li class="text-white"><i class="fas fa-check accent-lime me-2"></i> {t['p2_f1']}</li>
                <li class="text-white"><i class="fas fa-check accent-lime me-2"></i> {t['p2_f2']}</li>
                <li class="text-white"><i class="fas fa-check accent-lime me-2"></i> {t['p2_f3']}</li>
                <li class="text-white"><i class="fas fa-check accent-lime me-2"></i> {t['p2_f4']}</li>
                <li class="text-white"><i class="fas fa-check accent-lime me-2"></i> {t['p2_f5']}</li>
              </ul>
            </div>
            <a href="#contact" class="btn-lime text-center justify-content-center w-100 mt-4">{t['btn_contact']}</a>
          </div>
        </div>

        <!-- Tier 3 -->
        <div class="col-lg-4">
          <div class="pricing-card">
            <div>
              <h4 class="text-white font-weight-bold mb-2">{t['p3_name']}</h4>
              <p class="text-muted small mb-4">{t['p3_desc']}</p>
              <h2 class="accent-lime font-weight-bold mb-4">{t['p3_price']}</h2>
              <ul class="list-unstyled text-muted small" style="line-height: 2.2;">
                <li><i class="fas fa-check accent-lime me-2"></i> {t['p3_f1']}</li>
                <li><i class="fas fa-check accent-lime me-2"></i> {t['p3_f2']}</li>
                <li><i class="fas fa-check accent-lime me-2"></i> {t['p3_f3']}</li>
                <li><i class="fas fa-check accent-lime me-2"></i> {t['p3_f4']}</li>
              </ul>
            </div>
            <a href="#contact" class="btn btn-outline-light btn-block w-100 font-weight-bold mt-4" style="border-radius: 50px; padding: 12px 0;">{t['btn_contact']}</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="py-5" style="border-top: 1px solid rgba(255,255,255,0.06); background: #0e1012;">
    <div class="container py-4 text-center max-w-700 mx-auto">
      <span class="text-uppercase accent-lime font-weight-bold" style="letter-spacing: 2px; font-size: 13px;">{t['contact_sub']}</span>
      <h2 class="text-white mt-2 mb-3" style="font-size: 42px; font-weight: 800;">{t['contact_h2']}</h2>
      <p class="text-muted mb-4" style="font-size: 17px; line-height: 1.7;">{t['contact_p']}</p>

      <div class="d-flex justify-content-center gap-3 mb-4">
        <a href="https://wa.me/212600980685?text=Bonjour%20Ghaya%20Prod,%20je%20souhaite%20r%C3%A9server%20un%20audit%20ou%20discuter%20d'une%20collaboration." target="_blank" class="btn-wa-ghaya">
          <i class="fab fa-whatsapp fa-lg"></i> {t['contact_wa_btn']}
        </a>
      </div>

      <p class="text-muted small mb-0">
        <i class="fas fa-map-marker-alt text-light me-1"></i> {t['contact_loc']} <br>
        <i class="fas fa-phone-alt text-light me-1"></i> {t['contact_phone']}
      </p>
    </div>
  </section>

  <!-- Footer -->
  <footer class="py-4 text-center" style="border-top: 1px solid rgba(255,255,255,0.06); background: #0c0d0e;">
    <div class="container">
      <p class="text-muted small mb-0">
        &copy; 2026 <strong>GHAYA PROD</strong>. All rights reserved. Built for Elite Web Systems & Cinema Media Production.
      </p>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="assets/js/jquery-3.6.0.min.js"></script>
  <script src="assets/js/bootstrap.bundle.min.js"></script>
  <script src="assets/js/menu.js"></script>
  <script src="assets/js/app.js"></script>
</body>
</html>
'''
    return html

def main():
    en_html = get_page_html("en")
    fr_html = get_page_html("fr")
    ar_html = get_page_html("ar")

    (GHAYA_DIR / "index.html").write_text(en_html, encoding="utf-8")
    (GHAYA_DIR / "fr.html").write_text(fr_html, encoding="utf-8")
    (GHAYA_DIR / "ar.html").write_text(ar_html, encoding="utf-8")

    print("✅ Successfully built Ghaya Prod Official Platform:")
    print(" - English: index.html")
    print(" - French: fr.html")
    print(" - Arabic (RTL): ar.html")

if __name__ == "__main__":
    main()
