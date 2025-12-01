# Stack Class

class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
    
myStack=Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')

print("stack:",myStack.stack)
print("pop:",myStack.pop())
print("stack after pop:",myStack.stack)
print("peek:",myStack.peek())
print("isEmpty:",myStack.isEmpty())
print("length:",myStack.size())

