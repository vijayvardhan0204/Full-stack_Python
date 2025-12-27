# Python Program to left rotate the array by d positions

# Approach 1 (Using Temporary Array)
# using temporary array

# Function to rotate array
def rotateArr(arr, d):
    n = len(arr)

    # Handle case when d > n
    d %= n
    
    # Storing rotated version of array
    temp = [0] * n

    # Copy last n - d elements to the front of temp
    for i in range(n - d):
        temp[i] = arr[d + i]

    # Copy the first d elements to the back of temp
    for i in range(d):
        temp[n - d + i] = arr[i]

    # Copying the elements of temp in arr
    # to get the final rotated array
    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2

    rotateArr(arr, d)

    # Print the rotated array
    for i in range(len(arr)):
        print(arr[i], end=" ")



# Approach 2(Using Reversal Algorithm)
# Function to rotate an array by d elements to the left
def rotateArr(arr, d):
    n = len(arr)

    # Handle the case where d > size of array
    d %= n

    # Reverse the first d elements
    reverse(arr, 0, d - 1)

    # Reverse the remaining n-d elements
    reverse(arr, d, n - 1)

    # Reverse the entire array
    reverse(arr, 0, n - 1)

# Function to reverse a portion of the array
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2
    
    rotateArr(arr, d)
  
    for i in range(len(arr)):
        print(arr[i], end=" ")