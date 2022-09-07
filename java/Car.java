import java.time.LocalDateTime;

public class Car {
    Integer id;
    String number_plate;
    String category;
    LocalDateTime assembly_date;
    Boolean enrolled;
    String brand;
    String model;
    LocalDateTime enrrolment_date;
    Integer passengers;
    Integer capacity;
    Account driver;

    public Car(String number_plate, Account driver)
    {
        this.number_plate=number_plate;
        this.driver=driver;
    }

    void car_print_object()
    {
        System.out.println("Car");
        System.out.println("capacity: "+ this.capacity);
        System.out.println("brand: "+ this.brand);
        System.out.println("assembly_date: "+ this.assembly_date);
        System.out.println("number_plate: "+ this.number_plate);
        System.out.println("category: "+ this.category);
        System.out.println("enrolled: "+ this.enrolled);
        System.out.println("model: "+ this.model);
        System.out.println("enrrolment_date: "+ this.enrrolment_date);
        System.out.println("passengers: "+ this.passengers);
        System.out.println("capacity: "+ this.capacity);
        this.driver.print_object();
    }
}
