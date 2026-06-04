# Stage 05, Deploy

**One job**: Execute approved changes in sequence. Record what was done. Signal for outcome monitoring.

**Input**: `04-review/decisions/DEC-[NNN]-[date].md` (approved decision)
**Also read**: Original `03-propose/drafts/PROP-[NNN]-[slug].md` for deployment steps

---

## Before executing anything: verify the decision

1. Confirm the decision file says APPROVED (or MODIFIED with a modified version)
2. Confirm the proposal's scope check passed
3. Confirm the deployment type (autonomous vs. production-with-approval)
   - If production-with-approval: confirm the human has explicitly authorized production
4. If anything is ambiguous, ask before proceeding

---

## Deployment sequence

Follow the sequence from the proposal exactly. Standard sequence:

```
Step 1: Dev environment
  → Apply change
  → Run test command from proposal
  → Verify: [expected result from proposal]
  → Record: pass/fail + actual output

Step 2: Staging environment
  → Apply change
  → Monitor [30–60 minutes or as specified]
  → Check: no new errors, key metrics stable
  → Record: observations

Step 3: Production (requires human approval)
  → Confirm human authorization (from decision file)
  → Apply change
  → Monitor [24 hours or as specified]
  → Record: deployment time, initial observations

→ After 24h: trigger Stage 06 (learn) for outcome measurement
```

---

## Deployment record

Write `05-deploy/completed/DEPLOY-[NNN]-[date].md` as you go:

```markdown
# DEPLOY-[NNN]: [Proposal title]

**Proposal**: PROP-[NNN]
**Decision**: DEC-[NNN]
**Started**: [timestamp]
**Deployed by**: [agent-name] (with human authorization for production)

## Dev deployment
- Applied: [timestamp]
- Test result: [PASS / FAIL]
- Test output: [actual output]

## Staging deployment
- Applied: [timestamp]
- Monitoring window: [duration]
- Observations: [what was seen]
- Status: [stable / issues noted]

## Production deployment (if applicable)
- Human authorization: confirmed, [DEC-NNN, [date]]
- Applied: [timestamp]
- Initial observations: [first 30 minutes]
- Monitoring scheduled until: [date+24h]

## Status
- [ ] Dev complete
- [ ] Staging complete
- [ ] Production complete
- [ ] Stage 06 outcome measurement scheduled for [date]
```

---

## If a deployment fails

1. Execute the rollback plan from the proposal immediately
2. Document what failed in the deployment record
3. Write `05-deploy/rollbacks/ROLLBACK-[NNN]-[date].md`:
   ```markdown
   # Rollback: PROP-[NNN]
   Date: [timestamp]
   Reason: [what happened]
   Rollback steps taken: [exact steps]
   System status after rollback: [stable / still degraded]
   Next step: [re-investigate / escalate / accept as-is]
   ```
4. Notify human immediately regardless of severity

---

## Hard limits that apply here too

- Never modify IAM, secrets, audit logs, or systems outside scope, even if the proposal
  accidentally included them (escalate instead)
- Never skip the dev → staging sequence for urgency
- Never apply to production without explicit human authorization in the decision file

---

## Triggering Stage 06

After production deployment (or staging, if production wasn't in scope):
- Note the outcome measurement date in SESSION.md
- After 24h (or specified window), run Stage 06 for this deployment
