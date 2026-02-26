import urllib.request
import urllib.parse
import re

def get_yt_thumb(query):
    url = 'https://www.youtube.com/results?search_query=' + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode()
    match = re.search(r'"videoId":"(.*?)"', html)
    if match:
        return 'https://img.youtube.com/vi/' + match.group(1) + '/maxresdefault.jpg'
    return None

print('Surface Hero:', get_yt_thumb('Microsoft Surface Laptop Studio 2 official trailer hd'))
print('Surface Detail:', get_yt_thumb('Surface Laptop Studio 2 hands on unboxing 4k'))
print('MacBook Hero:', get_yt_thumb('MacBook Pro M4 Max official b-roll'))
print('MacBook Detail:', get_yt_thumb('MacBook Pro M4 Max close up macro'))
print('Dell Hero:', get_yt_thumb('Dell XPS 15 9530 official design'))
print('Dell Detail:', get_yt_thumb('Dell XPS 15 9530 ports display unboxing'))
