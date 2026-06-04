# CLAUDE.md

> Agent entry point, **router only**. This file is read first on every run. It
> says what the repo is, detects the mode, routes to the correct skill, and
> lists the available workspaces. It carries no execution rules or constraints;
> all behaviour lives in `skills/`. This keeps `CLAUDE.md` stable.

## What this repo is

This is an **ICM Repo-as-a-Workspace**: a private GitHub repository structured
per the Interpretable Context Methodology so a Claude Code cloud agent can clone
it, execute a single task prompt, and commit an artifact to an output branch, 
with no persistent agent state required between runs. All context, intent,
constraints, and workflow logic are explicit, human-readable, and
version-controlled. See `SPEC.md` for the full contract.

## Mode detection

Read the prompt and determine the mode from its first characters:

| Condition | Mode | Then read |
|---|---|---|
| Prompt starts with `[BUILD]` at position 0 | **Build** | `skills/build.md` |
| Anything else (default) | **Run** | `skills/run.md` |

The `[BUILD]` tag must be the very first characters of the prompt. A `[BUILD]`
token anywhere else does **not** activate build mode. This is the only mode
signal; there are no environment variables or config flags for mode switching.

Read the matched skill file **in full** before taking any action.

## Workspace routing table

Used in run mode to route a prompt to its target workspace. Build mode adds a
row here whenever it creates a new workspace.

| Workspace | Purpose |
|---|---|
| `competitive-intel` | Source-cited intelligence on competitor companies, financials, product moves, and public positioning. |

`competitive-intel` ships as a sample workspace to illustrate the four-level
hierarchy. Remove it for a clean deployment.

## Repo structure map

```
/
├── CLAUDE.md          ← this file, router only
├── SPEC.md            ← canonical reference and build contract
├── README.md          ← human-facing overview
├── claude.json        ← Claude Code tool and MCP config
├── .env.example       ← env var names only, no values
├── .gitignore         ← ignores projects/**
├── skills/
│   ├── run.md         ← run mode contract
│   └── build.md       ← build mode contract
├── workspaces/        ← workspace definitions (read-only in run mode)
│   └── {workspace}/{workflow}/{workstage}/{task}/context.md
├── projects/          ← runtime output, never on main, never tracked here
│   └── {project}/{workspace}/{workflow}/{workstage}/{task}/
└── .github/
    ├── workflows/
    │   ├── dispatch.yml      ← agent dispatch + artifact commit
    │   └── guard-main.yml    ← blocks projects/ on main
    └── hooks/
        └── pre-push          ← local guard
```
