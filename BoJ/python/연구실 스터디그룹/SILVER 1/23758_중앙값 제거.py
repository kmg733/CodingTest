# https://www.acmicpc.net/problem/23758
import math
import sys
input = sys.stdin.readline

n = int(input())
amel = list(map(int, input().split()))
amel.sort()

result = 0
for i in range((n + 1) // 2):
    result += int(math.log2(amel[i]))

print(result + 1)