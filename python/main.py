from datetime import datetime
import imp
import pytz

from car import Car
from account import Account
from driver import Driver
from driverlicense import DriverLicense

def get_datetime_by_timezone(timezone: str)->datetime:
    timezone = pytz.timezone(timezone)
    date_time=datetime.now(timezone)
    return date_time

def main():
    
    timezone="America/Bogota"
    date_now=get_datetime_by_timezone(timezone)
    
    driver_license=DriverLicense(1,"Active","TIPO_A",date_now,date_now)
    driver = Driver(1,"Daniel Zambrano","1145248","+4599845",date_now,date_now,"driver",0,"danielzambrano@gmail.com","pass7898","Peru","Lima","Active", driver_license)
    driver.print_driver()

    car = Car(1,"GTX3465","TIPO_B",date_now,True,"TESLA","X3",date_now,2,5, driver)
    car.car_print()



if __name__ == "__main__":
    main()