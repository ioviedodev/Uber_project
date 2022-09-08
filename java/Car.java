import java.time.LocalDateTime;

public class Car {
    private Integer id;
    private String number_plate;
    private String category;
    private LocalDateTime assembly_date;
    private Boolean enrolled;
    private String brand;
    private String model;
    private LocalDateTime enrrolment_date;
    protected Integer passengers;
    protected Integer capacity;
    private Account driver;
    private int places_availables;

    public Car(String number_plate, Account driver)
    {
        this.number_plate=number_plate;
        this.driver=driver;
    }

    void print_object()
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
        System.out.println("places_availables: "+ this.places_availables);
        this.driver.print_object();
    }

    public Integer getPassengers()
    {
        return this.passengers;
    }

    public void setPassengers(Integer passengers)
    {
        this.passengers=passengers;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getNumber_plate() {
        return number_plate;
    }

    public void setNumber_plate(String number_plate) {
        this.number_plate = number_plate;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public LocalDateTime getAssembly_date() {
        return assembly_date;
    }

    public void setAssembly_date(LocalDateTime assembly_date) {
        this.assembly_date = assembly_date;
    }

    public Boolean getEnrolled() {
        return enrolled;
    }

    public void setEnrolled(Boolean enrolled) {
        this.enrolled = enrolled;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public LocalDateTime getEnrrolment_date() {
        return enrrolment_date;
    }

    public void setEnrrolment_date(LocalDateTime enrrolment_date) {
        this.enrrolment_date = enrrolment_date;
    }

    public Integer getCapacity() {
        return capacity;
    }

    public void setCapacity(Integer capacity) {
        this.capacity = capacity;
    }

    public Account getDriver() {
        return driver;
    }

    public void setDriver(Account driver) {
        this.driver = driver;
    }

    public int getPacesAvailables() {
        return this.places_availables;
    }

    public void setPacesAvailables(int places_availables) {
        this.places_availables = places_availables;
    }
}
