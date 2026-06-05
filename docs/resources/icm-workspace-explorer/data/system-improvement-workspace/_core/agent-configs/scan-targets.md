# Scan Targets Configuration

**Loaded by**: Stage 01 (scan)
**Edit before each run** to set scope.

---

## Active targets

```yaml
targets:
  - id: target-001
    name: [service or repo name]
    type: [code / infra / runtime / all]
    environment: [dev / staging / production]
    credential_ref: [reference to credential store, never paste credentials here]
    agents:
      - code-quality
      - security
      - deps
    notes: [any scan-specific context]

  - id: target-002
    name: [service or repo name]
    type: runtime
    environment: production
    credential_ref: [reference]
    agents:
      - performance
      - db-health
      - log-intel
      - observability
      - api-health
      - cost
    notes: [context]
```

---

## Agent roster

| Agent | Domain | Scan types |
|-------|--------|-----------|
| `code-quality` | Code | Complexity, duplication, dead code, coverage gaps |
| `security` | Code + Infra | SAST, secrets, CVEs, IAM, OWASP |
| `deps` | Dependencies | CVE matching, licenses, outdated versions, SBOM |
| `infra-config` | Infrastructure | IaC drift, K8s misconfig, CIS benchmark |
| `performance` | Runtime | CPU hotspots, N+1 queries, memory leaks, cache |
| `db-health` | Database | Slow queries, missing indexes, bloat, locks |
| `log-intel` | Logs | New error patterns, rate spikes, PII, anomalies |
| `observability` | Monitoring | SLO/error budget, missing alerts, trace gaps |
| `api-health` | APIs | Schema drift, latency regression, breaking changes |
| `cost` | Cloud costs | Underutilized resources, waste, rightsizing |

---

## Severity definitions

| Level | Definition | Response time |
|-------|-----------|--------------|
| critical | Security breach, data loss, SLO breach imminent | Immediate |
| high | Significant performance or reliability impact | Same day |
| medium | Quality or efficiency issue | This sprint |
| low | Best practice, minor improvement | Backlog |
