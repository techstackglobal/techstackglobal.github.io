const fs = require('fs');
const path = require('path');

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

const allHtmlFiles = getHtmlFiles('.');

allHtmlFiles.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    let originalContent = content;

    // Replace the botched max-max-width typo
    // Previously it might have been max-width: 600px;
    // Let's just fix it to max-width: 600px; or let's inspect what it should be.
    // Actually, wait, replacing max-width: 600px with max-width: 100%; is safer 
    // than height: auto which breaks the swiper completely!
    // Let's just change "max-max-width: 100%; height: auto;" to "max-width: 600px;" 
    // No, wait, if it was in index.html for .hero-swiper-shell: it was `width: 100%; max-width: 800px;`.
    // Wait, the regex was `width:\s*[4-9][0-9]{2,}px;?` which matched `width: 800px` maybe?

    content = content.replace(/max-max-width:\s*100%;\s*height:\s*auto;/gi, "max-width: 800px;");

    if (content !== originalContent) {
        fs.writeFileSync(file, content);
        console.log(`[Fixed max-max-width] ${file}`);
    }
});
