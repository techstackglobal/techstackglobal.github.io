# Quality Assurance & Testing

**Analysis Date:** 2026-03-08

## Quality Philosophy
"Zero regressions on SEO or Layout."
As a static affiliate site, the most critical "tests" are for link hygiene, schema validity, and horizontal layout integrity on mobile viewport.

## Testing Protocols

### 1. Automated SEO Audit
- **Tool**: `seo_audit.py`.
- **Scope**: Scans all `posts/*.html` and root files.
- **Rules**:
  - Missing `alt` tags on images.
  - Missing `<meta description>` or `<title>`.
  - Duplicate `<h1` tags.
  - Broken internal links.
- **Reporting**: Writes audit results to `seo_audit_report.txt`.

### 2. Link Health & Affiliate Compliance
- **Tool**: `link_check.py` / `my_check_links.py`.
- **Scope**: Validates Amazon affiliate tag presence and 200 OK status.
- **Rules**:
  - Affiliate links must have `rel="nofollow sponsored"`.
  - Amazon product IDs must resolve.

### 3. Visual & Layout Regression
- **Tool**: `take_screenshots.py` / `capture_og.py`.
- **Scope**: Renders key pages at 1280px, 768px, 375px, and 320px.
- **Success Criteria**: 0 horizontal overflow pixels.
- **Manual Verification**: User check on mobile browsers to ensure "above the fold" TL;DR boxes are visible.

### 4. Form Submission Testing
- **Tool**: `test_formsubmit.py` / `test_formsubmit_live.py`.
- **Scope**: Core contact flow and newsletter signup.
- **Rules**: Validates submission to `FormSubmit.co` or similar backend.

## Continuous Verification (GSD Phase)
- **GSD Task**: `/gsd:verify-work <N>` executes specialized verification steps tailored to the specific phase.
- **Nyquist-1 Validation**: Ensures that every must-have feature has a corresponding verification step in the phase summary.

---
*Testing analysis: 2026-03-08*
*Updated with current automation suite.*
