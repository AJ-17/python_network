'''
There is no multi threading in python normaly 
because of the global interpeter lock
what we do is know as psudo threading 
we use the downtime of other task and then keep switching them 
'''

import threading 
import time


done=False

def worker(a):
    counter=0
    while True:
            time.sleep(1)
            counter+=1;
            print(a,counter)


# we just run a fnx inside a thread
# daemon =True means when no other code is running then these fnx will also end 
# args is for argument to the fnx a , is required after all args other wise args will be counted as character like 'N : ' will be counted as 4 arg

threading.Thread(target=worker ,daemon=True,args=("N : ",)).start()
threading.Thread(target=worker ,daemon=True,args=("M : ",)).start()

input("Press enter to quit\n")