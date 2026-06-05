# Fetch 10-Q

## Instruction

Find the target company's most recent quarterly financial filing (a 10-Q, or
the nearest public equivalent for non-US companies). Record its title, the
period it covers, its publication date, and a resolvable URL. Do not download
or transcribe the full filing, only locate and reference it.

## Input format

A company name, supplied as plain text from the workflow input.

## Output format

`output.md` containing:

- `Company`, the company name as filed.
- `Filing`, the filing type and the period it covers.
- `Published`, the filing's publication date (ISO-8601).
- `Source`, a resolvable URL and the access date.

## Error handling

If no quarterly filing can be located, write `output.md` with `Filing: not
found` and a one-line explanation. Set `status` to `partial` in `metadata.json`.
