from tasks.text_analyzer.file_manager import FileManager
from tasks.text_analyzer.text_analyzer import TextAnalyzer


class InteractiveTextAnalyzer:
    """
    Provides an interactive interface for analyzing a text file.
    """

    def __init__(self):
        self.filename = "input.txt"
        self.results_filename = "results.txt"
        self.text = ""

    def load_text(self):
        """
        Loads text from the file.
        """
        self.text = FileManager.read_text(self.filename)
        if not self.text:
            print("No text available for analysis.")
            return False
        return True

    def analyze_text(self):
        """
        Performs text analysis and saves results.
        """
        analyzer = TextAnalyzer(self.text)
        total_sentences, narrative, question, imperative = analyzer.count_sentences()
        avg_sent_len = analyzer.avg_sentence_length()
        avg_word_len = analyzer.avg_word_length()
        smilies = analyzer.find_smilies()
        repeated_words = analyzer.repeated_words()
        short_words = analyzer.short_words()
        shortest_a_word = analyzer.shortest_word_starting_with_a()

        highlighted = analyzer.highlight_lower_upper_pairs(self.text)
        word_count, even_words = analyzer.even_length_words(self.text)

        result_text = f"""
        === Text Analysis Results ===
        Total sentences: {total_sentences}
        Narrative: {narrative}, Question: {question}, Imperative: {imperative}

        Average sentence length (characters): {avg_sent_len:.2f}
        Average word length: {avg_word_len:.2f}

        Found smilies: {', '.join(smilies) if smilies else 'None'}

        Repeated words: {', '.join(repeated_words) if repeated_words else 'None'}

        Words shorter than 5 characters: {', '.join(short_words) if short_words else 'None'}
        Shortest word starting with 'a': {shortest_a_word if shortest_a_word else 'None'}

        Highlighted lower-upper pairs in test string: {highlighted}
        Total words in test string: {word_count}
        Even-length words: {', '.join(even_words) if even_words else 'None'}
        """
        print(result_text)
        FileManager.save_results(result_text, self.results_filename)
        zip_file = FileManager.archive_file(self.results_filename)
        print(f"Results saved to {self.results_filename} and archived as {zip_file}")

    def start(self):
        """
        Starts the interactive loop.
        """
        while True:
            print("\n1. Load text")
            print("2. Analyze text")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                if self.load_text():
                    print("Text loaded successfully!")
            elif choice == "2":
                if self.text:
                    self.analyze_text()
                else:
                    print("Please load a text file first!")
            elif choice == "3":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
