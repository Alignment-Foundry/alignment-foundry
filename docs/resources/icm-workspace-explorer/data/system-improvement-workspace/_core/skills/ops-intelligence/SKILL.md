# Ops Intelligence Skill

**Load at**: Stages 01 and 02
**Token budget**: ~800 tokens (this stub) | Full version: ~2,000 tokens

---

## 10 Sensing Agents, Domain Coverage

| Agent | Checks | Key signals |
|-------|--------|-------------|
| `code-quality` | Complexity (>15 cyclomatic), duplication, dead code, coverage gaps | AST analysis, linter output |
| `security` | Secrets, injection, broken auth, IAM, CVEs, OWASP Top 10 | SAST results, entropy scores, CVE DB |
| `deps` | CVE matching, outdated versions, license conflicts, supply chain | SBOM, NVD/OSV, semver |
| `infra-config` | IaC drift, K8s misconfig, CIS benchmark, encryption gaps | Terraform plan, kubectl audit |
| `performance` | N+1 queries, CPU hotspots, memory leaks, cache miss rate | Profiler traces, APM data |
| `db-health` | Slow queries (P95 > 100ms), missing indexes, table bloat, locks | EXPLAIN, slow query log |
| `log-intel` | New error patterns, rate spikes vs baseline, PII in logs | Log stream, pattern matching |
| `observability` | SLO burn rate, error budget, missing alert rules, trace gaps | SLO config, metrics API |
| `api-health` | Schema drift, latency regression, breaking changes, error rates | OpenAPI diff, APM |
| `cost` | Underutilized resources (CPU < 20%), idle services, waste | Cloud cost API, utilization data |

---

## Coordinator, Correlation Heuristics

**Cluster when 2+ of these are true**:
- Same file, service, endpoint, or database table
- Started within the same deploy window (±2 hours)
- Causal relationship (A logically causes B)
- Semantic similarity in description (different agents, same symptom)

**Priority scoring**:
`score = severity_weight + blast_radius - fix_effort`
`severity: critical=4, high=3, medium=2, low=1`
`blast_radius: affected_service_count`
`fix_effort: high=-2, medium=-1, low=0`

---

## Remediation Agent, Fix Quality Standards

Every fix proposal must include:
- Exact before/after diff (not description, actual code/config)
- Runnable test command with expected output
- Rollback plan with time estimate
- Scope check result (all 4 questions answered)
- PACE note (does this affect resilience design?)

**Auto-reject conditions** (send back to fix-gen):
- No test command
- No rollback plan
- Change touches IAM, secrets, or audit logs without second reviewer flag
- Scope check not completed

---

## Severity escalation rules

If a finding is `critical`:
- Bypass normal queue, surface immediately
- Require second human reviewer before production
- Monitor post-deploy for minimum 48h (vs standard 24h)

If a finding involves secrets or credentials:
- Rotate the credential BEFORE deploying any code fix
- Document rotation in the fix proposal

---

## Reference

Full automation patterns per technology category:
`_core/patterns/automation-patterns.md`
