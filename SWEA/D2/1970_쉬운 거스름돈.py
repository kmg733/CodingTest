# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PsIl6AXIDFAUq&categoryId=AV5PsIl6AXIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

t = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for case in range(1, t + 1):
    n = int(input())

    print(f"#{case}")
    for m in money:
        print(n // m, end = " ")
        n = n % m
    print()