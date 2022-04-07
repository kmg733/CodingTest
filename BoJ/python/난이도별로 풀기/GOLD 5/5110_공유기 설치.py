# https://www.acmicpc.net/problem/2110
import sys

input = sys.stdin.readline

n, c = map(int, input().split())

xy = [int(input()) for _ in range(n)]
xy.sort()

def binary(start, end):
    print(f"start = {start}, end = {end}")
    if start > end:
        return end
    # 공유기 사이의 거리
    mid = (start + end) // 2
    # 전 집의 좌표
    old = xy[0]
    # 공유기를 설치한 집의 개수
    count = 1
    
    for i in range(1, len(xy)):
        # 전집으로부터 mid이상 떨어졌을 때
        if xy[i] >= old + mid:
            count += 1
            old = xy[i]

    if count >= c:
        return binary(mid + 1, end)
    else:
        return binary(start, mid - 1)

print(binary(1, xy[-1] - xy[0]))

# 이진 탐색