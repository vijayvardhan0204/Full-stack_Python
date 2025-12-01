n=int(input("enter number of elements"))
arr=(map(int,input().split()))
#This takes the next line of input, splits it by spaces, and converts each piece into an integer.
a=list(set(arr))
a.sort() 
print(a[-2])


''''example
input=7,4,5,6,7,7
then if we sort we get 4,5,6,7,7,7
so 1st we changing list to set to eliminate duplicates'''


#for sets
nums = {5, 3, 1, 4, 2}
sorted_list = sorted(nums)   # returns a sorted list
print(sorted_list)
