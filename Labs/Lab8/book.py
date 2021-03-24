from item import Item


class Book(Item):
    """
    Represents a single book in a library which is identified through
    it's call number.
    """

    def __init__(self, author, **kwargs):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(**kwargs)
        self._author = author

    @property
    def author(self):
        """
        Gets the book's author.
        :return: a string
        """
        return self._author

    def __str__(self):
        """
        Formats the attributes of this book.
        :return: a string
        """
        return f"---- Book: {self.title} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self.num_copies}\n" \
               f"Author: {self.author}"
