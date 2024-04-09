class Basket:
    def collect_aviailable_things_from_shoppinglist(self, shopping_list: list, available_things_in_shop):
        things_in_basket = []

        for thing_on_list in shopping_list:
            name_to_search = thing_on_list.get('name')
            for thing_in_shop in available_things_in_shop:
                if name_to_search == thing_in_shop.get('name'):
                    things_in_basket.append({
                        "name": name_to_search,
                        "price": thing_in_shop.get('price'),
                        "amount": thing_on_list.get('amount')
                    })
        return things_in_basket

2
