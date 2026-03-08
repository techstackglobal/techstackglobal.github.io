# Risks & Considerations

**Analysis Date:** 2026-03-08

## High-Priority Concerns

### 1. Mobile Layout Integrity (Horizontal Overflow)
- **Problem**: Large tables, un-wrapped images, and fixed-width `iframe` embeds often break the layout on 320px/375px screens.
- **Goal**: Maintain 0-pixel horizontal scroll on all blog posts.
- **Action**: Always wrap tables in `.table-responsive` and use `max-width: 100%` globally.

### 2. Affiliate Compliance & Disclosures
- **Problem**: FTC and Amazon require "clear and conspicuous" affiliate disclosures.
- **Goal**: Every page matching `posts/*.html` MUST have the affiliate disclosure above the fold.
- **Action**: Automate checks in `seo_audit.py` for the disclosure component.

### 3. SEO Entropy (Sitemap Synchronization)
- **Problem**: As more posts are added, the `sitemap.xml` and `robots.txt` can lag, leading to crawl errors.
- **Goal**: Auto-update the sitemap every time a new `.html` is added to `/posts`.
- **Action**: Integrate `generate_sitemap.py` into the deployment or post-creation workflow.

### 4. Code Refactoring Side-Effects
- **Problem**: Global scripts like `gen_head.py` or `seo_fixer.py` can inadvertently overwrite custom page-specific metadata.
- **Goal**: Use idempotent scripts that check for existing tags before injecting.
- **Action**: Refactor Python tools to use "Search-then-Inject" patterns instead of blind replacements.

### 5. Google Search Console "Couldn't Fetch"
- **Problem**: Intermittent fetch errors in Search Console.
- **Goal**: Resolve and maintain green status for sitemaps.
- **Action**: Ensure the sitemap is served with `Content-Type: application/xml` and contains simplified namespaces.

## Technical Debt Tracker
- [ ] Migrate `blogging_project/` scripts into a unified package structure.
- [ ] Implement a lightweight image optimization pipeline for `assets/images`.
- [ ] Harmonize CSS classes between root `index.html` and guide pages (`posts/`).

---
*Concerns analysis: 2026-03-08*
