# Current candidate — v0.7.0-rc.1

16 additional quadratic tasks bring coverage to 163 implemented source-informed entries / 5,425 English records; 5,262 unintegrated. Exact real-root sets, repeated roots, radical equivalence, factoring/completing-square/formula steps and discriminant classification. [Specification](docs/change-specs/v0.7.0-quadratics.md). Implementation awaiting verification; no release or deployment. Course name, IDs and Grade 5-only differentiation remain unchanged. Historical states follow.

# Current candidate v0.6.0-rc.1

Course display: **Introduction to PreAlgebra (8/7)**. 29 additional linear-equation adaptations bring working source entries to 147 of 5,425. Fractional coefficients, decimals, brackets and variables on both sides use exact rational solutions. See docs/change-specs/v0.6.0-linear-equations.md. Checks passed; see docs/verification/v0.6.0-linear-equations.md. Prior states below are historical.

# Test and Practice Studio — v0.4.0-rc.1

A WILLIAM MCADA PRODUCT

Download index.html using GitHub's Download raw file button, then open it in Chrome or Edge. Six English course banks contain 5,425 records. Spanish has been removed from the active catalog and loader.

Select **Engine-ready questions only** to use six source-informed generator families, one per course. Their live previews need no recovered-content upload. Choose a seed, request the next variant, try an answer, or open the teacher solution. Math Engine owns these generators; Studio pins its canonical source commit in vendor/math-engine-provenance.json. These are explicitly labeled original adaptations, not exact legacy reconstructions.

The other 5,419 records retain incomplete source previews. To inspect them, extract Course-Bank-Content-Recovery-v0.2.zip and load only its English course JSON files. No files are uploaded. Historical recovery archives still contain their original sources; Spanish entries cannot be loaded into this build.

Select lessons/questions, reorder and download a draft. Version 2 drafts preserve seed and variant indices. Old English drafts migrate; Spanish selections are rejected without losing current work. There is no browser/cloud persistence; download before closing. Student-ready print, Word/PDF and GradeCam differentiation remain pending. Manual selection needs no standards codes.

Build: python3 scripts/build-studio.py. Checks: npm test, tests/studio-browser.cjs, tests/engine-integration.cjs. Desktop Chromium is the initial verification target; no hosted or physical-device verification is claimed. This is an implementation checkpoint, not a full-bank release.
