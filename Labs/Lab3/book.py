class Book:
    """
    Represents a single book in a library which is identified through
    it's call number.
    """

    def __init__(self, call_num, title, num_copies, author):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        self._call_num = call_num
        self._title = title
        self._num_copies = num_copies
        self._author = author

    def __str__(self):
        return f"---- Book: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Author: {self._author}"
