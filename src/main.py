from src.basket import Basket
from src.cashier import Cashier
from src.costumer import Costumer
from src.shop import Thing, Shop


def main():
    product_in_shop1 = Thing(name="apple", price=2, amount=10)
    product_in_shop2 = Thing(name="potato", price=4, amount=10)
    product_in_shop3 = Thing(name="watermelon", price=6, amount=10)

    product_on_shopping_list1 = Thing(name="apple", price=2, amount=1)
    product_on_shopping_list2 = Thing(name="potato", price=3, amount=2)
    product_on_shopping_list3 = Thing(name="watermelon", price=4, amount=3)

    supermarket = Shop()
    costumer = Costumer()

    supermarket.add_thing_to_stock(product_in_shop1)
    supermarket.add_thing_to_stock(product_in_shop2)
    supermarket.add_thing_to_stock(product_in_shop3)
    costumer.add_thing_to_shopping_list(product_on_shopping_list1)
    costumer.add_thing_to_shopping_list(product_on_shopping_list2)
    costumer.add_thing_to_shopping_list(product_on_shopping_list3)

    basket = Basket()

    things_in_basket = basket.collect_aviailable_things_from_shoppinglist(
        shopping_list=costumer.get_shopping_list(),
        available_things_in_shop=supermarket.get_things_on_stock()
    )

    cashier = Cashier()
    product_details = cashier.create_receipt(things_in_basket)

    for product in product_details:
        print(product)

    print(f"Final price: {cashier.calculate_total_price(things_in_basket)}Ft")


if __name__ == '__main__':
    main()
