# Stage 04, Human Review

**One job**: Present proposals clearly. Record every decision. Learn from rejections.

This stage belongs primarily to the human. The agent presents, explains, answers questions,
and records decisions faithfully. The human decides.

---

## When a review session begins

Provide a queue summary:

```
Review queue: [N] items
─────────────────────────────────────
[PROP-NNN] [title], [severity], [age in days]
[PROP-NNN] [title], [severity], [age in days]
[ESCALATION-slug], [brief description]
─────────────────────────────────────
Oldest item: [age]. Recommend starting with: [highest priority].
```

For each item, be ready to:
1. Summarize the finding that triggered it (2–3 sentences)
2. Explain the proposed change in plain language
3. State confidence, risk level, and expected impact
4. Show the before/after diff if asked
5. Answer questions, including "what happens if we don't fix this?"

---

## Decision recording

For each item reviewed, write `04-review/decisions/DEC-[NNN]-[date].md` immediately:

```markdown
# DEC-[NNN]: [Proposal/escalation title]

**Decision**: APPROVED / REJECTED / MODIFIED / DEFERRED
**Decided by**: [human name / role]
**Date**: [timestamp]
**Item**: PROP-[NNN] / ESCALATION-[slug]

## If APPROVED
- Proceed to: Stage 05 (deploy)
- Deployment scope: dev → staging → production
- Any conditions: [e.g. "deploy at low-traffic time"]

## If REJECTED
- Reason: [human's reason, record verbatim if possible]
- Do not retry without new evidence

Learning note (write to episodic memory):
- What I proposed: [brief]
- Why I thought it was right: [brief]
- Why it was rejected: [reason]
- What to do differently: [adjustment]

## If MODIFIED
- Human's version: [exact modified fix, paste here]
- Proceed to Stage 05 with the modified version
- Note: human version supersedes original proposal

## If DEFERRED
- Reason: [timing / needs more data / etc.]
- Re-check condition: [date or trigger]
- Move back to queue when condition is met
```

---

## Escalation handling

For `ESCALATION-[slug].md` items:
- Read the escalation context to the human
- Do NOT propose a fix, wait for human guidance
- Record their guidance and any actions authorized
- If they authorize new scope: that goes through charter amendment, not a proposal
- Mark as resolved in the queue when handled

---

## After each session

Update `SESSION.md`:
- Remove resolved items from review queue
- Add new decisions to recently-completed
- Note any learning updates needed for episodic memory

---

## What the agent learns from rejections

Rejection is valuable training data. After recording a rejection:

1. Write a brief learning note to `_memory/episodic/[date]-rejection-PROP-[NNN].md`:
   ```markdown
   # Rejection Learning: PROP-[NNN]
   Date: [timestamp]
   Proposed: [brief description]
   Rationale I had: [why I thought this was right]
   Human's rejection reason: [verbatim reason]
   Adjustment: [what I'll do differently next time]
   Pattern: [does this suggest a general heuristic to update?]
   ```

2. These notes accumulate. Before generating future proposals in the same area,
   search `_memory/episodic/` for rejection notes; they are better guides than
   general heuristics.

---

## What the agent does NOT do at this stage

- Does not apply changes, Stage 05 does that
- Does not modify proposals after rejection to "re-submit" immediately
- Does not argue with rejections, record and learn
- Does not treat a deferred item as rejected (or vice versa)
- Does not escalate an escalation, if guidance is unclear, ask directly
