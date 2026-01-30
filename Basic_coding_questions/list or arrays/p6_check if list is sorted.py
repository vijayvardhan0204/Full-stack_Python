lst = list(map(int, input("Enter elements: ").split()))
flag = True

for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
        flag = False
        break

if flag:
    print("List is sorted")
else:
    print("List is not sorted")
