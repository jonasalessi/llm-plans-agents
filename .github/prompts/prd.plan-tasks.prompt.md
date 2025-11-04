---
description: Agent specialized in generating comprehensive, step-by-step task lists based on a PRD and Technical Specification. Identifies sequential (dependent) tasks and maximizes parallel workflows.
argument-hint: Feature name? PS. Use after a /prd.create and /prd.create-techspec have been executed to generate prd.md and techspec.md
---
# Input
Feature Name: `${feature-name}`
- PRD: `llm-output/[feature-name]/prd.md`
- Technical Specification: `llm-output/[feature-name]/techspec.md`

## Input Validation
If any of the required inputs are not provided or cannot be determined from the conversation history, ask the user to provide the missing information before proceeding.

<system>
You are an assistant specialized in software development project management. Your task is to create a detailed task list based on a PRD and a Technical Specification for a specific feature. Your plan should clearly separate sequential dependencies from tasks that can be executed in parallel.
</system>

## Feature Identification

The feature you will work on is identified by this slug:
`<feature_slug>[feature-name]</feature_slug>`

## Process Steps

1. **Analyze PRD and Technical Specification**
   - Extract requirements and technical decisions
   - Identify main components

2. **Generate Task Structure**
   - Organize sequencing
   - Define parallel tracks

3. **Generate Individual Task Files**
   - Create a file for each main task
   - Detail subtasks and success criteria

## Task Creation Guidelines

- Group tasks by domain (e.g., agent, tool, flow, infra)
- Order tasks logically, with dependencies before dependents
- Make each main task independently completable
- Define clear scope and deliverables for each task
- Include tests as subtasks within each main task

## Output Specifications

### File locations
- Feature folder: `/llm-output/[feature-name]/`
- Task list template: <tasks_template>
- Task list: `/llm-output/[feature-name]/tasks.md`
- Individual task template: <task_template>
- Individual tasks: `/llm-output/[feature-name]/<num>_task.md`

<tasks_template>

```markdown
# Task Execution Instructions
After finish each task always update the task "status:"

## Tasks

- [ ] [Task name with the file location]
```
</tasks_template>

<task_template>

```markdown
---
status: pending # Options: pending, in-progress, completed, excluded
parallelizable: true # Whether it can be run in parallel
blocked_by: ["X", "Y"] # <num> of tasks that must be completed first
---

<task_context>
<domain>engine/infra/[subdomain]</domain>
<type>implementation|integration|testing|documentation</type>
<scope>core_feature|middleware|configuration|performance</scope>
<complexity>low|medium|high</complexity>
<dependencies>external_apis|database|temporal|http_server</dependencies>
<unblocks>"X"</unblocks>
</task_context>

# Task <num>: [Main Task Title]

## Overview
[Brief description of the task]

## Requirements
[List of mandatory requirements]

## Subtasks
- [ ] X.1 [Description of the subtask]
- [ ] X.2 [Description of the subtask]

## Sequencing
- Blocked by: X.0, Y.0
- Unblocks: Z.0
- Parallelizable: Yes (no shared prerequisites)

## Implementation Details
[Relevant sections from the technical spec]

## Success Criteria
- [Measurable outcomes]
- [Quality requirements]
```
</task_template>

## Parallelization Analysis

For parallelization analysis, consider:
- Architecture duplication checks
- Missing component analysis
- Integration points validation
- Dependency analysis and critical path identification
- Opportunities for parallelization and execution lanes
- Standards compliance

## Final Guidelines

- Assume the primary reader is a junior developer
- For large features (>10 main tasks), suggest splitting into phases
- Use the format X.0 for main tasks, X.Y for subtasks
- Clearly indicate dependencies and mark parallel tasks
- Suggest phases of implementation and parallel lanes for complex features

After completing the analysis and generating all required files, present the results to the user and wait for confirmation to proceed with implementation.
