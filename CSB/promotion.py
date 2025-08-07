class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class Order:
    def __init__(self, customer, cart=[]):
        self.customer = customer
        self.cart = cart

    def add(self, item):
        self.cart.append(item)

class Promotion:
    def __init__(self, item, sale):
        pass

TV = Item("TV Sony", 2, 3500)
Phone = Item("Iphone 15", 8, 1799)
Chair = Item("Wooden Chair", 5, 179)

Customer_1 = Order("Emma")
Customer_1.add(TV)
print(Customer_1.cart[0].name)
