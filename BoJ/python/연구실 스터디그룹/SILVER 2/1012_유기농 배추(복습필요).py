# https://www.acmicpc.net/problem/1012
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# 너비우선 탐색
def bfs(i, j, field):
    que = deque()
    que.append((i, j))
    field[i][j] = 0

    while que:
        y, x = que.popleft()        

        for i in range(4):
            my = y + dxy[i][0]
            mx = x + dxy[i][1]
            if my < 0 or my >= n or mx < 0 or mx >= m:
                continue
            if field[my][mx] == 1:
                field[my][mx] = 0
                que.append((my, mx))

    return

# 배추밭 만들기
for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    cnt = 0

    # 배추를 심은곳 입력받기
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(i, j, field)
                cnt += 1
    
    print(cnt)
