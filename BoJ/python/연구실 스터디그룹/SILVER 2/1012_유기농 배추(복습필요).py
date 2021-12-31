# https://www.acmicpc.net/problem/1012
import sys
from collections import deque

input = sys.stdin.readline

# 너비우선탐색
def bfs(f, x, y):
    que = deque()
    que.append([x, y])
    f[x][y] = 0
    
    # 큐가 비어있지 않다면 반복실행
    while que:
        x2, y2 = que.popleft()
        for i in range(4):
            x2 = x + dxy[i][0]
            y2 = y + dxy[i][1]
            if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m:
                continue
            if f[x2][y2] == 1:
                f[x2][y2] = 0
                que.append([x2, y2])
    return

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

t = int(input())


# 배추밭 생성
for _ in range(t):
    count = 0
    n, m, k = map(int, input().split())
    field = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1
    
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(field, i, j)
                count += 1
    print(count)