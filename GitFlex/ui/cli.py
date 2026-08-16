import os
import sys
import time
import argparse
import webbrowser
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich.text import Text
from rich.align import Align

from GitFlex.ui.banner import print_banner
from GitFlex.services.github import GitHubProvider
from GitFlex.engine.renderer import GitFlexEngine
from GitFlex.engine.synthesizer import ScriptSynthesizer
from GitFlex.services.templates import DeployTemplates
from GitFlex.services.git_deploy import GitOps
from GitFlex.modules.themes import list_themes
from GitFlex.services.icons import list_local_icons

console = Console()

def cmd_init():
    """Ultra-Premium Interactive Cyberpunk Setup Wizard."""
    console.clear()
    print_banner()

    console.print()
    setup_panel = Panel(
        Align.center(
            Text.from_markup(
                "[bold cyan]Welcome to the GitFlex Configuration Studio![/bold cyan]\n"
                "[dim]Design your dynamic animated GitHub profile in seconds with live API telemetry.[/dim]"
            )
        ),
        border_style="cyan",
        padding=(0, 2),
    )
    console.print(setup_panel)
    console.print()

    # Step 1: User Identity
    console.print("[bold bright_magenta]━━━ STEP 1 / 4: DEVELOPER IDENTITY ━━━━━━━━━━━━━━━━━━━━━━[/bold bright_magenta]")
    username = Prompt.ask(
        "\n[bold green]?[/bold green] [bold white]GitHub Username[/bold white]"
    ).strip()

    if not username:
        console.print("[bold red]✖ Error: GitHub username cannot be empty![/bold red]")
        return

    default_repo = f"https://github.com/{username}/{username}.git"
    repo_url = Prompt.ask(
        "[bold green]?[/bold green] [bold white]Target Profile Repository URL[/bold white]",
        default=default_repo
    ).strip()

    name = Prompt.ask(
        "[bold green]?[/bold green] [bold white]Display Name[/bold white] [dim](Leave empty to use GitHub name)[/dim]",
        default=""
    ).strip()

    bio = Prompt.ask(
        "[bold green]?[/bold green] [bold white]Bio / Subtitle[/bold white] [dim](Leave empty to use GitHub bio)[/dim]",
        default=""
    ).strip()

    # Step 2: Theme Selection
    console.print("\n[bold bright_magenta]━━━ STEP 2 / 4: THEME & PALETTE ENGINE ━━━━━━━━━━━━━━━━━━━[/bold bright_magenta]\n")
    themes = list_themes()

    theme_cards = [
        {"num": "1", "name": "Cyberpunk Nebula", "badge": "[bold magenta]● NEON PURPLE / GREEN[/bold magenta]", "desc": "Deep space canvas with glowing purple nebula & neon emerald auroras"},
        {"num": "2", "name": "Midnight Sapphire", "badge": "[bold cyan]● OCEANIC SAPPHIRE[/bold cyan]", "desc": "Deep oceanic blues with high-tech electric cyan highlights"},
        {"num": "3", "name": "Sunset Crimson", "badge": "[bold red]● AMBER SUNSET[/bold red]", "desc": "Warm dusk gradients with vibrant pink & golden amber glow"},
        {"num": "4", "name": "Matrix Emerald", "badge": "[bold green]● TERMINAL EMERALD[/bold green]", "desc": "Cyberpunk terminal black with electric neon emerald lasers"}
    ]

    for item in theme_cards:
        console.print(f"  [bold bright_yellow][{item['num']}][/bold bright_yellow] [bold white]{item['name']:<20}[/bold white] {item['badge']}")
        console.print(f"      [dim]{item['desc']}[/dim]\n")

    theme_choice = Prompt.ask(
        "[bold green]?[/bold green] [bold white]Select Theme Number[/bold white]",
        default="1"
    ).strip()
    try:
        chosen_theme = themes[int(theme_choice) - 1]["id"]
        chosen_theme_name = themes[int(theme_choice) - 1]["name"]
    except Exception:
        chosen_theme = "cyberpunk_nebula"
        chosen_theme_name = "Cyberpunk Nebula"

    console.print(f"[dim]Selected theme:[/dim] [bold cyan]{chosen_theme_name}[/bold cyan]")

    # Step 3: Tech Stack
    console.print("\n[bold bright_magenta]━━━ STEP 3 / 4: TECH MATRIX & CUSTOM ICONS ━━━━━━━━━━━━━[/bold bright_magenta]")
    console.print("[dim]Popular: python, javascript, typescript, react, csharp, dotnet, nodejs, docker, git, go, rust[/dim]\n")
    
    available_icons = list_local_icons()
    if available_icons:
        console.print(f"[bold yellow]📁 Detected Local Icons in GitFlex/icons/:[/bold yellow] [dim cyan]{', '.join(available_icons)}[/dim cyan]\n")
        default_tech = ", ".join(available_icons[:8])
    else:
        default_tech = ""

    tech_input = Prompt.ask(
        "[bold green]?[/bold green] [bold white]Tech Stack Chips[/bold white] [dim](Enter tech names comma-separated)[/dim]",
        default=default_tech
    ).strip()
    tech_items = [t.strip().lower() for t in tech_input.split(",") if t.strip()]

    # Configuration Assembly
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

    # Step 4: Live Telemetry & Build Pipeline
    console.print("\n[bold bright_magenta]━━━ STEP 4 / 4: TELEMETRY & BUILD PIPELINE ━━━━━━━━━━━━━━[/bold bright_magenta]\n")

    user_data = {}
    repos_data = []
    stats_data = {}

    with Progress(
        SpinnerColumn(spinner_name="dots12", style="bold cyan"),
        TextColumn("[bold cyan]{task.description}[/bold cyan]"),
        BarColumn(bar_width=40, style="purple", complete_style="bold green"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        console=console
    ) as progress:
        
        task1 = progress.add_task("Connecting to GitHub REST API...", total=100)
        provider = GitHubProvider(username)
        
        # Step 1: User Profile
        progress.update(task1, advance=25, description="Fetching GitHub profile metadata...")
        time.sleep(0.3)
        try:
            user_data = provider.fetch_user_data()
        except Exception as e:
            user_data = {"name": name, "bio": bio, "public_repos": 0, "followers": 0}
        
        # Step 2: Repositories
        progress.update(task1, advance=25, description="Scanning repository metrics & activity...")
        time.sleep(0.4)
        try:
            repos_data = provider.fetch_repositories()
        except Exception as e:
            repos_data = []

        # Step 3: Math & Calculations
        progress.update(task1, advance=25, description="Computing slot-machine stats & language ratios...")
        time.sleep(0.3)
        stats_data = provider.calculate_stats(user_data, repos_data)

        # Step 4: Asset Generation
        progress.update(task1, advance=25, description="Compiling SVG canvas & synthesizing standalone Action...")
        
        context = {
            "user": user_data,
            "repos": repos_data,
            "stats": stats_data,
        }

        # 1. Compile SVG
        engine = GitFlexEngine(config)
        svg_content = engine.render_svg(context)

        os.makedirs("build/assets", exist_ok=True)
        with open("build/assets/profile.svg", "w", encoding="utf-8") as f:
            f.write(svg_content)

        # 2. Synthesize Autonomous Action Script
        custom_script = ScriptSynthesizer.generate_standalone_script(config)
        with open("build/generate_profile.py", "w", encoding="utf-8") as f:
            f.write(custom_script)

        # 3. Create Workflow YAML
        os.makedirs("build/.github/workflows", exist_ok=True)
        with open("build/.github/workflows/generate_profile.yml", "w", encoding="utf-8") as f:
            f.write(DeployTemplates.get_workflow_yml())

        # 4. Create README.md
        with open("build/README.md", "w", encoding="utf-8") as f:
            f.write(DeployTemplates.get_readme_md(username))

        time.sleep(0.2)

    console.print()
    
    # Telemetry Summary Table
    summary_table = Table(title="[bold green]✓ Live GitHub Telemetry Summary[/bold green]", border_style="bright_cyan")
    summary_table.add_column("Metric", style="bold white")
    summary_table.add_column("Value", style="bold yellow")
    
    summary_table.add_row("Repositories", str(stats_data.get("public_repos", 0)))
    summary_table.add_row("Total Stars", str(stats_data.get("total_stars", 0)))
    summary_table.add_row("Followers", str(stats_data.get("followers", 0)))
    summary_table.add_row("Forks Generated", str(stats_data.get("total_forks", 0)))
    
    top_langs = ", ".join([f"{l['name']} ({l['percentage']:.1f}%)" for l in stats_data.get("top_languages", [])[:3]]) or "None"
    summary_table.add_row("Top Languages", top_langs)

    recent_focus = stats_data.get("recent_focus")
    summary_table.add_row("Current Focus", recent_focus.get("name", "None") if recent_focus else "None")

    console.print(summary_table)

    # Success Notice
    success_box = Panel(
        Text.from_markup(
            "[bold green]✨ All assets successfully compiled into isolated [cyan]build/[/cyan] directory![/bold green]\n\n"
            "  [bold white]•[/bold white] [cyan]build/assets/profile.svg[/cyan] [dim](Animated SVG profile card)[/dim]\n"
            "  [bold white]•[/bold white] [cyan]build/generate_profile.py[/cyan] [dim](Zero-dependency Actions script)[/dim]\n"
            "  [bold white]•[/bold white] [cyan]build/.github/workflows/generate_profile.yml[/cyan] [dim](Daily auto-sync workflow)[/dim]\n"
            "  [bold white]•[/bold white] [cyan]build/README.md[/cyan] [dim](Profile README display)[/dim]"
        ),
        title="[bold bright_green]BUILD COMPLETE[/bold bright_green]",
        border_style="bright_green",
        padding=(1, 2)
    )
    console.print(success_box)

    # Automated Deployment
    console.print()
    auto_push = Confirm.ask(
        f"[bold magenta]🚀 Automatically push build/ assets to [cyan]{repo_url}[/cyan]?[/bold magenta]",
        default=True
    )
    if auto_push:
        with console.status("[bold green]Executing isolated GitOps push from build/ to target repo...[/bold green]", spinner="aesthetic"):
            success = GitOps.deploy_build_to_repo(repo_url)
            if success:
                console.print("\n[bold bright_green]🎉 SUCCESS! Your profile is now LIVE on GitHub![/bold bright_green]")
            else:
                console.print("\n[yellow]💡 Tip: You can manually push the contents of 'build/' anytime.[/yellow]")

    # Live Preview
    open_browser = Confirm.ask(
        "\n[bold cyan]👀 Open live animated SVG preview in browser?[/bold cyan]",
        default=True
    )
    if open_browser:
        svg_path = os.path.abspath("build/assets/profile.svg")
        webbrowser.open(f"file://{svg_path}")
        console.print(f"[bold green]✓ Opened live preview:[/bold green] [dim]{svg_path}[/dim]\n")

def cmd_preview():
    """Opens generated build/assets/profile.svg in default web browser."""
    svg_path = os.path.abspath("build/assets/profile.svg")
    if not os.path.exists(svg_path):
        console.print("[bold red]✖ Error:[/bold red] [yellow]build/assets/profile.svg not found. Run 'python main.py' first.[/yellow]")
        return
    webbrowser.open(f"file://{svg_path}")
    console.print(f"[bold green]✓ Opened live preview in browser:[/bold green] [cyan]{svg_path}[/cyan]")

def main():
    parser = argparse.ArgumentParser(
        description="GitFlex: Next-Gen Modular Animated SVG Profile & CV Engine for GitHub",
        prog="gitflex"
    )
    subparsers = parser.add_subparsers(dest="command", help="GitFlex Commands")

    subparsers.add_parser("init", help="Launch the interactive setup wizard")
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
