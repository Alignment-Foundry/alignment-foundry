# Gather sources

## Purpose

Locate and record the public sources that later stages draw on: the most recent
financial filing and a set of recent, relevant news items.

## Receives

- The target company name from the workflow input.

## Produces

- `fetch-10q/output.md`, a reference to the latest quarterly filing.
- `fetch-news/output.md`, a list of recent news items with links.

## Tasks (ordered)

1. **fetch-10q**, Identify and record the company's most recent quarterly filing.
2. **fetch-news**, Collect recent news items about the company.

## Constraints

- Sources must be public and directly attributable (a resolvable URL).
- Record the access date for every source.
- If no filing is found, fetch-news still runs; the gap is recorded downstream.
