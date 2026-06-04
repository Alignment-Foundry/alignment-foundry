# Stage 06, Ongoing Monitor & Improve

**One job**: Capture exceptions, edge cases, and real-world deviations, and propose
targeted updates to the process model.

**When to activate**: After Stage 05 is complete and the process has been running in
production for at least 2 weeks.

**This stage runs continuously**; it is never "complete." Each monitoring session is
a cycle: observe → classify → propose → human approves → update.

---

## What this stage watches for

A "finding" worth logging is any of the following:

1. **Process exception**, a step that couldn't complete as documented; required a workaround
2. **Undocumented path**, someone handled a case not covered by the current decomposition
3. **Assumption invalidated**, something the decomposition assumed turns out to be wrong
4. **Automation failure**, a Tier 1–2 step failed or required manual intervention
5. **Performance deviation**, cycle time or error rate has drifted from the A8 baseline
6. **Human feedback**, an operator notes that a step description is wrong or incomplete
7. **Scope boundary hit**, someone tries to use this process for something adjacent but out of scope

---

## Finding format

Write to `findings/FIND-[NNN]-[slug].md`:

```markdown
# FIND-[NNN]: [Brief title]

**Date**: [timestamp]
**Source**: [operator report / automation log / human feedback / observation]
**Affected stage/step**: [Stage N / Step N.N]
**Type**: exception / undocumented-path / assumption / automation-failure / performance / feedback / scope

## What happened
[Plain description, what occurred that wasn't covered by the process model?]

## Evidence
[Log lines, error messages, operator quote, metric readings]

## Impact
[How many times has this occurred? What was the consequence?]

## Hypothesis
[What change to the process model would prevent or handle this?]
[Confidence: XX%]

## Similar past findings
[Check this folder, has this pattern occurred before?]
```

---

## Threshold for proposing an update

Move a finding to a proposal when:
- Same pattern seen **3+ times** in 30 days, OR
- Single occurrence that's **critical severity**, OR
- Human explicitly requests a proposal for a specific finding

---

## Proposal format

Write to `proposals/PROP-[NNN]-[slug].md`:

```markdown
# PROP-[NNN]: Update, [what changes]

**Finding(s)**: FIND-[NNN], [FIND-NNN, ...]
**Affected artifact(s)**: [A2 / A4 / A6 / A9 / etc.]
**Change type**: new-branch / updated-rule / pace-update / actor-change / scope-note

## Proposed change

### Current (from [artifact file, line/section]):
[exact current text]

### Proposed:
[exact replacement or addition]

## Rationale
[Why this change? What evidence supports it?]

## Artifacts to update
- [ ] `05-artifacts/output/A[N]-[name].md`, [what changes]
- [ ] `02-decompose/output/decomposition.md`, [what changes] (if A2 affected)

## Risk
[low / medium / high], [brief rationale]
```

---

## Decision recording

After human reviews, write to `decisions/DEC-[NNN]-[date].md`:

```markdown
# DEC-[NNN]: [Proposal title]

**Decision**: APPROVED / REJECTED / MODIFIED / DEFERRED
**Decided by**: [name/role]
**Date**: [timestamp]

## Action taken
[What was updated, or why it wasn't]

## If rejected
Reason: [human's reason]
Learning: [what to remember for future proposals]

## Changelog entry
[One-line summary for changelog/]
```

---

## Changelog maintenance

After each approved decision, append to `changelog/process-changelog.md`:

```markdown
| [date] | v[N.N] | [A2/A4/etc.] | [one-line description of change] | [approved by] |
```

---

## Human collaboration pattern

This stage operates asynchronously. The agent:
- Logs findings as they surface (or when reported)
- Proposes updates when threshold is met
- Notifies human: "PROP-[NNN] is ready in `06-monitor/proposals/`"
- Waits for decision before updating any artifact
- Applies approved updates and records them

The human:
- Reviews proposals on their schedule
- Approves, rejects, or modifies
- Provides feedback that improves future proposals

---

## What this stage does NOT do

- Does not update artifact files without human approval
- Does not expand the process scope beyond what was originally defined
- Does not make automation changes; it proposes documentation/model updates only
- Does not modify `_core/` reference files; those are workspace-level, not process-level
