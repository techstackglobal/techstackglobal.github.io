import json
import re
import os

def word_count(html):
    # Strip HTML tags
    text = re.sub('<[^<]+?>', ' ', html)
    # Strip scripts and styles
    text = re.sub(r'\{(.*?)\}', ' ', text)
    words = text.split()
    return len(words)

# Helper for wrapping
def generate_page(filepath, title, meta_desc, canonical, og_image, faqs, links, top_picks, content_blocks):
    
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a
                }
            } for q, a in faqs.items()
        ]
    }
    
    webpage_schema = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": title,
        "description": meta_desc,
        "url": canonical
    }

    schema_str = f"""
    <script type="application/ld+json">
    [
        {json.dumps(webpage_schema, indent=4)},
        {json.dumps(faq_schema, indent=4)}
    ]
    </script>
    """

    hero_filename = og_image.split("/")[-1]

    # Content generation logic
    # Putting it all together...
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <title>{title}</title>
    <meta content="{meta_desc}" name="description" />
    
    <link href="{canonical}" rel="canonical" />
    
    <meta content="article" property="og:type" />
    <meta content="{canonical}" property="og:url" />
    <meta content="{title}" property="og:title" />
    <meta content="{meta_desc}" property="og:description" />
    <meta content="{og_image}" property="og:image" />
    
    <meta content="summary_large_image" name="twitter:card" />
    <meta content="{title}" name="twitter:title" />
    <meta content="{meta_desc}" name="twitter:description" />
    <meta content="{og_image}" name="twitter:image" />

    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
    <link href="../style.css?v=9" rel="stylesheet" />
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet" />
    
    {schema_str}
</head>
<body class="dark-theme">
    <div class="ambient-grid"></div>
    <header class="glass-header">
        <nav class="container">
            <div class="logo"><a href="../index.html">TechStack<span class="accent">Global</span></a></div>
            <button aria-label="Toggle Menu" class="menu-toggle"><i class="fa-solid fa-bars"></i></button>
            <ul class="nav-links" id="nav-links">
                <li><a href="../index.html">Home</a></li>
                <li><a href="../blog.html">Guides</a></li>
            </ul>
        </nav>
    </header>

    <div id="site-affiliate-notice" style="background:#0f1724;color:#d1d5db;padding:8px 1.25rem;font-size:13px;text-align:center;border-bottom:1px solid rgba(255,255,255,0.05);">
        <strong>Note:</strong> TechStack Global uses affiliate links we may earn a commission on purchases at no extra cost to you.
    </div>

    <main class="article-container">
        <article class="post-body">
            <div class="affiliate-disclosure">
                <strong>Affiliate disclosure:</strong> This page contains affiliate links. If you purchase via these links we may earn a commission at no extra cost to you.
            </div>

            <span class="badge">{content_blocks['badge']}</span>
            <h1 class="post-title">{title}</h1>

            <div class="tldr-verdict glass-card">
                <h2 style="margin-top: 0; color: var(--accent);">TL;DR Verdict</h2>
                <p>{content_blocks['tldr']}</p>
                <div class="cta-center" style="margin-top: 1.5rem;">
                    <a href="{top_picks[0]['link']}?tag=techstackglob-20" class="btn-primary" target="_blank" rel="nofollow noopener sponsored">Check Price on Amazon</a>
                </div>
            </div>

            <div style="background-color: white; border-radius: 12px; margin-bottom: 2rem; margin-top: 2rem; padding: 2rem; text-align: center;">
                <img alt="Hero image for {title}" class="post-hero-img" loading="lazy" src="images/{hero_filename}" style="max-width:100%; max-height: 500px; object-fit: contain;" />
            </div>

            <div class="quick-decision-matrix" style="margin-bottom: 2rem;">
                <h3>Quick Decision Matrix</h3>
                <ul>
                    {"".join(f"<li>{m}</li>" for m in content_blocks['matrix'])}
                </ul>
            </div>

            <h2>Why This Category Matters</h2>
            <p>{content_blocks['why_matters']}</p>

            <h2 id="top-picks">Top Picks</h2>
            {"".join([f'''
            <div class="top-pick">
                <h3>{p['title']}</h3>
                <p><strong>Verdict:</strong> {p['verdict']}</p>
                <p>{p['description']}</p>
                <div class="cta-center" style="margin: 1.5rem 0;">
                    <a href="{p['link']}?tag=techstackglob-20" class="btn-primary" target="_blank" rel="nofollow noopener sponsored">View {p['name']} on Amazon</a>
                </div>
            </div>
            ''' for p in top_picks])}

            <h2 id="comparison">Mini Comparison Table</h2>
            <div class="table-responsive">
                <table class="specs-table">
                    <thead>
                        <tr>
                            <th>Model</th>
                            <th>Best For</th>
                            <th>Key Strength</th>
                        </tr>
                    </thead>
                    <tbody>
                        {"".join(f"<tr><td>{p['name']}</td><td>{p['best_for']}</td><td>{p['strength']}</td></tr>" for p in top_picks)}
                    </tbody>
                </table>
            </div>

            <div class="audience-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 2rem; margin-top: 2rem;">
                <div class="glass-card" style="padding: 1.5rem; border-top: 3px solid #00ff9d;">
                    <h4 style="margin-bottom: 0.5rem;"><i class="fa-solid fa-check-circle" style="color: #00ff9d;"></i> Buy this if...</h4>
                    <p>{content_blocks['buy_if']}</p>
                </div>
                <div class="glass-card" style="padding: 1.5rem; border-top: 3px solid #ff4b2b;">
                    <h4 style="margin-bottom: 0.5rem;"><i class="fa-solid fa-times-circle" style="color: #ff4b2b;"></i> Skip if...</h4>
                    <p>{content_blocks['skip_if']}</p>
                </div>
            </div>

            <h2 id="how-to-choose">How to Choose</h2>
            <p>{content_blocks['how_choose']}</p>

            <h2>Accessories &amp; Setup</h2>
            <p>{content_blocks['accessories']}</p>

            <div class="faq-section" style="margin-top: 4rem;">
                <h2>Frequently Asked Questions</h2>
                {"".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q, a in faqs.items())}
            </div>

            <div class="expert-verdict glass-card" style="padding: 2.5rem; border-top: 4px solid var(--accent); margin-top: 3rem;">
                <h2 style="margin-top: 0;">Final Verdict</h2>
                <p>{content_blocks['final_verdict']}</p>
                <div class="cta-center" style="margin-top: 2rem;">
                    <a href="{top_picks[0]['link']}?tag=techstackglob-20" class="btn-primary" style="padding: 1rem 2rem; font-size: 1.1rem;" target="_blank" rel="nofollow noopener sponsored">Buy {top_picks[0]['name']}</a>
                    <a href="{top_picks[1]['link']}?tag=techstackglob-20" class="btn-primary" style="padding: 1rem 2rem; font-size: 1.1rem; background: #333;" target="_blank" rel="nofollow noopener sponsored">Buy {top_picks[1]['name']}</a>
                </div>
            </div>

            <div style="margin-top: 3rem; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem;">
                <h3>Further Reading / Related</h3>
                <ul>
                    {"".join(f'<li><a href="{l_href}">{l_text}</a></li>' for l_text, l_href in links)}
                </ul>
        </article>
        <div class="sidebar-standard-wrapper">
            <aside class="sticky-sidebar">
                <div class="sidebar-widget verdict-widget">
                    <h4>Quick Verdict</h4>
                    <p style="font-size: 0.9rem; line-height: 1.5; color: var(--text-secondary); margin-bottom: 1.25rem;">
                        {content_blocks['tldr'][:150]}...
                    </p>
                    <a href="{top_picks[0]['link']}?tag=techstackglob-20" class="mini-card-btn" style="width: 100%; text-align: center;" target="_blank" rel="nofollow noopener sponsored">
                        Check Price →
                    </a>
                </div>

                <div class="sidebar-widget nav-widget">
                    <h4>Navigation</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="margin-bottom: 0.75rem;"><a href="#top-picks" style="color: var(--text-secondary); text-decoration: none; font-size: 0.9rem;"><i class="fa-solid fa-star" style="margin-right: 8px; color: var(--accent);"></i> Top Picks</a></li>
                        <li style="margin-bottom: 0.75rem;"><a href="#comparison" style="color: var(--text-secondary); text-decoration: none; font-size: 0.9rem;"><i class="fa-solid fa-table" style="margin-right: 8px; color: var(--accent);"></i> Comparison Table</a></li>
                        <li style="margin-bottom: 0.75rem;"><a href="#how-to-choose" style="color: var(--text-secondary); text-decoration: none; font-size: 0.9rem;"><i class="fa-solid fa-bolt" style="margin-right: 8px; color: var(--accent);"></i> How to Choose</a></li>
                    </ul>
                </div>

                <div class="sidebar-widget related-widget">
                    <h4>Related Guides</h4>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        {"".join([f'<li style="margin-bottom: 0.75rem;"><a href="{l_href}" style="color: var(--text-secondary); text-decoration: none; font-size: 0.85rem; display: flex; align-items: center;"><i class="fa-solid fa-chevron-right" style="margin-right: 8px; font-size: 0.7rem; opacity: 0.5;"></i> {l_text[:30]}</a></li>' for l_text, l_href in links[:3]])}
                    </ul>
                </div>
            </aside>
        </div>
    </main>

    <footer class="glass-footer" style="margin-top: 6rem;">
        <div class="container footer-content">
            <div class="footer-brand">
                <h3><a href="../index.html" style="text-decoration: none; color: inherit;">TechStack<span class="accent">Global</span></a></h3>
                <p>Tech guides built for everyday work, study, and smarter decisions.</p>
            </div>
        </div>
    </footer>
</body>
</html>
"""

    return html, word_count(html)
