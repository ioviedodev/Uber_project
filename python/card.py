from datetime import datetime
from payment import Payment

class Card(Payment):
    serial          =   str
    expedition_date =   datetime
    expiration_date =   datetime
    cvc             =   str
    owner_name      =   str

    def __init__ (self, serial, expedition_date, expiration_date, cvc, owner_name):
        self.serial = serial
        self.expedition_date = expedition_date
        self.expiration_date = expiration_date
        self.cvc = cvc
        self.owner_name = owner_name

    def print_card(self):
        self.print_object()
        print("status: "+ self.status);
        print("expedition_date: ", self.expedition_date.strftime("%d/%m/%Y, %H:%M:%S"));
        print("expiration_date: ", self.expiration_date.strftime("%d/%m/%Y, %H:%M:%S"));
        print("cvc: "+ self.cvc);
        print("owner_name: "+ self.owner_name);
          