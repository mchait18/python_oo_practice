"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """Machine for finding random words from dictionary."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.list_words = []
        self.read_file()

    def read_file(self):
        """Reads a file and lists each line into the list_words list"""
        file = open(self.file_path)
        for line in file:
            self.list_words.append(line[:len(line)-1])
        print(f"{len(self.list_words)} words read")

    def random(self):
        """chooses a random word from list_words to return"""
        return choice(self.list_words)


class SpecialWordFinder(WordFinder):

    def __init__(self, file_path):
        super().__init__(file_path)
        self.filter_words()

    def filter_words(self):
        """filters word_list to remove spaces and commented out words"""
        for word in self.list_words:
            if word == "" or word[0] == '#':
                self.list_words.remove(word)
