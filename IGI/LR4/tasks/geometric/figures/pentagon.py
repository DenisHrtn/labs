import matplotlib.pyplot as plt
import numpy as np
import math

from tasks.geometric.abstraction.geometric_figure import GeometricFigure
from tasks.geometric.figure_color import FigureColor


class Pentagon(GeometricFigure):
    """Класс Правильный пятиугольник."""
    name = "Пятиугольник"

    def __init__(self, side: float, color: str):
        self.side = side
        self.color = FigureColor(color)

    def area(self):
        return (5 * self.side ** 2) / (4 * math.tan(math.pi / 5))

    @classmethod
    def get_name(cls):
        return cls.name

    def __str__(self):
        return "{} {} цвета со стороной {}. Площадь: {:.2f}".format(
            self.get_name(), self.color.color, self.side, self.area()
        )

    def draw(self, text=""):
        fig, ax = plt.subplots()
        angles = np.linspace(0, 2 * np.pi, 6)
        x = self.side * np.cos(angles)
        y = self.side * np.sin(angles)
        ax.fill(x, y, color=self.color.color, alpha=0.5)
        plt.xlim(-self.side, self.side)
        plt.ylim(-self.side, self.side)
        plt.text(0, 0, text, ha='center', va='center', fontsize=12)
        plt.grid()
        plt.savefig("pentagon.png")
        plt.show()
