# Test and Practice Studio

A WILLIAM MCADA PRODUCT

## v0.3.0-rc.1 — manual bank review

Download [index.html](index.html) using GitHub's **Download raw file** button, then open the downloaded file in Chrome or Edge. It is a standalone teacher-review build with all 8,166 metadata records embedded; no server or internet connection is required after download. Supported test target: desktop Chromium. Physical iPad/iPhone and hosted delivery are not yet verified.

1. Choose a course/language and lesson, or search by question ID or lesson title.
2. Select individual questions or add a lesson. Selections stay when switching banks.
3. To inspect source wording, extract the retained Course-Bank-Content-Recovery-v0.2.zip and use **Load recovered content** to select its course/language JSON files. Files stay on your device and must match the pinned recovery checkpoint.
4. Reorder/remove questions, name the draft and choose Practice/Test. **Download draft** preserves the selection for **Open draft** later. The page does not persist drafts after closing.

Incomplete source previews are teacher evidence only. Equations, diagrams, formatting and dynamic variants remain unresolved. Teacher answers are separate and collapsed by default. Student output/printing and Word/PDF generation are unavailable. No standards mapping or GradeCam import is needed for manual selection; GradeCam differentiation remains Grade 5 only.

Build with `python3 scripts/build-studio.py`. Test with `npm test`; the browser test requires Playwright and a Chromium executable (see tests/studio-browser.cjs). The build includes metadata and source file hashes only, never the private recovered question bodies. Math Engine remains a separate repository and is unchanged in this increment.

- [Project brief](docs/PROJECT-BRIEF.md)
- [Current change specification](docs/change-specs/v0.3-manual-bank-review.md)
- [Recovery limitations](data/recovery/v0.2/README.md)
- [GradeCam import findings](docs/GRADECAM-IMPORT-FINDINGS.md)

Canonical repository: https://github.com/williammcada/test-and-practice-studio.
No deployment is claimed. The exact implementation checkpoint passed the [recorded teacher-review checks](docs/STUDIO-REVIEW-VERIFICATION.md). It is not a complete application release.
