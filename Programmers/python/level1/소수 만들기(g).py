import math

def solution(nums):
    count = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if isDecimal(nums[i] + nums[j] + nums[k]):
                    count += 1
    return count

def isDecimal(num):
    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:            
            return False
        
    return True

nums = [1,2,3,4]
print(solution(nums))