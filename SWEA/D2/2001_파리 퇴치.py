# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

t = int(input())
for i in range(1, t + 1):
    n, m = map(int, input().split())

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    result = 0
    for j in range(n - m + 1):
        for k in range(n - m + 1):
            temp = 0
            for j2 in range(j, j + m):
                for k2 in range(k, k + m):
                    temp += graph[j2][k2]
            
            result = max(result, temp)
    
    print(f"#{i} {result}")