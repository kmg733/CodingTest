# https://www.acmicpc.net/problem/2178
from collections import deque
import sys
input = sys.stdin.readline

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
n, m = map(int, input().split())

maze = []
for _ in range(n):
    maze.append(list(map(int,input().strip())))

# 너비 우선 탐색
def bfs(i, j):
    que = deque()
    que.append((i, j))

    while que:
        x, y = que.popleft()
        for i in range(4):
            x2 = x + dxy[i][0]
            y2 = y + dxy[i][1]
        
            if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m:
                continue

            if maze[x2][y2] == 0:
                continue

            if maze[x2][y2] == 1:
                que.append((x2, y2))
                maze[x2][y2] = maze[x][y] + 1
    
    return maze[n-1][m-1]

print(maze)