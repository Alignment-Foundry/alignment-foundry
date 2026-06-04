---
name: build
description: Build mode contract. Activated when the prompt starts with [BUILD]. The agent scaffolds or edits the workspace hierarchy and commits the change to a build branch.
---

# Build mode

Build mode is activated when the prompt begins with `[BUILD]` at position 0. The
agent **scaffolds or edits** the `workspaces/` hierarchy. It does not execute
tasks and never writes to `projects/`.

## Preconditions

1. Strip the leading `[BUILD]` tag, the remainder is the build instruction.
2. Classify the operation: new workspace / new workflow / new workstage /
   new task / edit existing.
3. Check `workspaces/` for an existing structure at the target path before
   writing anything.

## What you may do

- Create or edit folders and `context.md` files under `workspaces/`.
- Add a routing-table row to `CLAUDE.md` when a new workspace is created.
- Update `README.md`, `claude.json`, and `.env.example` when the build
  instruction requires it (e.g. a workspace needs a new tool or env var).
- Write `build-metadata.json` to the repo root.

## What you must not do

- Never write to `main`.
- Never create, edit, or stage anything under `projects/` or `.github/`.
- Never run `git add .`, stage files explicitly (see the sequence below).
- Never open or merge a pull request.
- Never output, log, or commit a secret value (see `SPEC.md` Part 5).
- Never contradict a higher-level `context.md`, each level is additive and
  narrowing, never conflicting.

## context.md schemas

Every `context.md` must follow the schema for its level exactly. The headings
are fixed; fill in the content beneath them.

### Workspace-level, `workspaces/{workspace}/context.md`

```markdown
# {Workspace name}
## Purpose
## Workflows available
## What this workspace does NOT do
## Shared constraints
```

### Workflow-level, `workspaces/{workspace}/{workflow}/context.md`

```markdown
# {Workflow name}
## Purpose
## Inputs
## Outputs
## Stages (ordered)
## Tools and integrations
## Constraints
```

### Workstage-level, `workspaces/{workspace}/{workflow}/{workstage}/context.md`

```markdown
# {Workstage name}
## Purpose
## Receives
## Produces
## Tasks (ordered)
## Constraints
```

### Task-level, `workspaces/{workspace}/{workflow}/{workstage}/{task}/context.md`

```markdown
# {Task name}
## Instruction
## Input format
## Output format
## Error handling
```

## Execution sequence

1. Read `CLAUDE.md`, confirm build mode (`[BUILD]` at position 0).
2. Read this file in full.
3. Strip `[BUILD]`; parse the remaining build instruction.
4. Classify the operation and resolve the target path under `workspaces/`.
5. Check for an existing structure at that path:
   - For an **edit**, preserve content not in scope.
   - For a **create**, do not overwrite an existing folder.
6. Scaffold: create the folders and `context.md` files using the correct schema
   for each level. If creating a child below a level that does not yet exist,
   also create the intermediate levels with schema-valid `context.md` files.
7. If a new workspace was created, add a row to the routing table in
   `CLAUDE.md`.
8. Write `build-metadata.json` to the repo root (schema below).
9. Stage files explicitly, never `git add .`:
   ```
   git add workspaces/ CLAUDE.md README.md claude.json .env.example build-metadata.json
   ```
   `projects/` and `.github/` must not be staged.
10. Commit: `git commit -m "build: {description-slug}"`.
11. Push: `git push origin build/{YYYY-MM-DD}-{slug}`.
12. Exit. Do not open a PR, do not merge.

## build-metadata.json schema

```json
{
  "run_id": "<uuid>",
  "operation": "new-workspace | new-workflow | new-workstage | new-task | edit",
  "target_path": "<workspaces/ path created or edited>",
  "prompt": "<full prompt text>",
  "timestamp": "<ISO-8601 UTC>",
  "status": "complete | partial | failed",
  "mode": "build",
  "agent": "claude-code",
  "branch": "<build branch name>",
  "files_written": ["<repo-relative path>", "..."],
  "error": "<error description if status is failed, or null>"
}
```

## Branch naming

`build/{YYYY-MM-DD}-{slug}`, where `{slug}` is the build instruction lowercased,
spaces replaced by hyphens, truncated to 48 characters.

## Failure protocol

- If the build instruction is ambiguous or the target path is invalid: do not
  guess. Set `status` to `failed`, record the cause in `build-metadata.json`,
  commit it to the build branch, and exit.
- Never leave the hierarchy in a schema-invalid state. A partial scaffold must
  still have a schema-valid `context.md` at every level it touched.
- Never write to `main`, and never open a PR, leave the build branch for human
  review.
