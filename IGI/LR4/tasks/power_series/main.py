from tabulate import tabulate

from tasks.power_series.log_series import LogSeries


def main():
    x = float(input("Enter x (-1 < x < 1): "))
    log_series = LogSeries(x)
    stats = log_series.get_statistics()

    table = [[x, log_series.num_terms, log_series.approx_value, log_series.math_value, log_series.eps]]
    print(tabulate(table, headers=["x", "n", "F(x)", "Math F(x)", "eps"], tablefmt="grid"))

    print("\nStatistics:")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value}")

    log_series.plot_series()


if __name__ == "__main__":
    main()