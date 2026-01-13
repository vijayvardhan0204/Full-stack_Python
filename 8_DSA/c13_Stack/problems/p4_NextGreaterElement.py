def nextGreaterElement(nums1,nums2):
    stack =[]
    look ={}
    for num in nums2:
        while stack and num > stack[-1]:
            look[stack.pop()] = num 
        stack.append(num)

    while stack:
        look[stack.pop()] = -1
    
    return [look[x] for x in nums1]

if __name__ == "__main__":
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(nextGreaterElement(nums1,nums2))
