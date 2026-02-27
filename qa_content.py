import os
import csv
import re

def check_content():
    posts_dir = 'c:/Users/PMLS/Desktop/Youtube Shorts/b2b_blog/posts'
    output_file = 'c:/Users/PMLS/.gemini/antigravity/brain/8acb5e45-297b-4c05-ae50-1d7cdeac50b0/product_checks.csv'
    
    files = [f for f in os.listdir(posts_dir) if f.endswith('.html') and f != 'template.html']
    
    results = []
    
    for filename in files:
        path = os.path.join(posts_dir, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            has_tldr = bool(re.search(r'TL;DR', content, re.IGNORECASE))
            has_specs = bool(re.search(r'Spec|Technical', content, re.IGNORECASE) or '<table' in content.lower())
            has_proscons = bool(re.search(r'Pros|Cons', content, re.IGNORECASE))
            has_whofor = bool(re.search(r'Who is this for|Who Should Buy|Who is', content, re.IGNORECASE))
            has_faqs = bool(re.search(r'FAQ', content, re.IGNORECASE))
            has_cta = bool(re.search(r'amazon\.com', content, re.IGNORECASE))
            
            results.append([
                filename,
                'Yes',
                'Y' if has_tldr else 'N',
                'Y' if has_specs else 'N',
                'Y' if has_proscons else 'N',
                'Y' if has_whofor else 'N',
                'Y' if has_faqs else 'N',
                'Y' if has_cta else 'N'
            ])
            
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Filename', 'Exists', 'TLDR', 'Specs', 'ProsCons', 'WhoFor', 'FAQs', 'CTA (Y/N)'])
        writer.writerows(results)
        
    print(f"Content audit complete. Results saved to {output_file}")

if __name__ == '__main__':
    check_content()
