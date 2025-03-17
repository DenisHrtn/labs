from tasks.decors.log_function_call import log_function_call


@log_function_call
def odd_words(text):
    """
    Function to return a list of odd-positioned words (1-based indexing).
    """
    words = text.replace(",", " ").split()  # Replace commas and split by spaces
    return [words[i] for i in range(len(words)) if i % 2 == 0]
