
instack = []
outstack = []
def push(i):
    instack.append(i)
def pop():
    if not outstack:
        while instack:
            outstack.append(instack.pop())
    return outstack.pop()

def peek():
    if not outstack:
        while instack:
            outstack.append(instack.pop())
    return outstack[-1]
def empty():
    return not instack and not outstack


push(1)
push(2)
print(peek())   # 1
print(pop())    # 1
print(empty())  # False

