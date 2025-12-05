#Access List Items in Python
a = [10, 20, 30, 40, 50]
# Accessing the first item
print(a[0])  
# Accessing the last item
print(a[-1])

#Using List Comprehension
a = [10, 20, 30, 40, 50]
# Create a new list with items greater than 20
b = [item for item in a if item > 20]
print(b)

#Using List Slicing
a = [10, 20, 30, 40, 50]
# Get a slice of the list from index 1 to 3
print(a[1:4])

#Using Loop
a = [10, 20, 30, 40, 50]
# Loop through the list and print each item
for item in a:
    print(item)

arr=[54,43,2,1,5]
print(arr[0::])
print(len(arr))
print(sum(arr))
for i,a in enumerate(arr):
    print(a-1,end=" ")


b=[]
c=(1,2,3)
b.append(c)
print(b)