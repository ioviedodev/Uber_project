class CarCustomized extends Car
{
    constructor(number_plate, category, brand, model, driver, seat_material, type_car_accepted)
    {
        super(number_plate, category, brand, model, driver);
        this.seat_material=seat_material;
        this.type_car_accepted=type_car_accepted;
    }
}