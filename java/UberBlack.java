import java.util.ArrayList;
import java.util.Map;

public class UberBlack extends CarCustomized{
    public UberBlack(String number_plate, Account driver, Map<String, Map<String,Integer>> type_car_accepted, ArrayList<String> seat_material)
    {
        super(number_plate, driver, type_car_accepted, seat_material);
    }
}
