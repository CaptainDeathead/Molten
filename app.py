from core.molten import Window
from core.css.stylesheet import Stylesheet
from core.UI.label import Label

class App:
    def __init__(self) -> None:
        self.window = Window(400, 400, "Molten")

        title_lbl = self.window.ui_manager.Label()
