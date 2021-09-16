class Order:

    def __init__(self, customer_name, order_date, order_time, pizza_topping, quantity, delivery):
        self.customer_name = customer_name
        self.order_date = order_date
        self.order_time = order_time
        self.pizza_topping = pizza_topping
        self.quantity = quantity
        self.delivery = delivery