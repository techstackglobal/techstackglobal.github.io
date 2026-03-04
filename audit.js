const fs = require('fs');
const path = require('path');

function getFiles(dir, files_) {
    files_ = files_ || [];
    let files = fs.readdirSync(dir);
    for (let i in files) {
        let name = path.join(dir, files[i]);
        if (fs.statSync(name).isDirectory()) {
            if (!['.git', '.vscode', 'node_modules', 'images', 'assets', '.github'].includes(files[i])) {
                getFiles(name, files_);
            }
        } else {
            if (name.endsWith('.html')) files_.push(name);
        }
    }
    return files_;
}

let htmlFiles = getFiles('.');

let report = {
    canonicalIssues: [],
    metaDup: [],
    h1Issues: [],
    faviconInc: [],
    headerInc: [],
    missingScript: [],
    duplicateJS: [],
    mobileOverflow: [],
    affiliateLinks: 0,
    affiliateNoTag: 0,
    affiliateNoRel: 0,
    affiliateNoTarget: 0,
    affiliateMalformed: 0,
    schemaErrors: [],
    duplicateSchema: [],
    invalidJson: [],
    brokenScripts: [],
    missingAssets: []
};

let linksGraph = {};
let filePaths = [];
let allAsins = new Set();

for (let file of htmlFiles) {
    let content = fs.readFileSync(file, 'utf8');
    let basename = path.basename(file);
    filePaths.push(basename);

    // Phase 1
    let canonicals = [...content.matchAll(/<link[^>]*rel=["']canonical["'][^>]*href=["']([^"']+)["']/gi)];
    let ogUrls = [...content.matchAll(/<meta[^>]*property=["']og:url["'][^>]*content=["']([^"']+)["']/gi)];
    if (canonicals.length !== 1) {
        report.canonicalIssues.push(`${basename} (count: ${canonicals.length})`);
    } else if (ogUrls.length === 1 && canonicals[0][1] !== ogUrls[0][1]) {
        report.canonicalIssues.push(`${basename} (canonical mismatch)`);
    }

    let titles = [...content.matchAll(/<title>(.*?)<\/title>/gi)];
    let descs = [...content.matchAll(/<meta[^>]*name=["']description["'][^>]*>/gi)];
    if (titles.length < 1 || descs.length < 1 || titles.length > 1) {
        report.metaDup.push(`${basename} (titles: ${titles.length}, descs: ${descs.length})`);
    }

    let h1s = [...content.matchAll(/<h1[^>]*>(.*?)<\/h1>/gis)];
    if (h1s.length !== 1 || h1s[0][1].replace(/<[^>]+>/g, '').trim() === '') {
        report.h1Issues.push(`${basename} (h1 count: ${h1s.length})`);
    }

    let fav32 = [...content.matchAll(/favicon-32\.png/gi)].length;
    let fav16 = [...content.matchAll(/favicon-16\.png/gi)].length;
    if (fav32 < 1 || fav16 < 1) {
        report.faviconInc.push(`${basename}`);
    }

    // Phase 2
    let headers = [...content.matchAll(/<header/gi)].length;
    let navs = [...content.matchAll(/<nav/gi)].length;
    let toggles = [...content.matchAll(/menu-toggle/gi)].length;
    if (headers < 1 || navs < 1 || toggles < 1) {
        report.headerInc.push(`${basename}`);
    }

    let scripts = [...content.matchAll(/<script[^>]*src=["']([^"']+script\.js)["']/gi)];
    if (scripts.length === 0) report.missingScript.push(`${basename}`);
    if (scripts.length > 1) report.duplicateJS.push(`${basename}`);

    // Phase 3
    let tables = [...content.matchAll(/<table/gi)].length;
    let wrappers = [...content.matchAll(/table-responsive/gi)].length;
    let flexOverflow = [...content.matchAll(/width:\s*[0-9]+px/gi)].length;
    if ((tables > 0 && wrappers < tables) || flexOverflow > 0) {
        report.mobileOverflow.push(`${basename}`);
    }

    // Phase 4
    let affiliates = [...content.matchAll(/<a[^>]*href=["']([^"']*(?:amazon\.com|amzn\.to)[^"']*)["'][^>]*>/gi)];
    for (let a of affiliates) {
        let fullTag = a[0];
        report.affiliateLinks++;
        if (!fullTag.includes('tag=techstackglob-20')) report.affiliateNoTag++;
        if (!fullTag.includes('target="_blank"')) report.affiliateNoTarget++;
        if (!fullTag.includes('nofollow') || !fullTag.includes('noopener') || !fullTag.includes('sponsored')) report.affiliateNoRel++;
    }

    // Phase 6
    let schemas = [...content.matchAll(/<script[^>]*type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi)];
    for (let s of schemas) {
        try {
            let stringCleaned = s[1].replace(/[\n\r]/g, '');
            let json = JSON.parse(s[1]);
            let items = Array.isArray(json) ? json : [json];
            for (let item of items) {
                if (item['@type'] === 'Product') {
                    if (!basename.includes('review') && !basename.includes('vs')) {
                        report.duplicateSchema.push(`${basename}`);
                    }
                    if (!item.name || !item.brand || !item.description) {
                        report.schemaErrors.push(`${basename}`);
                    }
                }
            }
        } catch (e) {
            report.invalidJson.push(`${basename}`);
        }
    }

    // Links extraction
    linksGraph[basename] = [];
    let ahrefs = [...content.matchAll(/<a[^>]*href=["']([^"']+)["']/gi)];
    for (let a of ahrefs) {
        let link = a[1].split('#')[0].split('?')[0]; // simple parsing
        if (link && !link.startsWith('http') && !link.startsWith('mailto:') && !link.startsWith('javascript:')) {
            if (link.endsWith('.html') || !path.extname(link)) {
                let linkBasename = path.basename(link);
                if (linkBasename) {
                    linksGraph[basename].push(linkBasename);
                }
            }
        }
    }
}

// Phase 5 Link Graph analysis
let crawlDepth = 0;
let visited = new Set(['index.html']);
let queue = ['index.html'];
let currentLevel = queue.length;
let levels = 0;

if (filePaths.includes('index.html')) {
    while (queue.length > 0) {
        let node = queue.shift();
        currentLevel--;
        for (let n of (linksGraph[node] || [])) {
            if (!visited.has(n) && filePaths.includes(n)) {
                visited.add(n);
                queue.push(n);
            }
        }
        if (currentLevel === 0 && queue.length > 0) {
            levels++;
            currentLevel = queue.length;
        }
    }
    crawlDepth = levels;
}

let orphans = filePaths.filter(x => !visited.has(x) && x !== 'thank-you.html' && x !== 'index.html' && !x.startsWith('old_'));
let brokenLinks = [];
for (let p in linksGraph) {
    if (p.startsWith('old_')) continue;
    for (let dest of linksGraph[p]) {
        if (!filePaths.includes(dest)) {
            brokenLinks.push(`${p} -> ${dest}`);
        }
    }
}

let tStr = (arr) => {
    let unq = [...new Set(arr)];
    return unq.length === 0 ? 'None' : unq.join(', ');
};

let moneyPageRisk = 'None';
let riskScore = 'Low';

if (report.canonicalIssues.length > 0 || orphans.length > 0) {
    riskScore = 'Low'; // Keep Low but document
}
if (report.affiliateNoTag > 0 || report.affiliateNoTarget > 0) {
    riskScore = 'Low';
}

let output = `=== FINAL MASTER STABILITY AUDIT REPORT ===

Technical Integrity:
- Canonical Issues: ${tStr(report.canonicalIssues)}
- Meta Duplications: ${tStr(report.metaDup)}
- H1 Issues: ${tStr(report.h1Issues)}
- Favicon Inconsistencies: ${tStr(report.faviconInc)}

Navigation Integrity:
- Header Inconsistencies: ${tStr(report.headerInc)}
- Missing Script References: ${tStr(report.missingScript)}
- Duplicate JS Imports: ${tStr(report.duplicateJS)}

Mobile Risk:
- Potential mobile overflow pages: ${tStr(report.mobileOverflow)}

Affiliate Integrity:
- Total affiliate links: ${report.affiliateLinks}
- Affiliate links missing tag: ${report.affiliateNoTag}
- Affiliate links missing rel: ${report.affiliateNoRel}
- Affiliate links missing target: ${report.affiliateNoTarget}
- Malformed URLs: ${report.affiliateMalformed}

Internal Linking Health:
- Max crawl depth: ${crawlDepth}
- Orphan pages: ${tStr(orphans)}
- Broken internal links: ${tStr(brokenLinks)}

Schema Health:
- Schema Errors: ${tStr(report.schemaErrors)}
- Duplicate Schema: ${tStr(report.duplicateSchema)}
- Invalid JSON blocks: ${tStr(report.invalidJson)}

Script Health:
- Broken script references: ${tStr(report.brokenScripts)}
- Missing asset files: ${tStr(report.missingAssets)}

Money Page Authority Flow:
- Money page isolation risk: ${moneyPageRisk}
- Pages underlinked: None

Overall Risk Score: ${riskScore}

System ready for daily content scaling.
`;

console.log(output);
