from abc import ABC

class BaseTheme(ABC):
    """Base class for all GitFlex themes."""
    
    id: str = "base"
    name: str = "Base Theme"
    description: str = "Base theme blueprint"
    
    # Color Palette
    bg_gradient: list = ["#0a0813", "#120e25", "#07050e"]
    glow_colors: list = ["#7f5af0", "#2cb67d"]
    primary_color: str = "#7f5af0"
    accent_color: str = "#2cb67d"
    text_primary: str = "#ffffff"
    text_secondary: str = "#94a3b8"
    
    # Glassmorphism & Card styling
    card_bg: str = "rgba(255, 255, 255, 0.02)"
    card_border: str = "rgba(255, 255, 255, 0.05)"
    card_radius: int = 24
    
    # Particle Colors
    particle_colors: list = ["#7f5af0", "#2cb67d", "#ffffff"]
    
    # Language progress bar neon palette
    lang_colors: list = ["#FF5E97", "#A594F9", "#4DEEEA", "#38EF7D", "#F9D423"]

    def apply_overrides(self, overrides: dict):
        if not overrides:
            return
        for key, value in overrides.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def get_defs(self) -> str:
        """SVG Gradient, Filter and Mask definitions matching exact SwomSanchez signature."""
        return f'''
    <!-- Background Gradients -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{self.bg_gradient[0]}" />
      <stop offset="50%" stop-color="{self.bg_gradient[1]}" />
      <stop offset="100%" stop-color="{self.bg_gradient[2]}" />
    </linearGradient>
    
    <radialGradient id="glowPurple" cx="10%" cy="10%" r="50%">
      <stop offset="0%" stop-color="{self.glow_colors[0]}" stop-opacity="0.15" />
      <stop offset="100%" stop-color="{self.glow_colors[0]}" stop-opacity="0" />
      <animate attributeName="cx" values="10%;25%;10%" dur="12s" repeatCount="indefinite" />
      <animate attributeName="cy" values="10%;25%;10%" dur="14s" repeatCount="indefinite" />
    </radialGradient>
    
    <radialGradient id="glowCyan" cx="90%" cy="90%" r="50%">
      <stop offset="0%" stop-color="{self.glow_colors[1]}" stop-opacity="0.1" />
      <stop offset="100%" stop-color="{self.glow_colors[1]}" stop-opacity="0" />
      <animate attributeName="cx" values="90%;75%;90%" dur="14s" repeatCount="indefinite" />
      <animate attributeName="cy" values="90%;75%;90%" dur="12s" repeatCount="indefinite" />
    </radialGradient>

    <!-- Center Nebula Glow Gradient -->
    <radialGradient id="glowCenter" cx="50%" cy="50%" r="45%">
      <stop offset="0%" stop-color="{self.primary_color}" stop-opacity="0.12" />
      <stop offset="100%" stop-color="{self.primary_color}" stop-opacity="0" />
      <animate attributeName="cx" values="50%;42%;58%;42%;50%" dur="18s" repeatCount="indefinite" />
      <animate attributeName="cy" values="50%;58%;42%;48%;50%" dur="22s" repeatCount="indefinite" />
    </radialGradient>

    <!-- Shimmering Text Gradient -->
    <linearGradient id="textGrad" x1="-150%" y1="0%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="{self.primary_color}" />
      <stop offset="45%" stop-color="{self.primary_color}" />
      <stop offset="50%" stop-color="#ffffff" />
      <stop offset="55%" stop-color="{self.primary_color}" />
      <stop offset="100%" stop-color="{self.primary_color}" />
      <animate attributeName="x1" values="-150%;150%" dur="2.5s" repeatCount="indefinite" />
      <animate attributeName="x2" values="0%;300%" dur="2.5s" repeatCount="indefinite" />
    </linearGradient>

    <!-- Avatar Circle Mask -->
    <clipPath id="avatarCircle">
      <circle cx="95" cy="95" r="45" />
    </clipPath>

    <!-- Digit Clip Path -->
    <clipPath id="digitClip">
      <rect x="-2" y="2" width="22" height="30" />
    </clipPath>

    <!-- Glow Filter -->
    <filter id="glowEffect" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>'''

    def get_css(self) -> str:
        """Original Outfit typography, rotating glow ring, and glassmorphism styles."""
        return f'''
      @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&amp;display=swap');
      
      * {{
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      }}
      
      .title {{
        fill: url(#textGrad);
        font-size: 32px;
        font-weight: 800;
        letter-spacing: -0.5px;
      }}
      
      .subtitle {{
        fill: {self.text_secondary};
        font-size: 15px;
        font-weight: 400;
      }}
      
      .section-title {{
        fill: #ffffff;
        font-size: 18px;
        font-weight: 700;
        letter-spacing: 0.5px;
      }}
      
      .stat-val {{
        fill: {self.text_primary};
        font-size: 24px;
        font-weight: 800;
      }}
      
      .stat-lbl {{
        fill: #64748b;
        font-size: 12px;
        font-weight: 500;
        letter-spacing: 0.5px;
      }}
      
      .card-desc {{
        fill: #e2e8f0;
        font-size: 14px;
      }}
      
      .tech-text {{
        fill: #e2e8f0;
        font-size: 11px;
        font-weight: 600;
      }}
      
      .card-bg {{
        fill: {self.card_bg};
        stroke: {self.card_border};
        stroke-width: 1px;
        transition: fill 0.2s ease, stroke 0.2s ease;
      }}
      
      .card-bg:hover {{
        fill: rgba(255, 255, 255, 0.04);
        stroke: rgba(255, 255, 255, 0.12);
      }}
      
      .tech-chip rect {{
        transition: fill 0.25s ease, stroke 0.25s ease, filter 0.25s ease;
      }}
      
      .tech-chip:hover rect {{
        fill: rgba(255, 255, 255, 0.05);
        stroke: #a78bfa;
        filter: drop-shadow(0px 0px 5px rgba(167, 139, 250, 0.5));
      }}
      
      .avatar-glow {{
        stroke: url(#textGrad);
        stroke-width: 3px;
        stroke-linecap: round;
        animation: rotate-cw 1.5s linear infinite;
        filter: drop-shadow(0px 0px 8px rgba(167, 139, 250, 0.6));
      }}

      /* Animations */
      @keyframes rotate-cw {{
        0% {{
          stroke-dasharray: 20 275;
          stroke-dashoffset: 0;
        }}
        50% {{
          stroke-dasharray: 85 210;
          stroke-dashoffset: -147;
        }}
        100% {{
          stroke-dasharray: 20 275;
          stroke-dashoffset: -295;
        }}
      }}

      @keyframes pulse {{
        0% {{ opacity: 0.8; }}
        50% {{ opacity: 1; }}
        100% {{ opacity: 0.8; }}
      }}
      
      .pulse-glow {{
        animation: pulse 4s infinite ease-in-out;
        transition: filter 0.3s ease, opacity 0.3s ease;
      }}
      
      svg:hover .pulse-glow {{
        filter: brightness(1.3) contrast(1.05);
      }}
    '''
