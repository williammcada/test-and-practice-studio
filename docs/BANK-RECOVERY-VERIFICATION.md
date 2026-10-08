# Bank recovery v0.2 — verification record

Exact tested implementation checkpoint: 4d689c99313e27f1737139043691a5f404c9ced9. All nine implementation, metadata and scope files have Git blob identities matching the locally tested files. Linux/Python validation on 2026-10-08.

Passed:
- All 8,166 indexed identities accounted for without duplicate namespace IDs.
- 16,911 generator blocks and 171 resources (137 binary) compared byte-for-byte with original banks; all source hashes match.
- All 5,482 ExamView source lesson associations resolve, including 74 records requiring ten additional course/language labels.
- All 2,499 ExamView choice keys point to displayed labels; all 2,983 free-response fields match their source text.
- Nine independently checked fixed Course 1 examples match recovered answers (equation, distance/length units, square perimeter, sequence, odd number, sum, change and dozen count).
- Regenerating all content and link-overlay JSON gives byte-identical files.
- ZIP CRC and all 60 payload file hashes match the manifest.

Retained package: Course-Bank-Content-Recovery-v0.2.zip, 10,222,633 bytes, SHA-256 f64a35dc9197da639ca28d354f299812cb9d7f6ebcb64134a73c33b2c52682b5.

Unresolved:
- Faithful equation/diagram and rich-style rendering; plain text is not a full visual reconstruction.
- Legacy dynamic scripts, variant behavior and font-specific symbols.
- Correct-choice conventions for 837 generator choice-only records; choices are preserved but not certified.
- Full mathematical audit, source-app print comparison and browser/export integration.

The legacy image conversion experiment produced an unusable image and is not shipped. No failed rendering is promoted to usable content. Source-app question/key exports remain useful comparison evidence.

This is verified extraction integrity at a preserved checkpoint, not completion of Step 2 or an application release. All recovered records remain unverified for generation. Original files and raw blocks are retained so later decoding does not require re-extraction.
