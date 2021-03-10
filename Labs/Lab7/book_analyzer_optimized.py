"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""

import itertools


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a dict of common punctuation to be used with translate()
    COMMON_PUNCTUATION = {
        ord(','): '',
        ord('*'): '',
        ord(';'): '',
        ord('.'): '',
        ord(':'): '',
        ord('('): '',
        ord('['): '',
        ord(']'): '',
        ord(')'): ''
    }

    def __init__(self):
        self.text = None

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # read lines
        with open(src, mode='r', encoding='utf-8') as book_file:
            self.text = book_file.readlines()

        # strip out empty lines
        self.text = filter(lambda line: line != "\n", self.text)

        # convert list of lines to list of words
        words = map(lambda line: line.split(), self.text)
        self.text = list(itertools.chain.from_iterable(words))

        # remove common punctuation from words, change all words to lowercase
        # self.text assigned a set
        self.text = {word.translate(self.COMMON_PUNCTUATION).lower()
                     for word in self.text}

    @staticmethod
    def is_unique(word, word_list):
        """
        Checks to see if the given word appears in the provided sequence.
        This check is case in-sensitive.
        :param word: a string
        :param word_list: a sequence of words
        :return: True if not found, false otherwise
        """
        if word in word_list:
            return False
        return True

    def find_unique_words(self):
        """
        Filters out all the words in the text.
        :return: a list of all the unique words.
        """
        temp_text = self.text
        unique_words = []
        while temp_text:
            word = temp_text.pop()
            if self.is_unique(word, temp_text):
                unique_words.append(word)
        return unique_words


def main():
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    unique_words = book_analyzer.find_unique_words()
    print("-"*50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-"*50)
    for word in unique_words:
        print(word)
    print("-"*50)


if __name__ == '__main__':
    main()