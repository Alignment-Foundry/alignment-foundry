# Write summary

## Instruction

Render the metrics record from extract-metrics as a one-page competitor brief.
Include a one-line company descriptor, the latest revenue and growth figures,
the notable moves, and a short "what this means" paragraph. Keep every figure
attributed to its source.

## Input format

The `output.json` file from `summarise/extract-metrics/`.

## Output format

`output.md`, one page (~400 words), with these sections:

- Title, the company name.
- `Snapshot`, revenue, growth, and a one-line descriptor.
- `Recent moves`, the notable moves as a bulleted list.
- `Read`, a short interpretation paragraph.
- `Sources`, the cited URLs with access dates.

## Error handling

If the metrics record has null required fields, render the brief with those
fields marked "not available" and reflect the gap in the `Read` section. Set
`status` to `partial` in `metadata.json`.
