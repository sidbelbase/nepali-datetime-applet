from main.nepali import nepali_date
from main.english import english_date
from time import sleep

running= True;

#? Baisakh 9 : 17:00:01 : April 16, Thursday

def merger():
	merger= f'{nepali_date()} : {english_date()}'
	print("\r", merger, end="")
	sleep(1)

while running:
	merger()