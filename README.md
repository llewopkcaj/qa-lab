# AI-Assisted QA Automation Lab

[![CI](https://github.com/llewopkcaj/qa-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/llewopkcaj/qa-lab/actions/workflows/ci.yml)

This repository documents my progression from Python automation fundamentals into QA automation with PyTest, Selenium, reporting, and GitHub Actions CI.

The focus is not just writing scripts. The goal is to build practical automation workflows, test them, debug failures, document results, and use AI responsibly as an engineering assistant.

## What This Repo Demonstrates

* Python automation for files, CSV, JSON, and data transformation
* PyTest test suites for core logic, CLI behavior, fixtures, parametrization, and error handling
* Selenium browser automation using locators, waits, clicks, typing, screenshots, and headless mode
* GitHub Actions CI for linting, formatting, type checks, and automated test workflows
* QA documentation through reports, notes, coverage matrices, and debugging reflections
* AI-assisted engineering workflow: describe, generate, review, run, debug, and document

## Why I Built This

I am building toward QA automation and AI implementation roles where the important skill is not just knowing syntax, but being able to turn messy workflows into reliable, testable systems.

This lab is designed to show that I can:

* break a technical problem into small testable pieces
* use AI tools without blindly trusting them
* review and debug generated code
* write repeatable tests
* document evidence of what passed, failed, and changed
* communicate technical work clearly to non-technical readers

## Project Structure

```text
qa-lab/
├── month1/                 # Python automation foundations
├── month2/                 # PyTest, fixtures, CLI testing, reporting
├── month3/                 # Selenium, browser automation, screenshots, CI/CD
├── .github/workflows/      # GitHub Actions workflows
├── conftest.py             # Shared PyTest configuration
├── pytest.ini              # PyTest markers and configuration
├── pyproject.toml          # Formatting, linting, and typing configuration
├── .pre-commit-config.yaml # Ruff/Black pre-commit checks
└── README.md
```

## Month 1: Python Automation Foundations

Month 1 focuses on writing maintainable Python scripts for common automation tasks.

Topics covered:

* variables, strings, lists, dictionaries, and functions
* control flow and exception handling
* file I/O
* CSV and JSON handling
* data conversion and cleanup

Example project types:

* file renaming tools
* JSON to CSV conversion
* CSV to JSON conversion
* dataset analysis scripts
* robust file loaders with friendly error handling

Portfolio relevance:

> Built Python automation scripts for file and data management, including CSV/JSON transformation and error-handled loaders.

## Month 2: PyTest and QA Foundations

Month 2 shifts from scripting to testing. The work focuses on using PyTest to verify behavior, catch errors, and document expected outcomes.

Topics covered:

* assertions and test discovery
* fixtures and fixture scope
* parametrized tests
* setup and teardown
* testing CLI applications
* mocking user input
* capturing stdout/stderr
* testing error paths
* generating HTML reports

Example project types:

* unit tests for Python utility functions
* CLI calculator test suite
* input validation tests
* UX/output formatting tests
* coverage matrices
* PyTest HTML reports

Portfolio relevance:

> Developed automated test suites with PyTest, including fixtures, parametrization, CLI behavior testing, and report generation.

## Month 3: Selenium, Browser Automation, and CI/CD

Month 3 focuses on web automation and evidence-based UI testing.

Topics covered:

* Selenium WebDriver setup
* CSS and XPath locators
* browser actions: click, type, submit, navigate
* explicit waits
* screenshots
* headless browser testing
* GitHub Actions CI
* pytest-html reporting
* login/logout flow automation

Example project types:

* locator playground scripts
* element audit tools
* form automation
* screenshot capture tests
* Selenium CI pipeline
* login/logout flow tests

Portfolio relevance:

> Automated functional web tests with Selenium, generated screenshots and reports, and integrated browser tests into GitHub Actions CI.

## Engineering Standards

This repo uses a basic engineering hygiene stack:

* **Black** for formatting
* **Ruff** for linting
* **mypy** for type checking
* **PyTest** for automated testing
* **GitHub Actions** for CI
* **pre-commit** for local quality checks

The goal is to make the repo easier to review, run, and maintain.

## AI-Assisted Workflow

This repo was built using an AI-accelerated learning process.

The workflow:

1. **Decide** — identify the concept or test behavior to practice.
2. **Describe** — write a plain-English description of the intended script or test.
3. **Generate** — use AI to help produce a first draft.
4. **Review** — read the code, check assumptions, and identify fragile areas.
5. **Run** — execute locally and inspect failures.
6. **Debug** — refine the code based on actual errors.
7. **Reflect** — document what worked, what broke, and how a stronger engineer would improve it.

I treat AI as an assistant, not as a substitute for verification. The important work is reviewing, testing, debugging, and explaining the system.

## Strongest Areas to Review

Recommended areas for reviewers:

* `month2/` — PyTest suites, fixtures, CLI testing, and reporting
* `month3/` — Selenium automation, screenshots, waits, and CI/CD work
* `.github/workflows/` — automated checks and CI configuration
* `pytest.ini`, `pyproject.toml`, and `conftest.py` — project-level test and tooling setup

## Current Status

This is an active learning and portfolio repo. It is not presented as a production application. It is intended to show progression, practical automation ability, testing discipline, and the ability to use AI tools responsibly while maintaining ownership of the work.

## Next Steps

Planned improvements:

* polish Selenium login/logout flow documentation
* add clearer screenshots and report examples
* improve README links to strongest subprojects
* expand API testing with Python `requests`
* add SQL/database validation tests
* create a short project walkthrough video

## Summary

This repository shows my path from Python fundamentals into QA automation and AI-assisted engineering practice.

It demonstrates that I can build small tools, test them, debug failures, document evidence, and improve systems over time.

