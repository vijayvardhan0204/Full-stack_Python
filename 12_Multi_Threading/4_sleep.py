import threading
import time

def countdown():
    for i in range(5,0,-1):
        print("Counting:",i)
        time.sleep(1)

t=threading.Thread(target=countdown)
t.start()