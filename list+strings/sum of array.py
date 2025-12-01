# Sum of array
# Method 1
arr=[1,2,3,4]
add=0
for i in arr:
    add=add+i
print(add)

# Method 2
# using sum()
arr=[12,2,3,4,1]
ans=sum(arr)
print(ans)

# Method 3
# Using enumerate function 
list=[1,4,5,3,19]
s=0
for i,a in enumerate(list):
    print(i,a) #enumerate(numbers) gives both index (i) and value (a).
    s+=a
print(s)