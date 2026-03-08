# System Architecture

**Analysis Date:** 2026-03-08

## Overview
TechStack Global is a high-performance, SEO-centric content platform built on a "Decoupled Static" architecture. It combines a lightweight, vanilla frontend with a robust Python-based automation layer.

## Architectural Layers

### 1. Presentation Layer (Frontend)
- **Engine**: Static HTML5 + Vanilla JS.
- **Design System**: Atomic CSS principles expressed through CSS Variables in a single `style.css`.
- **Interactivity**: Selective use of Swiper.js for product showcases; otherwise, zero dependencies for maximum LCP (Largest Contentful Paint) performance.
- **SEO**: Deep use of JSON-LD for Organization, FAQ, and Product schemas.

### 2. Automation Layer (Building/Maintenance)
- **Engine**: Python 3.12.
- **Strategy**: "Script-Driven Content Management." Instead of a database, Python scripts (`blogging_project/`) act as a build-time CMS.
- **Responsibilities**: 
    - Injecting global headers/footers (`gen_head.py`).
    - Standardizing SEO metadata (`seo_fixer.py`).
    - Fixing broken product image links or affiliate tags.

### 3. Intelligence & Development (GSD)
- **Engine**: GSD (Get Shit Done) meta-prompting system.
- **Role**: Standardizes how features (like new guide layouts or affiliate grids) are researched, planned, and implemented across the team (Human + AI).

## Data Flow
1. **Creation**: Content is drafted based on templates (`posts/template.html`).
2. **Processing**: Python scripts scan the new HTML to inject branding, metadata, and cross-links.
3. **Verification**: `seo_audit.py` and `link_check.py` validate the build.
4. **Deployment**: Static assets are pushed to GitHub Pages.

## Core Performance Principles
- **No JS Framework overhead**: Minimizes time-to-interactive.
- **Glassmorphism at Scale**: Uses hardware-accelerated `backdrop-filter` but manages layout shifts strictly.
- **Image Strategy**: Responsive images with explicit aspect ratios to prevent CLS.

---
*Arch analysis: 2026-03-08*
