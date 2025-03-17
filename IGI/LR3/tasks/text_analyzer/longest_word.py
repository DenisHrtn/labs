from tasks.decors.log_function_call import log_function_call


@log_function_call
def find_longest_word(text: str):
    """
    Function to find the longest word and its position in the string.
    """
    words = text.replace(",", " ").split()
    longest_word = max(words, key=len)
    position = words.index(longest_word) + 1  # Position is 1-based
    return longest_word, position
