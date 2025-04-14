import re


class TextAnalyzer:
    """
    Performs various text analysis operations.
    """

    def __init__(self, text):
        self.text = text

    def count_sentences(self):
        """
        Counts sentences by type (narrative, question, imperative).
        """
        narrative = len(re.findall(r'[.!](?:\s|$)', self.text))
        question = len(re.findall(r'\?(?:\s|$)', self.text))
        imperative = len(re.findall(r'!(?:\s|$)', self.text))
        return narrative + question + imperative, narrative, question, imperative

    def avg_sentence_length(self):
        """
        Calculates the average sentence length in characters.
        """
        sentences = re.split(r'[.!?]', self.text)
        words_only = [re.findall(r'\b\w+\b', sentence) for sentence in sentences if sentence.strip()]
        total_chars = sum(sum(len(word) for word in words) for words in words_only)
        total_sentences = len(words_only)
        return total_chars / total_sentences if total_sentences else 0

    def avg_word_length(self):
        """
        Calculates the average word length in the text.
        """
        words = re.findall(r'\b\w+\b', self.text)
        total_chars = sum(len(word) for word in words)
        return total_chars / len(words) if words else 0

    def find_smilies(self):
        """
        Finds smiley faces in the text.
        """
        return re.findall(r'[:;]-*\(+|[:;]-*\)+|[:;]-*\[+|[:;]-*\]+', self.text)

    def repeated_words(self):
        """
        Finds repeated words in the text.
        """
        words = re.findall(r'\b\w+\b', self.text.lower())
        return {word for word in words if words.count(word) > 1}

    def short_words(self):
        """
        Returns a list of words shorter than 5 characters.
        """
        return [word for word in re.findall(r'\b\w+\b', self.text) if len(word) < 5]

    def highlight_lower_upper_pairs(self, input_string):
        """
        Highlights all pairs 'lowercase letter' + 'uppercase letter'.
        """
        return re.sub(r'([a-z])([A-Z])', r'_?_\1\2_?_', input_string)

    def even_length_words(self, input_string):
        """
        Returns count of words and those with even number of letters.
        """
        words = re.findall(r'\b\w+\b', input_string)
        even_words = [word for word in words if len(word) % 2 == 0]
        return len(words), even_words

    def shortest_word_starting_with_a(self):
        """
        Finds the shortest word starting with 'a'.
        """
        words = [word for word in re.findall(r'\b\w+\b', self.text.lower()) if word.startswith('a')]
        return min(words, key=len) if words else None

