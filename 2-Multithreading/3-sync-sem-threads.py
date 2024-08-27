import threading
import time

# A semaphore limits access to a shared data to a finite number, meaning
# only a nbr of threads can access the shared data, and until one of these
# threads is done accessing, others wait.
semaphore = threading.BoundedSemaphore(value=5)

def access(thread_nbr):
    print(f'{thread_nbr} is trying to access!')
    semaphore.acquire()
    print(f'{thread_nbr} Granted access!')
    time.sleep(10)
    print(f'{thread_nbr} is now releasing')
    semaphore.release()

for thread_nbr in range(1, 11):
    t = threading.Thread(target=access, args=(thread_nbr,)) 
    t.start()
    time.sleep(1)

