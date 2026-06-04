# System Improvement Workspace
## Interpretable Context Methodology, Agent Context File

**Workspace type**: Multi-agent scanning pipeline, find, fix, validate, deploy, learn
**ICM version**: 1.0

---

## What this workspace does

Runs a coordinated pipeline of specialized scanning agents against a software system or
infrastructure target. Agents detect issues across 10 domains, a coordinator clusters
findings by root cause, a remediation agent generates fix proposals, a CI pipeline
validates them, and a human approves before production deployment.

Every run produces: correlated findings, prioritized fix proposals with diffs,
validation results, human review queue, deployment records, and an outcome-linked changelog.

---

## How to orient yourself

1. Check `_state.md`, last scan time, current queue depth, active targets.
2. Read the current STAGE.md for whichever stage needs action.
3. Load the ops-intelligence skill only for Stage 01 (sensing) and Stage 02 (correlation).
4. All other stages operate from their STAGE.md and previous stage outputs.

---

## Stage map

```
01-scan/          10 agents scan in parallel across all domains.
02-correlate/     Coordinator clusters findings by root cause.
03-fix-gen/       Remediation agent drafts specific, testable fixes.
04-validate/      CI pipeline applies fixes to dev/staging, reports results.
05-human-review/  Human reviews diff + test result + reasoning → approves/rejects.
06-deploy-learn/  Approved changes deployed. Outcomes measured. Changelog updated.
```

---

## Skills

| Skill | File | Load when |
|-------|------|-----------|
| Ops Intelligence | `_core/skills/ops-intelligence/SKILL.md` | Stages 01 and 02 |

No other skills are needed; this workspace is self-contained.

---

## Hard rules

1. No fix is ever auto-applied to production. Human review in Stage 05 is mandatory.
2. The coordinator (Stage 02) must run before fix generation (Stage 03), never skip correlation.
3. Validation (Stage 04) runs before human review (Stage 05), never ask a human to review
   an untested fix when testing is possible.
4. Never modify: IAM policies, production databases (schema), firewall rules, secrets.
   These require a second human reviewer regardless of severity.
5. Rejected fixes are logged with reasons; they are not immediately re-submitted.
6. Every production deployment has a rollback plan in the fix proposal.

---

## Scan targets

Define scan targets in `_core/agent-configs/scan-targets.md` before running Stage 01.
Each target specifies: environment, credential reference, scope, and which agents to run.

---

## Token budget

This file: ~350 tokens (always in context)
Current STAGE.md: ~350 tokens (swap per stage)
Ops Intelligence skill: ~2,000 tokens (Stages 01–02 only)
Stage input files: ~500–2,000 tokens per stage
Total typical context: ~3,000–5,000 tokens per stage
