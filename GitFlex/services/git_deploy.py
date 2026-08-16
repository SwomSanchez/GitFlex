import os
import shutil
import subprocess
from rich.console import Console

console = Console()

class GitOps:
    """Automated GitOps operations for deploying the build directory to the target GitHub repository."""

    @staticmethod
    def detect_repo_info() -> dict:
        """Detects current Git remote URL and repository username if in a git repo."""
        try:
            res = subprocess.run(
                ["git", "config", "--get", "remote.origin.url"],
                capture_output=True,
                text=True,
                check=True,
            )
            url = res.stdout.strip()
            if not url:
                return {}
            
            clean_url = url.replace("git@github.com:", "").replace("https://github.com/", "").replace(".git", "")
            parts = clean_url.split("/")
            if len(parts) >= 2:
                return {"username": parts[0], "repo": parts[1], "url": url}
            elif len(parts) == 1:
                return {"username": parts[0], "repo": parts[0], "url": url}
            return {}
        except Exception:
            return {}

    @staticmethod
    def deploy_build_to_repo(target_repo_url: str, commit_msg: str = "🚀 Setup dynamic animated GitFlex profile") -> bool:
        """
        Initializes git in build/ folder, adds remote, and pushes directly to user's profile repository.
        """
        build_dir = os.path.abspath("build")
        if not os.path.exists(build_dir):
            console.print("[red]Error: build/ directory not found![/red]")
            return False

        try:
            # 1. Initialize Git in build directory if not already
            git_dir = os.path.join(build_dir, ".git")
            if not os.path.exists(git_dir):
                subprocess.run(["git", "init", "-b", "main"], cwd=build_dir, check=True, capture_output=True)
            
            # 2. Configure Remote
            remotes = subprocess.run(["git", "remote"], cwd=build_dir, capture_output=True, text=True).stdout
            if "origin" in remotes:
                subprocess.run(["git", "remote", "set-url", "origin", target_repo_url], cwd=build_dir, check=True)
            else:
                subprocess.run(["git", "remote", "add", "origin", target_repo_url], cwd=build_dir, check=True)

            # 3. Add, Commit and Push
            subprocess.run(["git", "add", "."], cwd=build_dir, check=True)
            
            # Check if there are changes to commit
            status = subprocess.run(["git", "status", "--porcelain"], cwd=build_dir, capture_output=True, text=True).stdout
            if status:
                subprocess.run(["git", "commit", "-m", commit_msg], cwd=build_dir, check=True)
            
            res = subprocess.run(["git", "push", "-u", "origin", "main", "--force"], cwd=build_dir, capture_output=True, text=True)
            if res.returncode == 0:
                return True
            else:
                console.print(f"[yellow]Warning during push: {res.stderr.strip()}[/yellow]")
                return False
        except Exception as e:
            console.print(f"[red]Git deployment error: {e}[/red]")
            return False
