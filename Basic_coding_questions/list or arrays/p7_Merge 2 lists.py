list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))

merged = []

for i in list1:
    merged.append(i)
for i in list2:
    merged.append(i)

print("Merged list:", merged)
