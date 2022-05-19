# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

t = int(input())

def rotate90(arys):
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 90도 회전하는 공식
            temp[j][n - 1 - i] = arys[i][j]
    
    return temp

for case in range(1, t + 1):
    n = int(input())
    ary = []
    for _ in range(n):
        ary.append(list(map(str, input().split())))

    ary90 = rotate90(ary)
    ary180 = rotate90(ary90)
    ary270 = rotate90(ary180)

    print(f"#{case}")

    for i in range(n):
        print("".join(ary90[i]), end = " ")
        print("".join(ary180[i]), end = " ")
        print("".join(ary270[i]))