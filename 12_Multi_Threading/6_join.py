import threading
import time

def fun():
    time.sleep(2)
    print("Thread work done")

t = threading.Thread(target=fun)
t.start()

t.join()      # Main thread waits for t to finish
print("Main thread completed")
