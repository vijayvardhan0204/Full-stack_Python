import threading

def display():
    print("Thread is now running.")

# Create thread
t = threading.Thread(target=display)

# Start thread
t.start()

print("Main program finished")
