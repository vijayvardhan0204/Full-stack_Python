
# Approach 1(Greedy Min-Max Product - O(n) Time and O(1) Space)
def maxProduct(arr):

    n = len(arr)

    # max product ending at the current index
    currMax = arr[0]

    # min product ending at the current index
    currMin = arr[0]

    # Initialize overall max product
    maxProd = arr[0]

    # Iterate through the array
    for i in range(1, n):

        # Temporary variable to store the maximum product ending
        # at the current index
        temp = max(arr[i], arr[i] * currMax, arr[i] * currMin)

        # Update the minimum product ending at the current index
        currMin = min(arr[i], arr[i] * currMax, arr[i] * currMin)

        # Update the maximum product ending at the current index
        currMax = temp

        # Update the overall maximum product
        maxProd = max(maxProd, currMax)

    return maxProd


if __name__ == "__main__":
    
    arr = [-2, 6, -3, -10, 0, 2]
    
    print(maxProduct(arr))


# Approach (By Traversing in Both Directions - O(n) Time and O(1) Space)

def maxProduct(arr):

    n = len(arr)
    maxProd = float('-inf')
  
    # leftToRight to store product from left to Right
    leftToRight = 1
  
    # rightToLeft to store product from right to left
    rightToLeft = 1
  
    for i in range(n):
        if leftToRight == 0:
            leftToRight = 1
        if rightToLeft == 0:
            rightToLeft = 1
      
        # calculate product from index left to right
        leftToRight *= arr[i]
      
        # calculate product from index right to left
        j = n - i - 1
        rightToLeft *= arr[j]
        maxProd = max(leftToRight, rightToLeft, maxProd)
    
    return maxProd

if __name__=="__main__":
    
    arr = [-2, 6, -3, -10, 0, 2]