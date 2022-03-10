# https://www.acmicpc.net/problem/2468
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
# 입력받은 값 중 가장 큰 값
maxH = 0
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    maxH = max(maxH, max(temp))

dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(i, j, h):
    que = deque()
    que.append([i, j])
    visited[i][j] = 1

    while que:
        x, y = que.popleft()
        for px, py in dxy:
            newX = px + x
            newY = py + y

            if 0 <= newX < n and 0 <= newY < n and visited[newX][newY] == 0:
                if graph[newX][newY] > h:
                    visited[newX][newY] = 1
                    que.append([newX, newY])
                
maxArea = 0
# 물에 잠기는 높이를 1씩 증가
for rainH in range(maxH):
    visited = [[0] * n for _ in range(n)]
    countArea = 0

    for i in range(n):
        for j in range(n):
            # 물에 잠기는 높이보다 높은 지역인 경우 bfs탐색
            if graph[i][j] > rainH and visited[i][j] == 0:
                bfs(i, j, rainH)
                countArea += 1

    maxArea = max(maxArea, countArea)

print(maxArea)
# DFS/BFS