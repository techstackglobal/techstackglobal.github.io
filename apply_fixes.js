const fs = require('fs');
const path = require('path');

const faviconFiles = [
    'posts/best-laptops-for-students-2026.html',
    'posts/best-premium-laptop-for-work-2026.html',
    'posts/best-remote-work-setup-2026.html',
    'posts/budget-laptops-under-1000.html',
    'posts/do-you-need-thunderbolt-dock.html',
    'posts/is-a-4k-monitor-worth-it.html',
    'posts/is-samsung-990-pro-worth-it.html',
    'posts/samsung-odyssey-g8-vs-alienware-aw3423dwf.html'
];

const headerFiles = [
    'posts/best-laptops-for-students-2026.html',
    'posts/budget-laptops-under-1000.html',
    'privacy-policy.html',
    'terms-of-service.html'
];

const missingScriptFiles = [
    'about.html',
    'affiliate-disclosure.html',
    'amazon-stack.html',
    'blog.html',
    'contact.html',
    'index.html',
    'privacy-policy.html',
    'smart-tools.html',
    'terms-of-service.html',
    'thank-you.html'
];

const mobileRiskFiles = [
    'affiliate-disclosure.html', 'amazon-stack.html', 'contact.html', 'index.html',
    'posts/alienware-aw3423dwf-review.html', 'posts/alienware-aw3423dwf-vs-odyssey-g8.html',
    'posts/apple-macbook-pro-m4-pro-review.html', 'posts/best-laptops-for-students-2026.html',
    'posts/best-premium-laptop-for-work-2026.html', 'posts/budget-laptops-under-1000.html',
    'posts/dell-xps-15-9530-review.html', 'posts/do-you-need-thunderbolt-dock.html',
    'posts/is-a-4k-monitor-worth-it.html', 'posts/samsung-990-pro-ssd-review.html',
    'posts/samsung-odyssey-g8-review.html', 'posts/shure-sm7b-review.html',
    'posts/shure-sm7b-vs-sm7db.html', 'posts/shure-sm7db-review.html',
    'posts/surface-laptop-studio-2-review.html', 'privacy-policy.html',
    'smart-tools.html', 'terms-of-service.html', 'thank-you.html'
];

function getHtmlFiles(dir, files_) {
    files_ = files_ || [];
    let files = fs.readdirSync(dir);
    for (let file of files) {
        let name = path.join(dir, file);
        if (fs.statSync(name).isDirectory()) {
            if (!['.git', 'node_modules', 'images', 'assets'].includes(file)) {
                getHtmlFiles(name, files_);
            }
        } else if (name.endsWith('.html') && !name.startsWith('old_')) {
            files_.push(name);
        }
    }
    return files_;
}

const indexContent = fs.readFileSync('index.html', 'utf8');

// 1. Favicon Fix
const faviconBlockMatches = indexContent.match(/<link href="assets\/icons\/favicon-32\.png\?v=6"[\s\S]*?<link href="assets\/icons\/favicon\.ico\?v=6" rel="shortcut icon" \/>/);
if (faviconBlockMatches) {
    const canonicalFaviconBlock = faviconBlockMatches[0];
    faviconFiles.forEach(file => {
        let p = file;
        if (fs.existsSync(p)) {
            let content = fs.readFileSync(p, 'utf8');

            let relativeFaviconBlock = file.includes('posts/') ? canonicalFaviconBlock.replace(/href="assets\//g, 'href="../assets/') : canonicalFaviconBlock;

            content = content.replace(/<link[^>]+favicon[^>]+>/gi, '');
            content = content.replace(/<link[^>]+apple-touch-icon[^>]+>/gi, '');
            content = content.replace(/(<\/head>)/i, `${relativeFaviconBlock}\n$1`);

            fs.writeFileSync(p, content);
            console.log(`[Favicon] Fixed ${p}`);
        }
    });
}

// 2. Header Fix
const headerMatches = indexContent.match(/<header class="glass-header">[\s\S]*?<\/header>/);
if (headerMatches) {
    const canonicalHeaderBlock = headerMatches[0];
    headerFiles.forEach(file => {
        let p = file;
        if (fs.existsSync(p)) {
            let content = fs.readFileSync(p, 'utf8');

            let relativeHeaderBlock = canonicalHeaderBlock;
            if (file.includes('posts/')) {
                relativeHeaderBlock = relativeHeaderBlock.replace(/href="([a-zA-Z0-9-]+\.html)"/g, 'href="../$1"');
            }

            let existingHeaderMatch = content.match(/<header[^>]*>[\s\S]*?<\/header>/i);
            if (existingHeaderMatch) {
                content = content.replace(existingHeaderMatch[0], relativeHeaderBlock);
            } else {
                content = content.replace(/(<body[^>]*>)/i, `$1\n  ${relativeHeaderBlock}`);
            }

            fs.writeFileSync(p, content);
            console.log(`[Header] Fixed ${p}`);
        }
    });
}

// 3. Scripts Fix
missingScriptFiles.forEach(file => {
    let p = file;
    if (fs.existsSync(p)) {
        let content = fs.readFileSync(p, 'utf8');
        if (!content.match(/<script[^>]+script\.js"/i)) {
            let scriptTag = file.includes('posts/') ? '<script src="../script.js"></script>' : '<script src="script.js"></script>';
            content = content.replace(/(<\/body>)/i, `  ${scriptTag}\n$1`);
            fs.writeFileSync(p, content);
            console.log(`[Script] Added to ${p}`);
        }
    }
});

// 4. Affiliate Links Fix & Tracker report
let csvContent = "File,Old URL,New URL,Old Rel,New Rel,Old Target,New Target\n";
const allHtmlFiles = getHtmlFiles('.');

allHtmlFiles.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    let originalContent = content;

    // Custom parsing opening tags <a>
    let newContent = content.replace(/<a\s+([^>]+)>/gi, (match, innerProps) => {
        let lowerProps = innerProps.toLowerCase();

        // Check if it's an amazon link
        if (!lowerProps.includes('amazon.com') && !lowerProps.includes('amzn.to')) {
            return match;
        }

        // Extract href
        let hrefMatch = innerProps.match(/href=["']([^"']+)["']/i);
        if (!hrefMatch) return match;
        let oldHref = hrefMatch[1];
        let newHref = oldHref;

        // Modify HRREF
        if (!newHref.toLowerCase().includes('tag=techstackglob-20')) {
            if (newHref.includes('?')) {
                newHref = `${newHref}&tag=techstackglob-20`;
            } else {
                newHref = `${newHref}?tag=techstackglob-20`;
            }
        }

        // Extract target
        let targetMatch = innerProps.match(/target=["']([^"']*)["']/i);
        let oldTarget = targetMatch ? targetMatch[1] : '';
        let newTarget = '_blank';

        // Extract rel
        let relMatch = innerProps.match(/rel=["']([^"']*)["']/i);
        let oldRel = relMatch ? relMatch[1] : '';
        let relTokens = oldRel ? oldRel.split(' ').filter(x => x) : [];

        let requiredTokens = ['nofollow', 'noopener', 'sponsored'];
        requiredTokens.forEach(token => {
            if (!relTokens.map(t => t.toLowerCase()).includes(token)) {
                relTokens.push(token);
            }
        });
        let newRel = relTokens.join(' ');

        // Reconstruct
        let remaining = innerProps
            .replace(/href=["'][^"']+["']/gi, '')
            .replace(/target=["'][^"']*["']/gi, '')
            .replace(/rel=["'][^"']*["']/gi, '');

        // create clean tag
        let newTag = `<a ${remaining.trim()} href="${newHref}" target="${newTarget}" rel="${newRel}">`.replace(/\s+/g, ' ').replace(' >', '>');

        csvContent += `"${file}","${oldHref}","${newHref}","${oldRel}","${newRel}","${oldTarget}","${newTarget}"\n`;

        return newTag;
    });

    if (newContent !== originalContent) {
        fs.writeFileSync(file, newContent);
        console.log(`[Affiliate] Fixed in ${file}`);
    }
});

fs.writeFileSync('affiliate_report.csv', csvContent);

// 5. Mobile Overflow
mobileRiskFiles.forEach(file => {
    let p = file;
    if (fs.existsSync(p)) {
        let content = fs.readFileSync(p, 'utf8');
        let oContent = content;

        // Remove existing table-responsive div to rebuild them carefully
        content = content.replace(/<div class=["']table-responsive["']>\s*(<table[\s\S]*?<\/table>)\s*<\/div>/gi, '$1');
        content = content.replace(/(<table[\s\S]*?<\/table>)/gi, '<div class="table-responsive">\n$1\n</div>');

        // Images: max-width: 100%, height: auto, loading="lazy"
        // Also remove inline width="..." height="..." to let CSS logic handle it
        content = content.replace(/<img[^>]+>/gi, (match) => {
            let newImg = match;
            if (!newImg.includes('max-width: 100%') && !newImg.includes('max-width:100%')) {
                if (!newImg.includes('style=')) {
                    newImg = newImg.replace(/<img/i, '<img style="max-width: 100%; height: auto;"');
                } else {
                    newImg = newImg.replace(/style=["']([^"']*)["']/i, 'style="max-width: 100%; height: auto; $1"');
                }
            }
            if (!newImg.includes('loading=')) newImg = newImg.replace(/<img/i, '<img loading="lazy"');
            return newImg;
        });

        // Inline width fixes for extreme pixels e.g. width: 600px
        content = content.replace(/width:\s*[4-9][0-9]{2,}px;?/gi, 'max-width: 100%; height: auto;');

        if (content !== oContent) {
            fs.writeFileSync(p, content);
            console.log(`[Mobile] Responsive fixes in ${p}`);
        }
    }
});

// 6. Orphan Fix: samsung-odyssey-g8-vs-alienware-aw3423dwf.html
// Attach link from best-ultrawide-monitors-2026.html
let p1 = 'posts/best-ultrawide-monitors-2026.html';
if (fs.existsSync(p1)) {
    let c1 = fs.readFileSync(p1, 'utf8');
    if (!c1.includes('samsung-odyssey-g8-vs-alienware-aw3423dwf.html')) {
        // Add inside a relevant text paragraph
        c1 = c1.replace(/Our full comparison of these top contenders/i, 'Our full <a href="samsung-odyssey-g8-vs-alienware-aw3423dwf.html">AW3423DWF vs Odyssey G8 comparison</a>');
        if (c1 === fs.readFileSync(p1, 'utf8')) {
            // Find another anchor
            c1 = c1.replace(/Alienware AW3423DWF/i, '<a href="samsung-odyssey-g8-vs-alienware-aw3423dwf.html">AW3423DWF vs Odyssey G8 comparison</a> (also featuring the Alienware AW3423DWF)');
        }
        fs.writeFileSync(p1, c1);
        console.log(`[Orphan] Added to ${p1}`);
    }
}

let p2 = 'posts/alienware-aw3423dwf-review.html';
if (fs.existsSync(p2)) {
    let c2 = fs.readFileSync(p2, 'utf8');
    if (!c2.includes('samsung-odyssey-g8-vs-alienware-aw3423dwf.html')) {
        c2 = c2.replace(/(<\/article>)/i, `<p>If you're still on the fence, see our <a href="samsung-odyssey-g8-vs-alienware-aw3423dwf.html">AW3423DWF vs Odyssey G8 comparison</a> for a deep-dive against its biggest rival.</p>\n$1`);
        fs.writeFileSync(p2, c2);
        console.log(`[Orphan] Added to ${p2}`);
    }
}

console.log('All fixes applied successfully!');
