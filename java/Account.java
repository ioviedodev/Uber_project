import java.time.LocalDateTime;

public class Account {
    Integer id;
    String full_name;
    String dni;
    String telephone;
    LocalDateTime creation_date;
    LocalDateTime last_login_date;
    String role;
    float reputation;    
    String email;
    String password;
    String country;
    String city;

    public Account(String full_name, String dni)
    {
        this.full_name = full_name;
        this.dni = dni;
    }

    public void print_object()
    {
        System.out.println("full_name: "+ this.full_name);
        System.out.println("dni: "+ this.dni);
    }
}
