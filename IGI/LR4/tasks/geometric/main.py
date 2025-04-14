from tasks.geometric.figures.rectangle import Rectangle
from tasks.geometric.figures.pentagon import Pentagon


def main():
    try:
        shape_type = input("Выберите фигуру (прямоугольник/пятиугольник): ").strip().lower()
        if shape_type not in ("прямоугольник", "пятиугольник"):
            raise ValueError("Ошибка! Неизвестная фигура.")

        color = input("Введите цвет фигуры: ").strip().lower()
        text = input("Введите текст для подписи фигуры: ")

        if shape_type == "прямоугольник":
            width = float(input("Введите ширину: "))
            height = float(input("Введите высоту: "))
            if width <= 0 or height <= 0:
                raise ValueError("Ширина и высота должны быть положительными числами.")
            rectangle = Rectangle(width, height, color)
            print(rectangle)
            rectangle.draw(text)

        elif shape_type == "пятиугольник":
            side = float(input("Введите длину стороны: "))
            if side <= 0:
                raise ValueError("Длина стороны должна быть положительным числом.")
            pentagon = Pentagon(side, color)
            print(pentagon)
            pentagon.draw(text)

    except ValueError as e:
        print("Ошибка ввода:", e)
    except Exception as e:
        print("Произошла непредвиденная ошибка:", e)


if __name__ == "__main__":
    main()
