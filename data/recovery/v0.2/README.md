# English-only active scope — 2026-10-08

Spanish banks are removed from the active catalog, recovery overlays and content loader. Six English banks contain 5,425 records. Older counts below describe the archived extraction checkpoint and do not describe the current selection scope. Raw supplied archives and Git history remain intact.

# Bank content recovery v0.2

This metadata-only overlay accompanies the retained Course-Bank-Content-Recovery-v0.2.zip. It supplements data/course-banks/v0.1; the original checkpoint is immutable.

Apply each *-links.json by its course/language ID: add new_lessons by ID and update matching items by exact namespaced ID. Every ExamView item now has an item-record lesson link and a source answer association. Validate the base item's source-bank identity and the source hashes before applying. The four generator-course lesson links already exist in v0.1.

Recovered content covers all 8,166 indexed records. ExamView: 5,482 bounded question fields, 2,499 source choice-key associations and 2,983 separate free-response answer fields. Four generator banks: 2,684 items with question and answer/choice blocks, including 1,847 explicit answer-block records and 837 choice-only records whose correct-choice convention remains unverified. Scripts and template substitutions remain source data, not executable ports.

All 5,482 ExamView item-to-lesson links are now structurally resolved. Ten additional course/language scope labels support 74 records: one quote-bearing lesson title per Course 1 language plus two investigation subparts and two appendices per Intermediate 4 language. These were missed by the earlier restricted text scan. Existing labels remain preserved.

Equation and diagram data are retained byte-for-byte in rich blocks and source originals; 137 binary bank resources are additionally extracted from generator banks. Portable rendering remains incomplete. An attempted external PICT conversion returned an unusable black image, so it is not included or claimed as recovery. Text without an inline object marker is NOT proof that a question has no positioned diagram, superscript, table styling or other visual dependency.

All verified_for_use flags remain false. Do not show raw text fragments as complete student questions. Step 2 remains open for faithful equation/diagram rendering, legacy generator behavior and the remaining generator choice-key semantics. Source-application question/key exports would provide the comparison reference for those checks.

Reproduce after extracting the 8/7 installer with libarchive and unshield:

```sh
python scripts/recover-bank-content.py --source-root /path/to/recovered-workspace --indexes data/course-banks/v0.1 --output /path/to/private-content --metadata-output data/recovery/v0.2
python tests/validate-bank-recovery.py /path/to/private-content --indexes data/course-banks/v0.1
```

The source-root layout used by the importer is recorded in its four generator inputs and the original Step 1 source catalog. No source scripts, raw publisher banks or student data are placed in this repository. No rendering or application release is claimed.
