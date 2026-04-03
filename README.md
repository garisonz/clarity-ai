# ClarityAI

**See your code clearly.** ClarityAI catches what linters miss — combining fast static analysis with AI that understands your intent.

An intelligent CLI code review tool that performs multi-dimensional analysis (quality, security, performance) using AST parsing and pattern matching, then layers on contextual AI review via Ollama for deeper, human-like feedback.

---

## Features

- **Static Analysis Engine** — AST-based code inspection across three dimensions: quality, security, and performance
- **AI-Powered Review** — Contextual code review via Ollama models
- **Git Integration** — Review staged changes or specific commits
- **Plugin Architecture** — Modular analyzer system that's easy to extend with custom rules
- **Multiple Output Formats** — Rich terminal output, JSON (for CI pipelines), and Markdown (for PR comments)
- **Configurable** — TOML-based configuration with sensible defaults and per-project overrides

## Quick Start

### Installation

```bash
# Clone the repo
git clone https://github.com/garisonz/clarity-ai.git
cd clarity-ai

# Install in development mode
pip install -e .
```


### Run a review

```bash
# Review specific files
clarity-ai review main.py utils.py

# Review staged git changes
clarity-ai review --git-staged

```

## How It Works

ClarityAI runs in two passes:

**Pass 1 — Static Analysis** parses your Python files into ASTs and runs each enabled analyzer:

| Analyzer | What it catches |
|---|---|
| **Quality** | Long functions, deep nesting, missing docstrings, unused imports, bare excepts |
| **Security** | Hardcoded secrets, SQL injection patterns, `eval()`/`exec()` usage, `shell=True` in subprocess |
| **Performance** | List comprehension opportunities, string concat in loops, repeated attribute access |

**Pass 2 — AI Review** sends the source code, git diff, and static analysis results to Ollama Model, which returns structured feedback on architectural concerns, logic errors, and contextual improvements that rule-based tools can't catch.

If the API key is missing or the request fails, ClarityAI degrades gracefully — you still get the full static analysis.


## Output Examples

### Rich (Terminal)

```
┌─────────────────────────────────────────────────────────┐
│ ClarityAI Review — 3 files, 12 issues found             │
└─────────────────────────────────────────────────────────┘

 src/auth.py

  🔴 HIGH  SEC-001  Hardcoded secret detected (line 14)
     → Move to environment variable or secrets manager

  🟡 MED   QUAL-003 Function 'process_login' is 87 lines (line 22)
     → Extract validation logic into a helper function

  🔵 LOW   PERF-002 String concatenation in loop (line 45)
     → Use ''.join() or a list with .append()

  🟣 MED   AI-001   Auth token is never invalidated on logout (line 58)
     → Add token revocation to the logout handler
```

### JSON


## Project Structure

```
clarity-ai/
├── pyproject.toml
├── src/
│   └── clarity_ai/
│       ├── __init__.py
│       ├── cli.py          # Typer app, argument parsing
│       ├── ollama_reviewer.py        # Ollama API wrapper

```


## Tech Stack

- **Python 3.11+** — Core language
- **ast** — Abstract Syntax Tree parsing for static analysis
- **Ollama** — Ollama integration for AI review
- **Rich** — Terminal formatting and colored output
- **GitPython** — Git diff and staging integration
- **tomllib** — TOML configuration parsing

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run ClarityAI on itself
clarity-ai review src/
```


---

Built by [Garison Zagorski](https://garisonzagorski.com)
