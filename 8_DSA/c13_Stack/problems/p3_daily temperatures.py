def dailyTemperatures(arr):
    stack = []
    ans =[0] * len(arr)
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            prev = stack.pop()
            ans[prev] = i - prev
        stack.append(i)
    return ans

if __name__ == "__main__":
    arr = [73,74,75,71,69,72,76,73]
    print(dailyTemperatures(arr))