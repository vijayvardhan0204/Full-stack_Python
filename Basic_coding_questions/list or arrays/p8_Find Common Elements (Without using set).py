list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))

common = []

for i in list1:
    if i in list2 and i not in common:
        common.append(i)

print("Common elements:", common)
