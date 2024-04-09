

class Costumer:
    def __init__(self):
        self.shopping_list = []

    def add_thing_to_shopping_list(self, thing):
        self.shopping_list.append({"name": thing.get_name(), "price": thing.get_price(), "amount": thing.get_amount()})

    def get_shopping_list(self):
        return self.shopping_list
