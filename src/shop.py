from typing import Optional


class Thing:
    def __init__(self, name: str, price: Optional[int], amount: int = 1):
        self.__name = name
        self.__price = price
        self.__amount = amount

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_amount(self):
        return self.__amount


class Shop:
    def __init__(self):
        self.things_on_stock = []

    def add_thing_to_stock(self, thing):
        self.things_on_stock.append({"name": thing.get_name(), "price": thing.get_price(), "amount": thing.get_amount()})

    def get_things_on_stock(self):
        return self.things_on_stock

