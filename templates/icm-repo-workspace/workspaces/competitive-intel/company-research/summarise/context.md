# Summarise

## Purpose

Extract the key financial and product metrics from the sources gathered in the
previous stage into a single structured record.

## Receives

- `gather-sources/fetch-10q/output.md`, the latest filing reference.
- `gather-sources/fetch-news/output.md`, recent news items.

## Produces

- `extract-metrics/output.json`, structured metrics with source citations.

## Tasks (ordered)

1. **extract-metrics**, Pull revenue, growth, and notable product moves into a
   structured record.

## Constraints

- Every extracted value cites the source it came from.
- A missing metric is recorded as `null` with a note, never estimated.
