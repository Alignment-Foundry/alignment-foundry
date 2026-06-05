# SPEC.md
# ICM Repo-as-a-Workspace

**Version:** 1.0.0  
**Status:** Active, canonical reference and agent build contract  

---

## Part 1, Core Concepts

### Interpretable Context Methodology (ICM)

ICM is a design philosophy for structuring AI agent workspaces so that all context, intent, constraints, and workflow logic are **explicit, human-readable, and version-controlled**, never implicit in model memory, chat history, or runtime state.

**Core principle: the workspace must be fully interpretable without the agent that created it.**

ICM has four properties:

1. **Explicit context**, Everything the agent needs to execute a task lives in the repo as a readable file. No context is passed only through prompts or held only in memory.
2. **Defined scope**, Each workspace has a narrow, declared purpose. Narrow scope makes agent behavior predictable and auditable.
3. **Reproducible execution**, Given the same repo state and the same prompt, two independent runs produce equivalent outputs. Workflow logic is deterministic; the agent navigates it, not improvises it.
4. **Auditable history**, Every run produces a committed artifact on an output branch. Git history is the execution log.

ICM is not a framework or a library. It is a set of folder conventions, file contracts, and routing rules that this repo encodes structurally.

---

### Repo-as-a-Workspace

A **Repo-as-a-Workspace** is a private GitHub repository structured according to ICM conventions so that it can be cloned by a Claude Code cloud agent, executed against a single task prompt, and produce a committed artifact, with no persistent agent state required between runs.

The repository serves four roles simultaneously:

- **Workflow definition**, folder hierarchy and `context.md` files define what the agent does and in what order
- **Context layer**, `CLAUDE.md` and `context.md` files provide grounding at every level of the hierarchy
- **Secrets interface**, environment variable names are declared in `.env.example`; values are injected at runtime by GitHub Actions, never stored in the repo
- **Artifact store**, outputs are committed to named `output/*` branches, never to `main`

**The execution contract is always:** one prompt in → one artifact branch out → container exits.

---

## Part 2, Folder Hierarchy

The workspace is organised as a four-level hierarchy under a single root. Each level has a defined scope and a `context.md` that narrows the agent's instructions progressively as it descends.

```
/
└── workspaces/
    └── {workspace}/           ← specific domain area
        └── {workflow}/        ← defined process within the area
            └── {workstage}/   ← a single step within the workflow
                └── {task}/    ← atomic unit of work
```

### Level definitions

| Level | Scope | Example |
|---|---|---|
| **Workspace** | A specific domain or functional area | `competitive-intel`, `content`, `outreach` |
| **Workflow** | A defined, repeatable process within that area | `company-research`, `draft-post`, `prospect-list` |
| **Workstage** | One step within the workflow | `gather-sources`, `summarise`, `format-output` |
| **Task** | A single atomic action | `fetch-10q`, `extract-metrics`, `write-summary` |

### Progressive disclosure

The agent reads context top-down, accumulating scope as it descends:

```
CLAUDE.md                  → global routing rules, what the repo is, how to navigate
workspaces/
  context.md               → what this workspace covers, what it does not
  {workflow}/
    context.md             → inputs, outputs, and rules for this workflow
    {workstage}/
      context.md           → what this stage does, what it receives, what it produces
      {task}/
        context.md         → exact instructions for this atomic task
```

Each `context.md` is **additive and narrowing**; it adds specificity without contradicting the level above. The agent loads only the context relevant to the depth of the current task. It never loads the full tree upfront.

---

## Part 3, Routing, Skills, and Context Files

### CLAUDE.md (root)

`CLAUDE.md` is the agent's entry point and **router only**. It is the first file read on every run. It must contain:

1. **What this repo is**, one paragraph describing the repo's purpose
2. **Mode detection**, logic for routing to the correct skill based on the prompt prefix
3. **Workspace routing table**, list of available workspaces with one-line descriptions (used in run mode)
4. **Repo structure map**, the folder layout for orientation

`CLAUDE.md` carries no behavioural rules or constraints itself. All execution logic lives in the skill files. This keeps `CLAUDE.md` stable; it rarely needs to change, even as skills and workspaces evolve.

### Skills

Skill files live in `skills/` and contain the complete execution contract for each mode. The agent reads the relevant skill immediately after `CLAUDE.md` and before taking any action.

| File | Mode | Triggered when |
|---|---|---|
| `skills/run.md` | Run mode | Prompt does not start with `[BUILD]` (default) |
| `skills/build.md` | Build mode | Prompt starts with `[BUILD]` |

Each skill file has YAML frontmatter (`name`, `description`) followed by the full instruction set for that mode. Skills are the authoritative source for:
- What the agent may and must not do
- The execution sequence
- Output paths and artifact formats
- Failure protocol
- Branch naming conventions

### Mode detection

The `[BUILD]` tag must appear at the very start of the prompt to activate build mode. Any other position defaults to run mode. This is the only mode signal; there are no environment variables or config flags for mode switching.

| Prompt | Mode |
|---|---|
| `[BUILD] add workspace competitive-intel` | Build |
| `research Google competitors` | Run |
| `tell me about [BUILD] mode` | Run (tag not at position 0) |

### context.md schema by level

`context.md` files are the scoped instruction sets for the workspace hierarchy. They are read in run mode during task execution, and written in build mode during scaffolding. Each level has a fixed schema enforced by `skills/build.md`.

**Workspace-level:**
```markdown
# {Workspace name}
## Purpose
## Workflows available
## What this workspace does NOT do
## Shared constraints
```

**Workflow-level:**
```markdown
# {Workflow name}
## Purpose
## Inputs
## Outputs
## Stages (ordered)
## Tools and integrations
## Constraints
```

**Workstage-level:**
```markdown
# {Workstage name}
## Purpose
## Receives
## Produces
## Tasks (ordered)
## Constraints
```

**Task-level:**
```markdown
# {Task name}
## Instruction
## Input format
## Output format
## Error handling
```

---

## Part 4, Projects Tree and Output Paths

### Structure

Runtime outputs are written to a `projects/` tree. The `workspaces/` segment is **replaced** by `projects/{project-name}/`, the rest of the path is preserved exactly:

```
projects/
└── {project-name}/
    └── {workspace}/
        └── {workflow}/
            └── {workstage}/
                └── {task}/
                    ├── output.md
                    └── metadata.json
```

### Path convention

The `workspaces/` prefix is **replaced** by `projects/{project-name}/`. Everything below it is identical:

```
# Workspace definition path
workspaces/{workspace}/{workflow}/{workstage}/{task}/

# Corresponding output path
projects/{project-name}/{workspace}/{workflow}/{workstage}/{task}/
```

Any output can be located deterministically by substituting `workspaces/` with `projects/{project-name}/` in the workspace path. No lookup or mapping required.

### Artifact files

Every completed task directory contains exactly two files:

**`output.md`** (or `output.json` where structured data is more appropriate)  
The primary artifact. Format is defined by the task-level `context.md`.

**`metadata.json`**
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

### Branch isolation

`projects/` data is **never written to `main`**. It exists only on `output/*` branches. Three enforcement layers:

**Layer 1, GitHub Actions guard** (`.github/workflows/guard-main.yml`):
```yaml
on:
  push:
    branches: [main]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 2
      - name: Block projects/ on main
        run: |
          if git diff --name-only HEAD~1 HEAD | grep -q '^projects/'; then
            echo "ERROR: projects/ data must never be committed to main."
            exit 1
          fi
```

**Layer 2, pre-push hook** (installed to `.git/hooks/pre-push`):
```bash
#!/usr/bin/env bash
branch=$(git symbolic-ref HEAD 2>/dev/null | sed 's|refs/heads/||')
if [ "$branch" = "main" ]; then
  if git diff --cached --name-only | grep -q '^projects/'; then
    echo "ICM: projects/ data cannot be pushed to main. Use an output branch."
    exit 1
  fi
fi
```

**Layer 3, `.gitignore`:**
```
# Runtime output, never committed to main
projects/**
```

The agent uses `git add --force projects/` only when on an output branch. An accidental `git add .` from main cannot stage project data.

---

## Part 5, Secret Management

No secret value ever touches a repo file, a prompt, or an artifact.

| Tier | Location | Role |
|---|---|---|
| 1, Source of truth | GitHub Secrets (repo or org scoped) | Where values are stored |
| 2, Injection | GitHub Actions `env:` block in workflow YAML | Where values enter the container |
| 3, Consumption | `os.environ` in scripts | Where scripts read values |

### `.env.example`

Declares required variable names with no values:
```
ANTHROPIC_API_KEY=
GITHUB_TOKEN=
```

Workspace-specific variables are added below the base set. The GitHub Actions dispatch workflow generates its `env:` block from this file.

### MCP auth pattern

MCP server configs reference environment variable names, never values:
```json
{
  "mcpServers": {
    "example": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-example"],
      "env": {
        "API_KEY": "${EXAMPLE_API_KEY}"
      }
    }
  }
}
```

Stdio-based MCPs inherit the container environment automatically. HTTP-based MCPs receive auth via `Authorization` header constructed from an env var at config time.

### Secret scan rule

The following patterns in any tracked file must be treated as a hard error:
- `sk-...` (Anthropic), `ghp_...` (GitHub), `xoxb-...` (Slack), `AKIA...` (AWS)
- Any assignment where `key`, `token`, `secret`, or `password` is followed by a quoted string over 20 mixed alphanumeric characters

---

## Part 6, Claude Code Configuration

### `claude.json` (root)

```json
{
  "model": "claude-sonnet-4-5",
  "allowedTools": ["Bash", "Read", "Write", "WebSearch"],
  "mcpServers": {}
}
```

`allowedTools` should be kept to the minimum required for the workspace. Additional tools are added per workspace need, not by default.

---

## Part 7, GitHub Actions Dispatch

### `dispatch.yml`

```yaml
name: ICM dispatch

on:
  workflow_dispatch:
    inputs:
      prompt:
        description: Task prompt for the agent
        required: true
        type: string
      project:
        description: Project name (output path prefix)
        required: true
        type: string
      output_branch:
        description: Output branch name (auto-generated if blank)
        required: false
        type: string

jobs:
  run:
    runs-on: ubuntu-latest
    env:
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
      GITHUB_TOKEN:      ${{ secrets.GITHUB_TOKEN }}
      ICM_PROJECT:       ${{ github.event.inputs.project }}
    steps:
      - uses: actions/checkout@v4

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run agent
        run: claude --prompt "${{ github.event.inputs.prompt }}" --config claude.json

      - name: Commit and push artifact
        run: |
          SLUG=$(echo "${{ github.event.inputs.prompt }}" \
            | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | cut -c1-48)
          BRANCH="${{ github.event.inputs.output_branch }}"
          BRANCH="${BRANCH:-output/$(date +%Y-%m-%d)-${SLUG}}"
          git config user.name "icm-agent"
          git config user.email "icm-agent@noreply"
          git checkout -b "$BRANCH"
          git add --force projects/
          git commit -m "run: ${{ github.event.inputs.prompt }}"
          git push origin "$BRANCH"
          echo "artifact_branch=$BRANCH" >> $GITHUB_OUTPUT
```

### Scheduled runs

Add a `schedule` trigger alongside `workflow_dispatch` for recurring workflows:

```yaml
on:
  workflow_dispatch:
    inputs: ...
  schedule:
    - cron: '0 8 * * 1'   # Every Monday 08:00 UTC
```

Scheduled runs should derive the project name deterministically from the date so outputs are always predictably addressable.

---

## Part 8, Complete Repo File Layout

```
/
├── CLAUDE.md                              ← agent entry point, router only
├── SPEC.md                                ← this file, human reference and build contract
├── README.md                              ← human-facing overview
├── claude.json                            ← Claude Code tool and MCP config
├── .env.example                           ← env var names only, no values
├── .gitignore                             ← includes projects/**
│
├── skills/
│   ├── run.md                             ← run mode contract, execution, outputs, failure
│   └── build.md                           ← build mode contract, scaffolding, schemas, branch rules
│
├── workspaces/
│   └── {workspace}/
│       ├── context.md
│       └── {workflow}/
│           ├── context.md
│           └── {workstage}/
│               ├── context.md
│               └── {task}/
│                   └── context.md
│
├── projects/                              ← runtime only, never on main
│   └── {project-name}/                    ← replaces workspaces/ prefix
│       └── {workspace}/
│           └── {workflow}/
│               └── {workstage}/
│                   └── {task}/
│                       ├── output.md
│                       └── metadata.json
│
└── .github/
    ├── workflows/
    │   ├── dispatch.yml                   ← agent dispatch and artifact commit
    │   └── guard-main.yml                 ← blocks projects/ on main
    └── hooks/
        └── pre-push                       ← local guard
```

---

## Part 9, Agent Execution Flow

### Run mode (default)

```
1.  Clone repo
2.  Read CLAUDE.md, orient, detect mode (no [BUILD] tag → run mode)
3.  Read skills/run.md in full
4.  Confirm or derive ICM_PROJECT name
5.  Parse prompt → identify target workspace from routing table
6.  Read workspaces/{workspace}/context.md
7.  Identify target workflow from prompt
8.  Read workspaces/{workspace}/{workflow}/context.md
9.  For each workstage in order:
    a. Read {workstage}/context.md
    b. For each task in order:
       i.   Read {task}/context.md
       ii.  Execute task instructions exactly
       iii. Write output.md to:
            projects/{project}/{workspace}/{workflow}/{workstage}/{task}/
       iv.  Write metadata.json alongside output.md
10. git add --force projects/
11. git commit -m "run: {prompt-slug}"
12. git push origin output/{YYYY-MM-DD}-{slug}
13. Exit, no state retained
```

### Build mode ([BUILD] prefix)

```
1.  Clone repo
2.  Read CLAUDE.md, detect [BUILD] tag at position 0 → build mode
3.  Read skills/build.md in full
4.  Strip [BUILD] from prompt, remainder is the build instruction
5.  Parse build instruction → classify operation (new workspace / workflow /
    workstage / task / edit existing)
6.  Check workspaces/ for existing structure at target path
7.  Execute scaffolding operation using correct context.md schema from skills/build.md
8.  If new workspace created: add row to routing table in CLAUDE.md
9.  Write build-metadata.json to repo root
10. git add workspaces/ CLAUDE.md README.md claude.json .env.example
    (never git add ., do not stage projects/ or .github/)
11. git commit -m "build: {description-slug}"
12. git push origin build/{YYYY-MM-DD}-{slug}
13. Exit, do not open PR, do not merge
```

In both modes: never skip a `context.md`, never write to `main`, never output a secret value.

---

## Part 10, Glossary

| Term | Definition |
|---|---|
| **ICM** | Interpretable Context Methodology, all agent context is explicit, version-controlled, and human-readable |
| **Repo-as-a-Workspace** | A GitHub repo structured per ICM conventions, executable by a Claude Code cloud agent |
| **Workspace** | A domain area under `workspaces/`, the top level of the four-level hierarchy |
| **Workflow** | A defined, repeatable process within a workspace |
| **Workstage** | A single step within a workflow |
| **Task** | An atomic unit of work within a workstage |
| **CLAUDE.md** | Root-level agent entry point, router and mode detector only; carries no execution rules |
| **Skill** | A mode-scoped instruction file in `skills/`, the authoritative contract for agent behaviour in that mode |
| **Run mode** | Default execution mode, agent navigates and executes, repo hierarchy is read-only |
| **Build mode** | Activated by `[BUILD]` at prompt position 0, agent scaffolds or edits the workspace hierarchy |
| **context.md** | Scoped instruction file present at every level of the workspace hierarchy |
| **Progressive disclosure** | The pattern of reading context top-down, each level narrowing the agent's scope |
| **Projects tree** | Runtime output tree under `projects/`, `workspaces/` prefix replaced by `projects/{name}/`, never on main |
| **Artifact** | The `output.md` + `metadata.json` pair written at the task level |
| **Output branch** | The `output/{date}-{slug}` branch holding a single run mode run's project data |
| **Build branch** | The `build/{date}-{slug}` branch holding a single build mode run's scaffolding changes |
| **Run** | One agent execution: one prompt in, one branch out, container exits |
| **Dispatch** | Triggering a run via GitHub Actions `workflow_dispatch` |

---

*This SPEC.md is both a human reference and an agent build contract. An agent reading it has everything needed to execute a run or scaffold a new workspace. A human reading it has everything needed to understand, audit, or extend the system.*
