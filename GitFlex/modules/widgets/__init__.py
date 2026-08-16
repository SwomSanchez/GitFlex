from GitFlex.modules.widgets.particles import ParticlesWidget
from GitFlex.modules.widgets.header import HeaderWidget
from GitFlex.modules.widgets.stats import StatsWidget
from GitFlex.modules.widgets.languages import LanguagesWidget
from GitFlex.modules.widgets.current_focus import CurrentFocusWidget
from GitFlex.modules.widgets.tech_stack import TechStackWidget

_WIDGET_REGISTRY = {
    "particles": ParticlesWidget,
    "header": HeaderWidget,
    "stats": StatsWidget,
    "languages": LanguagesWidget,
    "current_focus": CurrentFocusWidget,
    "tech_stack": TechStackWidget,
}

def get_widget(widget_id: str, config: dict = None):
    """Returns an instance of a widget by its ID."""
    widget_cls = _WIDGET_REGISTRY.get(widget_id)
    if widget_cls:
        return widget_cls(config)
    return None

def list_registered_widgets() -> list:
    """Returns a list of all registered widgets."""
    return [
        {
            "id": wid,
            "name": wcls.name,
            "description": wcls.description,
            "default_enabled": wcls.default_enabled,
        }
        for wid, wcls in _WIDGET_REGISTRY.items()
    ]
