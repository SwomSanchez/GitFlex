from GitFlex.modules.themes import get_theme
from GitFlex.modules.widgets import get_widget
from GitFlex.config import DEFAULT_CONFIG

class GitFlexEngine:
    """GitFlex Core SVG Render Engine."""

    def __init__(self, config: dict = None):
        self.config = config or DEFAULT_CONFIG

    def render_svg(self, context: dict) -> str:
        """Combines all plug-and-play widgets and selected theme to generate the SVG output."""
        theme_id = self.config.get("theme", "cyberpunk_nebula")
        theme_overrides = self.config.get("theme_overrides", {})
        theme = get_theme(theme_id, theme_overrides)

        width = 850
        height = 650

        # Context enrichment
        context["username"] = self.config.get("username", "")

        # Collect and render widgets
        widget_configs = self.config.get("widgets", [])
        rendered_widgets = []
        custom_styles = []
        custom_defs = []

        for w_conf in widget_configs:
            if not w_conf.get("enabled", True):
                continue
            
            widget_id = w_conf.get("id")
            widget = get_widget(widget_id, w_conf)
            if not widget:
                continue

            rendered_svg = widget.render(context, theme, {})
            if rendered_svg:
                rendered_widgets.append(rendered_svg)

            styles = widget.get_styles(theme)
            if styles:
                custom_styles.append(styles)

            defs = widget.get_defs(theme)
            if defs:
                custom_defs.append(defs)

        # Combined CSS & Defs
        all_css = theme.get_css() + "\n" + "\n".join(custom_styles)
        all_defs = theme.get_defs() + "\n" + "\n".join(custom_defs)
        all_content = "\n\n".join(rendered_widgets)

        svg_document = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    {all_defs}
  </defs>

  <style>
    {all_css}
  </style>

  <!-- Background Layer -->
  <rect width="850" height="650" rx="24" fill="url(#bgGrad)" />
  <rect width="850" height="650" rx="24" fill="url(#glowPurple)" class="pulse-glow" />
  <rect width="850" height="650" rx="24" fill="url(#glowCyan)" class="pulse-glow" />
  <rect width="850" height="650" rx="24" fill="url(#glowCenter)" class="pulse-glow" />
  <rect width="848" height="648" x="1" y="1" rx="23" fill="none" stroke="rgba(255, 255, 255, 0.07)" stroke-width="2" />

{all_content}
</svg>'''
        return svg_document
