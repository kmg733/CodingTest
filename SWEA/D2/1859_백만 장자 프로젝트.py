# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    ary = list(map(int, input().split()))

    # 싸게 구매해서 비싸게 팔기만 하면 이득을 봄 
    profit = 0
    maxValue = -1
    for j in range(n - 1, -1, -1):
        if ary[j] > maxValue:
            maxValue = ary[j]
        else:
            profit += (maxValue - ary[j])

    print(f"#{i} {profit}")