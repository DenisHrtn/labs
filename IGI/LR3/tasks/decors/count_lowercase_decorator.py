from typing import Callable
from functools import wraps


def count_lowercase_words_decorator(func: Callable[[str], int]) -> Callable[[str], int]:
    """
    Decorator that prints additional information about the processing.
    """
    @wraps(func)
    def wrapper(text: str) -> int:
        count = func(text)
        print(f"Total words starting with a lowercase letter: {count}")
        return count
    return wrapper
