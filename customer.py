class Customer:
    def __init__(self, name):
        self.set_name(name)
        self._orders = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        coffees = []
        for order in self._orders:
            if order.get_coffee() not in coffees:
                coffees.append(order.get_coffee())
        return coffees

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order
