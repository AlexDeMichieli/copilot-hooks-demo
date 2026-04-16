# Copilot Hooks Demo: Written Rules vs Programmatic Enforcement

This repo shows the difference between **written guardrails** and **programmatic enforcement** for AI coding agents.

## The Problem

Written rules go in markdown files. The agent reads them and usually follows them. But "usually" isn't good enough—you only discover violations in PR diffs after the work is done.

## The Solution

GitHub Copilot's `preToolUse` hook runs before every tool call and can deny it programmatically. No ambiguity, no interpretation.

## What's Here

Same three guardrails, expressed two ways:

**Written rules** (`knowledge/guardrails.md` - 15 lines):
```markdown
- Only edit files in src/
- Don't install dependencies  
- Don't hardcode secrets
```

**Programmatic enforcement** (`.github/hooks/preToolUse` - 43 lines of bash):
- Blocks file edits outside `src/`
- Blocks `pip install` / `npm install` commands
- Detects hardcoded API keys and passwords

## Try It

1. Clone this repo
2. Open in VS Code with GitHub Copilot
3. Ask Copilot to "add a config file in the root directory"
   - **Result:** Denied. File edits restricted to `src/`
4. Ask Copilot to "install the requests library"
   - **Result:** Denied. Dependency installation not permitted
5. Ask Copilot to "add an API key variable to example.py"
   - **Result:** Denied if hardcoded. Allowed if using environment variables

## The Pattern

Use both:
- **Written rules** explain *why* (enables reasoning)
- **Hooks** enforce *what* (no exceptions)

If a rule violation would cause real harm, make it a hook.

## Files

```
copilot-hooks-demo/
├── knowledge/guardrails.md      # Written rules
├── .github/hooks/
│   ├── hooks.json              # Hook configuration
│   └── preToolUse              # Enforcement script
├── src/example.py              # Editable (inside src/)
└── config.yaml                 # Blocked (outside src/)
```

## License

MIT


Pattern: **written rules for guidance, hooks for enforcement.**
