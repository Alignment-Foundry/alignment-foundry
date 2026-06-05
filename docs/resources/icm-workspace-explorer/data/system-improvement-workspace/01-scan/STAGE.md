# Stage 01, Scan

**One job**: Run all configured scanning agents against targets. Produce structured findings.

**Skill to load**: `_core/skills/ops-intelligence/SKILL.md` (sensing agents section)
**Read first**: `_core/agent-configs/scan-targets.md`

---

## Run order

1. Read scan targets from `_core/agent-configs/scan-targets.md`
2. For each target, run the configured agents (in parallel where possible)
3. Each agent produces one findings file in `01-scan/output/`
4. After all agents complete, write the scan summary

---

## Finding format (each agent produces one file)

Write to `01-scan/output/findings-[agent]-[run-id].md`:

```markdown
# Findings: [agent-name], [run-id]

**Target**: [target-id]
**Scan completed**: [timestamp]
**Tool versions**: [tools used]
**Coverage**: [what was and wasn't scanned, be honest about gaps]

---

## FIND-[NNN]: [Title]

**Type**: [scan type]
**Severity**: critical / high / medium / low
**Location**: [file:line / service / table / endpoint]
**Evidence**: [specific data, log line, metric value, code snippet]
**Description**: [plain language explanation]
**Estimated fix effort**: low / medium / high

---

## FIND-[NNN]: [Title]
[repeat for each finding]

---

## Scan metadata
- Total findings: [N]
- Critical: [N] | High: [N] | Medium: [N] | Low: [N]
- Scan duration: [time]
- Gaps or limitations: [anything not covered]
```

---

## Scan summary

Write `01-scan/output/scan-summary-[run-id].md`:

```markdown
# Scan Summary, [run-id]

**Started**: [timestamp] | **Completed**: [timestamp]
**Targets scanned**: [N] | **Agents run**: [N]

| Agent | Findings | Critical | High |
|-------|---------|---------|------|
| code-quality | [N] | [N] | [N] |
| security | [N] | [N] | [N] |
[... one row per agent]
| **TOTAL** | **[N]** | **[N]** | **[N]** |

**Proceed to Stage 02**: yes (findings to correlate)
```

---

## Done signal

Update `_state.md`: Stage 01 → complete.
Tell the human (or proceed autonomously to Stage 02 per workspace configuration):
> "Scan complete, [N] findings across [N] agents. Proceeding to correlation."
