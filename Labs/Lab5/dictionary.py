from file_handler import *


class Dictionary:

    def __init__(self, filepath):
        self._dictionary = {}
        self.load_dictionary(filepath)

    def load_dictionary(self, filepath):
        try:
            self._dictionary = FileHandler.load_data(
                filepath, FileExtensions.JSON.value)
        except InvalidFileTypeError:
            print("File " + filepath + " must be a text or JSON file. \
                    The data was not added to the dictionary.")

    def query_definition(self, word):
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
            with open("queries.txt", mode='a') as queries_text:
                queries_text.write(word + ": " + definition + "\n")
            return definition

    def get_dictionary(self):
        return self._dictionary

def main():
    my_dictionary = Dictionary("data.json")

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


if __name__ == "__main__":
    main()
