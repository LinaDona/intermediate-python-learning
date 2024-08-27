import threading

def function1():
    for x in range(10):
        print(x)

def function2():
    for x in range(10, 20):
        print(x)

'''
- Thread(target=f) calls the ctr for the Thread class
- Each calls creates a thread (instance)
- target specifies the function that the thread should execute
'''
t1 = threading.Thread(target=function1) 
t2 = threading.Thread(target=function2)

# start the threads
t1.start()
t2.start()

# the main thread should wait for both threads to execute before continuing
t2.join() # joining the 2nd thread first somehow made execution more.. random
t1.join()

print("Main thread got control again!")