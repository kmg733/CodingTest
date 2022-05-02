# https://www.acmicpc.net/problem/4179
from collections import deque
import sys
input = sys.stdin.readline

# 미로의 행, 열 값
r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input().strip()))
visited = [[0] * c for _ in range(r)]
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs():
    while que:
        x, y = que.popleft()

        # 지훈이가 탈출에 성공했을 때
        if graph[x][y] != 'F':
            if x == 0 or x == r - 1 or y == 0 or y == c -1:
                return graph[x][y]

        # 미로탐색
        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < r and 0 <= ny < c:
                # 지훈이의 이동
                if visited[nx][ny] == 0 and graph[nx][ny] == '.' and graph[x][y] != 'F':
                    # 지훈이가 이동한 경로는 불도 이동할 수 있어야 하므로 방문처리를 하지 않음
                    graph[nx][ny] = graph[x][y] + 1
                    que.append([nx, ny])

                # 불의 이동
                if visited[nx][ny] == 0 and graph[nx][ny] != '#' and graph[x][y] == 'F':
                    visited[nx][ny] = 1
                    graph[nx][ny] = 'F'
                    que.append([nx, ny])

    # while문의 return에 안걸리고 빠져 나오면 탈출이 불가능 한것을 의미함
    return "IMPOSSIBLE"

que = deque()
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            que.append([i, j])
            graph[i][j] = 1
        if graph[i][j] == 'F':
            que.append([i, j])
            visited[i][j] = 1        

print(bfs())