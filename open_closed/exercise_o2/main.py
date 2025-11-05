import classes.credit_card
import classes.pay_pal

if __name__ == "__main__":
    c = classes.credit_card.CreditCard(23)
    c.pay()
    p = classes.pay_pal.PayPal(45)
    p.pay()