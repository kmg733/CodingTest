# https://www.acmicpc.net/problem/1654
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
l = []
for i in range(k):
    l.append(int(input()))

start, end = 1, max(l)

while True:
    if start > end:
        break

    mid = (start + end) // 2
    lan = 0
    for i in l:
        # 만들 수 있는 랜선의 갯수 더하기
        lan += (i // mid)

    if lan >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)