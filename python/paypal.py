from payment import Payment

class Paypal(Payment):
    email       =   str

    def __init__ (self, id, status, executed_date, email):
        super().__init__(id, status, executed_date)
        self.email = email

    def print_object(self):
        super().print_object()
        print("Paypal Layer");
        print("email: "+ self.email);

    