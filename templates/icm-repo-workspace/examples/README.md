# Examples

This directory holds a **frozen illustration** of what a completed run
produces. It is not part of the live workspace and is never read by the agent.

## Why it lives here

At runtime the agent writes outputs to `/projects/` at the repo root. That path
is git-ignored on `main` and exists only on `output/*` branches (see `SPEC.md`
Part 4). To show the artifact structure without committing real `projects/`
data to `main`, a representative copy is kept here instead.

## What it shows

`projects/google-competitor-scan/` is the output of one run of the
`competitive-intel / company-research` workflow. The path mirrors the workspace
definition exactly, with `workspaces/` replaced by `projects/{project-name}/`:

```
workspaces/competitive-intel/company-research/gather-sources/fetch-10q/
→ projects/google-competitor-scan/competitive-intel/company-research/gather-sources/fetch-10q/
```

Every task directory holds exactly two files: `output.md` (or `output.json`
where structured data fits better) and `metadata.json` (the run record). The
content here is illustrative sample data, not a real competitive analysis.

This run corresponds to:

- **Prompt:** `research Google`
- **Project:** `google-competitor-scan`
- **Output branch:** `output/2026-05-17-research-google`
