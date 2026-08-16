from abc import ABC, abstractmethod

class BaseWidget(ABC):
    """
    Abstract Base Class for all modular GitFlex widgets.
    Every profile visual component inherits from this class.
    """
    id: str = "base_widget"
    name: str = "Base Widget"
    description: str = "Base widget description"
    default_enabled: bool = True

    def __init__(self, config: dict = None):
        self.config = config or {}

    @abstractmethod
    def render(self, context: dict, theme, layout_box: dict) -> str:
        """
        Renders the SVG visual elements for the widget.
        :param context: Enriched GitHub context (user data, repos, stats).
        :param theme: Selected BaseTheme instance.
        :param layout_box: Layout positioning dictionary.
        """
        pass

    def get_styles(self, theme) -> str:
        """Optional widget-specific CSS animation styles."""
        return ""

    def get_defs(self, theme) -> str:
        """Optional widget-specific SVG <defs> elements (filters, clipPaths, gradients)."""
        return ""
