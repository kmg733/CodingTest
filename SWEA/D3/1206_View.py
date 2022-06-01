# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=1

t = 10

for case in range(1, t + 1):
    n = int(input())
    building = list(map(int, input().split()))

    result = 0
    for i in range(2, n - 2):
        if building[i] > building[i - 2] and building[i] > building[i - 1] and building[i] > building[i + 1] and building[i] > building[i + 2]:
            result += building[i] - max(building[i - 2], building[i - 1], building[i + 1], building[i + 2])
    
    print(f"#{case} {result}")