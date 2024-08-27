# Queues are data structures similar to lists and sequences in python.
# - They differ in the way elements are entered and extracted.
# - They are very useful to use between threads (dividing the workload on one shared data) by 
#   exchanging information SAFELY between threads.
# - There are 3 classes in the queue module: FIFO, LIFO, and PriorityQueue whose entries are sorted.

import queue
import time
import threading

#-------------------------FIFO & LIFO------------------------
qFIFO = queue.Queue()
qLIFO = queue.LifoQueue()


list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for nbr in list:
    qFIFO.put(nbr) # 10 goes in first (and goes out first)
    qLIFO.put(nbr) # 10 goes in first (and goes out last)

def access(id):
    while(not qFIFO.empty() and not qLIFO.empty()):
        print(f"{id} is getting queue element: {qFIFO.get()}")
        time.sleep(1)
        print(f"{id} is getting LIFO queue element: {qLIFO.get()}")

t1 = threading.Thread(target=access, args=(1,))
t2 = threading.Thread(target=access, args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()


#------------------------- Priority -------------------------

qPriority = queue.PriorityQueue()

# ENTRY = (Priority, Element): for "Priority", the lower the number, the more 'important' it is.
qPriority.put((1, "Hello"))
qPriority.put((3, 'L'))
qPriority.put((4, 4.09))
qPriority.put((10, 45))

while not qPriority.empty():
    entry = qPriority.get()
    print(f"{entry}: Element {entry[1]} with Priority {entry[0]}")