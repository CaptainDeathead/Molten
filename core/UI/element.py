import pygame as pg

from typing import List, Tuple
from typing_extensions import Self

class Element:
    surface: pg.Surface

    def __init__(self, parent: Self) -> None:
        self.parent = parent
        self.children: List[Self] = []

    @property
    def width(self) -> int:
        if hasattr(self, "surface"):
            if self.surface is not None:
                return self.surafce.width

        return 0

    @property
    def height(self) -> int:
        if hasattr(self, "surface"):
            if self.surface is not None:
                return self.surafce.height

        return 0

    def add_child(self, child: Self) -> None:
        self.children.append(child)

    def remove_child(self, child: Self) -> None:
        self.children.remove(child)

    def master_update(self) -> None:
        self.update()

        for child in self.children:
            child.master_update()

    def master_draw(self, shunt_x: int, shunt_y: int) -> Tuple[int, int]:
        self.draw(shunt_x, shunt_y)

        shunt_x += self.width
        shunt_y += self.height

        for child in self.children:
            shunt_x, shunt_y = child.master_draw(shunt_x, shunt_y)

        return shunt_x, shunt_y