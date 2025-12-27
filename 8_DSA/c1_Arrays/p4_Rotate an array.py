# Python Program to left rotate the array by d positions

# Approach 1 (Using Juggling algorithm)

# Function to rotate an array by d elements to the left
import math

def rotateArr(arr, d):
    n = len(arr)          # size of array

    # Handle the case where d > size of array
    d %= n

    # Number of cycles based on GCD of n and d
    cycles = math.gcd(n, d)

    # Loop through each cycle
    for i in range(cycles):
        startEle = arr[i]     # store starting element of current cycle
        currIndx = i          # current index starts from cycle index

        # Rotate elements within the current cycle
        while True:
            nextIndx = (currIndx + d) % n  # calculate next index
            if nextIndx == i:              # cycle completed
                break
            arr[currIndx] = arr[nextIndx]  # move next element to current position
            currIndx = nextIndx             # update current index

        # Place the stored element in its correct position
        arr[currIndx] = startEle



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