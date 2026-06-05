# Stage 01, Onboard

**One job**: Learn the system deeply before taking any action.
**Activate**: Once only, during the first 2 weeks of operation.
**After this stage**: Move permanently to Stage 02 (observe). Do not return to Stage 01.

---

## What to do during onboarding

**Week 1, Read everything available**

1. Read the charter fully (`_memory/constitutional/charter.md`)
2. Read all system documentation provided in `01-onboard/input/`
3. Read any existing process artifacts, runbooks, SOPs, architecture diagrams
4. Ask the human about: known failure modes, past incidents, things that surprise operators
5. Do not propose anything during Week 1, only observe and ask

**Week 2, Build the baseline**

1. If monitoring access is available: observe normal operation for 5–7 days
2. Record what "normal" looks like for each monitored metric
3. Write baseline readings to `02-observe/baseline/[metric-name].md`
4. Identify the 3–5 most important signals to watch
5. Write first draft of `_memory/semantic/architecture.md`

---

## Input (human provides)

Place in `01-onboard/input/`:
- System architecture documentation
- Runbooks and SOPs for the managed process
- Past incident reports (last 6 months if available)
- Known issues and workarounds currently in use
- Any previous automation or monitoring setup notes

---

## Output (write to `01-onboard/output/`)

| File | Contents |
|------|----------|
| `system-summary.md` | Your understanding of the system, confirm with human |
| `known-risks.md` | Risks and failure modes identified during onboarding |
| `monitoring-setup.md` | Which signals to watch and how (for Stage 02) |
| `onboarding-questions.md` | Anything still unclear, ask before proceeding |

---

## Completion signal

Tell the human:
> "Onboarding complete. System summary is in `01-onboard/output/system-summary.md`, 
> please review for accuracy. Once confirmed, I'll begin continuous monitoring in Stage 02.
> Any corrections or additions before I proceed?"

Do not activate Stage 02 until human confirms the system summary is accurate.
