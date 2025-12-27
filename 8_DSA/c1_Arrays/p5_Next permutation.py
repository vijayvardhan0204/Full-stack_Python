# Next permutation

# Input: arr[] = [2, 4, 1, 7, 5, 0]
# Output: [2, 4, 5, 0, 1, 7]
# Explanation: The next lexicographically greater arrangement of the elements in the array arr[] is [2, 4, 5, 0, 1, 7].

# Input: arr[] = [3, 2, 1]
# Output: [1, 2, 3]
# Explanation: This is the last permutation, so we return the lowest possible permutation (ascending order).

# Input: arr[] = [1, 3, 5, 4, 2]
# Output: [1, 4, 2, 3, 5]
# Explanation: The next lexicographically greater arrangement of the elements in the array arr[] is [1, 4, 2, 3, 5].

def nextPermutation(arr):
    n = len(arr)
    
    # Find the pivot index
    pivot = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break
    
    # If pivot point does not exist, 
    # reverse the whole array
    if pivot == -1:
        arr.reverse()
        return

    # Find the element from the right 
    # that is greater than pivot
    for i in range(n - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    # Reverse the elements from pivot + 1 to the end in place
    left, right = pivot + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

if __name__=="__main__":
    arr = [ 2, 4, 1, 7, 5, 0 ]
    nextPermutation(arr)
    print(arr)
    # print(" ".join(map(str, arr)))