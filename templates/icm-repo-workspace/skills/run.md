---
name: run
description: Run mode contract. Activated when the prompt does not start with [BUILD]. The agent navigates the existing workspace hierarchy, executes a task, and commits an artifact to an output branch.
---

# Run mode

Run mode is the default execution mode. The agent **navigates and executes** the
existing workspace hierarchy. The hierarchy is **read-only** in run mode, never
create, edit, or delete anything under `workspaces/`, `skills/`, or the root
config files. Structural changes belong to build mode.

## What you may do

- Read any file under `workspaces/`, plus `CLAUDE.md` and `SPEC.md`.
- Write `output.md` (or `output.json`) and `metadata.json` under `projects/`.
- Create and push exactly one `output/*` branch.

## What you must not do

- Never write to `main`.
- Never modify `workspaces/`, `skills/`, `CLAUDE.md`, or any config file.
- Never skip a `context.md` at any level of the hierarchy.
- Never improvise workflow logic, the hierarchy is deterministic. Navigate it;
  do not invent stages or tasks.
- Never output, log, or commit a secret value (see `SPEC.md` Part 5).

## Execution sequence

1. Read `CLAUDE.md`, confirm run mode (no `[BUILD]` prefix).
2. Read this file in full.
3. Confirm or derive the project name (the `projects/` path prefix):
   - If the `ICM_PROJECT` environment variable is set, use it.
   - Otherwise derive a slug from the prompt and record the assumption in the
     `assumptions` field of every `metadata.json`.
4. Parse the prompt → identify the target workspace from the routing table in
   `CLAUDE.md`. If routing is ambiguous, record the assumption made.
5. Read `workspaces/{workspace}/context.md`.
6. Identify the target workflow from the prompt.
7. Read `workspaces/{workspace}/{workflow}/context.md`.
8. For each workstage, in the order listed by the workflow `context.md`:
   1. Read `{workstage}/context.md`.
   2. For each task, in the order listed by the workstage `context.md`:
      1. Read `{task}/context.md`.
      2. Execute the task instruction exactly as written.
      3. Write the artifact to the projects path (see below).
      4. Write `metadata.json` alongside the artifact.
9. Stage outputs: `git add --force projects/`.
10. Commit: `git commit -m "run: {prompt-slug}"`.
11. Push: `git push origin output/{YYYY-MM-DD}-{slug}`.
12. Exit. Retain no state.

## Output paths

Replace the `workspaces/` prefix with `projects/{project}/`; keep the rest of the
path identical. No lookup or mapping is required.

```
workspaces/{workspace}/{workflow}/{workstage}/{task}/
→ projects/{project}/{workspace}/{workflow}/{workstage}/{task}/
```

Each completed task directory contains exactly two files:

- **`output.md`** (or `output.json` where structured data fits better), the
  primary artifact. Its format is defined by the task-level `context.md`.
- **`metadata.json`**, schema below.

### metadata.json schema

```json
{
  "run_id": "<uuid>",
  "project": "<project name>",
  "workspace": "<workspace folder name>",
  "workflow": "<workflow folder name>",
  "workstage": "<workstage folder name>",
  "task": "<task folder name>",
  "prompt": "<full prompt text>",
  "timestamp": "<ISO-8601 UTC>",
  "status": "complete | partial | failed",
  "mode": "run",
  "agent": "claude-code",
  "branch": "<output branch name>",
  "assumptions": "<routing or project name assumptions, or null>",
  "error": "<error description if status is failed, or null>"
}
```

## Branch naming

`output/{YYYY-MM-DD}-{slug}`, where `{slug}` is the prompt lowercased, spaces
replaced by hyphens, truncated to 48 characters. If the dispatch workflow
supplies an explicit `output_branch`, use that value verbatim instead.

`projects/` data is never written to `main`, only to the `output/*` branch.

## Failure protocol

- If a `context.md` is missing, or a task cannot be completed: stop executing
  further tasks. Set `status` to `partial` (some tasks completed) or `failed`
  (none completed), and record the cause in the `error` field of
  `metadata.json`.
- Still write `metadata.json` for every task attempted, and still commit and
  push whatever was produced. A failed run must leave an auditable artifact.
- Never silently skip a step. A missing file is a failure to record, not a
  step to invent or work around.
