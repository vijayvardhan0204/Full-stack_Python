# Approach 1(Using Hash Map or Dictionary - O(n) Time and O(n) Space)

def findMajority(arr):
    n = len(arr)
    freq = {}
    res = []

    # find frequency of each number
    for ele in arr:
        freq[ele] = freq.get(ele, 0) + 1

    # Iterate over each key-value 
    # pair in the hash map
    for ele, cnt in freq.items():
        
        # Add the element to the result, if its frequency
        # is greater than floor(n/3)
        if cnt > n // 3:
            res.append(ele)

    if len(res) == 2 and res[0] > res[1]:
        res[0], res[1] = res[1], res[0]
    return res

if __name__ == "__main__":
    arr = [2, 2, 3, 1, 3, 2, 1, 1]
    res = findMajority(arr)
    for ele in res:
        print(ele, end=" ")


# Approach 2(Boyer-Moore’s Voting Algorithm - O(n) Time and O(1) Space)

def findMajority(arr):
    n = len(arr)

    # Initialize two candidates and their counts
    ele1, ele2 = -1, -1
    cnt1, cnt2 = 0, 0

    for ele in arr:
        # Increment count for candidate 1
        if ele1 == ele:
            cnt1 += 1
        # Increment count for candidate 2
        elif ele2 == ele:
            cnt2 += 1
        # New candidate 1 if count is zero
        elif cnt1 == 0:
            ele1 = ele
            cnt1 += 1
        # New candidate 2 if count is zero
        elif cnt2 == 0:
            ele2 = ele
            cnt2 += 1
        # Decrease counts if neither candidate
        else:
            cnt1 -= 1
            cnt2 -= 1

    res = []
    cnt1, cnt2 = 0, 0

    # Count the occurrences of candidates
    for ele in arr:
        if ele1 == ele:
            cnt1 += 1
        if ele2 == ele:
            cnt2 += 1

    # Add to result if they are majority elements
    if cnt1 > n / 3:
        res.append(ele1)
    if cnt2 > n / 3 and ele1 != ele2:
        res.append(ele2)

    if len(res) == 2 and res[0] > res[1]:
        res[0], res[1] = res[1], res[0]

    return res

if __name__ == "__main__":
    arr = [2, 2, 3, 1, 3, 2, 1, 1]
    res = findMajority(arr)
    for ele in res:
        print(ele, end = " ")