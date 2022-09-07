
from car import Car

class CarBasic(Car):
    places_available    = int
    set_places          = bool

    def __init__ (self, id,number_plate, category, assembly_date, enrolled, brand, model, enrrollment_date, passengers, capacity, driver,places_available,set_places):
        super.__init__(id,number_plate, category, assembly_date, enrolled, brand, model, enrrollment_date, passengers, capacity, driver)
        self.places_available = places_available
        self.set_places = set_places
