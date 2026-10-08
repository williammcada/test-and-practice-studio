# Studio v0.3.0-rc.1 — teacher review verification

Exact implementation checkpoint: 7ef0fda9524305c2eb99edf7573f1dce048c8913. All 11 locally tested implementation/specification files match the committed Git blob identities. index.html: 151,759 bytes; SHA-256 9a952414bd91385daa0cf6fb22699fd7b90d2e995053b0a3a6ef180cf79e7aae.

Environment: local Linux, Node 24, Chromium 153.0.8010.0 via Playwright. Opened the actual standalone file:// index.html; no web server or external runtime assets. Browser test uses the pinned eight recovered source JSON files held separately from git.

Passed:
- All eight banks contribute selections with no standards or GradeCam data.
- Empty Algebra 2 lesson 128 remains visible and cannot bulk-add nonexistent questions.
- Search, pagination, course/language switching preserve draft selections.
- All eight exact recovered-content files load; changed/mismatched files are rejected without discarding existing work.
- Known fixed question text, separate collapsed teacher key, key reset on another preview, missing-object markers and dynamic-template warnings.
- Draft reordering, title/purpose, JSON download/open roundtrip, unknown-ID rejection and preservation of the active draft.
- Group removal cancellation, confirmation and undo; clear-draft cancellation/confirmation; source-preview unload leaves selections intact.
- Lesson bulk-add avoids duplicates.
- Keyboard Space toggles selection and retains focus.
- Print mode exposes only the teacher-review warning, not incomplete questions/keys.
- Desktop 1440×1000 and narrow 390×844 layouts inspected; no horizontal overflow at the tested narrow width.
- No browser page errors during the workflow.
- Build regenerates byte-identically.

Commands:
```sh
npm test
CHROMIUM_EXECUTABLE_PATH=/tmp/chromium PLAYWRIGHT_MODULE=/opt/codex/runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright RECOVERY_CONTENT=/path/to/recovery/content node tests/studio-browser.cjs
python3 scripts/build-studio.py
```

Not run: physical Windows Chrome/Edge, iPad/iPhone, hosted deployment. Not implemented: faithful full math/diagram preview, dynamic generation, student-ready printing, Word/PDF, GradeCam differentiation. All recovered records remain unverified for student use. This is a verified teacher-review implementation checkpoint, not a complete application release.
