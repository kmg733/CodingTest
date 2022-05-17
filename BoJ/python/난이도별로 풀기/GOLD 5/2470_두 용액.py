# https://www.acmicpc.net/problem/2470
import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l.sort()

left = 0
right = n - 1
result = sys.maxsize
answer = []

while True:
    if left >= right:
        break
    sum = l[left] + l[right]

    if result > abs(sum):
        result = abs(sum)
        answer = [l[left], l[right]]

    if result == 0:
        break

    if sum > 0:
        right -= 1
    else:
        left += 1

print(*answer)