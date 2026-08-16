import random
from GitFlex.modules.widgets.base import BaseWidget

class ParticlesWidget(BaseWidget):
    """Original 32 Floating Background Particles."""
    id = "particles"
    name = "Background Floating Particles"
    description = "Dynamic floating glowing space particles in the canvas background"
    default_enabled = True

    def render(self, context: dict, theme, layout_box: dict) -> str:
        rng = random.Random(42)
        particles_svg = ""
        particle_colors = theme.particle_colors
        
        for i in range(32):
            cx = rng.randint(20, 830)
            cy = rng.randint(20, 630)
            r = round(rng.uniform(0.8, 2.2), 1)
            color = rng.choice(particle_colors)
            dur_move = rng.randint(6, 15)
            dur_opacity = rng.randint(5, 12)
            anim_type = rng.choice(["cx", "cy"])
            if anim_type == "cx":
                delta = rng.randint(15, 30)
                anim_vals = f"{cx};{cx + delta if cx + delta < 830 else cx - delta};{cx}"
            else:
                delta = rng.randint(15, 30)
                anim_vals = f"{cy};{cy + delta if cy + delta < 630 else cy - delta};{cy}"
            particles_svg += f'''
    <circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}">
      <animate attributeName="{anim_type}" values="{anim_vals}" dur="{dur_move}s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.15;0.85;0.15" dur="{dur_opacity}s" repeatCount="indefinite" />
    </circle>'''

        return f'''  <!-- Floating Background Particles -->
  <g opacity="0.38">
    {particles_svg}
  </g>'''
