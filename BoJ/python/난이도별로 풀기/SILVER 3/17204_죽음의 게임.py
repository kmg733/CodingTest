# https://www.acmicpc.net/problem/17204
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

t = []
for i in range(n):
    t.append([int(input()), False])

# 보성이가 걸리지 않을 경우
# - 보성이를 빼고 무한 루프에 걸리는 경우
count = 0
target = 0
while True:
    if t[target][1] == False:
        t[target][1] = True
        count += 1
        if t[target][0] == k:
            print(count)
            break
        target = t[target][0]
    else:
        print(-1)
        break
    