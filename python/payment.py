
from datetime import datetime



class Payment:
    id              = int
    status          = str
    executed_date   = datetime

    def __init__(self, id, status, executed_date):
        self.id = id
        self.status = status
        self.executed_date = executed_date
    
    def print_object(self):
        print("id: "+ str(self.id));
        print("status: "+ self.status);
        print("executed_date: ", self.executed_date.strftime("%d/%m/%Y, %H:%M:%S"));