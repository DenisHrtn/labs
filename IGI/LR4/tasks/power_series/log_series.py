import math
import matplotlib.pyplot as plt
from statistics import mean, median, mode, variance


class LogSeries:
    def __init__(self, x: float, eps=1e-6, max_iter=500):
        if not (-1 < x < 1):
            raise ValueError("x must be in the range (-1, 1)")
        self.x = x
        self.eps = eps
        self.max_iter = max_iter
        self.series_values = []
        self.num_terms = 0
        self.approx_value = self.calculate_series()
        self.math_value = math.log(1 - x)

    def calculate_series(self):
        sum_value = 0
        term = self.x
        n = 1

        while abs(term) > self.eps and n < self.max_iter:
            sum_value -= term / n
            self.series_values.append(sum_value)
            n += 1
            term *= self.x

        self.num_terms = n
        return sum_value

    def get_statistics(self):
        return {
            "mean": mean(self.series_values) if self.series_values else None,
            "median": median(self.series_values) if self.series_values else None,
            "mode": mode(self.series_values) if len(set(self.series_values)) > 1 else None,
            "variance": variance(self.series_values) if len(self.series_values) > 1 else None,
            "std_dev": math.sqrt(variance(self.series_values)) if len(self.series_values) > 1 else None
        }

    def plot_series(self):
        n_values = list(range(1, len(self.series_values) + 1))  # Обновленный список n
        plt.figure(figsize=(8, 5))

        plt.plot(n_values, self.series_values, label='Series Approximation', color='blue')
        plt.axhline(y=self.math_value, color='red', linestyle='dashed', label='Math.log(1-x)')

        plt.xlabel("Number of Terms")
        plt.ylabel("Value of Series")
        plt.title("Ln(1-x) Series Approximation")
        plt.legend()
        plt.grid()

        plt.savefig("log_series_plot.png")
        plt.show()
