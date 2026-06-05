# Format output

## Purpose

Assemble the extracted metrics into the final one-page competitor brief.

## Receives

- `summarise/extract-metrics/output.json`, the structured metrics record.

## Produces

- `write-summary/output.md`, the final one-page brief.

## Tasks (ordered)

1. **write-summary**, Render the metrics record as a readable one-page brief.

## Constraints

- The brief must fit one page when rendered (roughly 400 words).
- Every figure in the brief carries its source citation.
- No content may appear that is not traceable to the metrics record.
