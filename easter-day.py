import datetime
from typing import List


class EasterChallenge2022Python:

    @staticmethod
    def calculate_easter_sunday(year: int) -> datetime.datetime:
        # scenario 1
        "Returns Easter as a date object."
        a = year % 19
        b = year // 100
        c = year % 100
        d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
        e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
        f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
        month = f // 31
        day = f % 31 + 1 
        easter_day =  datetime.datetime(year, month, day)  
        return easter_day
        

    @staticmethod
    def calculate_easter_days(year: int) -> List[datetime.datetime]:
        # scenario 2
        a = year % 19
        b = year // 100
        c = year % 100
        d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
        e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
        f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
        month = f // 31
        day = f % 31 + 1 

        datetime_list = []

        easter_day =  datetime.datetime(year, month, day)
        f = easter_day - datetime.timedelta(days=2)
        m = easter_day + datetime.timedelta(days=1)

        datetime_list.append(f)
        datetime_list.append(easter_day)
        datetime_list.append(m)
        

        return datetime_list
        

year = EasterChallenge2022Python()
print(year.calculate_easter_days(2022))