# Queue(lists)

queue=[]

# Enqueue(Add element)
queue.append('A')
queue.append('B')
queue.append('C')

# peek(first element)

frontElement=queue[0]
print("peek:",frontElement)

# Dequeue(delete 1st element)
print("Dequeue:",queue.pop(0))
print("Queue after Dequeue: ", queue)

# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))