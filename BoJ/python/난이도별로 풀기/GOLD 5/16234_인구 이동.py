# https://www.acmicpc.net/problem/16234
from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def bfs(i, j):    
    que = deque()
    que.append([i, j])
    result = [[i, j]]

    sum = graph[i][j]
    while que:  
        x, y = que.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                        visited[nx][ny] = 1
                        result.append([nx, ny])
                        que.append([nx, ny])
                        sum += graph[nx][ny]
    
    return sum, result

count = 0
while True:
    visited = [[0] * n for _ in range(n)]
    flag = True
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                sumCountry, visitedCountry = bfs(i, j)
                if len(visitedCountry) != 1:
                    flag = False
                    for x, y in visitedCountry:
                        graph[x][y] = sumCountry // len(visitedCountry)
    if flag:
        break
    count += 1
print(count)