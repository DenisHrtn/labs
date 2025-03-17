class FigureColor:
    def __init__(self, color: str) -> None:
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color: str):
        self._color = new_color