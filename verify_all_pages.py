import sys
import re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


GHAYA = Path(r"C:\Users\USER\.gemini\antigravity\scratch\ghaya-prod")

files_to_check = [
    "index.html",
    "fr.html",
    "en.html",
    "ar.html",
    "about-us.html",
    "pricing.html",
    "service.html",
    "portfolio-01.html",
    "portfolio-02.html",
    "team.html",
    "faq.html",
    "testimonial.html",
    "contact-us.html"
]

print("=== CHECKING ALL PAGES ===")
for fname in files_to_check:
    fpath = GHAYA / fname
    if not fpath.exists():
        print(f"❌ MISSING: {fname}")
        continue
    content = fpath.read_text(encoding="utf-8", errors="replace")
    
    # Check title
    title_match = re.search(r"<title>(.*?)</title>", content)
    title = title_match.group(1) if title_match else "NO TITLE"
    
    # Check lang switcher
    switcher_match = re.search(r'<div class="lang-switcher[^"]*"[\s\S]*?</div>', content)
    has_switcher = bool(switcher_match)
    switcher_content = switcher_match.group(0).replace("\n", " ").strip() if switcher_match else "NONE"
    
    # Check total lines
    line_count = len(content.splitlines())
    
    print(f"📄 {fname:18} | Lines: {line_count:4} | Switcher: {'YES' if has_switcher else 'NO'} | Title: {title[:40]}...")

print("\n=== LANGUAGE SWITCHERS DETAILS ===")
for name in ["index.html", "en.html", "ar.html"]:
    c = (GHAYA / name).read_text(encoding="utf-8")
    m = re.search(r'<div class="lang-switcher[^"]*"[\s\S]*?</div>', c)
    print(f"\n--- {name} ---")
    if m:
        print(m.group(0))
    else:
        print("NO SWITCHER")

