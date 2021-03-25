from order import *


class Store:
    def __init__(self):
        self._inventory = {}
        self._orders = {}

    def check_inventory(self):
        for key, item in self._inventory.items():
            print(item.quantity)

    def receive_order(self, order):
        self._orders[order.order_num] = order

    def print_orders(self):
        for order_num, order in self._orders.items():
            print(order_num, order.item_name)
