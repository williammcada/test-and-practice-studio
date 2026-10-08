# Test and Practice Studio — v0.4.0-rc.1

A WILLIAM MCADA PRODUCT

Download index.html using GitHub's Download raw file button, then open it in Chrome or Edge. Six English course banks contain 5,425 records. Spanish has been removed from the active catalog and loader.

Select **Engine-ready questions only** to use six source-informed generator families, one per course. Their live previews need no recovered-content upload. Choose a seed, request the next variant, try an answer, or open the teacher solution. Math Engine owns these generators; Studio pins its canonical source commit in vendor/math-engine-provenance.json. These are explicitly labeled original adaptations, not exact legacy reconstructions.

The other 5,419 records retain incomplete source previews. To inspect them, extract Course-Bank-Content-Recovery-v0.2.zip and load only its English course JSON files. No files are uploaded. Historical recovery archives still contain their original sources; Spanish entries cannot be loaded into this build.

Select lessons/questions, reorder and download a draft. Version 2 drafts preserve seed and variant indices. Old English drafts migrate; Spanish selections are rejected without losing current work. There is no browser/cloud persistence; download before closing. Student-ready print, Word/PDF and GradeCam differentiation remain pending. Manual selection needs no standards codes.

Build: python3 scripts/build-studio.py. Checks: npm test, tests/studio-browser.cjs, tests/engine-integration.cjs. Desktop Chromium is the initial verification target; no hosted or physical-device verification is claimed. This is an implementation checkpoint, not a full-bank release.
