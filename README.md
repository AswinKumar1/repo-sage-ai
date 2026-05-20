# RepoSage AI

RepoSage AI is a lightweight, Streamlit-based repository intelligence tool that analyzes code repositories and produces engineering artifacts such as test cases, API summaries, architecture notes, and other developer-focused insights.

This project is a reference implementation focused on rapidly scanning repositories (local or from Git), detecting technologies, traversing source code (with special handling for Java/Spring Boot projects and FTL templates), and generating prompts for an LLM to produce enterprise-grade test cases.

## Key features

- Load a repository from Git (branch-aware) or from a local path.
- Build a folder/tree view of the repository.
- Detect technologies (Java/Spring Boot, Node/Express, React, Python frameworks, GraphQL).
- Traverse Java repositories to find controllers, imports, utility classes, method calls, and workflow objects.
- Extract FTL template context (variables, GraphQL operations, field mappings, conditions).
- Build structured prompts for an LLM (via OpenRouter) to generate test cases and other artifacts.

## Getting started

Prerequisites

- Python 3.8+
- Git (if you plan to fetch remote repositories)

Install dependencies

Create a virtual environment and install the required packages:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Configuration

The project expects an OpenRouter API key (used in `services/ai/openrouter_service.py`) as an environment variable named `OPENROUTER_API_KEY`. You can provide it in a `.env` file at the repository root:

```
OPENROUTER_API_KEY=your_api_key_here
```

Usage

Start the Streamlit app:

```bash
streamlit run app.py
```

UI flow

- On the left: provide either a Git repository URL (then fetch branches and choose one) or a local repository path.
- After loading a repository, the app scans the project, detects technologies, builds a folder tree, and enables traversal and AI-powered analysis.
- Use the AI Workspace to extract FTL context, traverse repository artifacts, or generate test cases via the configured OpenRouter model.

Project structure

- `app.py` — Streamlit frontend and orchestration of services.
- `requirements.txt` — Python dependencies.
- `services/` — Collection of small utility modules that implement cloning, scanning, detection, traversal, prompt building and AI integration.
  - `git_service.py` — fetches remote branches (uses GitPython).
  - `repository_service.py` — clone or validate local repositories.
  - `scanner_service.py` — builds a folder tree while ignoring common build/artifact folders.
  - `detector_service.py` — lightweight heuristics to detect tech stack and APIs.
  - `analyzer_service.py` — basic repo stats, build tool & API style detection.
  - `traversal_service.py` — scans Java source files for controllers, imports, workflow objects and endpoints.
  - `ftl_extractor_service.py` — extracts information from FreeMarker (`.ftl`) templates.
  - `ai/` — contains LLM prompt builders and an OpenRouter client wrapper.

Notes and limitations

- This is a simple scanner and relies on heuristics (string matching, file presence). It is not a full static analysis tool.
- The OpenRouter integration requires a valid API key and network access.
- Cloning remote repositories uses temporary directories; ensure your environment has permissions and sufficient disk space.
- The tool currently focuses heavily on Java/Spring Boot/FTL patterns and basic Node/Python detection. Extend detectors as needed for other stacks.

Contributing

Contributions are welcome. Small, focused improvements that add detectors, improve parsing accuracy, or harden error handling are especially helpful.

Suggested next steps

- Add unit tests for the services in `services/`.
- Improve technology detection to parse lockfiles / build files instead of simple string checks.
- Add authentication and rate-limiting around LLM calls.

LICENSE

This repository does not include a license file by default. Add one if you plan to open-source this project.
