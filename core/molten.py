import pygame as pg
import sys

pg.init()

from core.UI.ui_manager import UIManager

class Window:
    FPS: int = 60

    def __init__(self, width: int, height: int, title: str) -> None:
        self.width: int = width
        self.height: int = height
        self.title: str = title

        self.ui_manager: UIManager = UIManager()

        self.clock: pg.time.Clock = pg.time.Clock()
        self.running: bool = True

    def main(self) -> None:
        while self.running:
            dt = self.clock.tick(self.FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.ui_manager.update()

            pg.display.flip()

        pg.quit()
        sys.exit(0)

if __name__ == "__main__":
    window = Window(400, 400, "Molten")
    window.ui_manager.add_element()