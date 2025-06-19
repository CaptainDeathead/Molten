import pygame as pg

from css.stylesheet import Stylesheet
from css.theme import Theme

from UI.element import Element
from UI.label import Label

from typing import Dict

class RootElement(Element):
    def __init__(self) -> None:
        super().__init__(parent=self)

class UIManager:
    def __init__(self) -> None:
        self.root_element: RootElement = RootElement()
        self.base_styles = Theme()

    def add_element(self, element: Element) -> None:
        self.root_element.children.append(element)

    def update(self) -> None:
        self.root_element.master_update()
        
        self.draw()

    def draw(self) -> None:
        self.root_element.master_draw()

    """Elements"""

    def Label(self, styles: Stylesheet | Dict, text: str) -> Label:
        label = Label(self.root_element, styles, text)
        self.add_element(label)

        return label