from payment import Payment


class Cash(Payment):
    def __init__ (self, id, status, executed_date):
        super().__init__(id, status, executed_date)
    
    def print_cash(self):
        self.print_object()
