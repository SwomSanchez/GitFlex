import json
import os

DEFAULT_CONFIG = {
    "username": "",
    "name": "",
    "bio": "",
    "theme": "cyberpunk_nebula",
    "theme_overrides": {},
    "layout": {
        "width": 850,
        "height": 650,
    },
    "widgets": [
        {"id": "particles", "enabled": True, "count": 32},
        {"id": "header", "enabled": True},
        {"id": "stats", "enabled": True},
        {"id": "languages", "enabled": True, "limit": 5},
        {"id": "current_focus", "enabled": True},
        {
            "id": "tech_stack",
            "enabled": True,
            "items": [],
        },
    ],
}

class ConfigManager:
    """Manages reading, writing, and validating the gitflex.json configuration file."""
    
    def __init__(self, config_path: str = "gitflex.json"):
        self.config_path = config_path

    def exists(self) -> bool:
        return os.path.exists(self.config_path)

    def load(self) -> dict:
        if not self.exists():
            return DEFAULT_CONFIG.copy()
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"Warning: Could not read config, using default ({e})")
            return DEFAULT_CONFIG.copy()

    def save(self, config_data: dict):
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(config_data, f, indent=2, ensure_ascii=False)
