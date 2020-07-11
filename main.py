from main.nepali import nepali_date
from main.english import english_date
from time import sleep

running = True


def merger():
    merger = f'{nepali_date()} : {english_date()}'
    print("\r", merger, end="")
    sleep(1)


while running:
    merger()

# ? Ouptuts >> Ashadh 27 : 10.47.46 : July 11, Saturday
