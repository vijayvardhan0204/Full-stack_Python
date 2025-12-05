
# Method 1
mylist=[64, 34, 25, 12, 22, 11, 90, 5]
for i in range(1,len(mylist)):
    j=i
    while mylist[j-1]>mylist[j] and j>0:
        mylist[j-1],mylist[j]=mylist[j],mylist[j-1]
        j -= 1
print(mylist)


# Method 2

mylist=[64, 34, 25, 12, 22, 11, 90, 5]
n=len(mylist)
for i in range(1,n):
    insert_index=i
    current_value=mylist.pop(i)
    for j in range(i-1,-1,-1):
        if mylist[j]>current_value:
            insert_index=j
    mylist.insert(insert_index,current_value)
print(mylist)