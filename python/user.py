from account import Account

class User(Account):
    number_trips    =   int
    def __init__(self, id, full_name, dni, telephone, creation_date, last_login_date, role, reputation, email, password, country, city, number_trips):
        super().__init__(id, full_name, dni, telephone, creation_date, last_login_date, role, reputation, email, password, country, city)
        self.number_trips = number_trips

    def print_object(self):
        super().print_object()
        print("User layer")
        print("number_trips              : "+ str(self.number_trips));  
        
