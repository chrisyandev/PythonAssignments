from item import Item


class Journal(Item):

    def __init__(self, call_num, title, num_copies, issue_num, publisher):
        super().__init__(call_num, title, num_copies)
        self._issue_num = issue_num
        self._publisher = publisher

    @property
    def issue_number(self):
        return self._issue_num

    @property
    def publisher(self):
        return self._publisher

    def __str__(self):
        return f"---- Journal: {self.title} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self.num_copies}\n" \
               f"Issue Number: {self.issue_number}\n" \
               f"Publisher: {self.publisher}"
