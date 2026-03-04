const fs = require('fs');

function fixImages(filePath) {
    if (!fs.existsSync(filePath)) return;
    let content = fs.readFileSync(filePath, 'utf8');
    let originalContent = content;

    // Remove the intrusive inline style from our previous bulk script
    // that ruins object-fit by forcing height: auto.

    // Specific match for product-thumbnails and swiper slides that had this injected:
    // Actually, let's just safely strip `style="max-width: 100%; height: auto;"` 
    // and `style="max-width: 100%; height: auto; "` if it's there.
    // Also remove generic inline style if it ONLY contains that.

    content = content.replace(/style=["']max-width:\s*100%;\s*height:\s*auto;?\s*["']/gi, '');

    // For images that had object-fit contain inside the inline style like we saw in some debug output:
    content = content.replace(/style=["']max-width:\s*100%;\s*height:\s*auto;\s*object-fit:\s*contain;?["']/gi, 'style="object-fit: contain;"');

    // Clean up empty styles
    content = content.replace(/style=["']\s*["']/gi, '');

    if (content !== originalContent) {
        fs.writeFileSync(filePath, content);
        console.log(`Fixed images in ${filePath}`);
    } else {
        console.log(`No changes needed for ${filePath}`);
    }
}

// Fix the two pages the user explicitly mentioned
fixImages('amazon-stack.html');
fixImages('index.html');
