import os
import re

def verify_seo():
    base_dir = 'c:/Users/PMLS/Desktop/Youtube Shorts/b2b_blog'
    report_path = 'c:/Users/PMLS/.gemini/antigravity/brain/8acb5e45-297b-4c05-ae50-1d7cdeac50b0/seo_affiliate_report.txt'
    
    with open(report_path, 'w', encoding='utf-8') as report:
        # Check robots.txt
        robots_path = os.path.join(base_dir, 'robots.txt')
        if os.path.exists(robots_path):
            with open(robots_path, 'r', encoding='utf-8') as f:
                report.write("--- robots.txt ---\n")
                report.write(f.read().strip() + "\n\n")
        else:
            report.write("--- robots.txt NOT FOUND ---\n\n")

        # Check sitemap.xml
        sitemap_path = os.path.join(base_dir, 'sitemap.xml')
        if os.path.exists(sitemap_path):
            with open(sitemap_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                report.write("--- sitemap.xml (First 20 Lines) ---\n")
                report.write("".join(lines[:20]).strip() + "\n\n")
        else:
            report.write("--- sitemap.xml NOT FOUND ---\n\n")

        # Check meta tags and JSON-LD
        samples = [
            'index.html',
            'posts/apple-macbook-pro-m4-pro-review.html',
            'posts/lg-27us500-w-ultrafine-monitor-review.html',
            'posts/surface-laptop-studio-2-review.html'
        ]
        
        report.write("--- Meta Title & Description Samples ---\n")
        for sample in samples:
            filepath = os.path.join(base_dir, sample)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    title = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
                    title_text = title.group(1).strip() if title else "NO TITLE"
                    
                    desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
                    desc_text = desc.group(1).strip() if desc else "NO DESCRIPTION"
                    
                    report.write(f"\n{sample}:\nTitle: {title_text}\nDesc: {desc_text}\n")
                    
                    if sample.startswith('posts/'):
                        schema = "YES" if '<script type="application/ld+json">' in content else "NO"
                        report.write(f"Has JSON-LD Schema: {schema}\n")
                        
                        # Check affiliate links
                        amazon_links = re.findall(r'<a[^>]+href=["\'][^"\']*amazon\.com[^"\']*["\'][^>]*>', content, re.IGNORECASE)
                        has_sponsored = all('rel="sponsored"' in link or "rel='sponsored'" in link for link in amazon_links) if amazon_links else False
                        sample_link = amazon_links[0] if amazon_links else "No Amazon links found"
                        
                        clean_sample = re.sub(r'\s+', ' ', sample_link).strip()
                        
                        report.write(f"Has Amazon Links: {'YES' if amazon_links else 'NO'}\n")
                        report.write(f"All Amazon links use rel='sponsored': {'YES' if has_sponsored else 'NO'}\n")
                        report.write(f"Sample Affiliate Link Tag: {clean_sample[:100]}...\n")

            except FileNotFoundError:
                report.write(f"\n{sample}: FILE NOT FOUND\n")

if __name__ == '__main__':
    verify_seo()
