import threading
import time

x = 8192

# locks the access to the resource: only one thread can access at a time in 
# an acquire() ==> release() fashion.
lock = threading.Lock() 

def double():
    # global keyword enables this function to change the global variable x
    # otheriwse, it can only read it.
    global x, lock
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached maximum!")
    lock.release()

def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached minimum!")
    lock.release()

t1 = threading.Thread(target=double)
t2 = threading.Thread(target=halve)

t2.start()
t1.start()

