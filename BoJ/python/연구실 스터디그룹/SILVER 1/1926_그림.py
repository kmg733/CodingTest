# https://www.acmicpc.net/problem/1926
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    que = deque()
    que.append((x, y))
    paint[x][y] = 0
    area = 1

    while que:
        popX, popY = que.popleft()

        for i in range(4):
            newX = popX + dx[i]
            newY = popY + dy[i]

            if newX < 0 or newX >= n or newY < 0 or newY >= m:
                continue
            if paint[newX][newY] == 1:
                paint[newX][newY] = 0
                que.append((newX, newY))
                area += 1
    return area

n, m = map(int, input().split())

paint = []
for _ in range(n):
    paint.append(list(map(int, input().split())))

# 그림의 개수
paintCount = 0
# 넓이 == 1의 개수
area = 0
for i in range(n):
    for j in range(m):
        if paint[i][j] == 1:
            area = max(area, bfs(i, j))
            paintCount += 1

print(paintCount)
print(area)