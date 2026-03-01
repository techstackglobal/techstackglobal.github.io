import os
import re

affiliate_text = '<strong>Affiliate disclosure:</strong> This page contains affiliate links. If you purchase via these links we may earn a commission at no extra cost to you. This helps support our research and operating costs.'

# Step 1: Update all reviews in /posts
directory = 'posts'
for filename in os.listdir(directory):
    if not filename.endswith('.html'): continue
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f: content = f.read()
    
    # Standardize affiliate disclosures
    content = re.sub(r'<p class=[\'\"]affiliate-disclosure[\'\"][^>]*>.*?</p>', f'<p class=\"affiliate-disclosure\">{affiliate_text}</p>', content, flags=re.DOTALL)
    content = re.sub(r'<div class=[\'\"]affiliate-disclaimer[\'\"][^>]*>.*?</div>', f'<div class=\"affiliate-disclosure\">\n    {affiliate_text}\n</div>', content, flags=re.DOTALL)
    
    # For SM7B specifically, clean emojis and dashes
    if filename == 'shure-sm7b-review.html':
        content = re.sub(r'🎙️|🎛️|🏢|🔊|🎵|🔌|💰|🎒|✅|❌|✨|🚀', '', content)
        content = content.replace('—', ':').replace('–', '-')
        
    with open(filepath, 'w', encoding='utf-8') as f: f.write(content)

# Step 2: Fix Navigation/Library Pages
if os.path.exists('blog.html'):
    with open('blog.html', 'r', encoding='utf-8') as f: blog_content = f.read()
    # Find the SM7B review element and remove it
    blog_content = re.sub(r'<!-- Reviews -->.*?Read Review &rarr;</a>\n\s*</div>', '', blog_content, flags=re.DOTALL)
    with open('blog.html', 'w', encoding='utf-8') as f: f.write(blog_content)
    
if os.path.exists('amazon-stack.html'):
    with open('amazon-stack.html', 'r', encoding='utf-8') as f: stack_content = f.read()
    if 'shure-sm7b-review.html' not in stack_content:
        # Create the SM7B card for Amazon Stack
        sm7b_card = '''
                    <! Shure SM7B>
                        <div class="product-item glass-card">
                            <div class="product-thumbnail-wrapper">
                                <img src="posts/images/shure-sm7b-primary.jpg" alt="Shure SM7B dynamic studio microphone profile view thumbnail" class="product-thumbnail" loading="lazy">
                            </div>
                            <div class="product-info">
                                <div class="product-meta">Broadcast Standard</div>
                                <h3><a href="posts/shure-sm7b-review.html" aria-label="Open review: Shure SM7B">Shure SM7B Microphone</a></h3>
                                <a href="posts/shure-sm7b-review.html" class="view-review-cta">View Review <i class="fa-solid fa-arrow-right"></i></a>
                            </div>
                        </div>'''
        # Insert before SM7dB
        stack_content = stack_content.replace('<! Shure SM7dB>', sm7b_card + '\n\n                    <! Shure SM7dB>')
        with open('amazon-stack.html', 'w', encoding='utf-8') as f: f.write(stack_content)

print('Success.')
