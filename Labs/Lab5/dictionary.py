import os

from file_handler import *


class Dictionary:
    """ Represents a dictionary. """

    def __init__(self, filepath):
        """
        :param filepath: a string
        """
        self._dictionary = None
        self.__load_dictionary(filepath)

    def __load_dictionary(self, filepath):
        """
        Gets and assigns a dict object.
        :param filepath: a string
        :return: none
        """
        ext = os.path.splitext(filepath)[1]
        try:
            self._dictionary = FileHandler.load_data(
                filepath, ext)
        except InvalidFileTypeError as e:
            print(e)

    def query_definition(self, word):
        """
        Tries to find the word in the dictionary. If it finds it,
        appends the query and definition to a text file, otherwise
        it returns None.
        :param word: a string
        :return: a string or None
        """
        definition = None
        try:
            definition = self._dictionary[word.lower()][0]
        except KeyError:
            try:
                definition = self._dictionary[word.title()][0]
            except KeyError:
                print("Could not find " + word + " in dictionary")

        if definition is None:
            return None
        else:
            line = word + ": " + definition + "\n"
            FileHandler.write_lines("queries.txt", line)
            return definition

    def get_dictionary(self):
        """
        Gets the dictionary.
        :return: a dict
        """
        return self._dictionary

def main():
    """
    Drives the program.
    :return: None
    """
    my_dictionary = createDictionary()

    if my_dictionary.get_dictionary() is None:
        return

    user_input = None

    while user_input != "exitprogram":
        print("Dictionary")
        print("----------")
        print("1. Make a query")
        string_input = input("Enter '1' or 'exitprogram': ")

        if string_input == '':
            continue

        try:
            user_input = int(string_input)
        except ValueError:
            user_input = string_input

        if user_input == 1:
            word = input("What word do you want to search for? ")
            result = my_dictionary.query_definition(word)
            if result is not None:
                print(result)
            input("Press ENTER to continue")
        elif user_input == "exitprogram":
            pass
        else:
            print("Please enter a valid input")


def createDictionary():
    """
    Prompts the user for name of file containing the dictionary data.
    :return: a dict
    """
    file = input("Enter the file name: ")
    try:
        dictionary = Dictionary(file)
    except FileNotExistError as e:
        print(e)
        return createDictionary()
    else:
        return dictionary


if __name__ == "__main__":
    main()
