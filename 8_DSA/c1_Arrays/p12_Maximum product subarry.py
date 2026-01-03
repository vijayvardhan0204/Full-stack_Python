def maxProduct(arr):
    n = len(arr)
    currMax = arr[0]
    currMin = arr[0]
    maxprod = arr[0]

    for i in range(1,n):

        temp = max(arr[i],arr[i] * currMax,arr[i] * currMin)
        currMin = min(arr[i],arr[i] * currMax,arr[i] * currMin)
        currMax = temp
        maxprod = max(maxprod,currMax)
    return maxprod

if __name__ =="__main__" :
    arr = [-2,6,-3,-10,0,2]
    print(maxProduct(arr))