# Python Virtual Environments — Complete Guide

## Table of Contents
- [What is a Virtual Environment?](#what-is-a-virtual-environment)
- [Why Use One?](#why-use-a-virtual-environment)
- [Project Structure](#project-structure)
- [Using `venv` (built-in)](#using-venv-built-in)
- [Using `uv` (modern, fast)](#using-uv-modern-tool)
- [pip vs uv — Comparison](#pip-vs-uv-comparison)
- [Common Commands Cheat Sheet](#common-commands-cheat-sheet)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [Summary](#summary)

---

## What is a Virtual Environment?

A **virtual environment** is an isolated Python environment created for a specific project. Each one has its own:

- Python interpreter (or a reference to one)
- Installed packages
- Dependency versions
- `pip`/package manager configuration

This isolation prevents conflicts between projects that need different package versions.

## Why Use a Virtual Environment?

Without isolation, all packages install **globally**, shared across every project on your machine.

**Example conflict:**
| Project | Needs |
|---|---|
| Project A | `numpy==1.24` |
| Project B | `numpy==2.0` |

Installing one globally breaks the other. A virtual environment solves this by giving each project its own private set of packages.

**Advantages:**
- Isolates project dependencies
- Prevents version conflicts
- Keeps the global/system Python clean
- Makes projects reproducible across machines
- Simplifies collaboration and onboarding
- Avoids needing `sudo`/admin rights to install packages

## Project Structure

```
My_Project/
│
├── .venv/              # virtual environment (not committed to git)
├── main.py
├── requirements.txt    # pip-based dependency list
├── pyproject.toml      # used by uv / modern tooling
├── .gitignore
└── README.md
```

---

## Using `venv` (built-in)

### 1. Create

```bash
python -m venv .venv
# or, if 'python' isn't aliased:
python3 -m venv .venv
```

This creates a `.venv/` folder containing a private Python interpreter and `site-packages`.

### 2. Activate

| OS / Shell | Command |
|---|---|
| Windows (Command Prompt) | `.venv\Scripts\activate` |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Linux / macOS | `source .venv/bin/activate` |

Once active, your prompt shows the environment name:
```
(.venv) C:\Projects\My_Project>
```

> **PowerShell execution policy error?** See [Troubleshooting](#troubleshooting).

### 3. Verify the Active Interpreter

```bash
python --version
```

| OS | Command to locate interpreter |
|---|---|
| Windows | `where python` |
| Linux/macOS | `which python` |

The path should point **inside** `.venv/`, confirming you're not using the global interpreter.

### 4. Install, List, Upgrade, Remove Packages

```bash
pip install requests
pip install numpy pandas matplotlib   # multiple at once

pip list                              # human-readable list
pip freeze                            # pinned versions, script-friendly

pip install --upgrade requests

pip uninstall requests
```

### 5. Export & Restore Dependencies

```bash
pip freeze > requirements.txt
```

Example `requirements.txt`:
```
numpy==2.3.0
pandas==2.2.3
requests==2.32.4
```

Install from it (e.g. after cloning a repo):
```bash
pip install -r requirements.txt
```

### 6. Deactivate & Delete

```bash
deactivate
```

To remove the environment entirely, just delete the folder:
```bash
rm -rf .venv        # Linux/macOS
rmdir /s .venv       # Windows CMD
```

Recreate anytime with `python -m venv .venv`.

---

## Using `uv` (modern tool)

[`uv`](https://docs.astral.sh/uv/) is a modern, Rust-based Python package and project manager — a drop-in replacement for `pip` + `venv` that is dramatically faster and manages dependencies declaratively.

```bash
# Install uv itself (one-time), e.g.:
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 1. Initialize a Project

```bash
uv init
```
Creates `pyproject.toml`, `.python-version`, and other scaffolding.

### 2. Create the Virtual Environment

```bash
uv venv
```

### 3. Activate

| OS | Command |
|---|---|
| Windows | `.venv\Scripts\activate` |
| Linux/macOS | `source .venv/bin/activate` |

### 4. Add / Remove Packages

```bash
uv add requests
uv add numpy pandas matplotlib

uv remove requests
```
`uv` automatically updates `pyproject.toml` and its lockfile — no manual `requirements.txt` bookkeeping needed.

### 5. Sync Dependencies

```bash
uv sync
```
Installs everything declared in `pyproject.toml`/lockfile — the standard step after cloning a repo.

### 6. Run Without Manually Activating

```bash
uv run main.py
```
Runs the script inside the project's environment automatically, even if it isn't activated in your current shell — handy for scripts, CI, and one-off commands.

### 7. Pin a Python Version

```bash
uv python install 3.12
uv python pin 3.12
```
`uv` can download and manage Python interpreters itself, so you don't need `pyenv` or a system install.

---

## pip vs uv Comparison

| Feature | pip + venv | uv |
|---|---|---|
| Package installation | ✅ | ✅ (much faster — parallel, cached) |
| Virtual environment creation | Separate (`venv`) | Built-in (`uv venv`) |
| Speed | Moderate | Very fast (Rust-based resolver) |
| Dependency file | Manual `requirements.txt` | Auto-managed `pyproject.toml` + lockfile |
| Lockfile / reproducibility | Not by default | Yes, built-in |
| Manage Python versions | No (needs pyenv, etc.) | Yes (`uv python`) |
| Run scripts in-env without activating | No | Yes (`uv run`) |

`uv` is generally the better choice for new projects; `pip`/`venv` remain the universal baseline every Python environment supports out of the box.

---

## Common Commands Cheat Sheet

| Task | venv / pip | uv |
|---|---|---|
| Create environment | `python -m venv .venv` | `uv venv` |
| Activate (Linux/macOS) | `source .venv/bin/activate` | same |
| Activate (Windows) | `.venv\Scripts\activate` | same |
| Install a package | `pip install <pkg>` | `uv add <pkg>` |
| Install from file | `pip install -r requirements.txt` | `uv sync` |
| List packages | `pip list` | `uv pip list` |
| Export dependencies | `pip freeze > requirements.txt` | automatic (`pyproject.toml`) |
| Upgrade a package | `pip install --upgrade <pkg>` | `uv add <pkg> --upgrade` |
| Remove a package | `pip uninstall <pkg>` | `uv remove <pkg>` |
| Run a script | `python main.py` (env active) | `uv run main.py` |
| Deactivate | `deactivate` | `deactivate` |
| Delete environment | delete `.venv/` folder | delete `.venv/` folder |

---

## Best Practices

- Create **one virtual environment per project** — never share across projects.
- **Never install project dependencies globally.**
- Activate the environment before writing or running any project code.
- Add `.venv/` to `.gitignore` — never commit it to version control.
- Share `requirements.txt` or `pyproject.toml`, not the environment folder itself.
- Recreate environments when needed rather than backing them up or copying them between machines (they contain absolute paths and aren't portable).
- Pin dependency versions for production projects to keep builds reproducible.
- Periodically review and remove unused dependencies.

## Troubleshooting

**"cannot be loaded because running scripts is disabled" (PowerShell)**
Run PowerShell as Administrator and allow local scripts:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**`python` command not found**
On some systems only `python3` is available; use `python3 -m venv .venv` instead.

**Activated environment still shows the global interpreter**
Check `which python` / `where python` — you may have a shell alias or another environment already active. Try opening a fresh terminal.

**`pip install` seems to affect packages outside the project**
The environment likely isn't activated. Reactivate it and confirm the prompt shows `(.venv)`.

**Cloned a project but `python main.py` fails with `ModuleNotFoundError`**
Dependencies weren't installed in the new environment yet — run `pip install -r requirements.txt` or `uv sync`.

---

## Summary

- A virtual environment isolates a project's dependencies from the system and other projects.
- Every project should have its own environment.
- `venv` is Python's built-in, universally supported tool.
- `uv` is a faster, modern alternative that also manages Python versions and lockfiles automatically.
- Share `requirements.txt` (pip) or `pyproject.toml` (uv) — never the environment folder itself.
- Recreate environments as needed instead of storing or copying them between machines.
