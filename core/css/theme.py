import pygame as pg

from css.stylesheet import Stylesheet

from typing import Dict

class Theme:
    THEMES: Dict[str, Dict[str, any]] = {
        "dark": {
            "fg_color": pg.Color(255, 255, 255),
            "bg_color": pg.Color(30, 30, 30),
            "font": pg.font.SysFont(None, 30),
            "align": "left"
        }
    }


    def __init__(self, theme: str = "dark") -> Stylesheet:
        if theme not in self.THEMES:
            theme = "dark"

        return Stylesheet({}, self.THEMES[theme])