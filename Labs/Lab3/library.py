""" This module houses the library"""
from catalogue import Catalogue


class Library:
    """
    The Library consists of catalogues of items and provides an
    interface for users to check out, return and find items.
    """

    def __init__(self, catalogues):
        self._catalogue_list = []
        for c in catalogues:
            self._catalogue_list.append(c)

    def display_library_menu(self):
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
                self.display_available_books()
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                call_number = input("Enter the call number of the book"
                                    " you wish to check out.")
                self.check_out(call_number)
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
                self.add_book()

            elif user_input == 6:
                call_number = input("Enter the call number of the book")
                self.remove_book(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")

    def display_all_items(self):
        """
        Display all the items in the library.
        """
        for catalogue in self._catalogue_list:
            print(f"{catalogue.type}")
            print("--------------", end="\n\n")
            for item in catalogue.items:
                print(item)


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    books = Catalogue("Books")
    journals = Catalogue("Journals")
    dvds = Catalogue("DVDs")
    library = Library((books, journals, dvds))
    library.display_all_items()


if __name__ == '__main__':
    main()
