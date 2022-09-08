import java.util.ArrayList;
import java.util.Map;

public class UberVan extends CarCustomized
{
    public UberVan(String number_plate, Account driver, Map<String, Map<String,Integer>> type_car_accepted, ArrayList<String> seat_material)
    {
        super(number_plate, driver, type_car_accepted, seat_material);
    }
    
    @Override
    public void setCapacity(Integer capacity) {
        if(capacity == 6)
        {
            super.capacity=capacity;            
        }
        else
        {
            System.out.println("Please insert a valid capacity");
        }        
    }
}
