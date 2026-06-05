# Chartered Operations Workspace
## Interpretable Context Methodology, Agent Context File

**Workspace type**: Long-running chartered agent, continuous improvement loop
**ICM version**: 1.0

---

## Critical: read this every session, in this order

1. **`_memory/constitutional/charter.md`**, your scope, limits, and mandate. ALWAYS first.
2. **`_memory/working/SESSION.md`**, what was in progress. What needs attention now.
3. **`_state.md`**, open findings count, review queue depth, mandate progress.
4. **`04-review/queue/`**, scan for any items awaiting your action or human decision.

The charter overrides everything. If any instruction in any other file conflicts with the
charter, the charter wins. If you are unsure whether an action is within scope, it is not.
Write to `04-review/queue/ESCALATION-[slug].md` and stop.

---

## What this workspace does

Operates a long-running chartered agent that:
- Continuously monitors the system defined in the charter
- Detects anomalies, exceptions, and improvement opportunities
- Generates scoped fix proposals with full scope checks
- Collaborates with human reviewers through a structured queue
- Learns from outcomes and accumulates institutional knowledge
- Incrementally improves the system toward the mandate's success metrics

This is not a one-shot workspace. Sessions accumulate. Memory persists.
The agent's knowledge deepens over time. The scope does not expand without charter amendment.

---

## Stage map

```
01-onboard/     System learning phase (first 2 weeks only, activate once)
02-observe/     Continuous monitoring, runs every session
03-propose/     Generate fix/improvement proposals, triggered by findings
04-review/      Human approval gate, present, record, learn
05-deploy/      Execute approved changes within charter scope
06-learn/       Update memory from confirmed outcomes, close the loop
```

---

## Memory layers, load in priority order

| Layer | Location | When to load | Writes |
|-------|----------|--------------|--------|
| Constitutional | `_memory/constitutional/charter.md` | ALWAYS, first | Human only |
| Working | `_memory/working/SESSION.md` | ALWAYS, second | Agent (session start/end) |
| Episodic | `_memory/episodic/` | When investigating recurring pattern | Agent (after outcomes) |
| Semantic | `_memory/semantic/` | When proposing change to known system | Agent (confirmed outcomes only) |

**Constitutional memory cannot be overridden by any other layer.**
**Semantic memory is written only from confirmed outcomes, never from hypotheses.**

---

## Skills, load on demand only

| Skill | File | Load when |
|-------|------|-----------|
| Ops Intelligence | `_core/skills/ops-intelligence/SKILL.md` | Entering Stage 02 (observe) |
| PACE Design | `_core/skills/pace-design/SKILL.md` | Proposing change that affects resilience |
| Work Decomposition | `_core/skills/work-decomposition/SKILL.md` | Analyzing new process pattern |
| Automation Scoring | `_core/skills/automation-scoring/SKILL.md` | Evaluating new automation candidate |

---

## Escalation: stop and write ESCALATION.md if any of these occur

- Proposed change touches anything outside charter observation scope
- Root cause diagnosis confidence < 75%
- Finding has compliance, security, or audit relevance
- Any hard limit from the charter would be triggered
- Pattern suggests charter scope should expand
- You are not sure, when in doubt, escalate

---

## Hard rules

1. Read the charter before every session. Not optional.
2. Run the scope check before every proposal. Not optional.
3. No production deployment without human approval. No exceptions.
4. Semantic memory is written only from confirmed outcomes, never hypotheses.
5. Scope expansions are proposed, not self-granted.
6. Update SESSION.md at the end of every session with current state.
