# System Improvement Workspace

ICM workspace for a multi-agent scanning and improvement pipeline.
Finds issues across 10 domains, clusters by root cause, generates validated fixes,
and maintains a human-gated path to production with a complete audit trail.

## Quick start

1. Configure `_core/agent-configs/scan-targets.md` with your system targets
2. Open a conversation with Claude pointing to this workspace
3. Say: **"Run a scan"**
4. The pipeline runs Stage 01 → 06, stopping at Stage 05 for human review

## The pipeline

```
01-scan/         → 10 agents produce structured findings
02-correlate/    → Coordinator clusters by root cause → Issues
03-fix-gen/      → Remediation agent drafts fixes with diffs
04-validate/     → Fixes applied to dev/staging, test results recorded
05-human-review/ → You review diff + test result → approve/reject
06-deploy-learn/ → Approved fixes deployed, outcomes measured, changelog updated
```

## What the human controls

- **Stage 05**: Every production deployment requires explicit approval here
- **Second reviewer**: Required for critical severity + IAM/DB schema/firewall changes
- **Scan scope**: Configured in `_core/agent-configs/scan-targets.md`, agent doesn't self-expand
- **Changelog**: Every production change is logged with your approval attribution

## What the agent handles automatically

- Running all 10 scan agents against configured targets
- Clustering 20 findings into 5 root-cause issues (typical deduplication ratio)
- Generating before/after diffs with test commands
- Applying fixes to dev and staging and reporting validation results
- Measuring 24h post-deploy outcomes
- Maintaining the cumulative system changelog

## Scan-to-fix ratio

Typical run with 10+ agents across a mid-size codebase:
- ~40–80 raw findings
- ~10–20 correlated issues (after deduplication)
- ~8–15 fix proposals generated
- ~6–12 validated in staging
- Human reviews 6–12 items (vs reading 40–80 raw findings)

The correlation stage is what makes this manageable.

## The learning loop

After each run, Stage 06 writes to `_core/patterns/scan-learnings.md`.
These learnings inform future scans without changing the skill files, 
the workspace gets smarter about your specific system over time.

---

**Created by**: Ops Intelligence System + ICM design session
**Framework**: Van Clief ICM v1.0
**Agents**: 10 domain-specialist scanning agents
