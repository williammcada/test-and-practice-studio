# Course bank index v0.1

Metadata import for six supplied courses, eight language banks, 1,044 lesson/scope records and 8,166 question records. Language editions count separately; these totals are not counts of distinct mathematical families. Includes 52 source banks: four recovered generator courses and 48 ExamView files.

Start with catalog.json; each entry points to a course/language JSON with an integrity hash. The catalog retains source input hashes. Item IDs are namespaced by course/language and original node or bank/item identity. Empty lessons are preserved. Local grade assignment is only supplied for 8/7 (Grade 5); other course names are not converted into guessed local grades.

Metadata is available for browsing and selection integration. Question bodies, answers, executable legacy scripts and student records are not shipped. No entry is certified usable for generation. An empty standards array means no standards links imported in this catalog, not absence of the separate Grade 5 mapping. Do not gate manual bank use on standards.

Each bank carries conservative readiness shared by all its records. Later per-item promotion must require decoded prompts, math/diagrams, linked answers and relevant verification. Eight original Grade 5 engine families have separate verification; this does not promote recovered source question records.

ExamView lesson records are associated with a source bank/section only. All 5,482 ExamView item-to-lesson links remain null. Do not assign every section question to each lesson or treat question ID order as lesson evidence. Offsets retain the recovered source-index locations, not offsets into the original compressed .bnk files. English/Spanish items are separate language records; no unverified translation pairing is inferred.

Reproduce with Python 3 and openpyxl, using the original recovery inputs outside the repository:

```sh
python scripts/import-course-indexes.py --source-root /path/to/recovered-workspace --output data/course-banks/v0.1
python tests/validate-course-indexes.py
```

Source paths and hashes are listed in catalog.json. Raw publisher banks, executables and recovery archives remain outside this repository. This checkpoint does not implement the bank browser, question preview or exports.
