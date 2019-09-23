# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 
import datetime as dt
from time import sleep

t = dt.datetime.now()
minute_count = 0 


def print_cube(num): 
	""" 
	function to print cube of given num 
	"""
	while True:
    delta_minutes = (dt.datetime.now() -t).seconds / 60                
    if delta_minutes and delta_minutes != minute_count:
        print("1 Min has passed since the last print")
        minute_count = delta_minutes
    sleep(1) # Stop maxing out CPU

def print_square(num): 
	""" 
	function to print square of given num 
	"""
	while True:
    delta_minutes = (dt.datetime.now() -t).seconds / 120                
    if delta_minutes and delta_minutes != minute_count:
        print("2 Min has passed since the last print")
        minute_count = delta_minutes
    sleep(1) # Stop maxing out CPU

if __name__ == "__main__": 
	# creating thread 
	t1 = threading.Thread(target=print_square, args=(10,)) 
	t2 = threading.Thread(target=print_cube, args=(10,)) 

	# starting thread 1 
	t1.start() 
	# starting thread 2 
	t2.start() 

	# wait until thread 1 is completely executed 
	t1.join() 
	# wait until thread 2 is completely executed 
	t2.join() 

	# both threads completely executed 
	print("Done!") 
