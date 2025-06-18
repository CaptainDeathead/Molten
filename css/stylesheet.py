import pygame as pg

from typing import Dict

class Stylesheet:
    def __init__(self, default_styles: Dict[str, any], styles: Dict[str, any]) -> None:
        self.default_styles = default_styles
        self.styles = styles

    def get_style(self, style_name: str) -> any:
        style = self.styles.get(style_name)

        if style is None:
            if self.default_styles.get(style_name) is None:
                raise Exception(f"{style_name} not found in default styles.")
            
            style = self.default_styles.get(style_name)

        return style