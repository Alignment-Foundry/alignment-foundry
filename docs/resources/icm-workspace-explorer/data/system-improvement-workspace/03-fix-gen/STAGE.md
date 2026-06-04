# Stage 03, Fix Generation

**One job**: For each Issue, generate a specific, testable fix proposal with full context.

**No skill needed**; this stage uses the Issue context directly.
**Input**: `02-correlate/output/issues-[run-id].md` (work top-priority first)

---

## For each issue, produce a fix proposal

Work through issues in priority order. Write each to `03-fix-gen/output/FIX-[NNN]-[slug].md`:

```markdown
# FIX-[NNN]: [Issue title]

**Issue**: ISS-[NNN]
**Run**: [run-id]
**Risk level**: low / medium / high
**Requires second reviewer**: [yes, for critical + IAM/DB/firewall changes] / no

## Root cause (from correlation)
[Copy from ISS-NNN, expand with any additional analysis]
Confidence: [XX]%

## Proposed fix

### Change 1: [title]
**File/service/config**: [exact location]

**Before**:
[exact current state, code, config, SQL, YAML, etc.]

**After**:
[exact proposed state]

**Why this fixes it**: [brief causal explanation]

### Change 2: [title] (if multiple changes needed)
[repeat format]

## Scope check
- All changes are within defined target scope: ✓ / ✗ [explain if ✗]
- No IAM, secrets, or audit log modifications: ✓ / ✗
- Production database schema unchanged: ✓ / ✗ [note if schema change needed]
- Rollback is straightforward: ✓ / ✗

## Test command
[Exact runnable command, must be copy-pasteable]
Expected output: [what a passing test looks like]

## Expected impact
[Specific metric] should improve from [current] to approximately [target].
Regression risk: [none / low / describe]

## PACE consideration
[Does this fix change any system's resilience? If yes, which PACE level needs updating?]

## Rollback plan
[Step-by-step, how to undo this if it causes problems]
Rollback effort: [< 5 min / 5–30 min / > 30 min]

## Deployment notes
[Any timing constraints, ordering requirements, or coordination needed]
```

---

## Issues that cannot be fixed in this run

If an issue requires changes outside the defined target scope, write:
`03-fix-gen/output/OUT-OF-SCOPE-[NNN].md` with:
- Why it's out of scope
- Which team or system owns the required change
- Recommended routing

---

## Done signal

Update `_state.md`. Proceed to Stage 04 for each fix proposal.
