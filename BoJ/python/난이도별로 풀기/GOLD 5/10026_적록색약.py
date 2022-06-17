# https://www.acmicpc.net/problem/10026
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(str, input().strip())))

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def bfs(i, j):
    visited[i][j] = 1
    que = deque()
    que.append([i, j])

    while que:
        x, y = que.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:
                    que.append([nx, ny])
                    visited[nx][ny] = 1

# 정상
visited = [[0] * n for _ in range(n)]
result1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            result1 += 1

# G를 R로 바꾸기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

# 적록색약
visited = [[0] * n for _ in range(n)]
result2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            result2 += 1

print(result1, result2)