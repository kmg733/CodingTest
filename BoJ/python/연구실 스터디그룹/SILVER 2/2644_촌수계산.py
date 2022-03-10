# https://www.acmicpc.net/problem/2644
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
t1, t2 = map(int, input().split())
m = int(input())
graph = [[0] * (n + 1) for i in range(n + 1)]
visited = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 깊이 우선 탐색
def dfs(start, visited, d = 0):
    visited.append(start)
    for i in range(1, n + 1):
        if graph[start][i] == 1 and i not in visited:
            d += 1
            if i == t2:
                print(d)
                sys.exit()
            dfs(i, visited, d)
            d -= 1
    return -1

ds = [0] * (n + 1)
# 너비 우선 탐색
def bfs(start, visited=[]):
    que = deque() 
    que.append(start)
    visited.append(start)

    while que:
        t = que.popleft()
        for i in range(1, n + 1):
            if graph[t][i] == 1 and i not in visited:
                ds[i] = ds[t] + 1
                que.append(i)
                visited.append(i)

# print(dfs(t1, visited))
bfs(t1)
print(ds[t2] if ds[t2] != 0 else -1)