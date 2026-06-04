# Stage 05, Artifact Assembly

**One job**: Assemble all confirmed outputs into final, formatted deliverables ready for use.

**No new skill to load**; this stage assembles; it does not analyze.

**Input**: All previous stage `output/` folders plus `01-intake/output/artifact-selection.md`

---

## What this stage does

Stage 05 is the assembly and formatting stage. You are not generating new analysis, 
you are taking all the work produced in Stages 01–04 and assembling it into the
final artifacts the human selected at intake.

Read `01-intake/output/artifact-selection.md` first. Produce only the artifacts that were
selected. Do not produce artifacts that weren't requested.

---

## The 10 artifacts

| ID | Name | Sources | Format |
|----|------|---------|--------|
| A1 | SIPOC Summary | Stage 01 output | Markdown table |
| A2 | Decomposition Tree | Stage 02 output | Indented markdown |
| A3 | Flow Diagram | Stage 02 output | Mermaid code block |
| A4 | Automation Scorecard | Stage 03 output | Table per step |
| A5 | Technology Fit Matrix | Stage 03 output | Grouped table |
| A6 | PACE Analysis | Stage 04 output | Structured blocks |
| A7 | RACI Matrix | Stage 04 output | Table |
| A8 | Value Stream Summary | Stage 03 + 04 data | Table + metrics |
| A9 | Implementation Roadmap | Stage 03 tier summary | Phased plan |
| A10 | Process Spec Sheet | All stages | Full document |

---

## Assembly instructions per artifact

### A1, SIPOC Summary
Copy from `01-intake/output/sipoc.md`. Clean formatting only. No new content.

### A2, Decomposition Tree
Copy from `02-decompose/output/decomposition.md`. Confirm hierarchy is intact and
annotations are present. Add a legend if actor codes are used.

### A3, Flow Diagram
Copy Mermaid block from `02-decompose/output/flow-diagram.md`.
Validate that stage labels match A2 stage names exactly.
Add a plain-language description above the diagram.

### A4, Automation Scorecard
Copy from `03-analyze/output/automation-scorecard.md`.
Add a summary row at the top: total steps scored, breakdown by tier.

### A5, Technology Fit Matrix
Copy from `03-analyze/output/tech-fit-matrix.md`.
Group by technology category, not by step.
Add brief description of each technology category recommended.

### A6, PACE Analysis
Copy from `04-pace-raci/output/pace-analysis.md`.
Add a summary table at the top: step → tiers covered → key trigger.

### A7, RACI Matrix
Copy from `04-pace-raci/output/raci-matrix.md`.
Include the flags section. Add a legend for R/A/C/I.

### A8, Value Stream Summary
Synthesize from Stage 03 scoring data and Stage 02 annotations.
Estimate cycle time vs wait time per stage. Calculate process efficiency.
Flag the top 3 waste opportunities.

Template:
```markdown
| Stage | Cycle Time | Wait Time | Value-Add? | Primary Waste |
|-------|-----------|-----------|-----------|---------------|
| [name] | [est] | [est] | Yes/No/Partial | [waste type] |

**Process efficiency**: [cycle time total] / [lead time total] = [%]
**Top waste opportunities**: [1], [2], [3]
```

### A9, Implementation Roadmap
Build from `03-analyze/output/tier-summary.md`.
Organize into phases by dependency, not just priority.

Template:
```markdown
## Phase 1, Quick Wins (0–30 days)
Steps: [Tier 1 steps with no dependencies]
Technology: [specific tools]
Effort: [estimate]
Outcome: [what improves]

## Phase 2, AI Integration (30–90 days)
...

## Phase 3, Full Orchestration (90–180 days)
...

## Phase 4, Monitoring & Optimization (ongoing)
...
```

### A10, Process Spec Sheet
Use template from `_core/patterns/process-spec-sheet-template.md`.
Populate every section from previous stage outputs.
This is the formal document, clean language, consistent formatting.

---

## Output files, write to `output/`

One file per artifact produced. Name them:
`A1-sipoc.md`, `A2-decomposition.md`, `A3-flow-diagram.md`, etc.

For A10, use: `A10-process-spec-sheet.md`

---

## Human edit window

Tell the human:
> "Stage 05 complete. All requested artifacts are in `05-artifacts/output/`.
> These are your final deliverables, review them as you would any document you'd share
> with stakeholders. If anything needs revision, edit the files directly.
> If you want to activate ongoing monitoring (Stage 06), let me know.
> Otherwise, this run is complete."

Update `_state.md`: current stage → complete (or 06 if monitoring is being activated).

---

## Done checklist

- [ ] One output file per selected artifact
- [ ] A10 (if selected) fully populated from all stage outputs
- [ ] A3 Mermaid diagram syntactically valid
- [ ] A9 roadmap phases ordered by dependency (not just priority)
- [ ] All artifact names match `A[N]-[slug].md` convention
- [ ] `_state.md` updated to reflect completion
