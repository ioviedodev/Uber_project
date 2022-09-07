class Car
{
    // constructor(id,number_plate, category, assembly_date, enrolled, brand, model, enrrolment_date, passengers, capacity)
    // {
    //     this.id=id;
    //     this.number_plate=number_plate;
    //     this.category=category;
    //     this.assembly_date=assembly_date;
    //     this.enrolled=enrolled;
    //     this.brand=brand;
    //     this.model=model;
    //     this.enrrolment_date=enrrolment_date;
    //     this.passengers=passengers;
    //     this.capacity=capacity;
    // }
    constructor(number_plate, category, brand, model, driver)
    {
        this.number_plate=number_plate;
        this.category=category;
        this.brand=brand;
        this.model=model;
        this.driver=driver;
    }

    print_object = function ()
    {
        console.log(this.number_plate)
        console.log(this.category)
        console.log(this.brand)
        console.log(this.model)
        this.driver.print_object()
    }
}