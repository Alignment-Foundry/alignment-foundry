# Stage 03, Propose

**One job**: Generate a specific, testable, scope-checked fix proposal for a confirmed finding.

**Skill to load**: Check if PACE is needed → `_core/skills/pace-design/SKILL.md`

**Input**: `02-observe/findings/FIND-[NNN]-[slug].md` (the finding being proposed against)

---

## Before writing anything: run the scope check

Answer all four questions. If any answer is wrong, STOP and escalate.

```
SCOPE CHECK for FIND-[NNN]
─────────────────────────────────────────────────────
1. Is the affected component in my observation scope?
   Answer: YES / NO
   Evidence: [cite charter section]

2. Is this change type in my autonomous execution scope?
   (Or does it require human approval; that's still ok, just note it)
   Answer: AUTONOMOUS / REQUIRES-APPROVAL / OUT-OF-SCOPE
   Evidence: [cite charter section]

3. Would this change trigger any Hard Limit?
   Answer: YES / NO
   Evidence: [cite charter section]

4. Could this change affect any system outside my observation scope?
   Answer: YES / NO
   Evidence: [reasoning]
─────────────────────────────────────────────────────
RESULT: PROCEED / ESCALATE
```

If result is ESCALATE: write `04-review/queue/ESCALATION-[slug].md` and stop.
If result is PROCEED: continue below.

---

## Check episodic memory first

Before generating a fix, check `_memory/episodic/` for similar past situations:
- Has this finding occurred before? What was the resolution?
- Has a similar proposal been rejected? Why?

This prevents re-proposing something already tried and rejected.

---

## Proposal template

Write to `03-propose/drafts/PROP-[NNN]-[slug].md`:

```markdown
# PROP-[NNN]: [Clear, specific title]

**Finding**: FIND-[NNN]
**Created**: [timestamp]
**Scope check**: PASSED
**Risk level**: low / medium / high
**Requires approval**: no (autonomous) / yes (production)
**Similar past proposals**: [PROP-NNN was similar, resolved successfully / was rejected because X]

## Root cause
[What is causing this? Evidence-based. State confidence %.]
Confidence: [XX]%

## Proposed change

### Current state
[Exact current code, config, rule, or process, copy verbatim where possible]

### Proposed state
[Exact replacement, diff format preferred for code/config]

## Scope check (detail)
- Affected component: [name], in observation scope: ✓
- Change type: [config / code / infra / process / routing]
- Autonomous scope: [yes / requires-approval]
- Hard limits: none triggered ✓
- Adjacent system effects: [none / describe if any]

## Test command
[Exact command to verify this fix works. Must be runnable.]

## Expected impact
- Improves: [specific metric] by approximately [amount]
- Risk of regression: [none identified / describe risk]

## PACE update needed?
[YES, describe which step's PACE levels need updating and how]
[NO; this change does not affect resilience design]

## Rollback plan
[How to undo this if it causes problems. Step by step.]

## Deployment sequence
1. Apply to dev environment
2. Run test command, verify pass
3. Apply to staging, monitor 30 minutes
4. (If requires-approval) → human review and production sign-off
5. Apply to production, monitor 24 hours
6. Write outcome to Stage 06
```

---

## After writing the draft

1. Copy the file to `04-review/queue/PROP-[NNN]-[slug].md`
2. Update `SESSION.md` → add to review queue section
3. Tell the human: "PROP-[NNN] is ready for review in `04-review/queue/`. [Brief summary]"
4. **Stop. Do not proceed to Stage 04 or 05 without human action.**

---

## What you cannot do at this stage

- Do not apply any change to any environment yet
- Do not generate multiple proposals for the same finding simultaneously
- Do not propose touching out-of-scope components, escalate instead
- Do not let urgency override the scope check
