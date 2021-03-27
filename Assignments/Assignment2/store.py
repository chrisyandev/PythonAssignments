import datetime

from order import *
from custom_exceptions import *


class Store:
    def __init__(self):
        self._inventory = {}
        self._orders = {}

    def check_inventory(self):
        for key, item in self._inventory.items():
            print(item.quantity)

    def receive_order(self, order):
        target_item = self._inventory.get(order.product_id)
        order_quantity = order.product_details.get("quantity")
        if target_item is None:
            item_type_to_create = ItemFactoryMapper.get_method(order.factory, order.item_type)
            item_properties = order.product_details
            item_properties["name"] = order.item_name
            item_properties["product_id"] = order.product_id
            try:
                new_item = item_type_to_create(**item_properties)
                self._inventory[new_item.product_id] = new_item
            except OrderProcessError as e:
                print(e)
        else:
            while target_item.quantity < order_quantity:
                target_item.quantity += 100
            target_item.quantity - order_quantity
        self._orders[order.order_num] = order

    def print_orders(self):
        for order_num, order in self._orders.items():
            print(order_num, order.item_name)

    def create_daily_transaction_report(self):
        current_time = datetime.datetime.now()
        file_name = current_time.strftime("DTR_%d%m%y_%H%M.txt")
        with open(file_name, mode='w', encoding="utf-8") as report:
            report.write("HOLIDAY STORE - DAILY TRANSACTION REPORT (DRT)\n")
            report.write(current_time.strftime("%d-%m-%Y %H:%M\n"))
            for order_num, order in self._orders.items():
                report.write(order.__str__() + "\n")

    def show_user_menu(self):
        """ Displayed on program start. """
        user_input = None

        while user_input != 3:
            print("Main Menu")
            print("-----------------------")
            print("1. Process Web Orders")
            print("2. Check Inventory")
            print("3. Exit")
            print("-----------------------")

            try:
                user_input = int(input("Please enter your choice (1-3): "))
            except ValueError:
                print("Must be an integer")
                continue

            if user_input == 1:
                OrderProcessor.process(self)
            elif user_input == 2:
                self.check_inventory()
            elif user_input == 3:
                self.create_daily_transaction_report()
            else:
                print("Please enter a number from 1-3")