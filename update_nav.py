import re
import glob

new_nav = '''                <div class="nav-links">
                    <div class="dropdown">
                        <span class="nav-link dropdown-toggle">Services</span>
                        <div class="dropdown-menu">
                            <span class="dropdown-header">Urgent Home Services</span>
                            <a href="/plumber-marketing.html" class="dropdown-item">Plumber Marketing</a>
                            <a href="/hvac-marketing.html" class="dropdown-item">HVAC Marketing</a>
                            <a href="/electrician-marketing.html" class="dropdown-item">Electrician Marketing</a>
                            <a href="/garage-door-marketing.html" class="dropdown-item">Garage Door Marketing</a>
                            <a href="/roofer-marketing.html" class="dropdown-item">Roofer Marketing</a>
                            <a href="/locksmith-marketing.html" class="dropdown-item">Locksmith Marketing</a>
                            <a href="/tree-removal-marketing.html" class="dropdown-item">Tree Removal Marketing</a>
                            <div class="dropdown-divider"></div>
                            <span class="dropdown-header">Home Improvement</span>
                            <a href="/kitchen-remodeling-marketing.html" class="dropdown-item">Kitchen Remodeling</a>
                            <a href="/bathroom-remodeling-marketing.html" class="dropdown-item">Bathroom Remodeling</a>
                            <a href="/smart-home-marketing.html" class="dropdown-item">Smart Home Automation</a>
                            <a href="/water-filtration-marketing.html" class="dropdown-item">Water Filtration</a>
                            <div class="dropdown-divider"></div>
                            <span class="dropdown-header">Health & Wellness</span>
                            <a href="/medspa-marketing.html" class="dropdown-item">Med Spa Marketing</a>
                            <a href="/chiropractor-marketing.html" class="dropdown-item">Chiropractor Marketing</a>
                            <div class="dropdown-divider"></div>
                            <a href="/industries.html" class="dropdown-item">All Industries →</a>
                        </div>
                    </div>
                    <a href="/industries.html" class="nav-link">Industries</a>
                    <a href="/audit.html" class="nav-link">Free Audit</a>
                    <a href="/index.html#results" class="nav-link">Results</a>
                    <a href="/index.html#contact" class="nav-link">Contact</a>
                </div>'''

# Simple pattern to find and replace nav-links sections
old_nav_patterns = [
    r'<div class="nav-links">\s*<a href="/industries\.html"[^>]*>[^<]*</a>\s*<a href="/audit\.html"[^>]*>[^<]*</a>\s*<a href="[^"]*services[^"]*"[^>]*>[^<]*</a>\s*<a href="[^"]*results[^"]*"[^>]*>[^<]*</a>\s*<a href="[^"]*contact[^"]*"[^>]*>[^<]*</a>\s*</div>',
    r'<div class="nav-links">\s*<a href="/industries\.html"[^>]*>[^<]*</a>\s*<a href="/audit\.html"[^>]*>[^<]*</a>\s*<a href="#[^"]*"[^>]*>[^<]*</a>\s*<a href="#[^"]*"[^>]*>[^<]*</a>\s*<a href="#[^"]*"[^>]*>[^<]*</a>\s*</div>',
]

files_updated = 0
for html_file in glob.glob('*.html'):
    if html_file in ['fix-logo.html', 'logo-test.html']:
        continue
    with open(html_file, 'r') as f:
        content = f.read()
    
    updated = False
    for pattern in old_nav_patterns:
        if re.search(pattern, content, re.IGNORECASE | re.DOTALL):
            content = re.sub(pattern, new_nav, content, flags=re.IGNORECASE | re.DOTALL)
            updated = True
            break
    
    if updated:
        with open(html_file, 'w') as f:
            f.write(content)
        files_updated += 1
        print(f"Updated: {html_file}")
    else:
        print(f"No match: {html_file}")

print(f"\nTotal files updated: {files_updated}")
