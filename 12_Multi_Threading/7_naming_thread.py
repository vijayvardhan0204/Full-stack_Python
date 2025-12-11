import threading
import time

def show():
    print("Running:", threading.current_thread().name)

t1 = threading.Thread(target=show, name="Worker-1")
t2 = threading.Thread(target=show, name="Worker-2")

t1.start()
t2.start()
