# TechStack Global Blog

The elite B2B authority platform for SaaS tools, web hosting, AI technology, and digital assets. Build your ultimate startup tech stack.

## 🚀 Overview

This repository contains the source code for the TechStack Global blog, a high-performance static website designed with a modern dark theme and glassmorphism aesthetics.

## 📂 Project Structure

-   `index.html`: The landing page and hero section.
-   `blog.html`: Category-based software review listing.
-   `posts/`: Directory containing individual blog posts and reviews.
-   `assets/`: Shared assets including images, icons, and fonts.
-   `style.css`: Core design system and responsive styles.
-   `script.js`: Interactive UI logic and animations.
-   `blogging_project/`: Python scripts and utilities for automation.

## 🛠️ Getting Started

### Prerequisites

-   Node.js (for local development server)
-   Python 3.x (for blog automation scripts)

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/techstackglobal/techstackglobal.github.io.git
    cd techstackglobal.github.io
    ```

2.  Install development dependencies:
    ```bash
    npm install
    ```

3.  Start the local development server:
    ```bash
    npm start
    ```

## 📝 Writing New Posts

Use the `posts/template.html` file as a starting point for new articles. The site uses semantic HTML and JSON-LD schema for FAQ sections to ensure high SEO rankings.

## 🤖 Automation Scripts

The `blogging_project` directory contains several utility scripts:
-   `update_posts.py`: Manages post metadata and content updates.
-   `deploy_blog.py`: Handles deployment workflows.
-   `global_logo_fix.py`: Ensures consistent branding across all pages.

## 🛠️ Get Shit Done (GSD) Integration

This project is integrated with [Get Shit Done (GSD)](https://github.com/gsd-build/get-shit-done), a spec-driven development system for AI agents.

### Core Workflow
GSD provides a structured workflow for building and maintaining this blog:
1.  **Initialize**: `/gsd:new-project` (Define goals and roadmap)
2.  **Discuss**: `/gsd:discuss-phase <N>` (Detailed implementation preferences)
3.  **Plan**: `/gsd:plan-phase <N>` (Research and task planning)
4.  **Execute**: `/gsd:execute-phase <N>` (AI-driven implementation)
5.  **Verify**: `/gsd:verify-work <N>` (Automated and manual verification)

### Commands
-   **Help**: `/gsd:help` (Claude Code/Gemini) or `/gsd-help` (OpenCode).
-   **Status**: `/gsd:progress` (Check milestone progress).
-   **Debugging**: `/gsd:debug` (Expert scientific debugging).

The system configs are stored in local directories: `.claude`, `.gemini`, `.opencode`, and `.codex`.

## ⚖️ Legal

Refer to `affiliate-disclosure.html` for our compliance guidelines regarding affiliate links.

---

Built with ❤️ by [TechStack Global](https://techstackglobal.github.io).
