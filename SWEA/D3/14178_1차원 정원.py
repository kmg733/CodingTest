# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX_N3oSqcyUDFARi&categoryId=AX_N3oSqcyUDFARi&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=1
import math
t = int(input())

for case in range(1, t + 1):
    n, d = map(int, input().split())

    range = d * 2 + 1
    result = math.ceil(n / range)
    print(f"#{case} {result}")
    