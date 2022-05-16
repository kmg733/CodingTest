# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5P0-h6Ak4DFAUq&categoryId=AV5P0-h6Ak4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

t = int(input())
for z in range(1, t + 1):
    n = int(input())
    p = [[0] * n for _ in range(n)]

    for i in range(len(p)):
        for j in range(len(p[0])):
            if i == 0:
                if j == 0:            
                    p[i][j] = 1
            else:
                p[i][j] = p[i - 1][j - 1] + p[i - 1][j]

    print(f"#{z}")
    for a in p:
        for b in a:
            if b != 0:
                print(b, end = ' ')
        print()