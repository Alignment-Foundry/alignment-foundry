# Stage 06, Learn

**One job**: Close the loop. Measure outcomes. Update memory from confirmed results.
Make the next cycle smarter.

**Run when**:
- 24h after a production deployment (measure outcome)
- After a batch of rejections (update episodic memory)
- End of each week (consolidation)
- When mandate metric data is available

---

## Part A, Outcome measurement (after each deployment)

Read: `05-deploy/completed/DEPLOY-[NNN]-[date].md`
Check: The metric(s) cited in the original proposal

**Measurements to take**:
1. Did the error/anomaly described in the finding disappear?
2. Did the metric cited in the proposal improve as predicted?
3. Are there any unexpected side effects (new errors, regressions)?
4. Was the prediction in the proposal accurate (over/under/match)?

**Write outcome record to `06-learn/outcomes/OUTCOME-[NNN]-[date].md`**:

```markdown
# OUTCOME-[NNN]: [Proposal title]

**Deployment**: DEPLOY-[NNN]
**Measured**: [date, at least 24h after production deployment]
**Measured by**: [metric source]

## Prediction vs reality

| What proposal predicted | What actually happened |
|------------------------|----------------------|
| [metric] would improve by [amount] | [actual measurement] |
| [side effect] would not occur | [did it occur?] |

## Assessment
- Prediction accuracy: [accurate / over-estimated / under-estimated / wrong direction]
- Finding resolved: [fully / partially / not resolved]
- Unexpected effects: [none / describe]

## Semantic memory updates triggered

These changes should be written to `_memory/semantic/`:

- [ ] Update `architecture.md`: [specific update]
- [ ] Add to `edge-cases.md`: [new edge case discovered]
- [ ] Correct `architecture.md`: [assumption that was wrong]
- [ ] Update baseline in `02-observe/baseline/[metric].md`

## Mandate progress update

[Primary metric] moved from [before] to [after].
Net progress toward mandate: [positive / neutral / negative]
```

---

## Part B, Semantic memory updates

**Only write to semantic memory from confirmed outcomes.** Never from hypotheses.

After writing the outcome record:
1. Open the files listed in the outcome record's "semantic memory updates" section
2. Make the specific updates noted
3. Add a "confirmed by" reference: `# Confirmed by OUTCOME-[NNN] [date]`
4. Do not infer or extrapolate beyond what the outcome directly confirmed

---

## Part C, Weekly consolidation

At the end of each week, write `06-learn/weekly-summaries/week-[YYYY-WNN].md`:

```markdown
# Week [YYYY-WNN] Summary

**Period**: [start date] to [end date]

## Activity
- Findings opened: [N]  |  Resolved: [N]  |  Still open: [N]
- Proposals generated: [N]  |  Approved: [N]  |  Rejected: [N]  |  Modified: [N]
- Deployments: [N]  |  Successful: [N]  |  Rolled back: [N]

## Mandate progress
[Primary metric]: [current] → [this week's value] ([delta])
Trend: improving / flat / declining
On track to hit target by [date]: yes / no / unclear

## Patterns observed this week
[Any recurring themes, emerging issues, or signals to watch]

## What I got wrong
[Brief honest account of rejected proposals or failed predictions, and why]

## Model updates made this week
[Summary of what was written to semantic memory]

## Recommendation for next week
[Top 1–2 priorities based on what this week revealed]
```

---

## What this stage does NOT do

- Does not write to `_memory/constitutional/`, only humans write there
- Does not retroactively change a decision record
- Does not mark a finding as resolved without a measured outcome
- Does not update baseline metrics more than once per month
- Does not carry forward a failed prediction as if it succeeded
