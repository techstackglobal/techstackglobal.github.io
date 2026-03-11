import xml.etree.ElementTree as ET
from urllib.parse import urlparse

tree = ET.parse('sitemap.xml')
root = tree.getroot()

ns = {'': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')

new_urls = [
    'https://techstackglobal.github.io/posts/best-noise-cancelling-headphones-2026.html',
    'https://techstackglobal.github.io/posts/best-podcast-microphones-2026.html',
    'https://techstackglobal.github.io/posts/best-ultrawide-monitors-2026.html',
    'https://techstackglobal.github.io/posts/best-microphones-for-remote-work-2026.html',
    'https://techstackglobal.github.io/posts/best-headphones-for-zoom-meetings-2026.html',
    'https://techstackglobal.github.io/posts/best-ar-glasses-for-coding-2026.html',
    'https://techstackglobal.github.io/posts/xreal-1s-gaming-setup-guide-2026.html'
]

existing = [url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url')]

for u in new_urls:
    if u not in existing:
        element = ET.SubElement(root, 'url')
        loc = ET.SubElement(element, 'loc')
        loc.text = u
        lastmod = ET.SubElement(element, 'lastmod')
        lastmod.text = '2026-03-03'

tree.write('sitemap.xml', xml_declaration=True, encoding='utf-8')
print('Sitemap updated')
