from book import Book
from journal import Journal
from dvd import DVD


class LibraryItemGenerator:

    @classmethod
    def generate_item(cls, item_type):
        if item_type.lower() == "books":
            return cls.create_book()
        if item_type.lower() == "journals":
            return cls.create_journal()
        if item_type.lower() == "dvds":
            return cls.create_dvd()

    @staticmethod
    def create_book():
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        author = input("Enter Author Name: ")
        return Book(call_number, title, num_copies, author)

    @staticmethod
    def create_journal():
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        issue_num = input("Enter issue number: ")
        publisher = input("Enter publisher: ")
        return Journal(call_number, title, num_copies, issue_num, publisher)

    @staticmethod
    def create_dvd():
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        release_date = input("Enter release date: ")
        region_code = input("Enter region code: ")
        return DVD(call_number, title, num_copies, release_date, region_code)
