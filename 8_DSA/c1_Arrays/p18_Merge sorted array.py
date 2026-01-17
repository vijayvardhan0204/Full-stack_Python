def merge(nums1, m, nums2, n):
    # Pointer for last valid element in nums1
    i = m - 1
    
    # Pointer for last element in nums2
    j = n - 1
    
    # Pointer for last position in nums1
    k = m + n - 1

    # Merge nums1 and nums2 from the back
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]   # place larger element
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1   # move write pointer left

    # Copy remaining elements of nums2 (if any)
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


# Example usage
nums1 = [4, 5, 6, 0, 0, 0]
nums2 = [1, 2, 3]
m = 3
n = 3

merge(nums1, m, nums2, n)
print(nums1)
