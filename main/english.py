from datetime import datetime
from time import sleep

#? FORMAT 17:00:01: Thursday, April 16

def english_date():
	now = datetime.now()
	return now.strftime('%H.%M.%S : %B %e, %A')