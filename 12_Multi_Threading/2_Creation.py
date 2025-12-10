import threading

def greet():
    print("Hello from thread")

# thread creation
mythread=threading.Thread(target=greet)

print("Thread Created")