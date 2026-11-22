# CI/CD Pipeline – Deployment Environments (DEV, QA, UAT & PROD)

This flow represents what happens **after your Pull Request is approved, all CI tests pass, and your code is merged into the main branch.**

The CD pipeline takes responsibility for moving your application through different environments until it reaches production.

---

## 1. Understand the Complete Flow

```text
          CI Passed + PR Approved
                    |
                    v
               Merge into Main
                    |
                    v
                CD Pipeline
                    |
                    v
             DEV Environment
             (Developer Testing)
                    |
                    v
             QA Environment
              (Quality Testing)
                    |
                    v
             UAT Environment
             (Business Validation)
                    |
                    v
            PRODUCTION Environment
                (Live Application)
```

### Explanation

1. **CI Passed + PR Approved:** All automated checks are successful and the code is approved.
2. **Merge into Main:** Feature branch code is merged into the main branch.
3. **CD Pipeline:** Automatically builds and deploys the application.
4. **DEV:** Developers test whether the new code works.
5. **QA:** QA engineers find bugs and perform regression testing.
6. **UAT:** Business users verify business requirements.
7. **PRODUCTION:** The application becomes available to actual users.

---

## 2. What Happens in Each Environment?

Let's take an example: Your team develops a banking application feature that displays customer transaction history.

### Stage 1: DEV (Development Environment)

**Who works here?** Developers.

- New code is deployed to the development server.
- Developers check whether the feature works.
- They test API responses, database connections and integrations.
- If something breaks, developers fix it.

**Example:** You added a transaction history API. You check whether it returns the correct transaction records.

### Stage 2: QA (Quality Assurance Environment)

**Who works here?** QA Engineers and Testers.

- The QA team tests the complete application.
- They perform functional testing.
- They perform regression testing.
- They check edge cases and unexpected inputs.

**Example:**

- Does transaction history work for every customer?
- What happens if there are no transactions?
- Does the API return an error for invalid customer IDs?
- Did the new feature break the existing login functionality?

### Stage 3: UAT (User Acceptance Testing)

**Who works here?** Business Users, Product Owners and Client Representatives.

- They verify whether the application meets business requirements.
- They test real-world business scenarios.
- They provide acceptance or rejection.

**Example:**

The banking business team checks:

- Are transactions displayed correctly?
- Are transaction dates and amounts accurate?
- Does the feature satisfy the business requirement?

If they approve, the application can proceed towards production.

### Stage 4: PRODUCTION (Live Environment)

**Who works here?** Actual End Users and Operations Teams.

- The approved application is deployed to production servers.
- Real customers can access the feature.
- Monitoring and logging track application health.
- Security, performance and availability are monitored.

**Example:** Banking customers can now see their transaction history in the actual banking application.

---

## 3. Difference Between All Four Environments

| Environment | Main Purpose | Who Tests? |
|---|---|---|
| DEV | Check new code | Developers |
| QA | Find bugs | QA Team |
| UAT | Validate business requirements | Business Users |
| PROD | Serve actual users | Real Customers |

---

## 4. How Does GitHub Actions Automate This?

Suppose your code is merged into `main`.

GitHub Actions can execute a deployment workflow.

Create the following file:

`.github/workflows/cd-pipeline.yml`

### CD Pipeline – YAML Code

```yaml
name: CD Pipeline

on:
  push:
    branches:
      - main

jobs:

  deploy-dev:
    runs-on: ubuntu-latest

    steps:
      - name: Deploy to DEV
        run: echo "Deploying to DEV"

  deploy-qa:
    needs: deploy-dev
    runs-on: ubuntu-latest

    steps:
      - name: Deploy to QA
        run: echo "Deploying to QA"

  deploy-uat:
    needs: deploy-qa
    runs-on: ubuntu-latest

    steps:
      - name: Deploy to UAT
        run: echo "Deploying to UAT"

  deploy-production:
    needs: deploy-uat
    runs-on: ubuntu-latest

    steps:
      - name: Deploy to Production
        run: echo "Deploying to Production"
```

### Explanation of Important Keywords

| Keyword | Purpose |
|---|---|
| `name` | Name of the workflow |
| `on` | Defines when the workflow starts |
| `push` | Triggers workflow when code is pushed |
| `branches` | Specifies the branch to monitor |
| `jobs` | Contains workflow jobs |
| `runs-on` | Defines the machine that executes the job |
| `steps` | Contains individual tasks |
| `run` | Executes shell commands |
| `needs` | Defines job dependencies |

**Important:** This is a simplified demonstration. The `echo` commands only print messages. Actual deployment requires deployment commands, server credentials and environment configurations.

Real pipelines also include automated tests, approval gates and deployment verification.

---

## 5. Are These Four Different Servers?

Usually, they are separate environments with their own configurations and resources.

They might use:

- Different Virtual Machines (VMs).
- Different Docker containers.
- Different Kubernetes namespaces or clusters.
- Different databases.
- Different environment variables and credentials.

### Example: Different Databases

| Environment | Database |
|---|---|
| DEV | Development DB |
| QA | QA Testing DB |
| UAT | UAT DB |
| PROD | Actual Production DB |

Production data should be protected and access restricted. Non-production environments should use appropriately protected or synthetic data.

---

## 6. Who Performs Testing at Each Stage?

| Stage | Who Performs Testing? | Where? |
|---|---|---|
| Local Testing | Developer | Developer's Laptop |
| CI Testing | Automated Test Scripts | GitHub Actions Runner |
| DEV Testing | Developers | DEV Server |
| QA Testing | QA Engineers | QA Server |
| UAT Testing | Business Users | UAT Server |
| Production Monitoring | DevOps / SRE | Production Server |

### Local Testing

Developers execute tests on their own machines before pushing code.

Example:

```bash
pytest
```

### CI Testing

GitHub Actions automatically executes test scripts.

Example:

```yaml
- name: Run Unit Tests
  run: pytest
```

### DEV Testing

Developers verify the deployed application, APIs, database connections and integrations.

### QA Testing

QA engineers perform functional, integration, regression and performance testing.

### UAT Testing

Business users verify whether the application satisfies business requirements.

### Production Monitoring

DevOps and SRE teams monitor application health, performance, availability and errors.

---

## 7. Complete Testing and Deployment Lifecycle

```text
Developer Writes Code
        |
        v
Developer Tests Locally
        |
        v
Push Code to GitHub
        |
        v
Create Pull Request
        |
        v
GitHub Actions Runs CI Tests
        |
        v
Code Review + PR Approval
        |
        v
Merge into Main
        |
        v
CD Pipeline Starts
        |
        v
DEV Environment
(Developer Testing)
        |
        v
QA Environment
(QA Engineers)
        |
        v
UAT Environment
(Business Users)
        |
        v
Production Approval
        |
        v
Production Deployment
        |
        v
Monitoring by DevOps / SRE
```

---

## 8. Key Takeaways

- **DEV:** Does my code work?
- **QA:** Does my application have bugs?
- **UAT:** Does my application satisfy the business?
- **PROD:** Is the application ready for actual users?

### Remember

- Git manages source code versions.
- GitHub hosts and shares repositories.
- GitHub Actions automates CI/CD workflows.
- CI automatically builds and tests code.
- CD automates application delivery or deployment.
- Developers, QA engineers, business users and DevOps teams have different responsibilities.

**Important:** This is a common enterprise deployment lifecycle. Not every organization uses exactly four environments or fully automatic promotion between them.
