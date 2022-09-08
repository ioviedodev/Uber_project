from carbasic import CarBasic


class UberX(CarBasic):
    
    def __init__ (self, id,number_plate, category, assembly_date, enrolled, brand, model, enrrollment_date, passengers, capacity, driver,places_available):
        super().__init__(id,number_plate, category, assembly_date, enrolled, brand, model, enrrollment_date, passengers, capacity, driver,places_available)

    def set_capacity(self, capacity):
        if capacity==4:
            self.capacity = capacity
        else:
            print("Set a valid capacity")

    def car_print(self):
        print("Uberx")
        super().car_print()
