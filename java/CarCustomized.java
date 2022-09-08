import java.util.ArrayList;
import java.util.Map;

public class CarCustomized extends Car{

    Map<String, Map<String,Integer>> type_car_accepted;
    ArrayList<String> seat_material;

    public CarCustomized(String number_plate, Account driver, Map<String, Map<String,Integer>> type_car_accepted, ArrayList<String> seat_material)
    {
        super(number_plate, driver);
        this.type_car_accepted = type_car_accepted;
        this.seat_material = seat_material;
    }

    @Override
    void print_object()
    {
        System.out.println("CarCustomized layer");
        super.print_object();
        System.out.println("type_car_accepted: "+ this.type_car_accepted);
        System.out.println("seat_material: "+ this.seat_material);
    }
}
