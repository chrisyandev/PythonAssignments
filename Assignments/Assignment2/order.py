from item_factory import *
import pandas as pd


class Order:
    def __init__(self, order_num, product_id, item_type, item_name, product_details, factory):
        self._order_num = order_num
        self._product_id = product_id
        self._item_type = item_type
        self._item_name = item_name
        self._product_details = product_details
        self._factory = factory

    @property
    def order_num(self):
        return self._order_num

    @property
    def item_name(self):
        return self._item_name


class OrderProcessor:
    @staticmethod
    def process(file_name, store):
        df = pd.read_excel(file_name)
        for x in range(0, len(df.index)):
            product_details = {
                "quantity": df["quantity"][x],
                "description": df["description"][x],
                "has_batteries": df["has_batteries"][x],
                "min_age": df["min_age"][x],
                "dimensions": df["dimensions"][x],
                "num_rooms": df["num_rooms"][x],
                "speed": df["speed"][x],
                "jump_height": df["jump_height"][x],
                "has_glow": df["has_glow"][x],
                "spider_type": df["spider_type"][x],
                "num_sound": df["num_sound"][x],
                "colour": df["colour"][x],
                "has_lactose": df["has_lactose"][x],
                "has_nuts": df["has_nuts"][x],
                "variety": df["variety"][x],
                "pack_size": df["pack_size"][x],
                "stuffing": df["stuffing"][x],
                "size": df["size"][x],
                "fabric": df["fabric"][x]
            }
            factory = ItemFactoryType.get_factory(df["holiday"][x].lower())
            new_order = Order(df["order_number"][x], df["product_id"][x],
                              df["item"][x], df["name"][x], product_details, factory)
            store.receive_order(new_order)


