class Inventory:
    def __init__(self):
        self._item_dict = {}

    def check_inventory(self):
        for key, item in self._item_dict.items():
            print(item.quantity)
