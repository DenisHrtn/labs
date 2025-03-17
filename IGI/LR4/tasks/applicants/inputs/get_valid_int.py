import sys


def get_valid_int(prompt, min_val, max_val):
    """Функция для получения корректного числа в заданном диапазоне."""
    while True:
        try:
            value = input(prompt).strip()
            if value == '0':
                sys.exit("Exit requested by user.")
            value = int(value)
            if min_val <= value <= max_val:
                return value
            print(f"Number must be between {min_val} and {max_val}. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")
