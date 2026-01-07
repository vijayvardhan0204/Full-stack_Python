stack=[]

# push
stack.append('A')
stack.append('B')
stack.append('C')

# Display
print("stack:",stack)

# peek(last element)
top_element=stack[-1]
print(f"top element is {top_element}")

# Pop(deleting)
popped_element=stack.pop()
print(f"popped:{popped_element}")

# Stack after Pop
print("Stack after Pop: ", stack)

# isEmpty
is_empty=not bool(stack)
print("isempty:",is_empty)

# size
print("size:",len(stack))
