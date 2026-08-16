import os
import sys
import argparse
import webbrowser
from rich.console import Console
from rich.prompt import Prompt, Confirm

from GitFlex.ui.banner import print_banner
from GitFlex.config import ConfigManager
from GitFlex.services.github import GitHubProvider
from GitFlex.engine.renderer import GitFlexEngine
from GitFlex.engine.synthesizer import ScriptSynthesizer
from GitFlex.services.templates import DeployTemplates
from GitFlex.services.git_deploy import GitOps
from GitFlex.modules.themes import list_themes

console = Console()

def cmd_init():
    """Interactive Setup Wizard & Isolated Build Generator."""
    print_banner()
    
    console.print("\n[bold cyan]🚀 GitFlex Profile & CV Setup Wizard[/bold cyan]\n")
    
    username = Prompt.ask(
        "[bold green]?[/bold green] GitHub Username"
    ).strip()

    if not username:
        console.print("[red]Username cannot be empty![/red]")
        return

    repo_url = Prompt.ask(
        "[bold green]?[/bold green] Target Profile Repository URL",
        default=f"https://github.com/{username}/{username}.git"
    ).strip()

    name = Prompt.ask(
        "[bold green]?[/bold green] Display Name (Leave empty to use GitHub name)",
        default=""
    ).strip()

    bio = Prompt.ask(
        "[bold green]?[/bold green] Bio / Subtitle (Leave empty to use GitHub bio)",
        default=""
    ).strip()

    # Theme Selection
    themes = list_themes()
    console.print("\n[bold magenta]🎨 Theme Selection:[/bold magenta]")
    for idx, t in enumerate(themes, 1):
        console.print(f"  [bold cyan]{idx}[/bold cyan]. [bold white]{t['name']}[/bold white] - [dim]{t['description']}[/dim]")
    
    theme_choice = Prompt.ask(
        "[bold green]?[/bold green] Select Theme Number",
        default="1"
    )
    try:
        chosen_theme = themes[int(theme_choice) - 1]["id"]
    except Exception:
        chosen_theme = "cyberpunk_nebula"

    # Tech Stack Selection
    from GitFlex.services.icons import list_local_icons
    available_icons = list_local_icons()
    if available_icons:
        console.print(f"\n[bold yellow]⚡ Detected Icons in GitFlex/icons/:[/bold yellow] [dim]{', '.join(available_icons)}[/dim]")
        default_tech = ", ".join(available_icons[:8])
    else:
        default_tech = ""

    tech_input = Prompt.ask(
        "\n[bold green]?[/bold green] Tech Stack (Enter icon names or leave empty)",
        default=default_tech
    ).strip()
    tech_items = [t.strip().lower() for t in tech_input.split(",") if t.strip()]

    # Save to build/gitflex.json
    config = {
        "username": username,
        "repo_url": repo_url,
        "name": name,
        "bio": bio,
        "theme": chosen_theme,
        "theme_overrides": {},
        "layout": {"width": 850, "height": 650},
        "widgets": [
            {"id": "particles", "enabled": True, "count": 32},
            {"id": "header", "enabled": True, "name": name, "bio": bio},
            {"id": "stats", "enabled": True},
            {"id": "languages", "enabled": True, "limit": 5},
            {"id": "current_focus", "enabled": True},
            {"id": "tech_stack", "enabled": True, "items": tech_items},
        ]
    }

    # Fetch Data & Generate Build Assets
    with console.status("[bold cyan]Analyzing GitHub data & building isolated assets in build/...[/bold cyan]", spinner="dots"):
        provider = GitHubProvider(username)
        try:
            user_data = provider.fetch_user_data()
        except Exception as e:
            console.print(f"[yellow]Warning: Could not fetch GitHub profile: {e}[/yellow]")
            user_data = {"name": name, "bio": bio, "public_repos": 0, "followers": 0}
        
        try:
            repos_data = provider.fetch_repositories()
        except Exception as e:
            console.print(f"[yellow]Warning: Could not fetch repositories: {e}[/yellow]")
            repos_data = []

        stats_data = provider.calculate_stats(user_data, repos_data)
        
        context = {
            "user": user_data,
            "repos": repos_data,
            "stats": stats_data,
        }

        # 1. Render SVG inside build/assets/profile.svg
        engine = GitFlexEngine(config)
        svg_content = engine.render_svg(context)

        os.makedirs("build/assets", exist_ok=True)
        with open("build/assets/profile.svg", "w", encoding="utf-8") as f:
            f.write(svg_content)

        # 2. Synthesize custom standalone script inside build/generate_profile.py
        custom_script = ScriptSynthesizer.generate_standalone_script(config)
        with open("build/generate_profile.py", "w", encoding="utf-8") as f:
            f.write(custom_script)

        # 3. Create build/.github/workflows/generate_profile.yml
        os.makedirs("build/.github/workflows", exist_ok=True)
        with open("build/.github/workflows/generate_profile.yml", "w", encoding="utf-8") as f:
            f.write(DeployTemplates.get_workflow_yml())

        # 4. Create build/README.md
        with open("build/README.md", "w", encoding="utf-8") as f:
            f.write(DeployTemplates.get_readme_md(username))

    console.print("\n[bold green]✓[/bold green] [cyan]build/assets/profile.svg[/cyan] successfully built!")
    console.print("[bold green]✓[/bold green] Tailored [magenta]build/generate_profile.py[/magenta] synthesized!")
    console.print("[bold green]✓[/bold green] [yellow]build/.github/workflows/generate_profile.yml[/yellow] & [yellow]build/README.md[/yellow] ready!")

    # Automated Deployment to Target Repository
    auto_push = Confirm.ask(f"\n[bold magenta]🚀 Automatically push build/ assets to [cyan]{repo_url}[/cyan]?[/bold magenta]", default=True)
    if auto_push:
        with console.status("[bold green]Pushing build/ to your GitHub profile repository...[/bold green]", spinner="arrow3"):
            success = GitOps.deploy_build_to_repo(repo_url)
            if success:
                console.print("\n[bold green]🎉 SUCCESS! Your profile is now LIVE on GitHub![/bold green]")
            else:
                console.print("\n[yellow]💡 You can manually push the contents of the 'build/' folder to your repository anytime.[/yellow]")

    # Live Preview
    open_browser = Confirm.ask("\n[bold cyan]👀 Open live preview in browser?[/bold cyan]", default=True)
    if open_browser:
        svg_path = os.path.abspath("build/assets/profile.svg")
        webbrowser.open(f"file://{svg_path}")

def cmd_preview():
    """Opens generated build/assets/profile.svg in default web browser."""
    svg_path = os.path.abspath("build/assets/profile.svg")
    if not os.path.exists(svg_path):
        console.print("[yellow]build/assets/profile.svg not found. Run 'python main.py' first.[/yellow]")
        return
    webbrowser.open(f"file://{svg_path}")
    console.print(f"[bold green]✓ Opened in browser:[/bold green] {svg_path}")

def main():
    parser = argparse.ArgumentParser(
        description="GitFlex: Next-Gen Modular Animated SVG Profile & CV Engine for GitHub",
        prog="gitflex"
    )
    subparsers = parser.add_subparsers(dest="command", help="GitFlex Commands")

    subparsers.add_parser("init", help="Interactive setup wizard & build generator")
    subparsers.add_parser("preview", help="Open live SVG preview in browser")

    args = parser.parse_args()

    if args.command == "init" or len(sys.argv) == 1:
        cmd_init()
    elif args.command == "preview":
        cmd_preview()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
