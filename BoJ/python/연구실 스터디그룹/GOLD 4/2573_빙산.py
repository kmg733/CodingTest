# https://www.acmicpc.net/problem/2573
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maxH = 0
graph = []
for _ in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    maxH = max(maxH, max(temp))

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def bfs(i, j):
    que = deque()
    que.append((i, j))
    visited[i][j] = 1

    while que:
        x, y = que.popleft()
        for px, py in dxy:
            newX = px + x
            newY = py + y
            if 0 <= newX < n and 0 <= newY < m:
                if graph[newX][newY] != 0 and visited[newX][newY] == 0: 
                    visited[newX][newY] = 1
                    que.append((newX, newY))
                
                if graph[newX][newY] == 0 and visited[newX][newY] == 0:
                    if graph[x][y] > 0:
                        graph[x][y] -= 1

year = 0
while True:
    visited = [[0] * m for _ in range(n)]

    # 빙산의 갯수
    counts = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == 0:
                bfs(i, j)
                counts += 1

    if counts == 0:
        print(0)
        break
    elif counts >= 2:
        print(year)
        break

    year += 1

# DFS/BFS