# GradeCam Student By Standard — import findings

Inspected supplied Student By Standard(1).xlsx on 2026-10-08 using read-only openpyxl. Workbook was not modified. No learner names, identifiers, records or source workbook are included here.

## Observed structure
- One sheet named Student By Standard; used range 75 rows × 64 columns.
- Rows 1–5 are report preamble. Row 6 is the header row.
- A–C: Name, ID, GradeCam ID.
- D–BH: 57 custom PS.MAT.G5... standard columns, including an INV outcome.
- Rows 7–75: 69 data rows.
- Standard cells: 3,872 numeric values in [0,1], displayed with 0% formatting; 61 literal hyphens. No empty standard cells in this sample.
- A score of 0.7 means 70%, not 0.7%. Zero is an observed numeric score. Treat '-' as missing/unavailable evidence, not zero; confirm precise GradeCam semantics if targeting depends on why it is absent.
- BI is a separator; BJ onward contains a performance-band legend. These are not extra student-standard scores.

## Import implications
Detect the header and columns by names/codes, not fixed coordinates alone. Preserve identifiers as strings. Normalize numeric proportions without double-scaling. Separate missing values, invalid values and genuine zero. Reject or flag unknown outcome IDs until the custom map is loaded. Do not infer difficulty, recency, question counts or mastery from these aggregated percentages; the inspected structure does not supply that evidence.

## Next verification
Implement against synthetic fixtures with this structure, then privately compare the parser against the supplied sample. No parser has been implemented or tested yet.
