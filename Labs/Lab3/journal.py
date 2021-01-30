from item import Item


class Journal(Item):
    """Represents a journal that will be added to a library."""
    def __init__(self, call_num, title, num_copies, issue_num, publisher):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an integer
        :param issue_num: an integer
        :param publisher: a string
        """
        super().__init__(call_num, title, num_copies)
        self._issue_num = issue_num
        self._publisher = publisher

    @property
    def issue_number(self):
        """
        Gets the issue number.
        :return: an integer
        """
        return self._issue_num

    @property
    def publisher(self):
        """
        Gets the publisher's name.
        :return: a string
        """
        return self._publisher

    def __str__(self):
        """
        Formats the attributes of this journal.
        :return: a string
        """
        return f"---- Journal: {self.title} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self.num_copies}\n" \
               f"Issue Number: {self.issue_number}\n" \
               f"Publisher: {self.publisher}"
