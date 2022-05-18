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

# 이분 탐색
while True:
    if left >= right:
        break

    # 두 용액의 합
    sum = l[left] + l[right]

    # 기존 결과값 보다 두 용액의 합이 작다면
    if result > abs(sum):
        result = abs(sum)
        answer = [l[left], l[right]]

    # 결과값이 0이라면 탐색 바로 종료
    if result == 0:
        break

    if sum > 0:
        right -= 1
    else:
        left += 1

print(*answer)