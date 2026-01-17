def threeSum(nums):
    result = []
    nums.sort()

    for i, a in enumerate(nums):
        # Skip duplicate values for a
        if i > 0 and a == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            threesum = a + nums[left] + nums[right]

            if threesum > 0:
                right -= 1
            elif threesum < 0:
                left += 1
            else:
                result.append([a, nums[left], nums[right]])

                left += 1
                right -= 1

                # Skip duplicate values for left
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicate values for right
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result


# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
