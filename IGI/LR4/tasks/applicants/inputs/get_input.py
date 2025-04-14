import sys


def get_input(prompt, allow_exit=True):
    """
    Функция для получения строки с возможностью выхода.
    """
    while True:
        value = input(prompt).strip()
        if allow_exit and value == '0':
            sys.exit("Exit requested by user.")
        if value:
            return value
        print("Input cannot be empty. Try again.")
