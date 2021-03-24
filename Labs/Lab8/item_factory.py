from abc import *
from book import Book
from journal import Journal
from dvd import DVD


class ItemFactory(ABC):
    """ Creates different types of Items. """

    def __init__(self):
        self.call_num = input("Enter Call Number: ")
        self.title = input("Enter title: ")
        self.num_copies = int(input("Enter number of copies "
                                    "(positive number): "))

    @abstractmethod
    def create_item(self):
        """
        Asks for user input then creates an Item from it.
        :return: Object that is subtype of Item
        """
        pass


class BookItemFactory(ItemFactory):

    def create_item(self):
        """
        Creates a Book object.
        :return: a Book object
        """
        author = input("Enter Author Name: ")
        return Book(author, call_num=self.call_num, title=self.title,
                    num_copies=self.num_copies)


class JournalItemFactory(ItemFactory):

    def create_item(self):
        """
        Creates a Journal object.
        :return: a Journal object
        """
        issue_num = input("Enter issue number: ")
        publisher = input("Enter publisher: ")
        return Journal(issue_num, publisher, call_num=self.call_num,
                       title=self.title, num_copies=self.num_copies)


class DvdItemFactory(ItemFactory):

    def create_item(self):
        """
        Creates a DVD object.
        :return: a DVD object
        """
        release_date = input("Enter release date: ")
        region_code = input("Enter region code: ")
        return DVD(release_date, region_code, call_num=self.call_num,
                   title=self.title, num_copies=self.num_copies)


class FactoryTypes:
    """ Matches category types to their respective ItemFactory. """

    factory_types = {
        "books": BookItemFactory,
        "journals": JournalItemFactory,
        "dvds": DvdItemFactory
    }
