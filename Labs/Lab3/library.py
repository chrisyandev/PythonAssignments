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

    def show_catalogues(self):
        """
        Allows the user to pick a catalogue.
        :return: none
        """
        user_input = None

        print("\nWelcome to the Library!")
        print("-----------------------")

        while user_input != 4:
            print(f"\nWhich catalogue do you want to browse?")
            print("-----------------------")
            print("1. Books")
            print("2. Journals")
            print("3. DVDs")
            print("4. Quit")
            string_input = input("Please enter your choice (1-4): ")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                c = self.get_catalogue("books")
                if c is not None:
                    self.show_main_menu(c)
            elif user_input == 2:
                c = self.get_catalogue("journals")
                if c is not None:
                    self.show_main_menu(c)
            elif user_input == 3:
                c = self.get_catalogue("dvds")
                if c is not None:
                    self.show_main_menu(c)
            elif user_input == 4:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1-4: ")

        print("Thank you for visiting the Library.")

    def show_main_menu(self, catalogue):
        """
        Display the menu within the user's catalogue choice.
        The user can choose to display all check out, return,
        find, add, or remove an item.
        :param catalogue: a Catalogue object
        :return: none
        """
        user_input = None
        while user_input != 7:
            print(f"You are browsing {catalogue.item_type.title()}")
            print("-----------------------")
            print("1. Display all")
            print("2. Check Out")
            print("3. Return")
            print("4. Find")
            print("5. Add")
            print("6. Remove")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7): ")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.display_items_in_catalogue(catalogue)
                input("Press Enter to continue")
                continue
            elif user_input == 2:
                catalogue.check_out(input("Enter the call number: "))
            elif user_input == 3:
                catalogue.return_item(input("Enter the call number: "))
            elif user_input == 4:
                input_title = input("Enter the title: ")
                found_titles = catalogue.find_items(input_title)
                if len(found_titles) > 0:
                    print("We found the following:")
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                catalogue.add_item()

            elif user_input == 6:
                catalogue.remove_item(input("Enter the call number: "))

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7: ")

    def display_all_items(self):
        """
        Display all the items in the library.
        :return: none
        """
        for catalogue in self._catalogue_list:
            print(f"{catalogue.item_type.title()}")
            print("--------------", end="\n")
            for item in catalogue.items:
                print(item)
            print("\n")

    @staticmethod
    def display_items_in_catalogue(catalogue):
        """
        Display all items in a catalogue.
        :param catalogue: a Catalogue object
        :return: none
        """
        for item in catalogue.items:
            print(item)
        print("\n")

    def add_catalogue(self, catalogue):
        """
        Adds a catalogue to the library.
        :param catalogue: a Catalogue object
        :return: a boolean
        """
        for c in self._catalogue_list:
            if c.item_type == catalogue.item_type:
                return False
        self._catalogue_list.append(catalogue)
        return True

    def get_catalogue(self, item_type):
        """
        Gets a catalogue that exists.
        :param item_type: name of the Catalogue as a string
        :return: a Catalogue object or None if not found
        """
        for c in self._catalogue_list:
            if c.item_type == item_type.lower():
                return c
        print(f"Catalogue {item_type.title()} not found")
        return None


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

    library.show_catalogues()


if __name__ == '__main__':
    main()
