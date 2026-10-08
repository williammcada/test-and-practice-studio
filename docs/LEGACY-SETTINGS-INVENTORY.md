# Original generator settings — initial static inventory

Inspected supplied Tester.exe (2,400,256 bytes), SHA-256 700b6e53182d680f91e98b8e3a9e68d7de2573f52c32413128b9454dc3286476. The embedded version text identifies v2.13f0, 2001-01-22. The executable differs from the Tester.exe copies in the recovered algebra packages; those share SHA-256 54a2768e9736fdb12143a801278af5d1ec7a0d929aef5ca192123a35a667ff53.

Method: static Unicode string inspection, followed by exact byte-offset checks for 39 selected labels in legacy-settings-evidence.json. No executable was run. These labels establish the presence of options in the binary, not their runtime availability, dependencies, defaults, or complete behavior. This is an initial inventory, not a complete application reproduction.

| Area | Observed options | Proposed Studio treatment |
| --- | --- | --- |
| Bank browsing | Expand/collapse, details, find, selected items, random items, multiple versions | Core manual bank workflow for all courses |
| Search | Keywords, partial words, current selection/entire library, free response/multiple choice, static/dynamic | Preserve supported filters with clear empty states |
| Item variants | New values, always the same, duplicate-reference warning | Distinguish fixed questions from seeded dynamic variants; explain duplicate limits |
| Ordering | Ascending/descending/random sort; shuffle questions, answers, distractors | Separate controls; regenerate corresponding keys |
| Response format | Multiple choice and free response | Offer only when the selected item supports the format |
| Forms/output | Number of forms, first form number; question, answer, key sheets | Versioned outputs with explicit question-to-key pairing |
| Page layout | Margins, mirrored margins, column count, vertical/horizontal dividers | Include in print design and preview |
| Item layout | Question/answer spacing, answer blank placement, separate sheet/next to question, distractor placement, orphan control, instructions placement | Simplify controls while preserving mathematical readability |
| Headers/footers | Sheet targeting, odd/even pages, first/subsequent pages, whole worksheet/until section break, rules above/below | Basic controls plus advanced scope options |
| Breaks/annotations | New page, section break, optional break, annotation, keep with next | Teacher-controlled composition with preview |
| Authoring/styles | Create/clone/edit item; equation/plot insertion; text/paragraph styles | Separate authoring scope; do not assume legacy editor/script compatibility |

Final defaults, control dependencies, help text and exact authoring scope remain open. Inspect supporting help/resources and, where necessary, an observed running app to resolve them. Preserve evidence separately from design decisions. Do not copy obsolete platform implementation details into teacher controls.

Verification: all 39 recorded label byte ranges matched this exact executable. Runtime interaction, print behavior and compatibility: not run.
