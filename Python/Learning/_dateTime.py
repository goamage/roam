import time
from datetime import datetime


# same time
def displayTime(time=datetime.now()):
	print(time.strftime('%B %d, %Y %H:%M:%S'))

#new time
def displayTime(time=None):
	if time is None:
		time=datetime.now()
	print(time.strftime('%B %d, %Y %H:%M:%S'))

displayTime()
time.sleep(1)
displayTime()