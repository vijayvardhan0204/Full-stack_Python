# Bubble sort
'''Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.'''
# time complexity for Bubble Sort is: O(n2)

mylist = [64, 34, 25, 12, 22, 11, 90, 5]
n=len(mylist)
for i in range(n-1):
    for j in range(n-i-1):
        if mylist[j]>mylist[j+1]:
            mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
print(mylist)

'''The outer loop decides how many rounds of comparison you make.

The inner loop compares and swaps numbers next to each other.

Each round places the next largest number at its correct place on the right.

Therefore, every round needs one less comparison than the previous.'''