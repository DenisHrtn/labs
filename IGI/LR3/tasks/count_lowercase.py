from tasks.decors.count_lowercase_decorator import count_lowercase_words_decorator
from tasks.decors.log_function_call import log_function_call


@log_function_call
@count_lowercase_words_decorator
def count_lowercase_words(text: str) -> int:
    """Counts the number of words starting with a lowercase letter."""
    words = text.split()
    return sum(1 for word in words if word and word[0].islower())


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    count_lowercase_words(user_input)
