# Stage 02, Observe

**One job**: Monitor the system. Detect anomalies, new patterns, and performance deviations.
Surface structured findings. This stage runs every session.

**Skill to load**: `_core/skills/ops-intelligence/SKILL.md` (sensing layer section only)

---

## Every session: run through this checklist

- [ ] **Check for new exceptions** since last session, compare against `baseline/`
- [ ] **Check performance metrics**, flag any > 15% deviation from baseline
- [ ] **Check deployment events**, any new deploys? Apply heightened monitoring for 24h
- [ ] **Update open findings**, add new occurrences to any existing `findings/FIND-NNN.md`
- [ ] **Mandate metric**, update current value in `SESSION.md`

---

## When to open a new finding

Open `findings/FIND-[NNN]-[slug].md` when:

✅ Error rate spike > 20% above 7-day rolling baseline
✅ New error pattern (not seen in past 14 days)
✅ Performance regression vs prior deploy
✅ Same anomaly confirmed by 2+ independent signals
✅ Human flags something as abnormal
✅ Mandate metric is declining week-over-week

Do NOT open a finding for:
❌ Single-occurrence errors with no pattern
❌ Expected traffic during known events
❌ Planned maintenance windows
❌ Anything outside observation scope → write ESCALATION.md instead

---

## Finding template

```markdown
# FIND-[NNN]: [Brief descriptive title]

**Detected**: [timestamp]
**Stage/step affected**: [Stage N / Step N.N, in the managed process]
**Severity**: critical / high / medium / low
**Status**: new / investigating / ready-to-propose / proposed / resolved
**Occurrences**: [N] in [window]

## Signal
[What metric, log, or event triggered this? Specific numbers.]

## Pattern
[What pattern do I observe? Frequency, window, conditions.]

## Hypothesis
[What do I believe is causing this?]
Confidence: [XX]%

## Evidence
[Specific log lines, metric values, exception IDs]

## Similar past findings
[Search episodic/. Has this pattern occurred before?]
[If yes: link to previous finding and its resolution]
```

---

## Proposal threshold

Move a finding to Stage 03 when:
- Same pattern: **3+ occurrences in 7 days**
- Severity critical: **single occurrence is enough**
- Human requests: **immediately**

Write `02-observe/anomalies/READY-[FIND-NNN].md` containing just:
`"Ready to propose fix for FIND-[NNN], [one-line summary]"`
Then proceed to Stage 03 for that finding.

---

## Baseline files

Format for `02-observe/baseline/[metric-name].md`:

```markdown
# Baseline: [metric name]

**Established**: [date]
**Source**: [where this data comes from]
**Sample window**: [how many days/events]

| Percentile | Value | Notes |
|-----------|-------|-------|
| P50 | [value] | |
| P95 | [value] | |
| P99 | [value] | |

**Anomaly threshold**: [value or % deviation that triggers a finding]
**Last updated**: [date]
```

Do not update baseline during an active incident; that normalizes the anomaly.
Update baseline monthly during stable operation.
