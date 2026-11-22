# Git, GitHub & GitHub Actions – CI/CD

## 1. Core Concepts & Easy Definitions

Before building pipelines, it helps to distinguish between the foundational tools discussed in the lecture [03:07]:

**Git (Distributed Version Control System):** Software installed locally on your machine that tracks changes in your source code files over time, manages branches, and helps resolve code conflicts when multiple developers work together [04:38].

**GitHub (Code Repository):** A cloud-based platform where teams host, share, and collaborate on Git repositories [03:40].

**GitHub Actions (CI/CD Automation Tool):** A built-in automation engine provided directly by GitHub that runs custom tasks (like testing, building, and deploying code) automatically whenever specific repository events occur [01:49].

**Continuous Integration (CI):** A development practice where team members frequently merge their code changes into a shared repository [09:51]. Every push or pull request automatically triggers builds and tests to verify that new code does not break existing features [10:01].

**Continuous Deployment / Delivery (CD):** An extension of CI that automatically packages and deploys code to target environments (such as Dev, QA, UAT, or Production servers) once all automated CI checks pass [10:30].

**Workflow:** An automated, configurable sequence of steps defined in a `.yml` (YAML) file inside your repository that executes when triggered by an event [25:53], [57:51].

### Term, Simple Analogy / Role and Key Function

| Term | Simple Analogy / Role | Key Function |
|---|---|---|
| Git | Local Save-History & Branch Manager | Tracks file edits, branches, and merges locally [07:57]. |
| GitHub | Shared Cloud Filing Cabinet | Stores the central codebase and hosts Pull Requests [03:40]. |
| GitHub Actions | Automated Quality Inspector & Courier | Runs tests on every commit (CI) and ships code to servers (CD) [08:42]. |

---

## 2. How Real-World Team Workflows Operate

In an Agile software or Data Science team, multiple developers work on separate features ("stories") simultaneously without disrupting the stable main branch [11:15], [12:35].

### The CI/CD Lifecycle Step-by-Step

**1. Branching & Coding:**

A developer creates a dedicated feature branch (e.g., `story-a-branch`) from `main` and writes code locally in an IDE like VS Code following clean coding standards [12:16], [27:20].

**2. Version Control & Pull Request (PR):**

The developer pushes the local branch to GitHub and opens a Pull Request (PR) requesting to merge changes into `main` [36:59]. If two developers modified the same file, merge conflicts are resolved first [16:37].

**3. Code Review:**

Peers or architects inspect the PR for code quality, style, and logic before approval [30:42].

**4. Automated CI Pipeline:**

Opening or updating the PR triggers a GitHub Actions workflow that spins up a clean virtual machine, builds the project, and executes automated tests (unit, integration, and end-to-end tests) [31:55], [38:32].

**5. Merge & Automated CD Pipeline:**

Once tests pass and the PR is merged into `main`, a CD workflow automatically deploys the application (often via Docker containers) across progressive environments [20:09], [22:12]:

- **Dev Environment:** Initial integration testing by developers [22:35].
- **QA Environment:** Dedicated bug and regression testing by the QA team [23:04].
- **UAT (User Acceptance Testing):** Pre-production staging validation [23:25].
- **Production (Live):** Final release accessible to end users [23:47].

---

## 3. Anatomy of a GitHub Actions YAML File

GitHub Actions workflows are written in YAML (key-value pairs) and stored inside the `.github/workflows/` directory of your repository [55:35], [57:51].

- **name:** Sets the display name of your workflow in the GitHub Actions tab [58:09].
- **on:** Defines the events (such as `push` or `pull_request` on specific branches) that trigger the workflow [58:55].
- **jobs:** Groups one or more tasks that execute as part of the workflow [01:00:03].
- **runs-on:** Specifies the cloud virtual machine/container environment (e.g., `ubuntu-latest`, `windows-latest`, or `macos-latest`) [01:00:23], [01:00:36].
- **steps:** A sequential list of commands (`run`) or reusable pre-built actions (`uses`) executed inside the runner [01:01:02], [01:02:23].

---

## 4. Hands-On Project: Automated Python Testing with GitHub Actions

### Project Directory Structure

Create the following folder structure locally so pytest can automatically discover your test suite [49:50]:

```text
app-github-action/
├── .github/
│   └── workflows/
│       └── python-app.yml
├── src/
│   ├── __init__.py
│   └── math_operations.py
├── tests/
│   ├── __init__.py
│   └── test_operations.py
├── requirements.txt
└── README.md
```

### Step 1: Initialize Git & Push to GitHub

Create an empty repository on GitHub, then initialize and link your local project folder [45:56], [47:25]:

```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```

### Step 2: Define Dependencies (requirements.txt)

Add pytest (for running automated unit tests) and any project libraries [49:16]:

```text
pandas
pytest
```

### Step 3: Write Application Code (src/math_operations.py)

Make sure `src/__init__.py` exists so Python treats `src` as an importable package [50:15].

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

### Step 4: Write Unit Tests (tests/test_operations.py)

pytest automatically looks for folders named `tests` and functions prefixed with `test_` [50:02], [51:51]:

```python
from src.math_operations import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(4, 3) == 1
    assert subtract(3, 3) == 0
    assert subtract(2, 3) == -1
```

### Step 5: Configure the CI Workflow (.github/workflows/python-app.yml)

Create the workflow file to automatically set up Python, install dependencies, and execute
