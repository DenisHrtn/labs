from tasks.decors.log_function_call import log_function_call


@log_function_call
def count_words(text: str) -> int:
    """
    Function to count the number of words in a string.
    Words are separated by spaces or commas.
    """
    words = text.replace(",", " ").split()
    return len(words)
