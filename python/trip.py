from datetime import datetime
from payment import Payment
from user import User
from car import Car
from route import Route

class trip:
    id              =   int
    created_trip    =   datetime
    init_trip       =   datetime
    finish_trip     =   datetime
    status          =   str
    cost            =   float
    user            =   User
    car             =   Car
    route           =   Route
    payment         =   Payment

    def __init__(self, id, created_trip, init_trip, finish_trip,status,cost, user, car, route,payment):
        self.id             =   id
        self.created_trip   =   created_trip
        self.init_trip      =   init_trip
        self.finish_trip    =   finish_trip
        self.status         =   status
        self.cost           =   cost
        self.user           =   user
        self.car            =   car
        self.route          =   route
        self.payment        =   payment

    def print_object(self):
        print("id       : "+ str(self.id));
        print("created_trip: ", self.created_trip.strftime("%d/%m/%Y, %H:%M:%S"));
        print("init_trip: ", self.init_trip.strftime("%d/%m/%Y, %H:%M:%S"));
        print("finish_trip: ", self.finish_trip.strftime("%d/%m/%Y, %H:%M:%S"));
        print("status       : "+ self.status);
        print("cost       : "+ str(self.cost));
        self.user.print_user()
        self.car.car_print()
        self.route.print_object()
        self.payment.print_object()
        
    
