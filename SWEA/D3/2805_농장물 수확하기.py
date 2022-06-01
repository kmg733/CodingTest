# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=1

t = int(input())

for case in range(1, t + 1):
    n = int(input())
    graph =[]
    for _ in range(n):
        graph.append(list(map(int, input().strip())))

    s, e = n // 2, n // 2

    result = 0
    for i in range(n):
        for j in range(s, e + 1):
            result += graph[i][j]
        if i < n // 2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print(f"#{case} {result}")