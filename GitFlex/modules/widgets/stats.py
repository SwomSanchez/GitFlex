from GitFlex.modules.widgets.base import BaseWidget

class StatsWidget(BaseWidget):
    """Original Stats Widget: 4 Cards with custom icons and slot machine number roll."""
    id = "stats"
    name = "Animated Rolling Stats"
    description = "Slot machine animated repository, star, follower, and fork counters with SVG icons"
    default_enabled = True

    def _make_animated_number(self, num: int, stat_type: str = "stat") -> str:
        num_str = str(num)
        svg_output = ""
        x_offset = 20
        for idx, digit in enumerate(num_str):
            if digit.isdigit():
                val = int(digit)
                svg_output += f'''
        <g transform="translate({x_offset}, 18)" clip-path="url(#digitClip)">
          <g style="animation: roll-{val} 1.5s cubic-bezier(0.16, 1, 0.3, 1) forwards; animation-delay: {idx * 0.08}s;">
            <text x="0" y="24" class="stat-val">0</text>
            <text x="0" y="54" class="stat-val">1</text>
            <text x="0" y="84" class="stat-val">2</text>
            <text x="0" y="114" class="stat-val">3</text>
            <text x="0" y="144" class="stat-val">4</text>
            <text x="0" y="174" class="stat-val">5</text>
            <text x="0" y="204" class="stat-val">6</text>
            <text x="0" y="234" class="stat-val">7</text>
            <text x="0" y="264" class="stat-val">8</text>
            <text x="0" y="294" class="stat-val">9</text>
          </g>
        </g>'''
                x_offset += 16
            else:
                svg_output += f'<text x="{x_offset}" y="42" class="stat-val">{digit}</text>'
                x_offset += 10
        return svg_output

    def render(self, context: dict, theme, layout_box: dict) -> str:
        stats = context.get("stats", {})
        username = context.get("username", "")
        
        public_repos = stats.get("public_repos", 0)
        total_stars = stats.get("total_stars", 0)
        followers = stats.get("followers", 0)
        total_forks = stats.get("total_forks", 0)

        repos_val = self._make_animated_number(public_repos, "repos")
        stars_val = self._make_animated_number(total_stars, "stars")
        followers_val = self._make_animated_number(followers, "followers")
        forks_val = self._make_animated_number(total_forks, "forks")

        return f'''  <!-- Left Side: Core Stats (Grid Layout) -->
  <g transform="translate(45, 170)">
    <!-- Section Title with Chart Icon -->
    <g transform="translate(0, 3)" stroke="#ffffff" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0.9">
      <path d="M3 3v18h18M7 17v-4M11 17V9M15 17v-6M19 17V5"/>
    </g>
    <text x="32" y="20" class="section-title">GitHub Performance</text>
    
    <!-- Stat 1: Repositories -->
    <a href="https://github.com/{username}?tab=repositories" target="_blank" style="text-decoration: none;">
      <g transform="translate(0, 40)">
        <rect width="180" height="75" rx="16" class="card-bg" />
        <g transform="translate(142, 14)" stroke="#64748b" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0.7">
          <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
        </g>
        {repos_val}
        <text x="20" y="58" class="stat-lbl">REPOSITORIES</text>
      </g>
    </a>
    
    <!-- Stat 2: Total Stars -->
    <g transform="translate(200, 40)">
      <rect width="180" height="75" rx="16" class="card-bg" />
      <g transform="translate(142, 14)" stroke="#a78bfa" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0.8">
        <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
      </g>
      {stars_val}
      <text x="20" y="58" class="stat-lbl" fill="#a78bfa">TOTAL STARS</text>
    </g>
    
    <!-- Stat 3: Followers -->
    <g transform="translate(0, 130)">
      <rect width="180" height="75" rx="16" class="card-bg" />
      <g transform="translate(142, 14)" stroke="#64748b" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0.7">
        <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z"/>
      </g>
      {followers_val}
      <text x="20" y="58" class="stat-lbl">FOLLOWERS</text>
    </g>
    
    <!-- Stat 4: Forks -->
    <g transform="translate(200, 130)">
      <rect width="180" height="75" rx="16" class="card-bg" />
      <g transform="translate(142, 14)" stroke="#64748b" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0.7">
        <path d="M18 18a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM6 6a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM6 18a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM21 21v-6a3 3 0 0 0-3-3h-6M6 6v6"/>
      </g>
      {forks_val}
      <text x="20" y="58" class="stat-lbl">FORKS GENERATED</text>
    </g>
  </g>'''

    def get_styles(self, theme) -> str:
        return '''
      @keyframes roll-0 { from { transform: translateY(0); } to { transform: translateY(0); } }
      @keyframes roll-1 { from { transform: translateY(0); } to { transform: translateY(-30px); } }
      @keyframes roll-2 { from { transform: translateY(0); } to { transform: translateY(-60px); } }
      @keyframes roll-3 { from { transform: translateY(0); } to { transform: translateY(-90px); } }
      @keyframes roll-4 { from { transform: translateY(0); } to { transform: translateY(-120px); } }
      @keyframes roll-5 { from { transform: translateY(0); } to { transform: translateY(-150px); } }
      @keyframes roll-6 { from { transform: translateY(0); } to { transform: translateY(-180px); } }
      @keyframes roll-7 { from { transform: translateY(0); } to { transform: translateY(-210px); } }
      @keyframes roll-8 { from { transform: translateY(0); } to { transform: translateY(-240px); } }
      @keyframes roll-9 { from { transform: translateY(0); } to { transform: translateY(-270px); } }
        '''
