// Minimal JS for interactions (No 3D canvas libraries)
document.addEventListener('DOMContentLoaded', () => {
    // Current Year for Footer
    document.getElementById('year').textContent = new Date().getFullYear();

    // Mobile Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (menuToggle && navLinks) {
        const toggleMenu = (state) => {
            const isActive = state !== undefined ? state : !navLinks.classList.contains('active');
            navLinks.classList.toggle('active', isActive);
            const icon = menuToggle.querySelector('i');
            icon.classList.replace(isActive ? 'fa-bars' : 'fa-xmark', isActive ? 'fa-xmark' : 'fa-bars');
        };

        menuToggle.addEventListener('click', (e) => {
            e.stopPropagation();
            toggleMenu();
        });

        // Close menu when a link is clicked
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => toggleMenu(false));
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (navLinks.classList.contains('active') && !navLinks.contains(e.target) && !menuToggle.contains(e.target)) {
                toggleMenu(false);
            }
        });
    }

    // Smooth scrolling for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
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
