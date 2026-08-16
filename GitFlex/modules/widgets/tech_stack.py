import html
from GitFlex.modules.widgets.base import BaseWidget
from GitFlex.services.icons import resolve_icon, get_as_base64, list_local_icons

class TechStackWidget(BaseWidget):
    """Original Tech Stack: Reads dynamically from GitFlex/icons/ or user config."""
    id = "tech_stack"
    name = "Tech Stack Grid Matrix"
    description = "Developer skills and technologies chip matrix with interactive glow hover"
    default_enabled = True

    def render(self, context: dict, theme, layout_box: dict) -> str:
        # Config items or scan local GitFlex/icons/ folder
        items = self.config.get("items")
        if not items:
            items = list_local_icons()
        
        if not items:
            return ""

        icons_svg = ""
        x_coords = [45, 240, 435, 630]
        y_coords = [530, 580]
        
        for idx, item_key in enumerate(items[:8]):
            row = idx // 4
            col = idx % 4
            x = x_coords[col]
            y = y_coords[row]
            
            tech_name, icon_src = resolve_icon(item_key)
            escaped_tech_name = html.escape(tech_name)
            base64_icon = get_as_base64(icon_src) if icon_src else ""

            icons_svg += f'''
        <g class="tech-chip" transform="translate({x}, {y})">
          <rect width="175" height="40" rx="12" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1" />
          <image x="12" y="8" width="24" height="24" href="{base64_icon}" />
          <text x="46" y="24" class="tech-text" font-size="13px">{escaped_tech_name}</text>
        </g>'''

        return f'''  <!-- Bottom: Tech Stack -->
  <g transform="translate(0, 0)">
    <!-- Section Title with Layers Icon -->
    <g transform="translate(45, 493)" stroke="#ffffff" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0.9">
      <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
    </g>
    <text x="77" y="510" class="section-title">Tech Stack</text>
    {icons_svg}
  </g>'''
