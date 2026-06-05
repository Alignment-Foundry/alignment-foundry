# PACE Design Skill

**Load at**: Stage 04 entry
**Token budget**: ~700 tokens (this stub) | Full version: ~1,200 tokens

---

## Purpose

Design four-level resilience for critical process steps:
Primary → Alternative → Contingent → Emergency

---

## When to apply PACE

Apply to a step if ANY of these are true:
- Automation Tier 1 or 2 (new failure modes introduced)
- On the critical path
- Customer-facing or safety-critical
- External dependency present (third-party, vendor, API)
- Single point of failure with no existing backup
- Compliance requirement, must complete regardless of system state

---

## The four levels

```
PRIMARY      The default, preferred method under normal conditions.
             Optimized for performance, cost, and quality.

ALTERNATIVE  A different approach achieving the same outcome.
             Triggered when Primary is unavailable or degraded.
             Same capability level, different execution path.

CONTINGENT   A degraded-mode option.
             Achieves partial goal when Alternative also fails.
             Accepts reduced speed, accuracy, or completeness.
             Document the acceptable degradation explicitly.

EMERGENCY    Last resort. Minimum viable action.
             Must be executable WITHOUT any digital system.
             Paper, phone, manual entry, or verbal handoff only.
             Escalation path is required.
```

---

## PACE design rules

1. Each level must be **independently executable**, don't assume a higher level ran
2. **Trigger conditions must be observable**, not "if it feels slow" but "if API error rate > 5%"
3. **Emergency must be analog-safe**, no laptop, no internet, no cloud access required
4. **Recovery path required**, how does the step re-enter Primary after emergency mode?
5. **Cost escalation is acceptable**, each fallback level will cost more; that's the tradeoff
6. **Test all levels**, don't wait for a real failure to discover the emergency procedure is broken

---

## PACE block template

```markdown
### PACE: [Step name]

**Why PACE is needed**: [risk or dependency that justifies resilience design]

**PRIMARY**
- Method: [specific approach]
- Tools: [systems, APIs, platforms used]
- Normal conditions: [what "working" looks like]
- Reliability target: [availability %, SLA, or similar]

**ALTERNATIVE**
- Method: [different approach, same outcome]
- Trigger: [specific observable condition, be precise]
- Trade-off: [slower / more expensive / less accurate by how much?]

**CONTINGENT**
- Method: [partial capability approach]
- Trigger: [specific observable condition, Alternative unavailable]
- Acceptable degradation: [what the business can tolerate, be specific]
- Recovery: [how to return to PRIMARY when systems recover]

**EMERGENCY**
- Method: [analog-safe procedure, no digital tools assumed]
- Trigger: [all other levels unavailable]
- Escalation: [who to contact, what to say, what to document]
- Manual record: [what paper/physical log is maintained]
```

---

## Common PACE mistakes to avoid

- **Vague triggers** ("when it's down") → use measurable conditions
- **Emergency that needs a computer** → defeats the purpose
- **Missing recovery path** → system stays in contingent mode indefinitely
- **Identical Primary and Alternative** → if Primary fails, Alternative fails for the same reason
- **No escalation in Emergency** → urgent issues go nowhere

---

## Reference

For worked PACE examples across different process types, see:
`_core/patterns/pace-examples.md`
