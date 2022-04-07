# https://www.acmicpc.net/problem/2606
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
r = int(input())

visited = []
graph = [[0] * (n + 1) for i in range(n + 1)]
# 간선 연결
for i in range(r):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def bfs(start, count = 0):
    que = deque()
    que.append(start)
    visited.append(start)

    while que:
        s = que.popleft()
        for i in range(1, n + 1):
            if graph[s][i] == 1 and i not in visited:
                que.append(i)
                visited.append(i)
                count += 1
    
    return count

def dfs(start):
    visited.append(start)

    for i in range(1, n + 1):
        if graph[start][i] == 1 and i not in visited:
            dfs(i)

    return len(visited) - 1

# print(bfs(1))
print(dfs(1))

# DFS/BFS