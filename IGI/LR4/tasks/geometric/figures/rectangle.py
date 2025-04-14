import matplotlib.pyplot as plt

from tasks.geometric.abstraction.geometric_figure import GeometricFigure
from tasks.geometric.figure_color import FigureColor


class Rectangle(GeometricFigure):
    name = "Прямоугольник"

    def __init__(self, width: float, height: float, color: str):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self):
        return self.width * self.height

    @classmethod
    def get_name(cls):
        return cls.name

    def __str__(self):
        return "{} {} цвета шириной {} и высотой {}. Площадь: {:.2f}".format(
            self.get_name(), self.color.color, self.width, self.height, self.area()
        )

    def draw(self, text=""):
        fig, ax = plt.subplots()
        rect = plt.Rectangle((0, 0), self.width, self.height, color=self.color.color, alpha=0.5)
        ax.add_patch(rect)
        plt.xlim(-1, self.width + 1)
        plt.ylim(-1, self.height + 1)
        plt.gca().set_aspect('equal')
        plt.text(self.width / 2, self.height / 2, text, ha='center', va='center', fontsize=12)
        plt.grid()
        plt.savefig("rectangle.png")
        plt.close(fig)

