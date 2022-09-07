from datetime import datetime
import string

class DriverLicense:

    id                  =   int
    status              =   string
    category_license    =   string
    expedition_date     =   datetime
    expiration_date     =   datetime

    def __init__(self, id, status, category_license, expedition_date, expiration_date):
        self.id                 =   id
        self.status             =   status
        self.category_license   =   category_license
        self.expiration_date    =   expiration_date
        self.expedition_date    =   expedition_date
    
    def print_object(self):
        print("DriverLicense Layer")
        print("id: "+ str(self.id));
        print("status: "+ self.status);
        print("category_license: "+ self.category_license);
        print("expiration_date: ", self.expiration_date.strftime("%d/%m/%Y, %H:%M:%S"));
        print("expedition_date: ", self.expedition_date.strftime("%d/%m/%Y, %H:%M:%S"));

