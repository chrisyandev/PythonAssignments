""" This module houses the library"""
from catalogue import Catalogue
from book import Book
from journal import Journal
from dvd import DVD


class Library:
    """
    The Library consists of catalogues of items and provides an
    interface for users to check out, return and find items.
    """
    def __init__(self):
        self._catalogue_list = []

    def show_main_menu(self):
        """
        Display the library menu allowing the user to either access the
        list of books, check out, return, find, add, remove a book.
        """
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all items")
            print("2. Check Out an item")
            print("3. Return an item")
            print("4. Find an item")
            print("5. Add an item")
            print("6. Remove an item")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7)")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.display_all_items()
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                self.show_check_out_menu()
            elif user_input == 3:
                call_number = input("Enter the call number of the book"
                                    " you wish to return.")
                self.return_book(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the book:")
                found_titles = self.find_books(input_title)
                print("We found the following:")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                self.show_add_item_menu()

            elif user_input == 6:
                call_number = input("Enter the call number of the book")
                self.remove_book(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")

    def show_check_out_menu(self):
        user_input = None
        while user_input != 4:
            print("\nWhich item do you want to check out?")
            print("-----------------------")
            print("1. Books")
            print("2. Journals")
            print("3. DVDs")
            print("4. Quit")
            string_input = input("Please enter your choice (1-4)")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                c = self.get_catalogue("books")
                if c is not None:
                    call_number = input("Enter the call number of the item"
                                        " you wish to check out.")
                    c.check_out(call_number)
            elif user_input == 2:
                c = self.get_catalogue("journals")
                if c is not None:
                    call_number = input("Enter the call number of the item"
                                        " you wish to check out.")
                    c.check_out(call_number)
            elif user_input == 3:
                c = self.get_catalogue("dvds")
                if c is not None:
                    call_number = input("Enter the call number of the item"
                                        " you wish to check out.")
                    c.check_out(call_number)
            elif user_input == 4:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 4.")

    def show_add_item_menu(self):
        user_input = None
        while user_input != 4:
            print("\nWhich item do you want to create?")
            print("-----------------------")
            print("1. Books")
            print("2. Journals")
            print("3. DVDs")
            print("4. Quit")
            string_input = input("Please enter your choice (1-4)")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                c = self.get_catalogue("Books")
                if c is not None:
                    c.add_item()
            elif user_input == 2:
                c = self.get_catalogue("Journals")
                if c is not None:
                    c.add_item()
            elif user_input == 3:
                c = self.get_catalogue("DVDs")
                if c is not None:
                    c.add_item()
            elif user_input == 4:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 4.")

    def display_all_items(self):
        """
        Display all the items in the library.
        """
        for catalogue in self._catalogue_list:
            print(f"{catalogue.item_type.title()}")
            print("--------------", end="\n")
            for item in catalogue.items:
                print(item)
            print("\n")

    def add_catalogue(self, catalogue):
        for c in self._catalogue_list:
            if c.item_type == catalogue.item_type:
                return False
        self._catalogue_list.append(catalogue)
        return True

    def get_catalogue(self, item_type):
        for c in self._catalogue_list:
            if c.item_type == item_type.lower():
                return c
        print(f"Catalogue {item_type.title()} not found")
        return None

    def show_catalogues(self):
        for c in self._catalogue_list:
            print(c.item_type)


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    library = Library()
    books = Catalogue("Books")
    journals = Catalogue("Journals")
    dvds = Catalogue("DVDs")
    library.add_catalogue(books)
    library.add_catalogue(journals)
    library.add_catalogue(dvds)

    book_list = [
        Book("100.200.300", "Harry Potter 1", 2, "J K Rowling"),
        Book("999.224.854", "Harry Potter 2", 5, "J K Rowling"),
        Book("631.495.302", "Harry Potter 3", 4, "J K Rowling"),
        Book("123.02.204", "The Cat in the Hat", 1, "Dr. Seuss")
    ]

    journal_list = [
        Journal("101.201.301", "Someone's Journal", 3, 50, "Mr Publisher"),
        Journal("640.450.200", "Random Journal", 1, 28, "The Best")
    ]

    dvd_list = [
        DVD("980.242.580", "Rock Music", 5, "1/1/2007", 1),
        DVD("222.333.444", "Classical Music", 6, "5/20/2010", 2)
    ]

    for book in book_list:
        books.items.append(book)

    for journal in journal_list:
        journals.items.append(journal)

    for dvd in dvd_list:
        dvds.items.append(dvd)

    library.show_main_menu()


if __name__ == '__main__':
    main()
