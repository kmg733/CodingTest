# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&problemLevel=3&contestProbId=AX8BAN1qTwoDFARO&categoryId=AX8BAN1qTwoDFARO&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=1&problemLevel=1%2C2%2C3&&&&&&&&&
from collections import deque

t = int(input())

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(a ,b):
    visited[a][b] = 1
    que = deque()
    que.append([a, b])

    # 가운데 값이 비어있는지 확인용
    countSharp = 1
    # 정사각형인지 확인하기 위한 좌표 입력
    minX, minY, maxX, maxY = a, b, a, b
    while que:
        x, y = que.popleft()

        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and square[nx][ny] == '#':
                    visited[nx][ny] = 1
                    countSharp += 1
                    minX = min(minX, nx)
                    minY = min(minY, ny)
                    maxX = max(maxX, nx)
                    maxY = max(maxY, ny)

                    que.append([nx, ny])

    # 사각형의 높이
    sx = maxX - minX + 1
    # 사각형의 밑변
    sy = maxY - minY + 1
    
    result = "-1"
    if sx == sy:
        if sx ** 2 == countSharp:
            result = "yes"
        else:
            result = "no"
    else:
            result = "no"
    
    return result

for case in range(1, t + 1):
    n = int(input())

    square = []
    for _ in range(n):
        square.append(list(input().strip()))
    
    flag = False
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if square[i][j] == '#' and visited[i][j] == 0:                
                if flag:
                    result = "no"
                    break
                flag = True
                result = bfs(i, j)
    
    print(f"#{case} {result}")