# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QGNvKAtEDFAUq&categoryId=AV5QGNvKAtEDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=1

t = int(input())
for i in range(1, t + 1):
    a, b = map(int, input().split())
    print(f"#{i} {a // b} {a % b}")