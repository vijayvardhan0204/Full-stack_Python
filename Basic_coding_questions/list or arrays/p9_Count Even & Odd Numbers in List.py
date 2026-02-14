lst = list(map(int, input("Enter elements: ").split()))
even = 0
odd = 0

for i in lst:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even count:", even)
print("Odd count:", odd)
