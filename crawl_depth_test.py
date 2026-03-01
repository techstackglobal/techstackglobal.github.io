import os
from bs4 import BeautifulSoup
from collections import deque
import urllib.parse

def clean_link(link):
    if not link:
        return None
    link = link.split('#')[0]
    link = link.split('?')[0]
    if link.startswith('http') or link.startswith('mailto:') or link.startswith('tel:'):
        return None
    return link

def build_graph(root_dir='.'):
    graph = {}
    for root, dirs, files in os.walk(root_dir):
        if '.git' in root or '.venv' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                abs_path = os.path.abspath(os.path.join(root, file))
                rel_path = os.path.relpath(abs_path, root_dir).replace('\\', '/')
                graph[rel_path] = []
                with open(abs_path, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f.read(), 'html.parser')
                    for a in soup.find_all('a', href=True):
                        link = clean_link(a['href'])
                        if not link:
                            continue
                        target_abs = os.path.normpath(os.path.join(root, link))
                        target_rel = os.path.relpath(target_abs, root_dir).replace('\\', '/')
                        if os.path.exists(target_abs) and target_rel.endswith('.html'):
                            graph[rel_path].append(target_rel)
    return graph

def check_depth(graph, start='index.html'):
    if start not in graph:
        print(f"Start node {start} not found.")
        return
    
    distances = {start: 0}
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        for neighbor in graph.get(current, []):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
                
    unreachable = [node for node in graph if node not in distances]
    
    print("=== CRAWL DEPTH REPORT (FROM index.html) ===")
    for node, dist in sorted(distances.items(), key=lambda x: x[1]):
        print(f"Depth {dist}: {node}")
        
    print("\n=== UNREACHABLE (ORPHAN) HTML PAGES ===")
    if unreachable:
        for u in unreachable:
            print(f"- {u}")
    else:
        print("None! All HTML pages are reachable.")

if __name__ == '__main__':
    graph = build_graph()
    check_depth(graph)
