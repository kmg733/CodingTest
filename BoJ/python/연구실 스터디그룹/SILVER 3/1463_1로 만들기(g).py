# https://www.acmicpc.net/problem/1463
import sys
input = sys.stdin.readline

n = int(input())
d = [0] * 1000001

for i in range(2, n + 1):
    # 1을 빼준 경우 
    d[i] = d[i - 1] + 1

    # 2으로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

print(d[n])

# DP