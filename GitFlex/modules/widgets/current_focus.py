import html
from GitFlex.modules.widgets.base import BaseWidget

class CurrentFocusWidget(BaseWidget):
    """Original Current Focus card positioned inside the Left Side (translate 0, 220)."""
    id = "current_focus"
    name = "Current Focus Active Project"
    description = "Displays the latest updated project with live pulsing radar dot"
    default_enabled = True

    def render(self, context: dict, theme, layout_box: dict) -> str:
        stats = context.get("stats", {})
        recent = stats.get("recent_focus")
        username = context.get("username", "")

        if not recent:
            return ""

        repo_name_raw = recent.get("name", "")
        repo_name = html.escape(repo_name_raw)
        repo_lang = html.escape(recent.get("language", "") or "Unknown")
        repo_updated = recent.get("relative_time", "Recently")

        if len(repo_name) > 24:
            repo_name = repo_name[:21] + "..."

        return f'''  <!-- Left Side: Recent Focus Card -->
  <g transform="translate(45, 170)">
    <a href="https://github.com/{username}/{repo_name_raw}" target="_blank" style="text-decoration: none;">
      <g transform="translate(0, 220)">
        <rect width="380" height="85" rx="16" class="card-bg" />
        
        <!-- Pulsing Green Dot -->
        <circle cx="26" cy="24" r="4.5" fill="#38ef7d" />
        <circle cx="26" cy="24" r="4.5" fill="none" stroke="#38ef7d" stroke-width="1.8">
          <animate attributeName="r" values="4.5;10" dur="1.8s" repeatCount="indefinite" />
          <animate attributeName="opacity" values="0.8;0" dur="1.8s" repeatCount="indefinite" />
        </circle>
        
        <text x="40" y="28" class="stat-lbl" font-weight="700" letter-spacing="0.5px">CURRENT FOCUS</text>
        <text x="20" y="50" font-size="15px" font-weight="700" fill="#ffffff">{repo_name}</text>
        <text x="20" y="68" font-size="11px" font-weight="400" fill="#94a3b8">{repo_lang} • Active {repo_updated}</text>
      </g>
    </a>
  </g>'''
