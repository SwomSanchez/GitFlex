class DeployTemplates:
    """Deployment templates for README.md and GitHub Actions workflows."""

    @staticmethod
    def get_workflow_yml() -> str:
        return """name: Update GitFlex Profile

on:
  schedule:
    # Runs daily at midnight UTC
    - cron: '0 0 * * *'
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: write

jobs:
  generate-profile:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install requests

      - name: Generate Profile SVG
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python generate_profile.py

      - name: Commit and push if changed
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add assets/profile.svg
          git diff --quiet && git diff --staged --quiet || (git commit -m "🚀 Auto-update GitFlex profile SVG" && git push)
"""

    @staticmethod
    def get_readme_md(username: str) -> str:
        return f"""<p align="center">
  <a href="https://github.com/{username}">
    <img src="assets/profile.svg" alt="{username}" width="850" />
  </a>
</p>
"""
