import threading

event = threading.Event()
user_input = 0

def eventHandler():
    global user_input
    print("Waiting for the event!")
    event.wait()
    print("Event is triggered!")
    print(f"User input is {user_input}")
    if user_input < 10:
        print(f"{user_input} doubled is {user_input ** 2}")
    else:
        print("Value entered is too big!") 
    
t = threading.Thread(target=eventHandler)
t.start()

x = input("Do you want to double a number? (y/n) ")
if x == "y":
    user_input = int(input("Enter the number: "))
    event.set()
