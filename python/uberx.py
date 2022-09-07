from carbasic import CarBasic


class UberX(CarBasic):
    
    def __init__ (self, id,number_plate, category, assembly_date, enrolled, brand, model, enrrollment_date, passengers, capacity, driver,places_available,set_places):
        super.__init__(id,number_plate, category, assembly_date, enrolled, brand, model, enrrollment_date, passengers, capacity, driver,places_available,set_places)
