public class UberPool extends CarBasic{
    
    public UberPool(String number_plate, Account driver)
    {
        super(number_plate, driver);
    }

    @Override
    public void setCapacity(Integer capacity) {
        if(capacity == 4)
        {
            super.capacity=capacity;            
        }
        else
        {
            System.out.println("Please insert a valid capacity");
        }        
    }
}
