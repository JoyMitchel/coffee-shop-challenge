class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
        self._orders = []

    def get_name(self):
        return self._name

    def orders(self):
        return self._orders

    def customers(self):
        customers = []
        for order in self._orders:
            if order.get_customer() not in customers:
                customers.append(order.get_customer())
        return customers

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total = sum(order.get_price() for order in self._orders)
        return total / len(self._orders)