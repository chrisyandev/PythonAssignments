from abc import *
from book import Book
from journal import Journal
from dvd import DVD


class ItemFactory(ABC):

    @abstractmethod
    def create_item(self):
        pass


class BookItemFactory(ItemFactory):

    def create_item(self):
        """
        Creates a Book object.
        :return: a Book object
        """
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        author = input("Enter Author Name: ")
        return Book(call_number, title, num_copies, author)


class JournalItemFactory(ItemFactory):

    def create_item(self):
        """
        Creates a Journal object.
        :return: a Journal object
        """
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        issue_num = input("Enter issue number: ")
        publisher = input("Enter publisher: ")
        return Journal(call_number, title, num_copies, issue_num, publisher)


class DvdItemFactory(ItemFactory):

    def create_item(self):
        """
        Creates a DVD object.
        :return: a DVD object
        """
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        release_date = input("Enter release date: ")
        region_code = input("Enter region code: ")
        return DVD(call_number, title, num_copies, release_date, region_code)


class FactoryTypes:
    factory_types = {
        "books": BookItemFactory,
        "journals": JournalItemFactory,
        "dvds": DvdItemFactory
    }
