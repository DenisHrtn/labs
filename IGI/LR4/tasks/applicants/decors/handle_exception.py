import sys
from functools import wraps


def handle_errors(func):
    """
    Декоратор для обработки ошибок и выхода из программы.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print("\nExit requested by user. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\n⚠️ Unexpected error: {e}")
            sys.exit(1)
    return wrapper
