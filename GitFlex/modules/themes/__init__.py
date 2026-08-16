from GitFlex.modules.themes.presets import (
    CyberpunkNebulaTheme,
    MidnightSapphireTheme,
    SunsetCrimsonTheme,
    MatrixEmeraldTheme,
)

_THEMES = {
    "cyberpunk_nebula": CyberpunkNebulaTheme,
    "midnight_sapphire": MidnightSapphireTheme,
    "sunset_crimson": SunsetCrimsonTheme,
    "matrix_emerald": MatrixEmeraldTheme,
}

def get_theme(theme_id: str = "cyberpunk_nebula", overrides: dict = None):
    """Returns a theme instance based on theme_id."""
    theme_cls = _THEMES.get(theme_id, CyberpunkNebulaTheme)
    theme = theme_cls()
    if overrides:
        theme.apply_overrides(overrides)
    return theme

def list_themes() -> list:
    """Returns a list of all available themes."""
    return [{"id": tid, "name": tcls.name, "description": tcls.description} for tid, tcls in _THEMES.items()]
