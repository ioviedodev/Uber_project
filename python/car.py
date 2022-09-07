from datetime import datetime
from account import Account


class Car:
    id              =   int
    number_plate    =   str
    category        =   str
    assembly_date   =   datetime
    enrolled        =   bool
    brand           =   str
    model           =   str
    enrrolment_date =   datetime
    passengers      =   int
    capacity        =   int
     

    def __init__(self, id,number_plate, category, assembly_date, enrolled, brand, model, enrrollment_date, passengers, capacity, driver):
        self.id              = id              
        self.number_plate    = number_plate    
        self.category        = category        
        self.assembly_date   = assembly_date   
        self.enrolled        = enrolled        
        self.brand           = brand           
        self.model           = model           
        self.enrrolment_date = enrrollment_date 
        self.passengers      = passengers      
        self.capacity        = capacity        
        self.driver          = driver

    def car_print(self):
        print("capacity: "+ str(self.capacity));
        print("brand: "+ self.brand);
        print("assembly_date: ", self.assembly_date.strftime("%d/%m/%Y, %H:%M:%S"));
        print("number_plate: "+ self.number_plate);
        print("category: "+ self.category);
        print("enrolled: "+ str(self.enrolled));
        print("model: "+ self.model);
        print("enrrolment_date: "+ self.enrrolment_date.strftime("%d/%m/%Y, %H:%M:%S"));
        print("passengers: "+ str(self.passengers));
        print("capacity: "+ str(self.capacity));
        self.driver.print_object()














