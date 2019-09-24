# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 
import time
def print_cube(num): 
    while(True):
        print("from 1st Thread ",time.ctime())
        time.sleep(60)


def print_square(num):
    while(True):
        print("From 2nd thread",time.ctime())
        time.sleep(120)

if __name__ == "__main__": 
	# creating thread 
	t1 = threading.Thread(target=print_square, args=(10,)) 
	t2 = threading.Thread(target=print_cube, args=(10,)) 

	# starting thread 1 
	t1.start() 
	# starting thread 2 
	t2.start() 

	# both threads completely executed 
	print("Done!") 
