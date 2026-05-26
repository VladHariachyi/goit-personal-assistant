# Repository Contribution Guide

## Overview
This guide describes the contribution workflow and naming conventions for the project repository.
**PA** stands for Personal Assistant and is used as the project prefix in task identifiers.

## Branching Strategy
* For every task, you must create a separate branch from the `main` branch.
* Direct development inside `main` is not allowed.

## Branch Naming Convention
Branches must follow this pattern:
`[type]/PA-[task-number]-[short-description]`

### Examples
* `feat/PA-1-implemented-error-handling`
* `fix/PA-12-fixed-login-validation`
* `refactoring/PA-20-improved-events-structure`

## Task Types
There are 3 supported task types:

| Prefix | Purpose |
| :--- | :--- |
| `feat/` | New features or improvements |
| `fix/` | Bug fixes and defect resolution |
| `refactoring/` | Code structure and readability improvements without changing functionality |

These prefixes must be used both in:
* branch names
* commit messages

## Commit Message Convention
All commits must follow this format:
`[type]: [short descriptive message] [PA-task-number]`

### Examples
* `feat: implemented error handling for address book events [PA-1]`
* `fix: resolved issue with contact validation [PA-12]`
* `refactoring: improved event service architecture [PA-20]`

## Pull Request Policy
Pushing directly to the `main` branch is strictly prohibited.

This rule helps to:
* prevent merge conflicts
* avoid delivering unreviewed code
* reduce the risk of breaking the project

## Required Workflow
1. Create a separate branch from `main`
2. Implement your changes
3. Push your branch to the repository
4. Create a Pull Request (PR)
5. Wait for approval and code review
6. Merge into `main` only after approval

## Summary
* Always branch from `main`
* Use the correct branch naming convention
* Follow the commit message format
* Never push directly to `main`
* All changes must go through Pull Requests