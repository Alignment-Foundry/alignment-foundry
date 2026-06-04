# Stage 04, PACE Resilience & RACI

**One job**: Design PACE resilience for critical steps. Build the RACI ownership matrix.

**Skills to load**:
- `_core/skills/pace-design/SKILL.md`, for PACE analysis
- Keep `_core/skills/automation-scoring/SKILL.md` in context if needed for Tier review

**References**: `_core/patterns/pace-examples.md` (load for worked examples if needed)

**Input**:
- `02-decompose/output/decomposition.md`
- `02-decompose/output/actors.md`
- `03-analyze/output/automation-scorecard.md`
- `03-analyze/output/tier-summary.md`

---

## Part A, PACE Analysis

### Which steps need PACE?

Apply PACE to a step if it meets ANY of these criteria:

- ✅ Automation tier 1 or 2 (automation creates new failure modes)
- ✅ On the critical path (delays cascade)
- ✅ Customer-facing or safety-critical
- ✅ Has an external dependency (third-party, vendor, API outside your control)
- ✅ Single point of failure (no current backup)
- ✅ Compliance requirement, must complete regardless of system state

Skip PACE for:
- ❌ Tier 4–5 internal human steps without high risk
- ❌ Steps with natural retry/idempotency built in
- ❌ Steps explicitly marked out-of-scope

### PACE levels

```
PRIMARY      Default method under normal conditions.
             Optimized for speed, quality, cost. All systems nominal.

ALTERNATIVE  Different approach, same outcome.
             Triggered when Primary is unavailable or degraded.
             Same capability level as Primary.

CONTINGENT   Degraded-mode option.
             Triggered when Alternative also fails.
             Achieves partial goal. Accepts reduced quality/speed.

EMERGENCY    Last resort. Minimum viable action.
             Must be executable WITHOUT any digital system.
             Analog-safe. Paper/phone/manual.
```

### PACE block format

```markdown
### PACE: [Step name]

**Trigger context**: [when does this step need resilience? what's at stake if it fails?]

**PRIMARY**
- Method: [default approach]
- Tools: [systems/APIs/tools used]
- Conditions: [what "normal" looks like]
- Reliability target: [SLA or availability expectation]

**ALTERNATIVE**
- Method: [different approach, same outcome]
- Trigger: [observable condition that causes fallback, be specific]
- Degradation: [what is slower/less accurate/more expensive]

**CONTINGENT**
- Method: [partial capability, degraded mode]
- Trigger: [observable condition, Alternative also unavailable]
- Acceptable degradation: [what the business can tolerate]
- Recovery path: [how to re-enter Primary after contingent mode]

**EMERGENCY**
- Method: [analog-safe last resort, no digital dependency]
- Trigger: [observable condition, all other levels unavailable]
- Escalation: [who to contact, what to communicate]
- Documentation: [what paper/manual record is kept]
```

---

## Part B, RACI Matrix

Build a RACI matrix mapping all actors (from `02-decompose/output/actors.md`) against all Stages.

### RACI definitions

- **R** = Responsible, does the work for this stage
- **A** = Accountable, owns the outcome; single point; the buck stops here
- **C** = Consulted, provides input; two-way communication
- **I** = Informed, receives update; one-way communication

### RACI rules to enforce

- Every Stage must have exactly **one A**, flag if missing or multiple
- Every Stage must have at least **one R**, flag if missing
- Multiple Rs in a stage means coordination risk, note it
- A system can be R but not A (accountability is always human)

### RACI format

```markdown
| | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 |
|--|---------|---------|---------|---------|---------|
| [Role A] | R | I | C |, | R |
| [Role B] | A | A | A | A | A |
| [System X] | C | R | R |, | R |
| [External] | I |, | I |, | I |

**Flags**:
- Stage [N]: No A assigned → accountability gap ⚠️
- Stage [N]: Multiple Rs → coordination risk, clarify ownership
```

---

## Output files, write to `output/`

| File | Contents | Required |
|------|----------|----------|
| `pace-analysis.md` | PACE block for every flagged step | Yes (if any Tier 1–2 steps) |
| `pace-summary.md` | Table: step → PACE levels applied, key trigger conditions | Yes |
| `raci-matrix.md` | Full RACI table with flags | Yes |
| `ownership-gaps.md` | Stages with no A, multiple Rs, or unclear accountability | If gaps found |

---

## Human edit window

Tell the human:
> "Stage 04 complete. PACE analysis is in `04-pace-raci/output/pace-analysis.md` and the
> RACI is in `raci-matrix.md`. The PACE emergency levels especially benefit from your
> domain knowledge, what's the real last-resort procedure your team would follow?
> The RACI accountability column (A) is the most important to verify.
> Say **proceed to stage 05** when ready."

---

## Done checklist

- [ ] PACE block exists for every Tier 1–2 step and every critical path step
- [ ] Every PACE emergency level is analog-safe (no digital dependency)
- [ ] RACI matrix has exactly one A per Stage
- [ ] All accountability gaps flagged in `ownership-gaps.md`
- [ ] `_state.md` updated: Stage 04 → complete, awaiting human review
