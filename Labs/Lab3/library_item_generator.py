from book import Book
from journal import Journal
from dvd import DVD


class LibraryItemGenerator:

    @classmethod
    def show_item_types(cls):
        user_input = None
        while user_input != 4:
            print("\nWhich item do you want to create?")
            print("-----------------------")
            print("1. Book")
            print("2. Journal")
            print("3. DVD")
            print("4. Quit")
            string_input = input("Please enter your choice (1-4)")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                return cls.create_book()
            elif user_input == 2:
                return cls.create_journal()
            elif user_input == 3:
                return cls.create_dvd()
            elif user_input == 4:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 4.")

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
