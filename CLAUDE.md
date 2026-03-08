# TechStack Global - GSD Integration

This project uses the **Get Shit Done (GSD)** system for spec-driven development.

## GSD Commands

Always use the GSD workflow for significant changes or new features:

- **Help**: `/gsd:help`
- **New Project/Milestone**: `/gsd:new-project`
- **Discussion Phase**: `/gsd:discuss-phase <N>`
- **Planning Phase**: `/gsd:plan-phase <N>`
- **Execution Phase**: `/gsd:execute-phase <N>`
- **Verification**: `/gsd:verify-work <N>`
- **Progress**: `/gsd:progress`
- **Debugging**: `/gsd:debug`

## Architecture & Conventions

- **Root Structure**: 
  - `.claude/`, `.gemini/`, etc.: GSD configuration and command definitions.
  - `.planning/`: Active and completed project specifications, plans, and research.
- **Workflow**: 
  - Discuss → Plan → Research → Execute → Verify.
  - No code changes until the `SPEC.md` and phase plans are approved.

## Tech Stack

- **Frontend**: Tailwind CSS (if requested), HTML5, Vanilla JS.
- **Backend/AI Tools**: Python scripts for blog automation (`blogging_project/`).
- **Development**: Local server using `python -m http.server 8000`.
