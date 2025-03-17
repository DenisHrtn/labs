import math
from tabulate import tabulate

from tasks.decors.log_function_call import log_function_call


@log_function_call
def ln_series(x: float | int, eps=1e-6, max_iter=500):
    """
    Function to calculate ln(1-x) using power series.

    :param x: Value of x (should be |x| < 1)
    :param eps: Required accuracy
    :param max_iter: Maximum number of iterations
    :return: Approximated value, number of terms used
    """
    if not (-1 < x < 1):
        raise ValueError("x must be in the range (-1, 1)")

    sum_value = 0
    term = x
    n = 1

    while abs(term) > eps and n < max_iter:
        sum_value -= term / n
        n += 1
        term *= x  # Update term for next iteration

    return sum_value, n


@log_function_call
def get_user_input():
    """
    Get a valid user input for x.
    """
    while True:
        try:
            x = float(input("Enter x (-1 < x < 1): "))
            if -1 < x < 1:
                return x
            else:
                print("x must be in range (-1, 1). Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


@log_function_call
def main():
    """
    Main function to execute the program.
    """
    x = get_user_input()
    eps = 1e-6  # Precision

    approx_value, num_terms = ln_series(x, eps)
    math_value = math.log(1 - x)

    table = [[x, num_terms, approx_value, math_value, eps]]
    print(tabulate(table, headers=["x", "n", "F(x)", "Math F(x)", "eps"], tablefmt="grid"))


if __name__ == "__main__":
    main()