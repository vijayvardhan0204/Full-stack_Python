# Python program to find the second largest element in the array
# using one traversal

# function to find the second largest element in the array


def getSecondLargest(arr):
    n = len(arr)

    largest = -1
    secondLargest = -1

    # finding the second largest element
    for i in range(n) :

        # If arr[i] > largest, update second largest with
        # largest and largest with arr[i]
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]

        # If arr[i] < largest and arr[i] > second largest, 
        # update second largest with arr[i]
        elif arr[i] < largest and arr[i] > secondLargest:
            secondLargest = arr[i]

    return secondLargest

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))
