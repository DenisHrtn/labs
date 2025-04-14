import numpy as np

n, m = 5, 5

A = np.random.randint(-100, 100, (n, m))
print("Исходная матрица A:")
print(A)

print("\nПервый столбец:", A[:, 0])

print("\nПервый ряд:", A[0, :])

A_abs_max = np.max(np.abs(A))

# новая матрица B путем деления всех элементов на максимальный по модулю элемент
B = A / A_abs_max
print("\nНовая матрица B:")
print(B)

mean_B = np.mean(B)  # среднее
median_B = np.median(B)  # медиана
corrcoef_B = np.corrcoef(B, rowvar=False)  # корреляционная матрица по столбцам
var_B = np.var(B)  # дисперсия
std_B = np.std(B)  # стандартное отклонение

var_formula = np.mean(B**2) - np.mean(B)**2

print("\nСтатистики матрицы B:")
print(f"Среднее: {mean_B:.2f}")
print(f"Медиана: {median_B:.2f}")
print(f"Дисперсия (через var()): {var_B:.2f}")
print(f"Дисперсия (по формуле): {var_formula:.2f}")
print(f"Стандартное отклонение: {std_B:.2f}")

print("\nКорреляционная матрица:")
print(corrcoef_B)
