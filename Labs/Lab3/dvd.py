from item import Item


class DVD(Item):
    """Represents a DVD that will be added to a library."""
    def __init__(self, call_num, title, num_copies, release_date, region_code):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an integer
        :param release_date: a string
        :param region_code: an integer
        """
        super().__init__(call_num, title, num_copies)
        self._release_date = release_date
        self._region_code = region_code

    @property
    def release_date(self):
        """
        Gets the release date.
        :return: a string
        """
        return self._release_date

    @property
    def region_code(self):
        """
        Gets the region code.
        :return: an integer
        """
        return self._region_code

    def __str__(self):
        """
        Formats the attributes of this DVD.
        :return: a string
        """
        return f"---- DVD: {self.title} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self.num_copies}\n" \
               f"Release Date: {self.release_date}\n" \
               f"Region Code: {self.region_code}"
