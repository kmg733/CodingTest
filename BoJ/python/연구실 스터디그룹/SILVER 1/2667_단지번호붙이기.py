# https://www.acmicpc.net/problem/2667
from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph):
    que = deque()
    que.append((x, y))
    graph[x][y] = value
    count[value] = 1

    while que:
        popX, popY = que.popleft()
        
        for i in range(4):
            newX = popX + dx[i]
            newY = popY + dy[i]

            if newX < 0 or newX >= n or newY < 0 or newY >= n:
                continue
            if graph[newX][newY] == value or graph[newX][newY] == 0:                
                continue
            
            graph[newX][newY] = value
            count[value] += 1
            que.append((newX, newY))
    return

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))

count = {}
value = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j, graph)
            value += 1

ary = sorted(list(count.values()))
print(len(ary))
for i in ary:
    print(i)