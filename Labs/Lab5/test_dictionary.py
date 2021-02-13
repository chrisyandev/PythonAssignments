from unittest import TestCase
from dictionary import Dictionary
from file_handler import *


class TestDictionary(TestCase):
    """ Tests the creation of a dictionary and making queries. """

    def test_load_dictionary(self):
        """ Tests if the dictionary gets initialized. """
        test_dictionary = Dictionary("data.txt")
        self.assertTrue(test_dictionary.get_dictionary() is not None)

    def test_invalid_file_type(self):
        """ Tests if given a bad extension, error will be raised. """
        with self.assertRaises(InvalidFileTypeError):
            FileHandler.load_data("data.txt", ".png")

    def test_write_to_file(self):
        """ Tests if string is properly written to a file. """
        with open("queries.txt", mode="w+") as my_text_file:
            write_text = "hello and goodbye"
            my_text_file.write(write_text)
            my_text_file.seek(0)
            read_text = my_text_file.read()
            self.assertEqual(write_text, read_text)

    def test_dictionary_query(self):
        """ Tests if expected definition is retrieved. """
        test_dictionary = Dictionary("data.json")
        self.assertEqual("An alcoholic beverage commonly fermented from "
                         "barley malt, with hops or some other substance "
                         "to impart a bitter flavor.",
                         test_dictionary.query_definition("BEER"))

    def test_dictionary_query_not_found(self):
        """ Tests if None is returned if word is not found. """
        test_dictionary = Dictionary("data.json")
        self.assertEqual(test_dictionary.query_definition("Chris"), None)

