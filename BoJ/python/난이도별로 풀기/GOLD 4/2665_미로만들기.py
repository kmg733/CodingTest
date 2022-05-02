# https://www.acmicpc.net/problem/2665
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))

# 이동 거리
dist = [[-1] * n for i in range(n)]
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def bfs():
    que = deque()
    # 시작 지점
    que.append([0, 0])
    dist[0][0] = 0

    while que:
        x, y = que.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n:
                # 방문한 적이 없다면
                if dist[nx][ny] == -1:
                    # 탐색하는 곳이 검은 방인 경우
                    if graph[nx][ny] == 0:
                        dist[nx][ny] = dist[x][y] + 1
                        que.append([nx, ny])

                    # 탐색하는 곳이 흰 방인 경우
                    else:
                        dist[nx][ny] = dist[x][y]
                        # 흰방들 우선 탐색을 위해 큐의 왼쪽에 추가
                        que.appendleft([nx, ny])

bfs()
print(dist[n - 1][n - 1])