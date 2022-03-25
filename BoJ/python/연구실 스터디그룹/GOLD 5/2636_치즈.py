# https://www.acmicpc.net/problem/2636
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph= []
for i in range(n):
    graph.append(list(map(int, input().split())))

dxy = [[1, 0], [-1, 0], [0, -1], [0, 1]]
def bfs(i, j):
    que = deque()
    que.append([i, j])
    visited[i][j] = 1
    count = 0
    
    while que:
        x, y = que.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m:
                # 0인 공간
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:                    
                    visited[nx][ny] = 1
                    que.append([nx, ny])
                # 1인 공간
                elif graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    graph[nx][ny] = 0
                    count += 1

    return count

times = 0
while True:
    visited = [[0] * m for _ in range(n)]  
    # 치즈 안쪽에 0 공간은 포함하지 않기 위해 시작지점인 [0, 0]에서부터 bfs 탐색을 시작
    result = bfs(0, 0)

    if result == 0:
        break
    cheese = result
    times += 1

print(times)
print(cheese)