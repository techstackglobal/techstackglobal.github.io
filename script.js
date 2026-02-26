// Minimal JS for interactions (No 3D canvas libraries)
document.addEventListener('DOMContentLoaded', () => {
    // Current Year for Footer
    document.getElementById('year').textContent = new Date().getFullYear();

    // Smooth scrolling for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});

/**
 * Affiliate & Tracking Helpers
 */
function buildAffiliateLink(url, campaign) {
    try {
        // If URL already has ?, append with &, else with ?
        var separator = url.indexOf('?') !== -1 ? '&' : '?';
        // Build utm string
        var utm = 'utm_source=techstackglobal&utm_medium=affiliate&utm_campaign=' + encodeURIComponent(campaign);
        return url + separator + utm;
    } catch (e) {
        return url;
    }
}

function trackAffiliateClick(productShortName) {
    console.log('Tracking affiliate click for:', productShortName);
    // For gtag / GA4
    if (window.gtag) {
        gtag('event', 'affiliate_click', {
            'event_category': 'affiliate',
            'event_label': productShortName
        });
    }
    // If using dataLayer:
    if (window.dataLayer) {
        window.dataLayer.push({
            'event': 'affiliate_click',
            'product': productShortName
        });
    }
}
