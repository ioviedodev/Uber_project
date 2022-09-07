from datetime import datetime
import pytz

from car import Car
from account import Account

def get_datetime_by_timezone(timezone: str)->datetime:
    timezone = pytz.timezone(timezone)
    date_time=datetime.now(timezone)
    return date_time

def main():
    
    timezone="America/Bogota"
    date_now=get_datetime_by_timezone(timezone)
    
    car = Car(1,"GTX3465","TIPO_B",date_now,True,"TESLA","X3",date_now,2,5, Account(1,"Cristiana Segovia","19874512","+45123581",date_now,date_now,"driver",0,"testing@gmail.com","pass123456","Colombia","Cali"))
 
    car.car_print()



if __name__ == "__main__":
    main()