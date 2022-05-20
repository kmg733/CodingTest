# https://www.acmicpc.net/problem/1920
import sys
input = sys.stdin.readline

n = int(input())
origin = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

origin.sort()

for c in check:
    left = 0
    right = n - 1
    answer = False

    while True:
        if left > right:
            break
        
        mid = (left + right) // 2
        if origin[mid] == c:
            answer = True
            break

        if origin[mid] < c:
            left = mid + 1
        elif origin[mid] > c:
            right = mid - 1

    if answer:
        print(1)
    else:
        print(0)