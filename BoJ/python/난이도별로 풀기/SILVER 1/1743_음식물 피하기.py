# https://www.acmicpc.net/problem/1743
from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

# bfs 방문여부 체크용 리스트
visited = [[0] * m for _ in range(n)]

# 쓰레기 위치를 담을 리스트
graph = [[0] * m for _ in range(n)]

# 쓰레기 위치 입력받기
for i in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1

# 상, 하, 좌, 우 4방향 체크를 위한 리스트
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def bfs(i, j):
    que = deque()
    que.append((i, j))
    visited[i][j] = 1
    count = 1

    while que:
        x, y = que.popleft()

        # 상, 하, 좌, 우 4방향
        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y

            # 리스트를 벗어나지 않으면
            if 0 <= nx < n and 0 <= ny < m:
                # 해당 좌표에 쓰레기가 존재하고 방문하지 않았다면
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    que.append((nx, ny))
                    count += 1
    return count            

# 가장 큰 쓰레기 체크하기 위한 변수
maxGarbage = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            maxGarbage = max(maxGarbage, bfs(i, j))

print(maxGarbage)