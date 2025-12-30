# Maximum subarray sum(circular)

def Maxsubarray(arr):
    # Initialize total sum with first element
    totalSum = arr[0]

    # For normal maximum subarray sum (Kadane’s Algorithm)
    currMaxSum = arr[0]   # Current maximum ending at index i
    maxSum = arr[0]       # Overall maximum subarray sum

    # For minimum subarray sum (used in circular case)
    currMinSum = arr[0]   # Current minimum ending at index i
    minSum = arr[0]       # Overall minimum subarray sum

    # Start loop from index 1 because arr[0] is already used
    for i in range(1, len(arr)):

        # Kadane's algorithm for maximum subarray sum
        # Either extend previous subarray or start new subarray
        currMaxSum = max(arr[i], currMaxSum + arr[i])
        maxSum = max(maxSum, currMaxSum)

        # Kadane's algorithm for minimum subarray sum
        # Used to calculate circular subarray sum
        currMinSum = min(arr[i], currMinSum + arr[i])
        minSum = min(minSum, currMinSum)

        # Keep track of total sum of the array
        totalSum += arr[i]

    # Edge case:
    # If all numbers are negative, circular sum becomes 0
    # So we return the normal maximum subarray sum
    if totalSum == minSum:
        return maxSum

    # Circular subarray sum formula
    circularSum = totalSum - minSum

    # Return the maximum of normal and circular subarray sums
    return max(maxSum, circularSum)


# Driver code
if __name__ == "__main__":
    arr = [10, -3, -4, 7, 6, 5, -4, -1]
    print(Maxsubarray(arr))
