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

// Helper to get all HTML files
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

// 1. Favicon Fix
const indexContent = fs.readFileSync('index.html', 'utf8');
const faviconBlockMatches = indexContent.match(/<link href="assets\/icons\/favicon-32\.png\?v=6"[\s\S]*?<link href="assets\/icons\/favicon\.ico\?v=6" rel="shortcut icon" \/>/);
if (faviconBlockMatches) {
    const canonicalFaviconBlock = faviconBlockMatches[0];
    faviconFiles.forEach(file => {
        let p = file;
        if (fs.existsSync(p)) {
            let content = fs.readFileSync(p, 'utf8');

            let relativeFaviconBlock = canonicalFaviconBlock.replace(/href="assets\//g, 'href="../assets/');

            // Remove any existing favicon links
            content = content.replace(/<link[^>]+favicon[^>]+>/gi, '');
            content = content.replace(/<link[^>]+apple-touch-icon[^>]+>/gi, '');

            // Insert right before </head>
            content = content.replace(/(<\/head>)/i, `${relativeFaviconBlock}\n  $1`);

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
                // adjust links: "index.html" -> "../index.html"
                relativeHeaderBlock = relativeHeaderBlock.replace(/href="([a-zA-Z0-9-]+\.html)"/g, 'href="../$1"');
            }

            let existingHeaderMatch = content.match(/<header[^>]*>[\s\S]*?<\/header>/i);
            if (existingHeaderMatch) {
                content = content.replace(existingHeaderMatch[0], relativeHeaderBlock);
            } else {
                // insert after <body>
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

        // check if it already has script.js
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

    // Find Amazon tags
    let aTags = [...content.matchAll(/<a([^>]*)href=["']([^"']*(?:amazon\.com|amzn\.to)[^"']*)["']([^>]*)>/gi)];

    // We need to replace these correctly without messing up indices, so we'll do replace across the whole file or carefully.
    // Using replace with a replacer function on the precise regex format:
    content = content.replace(/<a([^>]*)href=["']([^"']*(?:amazon\.com|amzn\.to)[^"']*)["']([^>]*)>/gi, (match, prefix, href, suffix) => {
        let attrStr = `${prefix} ${suffix}`.replace(/\s+/g, ' ');

        let oldHref = href;
        let newHref = href;
        if (!newHref.includes('tag=techstackglob-20')) {
            if (newHref.includes('?')) {
                newHref = `${newHref}&tag=techstackglob-20`;
            } else {
                newHref = `${newHref}?tag=techstackglob-20`;
            }
        }

        let targetMatch = attrStr.match(/target=["']([^"']*)["']/i);
        let oldTarget = targetMatch ? targetMatch[1] : '';
        let newTarget = '_blank';

        let relMatch = attrStr.match(/rel=["']([^"']*)["']/i);
        let oldRel = relMatch ? relMatch[1] : '';
        let relTokens = oldRel ? oldRel.split(' ').filter(x => x) : [];
        if (!relTokens.includes('nofollow')) relTokens.push('nofollow');
        if (!relTokens.includes('noopener')) relTokens.push('noopener');
        if (!relTokens.includes('sponsored')) relTokens.push('sponsored');
        let newRel = relTokens.join(' ');

        // Formulate the new tag
        // remove existing href, target, rel from attributes string
        let remainingAttr = attrStr
            .replace(/target=["'][^"']*["']/gi, '')
            .replace(/rel=["'][^"']*["']/gi, '');

        // Reconstruct
        let newTag = `<a${remainingAttr} href="${newHref}" target="${newTarget}" rel="${newRel}">`;
        newTag = newTag.replace(/\s+/g, ' ').replace(/ >/g, '>');

        csvContent += `"${file}","${oldHref}","${newHref}","${oldRel}","${newRel}","${oldTarget}","${newTarget}"\n`;

        return newTag;
    });

    if (content !== originalContent) {
        fs.writeFileSync(file, content);
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

        // Wrap tables
        // Regex looks for <table...>...</table> and if not surrounded by <div class="table-responsive">, replaces it.
        // Better simple approach: replace <table> with <div class="table-responsive"><table> and </table> with </table></div>
        // BUT only if not already wrapped.
        // Simplest: Un-wrap all first (if we can), then re-wrap.
        content = content.replace(/<div class=["']?table-responsive["']?>\s*(<table[\s\S]*?<\/table>)\s*<\/div>/gi, '$1');
        content = content.replace(/(<table[\s\S]*?<\/table>)/gi, '<div class="table-responsive">\n$1\n</div>');

        // Fix images max-width and inline width
        content = content.replace(/<img([^>]*)>/gi, (match, attrs) => {
            // remove hardcoded width="...", height="..." unless we want them? Actually they said remove fixed widths > viewport. Or just add style max-width:100%, height:auto, loading="lazy"
            if (!attrs.includes('max-width: 100%')) {
                if (!attrs.includes('loading="lazy"')) attrs += ' loading="lazy"';
                // remove explicit width constraints that might break mobile
            }
            return `<img${attrs}>`;
        });

        // remove inline widths > 100% or absolute px widths (optional, but requested: remove fixed pixel widths > viewport)
        content = content.replace(/width:\s*[4-9][0-9]{2,}\s*px;?/gi, 'max-width: 100%;');

        if (content !== oContent) {
            fs.writeFileSync(p, content);
            console.log(`[Mobile] Responsive fixes in ${p}`);
        }
    }
});
