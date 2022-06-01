# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV5LyE7KD2ADFAXc&categoryId=AV5LyE7KD2ADFAXc&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=3

t = int(input())
tankList = ["<", ">", "^", "v"]
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for case in range(1, t + 1):
    h, w = map(int, input().split())
    graph = []
    for _ in range(h):
        graph.append(list(input().strip()))
    
    for i in range(h):
        for j in range(w):
            # 탱크 위치 찾기
            if graph[i][j] in tankList:
                tank_x = i
                tank_y = j
                direct = graph[i][j]
    
    input()
    commandLine = input().strip()

    for command in commandLine:
        # 포탄 발사
        if command == 'S':
            if direct == "<":
                for i in range(tank_y, -1, -1):
                    if graph[tank_x][i] == "*":
                        graph[tank_x][i] = "."
                        break
                    elif graph[tank_x][i] == "#":
                        break
            elif direct == ">":
                for i in range(tank_y, w):
                    if graph[tank_x][i] == "*":
                        graph[tank_x][i] = "."
                        break
                    elif graph[tank_x][i] == "#":
                        break
            elif direct == "^":
                for i in range(tank_x, -1, -1):
                    if graph[i][tank_y] == "*":
                        graph[i][tank_y] = "."
                        break
                    elif graph[i][tank_y] == "#":
                        break
            elif direct == "v":
                for i in range(tank_x, h):
                    if graph[i][tank_y] == "*":
                        graph[i][tank_y] = "."
                        break
                    elif graph[i][tank_y] == "#":
                        break
        
        elif command == "U":
            direct = "^"
            # 맵 범위 내에 있는지 확인
            if tank_x - 1 >= 0:
                # 평지인지 확인
                if graph[tank_x - 1][tank_y] == ".":
                    graph[tank_x][tank_y] = "."
                    graph[tank_x - 1][tank_y] = direct
                    tank_x -= 1
                else:   
                    graph[tank_x][tank_y] = direct
            else:   
                graph[tank_x][tank_y] = direct

        elif command == "D":
            direct = "v"
            # 맵 범위 내에 있는지 확인
            if tank_x + 1 < h:
                # 평지인지 확인
                if graph[tank_x + 1][tank_y] == ".":
                    graph[tank_x][tank_y] = "."
                    graph[tank_x + 1][tank_y] = direct
                    tank_x += 1
                else:   
                    graph[tank_x][tank_y] = direct
            else:
                graph[tank_x][tank_y] = direct

        elif command == "L":
            direct = "<"
            # 맵 범위 내에 있는지 확인
            if tank_y - 1 >= 0:
                # 평지인지 확인
                if graph[tank_x][tank_y - 1] == ".":
                    graph[tank_x][tank_y] = "."
                    graph[tank_x][tank_y - 1] = direct
                    tank_y -= 1
                else:   
                    graph[tank_x][tank_y] = direct
            else:
                graph[tank_x][tank_y] = direct

        elif command == "R":
            direct = ">"
            # 맵 범위 내에 있는지 확인
            if tank_y + 1 < w:
                # 평지인지 확인
                if graph[tank_x][tank_y + 1] == ".":
                    graph[tank_x][tank_y] = "."
                    graph[tank_x][tank_y + 1] = direct
                    tank_y += 1
                else:   
                    graph[tank_x][tank_y] = direct
            else:
                graph[tank_x][tank_y] = direct

    print(f"#{case}", end = " ")
    for m in graph:
        print("".join(m))
