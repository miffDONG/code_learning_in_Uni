package 상속.매개변수다형성;

public class DriverExample {
    public static void main(String[] args) {
        Driver driver = new Driver();

        Bus bus = new Bus();
        Taxi taxi = new Taxi();

        driver.driver(bus);
        driver.driver(taxi);
        
    }
}
