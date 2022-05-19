# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PuPq6AaQDFAUq&categoryId=AV5PuPq6AaQDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

t = int(input())
for case in range(1, t + 1):
    n, k = map(int, input().split())

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    temp = 0
    answer = 0

    # 가로 탐색
    for i in range(n):
        for j in range(n):
            # 검은색 부분
            if graph[i][j] == 0:
                if temp == k:
                    answer += 1
                temp = 0
            # 흰색 부분
            else:
                temp += 1

        if temp == k:
            answer += 1
        temp = 0

    # 세로 탐색
    for i in range(n):
        for j in range(n):
            # 검은색 부분
            if graph[j][i] == 0:
                if temp == k:
                    answer += 1
                temp = 0
            # 흰색 부분
            else:
                temp += 1
 
        if temp == k:
            answer += 1
        temp = 0

    print(f"#{case} {answer}")