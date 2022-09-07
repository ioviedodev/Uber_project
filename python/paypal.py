from payment import Payment

class Paypal(Payment):
    email       =   str

    def __init__ (self, id, status, executed_date, email):
        super().__init__(id, status, executed_date)
        self.email = email

    def print_paypal(self):
        self.print_object()
        print("email: "+ self.email);

    