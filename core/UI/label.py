import pygame as pg

from core.css.stylesheet import Stylesheet

class Label:
    surface: pg.Surface

    x: int
    y: int

    def __init__(self, master_surface: pg.Surface, text: str, styles: Stylesheet) -> None:
        self.master_surface = master_surface

        self.text: str = text
        self.styles: Stylesheet = styles

        self.fg_color: pg.Color = self.styles.get_style("fg_color")
        self.bg_color: pg.Color = self.styles.get_style("bg_color")
        self.font: pg.Font = self.styles.get_style("font")

        self.align: bool = self.styles.get_style("align") == "center"

        self.position()
        self.rebuild()

    def position(self) -> None:
        self.x = 0
        self.y = 0
        
    def rebuild(self) -> None:
        self.surface = self.font.render(self.text, True, self.fg_color, self.bg_color)

        if self.align == "center": self.x = -self.surface.width / 2

    def update(self) -> None:
        ...

    def draw(self, shunt_x: int, shunt_y: int) -> None:
        self.master_surface.blit(self.surface, self.x + shunt_x, self.y + shunt_y)