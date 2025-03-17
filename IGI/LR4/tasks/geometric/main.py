from tasks.geometric.figures.rectangle import Rectangle
from tasks.geometric.figures.pentagon import Pentagon


def main():
    shape_type = input("Выберите фигуру (прямоугольник/пятиугольник): ").strip().lower()
    color = input("Введите цвет фигуры: ").strip().lower()
    text = input("Введите текст для подписи фигуры: ")

    if shape_type == "прямоугольник":
        width = float(input("Введите ширину: "))
        height = float(input("Введите высоту: "))
        rectangle = Rectangle(width, height, color)
        print(rectangle)
        rectangle.draw(text)

    elif shape_type == "пятиугольник":
        side = float(input("Введите длину стороны: "))
        pentagon = Pentagon(side, color)
        print(pentagon)
        pentagon.draw(text)

    else:
        print("Ошибка! Неизвестная фигура.")


if __name__ == "__main__":
    main()
