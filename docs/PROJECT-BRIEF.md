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
