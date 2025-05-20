class Customer:
    def __init__(self, name):
        self.set_name(name)
        self._orders = []

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters")

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.get_coffee() for order in self._orders})

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._add_order(order)
        return order


