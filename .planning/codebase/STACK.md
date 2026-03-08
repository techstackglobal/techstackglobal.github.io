# Technology Stack

**Analysis Date:** 2026-03-08

## Languages

**Primary:**
- **HTML5** - Backbone of the blog and post pages.
- **CSS3 (Vanilla)** - Custom design system using CSS variables and modern flexbox/grid.
- **JavaScript (Vanilla)** - Interactive UI logic, animations, and Swiper initialization.

**Secondary:**
- **Python 3.12** - Heavy lifting for automation: SEO audits, sitemap generation, content updates, and deployment checks.

## Runtime

**Environment:**
- **Web Browser** - User-facing runtime for the static site.
- **Python 3.x** - Execution environment for `blogging_project` and other utility scripts.
- **Node.js** - Used for local dev server and managing GSD commands.

**Package Manager:**
- **npm** - Handles dev dependencies and GSD systems.
- **pip** - Manages Python dependencies (captured in `requirements.txt`).

## Frameworks

**Core:**
- **Vanilla Core** - No heavyweight JS framework (React/Vue) is used for the frontend to maintain speed.
- **Swiper.js** - Used for interactive carousels.
- **Font Awesome 6** - Iconography system.

**Testing & QA:**
- **Custom Python Suite** - Hand-rolled scripts for SEO auditing, link checking, and form validation.

## Key Dependencies

**Critical:**
- **Swiper** - Essential for product showcases.
- **Google Fonts (Inter)** - Core typography foundation.
- **Python `requests`** - Used in link checkers and API interactions.
- **Python `BeautifulSoup4`** - Core for many HTML manipulation scripts.

## Platform Requirements

**Development:**
- Cross-platform (Windows/Mac/Linux).
- Requires Python 3.12 and Node.js.

**Production:**
- **GitHub Pages** - Static hosting target.
- **Cloudflare** (likely) - For CDN and performance.

---
*Stack analysis: 2026-03-08*
*Based on codebase survey.*
