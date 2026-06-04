# Company research

## Purpose

Turn a single competitor company name into a one-page, source-cited summary of
its financial position, recent product activity, and public positioning.

## Inputs

- A target company name (from the run prompt).
- Optionally, a focus area named in the prompt (e.g. "pricing", "AI products").

## Outputs

- One artifact per task, under the project's `company-research/` path.
- Final artifact: `format-output/write-summary/output.md`, the one-page brief.

## Stages (ordered)

1. **gather-sources**, Collect public filings and recent news on the company.
2. **summarise**, Extract the key financial and product metrics from sources.
3. **format-output**, Assemble the metrics into the one-page brief.

## Tools and integrations

- `WebSearch`, locate filings, news, and the company's public pages.
- No MCP servers are required for this workflow.

## Constraints

- Stages run strictly in order; each stage consumes the prior stage's output.
- The workflow targets exactly one company per run.
- The full artifact set must be reproducible from the cited sources alone.
