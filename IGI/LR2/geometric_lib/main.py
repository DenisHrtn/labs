import circle
import square

var = int(input("Введи длину стороны квадрата: "))
print("Площадь (квадрата) = ", square.area(var))
print("Периметр квадрата = ", square.perimeter(var))
var = int(input("Введи радиус круга: "))
print("Площадь круга = ", circle.area(var))
print("Периметр круга = ", circle.perimeter(var))