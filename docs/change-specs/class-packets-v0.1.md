# Class packets and advanced formatting v0.1

Authorized 2026-10-09: implement the accepted formatting and whole-class GradeCam workflow. Baseline Studio ea5b024c62bc56a906bea17d5fb23c754f1886c9 (local tree fd6ca3c), v0.35.0-rc.1. Canonical Engine 4fb2db45c1c7ee6cfa04b369c6911bc3cf7f9081; vendored implementation a1484d714bba3790a8c228fc69b9ae7174135068, v0.33.0-rc.1. Engine stays unchanged. Target Studio v0.36.0-rc.1.

Handbook fd4330863f4cc0812180fbf1de122970a42c7885: AI-START-HERE.md, UNIVERSAL-RULES.md, CONDITIONAL-STANDARDS.md S-02/S-04, RELEASE-CHECKLIST.md. Apply version increments to each changed HTML, clear help, retained behavior, actual output verification and saved-work deletion/undo. No game controls or narrative standards apply. No main merge or hosted deployment authorized here.

## Class workflow

Drop or select Student By Standard XLSX/CSV. Detect students and Grade 5 source-code mappings locally. Preserve explicit numeric score scale selection; show ambiguities rather than guessing. Ask for default output course during import; suggest Grade 5 from recognized codes. Output course is separate from source standards. Support default, per-student and bulk overrides, including a mix of core/support/extension courses. Course order is not a difficulty score.

Use original task in its course; otherwise prefer the canonical Engine's supported directed relationships or shared focus, with stated reasons. Never auto-select a broad strand-only relation or a conflicting direction. Display reuse and unranked shared-focus cases truthfully. Keep source evidence/outcome separate from selected task identity. A missing supported match is a visible unresolved row; teacher can retain original, exclude it or explicitly select another related task. No silent omission or forced substitution.

Review student names, courses, outcomes, question counts, substitutions, gaps and cap omissions. Preview, replace/remove tasks and generate a class preview. Require explicit Approve class batch before export; changes to allocation or packet formatting revoke approval. Export entire class or selected student, plus individual documents in a ZIP, with matching student/key/study modes. Save/reopen exact task selections, provenance and layout; imported raw scores are not saved. Reopened class batches require approval again.

## Formatting

Basic controls remain title, header, instructions, footer, A4/Letter, one/two columns, work space and dividers. Advanced controls: custom/mirrored margins; column gutter and vertical divider; font family/size and paragraph/line spacing; answer blanks next to/below questions or on a separate answer sheet; distractor placement automatic/vertical/horizontal; first/subsequent and odd/even header/footer text; output-mode targeting and rules above/below; instruction placement; automatic keep-question-together plus keep-with-next. Per-question editor: space override, annotation, page/column/optional break, and a new section with columns/header/footer overrides that persist until the next section. Blank template fields inherit defaults; supported tokens include student, title, course and page.

Both Word and PDF must use actual repeating student-name headers. Word remains editable with native equations from MathML, editable tables and high-resolution diagrams. Browser and Word pagination may differ. No legacy binary authoring compatibility, free-form equation editor or arbitrary publisher-script execution is claimed. These are the approved formatting controls, not an assertion of complete legacy application parity.

## Implementation and verification

Keep Engine mathematics/mapping canonical. Add Studio-owned composition, format and targeting modules; preserve old v1 teacher sessions and prior downloads. Validate bounded layout values, source IDs, output courses and saved overrides. Do not expose student scores or adjustment labels on student pages.

Checkpoint before extended tests. Verify zero/blank/unknown imports, default course and overrides, missing-counterpart handling, broad-link rejection, review changes, stale approval blocking, session roundtrip and clear/undo. Exercise a synthetic whole-class report and six-course substitutions, student names and isolation on every page, combined and individual exports. Test formatting controls in meaningful combinations, inspect every representative Word/PDF page, and retain original core/GradeCam/concept-finder checks. Record failures and fixes honestly, and save exact hashes and handoff on a review branch.
