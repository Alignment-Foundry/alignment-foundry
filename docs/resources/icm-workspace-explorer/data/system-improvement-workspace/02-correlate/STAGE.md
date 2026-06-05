# Stage 02, Correlate

**One job**: Cluster findings by root cause. Deduplicate. Prioritize. Produce Issues.

**Skill to load**: `_core/skills/ops-intelligence/SKILL.md` (coordinator section)
**Input**: All files in `01-scan/output/`

---

## Why correlation matters

The same root cause often produces findings in multiple agents simultaneously.
A missing database index appears as:
- A performance finding (slow queries)
- A cost finding (RDS CPU spike)
- A log finding (timeout errors in the log stream)

Without correlation: 3 separate fix proposals for the same underlying problem.
With correlation: 1 issue, 1 fix, measured once.

---

## Clustering approach

For each pair of findings, assess:

1. **Structural proximity**: Same file, service, table, or endpoint?
2. **Temporal correlation**: Did they start around the same time? Same deploy?
3. **Causal relationship**: Could finding A cause finding B?
4. **Semantic similarity**: Do they describe the same underlying problem in different words?

Group findings into Issues when 2+ of these conditions are true.

---

## Issue format

Write all issues to `02-correlate/output/issues-[run-id].md`:

```markdown
# Issues, [run-id]

## ISS-[NNN]: [Descriptive title]

**Priority**: critical / high / medium / low
**Root cause**: [one-sentence root cause hypothesis]
**Confidence**: [XX]%
**Blast radius**: [N services / [N] users / [description]]

**Findings clustered**:
- FIND-[NNN] ([agent]): [brief description]
- FIND-[NNN] ([agent]): [brief description]
[list all findings that share this root cause]

**Evidence for clustering**:
[Why do these belong together? What's the connecting thread?]

**Recommended fix approach**: [brief, Stage 03 will expand]
**Fix effort**: low / medium / high
**Risk if unaddressed**: [what happens if this isn't fixed?]

---

## ISS-[NNN]: [Title]
[repeat for each issue]
```

---

## Priority scoring

Score each Issue:

```
priority_score = (severity_weight × max_severity) + (blast_weight × blast_radius_count) - (effort_weight × fix_effort)

severity weights:  critical=4, high=3, medium=2, low=1
blast_radius:      count of affected services/users
fix_effort:        high=2, medium=1, low=0 (subtract, easier fixes rank higher)
```

Sort issues by priority_score descending in the output file.

---

## Correlation summary

Write `02-correlate/output/correlation-summary-[run-id].md`:

```markdown
# Correlation Summary, [run-id]

**Findings in**: [N] (from Stage 01)
**Issues out**: [N] (after deduplication)
**Deduplication ratio**: [N findings per issue average]

**Notable clusters**:
[List the 2–3 most interesting root-cause clusters and what they reveal]

**Singletons** (findings with no cluster): [N]
[These proceed to Stage 03 individually]

**Priority queue** (top 5 by score):
1. ISS-[NNN]: [title], priority [score]
2. ...
```

---

## Done signal

Update `_state.md`: Stage 02 → complete.
Proceed to Stage 03 starting with the highest-priority issue.
