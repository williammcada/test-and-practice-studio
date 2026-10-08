# Course index v0.1 verification

Tested implementation checkpoint: efa0625edd7abe050e24cb23173edbaf88aa2ebf. Baseline Studio: e24def5949f688517a697b3b48c22ac4eff43ebe. Validation ran in the local Linux/Python environment on 2026-10-08. Git blob identities for all 13 imported implementation/data/documentation files match that checkpoint.

Passed: six courses, eight language banks, 8,166 globally unique namespaced question records; catalog hashes; lesson and source-bank references; per-lesson algebra source counts; all 133 8/7 workbook scope counts; retained empty Algebra 2 scope 128; all 5,482 ExamView question-to-lesson links remain explicitly unresolved; conservative readiness; no standards prerequisite. A fresh import produced byte-identical JSON for all nine catalog/bank files.

Importer: scripts/import-course-indexes.py. Validation: tests/validate-course-indexes.py. Input identities: data/course-banks/v0.1/catalog.json. Requires Python 3 and openpyxl to reproduce from the recovery files.

Not run / outside this step: question rendering, answer verification, legacy generator execution, browser selection, exports, deployment and physical-device checks. This is a verified metadata checkpoint, not a verified application release. Step 2 remains question-content recovery.
