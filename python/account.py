from datetime import datetime


class Account:
    id              =   int   
    full_name       =   str
    dni             =   str
    telephone       =   str
    creation_date   =   datetime
    last_login_date =   datetime
    role            =   str
    reputation      =   float 
    email           =   str
    password        =   str
    country         =   str
    city            =   str

    def __init__(self, id, full_name, dni, telephone, creation_date, last_login_date, role, reputation, email, password, country, city):
        self.id              = id              
        self.full_name       = full_name       
        self.dni             = dni             
        self.telephone       = telephone       
        self.creation_date   = creation_date   
        self.last_login_date = last_login_date 
        self.role            = role            
        self.reputation      = reputation      
        self.email           = email           
        self.password        = password        
        self.country         = country         
        self.city            = city            

    def print_object(self):
        print("id              : "+ str(self.id));  
        print("full_name       : "+ self.full_name);
        print("dni             : "+ self.dni);
        print("telephone       : "+ self.telephone);
        print("creation_date: ", self.creation_date.strftime("%d/%m/%Y, %H:%M:%S"));
        print("last_login_date: ", self.last_login_date.strftime("%d/%m/%Y, %H:%M:%S"));
        print("role            : "+ self.role);
        print("reputation      : "+ str(self.reputation));
        print("email           : "+ self.email);
        print("password        : "+ self.password);
        print("country         : "+ self.country);
        print("city            : "+ self.city);