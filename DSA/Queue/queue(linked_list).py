class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.length=0
    def enqueue(self,element):
        new_node=Node(element)
        if self.rear is None:
            self.front=self.rear=new_node
            self.length+=1
            return
        self.rear.next=new_node
        self.rear=new_node
        self.length+=1
    
    def dequeue(self):
        if self.isEmpty():
            return "queue is empty"
        temp=self.front
        self.front=temp.next
        self.length-=1
        if self.front is None:
            self.rear=None
        return temp.value
    
    def peek(self):
        if self.isEmpty():
            return "queue is empty"
        return self.front.value
    
    def isEmpty(self):
        return self.length==0
    
    def size(self):
        return self.length
    
    def display(self):
        temp=self.front
        while temp:
            print(temp.value,end=" ->")
            temp=temp.next
        print()

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", end="")
myQueue.display()
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", end="")
myQueue.display()
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())