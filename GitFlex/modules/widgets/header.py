import html
from GitFlex.modules.widgets.base import BaseWidget
from GitFlex.services.icons import get_as_base64

class HeaderWidget(BaseWidget):
    """Original Header: Rotating Neon Glow Avatar + Shimmering Name + Subtitle."""
    id = "header"
    name = "Header Card"
    description = "Avatar with spinning glowing neon ring, shimmering gradient name and subtitle"
    default_enabled = True

    def render(self, context: dict, theme, layout_box: dict) -> str:
        user = context.get("user", {})
        username = context.get("username", "")
        name = html.escape(self.config.get("name") or user.get("name") or username)
        bio = html.escape(self.config.get("bio") or user.get("bio") or "")
        
        avatar_raw = user.get("avatar_url", "")
        avatar_base64 = get_as_base64(avatar_raw) if avatar_raw else ""
        avatar_url = html.escape(avatar_base64)

        return f'''  <!-- Header Section -->
  <g transform="translate(0, 0)">
    <!-- Avatar with Glow & Rotating Neon Ring -->
    <circle cx="95" cy="95" r="47" fill="none" class="avatar-glow" />
    <circle cx="95" cy="95" r="47" fill="none" class="avatar-glow" transform="rotate(180 95 95)" />
    <image x="48" y="48" width="94" height="94" href="{avatar_url}" clip-path="url(#avatarCircle)" />
    
    <!-- Profile Info -->
    <text x="165" y="88" class="title">{name}</text>
    <text x="165" y="115" class="subtitle">{bio}</text>
  </g>'''
