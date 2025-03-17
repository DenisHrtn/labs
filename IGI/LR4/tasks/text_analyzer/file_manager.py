import zipfile


class FileManager:
    """Handles file operations such as reading, writing, and archiving."""

    @staticmethod
    def read_text(filename):
        """Reads text from a file and returns it as a string."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print("Error: File not found!")
            return ""

    @staticmethod
    def save_results(results, filename):
        """Saves analysis results to a text file."""
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(results)

    @staticmethod
    def archive_file(filename):
        """Archives a given file in ZIP format."""
        zip_filename = f"{filename}.zip"
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            zipf.write(filename)
        return zip_filename