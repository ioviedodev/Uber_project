class Main {
    public static void main(String[] args) {
        System.out.println("Hola mundo");

        Account driver = new Account("Derek Tristan", "1130750917");
        Car car = new Car("GTX3465",driver);
        car.setBrand("GM");
        car.print_object();

        
        UberX uberx = new UberX("P541235", driver);
        uberx.setPassengers(5);
        System.out.print(uberx.getPassengers());


    }
}