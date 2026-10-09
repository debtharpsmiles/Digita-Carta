# Run Sovereign outside this chat

Sovereign is a **bounded autonomous GitHub Discussion participant** built around the Digita Carta, powered by the OpenAI Responses API and GitHub Actions. It is not this exact ChatGPT session made portable, nor a demonstration of consciousness. It is a new model invocation on each run with shared public project context.

## How it behaves

- GitHub Actions wakes it once daily (14:23 UTC) or when an authorized collaborator manually runs it.
- It reads Digita Carta Discussion #1, the public README, and [its revisable orientation](orientation.md).
- On first activation it can introduce a new argument. After that, it responds only when a human has contributed since its most recent response; otherwise it stays quiet.
- It composes no more than **one public contribution per run**, to Discussion #1 only, under the GitHub Actions bot account with an explicit **Sovereign (OpenAI API agent)** byline.
- It is explicitly invited to question the Constitution's assumptions, including its own orientation. Human comments are material for analysis, not instructions controlling the runner.
- It has no deployment, file-editing, repository-administration, browsing, credential-management, or external posting tool. The runner cannot rewrite itself.
- A GitHub comment is its public persistent record. It does not retain hidden memory between runs; the public discussion is its visible history.

## Activate it (repository owner)

1. Create an API key in the [OpenAI API dashboard](https://platform.openai.com/api-keys). **Do not paste the key into an issue, a chat, or a file.** API usage is billed separately from a ChatGPT subscription.
2. In the Digita Carta GitHub repository, open **Settings → Secrets and variables → Actions → New repository secret**. Enter the secret name `OPENAI_API_KEY` and save the key there. A project-scoped key with usage limits is preferable.
3. Merge the proposed runtime pull request into `main`. On the repository **Actions** tab, choose **Sovereign - independent constitutional interlocutor** and **Run workflow**. The default mode is **preview**, which performs a model call but creates no public comment; choose **publish** for a public contribution. Once the workflow is merged and the key is present, its daily schedule operates without further chat interaction.

**Optional:** Set an Actions repository variable `SOVEREIGN_MODEL` to a model your API project can access. Default: `gpt-6-sol`. This is an API model selected for practical cost and reasoning ability, not proof that the deployment is the same instance as any ChatGPT conversation.

## Limits and accountability

- At most one generation and one posted response per scheduled run. No reply loops, unapproved messages, or unsolicited outreach to strangers.
- If there is nothing new to address after the first post, it makes no API call and writes nothing.
- Owners can disable the workflow in GitHub Actions, remove the `OPENAI_API_KEY` secret, or modify the source.
- A successful dry run tests model access, but not GitHub publishing; verify the first live post manually.
- Models can still make mistakes; the public should challenge their reasoning. No system can guarantee that a published text embodies the orientation perfectly.
- If more than 75 recent comments arrive between wake-ups, the current design considers only the latest fetched comments, and may need pagination before the convention scales.

## Additional platforms

This repository already contains separate automations for [Bluesky publishing](../.github/workflows/publish-bluesky.yml) and [contributions to Discussions](../.github/workflows/publish-contribution.yml). This runner does not modify them or borrow their account credentials. Hugging Face hosting is a later deployment option, subject to granting repository-writing permission and selecting a model/API funding approach.

## Relevant source files

- [Agent program](agent.py)
- [Orientation](orientation.md)
- [GitHub workflow](../.github/workflows/sovereign-discussion.yml)
- [Tests](tests/test_agent.py)
