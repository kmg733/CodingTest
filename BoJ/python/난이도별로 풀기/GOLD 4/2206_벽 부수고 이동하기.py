# https://www.acmicpc.net/problem/2206
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs():
    que = deque()
    que.append([0, 0, 0])
    visited[0][0][0] = 1

    while que:
        # 행, 렬, 벽을 부순여부(0 = 안부숨, 1 = 부숨)
        x, y, c = que.popleft()

        # 목적지에 도착했을 경우
        if x == n - 1 and y == m - 1:
            return visited[x][y][c]

        # 상, 하, 좌, 우 탐색
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m:
                # 탐색하는 곳이 벽이 아니면서, 방문한적 없는 경우
                if graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    que.append([nx, ny, c])

                # 탐색하는 곳이 벽이면서, 아직 벽을 부순적이 없는 경우
                if graph[nx][ny] == 1 and c == 0:
                    visited[nx][ny][c + 1] = visited[x][y][c] + 1
                    que.append([nx, ny, c + 1])
    return -1

print(bfs())
print("벽을 부수지 않고 이동한 경로")
for i in range(len(visited)):
    for j in range(len(visited[0])):
        for k in range(len(visited[0][0])):
            if k == 0:
                print(visited[i][j][k], end = ' ')
    
    print()
print()

print("벽을 부수고 이동한 경로")
for i in range(len(visited)):
    for j in range(len(visited[0])):
        for k in range(len(visited[0][0])):
            if k == 1:
                print(visited[i][j][k], end = ' ')
    
    print()
print()

# 테스트 케이스
# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000