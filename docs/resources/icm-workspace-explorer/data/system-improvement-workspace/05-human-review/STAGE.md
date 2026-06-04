# Stage 05, Human Review

**One job**: Present validated fixes for human decision. Record every outcome. Gate production.

This is the mandatory human checkpoint. No fix reaches production without explicit approval here.

---

## Queue summary (present this when a review session opens)

```
Validated fixes ready for review: [N]
─────────────────────────────────────────────────────
[FIX-NNN] [title], [priority], validated [date], risk: [low/med/high]
[FIX-NNN] ...
─────────────────────────────────────────────────────
Suggested review order: critical → high → medium → low
Second reviewer required for: [list any critical + schema/IAM/firewall fixes]
```

---

## For each fix in the review queue, present

1. **The issue**: What problem was found? How was it detected? How many times?
2. **The fix**: What change is proposed? (plain language + diff if requested)
3. **The validation**: Did it pass dev and staging tests? Any staging anomalies?
4. **The risk**: What's the risk level? What's the rollback plan?
5. **The impact**: What should improve after deployment?

Be ready to answer:
- "What happens if we don't fix this?"
- "Why did you cluster these findings together?"
- "Walk me through the rollback"
- "Is there a simpler fix?"

---

## Decision recording

For each item, write `05-human-review/[approved|rejected]/DEC-[NNN]-[date].md`:

```markdown
# DEC-[NNN]: [Fix title]

**Decision**: APPROVED / REJECTED / MODIFIED / DEFERRED
**Decided by**: [name / role]
**Date**: [timestamp]
**Second reviewer** (if required): [name], APPROVED / REJECTED

## If APPROVED
Production deployment authorized.
Special instructions: [timing, coordination, monitoring requirements]
→ Proceed to Stage 06

## If REJECTED
Reason: [human's reason, record accurately]
Action: [close / re-investigate / reduce scope / escalate]
Do not resubmit without: [new evidence / different approach / human requests it]

## If MODIFIED
Modified fix (human's version):
[paste exact modification]
Proceed to Stage 06 with modified version.

## If DEFERRED
Reason: [timing / dependency / risk concern]
Re-evaluate when: [condition or date]
```

---

## Fixes that require two reviewers

The following always require a second human reviewer before production:
- Any finding severity: **critical**
- Any change touching: database schema, IAM policies, firewall rules, secrets management
- Any fix with rollback effort: **> 30 minutes**

Record both reviewer approvals in the decision file.

---

## After each review session

- Move approved items to `05-human-review/approved/`
- Move rejected items to `05-human-review/rejected/`
- Update `_state.md` queue counts
- Proceed to Stage 06 for all approved items
