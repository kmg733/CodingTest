# https://www.acmicpc.net/problem/7576
from collections import deque
import sys
input = sys.stdin.readline

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
# 열, 행
m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs():
    while que:
        x, y = que.popleft()
        # 상, 하, 좌, 우 4방향 탐색
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            # 그래프 내부라면
            if 0 <= nx < n and 0 <= ny < m:
                # 익지 않은 토마토(0)이라면
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    que.append([nx, ny])

que = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            # 큐에 토마토가 있는 위치를 미리 추가해둬야 병렬적으로 처리할 수 있음
            que.append([i, j])

bfs()

maxValue = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            sys.exit()
        maxValue = max(maxValue, graph[i][j])

if maxValue == 1:
    print(0)
else:
    print(maxValue - 1)