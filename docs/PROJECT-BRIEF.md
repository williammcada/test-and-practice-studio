# Current candidate — v0.11.0-rc.1

38 new statistics and probability entries bring coverage to 283 / 5,425 English records; 5,142 unintegrated. Introduction to PreAlgebra (8/7) now has 72 working entries. Exact arithmetic, explicit rounding, ordered multi-part answers and corrected card-event order. [Specification](change-specs/v0.11.0-statistics.md) · [Verification](verification/v0.11.0-statistics.md). Passed recorded checks; verified implementation only, no release/deployment. Grade 5 differentiation scope retained. Historical states follow.

# Current candidate — v0.10.0-rc.1

26 new measurement, rate and financial-arithmetic entries bring coverage to 245 / 5,425 English records; 5,180 unintegrated. Introduction to PreAlgebra (8/7) now has 60 working entries. Exact arithmetic and explicit final cent rounding. [Specification](change-specs/v0.10.0-measurement.md) · [Verification](verification/v0.10.0-measurement.md). Passed recorded checks; verified implementation only, no release/deployment. Grade 5 differentiation scope retained. Historical states follow.

# Current candidate — v0.9.0-rc.2

38 new fraction, ratio and percent entries bring coverage to 219 / 5,425 English records; 5,206 unintegrated. Introduction to PreAlgebra (8/7) now has 44 working entries. Required answer forms are enforced; recurring percentages use exact values. Passed recorded arithmetic and browser checks. [Specification](change-specs/v0.9.0-proportions.md) · [Verification](verification/v0.9.0-proportions.md). Verified implementation only; no release/deployment. Grade 5 differentiation scope retained. Historical states follow.

# Current candidate — v0.8.0-rc.1

18 new source-informed equation entries (12 affine, 6 domain-aware rational/radical) bring coverage to 181 / 5,425 English records; 5,244 unintegrated. Exact checks reject excluded denominators and extraneous roots; no-real-solution answer sets are explicit. [Specification](change-specs/v0.8.0-domain-equations.md). Passed the recorded domain-equation verification; no release/deployment. Existing course identity, IDs and Grade 5 differentiation scope retained. Historical states follow.

# Current candidate — v0.7.0-rc.1

16 additional quadratic tasks bring coverage to 163 implemented source-informed entries / 5,425 English records; 5,262 unintegrated. Exact real-root sets, repeated roots, radical equivalence, factoring/completing-square/formula steps and discriminant classification. [Specification](change-specs/v0.7.0-quadratics.md). Passed the recorded quadratic verification; no release or deployment. Course name, IDs and Grade 5-only differentiation remain unchanged. Historical states follow.

# Current candidate — v0.6.0-rc.1

Course 8/7 is now **Introduction to PreAlgebra (8/7)** with unchanged IDs and Grade 5 designation. Added 29 reviewed linear-equation adaptations: 15 Algebra 1 and 14 Algebra 1/2. 147 working entries; 5,278 remain unintegrated. Exact affine solving and MathML share the Engine implementation. Handbook fd4330863f4cc0812180fbf1de122970a42c7885. Passed the [recorded verification](verification/v0.6.0-linear-equations.md); no release or deployment. Historical entries follow.

# Current candidate — v0.5.0-rc.1

Shared exact arithmetic and MathML add 100 mapped questions (29 Course 1, 71 Intermediate 4). Total 118 adaptations; 5,307 source previews remain unintegrated. See [specification](change-specs/v0.5.0-structured-math.md). Exact pinned Engine modules include per-file hashes. Historical states follow.

# Current candidate — v0.4.1-rc.1

Eighteen source question entries support new number variants, including thirteen in 8/7. English-only catalog remains 5,425; 5,407 remain source previews. See [scope](change-specs/v0.4.1-early-87-expansion.md). Historical entries below record earlier states.

# Current candidate — v0.4.0-rc.2

Versioned English-only HTML delivery; see [change specification](change-specs/v0.4.0-rc.2-versioned-delivery.md). Handbook U-01 amendment: fd4330863f4cc0812180fbf1de122970a42c7885. Historical entries below record earlier states.

# English-only banks with live Math Engine integration — v0.4.0-rc.1

Spanish is removed from active scope and imports. Six English banks contain 5,425 source records. Six explicitly mapped source questions now generate original source-informed variants using the pinned canonical MATH-ENGINE module. Use Engine-ready questions only to find them. The other 5,419 remain source previews; full bank integration is unfinished. Seed/index save in version 2 drafts; English version 1 drafts migrate with defaults, Spanish selections reject without losing current work. See [specification](change-specs/v0.4-english-engine-integration.md). No standards prerequisite, print or export release. Handbook remains 8fc5e3b6cd163278dd618081333f2264bf392db6. Implementation checkpoint awaiting checks.

# Manual bank browser — v0.3.0-rc.1 implementation checkpoint

The exact candidate passed the [recorded desktop and standalone checks](STUDIO-REVIEW-VERIFICATION.md). Runnable standalone index.html now supports all eight course/language banks, lesson/search filters, individual and lesson selection, ordered drafts, JSON draft save/open, group removal/clear/undo, and local recovered-content inspection. See [change specification](change-specs/v0.3-manual-bank-review.md). Source previews explicitly remain incomplete; no print-ready question, variant generator or Word/PDF export is claimed. No browser/cloud persistence or deployment. Download drafts before closing. Handbook refreshed to 8fc5e3b6cd163278dd618081333f2264bf392db6.

# Bank content recovery — v0.2 implementation checkpoint

Recovered bounded source content for all 8,166 indexed records and structurally resolved all 5,482 ExamView question-to-lesson links. See [recovery scope and remaining limits](../data/recovery/v0.2/README.md) and [specification](change-specs/v0.2-bank-content-recovery.md). Source answer associations and raw rich objects are preserved; portable equation/diagram rendering, source generator behavior and 837 generator choice-only key conventions remain unverified. Step 2 is not yet fully complete. No question is promoted to verified-for-use by extraction alone.

# Course bank metadata — v0.1 implementation checkpoint

Step 1 imports six courses / eight language banks with 8,166 question records. See [catalog](../data/course-banks/v0.1/README.md) and [change specification](change-specs/v0.1-course-index-import.md). This is metadata only; question recovery, selection UI and exports remain pending. Handbook refreshed to 14ab24e3e55928a5d37e567283f0edb9172a2ce6 (AI-START-HERE, UNIVERSAL-RULES and CONDITIONAL-STANDARDS); applicable scope recorded in the specification.

# Manual banks — confirmed requirement, 2026-10-08

All supplied courses must be available as selectable banks for teacher-built tests and practice by lesson and question. Missing standards must not gate this workflow. Only standards-driven differentiation remains Grade 5 restricted. See [manual bank specification](change-specs/manual-course-banks.md) for source readiness and acceptance criteria.

# Current curriculum scope

See [Confirmed curriculum and packet scope](CURRICULUM-SCOPE.md). GradeCam-driven differentiated packets are Grade 5 only; the 331 custom outcomes belong only to that curriculum. Engine expansion includes all supplied courses. The 57 observed standards are a growing Q1 snapshot, not a fixed scope.

# Test and Practice Studio — project brief

## Identity and baseline
Owner: William McAda. Canonical repository: williammcada/test-and-practice-studio.
Initial source: README-only commit f3e41a25b006ba1a8e5670c7ffb9686d1ad00259. No application or approved change specification existed at intake on 2026-10-08.
Target: v0.1.0, design stage. Confirmed product name: Test and Practice Studio, replacing Saxon Practice Studio.

## Purpose and separation
Teacher-facing HTML application for tests, practice, individualized worksheets, keys and study guides. Consume the separately versioned Math Engine instead of duplicating generator logic. Import GradeCam Student By Standard exports to inform teacher-selected practice. Retain the custom curriculum outcome IDs; CCSS must not replace the custom Saxon 8/7 map.

## Requested workflow and features
Import → review mappings and scores → choose students/standards and item counts → preview generated work → produce student output and keys. Include seed/repeatability controls, batch class output, headers, footers, columns, dividers and contextual question-mark help for consequential options. Exact defaults and first-release feature scope remain to be finalized. Simplify the historical generator workflow rather than recreating every feature.

## Must retain and data semantics
Keep student questions and teacher keys consistent. Preserve blanks/missing evidence separately from zero. Teacher controls targeting and item allocations; a reported percentage alone is not a validated mastery diagnosis. Unknown standards require review and cannot silently map to a guessed skill. Original lesson outcomes remain source metadata even when canonical assessment skills are deduplicated.

## Devices, output and deployment
Primary teacher workflow proposed for desktop browsers; touch-friendly settings are desirable. Exact supported browser/device matrix and hosted/offline delivery remain undecided. Word/PDF output requirements and template details must be consolidated before implementation. No deployed application exists in this repository.

## Data handling
Keep uploaded student records out of source control, logs and test fixtures. Proposed default: process imports locally in the browser. Use synthetic data for repository tests. If saved work is introduced, provide U-09 individual/group/clear-all controls with confirmation and recovery guidance.

## Next prerequisites and checks
Inspect the current custom standards map, actual engine source and historical generator options. Finalize print template/output choices. Verify XLSX parsing against the observed structure using synthetic fixtures; cover zero, missing, unknown standards and non-data legend cells. Verify generated worksheet/key agreement and real export layout before any release claim.

## Handbook baseline
Consulted mcada-project-handbook v0.1.3, commit c50115ba1fea9cb552f3ad1415e670a219118b56: AI-START-HERE.md, UNIVERSAL-RULES.md, CONDITIONAL-STANDARDS.md, PROJECT-TEMPLATE.md and RELEASE-CHECKLIST.md.
U-01–U-08 are seeded guidance, not globally ratified rules. Apply relevant mathematical clarity, validation, help, versioning, retention and verification principles here. U-09 is approved and applies when saved user work exists. U-10 is not applicable to this non-game scope. Select S-02 for curriculum/assessment and S-04 for eventual distribution. S-03-M identifies the existing shared game source for investigation; its game UI requirements are not imposed on Studio. S-01 external-AI roundtrips and unrelated game/assessment restrictions are not selected.

## Release workflow
DESIGN → CHANGE SPEC → IMPLEMENT → CHECKPOINT → VERIFY → VERIFIED CHECKPOINT → RELEASE → DEPLOY.
This commit documents design only. No executable implementation, verified release or deployment is claimed. Preserve the exact source before extended testing and the exact candidate that passes. Packaging failures must recover that candidate.
