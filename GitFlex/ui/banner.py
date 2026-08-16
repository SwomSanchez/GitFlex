import time
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.align import Align

console = Console()

BANNER_ASCII = r"""
   ██████╗ ██╗████████╗███████╗██╗     ███████╗██╗  ██╗
  ██╔════╝ ██║╚══██╔══╝██╔════╝██║     ██╔════╝╚██╗██╔╝
  ██║  ███╗██║   ██║   █████╗  ██║     █████╗   ╚███╔╝ 
  ██║   ██║██║   ██║   ██╔══╝  ██║     ██╔══╝   ██╔██╗ 
  ╚██████╔╝██║   ██║   ██║     ███████╗███████╗██╔╝ ██╗
   ╚═════╝ ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝
"""

def print_banner(animated: bool = False):
    """Renders a futuristic cyber cyberpunk banner with optional typewriter/gradient intro."""
    banner_lines = BANNER_ASCII.strip().split("\n")
    colors = ["bold magenta", "bold purple", "bold violet", "bold cyan", "bold bright_cyan"]
    
    table = Table.grid(padding=(0, 0))
    table.add_column(justify="center")
    
    for idx, line in enumerate(banner_lines):
        color = colors[idx % len(colors)]
        table.add_row(Text(line, style=color))

    subtitle = Text()
    subtitle.append("\n⚡ ", style="bold yellow")
    subtitle.append("NEXT-GEN MODULAR ANIMATED SVG PROFILE & CV ENGINE", style="bold cyan")
    subtitle.append(" ⚡\n", style="bold yellow")
    subtitle.append("Created with passion by ", style="dim white")
    subtitle.append("SwomSanchez", style="bold green")
    subtitle.append(" | Powered by GitFlex Core\n", style="dim cyan")
    
    table.add_row(subtitle)

    panel = Panel(
        Align.center(table),
        border_style="bright_magenta",
        padding=(1, 3),
        title="[bold bright_yellow]◆ G I T F L E X   E N G I N E ◆[/bold bright_yellow]",
        subtitle="[dim cyan]v1.0.0 Cyberpunk Edition[/dim cyan]",
        subtitle_align="right"
    )
    console.print(panel)
