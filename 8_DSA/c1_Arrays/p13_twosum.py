def twosum(arr,k):
    seen = {}
    for i,num in enumerate(arr):
        complement = k - num
        if complement in seen:
            return [seen[complement],i]
        seen[num] = i

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    k = 9
    print(twosum(arr,k))