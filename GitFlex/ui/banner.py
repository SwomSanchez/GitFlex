from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

BANNER_ASCII = r"""
   ██████╗ ██╗████████╗███████╗██╗     ███████╗██╗  ██╗
  ██╔════╝ ██║╚══██╔══╝██╔════╝██║     ██╔════╝╚██╗██╔╝
  ██║  ███╗██║   ██║   █████╗  ██║     █████╗   ╚███╔╝ 
  ██║   ██║██║   ██║   ██╔══╝  ██║     ██╔══╝   ██╔██╗ 
  ╚██████╔╝██║   ██║   ██║     ███████╗███████╗██╔╝ ██╗
   ╚═════╝ ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝
"""

def print_banner():
    banner_text = Text(BANNER_ASCII, style="bold magenta")
    subtitle = Text("✨ Next-Gen Modular Animated SVG Profile & CV Engine ✨\n", style="bold cyan")
    subtitle.append("⚡ Built for Developers by SwomSanchez ⚡", style="dim green")
    
    panel = Panel(
        Text.assemble(banner_text, "\n", subtitle),
        border_style="bright_magenta",
        padding=(0, 2),
    )
    console.print(panel)
