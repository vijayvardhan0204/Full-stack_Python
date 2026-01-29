lst = list(map(int, input("Enter elements: ").split()))
smallest = lst[0]

for i in lst:
    if i < smallest:
        smallest = i

print("Smallest element:", smallest)
