from datetime import datetime
import imp
import pytz

from car import Car
from trip import Trip
from card import Card
from route import Route
from user import User
from driver import Driver
from uberx import UberX
from driverlicense import DriverLicense
from uberblack import UberBlack

def get_datetime_by_timezone(timezone: str)->datetime:
    timezone = pytz.timezone(timezone)
    date_time=datetime.now(timezone)
    return date_time

def main():
    
    timezone="America/Bogota"
    date_now=get_datetime_by_timezone(timezone)
    
#create a driver
    print("****create a driver****")
    driver_license=DriverLicense(1,"Active","TIPO_A",date_now,date_now)
    driver = Driver(1,"Daniel Zambrano","1145248","+4599845",date_now,date_now,"driver",0,"danielzambrano@gmail.com","pass7898","Peru","Lima","Active", driver_license)
    driver.print_object()

#create a UberX
    print("****create a UberX****")
    uberx = UberX(1,"GTX3465","TIPO_B",date_now,True,"TESLA","X3",date_now,2,5, driver, 4)
    uberx.car_print()
    uberx.set_capacity(5)


#create a user
    print("****Creating a user****")
    user=User(1,"Daniel Zambrano","1145248","+4599845",date_now,date_now,"driver",0,"danielzambrano@gmail.com","pass7898","Peru","Lima",0)
    user.print_object()

#create a route
    print("****Creating a route****")
    route = Route(1,[1,1],[5,4])
    route.print_object()

#create a card
    print("****Creating a card****")
    card=Card(1,"Active",date_now,"589455521",date_now,date_now,"125","Diego Maradona")
    card.print_object()

#create a trip
    print("****create a trip****")
    trip = Trip(1, date_now,date_now,date_now,"Requested",5,user,uberx,route,card)
    trip.print_object()

if __name__ == "__main__":
    main()