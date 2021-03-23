""" This module houses the library"""
import difflib
from library_item_generator import LibraryItemGenerator
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

    class Catalogue:
        """
        Represents a list of items belonging to a specific catalogue.
        """
        def __init__(self, item_type):
            """
            Initializes a list to store Item objects.
            :param item_type: a string
            """
            self._type = item_type.lower()
            self._item_list = []

        def _retrieve_item_by_call_number(self, call_number):
            """
            A private method that encapsulates the retrieval of an item with
            the given call number from the library.
            :param call_number: a string
            :return: Item object if found, None otherwise
            """
            found_item = None
            for item in self._item_list:
                if item.call_number == call_number:
                    found_item = item
                    break
            return found_item

        def find_items(self, title):
            """
            Find items with the same and similar title.
            :param title: a string
            :return: a list of titles.
            """
            title_list = []
            for item in self._item_list:
                title_list.append(item.title)
            results = difflib.get_close_matches(title, title_list,
                                                cutoff=0.5)
            return results

        def add_item(self):
            """
            Add an item to the library with a unique call number.
            """
            new_item = LibraryItemGenerator.generate_item(self._type)
            found_item = self._retrieve_item_by_call_number(
                new_item.call_number)
            if found_item:
                print(f"Could not add item with call number "
                      f"{new_item.call_number}. It already exists. ")
            else:
                self._item_list.append(new_item)
                print("item added successfully! item details:")
                print(new_item)

        def remove_item(self, call_number):
            """
            Remove an existing item from the library
            :param call_number: a string
            :precondition call_number: a unique identifier
            """
            found_item = self._retrieve_item_by_call_number(call_number)
            if found_item:
                self._item_list.remove(found_item)
                print(f"Successfully removed {found_item.title} with "
                      f"call number: {call_number}")
            else:
                print(f"item with call number: {call_number} not found.")

        def check_out(self, call_number):
            """
            Check out an item with the given call number from the library.
            :param call_number: a string
            :precondition call_number: a unique identifier
            """
            target_item = self._retrieve_item_by_call_number(call_number)
            if target_item is not None and target_item.check_availability():
                status = self.reduce_item_count(call_number)
                if status:
                    print("Checkout complete!")
                else:
                    print(f"Could not find item with call number {call_number}"
                          f". Checkout failed.")
            else:
                print(f"No copies left for call number {call_number}"
                      f". Checkout failed.")

        def return_item(self, call_number):
            """
            Return an item with the given call number from the library.
            :param call_number: a string
            :precondition call_number: a unique identifier
            """
            status = self.increment_item_count(call_number)
            if status:
                print("item returned successfully!")
            else:
                print(f"Could not find item with call number {call_number}"
                      f". Return failed.")

        def reduce_item_count(self, call_number):
            """
            Decrement the item count for an item with the given call number
            in the library.
            :param call_number: a string
            :precondition call_number: a unique identifier
            :return: True if the item was found and count decremented, false
            otherwise.
            """
            target_item = self._retrieve_item_by_call_number(call_number)
            if target_item:
                target_item.decrement_number_of_copies()
                return True
            else:
                return False

        def increment_item_count(self, call_number):
            """
            Increment the item count for an item with the given call number
            in the library.
            :param call_number: a string
            :precondition call_number: a unique identifier
            :return: True if the item was found and count incremented, false
            otherwise.
            """
            target_item = self._retrieve_item_by_call_number(call_number)
            if target_item:
                target_item.increment_number_of_copies()
                return True
            else:
                return False

        @property
        def items(self):
            """
            Gets the list of items in this catalogue.
            :return: a List
            """
            return self._item_list

        @property
        def item_type(self):
            """
            Gets the type of items in this catalogue.
            :return: a string
            """
            return self._type


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    library = Library()
    books = library.Catalogue("Books")
    journals = library.Catalogue("Journals")
    dvds = library.Catalogue("DVDs")
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
