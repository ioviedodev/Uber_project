from carcustomized import CarCustomized

class UberVan(CarCustomized):
    
    def __init__(self, id,number_plate, category, assembly_date, enrolled, brand, model, enrrollment_date, passengers, capacity, driver, seat_material, type_car_accepted):
        super.__init__(id,number_plate, category, assembly_date, enrolled, brand, model, enrrollment_date, passengers, capacity, driver, seat_material, type_car_accepted)