def buildPrefix(nums):
    prefix = [0]
    for i in nums:
        prefix.append(prefix[-1] + i)
    return prefix

def sumRange(prefix, left, right):
    return prefix[right + 1] - prefix[left]


# Example usage
nums = [2, 4, 6, 8]
prefix = buildPrefix(nums)

print(sumRange(prefix, 1, 3))   # Output: 18