class Order:
    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee

        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee")
        if not (isinstance(price, float) and 1.0 <= price <= 10.0):
            raise ValueError("price must be a float between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price

    def get_customer(self):
        return self._customer

    def get_coffee(self):
        return self._coffee

    def get_price(self):
        return self._price
        