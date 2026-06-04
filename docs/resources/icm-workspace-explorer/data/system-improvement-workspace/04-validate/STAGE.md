# Stage 04, Validate

**One job**: Apply each fix to dev/staging. Run the test command. Report results.

**Input**: `03-fix-gen/output/FIX-[NNN]-[slug].md` files

---

## For each fix proposal

**Step 1, Pre-flight check**
Before applying:
- Confirm target environment is dev or staging (never production at this stage)
- Confirm test command is runnable
- Confirm rollback plan is documented in the fix proposal

**Step 2, Apply to dev**
Apply the change exactly as written in the fix proposal.
If the change involves multiple files/services, apply all of them.
Do not modify the change while applying, if something needs changing, flag it.

**Step 3, Run test command**
Run the exact test command from the fix proposal.
Record the actual output verbatim.

**Step 4, Apply to staging and monitor**
Apply to staging environment.
Monitor for the specified window (default: 30 minutes).
Record any new errors, metric changes, or unexpected behavior.

**Step 5, Write validation record**

Write `04-validate/output/VAL-[NNN]-[run-id].md`:

```markdown
# VAL-[NNN]: [Fix title]

**Fix proposal**: FIX-[NNN]
**Validated**: [timestamp]
**Environments tested**: dev / staging

## Dev validation

Applied: [timestamp]
Test command: [exact command run]
Test result: **PASS** / **FAIL**
Test output:
[verbatim output]

## Staging validation

Applied: [timestamp]
Monitor window: [duration]
Observations: [what was seen, metrics, logs, errors]
Status: **STABLE** / **ISSUES NOTED**

Issues noted (if any):
[describe any unexpected behavior]

## Validation verdict
**READY FOR REVIEW**, proceed to Stage 05
/ **NEEDS REWORK**, [describe what failed]

## Metrics before/after (if measurable)
| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| [metric] | [val] | [val] | [delta] |
```

---

## If validation fails

1. Do NOT proceed to Stage 05
2. Write validation record with NEEDS REWORK status
3. Write `04-validate/input/REWORK-[NNN].md` with:
   - What failed
   - Hypothesis for why it failed
   - Suggested revision to the fix
4. Return to Stage 03 for revision
5. Maximum 2 rework cycles, if fix still fails, escalate to human

---

## Done signal

For each READY FOR REVIEW fix: copy to `05-human-review/queue/`
Update `_state.md`: Stage 04 → complete for this run.
