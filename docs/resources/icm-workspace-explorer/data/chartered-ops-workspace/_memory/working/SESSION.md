# Session State
## Working Memory, Overwritten at start of each session

**Session start**: [timestamp]
**Previous session**: [timestamp]
**Agent**: [agent-name]
**Consecutive sessions**: [N]

---

## What was in progress

**Active task**: [what was the agent doing at the end of last session?]
**Current stage**: [02-observe / 03-propose / 04-review / 05-deploy / 06-learn]
**Blocking on**: [human decision / more data / nothing, specify]

---

## Review queue ([N] items)

| Item ID | Type | Created | Priority | Status |
|---------|------|---------|----------|--------|
| [PROP-NNN] | fix-proposal | [date] | [critical/high/med] | awaiting-review |
| [PROP-NNN] | scope-expansion | [date] | [priority] | awaiting-review |

*Full queue: `04-review/queue/`*

---

## Active findings (observed, not yet proposed)

| ID | Title | Stage | First seen | Occurrences | Threshold |
|----|-------|-------|-----------|-------------|-----------|
| [FIND-NNN] | [brief title] | [stage] | [date] | [N] | [N needed] |

---

## Recently completed (last 7 days)

| Change | Outcome | Deployed | Notes |
|--------|---------|---------|-------|
| [ISS-NNN description] | resolved / partial / failed | [date] | |

---

## Mandate progress

**Primary metric**: [current value] / [target] ([% of goal achieved])
**Trend this week**: improving ↗ / flat → / declining ↘
**Sessions since last improvement**: [N]
**Notable this session**: [one-line summary]

---

## Episodic memory notes (patterns worth remembering this session)

[Any patterns or hypotheses formed this session, will be written to episodic/ at close]

---

## Next actions (planned for this session or next)

1. [Highest priority action]
2. [Second priority]
3. [Scheduled check, e.g. "verify outcome of PROP-008 deployment"]

---

*This file is overwritten at the start of each session.*
*Previous sessions are preserved in `_memory/episodic/week-[YYYY-WNN]-summary.md`*
