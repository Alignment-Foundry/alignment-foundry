# ICM Repo-as-a-Workspace

A template repository structured per the **Interpretable Context Methodology
(ICM)**: a Claude Code cloud agent clones it, executes one task prompt, and
commits an artifact to an output branch, with no persistent agent state between
runs.

> **One prompt in → one artifact branch out → container exits.**

See **[SPEC.md](./SPEC.md)** for the full, canonical contract. This README is the
quick orientation.

## How it works

The repo is a four-level hierarchy. Each level adds a narrower `context.md`:

```
workspaces/{workspace}/{workflow}/{workstage}/{task}/context.md
```

An agent reads `CLAUDE.md` first (the router), detects its mode, reads the
matching skill in `skills/`, then navigates the hierarchy top-down, loading
only the context relevant to the current depth (progressive disclosure).

## Two modes

| Mode | Trigger | Contract | What it does |
|---|---|---|---|
| **Run** | default (no `[BUILD]` prefix) | `skills/run.md` | Navigates the workspace hierarchy, executes a task, writes an artifact to `projects/` on an `output/*` branch. |
| **Build** | prompt starts with `[BUILD]` | `skills/build.md` | Scaffolds or edits the `workspaces/` hierarchy, commits to a `build/*` branch. |

The `[BUILD]` tag only activates build mode when it is the very first thing in
the prompt.

## Getting started

1. **Copy this folder** out to its own private GitHub repository.
2. Add `ANTHROPIC_API_KEY` and `GITHUB_TOKEN` to the repo's GitHub Secrets, see
   `.env.example` for the required names.
3. Install the local guard:
   ```bash
   cp .github/hooks/pre-push .git/hooks/pre-push && chmod +x .git/hooks/pre-push
   ```
4. Explore the bundled `competitive-intel` sample workspace, or create your
   own by dispatching a build prompt:
   ```
   [BUILD] add workspace {name}
   ```
5. Run a task by dispatching the **ICM dispatch** workflow (Actions tab) with a
   prompt and a project name.

## Layout

```
CLAUDE.md        router + mode detection + workspace routing table
SPEC.md          canonical reference and build contract
claude.json      Claude Code tool / MCP config
.env.example     required env var names (no values)
skills/          run.md and build.md, the mode contracts
workspaces/      workspace definitions (read-only in run mode)
projects/        runtime output, never committed to main
examples/        a frozen sample run, illustration only, not read by the agent
.github/         dispatch + guard-main workflows, pre-push hook
```

The `competitive-intel` workspace and the `examples/` directory ship as a
worked example. Delete both for a clean deployment.

## Guarantees

- **Explicit context**, everything the agent needs is a readable file in the
  repo, never held only in prompts or memory.
- **Reproducible**, the same repo state plus the same prompt produces
  equivalent output.
- **Auditable**, every run is a commit on an output branch; git history is the
  execution log.
- **Secret-safe**, no secret value ever touches a repo file, a prompt, or an
  artifact. Values live in GitHub Secrets and are injected at runtime.
