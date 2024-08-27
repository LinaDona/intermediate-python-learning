import threading
import time


path = "text.txt"
txt = ""

def readFile():
    global path, txt
    while True:
        with open(path, "r") as f:
            txt = f.read()
        time.sleep(3)

def printLoop():
    for x in range(30):
        print(txt)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printLoop)

t1.start()
t2.start()