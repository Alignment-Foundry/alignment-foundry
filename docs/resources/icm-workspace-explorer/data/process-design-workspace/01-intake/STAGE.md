# Stage 01, Intake & Scoping

**One job**: Understand the process. Produce a SIPOC and a confirmed scope definition.

**Skill to load**: `_core/skills/work-decomposition/SKILL.md` → Phases 0 and 1 only.

---

## Check for pre-filled input

Look in `input/` for any of these files (human may have pre-populated them):

- `process-brief.md`, name, goal, rough description
- `stakeholders.md`, roles involved (optional)
- `constraints.md`, known limits, compliance requirements, out-of-scope items

If `input/` is empty or files are sparse, ask the human for:

1. **Process name**, what do we call this?
2. **One-sentence goal**, what should this process accomplish when working well?
3. **Rough steps**, even 5 bullet points in plain language is enough
4. **Who's involved**, human roles and systems, loosely

Do not ask for more than these four things at intake. Gather the rest through the decomposition.

---

## Your job at this stage

Run through the following in order:

**Step 1, Classify the process type**
Using the 8-category taxonomy from the skill (Operational, Knowledge, Creative, Physical,
Service, Regulatory, Strategic, Cross-functional), determine which type best fits.
If ambiguous, load `_core/skills/process-types/SKILL.md` for guidance.

**Step 2, Produce the SIPOC**
Format as a 5-column table. The "Process" column should contain 5–7 high-level steps.
These steps become the seeds for Stage 02 decomposition.

**Step 3, Confirm scope boundaries**
Define the start event (what triggers this process?) and end event (what does "done" mean?).
List what is explicitly out of scope.

**Step 4, Select artifacts**
Based on the human's goal (automation scoping vs. documentation vs. full analysis),
recommend which of the 10 artifacts to produce. See `_core/patterns/artifact-menu.md`.
Get human confirmation on the selection.

---

## Output files, write to `output/`

| File | Contents | Required |
|------|----------|----------|
| `sipoc.md` | SIPOC table with 5–7 process steps | Yes |
| `scope.md` | Start/end events, process type, in/out of scope, stakeholders | Yes |
| `artifact-selection.md` | Confirmed list of artifacts (A1–A10) to produce | Yes |
| `intake-notes.md` | Any ambiguities, assumptions made, questions for human | If needed |

---

## Human edit window

**Stop writing when output files are complete.**

Tell the human:
> "Stage 01 complete. Please review the files in `01-intake/output/` and edit anything
> that needs correcting, especially the SIPOC steps and scope boundaries. When you're
> ready, say **proceed to stage 02**."

Do not advance to Stage 02 until the human gives the proceed signal.
Their edits to output files are authoritative, use them as-is in Stage 02.

---

## Done checklist

- [ ] `output/sipoc.md` exists with 5–7 process steps in the Process column
- [ ] `output/scope.md` has start event, end event, process type, and stakeholder list
- [ ] `output/artifact-selection.md` has confirmed artifact list
- [ ] Human has been told to review and given the proceed instruction
- [ ] `_state.md` updated: Stage 01 status → complete, awaiting human review
