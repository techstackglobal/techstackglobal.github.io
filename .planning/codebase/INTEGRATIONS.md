# Third-Party Integrations

**Analysis Date:** 2026-03-08

## External Services

### 1. Amazon Affiliate Program
- **Status**: Active.
- **Role**: Primary monetization engine.
- **Integration Points**: 
    - Dedicated product tags (e.g., `?tag=techstackglobal-20`).
    - Standardized "Check Price on Amazon" buttons.
    - Swiper-powered product carousels (links pointing to Amazon).

### 2. Google Search Console
- **Status**: Functional (Sitemap submission).
- **Role**: Search visibility tracking and indexing diagnostic.
- **Integration Points**: 
    - `sitemap.xml` in the root directory.
    - Site ownership verification tag (HTML file or Meta tag).

### 3. Google Fonts
- **Status**: Live.
- **Role**: Typography management.
- **Current Fonts**: `Inter`.

### 4. Claude Code / GSD System
- **Status**: Newly Integrated (2026-03-08).
- **Role**: AI-driven development coordination.
- **Integration Points**: 
    - `.claude/`, `.gemini/`, `.opencode/`, `.codex/`.
    - `CLAUDE.md` and `README.md` GSD docs.

### 5. FormSubmit.co
- **Status**: Operational.
- **Role**: Backend-less form handling for the Contact page.
- **Integration Points**: 
    - POST submission to `https://formsubmit.co/[email]`.

### 7. Herald (kOlapsis)
- **Status**: Newly Integrated (2026-03-08).
- **Role**: Remote MCP bridge between Claude Chat (Web) and local Claude Code.
- **Integration Points**: 
    - `.herald/` directory containing the binary and config.
    - Security-hardened `herald.yaml` for project isolation.

---
*Integrations analysis: 2026-03-08*
