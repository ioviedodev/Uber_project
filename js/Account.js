class Account
{
    // constructor(full_name, dni, telephone, role, email, password, country, city)
    // {
    //     this.id=0;
    //     this.full_name=full_name;
    //     this.dni=dni;
    //     this.telephone=telephone;
    //     this.creation_date;
    //     this.last_login_date;
    //     this.role=role;
    //     this.reputation=5;    
    //     this.email=email;
    //     this.password=password;
    //     this.country=country;
    //     this.city=city;
    // }

    constructor(full_name, dni)
    {
        this.full_name=full_name;
        this.dni=dni;
    }

    print_object = function ()
    {
        console.log(this.full_name)
        console.log(this.dni)
    }

}