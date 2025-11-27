class Cart:
    def __init__(self, name, price, items):
        self.name = name
        self.price= price
        self.items = items

    def add_item(self):
        self.items[self.items] = self.price

    def total_price(self):
       return sum(self.items)