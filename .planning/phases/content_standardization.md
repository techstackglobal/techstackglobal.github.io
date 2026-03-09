# Phase 3.1: Content Standardization (Remove Redundant Sections)

**Objective**: Clean up all article pages by removing specific sections that are redundant or moving them to the sidebar.

## 📋 Requirements
- **REQ-CS-001**: Remove all `<section>` or `<div>` blocks with the header "The Quick Ruling" (or similar).
- **REQ-CS-002**: Remove all `<section>` or `<div>` blocks with the header "Technical Specs".
- **REQ-CS-003**: Remove all `<section>` or `<div>` blocks with the header "Comfort Verdict".
- **REQ-CS-004**: Remove all `<section>` or `<div>` blocks with the header "Final Recommendation".
- **REQ-CS-005**: Ensure that no broken HTML tags are left behind.
- **REQ-CS-006**: Verify that mobile and desktop layouts remain intact.

## 🛠️ Implementation Plan

### Wave 1: Identification & Multi-Article Audit
1. Run a `grep_search` to identify all files containing these headers.
2. List the specific HTML structures (classes/IDs) used for these sections to create a safe regex.

### Wave 2: Automated Cleanup
1. Use a Python script (leveraging `BeautifulSoup`) to identify headers and remove their parent containers.
2. Run the script on all files in `/posts/`.

### Wave 3: Verification
1. Manually check 3 representative pages:
   - A standard review (e.g., Shure SM7dB)
   - A comparison page (e.g., Sony vs AirPods)
   - A guide page (e.g., Best Headphones for Zoom)
2. Run `seo_audit.py` if available to ensure no critical SEO impact.

## 🎯 Success Criteria
- [ ] No "Quick Ruling", "Technical Specs", "Comfort Verdict", or "Final Recommendation" headers exist in any page.
- [ ] Pages still look premium and follow Glassmorphism standards.
- [ ] Zero broken links or malformed HTML.
