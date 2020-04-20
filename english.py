from datetime import datetime
from time import sleep

#? FORMAT 17:00:01: Thursday, April 16

now = datetime.now()

def time_string():
    return now.strftime('%H.%M.%S')


def date_string():
    return now.strftime('%A, %M %e')


def colonize_them():
    colon_between = f'{time_string()} : {date_string()}'
    while True:
        a = datetime.now()
        sleep(1)
        print("\r" + str(a), end="")


colonize_them()
