# Project Structure

**Analysis Date:** 2026-03-08

## Core Components

### Root Level
- `index.html`: Main landing page with hero, categories, and trust signals.
- `blog.html`: Hub for all software reviews and category listings.
- `style.css`: The "master" design system and global styles.
- `script.js`: Core UI interactivity and Swiper initialization.
- `sitemap.xml`: SEO index for search engines.

### Content
- `posts/`: Subdirectory containing all review articles (e.g., `best-microphones-...html`).

### Assets
- `assets/images/`: Logos, product photos, and branding assets.
- `assets/icons/`: Favicons and SVG iconography.

### Infrastructure & Automation
- `blogging_project/`: Python modules for core business logic:
    - `generator_base.py`: Likely a base class for HTML generators.
    - `content_manager.py` (referenced scripts): Managing post metadata.
- `tools/`: Utility workspace for maintenance scripts.
- `.claude/`, `.gemini/`, `.opencode/`, `.codex/`: GSD configuration and command sets.
- `.venv/`: Dedicated Python virtual environment.

### SEO & Verification Tools
- `seo_audit.py`: Scans pages for metadata, headings, and schema compliance.
- `link_check.py`: Validates internal and external link health.
- `generate_sitemap.py`: Synchronizes the XML sitemap with new posts.
- `deploy_site.py`: Orchestrates the transition to production.

## Dependency Management
- `package.json`: npm configuration (mostly for GSD and server).
- `requirements.txt`: Python package list (bs4, requests, etc.).
- `.gitignore`: Prevents VENV and node_modules from being tracked.

---
*Structure analysis: 2026-03-08*
