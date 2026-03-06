import os
import glob
import re

html_files = glob.glob("*.html") + glob.glob("posts/*.html")

favicon_tags = [
    '<link rel="icon" href="/favicon.ico">',
    '<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">',
    '<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">',
    '<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">',
    '<meta name="theme-color" content="#0a2540">',
    '<meta property="og:site_name" content="TechStack Global">',
    '<meta name="application-name" content="TechStack Global">',
]

org_schema = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "TechStack Global",
  "url": "https://techstackglobal.github.io/",
  "logo": "https://techstackglobal.github.io/favicon-32x32.png"
}
</script>"""

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Favicon Tags
    tags_to_insert = []
    
    # We only insert tags that DO NOT exist in the file
    for tag in favicon_tags:
        if tag not in content:
            # Special check for theme-color to avoid duplicates if other variations exist
            if "theme-color" in tag and "name=\"theme-color\"" in content:
                continue
            if "og:site_name" in tag and "property=\"og:site_name\"" in content:
                continue
            if "application-name" in tag and "name=\"application-name\"" in content:
                continue
            tags_to_insert.append(tag)

    if tags_to_insert:
        # Prepend the comment if we are adding anything
        tags_to_insert.insert(0, "<!-- Site Favicons -->")
        block = "\n" + "\n".join(tags_to_insert) + "\n"
        content = content.replace("</head>", block + "</head>")
        
    # 2. Org Schema
    if '"@type": "Organization"' not in content and '"@type":"Organization"' not in content:
        content = content.replace("</head>", org_schema + "\n</head>")
        
    # 3. Homepage fixes ONLY for index.html
    if filepath == "index.html":
        # Enforce canonical
        if "rel=\"canonical\"" in content:
            content = re.sub(r'<link[^>]+rel=["\']canonical["\'][^>]*>', '<link rel="canonical" href="https://techstackglobal.github.io/index.html">', content)
        else:
            content = content.replace("</head>", '<link rel="canonical" href="https://techstackglobal.github.io/index.html">\n</head>')
        
        # Enforce og:url
        if "og:url" in content:
            content = re.sub(r'<meta[^>]+property=["\']og:url["\'][^>]*>', '<meta property="og:url" content="https://techstackglobal.github.io/index.html">', content)
        else:
            content = content.replace("</head>", '<meta property="og:url" content="https://techstackglobal.github.io/index.html">\n</head>')
            
        # Enforce title
        if "<title>" in content:
            content = re.sub(r'<title>.*?</title>', '<title>TechStack Global | Smarter Tech Decisions</title>', content, flags=re.IGNORECASE)
        else:
            content = content.replace("</head>", '<title>TechStack Global | Smarter Tech Decisions</title>\n</head>')
            
        # Enforce og:title
        if "og:title" in content:
            content = re.sub(r'<meta[^>]+property=["\']og:title["\'][^>]*>', '<meta property="og:title" content="TechStack Global | Smarter Tech Decisions">', content)
        else:
            content = content.replace("</head>", '<meta property="og:title" content="TechStack Global | Smarter Tech Decisions">\n</head>')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Headers injected successfully.")
