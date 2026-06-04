# Stage 06, Deploy & Learn

**One job**: Deploy approved fixes to production. Measure outcomes. Update the changelog.
Close the feedback loop so the next scan is smarter.

**Input**: `05-human-review/approved/`, only approved decision files

---

## Part A, Production deployment

For each approved fix:

**Step 1, Final pre-deploy check**
- Decision file confirms APPROVED with required reviewers
- Rollback plan is present and understood
- Any special timing/coordination requirements from the decision file are met

**Step 2, Deploy**
Follow the deployment notes from the fix proposal.
Apply to production exactly as validated in staging.

**Step 3, Monitor**
Minimum monitoring window: 24 hours (or as specified in fix proposal).
Watch specifically: the metric cited in the fix's expected impact.

**Step 4, Write deployment record**

Write `06-deploy-learn/deployed/DEPLOY-[NNN]-[date].md`:

```markdown
# DEPLOY-[NNN]: [Fix title]

**Fix**: FIX-[NNN]
**Decision**: DEC-[NNN]
**Deployed**: [timestamp]
**Deployed by**: agent + [human authorization]
**Monitoring window**: [duration]

## Deployment steps taken
[Exact steps applied, verbatim where code/config]

## Initial observations (first 30 minutes)
[What was seen immediately after deployment]

## 24h outcome
[Measured 24h after deployment]
- Target metric: [metric], before: [value] → after: [value]
- New errors introduced: [none / describe]
- Unexpected behavior: [none / describe]
- Verdict: RESOLVED / PARTIAL / NOT RESOLVED / REGRESSED
```

---

## Part B, Outcome measurement and learning

After the monitoring window, write `06-deploy-learn/outcomes/OUTCOME-[NNN]-[date].md`:

```markdown
# OUTCOME-[NNN]: [Fix title]

**Based on**: DEPLOY-[NNN]
**Measured**: [date, at least 24h post-deploy]

## Did it work?

| Finding/Issue resolved | Expected | Actual | Match? |
|----------------------|---------|--------|-------|
| ISS-[NNN]: [description] | [predicted improvement] | [measured] | yes/partial/no |

## Prediction accuracy
The fix proposal predicted: [what]
What actually happened: [what]
Assessment: accurate / over-estimated / under-estimated / wrong direction

## Secondary effects
New issues introduced: [none / describe]
Adjacent improvements noticed: [none / describe]

## Agent calibration notes
[What should future scanning agents know from this outcome?]
[e.g. "The N+1 pattern in this ORM requires checking join depth, not just loop count"]
```

---

## Part C, Changelog update

Append to `06-deploy-learn/changelog/system-changelog.md`:

```markdown
| [date] | [run-id] | [ISS-NNN] | [fix title] | [verdict] | [approved by] |
```

Maintain `changelog/system-changelog.md` as the authoritative record of all changes
made by this workspace. It is the audit trail for every production modification.

---

## Part D, Feeding back to future scans

After measuring outcomes, add to `_core/patterns/scan-learnings.md`:

```markdown
## Learning from [run-id] [date]

**Finding type**: [type]
**Root cause pattern**: [description]
**Fix that worked**: [brief]
**Fix that didn't work (if applicable)**: [brief + why]
**Signal to watch earlier**: [what would have caught this sooner?]
**Scan agent calibration**: [any adjustment to thresholds or detection logic]
```

These learnings improve future scan accuracy without requiring changes to the skill files.

---

## Done signal

Update `_state.md`: Stage 06 → complete for this run.
Current stage → idle (until next scan is triggered).

Tell the human:
> "Run [run-id] complete. [N] fixes deployed. Changelog updated. 
> Summary in `06-deploy-learn/outcomes/`. Ready for next scan when you are."
