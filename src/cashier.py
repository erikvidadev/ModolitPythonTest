class Cashier:
    def create_receipt(self, things_in_basket):
        product_details = []

        for thing in things_in_basket:
            name = thing.get('name')
            price = thing.get('price')
            amount = thing.get('amount')
            total_price = price * amount
            product_details.append(f"{name} - {price} Ft * {amount} db = {total_price} Ft")
        return product_details

    def calculate_total_price(self, things_in_basket):
        total_price = sum(thing['price'] * thing['amount'] for thing in things_in_basket)
        return total_price
