lst = list(map(int, input("Enter elements: ").split()))
result = []

for i in lst:
    if i not in result:
        result.append(i)

print("After removing duplicates:", result)
