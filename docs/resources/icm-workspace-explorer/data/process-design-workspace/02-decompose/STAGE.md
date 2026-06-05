# Stage 02, Hierarchical Decomposition

**One job**: Break each SIPOC process step into a full Stage → Step → Task tree.

**Skill to load**: `_core/skills/work-decomposition/SKILL.md` → Phase 2 only.

**Input**: Read from `01-intake/output/`, use human-edited versions as-is.

---

## Read before starting

Open and read:
- `01-intake/output/sipoc.md`, the 5–7 process steps are your decomposition seeds
- `01-intake/output/scope.md`, process type and boundaries define decomposition depth
- `01-intake/output/artifact-selection.md`, determines how detailed to go

Do not re-run intake. Do not ask scope questions that Stage 01 already answered.
Do not modify anything in `01-intake/output/`.

---

## Decomposition rules

**Three levels** (go deeper only if the process type warrants it):

```
PROCESS
└── STAGE: Named phase with clear entry and exit condition
    ├── STEP: Discrete activity producing a specific output or state change
    │   ├── TASK: Atomic action, one actor, one tool, one output
    │   └── TASK: ...
    └── STEP: ...
└── STAGE: ...
```

**Definitions**:
- **Stage** = 10–60 minutes of work, or a logical handoff point. Has a named owner.
- **Step** = One activity with a clear deliverable. Actor and tool are identifiable.
- **Task** = Cannot be broken down further without losing meaning. Performed by one entity.

**Annotate every Stage and Step** with:
```
actor:          [human role / system / external / hybrid]
trigger:        [what starts this unit]
output:         [what it produces]
decision_point: [true / false, does this require human judgment?]
data_in:        [information/material consumed]
data_out:       [information/material produced]
tools:          [current tools or systems used, if known]
```

**Mark decision gateways**, points where the path branches on a condition. Use:
`⊕ DECISION: [condition] → [option A] | [option B]`

**Mark parallel tracks**, steps that can run concurrently:
`‖ PARALLEL: steps X and Y can run simultaneously`

**Mark loops**, steps that repeat until a condition is met:
`↺ LOOP: repeat until [condition]`

---

## Decomposition depth by process type

| Process type | Minimum depth | Flag for deeper if |
|-------------|--------------|-------------------|
| Operational/Transactional | 3 levels | Volume > 100/day |
| Knowledge/Decision | 3 levels + decision tree | Multiple expert roles |
| Physical/Industrial | 3 levels + safety notes | Machinery or hazards involved |
| Service/Customer-facing | 3 levels + customer journey | SLA or compliance requirement |
| Cross-functional | 3 levels + swim lanes | 3+ teams involved |

---

## Output files, write to `output/`

| File | Contents | Required |
|------|----------|----------|
| `decomposition.md` | Full indented Stage/Step/Task tree with annotations | Yes |
| `flow-diagram.md` | Mermaid flowchart (if complexity > 3 stages) | If complex |
| `decision-points.md` | List of all branch points, conditions, and options | Yes |
| `actors.md` | Full actor inventory, roles, systems, and responsibilities | Yes |
| `data-flows.md` | What data enters and exits each stage | If automation is a goal |
| `handoffs.md` | Stage-to-stage transitions: type, latency, failure mode | If efficiency is a goal |

---

## Human edit window

Tell the human:
> "Stage 02 complete. The decomposition tree is in `02-decompose/output/decomposition.md`.
> Common things to review: actor assignments, missed steps, granularity (too detailed or
> not enough), anything marked as a decision point that shouldn't be (or vice versa).
> Edit freely, your version is what Stage 03 will use. Say **proceed to stage 03** when ready."

---

## Done checklist

- [ ] `output/decomposition.md` has minimum 3 levels of hierarchy for every SIPOC step
- [ ] Every Stage and Step has: actor, trigger, output
- [ ] All decision gateways are marked with conditions and options
- [ ] `output/decision-points.md` exists (may be empty if no branches)
- [ ] `output/actors.md` exists with complete role/system list
- [ ] `_state.md` updated: Stage 02 → complete, awaiting human review
