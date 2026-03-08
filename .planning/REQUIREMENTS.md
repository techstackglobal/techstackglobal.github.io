# Project Requirements

**Generated:** 2026-03-08

## 🧱 Functional Requirements

### FR-01: SEO Infrastructure
- [✓] Must have an automated `<title>` and `<meta description>` auditor.
- [✓] Every guide MUST have a single `<h1>` tag for search value.
- [✓] Sitemap must be valid for Google Search Console.
- [ ] Automate the "Triangle Internal Linking" pattern (Hub ↔ Article ↔ Comparison).

### FR-02: Content Components
- [✓] Affiliate disclosure section must be present "above the fold" on reviews.
- [✓] Product carousels (Swiper) must link to affiliate targets.
- [ ] Sidebar for desktop articles: "Quick Verdict", "Navigation Links".
- [ ] FAQ Schema support for every guide to boost SERP real estate.

### FR-03: Performance & Mobile
- [✓] Page load time < 1.5s for 4G mobile devices.
- [✓] 0px horizontal overflow on 320px/375px viewports.
- [✓] Google PageSpeed Insights: Score > 90 for mobile and desktop.

## 🧱 Technical Requirements

### TR-01: Automation Suite
- [✓] Content generation scripts must be idempotent (safe to re-run).
- [ ] Error-free sitemap generation via Python.
- [ ] Automated form submission verification.

### TR-02: GSD Workflow Standard
- [✓] All new feature requests must result in a `.planning/phases/` plan.
- [✓] Research must be conducted for any new technology introductions.
- [✓] Verification steps must be documented and passed before merge.

## 🏁 Out of Scope (Non-Requirements)
- User authentication and accounts.
- Real-time commenting.
- Dynamic data polling (all content is static/build-time).

---
*Last updated: 2026-03-08*
