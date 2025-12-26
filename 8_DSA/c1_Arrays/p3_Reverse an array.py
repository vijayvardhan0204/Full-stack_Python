


# Approach 1
def reverseArray(arr):
    
    # Initialize left to the beginning 
    # and right to the end
    left = 0
    right = len(arr) - 1
  
    # Iterate till left is less than right
    while left < right:
        
        # Swap the elements at left
        # and right position
        arr[left], arr[right] = arr[right], arr[left]
      
        # Increment the left pointer
        left += 1
      
        # Decrement the right pointer
        right -= 1

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    reverseArray(arr)
  
    for i in range(len(arr)):
        print(arr[i], end=" ")



# Approach 2
def reverseArray(arr):
    n = len(arr)
    
    # Iterate over the first half 
    # and for every index i, swap
    # arr[i] with arr[n - i - 1]
    for i in range(n // 2):
        temp = arr[i]
        arr[i] = arr[n - i - 1]
        arr[n - i - 1] = temp

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    reverseArray(arr)
  
    for i in range(len(arr)):
        print(arr[i], end=" ")


# Time Complexity: O(n), the loop runs through half of the array, so it's linear with respect to the array size.
# Auxiliary Space: O(1), no extra space is required, therefore we are reversing the array in-place.