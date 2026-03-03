import urllib.request
import re

pages = [
  'http://localhost:8080/posts/best-noise-cancelling-headphones-2026.html',
  'http://localhost:8080/posts/best-podcast-microphones-2026.html',
  'http://localhost:8080/posts/best-ultrawide-monitors-2026.html'
]

for p in pages:
    req = urllib.request.urlopen(p)
    print(p, req.getcode())
    html = req.read().decode('utf-8')
    links = re.findall(r'href=[\'\"](/posts/[^\'\"]+)[\'\"]', html)
    for l in set(links):
        url = 'http://localhost:8080' + l
        try:
           res = urllib.request.urlopen(url)
           print('  [OK]  ', l)
        except Exception as e:
           print('  [ERR] ', l, e)
