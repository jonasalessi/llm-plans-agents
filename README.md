# LLM-Plan-Agents

This repository contains reusable prompt and agent markdown I use in daily work with GitHub Copilot. It centralizes planning flows (PRDs, Tech Specs, task plans) and reference agents for consistent engineering practices.

## Prompt Library

- `/.github/prompts` — curated Copilot prompts.
- `/.github/templates` — document templates used by prompts.
- Output folder: `./.prd/` (prompts write results here).

### Using the PRD Prompts (`/prd.*`)

Recommended flow inside GitHub Copilot Chat:

1) `/prd.create "<Feature Name>"`
- Purpose: creates a complete PRD from a guided clarify → plan → draft workflow.
- Template: `.github/templates/prd-template.md`
- Output: `.prd/prd-<feature-name-kebab>/prd.md`
- Notes: answer the agent’s clarifying questions before it drafts and saves the file.

2) `/prd.create-techspec "<Feature Name>"`
- Purpose: generates a technical specification from the approved PRD.
- Template: `.github/templates/techspec-template.md`
- Reads: `.prd/prd-<feature-name-kebab>/prd.md`
- Output: `.prd/prd-<feature-name-kebab>/techspec.md`

3) `/prd.plan-tasks "<Feature Name>"`
- Purpose: produces a sequenced task plan and individual task files derived from the PRD and Tech Spec.
- Reads: the PRD and Tech Spec produced in the previous steps.
- Outputs: `.prd/prd-<feature-name-kebab>/tasks.md` and numbered `.prd/prd-<feature-name-kebab>/<num>_task.md`
- Tip: use the same feature folder you created with `/prd.create`.

Where to find the prompt definitions and linked agents:
- `.github/prompts/prd.create.prompt.md`
- `.github/prompts/prd.create-techspec.prompt.md`
- `.github/prompts/prd.plan-tasks.prompt.md` (these reference the PRD/Tech Spec/Task Planning agents for the detailed flows)

Example
- In Copilot Chat: `/prd.create "Team Mentions"` → generates `.prd/prd-team-mentions/prd.md`. You can follow the agent’s handoff prompt to start the Tech Spec.
- Then: `/prd.create-techspec "Team Mentions"` → writes `.prd/prd-team-mentions/techspec.md`. Accept the handoff to move into task planning.
- Finally: `/prd.plan-tasks "Team Mentions"` → writes tasks under `.prd/prd-team-mentions/`

### Other Useful Prompts

- `.github/prompts/shapeup-pdr.prompt.md` — Shape Up style PRD using `prd-shapeup-template.md`.
- `.github/prompts/release.create.prompt.md` — creates release notes from grouped commits; uses `.github/scripts/git_grouped_commits_markdown.py`.
- `.github/prompts/refactor.react.prompt.md` — React refactor plan aligned with the React Agent.

## Agents

Agent guides live in `/.github/agents` and serve as style and architectural references that prompts (and your own chat requests) can reference explicitly.

- `.github/agents/React Agent.agent.md` — React + TypeScript standards, component structure, hooks, testing, styling with Tailwind.
- `.github/agents/Kotlin Agent.agent.md` — Kotlin backend standards, Spring Boot, clean architecture, SOLID, testing.
- `.github/agents/prd.create.agent.md` — guided PRD creation workflow with template usage and clarification steps.
- `.github/agents/prd.techspec.agent.md` — Tech Spec drafting flow based on an approved PRD.
- `.github/agents/prd.plan-tasks.agent.md` — task planning workflow that consumes the PRD and Tech Spec.

How to use
- In Copilot Chat, you can reference these agents explicitly in your request (e.g., “follow the React Agent guidelines”) or use prompts that already link to them (e.g., `refactor.react.prompt.md`).

## Conventions

- Feature folder naming: prefer kebab-case (e.g., `team-mentions`).
- PRD/Tech Spec default folder: `.prd/prd-<feature-name-kebab>/` as defined in the PRD prompts.
- Task plans and task files are also saved under `.prd/prd-<feature-name-kebab>/`; keep the same feature slug consistently when running the three `/prd.*` prompts.
