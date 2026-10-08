# Create student practice and matching keys

Open `downloads/Test-and-Practice-Studio-v0.23.0-rc.6.html` in desktop Chrome or Edge. The application processes files locally and has no sign-in or automatic cloud storage.

## Build from lessons or questions

1. Select a course and turn on **Engine-ready questions only**. Add the desired questions to the manual draft. Unfinished source previews can still be inspected and saved in drafts, but cannot be put into student packets.
2. In **Packets and teacher keys**, set the title, instructions, seed, variants per task, paper size, columns, work space and optional dividers. The manual draft's Test/Practice setting supplies the purpose.
3. Choose **Build packet from manual draft**. Review **Student worksheet**, then switch to **Teacher key** to check the answers and any drawing or method criteria. **Study guide with solutions** intentionally includes answers.
4. Download the teacher session to preserve these exact questions, settings and variants. Changing controls later does not change an existing packet: rebuild to apply new settings.

Manual packets work with the available Engine-ready questions in all six English banks, without GradeCam or standards. A packet supports up to 100 questions, including repeated variants.

## Build individualized Grade 5 practice

1. Expand **GradeCam targeting**. Keep **0–1 proportions** for the supplied Student By Standard XLSX format. If a CSV contains numeric percentages such as `70`, select **0–100 percentages** before importing. Literal strings such as `70%` are unambiguous. Changing the scale requires importing again.
2. Import the XLSX sheet named **Student By Standard**, or a CSV with the report headers. Review the students and mapped standards. Only the custom Grade 5 Saxon outcomes are mapped. Unknown or other-grade codes are displayed for exclusion review; they are never guessed.
3. Select students and standards, set the threshold and number of variants, and decide whether to include missing evidence. The default targets scores **below 70%**, uses **two questions per outcome**, and caps a packet at **40 questions**. Blank/hyphen evidence is excluded by default; numeric zero is a real score. Outcomes absent from the export are not treated as weaknesses.
4. Choose **Review allocations**. Open the student summaries to see selected outcomes, repeated coverage, empty packets and exactly which outcomes the cap omits. Change the included standards, threshold, count or cap and review again if necessary. Scores remain attached to their original source outcomes; shared assessment skills do not merge student evidence.
5. Choose **Build reviewed student packets**. Students with no qualifying items are explicitly shown in the review and receive no packet. A batch supports up to 3,000 questions; choose fewer students or a lower cap for larger classes.

These aggregated percentages do not establish mastery, recency or the cause of an error. A teacher makes the targeting decision. The app does not upload assignments or configure response types in GradeCam.

## Print, PDF and Word

Select one packet or the entire batch, then choose the desired output type. **Print / Save as PDF** prints the packet preview, not the teacher interface. Match A4/Letter to the packet and disable the browser's extra headers/footers. Student pages contain no teacher answers; teacher keys and study guides do.

**Download Word document** creates an editable `.docx`. Expressions supplied by the Engine as MathML become native Word equations; ordinary prompt/answer text remains text. Diagrams become high-resolution images, and tables remain editable. Word and browser PDF use different page-flow engines, so page counts can differ while question variants and answers stay the same. Learner names continue in Word footers. Review the actual Word/printer output before classroom distribution.

One column is recommended for large diagrams. If the app reports a layout that cannot fit, reduce work space or shorten the header/instructions and rebuild. The generated packet and teacher session remain available after export errors.

## Keep and clear work

**Download teacher session** saves a private file containing learner names, selected question IDs, seeds/indices and packet settings. It can reproduce the keys, so do not give it to students. It does not include imported score tables: retain the original GradeCam export separately. Reopen a teacher session in the same Studio/Engine version; keep the versioned HTML with it. Old manual draft files remain supported separately.

Individual student/packet removal, **Clear imported class**, and **Clear all packets** have confirmation and undo controls. They identify which group is affected. Clearing imported scores does not delete generated packets; clearing packets does not remove the manual draft or downloaded files. There is no automatic browser persistence after closing.

## Verification boundary

The recorded checks used Chromium 153 on Linux, including a narrow viewport, and LibreOffice document rendering. Physical Windows Chrome/Edge, Microsoft Word and printer checks have not been performed here. No hosted deployment was made. Use the first desktop session to import your export, create a small packet, compare the key, save/reopen the teacher session, and print one page or inspect it in Microsoft Word.
