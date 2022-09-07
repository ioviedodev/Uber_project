
public class CarBasic extends Car {
    int places_availables;

    public CarBasic(String number_plate, Account driver, int places_availables)
    {
        super(number_plate, driver);
        this.places_availables = places_availables;
    }
}
    