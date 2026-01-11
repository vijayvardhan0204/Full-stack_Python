
def twoSum(numbers,target):
        left = 0
        right = len(numbers) - 1
        while left < right :
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1,right+1]
            elif target > s:
                left += 1
            else:
                right -= 1   

if __name__ == "__main__":
     numbers = [2,7,11,15]
     target = 9
     print(twoSum(numbers,target))