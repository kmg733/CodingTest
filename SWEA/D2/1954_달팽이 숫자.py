# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

t = int(input())

# 오른쪽, 아래, 왼쪽, 위
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for case in range(1, t + 1):
    n = int(input())
    graph = [[0] * n for _ in range(n)]

    # 리스트의 끝을 만나는 경우, 0이 아닌 경우 방향을 틈
    line = 0
    x, y = 0, 0
    graph[x][y] = 1
    while graph[x][y] < n ** 2:
        
        nx = x + dxy[line][0]
        ny = y + dxy[line][1]

        # 그래프를 벗어날 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            line += 1
            line %= 4
            continue

        # 0이 아닌 수를 만난 경우
        if graph[nx][ny] != 0:
            line += 1
            line %= 4
            continue
            
        graph[nx][ny] = graph[x][y] + 1
        x = nx
        y = ny

    print(f"#{case}")
    for g in graph:
        print(*g)