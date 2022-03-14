# https://www.acmicpc.net/problem/7569
from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
tomato = []
que = deque()

for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
    tomato.append(temp)

dxyz = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]

def bfs():
    while que:
        # 높이 행 열
        z, x, y = que.popleft()

        for px, py, pz in dxyz:
            newX = x + px
            newY = y + py
            newZ = z + pz
            if newX < 0 or newX >= n or newY < 0 or newY >= m or newZ < 0 or newZ >= h:
                continue
            
            if tomato[newZ][newX][newY] == 0:
                que.append((newZ, newX, newY))
                tomato[newZ][newX][newY] = tomato[z][x][y] + 1
        

for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 1:      
                # 시작지점이 여러개일 경우 미리 queue에 추가시켜 놓아야 문제가 발생하지 않음          
                que.append((z, x, y))

bfs()

count = -1
for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 0:
                print(-1)
                sys.exit()
            count = max(count, tomato[z][x][y])
for i in tomato:
    for j in i:
        for k in j:
            print(k, end = ' ')
        print()
    print()
print(count - 1)

# DFS/BFS