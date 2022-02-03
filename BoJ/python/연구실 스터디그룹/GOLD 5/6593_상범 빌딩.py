# https://www.acmicpc.net/problem/6593
from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j, k):
    que = deque()
    que.append((i, j, k))
    times[i][j][k] = 0

    while que:
        z, x, y = que.popleft()

        for i in range(6):
            newZ = z + dz[i] 
            newX = x + dx[i]
            newY = y + dy[i]

            if 0 <= newZ < l and 0 <= newX < r and 0 <= newY < c:
                if building[newZ][newX][newY] == "E":
                    print(f"Escaped in {times[z][x][y] + 1} minute(s).")
                    return
                
                if times[newZ][newX][newY] == -1 and building[newZ][newX][newY] == ".":
                    times[newZ][newX][newY] = times[z][x][y] + 1
                    que.append((newZ, newX, newY))

    print("Trapped!")

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]


while True:
    l, r, c = map(int, input().split())

    if l == 0 and r == 0 and c == 0:
        break

    # 3차원 리스트
    building = [[[] * c for i in range(r)] for j in range(l)]
    times = [[[-1] * c for i in range(r)] for j in range(l)]

    # 빌딩 구조 입력받기
    for i in range(l):
        building[i] = [list(input().strip()) for i in range(r)]
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == "S":
                    bfs(i, j, k)


# 참고: https://it-garden.tistory.com/189