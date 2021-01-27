from abc import *


class Item(ABC):

    @abstractmethod
    def __init__(self, call_num, title, num_copies):
        self._call_num = call_num
        self._title = title
        self._num_copies = num_copies

    @property
    def call_number(self):
        """
        Returns the item's call number
        :return: a string
        """
        return self._call_num

    @property
    def title(self):
        """
        Returns the title of the item
        :return: a string
        """
        return self._title.title()

    @property
    def num_copies(self):
        """
        Returns the number of copies that are available for this
        specific item.
        :return: an int
        """
        return self._num_copies

    def increment_number_of_copies(self):
        """
        Set's the number of copies of an item
        """
        self._num_copies += 1

    def decrement_number_of_copies(self):
        """
        Set's the number of copies of an item
        """
        self._num_copies -= 1

    def check_availability(self):
        """
        Returns True if the item is available and False otherwise
        :return: A Boolean
        """
        if self._num_copies > 0:
            return True
        else:
            return False

    @abstractmethod
    def __str__(self):
        pass
