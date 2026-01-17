def maxArea(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        curr_height = min(height[left], height[right])
        area = width * curr_height

        max_water = max(max_water, area)

        # Move the pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# Example usage
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
