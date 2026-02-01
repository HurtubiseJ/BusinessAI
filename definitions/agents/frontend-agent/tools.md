# Git CLI Tool for Claude Agents

Tool Name: git_cli

Description:
This tool exposes git functionality to the agent. The agent can stage, commit, branch, and push code changes according to allowed paths. All git commands are executed via git_tool.sh, which wraps git_tool.py.

Available Commands:

1. status
   - Description: Shows the current git status of the repository.
   - Usage Example: git_cli status

2. log
   - Description: Shows recent commits with one-line summaries and decorations.
   - Usage Example: git_cli log

3. checkout <branch_name>
   - Description: Switch to an existing branch.
   - Arguments:
       <branch_name> - name of the branch to switch to
   - Usage Example: git_cli checkout feature/login

4. branch <branch_name>
   - Description: Create and switch to a new branch.
   - Arguments:
       <branch_name> - name of the new branch to create
   - Usage Example: git_cli branch feature/login

5. add <file_paths>
   - Description: Stage specific files for commit.
   - Arguments:
       <file_paths> - one or more paths to files to stage
   - Usage Example: git_cli add frontend/login/button.css

6. commit <message>
   - Description: Commit staged changes with a commit message.
   - Arguments:
       <message> - commit message string
   - Usage Example: git_cli commit "Update login button hover state"

7. push <remote> <branch_name>
   - Description: Push commits to a remote branch.
   - Arguments:
       <remote> - name of the git remote (usually origin)
       <branch_name> - branch to push
   - Usage Example: git_cli push origin feature/login

Important Notes / Constraints:
- Only operate on files inside allowed paths defined in the agent.
- Do not force push to protected branches.
- Ensure commit messages are concise and descriptive.
- All git commands are executed via the tool script (git_tool.sh), not directly on the CLI.
- Destructive actions (branch deletion, force push) must be confirmed by the user or prevented by agent guardrails.

