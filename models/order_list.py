from models.order import Order

order_1 = Order("Steve", "15/09/21", "13:12", "Pepperoni", 2, True)
order_2 = Order("Stan", "16/09/21", "12:00", "Hawaiian", 1, False)
order_3 = Order("Jenny", "16/09/21", "12:00", "Margherita", 1, False)
order_4 = Order("Craig", "22/09/21", "10:00", "Vegetarian", 3, True)

orders = [order_1, order_2, order_3, order_4]