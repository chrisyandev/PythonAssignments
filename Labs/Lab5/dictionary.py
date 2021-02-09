from file_handler import *


class Dictionary:

    def __init__(self, filepath):
        self._dictionary = {}
        self.load_dictionary(filepath)

    def load_dictionary(self, filepath):
        self._dictionary = FileHandler.load_data(filepath, ".json")

    def query_definition(self, word):
        definition = self._dictionary[word][0]
        with open("queries.txt", mode='a') as queries_text:
            queries_text.write(word + ": " + definition + "\n")
        return definition

    def get_dictionary(self):
        return self._dictionary

def main():
    word = input("What word do you want to search for? ")

    my_dictionary = Dictionary("data.json")
    # print(my_dictionary.get_dictionary())

    result = my_dictionary.query_definition(word)
    print(result)


if __name__ == "__main__":
    main()