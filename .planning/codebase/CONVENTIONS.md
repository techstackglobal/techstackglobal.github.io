# Coding & Content Conventions

**Analysis Date:** 2026-03-08

## Frontend Patterns

### HTML Structure
- **Root Element**: `<main class="container">` for consistent content column width.
- **Article Container**: `<article class="entry-content">` or `<div class="glass-card">` for layout.
- **Headings**: 
  - One `<h1>` per page.
  - Sequential `<h2>`, `<h3>` hierarchy.
  - No skipping heading levels (Accessibility/SEO).
- **Meta-Data**: 
  - Standardized OpenGraph, Twitter Cards, and Schema.org.
  - Canonical URL points to `techstackglobal.github.io`.

### CSS (Vanilla BEM-Lite)
- Use **CSS Variables** defined in `:root`.
- Scope layout components: `.glass-card`, `.product-item`, `.btn-primary`.
- **Naming**: Dash-separated lowercase (e.g., `section-padding`).
- **Responsive**: Mobile-first media queries (320px, 375px, 768px, 1024px).

### JavaScript
- Vanilla JS preferred.
- Use `DOMContentLoaded` for initialization.
- Heavy use of `IntersectionObserver` for scroll-triggered animations.

## Python (Automation) Patterns
- **Docstrings**: Functional descriptions on all classes/methods.
- **Paths**: Use absolute paths or project-root relative paths.
- **Dependencies**: Listed in `requirements.txt`.
- **Parsing**: `BeautifulSoup4` is the standard for DOM manipulation.
- **Logging**: Detailed stdout logging for audit trails.

## GSD Workflow (The New Standard)
- **Phase Management**: All major changes MUST follow the Discuss → Plan → Research → Execute → Verify cycle.
- **Documentation**: 
  - Phase plans stored in `.planning/phases/`.
  - Research stored in `.planning/research/`.
- **Commits**: Atomic commits with descriptive prefixes (`feat:`, `fix:`, `docs:`, `chore:`).

### 6. 🛡️ GSD Safety & Implementation Rules (The "Antigravity Guard")
- **NO structural code changes without explicit approval**: This applies to new CSS classes, layout wrappers, or directory shifts.
- **Spec-Driven**: Always create a `.planning/phases/` document BEFORE modifying operational code.
- **Approval Flow**: Present the plan to the USER. Do not EXECUTE until the USER provides a confirmative response.
- **Verification First**: Every structural change must be followed by a full `seo_audit.py` and `link_check.py` run to ensure zero regression.

### 7. 🖋️ The "No-AI" Content Mandate (100% Human-First)
- **Zero AI-Speak**: Content must NOT sound AI-written even 1%. No fluffy introductions, generic summaries, or robotic transitions.
- **Direct & Concise**: Avoid standard AI filler (e.g., "In the ever-evolving world of...", "It’s important to note...").
- **Opinionated & Raw**: Use personal expertise and real-world testing data. If a product is bad, say it. If it's the best, explain why based on data, not generic praise.
- **No Em-Dash Over-Use**: Standard AI often uses long sentences with em-dashes. Break these up into short, punchy, human sentences.
- **Verification**: Content will be manually reviewed against this standard by the USER before any merge.

---
*Last updated: 2026-03-08*
