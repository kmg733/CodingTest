import sys

n = int(sys.stdin.readline())                 # 숫자 개수
nums = list(sys.stdin.readline().strip())     # 숫자들

sum = 0
for i in nums:
    sum += int(i)

print(sum)