import string
from account import Account
from driverlicense import DriverLicense

class Driver(Account):

    status      =   string
    license     =   DriverLicense
    
    def __init__(self, id, full_name, dni, telephone, creation_date, last_login_date, role, reputation, email, password, country, city, status, license):
        super().__init__(id, full_name, dni, telephone, creation_date, last_login_date, role, reputation, email, password, country, city)
        self.status = status
        self.license = license

    def print_object(self):
        super().print_object()
        print("Driver layer")
        print("status            : "+ self.status);
        self.license.print_object()

