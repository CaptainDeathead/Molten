import pygame as pg

from typing import Dict
from typing_extensions import Self

class Stylesheet:
    def __init__(self, default_styles: Dict[str, any], styles: Dict[str, any]) -> None:
        self.default_styles = default_styles
        self.styles = styles

    def get(self, style_name: str) -> any:
        # TODO: THIS IS DANGEROUS! THERE IS A POSSIBLE EXPLOIT WITH THIS THAT WOULD NEED TO BE FIXED
        #       A MALICOUS INJECTION COULD HAPPEN IF SOMEONE CHANGED style_name TO SOMETHING SUCH AS "self"

        if hasattr(self, style_name):
            return getattr(self, style_name)
        else:
            return None

    def get_style(self, style_name: str) -> any:
        style = self.styles.get(style_name)

        if style is None:
            if self.default_styles.get(style_name) is None:
                raise Exception(f"{style_name} not found in default styles.")
            
            style = self.default_styles.get(style_name)

        return style