class Main {
    public static void main(String[] args) {
        System.out.println("Hola mundo");

        Car car = new Car("GTX3465",new Account("Derek Tristan", "1130750917"));
        car.capacity=5;
        car.brand="GM";
        
        car.car_print_object();

    }
}