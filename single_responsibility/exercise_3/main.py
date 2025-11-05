from single_responsibility.exercise_3.classes.order import Order
from single_responsibility.exercise_3.classes.order_details import OrderDetails

if __name__ == "__main__":
     s = Order(["banana","pizza"],45)
     OrderDetails.print_invoice(s.items,s.total_price)