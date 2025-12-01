# Bubble sort

mylist = [64, 34, 25, 12, 22, 11, 90, 5]
n=len(mylist)
for i in range(n-1):
    for j in range(n-i-1):
        if mylist[j]>mylist[j+1]:
            mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
print(mylist)