from car import Car

class CarCustomized(Car):
    seat_material       = []
    type_car_accepted   = []


    def __init__(self, id,number_plate, category, assembly_date, enrolled, brand, model, enrrollment_date, passengers, capacity, driver, seat_material, type_car_accepted):
        super.__init__(id,number_plate, category, assembly_date, enrolled, brand, model, enrrollment_date, passengers, capacity, driver)
        self.type_car_accepted = type_car_accepted
        self.seat_material = seat_material

