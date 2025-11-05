from open_closed.exercise_o2.classes.payment import Payment


class CreditCard(Payment):
    def __init__(self,amount):
        self.amount = amount

    def pay(self):
        print(f"{self.amount} paid by credit card")
