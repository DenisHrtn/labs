from tasks.decors.log_function_call import log_function_call
from tasks.text_analyzer.count_words import count_words
from tasks.text_analyzer.longest_word import find_longest_word
from tasks.text_analyzer.odd_words import odd_words


text = (
        "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and "
        "stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the "
        "daisies, when suddenly a White Rabbit with pink eyes ran close by her."
        )


@log_function_call
def analyze_text(data: str):
    """
    Function to analyze the given text.
    It counts the number of words, finds the longest word and its position,
    and extracts odd-positioned words.
    """
    word_count = count_words(data)
    longest_word, position = find_longest_word(data)
    odd_words_list = odd_words(data)
    return word_count, longest_word, position, odd_words_list


def main():
    # Analyze the given text
    word_count, longest_word, position, odd_words_list = analyze_text(text)

    print(f"\nAnalysis of the text:")
    print(f"1. The number of words is: {word_count}")
    print(f"2. The longest word is '{longest_word}' at position {position}")
    print(f"3. Odd-positioned words are: {', '.join(odd_words_list)}")


if __name__ == "__main__":
    main()
