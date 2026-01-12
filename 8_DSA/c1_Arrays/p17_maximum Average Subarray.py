def findMaxAverage(nums, k):
        # Step 1: Sum of first k elements
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Step 2: Slide the window
        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        # Step 3: Return maximum average
        return max_sum / k
if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50 , 3]
    k = 4
    print(findMaxAverage(nums, k))

