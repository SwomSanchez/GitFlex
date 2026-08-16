import html
from GitFlex.modules.widgets.base import BaseWidget

class LanguagesWidget(BaseWidget):
    """Original Languages Widget with Code Icon and Top Languages header."""
    id = "languages"
    name = "Neon Language Breakdown"
    description = "Animated progress bars showing top language distribution"
    default_enabled = True

    def render(self, context: dict, theme, layout_box: dict) -> str:
        stats = context.get("stats", {})
        lang_stats = stats.get("top_languages", [])
        limit = self.config.get("limit", 5)
        lang_stats = lang_stats[:limit]

        bars_svg = ""
        by = 50
        colors = theme.lang_colors

        for i, lang_item in enumerate(lang_stats):
            escaped_lang = html.escape(lang_item["name"])
            pct = lang_item["percentage"]
            color = colors[i % len(colors)]
            bar_width = max(pct * 3.3, 8)  # Max width is 330px
            
            bars_svg += f'''
        <g transform="translate(460, {by})">
          <text x="0" y="15" class="card-desc" font-weight="600">{escaped_lang}</text>
          <text x="330" y="15" class="card-desc" font-weight="700" fill="{color}">{pct:.1f}%</text>
          <rect x="0" y="25" width="330" height="8" rx="4" fill="rgba(255, 255, 255, 0.05)" />
          <rect x="0" y="25" width="{bar_width}" height="8" rx="4" fill="{color}">
            <animate attributeName="width" from="0" to="{bar_width}" dur="1.2s" fill="freeze" />
          </rect>
        </g>'''
            by += 45

        return f'''  <!-- Right Side: Top Languages -->
  <g transform="translate(0, 170)">
    <!-- Section Title with Code Icon -->
    <g transform="translate(460, 3)" stroke="#ffffff" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0.9">
      <path d="M16 18l6-6-6-6M8 6L2 12l6 6"/>
    </g>
    <text x="492" y="20" class="section-title">Top Languages</text>
    {bars_svg}
  </g>'''
